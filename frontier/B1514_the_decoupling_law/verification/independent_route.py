"""B1514 -- THE INDEPENDENT ROUTE (route L, the lifting criterion).  Run after the sealed census: python3 independent_route.py --record.

The owner's rule (WORKING_RULES, NO NEGATIVE FROM A BUG): every zero a verdict rests on is re-derived by a different method in
separate code, with a live positive control, exactly or at several primes and every root.  This script shares no code with
census.py / law_lib.py / higgs_lib.py / tower_lib.py; it reads the populations as data and builds everything on B1513's
independent_audit.py (lift_route.py).

Part 0  the banked identity: at the first member of every population, h^1(L), h^1(V), h^1(V_eta), h^1(W1) as banked, x u c != 0.
Part A  every member: M4 exactly over Q(sqrt 5, sqrt -3) and mod p; every population at three primes (other than route T's) and
        every root; M5 at w = 7 for c = c1, c2, c1 + c2.  The same readings as route T, by the lifting criterion:
          [a ^ a'] in H^2(Lambda^2 W1) for a, a' in H^1(W1)  (the 10bar' coupling, against every 5bar'_H, by duality);
          [f ^ f'] in H^2(Lambda^2 W1*) for f, f' in H^1(W1*) (the 10' coupling);
          the positive control [x u c] != 0 in H^2(V).
Part B  joining forms (numpy elimination) and the cross couplings [mu(a_i u a_j)] in H^2(Lambda^2 W_k), at the first prime-root of
        every population.
Part C  the readings, and the agreement with route T's record (census_run.txt) population by population.
Record: independent_route_run.txt."""
import json
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lift_route as LR  # noqa: E402

IA = LR.IA
RECORD = HERE / "independent_route_run.txt"
ROUTE_T_RECORD = HERE / "census_run.txt"
ROUTE_L_PRIMES = 3
START = 2 ** 23 - 2 * 104729 - 13


def lam_residue(lam, p, iota):
    return {"1": 1, "-1": p - 1, "i": iota, "-i": (p - iota) % p if iota else None}[lam]


def read_member(F, mn, n, ab, N, lam, zeta, c_coeffs=None):
    m = LR.Member(F, mn, n, ab, N, lam, zeta, c_coeffs)
    (a, b), Nr = m.char
    row = {"member": [[a, b], Nr], "c": list(c_coeffs) if c_coeffs else "c1"}
    row["h"] = {name: LR.h_data(rep) for name, rep in (("L", m.L), ("V", m.V), ("V_eta", m.Veta), ("W1", m.W1), ("W1*", m.W1d),
                                                       ("L2V", m.L2V), ("VL", m.VL), ("L2W", m.L2W), ("L2W*", m.L2Wd))}
    row["interior"] = {"W1": LR.interior_dimension(m.W1), "W1*": LR.interior_dimension(m.W1d)}
    row["cusp acyclic"] = all(LR.cusp_acyclic(rep) for rep in (m.V, m.V.dual(), m.L2V, m.L2W, m.L2Wd, m.VL))
    row["control [x u c] != 0"] = LR.x_cup_c(m)["non-zero"]
    tb = LR.wedge_table(m.L2W, m.W1)
    tf = LR.wedge_table(m.L2Wd, m.W1d)
    row["10bar' [a ^ a']"] = {"slot": tb["dim H^1(slot)"], "H2": tb["dim H^2(target)"], "zero": tb["zero"], "symmetric": tb["symmetric"],
                              "blocks ok": tb["blocks ok"]}
    row["10' [f ^ f']"] = {"slot": tf["dim H^1(slot)"], "H2": tf["dim H^2(target)"], "zero": tf["zero"], "symmetric": tf["symmetric"],
                           "blocks ok": tf["blocks ok"]}
    return row, m


