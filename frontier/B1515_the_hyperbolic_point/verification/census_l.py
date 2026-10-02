"""B1515 -- THE SEALED CENSUS, route L (the owner's rule's independent route).  Run after route T:
python3 census_l.py --record  ->  census_l_run.txt (log: census_l_log.txt).

Route L shares no code with route T (route_l.py's header; the lock asserts it).  It reads the same populations with its own
presentation (the mapping torus G_n = <x, y, t>), its own character enumeration, its own elimination and the joint-system interior
dimension, at three primes per level below 2^22 (route T's lie above 2^23), and exactly over Q(zeta_12) at levels 1 and 3.

Part 0  the banked identity (stops the run if it fails): K2 exactly and the positive control R40 on m010 exactly.
Part A  population A (lam = 1), every fibre character of M_1-M_6.
Part B  population B (lam = -1, i, -i, w, w^2): the member test, and every member read in full.
Part C  route L's own D-checks, and the comparison with route T's record (census_t_run.txt), key by key (level, character, lam):
        every dimension (a0, h1, t0, n, b0, h1*, s0, n*) and every index, zero and non-zero."""
import json
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import route_l as RL  # noqa: E402

RECORD, LOG = HERE / "census_l_run.txt", HERE / "census_l_log.txt"
ROUTE_T_RECORD = HERE / "census_t_run.txt"
PRIMES_PER_LEVEL = 3
START = 2 ** 22 - 104729
LAMS = [("1", Fr(0)), ("-1", Fr(1, 2)), ("i", Fr(1, 4)), ("-i", Fr(3, 4)), ("w", Fr(1, 3)), ("w^2", Fr(2, 3))]


def primes_L(K, count, start):
    out, p = [], start
    while len(out) < count:
        p = int(sp.prevprime(p))
        if (p - 1) % K == 0:
            out.append(p)
    return out


def sig(s):
    """(a0, h1, t0, n, b0, h1*, s0, n*, I)"""
    return s["E(a0,h1,t0,n)"] + s["E*(b0,h1,s0,n)"] + [s["I"]]


def primary(d):
    return d["c1"] if len(d) == 1 else d["generic"]


def row_signature(row):
    s = {"h1(V_eta)": row["h1(V_eta)"]}
    if "pieces" not in row:
        return s
    s["pieces"] = {k: sig(v) for k, v in row["pieces"].items()}
    s["case"], s["h1(V_eta*)"] = row["case"], row["h1(V_eta*)"]
    w = primary(row["W1"])
    s["W1"], s["L2W1"] = sig(w["W1"]), sig(w["L2W1"])
    w2 = primary(row["W2"])
    s["W2"] = [w2["I(W2)"], w2["I(L2W2)"]]
    return s


def lab(ab):
    return [str(ab[0]), str(ab[1])]


def deck_orbit(ab):
    orb, cur = [ab], RL.deck_image(ab)
    while cur != ab:
        orb.append(cur)
        cur = RL.deck_image(cur)
    return orb


def part0(log):
    F = RL.Exact(RL.K12, "Q(zeta12)")
    G = RL.rho1(F, 1)
    k2 = {"h1(rho1)": RL.dims(G)["h1"], "h1(rho1*)": RL.dims(G.dual())["h1"], "h1(L2 rho1)": RL.dims(G.wedge2())["h1"]}
    r40 = {k: RL.summary(RL.index(m)) for k, m in RL.m010_modules(F, F.s((1 + sp.sqrt(-3)) / 2)).items()}
    ok = k2 == {"h1(rho1)": 1, "h1(rho1*)": 1, "h1(L2 rho1)": 2} and all(r40[k]["I"] == 1 for k in ("V", "L2V", "W", "L2W"))
    log(f"Part 0: {k2}; R40 I = {[r40[k]['I'] for k in ('V', 'L2V', 'W', 'L2W')]}; passed = {ok}")
    return {"K1/K2": k2, "R40 exact": r40, "passed": ok}


