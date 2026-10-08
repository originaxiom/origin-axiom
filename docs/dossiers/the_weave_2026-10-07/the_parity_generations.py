#!/usr/bin/env python3
"""W18: THE FIVE CARRIED BY EACH PARITY LINE. W17's SU(5)' five, split by the forced cover's sectors.

W17's five W(nu, c) = [[D nu^3, c P nu^-2], [0, P nu^-2]] lives on the thread M itself (tick 1). On the forced A4 cover
the count of the pulled-back five splits over A4's irreducibles R: 1, the deck characters w and w^2, and the triplet P.
Each sector has weight dim R (Shapiro), and the R-part of the cover's pair is (I(W (x) R), I(Lambda^2 W (x) R)) on M. At
the resolving tick M3 the parity lines B_p of W8 are A4's three characters restricted (B_p(t^3) = 1 on all 32 states).
So the P-part is also the part carried by each parity line: (I(W|M3 (x) B_p), I(Lambda^2 W|M3 (x) B_p)) for each p.

The rule is W18_PREDICTION.md's, committed before this ran (b5223cbb):
  route A (tick 1): every odd-trace state to length 8; both lifts; every nu in mu_24 with a gluing class; every basis
    class and one generic combination (W17's readings: the generic coefficients are drawn as W17 drew them); for R in
    (1, w, w^2, P), the pairs for W and for its dual;
  route B (tick 3, direct): the twelve states to length 6; both lifts; every nu with a class; the first basis class; for
    q in (0, p1, p2, p3), the pair (I(W|M3 (x) B_q), I(Lambda^2 W|M3 (x) B_q)), with B_0 trivial.
The checks: route B's parities equal route A's P-sector; route B's zero parity equals the sum of route A's singlets; and
the three parities agree with each other.

    python3 the_parity_generations.py   ->  the_parity_generations.json beside it
"""
import json
import random
import sys
import time
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_weave_extension as WE  # noqa: E402
import the_weaves_five as FV  # noqa: E402
import the_weaves_five_tick1 as T1  # noqa: E402

IL, LV, CP = WE.IL, WE.LV, WE.CP
SEED = 13                                     # W17's seed: the generic coefficients below are W17's
SECTORS = ("1", "w", "w^2", "P")
DIMS = {"1": 1, "w": 1, "w^2": 1, "P": 3}
QS = ("0", "p1", "p2", "p3")


def setup():
    p = LV.primes_for(24, k=1, start=20000)[0]
    F = IL.GF(p)
    return p, F, F.root_of_unity(24)


def gluing_basis(F, S, g, nexp):
    Dm, Pm = S.D(g, nexp), S.P(g, nexp)
    H = IL.Rep(F, S.gens, T1.hom_rep(F, S.gens, Dm, Pm))
    Sx = WE.Tick3.__new__(WE.Tick3)
    Sx.F, Sx.gens, Sx.rels = F, S.gens, S.rels
    return Dm, Pm, WE.Tick3.h1_basis(Sx, H)


def plan(states):
    """W17's readings in W17's order, with the generic coefficients drawn from W17's random stream"""
    p, F, z = setup()
    rng = random.Random(SEED)
    out = {}
    for sw in states:
        S = T1.Tick1(sw, F, z)
        jobs = []
        for li, g in enumerate(S.lifts):
            for nexp in range(24):
                _, _, basis = gluing_basis(F, S, g, nexp)
                if not basis:
                    continue
                coef = [rng.randrange(1, p) for _ in basis] if len(basis) > 1 else None
                jobs.append((li, nexp, coef))
        out[sw] = jobs
    return out


def kron(F, A, B):
    m = len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] % F.p for j in range(len(A) * m)] for i in range(len(A) * m)]


def pair(F, gens, rels, mu, lam, X, L2):
    """(I(X), I(L2)) on the presentation given"""
    I1 = IL.index(IL.Rep(F, gens, X), rels, mu, lam)[0]
    I2 = IL.index(IL.Rep(F, gens, L2), rels, mu, lam)[0]
    return [I1, I2]


