#!/usr/bin/env python3
"""sm:B1549 -- the controls, run before the seal (and again by identity.py).

  K1  an independent rank method: every member orbit of population.json, and the first two non-member orbits of every
      cover in the census, re-read in both routes with ranks by complex SVD (mpmath) instead of elimination; (h1, r1, n)
      must equal the census's.
  K2  main's banked counts (B1492, B1493): on L8a15 (+LLLR's companion, its three-ended cover) the sign member reads
      (-1, -1) and the order-4 member (1, 1, i) reads (-1, 0); on o10_150729 (m003's companion, five ends) an interior
      class at a member trivial on one end and at one trivial on two ends reads (-1, -1). Both routes, one draw.
  K3  sm:B1545's banked reading on m136's companion (m136.D4.2-0-2.w0) at the fibre sign (zeta = 0, s = 1/2): the interior
      class reads I(W1) = -1 (the Lambda^2 component is recorded, not banked there). Both routes, one draw.
  K4  the read-out on synthetic rows: its verdicts and refutations.
  K5  n(1) = 0 on every three-ended cover, exact (sm:B1538's reader at the trivial character, two primes).

    python3 controls.py   ->  controls.json beside this file"""
import json
import random
import time

import mpmath as mp

import read_out as RO
import three_lib as T

HERE = T.HERE


# ------------------------------------------------------------------------------------------------ K1: SVD ranks
def svd_rank(A, ncols):
    if not A or ncols == 0:
        return 0
    M = mp.matrix(A)
    s = [abs(x) for x in mp.svd_c(M, compute_uv=False)]
    smax = max(s)
    return sum(1 for x in s if smax and x / smax > T.REL)


def svd_structure(mod, P):
    """h1, r1, n with SVD ranks (no elimination)"""
    e, ng = mod.e, P.ngen
    fox = T.vstack(*[mod.fox(r, ng)[0] for r in P.rels])
    rk = svd_rank(fox, ng * e)
    I = T.eye(e)
    dg = T.vstack(*[[[mod.M[j][i][k] - I[i][k] for k in range(e)] for i in range(e)] for j in range(ng)])
    h0 = e - svd_rank(dg, e)
    h1 = ng * e - rk - (e - h0)
    # kernel of fox via SVD (full V)
    M = mp.matrix(fox)
    U, S, V = mp.svd_c(M, full_matrices=True)
    s = [abs(x) for x in S]
    smax = max(s) if s else 0
    r = sum(1 for x in s if smax and x / smax > T.REL)
    Z = [[mp.conj(V[r + j, i]) for i in range(ng * e)] for j in range(ng * e - r)]
    rowsR, BPb = [], []
    for (w1, w2) in P.periph:
        F1, W1 = mod.fox(w1, ng)
        F2, W2 = mod.fox(w2, ng)
        rowsR += [F1, F2]
        BPb.append(T.vstack([[W1[i][k] - I[i][k] for k in range(e)] for i in range(e)],
                            [[W2[i][k] - I[i][k] for k in range(e)] for i in range(e)]))
    nc = len(P.periph)
    BP = [[mp.mpc(0)] * (e * nc) for _ in range(2 * e * nc)]
    for c, b in enumerate(BPb):
        for i in range(2 * e):
            for k in range(e):
                BP[2 * e * c + i][e * c + k] = b[i][k]
    R = T.vstack(*rowsR)
    rBP = svd_rank(BP, e * nc)
    if Z:
        RZ = [[mp.fsum(R[i][l] * z[l] for l in range(ng * e)) for z in Z] for i in range(len(R))]
        r1 = svd_rank(T.hstack(BP, RZ), e * nc + len(Z)) - rBP
    else:
        r1 = 0
    return {"h1": h1, "r1": r1, "n": h1 - r1}


def K1():
    pop = json.loads((HERE / "population.json").read_text())
    import census as CEN
    census = [json.loads(x) for p in (0, 1) for x in CEN._lines(HERE / f"census_{p}.jsonl") if x.strip()]
    picks = [r for r in census if r["P"]["n"] > 0 or r["S"]["n"] > 0]
    per_cover = {}
    for r in census:
        k = (r["state"], tuple(r["lattice"]), r["wbar"])
        if r["P"]["n"] == 0 and r["S"]["n"] == 0 and per_cover.get(k, 0) < 2:
            picks.append(r)
            per_cover[k] = per_cover.get(k, 0) + 1
    bad, n = [], 0
    for r in picks:
        C = T.PC.Cover(T.PC.State(r["state"]), tuple(r["lattice"]), r["wbar"])
        c = r["orbit"][0]
        ez, es = tuple(c[:-1]), c[-1]
        Pr, P = T.presentation_P(C)
        sP = svd_structure(T.Mod(T.module_P(r["state"], C, Pr, ez, es, 4)), P)
        PS, _ = T.presentation_S(C.st)
        sS = svd_structure(T.Mod(T.ind_blocks(r["state"], C, ez, es, 4)), PS)
        n += 1
        for name, got, want in (("P", sP, r["P"]), ("S", sS, r["S"])):
            if (got["h1"], got["r1"], got["n"]) != (want["h1"], want["r1"], want["n"]):
                bad.append([r["state"], r["lattice"], r["wbar"], c, name, got, want])
    return {"orbits re-read": n, "member orbits among them": len(pop["member orbits"]), "disagreements": bad,
            "holds": not bad}


