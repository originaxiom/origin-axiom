"""AXIS 1 -- does the chain COMPOSE?  One annihilator, not two chained results.

Stab_{e6}( e_i , ebar_j , s )  where e_i, ebar_j are the trivial-character idempotents
that produce the so(10), and s is the omega-covariant PURE SPINOR found on that so(10).

SEALED EXPECTATION (declared here, before the number is read):
  the pure spinor lives inside the so(10)'s 16, so its e6-stabiliser must be exactly the
  so(10)-stabiliser of s:  dim 34, Killing rank 24 = su(5).
  Anything else means the two steps do not compose and the chain is an illusion.

CONTROL, run first: the su(5) control from cell3 must pass in this same process.
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

def basis16(forms):
    S = [(Pm16 @ vec(embed_form(f, n, TWENTYSEVEN))) % P for f, n in forms]
    ind = []
    for s in S:
        T = np.array([[int(t) % P for t in u] for u in ind + [s]], dtype=np.int64)
        if rank_mod_p(T) > len(ind):
            ind.append(s)
    return ind

OM = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
ind = basis16(OM)
print(f"\nomega 16-parts span dimension {len(ind)}")

# locate the pure spinors on the line
pure = []
for t in list(range(P)) + [None]:
    s = (ind[0] + t*ind[1]) % P if t is not None else ind[1] % P
    if not np.count_nonzero(s):
        continue
    rows = [[int(z) % P for z in (A_.astype(object) @ s) % P] for A_ in ops]
    if 45 - rank_mod_p(np.array(rows, dtype=np.int64).T % P) == 34:
        pure.append((t, s))
print(f"pure-spinor points on the line: {len(pure)}  at t = {[t for t,_ in pure]}")
if not pure:
    print("NO PURE SPINOR AT THIS PRIME -- axis 1 not testable here.")
    sys.exit(0)

# the two idempotents that made the so(10)
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

g27 = idem(V27, POP27, QOP27, IDX27); gb = idem(VBAR, POPBAR, QOPBAR, IDXBAR)
pair = None
for v in g27:
    for w in gb:
        M = np.vstack([act(v, IDX27), act(w, IDXBAR)]) % P
        if reductive_dim(M) == (45, 45): pair = (v, w, M); break
    if pair: break
v, w, Mpair = pair
print(f"so(10) pair recovered: dim/Killing = {reductive_dim(Mpair)}")

print("\nTHE COMPOSITION -- one annihilator over all three objects")
for t, s in pure:
    # action of ALL of e6 on the pure spinor (not just the so(10))
    rows = []
    for Xb in E6_BASIS:
        img = E.br(Xb, {E.N+E.IDX[TWENTYSEVEN[i2]]: Fraction(int(s[i2]) % P)
                        for i2 in range(27) if int(s[i2]) % P})
        col = [0]*27
        for k, val in img.items():
            col[IDX27[E.ROOTS[k-E.N]]] = (val.numerator % P)*pow(val.denominator % P, P-2, P) % P
        rows.append(col)
    Ms = np.array(rows, dtype=np.int64).T % P
    Mall = np.vstack([act(v, IDX27), act(w, IDXBAR), Ms]) % P
    d, kr = reductive_dim(Mall)
    print(f"  t={t}: Stab_e6(e_i, ebar_j, s) = dim {d}, Killing rank {kr}"
          + ("   <<< su(5), THE CHAIN COMPOSES >>>" if kr == 24 else "   <-- does NOT compose"))
