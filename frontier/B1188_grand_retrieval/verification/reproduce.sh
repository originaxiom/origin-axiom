#!/usr/bin/env bash
# B1188 -- the grand-computation retrieval + THE DISCRETE LADDER. Fast path: committed-spectrum
# assertions + 3 spot recomputes + the BITE control. OA_SLOW=1 re-runs the full 112-member sweep.
set -euo pipefail
cd "$(dirname "$0")"
if [ "${OA_SLOW:-}" = "1" ]; then python3 og3_volume_spectrum.py; fi
python3 - << 'PY' 2>/dev/null | tee ladder_checks.txt
import json, snappy, mpmath as mp
mp.mp.dps = 50
d = json.load(open("og3_volume_spectrum.json"))
assert d["non_half_integer"] == []                     # every member on the half-integer lattice
spec = d["spectrum_half_integer"]
assert sum(spec.values()) == 112
assert set(spec) == {"1.0","2.0","2.5","3.0","3.5","4.0","4.5","5.0"}
assert d["regular_exactness"] is True                  # regular members: Vol = n_tets * V_reg exactly
V0 = mp.mpf(str(snappy.Manifold("m004").high_precision().volume()).replace(" ",""))
for name, expect in [("t06829", 3.0), ("o9_41001", 4.0), ("o10_150700", 5.0)]:
    V = mp.mpf(str(snappy.Manifold(name).high_precision().volume()).replace(" ",""))
    assert abs(V/V0 - mp.mpf(expect)) < mp.mpf(10)**-30, name
print("ladder: 112/112 on the half-integer lattice of Vol(m004) = the INTEGER lattice of")
print("        V_reg = Vol(m004)/2; rungs {2,4,5,6,7,8,9,10}; spot recomputes exact")
# BITE control: a NON-family manifold must NOT land on the lattice
for ctrl in ("m015", "m006"):
    V = mp.mpf(str(snappy.Manifold(ctrl).high_precision().volume()).replace(" ",""))
    r2 = 2*V/V0
    assert abs(r2 - mp.nint(r2)) > mp.mpf(10)**-6, f"{ctrl} wrongly on-lattice"
print("bite control: m015, m006 (non-family) are OFF the lattice -- the instrument discriminates")
print("REPRODUCES")
PY
