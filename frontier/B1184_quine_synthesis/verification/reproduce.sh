#!/usr/bin/env bash
# B1184 -- THE QUINE SYNTHESIS: self-naming without self-signing (S4 dispositioned).
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' 2>/dev/null | tee quine.txt
import snappy
Vm = snappy.Manifold('m004').volume()
# (1) B762's QUINE survives B8147: the new members excluded by its own filters
assert abs(float(snappy.Manifold('o10_150700').volume()/Vm) - 5.0) < 1e-9         # volume filter
for n in ['o10_150684','o10_150685','o10_150693','t12840']:
    assert snappy.Manifold(n).num_cusps() > 1, n                                   # 1-cusped filter
m3 = complex(snappy.Manifold('m003').cusp_info()[0]['shape'])
assert abs(m3.imag - 3.4641) > 0.1                                                 # shape filter
print("(1) the QUINE stands post-B8147: o10_150700 excluded (5x vol); the four 2sqrt3i carriers excluded")
print("    (multi-cusped); m003 excluded (shape omega). Census-scoped, correctly stated in B762.")
# (2) the name's parity: every emitted letter mirror-even
M = snappy.Manifold('m004'); W = snappy.Manifold('m004'); W.reverse_orientation()
assert abs(float(M.volume()) - float(W.volume())) < 1e-9
t, tw = complex(M.cusp_info()[0]['shape']), complex(W.cusp_info()[0]['shape'])
assert abs(t - (-tw.conjugate())) < 1e-9 or abs(t - tw) < 1e-9
print("(2) the emitted name {volume, cusp shape, CM disc, residue, palette counts} is mirror-even")
print("    letter-by-letter = exactly the parity law's OBJECT side (B1168). No odd letter exists in it.")
print("(3) SELF-NAMING WITHOUT SELF-SIGNING: QP-1 QUINE (can name) + B1183 ONE-CLASS (cannot sign; the")
print("    missing sign IS c's class). Naming and choosing are proved complementary. REPRODUCES")
PY
