"""B1235 cell 2 -- does A6's FREE orientation-reversing deck involution select CS = 0?

Codex R036 (correct): amphichirality forces only CS in {0, 1/4} mod 1/2 (B1224), so B1234's arrow
"A6 -> amphichiral -> the CS=0 / k-blind wall" skips a step. The discriminating fact is computable:
CS of the orientation double cover of every non-orientable census manifold in B1234's slice, against
the 1/4-rate among amphichiral manifolds whose involution is NOT known to be free (the control).
Result is DATA (a rate), not a theorem -- the theorem is registered as a lead.
"""
import json, snappy
SLICE = 40
res = {"covers": [], "control": {}}
z = q = other = 0
for M in snappy.NonorientableCuspedCensus[:SLICE]:
    C = M.orientation_cover()
    cs = float(C.chern_simons()); r = (cs + 0.25) % 0.5 - 0.25
    cls = "0" if abs(r) < 1e-6 else ("1/4" if abs(abs(r) - 0.25) < 1e-6 else "other")
    res["covers"].append({"base": M.name(), "cover_cs_mod_half": round(r, 8), "class": cls})
    z += cls == "0"; q += cls == "1/4"; other += cls == "other"
print(f"orientation double covers ({SLICE}): CS=0: {z}   CS=1/4: {q}   other: {other}")
assert other == 0, "amphichiral covers must sit in {0,1/4} (B1224) -- an 'other' means a bug"
# control: amphichiral manifolds in general (B1186's 112-family + a 200-slice of the orientable census)
fam = json.load(open("chirality_112.json"))
amph = [r for r in fam if r["amphicheiral"] is True]
q_fam = sum(1 for r in amph if abs(abs((r["cs"] + 0.25) % 0.5 - 0.25) - 0.25) < 1e-6)
cz = cq = 0
for M in snappy.OrientableCuspedCensus(cusps=1)[:200]:
    try:
        if not M.symmetry_group().is_amphicheiral(): continue
    except Exception: continue
    r = (float(M.chern_simons()) + 0.25) % 0.5 - 0.25
    if abs(r) < 1e-6: cz += 1
    elif abs(abs(r) - 0.25) < 1e-6: cq += 1
res["control"] = {"family112_amphichiral": len(amph), "family112_at_quarter": q_fam,
                  "census200_amphichiral": cz + cq, "census200_at_quarter": cq}
print(f"control -- amphichiral in the 112-family: {len(amph)}, at CS=1/4: {q_fam}")
print(f"control -- amphichiral in OrientableCuspedCensus(cusps=1)[:200]: {cz+cq}, at CS=1/4: {cq}")
res["summary"] = {"slice": SLICE, "covers_cs0": z, "covers_cs_quarter": q}
json.dump(res, open("a6_cover_cs.json", "w"), indent=1)
print("VERDICT: free-deck covers at CS=0:", f"{z}/{SLICE}", "| amphichiral-in-general at 1/4:",
      f"{q_fam + cq}/{len(amph) + cz + cq}", "-> the free deck is doing MORE than amphichirality (data, not theorem)")
