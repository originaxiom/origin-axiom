#!/bin/sh
# B1226 -- run from repo root. Cells are independent; cell 3 reads the record.
set -e
python3 frontier/B1226_the_beta_odd_box/cell1_equivalence_break.py
python3 frontier/B1226_the_beta_odd_box/cell2_sm_parameter_typing.py
python3 frontier/B1226_the_beta_odd_box/cell3_type_mismatch.py