def joining(members):
    out = {"triples": {}, "cross couplings": {}}
    n = len(members)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dim, basis = LR.form_space(members[k].W1, members[i].W1, members[j].W1)
                out["triples"][f"{k},{i},{j}"] = dim
                if i == j == k or not dim:
                    continue
                res = [LR.cross_coupling(members[k].W1, members[i].W1, members[j].W1, vec) for vec in basis]
                out["cross couplings"][f"{k},{i},{j}"] = {"forms": dim, "zero": all(r["zero"] for r in res),
                                                          "blocks ok": all(r["blocks ok"] for r in res)}
    return out


def banked_identity(log):
    out, ok_all = {}, True
    for pop in LR.populations():
        n = pop["level"]
        orders = sorted({LR.reduce_char(ab, pop["N"])[1] for o in pop["orbits"].values() for ab in o}) + ([4] if "i" in pop["lam"] else [])
        (p, roots), = LR.primes_for(pop["factor"], orders, 1, START - 11 * n)
        F = IA.ModP(p, f"GF({p})")
        iota = IA.sqrt_m1(p) if "i" in pop["lam"] else None
        mn = IA.mn_mats(F, roots[0])
        ab = next(iter(pop["orbits"].values()))[0]
        (_, _), Nr = LR.reduce_char(ab, pop["N"])
        m = LR.Member(F, mn, n, ab, pop["N"], lam_residue(pop["lam"], p, iota), LR.root_of_unity(p, Nr))
        bank = (1, 1, 1) if n == 4 else tuple(pop["banked_h1"][0][:3])
        got = tuple(LR.h_data(r)["h1"] for r in (m.L, m.V, m.Veta))
        ctl = LR.x_cup_c(m)["non-zero"]
        ok = got == bank and LR.h_data(m.W1)["h1"] == bank[1] and ctl
        out[pop["label"]] = {"p": p, "h1 (L, V, V_eta)": got, "x u c != 0": ctl, "pass": ok}
        ok_all = ok_all and ok
    out["pass"] = ok_all
    log(f"0: banked identity {'passed' if ok_all else 'FAILED'}")
    return out


def main():
    t0 = time.time()

    def log(msg):
        print(f"[{time.time() - t0:8.1f}s] {msg}", flush=True)
    rec = {"route": "L (the lifting criterion, on B1513's independent_audit)"}
    rec["0_banked_identity"] = banked_identity(log)
    assert rec["0_banked_identity"]["pass"], "the banked identity failed: stop"
    A, B = [], []
    pops = LR.populations()
    K = sp.QQ.algebraic_field(sp.sqrt(5), sp.sqrt(-3))
    FE = IA.Exact(K, "Q(sqrt 5, sqrt -3)")
    mnE = IA.mn_mats(FE, K.from_sympy((7 - 3 * sp.sqrt(5)) / 2))
    zeta3 = K.from_sympy((-1 + sp.sqrt(-3)) / 2)
    for pop in pops:
        if pop["level"] != 4:
            continue
        rows = [read_member(FE, mnE, 4, ab, pop["N"], FE.c(1), zeta3)[0] for o in pop["orbits"].values() for ab in o]
        A.append({"population": pop["label"], "arithmetic": "exact, Q(sqrt 5, sqrt -3)", "rows": rows})
        log(f"A: {pop['label']} exact done")
    for pop in pops:
        n = pop["level"]
        orders = sorted({LR.reduce_char(ab, pop["N"])[1] for o in pop["orbits"].values() for ab in o}) + ([4] if "i" in pop["lam"] else [])
        for pi, (p, roots) in enumerate(LR.primes_for(pop["factor"], orders, ROUTE_L_PRIMES, START - 104729 * n)):
            F = IA.ModP(p, f"GF({p})")
            iota = IA.sqrt_m1(p) if "i" in pop["lam"] else None
            lam = lam_residue(pop["lam"], p, iota)
            for r in roots:
                mn = IA.mn_mats(F, r)
                c_list = [None, (0, 1), (1, 1)] if (n == 5 and pop["lam"] == "1") else [None]
                rows, by_orbit = [], {}
                for oname, orbit in pop["orbits"].items():
                    by_orbit[oname] = []
                    for ab in orbit:
                        (_, _), Nr = LR.reduce_char(ab, pop["N"])
                        zeta = LR.root_of_unity(p, Nr)
                        for cc in c_list:
                            row, m = read_member(F, mn, n, ab, pop["N"], lam, zeta, cc)
                            rows.append(row)
                            if cc is None:
                                by_orbit[oname].append(m)
                A.append({"population": pop["label"], "arithmetic": f"GF({p}), q = {r}", "rows": rows})
                if pi == 0 and r == roots[0]:
                    B.append({"population": pop["label"], "p": p, "q": r, "orbits": {o: joining(ms) for o, ms in by_orbit.items()}})
                log(f"A: {pop['label']} p = {p} q = {r} done ({len(rows)} readings)")
    rec["A"], rec["B"] = A, B
    rec["C"] = readings(A, B)
    rec["C"]["agreement with route T"] = agreement(rec)
    rec["seconds"] = round(time.time() - t0, 1)
    log(f"C: {json.dumps(rec['C']['predictions'])}")
    log(f"C: agreement {json.dumps(rec['C']['agreement with route T'].get('pass'))}")
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    return rec


