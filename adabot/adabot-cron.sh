#!/bin/bash

# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

cd /home/tannewt/adabot

source .env/bin/activate
source env.sh

python -m adabot.circuitpython_bundle
