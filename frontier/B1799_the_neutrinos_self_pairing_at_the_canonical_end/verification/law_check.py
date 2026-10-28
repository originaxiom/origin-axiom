"""B1799: the Dirac sector L nu^c's exact zeros against B1716's law (left twist -3w of exact order 4, right twist 0 of order
1), row by row; the slope-2/5 lines; reads majorana_rows.jsonl only.
    python3 -B law_check.py"""
import json, math, pathlib
from fractions import Fraction as Fr
HERE = pathlib.Path(__file__).resolve().parent
rows = [json.loads(l) for l in (HERE / "majorana_rows.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
def order(q, a, b):
    qa, qb = (q * Fr(a)) % 1, (q * Fr(b)) % 1; return math.lcm(qa.denominator, qb.denominator)
agree = dis = 0; zl = set(); bad = []
for r in rows:
    pred = order(-3, r["a"], r["b"]) == 4 and order(0, r["a"], r["b"]) <= 2
    z = r["Lnuc"]["Dn"] < 1e-10
    if z: zl.add((r["a"], r["b"]))
    if z == pred: agree += 1
    else: dis += 1; bad.append((r["a"], r["b"], r["point"], r["Lnuc"]["Dn"]))
print("Dirac L nu^c: exact zeros on %d lines; B1716's law (left twist -3w of exact order 4) agrees on %d of %d rows, disagrees on %d %s" % (len(zl), agree, agree + dis, dis, bad[:3]))
six = [r for r in rows if r["a"] == "2/5"]
print("slope-2/5 lines: Dirac exact zeros on %d rows of %d; LL min Dn %.2e; nucnuc min Dn %.2e" % (sum(r["Lnuc"]["Dn"] < 1e-10 for r in six), len(six), min(r["LL"]["Dn"] for r in six), min(r["nucnuc"]["Dn"] for r in rows if "nucnuc" in r)))
nz = [r["Lnuc"]["Dn"] for r in rows if r["Lnuc"]["Dn"] >= 1e-10]
print("Dirac non-zero rows: least Dn %.2e" % min(nz))
print("law_check exit 0")
