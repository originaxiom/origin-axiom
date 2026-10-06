#!/usr/bin/env python3
"""B1543 -- Corollary C' on the banked record, and the census of the cyclic covers the banked rows fix.  Banked data only:
nothing twisted is computed here.

Corollary C' (from sm:B1535's Theorem C (ii), I(W1) = dim(<c_i> & Lambda(V)) - b0 + rk delta1_W - dim(im delta1_W* & K_L)):
    I(W1) >= rk delta1_W - b0 - n(nu^4),
since the first term is >= 0 and the last is <= dim K_L = n(nu^4).  A reading records rk delta1_W as "rk d1"["E"], b0 and
n(L) = n(nu^4).  The check runs over every reading of sm:B1541's record and of sm:B1536's Parts P and O, both routes.

The census: every cyclic cover N_c of sm:B1536's thirty room covers along a pulled-back character c whose every power has the
line and the four fixed by the banked rows (sm:B1540's construction, loaded by path), with (n(1), n(rho)) at its trivial
character by Lemma A, and the maximal-rank criterion of Corollary C'': 3 <= n(rho) <= n(1) - 2.

The direct census (--direct): every one of those covers built (sm:B1540's room_lib.cyclic_cover) and read at its trivial
character without Lemma A -- route N with the cover's own permutation module, route R on the cover's own presentation at another
prime, and H_1 by PARI's Smith form (room_lib.read_cover) -- against Lemma A's sums.

The graded census (--graded): on the k-fold cyclic cover N_c, Shapiro grades H^1(N_c; C) = sum_m H^1(N; c^m) and
H^1(N_c; rho) = sum_j H^1(N; c^j rho), and the cup product and the interior part of H^2 respect (j, m) -> j + m.  So a class in
the c^j eigenspace of the deck group has rk delta1_W <= B_j = sum_m min(h^1(N; c^m), n(c^(j+m) rho)), which can be smaller than
the global bound.  Half lives for unitary characters gives h^1(N; c^m) = n(c^m) + #{cusps of N where c^m is trivial} and the
four's h^1(N; c^j rho) = n(c^j rho) + #{cusps of N where c^j is trivial} (a cusp torus carries H^1 of dimension 2 for each,
when the character is trivial on it, and 0 otherwise).  At the trivial character of N_c, three at a class of the c^j
eigenspace at its graded bound needs B_j <= n(1) - 2 (Corollary C') and n(rho) >= 3 (Theorem C (i)), with the eigenspace
non-empty.  The cusps of N where c^m is trivial are read off N_c itself: a cusp of N with c of order o under it has k / o cusps
of N_c above it.

    python3 corollary_check.py [--record]                ->  corollary_check.json
    python3 corollary_check.py --direct [--record]       ->  census_direct.json
The check on sm:B1542's record (--b1542, after its read-out): Corollary C' and the two facts C'' rests on at every one of its
readings, and the deck grading: at every eigenspace reading (Part B) rk delta1_W <= B_j, the graded bound graded_census.json
records for the cover (labels j and -j alike: B_j = B_-j on these covers), and at every reading rk delta1_W <= the global bound
min(h^1(N; C), n(rho)).

    python3 corollary_check.py [--record]                ->  corollary_check.json
    python3 corollary_check.py --direct [--record]       ->  census_direct.json
    python3 corollary_check.py --graded [--record]       ->  graded_census.json
The floor (--floor): at every banked reading of the frame that carries the count (sm:B1535's Part M, sm:B1536's Parts P and O,
sm:B1541, sm:B1542), whether I(W) >= -b0, and how often the line has interior classes there (n(nu^4) >= 1, where Theorem C
(ii) alone would allow I(W) down to -b0 - n(nu^4)).  An observation tallied, not a theorem.

    python3 corollary_check.py --b1542 [--record]        ->  b1542_check.json
    python3 corollary_check.py --floor [--record]        ->  floor.json"""
import gzip
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction as Fr
from math import lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1536V = ROOT / "frontier" / "B1536_the_finite_covers" / "verification"
B1540V = ROOT / "frontier" / "B1540_the_room_for_three" / "verification"
B1541V = ROOT / "frontier" / "B1541_the_count_on_the_room" / "verification"
B1542V = ROOT / "frontier" / "B1542_the_count_at_the_eisenstein_order" / "verification"


