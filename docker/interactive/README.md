# Dockerize an Interactive Python Program

A Dockerfile example for running an interactive Python program.

## Setup

1. Build the docker image.

   ```bash
   $ docker build -t hello-chat .
   ```

1. Run the image.

   ```bash
   $ docker run -it --rm hello-chat
   ```

1. Debug the container.

   ```bash
   $ docker run -it --rm --entrypoint /bin/bash hello-chat
   ```