def read_level(n, fields, log, t0):
    chars, D = RL.fibre_characters(n)
    reps, seen = [], set()
    for ab in chars:
        if ab not in seen:
            reps.append(ab)
            seen.update(deck_orbit(ab))
    A_rows, B_rows = [], []
    for tag, F, U, reps_only in fields:
        rho = RL.rho1(F, n)
        assert rho.holds()
        for ab in (reps if reps_only else chars):
            for lname, lam in LAMS:
                if lname == "1":
                    row = RL.read_member(F, U, n, rho, ab, lam)
                    A_rows.append({"level": n, "field": tag, "char": lab(ab), "lam": lname, "row": row})
                else:
                    row = RL.read_member(F, U, n, rho, ab, lam, full=False)
                    if row["h1(V_eta)"] >= 1:
                        row = RL.read_member(F, U, n, rho, ab, lam)
                    B_rows.append({"level": n, "field": tag, "char": lab(ab), "lam": lname, "row": row})
        log(f"[{time.time() - t0:8.1f}s] M{n} {tag}: {len(reps if reps_only else chars)} characters read")
    return A_rows, B_rows


def sig_T(b):
    a0, a1, t0, r1 = b["E(a0,a1,t0,r1)"]
    b0, b1, s0, q1 = b["E*(b0,b1,s0,q1)"]
    return [a0, a1, t0, a1 - r1, b0, b1, s0, b1 - q1, b["I"]]


def row_signature_T(row):
    """route T's record in route L's signature (route T's r1 is the rank of the restriction, so n = a1 - r1)"""
    s = {"h1(V_eta)": row["h1(V_eta)"]}
    if "pieces" not in row:
        return s
    s["pieces"] = {k: sig_T(v) for k, v in row["pieces"].items()}
    s["case"], s["h1(V_eta*)"] = row["case"], row["h1(V_eta*)"]
    w = primary(row["W1"])
    s["W1"], s["L2W1"] = sig_T(w["W1"]), sig_T(w["L2W1"])
    w2 = primary(row["W2"])
    s["W2"] = [w2["I(W2)"], w2["I(L2W2)"]]
    return s


