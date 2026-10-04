#!/usr/bin/env python3
"""B1539 -- THE READ-OUT (PREREGISTRATION.md sections 7 and 9): the predictions from the records, once.

    python3 read_out.py [--record]    ->  read_out.json, read_out_log.txt

Inputs: identity.json (the banked identity, checked before the run), run_R.jsonl, run_P.jsonl, run_N.jsonl, and the population
by structure (population.py: every member's m, its Galois orbits and its sampled orbits).  evaluate() is pure: control K6 calls
it on synthetic rows.

Coverage: the records are complete only if, in each of routes R' and P', every member's every orbit representative is read
exactly once, every member of every sampled orbit is read exactly once, and route N has read every cover the sealed rule
selects, once.  A prediction that a found row can refute is False on that row whatever the coverage; a population-wide one is
True only on complete records, else None.  A positive (P4-P7) needs both routes.

  P1  routes R' and P' agree at every reading (every field of the frame and both supplies).
  P2  Lemma C: on every sampled orbit, every member's reading equals the representative's, in each route.
  P3  route N's (n(1), n(rho)) on every cover it reads equals Lemma A''s sums, in both routes.
  P4  some member has room for three (min(1 + n(1), n(rho)) >= 3) on an abelian cover of exponent dividing m: on N_m, by Lemma
      A''s sums over all its characters, in both routes.
  P4c some member has room for three on a cyclic cover N_c (Lemma A's sums), in both routes.
  P5  on d5.2 or d5.3, some own character of order 3 has n(c) >= 1 and n(rho c) >= 1, in both routes.
  P6  some own character of the population has min(capW, capL2) >= 3 at nu = c itself, in both routes.
  P7  the line grows: some member has an own character c != 1 with n(c) >= 1, in both routes."""
import json
import sys
import zlib
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _sib(alias, name):
    """this arc's own modules, by path under unique names (E12: sm:B1536's route_r puts sm:B1535's folder, with its own
    read_out.py and controls.py, first on sys.path, and sm:B1536's has its own population.py and run.py)"""
    import importlib.util
    if alias not in sys.modules:
        spec = importlib.util.spec_from_file_location(alias, HERE / name)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        spec.loader.exec_module(mod)
    return sys.modules[alias]


ROOM = 3
N_CAP = 240          # route N reads a selected abelian cover only if its degree is at most N_CAP
N_SAMPLE = 200       # route N's outcome-blind sample: crc32 = 0 mod N_SAMPLE among the cyclic subgroups within N_CAP
LINE, FOUR = "n(nu)", "n(rho nu)"
FRAME = ("h1(V_eta)", "n(V_eta)", "b0", "n(L)", "n((VL)*)", "capW", "capL2", "n(nu)", "h1(nu)", "n(rho nu)", "h1(rho nu)")


def units(m):
    return [a for a in range(1, m + 1) if gcd(a, m) == 1]


def order_of(c, m):
    g = m
    for x in c:
        g = gcd(g, x)
    return m // g


def phi(d):
    return len(units(d))


def rep_of(c, m, U=None):
    """the least member of c's Galois orbit"""
    return min(tuple((a * x) % m for x in c) for a in (U or units(m)))


def room(n1, nr):
    return min(1 + n1, nr)


