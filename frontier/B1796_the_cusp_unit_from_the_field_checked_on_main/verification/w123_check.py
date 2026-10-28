"""Main's own check of the SM seat's W123 (P-288), with B1691's module (main's code; no seat code read): for n uniform
units of end data at the cusp, the weight-3/2 sections of rho_T (= rho_R) are Delta^-n M_{3/2+12n}(rho_T) with the
canonical exponents, i.e. f0 R + f1 DR + f2 D2R with f0 in M_{2+12n}, f1 in M_{12n}, f2 in M_{12n-2} and eigenline orders
>= (1, 7, 3) on (P, M, N) in x = q^(1/8) (B1700's conventions).  The dimension for n = 0..4, exactly; and the count
(3n + 1 candidates, one condition: the x^-1 coefficient on M) that gives 3n for every n.
    python3 -B w123_check.py"""
import sys, io, contextlib, importlib.util, pathlib
from fractions import Fraction as F
import sympy as sp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
P = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
sys.path.insert(0, str(P))
spec = importlib.util.spec_from_file_location("te", P / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
S = te.S; R, D1, D2 = te.B; I = S.c(0, 1)
def lines(a): return a[0], a[1] + I * a[2], a[1] - I * a[2]
def sc(c, a): return [c * x for x in a]
def coef(s, k): a, b = s.d.get(k, (F(0), F(0))); return sp.Rational(a.numerator, a.denominator) + sp.I * sp.Rational(b.numerator, b.denominator)
def Mb(w): return te.Mbasis(w) if w >= 0 else []
print("line orders R, DR, D2R:", [[x.ord() for x in lines(v)] for v in (R, D1, D2)])
res = {}
for n in range(0, 5):
    cand = [sc(f, R) for f in Mb(2 + 12 * n)] + [sc(f, D1) for f in Mb(12 * n)] + [sc(f, D2) for f in Mb(12 * n - 2)]
    conds = []
    for li, bound in ((0, 1), (1, 7), (2, 3)):
        ks = sorted({k for c in cand for k in lines(c)[li].d if k < bound})
        for k in ks: conds.append(((li, k), [coef(lines(c)[li], k) for c in cand]))
    A = sp.Matrix([row for _, row in conds]) if conds else sp.zeros(0, len(cand))
    d = len(cand) - (A.rank() if conds else 0)
    res[n] = d
    print("n = %d: candidates %d (M_%d, M_%d, M_%d: %d + %d + %d), conditions at %s, rank %d -> dim %d (3n = %d)" % (
        n, len(cand), 2 + 12 * n, 12 * n, 12 * n - 2, len(Mb(2 + 12 * n)), len(Mb(12 * n)), len(Mb(12 * n - 2)),
        [c for c, _ in conds], A.rank() if conds else 0, d, 3 * n))
# the general count: dim M_{12n+2} = n, dim M_{12n} = n + 1, dim M_{12n-2} = n (n >= 1); on M the series has only powers
# = 7 mod 8 (the eigenvalue), so the one condition below 7 is the x^-1 coefficient, and it has rank one (DR E4^{3n} has it)
gen = all(len(Mb(2 + 12 * n)) == n and len(Mb(12 * n)) == n + 1 and len(Mb(12 * n - 2)) == (n if n >= 1 else 0) for n in range(0, 12))
mod8 = all(all((k - 7) % 8 == 0 for k in lines(v)[1].d) for v in (R, D1, D2))
print("dimension formulas hold for n = 0..11:", gen, "| M-line powers all = 7 mod 8 for R, DR, D2R:", mod8)
print("W123 (dim = 3n) holds for n = 0..4:", all(res[n] == 3 * n for n in res))
print("w123_check exit 0")


# ---- per-line end data: m = (m_P, m_M, m_N) units on each eigenline; orders >= (1, 7, 3) - 8m; built at weight 3/2 + 12N
def d_of(m):
    N = max(0, max(m))
    cand = [sc(f, R) for f in Mb(2 + 12 * N)] + [sc(f, D1) for f in Mb(12 * N)] + [sc(f, D2) for f in Mb(12 * N - 2)]
    bounds = [b + 8 * (N - mi) for b, mi in zip((1, 7, 3), m)]          # on the weight 3/2 + 12N piece (Delta^N shifts 8N)
    conds = []
    for li in range(3):
        ks = sorted({k for c in cand for k in lines(c)[li].d if k < bounds[li]})
        for k in ks: conds.append([coef(lines(c)[li], k) for c in cand])
    A = sp.Matrix(conds) if conds else sp.zeros(0, len(cand))
    return len(cand) - (A.rank() if conds else 0)
import itertools, json
table = {str(m): d_of(m) for m in itertools.product((-1, 0, 1, 2), repeat=3)}
seat_f = pathlib.Path(__file__).resolve().parent / "seat_the_higgs_route_exact.json"      # the seat's output, read as data (its code not read)
seat = json.loads(seat_f.read_text(encoding="utf-8"))["d at N = 3"]
key = lambda m: "(%d, %d, %d)" % m
agree = [m for m in itertools.product((-1, 0, 1, 2), repeat=3) if seat.get(key(m)) == table[str(m)]]
print("per-line table: 64 entries; main's d(m) = max(0, sum m) for all:", all(table[str(m)] == max(0, sum(m)) for m in itertools.product((-1, 0, 1, 2), repeat=3)))
print("agreement with the seat's output (its 'd at N = 3', read as data; the formula is symmetric, so the slot order does not matter):", len(agree), "of 64")
print("one unit on one line: d(1,0,0), d(0,1,0), d(0,0,1) =", table[str((1, 0, 0))], table[str((0, 1, 0))], table[str((0, 0, 1))], "| uniform: d(1,1,1) =", table[str((1, 1, 1))])
print("w123_check per-line exit 0")
