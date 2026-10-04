#!/usr/bin/env python3
"""B1540 -- THE ROOM FOR THREE AT THE EISENSTEIN ORDER: every cyclic cover with room >= 3 in pulled_back_rooms.json other than
m003's d9.2 (N_45, read by room_n45.py) -- six covers, each the 6-fold cyclic cover of a degree-10 cover of m003 along a
pulled-back character of order 6, degree 60 -- read directly at the trivial character (room_lib.read_cover): route N (Shapiro on
m003 with the degree-60 permutation module), route R (the cover's own presentation, another prime) and H_1 (b1 - cusps = n(1));
then the six sorted into conjugacy classes of subgroups of pi_1(m003) (sm:B1536's canonical form).

    python3 room_60.py [--record]      ->  room_60.json (about a minute)"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import room_lib as L  # noqa: E402


def main():
    pb = json.loads((HERE / "pulled_back_rooms.json").read_text())
    todo = [(k, x) for k, v in sorted(pb["by member"].items()) for x in v["room >= 3"] if k != "m003:d9.2"]
    assert sorted(k for k, _ in todo) == ["m003:d10.13", "m003:d10.14", "m003:d10.16", "m003:d10.36", "m003:d10.38",
                                          "m003:d10.40"] and all(x["order"] == 6 for _, x in todo), "the census's list"
    rep, canon, agree = {"covers": {}}, {}, True
    for key, x in todo:
        st, cid = key.split(":")
        S, perms, cov = L.cover(st, cid)
        ab = L.Ab(cov)
        pe, k = L.cyclic_cover(cov, ab, tuple(x["c"]), pb["by member"][key]["M"])
        assert k == x["order"] == 6
        r = L.read_cover(S, pe)
        rN, rR = r["route N (prime, n(1), n(rho), capW, capL2)"], r["route R (prime, n(1), n(rho), capW, capL2)"]
        r["Lemma A from the banked rows: (n(1), n(rho)), room"] = [x["(n(1), n(rho))"], x["room"]]
        r["the character (own coordinates mod M, M, order)"] = [x["c"], pb["by member"][key]["M"], x["order"]]
        ok = (r["connected"] and rN[1:3] == rR[1:3] == x["(n(1), n(rho))"] and rN[3:] == rR[3:]
              and r["H_1 (free rank, torsion); b1 - cusps"][2] == rN[1] and min(rN[3], rN[4]) == x["room"])
        r["every route agrees"] = bool(ok)
        agree &= ok
        canon[key] = L.canonical(S, pe)
        rep["covers"][key] = r
        print(key, json.dumps(r), flush=True)
    classes = []
    for key in sorted(canon):
        for cl in classes:
            if canon[cl[0]] == canon[key]:
                cl.append(key)
                break
        else:
            classes.append([key])
    rep["conjugacy classes (covers of m003 up to conjugacy)"] = classes
    rep["rooms"] = {key: min(r["route N (prime, n(1), n(rho), capW, capL2)"][3:]) for key, r in rep["covers"].items()}
    rep["every route agrees"] = bool(agree)
    print(json.dumps({k: v for k, v in rep.items() if k != "covers"}))
    if "--record" in sys.argv:
        (HERE / "room_60.json").write_text(json.dumps(rep, indent=1) + "\n")
    if not agree:      # fail closed (the audit lane's R92): a disagreeing run is kept on record, and exits non-zero
        raise SystemExit("room_60.py: the routes disagree (see 'every route agrees')")
    return rep


if __name__ == "__main__":
    main()
