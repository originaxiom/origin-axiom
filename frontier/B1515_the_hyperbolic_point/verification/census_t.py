"""B1515 -- THE SEALED CENSUS, route T.  Run after the seal: python3 census_t.py --record  ->  census_t_run.txt (log: census_t_log.txt).

Part 0  the banked identity (the run stops if it fails): K2 exactly (h^1(m004; rho_1) = h^1(m004; rho_1*) = 1), K1 at level 1
        (h^1(Lambda^2 rho_1) = 2), and the positive control R40 on m010 exactly (I = +1 on V, Lambda^2 V, W and Lambda^2 W).
Part A  population A: every fibre character of every level M_1-M_6 at lam = 1.  Over GF(p) at two primes per level (every character)
        and exactly over Q(zeta_12) at levels 1 and 3 (one character per deck orbit).
Part B  population B: every fibre character at lam = -1, i, -i, w, w^2.  The member test h^1(V_eta) at both primes (exactly at levels 1
        and 3, one character per deck orbit); every member found is read in full.
Part C  the D-checks and the readings of P1-P5 (PREREGISTRATION Section 6)."""
import json
import sys
import time
from fractions import Fraction as Fr
from math import gcd
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import route_t as RT  # noqa: E402

T = RT.T
RECORD, LOG = HERE / "census_t_run.txt", HERE / "census_t_log.txt"
PRIMES_PER_LEVEL = 2
START = 2 ** 24 - 104729                 # route T's primes lie in (2^23, 2^24); route L's lie below 2^22
LAM_B = [lk for lk, _ in RT.LAMBDAS if lk != 0]
LAM_NAME = dict(RT.LAMBDAS)
MU4, MU2_MU3 = {0, 3, 6, 9}, {0, 6, 4, 8}


def primes_T(K, count, start):
    out, p = [], start
    while len(out) < count:
        p = int(sp.prevprime(p))
        if (p - 1) % K == 0:
            out.append(p)
    return out


def label(ab, N):
    return [str(Fr(ab[0], N)), str(Fr(ab[1], N))]


def sig(b):
    """(a0, h1, t0, n, b0, h1*, s0, n*, I) of one module"""
    a0, a1, t0, r1 = b["E(a0,a1,t0,r1)"]
    b0, b1, s0, q1 = b["E*(b0,b1,s0,q1)"]
    return [a0, a1, t0, a1 - r1, b0, b1, s0, b1 - q1, b["I"]]


def primary(d):
    """the class read for a member's verdict: the unique class, or the fixed generic combination when h^1 >= 2"""
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


def part0(log):
    lev = RT.Level(1)
    A = RT.Arith("exact", 12)
    R = T.DMRep(lev.cov["gens"], T.rs_rho(lev.cov, A.field))
    k2 = {"h1(rho1)": T.h1_classes(R, lev.rels)[1], "h1(rho1*)": T.h1_classes(R.dual(), lev.rels)[1],
          "h1(L2 rho1)": T.h1_classes(T.wedge2_rep(R), lev.rels)[1]}
    r40 = RT.m010_indices(A, (1 + sp.sqrt(-3)) / 2)
    ok = k2 == {"h1(rho1)": 1, "h1(rho1*)": 1, "h1(L2 rho1)": 2} and all(r40[k]["I"] == 1 for k in ("V", "L2V", "W", "L2W"))
    log(f"Part 0: {k2}; R40 I = {[r40[k]['I'] for k in ('V', 'L2V', 'W', 'L2W')]}; passed = {ok}")
    return {"K1/K2": k2, "R40 exact": r40, "passed": ok}


