"""B1511 controls, run before the seal (record: controls_run.txt).  None of them touches a non-trivial fibre character: no twisted
polynomial of a non-trivial orbit, no exceptional point of one, and no index of a twisted extension is computed here.

C1  level 1, nu = 1: the characteristic polynomial of S on H^1(F; rho_q) is B1509's monic Q (symbolic in q); S B = B rho(m)^-1.
C2  level 3, nu = 1: the product of three one-step matrices equals the direct computation from the words phi^3(x), phi^3(y), and its
    characteristic polynomial on H^1 is prod (s - r^3) over the roots r of Q (the cube relation), symbolic in q.
C3  the torsion and the characters (B1506, banked): |T_n| = 1, 5, 16, 45, 121, 320 with their invariant factors, T_3 = (Z/4)^2; the
    orbit sizes under the root's deck by level; T_3's orbits are 1 + 3 + 3 x 4.
C4  the cover presentations: rs_cover(n) equals B1506's rs_cover(n) after renaming (n = 1..6); rho_q satisfies every relator exactly
    (symbolic q) for n = 1, 2, 3; the deck on the RS generators acts on the characters as (a, b) -> (b, 3b - a) with lam fixed
    (n = 2..6), and agrees with B1506's closed form.
C5  the banked identity: B1509's index rows at the six points (I(W1), I(W2), I(L2 W1), I(L2 W2), the data of W1 and W1*,
    h^1(A), h^1(A*)), on this arc's general-presentation index over Q(i)[q]/(g) (M_1's RS presentation), and over GF(p) through
    B1374's index_lib at p = 1009, 1033, 1129, at both roots of g.
C6  the pullback (Theorem D, decided at design time by Shapiro and B1509's T2-T3): on s961 with nu_F = 1 and lam = -1,
    at q = 17 + 12 sqrt2 (h^1 = 1, Jordan) the pulled-back extension counts -1; at q = (7 + 3 sqrt5)/2 (h^1 = 2: the simple roots
    s = e^{+-i pi/3} of Q, s^3 = -1) every extension class tried counts 0.  Exact and over GF(p)."""
import json
import sys
import time
import importlib.util
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tower_lib as T  # noqa: E402

ROOT = HERE.parents[2]
PRIMES = (1009, 1033, 1129)


