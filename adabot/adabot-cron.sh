#!/bin/bash

cd /home/tannewt/adabot

source .env/bin/activate
source env.sh

python -m adabot.circuitpython_bundle

