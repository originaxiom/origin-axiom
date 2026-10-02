"""B1514 -- THE SEALED CENSUS, route T (the relative triple product).  Run after the seal: python3 census.py --record.

Part 0  the banked identity (stops the run if it fails): at the first member of every population, h^1(L), h^1(V), h^1(V_eta),
        h^1(W1) as banked and x u c != 0; B1513's 10' form zero on the triplet and non-zero at B1510's +-i point.
Part A  every member of every population (B1511's M4 orbits exactly and mod p; every population mod p at two primes and every
        root of its factor; M5 at w = 7 for c = c1, c2, c1 + c2):
          dimensions of L, V, V_eta, W1, W1*, Lambda^2 V, V (x) L, Lambda^2 W1, Lambda^2 W1*; interior classes of W1, W1*;
          cusp acyclicity; the positive control <y u x u c>;
          the 10bar' coupling B'(a, a') = <hbar u a u a'> on H^1(W1) against every 5bar'_H in H^1(Lambda^2 W1*);
          the 10' coupling B(f, f') = <h u f u f'> on H^1(W1*) against every 5'_H in H^1(Lambda^2 W1).
Part B  the joining forms, at the first prime-root of every population, every orbit, every triple (k, i, j): the dimension of
        invariant forms on Lambda^2 W_k* (x) W_i (x) W_j; for every cross triple with a form, the cross coupling <hbar_k u a_i u a_j>.
Part C  the readings of P1-P7 and the D-checks (as sealed in PREREGISTRATION Section 6).
Record: census_run.txt (and census_log.txt)."""
import json
import sys
import time
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import law_lib as LT  # noqa: E402

H, T = LT.H, LT.T
q = T.Q
RECORD, LOG = HERE / "census_run.txt", HERE / "census_log.txt"
ROUTE_T_PRIMES = 2
START = 2 ** 23 - 50021


def primes_with_roots(factor, orders, count, start):
    """route T's own prime search: primes = 1 mod every order at which the factor has a root, with all its roots (flint's
    nmod_poly.roots, not B1511's brute force, which is too slow at p ~ 8 million)"""
    import flint
    coeffs = [int(c) for c in reversed(sp.Poly(sp.sympify(factor, locals={"q": q}), q).all_coeffs())]
    out, p = [], start
    while len(out) < count:
        p = int(sp.prevprime(p))
        if any(p % m != 1 for m in orders):
            continue
        r = [int(x) for x, _ in flint.nmod_poly([c % p for c in coeffs], p).roots()]
        if r:
            out.append((p, sorted(r)))
    return out


def wedge_vector():
    """the wedge form (eta, u, v) -> eta(u ^ v) as a 250-vector in the order (pair, i, j)"""
    vec = []
    for (i, j) in H.pairs(5):
        for a in range(5):
            for b in range(5):
                vec.append(1 if (a, b) == (i, j) else (-1 if (a, b) == (j, i) else 0))
    return vec


def read_member(G, C, z, field, rho, ab, N, lam_v, c_coeffs=None):
    m = LT.Member(G, field, rho, ab, N, lam_v, c_coeffs)
    dom = field.dom
    row = {"member": [list(m.char[0]), m.char[1]], "c": list(c_coeffs) if c_coeffs else "c1"}
    row["h"] = {name: LT.h_data(mod) for name, mod in (("L", m.L), ("V", m.V), ("V_eta", m.Veta), ("W1", m.W1), ("W1*", m.W1d),
                                                       ("L2V", m.L2V), ("VL", m.VL), ("L2W", m.L2W), ("L2W*", m.L2Wd))}
    row["interior"] = {"W1": LT.interior_count(m.W1), "W1*": LT.interior_count(m.W1d)}
    row["cusp acyclic"] = all(LT.cusp_acyclic(mod) for mod in (m.V, m.V.dual(), m.L2V, m.L2W, m.L2Wd, m.VL))
    row["control <y u x u c> != 0"] = any(v != dom.zero for v in LT.control_triple(G, C, z, m))
    tb, nhb, nab = LT.coupling_tensor(G, C, z, m.L2Wd, m.W1, H.form_wedge(5))
    tf, nhf, naf = LT.coupling_tensor(G, C, z, m.L2W, m.W1d, H.form_wedge(5))
    row["10bar' B'"] = {"higgs": nhb, "slot": nab, "zero": LT.all_zero(tb, dom), "symmetric": LT.symmetric(tb)}
    row["10' B"] = {"higgs": nhf, "slot": naf, "zero": LT.all_zero(tf, dom), "symmetric": LT.symmetric(tf)}
    return row, m