def read_level(n, arith_list, reps_only, log, t0):
    """Part A and Part B on one level, for every field in arith_list"""
    lev = RT.Level(n)
    reps = [o[0] for o in T.orbits(lev.chars, lev.N)]
    A_rows, B_rows = [], []
    for tag, A in arith_list:
        rho = T.rs_rho(lev.cov, A.field)
        chars = reps if reps_only.get(tag) else lev.chars
        for ab in chars:
            row = RT.read_member(lev, A, rho, ab, 0)
            A_rows.append({"level": n, "field": tag, "char": label(ab, lev.N), "lam": "1", "row": row})
            for lk in LAM_B:
                rb = RT.read_member(lev, A, rho, ab, lk, full=False)
                if rb["h1(V_eta)"] >= 1:
                    rb = RT.read_member(lev, A, rho, ab, lk)
                B_rows.append({"level": n, "field": tag, "char": label(ab, lev.N), "lam": LAM_NAME[lk], "row": rb})
        log(f"[{time.time() - t0:8.1f}s] M{n} {tag}: {len(chars)} characters read")
    return A_rows, B_rows


# ============================================================================================ Part C
def deck_orbit(ab, N):
    orb, cur = [tuple(x % N for x in ab)], T.deck(ab, N)
    while cur != orb[0]:
        orb.append(cur)
        cur = T.deck(cur, N)
    return orb


def full_members(rows):
    return [r for r in rows if "pieces" in r["row"]]


