"""B1788 after its referee (data-free): the closed form's domain and the honest count.
(1) The excluded pairs: a line-sector where a theta constant vanishes exactly (q alpha in {0, 1/2} mod 1 with 2 q b = 1/2 mod
    1, for q_L or q_R: X0(0) or X1(0) is then identically zero and the block exponents E_ij do not apply).
(2) The tropical prediction (tropical.predict) against the closed form 1/2 - (||2 q_L a|| + ||2 q_R a||)/2 on every slope,
    sector and reading of B1785's census.
(3) The agreement with B1785's window fits on the domain (torsion degeneracy and excluded pairs apart), m2/m3 and m1/m3
    separately, and the failing m2/m3 classes (slope, sector, reading) with their case counts.
(4) Where (e_up, e_down) = (3/10, 1/5) over alpha with denominator <= 800 (the closed form, exact).
Writes domain.json."""
import json, pathlib
from fractions import Fraction as Fr
from collections import Counter, defaultdict
import tropical as T, classify as C
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HERE = pathlib.Path(__file__).resolve().parent


def closed(ql, qr, a):
    return Fr(1, 2) - (T.nd(2 * ql * a) + T.nd(2 * qr * a)) / 2


def zero_theta(a, b, q):
    return (q * a) % Fr(1, 2) == 0 and (2 * q * b - Fr(1, 2)) % 1 == 0


if __name__ == "__main__":
    P = {rd: T.polys(rd) for rd in ("S", "St")}
    d = json.load(open(ROOT / "frontier/B1785_the_slope_sets_the_exponents/verification/exponents.json"))
    excluded, mism, tally = [], 0, Counter(); fail_cls = defaultdict(int); ncases = 0
    for r in d:
        a, b = Fr(r["alpha"]), Fr(r["b"])
        for sec, (lf, rf) in T.SECTORS.items():
            ql, qr = T.SIXY[lf], T.SIXY[rf]; mu = T.E(ql * a, qr * a)
            for rd in ("S", "St"):
                e2, e3 = T.predict(P[rd], mu); ncases += 1
                if e2 != closed(ql, qr, a): mism += 1
            if C.torsion_deg(a, b, ql, qr): tally["degenerate (B1716)"] += 4; continue
            if zero_theta(a, b, ql) or zero_theta(a, b, qr): excluded.append((r["alpha"], r["b"], sec)); tally["excluded (a theta constant zero)"] += 4; continue
            for rd in ("S", "St"):
                e2, e3 = T.predict(P[rd], mu)
                for nm, pe in (("m2/m3", e2), ("m1/m3", e3)):
                    obs = r["%s|L_max|%s|%s" % (sec, rd, nm)]["exponent"]; ok = abs(obs - float(pe)) <= 0.05
                    tally["%s %s" % (nm, "agree" if ok else "differ")] += 1
                    if nm == "m2/m3" and not ok: fail_cls[(r["alpha"], sec, rd)] += 1
    pairs = sorted({Fr(k, n) for n in range(1, 801) for k in range(0, n // 2 + 1)
                    if (closed(1, -4, Fr(k, n)), closed(1, 2, Fr(k, n))) == (Fr(3, 10), Fr(1, 5))})
    out = dict(tropical_vs_closed_mismatches=mism, tropical_vs_closed_cases=ncases, excluded_pairs=excluded,
               excluded_outside_degeneracy=len(excluded), tally=dict(tally),
               failing_m2m3_classes=len(fail_cls), failing_m2m3_cases=sum(fail_cls.values()),
               failing_m2m3_class_list=sorted("%s %s %s:%d" % (k[0], k[1], k[2], v) for k, v in fail_cls.items()),
               pair_3_10_1_5_alphas=[str(x) for x in pairs])
    json.dump(out, open(HERE / "domain.json", "w"), indent=1)
    for k in ("tropical_vs_closed_mismatches", "tropical_vs_closed_cases", "excluded_outside_degeneracy", "tally",
              "failing_m2m3_classes", "failing_m2m3_cases", "pair_3_10_1_5_alphas"):
        print(k, out[k])