def part_c(rec):
    out = {}
    rows = rec["A"] + rec["B"]
    by_key = {}
    for r in rows:
        by_key.setdefault((r["level"], tuple(r["char"]), r["lam"]), []).append(json.dumps(row_signature(r["row"]), sort_keys=True))
    out["route L: every field reads the same"] = all(len(set(v)) == 1 for v in by_key.values())
    deck_ok = True
    for (n, ch, lam), v in by_key.items():
        for o in deck_orbit((Fr(ch[0]), Fr(ch[1]))):
            k2 = (n, tuple(lab(o)), lam)
            if k2 in by_key and by_key[k2][0] != v[0]:
                deck_ok = False
    out["route L: readings constant on deck orbits"] = deck_ok
    full = [r for r in rows if "pieces" in r["row"]]
    out["route L: pieces have index 0"] = all(v["I"] == 0 for r in full for v in r["row"]["pieces"].values())
    lamk = {"1": 0, "-1": 6, "i": 3, "-i": 9, "w": 4, "w^2": 8}
    out["route L: indices vanish off mu_4 (W) and off mu_2 u mu_3 (Lambda^2 W)"] = all(
        (lamk[r["lam"]] in (0, 3, 6, 9) or all(v["W1"]["I"] == 0 for v in r["row"]["W1"].values()))
        and (lamk[r["lam"]] in (0, 6, 4, 8) or all(v["L2W1"]["I"] == 0 for v in r["row"]["W1"].values())) for r in full)
    uniq = [r for r in full if r["row"]["h1(V_eta)"] == 1 and r["row"]["h1(V_eta*)"] == 1]
    out["route L: mirror I(W2) = -I(W1), I(L2W2) = -I(L2W1)"] = all(
        r["row"]["W2"]["c1"]["I(W2)"] == -r["row"]["W1"]["c1"]["W1"]["I"] and r["row"]["W2"]["c1"]["I(L2W2)"] == -r["row"]["W1"]["c1"]["L2W1"]["I"]
        for r in uniq)
    out["route L: the classes read, where h^1(V_eta) >= 2"] = [
        {"level": r["level"], "field": r["field"], "char": r["char"], "lam": r["lam"],
         "(I(W1), I(L2W1)) by class": {c: [v["W1"]["I"], v["L2W1"]["I"]] for c, v in r["row"]["W1"].items()}}
        for r in full if r["row"]["h1(V_eta)"] >= 2]
    out["route L: P4 I(Lambda^2 W1) = 0 at every member"] = all(v["L2W1"]["I"] == 0 for r in full for v in r["row"]["W1"].values())
    both = [{"level": r["level"], "field": r["field"], "char": r["char"], "lam": r["lam"], "class": c, "I(W1)": v["W1"]["I"], "I(L2W1)": v["L2W1"]["I"]}
            for r in full for c, v in r["row"]["W1"].items() if v["W1"]["I"] != 0 and v["L2W1"]["I"] != 0]
    out["route L: P5 no member with both"] = not both
    out["route L: members with both"] = both
    out["route L: population B members"] = [{"level": r["level"], "char": r["char"], "lam": r["lam"]} for r in rec["B"] if r["row"]["h1(V_eta)"] >= 1]
    # the comparison with route T
    if not ROUTE_T_RECORD.exists():
        out["comparison with route T"] = "route T's record is missing"
        return out
    recT = json.loads(ROUTE_T_RECORD.read_text())
    sigT = {}
    for r in recT["A"] + recT["B"]:
        sigT.setdefault((r["level"], tuple(r["char"]), r["lam"]), set()).add(json.dumps(row_signature_T(r["row"]), sort_keys=True))
    keysL = set(by_key)
    keysT = set(sigT)
    disagree = []
    for k in sorted(keysL & keysT, key=str):
        if set(by_key[k]) != sigT[k]:
            disagree.append({"key": list(k), "route L": sorted(set(by_key[k])), "route T": sorted(sigT[k])})
    primesT = {p for v in recT["primes"].values() for p in v}
    primesL = {p for v in rec["primes"].values() for p in v}
    out["comparison with route T"] = {
        "keys read by both": len(keysL & keysT), "keys only in route L": len(keysL - keysT), "keys only in route T": len(keysT - keysL),
        "disagreements": disagree, "agree everywhere": not disagree and keysL == keysT,
        "primes disjoint": not (primesT & primesL)}
    return out


def main():
    t0 = time.time()
    lines = []

    def log(msg):
        print(msg, flush=True)
        lines.append(msg)
    rec = {"route": "L", "Part 0": part0(log)}
    if not rec["Part 0"]["passed"]:
        log("Part 0 FAILED: nothing of the census is read")
        if "--record" in sys.argv:
            RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
        return rec
    rec["A"], rec["B"], rec["primes"] = [], [], {}
    for n in range(1, 7):
        D = RL.fibre_characters(n)[1]
        K = RL.lcm(D, 12)
        ps = primes_L(K, PRIMES_PER_LEVEL, START - 6911 * n)
        rec["primes"][f"M{n}"] = ps
        fields = []
        for p in ps:
            F = RL.ModP(p, f"GF({p})")
            fields.append((f"GF({p})", F, RL.Units(F, K), False))
        if n in (1, 3):
            F = RL.Exact(RL.K12, "Q(zeta12)")
            fields.append(("exact", F, RL.Units(F, 12), True))
        a, b = read_level(n, fields, log, t0)
        rec["A"] += a
        rec["B"] += b
    rec["C"] = part_c(rec)
    rec["seconds"] = round(time.time() - t0, 1)
    log(json.dumps({k: v for k, v in rec["C"].items() if k != "comparison with route T"}, indent=1, default=str))
    comp = rec["C"]["comparison with route T"]
    log(json.dumps(comp if isinstance(comp, str) else {k: v for k, v in comp.items() if k != "disagreements"}, indent=1))
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
        LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return rec


if __name__ == "__main__":
    main()
