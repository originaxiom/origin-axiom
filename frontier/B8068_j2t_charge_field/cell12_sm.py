"""AXIS 1b -- from su(5), can the object reach su(3)+su(2)+u(1)?

SEALED BEFORE READING:
  the SM algebra su(3)+su(2)+u(1) has dim 12 with SEMISIMPLE part 11 (su(3)+su(2)).
  So the signature to look for is (dim 12, Killing rank 11).
  dim 24 / rank 24 would be su(5) unbroken; anything else is reported as found.

Starting point: Stab(e_i, ebar_j, s) = dim 34, Killing rank 24 (cell 11, verified).
Then adjoin every remaining canonical element the object supplies and take all subsets.
"""
import os, sys, pathlib, itertools
import numpy as np, sympy as sp
from fractions import Fraction
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093
src = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "cell5_spinor_test.py")).read_text()
src = src.split('print("\\nSTABILISER')[0].replace(
    "PRIME = int(sys.argv[1]) if len(sys.argv) > 1 else 1093", f"PRIME = {PRIME}")
exec(compile(src, "c5", "exec"))
import e8_build as E

def act_any(s_arr, idx):
    rows = []
    for Xb in E6_BASIS:
        d = {E.N+E.IDX[(TWENTYSEVEN if idx is IDX27 else TWENTYSEVENBAR)[i2]]:
             Fraction(int(s_arr[i2]) % P) for i2 in range(27) if int(s_arr[i2]) % P}
        img = E.br(Xb, d); col = [0]*27
        for k, val in img.items():
            col[idx[E.ROOTS[k-E.N]]] = (val.numerator % P)*pow(val.denominator % P, P-2, P) % P
        rows.append(col)
    return np.array(rows, dtype=np.int64).T % P

def basis16(forms):
    S = [(Pm16 @ vec(embed_form(f, n, TWENTYSEVEN))) % P for f, n in forms]
    ind = []
    for s in S:
        T = np.array([[int(t) % P for t in u] for u in ind+[s]], dtype=np.int64)
        if rank_mod_p(T) > len(ind): ind.append(s)
    return ind

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
OM  = [(sp.expand(Psi**2), 8), (sp.expand(Phi**4), 16), (sp.expand(Wp*Psi**2), 16)]
OM2 = [(sp.expand(Phi**2), 8), (sp.expand(Psi**4), 16), (sp.expand(Wp*Phi**2), 16)]
ind = basis16(OM)
pure = []
for t in range(P):
    s = (ind[0] + t*ind[1]) % P
    if not np.count_nonzero(s): continue
    rows = [[int(z) % P for z in (A_.astype(object) @ s) % P] for A_ in ops]
    if 45 - rank_mod_p(np.array(rows, dtype=np.int64).T % P) == 34: pure.append(s)
print(f"pure spinors found: {len(pure)}", flush=True)
if not pure:
    print("none at this prime"); sys.exit(0)

# the canonical objects available
OBJ = []
for k, v in enumerate(g27): OBJ.append((f"e{k+1}", act(v, IDX27)))
for k, v in enumerate(gb):  OBJ.append((f"eb{k+1}", act(v, IDXBAR)))
OBJ.append(("s(pure)", act_any(pure[0], IDX27)))
# the omega and omega^2 covariants themselves (full vectors, not just 16-parts)
for nm, FS in (("w", OM), ("w2", OM2)):
    for i2, (f, n) in enumerate(FS):
        OBJ.append((f"{nm}{i2+1}", act(embed_form(f, n, TWENTYSEVEN), IDX27)))
print(f"canonical objects available ({len(OBJ)}): {[n for n,_ in OBJ]}", flush=True)
print(f"subsets to enumerate: 2^{len(OBJ)} - 1 = {2**len(OBJ)-1}", flush=True)

print("ALL SUBSETS -- looking for (dim 12, Killing rank 11) = su(3)+su(2)+u(1)", flush=True)
NSEEN=0
seen = defaultdict(list)
for r in range(1, len(OBJ)+1):
    for combo in itertools.combinations(range(len(OBJ)), r):
        M = np.vstack([OBJ[i][1] for i in combo]) % P
        d, kr = reductive_dim(M)
        seen[(d, kr)].append("+".join(OBJ[i][0] for i in combo)); NSEEN += 1
print(f"SUBSETS ACTUALLY ENUMERATED: {NSEEN}  (must equal 2^{len(OBJ)}-1 = {2**len(OBJ)-1})", flush=True)
assert NSEEN == 2**len(OBJ)-1, f"ACCOUNTING FAILURE: {NSEEN} != {2**len(OBJ)-1}"
for (d, kr) in sorted(seen):
    tag = ""
    if (d, kr) == (12, 11): tag = "   <<<<<< su(3)+su(2)+u(1) -- THE STANDARD MODEL ALGEBRA >>>>>>"
    elif kr == 24: tag = "   <- su(5)"
    elif (d, kr) == (45, 45): tag = "   <- so(10)"
    print(f"  dim {d:3d}  reductive {kr:3d}   ({len(seen[(d,kr)])} subsets){tag}")
