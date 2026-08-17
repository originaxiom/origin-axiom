"""ITEM 1 -- the OUTER tau-composite real forms.  Does any make su(5) real?

The 63 INNER forms all return so(10) (126/126, cell18).  Per THE RULE that named a class,
and the boundary is the outer forms.  B907 swept all 128 inner AND outer representatives and
found this object's first measurement wall real in e6(2) and ONLY there -- non-compact.

CONSTRUCTION, with the trap recorded.  sigma is an automorphism of e6, NOT of e8: permuting
the first six ROOT coordinates keeps a block root inside its own block.  sigma must act on
the e6-WEIGHT, and that weight pairs over ALL EIGHT coordinates (a 27-root has c7 != 0 and
the E8 Cartan couples node 5 to node 6).  Truncating to six was the first bug and the gate
caught it.

GATE, binding: sigma must carry the 27's weights onto the 27-bar's, 27 of 27.
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

SIG = {0: 5, 5: 0, 2: 4, 4: 2, 1: 1, 3: 3}
A8 = E.A
BARB = [r for r in E.ROOTS if r[6] % 3 == 2 and r[7] == 0]
IB = {r: i for i, r in enumerate(BARB)}

def wt(r):   return tuple(sum(r[k]*A8[k][i] for k in range(8)) for i in range(6))
def sig_wt(w): return tuple(w[SIG[i]] for i in range(6))
W27 = {wt(r): r for r in TWENTYSEVEN}
WBAR = {wt(r): r for r in BARB}
SIGMA = {}
for w, r in W27.items():
    t = sig_wt(w)
    assert t in WBAR, "GATE FAILED: sigma does not land in the 27-bar"
    SIGMA[r] = WBAR[t]
print(f"GATE sigma: 27 -> 27-bar, {len(SIGMA)} of 27 -- PASS", flush=True)

def line(f_):
    S = [(Pm16@vec(embed_form(f, n, TWENTYSEVEN)))%P for f, n in f_]
    ind = []
    for s_ in S:
        T = np.array([[int(t)%P for t in u] for u in ind+[s_]], dtype=np.int64)
        if rank_mod_p(T) > len(ind): ind.append(s_)
    return ind
def act_blk(s, blk, idx):
    rows = []
    for Xb in E6_BASIS:
        d = {E.N+E.IDX[blk[i]]: Fraction(int(s[i])%P) for i in range(27) if int(s[i])%P}
        img = E.br(Xb, d); col = [0]*27
        for k, val in img.items(): col[idx[E.ROOTS[k-E.N]]] = (val.numerator%P)*pow(val.denominator%P, P-2, P)%P
        rows.append(col)
    return np.array(rows, dtype=np.int64).T%P
def pures(ind):
    o = []
    for t in range(P):
        s_ = (ind[0]+t*ind[1])%P
        if not np.count_nonzero(s_): continue
        r_ = [[int(z)%P for z in (A_.astype(object)@s_)%P] for A_ in ops]
        if 45-rank_mod_p(np.array(r_, dtype=np.int64).T%P) == 34: o.append((t, s_))
    return o
OM  = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
OM2 = [(sp.expand(Phi**2), 8), (sp.expand(Psi**4), 16), (sp.expand(Wp*Phi**2), 16)]
pw, pw2 = pures(line(OM)), pures(line(OM2)); d2 = dict(pw2)
print(f"pure spinors: omega t={[t for t,_ in pw]}", flush=True)

def tau_outer(s_conj, eps):
    """outer conjugation: coefficient-conjugated (the omega^2 vector), then sigma,
       twisted by the sign grading eps."""
    out = np.zeros(27, dtype=object)
    for i, r in enumerate(TWENTYSEVEN):
        c = int(s_conj[i]) % P
        if c:
            sgn = -1 if sum(eps[k]*r[k] for k in range(6)) % 2 else 1
            out[IB[SIGMA[r]]] = (sgn*c) % P
    return out

grad = list(itertools.product((0, 1), repeat=6))
print(f"outer real forms to sweep: {len(grad)} gradings x {len(pw)} spinors = {len(grad)*len(pw)}\n", flush=True)
spec = Counter(); hits = []
for eps in grad:
    for (t, s1) in pw:
        ts = tau_outer(d2[t], eps)
        M = np.vstack([act_blk(s1, TWENTYSEVEN, IDX27), act_blk(ts, BARB, IB)])%P
        d, kr = reductive_dim(M)
        spec[(d, kr)] += 1
        if kr == 24: hits.append((eps, t))
print("(dim, reductive) over all OUTER forms:")
for (d, kr) in sorted(spec):
    tag = "   <<<<<< su(5) REAL IN AN OUTER FORM >>>>>>" if kr == 24 else ("   <- so(10)" if kr == 45 else "")
    print(f"  dim {d:3d}  reductive {kr:3d}   ({spec[(d,kr)]} of {len(grad)*len(pw)}){tag}")
print(f"\nIS su(5) REAL IN ANY OUTER FORM?  {bool(hits)}")
if hits: print(f"  {len(hits)} hits, first gradings: {[h[0] for h in hits[:4]]}")
