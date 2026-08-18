"""T1 -- is the su(3)+su(3) actually Stab(B) for a 9-dimensional B in the 27?

Stab(B) preserves B SETWISE.  So if our 16-dim su(3)+su(3) is Stab(B)_0, then B is a
9-DIMENSIONAL INVARIANT SUBSPACE of the 27 under it, and it must contain the Jordan
IDENTITY (h3(C) contains the identity of h3(O)).

Method: Casimir of the 16 acting on the 27; eigenvalue multiplicities give the
isotypic decomposition.  Look for a 9.  Then check the identity's component.

CONTROL: the Casimir must have integer-consistent multiplicities summing to 27.
"""
import os, sys, pathlib, random
import numpy as np, sympy as sp
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
exec(compile(pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
     "cell29_subalgebra.py")).read_text().split('print("\\n  scanning charge')[0], "c29", "exec"))
import e8_build as E
random.seed(11); degs = sorted(Cb)
CAND = []
for i in range(len(degs)):
    for j in range(i+1, len(degs)):
        for t in range(P):
            v = [0]*len(degs); v[i] = 1; v[j] = t; CAND.append(tuple(v))
for _ in range(3000): CAND.append(tuple(random.randrange(P) for _ in degs))
CAND = [c for c in set(CAND) if any(c)]
S16 = None; CDIR = None
for co in CAND:
    c = {}
    for a_, n in zip(co, degs):
        if a_: c = E.vadd(c, E.vmul(Fraction(a_%P), Cb[n]))
    sub = cent_in(F4, c)
    if len(sub) == 16 and kr_of(sub) == 16: S16, CDIR = sub, co; break
print(f"su(3)+su(3) recovered at charge direction {CDIR}, dim {len(S16)}", flush=True)

# action of the 16 on the 27
def act27(x):
    cols = []
    for r in TWENTYSEVEN:
        img = E.br(x, E.ev(r)); col = [0]*27
        for k, val in img.items():
            rr = E.ROOTS[k-E.N]
            if rr not in IDX27: raise AssertionError("left the 27")
            col[IDX27[rr]] = (val.numerator%P)*pow(val.denominator%P, P-2, P)%P
        cols.append(col)
    return np.array(cols, dtype=np.int64).T%P
A27 = [act27(x) for x in S16]
print(f"  {len(A27)} action matrices on the 27 built", flush=True)

# Casimir via the trace form on the 16
G = np.array([[int(np.trace(A27[i].astype(object)@A27[j].astype(object))%P)
               for j in range(16)] for i in range(16)], dtype=np.int64)
print(f"  CONTROL: trace form on the 16 is nondegenerate: rank {rank_mod_p(G)} of 16", flush=True)
Gi = sp.Matrix(16, 16, lambda r, c: int(G[r, c])).inv_mod(P)
Om = np.zeros((27, 27), dtype=object)
for i in range(16):
    for j in range(16):
        g = int(Gi[i, j]) % P
        if g: Om = (Om + g*(A27[i].astype(object)@A27[j].astype(object))) % P
Om = Om % P
Mo = sp.Matrix(27, 27, lambda r, c: int(Om[r, c]))
L = sp.Symbol('L')
cp = Mo.charpoly(L).as_expr()
eig = {}
for r0 in range(P):
    Kn = np.array([[int((Mo - r0*sp.eye(27))[i, j])%P for j in range(27)] for i in range(27)], dtype=np.int64)
    m = 27 - rank_mod_p(Kn)
    if m: eig[r0] = m
print(f"\n  Casimir eigenvalue -> multiplicity: {eig}")
print(f"  multiplicities sum to {sum(eig.values())} of 27")
nine = [e for e, m in eig.items() if m == 9]
print(f"\n  T1 -- is there a 9-DIMENSIONAL invariant subspace?  {bool(nine)}")
if nine:
    lam = nine[0]
    Pm = np.eye(27, dtype=object)
    for mu in eig:
        if mu != lam: Pm = (Pm@((Om - mu*np.eye(27, dtype=object))*pow((lam-mu)%P, P-2, P))) % P
    v0 = embed_form(sp.Integer(1), 0, TWENTYSEVEN)
    w = np.zeros(27, dtype=object)
    for k, val in v0.items(): w[IDX27[E.ROOTS[k-E.N]]] = (val.numerator%P)*pow(val.denominator%P, P-2, P)%P
    proj = (Pm@w) % P
    inB = bool(np.count_nonzero(proj))
    print(f"     does the Jordan IDENTITY lie in it?  {inB}")
    print(f"     (h3(C) must contain the identity of h3(O))")
    if inB:
        print("\n     => a 9-dimensional invariant subspace containing the identity.")
        print("        CONSISTENT with B = h3(C).  NOT yet proof that it IS h3(C):")
        print("        that needs the Jordan product, which this machinery does not carry.")
else:
    print("     no 9-dimensional invariant subspace under the su(3)+su(3).")
    print("     => the 16 is NOT Stab(B) for a 9-dim B in this action.  T1 FAILS.")
