#!/bin/bash
# It will take approx 80 minutes to run the script.
set -e
sudo apt-get update
echo Installing git
sudo apt-get install git
echo Installing python3-pip
sudo apt-get -y install python3-pip
cd "${KOKORO_ARTIFACTS_DIR}/github/gcsfuse"
python3 perfmetrics/scripts/presubmit_test/pr_perf_test/test.py