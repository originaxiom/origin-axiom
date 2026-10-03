#!/usr/bin/env python3
"""B1534 controls -- run before the seal; none reads a twisted term T(nu, chi, c) with chi != 1 in the population, and no
chi = 1 term at a special class.  Writes controls.json and controls_run.txt.

K0  the states: route E's exact holonomies of m135 and m136 satisfy the relators in PGL(2, Q(i)), the cusp generators commute
    and are parabolic, and the four satisfies the relators exactly.
K1  the banked identity: every member of m135 and m136 (h^1(V_eta), the interior dimension, kappa in {1, -1, +-i, omega,
    omega^2}) and every chi = 1 term at the banked classes reproduce sm:B1530 (run_a.json, post_run_e136.json).
K2  Lemma Z': at characters outside the contributing set the cusp is acyclic for W1 (x) chi and Lambda^2 W1 (x) chi
    (t0 = s0 = 0) and the term is (0, 0): sampled at every member.
K3  the contributing sets are groups (closed), of the orders Lemma Z' gives, with the subgroup counts of Goursat's formula.
K4  Lemma J's pencil at chi = 1 (m135's two non-simple members): for each of the four modules and c in {c_b, c_int,
    c_b + c_int}, h^1 predicted by the pencil (h^1(S) - rank delta^0 + h^1(Q) - rank delta^1_c) equals h^1 computed directly; the
    pencil's generic rank and its special points are recorded (no term is read there); route N's pencil ranks agree.
K5  the quadratic test over K = Q(i, sqrt 2, sqrt 3): split and irreducible examples.
K6  the restriction of scalars: at chi = 1 on m135's member u = (0, 1/2), R at s = 2 + 0 sqrt 5 reproduces the banked
    reading at c_b + 2 c_int, and R at s = sqrt 5 (generic unless K4 lists it) reads the banked generic boundary value.
K7  route C (the permutation module, Lemma S's middle term, never split into characters) on two covers whose characters other
    than 1 lie outside the contributing set or were banked: the 3-fold cyclic cover along t at m135's interior class (Lemma Z'
    gives the base's count) and the common double cover at m136's kappa = -1 member (sm:B1530 post-run: (-1, -1)).
K8  route N reproduces the banked chi = 1 terms at route E's carried classes.
K9  route N's own pencils at chi = 1 (m135's two-class members) have route E's generic ranks and special points (no term read
    there)."""
import json
import sys
import time
import warnings
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import silver_lib as SL  # noqa: E402

E, S = SL.E, SL.S
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def banked():
    B = SL.B1530V
    a = json.loads((B / "run_a.json").read_text())
    e = json.loads((B / "post_run_e136.json").read_text())
    out = {}
    for r in a["rows"]:
        RE = r["route E"]
        out[("-LLRR", tuple(r["u"]), "0")] = {"h1": RE["h1"]["V_eta"], "n": RE["n"]["V_eta"],
                                              "W1": {k: (v["I(W)"], v["I(L2W)"]) for k, v in RE["W1"].items()}}
    turn = {"1": "0", "-1": "1/2"}                      # sm:B1530 labels kappa; this arc labels its turn
    for r in e["rows"]:
        if r["h1"]["V_eta"] == 0:
            out[("+LLRR", tuple(r["u"]), turn[r["kappa"]])] = {"h1": 0, "n": 0, "W1": {}}
            continue
        out[("+LLRR", tuple(r["u"]), turn[r["kappa"]])] = {"h1": r["h1"]["V_eta"], "n": r["n (interior)"]["V_eta"],
                                                           "W1": {k: (v["I(W)"], v["I(L2W)"]) for k, v in r["W1"].items()}}
    return out


def kron(A, P):
    n, m = len(A), len(P)
    out = E.zeros(n * m, n * m)
    for i in range(n):
        for j in range(n):
            if A[i][j].is_zero():
                continue
            for k in range(m):
                for l in range(m):
                    if P[k][l] != 0:
                        out[i * m + k][j * m + l] = A[i][j]
    return out


def perm_module(G, mod, psi, order):
    """mod (x) C[Z/order], Gamma acting on C[Z/order] by translation by psi(g)"""
    mats = {}
    for g in G.gens:
        P = [[1 if (k - l - psi[g]) % order == 0 else 0 for l in range(order)] for k in range(order)]
        mats[g] = kron(mod.M[g], P)
    return E.Module(G.gens, mats)


