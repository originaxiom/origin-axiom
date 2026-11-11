#!/bin/bash
# The one run of the card. The script and its sha256 were committed and pushed before this was executed.
cd "$(dirname "$0")"
sha256sum -c prereg_sha256.txt > run_sha_check.txt 2>&1 || { echo "sha mismatch" >> run_sha_check.txt; exit 3; }
python3 -I value_not_place.py > run_out.txt 2> run_err.txt
echo $? > run_exit.txt