# ------------------------------------------------------------------------------------------------ K2, K3: banked counts
def count_at(sw, lat, wl, ch, route, m=4, tag="K"):
    C = T.PC.Cover(T.PC.State(sw), tuple(lat), wl)
    ez, es = tuple(ch[:-1]), ch[-1]
    rng = random.Random(f"B1549|{tag}|{sw}|{route}|{ch}")
    r = (T.read_P if route == "P" else T.read_S)(sw, C, ez, es, m, [rng])
    return {"structure": r["structure"], "interior dimension": r["interior dimension"],
            "count": r["draws"][0]["count"] if r["draws"] else None}


def K2_o10():
    st = T.PC.State("-LR")
    lat = None
    for L in T.PC.lattices(st.M, 5, 5):
        (a, b), (c, e) = st.M
        if all(T.PC.in_lattice(L, v) for v in [(a - 1, c), (b, e - 1)]):
            lat = L
    wl = [w for w in range(5) if len(T.PC.Cover(st, lat, w).cusps) == 5][0]
    C = T.PC.Cover(st, lat, wl)
    want = {1: None, 2: None}
    for orb in T.orbits(C, 2):
        c = orb[0]
        mA = len(C.trivial_cusps(c[0], c[1], 2))
        if mA in want and want[mA] is None:
            want[mA] = list(c[0]) + [c[1]]
    return lat, wl, want


def run_K2_K3():
    rows = []
    cases = [("+LLLR", (1, 0, 3), 0, [0, 2, 0, 2, 0], [-1, -1], "B1492: a sign member of L8a15"),
             ("+LLLR", (1, 0, 3), 0, [0, 3, 0, 1, 0], [-1, 0], "B1493: the order-4 member (1, 1, i)")]
    lat, wl, want = K2_o10()
    for mA, ch in want.items():
        ch4 = [2 * x for x in ch]                     # a sign character as exponents mod 4
        cases.append(("-LR", tuple(lat), wl, ch4, [-1, -1], f"B1492: o10_150729, a member trivial on {mA} end(s)"))
    k3 = [("+LLRR", (2, 0, 2), 0, [0, 0, 0, 0, 0, 2], [-1, None], "sm:B1545 banked I(W1) = -1 on m136's companion at the "
           "fibre sign (the Lambda^2 component is not banked there: main's B1485 (-1, -1) is on m136 itself, one end)")]
    out = {"K2": [], "K3": []}
    for name, lst in (("K2", cases), ("K3", k3)):
        for sw, lat_, wl_, ch, expect, src in lst:
            for route in ("P", "S"):
                t0 = time.time()
                r = count_at(sw, lat_, wl_, ch, route, tag=name)
                ok = r["count"] is not None and all(e is None or e == g for e, g in zip(expect, r["count"]))
                out[name].append({"state": sw, "lattice": list(lat_), "wbar": wl_, "character": ch, "route": route,
                                  "expect": expect, "source": src, "got": r["count"], "structure": r["structure"],
                                  "holds": ok, "seconds": round(time.time() - t0, 1)})
    return out


