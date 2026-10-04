#!/usr/bin/env python3
"""B1536 control K6: read_out.py's logic on synthetic rows (no cohomology; nothing of the population is read).

Two hand-made states with two covers each are written in run.py's row format to a temporary directory, and read_out.main() reads
them with the population replaced by the synthetic one.  The clean record must give every prediction and completeness true;
then each defect below is planted alone, and exactly the predictions it bears on must turn false:
  - a supply differing between the routes (P1), a Part P count differing (P1), a Part O stratum's generic reading differing (P1);
  - a failed identity in one Part O draw of route R (P2);
  - an abelian row with n(L) = 1 (P3); n(1) = 1 at kappa = 1 on a d-cover (P4); the tower's n(1) at 3 (P5) and at 5 (P5);
    n(rho) = 1 at kappa = 1 on a d-cover (P6);
  - both caps >= 3 at a member (P7), and at a non-member (nothing: P7 counts members);
  - (-3, -3) in the second draw of one stratum in route R only (P8 and P1 stay as they are, since the generic draw agrees);
  - (-1, -1) at the pulled-back class in route N only (P9 and P1);
  - a stratum with both bounds >= 3, k = |S| and a generic count (-1, -1) (P10); the same with k < |S| in every draw (nothing);
  - a bound reached only by the non-generic draw's E* rank (P10: the bounds take each rank's larger value);
  - a missing row in route R (completeness).

    python3 read_out_selftest.py [--record]   ->  k6.json"""
import copy
import json
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import read_out as RO  # noqa: E402

STATES = RO.STATES


def reading(count=(0, 0), k=0, b0=0, rk=None, ok=True):
    rk = rk or {"E": 0, "E*": 0, "L2": 0, "L2*": 0}
    return {"count": list(count), "k": k, "b0": b0, "n(L)": 0, "n((VL)*)": 0, "n(V)": 0, "rk d1": dict(rk),
            "bound W": b0 - k + rk["E*"], "bound L2": rk["L2*"] - k, "all": ok, "failed": [] if ok else ["synthetic"]}


def supplies(h1=1, b0=0, nL=0, nq=0):
    return {"h1(V_eta)": h1, "n(V_eta)": 0, "b0": b0, "n(L)": nL, "n((VL)*)": nq, "capW": b0 + nL, "capL2": nq}


def clean():
    """{(state, route): [rows]}: per state a d-cover (abelian, three characters) and a tower cover (two characters)"""
    rec = {}
    for st in STATES:
        for rt in ("N", "R"):
            rows = []
            for cid, abel, kaps in (("d2.1", True, ("0", "1/3", "2/3")), ("Q8.m3", False, ("0", "1/2"))):
                n = 0
                for kap in kaps:
                    row = {"route": rt, "state": st, "cover": cid, "degree": 2, "cusps": 1, "L": 1, "prime": 7,
                           "abelian": abel, "u": ["0", "0"], "kappa": kap}
                    if kap == "0":
                        row["S"] = supplies(h1=1, b0=1, nL=4 if cid == "Q8.m3" else 0, nq=2 if cid == "Q8.m3" else 0)
                        row["member"] = True
                        row["P"] = reading((0, 0), k=1, b0=1)
                        if cid == "Q8.m3":
                            row["O"] = [{"S": [], "readings": [reading(), reading()]},
                                        {"S": [0], "readings": [reading((-1, 0), k=1, b0=1, rk={"E": 0, "E*": 1, "L2": 0,
                                                                                                    "L2*": 1}),
                                                                reading((-1, 0), k=1, b0=1, rk={"E": 0, "E*": 1, "L2": 0,
                                                                                                    "L2*": 1})]}]
                    else:
                        row["S"] = supplies(h1=0)
                        row["member"] = False
                    rows.append(row)
                    n += 1
                rows.append({"route": rt, "state": st, "cover": cid, "done": True, "rows": n, "seconds": 0})
            rec[(st, rt)] = rows
    return rec


def keys_of(rec):
    return {st: {(r["state"], r["cover"], tuple(r["u"]), r["kappa"]) for r in rec[(st, "N")] if not r.get("done")}
            for st in STATES}


def find(rec, st, rt, cover, kap):
    return next(r for r in rec[(st, rt)] if r["cover"] == cover and r.get("kappa") == kap and not r.get("done"))


