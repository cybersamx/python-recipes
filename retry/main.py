#!/usr/bin/env python

# See https://github.com/jd/tenacity

import logging
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from tenacity import (
    retry,
    retry_if_result,
    retry_if_exception_type,
    before_log,
    before_sleep_log,
    after_log,
    wait_exponential,
    stop_after_attempt,
    RetryError,
)


class TimeoutException(Exception):
    pass


# Represent a job.
@dataclass
class Job:
    id: str
    start_time: datetime


# Represent the status of a job.
# Status can be: QUEUED, PROCESSING, DONE, ERROR.
@dataclass
class JobStatus:
    status: str


def is_job_processing(job_status: JobStatus) -> bool:
    return job_status.status == 'QUEUED' or job_status.status == 'PROCESSING'


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def log_config() -> dict:
    logger = logging.getLogger('main')

    return {
        'before': before_log(logger, logging.DEBUG),
        'before_sleep': before_sleep_log(logger, logging.DEBUG),
        'after': after_log(logger, logging.DEBUG),
    }


# Initialize a job and place it in a queue.
def create_job() -> Job:
    return Job(
        id=str(time.time()),
        start_time=datetime.now(),
    )


@retry(
    retry=retry_if_exception_type(TimeoutException) | retry_if_result(is_job_processing),
    wait=wait_exponential(multiplier=1, min=2, max=5),
    stop=stop_after_attempt(3),
    **log_config(),
)
def query_job_timeout() -> JobStatus:
    """
    The api will take a long time to respond. This is a test for timeout.
    """

    # Let's suppose the job api takes a long time to respond.
    # It's the responsibility of the caller to time out the call.
    # We simulate a timeout by raising an exception after some seconds.
    time.sleep(5)

    # We have code to handle timeout and raise an exception.
    raise TimeoutException()


def get_job_status(job: Job, status: str, process_sec=2, done_sec=5) -> JobStatus:
    """
    Simulate how long it takes a job to transition from queued to processing to done|error.
    """
    started = job.start_time.timestamp()
    now = time.time()
    diff = now - started

    if diff <= process_sec:
        return JobStatus(status='QUEUED')
    elif process_sec < diff <= done_sec:
        return JobStatus(status='PROCESSING')
    elif diff > done_sec:
        return JobStatus(status=status)


# Retry if:
# 1. We get a timeout exception ie. too long for the api to respond.
# 2. The job is still queued or processing.
@retry(
    retry=retry_if_exception_type(TimeoutException) | retry_if_result(is_job_processing),
    # Wait 2^x*1 (where x is attempt) seconds before retrying with min of 3 sec and max of 5 sec.
    # Retries times at:
    # Attempt 0: 2^0*1 = 1 becomes 6 (as 6 is min), retry at 6 sec
    # Attempt 1: 2^1*1 = 2 becomes 6 (as 6 is min), retry at 12 sec
    # Attempt 2: 2^2*1 = 4 becomes 6 (as 6 is min), retry at 18 sec
    # Attempt 3: 2^3*1 = 8, retry at 26 sec
    wait=wait_exponential(multiplier=1, min=6, max=20),
    stop=stop_after_attempt(6),
    **log_config(),
)
def query_job(job: Job) -> JobStatus:
    """
    The api will return the appropriate state based of the time after the job
    was created. This is to help test the polling for the job until it completes.
    """
    return get_job_status(job, 'DONE', process_sec=8, done_sec=23)


@retry(
    retry=retry_if_exception_type(TimeoutException) | retry_if_result(is_job_processing),
    wait=wait_exponential(multiplier=1, min=2, max=5),
    stop=stop_after_attempt(3),
    **log_config(),
)
def query_job_error(job: Job) -> JobStatus:
    """
    The api will return an ERROR status. This is to help test if we can stop the
    retry given the job failed.
    """
    return get_job_status(job, 'ERROR')


def print_separator(mesg: str):
    print(f'\n{mesg}\n')


def main():
    print_separator('Timeout - api takes too long to respond at each retry')

    try:
        query_job_timeout()
    except RetryError as err:
        print(f'Expected exception: retry timeout after {err.last_attempt.attempt_number} attempts')

    print_separator('Happy path - job is done eventually')

    try:
        job = create_job()
        job_status = query_job(job)
        print(f'{job_status.status=}')
    except RetryError as err:
        print(f'Unexpected exception: {err}')

    print_separator('Error path - job is done but there is an error')

    try:
        job = create_job()
        job_status = query_job_error(job)
        print(f'{job_status.status=}')
    except RetryError as err:
        print(f'Unexpected exception: this should not happen {err}')
    finally:
        # Clean up goes here.
        pass


if __name__ == '__main__':
    main()
