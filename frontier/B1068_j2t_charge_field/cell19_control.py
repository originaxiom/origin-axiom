"""POSITIVE CONTROL, done properly -- can the instrument detect su(3)+su(2)+u(1)?

The first attempt sampled RANDOM elements of the su(5) and got dim 4 every time: the
centraliser of a GENERIC element is the Cartan.  The Standard Model sits on a WALL --
where an A2+A1 subsystem of roots vanishes -- which is measure zero.  Random sampling
can never find it, so that control was uninformative about the detector.

Done properly: decompose the carrier under ad(Cartan), get the root functionals, and
SOLVE for the y they annihilate.  If (12,11) is found, the detector works and the
"rank 11 never occurs over C" result is meaningful.  If not, that result means nothing.
"""
import os, sys, pathlib, itertools, random
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

def line(f_):
    S = [(Pm16@vec(embed_form(f, n, TWENTYSEVEN)))%P for f, n in f_]
    ind = []
    for s_ in S:
        T = np.array([[int(t)%P for t in u] for u in ind+[s_]], dtype=np.int64)
        if rank_mod_p(T) > len(ind): ind.append(s_)
    return ind
def act_blk(s):
    rows = []
    for Xb in E6_BASIS:
        d = {E.N+E.IDX[TWENTYSEVEN[i]]: Fraction(int(s[i])%P) for i in range(27) if int(s[i])%P}
        img = E.br(Xb, d); col = [0]*27
        for k, val in img.items(): col[IDX27[E.ROOTS[k-E.N]]] = (val.numerator%P)*pow(val.denominator%P, P-2, P)%P
        rows.append(col)
    return np.array(rows, dtype=np.int64).T%P
def pures(ind):
    o = []
    for t in range(P):
        s_ = (ind[0]+t*ind[1])%P
        if not np.count_nonzero(s_): continue
        r_ = [[int(z)%P for z in (A_.astype(object)@s_)%P] for A_ in ops]
        if 45-rank_mod_p(np.array(r_, dtype=np.int64).T%P) == 34: o.append(s_)
    return o
OM  = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
OM2 = [(sp.expand(Phi**2), 8), (sp.expand(Psi**4), 16), (sp.expand(Wp*Phi**2), 16)]
pu, pu2 = pures(line(OM)), pures(line(OM2))
M = np.vstack([act_blk(pu[0]), act_blk(pu2[1])])%P
els = []
for vv in nullspace(M):
    xx = {}
    for co, Xb in zip(vv, E6_BASIS):
        if co % P: xx = E.vadd(xx, E.vmul(Fraction(int(co)%P), Xb))
    els.append(xx)
print(f"su(5) carrier: dim {len(els)}, reductive {reductive_dim(M)[1]}", flush=True)

def cent_of(y):
    rows = []
    for z in els:
        b_ = E.br(y, z)
        rows.append([(b_.get(k, Fraction(0)).numerator%P)*pow(b_.get(k, Fraction(0)).denominator%P, P-2, P)%P
                     for k in range(E.DIM)])
    sub = []
    for vv in nullspace(np.array(rows, dtype=np.int64).T%P):
        xx = {}
        for co, z in zip(vv, els):
            if co % P: xx = E.vadd(xx, E.vmul(Fraction(int(co)%P), z))
        sub.append(xx)
    K = np.zeros((len(sub), len(sub)), dtype=np.int64)
    for r1, z1 in enumerate(sub):
        for r2, z2 in enumerate(sub):
            kv = E.killing_pair(z1, z2); K[r1, r2] = (kv.numerator%P)*pow(kv.denominator%P, P-2, P)%P
    return len(sub), (rank_mod_p(K) if sub else 0), sub

random.seed(3); y0 = {}
for z in els: y0 = E.vadd(y0, E.vmul(Fraction(random.randrange(P)), z))
_, _, cart = cent_of(y0)
print(f"Cartan of the carrier: dim {len(cart)}", flush=True)

# root functionals: how ad(cartan) acts.  Build the matrix of ad(h_i) on the carrier and
# read simultaneous eigenvalues by scanning which elements are killed by which h.
# Practical route: for each candidate y in the span of the Cartan, cent dimension is what
# we want -- so SOLVE by picking triples of "root directions" found from the adjoint action.
# Root directions = the distinct kernels of ad(h) for h in a spanning set.
print("\nsolving for wall points (kernels of triples of root functionals):", flush=True)
basis = cart
seen = Counter(); found = None
tried = 0
for combo in itertools.combinations(range(len(els)), 3):
    # use three carrier elements as 'root vectors'; y must satisfy [y, z] = 0 for each
    rows = []
    for i in combo:
        z = els[i]
        for h in basis:
            pass
    # build the linear map y -> ([y,z1],[y,z2],[y,z3]) restricted to y in the Cartan
    Amat = []
    for h in basis:
        col = []
        for i in combo:
            b_ = E.br(h, els[i])
            col += [(b_.get(k, Fraction(0)).numerator%P)*pow(b_.get(k, Fraction(0)).denominator%P, P-2, P)%P
                    for k in range(E.DIM)]
        Amat.append(col)
    ker = nullspace(np.array(Amat, dtype=np.int64).T%P)
    tried += 1
    for vv in ker:
        y = {}
        for co, h in zip(vv, basis):
            if co % P: y = E.vadd(y, E.vmul(Fraction(int(co)%P), h))
        if not y: continue
        d, kr, _ = cent_of(y)
        seen[(d, kr)] += 1
        if (d, kr) == (12, 11): found = (combo, y); break
    if found or tried >= 300: break
print(f"  wall points examined from {tried} triples")
for k in sorted(seen): print(f"    dim {k[0]:3d} reductive {k[1]:3d}  ({seen[k]})"
                             + ("   <<< su(3)+su(2)+u(1) -- DETECTOR WORKS >>>" if k == (12,11) else ""))
print(f"\nDETECTOR CAN SEE rank 11:  {(12,11) in seen}")