def read(rec, want):
    with tempfile.TemporaryDirectory() as d:
        for (st, rt), rows in rec.items():
            (Path(d) / f"run_{rt}_{st}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
        saved_argv, saved_keys, saved_out = sys.argv, RO.expected_keys, sys.stdout
        sys.argv = ["read_out.py", "--dir", d]
        RO.expected_keys = lambda st: want[st]
        try:
            sys.stdout = open("/dev/null", "w")
            out = RO.main()
        finally:
            sys.stdout.close()
            sys.argv, RO.expected_keys, sys.stdout = saved_argv, saved_keys, saved_out
    return out


def outcome(out):
    return dict(out["predictions"], complete=out["complete"])


def main():
    base = clean()
    want = keys_of(base)
    res = {}
    ok_all = True

    def case(name, mutate, flips):
        nonlocal ok_all
        rec = copy.deepcopy(base)
        mutate(rec)
        got = outcome(read(rec, want))
        expect = {k: (k not in flips) for k in got}
        ok = got == expect
        res[name] = {"false": sorted(k for k, v in got.items() if not v), "expected false": sorted(flips), "holds": ok}
        ok_all = ok_all and ok

    got = outcome(read(base, want))
    res["clean"] = {"false": sorted(k for k, v in got.items() if not v), "expected false": [], "holds": all(got.values())}
    ok_all = ok_all and all(got.values())

    def supply_differs(rec):
        find(rec, "m004", "R", "Q8.m3", "1/2")["S"]["n(V_eta)"] = 2
    case("a supply differs", supply_differs, {"P1"})

    def p_differs(rec):
        find(rec, "m003", "R", "d2.1", "0")["P"]["rk d1"]["E"] = 1
    case("a Part P connecting rank differs", p_differs, {"P1"})

    def o_differs(rec):
        for x in find(rec, "m004", "R", "Q8.m3", "0")["O"][1]["readings"]:
            x["count"] = [-2, 0]
    case("a Part O generic reading differs", o_differs, {"P1"})

    def failed_draw(rec):
        find(rec, "m003", "R", "Q8.m3", "0")["O"][0]["readings"][1]["all"] = False
    case("a failed identity in one draw", failed_draw, {"P2"})

    def abelian_line(rec):
        for rt in ("N", "R"):
            find(rec, "m004", rt, "d2.1", "2/3")["S"]["n(L)"] = 1
    case("an abelian row with n(L) = 1", abelian_line, {"P3"})

    def d_line(rec):
        for rt in ("N", "R"):
            find(rec, "m003", rt, "d2.1", "0")["S"]["n(L)"] = 1
    case("n(1) = 1 at kappa = 1 on a d-cover", d_line, {"P3", "P4"})

    def tower3(rec):
        for st in STATES:
            for rt in ("N", "R"):
                find(rec, st, rt, "Q8.m3", "0")["S"]["n(L)"] = 3
    case("the tower's n(1) is 3", tower3, {"P5"})

    def tower5(rec):
        for rt in ("N", "R"):
            find(rec, "m004", rt, "Q8.m3", "0")["S"]["n(L)"] = 5
    case("the tower's n(1) is 5", tower5, {"P5"})

    def d_rho(rec):
        for rt in ("N", "R"):
            find(rec, "m004", rt, "d2.1", "0")["S"]["n((VL)*)"] = 1
    case("n(rho) = 1 at kappa = 1 on a d-cover", d_rho, {"P6"})

    def caps_member(rec):
        for rt in ("N", "R"):
            r = find(rec, "m004", rt, "Q8.m3", "0")
            r["S"]["n((VL)*)"] = 3
            r["S"]["capL2"] = 3
    case("both caps >= 3 at a member", caps_member, {"P7"})

    def caps_nonmember(rec):
        for rt in ("N", "R"):
            r = find(rec, "m004", rt, "Q8.m3", "1/2")
            r["S"].update({"b0": 1, "n(L)": 3, "capW": 4, "n((VL)*)": 3, "capL2": 3})
    case("both caps >= 3 at a non-member", caps_nonmember, set())

    def three_in_draw(rec):
        find(rec, "m003", "R", "Q8.m3", "0")["O"][1]["readings"][1]["count"] = [-3, -3]
    case("(-3, -3) in route R's second draw only", three_in_draw, {"P8"})

    def pulled_shaped(rec):
        find(rec, "m004", "N", "d2.1", "0")["P"]["count"] = [-1, -1]
    case("(-1, -1) at the pulled-back class in route N only", pulled_shaped, {"P1", "P9"})

    def open_stratum(rec):
        for rt in ("N", "R"):
            for x in find(rec, "m004", rt, "Q8.m3", "0")["O"][1]["readings"]:
                x.update({"count": [-1, -1], "k": 1, "b0": 1})
                x["rk d1"].update({"E*": 3, "L2*": 4})
    case("an open stratum", open_stratum, {"P10"})

    def closed_by_k(rec):
        for rt in ("N", "R"):
            for x in find(rec, "m004", rt, "Q8.m3", "0")["O"][1]["readings"]:
                x.update({"count": [-1, -1], "k": 0, "b0": 1})
                x["rk d1"].update({"E*": 3, "L2*": 4})
    case("bounds >= 3 but k < |S| in every draw", closed_by_k, set())

    def open_by_second_rank(rec):
        for rt in ("N", "R"):
            r0, r1 = find(rec, "m003", rt, "Q8.m3", "0")["O"][1]["readings"]
            r0.update({"count": [-1, 0], "k": 1, "b0": 1})
            r0["rk d1"].update({"E*": 1, "L2*": 4})
            r1.update({"count": [-1, 0], "k": 1, "b0": 1})
            r1["rk d1"].update({"E*": 3, "L2*": 3})
    case("bound W reached only by the second draw's E* rank", open_by_second_rank, {"P10"})

    def missing(rec):
        rows = rec[("m003", "R")]
        rec[("m003", "R")] = [r for r in rows if not (r.get("cover") == "d2.1" and r.get("kappa") == "1/3")]
    case("a missing row in route R", missing, {"complete"})

    out = {"cases": res, "holds": ok_all}
    print(json.dumps(out, indent=1))
    if "--record" in sys.argv:
        (HERE / "k6.json").write_text(json.dumps(out, indent=1) + "\n")
    return out


if __name__ == "__main__":
    main()