def main():
    t0 = time.time()
    out = {"started": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    say(f"B1534 controls, {out['started']}")
    bk = banked()
    sts = {s: SL.setup(s) for s in ("-LLRR", "+LLRR")}
    # K0
    k0 = {}
    for s, st in sts.items():
        chk = S.check_sl2(st["G"], SL.holonomy(s))
        k0[s] = {"PGL(2) checks": chk, "the four satisfies the relators": st["rho"].check(st["G"].rels)}
    out["K0"] = {"holds": all(all(v["PGL(2) checks"].values()) and v["the four satisfies the relators"] for v in k0.values()),
                 "detail": k0}
    say(f"K0 holds: {out['K0']['holds']}")
    # K1
    k1 = {"members": {}, "terms": {}}
    ok1 = True
    allm = {}
    for s, st in sts.items():
        ms = SL.members(st)
        allm[s] = ms
        found = {(tuple(str(x) for x in m["u"]), str(m["kappa"])): (m["h1"], m["n"]) for m in ms}
        exp = {(k[1], k[2]): (v["h1"], v["n"]) for k, v in bk.items() if k[0] == s and v["h1"] > 0}
        k1["members"][s] = {"found": {f"{k}": v for k, v in found.items()}, "agree": found == exp}
        ok1 &= found == exp
        one = SL.char(st, (0, 0), 0)
        for m in ms:
            kk = (s, tuple(str(x) for x in m["u"]), str(m["kappa"]))
            want = bk[kk]["W1"]
            if m["h1"] == 1:
                T, _ = SL.term(st, m, m["classes"]["the class"], one)
                got = {"the class": T}
                ref = {"the class": tuple(want.get("the class", want.get("basis 0")))}
            else:
                T1, _ = SL.term(st, m, m["c_int"], one)
                T2, _ = SL.term(st, m, m["c_b"], one)
                got = {"c_int": T1, "c_b": T2}
                ref = {"c_int": tuple(want["c_int"]), "c_b": tuple(want["c_b"])}
            agree = got == ref
            ok1 &= agree
            k1["terms"][str(kk)] = {"read": got, "banked": ref, "agree": agree}
    out["K1"] = {"holds": ok1, "detail": k1}
    say(f"K1 holds: {ok1} ({time.time() - t0:.0f} s)")
    # K2
    k2, ok2 = {}, True
    for s, st in sts.items():
        for m in allm[s]:
            c = m["classes"]["the class"] if m["h1"] == 1 else m["c_b"]
            for wk in SL.non_contributing_sample(st, m, 2):
                chi = SL.char(st, *wk)
                T, det = SL.term(st, m, c, chi)
                acyc = all(det[x][y] == 0 for x in ("W", "L2W") for y in ("t0", "s0"))
                good = T == (0, 0) and acyc
                ok2 &= good
                k2[f"{s} {tuple(str(x) for x in m['u'])} {m['kappa']} chi {SL.key(wk)}"] = {"T": T, "cusp acyclic": acyc}
    out["K2"] = {"holds": ok2, "detail": k2}
    say(f"K2 holds: {ok2} ({len(k2)} samples, {time.time() - t0:.0f} s)")
    # K3
    k3, ok3 = {}, True
    for s, st in sts.items():
        for m in allm[s]:
            C = SL.contributing(st, m)
            subs = SL.subgroups(C)
            full = SL.closure([((Fraction(w[0]), Fraction(w[1])), k) for w, k in C])
            closed = len(full) == len(C)
            k3[f"{s} {tuple(str(x) for x in m['u'])} {m['kappa']}"] = {"order": len(C), "subgroups": len(subs),
                                                                       "closed": closed}
            ok3 &= closed
    # Goursat (Toth, eq. (5)): Z/4 x Z/2 has 8 subgroups, (Z/2)^2 has 5, (Z/2)^3 has 16
    orders = {(v["order"], v["subgroups"]) for v in k3.values()}
    ok3 &= orders <= {(8, 8), (4, 5), (8, 16)}
    out["K3"] = {"holds": ok3, "detail": k3, "(order, subgroups) seen": sorted(orders)}
    say(f"K3 holds: {ok3}; (order, subgroups): {sorted(orders)}")
    # K4
    k4, ok4 = {}, True
    st = sts["-LLRR"]
    one = SL.char(st, (0, 0), 0)
    for m in allm["-LLRR"]:
        if m["h1"] != 2:
            continue
        for which in ("E", "E*", "L2E", "(L2E)*"):
            Pb, Pi, h1Q, h2S = SL.pencil(st, m, one, which)
            sp = SL.special_points(Pb, Pi)
            rows = {}
            for cname, (a, b) in (("c_b", (E.ONE, E.ZERO)), ("c_int", (E.ZERO, E.ONE)), ("c_b + c_int", (E.ONE, E.ONE))):
                c = SL.lin(m["c_b"], m["c_int"], a, b)
                mods = {n: (M, dS) for n, M, dS in SL.four_modules(m, c, one)}
                M, dS = mods[which]
                A, B = SL._blocks(M, dS)
                CM, CS, CQ = E.Cohomology(st["G"], M), E.Cohomology(st["G"], A), E.Cohomology(st["G"], B)
                rk_d0 = CS.a0 + CQ.a0 - CM.a0
                P = [[a * x + b * y for x, y in zip(rb, ri)] for rb, ri in zip(Pb, Pi)]
                rk_d1 = E.rank(P, h1Q) if P and h1Q else 0
                pred = CS.h1 - rk_d0 + h1Q - rk_d1
                rows[cname] = {"h1 direct": CM.h1, "h1 by the pencil": pred, "rank delta1": rk_d1}
                ok4 &= pred == CM.h1
            k4[f"{tuple(str(x) for x in m['u'])} {which}"] = {"h1(Q)": h1Q, "h2(S)": h2S, "generic rank": sp["generic rank"],
                                                              "special points (count, not read)":
                                                                  len(sp["rational"]) + 2 * len(sp["quadratic"]),
                                                              "rows": rows}
    out["K4"] = {"holds": ok4, "detail": k4}
    say(f"K4 holds: {ok4} ({time.time() - t0:.0f} s)")
    for k, v in k4.items():
        say(f"   {k}: h1(Q) {v['h1(Q)']}, h2(S) {v['h2(S)']}, generic rank {v['generic rank']}, special points "
            f"{v['special points (count, not read)']}")
    # K5
    k5 = {}
    K = E.K.of
    tests = {"(s - 1)(s - i)": [E.I_UNIT, -(E.ONE + E.I_UNIT), E.ONE],
             "s^2 - 2": [K(-2), E.ZERO, E.ONE],
             "s^2 - 5": [K(-5), E.ZERO, E.ONE],
             "s^2 + 1": [E.ONE, E.ZERO, E.ONE],
             "s^2 - 7": [K(-7), E.ZERO, E.ONE]}
    expect = {"(s - 1)(s - i)": 2, "s^2 - 2": 2, "s^2 - 5": None, "s^2 + 1": 2, "s^2 - 7": None}
    ok5 = True
    for name, g in tests.items():
        r = SL._quadratic_roots_in_K(g)
        got = None if r is None else len(r)
        k5[name] = got
        ok5 &= got == expect[name]
    out["K5"] = {"holds": ok5, "detail": k5}
    say(f"K5 holds: {ok5} {k5}")
    # K6
    m = next(x for x in allm["-LLRR"] if x["h1"] == 2 and x["u"] == (Fraction(0), Fraction(1, 2)))
    T_r2, _ = SL.term_quadratic(st, m, K(2), E.ZERO, K(5), one)
    T_d2, _ = SL.term(st, m, SL.lin(m["c_b"], m["c_int"], E.ONE, K(2)), one)
    T_s5, _ = SL.term_quadratic(st, m, E.ZERO, E.ONE, K(5), one)
    ok6 = T_r2 == T_d2 == (0, -1) and T_s5 == (0, -1)
    out["K6"] = {"holds": ok6, "R at s = 2": T_r2, "direct at s = 2": T_d2, "R at s = sqrt 5": T_s5}
    say(f"K6 holds: {ok6}: R(2) {T_r2}, direct(2) {T_d2}, R(sqrt 5) {T_s5} ({time.time() - t0:.0f} s)")
    # K7
    k7 = {}
    G = st["G"]
    W1 = E.extension(m["V"], m["c_int"], m["L"])
    psi = {"a": 0, "b": 0, "t": 1}
    I_w = E.class_index(G, perm_module(G, W1, psi, 3))["I"]
    I_l = E.class_index(G, perm_module(G, W1.wedge2(), psi, 3))["I"]
    k7["m135 u (0, 1/2), c_int, the 3-fold cover along t"] = {"route C": (I_w, I_l), "expected": (-1, -1)}
    st6 = sts["+LLRR"]
    m6 = next(x for x in allm["+LLRR"] if x["kappa"] == Fraction(1, 2) and x["u"] == (Fraction(0), Fraction(1, 2)))
    W16 = E.extension(m6["V"], m6["classes"]["the class"], m6["L"])
    I_w6 = E.class_index(st6["G"], perm_module(st6["G"], W16, psi, 2))["I"]
    I_l6 = E.class_index(st6["G"], perm_module(st6["G"], W16.wedge2(), psi, 2))["I"]
    k7["m136 u (0, 1/2), kappa -1, the common double cover (along t)"] = {"route C": (I_w6, I_l6), "expected": (-1, -1)}
    ok7 = all(v["route C"] == v["expected"] for v in k7.values())
    out["K7"] = {"holds": ok7, "detail": k7}
    say(f"K7 holds: {ok7} {k7} ({time.time() - t0:.0f} s)")
    # K8
    import silver_n as SN
    k8, ok8 = {}, True
    for s, stt in sts.items():
        stn = SN.setup(stt["sign"], stt["word"], stt["rho"])
        for mm in allm[s]:
            V, lval = SN.member_V(stn, mm["u"], mm["kappa"])
            one_n = SN.char(stn, (0, 0), 0)
            cls = {"the class": mm["classes"]["the class"]} if mm["h1"] == 1 else {"c_int": mm["c_int"], "c_b": mm["c_b"]}
            for name, c in cls.items():
                Tn, info = SN.term(stn, V, lval, SN.carry(stn, c), one_n)
                Te = tuple(k1["terms"][str((s, tuple(str(x) for x in mm["u"]), str(mm["kappa"])))]["read"][name])
                good = Tn == Te and info["checks"]
                ok8 &= good
                k8[f"{s} {tuple(str(x) for x in mm['u'])} {mm['kappa']} {name}"] = {"N": Tn, "E": Te, "checks": info["checks"]}
        k8[f"{s} the frames' conjugator"] = stn["xinfo"]
    out["K8"] = {"holds": ok8, "detail": k8}
    say(f"K8 holds: {ok8} ({time.time() - t0:.0f} s)")
    # K9: route N's own pencils at chi = 1 on m135's two-class members locate the same special points as route E's
    k9, ok9 = {}, True
    import mpmath as mp
    stt = sts["-LLRR"]
    stn = SN.setup(stt["sign"], stt["word"], stt["rho"])
    one = SL.char(stt, (0, 0), 0)
    one_n = SN.char(stn, (0, 0), 0)
    for mm in allm["-LLRR"]:
        if mm["h1"] != 2:
            continue
        V, lval = SN.member_V(stn, mm["u"], mm["kappa"])
        for which in ("E", "E*", "L2E", "(L2E)*"):
            Pb, Pi, h1Q, h2S = SL.pencil(stt, mm, one, which)
            sp = SL.special_points(Pb, Pi)
            ev = [s.num(mp) for s in sp["rational"]]
            for (c0, c1, c2) in sp["quadratic"]:
                a, b, c = c2.num(mp), c1.num(mp), c0.num(mp)
                dsc = mp.sqrt(b * b - 4 * a * c)
                ev += [(-b + dsc) / (2 * a), (-b - dsc) / (2 * a)]
            Pbn, Pin, inf = SN.pencil(stn, V, lval, SN.carry(stn, mm["c_b"]), SN.carry(stn, mm["c_int"]), one_n, which)
            spn = SN.special_points(Pbn, Pin)
            good = (sp["generic rank"] == spn["generic rank"] and len(ev) == len(spn["special"]) and
                    all(any(abs(x - y) < mp.mpf(10) ** -25 for y in spn["special"]) for x in ev) and
                    inf["h1(Q)"] == h1Q and inf["h2(S)"] == h2S)
            ok9 &= good
            k9[f"{tuple(str(x) for x in mm['u'])} {which}"] = {"generic rank (E, N)": [sp["generic rank"], spn["generic rank"]],
                                                               "special points (E, N)": [len(ev), len(spn["special"])],
                                                               "agree": good}
    out["K9"] = {"holds": ok9, "detail": k9}
    say(f"K9 holds: {ok9} ({time.time() - t0:.0f} s)")
    out["all hold"] = all(out[k]["holds"] for k in ("K0", "K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8", "K9"))
    out["seconds"] = round(time.time() - t0)
    say(f"all hold: {out['all hold']} ({out['seconds']} s)")
    (HERE / "controls.json").write_text(json.dumps(out, indent=1, default=str))
    (HERE / "controls_run.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
