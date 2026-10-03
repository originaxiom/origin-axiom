#!/usr/bin/env python3
"""B1530 -- the controls, run before the seal on banked data and on structure only.  python3 controls.py -> controls_run.txt,
controls.json.

Route E (exact over Q(zeta_24), exact_lib):
  K1  sm:B1515's member on M6 = +(LR)^6 at u = (1/8, 1/2), lam = 1 (banked: B1515 FINDINGS sections 3 and 5 (a)):
      h1(V) = h1(V_eta) = h1(V (x) L) = 2; (I(W1), I(Lambda^2 W1)) = (+1, -1) at a boundary-type class and (0, -1) at the
      interior class; W2 reads (-1, +1).  The holonomy is m004's, read exactly over Q(omega), with t -> t^6.
  K2  the positive control, R40 on m010 (sm:B1515 control K6; the audit lane's COEFFICIENT_PARENT), at u = e^{+-i pi/3}:
      I(V) = I(Lambda^2 V) = I(W) = I(Lambda^2 W) = +1, n(Lambda^2 W) = 2, n(Lambda^2 W*) = 1.  It is generation-shaped
      (I(W) = I(Lambda^2 W) != 0), so the instrument can read a generation where one exists.
  K3  m135's banked rows (sm:B1529's post_run_exact_m135.json): (h1, h1*, t0, s0) and n at its eight characters at kappa = 1.
  S   Lemma T on m135's cusp: for c_P in H^1(P; rho) at sample points, [[rho_P, c_P], [0, 1]] has (t0, s0) = (1, 2) and its
      exterior square (2, 3); e ^ c_P is non-zero in H^1(P; Lambda^2 rho).
  K4  the mechanism functions on banked cases:
      (a) the fibre monodromy of the four on m004 at the trivial character: chi_C = (s - 1)^2 (s^2 - 6 s + 1) and one Jordan
          block J2 at 1 (sm:B1515 Lemma 10, from sm:B1509's Q(1, s));
      (b) M6's trivial character (simple, case (a); sm:B1515 Lemma 8 (i) and its table): x cup c = 0 by the fibre test, and
          W1 reads (0, 0);
      (c) K1's member: the lift of the interior class of V (x) L to H^1(Lambda^2 W1) at c = c_int restricts outside Lambda_A
          (implied by the banked (0, -1): r1 = 4 = 2 + 1 + 1, sm:B1515 section 5 (c)).
Not computed here: any index of W1, W2 or their exterior squares on m135; the Jordan type of S0 there; mu; x cup c.  Those are
the sealed run's."""
import json
import sys
import time
import warnings
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import exact_lib as E  # noqa: E402
import exact_states as S  # noqa: E402

LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


def brief(r):
    return {k: r[k] for k in ("I", "a0", "b0", "t0", "s0", "h1", "h1*", "r1", "n", "n*")}


