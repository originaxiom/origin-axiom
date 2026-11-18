"""B1957: the physical lane's review of main's records of its lane (its findings M9-01 to M9-05) and its own support note
for the inverse on the cusp, the parts main can decide by its own computation (2026-11-18; data-free; nothing of the lane's
is run; one of its receipts is read as data).
 N1  M9-01: L_c exp(-delta t) for L_c = ell^-2 (-d^2/dt^2 + d/dt) + c, and the lane's control at ell = 2, c = 1, delta = 1/2.
 N2  M9-04: the lane's two engineering receipts at its pin: how many checks each ran and whether a scientific checker ran.
 N3  M9-05: main's key-coverage account (the counts of physical_outputs_key_coverage_run.txt).
 N4  its support note, section 3: the dimensions of its compact roster and the number of trivial summands.
 N5  its support note, section 4: (a + b)^2 - a^2/2 + b^2 as a square; and, for b(t) = exp(-(delta + 2) t) and t beyond the T
     of its condition (5), L b - (nu^2/(4 ell^2)) exp(-delta t) as a sum of non-negative terms.
 N6  its formula (9) at c = 0: the derivative and the constant-plus-decay form, with the factor ell^2."""
import json, pathlib, re, subprocess
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
show = lambda c, p: subprocess.run(["git", "show", "%s:%s" % (c, p)], capture_output=True, text=True, cwd=ROOT).stdout
t, ell, c, d, M, nu, w, m = sp.symbols("t ell c delta M nu w m", positive=True)
Lc = lambda u: (-sp.diff(u, t, 2) + sp.diff(u, t)) / ell ** 2 + c * u
k = sp.simplify(Lc(sp.exp(-d * t)) / sp.exp(-d * t)); num = {ell: 2, c: 1, d: sp.Rational(1, 2)}
print("N1: L_c exp(-delta t) = (%s) exp(-delta t); at ell = 2, c = 1, delta = 1/2 the factor is %s, so the source M exp(-t/2) has the particular solution (%s) M exp(-t/2); the lane says 13/16 and 16/13" % (sp.factor(k), k.subs(num), (1 / k).subs(num)))
D = "reports/physical_bridge_2026_09_05/registered_domain_index_join_2026_11_16/verification/engineering_results/"
for name in ("RECEIPT.json", "REPEAT_RECEIPT.json"):
    raw = show("8d5c91032", D + name)
    if not raw: print("N2: %s: the lane's branch is not fetched here" % name); continue
    r = json.loads(raw); flat = json.dumps(r)
    print("N2: %s at the lane's pin: keys %s; scientific_tests_run = %s; scientific_checker_imported = %s; numbers of tests it records: %s"
          % (name, sorted(r)[:12], r.get("scientific_tests_run"), r.get("scientific_checker_imported"), re.findall(r'"(?:tests_run|engineering_tests_run|tests)"\s*:\s*(\d+)', flat)[:4]))
cov = (HERE / "physical_outputs_key_coverage_run.txt").read_text().split("\n")
print("N3: %s" % "; ".join(l for l in cov if "leaf keys" in l))
roster = [((0, 0), 1), ((1, 0), 1), ((3, 0), 1), ((0, 1), 1), ((0, 3), 1), ((2, 2), 1), ((sp.Rational(3, 2), sp.Rational(3, 2)), 2)]
dims = [n * (2 * a + 1) * (2 * b + 1) for (a, b), n in roster]
print("N4: the roster's dimensions %s sum to %s; trivial summands: %d" % (dims, sum(dims), sum(n for (a, b), n in roster if (a, b) == (0, 0))))
a, b = sp.symbols("a b", real=True)
print("N5: (a + b)^2 - a^2/2 + b^2 = %s, a square: %s" % (sp.factor((a + b) ** 2 - a ** 2 / 2 + b ** 2), sp.simplify((a + b) ** 2 - a ** 2 / 2 + b ** 2 - (a / sp.sqrt(2) + sp.sqrt(2) * b) ** 2) == 0))
A = d + 2; bt = sp.exp(-A * t); V = (nu * sp.exp(t) + w / 2) ** 2
Lb = ((-sp.diff(bt, t, 2) + sp.diff(bt, t)) + V * bt) / ell ** 2 + m ** 2 * bt
rest = sp.simplify((Lb - nu ** 2 / (4 * ell ** 2) * sp.exp(-d * t)) / bt * ell ** 2)        # must be >= 0 beyond T
split = sp.expand(rest - ((V - nu ** 2 * sp.exp(2 * t) / 2 + w ** 2 / 4) + (nu ** 2 * sp.exp(2 * t) / 4 - w ** 2 / 4 - A ** 2 - A) + ell ** 2 * m ** 2))
print("N5: ell^2 (L b - (nu^2/(4 ell^2)) exp(-delta t))/b = [V - nu^2 e^(2t)/2 + w^2/4] + [nu^2 e^(2t)/4 - w^2/4 - a^2 - a] + ell^2 m^2 with a = delta + 2: %s; the first bracket is the square above, the second is non-negative beyond the T of the lane's (5), the third is non-negative" % (sp.simplify(split) == 0))
s = sp.Symbol("s", positive=True); up = ell ** 2 * sp.exp(t) * sp.integrate(sp.exp(-s) * sp.exp(-d * s), (s, t, sp.oo))
chk = sp.simplify((-sp.diff(up, t) + up) / ell ** 2 - sp.exp(-d * t))        # u' = up solves ell^-2 (-u'' + u') = exp(-delta t)
print("N6: at c = 0, u' = %s solves the equation (residual %s), and u - a = %s: the lane's (9), with the factor ell^2" % (sp.simplify(up), chk, sp.simplify(-sp.integrate(up.subs(t, s), (s, t, sp.oo)))))