def part_c(rec):
    A, B = rec["A"], rec["B"]
    out, D = {}, {}
    fullA, fullB = full_members(A), full_members(B)
    allfull = fullA + fullB
    lams = {"1": 0, "-1": 6, "i": 3, "-i": 9, "w": 4, "w^2": 8}
    # D2 (Lemma 2) and D3 (Lemma 3)
    D["D2 pieces: I = 0 and r1 = (t0 + s0)/2"] = all(
        v["I"] == 0 and 2 * v["E(a0,a1,t0,r1)"][3] == v["E(a0,a1,t0,r1)"][2] + v["E*(b0,b1,s0,q1)"][2]
        for r in allfull for v in r["row"]["pieces"].values())
    D["D3 Lambda^2 V: n = n* = 0; h1 = 2 at lam = +-1, else 0"] = all(
        sig(r["row"]["pieces"]["L2V"])[3] == 0 and sig(r["row"]["pieces"]["L2V"])[7] == 0
        and sig(r["row"]["pieces"]["L2V"])[1] == (2 if r["lam"] in ("1", "-1") else 0) for r in allfull)
    # D4 (Lemma 5)
    D["D4 indices vanish off mu_4 (W) and off mu_2 u mu_3 (Lambda^2 W)"] = all(
        (lams[r["lam"]] in MU4 or all(v["W1"]["I"] == 0 for v in r["row"]["W1"].values()) and all(v["I(W2)"] == 0 for v in r["row"]["W2"].values()))
        and (lams[r["lam"]] in MU2_MU3 or all(v["L2W1"]["I"] == 0 for v in r["row"]["W1"].values()) and all(v["I(L2W2)"] == 0 for v in r["row"]["W2"].values()))
        for r in allfull)
    simple = [r for r in fullA if r["row"].get("simple")]
    # D5 (Lemma 1's torus table read in the census)
    D["D5 torus table at simple members: W1 (t0, s0) = (1, 2), Lambda^2 W1 (2, 3)"] = all(
        (v["W1"]["E(a0,a1,t0,r1)"][2], v["W1"]["E*(b0,b1,s0,q1)"][2]) == (1, 2)
        and (v["L2W1"]["E(a0,a1,t0,r1)"][2], v["L2W1"]["E*(b0,b1,s0,q1)"][2]) == (2, 3)
        for r in simple for v in r["row"]["W1"].values())
    # D6 (Lemma 7, the mirror) where both classes are unique
    uniq = [r for r in allfull if r["row"]["h1(V_eta)"] == 1 and r["row"]["h1(V_eta*)"] == 1]
    D["D6 mirror: I(W2) = -I(W1), I(L2W2) = -I(L2W1)"] = all(
        r["row"]["W2"]["c1"]["I(W2)"] == -r["row"]["W1"]["c1"]["W1"]["I"] and r["row"]["W2"]["c1"]["I(L2W2)"] == -r["row"]["W1"]["c1"]["L2W1"]["I"]
        for r in uniq)
    # D7 (Lemma 8) at every simple lam = 1 member, and its consequences
    lev_N = {n: RT.Level(n).N for n in range(1, 7)}

    def ab_of(r):
        N = lev_N[r["level"]]
        return tuple(int(Fr(x) * N) for x in r["char"]), N

    def coincident(r):
        ab, N = ab_of(r)
        return tuple((5 * x) % N for x in ab) in deck_orbit(ab, N)
    mech = [(r, v) for r in simple for v in r["row"]["W1"].values()]
    D["D7 Lemma 8: I(W1) = 1 - b0 - rho and I(L2W1) = bit at every simple member"] = all(
        v["mechanism"]["Lemma 8 I(W1) = 1 - b0 - rho"] and v["mechanism"]["Lemma 8 I(L2W1) = bit"] for _, v in mech)
    D["D7 case (a) simple members: I(W1) = 0"] = all(v["W1"]["I"] == 0 for r, v in mech if r["row"]["case"] == "a")
    D["D7 deck-coincident case (b) simple members: rho = 0, I(W1) = 1"] = all(
        v["mechanism"]["rho"] == 0 and v["W1"]["I"] == 1 for r, v in mech if r["row"]["case"] == "b" and coincident(r))
    D["Remark 9 (proved half): e ^ c|P lies in pi_A at every simple member"] = all(v["mechanism"]["e ^ c|P in pi_A"] for _, v in mech)
    # D8 deck and Galois invariance, D10 the fields agree (route T's own rows)
    by_key = {}
    for r in A + B:
        by_key.setdefault((r["level"], tuple(r["char"]), r["lam"]), []).append(json.dumps(row_signature(r["row"]), sort_keys=True))
    D["D10 every field (both primes, and exact at levels 1 and 3) reads the same"] = all(len(set(v)) == 1 for v in by_key.values())
    sig_of = {k: v[0] for k, v in by_key.items()}
    deck_ok, gal_ok = True, True
    for (n, ch, lam), s in sig_of.items():
        N = lev_N[n]
        ab = tuple(int(Fr(x) * N) for x in ch)
        for o in deck_orbit(ab, N):
            k2 = (n, tuple(label(o, N)), lam)
            if k2 in sig_of and sig_of[k2] != s:
                deck_ok = False
        if lam == "1":
            for kk in range(1, N + 1):
                if gcd(kk, N) == 1:
                    k2 = (n, tuple(label(((kk * ab[0]) % N, (kk * ab[1]) % N), N)), lam)
                    if k2 in sig_of and sig_of[k2] != s:
                        gal_ok = False
    D["D8 readings constant on deck orbits"] = deck_ok
    D["D8 readings constant on Galois orbits (lam = 1; complex conjugation included)"] = gal_ok
    # D9 the trivial fibre character
    triv = [r for r in fullA if r["char"] == ["0", "0"]]
    D["D9 trivial fibre character: simple, case (a), I(W1) = 0 on every level"] = len({r["level"] for r in triv}) == 6 and all(
        r["row"]["simple"] and r["row"]["case"] == "a" and primary(r["row"]["W1"])["W1"]["I"] == 0 for r in triv)
    D["D9 trivial fibre character: no member off lam = 1"] = all(r["row"]["h1(V_eta)"] == 0 for r in B if r["char"] == ["0", "0"])
    out["D"] = D
    # the predictions
    P = {}
    P["P1 every lam = 1 member is simple"] = all(r["row"].get("simple") for r in fullA) and len(fullA) == len(A)
    membersB = [r for r in B if r["row"]["h1(V_eta)"] >= 1]
    P["P2 population B is empty"] = not membersB
    nonco = [(r, v) for r, v in mech if r["row"]["case"] == "b" and not coincident(r)]
    P["P3 off the deck coincidence, simple case (b): I(W1) = 0"] = all(v["W1"]["I"] == 0 for _, v in nonco)
    P["P4 I(Lambda^2 W1) = 0 at every member (every class read)"] = all(v["L2W1"]["I"] == 0 for r in allfull for v in r["row"]["W1"].values())
    P["P4 mechanism: Lambda_A meets pi_A in 0 at every simple member"] = all(v["mechanism"]["Lambda_A meets pi_A in 0"] for _, v in mech)
    both = [{"level": r["level"], "field": r["field"], "char": r["char"], "lam": r["lam"], "class": c, "I(W1)": v["W1"]["I"], "I(L2W1)": v["L2W1"]["I"]}
            for r in allfull for c, v in r["row"]["W1"].items() if v["W1"]["I"] != 0 and v["L2W1"]["I"] != 0]
    P["P5 no member carries both a non-zero I(W1) and a non-zero I(Lambda^2 W1)"] = not both
    out["P"] = P
    out["members with both"] = both
    # the readings
    tab = {}
    for n in range(1, 7):
        rows = [r for r in fullA if r["level"] == n and r["field"] != "exact"]
        f0 = sorted({r["field"] for r in rows})[:1]
        rows = [r for r in rows if r["field"] in f0]
        dist = {}
        for r in rows:
            v = primary(r["row"]["W1"])
            key = f"case {r['row']['case']}, simple {bool(r['row'].get('simple'))}, coincident {coincident(r)}: (I(W1), I(L2W1)) = ({v['W1']['I']}, {v['L2W1']['I']})"
            dist[key] = dist.get(key, 0) + 1
        tab[f"M{n}"] = {"members (lam = 1)": len(rows), "distribution": dist,
                        "prop E ranges W1": sorted({tuple(primary(r["row"]["W1"])["W1"]["prop E range"]) for r in rows}),
                        "prop E ranges L2W1": sorted({tuple(primary(r["row"]["W1"])["L2W1"]["prop E range"]) for r in rows})}
    out["table (one prime per level)"] = tab
    out["population B members"] = [{"level": r["level"], "field": r["field"], "char": r["char"], "lam": r["lam"],
                                    "signature": row_signature(r["row"])} for r in membersB]
    out["the classes read, where h^1(V_eta) >= 2"] = [
        {"level": r["level"], "field": r["field"], "char": r["char"], "lam": r["lam"],
         "(I(W1), I(L2W1)) by class": {c: [v["W1"]["I"], v["L2W1"]["I"]] for c, v in r["row"]["W1"].items()}}
        for r in allfull if r["row"]["h1(V_eta)"] >= 2]
    return out


def main():
    t0 = time.time()
    lines = []

    def log(msg):
        print(msg, flush=True)
        lines.append(msg)
    rec = {"route": "T", "Part 0": part0(log)}
    if not rec["Part 0"]["passed"]:
        log("Part 0 FAILED: nothing of the census is read")
        if "--record" in sys.argv:
            RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
        return rec
    rec["A"], rec["B"], rec["primes"] = [], [], {}
    for n in range(1, 7):
        lev = RT.Level(n)
        ps = primes_T(lev.K, PRIMES_PER_LEVEL, START - 7919 * n)
        rec["primes"][f"M{n}"] = ps
        arith = [(f"GF({p})", RT.Arith("gf", lev.K, p=p)) for p in ps]
        reps_only = {}
        if n in (1, 3):
            arith.append(("exact", RT.Arith("exact", 12)))
            reps_only["exact"] = True
        a, b = read_level(n, arith, reps_only, log, t0)
        rec["A"] += a
        rec["B"] += b
    rec["C"] = part_c(rec)
    rec["seconds"] = round(time.time() - t0, 1)
    log(json.dumps({"D": rec["C"]["D"], "P": rec["C"]["P"]}, indent=1))
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
        LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return rec


if __name__ == "__main__":
    main()