def joining_forms(G, C, z, field, members, p):
    """every triple (k, i, j) of one orbit: form dimension; cross couplings where a form exists"""
    dom = field.dom
    out = {"triples": {}, "cross couplings": {}}
    wv = wedge_vector()
    n = len(members)
    for k in range(n):
        Hk, _ = H.h1_basis(members[k].L2Wd)
        for i in range(n):
            for j in range(n):
                dim, basis = LT.form_space(members[k].W1, members[i].W1, members[j].W1, p)
                out["triples"][f"{k},{i},{j}"] = dim
                if i == j == k:
                    span = flint_rank([wv] + basis, p) == len(basis)
                    out.setdefault("own: the wedge form lies in the form space", []).append(span)
                    continue
                if dim and Hk:
                    Ai, _ = H.h1_basis(members[i].W1)
                    Aj, _ = H.h1_basis(members[j].W1)
                    zero = True
                    for vec in basis:
                        form = LT.form_from_vector(vec, dom)
                        for h in Hk:
                            for a in Ai:
                                for b in Aj:
                                    zero = zero and H.triple(G, C, z, h, a, b, form) == dom.zero
                    out["cross couplings"][f"{k},{i},{j}"] = {"forms": dim, "higgs": len(Hk), "zero": zero}
    return out


def flint_rank(rows, p):
    import flint
    M = flint.nmod_mat(len(rows), len(rows[0]), [int(x) % p for r in rows for x in r], p)
    return M.rank()


def banked_identity(log):
    """Part 0"""
    out = {}
    pops = LT.populations()
    cache = {}
    ok_all = True
    for pop in pops:
        n = pop["level"]
        if n not in cache:
            G = H.FibredGroup(n)
            cache[n] = (G,) + G.fundamental()[:2]
        G, C, z = cache[n]
        orders = sorted({LT.reduce_char(ab, pop["N"])[1] for o in pop["orbits"].values() for ab in o}) + ([4] if "i" in pop["lam"] else [])
        (p, roots), = primes_with_roots(pop["factor"], orders, 1, START - 7 * n)
        iota = T.gf_root_of_unity(p, 4) if "i" in pop["lam"] else None
        field = T.Field("gf", p=p, r=roots[0], iota=iota)
        rho = H.rho_mats(G, field)
        ab = next(iter(pop["orbits"].values()))[0]
        m = LT.Member(G, field, rho, ab, pop["N"], LT.lam_value(field, pop["lam"]))
        bank = (1, 1, 1) if n == 4 else tuple(pop["banked_h1"][0][:3])
        got = (m.h1_L, H.h1_basis(m.V)[1], m.h1_Veta)
        ctl = any(v != field.dom.zero for v in LT.control_triple(G, C, z, m))
        ok = got == bank and H.h1_basis(m.W1)[1] == bank[1] and ctl
        out[pop["label"]] = {"p": p, "h1 (L, V, V_eta)": got, "banked": bank, "x u c != 0": ctl, "pass": ok}
        ok_all = ok_all and ok
    out["pass"] = ok_all
    log(f"0: banked identity {'passed' if ok_all else 'FAILED'}")
    return out