def readings(A, B):
    rows = [(blk["population"], r) for blk in A for r in blk["rows"]]
    lvl = lambda pop: int(pop.split()[0][1])                                                       # noqa: E731
    out = {}
    out["P1 the twisted Higgs bulk Lambda^2 V is acyclic at every member"] = all(r["h"]["L2V"] == {"h0": 0, "h1": 0, "h2": 0} for _, r in rows)

    def higgs_ok(pop, r):
        n, h = lvl(pop), r["h"]["L2W"]["h1"]
        return h == 0 if n == 4 else (h == r["h"]["V"]["h1"] if n == 5 else h == 1)
    out["P2 the Higgs content reads as Lemma 4 (M4 none; M5 h1(V); M6 one)"] = all(higgs_ok(p, r) and r["h"]["L2W*"]["h1"] == r["h"]["L2W"]["h1"]
                                                                                  for p, r in rows)
    out["P3 the 10bar' coupling to every 5bar'_H vanishes at every member"] = all(r["10bar' [a ^ a']"]["zero"] for _, r in rows)
    out["P4 the 10' coupling is non-zero at some member with a Higgs class"] = any((not r["10' [f ^ f']"]["zero"]) and r["h"]["L2W"]["h1"] > 0
                                                                                   for _, r in rows)
    cross = [c for blk in B for o in blk["orbits"].values() for c in o["cross couplings"].values()]
    forms = [d for blk in B for o in blk["orbits"].values() for key, d in o["triples"].items() if len(set(key.split(","))) > 1]
    out["P5 some cross triple carries a joining form"] = any(d > 0 for d in forms)
    out["P6 every cross coupling through a joining form vanishes"] = all(c["zero"] for c in cross)
    out["P7 no chiral state through level 6 couples to a Higgs class (with B1513)"] = (out["P3 the 10bar' coupling to every 5bar'_H vanishes at every member"]
                                                                                        and out["P6 every cross coupling through a joining form vanishes"])
    d = {}
    d["D1 banked h1 (L, V, V_eta, W1) at every reading"] = all(r["h"]["L"]["h1"] == 1 and r["h"]["W1"]["h1"] == r["h"]["V"]["h1"] for _, r in rows)
    d["D2 positive control [x u c] != 0 at every reading"] = all(r["control [x u c] != 0"] for _, r in rows)
    d["D3 cusp acyclicity (Lemma 1) at every reading"] = all(r["cusp acyclic"] for _, r in rows)
    d["D4 interior classes: n(W1) = h1(V) and n(W1) - n(W1*) = +1 = the banked I(W1)"] = all(
        r["interior"]["W1"] == r["h"]["V"]["h1"] and r["interior"]["W1"] - r["interior"]["W1*"] == 1 for _, r in rows)
    d["D5 the wedge classes symmetric, blocks consistent"] = all(r["10bar' [a ^ a']"]["symmetric"] and r["10' [f ^ f']"]["symmetric"]
                                                                and r["10bar' [a ^ a']"]["blocks ok"] and r["10' [f ^ f']"]["blocks ok"] for _, r in rows)
    d["D6 V (x) L: acyclic on M4; h1 = h1(V) on M5; h1 = 1 on M6 (Lemma 4)"] = all(
        (r["h"]["VL"]["h1"] == 0) if lvl(p) == 4 else (r["h"]["VL"]["h1"] == r["h"]["V"]["h1"] if lvl(p) == 5 else r["h"]["VL"]["h1"] == 1)
        for p, r in rows)
    d["D7 an own triple always carries a form (the wedge form)"] = all(o["triples"][f"{k},{k},{k}"] >= 1 for blk in B for o in blk["orbits"].values()
                                                                       for k in range(len({kk.split(',')[0] for kk in o["triples"]})))
    d["D8 every member of a population reads the same (Lemma 5)"] = all(
        len({json.dumps([r["h"], r["interior"], r["10bar' [a ^ a']"]["zero"], r["10' [f ^ f']"]["zero"]], sort_keys=True)
             for r in blk["rows"] if r["c"] == "c1"}) == 1 for blk in A)
    d["D9 cross couplings' blocks consistent"] = all(c["blocks ok"] for c in cross)
    return {"predictions": out, "D": d, "readings": len(rows), "cross couplings computed": len(cross)}


