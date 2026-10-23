"""B1741 post hoc read-outs (labelled; after the sealed comparison was read): the best row's line, its relation to the
thread at that apex (B1733's Smith rule: fixed up to sign by A, by A^2), its census-frame equivalent, the six's values
and pulls, D, |V_ud|; and the next-best rows below the bar."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
V = ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification"
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification")); import census as K
sys.path.insert(0, str(ROOT / "frontier" / "B1735_the_precision_bar_on_the_two_ingredient_censuses" / "verification")); import check
cmp = json.load(open(V / "comparison.json")); b6 = cmp["best_six"]["seat"]; print("best six (seat):", {k: b6[k] for k in b6 if k != "model_over_measured"})
L = K.lines(); a, b = L[b6["line"]]; N = math.lcm(a.denominator, b.denominator); print("line", b6["line"], (str(a), str(b)), "order", N)
th = json.load(open(ROOT / "frontier/B1720_the_thread_fixes_the_point/verification/the_thread_census.json"))
cls = [c for c in th["classes"] if abs(c["tau"][0] - b6["Re_tau"]) < 1e-9 and abs(c["tau"][1] - b6["Im_tau"]) < 1e-6]
for c in cls:
    A = c["A"]; A = [[A[0], A[1]], [A[2], A[3]]] if not isinstance(A[0], list) else A; own = [(str(Fr(x)), str(Fr(y))) for x, y in c["lines"]]
    def fixed(M, v):           # the line v = (a, b) as a row vector acted on by M^-1 (B1733's row convention), up to sign, mod 1
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]; Mi = [[M[1][1] * det, -M[0][1] * det], [-M[1][0] * det, M[0][0] * det]]
        w = ((v[0] * Mi[0][0] + v[1] * Mi[1][0]) % 1, (v[0] * Mi[0][1] + v[1] * Mi[1][1]) % 1)
        return w == (v[0] % 1, v[1] % 1) or w == ((-v[0]) % 1, (-v[1]) % 1)
    A2 = [[sum(A[i][k] * A[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    print("class", c["word"], "A", A, "| the line among its own lines:", (str(a), str(b)) in own, "| fixed by A:", fixed(A, (a, b)), "by A^2:", fixed(A2, (a, b)), "| own lines:", own[:12])
re0 = b6["Re_tau"] - math.floor(b6["Re_tau"]); n = math.floor(b6["Re_tau"]); bc = (b + n * a) % 1
print("census frame: tau", round(re0, 3), "+", round(b6["Im_tau"], 4), "i, line", (str(a), str(bc)), "| in B1726's list:", (a, bc) in L or ((-a) % 1, (-bc) % 1) in L)
v = json.load(open(ROOT / "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"))["masses_GeV"]["value"]
T = np.log([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]); sg = check.sigma()
mo = np.array(b6["model_over_measured"]); print("model/measured", np.round(mo, 3), "| pulls", np.round(np.log(mo) / sg, 2), "| chi2 %.2f" % float(((np.log(mo) / sg) ** 2).sum()))
rows = [json.loads(l) for l in open(V / "census.jsonl")]
r = [x for x in rows if x["line"] == b6["line"] and abs(x["Re_tau"] - b6["Re_tau"]) < 1e-9 and abs(x["Im_tau"] - b6["Im_tau"]) < 1e-6][0]
k = r["ckm|%s|St|S" % b6["horocycle"]]; print("|V_us|,|V_cb|,|V_ub| at the row", np.round(k[:3], 4), "|V_ud|", round(math.sqrt(max(0, 1 - k[0] ** 2 - k[2] ** 2)), 3), "J", k[3])
print("chi2 per menu:", {kk: (round(vv["min"], 2), vv["fraction_mean"]) for kk, vv in cmp["chi2"].items()})
