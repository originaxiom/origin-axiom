#!/usr/bin/env python3
"""B1540 -- THE PULLED-BACK ROOMS: what sm:B1536's banked rows fix about the room covers' pulled-back characters, and the room at
the trivial character of every cyclic cover along a pulled-back character whose every power they fix (Lemma A).  Banked data
and structure only: nothing twisted is computed here.

The population: sm:B1536's 30 room covers (room_lib.members()).  A banked row at the member nu = (u, kappa) of a cover N (routes
R and N alike) fixes three own-character readings of N (rho is self-dual):
    the line at nu^-4 = n(L);     the four at nu^3 = n((VL)*);     the four at nu^5 = n(V_eta)
(L = nu^-4, (V (x) L)* = nu^3 (x) rho* = nu^3 (x) rho, V_eta = nu^5 (x) rho).  Each power of nu is restricted to N in own
coordinates (room_lib.restrict).  A value is taken as fixed only when routes R and N both give it and no two members give it
differently (a conflict is recorded and fails the run).  For each cyclic subgroup <c> of fixed characters whose every power has
the line and the four fixed, Lemma A gives N_c's supplies (sum_j n(c^j), sum_j n(rho c^j)) and its room min(1 + n(1), n(rho)).

    python3 pulled_back_rooms.py [--record]      ->  pulled_back_rooms.json (about a minute)"""
import gzip
import json
import sys
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import room_lib as L  # noqa: E402

FIELDS = ((-4, "n(L)", "line"), (3, "n((VL)*)", "four"), (5, "n(V_eta)", "four"))


def banked(route, st):
    out = {}
    for line in gzip.open(L.B1536V / f"run_{route}_{st}.jsonl.gz", "rt"):
        r = json.loads(line)
        if not r.get("done"):
            out.setdefault(r["cover"], []).append(r)
    return out


def member_rooms(st, cid, deg, n1, nr, rows):
    S, perms, cov = L.cover(st, cid)
    ab = L.Ab(cov)
    M = 1
    for r in rows["R"] + rows["N"]:
        for x in list(r["u"]) + [r["kappa"]]:
            M = lcm(M, Fr(x).denominator)
    vals = {}          # c -> kind -> route -> set of values
    for route in ("R", "N"):
        for r in rows[route]:
            u, k = (Fr(r["u"][0]), Fr(r["u"][1])), Fr(r["kappa"])
            for pw, field, kind in FIELDS:
                c = L.restrict(S, cov, ab, ((pw * u[0]) % 1, (pw * u[1]) % 1, (pw * k) % 1), M)
                vals.setdefault(c, {}).setdefault(kind, {}).setdefault(route, set()).add(r["S"][field])
    fixed, conflicts = {}, []
    for c, d in vals.items():
        fixed[c] = {}
        for kind, byroute in d.items():
            allv = set().union(*byroute.values())
            if len(allv) > 1:
                conflicts.append([list(c), kind, sorted(allv)])
            elif set(byroute) == {"R", "N"}:
                fixed[c][kind] = allv.pop()
    zero = tuple(0 for _ in ab.coords)
    assert fixed[zero] == {"line": n1, "four": nr}, "the trivial character's banked values"
    cyc, seen = [], set()
    for c in sorted(fixed):
        if c == zero:
            continue
        k = L.order_of(c, M)
        pw = [tuple((j * x) % M for x in c) for j in range(k)]
        if frozenset(pw) in seen:
            continue
        seen.add(frozenset(pw))
        if all(len(fixed.get(p, {})) == 2 for p in pw):
            s1, s4 = sum(fixed[p]["line"] for p in pw), sum(fixed[p]["four"] for p in pw)
            cyc.append({"c": list(c), "order": k, "degree": deg * k, "(n(1), n(rho))": [s1, s4], "room": min(1 + s1, s4)})
    jumps = lambda kind: sorted({(L.order_of(c, M), v[kind]) for c, v in fixed.items()  # noqa: E731
                                 if c != zero and v.get(kind, 0) >= 1})
    return {"degree": deg, "(n(1), n(rho))": [n1, nr], "H_1 (free rank, torsion)": [len(ab.free), ab.torsion], "M": M,
            "banked members (routes R, N)": [len(rows["R"]), len(rows["N"])],
            "pulled-back characters reached": len(fixed),
            "fixed (line, four)": [sum(1 for v in fixed.values() if "line" in v), sum(1 for v in fixed.values() if "four" in v)],
            "conflicts": conflicts, "line >= 1 at (order, n)": [list(x) for x in jumps("line")],
            "four >= 1 at (order, n)": [list(x) for x in jumps("four")],
            "cyclic subgroups fully fixed": len(cyc), "best room": max([x["room"] for x in cyc], default=None),
            "room >= 3": sorted([x for x in cyc if x["room"] >= 3], key=lambda x: (x["degree"], x["c"]))}


def main():
    rep = {"population": len(L.members())}
    bk = {(route, st): banked(route, st) for route in ("R", "N") for st in ("m004", "m003")}
    by = {}
    for st, cid, deg, n1, nr, cus in L.members():
        rows = {route: bk[(route, st)].get(cid, []) for route in ("R", "N")}
        by[f"{st}:{cid}"] = x = member_rooms(st, cid, deg, n1, nr, rows)
        print(f"{st}:{cid} degree {deg} ({n1}, {nr}): reached {x['pulled-back characters reached']}, "
              f"line {x['line >= 1 at (order, n)']}, four {x['four >= 1 at (order, n)']}, cyclic {x['cyclic subgroups fully fixed']}, "
              f"best room {x['best room']}, room >= 3 at {[(y['order'], y['degree'], y['(n(1), n(rho))']) for y in x['room >= 3']]}",
              flush=True)
    rep["by member"] = by
    rep["conflicts"] = sum(len(x["conflicts"]) for x in by.values())
    rep["members with room >= 3 on a fixed pulled-back cyclic cover"] = sorted(k for k, x in by.items() if x["room >= 3"])
    rep["m004: best room on a fixed pulled-back cyclic cover"] = max(x["best room"] or 0 for k, x in by.items()
                                                                     if k.startswith("m004"))
    print(json.dumps({k: v for k, v in rep.items() if k != "by member"}))
    if "--record" in sys.argv:
        (HERE / "pulled_back_rooms.json").write_text(json.dumps(rep, indent=1) + "\n")
    if rep["conflicts"]:      # fail closed: two banked rows disagree on one reading
        raise SystemExit("pulled_back_rooms.py: conflicting banked values (see 'conflicts')")
    return rep


if __name__ == "__main__":
    main()
