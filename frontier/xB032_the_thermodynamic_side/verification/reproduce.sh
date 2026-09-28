#!/bin/sh
cd "$(dirname "$0")" && python3 thermo.py && python3 thermo_t3.py