# ------------------------------------------------------------------------------------------------ K4: the read-out
def K4():
    pop = {"member orbits": [
        {"state": "+LLLR", "lattice": [1, 0, 3], "wbar": 0, "orbit": [[0, 2, 0, 2, 0], [2, 0, 0, 2, 0], [2, 2, 0, 0, 2]],
         "size": 3, "order": 2, "m_A": 0},
        {"state": "-X", "lattice": [3, 1, 1], "wbar": 0, "orbit": [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "size": 3, "order": 4,
         "m_A": 0}]}
    gap = [[0.01, 1e-50]] * 4

    def row(route, orb, ch, count, n=1, draws=3, order=None):
        reads = {k: {"h0": 0, "h1": 1, "r1": 0, "n": 1, "gaps": gap} for k in ("W1", "W1*", "L2", "L2*")}
        return {"route": route, "state": orb["state"], "lattice": orb["lattice"], "wbar": orb["wbar"], "character": ch,
                "order": order or orb["order"], "m_A": orb["m_A"], "m_A (this character)": orb["m_A"],
                "structure": {"h0": 0, "h1": n, "r1": 0, "n": n, "gaps": gap}, "interior dimension": n,
                "draws": [{"count": list(count), "reads": reads} for _ in range(draws)]}

    def good():
        rows = []
        for orb, cnt in ((pop["member orbits"][0], (-1, -1)), (pop["member orbits"][1], (-1, 0))):
            for ch in orb["orbit"]:
                for route in ("P", "S"):
                    rows.append(row(route, orb, ch, cnt))
        return rows
    ctl = {"all hold": True}
    cases = {}
    r = good()
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["all good, +LLLR alone: PROVED"] = out["verdict"] == "PROVED" and out["P7"] and out["P6"]
    r = good()
    r[-1]["draws"][0]["count"] = [-1, -1]
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["draws disagree: P5 false, OPEN"] = (out["P5"] is False) and out["verdict"] == "OPEN"
    r = good()
    for x in r:
        if x["state"] == "-X":
            for d in x["draws"]:
                d["count"] = [-1, -1]
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["a second cover with three: NEGATIVE"] = out["verdict"] == "NEGATIVE" and out["P8"] is False and \
        out["P7"] is False
    r = good()[:-1]
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["a missing task: incomplete, OPEN"] = out["complete"] is False and out["verdict"] == "OPEN"
    r = good() + [good()[0]]
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["a duplicated task: incomplete, OPEN"] = out["complete"] is False and out["verdict"] == "OPEN"
    r = good()
    r[1]["structure"]["h1"] = 2
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["routes disagree on structure: P2 false, OPEN"] = out["P2"] is False and out["verdict"] == "OPEN"
    r = good()
    for d in r[0]["draws"]:
        d["count"] = [-2, -1]
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["below the cap: P4 false, OPEN"] = out["P4"] is False and out["verdict"] == "OPEN"
    r = good()
    out, _ = RO.evaluate(r, pop, {"all hold": False}, True)
    cases["a control failed: P1 false, OPEN"] = out["P1"] is False and out["verdict"] == "OPEN"
    r = good()
    r[0]["structure"]["gaps"] = [[1e-28, 1e-40]]
    for d in r[0]["draws"]:
        d["reads"]["W1"]["gaps"] = [[1e-28, 1e-40]]
    out, _ = RO.evaluate(r, pop, ctl, True)
    cases["a murky gap: P4 false, OPEN"] = out["P4"] is False and out["verdict"] == "OPEN"
    return {"cases": cases, "holds": all(cases.values())}


# ------------------------------------------------------------------------------------------------ K5: n(1) = 0
def K5():
    """the trivial line's room on every cover, exact: sm:B1538's reader at the trivial character, two primes"""
    rows, ok = [], True
    for sw, d, lat, wl in T.three_covers():
        C = T.PC.Cover(T.PC.State(sw), lat, wl)
        Pr = T.RP.Presentation(C)
        ez = tuple([0] * C.n)
        reads = [T.RP.read(Pr, ez, 0, 2, p) for p in (1000003, 998244353)]
        same = reads[0] == reads[1]
        rows.append({"state": sw, "lattice": list(lat), "wbar": wl, "h1": reads[0]["h1"], "r1": reads[0]["r1"],
                     "n(1)": reads[0]["n"], "primes agree": same})
        ok = ok and same and reads[0]["n"] == 0 and reads[0]["h1"] == 3
    return {"covers": rows, "holds": ok}


def main():
    t0 = time.time()
    out = {"K1": K1()}
    out.update(run_K2_K3())
    out["K4"] = K4()
    out["K5"] = K5()
    out["all hold"] = (out["K1"]["holds"] and all(x["holds"] for x in out["K2"]) and all(x["holds"] for x in out["K3"])
                       and out["K4"]["holds"] and out["K5"]["holds"])
    out["seconds"] = round(time.time() - t0, 1)
    (HERE / "controls.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({"K1": out["K1"]["holds"], "K2": [(x["character"], x["route"], x["got"]) for x in out["K2"]],
                      "K3": [(x["route"], x["got"]) for x in out["K3"]], "K4": out["K4"]["cases"],
                      "K5": [(x["state"], x["lattice"], x["n(1)"]) for x in out["K5"]["covers"]],
                      "all hold": out["all hold"]}, indent=1))


if __name__ == "__main__":
    main()
