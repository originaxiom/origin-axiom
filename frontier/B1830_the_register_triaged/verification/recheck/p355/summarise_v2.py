"""P-355 item 1: summarise identity_lines_v2's two runs (two tau, two seeds); require the two to agree point by point.
Writes ../register_triage/recheck/p355_item1.txt (the register note) and p355_item1_short.txt (the changelog line)."""
import collections, json, pathlib
from fractions import Fraction as F
HERE = pathlib.Path(__file__).resolve().parent
runs = [json.loads((HERE / ("identity_v2_%s.json" % t)).read_text()) for t in ("tauA", "tauBp")]
TOL = 1e-9
def cls(r):
    k = "T" if r["res_T"] < TOL else "P" if r["res_P"] < TOL else "-"
    s = "all" if r["dev_any"] < TOL else "noQI" if r["dev_noQI"] < TOL else "split"
    return k + "/" + s
table = {}
for run in runs:
    for p in run["points"]:
        for ri in ("r0", "r1"):
            table.setdefault(p["pt"], set()).add((p["order"], cls(p[ri])))
disagree = {k: v for k, v in table.items() if len(v) != 1}
print("points", len(table), "; disagreeing across tau/radius:", len(disagree), sorted(disagree.items())[:6])
by = collections.Counter(next(iter(v)) for k, v in table.items() if k not in disagree)
for k in sorted(by): print(k, by[k])
def pt(s):
    a, b = s.split(","); return F(a), F(b)
noqi = sorted((pt(k) for k, v in table.items() if next(iter(v))[1].endswith("noQI")))
# the pattern: (alpha, 2 beta) lies on an identity line (N | 4 or 5) while (alpha, beta) does not
ident = {pt(k) for k, v in table.items() if next(iter(v))[1].endswith("all")}
lift = [p for p in noqi if ((p[0], (2 * p[1]) % 1) in ident)]
print("noQI points:", len(noqi), "; of them beta-half-lifts of an identity point:", len(lift))
others = [p for p in noqi if p not in lift]
print("noQI not a beta-lift:", others[:10])
# all beta-half-lifts of identity points that are NOT identity points themselves: are they all noQI?
cand = {(a, (b + F(1, 2) * s) % 1) for (a, b) in ident for s in (0,)}  # placeholder
halves = set()
for (a, b) in ident:
    for c in (b / 2, b / 2 + F(1, 2)):
        q = (a, c % 1)
        if q not in ident: halves.add(q)
covered = [q for q in halves if q in set(noqi)]
print("beta-half-lifts of identity points (not identity):", len(halves), "; noQI among them:", len(covered))
m_any = min(min(p[ri]["dev_any"] for ri in ("r0", "r1")) for run in runs for p in run["points"] if cls(p["r0"]).endswith("split"))
m_q = min(min(p[ri]["dev_noQI"] for ri in ("r0", "r1")) for run in runs for p in run["points"] if cls(p["r0"]).endswith("split"))
mx = max(max(p[ri]["res_T"] if cls(p[ri])[0] == "T" else p[ri]["res_P"] if cls(p[ri])[0] == "P" else 0 for ri in ("r0", "r1")) for run in runs for p in run["points"])
print("split margins: any-Higgs >= %.3f, QI-free >= %.4f; identity residual max %.1e" % (m_any, m_q, mx))
json.dump(dict(by={"%s %s" % k: v for k, v in by.items()}, disagree=len(disagree), noqi=len(noqi), lifts=len(lift),
               halves=len(halves), covered=len(covered), m_any=m_any, m_q=m_q, res_max=mx),
          open(HERE / "summary_v2.json", "w"), indent=1)
