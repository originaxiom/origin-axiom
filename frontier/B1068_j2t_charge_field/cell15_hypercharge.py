"""AXIS 1c -- the MISSING OPERATION CLASS.

Every object in the lattice sweep was a VECTOR in the 27 / 27-bar, and every operation
was a STABILISER.  But SU(5) -> SM is a CENTRALISER of an element of the ADJOINT -- the
object's own measurement operation, the one the paper computes in check_global_form.py
with Y = diag(2,2,2,-3,-3)/6.

So: take the su(5) reached by (idempotents + pure spinor), and intersect it with the
centraliser of elements of the charge algebra C = <x8, x14, x16, x22> inside e6.

SEALED: su(3)+su(2)+u(1) is (dim 12, Killing rank 11).  Report every (dim, reductive)
reached, and state explicitly whether 11 occurs under this MIXED operation class.
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
    C_ = restricted(Vd, Pp_, Qq); D = sp.expand(C_/sp.Poly(C_, a, b, c).coeff_monomial(a**3))
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

OM = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
g27 = idem(V27, POP27, QOP27, IDX27); gb = idem(VBAR, POPBAR, QOPBAR, IDXBAR)
S = [(Pm16@vec(embed_form(f, n, TWENTYSEVEN)))%P for f, n in OM]
ind = []
for s_ in S:
    T = np.array([[int(t)%P for t in u] for u in ind+[s_]], dtype=np.int64)
    if rank_mod_p(T) > len(ind): ind.append(s_)
pure = []
for t in range(P):
    s_ = (ind[0]+t*ind[1])%P
    if not np.count_nonzero(s_): continue
    rws = [[int(z)%P for z in (A_.astype(object)@s_)%P] for A_ in ops]
    if 45-rank_mod_p(np.array(rws, dtype=np.int64).T%P) == 34: pure.append(s_)
print(f"pure spinors: {len(pure)}", flush=True)

def act_arr(s_arr, blk, idx):
    rows = []
    for Xb in E6_BASIS:
        d = {E.N+E.IDX[blk[i2]]: Fraction(int(s_arr[i2])%P) for i2 in range(27) if int(s_arr[i2])%P}
        img = E.br(Xb, d); col = [0]*27
        for k, val in img.items():
            col[idx[E.ROOTS[k-E.N]]] = (val.numerator%P)*pow(val.denominator%P, P-2, P)%P
        rows.append(col)
    return np.array(rows, dtype=np.int64).T%P

# the su(5) from the composed chain
base = None
for v in g27:
    for w in gb:
        M = np.vstack([act(v, IDX27), act(w, IDXBAR)])%P
        if reductive_dim(M) == (45, 45):
            M2 = np.vstack([M, act_arr(pure[0], TWENTYSEVEN, IDX27)])%P
            if reductive_dim(M2) == (34, 24): base = M2; break
    if base is not None: break
print(f"su(5) base recovered: {reductive_dim(base)}", flush=True)

# the charge algebra C inside e6 -- the ADJOINT elements the paper measures with
# x8,x14,x16,x22 are the 2T-invariants of e6 ITSELF (the adjoint), built via the
# principal sl2 acting on e6 -- these are the paper's charge algebra C.
def hw_e6(n):
    cands = [r for r in E6_ROOTS if int(list(E.br(h, E.ev(r)).values())[0] if E.br(h, E.ev(r)) else 0) == n]
    M = sp.zeros(E.DIM, len(cands))
    for j, r in enumerate(cands):
        for k, val in E.br(ee, E.ev(r)).items(): M[k, j] = sp.Rational(val.numerator, val.denominator)
    ns = M.nullspace()
    if not ns: return None
    v = {}
    for j, r in enumerate(cands):
        co = sp.Rational(ns[0][j])
        if co: v = E.vadd(v, {E.N+E.IDX[r]: Fr(co)})
    return v
x_, y_ = sp.symbols('x y')
tf = x_**5*y_ - x_*y_**5; Wf = x_**8 + 14*x_**4*y_**4 + y_**8
ADJ_FORMS = {8: Wf, 14: sp.expand(tf*Wf), 16: sp.expand(Wf**2), 22: sp.expand(tf*Wf**2)}
Cbasis = {}
for n in (8, 14, 16, 22):
    top = hw_e6(n)
    if top is None: continue
    Pp = sp.Poly(ADJ_FORMS[n], x_, y_); acc, cur = {}, top
    for k in range(n+1):
        co = Pp.coeff_monomial(x_**(n-k)*y_**k)
        if co: acc = E.vadd(acc, E.vmul(Fr(sp.Rational(co)*sp.factorial(n-k)/sp.factorial(n)), cur))
        cur = E.br(ff, cur)
    Cbasis[n] = acc
print(f"charge algebra C rebuilt in the adjoint: degrees {sorted(Cbasis)}", flush=True)

# now: su(5) INTERSECT centraliser of c, for c ranging over C
ns0 = nullspace(base); els0 = []
for vv in ns0:
    xx = {}
    for co, Xb in zip(vv, E6_BASIS):
        if co % P: xx = E.vadd(xx, E.vmul(Fraction(int(co)%P), Xb))
    els0.append(xx)
print(f"su(5)-carrying algebra: dim {len(els0)}", flush=True)

def kill_rank(els):
    K = np.zeros((len(els), len(els)), dtype=np.int64)
    for r1, z1 in enumerate(els):
        for r2, z2 in enumerate(els):
            kv = E.killing_pair(z1, z2); K[r1, r2] = (kv.numerator%P)*pow(kv.denominator%P, P-2, P)%P
    return rank_mod_p(K) if els else 0

spec = Counter()
degs = sorted(Cbasis)
# EXHAUSTION, not sampling.  The previous run used range(3)^4 = 81 points out of ~p^4.
# The centraliser depends only on the LINE through c, so the object to sweep is P^3(F_p).
# That is p^3+p^2+p+1 points -- too many at p=1093 -- so: sweep the full projective space
# of the (x8,x16) measurement plane and the (x14,x22) odd plane exhaustively (p+1 each),
# every coordinate 2-plane, plus a large random sample of the full P^3.
import random
random.seed(20260817)
CAND = []
for i in range(len(degs)):
    for j in range(len(degs)):
        if i >= j: continue
        for t in range(P):
            v = [0]*len(degs); v[i] = 1; v[j] = t; CAND.append(tuple(v))
        v = [0]*len(degs); v[j] = 1; CAND.append(tuple(v))
for _ in range(4000):
    CAND.append(tuple(random.randrange(P) for _ in degs))
CAND = [c for c in set(CAND) if any(c)]
print(f"charge directions to test: {len(CAND)}  "
      f"(all 6 coordinate 2-planes exhaustively + 4000 random points of P^3)", flush=True)
for coeffs in CAND:
    if not any(coeffs): continue
    cel = {}
    for co, n in zip(coeffs, degs):
        if co: cel = E.vadd(cel, E.vmul(Fraction(co), Cbasis[n]))
    rows = []
    for z in els0:
        br_ = E.br(cel, z)
        rows.append([(br_.get(k, Fraction(0)).numerator % P)*pow(br_.get(k, Fraction(0)).denominator % P, P-2, P) % P
                     for k in range(E.DIM)])
    Rm = np.array(rows, dtype=np.int64).T % P
    ker = nullspace(Rm)
    sub = []
    for vv in ker:
        xx = {}
        for co, z in zip(vv, els0):
            if co % P: xx = E.vadd(xx, E.vmul(Fraction(int(co)%P), z))
        sub.append(xx)
    spec[(len(sub), kill_rank(sub))] += 1
print(f"\nsu(5) INTERSECT centraliser of c, over {len(CAND)} directions in C:")
for (d, kr) in sorted(spec):
    tag = "   <<<<<< su(3)+su(2)+u(1) >>>>>>" if (d, kr) == (12, 11) else ("   <- su(5)" if kr == 24 else "")
    print(f"  dim {d:3d}  reductive {kr:3d}   ({spec[(d,kr)]} directions){tag}")
print(f"\nIS (12,11) REACHED?  {(12,11) in spec}")
print(f"does reductive rank 11 occur? {any(kr==11 for _,kr in spec)}")
