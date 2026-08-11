"""B1027 -- the sealed verdict arithmetic (data contacted 2026-08-11, post-seal c58c8a88)."""
def circ_dist(a, b):
    d = abs(a - b) % 360
    return min(d, 360 - d)

# fetched post-seal, sources as declared (recorded in FINDINGS):
QUARK = {"central": 68.8, "sigma_up": 4.5, "sigma_dn": 4.5, "source": "PDG-cited delta_13 = 68.8 +- 4.5 deg"}
LEPTON = {"central": 197.0, "sigma_up": 42.0, "sigma_dn": 25.0, "source": "NuFIT 5.2 NO: 197 +42/-25 deg"}
PRED = [120.0, 240.0]

def sector_verdict(name, s):
    # power: mean sigma windows around the two predictions
    mean_sigma = (s["sigma_up"] + s["sigma_dn"]) / 2
    powered = 4 * mean_sigma <= 180.0
    rows = []
    for p in PRED:
        d = circ_dist(s["central"], p)
        sigma_toward = s["sigma_up"] if ((p - s["central"]) % 360) < 180 else s["sigma_dn"]
        hit = d <= sigma_toward
        rows.append((p, d, sigma_toward, "HIT" if hit else "MISS", round(d / sigma_toward, 2)))
    print(f"{name}: {s['source']}  |  POWERED: {powered} (4*mean_sigma = {4*mean_sigma:.0f} deg)")
    for p, d, st, v, ns in rows:
        print(f"   pred {p:5.0f} deg: distance {d:5.1f}, 1sigma(toward) {st:4.1f} -> {v}  ({ns} sigma)")
    return rows, powered

q, qp = sector_verdict("QUARK ", QUARK)
l, lp = sector_verdict("LEPTON", LEPTON)
allmiss = all(v == "MISS" for rows in (q, l) for (_,_,_,v,_) in rows)
print()
print("CROSSING VERDICT:", "ALL-MISS (powered both sectors)" if allmiss and qp and lp else "see rows")
print("the leptonic -120 (=240) margin: 1.0 degree beyond the 1-sigma edge (1.02 sigma) -- "
      "recorded as the precision frontier, NOT promoted (non-weakening).")
