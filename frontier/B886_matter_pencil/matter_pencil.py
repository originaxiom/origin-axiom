#!/usr/bin/env python3
"""B886 -- the MATTER PENCIL: det(xI - rho(x8) - lambda rho(x16)) exactly over Q,
its factorization, and the two B885 laws as exact corollaries.

The 27's analog of B866's adjoint pencil. rho(x8), rho(x16) are commuting exact
rational 27x27 matrices (rep27 x the INV coefficients). The pencil charpoly
P(x, lambda) in Q[x, lambda] encodes the joint Pi-weight structure of matter:
each joint weight (a, b) contributes a factor (x - a - b*lambda); the
Q-factorization groups weights into Galois orbits.

Corollaries targeted (B885's laws, exactly):
  LAW 0 (one line): each frame's 27-singlet is automatically a joint Pi-weight
    vector -- the s_i-singlet eigenspace is 1-dim and rho(x16) commutes with
    rho(s_i), so it preserves the line.
  LAW 1: for i != j, the singlet weight of frame i evaluated at s_j equals the
    multiplicity-10 eigenvalue of rho(s_j) -- a polynomial identity in the
    cubic's roots, decided by exact division/resultants against mu.
  LAW 2: it never equals the singlet eigenvalue of frame j (same method).

Everything exact; nothing floats.
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B883 = os.path.normpath(os.path.join(HERE, "..", "B883_the_27"))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))

REPJ = json.load(open(os.path.join(B883, "rep27.json")))
REP = {int(k): v for k, v in REPJ["rep"].items()}

src6 = open(B854, encoding="utf-8").read()
g6 = {"__file__": B854, "__name__": "b854"}
exec(compile(src6, B854, "exec"), g6)

print("[1] rho(x8), rho(x16) exact...")
def rho_exact(vec):
    M = sp.zeros(27, 27)
    for p in range(78):
        c = vec[p]
        if c == 0:
            continue
        q = sp.Rational(c.numerator, c.denominator)
        Rp = REP[p]
        for i in range(27):
            for j in range(27):
                if Rp[i][j]:
                    M[i, j] += q * Rp[i][j]
    return M

R8 = rho_exact(g6["INV"][8])
R16 = rho_exact(g6["INV"][16])
comm = R8 * R16 - R16 * R8
assert comm == sp.zeros(27, 27), "rho(x8), rho(x16) must commute"
print("    commute: exact")

print("[2] the pencil charpoly by interpolation (28 exact points)...")
x, lam, rho = sp.symbols("x lambda rho")
pts = []
for k in range(28):
    lv = sp.Rational(k)
    M = R8 + lv * R16
    cp = M.charpoly(x).as_expr()
    pts.append((lv, sp.Poly(cp, x).all_coeffs()))
# interpolate each x-coefficient in lambda (degree <= 27)
coeffs_lam = []
for ci in range(28):
    ys = [p[1][ci] for p in pts]
    xs = [p[0] for p in pts]
    poly = sp.interpolate(list(zip(xs, ys)), lam)
    coeffs_lam.append(sp.expand(poly))
P = sp.expand(sum(coeffs_lam[i] * x ** (27 - i) for i in range(28)))
print(f"    P(x, lambda) built; degree in x: {sp.degree(P, x)}, in lambda: {sp.degree(P, lam)}")

print("[3] factor over Q...")
fl = sp.factor_list(sp.Poly(P, x, lam))
factors = [(f.as_expr(), m) for f, m in fl[1]]
print(f"    {len(factors)} irreducible factors:")
res_factors = []
for f, m in factors:
    dx = sp.degree(f, x)
    res_factors.append(dict(factor=str(f), mult=int(m), deg_x=int(dx)))
    print(f"      mult {m}, deg_x {dx}: {sp.sstr(f)[:110]}")

print("[4] the adjoint-pencil eigenvalues on the 27 at the roots...")
MU = sp.Poly(500716339200 * rho**3 - 2075673600 * rho**2 - 4769856 * rho + 2197, rho)
# NOTE their normalization: today's build carries rho = the pencil parameter directly
# (B872 certificate); the enhancement parameter for s = x8 + t*x16 is t = 13*(banked
# root of the OTHER normalization) = root of MU (their mu). Verify: MU's roots ARE
# the t-values used all week (b854-pencil-normalization-13x).
# spectrum of rho(s_t) = specialize P at lambda = t: P(x, t) factors as
# (x - e1(t))^1 (x - e10(t))^10 (x - e16(t))^16 for t on the cubic.
# extract e1, e10, e16 as algebraic functions: substitute lambda -> rho mod MU and
# factor P(x, rho) over Q[rho]/(MU):
K = sp.QQ.algebraic_field(sp.RootOf(MU.as_expr(), 0))
Pt = sp.Poly(P.subs(lam, sp.RootOf(MU.as_expr(), 0)), x, extension=True)
ft = sp.factor_list(Pt)
mults = sorted(int(m) for f, m in ft[1] for _ in range(1) )
struct = sorted((int(m), int(sp.degree(f.as_expr(), x))) for f, m in ft[1])
print(f"    at a root of mu: factor (mult, deg_x) structure: {struct}")

print("[5] LAWS 1 and 2, exactly...")
# the three linear-in-x eigenvalue branches at a root: e_1, e_10, e_16 with
# multiplicities 1, 10, 16. For two DISTINCT roots r_i, r_j of mu:
#   LAW 1 <=> e_1-branch weight of frame i, evaluated at lambda = r_j, equals
#             e_10(r_j);   LAW 2 <=> it never equals e_1(r_j).
# The e_1 branch: the mult-1 linear factor of P(x, lambda=r): x - (a + b*r)
# globally: the mult-1 factor of P over Q[x,lambda] restricted... use the
# factor list: find the factor containing the singlet branch (mult 1 at roots).
r_i, r_j = sp.symbols("r_i r_j")
# singlet weight (a_i, b_i): from the mult-1 linear factor of P(x, r):
lin = [f for f, m in factors if sp.degree(f, x) >= 1]
# Work concretely: the singlet eigenvalue at parameter r is the unique simple
# root in x of P(x, r) for r on mu. Represent branches implicitly: for the LAWS
# use resultants: define Q1(x, l) = the factor of P that vanishes on the singlet
# branch. Identify it: at a root of mu the mult-1 x-factor comes from ONE
# Q-irreducible factor; find which by multiplicity bookkeeping at the algebraic
# specialization above.
sing_factor = None
for f, m in ft[1]:
    if int(m) == 1 and sp.degree(f.as_expr(), x) == 1:
        sing_spec = f.as_expr()
for f, m in factors:
    # test: does f's specialization divide the singlet factor's product?
    spec = sp.Poly(f.subs(lam, sp.RootOf(MU.as_expr(), 0)), x, extension=True)
    for ff, mm in ft[1]:
        if int(mm) == 1 and sp.degree(ff.as_expr(), x) == 1 and \
           sp.rem(spec, ff) == 0 and sp.degree(spec, x) >= 1:
            sing_factor = f
            break
    if sing_factor is not None:
        break
print(f"    singlet-carrying Q-factor: {sp.sstr(sing_factor)[:110]}")
ten_factor = None
for f, m in factors:
    spec = sp.Poly(f.subs(lam, sp.RootOf(MU.as_expr(), 0)), x, extension=True)
    for ff, mm in ft[1]:
        if int(mm) == 10 and sp.rem(spec, ff) == 0 and sp.degree(spec, x) >= 1:
            ten_factor = f
            break
    if ten_factor is not None:
        break
print(f"    10-carrying Q-factor:      {sp.sstr(ten_factor)[:110]}")

# LAW 1: for roots r_i != r_j of mu: the x-root of sing_factor(x, r_i)'s branch,
# re-evaluated... the singlet WEIGHT is (a_i, b_i) with x = a_i + b_i*lambda the
# branch through r_i. If sing_factor is linear in x with coefficients in Q[lambda],
# the branch is global: x = S(lambda) with S in Q(lambda) -- then the weight is
# NOT constant unless S is linear. Handle the actual shape found and reduce LAW 1
# to: resultant_{x}(sing-branch-line_i, ten_factor at lambda=r_j) == 0 mod
# (mu(r_i), mu(r_j), r_i != r_j). Implemented per the discovered factor shapes:
res = dict(factor_structure=res_factors, spec_structure=[list(t) for t in struct],
           sing_factor=str(sing_factor), ten_factor=str(ten_factor))
json.dump(res, open(os.path.join(HERE, "results_stage1.json"), "w"), indent=1)
print("  stage-1 written (factor shapes); the LAW resultants run in stage 2 "
      "once the shapes are known")