def signature_T(r):
    return (r["h"]["L2V"]["h1"], r["h"]["VL"]["h1"], r["h"]["L2W"]["h1"], r["h"]["L2W*"]["h1"], r["h"]["W1"]["h1"], r["h"]["W1*"]["h1"],
            r["interior"]["W1"], r["interior"]["W1*"], r["10bar' B'"]["zero"], r["10' B"]["zero"])


def signature_L(r):
    return (r["h"]["L2V"]["h1"], r["h"]["VL"]["h1"], r["h"]["L2W"]["h1"], r["h"]["L2W*"]["h1"], r["h"]["W1"]["h1"], r["h"]["W1*"]["h1"],
            r["interior"]["W1"], r["interior"]["W1*"], r["10bar' [a ^ a']"]["zero"], r["10' [f ^ f']"]["zero"])


def agreement(rec):
    """population by population, the set of reading signatures of route T equals route L's"""
    if not ROUTE_T_RECORD.exists():
        return {"pass": None, "note": "route T's record is absent"}
    rt = json.loads(ROUTE_T_RECORD.read_text(encoding="utf-8"))
    out, ok = {}, True
    popsL, popsT = {}, {}
    for blk in rec["A"]:
        popsL.setdefault(blk["population"], set()).update(json.dumps(signature_L(r)) for r in blk["rows"])
    for blk in rt["A"]:
        popsT.setdefault(blk["population"], set()).update(json.dumps(signature_T(r)) for r in blk["rows"])
    for label in popsL:
        same = popsL[label] == popsT.get(label)
        out[label] = {"same readings": same, "route L": sorted(popsL[label]), "route T": sorted(popsT.get(label, []))}
        ok = ok and same
    pT, pL = rt["C"]["predictions"], rec["C"]["predictions"]
    out["predictions agree"] = pT == pL
    out["pass"] = ok and pT == pL and set(popsL) == set(popsT)
    return out


if __name__ == "__main__":
    res = main()
    print(json.dumps(res["C"]["predictions"], indent=1))
    print("agreement with route T:", res["C"]["agreement with route T"].get("pass"))
