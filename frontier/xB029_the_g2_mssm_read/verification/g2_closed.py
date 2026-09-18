"""xB029 G3b -- FENCE 2, MEASURED.  THIRD VERSION; the first two were defective and both
failures are recorded in the arc rather than overwritten:

  v1 VOID  -- filled the meridian BEFORE covering.  That gives S^3, which has no covers, so
              the cell printed 'no cover' eleven times and measured nothing.
  v2 VOID  -- covered first, then filled slope (1,0).  For n = 2,3 that worked; for n >= 4
              the filled manifold still had b1 = 1, i.e. (1,0) is the HOMOLOGICAL LONGITUDE
              there and the fill killed nothing.  The 'closed |H_1|' column was then just the
              cusped torsion reprinted, and the '19 of 19' it reported was CONTAMINATED --
              only n = 2,3 were genuine closed measurements.  The b1 column caught it.

  v3 (this) -- SEARCH for the slopes that actually close the manifold (b1 = 0) and report what
              they give, with the calibration kept in front.
"""
import json, math, os, warnings
warnings.filterwarnings("ignore")
import snappy
from mpmath import mp
mp.dps = 40
RNG = 8


def lucas(m):
    a, b = 2, 1
    for _ in range(m):
        a, b = b, a + b
    return a


def order(H):
    t = 1
    for d in H.elementary_divisors():
        if d:
            t *= d
    return t, H.betti_number()


print("G3b v3   THE CLOSED SIDE -- does the growth rate survive compactification?")
print("         Qhat must be a COMPACT associative 3-cycle; the tower members are CUSPED.")
print("         CALIBRATION kept in front: the 2-fold branched cover of the figure-eight is")
print("         the lens space L(5,2), |H_1| = 5; the 3-fold has |H_1| = 16.")
K = snappy.Manifold("4_1")
vol1 = float(snappy.Manifold("m004").volume())
rows = []
for n in range(2, 19):
    cv = K.covers(n, cover_type="cyclic")
    if not cv:
        print(f"  n={n}: NO COVER"); continue
    X = cv[0]
    cusps = X.num_cusps()
    tor_c, b_c = order(X.homology())
    volc = float(X.volume())
    pred = lucas(2 * n) - 2
    hits = []
    for p in range(-RNG, RNG + 1):
        for q in range(-RNG, RNG + 1):
            if (p, q) == (0, 0) or math.gcd(abs(p), abs(q)) != 1:
                continue
            X.dehn_fill((p, q))
            try:
                t, b = order(X.homology())
            except Exception:
                continue
            if b == 0:
                v = None
                try:
                    if X.solution_type().startswith("all tetrahedra"):
                        v = float(X.volume())
                except Exception:
                    pass
                hits.append((p, q, t, v))
    X.dehn_fill((0, 0))
    hits.sort(key=lambda h: abs(h[2] - pred))
    best = hits[0] if hits else None
    exact = [h for h in hits if h[2] == pred]
    rows.append({"n": n, "cusps": cusps, "cusped_tor": tor_c, "cusped_b1": b_c,
                 "cusped_vol": volc, "pred": pred, "n_closing_slopes": len(hits),
                 "exact_slopes": [(h[0], h[1]) for h in exact],
                 "exact_vol": [h[3] for h in exact],
                 "best": best})
    ev = [h[3] for h in exact if h[3]]
    print(f"  n={n:3d} cusps={cusps} cusped|Tor|={tor_c:<12d} vol={volc:8.4f} | "
          f"closing slopes {len(hits):3d}; slopes giving EXACTLY L_{2*n}-2={pred}: "
          f"{[(h[0],h[1]) for h in exact]}"
          + (f"  vol={min(ev):.5f}" if ev else "  vol=(non-hyperbolic)"))

ok2 = [r for r in rows if r["n"] == 2 and r["exact_slopes"]]
ok3 = [r for r in rows if r["n"] == 3 and r["exact_slopes"]]
cal_ok = bool(ok2 and ok3)
print(f"\n         CALIBRATION passes (n=2 and n=3 each realise their known |H_1|): {cal_ok}")
have = [r for r in rows if r["exact_slopes"]]
print(f"         a closing slope realising EXACTLY L_2n - 2 exists for {len(have)} of {len(rows)} n")
volrows = [(r["n"], min([v for v in r["exact_vol"] if v]), r["cusped_vol"])
           for r in rows if any(v for v in r["exact_vol"])]
print(f"         hyperbolic closed volumes found for n = {[v[0] for v in volrows]}")
for n, vf, vc in volrows:
    print(f"           n={n:3d}  Vol(closed)={vf:9.5f}  <  Vol(cusped)={vc:9.5f}  "
          f"ratio {vf/vc:.6f}")
mono = all(volrows[i][1] / volrows[i][2] < volrows[i + 1][1] / volrows[i + 1][2]
           for i in range(len(volrows) - 1)) if len(volrows) > 1 else None
print(f"         ratio increasing toward 1 from below: {mono}")

kept = cal_ok and len(have) == len(rows)
print()
if kept:
    print("         *** FENCE 2 DOES NOT BITE.  Every n in range has a CLOSED filling whose")
    print("         |H_1| is EXACTLY the cusped tower's L_2n - 2.  The growth rate is NOT a")
    print("         property of the cusp.  THE SEAT'S SEALED PRIOR ON THIS POINT IS WRONG --")
    print("         it predicted this fence would be the one that bites.")
    print(f"         At n = 88: L_176 - 2 = {lucas(176)-2}, log = "
          f"{float(mp.log(lucas(176)-2)):.4f} >= 84,")
    print(f"         at a closed volume STRICTLY BELOW {88*vol1:.2f}.")
else:
    print("         *** FENCE 2 BITES, or calibration failed -- see the rows above.")
print()
print("         WHAT THIS IS NOT:  P_eff also needs C_1/C_2 -- BOTH hidden sectors, their")
print("         volumes and a cutoff.  None of that is computed here.  This is the T_O term")
print("         of eq.(A12) and nothing else.  Gate 5 absolute.")

out = {"calibration_ok": bool(cal_ok), "rows": rows, "n_with_exact": len(have),
       "n_total": len(rows), "vol_rows": volrows, "ratio_increasing": mono,
       "fence2_bites": (not kept), "H1_Sigma_88": str(lucas(176) - 2),
       "log_H1_Sigma_88": float(mp.log(lucas(176) - 2)),
       "cusped_vol_88": 88 * vol1}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "g2_closed.json"), "w", encoding="utf-8"),
          indent=1, default=str)
print(f"G3b {'PASS' if cal_ok else 'FAIL (calibration)'}  (content is the verdict above)")
