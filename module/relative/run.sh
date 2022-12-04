#!/usr/bin/env bash

echo 'running relative as a module'

# Where the script is located.
script_dir="$(dirname -- "$( readlink -f -- "${0}")")"
# The directory from where the script is called.
call_dir="${PWD}"

if [ "${script_dir}" != "${call_dir}" ]; then
  echo 'Run this script in the directory where the script is located.'
  exit 1
fi

cd  .. || exit 1
python3 -m relative.main
