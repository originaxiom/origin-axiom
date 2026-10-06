#!/usr/bin/env python3
"""B1487 THE ENDS -- cell E1: the floor I(W1) >= k - m_A - b0 (the SM seat's Lemma F') checked on every reading of that frame that is on
main: the 380 reproduced rows of sm:B1541 on N_45 (five cusps, trivial character: m_A = 5, b0 = 1) and B1485's 10 member
readings on m135 and m136 (one cusp; m_A = 1 where the member is trivial on the cusp, else 0; b0 = 1 for a sign
character; k = 1 at a boundary-type class, 0 at an interior one).  Also the one-cusped consequence |I(W1)| <= m_A + b0."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in [HERE, *HERE.parents] if (p / "docs" / "handoffs").is_dir())
out = dict(rows=[], violations=[])
rows = json.load(open(ROOT / "docs/handoffs/cc_2026-10-06_sm_b1541_reproduction/run_main_bench.json"))
for r in rows:
    I, k, b0 = r["reading"]["count"][0], r["reading"]["k"], r["reading"]["b0"]; mA = 5
    ok = I >= k - mA - b0; out["rows"].append(dict(src="N45", part=r["part"], subspace=r["subspace"], I=I, k=k, mA=mA, b0=b0, floor=k - mA - b0, ok=ok, tight=(I == k - mA - b0)))
    if not ok: out["violations"].append(out["rows"][-1])
for name, mA in (("m135", 1), ("m136", 0)):
    for m in json.load(open(ROOT / "frontier/B1485_the_silver_members_by_a_second_route/verification" / f"members_{name}.json")):
        for rd in m["readings"]:
            k = 0 if rd["cls"].startswith("interior") else 1; b0 = 1; I = rd["I_W1"]
            ok = I >= k - mA - b0 and abs(I) <= mA + b0
            out["rows"].append(dict(src=name, cls=rd["cls"], I=I, k=k, mA=mA, b0=b0, floor=k - mA - b0, ok=ok, tight=(I == k - mA - b0)))
            if not ok: out["violations"].append(out["rows"][-1])
out["summary"] = dict(rows=len(out["rows"]), violations=len(out["violations"]), tight=sum(1 for r in out["rows"] if r["tight"]),
                      n45_min_I=min(r["I"] for r in out["rows"] if r["src"] == "N45"), n45_floor_min=min(r["floor"] for r in out["rows"] if r["src"] == "N45"))
json.dump(out, open(HERE / "floor_check.json", "w"), indent=1); print(json.dumps(out["summary"]))
