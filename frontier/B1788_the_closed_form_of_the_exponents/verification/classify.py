"""Closed-form check over B1785's 662 lines (data-free): every (line, sector, reading, ratio) classified as
  DEG  -- the torsion degeneracy: one chiral twist point q w is exact 4-torsion and the other 2-torsion (4 q_L w, 2 q_R w in
          Z + Z tau, or L <-> R); then M is rank one, m2/m3 = 1/2 exactly and m1 = 0 (B1785's m1/m3 fit is noise there);
  CF   -- otherwise the closed form (tropical, generic): m2/m3 = min(1/2, E(det M) - 2 mu_min) = 1/2 - (||2 q_L a|| + ||2 q_R a||)/2
          and m1/m3 from det Y = 4 det M det S P;
and each disagreement > 0.05 flagged NEAR-TIE when a tropical minimum it rests on is attained within GAP by a competitor
(a finite-window crossover: the prefactors sqrt(2 pi L + c_s) then decide at Im tau 4-6), else OTHER."""
import json, itertools
from fractions import Fraction as Fr
from collections import Counter, defaultdict
import tropical as T
import pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
GAP = Fr(6, 100)


def torsion_deg(a, b, ql, qr):
    def k_torsion(q, k):            # k q w in Z + Z tau  <=>  k q a in Z and k q b in Z
        return (k * q * a).denominator == 1 and (k * q * b).denominator == 1
    def exact4(q): return k_torsion(q, 4) and not k_torsion(q, 2)
    return (exact4(ql) and k_torsion(qr, 2)) or (exact4(qr) and k_torsion(ql, 2))


def gaps(P, mu):
    """distances to the nearest DISTINCT competitor of each tropical minimum the prediction rests on:
    g1 -- sigma1: the next-larger M exponent above mu_min (an equal one is a tie, not a crossover);
    g12 -- sigma1 sigma2: the gap between its two branches, |1/2 - (E(det M) - 2 mu_min)|;
    g3 -- det Y's last factor P: the next-larger monomial exponent above its minimum."""
    ents, mins, det = P
    mm = min(mu); up_ = [m - mm for m in mu if m > mm]; g1 = min(up_) if up_ else Fr(1)
    g12 = abs(Fr(1, 2) - ((mu[0] + mu[3]) - 2 * mm))
    v = sorted(set(T.trop([m], mu) for m in det)); g3 = (v[1] - v[0]) if len(v) > 1 else Fr(1)
    return g1, g12, g3


if __name__ == "__main__":
    P = {rd: T.polys(rd) for rd in ("S", "St")}
    d = json.load(open(ROOT / "frontier/B1785_the_slope_sets_the_exponents/verification/exponents.json"))
    tally = Counter(); per = defaultdict(Counter); other = []
    for r in d:
        a, b = Fr(r["alpha"]), Fr(r["b"])
        for sec, (lf, rf) in T.SECTORS.items():
            ql, qr = T.SIXY[lf], T.SIXY[rf]; mu = T.E(ql * a, qr * a)
            dg = torsion_deg(a, b, ql, qr)
            for rd in ("S", "St"):
                e2, e3 = T.predict(P[rd], mu); g1, g12, g3 = gaps(P[rd], mu)
                for nm, pe, rel in (("m2/m3", e2, (g1, g12)), ("m1/m3", e3, (g1, g12, g3))):
                    obs = r["%s|L_max|%s|%s" % (sec, rd, nm)]["exponent"]
                    if dg:
                        if nm == "m2/m3": cls = "DEG ok" if abs(obs - 0.5) <= 0.05 else "DEG fail"
                        else: cls = "DEG m1=0 (not compared)"
                    else:
                        if abs(obs - float(pe)) <= 0.05: cls = "CF ok"
                        elif min(rel) < GAP: cls = "CF near-tie"
                        else: cls = "CF other"; other.append((r["alpha"], r["b"], sec, rd, nm, round(obs, 3), str(pe), [str(x) for x in rel]))
                    tally[cls] += 1; per[(sec, rd, nm)][cls] += 1
    for k, v in sorted(tally.items()): print("%-26s %d" % (k, v))
    print()
    for k in sorted(per):
        v = per[k]; n_ok = v["CF ok"] + v["DEG ok"]; n = sum(v.values()) - v["DEG m1=0 (not compared)"]
        print(k, "agree %d/%d (%.1f%%)" % (n_ok, n, 100 * n_ok / n), dict(v))
    print("\nCF other (not a near-tie):", len(other))
    slopes = Counter((o[0], o[2], o[3], o[4]) for o in other)
    for k, v in sorted(slopes.items(), key=lambda z: -z[1])[:25]: print("  ", k, v, next(o for o in other if (o[0], o[2], o[3], o[4]) == k)[5:])
    json.dump(other, open("classify_other.json", "w"), indent=0)
