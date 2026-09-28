#!/bin/sh
cd "$(dirname "$0")" && python3 closed_side.py && python3 y1b_reconcile.py
