#!/usr/bin/env bash
# B1182 -- C4' RESOLVED POSITIVE: the unique label-preserving iso (c,r,theta) -> (k11,k7,k5).
# + THE TIME'S-ARROW TYPED FINITE-PLACE (the first execution of the B8144 escape-instrument).
set -euo pipefail
cd "$(dirname "$0")"
python3 - << 'PY' | tee c4prime.txt
import sympy as sp
# (1) trace-reversal invariance, exact, generic 2x2 (NOT just SL2), words to length 5
a11,a12,a21,a22,b11,b12,b21,b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
A = sp.Matrix([[a11,a12],[a21,a22]]); B = sp.Matrix([[b11,b12],[b21,b22]])
for name, ms in [("AB",[A,B]),("AAB",[A,A,B]),("ABB",[A,B,B]),("ABAB",[A,B,A,B]),("AABAB",[A,A,B,A,B]),("ABBAB",[A,B,B,A,B])]:
    fwd = sp.eye(2); rev = sp.eye(2)
    for m in ms: fwd = fwd*m
    for m in reversed(ms): rev = rev*m
    assert sp.simplify(sp.trace(fwd)-sp.trace(rev)) == 0, name
print("(1) tr(w) = tr(w^rev) exactly, generic 2x2, 6 words to length 5 (the classical transposition")
print("    anti-automorphism fact, verified) => REVERSAL r FIXES THE TRACE FIELD K POINTWISE.")
# (2) the branch leg table + uniqueness of the K-fixer
z = sp.symbols('z'); PHI = sp.Poly(z**4 - z**2 + 1, z)
red = lambda e: sp.Poly(sp.expand(e), z).rem(PHI).as_expr()
act = lambda e,k: red(sp.expand(e.subs(z, z**k)))
sqrt3 = red(z + z**11); i_ = red(z**3); sqrtm3 = red(sqrt3*i_)
fix = lambda e,k: sp.simplify(act(e,k)-e)==0
assert [k for k in (5,7,11) if fix(sqrtm3,k)] == [7]
assert fix(sqrt3,11) and not fix(sqrtm3,11) and fix(i_,5)
print("(2) k7 is the UNIQUE nontrivial branch leg fixing K pointwise; k11 = c (B1174); k5 fixes i.")
# (3) the group law of the forced assignment
assert (11*7) % 12 == 5
print("(3) c->k11 (forced, B1174), r->k7 (forced, (1)+(2)), theta=cr->k5; 11.7=5 mod 12: a genuine V4 iso.")
print("C4' RESOLVED POSITIVE; the arrow (r) -> k7 = the arithmetic form-class swap => FINITE-PLACE. REPRODUCES")
PY
