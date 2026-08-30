#!/usr/bin/env bash
# B1180 -- cc3's B8147 family-denominator retraction ADOPTED; every named witness spot-verified here.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee witnesses.txt
import snappy, math
Vm = snappy.Manifold('m004').volume()
M = snappy.Manifold('o10_150700')
assert str(M.homology()) == 'Z' and M.num_cusps() == 1
assert abs(float(M.volume()/Vm) - 5.0) < 1e-9
omega = complex(0.5, math.sqrt(3)/2)
assert all(abs(complex(z)-omega) < 1e-9 for z in M.tetrahedra_shapes('rect'))
print("o10_150700: H1=Z, 1 cusp, all-regular, Vol=5xVol(m004) -- the H1 separator is DEAD")
for name in ['o10_150684','o10_150685','o10_150693','t12840']:
    N = snappy.Manifold(name)
    assert any(abs(abs(complex(c['shape']).imag)-2*math.sqrt(3))<1e-6 and abs(complex(c['shape']).real)<1e-6
               for c in N.cusp_info()), name
print("o10_150684/85/93 + t12840: each carries a 2sqrt3 i cusp -- the cusp-shape separator is DEAD (multi-cusped carriers)")
S = snappy.Manifold('s955')
assert 'Z/20' in str(S.homology()) and abs(float(S.volume()/Vm)-3.0) < 1e-9
print("s955: H1=Z/20+Z, Vol=3xVol(m004) -- R014's witness corrected exactly as B8147 states")
print("REPRODUCES")
PY
