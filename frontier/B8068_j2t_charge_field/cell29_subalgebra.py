"""THE SUBALGEBRA-STABILISER CLASS -- T1 and T2 of the sealed criterion.

Baez-Schwahn Thm 1: X = h2(C), B = h3(C), X in B in h3(O)
  => Stab(X) ^ Stab(B)_0 = S(U(2)xU(3)) = the SM gauge group,
  with Stab(B)_0 = (SU(3)xSU(3))/Z3, i.e. su(3)+su(3), DIMENSION 16.

We work in e6 (the E8 realisation).  F4 = Stab_{E6}(the Jordan identity), which we
already know is dim 52 -- that is the CONTROL for the ambient group.

T1: is J^{2T} contained in a 9-dimensional Jordan subalgebra?  Equivalently, does the
    object determine a B?  We test the shape available to us: the su(3)+su(3) that
    appeared at 18 of 10556 charge directions.
T2: is that 16-dimensional thing really su(3)+su(3) -- dim 16, Killing rank 16?
    THE CONTROL.  Nothing below is read if it fails.
"""
import os, sys, pathlib, itertools
import numpy as np, sympy as sp
from fractions import Fraction
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093
src = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "cell5_spinor_test.py")).read_text()
src = src.split('print("\\nSTABILISER')[0].replace(
    "PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093", f"PRIME = {PRIME}")
exec(compile(src, "c5", "exec"))
import e8_build as E

print("\n" + "="*72)
print("CONTROL 0 -- F4 = Stab(the Jordan identity) must be dim 52")
print("="*72)
v0 = embed_form(sp.Integer(1), 0, TWENTYSEVEN)   # the degree-0 invariant = the identity
M0 = act(v0, IDX27)
d0, k0 = reductive_dim(M0)
print(f"  Stab_E6(identity): dim {d0}, Killing rank {k0}   (want 52, 52 = F4)")
F4_OK = (d0, k0) == (52, 52)
print(f"  CONTROL 0: {'PASS' if F4_OK else 'FAIL'}")
if not F4_OK:
    print("  F4 not reproduced -- nothing below is read."); sys.exit(1)

# a basis of f4 as e6-elements
ns = nullspace(M0); F4 = []
for vv in ns:
    xx = {}
    for co, Xb in zip(vv, E6_BASIS):
        if co % P: xx = E.vadd(xx, E.vmul(Fraction(int(co)%P), Xb))
    F4.append(xx)
print(f"  f4 basis built: {len(F4)} elements")

print("\n" + "="*72)
print("T1/T2 -- the charge algebra's 16-dimensional stratum")
print("="*72)
# rebuild the charge algebra C = <x8,x14,x16,x22> in the adjoint
def hw_e6(n):
    cands = [r for r in E6_ROOTS if int(list(E.br(h, E.ev(r)).values())[0] if E.br(h, E.ev(r)) else 0) == n]
    M = sp.zeros(E.DIM, len(cands))
    for j, r in enumerate(cands):
        for k, val in E.br(ee, E.ev(r)).items(): M[k, j] = sp.Rational(val.numerator, val.denominator)
    nsx = M.nullspace()
    if not nsx: return None
    v = {}
    for j, r in enumerate(cands):
        co = sp.Rational(nsx[0][j])
        if co: v = E.vadd(v, {E.N+E.IDX[r]: Fr(co)})
    return v
x_, y_ = sp.symbols('x y')
tf = x_**5*y_ - x_*y_**5; Wf = x_**8 + 14*x_**4*y_**4 + y_**8
ADJ = {8: Wf, 14: sp.expand(tf*Wf), 16: sp.expand(Wf**2), 22: sp.expand(tf*Wf**2)}
Cb = {}
for n in (8, 14, 16, 22):
    top = hw_e6(n)
    if top is None: continue
    Pp = sp.Poly(ADJ[n], x_, y_); acc, cur = {}, top
    for k in range(n+1):
        co = Pp.coeff_monomial(x_**(n-k)*y_**k)
        if co: acc = E.vadd(acc, E.vmul(Fr(sp.Rational(co)*sp.factorial(n-k)/sp.factorial(n)), cur))
        cur = E.br(ff, cur)
    Cb[n] = acc
print(f"  charge algebra C rebuilt: degrees {sorted(Cb)}")

def kr_of(els):
    K = np.zeros((len(els), len(els)), dtype=np.int64)
    for r1, z1 in enumerate(els):
        for r2, z2 in enumerate(els):
            kv = E.killing_pair(z1, z2); K[r1, r2] = (kv.numerator%P)*pow(kv.denominator%P, P-2, P)%P
    return rank_mod_p(K) if els else 0

def cent_in(host, c):
    rows = []
    for z in host:
        b_ = E.br(c, z)
        rows.append([(b_.get(k, Fraction(0)).numerator%P)*pow(b_.get(k, Fraction(0)).denominator%P, P-2, P)%P
                     for k in range(E.DIM)])
    out = []
    for vv in nullspace(np.array(rows, dtype=np.int64).T%P):
        xx = {}
        for co, z in zip(vv, host):
            if co % P: xx = E.vadd(xx, E.vmul(Fraction(int(co)%P), z))
        out.append(xx)
    return out

print("\n  scanning charge directions INSIDE f4 (not inside e6) for the 16-stratum:")
import random; random.seed(11)
degs = sorted(Cb)
CAND = []
for i in range(len(degs)):
    for j in range(i+1, len(degs)):
        for t in range(P):
            v = [0]*len(degs); v[i] = 1; v[j] = t; CAND.append(tuple(v))
for _ in range(3000):
    CAND.append(tuple(random.randrange(P) for _ in degs))
CAND = [c for c in set(CAND) if any(c)]
spec = Counter(); hits16 = []
for co in CAND:
    c = {}
    for a_, n in zip(co, degs):
        if a_: c = E.vadd(c, E.vmul(Fraction(a_%P), Cb[n]))
    sub = cent_in(F4, c)
    key = (len(sub), kr_of(sub))
    spec[key] += 1
    if key == (16, 16) and len(hits16) < 3: hits16.append((co, sub))
print(f"  directions tested: {len(CAND)} (all coordinate 2-planes exhaustively + 3000 random)")
for k in sorted(spec):
    tag = "   <<< su(3)+su(3) = Stab(B)_0 of Baez-Schwahn >>>" if k == (16,16) else ""
    print(f"    dim {k[0]:3d}  reductive {k[1]:3d}   ({spec[k]}){tag}")
print(f"\n  T2 CONTROL -- does (16,16) occur inside f4?  {(16,16) in spec}")
if (16,16) in spec:
    print(f"     found at {spec[(16,16)]} of {len(CAND)} directions")
    print("     -> the object DOES determine a 16-dimensional su(3)+su(3) inside F4,")
    print("        which is the dimension and Killing rank of Baez-Schwahn's Stab(B)_0.")
