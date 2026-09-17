#!/bin/sh
# xB024 -- reproduce the computational cells.  The reading cells are quotations, verifiable
# against the sources named in FINDINGS.md and ADDENDUM_1.
cd "$(dirname "$0")" && python3 shape_field.py && python3 cghn_chain.py