def route_a(job):
    """tick 1, every reading of one state: the sectors 1, w, w^2 and P for W and for W*"""
    sw, jobs = job
    t0 = time.time()
    p, F, z = setup()
    S = T1.Tick1(sw, F, z)
    om = pow(z, 8, p)                                      # a primitive cube root of unity
    irreps = {"1": {g: [[1]] for g in S.gens},
              "w": {"a": [[1]], "b": [[1]], "t": [[om]]},
              "w^2": {"a": [[1]], "b": [[1]], "t": [[om * om % p]]}}
    rows = []
    for li, nexp, coef in jobs:
        g = S.lifts[li]
        Dm, Pm, basis = gluing_basis(F, S, g, nexp)
        irreps["P"] = S.P(g, 0)                            # A4's triplet: Ad(rho_Q) with t -> Ad(g), untwisted
        choices = [(f"basis {i}", v) for i, v in enumerate(basis)]
        if coef is not None:
            choices.append(("generic", [sum(c * v[j] for c, v in zip(coef, basis)) % p for j in range(len(basis[0]))]))
        for kind, cvec in choices:
            Wm = T1.five(F, S.gens, Dm, Pm, cvec)
            assert IL.Rep(F, S.gens, Wm).check_relators(S.rels)
            Wd = {g_: F.T(F.inverse(Wm[g_])) for g_ in S.gens}
            row = {"lift": li, "nu (24ths)": nexp, "class": kind}
            for name, Wx in (("W", Wm), ("W*", Wd)):
                L2 = {g_: FV.wedge2(F, Wx[g_]) for g_ in S.gens}
                row[name] = {R: pair(F, S.gens, S.rels, S.mu, S.lam,
                                     {g_: kron(F, Wx[g_], irreps[R][g_]) for g_ in S.gens},
                                     {g_: kron(F, L2[g_], irreps[R][g_]) for g_ in S.gens}) for R in SECTORS}
                row[name]["forced cover"] = [sum(DIMS[R] * row[name][R][k] for R in SECTORS) for k in (0, 1)]
            rows.append(row)
    return sw, rows, round(time.time() - t0, 1)


def route_b(job):
    """tick 3, directly: the five restricted to the resolving tick, carried by each parity line"""
    sw, jobs = job
    t0 = time.time()
    p, F, z = setup()
    S = T1.Tick1(sw, F, z)
    S3 = WE.Tick3(sw, F, z)
    lines = {"0": {"a": 1, "b": 1, "t": 1}, **{q: S3.B(q) for q in QS[1:]}}
    rows = []
    seen = set()
    for li, nexp, _ in jobs:
        if (li, nexp) in seen:
            continue
        seen.add((li, nexp))
        g = S.lifts[li]
        Dm, Pm, basis = gluing_basis(F, S, g, nexp)
        Wm = T1.five(F, S.gens, Dm, Pm, basis[0])
        W3 = {"a": Wm["a"], "b": Wm["b"], "t": F.mul(F.mul(Wm["t"], Wm["t"]), Wm["t"])}    # t3 -> t^3
        assert IL.Rep(F, S3.gens, W3).check_relators(S3.rels)
        L3 = {g_: FV.wedge2(F, W3[g_]) for g_ in S3.gens}
        row = {"lift": li, "nu (24ths)": nexp, "class": "basis 0"}
        for q in QS:
            Bv = lines[q]
            row[q] = pair(F, S3.gens, S3.rels, S3.mu, S3.lam,
                          {g_: F.scale(Bv[g_], W3[g_]) for g_ in S3.gens},
                          {g_: F.scale(Bv[g_], L3[g_]) for g_ in S3.gens})
        rows.append(row)
    return sw, rows, round(time.time() - t0, 1)


def kind(sw):
    """the two named laws: Theorem H's twin and W15's mod-16 silence"""
    word, sign = sw[1:], (1 if sw[0] == "+" else -1)
    t = sign * int(CP.mat(word, 1).trace())
    if t % 16 in (1, 15):
        return "mod-16 word"
    hand = (word.count("L") - word.count("R") + (2 if sign < 0 else 0)) % 4
    return "chiral twin" if hand == 2 else "carrier"


