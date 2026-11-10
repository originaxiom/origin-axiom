#!/bin/bash
# P-756(b), the tau side: the sealed full run (the rule is p756b_concentration.py's header). Run from this directory.
set -u
python3 -I p756b_concentration.py full out_p756b.json > run_out.txt 2> run_err.txt
echo $? > run_exit.txt
