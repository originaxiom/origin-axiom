#!/bin/sh
# xB024 -- reproduce the computational cell.  The reading cells are quotations, verifiable
# against the sources named in FINDINGS.md.
cd "$(dirname "$0")" && python3 shape_field.py