def lower_bound(x):
    return x["rk d1"]["E"] - x["b0"] - x["n(L)"]


def _tally(xs):
    """(readings, violations of C', equalities in C', violations of rk delta1_W <= n(V), violations of Theorem C (i))"""
    tot = bad = eq = kv = ci = 0
    for x in xs:
        tot += 1
        bad += x["count"][0] < lower_bound(x)
        eq += x["count"][0] == lower_bound(x)
        kv += x["rk d1"]["E"] > x["n(V)"]
        ci += not (-x["n((VL)*)"] <= x["count"][1] <= 0)
    return [tot, bad, eq, kv, ci]


def check_readings():
    """over every reading that carries the connecting ranks: Corollary C' (I(W) >= rk delta1_W - b0 - n(L)), and the two facts
    it and C'' rest on, re-read from the record: im delta1_W lies in K_V (rk delta1_W <= n(V)) and Theorem C (i)
    (-n(nu^3 rho) <= I(L2W) <= 0)"""
    xs = [json.loads(line)["reading"] for line in gzip.open(B1541V / "run.jsonl.gz", "rt")]
    out = {"columns": ["readings", "C' violations", "C' equalities", "rk delta1_W > n(V)", "Theorem C (i) violations"],
           "sm:B1541": _tally(xs)}
    xs = []
    for st in ("m004", "m003"):
        for route in ("N", "R"):
            for line in gzip.open(B1536V / f"run_{route}_{st}.jsonl.gz", "rt"):
                r = json.loads(line)
                if r.get("done"):
                    continue
                xs += ([r["P"]] if "P" in r else []) + [y for blk in (r.get("O") or []) for y in blk["readings"]]
    out["sm:B1536 Parts P and O"] = _tally(xs)
    return out


def b1541_ranks():
    """rk delta1_W by subspace in sm:B1541's record (route N), with h^1(N_45; C) = 9 = n(1) + #cusps"""
    out = {}
    for line in gzip.open(B1541V / "run.jsonl.gz", "rt"):
        r = json.loads(line)
        if r["route"] != "N":
            continue
        sub = r["subspace"]
        if sub.startswith("S="):
            sub = f"cusp strata with {len([x for x in sub[2:].split(',') if x])} free cusps"
        out.setdefault(f"{r['part']} {sub}", set()).add((r["reading"]["rk d1"]["E"], tuple(r["reading"]["count"])))
    return {k: sorted([a, list(b)] for a, b in v) for k, v in sorted(out.items())}


def _pulled_back_rooms():
    spec = importlib.util.spec_from_file_location("b1543_b1540_pulled_back_rooms", B1540V / "pulled_back_rooms.py")
    PB = importlib.util.module_from_spec(spec)
    if str(B1540V) not in sys.path:
        sys.path.insert(0, str(B1540V))
    spec.loader.exec_module(PB)
    return PB


def census_rows():
    """the cyclic covers N_c whose every power the banked rows fix, with Lemma A's (n(1), n(rho)) and the character c"""
    PB = _pulled_back_rooms()
    L = PB.L
    bk = {(route, st): PB.banked(route, st) for route in ("R", "N") for st in ("m004", "m003")}
    rows_out = []
    for st, cid, deg, n1, nr, cus in L.members():
        rows = {route: bk[(route, st)].get(cid, []) for route in ("R", "N")}
        S, perms, cov = L.cover(st, cid)
        ab = L.Ab(cov)
        M = 1
        for r in rows["R"] + rows["N"]:
            for x in list(r["u"]) + [r["kappa"]]:
                M = lcm(M, Fr(x).denominator)
        vals = {}
        for route in ("R", "N"):
            for r in rows[route]:
                u, k = (Fr(r["u"][0]), Fr(r["u"][1])), Fr(r["kappa"])
                for pw, field, kind in PB.FIELDS:
                    c = L.restrict(S, cov, ab, ((pw * u[0]) % 1, (pw * u[1]) % 1, (pw * k) % 1), M)
                    vals.setdefault(c, {}).setdefault(kind, set()).add(r["S"][field])
        fixed = {c: {kd: next(iter(v)) for kd, v in d.items() if len(v) == 1} for c, d in vals.items()}
        zero = tuple(0 for _ in ab.coords)
        seen = set()
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
                rows_out.append({"state": st, "cover": cid, "order": k, "degree": deg * k, "(n(1), n(rho))": [s1, s4],
                                 "criterion": 3 <= s4 <= s1 - 2, "c": list(c), "M": M})
    return rows_out


