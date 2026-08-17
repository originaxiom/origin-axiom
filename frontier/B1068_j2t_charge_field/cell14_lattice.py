"""AXIS 1b/2 -- EXHAUSTIVE over all subsets, via the meet-semilattice of annihilators.

The subset sweep is monotone: Stab(S u T) = Stab(S) ^ Stab(T).  So every one of the
2^n - 1 subsets has an annihilator that is a MEET of single-element annihilators.
Closing that lattice therefore covers ALL subsets exactly, with no enumeration of 2^19.

OBJECT LIST -- now complete across the axis matrix's character x representation cells:
    27      : 3 trivial idempotents, 3 omega covariants, 3 omega^2 covariants
    27-bar  : 3 trivial idempotents, 3 omega covariants, 3 omega^2 covariants   <- WAS MISSING
    plus    : the pure spinor(s)

SEALED: the Standard Model algebra su(3)+su(2)+u(1) is (dim 12, Killing rank 11).
Report every distinct (dim, reductive) reached, and state explicitly whether 11 occurs.
"""
import os, sys, pathlib, itertools
import numpy as np, sympy as sp
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093
src = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "cell5_spinor_test.py")).read_text()
src = src.split('print("\\nSTABILISER')[0].replace(
    "PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093", f"PRIME = {PRIME}")
exec(compile(src, "c5", "exec"))
import e8_build as E

def restricted(Vd, Pp_, Qq):
    pts, vals = [], []
    for A_, B_, C_ in itertools.product(range(-2, 3), repeat=3):
        if (A_, B_, C_) == (0, 0, 0): continue
        v = {}
        for co, n in ((A_, 0), (B_, 8), (C_, 16)):
            if co: v = E.vadd(v, E.vmul(co, Vd[n]))
        pts.append((A_, B_, C_)); vals.append(E.killing_pair(E.br(v, E.br(Pp_, v)), E.br(Qq, v)))
        if len(pts) >= 40: break
    M = sp.Matrix([[sp.Rational(int(sp.Poly(m, a, b, c).eval({a: q[0], b: q[1], c: q[2]}))) for m in mons] for q in pts])
    return sp.expand(sum(M.solve_least_squares(sp.Matrix([sp.Rational(v.numerator, v.denominator) for v in vals]))[i]*mons[i] for i in range(len(mons))))

def idem(Vd, Pp_, Qq, ti, p=P):
    C = restricted(Vd, Pp_, Qq); D = sp.expand(C/sp.Poly(C, a, b, c).coeff_monomial(a**3))
    s2, s3_ = sp.expand(D.coeff(a, 1)), sp.expand(D.coeff(a, 0))
    def red(e_, var):
        pl = sp.Poly(sp.expand(e_), var); o = 0
        for (k,), co in pl.terms():
            r = sp.Rational(co); o += (r.p % p)*pow(r.q % p, p-2, p) % p * var**k
        return sp.Poly(o, var, modulus=p)
    out = []
    for bv in range(p):
        q2 = red(s2.subs(b, bv)+sp.Rational(1, 3), c); q3 = red(s3_.subs(b, bv)-sp.Rational(2, 27), c)
        g = sp.gcd(q2, q3)
        if g.degree() < 1: continue
        for cv in sp.ground_roots(g.as_expr(), modulus=p):
            v = {}; i3 = pow(3, p-2, p)
            for co, n in ((i3, 0), (bv, 8), (int(cv) % p, 16)): v = E.vadd(v, E.vmul(Fraction(co % p), Vd[n]))
            if 78 - rank_mod_p(act(v, ti)) == 61: out.append(v)
    return out

OM  = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
OM2 = [(sp.expand(Phi**2), 8), (sp.expand(Psi**4), 16), (sp.expand(Wp*Phi**2), 16)]
OBJ = []
for k, v in enumerate(idem(V27, POP27, QOP27, IDX27)):  OBJ.append((f"e{k+1}",  act(v, IDX27)))
for k, v in enumerate(idem(VBAR, POPBAR, QOPBAR, IDXBAR)): OBJ.append((f"eb{k+1}", act(v, IDXBAR)))
for nm, FS, blk, idx in (("w", OM, TWENTYSEVEN, IDX27), ("w2", OM2, TWENTYSEVEN, IDX27),
                         ("bw", OM, TWENTYSEVENBAR, IDXBAR), ("bw2", OM2, TWENTYSEVENBAR, IDXBAR)):
    for i2, (f, n) in enumerate(FS):
        OBJ.append((f"{nm}{i2+1}", act(embed_form(f, n, blk), idx)))
