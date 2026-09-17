#!/bin/sh
# xB023 -- reproduce every cell from scratch.
cd "$(dirname "$0")" && python3 selection.py && python3 kawauchi_read.py
