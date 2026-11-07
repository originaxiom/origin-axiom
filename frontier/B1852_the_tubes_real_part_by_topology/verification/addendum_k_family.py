"""B1852's addendum (2026-11-07, S306l; the web seat's relay 991d7e2ac): the exact classes for the family L^6R(LR)^k,
k = 1..5, with SnapPy's systole lengths, and the covariant root of the energy form (algebra).
- classes: B1852's brute force (det -1 involutions reversing phi, entries up to 14) on each member;
- the systole: SnapPy's shortest geodesic's real length on b++L^6R(LR)^k (the web seat's table: 0.18486980, 0.18519963,
  0.18521766, 0.18521832, 0.18521828);
- the root: for E = [[E11, E12], [E12, E22]] the upper root of E22 t^2 + 2 E12 t + E11 is (-E12 + i sqrt(det E))/E22,
  covariant under E -> A E A^T (A in GL(2, Z)) and equal to (-E12 + i)/E22 iff det E = 1."""
import importlib.util, pathlib, warnings
warnings.filterwarnings("ignore")
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ffc", HERE / "fixed_fibre_classes.py")
src = (HERE / "fixed_fibre_classes.py").read_text()
ns = {}
exec(src.split("rows = []")[0], ns)                    # the definitions only, not the table
import snappy
out = []
for k in range(1, 6):
    w = "LLLLLLR" + "LR" * k
    n, pairs = ns["classes"](w)
    kind = "opposite classes" if pairs <= {(True, False), (False, True)} and pairs else ("both != I" if pairs == {(False, False)} else str(pairs))
    sys_len = None
    for how in ("plain", "canonize", "hp"):           # SnapPy's Dirichlet construction fails on some members' default triangulations
        try:
            M = snappy.ManifoldHP("b++" + w) if how == "hp" else snappy.Manifold("b++" + w)
            if how == "canonize": M.canonize()
            sys_len = float(M.length_spectrum(0.5)[0].length.real()); break
        except Exception:
            continue
    out.append("k = %d: %d reversing involutions, %s; systole %.8f" % (k, n, kind, sys_len))
E11, E12, E22 = sp.symbols("E11 E12 E22", real=True)
t = sp.symbols("t")
detE = E11 * E22 - E12 ** 2
root = (-E12 + sp.I * sp.sqrt(detE)) / E22
assert sp.simplify((E22 * root ** 2 + 2 * E12 * root + E11).subs({E11: 3, E12: 1, E22: 2})) == 0
a, b, c, d = 2, 1, 1, 1                                 # a GL(2, Z) change of basis
A = sp.Matrix([[a, b], [c, d]]); Em = sp.Matrix([[3, 1], [1, 2]]); Ep = A * Em * A.T
r = lambda M: (-M[0, 1] + sp.I * sp.sqrt(M.det())) / M[1, 1]
moved = sp.nsimplify(sp.simplify(r(Ep))); t0 = r(Em)
image = sp.nsimplify(sp.simplify((a * t0 - b) / (d - c * t0)))
assert sp.simplify(moved - image) == 0
out.append("covariant root: E = [[3,1],[1,2]] -> %s; A E A^T (A = [[2,1],[1,1]]) -> %s = the Mobius image t -> (a t - b)/(d - c t): HOLDS" % (sp.nsimplify(t0), moved))
print("\n".join(out))
# the per-centre rule's prediction (P-740): a sigma-fixed fibre at the middle of an EVEN run carries the class = I mod 2
# (Re 0), at the middle letter of an ODD run the class != I (Re 1/2); so two even-run centres give (True, True)
for w, want in (("LLRR", {(True, True)}), ("LLLLRR", {(True, True)}), ("LLRRRR", {(True, True)}), ("LLLRRR", {(False, False)})):
    n, pairs = ns["classes"](w)
    assert pairs == want, (w, pairs)
    print("%-8s %d reversing involutions, fixed-fibre classes %s: as the per-centre rule predicts" % (w, n, sorted(pairs)))