# DERIVED objects: the pure spinors.  Omitted from the first lattice run, which is why
# su(5) (reductive 24) did not appear there at all.  A list of what the object HAS is not
# a list of what it DETERMINES.
def basis16(forms):
    S=[(Pm16@vec(embed_form(f,n,TWENTYSEVEN)))%P for f,n in forms]
    ind=[]
    for s_ in S:
        T=np.array([[int(t)%P for t in u] for u in ind+[s_]],dtype=np.int64)
        if rank_mod_p(T)>len(ind): ind.append(s_)
    return ind
def act_arr(s_arr, blk, idx):
    rows=[]
    for Xb in E6_BASIS:
        d={E.N+E.IDX[blk[i2]]:Fraction(int(s_arr[i2])%P) for i2 in range(27) if int(s_arr[i2])%P}
        img=E.br(Xb,d); col=[0]*27
        for k,val in img.items():
            col[idx[E.ROOTS[k-E.N]]]=(val.numerator%P)*pow(val.denominator%P,P-2,P)%P
        rows.append(col)
    return np.array(rows,dtype=np.int64).T%P
ind=basis16(OM); npure=0
for t in range(P):
    s_=(ind[0]+t*ind[1])%P
    if not np.count_nonzero(s_): continue
    rws=[[int(z)%P for z in (A_.astype(object)@s_)%P] for A_ in ops]
    if 45-rank_mod_p(np.array(rws,dtype=np.int64).T%P)==34:
        npure+=1; OBJ.append((f"pure{npure}", act_arr(s_,TWENTYSEVEN,IDX27)))
print(f"  derived pure spinors added: {npure}", flush=True)
print(f"\nOBJECT LIST ({len(OBJ)}): {[n for n,_ in OBJ]}", flush=True)
print(f"subsets this covers: 2^{len(OBJ)} - 1 = {2**len(OBJ)-1}", flush=True)

def ann(M):
    """row-reduced basis of the annihilator, as a hashable canonical form"""
    ns = nullspace(M)
    if not ns: return ()
    A_ = np.array(ns, dtype=np.int64) % P
    rows, cols = A_.shape; piv = []; r = 0
    for cc in range(cols):
        pr = next((i for i in range(r, rows) if A_[i, cc]), None)
        if pr is None: continue
        A_[[r, pr]] = A_[[pr, r]]; A_[r] = (A_[r]*pow(int(A_[r, cc]), P-2, P)) % P
        for i in range(rows):
            if i != r and A_[i, cc]: A_[i] = (A_[i]-A_[i, cc]*A_[r]) % P
        piv.append(cc); r += 1
    return tuple(map(tuple, A_[:r]))

def mat_of(sub):  return np.vstack([OBJ[i][1] for i in sub]) % P
singles = {i: ann(mat_of([i])) for i in range(len(OBJ))}
lattice = {}
for i, A_ in singles.items(): lattice[A_] = {i}
frontier = dict(lattice)
while frontier:
    nxt = {}
    for A_, srcs in frontier.items():
        for i, B_ in singles.items():
            if i in srcs: continue
            M = np.vstack([np.array(A_, dtype=np.int64)] and [mat_of(sorted(srcs | {i}))])[0] \
                if False else mat_of(sorted(srcs | {i}))
            C_ = ann(M)
            if C_ not in lattice:
                lattice[C_] = srcs | {i}; nxt[C_] = srcs | {i}
    frontier = nxt
print(f"distinct annihilators over ALL subsets: {len(lattice)}", flush=True)

from collections import Counter
spec = Counter()
for A_, srcs in lattice.items():
    els = []
    for vv in A_:
        xx = {}
        for co, Xb in zip(vv, E6_BASIS):
            if int(co) % P: xx = E.vadd(xx, E.vmul(Fraction(int(co) % P), Xb))
        els.append(xx)
    K = np.zeros((len(els), len(els)), dtype=np.int64)
    for r1, z1 in enumerate(els):
        for r2, z2 in enumerate(els):
            kv = E.killing_pair(z1, z2); K[r1, r2] = (kv.numerator % P)*pow(kv.denominator % P, P-2, P) % P
    spec[(len(els), rank_mod_p(K) if els else 0)] += 1
print("\nEVERY (dim, reductive) reachable by ANY subset:")
for (d, kr) in sorted(spec):
    tag = ""
    if (d, kr) == (12, 11): tag = "   <<<<<< su(3)+su(2)+u(1) >>>>>>"
    elif kr == 24: tag = "   <- su(5)"
    elif (d, kr) == (45, 45): tag = "   <- so(10)"
    elif (d, kr) == (8, 8): tag = "   <- su(3)"
    print(f"  dim {d:3d}  reductive {kr:3d}{tag}")
print(f"\nIS su(3)+su(2)+u(1) (12,11) REACHABLE?  {(12,11) in spec}")
print(f"does reductive rank 11 occur at all?      {any(kr==11 for _,kr in spec)}")