def census():
    rows_out = census_rows()
    dist = Counter(tuple(r["(n(1), n(rho))"]) for r in rows_out)
    return {"cyclic covers": len(rows_out), "(n(1), n(rho)) distribution": [[list(k), v] for k, v in sorted(dist.items())],
            "meeting 3 <= n(rho) <= n(1) - 2": [{x: y for x, y in r.items() if x not in ("c", "M")}
                                                for r in rows_out if r["criterion"]],
            "largest n(1) - n(rho)": max(r["(n(1), n(rho))"][0] - r["(n(1), n(rho))"][1] for r in rows_out),
            "largest n(1)": max(r["(n(1), n(rho))"][0] for r in rows_out)}


def census_direct(say=print):
    """every census cover read directly at its trivial character (no Lemma A), against Lemma A's sums"""
    import time
    L = _pulled_back_rooms().L
    out, t0 = [], time.time()
    for r in census_rows():
        S, perms, cov = L.cover(r["state"], r["cover"])
        pe, k = L.cyclic_cover(cov, L.Ab(cov), tuple(r["c"]), r["M"])
        assert k == r["order"]
        d = L.read_cover(S, pe)
        rN, rR = d["route N (prime, n(1), n(rho), capW, capL2)"], d["route R (prime, n(1), n(rho), capW, capL2)"]
        h1 = d["H_1 (free rank, torsion); b1 - cusps"]
        ok = bool(d["connected"] and d["degree"] == r["degree"] and rN[1:3] == rR[1:3] == r["(n(1), n(rho))"]
                  and h1[2] == rN[1])
        out.append({"state": r["state"], "cover": r["cover"], "order": k, "degree": d["degree"], "cusps": d["cusps"],
                    "Lemma A (n(1), n(rho))": r["(n(1), n(rho))"], "route N": rN, "route R": rR, "H_1; b1 - cusps": h1,
                    "agrees": ok})
        say(r["state"], r["cover"], k, d["degree"], r["(n(1), n(rho))"], rN[1:3], rR[1:3], h1[2], "ok" if ok else "DISAGREES",
            round(time.time() - t0, 1), "s")
    return {"covers": len(out), "all agree": all(x["agrees"] for x in out),
            "meeting 3 <= n(rho) <= n(1) - 2 (route N and route R)":
                [x for x in out if 3 <= x["route N"][2] <= x["route N"][1] - 2 or 3 <= x["route R"][2] <= x["route R"][1] - 2],
            "rows": out, "seconds": round(time.time() - t0, 1)}