# ============================================================================================ K1: B1515's member on M6
def k1():
    t = time.time()
    G, img, chars, D = S.group("+", "LR" * 6)
    g2 = S.eisenstein_sl2("+", "LR")
    rho = S.four_module(S.power_t(g2, 6))
    assert rho.check(G.rels)
    u = (Fr(1, 8), Fr(1, 2))
    assert u in chars
    ch = S.nu("+", u, 0)
    V = rho.twist(ch)
    L = E.line(G.gens, S.power_char(ch, -4))
    Veta = rho.twist(S.power_char(ch, 5))
    VL = rho.twist(S.power_char(ch, -3))
    hs = {name: E.Cohomology(G, M).h1 for name, M in (("V", V), ("V_eta", Veta), ("V (x) L", VL))}
    CE = E.Cohomology(G, Veta)
    ints = CE.interior()
    assert len(ints) == 1
    c_int = CE.combine(ints[0])
    # a boundary-type class: the first representative not proportional to c_int modulo B^1
    c_b = next(z for z in CE.reps if E.rank_vectors(CE.Bvecs + [c_int, z], CE.d * CE.ng) == CE.dimB + 2)
    out = {"u": [str(x) for x in u], "h1": hs, "W1": {}, "W2": {}}
    for name, c in (("boundary-type", c_b), ("interior", c_int)):
        W1 = E.extension(V, c, L)
        assert W1.check(G.rels)
        a, b = E.class_index(G, W1), E.class_index(G, W1.wedge2())
        out["W1"][name] = {"I(W1)": a["I"], "I(L2W1)": b["I"], "W1": brief(a), "L2W1": brief(b)}
    # W2* = [[V*, c' L^-1], [0, L^-1]], c' in H^1(V* (x) L) = H^1(V_eta*)
    Vd = V.dual()
    Linv = E.line(G.gens, S.power_char(ch, 4))
    CEd = E.Cohomology(G, Veta.dual())
    ints_d = CEd.interior()
    cd_int = CEd.combine(ints_d[0])
    cd_b = next(z for z in CEd.reps if E.rank_vectors(CEd.Bvecs + [cd_int, z], CEd.d * CEd.ng) == CEd.dimB + 2)
    for name, c in (("boundary-type", cd_b), ("interior", cd_int)):
        W2s = E.extension(Vd, c, Linv)
        assert W2s.check(G.rels)
        a, b = E.class_index(G, W2s), E.class_index(G, W2s.wedge2())
        out["W2"][name] = {"I(W2)": -a["I"], "I(L2W2)": -b["I"]}
    ok = (hs == {"V": 2, "V_eta": 2, "V (x) L": 2}
          and (out["W1"]["boundary-type"]["I(W1)"], out["W1"]["boundary-type"]["I(L2W1)"]) == (1, -1)
          and (out["W1"]["interior"]["I(W1)"], out["W1"]["interior"]["I(L2W1)"]) == (0, -1)
          and (out["W2"]["boundary-type"]["I(W2)"], out["W2"]["boundary-type"]["I(L2W2)"]) == (-1, 1))
    out["seconds"] = round(time.time() - t)
    say("K1 (B1515's member on M6, u = (1/8, 1/2)):", json.dumps({k: v for k, v in out.items() if k != "W1"}, default=str))
    for name in out["W1"]:
        say("   W1 at the", name, "class:", (out["W1"][name]["I(W1)"], out["W1"][name]["I(L2W1)"]))
    say("   K1 holds:", ok)
    return out, ok


# ============================================================================================ K4: the mechanism, banked cases
def k4():
    t = time.time()
    out, ok = {}, True
    # (a) m004, trivial character
    G1, img1, _, _ = S.group("+", "LR")
    rho1 = S.four_module(S.eisenstein_sl2("+", "LR"))
    Q, _ = E.fibre_C(rho1, S.phi_prime("+", img1), S.tprime("+"))
    chi = [c.rational() for c in E.charpoly(Q)]
    # (s - 1)^2 (s^2 - 6 s + 1) = s^4 - 8 s^3 + 14 s^2 - 8 s + 1
    good_a = chi == [1, -8, 14, -8, 1] and E.jordan_partition(Q, 1) == [2]
    out["(a) m004 trivial character"] = {"chi_C": [str(x) for x in chi], "Jordan at 1": E.jordan_partition(Q, 1),
                                         "holds": good_a}
    # (b) M6, trivial character
    G6, img6, _, _ = S.group("+", "LR" * 6)
    rho6 = S.four_module(S.power_t(S.eisenstein_sl2("+", "LR"), 6))
    C6 = E.Cohomology(G6, rho6)
    assert C6.h1 == 1 and C6.n == 0
    c = C6.reps[0]
    vanishes, _ = E.cup_with_fibration_class_vanishes(rho6, c, S.phi_prime("+", img6), S.tprime("+"))
    W1 = E.extension(rho6, c)
    rb = (E.class_index(G6, W1)["I"], E.class_index(G6, W1.wedge2())["I"])
    good_b = vanishes and rb == (0, 0)
    out["(b) M6 trivial character"] = {"x cup c = 0": vanishes, "(I(W1), I(L2W1))": list(rb), "holds": good_b}
    # (c) K1's member: the lift of the interior class of V (x) L, at c = c_int of V_eta
    u = (Fr(1, 8), Fr(1, 2))
    ch = S.nu("+", u, 0)
    V = rho6.twist(ch)
    L = E.line(G6.gens, S.power_char(ch, -4))
    CE = E.Cohomology(G6, rho6.twist(S.power_char(ch, 5)))
    c_int = CE.combine(CE.interior()[0])
    CQ = E.Cohomology(G6, rho6.twist(S.power_char(ch, -3)))
    y_int = CQ.combine(CQ.interior()[0])
    in_lamA, dimLamA, is_cob, lifts = E.mu_test(G6, V, c_int, L, y_int)
    good_c = lifts and dimLamA == 2 and in_lamA is False
    out["(c) K1's member"] = {"y lifts": lifts, "dim Lambda_A": dimLamA, "mu in Lambda_A": in_lamA, "holds": good_c}
    ok = good_a and good_b and good_c
    out["seconds"] = round(time.time() - t)
    say("K4 (the mechanism on banked cases):", json.dumps(out, default=str))
    return out, ok


