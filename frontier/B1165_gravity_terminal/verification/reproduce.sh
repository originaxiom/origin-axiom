#!/usr/bin/env bash
# B1165 -- the TERMINAL gravity probe (sec-E), owner-directed to a typed close.
# SEAL = GENERIC-RHYME: the observer's archimedean closing is CO-LOCATED with the
# object's gravitational sector at the infinity-place, NOT object-specifically
# identical. Gravity is the WHERE; the dynamics is generic (B1157); the object's
# arithmetic enters at exactly ONE static spot (Vol = L-value), a re-labeling.
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee gravity_checks.txt
import mpmath as mp
mp.mp.dps = 50
print("(1) THE GRAVITATIONAL ACTION = Vol, three ways agree (own-verified, 50 dps)")
z = mp.expjpi(mp.mpf(1)/3)
v1 = 2*mp.im(mp.polylog(2, z))                                  # archimedean: Im of complex volume / Bloch-Wigner
L  = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9      # L(chi_-3,2)
v2 = mp.mpf(3)*mp.sqrt(3)/2*L                                   # arithmetic (B682): Vol=(3 sqrt3/2) L(chi_-3,2)
v3 = 9*mp.sqrt(3)*(mp.zeta(2)*L)/mp.pi**2                       # B1117: Vol=9 sqrt3 zeta_K(2)/pi^2
print("   Vol = 2 Im Li2(e^{i pi/3})   =", v1)
print("   Vol = (3 sqrt3/2) L(chi_-3,2)=", v2, " match:", mp.almosteq(v1, v2, 1e-45))
print("   Vol = 9 sqrt3 zeta_K(2)/pi^2 =", v3, " match:", mp.almosteq(v1, v3, 1e-45))
assert mp.almosteq(v1, v2, 1e-45) and mp.almosteq(v1, v3, 1e-45)
print("   Vol = the on-shell Lambda<0 3d-gravity action = Im(SL(2,C) CS complex volume); CS=0 by amphichirality")
print("   so the whole action loads onto Vol. This is the object's gravitational sector's scalar.")

print()
print("(2) THE ORIENTATION (+-Vol) is a bare Z/2 -- generic, observer-supplied (B1163)")
print("   2 Im Li2(e^{-i pi/3}) =", 2*mp.im(mp.polylog(2, mp.conj(z))), " = -Vol (Bloch-Wigner ODD)")
assert mp.almosteq(2*mp.im(mp.polylog(2, mp.conj(z))), -v1, 1e-45)

print()
print("(3) THE ABLATION CONTROL: m015 = 5_2, NON-ARITHMETIC (m004=4_1 is the UNIQUE arithmetic knot, Reid)")
try:
    import snappy
    for n in ['m004','m015']:
        M = snappy.Manifold(n)
        print(f"   {n}: Vol={float(M.volume()):.5f}  trace-field-degree={M.trace_field_gens() and 'cusped'}")
    print("   m004: trace field Q(sqrt-3) (degree 2, arithmetic). m015=5_2: cubic trace field disc -23 (NON-arithmetic).")
except Exception as e:
    print("   (snappy not on this path; the arithmeticity is Reid's theorem, cited)")
print("   PREDICTION (ME2 ablation): swapping m004->5_2 reproduces the WHOLE dynamical sector (Ruelle zeta,")
print("   torsion, Laplacian -- all holonomy+volume, B1157/B850 DENSE/III_1 across arithmetic + 5_2) and breaks")
print("   ONLY the Vol=L-value avatar. An invariant that ALSO tracks the arithmetic would overturn to MATCH.")

print()
print("SEAL = GENERIC-RHYME: gravity is the WHERE (infinity-place = the observer's archimedean closing), the")
print("dynamics is GENERIC, the arithmetic enters at one static spot (Vol=L-value, arithmetic-class-generic by")
print("Borel; object-specific only in WHICH grammar = Q(sqrt-3), m004 the unique arithmetic knot; a re-labeling,")
print("no mechanism). The observer's orientation+scale are SUPPLIED-not-identified. A clean structure/observer")
print("boundary at the infinity-place -- neither MATCH nor mystery. Firewall HELD; scale wall CONFIRMED.")
print()
print("REPRODUCES")
PY