PREDICTED = {"carrier": {"P": [1, 1], "1": [1, 1], "w": [0, 1], "w^2": [0, 1]},
             "chiral twin": {"P": [0, 2], "1": [0, 1], "w": [0, 1], "w^2": [0, 1]},
             "mod-16 word": {"P": [0, 0], "1": [0, 0], "w": [0, 0], "w^2": [0, 0]}}


def main():
    states = WE.STATES + WE.STATES8
    jobs = plan(states)
    with Pool(3) as pool:
        ra = {sw: (rows, sec) for sw, rows, sec in pool.map(route_a, [(sw, jobs[sw]) for sw in states], chunksize=1)}
        rb = {sw: (rows, sec) for sw, rows, sec in pool.map(route_b, [(sw, jobs[sw]) for sw in WE.STATES], chunksize=1)}
    out = {"prime": setup()[0], "rule": "W18_PREDICTION.md (b5223cbb)", "states": {}}
    hold = {"1": True, "2": True, "3": True, "4": True, "5": True}
    for sw in states:
        rows, sec = ra[sw]
        k = kind(sw)
        sectors = {R: sorted({tuple(r["W"][R]) for r in rows}) for R in SECTORS}
        dual = {R: sorted({tuple(r["W*"][R]) for r in rows}) for R in SECTORS}
        st = {"kind": k, "readings (route A)": len(rows), "seconds (route A)": sec,
              "route A, W: pairs per sector": {R: [list(x) for x in v] for R, v in sectors.items()},
              "route A, W*: pairs per sector": {R: [list(x) for x in v] for R, v in dual.items()},
              "forced cover totals": sorted({tuple(r["W"]["forced cover"]) for r in rows}),
              "rows (route A)": rows}
        pred = PREDICTED[k]
        ok_p = sectors["P"] == [tuple(pred["P"])]
        ok_s = all(sectors[R] == [tuple(pred[R])] for R in ("1", "w", "w^2"))
        st["the P-sector as predicted"] = ok_p
        st["the singlet sectors as predicted"] = ok_s
        if k == "carrier":
            hold["1"] &= ok_p
        elif k == "chiral twin":
            hold["2"] &= ok_p
        else:
            hold["3"] &= ok_p and ok_s
        if k != "mod-16 word":
            hold["4"] &= ok_s
        if sw in rb:
            brows, bsec = rb[sw]
            st["route B (tick 3)"] = {"readings": len(brows), "seconds": bsec, "rows": brows}
            agree, alike = True, True
            for b in brows:
                a = next(r for r in rows if r["lift"] == b["lift"] and r["nu (24ths)"] == b["nu (24ths)"]
                         and r["class"] == "basis 0")
                alike &= b["p1"] == b["p2"] == b["p3"]
                agree &= b["p1"] == a["W"]["P"]
                agree &= b["0"] == [a["W"]["1"][k_] + a["W"]["w"][k_] + a["W"]["w^2"][k_] for k_ in (0, 1)]
            st["route B: the three parities alike"] = alike
            st["route B agrees with route A (Shapiro)"] = agree
            hold["5"] &= agree and alike
        out["states"][sw] = st
        print(sw, k, json.dumps({R: st["route A, W: pairs per sector"][R] for R in SECTORS}),
              st.get("route B agrees with route A (Shapiro)"), flush=True)
    out["the predictions"] = {"1 (carriers: P-sector (1, 1))": hold["1"], "2 (chiral twins: P-sector (0, 2))": hold["2"],
                              "3 (mod-16 words: (0, 0) in every sector)": hold["3"],
                              "4 (singlet sectors as predicted)": hold["4"], "5 (the two routes agree)": hold["5"]}
    out["by kind"] = {k: sorted(sw for sw in states if kind(sw) == k) for k in PREDICTED}
    return out


if __name__ == "__main__":
    if sys.argv[1:]:                          # a partial run (states named on the command line) writes nothing
        j = plan(sys.argv[1:])
        for sw in sys.argv[1:]:
            print(route_a((sw, j[sw]))[0::2])
        sys.exit(0)
    res = main()
    with open(HERE / "the_parity_generations.json", "w") as f:
        json.dump(res, f, indent=1, ensure_ascii=False)
    print(json.dumps(res["the predictions"]))