class Member:
    """one member's readings in one route, at its orbit representatives: S[rep] = the reading"""

    def __init__(self, m, S):
        self.m, self.S, self.U, self._rep = m, S, units(m), {}

    def rep(self, c):
        c = tuple(c)
        if c not in self._rep:
            self._rep[c] = rep_of(c, self.m, self.U)
        return self._rep[c]

    def n(self, c, f):
        return self.S[self.rep(c)][f]

    def cyclic(self, c):
        """Lemma A, with Lemma C: (n(1), n(rho)) of N_c = sum over d | k of phi(d) n at the order-d subgroup's generators"""
        k, m = order_of(c, self.m), self.m
        out = []
        for f in (LINE, FOUR):
            out.append(sum(phi(d) * self.n(tuple((k // d) * x % m for x in c), f) for d in range(1, k + 1) if k % d == 0))
        return tuple(out)

    def total(self, sizes):
        """Lemma A' on N_m: the sums over every character of order dividing m (sizes: rep -> orbit size)"""
        return tuple(sum(s * self.S[c][f] for c, s in sizes.items()) for f in (LINE, FOUR))

    def abelian(self, chars):
        """Lemma A' on N_A: the sums over the characters of A-hat"""
        return tuple(sum(self.n(c, f) for c in chars) for f in (LINE, FOUR))


def subgroup(gens, m):
    if not gens:
        return set()
    zero = tuple(0 for _ in gens[0])
    S, fr = {zero}, [zero]
    while fr:
        nxt = []
        for v in fr:
            for g in gens:
                w = tuple((a + b) % m for a, b in zip(v, g))
                if w not in S:
                    S.add(w)
                    nxt.append(w)
        fr = nxt
    return S


def witness(mR, mP, deg, cap=10 ** 4):
    """the sealed witness rule, for a member with room for three on N_m in both routes: start from no generator; at each step add
    the candidate (an orbit representative c != 1 with a positive supply in both routes, in the order (order, c)) that most
    reduces the deficit max(0, 2 - n(1)) + max(0, 3 - n(rho)) of both routes' sums (the larger of the two), ties to the least
    |A-hat|, then the order; at most four generators, |A-hat| <= cap.  Returns (gens, |A-hat|, degree, (sums R, sums P)) or None."""
    m = mR.m
    cand = sorted((c for c in mR.S if any(c) and (min(mR.S[c][LINE], mP.S[c][LINE]) >= 1 or
                                                 min(mR.S[c][FOUR], mP.S[c][FOUR]) >= 1)),
                  key=lambda c: (order_of(c, m), c))

    def deficit(chars):
        worst = 0
        for mm in (mR, mP):
            n1, nr = mm.abelian(chars)
            worst = max(worst, max(0, 2 - n1) + max(0, 3 - nr))
        return worst
    gens, chars = [], {tuple(0 for _ in next(iter(mR.S)))}
    cur = deficit(chars)
    while cur > 0 and len(gens) < 4:
        best = None
        for c in cand:
            if c in chars:
                continue
            H = subgroup(gens + [c], m)
            if len(H) > cap:
                continue
            key = (deficit(H), len(H), order_of(c, m), c)
            if best is None or key < best[0]:
                best = (key, c, H)
        if best is None or best[0][0] >= cur:
            return None
        gens, chars, cur = gens + [best[1]], best[2], best[0][0]
    if cur > 0:
        return None
    return gens, len(chars), deg * len(chars), (mR.abelian(chars), mP.abelian(chars))


def blind_selection(structure):
    """route N's outcome-blind covers: every cyclic subgroup of order 2 or 3 on the covers of degree 5 and 9, and a fixed sample
    (crc32 = 0 mod N_SAMPLE) of the cyclic subgroups whose cover has degree at most N_CAP.  structure: {key: {"degree", "m",
    "reps": {rep: orbit size}}}.  Returns {(key, gens): reason}"""
    out = {}
    for key, s in structure.items():
        for c in s["reps"]:
            k = order_of(c, s["m"])
            if k == 1:
                continue
            g = (tuple(c),)
            if s["degree"] in (5, 9) and k <= 3:
                out[(key, g)] = "order 2 or 3 on a cover of degree 5 or 9"
            elif s["degree"] * k <= N_CAP and zlib.crc32(f"N:{key}:{','.join(map(str, c))}".encode()) % N_SAMPLE == 0:
                out[(key, g)] = "sample"
    return out


def selection(witnesses, structure):
    """route N's covers by the sealed rule: the outcome-blind ones and every member's witness within N_CAP.
    Returns {(key, gens): reason}"""
    sel = blind_selection(structure)
    for key, w in sorted(witnesses.items()):
        if w is not None and w["degree"] <= N_CAP:
            sel.setdefault((key, tuple(map(tuple, w["generators"]))), "witness")
    return sel


def readings_by_member(rows):
    """{key: {rep: S}} from one route's rows, with the samples and the problems found: (reps, samples, duplicates)"""
    reps, samples, dup = {}, {}, []
    for r in rows:
        if r.get("done"):
            continue
        key, c = f"{r['state']}:{r['cover']}", tuple(r["c"])
        if r.get("sample of") is None:
            if c in reps.setdefault(key, {}):
                dup.append([key, list(c)])
            reps[key][c] = r["S"]
        else:
            rp = tuple(r["sample of"])
            if c in samples.setdefault(key, {}).setdefault(rp, {}):
                dup.append([key, list(c), "sample"])
            samples[key][rp][c] = r["S"]
    return reps, samples, dup


def evaluate(ident, Rrows, Prows, Nrows, structure, say=print):
    """the predictions.  structure: {key: {"degree", "m", "n(1)", "n(rho)", "reps": {rep: orbit size},
    "sampled": {rep: [every member of its orbit]}}}"""
    out, pred = {}, {}
    R, sR, dR = readings_by_member(Rrows)
    P, sP, dP = readings_by_member(Prows)
    # ---- coverage
    problems = {"duplicates": dR + dP, "unexpected members": sorted((set(R) | set(P)) - set(structure)),
                "missing or extra orbits": [], "incomplete samples": []}
    for key, s in structure.items():
        for nm, rr, ss in (("R", R, sR), ("P", P, sP)):
            if set(rr.get(key, {})) != set(s["reps"]):
                problems["missing or extra orbits"].append([nm, key, len(rr.get(key, {})), len(s["reps"])])
            for rp, orbit in s["sampled"].items():
                have = set(ss.get(key, {}).get(rp, {})) | {rp}
                if have != set(map(tuple, orbit)):
                    problems["incomplete samples"].append([nm, key, list(rp)])
            extra = set(ss.get(key, {})) - set(s["sampled"])
            if extra:
                problems["incomplete samples"].append([nm, key, "unexpected samples", len(extra)])
    complete_RP = not any(problems.values())
    out["coverage problems"] = {k: v for k, v in problems.items() if v}
    out["routes R' and P' complete"] = complete_RP
    pred["P0 (identity)"] = bool(ident.get("identity holds"))

    def whole(found_false, complete):
        return False if found_false else (True if complete else None)
    # ---- P1: the routes agree
    dis = [[key, list(c)] for key in R for c in R[key] if key in P and c in P[key]
           and any(R[key][c][f] != P[key][c][f] for f in FRAME)]
    dis += [[key, list(c), "sample"] for key in sR for rp in sR[key] for c in sR[key][rp]
            if key in sP and rp in sP[key] and c in sP[key][rp]
            and any(sR[key][rp][c][f] != sP[key][rp][c][f] for f in FRAME)]
    pred["P1"] = whole(bool(dis), complete_RP)
    out["route disagreements"] = dis[:50]
    out["route disagreements (count)"] = len(dis)
    # ---- P2: Lemma C on the sampled orbits
    lc = []
    for nm, rr, ss in (("R", R, sR), ("P", P, sP)):
        for key in ss:
            for rp, mem in ss[key].items():
                base = rr.get(key, {}).get(rp)
                if base is None:
                    continue
                for c, S in mem.items():
                    if any(S[f] != base[f] for f in FRAME):
                        lc.append([nm, key, list(rp), list(c)])
    pred["P2"] = whole(bool(lc), complete_RP)
    out["Lemma C failures"] = lc[:50]
    # ---- the members, the sums, the rooms (only on members read in full in both routes)
    full = [key for key, s in structure.items() if set(R.get(key, {})) == set(s["reps"]) == set(P.get(key, {}))]
    MR = {key: Member(structure[key]["m"], R[key]) for key in full}
    MP = {key: Member(structure[key]["m"], P[key]) for key in full}
    rooms, cyc3, wit = {}, [], {}
    for key in full:
        s = structure[key]
        tR, tP = MR[key].total(s["reps"]), MP[key].total(s["reps"])
        trivial = tuple(0 for _ in next(iter(s["reps"])))
        rooms[key] = {"n(1), n(rho) at the trivial character (R, P)": [[R[key][trivial][LINE], R[key][trivial][FOUR]],
                                                                       [P[key][trivial][LINE], P[key][trivial][FOUR]]],
                      "N_m sums (R, P)": [list(tR), list(tP)], "N_m room (R, P)": [room(*tR), room(*tP)]}
        for c in s["reps"]:
            if any(c):
                a, b = MR[key].cyclic(c), MP[key].cyclic(c)
                if room(*a) >= ROOM and room(*b) >= ROOM:
                    cyc3.append([key, list(c), order_of(c, s["m"]), list(a), list(b)])
        if room(*tR) >= ROOM and room(*tP) >= ROOM:
            w = witness(MR[key], MP[key], s["degree"])
            wit[key] = None if w is None else {"generators": [list(g) for g in w[0]], "|A-hat|": w[1], "degree": w[2],
                                               "sums (R, P)": [list(w[3][0]), list(w[3][1])]}
    out["rooms"] = rooms
    out["room-three cyclic covers (count)"] = len(cyc3)
    out["room-three cyclic covers"] = cyc3[:200]
    out["witnesses"] = wit
    room3 = [k for k, v in rooms.items() if min(v["N_m room (R, P)"]) >= ROOM]
    pred["P4"] = True if room3 else (False if complete_RP else None)
    pred["P4c"] = True if cyc3 else (False if complete_RP else None)
    # ---- P5, P6, P7 (both routes)
    both = lambda key, c, f, v: R[key][c][f] >= v and P[key][c][f] >= v  # noqa: E731
    p5 = [[key, list(c)] for key in R if key.split(":")[1] in ("d5.2", "d5.3") and key in P for c in R[key]
          if c in P[key] and order_of(c, structure[key]["m"]) == 3 and both(key, c, LINE, 1) and both(key, c, FOUR, 1)]
    pred["P5"] = True if p5 else (False if complete_RP else None)
    p6 = [[key, list(c)] for key in R if key in P for c in R[key] if c in P[key]
          and min(R[key][c]["capW"], R[key][c]["capL2"]) >= ROOM and min(P[key][c]["capW"], P[key][c]["capL2"]) >= ROOM]
    pred["P6"] = True if p6 else (False if complete_RP else None)
    p7 = [[key, list(c), order_of(c, structure[key]["m"]), R[key][c][LINE]] for key in R if key in P for c in R[key]
          if any(c) and c in P[key] and both(key, c, LINE, 1)]
    pred["P7"] = True if p7 else (False if complete_RP else None)
    out["P5 rows"], out["P6 rows"], out["the line's jump points (P7)"] = p5[:200], p6[:200], p7[:500]
    out["the line's jump points (count)"] = len(p7)
    # ---- route N: the selection and P3
    sel = selection(wit, structure)
    got, ndup, p3bad = {}, [], []
    for r in Nrows:
        k = (f"{r['state']}:{r['cover']}", tuple(map(tuple, r["generators"])))
        if k in got:
            ndup.append([k[0], [list(g) for g in k[1]]])
        got[k] = r
    missing_N = [[k[0], [list(g) for g in k[1]]] for k in sel if k not in got]
    for k, r in got.items():
        key, gens = k
        if key not in MR:
            continue
        H = subgroup(list(gens), structure[key]["m"])
        a, b = MR[key].abelian(H), MP[key].abelian(H)
        if not (a == b == (r["n(1)"], r["n(rho)"])):
            p3bad.append([key, [list(g) for g in gens], list(a), list(b), [r["n(1)"], r["n(rho)"]]])
    complete_N = complete_RP and not missing_N and not ndup
    pred["P3"] = False if p3bad else (True if complete_N and got else None)
    out["route N"] = {"selected": len(sel), "read": len(got), "missing": missing_N[:50], "duplicates": ndup,
                      "disagreements with Lemma A'": p3bad, "complete": complete_N}
    out["complete"] = complete_N
    out["predictions"] = pred
    for k in ("P0 (identity)", "P1", "P2", "P3", "P4", "P4c", "P5", "P6", "P7"):
        say(f"{k}: {pred[k]}")
    return out


def load_rows(name):
    p = HERE / name
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]


def structure_now():
    """the population by structure (population.py), with each member's representatives and sampled orbits"""
    PO = _sib("b1539_population", "population.py")
    O = PO.O
    out = {}
    for st, cid, deg, n1, nr, cus in PO.members():
        S, perms, cov, ab = PO.cover(st, cid)
        m = PO.modulus(deg)
        reps = O.orbit_reps(ab, m)
        out[f"{st}:{cid}"] = {"degree": deg, "m": m, "n(1)": n1, "n(rho)": nr,
                              "reps": {c: s for c, s, _ in reps},
                              "sampled": {c: O.galois_orbit(c, m) for c, s, _ in reps if PO.sampled(st, cid, c)}}
    return out


def verdict(pred):
    """section 9: PROVED if P0-P3 hold and P4 holds; NEGATIVE (scoped) if P0-P3 hold and P4 is False; else OPEN"""
    if not all(pred[k] is True for k in ("P0 (identity)", "P1", "P2", "P3")):
        return "OPEN"
    return {True: "PROVED", False: "NEGATIVE"}.get(pred["P4"], "OPEN")


def main():
    log = []

    def say(s):
        log.append(s)
        print(s)
    ident = json.loads((HERE / "identity.json").read_text())
    res = evaluate(ident, load_rows("run_R.jsonl"), load_rows("run_P.jsonl"), load_rows("run_N.jsonl"), structure_now(), say)
    res["verdict"] = verdict(res["predictions"])
    say(f"verdict: {res['verdict']}")
    say(json.dumps({k: v for k, v in res.items() if k not in ("predictions", "rooms")})[:20000])
    res["log"] = log
    if "--record" in sys.argv:
        (HERE / "read_out.json").write_text(json.dumps(res, indent=1, default=list) + "\n")
        (HERE / "read_out_log.txt").write_text("\n".join(log) + "\n")
    return res


if __name__ == "__main__":
    main()