# ============================================================================================ K2: R40 on m010
M010 = E.Group(["a", "b"], ["aabaBaaBab"], ("AbAA", "babA"), "m010 (R40's presentation)")


def _binary_power(lin, k):
    """(alpha X + beta Y)^k as {(i, j): coefficient of X^i Y^j}"""
    out = {(0, 0): E.ONE}
    for _ in range(k):
        nxt = {}
        for (i, j), c in out.items():
            for (di, dj), f in (((1, 0), lin[0]), ((0, 1), lin[1])):
                key = (i + di, j + dj)
                nxt[key] = nxt.get(key, E.ZERO) + c * f
        out = nxt
    return out


def sym3(M):
    """Sym^3 of a 2 x 2 matrix: e1 -> M00 e1 + M10 e2, e2 -> M01 e1 + M11 e2 on the coordinates X, Y (as sm:B1515 route_t)"""
    mons = [(3, 0), (2, 1), (1, 2), (0, 3)]
    lx, ly = (M[0][0], M[1][0]), (M[0][1], M[1][1])
    cols = []
    for (a, b) in mons:
        pa, pb = _binary_power(lx, a), _binary_power(ly, b)
        img = {}
        for (i1, j1), c1 in pa.items():
            for (i2, j2), c2 in pb.items():
                key = (i1 + i2, j1 + j2)
                img[key] = img.get(key, E.ZERO) + c1 * c2
        cols.append([img.get(m, E.ZERO) for m in mons])
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def k2():
    t = time.time()
    out, ok = [], True
    for k in (4, 20):                                    # u = e^{+- i pi / 3}
        u = E.zeta(k)
        Am = E.mat([[0, 1], [-1, 1]])
        Bm = [[E.ZERO, u * u], [u, E.K.of(-2)]]
        V = E.Module(M010.gens, {"a": E.scal(sym3(Am), u), "b": E.scal(sym3(Bm), -1)})
        Lm = E.Module(M010.gens, {"a": [[u * u]], "b": [[E.ONE]]})
        W = E.Module(M010.gens, {g: [list(V.M[g][i]) + [E.ZERO] for i in range(4)] + [[E.ZERO] * 4 + [Lm.M[g][0][0]]]
                                 for g in M010.gens})
        row = {}
        for name, M in (("V", V), ("L2V", V.wedge2()), ("W", W), ("L2W", W.wedge2())):
            assert M.check(M010.rels)
            row[name] = brief(E.class_index(M010, M))
        good = (all(row[n]["I"] == 1 for n in row) and row["L2W"]["n"] == 2 and row["L2W"]["n*"] == 1)
        ok &= good
        out.append({"u": f"zeta_24^{k}", "rows": row, "holds": good})
        say(f"K2 (R40 on m010, u = zeta_24^{k}): I(V), I(L2V), I(W), I(L2W) =",
            [row[n]["I"] for n in ("V", "L2V", "W", "L2W")], "n(L2W), n(L2W*) =", (row["L2W"]["n"], row["L2W"]["n*"]),
            "holds:", good)
    return {"rows": out, "seconds": round(time.time() - t)}, ok


# ============================================================================================ K3: m135's banked rows
def k3():
    t = time.time()
    G, img, chars, D = S.group("-", "LLRR")
    g2 = S.m135_sl2()
    chk = S.check_sl2(G, g2)
    assert all(chk.values()), chk
    rho = S.four_module(g2)
    assert rho.check(G.rels)
    banked = json.loads((S.B1529 / "post_run_exact_m135.json").read_text())
    want = {tuple(r["u"]): (tuple(r["(h1, h1*, t0, s0)"]), tuple(r["n(V), n(V*)"])) for r in banked["rows"]}
    rows, ok = [], True
    for u in chars:
        V = rho.twist(S.nu("-", u, 0))
        ci = E.class_index(G, V)
        got = ((ci["h1"], ci["h1*"], ci["t0"], ci["s0"]), (ci["n"], ci["n*"]))
        w = want[(str(u[0]), str(u[1]))]
        good = (tuple(got[0]), tuple(got[1])) == (tuple(w[0]), tuple(w[1])) and ci["I"] == 0
        ok &= good
        rows.append({"u": [str(x) for x in u], "(h1, h1*, t0, s0)": list(got[0]), "n, n*": list(got[1]), "I": ci["I"],
                     "agrees with sm:B1529": good})
    say("K3 (m135's eight characters at kappa = 1 against sm:B1529's exact record):", "all agree" if ok else "DISAGREE",
        [(r["u"], r["(h1, h1*, t0, s0)"], r["n, n*"]) for r in rows if r["(h1, h1*, t0, s0)"] != [1, 1, 1, 1]])
    return {"sl2 checks": chk, "rows": rows, "seconds": round(time.time() - t)}, ok


