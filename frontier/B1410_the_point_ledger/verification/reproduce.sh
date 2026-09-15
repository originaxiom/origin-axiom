#!/bin/sh
# B1410 — reproduce every number in FINDINGS.md from a CLEAN CHECKOUT.
# No absolute paths outside the repo (E80: a verification that reaches outside the repository
# is not runnable by anyone else). Run from anywhere; resolves the repo root from this file.
set -eu
ROOT=$(cd "$(dirname "$0")/../../.." && pwd)
cd "$ROOT"

echo "== the seal is unmodified (a seal that can be edited afterwards is not a seal) =="
sha256sum frontier/B1410_the_point_ledger/PREREGISTRATION.md
cat frontier/B1410_the_point_ledger/ARTIFACT_HASHES.txt

echo
echo "== MB12: the decision rule, both directions =="
python3 scripts/checks/point_census.py --selftest

echo
echo "== calibration against the sealed sets (reported as measured, never tuned) =="
python3 scripts/checks/point_census.py --calibrate

echo
echo "== the ledger under the sealed rule =="
python3 scripts/checks/point_census.py --classify

echo
echo "== the two basis-free cusp facts on the ceiling cover (L219's reframe) =="
python3 - <<'PY'
import snappy
M = snappy.Manifold('L14n63694')
a = [float(x) for x in M.cusp_areas(policy='unbiased')]
print('  unbiased cusp areas / (2*sqrt6):', [round(x / (2 * 6 ** .5), 10) for x in a])
G = M.symmetry_group()
perms = {tuple(i.cusp_images()) for i in G.isometries()}
par = {i: i for i in range(M.num_cusps())}
find = lambda x: x if par[x] == x else find(par[x])
for p in perms:
    for i, j in enumerate(p):
        ri, rj = find(i), find(j)
        if ri != rj:
            par[ri] = rj
orb = {}
for i in range(M.num_cusps()):
    orb.setdefault(find(i), []).append(i)
print('  Isom =', G, '| cusp orbits:', sorted(map(sorted, orb.values())))
PY

echo
echo "== the locks =="
python3 -m pytest tests/test_b1410_point_ledger.py tests/test_b1264_h5_census.py -q