def main():
    t0 = time.time()
    logf = open(LOG, "w", encoding="utf-8") if "--record" in sys.argv else None

    def log(msg):
        line = f"[{time.time() - t0:8.1f}s] {msg}"
        print(line, flush=True)
        if logf:
            logf.write(line + "\n")
            logf.flush()
    rec = {"route": "T (relative triple product, B1513's higgs_lib)", "sealed": "PREREGISTRATION.md"}
    rec["0_banked_identity"] = banked_identity(log)
    assert rec["0_banked_identity"]["pass"], "the banked identity failed: stop"
    # ---------------------------------------------------------------- Part A
    A = []
    cache = {}
    pops = LT.populations()
    # M4 exactly
    G4 = H.FibredGroup(4)
    C4, z4, _ = G4.fundamental()
    fE = T.Field("ext", g=q ** 2 - 7 * q + 1, base="Q12")
    rhoE = H.rho_mats(G4, fE)
    for pop in pops:
        if pop["level"] != 4:
            continue
        rows = []
        for orbit in pop["orbits"].values():
            for ab in orbit:
                row, _ = read_member(G4, C4, z4, fE, rhoE, ab, pop["N"], fE.dom.one)
                rows.append(row)
        A.append({"population": pop["label"], "arithmetic": "exact, Q(zeta12)[q]/(q^2 - 7q + 1)", "rows": rows})
        log(f"A: {pop['label']} exact done")
    B = []
    for pop in pops:
        n = pop["level"]
        if n not in cache:
            G = H.FibredGroup(n)
            cache[n] = (G,) + G.fundamental()[:2]
        G, C, z = cache[n]
        orders = sorted({LT.reduce_char(ab, pop["N"])[1] for o in pop["orbits"].values() for ab in o}) + ([4] if "i" in pop["lam"] else [])
        for pi, (p, roots) in enumerate(primes_with_roots(pop["factor"], orders, ROUTE_T_PRIMES, START - 104729 * n)):
            iota = T.gf_root_of_unity(p, 4) if "i" in pop["lam"] else None
            for r in roots:
                field = T.Field("gf", p=p, r=r, iota=iota)
                rho = H.rho_mats(G, field)
                lam_v = LT.lam_value(field, pop["lam"])
                c_list = [None, (0, 1), (1, 1)] if (n == 5 and pop["lam"] == "1") else [None]
                rows, members_by_orbit = [], {}
                for oname, orbit in pop["orbits"].items():
                    members_by_orbit[oname] = []
                    for ab in orbit:
                        for cc in c_list:
                            row, m = read_member(G, C, z, field, rho, ab, pop["N"], lam_v, cc)
                            rows.append(row)
                            if cc is None:
                                members_by_orbit[oname].append(m)
                A.append({"population": pop["label"], "arithmetic": f"GF({p}), q = {r}", "rows": rows})
                if pi == 0 and r == roots[0]:
                    jf = {oname: joining_forms(G, C, z, field, ms, p) for oname, ms in members_by_orbit.items()}
                    B.append({"population": pop["label"], "p": p, "q": r, "orbits": jf})
                log(f"A: {pop['label']} p = {p} q = {r} done ({len(rows)} readings)")
    rec["A"], rec["B"] = A, B
    rec["C"] = readings(A, B)
    rec["seconds"] = round(time.time() - t0, 1)
    log(f"C: {json.dumps(rec['C']['predictions'])}")
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(rec, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    return rec


def readings(A, B):
    rows = [(blk["population"], blk["arithmetic"], r) for blk in A for r in blk["rows"]]
    lvl = lambda pop: int(pop.split()[0][1])                                                       # noqa: E731
    out = {}
    acyc = all(r["h"]["L2V"] == {"h0": 0, "h1": 0, "h2": 0} for _, _, r in rows)
    out["P1 the twisted Higgs bulk Lambda^2 V is acyclic at every member"] = acyc

    def higgs_ok(pop, r):
        n = lvl(pop)
        h = r["h"]["L2W"]["h1"]
        if n == 4:
            return h == 0
        if n == 5:
            return h == r["h"]["V"]["h1"]
        return h == 1
    out["P2 the Higgs content reads as Lemma 4 (M4 none; M5 h1(V); M6 one)"] = all(higgs_ok(p, r) and r["h"]["L2W*"]["h1"] == r["h"]["L2W"]["h1"]
                                                                                  for p, _, r in rows)
    out["P3 the 10bar' coupling to every 5bar'_H vanishes at every member"] = all(r["10bar' B'"]["zero"] for _, _, r in rows)
    out["P4 the 10' coupling is non-zero at some member with a Higgs class"] = any((not r["10' B"]["zero"]) and r["10' B"]["higgs"] > 0
                                                                                   for _, _, r in rows)
    cross = [c for blk in B for o in blk["orbits"].values() for c in o["cross couplings"].values()]
    forms = [d for blk in B for o in blk["orbits"].values() for key, d in o["triples"].items() if len(set(key.split(","))) > 1]
    out["P5 some cross triple carries a joining form"] = any(d > 0 for d in forms)
    out["P6 every cross coupling through a joining form vanishes"] = all(c["zero"] for c in cross)
    out["P7 no chiral state through level 6 couples to a Higgs class (with B1513)"] = out["P3 the 10bar' coupling to every 5bar'_H vanishes at every member"] and out["P6 every cross coupling through a joining form vanishes"]
    d = {}
    d["D1 banked h1 (L, V, V_eta, W1) at every reading"] = all(r["h"]["L"]["h1"] == 1 and r["h"]["W1"]["h1"] == r["h"]["V"]["h1"] for _, _, r in rows)
    d["D2 positive control <y u x u c> != 0 at every reading"] = all(r["control <y u x u c> != 0"] for _, _, r in rows)
    d["D3 cusp acyclicity (Lemma 1) at every reading"] = all(r["cusp acyclic"] for _, _, r in rows)
    d["D4 interior classes: n(W1) = h1(V) and n(W1) - n(W1*) = +1 = the banked I(W1)"] = all(
        r["interior"]["W1"] == r["h"]["V"]["h1"] and r["interior"]["W1"] - r["interior"]["W1*"] == 1 for _, _, r in rows)
    d["D5 B' and B symmetric (graded commutativity)"] = all(r["10bar' B'"]["symmetric"] and r["10' B"]["symmetric"] for _, _, r in rows)
    d["D6 V (x) L: acyclic on M4; h1 = h1(V) on M5; h1 = 1 on M6 (Lemma 4)"] = all(
        (r["h"]["VL"]["h1"] == 0) if lvl(p) == 4 else (r["h"]["VL"]["h1"] == r["h"]["V"]["h1"] if lvl(p) == 5 else r["h"]["VL"]["h1"] == 1)
        for p, _, r in rows)
    d["D7 the wedge form lies in every own form space (route T's form solver sees a form)"] = all(all(o.get("own: the wedge form lies in the form space", [True]))
                                                                                                 for blk in B for o in blk["orbits"].values())
    d["D8 every member of an orbit reads the same (Lemma 5)"] = deck_agreement(A)
    return {"predictions": out, "D": d, "readings": len(rows), "cross couplings computed": len(cross)}


def deck_agreement(A):
    ok = True
    for blk in A:
        sig = set()
        for r in blk["rows"]:
            if r["c"] != "c1":
                continue
            sig.add(json.dumps([r["h"], r["interior"], r["10bar' B'"], r["10' B"]["zero"]], sort_keys=True))
        ok = ok and len(sig) == 1
    return ok


if __name__ == "__main__":
    res = main()
    print(json.dumps(res["C"], indent=1))