def _b1506():
    spec = importlib.util.spec_from_file_location("b1506_the_level", ROOT / "frontier/B1506_the_level/verification/the_level.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def c1_c2():
    F = T.Field("sym", gaussian=False)
    FM = T.FibreMonodromy(F)
    S1, B1 = FM.level((0, 0), 1, 1)
    P1 = T.charpoly_on_H1(S1)
    S3, B3 = FM.level((0, 0), 1, 3)
    x = sp.Symbol("x")
    cube = sp.resultant(T.Q_MONIC.subs(T.S_, x), T.S_ - x ** 3, x)
    cube = sp.expand(cube / sp.Poly(cube, T.S_).LC())
    P3 = T.charpoly_on_H1(S3)
    m3 = FM.minv * FM.minv * FM.minv
    return {"C1_level1_charpoly_is_monic_Q": sp.simplify(P1 - T.Q_MONIC) == 0,
            "C1_S_B_equals_B_minv": T.dm_equal(S1 * B1, B1 * FM.minv),
            "C1_one_step_equals_words": T.dm_equal(FM.level_by_words((0, 0), 1, 1), S1),
            "C2_level3_product_equals_words": T.dm_equal(FM.level_by_words((0, 0), 1, 3), S3),
            "C2_level3_charpoly_is_the_cube_relation": sp.simplify(P3 - cube) == 0,
            "C2_S_B_equals_B_minv^3": T.dm_equal(S3 * B3, B3 * m3),
            "C2_level3_charpoly": str(sp.factor(P3))}


def c3():
    out = {}
    for n in range(1, 7):
        inv_f, order = T.torsion(n)
        chars, N = T.characters(n)
        orbs = T.orbits(chars, N)
        sizes = {}
        for o in orbs:
            sizes[len(o)] = sizes.get(len(o), 0) + 1
        out[f"level_{n}"] = {"order": order, "invariant_factors": inv_f, "exponent": N, "characters": len(chars),
                             "orbits_by_size": {str(k): v for k, v in sorted(sizes.items())}}
    chars3, N3 = T.characters(3)
    orbs3 = T.orbits(chars3, N3)
    by_order = sorted((sorted({T.order_of(c, N3) for c in o}), len(o)) for o in orbs3)
    out["T3_orbits_(orders, size)"] = [[o, s] for o, s in by_order]
    out["T3_orbit_list"] = [o for o in orbs3]
    out["orders_match_B1506"] = [out[f"level_{n}"]["order"] for n in range(1, 7)] == [1, 5, 16, 45, 121, 320]
    return out


def c4():
    L = _b1506()
    res = {}
    for n in range(1, 7):
        mine = T.rs_cover(n)
        g6, w6, rw6, rels6, mu6, lam6 = L.rs_cover(n)
        ren = {"a": "m", "A": "M", "b": "n", "B": "N", "z": "z", "Z": "Z"}
        for k in range(n):
            ren[L.RS_LETTERS[k]] = chr(ord("a") + k)
            ren[L.RS_LETTERS[k].upper()] = chr(ord("a") + k).upper()
        conv = lambda w: "".join(ren[c] for c in w)
        same_rels = [conv(r) for r in rels6] == mine["rels"]
        same_lam = conv(lam6) == mine["lam"]
        same_words = all(conv(w6[g]) == mine["words"][ren[g]] for g in g6)
        # the deck
        dk = T.rs_deck(mine)
        cf = L.rs_closed_form(n)
        same_deck = all(T.red(conv(cf[g])) == T.red(dk[ren[g]]) for g in g6) if n >= 2 else None
        res[n] = {"relators_equal_B1506": same_rels, "longitude_equal_B1506": same_lam, "words_equal_B1506": same_words,
                  "deck_equal_B1506_closed_form": same_deck}
    # rho_q satisfies the relators, symbolic
    mats = T.symbolic_mats()
    for n in (1, 2, 3):
        cov = T.rs_cover(n)
        gm = {g: T.word_matrix(mats, cov["words"][g]) for g in cov["gens"]}
        ok = True
        for r in cov["rels"]:
            X = sp.eye(4)
            for ch in r:
                X = X * (gm[ch] if ch.islower() else gm[ch.lower()].inv())
            ok = ok and X.applyfunc(sp.cancel) == sp.eye(4)
        res[n]["rho_q_satisfies_relators_symbolic"] = ok
    # the deck on characters: nu o tau on the RS generators is the character (deck(a, b), lam)
    for n in (2, 3, 4, 5, 6):
        cov = T.rs_cover(n)
        chars, N = T.characters(n)
        dk = T.rs_deck(cov)
        ok = True
        for ab in chars:
            for lam_k in range(4):
                ex = T.rs_character_exponents(cov, ab, N, lam_k, 4)
                ex2 = T.rs_character_exponents(cov, T.deck(ab, N), N, lam_k, 4)
                for g in cov["gens"]:
                    e1 = e2 = 0
                    for ch in dk[g]:
                        s = 1 if ch.islower() else -1
                        e1 += s * ex[ch.lower()][0]
                        e2 += s * ex[ch.lower()][1]
                    ok = ok and (e1 - ex2[g][0]) % N == 0 and (e2 - ex2[g][1]) % 4 == 0
                # and nu is a character: every relator has exponent 0
                for r in cov["rels"]:
                    e1 = e2 = 0
                    for ch in r:
                        s = 1 if ch.islower() else -1
                        e1 += s * ex[ch.lower()][0]
                        e2 += s * ex[ch.lower()][1]
                    ok = ok and e1 % N == 0 and e2 % 4 == 0
        res[n]["deck_acts_on_characters_as_(b,3b-a)_and_characters_kill_relators"] = ok
    return res


# ------------------------------------------------------------------------------------------------ the index rows
def index_rows(rep, rels, mu, lam, mode, p=None):
    """B1509's rows for V = rep (rank 4) with h^1(V) = h^1(V*) = 1 classes; mode 'exact' or 'gf'"""
    ix = (lambda R: T.index(R, rels, mu, lam)) if mode == "exact" else (lambda R: T.index_gf(R, rels, mu, lam, p))
    cls, h1A = T.h1_classes(rep, rels)
    clsd, h1Ad = T.h1_classes(rep.dual(), rels)
    out = {"h1(A)": h1A, "h1(A*)": h1Ad}
    if h1A >= 1:
        W1 = T.extension_rep(rep, cls[0])
        assert W1.check(rels)
        i1 = ix(W1)
        out["I(W1)"] = i1["I"]
        out["W1 data (a0,a1,t0,r1)"] = [i1["a0"], i1["a1"], i1["t0"], i1["r1"]]
        out["W1* data"] = [i1["b0"], i1["b1"], i1["s0"], i1["q1"]]
        out["I(Lambda2 W1)"] = ix(T.wedge2_rep(W1))["I"]
    if h1Ad >= 1:
        W1s = T.extension_rep(rep.dual(), clsd[0])
        assert W1s.check(rels)
        out["I(W2) = -I(W1[A*])"] = -ix(W1s)["I"]
        out["I(Lambda2 W2) = -I(Lambda2 W1[A*])"] = -ix(T.wedge2_rep(W1s))["I"]
    return out


def c5():
    rec = json.loads((ROOT / "frontier/B1509_the_join_on_the_projective_vacuum/verification/extension_index_run.txt").read_text())
    banked = {(r["q"], r["mu"]): r for r in rec["exact"]}
    keys = ["I(W1)", "I(W2) = -I(W1[A*])", "I(Lambda2 W1)", "I(Lambda2 W2) = -I(Lambda2 W1[A*])", "W1 data (a0,a1,t0,r1)", "W1* data",
            "h1(A)", "h1(A*)"]
    cov = T.rs_cover(1)
    rels, mu, lam = cov["rels"], cov["mu"], cov["lam"]
    pts = [("q^2-34q+1", Q2 := T.Q ** 2 - 34 * T.Q + 1, 2, 1, "-1", ("17-12sqrt2", "17+12sqrt2")),
           ("q^2-14q+1", T.Q ** 2 - 14 * T.Q + 1, 4, 1, "i", ("7-4sqrt3", "7+4sqrt3")),
           ("q^2-14q+1", T.Q ** 2 - 14 * T.Q + 1, 4, 3, "-i", ("7-4sqrt3", "7+4sqrt3"))]
    rows = []
    for gl, g, Nl, lk, mul, labels in pts:
        F = T.Field("ext", g=g)
        rep = T.DMRep(cov["gens"], T.twisted_rep(cov, F, (0, 0), 1, lk, Nl))
        assert rep.check(rels)
        ex = index_rows(rep, rels, mu, lam, "exact")
        agree_exact = all(ex.get(k) == banked[(lab, mul)][k] for lab in labels for k in keys)
        modp = []
        for p in PRIMES:
            iota = T.gf_root_of_unity(p, 4)
            for r in T.gf_roots(g, p):
                Fp = T.Field("gf", p=p, r=r, iota=iota)
                repp = T.DMRep(cov["gens"], T.twisted_rep(cov, Fp, (0, 0), 1, lk, Nl))
                assert repp.check(rels)
                rp = index_rows(repp, rels, mu, lam, "gf", p)
                modp.append({"p": p, "q mod p": r, "agrees_with_exact": all(rp.get(k) == ex.get(k) for k in keys)})
        rows.append({"g": gl, "mu": mul, "exact": ex, "exact_equals_B1509_at_both_roots": agree_exact, "mod_p": modp})
    return rows


def c6():
    cov = T.rs_cover(3)
    rels, mu, lam = cov["rels"], cov["mu"], cov["lam"]
    out = []
    for gl, g, expect_h1, expect_I in (("q^2-34q+1", T.Q ** 2 - 34 * T.Q + 1, 1, -1), ("q^2-7q+1", T.Q ** 2 - 7 * T.Q + 1, 2, 0)):
        F = T.Field("ext", g=g)
        rep = T.DMRep(cov["gens"], T.twisted_rep(cov, F, (0, 0), 1, 1, 2))      # nu_F = 1, lam = -1 (zeta_2)
        assert rep.check(rels)
        cls, h1 = T.h1_classes(rep, rels)
        trials = [("c1", cls[0])] + ([("c2", cls[1]), ("c1+c2", cls[0] + cls[1])] if len(cls) > 1 else [])
        counts = {}
        for name, c in trials:
            W = T.extension_rep(rep, c)
            assert W.check(rels)
            counts[name] = T.index(W, rels, mu, lam)["I"]
        modp = []
        for p in PRIMES:
            iota = T.gf_root_of_unity(p, 4)
            for r in T.gf_roots(g, p):
                Fp = T.Field("gf", p=p, r=r, iota=iota)
                repp = T.DMRep(cov["gens"], T.twisted_rep(cov, Fp, (0, 0), 1, 1, 2))
                clsp, h1p = T.h1_classes(repp, rels)
                cp = {}
                for k, c in enumerate(clsp):
                    cp[f"c{k + 1}"] = T.index_gf(T.extension_rep(repp, c), rels, mu, lam, p)["I"]
                if len(clsp) > 1:
                    cp["c1+c2"] = T.index_gf(T.extension_rep(repp, clsp[0] + clsp[1]), rels, mu, lam, p)["I"]
                modp.append({"p": p, "q mod p": r, "h1": h1p, "counts": cp})
        out.append({"g": gl, "lam": "-1", "h1": h1, "counts": counts, "expected_h1": expect_h1, "expected_count": expect_I,
                    "as_expected": h1 == expect_h1 and all(v == expect_I for v in counts.values())
                    and all(m["h1"] == expect_h1 and all(v == expect_I for v in m["counts"].values()) for m in modp),
                    "mod_p": modp})
    return out


def c7_c8():
    """C7: the closed form of the one-step matrix equals the Fox computation for symbolic character values X, Y.
    C8: the GF(p) interpolation reproduces the exact untwisted polynomials q^(16n) prod_j (lam - r_j^n) at levels 1-6, two primes."""
    X, Y = sp.symbols("X Y")
    mats = T.symbolic_mats()
    Rx, Ry, M = T.word_matrix(mats, T.FIBRE["x"]), T.word_matrix(mats, T.FIBRE["y"]), mats["m"].inv()
    g = {"x": X * Rx, "y": Y * Ry}

    def coc(word, z):
        val, pre = sp.zeros(4, 1), sp.eye(4)
        for ch in word:
            if ch.islower():
                val += pre * z[ch]
                pre = pre * g[ch]
            else:
                gi = g[ch.lower()].inv()
                val -= pre * gi * z[ch.lower()]
                pre = pre * gi
        return val
    cols = []
    for j in range(8):
        e = [sp.zeros(4, 1), sp.zeros(4, 1)]
        e[j // 4][j % 4] = 1
        z = {"x": e[0], "y": e[1]}
        cols.append((M * coc(T.PHI["x"], z)).col_join(M * coc(T.PHI["y"], z)))
    A1, A2, A3 = T.block_mats()
    Sc = sp.Matrix(sp.BlockMatrix([[sp.zeros(4), A1], [-(Y / X) * A2, A1 + (Y / X) * A2 + (Y ** 2 / X) * A3]]))
    c7 = (sp.Matrix.hstack(*cols) - Sc).applyfunc(sp.cancel) == sp.zeros(8)
    # Laurent ranges of the blocks
    def rng(A):
        lo, hi = 10 ** 9, -10 ** 9
        for e_ in A:
            e_ = sp.cancel(e_)
            if e_ == 0:
                continue
            num, den = sp.fraction(e_)
            dd = sp.Poly(den, T.Q)
            assert len(dd.terms()) == 1
            degs = [m_[0] for m_, c_ in sp.Poly(num, T.Q).terms()]
            lo, hi = min(lo, min(degs) - dd.degree()), max(hi, max(degs) - dd.degree())
        return [lo, hi]
    ranges = {"A1": rng(A1), "A2": rng(A2), "A3": rng(A3)}
    x = sp.Symbol("x")
    ok_all = True
    for n in range(1, 7):
        R = sp.resultant(T.Q_MONIC.subs(T.S_, x), T.S_ - x ** n, x)
        R = sp.expand(R / sp.Poly(R, T.S_).LC())
        for p in (1009, 1129):
            mp = T.ModP(p, 1)
            polys = T.f_polys_modp(mp, (0, 0), n, (0, 1, 2, 3))
            for l in range(4):
                ex = sp.expand(sp.cancel(R.subs(T.S_, sp.I ** l) * T.Q ** (16 * n)))
                P = sp.Poly(ex, T.Q, sp.I) if ex.has(sp.I) else sp.Poly(ex, T.Q)
                co = {}
                for mon, c in P.terms():
                    c = sp.Rational(c)
                    v = int(c.p) * pow(int(c.q), p - 2, p) % p
                    if len(mon) > 1 and mon[1]:
                        v = v * pow(mp.iota, mon[1], p) % p
                    co[mon[0]] = (co.get(mon[0], 0) + v) % p
                deg = max([e_ for e_, v in co.items() if v] + [0])
                exv = [co.get(e_, 0) for e_ in range(deg + 1)]
                while len(exv) > 1 and exv[-1] == 0:
                    exv.pop()
                ok_all = ok_all and exv == polys[l]
    return {"C7_closed_form_equals_Fox_for_symbolic_characters": c7, "C7_laurent_ranges_of_the_blocks": ranges,
            "C7_ranges_within_LAURENT_STEP": all(T.LAURENT_STEP[0] <= r[0] and r[1] <= T.LAURENT_STEP[1] for r in ranges.values()),
            "C8_interpolation_reproduces_untwisted_levels_1_6_two_primes": ok_all}


def c9_dry_run():
    """the census code on instances decided at design time (Theorem D, B1509): Part A and Part B on the trivial orbit of T_3,
    the gcd machinery on untwisted polynomials (a genuine common factor found, a coprime pair found coprime), and the case-(b)
    counter on M_1 (where L = 1 and eta = nu, so it must return B1509's -1 / +1)"""
    import tower_census as TC
    import flint
    logs = []
    log = lambda m: logs.append(m)
    a = TC.part_a(log, orbs=[[(0, 0)]])
    b = TC.part_b(a, log)
    summary_a = []
    for pt in a["points"]:
        w1 = sorted({v["I"] for r in pt["mod_p"] for m in r["counts"].values() for v in m["W1"].values()})
        w2 = sorted({v["I"] for r in pt["mod_p"] for m in r["counts"].values() for v in m["W2"].values()})
        ex1 = sorted({v["I"] for m in pt.get("exact_counts", {}).values() for v in m["W1"].values()})
        summary_a.append({"lam": pt["lam"], "g0": pt["g0"], "fibre": pt["fibre"], "W1_mod_p": w1, "W2_mod_p": w2, "W1_exact": ex1,
                          "h1": sorted({m["h1"] for r in pt["mod_p"] for m in r["counts"].values()})})
    theorem_d = all((s_["W1_mod_p"] == [-1] and s_["W2_mod_p"] == [1]) if (s_["g0"] == "q**2 - 34*q + 1" and s_["lam"] == "-1")
                    else (s_["W1_mod_p"] in ([0], []) and s_["W2_mod_p"] in ([0], [])) for s_ in summary_a)
    summary_b = [{"lam3": r["lam3"], "g0": r["g0"], "shapiro_h1": r["shapiro_h1_M6 = h1(lam3) + h1(-lam3)"],
                  "h1_M6": sorted({x["h1_M6"] for x in r["rows"]}), "W1_M6": sorted({v for x in r["rows"] for v in x["W1"].values()})}
                 for r in b]
    # gcd machinery: level 2 lam = 1 against level 4 lam = 1 (common q^2 - 34 q + 1), level 2 lam = 1 against level 2 lam = -1 (coprime)
    p = 1129
    mp = T.ModP(p, 1)
    f2 = T.f_polys_modp(mp, (0, 0), 2, (0, 2))
    f4 = T.f_polys_modp(mp, (0, 0), 4, (0,))
    g_common = flint.nmod_poly(f2[0], p).gcd(flint.nmod_poly(f4[0], p))
    g_coprime = flint.nmod_poly(f2[0], p).gcd(flint.nmod_poly(f2[2], p))
    rc, mq, m1 = TC.strip(g_common, p)
    rn, mqn, m1n = TC.strip(g_coprime, p)
    # case-(b) counter on M_1 at q^2 - 34 q + 1, nu = (1, -1): L = nu^-4 = 1, eta = nu
    cov1 = T.rs_cover(1)
    g0 = T.Q ** 2 - 34 * T.Q + 1
    K = T.Field("ext", g=g0, base="Q12")
    cb_exact = TC.counts_case_b(cov1, K, T.rs_rho(cov1, K), (0, 0), 1, 2, 4, "exact")
    cb_modp = []
    for pp in (1009, 1129):
        iota = T.gf_root_of_unity(pp, 4)
        for r in T.gf_roots(g0, pp):
            Fp = T.Field("gf", p=pp, r=r, iota=iota)
            cb_modp.append(TC.counts_case_b(cov1, Fp, T.rs_rho(cov1, Fp), (0, 0), 1, 2, 4, "gf", pp))
    cb_ok = all(c["W1"]["c1"]["I"] == -1 and c["W2"]["c1"]["I"] == 1 and c["h1(L)"] == 1 for c in [cb_exact] + cb_modp)
    # Part C1's exact path over Q(zeta12)(q), on the trivial character at level 4: the untwisted level-4 polynomial, f(+-1) rational
    F12 = T.Field("sym", base="Q12")
    bl = [F12.mat(A) for A in T.block_mats()]
    P4 = sp.expand(T.charpoly_on_H1(TC.fibre_P(F12, bl, (0, 0), 3, 4)))
    x = sp.Symbol("x")
    R4 = sp.resultant(T.Q_MONIC.subs(T.S_, x), T.S_ - x ** 4, x)
    R4 = sp.expand(R4 / sp.Poly(R4, T.S_).LC())
    c1_path = {"P_equals_untwisted_level4": sp.simplify(P4 - R4) == 0}
    for lam in (1, -1):
        f = sp.nsimplify(sp.expand(TC.numerator_in_q(P4.subs(T.S_, lam))))
        c1_path[f"f({lam})_rational"] = all(sp.sympify(c).is_rational for c in sp.Poly(f, T.Q).all_coeffs())
        c1_path[f"f({lam})"] = str(sp.factor(f))
    # the identically-exceptional handler, run on the trivial orbit at lam = 1 (not identically exceptional: h1 = 0 at q = 2, 3, 1/2)
    ie = TC.identically_exceptional_point([(0, 0)], 4, 0, T.rs_cover(3), log)
    ie_ok = ie["generic_ker_dims"] == [0, 0, 0, 0] and all(r["(0, 0)"]["h1"] == 0 for r in ie["rational_points"].values())
    return {"A_on_trivial_orbit": summary_a, "A_theorem_D_reproduced": theorem_d,
            "A_trivial_polynomial": a["orbits"][0]["P(q,s)"], "A_trivial_symmetries": a["orbits"][0]["symmetries"],
            "B_on_trivial_orbit": summary_b,
            "B_shapiro_holds": all(x["h1_M6"] == [x["shapiro_h1"]] for x in summary_b),
            "gcd_common_factor_found": {"deg_gcd": g_common.degree(), "mult_q": mq, "mult_q-1": m1, "deg_rest": rc.degree(),
                                        "rest": str(rc)},
            "gcd_coprime_pair": {"deg_gcd": g_coprime.degree(), "deg_rest": rn.degree()},
            "case_b_counter_on_M1": {"exact": cb_exact, "ok": cb_ok},
            "C1_exact_path_on_the_trivial_character_level4": c1_path,
            "identically_exceptional_handler_on_the_trivial_orbit_ok": ie_ok}


def c10_classification():
    """the case-(b) classification by character arithmetic alone (no polynomial): on levels 2, 4, 5, 6, every orbit with
    nu_F^4 != 1, whether nu^5 lies in the orbit (self-coincident) and whether the orbit is closed under inversion"""
    import tower_census as TC
    out = {}
    for n in TC.LEVELS_B:
        chars, N, orbs, idx, pairs = TC.classify_pairs(n)
        rows = {}
        for pr in pairs:
            k = pr["orbit_index"]
            if k in rows:
                continue
            rows[k] = {"rep": pr["orbit_rep"], "size": pr["orbit_size"], "order": pr["order"],
                       "self_coincident(nu^5 in orbit)": pr["orbit5_index"] == k, "closed_under_inversion": pr["orbit_inv_index"] == k}
        kinds = {}
        for pr in pairs:
            kinds[pr["kind"]] = kinds.get(pr["kind"], 0) + 1
        sc = [r for r in rows.values() if r["self_coincident(nu^5 in orbit)"]]
        out[n] = {"orbits_with_nu^4_not_1": len(rows), "pairs_by_kind": kinds,
                  "self_coincident_orbits": [{"rep": r["rep"], "size": r["size"], "order": r["order"],
                                              "closed_under_inversion": r["closed_under_inversion"]} for r in sc],
                  "exact_pairs": [(pr["orbit_rep"], ["1", "i", "-1", "-i"][pr["lam"]]) for pr in pairs if pr["kind"] == "exact"]}
    return out


def main():
    t0 = time.time()
    res = {"C1_C2": c1_c2()}
    res["C3"] = c3()
    res["C4"] = c4()
    res["C5"] = c5()
    res["C6"] = c6()
    res["C7_C8"] = c7_c8()
    res["C9_dry_run"] = c9_dry_run()
    res["C10_case_b_classification"] = c10_classification()
    res["seconds"] = round(time.time() - t0)
    return res


if __name__ == "__main__":
    out = main()
    txt = json.dumps(out, indent=1, sort_keys=True, default=str)
    print(txt)
    if "--record" in sys.argv:
        (HERE / "controls_run.txt").write_text(txt + "\n", encoding="utf-8")
