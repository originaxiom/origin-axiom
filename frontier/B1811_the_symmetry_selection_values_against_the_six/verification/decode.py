"""B1811 decode (P-517, 2026-11-19): the numbers B1811's FINDINGS states that no committed script printed, decoded from the
committed census.jsonl and comparison.json -- DATA-FREE.  This script reads no measured value: it opens neither the masses
file nor the CKM file, and it imports neither compare.py nor B1741's module (their loader reads the masses).  What it
decodes:
  D1  the seat-reading cells (208 = 52 rows x 2 radii x 2 seat readings) that carry a massless state, by the smallest of
      their six ratios, with the gap between the largest such ratio and the smallest non-zero one; the per-configuration
      split; the non-degenerate cells in the same unit, and in the unit of (configuration, direction, reading)
  D2  at line 70 (F_6 at (i, 0)), L_2, readings (S~, S~, S~), c = 3: D = c^2 (m_mu m_d)/(m_s m_e), V_ud and J
  D3  a_0 (line 1x) against F_6 (line 7x) at each configuration: the largest relative difference over the entries above
      1e-12, and where it sits
  D4  read back from comparison.json, as stored: chi2_six's minimum, best_six's row, factors and D, best_nine's row
What it cannot decode without comparing with data, so leaves as B1811 states them (its referee's rerun, Review 73): that
line 70 is the chi2-best row; that row's six model-over-measured factors; the location of chi2_nine's minimum; 'every ratio
is too large' on the non-degenerate cells.
    python3 -B decode.py > decode_run.txt"""
import json, math, pathlib, collections
HERE = pathlib.Path(__file__).resolve().parent
RD = ("S", "St")                                     # B1741's reading names: S~ is 'St'
SEAT = ((1, 0, 0), (1, 1, 1))                        # B1741's seat menu: (up, down, lepton) reading indices
ZERO = 1e-8                                          # a cell is massless when one of its six ratios is below this


def rows():
    out = [json.loads(l) for l in (HERE / "census.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(out) == 52 == len({r["line"] for r in out})
    return out


def six(r, h, rd):
    a, b, l = rd
    return r[f"up|{h}|{RD[a]}"] + r[f"down|{h}|{RD[b]}"] + r[f"lep|{h}|{RD[l]}"]   # (c/t, u/t, s/b, d/b, mu/tau, e/tau)


def main():
    R = rows(); by = {r["line"]: r for r in R}
    cells = [(r["config"], r["direction"], h, rd, min(six(r, h, rd))) for r in R for h in ("L_max", "L_2") for rd in SEAT]
    z = [c for c in cells if c[4] < ZERO]; nz = [c for c in cells if c[4] >= ZERO]
    print("D1 cells: %d; massless: %d; non-degenerate: %d" % (len(cells), len(z), len(nz)))
    print("D1 gap: largest massless ratio %.2e, smallest non-zero %.2e" % (max(c[4] for c in z), min(c[4] for c in nz)))
    sp = collections.Counter((c[0], c[4] < ZERO) for c in cells)
    for cf in ("(i, 0)", "(omega, 0)", "(i, (1/2, 1/2))", "(omega, (1/3, 2/3))"):
        print("D1 split %s: massless %d, non-degenerate %d" % (cf, sp[(cf, True)], sp[(cf, False)]))
    print("D1 massless at (i, 0): directions %s" % sorted({c[1] for c in z if c[0] == "(i, 0)"}))
    print("D1 non-degenerate, all at tau = i: %s" % all(c[0].startswith("(i,") for c in nz))
    u = {(c[0], c[1], c[3]) for c in nz}; v = {(c[0], c[1]) for c in nz}
    print("D1 non-degenerate in other units: (configuration, direction, reading) %d; (configuration, direction) %d" % (len(u), len(v)))
    r = by[70]; s = six(r, "L_2", (1, 1, 1)); k = r["ckm|L_2|St|St"]; c = 3.0
    D = c * c * (s[4] * s[3]) / (s[2] * s[5])
    print("D2 line 70 = %s at %s; L_2; (S~, S~, S~); c = 3: D = %.12f; V_ud = %.15f; J = %.3e" % (
        r["direction"], r["config"], D, math.sqrt(max(0.0, 1 - k[0] ** 2 - k[2] ** 2)), k[3]))
    for ci in range(4):
        a, f = by[10 + ci], by[70 + ci]; best = (0.0, "-", -1)
        for key in (x for x in a if "|" in x):
            for j, (p, q) in enumerate(zip(a[key], f[key])):
                if abs(p) > 1e-12 and abs(q) > 1e-12 and abs(p - q) / abs(q) > best[0]: best = (abs(p - q) / abs(q), key, j)
        print("D3 %s a_0 vs F_6: largest relative difference %.4g (%s, entry %d)" % (a["config"], *best))
    d = json.loads((HERE / "comparison.json").read_text(encoding="utf-8"))
    print("D4 stored chi2_six minimum (seat): %.3f" % d["chi2"]["six|seat"]["min"])
    b = d["best_six"]["seat"]
    print("D4 stored best_six (seat): line %d, %s, readings %s, c = %g, D = %.3f, factors %s" % (
        b["line"], b["horocycle"], b["readings"], b["lepton_factor"], b["D"], [round(x, 1) for x in b["model_over_measured"]]))
    b = d["best_nine"]["seat"]
    print("D4 stored best_nine (seat, by the worst factor): line %d, %s, readings %s" % (b["line"], b["horocycle"], b["readings"]))


if __name__ == "__main__":
    main()
