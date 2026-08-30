#!/usr/bin/env bash
# B1156 SEAM-A Gate 2 -- reproduce the archimedean anchor the FLOOR rests on.
# The single class xi=[e^{i pi/3}] in K_3(Q(sqrt-3)); its Borel/Bloch-Wigner
# regulator IS Vol(4_1). This is the real summand the full/Arakelov arithmetic
# CS carries -- the reason the a-priori "torsion codomain => cannot reach Vol"
# MISMATCH is refuted (it is a property of the finite mu_n truncation only).
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee archimedean_anchor.txt
import mpmath as mp
mp.mp.dps = 30
z = mp.expjpi(mp.mpf(1)/3)                 # e^{i pi/3} = (1+i sqrt3)/2
print("z                =", z)
print("z^2 - z + 1      =", mp.chop(z**2 - z + 1), " (0 => primitive 6th root; geometric shape of m004)")
D = mp.im(mp.polylog(2, z))                # Bloch-Wigner D(z); |z|=1 => arg-term vanishes
print("D(e^{i pi/3})    =", D, "  (= Borel regulator of xi in K_3(Q(sqrt-3)))")
print("2*D = Vol(4_1)   =", 2*D)
ok = mp.almosteq(2*D, mp.mpf('2.029883212819307'), 1e-14)
print("matches SnapPy Vol(4_1)=2.029883212819307... :", ok)
print("V'' (1-loop)     = sqrt(-3) =", mp.sqrt(-3))
assert mp.chop(z**2 - z + 1) == 0, "minpoly"
assert ok, "Vol"
print("REPRODUCES" if ok else "FAILED")
PY