# ============================================================================================ S: Lemma T on m135's cusp
def lemma_t():
    t = time.time()
    G, img, chars, D = S.group("-", "LLRR")
    rho = S.four_module(S.m135_sl2())
    P = [rho.word(w) for w in G.cusp]
    d = 4
    Id = E.eye(d)
    Dp = [E.madd(X_, Id, -1) for X_ in P]
    # Z^1(P; rho): (u1, u2) with (P1 - 1) u2 = (P2 - 1) u1; B^1(P) = {((P1 - 1) v, (P2 - 1) v)}
    eq = [[-x for x in Dp[1][i]] + list(Dp[0][i]) for i in range(d)]
    Z = E.nullspace(eq, 2 * d)
    BP = [sum(([Dp[k][i][j] for i in range(d)] for k in range(2)), []) for j in range(d)]
    basis, reps = [], []
    for v in BP:
        if E.rank_vectors(basis + [v], 2 * d) > len(basis):
            basis.append(v)
    for z in Z:
        if E.rank_vectors(basis + [z], 2 * d) > len(basis):
            basis.append(z)
            reps.append(z)
    assert len(reps) == 2, len(reps)
    e = E.nullspace(Dp[0] + Dp[1], d)
    assert len(e) == 1
    e = e[0]
    samples = [(1, 0), (0, 1), (1, 1), (1, -1), (1, 2), (2, 1), (3, -5), (Fr(1, 3), 7)]
    rows, ok = [], True
    for (x, y) in samples:
        cP = [E.K.of(x) * a + E.K.of(y) * b for a, b in zip(reps[0], reps[1])]
        mats = []
        for k in range(2):
            Wk = E.zeros(d + 1, d + 1)
            for i in range(d):
                for j in range(d):
                    Wk[i][j] = P[k][i][j]
                Wk[i][d] = cP[k * d + i]
            Wk[d][d] = E.ONE
            mats.append(Wk)
        assert all((E.mmul(mats[0], mats[1])[i][j] == E.mmul(mats[1], mats[0])[i][j]) for i in range(d + 1)
                   for j in range(d + 1)), "c_P is not a cocycle"

        def t0s0(ms):
            n = len(ms[0])
            I_ = E.eye(n)
            t0 = n - E.rank(E.madd(ms[0], I_, -1) + E.madd(ms[1], I_, -1), n)
            mi = [E.transpose(E.minv(m)) for m in ms]
            s0 = n - E.rank(E.madd(mi[0], I_, -1) + E.madd(mi[1], I_, -1), n)
            return t0, s0
        w1 = t0s0(mats)
        w2 = t0s0([E.wedge2(m) for m in mats])
        # e ^ c_P in H^1(P; Lambda^2 rho): non-zero modulo B^1(P; Lambda^2 rho)
        L2P = [E.wedge2(m) for m in P]
        D2 = [E.madd(m, E.eye(6), -1) for m in L2P]
        BP2 = [sum(([D2[k][i][j] for i in range(6)] for k in range(2)), []) for j in range(6)]
        ewc = E.wedge_vec(e, cP[:d]) + E.wedge_vec(e, cP[d:])
        nonzero = not E.in_span(ewc, BP2, 12)
        good = w1 == (1, 2) and w2 == (2, 3) and nonzero
        ok &= good
        rows.append({"c_P": [str(x), str(y)], "(t0, s0) of W1|P": list(w1), "of Lambda^2": list(w2), "e ^ c_P != 0": nonzero})
    say("S (Lemma T on m135's cusp): (t0, s0) = (1, 2) and (2, 3), e ^ c_P != 0 at all", len(samples), "samples:", ok)
    return {"rows": rows, "seconds": round(time.time() - t)}, ok


def main():
    t0 = time.time()
    say(f"B1530 controls, {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}")
    res = {}
    oks = {}
    for name, fn in (("S", lemma_t), ("K3", k3), ("K2", k2), ("K1", k1), ("K4", k4)):
        res[name], oks[name] = fn()
    res["all hold"] = all(oks.values())
    res["holds"] = oks
    res["seconds"] = round(time.time() - t0)
    say("all controls hold:", res["all hold"], oks, f"({res['seconds']} s)")
    (HERE / "controls.json").write_text(json.dumps(res, indent=1, default=str))
    (HERE / "controls_run.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
