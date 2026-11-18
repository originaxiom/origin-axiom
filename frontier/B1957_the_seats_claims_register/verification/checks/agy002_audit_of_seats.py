"""B1957: agy-002's audit of the other seats' work in its closing note (relays/AGY002_MASTER_CLOSURE_SYNTHESIS_2026-11-16.md,
lines 45 to 62), the facts it rests on, tested by main (2026-11-18; data-free).  The other seat's checkers are read as
text at the commit agy-002 audited (80fdd90b2) and parsed, never run or imported.
 K1  agy-exp's fourth X-SYNTHESIS checker: how many names its literal scan covers, how many float literals the file holds
     and how many lie inside the scanned functions; the one-loop gauge coefficients; the second three-family copy and the
     block it enters; the calls at the typed-in point (4/15, 8/15).
 K2  its third checker's count of sections of a line bundle of negative degree: what the function returns.
 K3  with a second three-family copy coupled, the one-loop coefficients of SU(2) and SU(3); the shift of 1/alpha_3 over a
     logarithmic range t.
 K4  the set u1 v2 - u2 v1 = 0 in R^4: a path inside it between two of its points, and its energy when traversed at
     uniform speed over lengths 6, 12, 24, 48.
 K5  the twelve commits the note pins are commits of this repository."""
import ast, math, pathlib, subprocess
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
show = lambda c, p: subprocess.run(["git", "show", "%s:%s" % (c, p)], capture_output=True, text=True, cwd=ROOT).stdout
AUD = "80fdd90b2"
s4 = show(AUD, "relays/x_synthesis_4_verify/verify_x_synthesis_4.py"); s3 = show(AUD, "relays/x_synthesis_3_verify/verify_x_synthesis_3.py")
if not s4 or not s3: raise SystemExit("the seat's branch is not fetched here: nothing checked")
t = ast.parse(s4); funcs = [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]
scanned = next({e.value for e in n.value.elts} for n in ast.walk(t) if isinstance(n, ast.AnnAssign) and getattr(n.target, "id", "") == "TARGET_FREE_MODEL_FUNCTIONS")
floats = lambda node: sum(1 for x in ast.walk(node) if isinstance(x, ast.Constant) and isinstance(x.value, float))
L4 = s4.splitlines(); at = lambda pat: [i + 1 for i, l in enumerate(L4) if pat in l]
print("K1: names in the scanned set %d; functions defined in the file %d; float literals in the file %d, inside the scanned functions %d; one-loop coefficients at lines %s, %s, %s (41/10, -19/6, -7); the second copy integrated at line %s and placed in a block with zeros off the diagonal at line %s; calls at (4/15, 8/15): lines %s"
      % (len(scanned), len(funcs), floats(t), sum(floats(f) for f in funcs if f.name in scanned), at("k1_mp * F(41, 10)"), at("k1_mp * (-F(19, 6))"), at("k1_mp * (-7) * (g3 ** 3)"), at("fl_m = rk4_integrate_full_f64("), at('fl_m["Yu"] @ fl_m["Yd"]'), at("Fraction(4, 15), Fraction(8, 15)")))
f = next(n for n in ast.walk(ast.parse(s3)) if isinstance(n, ast.FunctionDef) and n.name == "h0_elliptic_jet_checked")
rets = [ast.unparse(r.value) for r in ast.walk(f) if isinstance(r, ast.Return)]; calls = [ast.unparse(c.func) for c in ast.walk(f) if isinstance(c, ast.Call)]
print("K2: the function h0_elliptic_jet_checked returns %s and calls %s: no contour integral is computed in it" % (rets, calls or "nothing"))
b2, b3 = Fr(-19, 6), Fr(-7); d = Fr(4, 3) * 3
print("K3: three more families add %s to each: SU(2) %s -> %s (positive), SU(3) %s -> %s; the shift of 1/alpha_3 over a range t is (4/(2 pi)) t = %.4f t, above 18 for t above %.2f" % (d, b2, b2 + d, b3, b3 + d, 4 / (2 * math.pi), 18 * 2 * math.pi / 4))
def path(s):          # rank-one matrices a b^T, from e1 e1^T to e2 e2^T
    th = s * math.pi / 2; a = np.array([math.cos(th), math.sin(th)]); return np.outer(a, a)
ss = np.linspace(0, 1, 4001); P = np.array([path(s) for s in ss]); dets = [abs(np.linalg.det(m)) for m in P]
E = {Lx: float(0.5 * (np.linalg.norm(np.diff(P, axis=0), axis=(1, 2)) ** 2).sum() / (Lx / 4000)) for Lx in (6, 12, 24, 48)}
print("K4: on the path the largest |u1 v2 - u2 v1| is %.1e; its energy at L = 6, 12, 24, 48: %s; E times L: %s" % (max(dets), ["%.5f" % E[k] for k in E], ["%.4f" % (E[k] * k) for k in E]))
pins = ["ec5678547", "599c59998", "af08bc3d2", "2ff7784b1", "001540efe", "a2185d1cf", "80fdd90b2", "3243ce870", "9e82adbe9", "844db35d0", "15c9504f4", "e250dab15"]
ok = [c for c in pins if subprocess.run(["git", "cat-file", "-e", c + "^{commit}"], cwd=ROOT).returncode == 0]
print("K5: pinned commits found: %d of %d" % (len(ok), len(pins)))
