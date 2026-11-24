#!/bin/bash
# B1972: run one seat script inside the sandbox clone (usage: SANDBOX=<dir> reproduce_one.sh <relays subfolder>); record time, exit code and output hash
SB="${SANDBOX:?set SANDBOX to a folder holding clone/ (a sparse shared clone of the seat branch at 9b34bfc03) and logs/}"
d=$1; cd $SB/clone/relays/$d || exit 1
py=$(ls *.py | head -1); out=$(ls *_out.json 2>/dev/null | head -1)
committed_hash=$(git show 9b34bfc03:relays/$d/$out 2>/dev/null | shasum -a 256 | cut -c1-64)
start=$(date +%s)
python3 -I "$py" > $SB/logs/$d.stdout 2> $SB/logs/$d.stderr; rc=$?
end=$(date +%s)
new_hash=$(shasum -a 256 "$out" 2>/dev/null | cut -c1-64)
echo "$d rc=$rc secs=$((end-start)) committed=${committed_hash:0:16} rerun=${new_hash:0:16} $([ "$committed_hash" = "$new_hash" ] && echo IDENTICAL || echo DIFFERS)" >> $SB/logs/SUMMARY.txt
