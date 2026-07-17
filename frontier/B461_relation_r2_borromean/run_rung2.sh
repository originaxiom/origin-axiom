#!/bin/bash
# per-class isolation, 20-min timeout each (the ladder's stop-criteria), unbuffered
cd "$(dirname "$0")"
SAGEBIN=/Users/dri/micromamba/envs/sage/bin/sage
for nm in L6a4 s776; do
  n=$(python3 -c "import json; print(len(json.load(open('ptolemy_systems.json'))['$nm']['3']))")
  for ((ci=0; ci<n; ci++)); do
    if ! timeout 1200 $SAGEBIN rung2_perclass.sage $nm $ci 2>/dev/null; then
      echo "$nm class $ci: TIMEOUT(20min) — recorded per ladder"
    fi
  done
done
echo "RUNG2 SWEEP COMPLETE"