def graded_census(say=print):
    """every census cover's deck eigenspaces: the graded bound B_j on rk delta1_W, the four's h^1 in each eigenspace, and the
    graded criterion for three at the trivial character of N_c"""
    PB = _pulled_back_rooms()
    L = PB.L
    bk = {(route, st): PB.banked(route, st) for route in ("R", "N") for st in ("m004", "m003")}
    cache, out = {}, []
    for r in census_rows():
        st, cid, k, M, c = r["state"], r["cover"], r["order"], r["M"], tuple(r["c"])
        if (st, cid, M) not in cache:
            S, perms, cov = L.cover(st, cid)
            ab = L.Ab(cov)
            vals = {}
            for route in ("R", "N"):
                for x in bk[(route, st)].get(cid, []):
                    u, kap = (Fr(x["u"][0]), Fr(x["u"][1])), Fr(x["kappa"])
                    for pw, field, kind in PB.FIELDS:
                        cc = L.restrict(S, cov, ab, ((pw * u[0]) % 1, (pw * u[1]) % 1, (pw * kap) % 1), M)
                        vals.setdefault(cc, {}).setdefault(kind, set()).add(x["S"][field])
            cache[(st, cid, M)] = (S, perms, cov, ab, vals)
        S, perms, cov, ab, vals = cache[(st, cid, M)]
        pw = [tuple((j * x) % M for x in c) for j in range(k)]
        assert all(len(vals[q]["line"]) == 1 and len(vals[q]["four"]) == 1 for q in pw)
        nL = [next(iter(vals[q]["line"])) for q in pw]
        n4 = [next(iter(vals[q]["four"])) for q in pw]
        assert [sum(nL), sum(n4)] == r["(n(1), n(rho))"]
        pe, kk = L.cyclic_cover(cov, ab, c, M)
        assert kk == k
        G = S["G"]
        up = [set(U["orbit"]) for U in L.CL.cusps(G, pe)]
        ords = []
        for D in L.CL.cusps(G, perms):
            pts = {x * k + i for x in D["orbit"] for i in range(k)}
            above = sum(1 for U in up if U & pts)
            assert k % above == 0
            ords.append(k // above)
        assert sum(k // o for o in ords) == len(up)
        triv = [sum(1 for o in ords if m % o == 0) for m in range(k)]
        h1L = [nL[m] + triv[m] for m in range(k)]
        h1four = [n4[j] + triv[j] for j in range(k)]
        n1, nr = sum(nL), sum(n4)
        B = [sum(min(h1L[m], n4[(j + m) % k]) for m in range(k)) for j in range(k)]
        meets = [j for j in range(k) if B[j] <= n1 - 2 and nr >= 3]
        out.append({"state": st, "cover": cid, "order": k, "(n(1), n(rho))": [n1, nr],
                    "orders of c on the cusps of N": ords, "line: n, h^1 by power": [nL, h1L],
                    "four: n, h^1 by power": [n4, h1four], "graded bounds B_j": B,
                    "eigenspaces meeting the graded criterion": meets,
                    "of them non-empty": [j for j in meets if h1four[j] > 0]})
        say(st, cid, k, [n1, nr], "h1L", h1L, "h1 four", h1four, "B", B, "meets", meets,
            "non-empty", [j for j in meets if h1four[j] > 0])
    return {"covers": len(out), "eigenspaces": sum(x["order"] for x in out),
            "meeting the graded criterion": [[x["state"], x["cover"], x["order"], x["eigenspaces meeting the graded criterion"]]
                                             for x in out if x["eigenspaces meeting the graded criterion"]],
            "meeting it and non-empty": [[x["state"], x["cover"], x["order"], x["of them non-empty"]]
                                         for x in out if x["of them non-empty"]],
            "rows": out}


def check_b1542():
    """Corollary C', rk delta1_W <= n(V) and Theorem C (i) at every reading of sm:B1542's record, and the deck grading's
    bounds: rk delta1_W <= B_j on every eigenspace reading, rk delta1_W <= min(h^1(N; C), n(rho)) on every reading"""
    g = json.loads((HERE / "graded_census.json").read_text())
    graded = {x["cover"]: x for x in g["rows"] if x["state"] == "m003" and x["order"] == 6}
    rows = [json.loads(line) for line in gzip.open(B1542V / "run.jsonl.gz", "rt") if line.strip()]
    xs = [r["reading"] for r in rows]
    out = {"columns": ["readings", "C' violations", "C' equalities", "rk delta1_W > n(V)", "Theorem C (i) violations"],
           "sm:B1542": _tally(xs)}
    bad_graded, bad_global, n_graded, by = [], [], 0, {}
    for r in rows:
        x, gc = r["reading"], graded[r["cover"]]
        rk = x["rk d1"]["E"]
        h1L, n4 = gc["line: n, h^1 by power"][1], gc["four: n, h^1 by power"][0]
        glob = min(sum(h1L), sum(n4))
        if rk > glob:
            bad_global.append([r["cover"], r["part"], r["subspace"], r["draw"], r["route"], rk, glob])
        if r["part"] == "B":
            j = int(r["subspace"].split()[0][2:])
            Bj = gc["graded bounds B_j"][j]
            assert Bj == gc["graded bounds B_j"][(-j) % 6]
            n_graded += 1
            if rk > Bj:
                bad_graded.append([r["cover"], r["subspace"], r["draw"], r["route"], rk, Bj])
            by.setdefault(f"{r['cover']} {r['subspace']}", set()).add((rk, Bj, tuple(x["count"])))
    out["eigenspace readings"] = n_graded
    out["rk delta1_W > B_j (graded bound)"] = bad_graded
    out["rk delta1_W > the global bound"] = bad_global
    out["eigenspace readings: (rk delta1_W, B_j, count) by subspace"] = {k: sorted([a, b, list(c)] for a, b, c in v)
                                                                       for k, v in sorted(by.items())}
    return out


def floor_tally():
    """I(W) against -b0 at every banked reading that carries the count"""
    B1535V = ROOT / "frontier" / "B1535_the_cap" / "verification"

    def gen():
        for line in gzip.open(B1535V / "part_m.jsonl.gz", "rt"):
            r = json.loads(line)
            for rt in ("RS p1", "RS p2"):
                x = r[rt]
                yield "sm:B1535 Part M", x["I(W)"], x["b0"], x["n(L)"]
        for st in ("m004", "m003"):
            for route in ("N", "R"):
                for line in gzip.open(B1536V / f"run_{route}_{st}.jsonl.gz", "rt"):
                    r = json.loads(line)
                    if r.get("done"):
                        continue
                    for x in ([r["P"]] if "P" in r else []) + [y for blk in (r.get("O") or []) for y in blk["readings"]]:
                        yield "sm:B1536 Parts P and O", x["count"][0], x["b0"], x["n(L)"]
        for src, path in (("sm:B1541", B1541V / "run.jsonl.gz"), ("sm:B1542", B1542V / "run.jsonl.gz")):
            for line in gzip.open(path, "rt"):
                if line.strip():
                    x = json.loads(line)["reading"]
                    yield src, x["count"][0], x["b0"], x["n(L)"]
    out = {}
    for src, w, b0, nL in gen():
        row = out.setdefault(src, {"readings": 0, "I(W) = -b0": 0, "I(W) < -b0": 0, "with n(nu^4) >= 1": 0,
                                   "lowest I(W) + b0": None})
        row["readings"] += 1
        row["I(W) = -b0"] += w == -b0
        row["I(W) < -b0"] += w < -b0
        row["with n(nu^4) >= 1"] += nL >= 1
        row["lowest I(W) + b0"] = w + b0 if row["lowest I(W) + b0"] is None else min(row["lowest I(W) + b0"], w + b0)
    return {"by record": out, "readings": sum(r["readings"] for r in out.values()),
            "below the floor": sum(r["I(W) < -b0"] for r in out.values())}


def main():
    if "--floor" in sys.argv:
        rep = floor_tally()
        print(json.dumps(rep, indent=1))
        if "--record" in sys.argv:
            (HERE / "floor.json").write_text(json.dumps(rep, indent=1) + "\n")
        return rep
    if "--b1542" in sys.argv:
        rep = check_b1542()
        print(json.dumps(rep, indent=1, default=str))
        if "--record" in sys.argv:
            (HERE / "b1542_check.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
        return rep
    if "--graded" in sys.argv:
        rep = graded_census(say=lambda *a: print(*a, flush=True))
        print(json.dumps({k: v for k, v in rep.items() if k != "rows"}, indent=1, default=str))
        if "--record" in sys.argv:
            (HERE / "graded_census.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
        return rep
    if "--direct" in sys.argv:
        rep = census_direct(say=lambda *a: print(*a, flush=True))
        print(json.dumps({k: v for k, v in rep.items() if k != "rows"}, indent=1, default=str))
        if "--record" in sys.argv:
            (HERE / "census_direct.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
        return rep
    rep = {"Corollary C' on the banked readings": check_readings(), "sm:B1541's rk delta1_W by subspace": b1541_ranks(),
           "the census of cyclic covers": census()}
    print(json.dumps(rep, indent=1, default=str))
    if "--record" in sys.argv:
        (HERE / "corollary_check.json").write_text(json.dumps(rep, indent=1, default=str) + "\n")
    return rep


if __name__ == "__main__":
    main()
