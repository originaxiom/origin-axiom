"""B1700 (P-245): the Higgs's end data and FK10's unit.  No data.  W46's unit (n = 1 uniform unit at the cusp; B1641's
index -chi_{3/2+12n}(rho_T)) makes the weight-3/2 sections of rho_T (= rho_R, B1634) the space Delta^-1 M_{27/2}(rho_T)
with the canonical exponents.  Computed exactly (q-series in x = q^(1/8), B1691's module): the eigenline orders of R,
DR, D2R at the cusp; the canonical conditions on the free module's weight-27/2 piece; the dimension and a basis; whether
DR lies in it and which member is holomorphic on the two lines other than v+ (R's own end condition); and the
second-to-third hierarchy exponent at the cusp (B1691's census formula) for each basis member and generic members.
    python3 -B the_units_sheaf.py      # writes the_units_sheaf.json beside itself"""
import sys, io, json, contextlib, importlib.util, pathlib, random
from fractions import Fraction as F
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
P = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P))
spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
S = te.S; R, D1, D2 = te.B; e4, e6 = te.e4, te.e6
I = S.c(0, 1)
def lines(a):                       # the eigenlines of rho(T): P = a_i, M = a_j + i a_k, N = a_j - i a_k
    return a[0], a[1] + I * a[2], a[1] - I * a[2]
def sc(c, a): return [c * x for x in a]
def add(*vs): return [sum((v[i] for v in vs[1:]), vs[0][i]) for i in range(3)]
def coef(s, k): a, b = s.d.get(k, (F(0), F(0))); return sp.Rational(a.numerator, a.denominator) + sp.I * sp.Rational(b.numerator, b.denominator)
out = {}
out["line_orders_R"] = [x.ord() for x in lines(R)]; out["line_orders_DR"] = [x.ord() for x in lines(D1)]; out["line_orders_D2R"] = [x.ord() for x in lines(D2)]
Delta = (e4 * e4 * e4 - e6 * e6) * S.c(F(1, 1728))
out["Delta_order_x"] = Delta.ord()
cand = {"E4^2E6 R": sc(e4 * e4 * e6, R), "E4^3 DR": sc(e4 * e4 * e4, D1), "Delta DR": sc(Delta, D1), "E4E6 D2R": sc(e4 * e6, D2)}
names = list(cand)
# the canonical conditions at weight 27/2: line orders >= (1, 7, 3); list every coefficient below the bound
conds = []
for li, bound in ((0, 1), (1, 7), (2, 3)):
    ks = sorted({k for nm in names for k in lines(cand[nm])[li].d if k < bound})
    for k in ks: conds.append((li, k, [coef(lines(cand[nm])[li], k) for nm in names]))
out["conditions"] = [[li, k] for li, k, _ in conds]
A = sp.Matrix([row for _, _, row in conds]) if conds else sp.zeros(0, 4)
ker = A.nullspace(); out["dim_weight_27/2_canonical"] = len(ker)
basis = []
Dinv = Delta.inv()
for v in ker:
    a = [S() for _ in range(3)]
    for c, nm in zip(v, names):
        re, im = sp.nsimplify(sp.re(c)), sp.nsimplify(sp.im(c))
        a = add(a, sc(S.c(F(int(sp.fraction(re)[0]), int(sp.fraction(re)[1])), F(int(sp.fraction(im)[0]), int(sp.fraction(im)[1]))), cand[nm]))
    basis.append(sc(Dinv, a))
out["basis_kernel_vectors"] = [[str(c) for c in v] for v in ker]
out["basis_line_orders_weight_3/2"] = [[x.ord() for x in lines(b)] for b in basis]
# DR in the span? and the subspace holomorphic on the P and N lines (orders >= 1, >= 3)
out["Delta_DR_in_kernel"] = (A * sp.Matrix([0, 0, 1, 0])).is_zero_matrix if conds else True
rows = []
for li, bound in ((0, 1), (2, 3)):
    ks = sorted({k for b in basis for k in lines(b)[li].d if k < bound})
    for k in ks: rows.append([coef(lines(b)[li], k) for b in basis])
H = sp.Matrix(rows); hk = H.nullspace() if rows else [sp.eye(len(basis))[:, i] for i in range(len(basis))]
out["dim_holomorphic_on_P_and_N"] = len(hk)
if len(hk) == 1:
    v = hk[0]; comb = [S() for _ in range(3)]
    for c, b in zip(v, basis):
        re, im = sp.re(c), sp.im(c)
        comb = add(comb, sc(S.c(F(int(sp.fraction(re)[0]), int(sp.fraction(re)[1])), F(int(sp.fraction(im)[0]), int(sp.fraction(im)[1]))), b))
    # proportional to DR?
    k0 = D1[1].ord(); lam = coef(comb[1], k0) / coef(D1[1], k0)
    diff = [comb[i] - S.c(F(int(sp.fraction(sp.re(lam))[0]), int(sp.fraction(sp.re(lam))[1])), F(int(sp.fraction(sp.im(lam))[0]), int(sp.fraction(sp.im(lam))[1]))) * D1[i] for i in range(3)]
    out["the_P_N_holomorphic_member_is_DR"] = all(d.ord() is None or d.ord() > 120 for d in diff)
# the hierarchy exponents (B1691's cusp census formula) for each basis member and generic combinations
def m2m3(a): return te.cusp_exps(a)["m2/m3_exponent_in_|q|"]     # m1/m3 is not read here (truncation-limited for a.R)
out["m2/m3_exponent_DR"] = m2m3(D1)
out["m2/m3_exponent_basis"] = [m2m3(b) for b in basis]
rng = random.Random(245); gen = []
for _ in range(3):
    a = [S() for _ in range(3)]
    for b in basis: a = add(a, sc(S.c(F(rng.randint(-9, 9) or 1, rng.randint(1, 5)), F(rng.randint(-9, 9), rng.randint(1, 5))), b))
    gen.append(m2m3(a))
out["m2/m3_exponent_generic"] = gen
if __name__ == "__main__":
    json.dump(out, open(HERE / "the_units_sheaf.json", "w"), indent=1, default=str)
    for k, v in out.items(): print(k, v)
