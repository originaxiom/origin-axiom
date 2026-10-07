#!/usr/bin/env python3
"""B1492 -- the sealed surveys (survey_L8a15.json, survey_o10_150729.json, by multicusp.py) read against the sealed
predictions D1-D4, with the cusp decomposition of every reading; writes summary.json and prints the tables for FINDINGS.

The floor is the SM seat's k - m_A - b0 (one-sided, B1491); the ceiling 2 m_A + m_B - b0.  The survey's 'ceiling'
column set m_B = 0; for a sign character nu^4 = 1 on every cusp, so m_B = (cusps) - m_A and the seat's ceiling is the
larger number -- both are checked here (the survey's is the stricter)."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent


def read(name):
    d = json.load(open(HERE / f"survey_{name}.json")); m = d["cusps"]; out = dict(name=name, cusps=m, gens=d["gens"], characters=len(d["rows"]), rows=[])
    for r in d["rows"]:
        for x in r["readings"]:
            fl = x["k"] - r["m_A"] - r["b0"]; ce_strict = 2 * r["m_A"] - r["b0"]; ce_seat = 2 * r["m_A"] + (m - r["m_A"]) - r["b0"]
            out["rows"].append(dict(nu="".join("+" if r["nu"][g] == 1 else "-" for g in d["gens"]), cusp_trivial=r["cusp_trivial"], m_A=r["m_A"], b0=r["b0"],
                                    cls=x["cls"], dead_on_cusps=x["dead_on_cusps"], k=x["k"], I_W1=x["I_W1"], I_L2W1=x["I_L2W1"], generations=-x["I_W1"],
                                    floor=fl, ceiling_strict=ce_strict, ceiling_seat=ce_seat,
                                    floor_holds=x["I_W1"] >= fl, ceiling_strict_holds=x["I_W1"] <= ce_strict, ceiling_seat_holds=x["I_W1"] <= ce_seat))
    triv = [r for r in d["rows"] if all(v == 1 for v in r["nu"].values())][0]
    members = [r for r in d["rows"] if r["interior"]]
    interior_readings = [x for x in out["rows"] if x["cls"].startswith("interior")]
    out.update(trivial_character=dict(h1=triv["V"]["a1"], interior=triv["interior"], other=triv["other"], readings=[(x["k"], x["I_W1"], x["I_L2W1"]) for x in triv["readings"]]),
               members=[dict(nu="".join("+" if r["nu"][g] == 1 else "-" for g in d["gens"]), m_A=r["m_A"], cusp_trivial=r["cusp_trivial"]) for r in members],
               n_members=len(members), interior_readings=len(interior_readings),
               interior_all_minus_one=all(x["I_W1"] == -1 and x["I_L2W1"] == -1 and x["k"] == 0 for x in interior_readings),
               m_A_at_members=sorted(set(r["m_A"] for r in members)),
               max_generations=max((x["generations"] for x in out["rows"]), default=None), min_I_W1=min((x["I_W1"] for x in out["rows"]), default=None),
               max_I_W1=max((x["I_W1"] for x in out["rows"]), default=None),
               floor_violations=[x for x in out["rows"] if not x["floor_holds"]], ceiling_strict_violations=[x for x in out["rows"] if not x["ceiling_strict_holds"]],
               ceiling_seat_violations=[x for x in out["rows"] if not x["ceiling_seat_holds"]],
               generation_shaped=[x for x in out["rows"] if x["I_W1"] == x["I_L2W1"] and x["I_W1"] < 0],
               no_interior_where_an_end_is_trivial=all(r["interior"] == 0 for r in d["rows"] if r["m_A"] >= 1))
    return out


def table(s):
    print(f"\n{s['name']}: {s['cusps']} cusps, {s['characters']} sign characters; trivial character h1 = {s['trivial_character']['h1']}, interior {s['trivial_character']['interior']}, other {s['trivial_character']['other']}")
    print(f"  members (characters with an interior class): {s['n_members']} at m_A in {s['m_A_at_members']}; every interior reading (-1, -1) at k = 0: {s['interior_all_minus_one']}")
    print(f"  generations = -I(W1): max {s['max_generations']}; I(W1) in [{s['min_I_W1']}, {s['max_I_W1']}]; floor violations {len(s['floor_violations'])}, ceiling (strict) {len(s['ceiling_strict_violations'])}, ceiling (seat) {len(s['ceiling_seat_violations'])}")
    print(f"  no interior class at any character trivial on some end: {s['no_interior_where_an_end_is_trivial']}")
    print("  | ν | trivial on cusp | m_A | class | dead on cusp | k | I(W₁) | I(Λ²W₁) | floor | ceiling |")
    print("  |---|---|---|---|---|---|---|---|---|---|")
    for x in s["rows"]:
        print(f"  | {x['nu']} | {''.join('1' if t else '·' for t in x['cusp_trivial'])} | {x['m_A']} | {x['cls']} | {''.join('d' if t else '·' for t in x['dead_on_cusps'])} | {x['k']} | {x['I_W1']:+d} | {x['I_L2W1']:+d} | {x['floor']:+d} | {x['ceiling_strict']:+d} / {x['ceiling_seat']:+d} |")


if __name__ == "__main__":
    out = {}
    for name in ("L8a15", "o10_150729"):
        if (HERE / f"survey_{name}.json").exists(): out[name] = read(name); table(out[name])
    L = out.get("L8a15"); O = out.get("o10_150729")
    verdicts = {}
    if L:
        verdicts["D1"] = L["trivial_character"]["h1"] == 3 and L["trivial_character"]["interior"] == 0 and not any(not x["floor_holds"] or not x["ceiling_seat_holds"] for x in L["rows"] if x["nu"] == "+++")
        verdicts["D2"] = L["max_generations"] <= 1
        verdicts["D3"] = L["n_members"] >= 1
    if O:
        verdicts["D4"] = O["trivial_character"]["h1"] == 5 and O["trivial_character"]["interior"] == 0 and all(-x["I_W1"] < 3 for x in O["rows"] if x["nu"] == "+++++")
        verdicts["D4_every_character_no_three"] = O["max_generations"] < 3
    out["verdicts"] = verdicts; print("\nverdicts", verdicts)
    json.dump(out, open(HERE / "summary.json", "w"), indent=1)
