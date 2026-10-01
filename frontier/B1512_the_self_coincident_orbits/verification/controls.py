"""B1512 controls, run before the seal (record: controls_run.txt).  No control computes a twisted polynomial, a root or a count of any
of the twelve self-coincident orbits of M5 and M6 (the sealed question); every control is a lemma check or a reproduction of a
banked number.

K1  the involution: iota is an involutive automorphism of pi (iota^2 = id on the generators, iota(R) a cyclic conjugate of R^-1),
    iota(x) = x^-1, iota(y) = y^-1, iota(m) = y m, iota(longitude) a cyclic conjugate of the longitude^(+-1); the intertwiner
    C(q) with C rho_q(g) C^-1 = rho_q(iota g) exists, is unique up to scale, has det 16 q^2, and C^2 = 4q.
K2  nu o iota = (nu_F^-1, lam) for every character of T_n, n = 1 ... 6.
K3  the case-(b) classification: the self-coincident orbits of levels 4-6 (B1511 C10), their Galois classes (closed under nu -> nu^k
    and nu -> nu^-1 within the deck orbit and its inverse), and the 32 pairs of B1511's record, matched one for one.
K4  the reconstruction reproduces banked polynomials exactly: the untwisted levels 1-6 against Res_r(Q(q, r), s - r^n); s961's
    O2 (= Q(q^3, s)), O_A and O_B (B1511 Part A); M4's two 3-torsion classes (B1511 Part C1).
K5  the root-and-count driver on B1511's banked case-(b) point (M4, both 3-torsion orbits, lam = 1, q^2 - 7q + 1): every member,
    every root, three primes: I(W1) = +1, I(W2) = -1, I(L2 W1) = 0, data (0, 1, 1, 0), fibre (1, 1, 1, 1), rank B = 4.
K6  the numeric fibre data at the real root itself (60 digits): (1, 1, 1, 1) at M4's point for three members, and B1509's Jordan
    block (1, 2, 2, 2) at q^2 - 34 q + 1, lam = -1, level one.
K7  B1511's banked degrees for the 32 pairs (the record's GF(p) gcd rows), read back as the targets the sealed run must reproduce.
K8  duality and amphichirality: the exact intertwiners D (rho_q^-T -> rho_(1/q)) and E (rho_q -> rho_(1/q) o eps), each unique up to
    scale, det D = -16 q (q^2 + q + 1), det E = 16 q^4; eps an involutive automorphism (x <-> y, m -> x^-1 m^-1, longitude to a
    conjugate of its inverse).  Lemma D's consequence P(1/q, s) = s^4 P(q, 1/s) / P(q, 0) on every banked polynomial: the untwisted
    levels 1-6, s961's O2, O_A, O_B, M4's two 3-torsion classes.
K9  Lemma E's consequence on characters: P_(b,a) = P_(a,b) over GF(p) at all 32 n + 1 interpolation points, for every character of
    T_n, n = 2, 3, 4 (one prime per level; levels 5 and 6 are the sealed ones and are not touched); and the swap's action on the
    classes of M5 and M6 (character arithmetic only).
K10 amphichirality: alpha (fibre action [[2, 1], [-1, -1]], a square root of Phi^-1 of det -1; alpha(m) = y m) is an automorphism of
    pi reversing orientation, with an exact intertwiner A (rho_q -> rho_(1/q) o alpha, det -16 q^3); the table of the four
    symmetries (iota, eps, alpha, the audit lane's theta) with theta = iota phi^-2 eps on H_1(F); Lemma A's consequence
    P_(nu o alpha)(q, s) = P_nu(1/q, s) on the banked polynomials (s961: O_A -> conjugate O_B, O2 -> O2; M4: class 1 -> class 10);
    the class maps under alpha on M5 and M6 (character arithmetic only)."""
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import selfco_lib as L  # noqa: E402

q, s = L.q, L.s
REC1511 = L.B1511 / "tower_census_run.txt"


def k1():
    return L.involution_checks()


def k2():
    return [L.iota_on_characters(n) for n in range(1, 7)]


def k3():
    rec = json.loads(REC1511.read_text(encoding="utf-8"))
    out = {}
    for n in (4, 5, 6):
        N, orbs, idx, sc = L.self_coincident_orbits(n)
        rows = []
        for k, o in sc:
            gc = L.galois_class(o[0], N)
            rows.append({"orbit_index": k, "orbit": o, "order": L.T.order_of(o[0], N),
                         "Galois-closed within orbit and inverse orbit": L.galois_closure_in_orbit_union(o[0], N),
                         "class (orbit indices)": sorted({idx[c] for c in gc}),
                         "inverse orbit": idx[((-o[0][0]) % N, (-o[0][1]) % N)]})
        classes = sorted({tuple(r["class (orbit indices)"]) for r in rows})
        out[f"level_{n}"] = {"N": N, "self_coincident": rows, "classes": [list(c) for c in classes]}
    # B1511's 32 self-coincident UNRESOLVED pairs, matched
    banked = []
    for n_str in ("5", "6"):
        for pr in rec["C2"][n_str]["pairs"]:
            if not pr["no_common_root_other_than_0_1"] and pr["orbit5_index"] == pr["orbit_index"]:
                banked.append((int(n_str), pr["orbit_index"], pr["lam"]))
    mine = []
    for n in (5, 6):
        for r in out[f"level_{n}"]["self_coincident"]:
            for l in ((0, 1, 2, 3) if n == 5 else (0, 2)):
                mine.append((n, r["orbit_index"], l))
    out["the 32 pairs"] = {"banked": len(banked), "here": len(mine), "match": sorted(banked) == sorted(mine)}
    return out


def k4():
    rec = json.loads(REC1511.read_text(encoding="utf-8"))
    out = {"untwisted": [], "s961": [], "M4": []}
    r = sp.Symbol("r")
    for n in range(1, 7):
        chars, N = L.T.characters(n)
        t = time.time()
        P, rr = L.reconstruct_P((0, 0), n, N)
        ex = sp.expand(sp.resultant(sp.numer(sp.together(L.T.Q_MONIC.subs(s, r))), s - r ** n, r))
        ex = sp.expand(sp.cancel(ex / sp.Poly(ex, s).LC()))
        out["untwisted"].append({"level": n, "N": N, "primes": rr["primes_used"], "fresh_agree": rr["all_fresh_agree"],
                                 "equals Res(Q, s - r^n)": sp.simplify(P - ex) == 0, "seconds": round(time.time() - t, 1)})
    banked = {str(o["orbit"]): sp.sympify(o["P(q,s)"], locals={"q": q, "s": s}) for o in rec["A"]["orbits"]}
    for ab, key in [((0, 2), "[[0, 2], [2, 2], [2, 0]]"), ((0, 1), "[[0, 1], [1, 3], [3, 0]]"), ((1, 1), "[[1, 1], [1, 2], [2, 1]]")]:
        P, rr = L.reconstruct_P(ab, 3, 4)
        out["s961"].append({"orbit_rep": ab, "primes": rr["primes_used"], "fresh_agree": rr["all_fresh_agree"],
                            "equals B1511 Part A": sp.simplify(P - banked[key]) == 0,
                            "O2: equals Q(q^3, s)": (sp.simplify(P - L.T.Q_MONIC.subs(q, q ** 3)) == 0) if ab == (0, 2) else None})
    for row in rec["C1"]["4"]:
        if row["lam"] != "1":
            continue
        ab = tuple(row["orbit"][0])
        Pb = sp.sympify(row["P(q,s)"], locals={"q": q, "s": s})
        P, rr = L.reconstruct_P(ab, 4, 15)
        out["M4"].append({"orbit_rep": ab, "primes": rr["primes_used"], "fresh_agree": rr["all_fresh_agree"],
                          "equals B1511 Part C1": sp.simplify(P - Pb) == 0})
    return out


def k5():
    n, N = 4, 15
    cc = L.CoverCache(n)
    orbs = L.T.orbits(*L.T.characters(n))
    out = []
    for ab in [(0, 5), (5, 5)]:
        P, _ = L.reconstruct_P(ab, n, N)
        G, info = L.specialisation(P, 0)
        rep = L.positive_roots_report(G)
        o = [c for c in orbs if ab in c][0]
        for fr in rep:
            if not fr["positive_roots_not_1"]:
                continue
            vals = set()
            pts = 0
            for p, roots in L.primes_with_roots(sp.sympify(fr["factor"]), 60, 3):
                for r_ in roots:
                    rows = L.counts_at(cc, p, r_, o, N, (0,))
                    for v in rows.values():
                        c = v["counts"]
                        vals.add((c["W1"]["c1"]["I"], c["W2"]["c1"]["I"], c["W1"]["c1"]["I_L2"], tuple(c["W1"]["c1"]["data(a0,a1,t0,r1)"]),
                                  tuple(v["fibre"]["ker_dims"]), v["fibre"]["rank_B"]))
                    pts += 1
            out.append({"orbit": o, "factor": fr["factor"], "positive_roots": fr["positive_roots_not_1"], "prime_root_pairs": pts,
                        "values (I(W1), I(W2), I(L2 W1), data, fibre, rank B)": sorted(vals),
                        "B1511's row reproduced": vals == {(1, -1, 0, (0, 1, 1, 0), (1, 1, 1, 1), 4)}})
    return out


def k6():
    out = []
    for alpha in sp.real_roots(sp.Poly(q ** 2 - 7 * q + 1, q)):
        for ab in [(0, 5), (5, 0), (5, 5)]:
            d = L.fibre_data_numeric(ab, 15, 4, alpha, 0)
            out.append({"q": str(sp.N(alpha, 12)), "nu": ab, "lam": "1", **d, "expected (1,1,1,1)": d["ker_dims"] == [1, 1, 1, 1]})
    for alpha in sp.real_roots(sp.Poly(q ** 2 - 34 * q + 1, q)):
        d = L.fibre_data_numeric((0, 0), 1, 1, alpha, 2)
        out.append({"q": str(sp.N(alpha, 12)), "nu": (0, 0), "lam": "-1", **d, "expected (1,2,2,2)": d["ker_dims"] == [1, 2, 2, 2]})
    return out


def k7():
    rec = json.loads(REC1511.read_text(encoding="utf-8"))
    out = {}
    for n_str in ("5", "6"):
        rows = []
        for pr in rec["C2"][n_str]["pairs"]:
            if not pr["no_common_root_other_than_0_1"] and pr["orbit5_index"] == pr["orbit_index"]:
                degs = {(x["deg_f"], x["mult_q"], x["mult_q-1"], x["deg_gcd_without_q_and_q-1"]) for x in pr["per_prime"]}
                rows.append({"orbit_index": pr["orbit_index"], "orbit_rep": pr["orbit_rep"], "lam": pr["lam"],
                             "(deg f, mult q, mult q-1, rest) at the three primes": sorted(degs)})
        # the lam = +-i rows of M6 were resolved (no common root): recorded as the non-palindromic evidence
        res_i = [(pr["orbit_index"], pr["lam"]) for pr in rec["C2"][n_str]["pairs"]
                 if pr["orbit5_index"] == pr["orbit_index"] and pr["lam"] in (1, 3) and pr["no_common_root_other_than_0_1"]]
        out[n_str] = {"unresolved_self_coincident": rows, "resolved self-coincident pairs at lam = +-i": res_i}
    return out


def k8():
    out = {"lemmas": L.duality_checks(), "identity on banked polynomials": []}
    rec = json.loads(REC1511.read_text(encoding="utf-8"))
    r = sp.Symbol("r")
    for n in range(1, 7):
        ex = sp.expand(sp.resultant(sp.numer(sp.together(L.T.Q_MONIC.subs(s, r))), s - r ** n, r))
        ex = sp.expand(sp.cancel(ex / sp.Poly(ex, s).LC()))
        out["identity on banked polynomials"].append({"what": f"untwisted level {n}", "P(1/q,s) = rec P(q,s)": L.reciprocal_in_q_identity(ex)})
    for o in rec["A"]["orbits"]:
        P = sp.sympify(o["P(q,s)"], locals={"q": q, "s": s})
        out["identity on banked polynomials"].append({"what": f"s961 orbit {o['orbit']}", "P(1/q,s) = rec P(q,s)": L.reciprocal_in_q_identity(P)})
    for row in rec["C1"]["4"]:
        if row["lam"] != "1":
            continue
        P = sp.sympify(row["P(q,s)"], locals={"q": q, "s": s})
        out["identity on banked polynomials"].append({"what": f"M4 orbit {row['orbit'][0]}", "P(1/q,s) = rec P(q,s)": L.reciprocal_in_q_identity(P)})
    out["all hold"] = all(x["P(1/q,s) = rec P(q,s)"] for x in out["identity on banked polynomials"])
    return out


def k9():
    out = {"levels 2-4": [], "class map under the swap": {}}
    for n in (2, 3, 4):
        chars, N = L.T.characters(n)
        cs = set(chars)
        mod = N * 4 // __import__("math").gcd(N, 4)
        p = L.next_prime_1_mod(mod, 10 ** 6)
        mp = L.T.ModP(p, N)
        pairs = [(ab, (ab[1], ab[0])) for ab in chars if (ab[1], ab[0]) > ab]
        swap_is_char = all((ab[1], ab[0]) in cs for ab in chars)
        bad = set()
        for r_ in range(1, 32 * n + 2):
            B = mp.blocks_at(r_)
            for ab, ba in pairs:
                if (ab, ba) in bad:
                    continue
                if mp.charpoly_H1(mp.level(B, ab, n)) != mp.charpoly_H1(mp.level(B, ba, n)):
                    bad.add((ab, ba))
        out["levels 2-4"].append({"level": n, "prime": p, "swap maps characters to characters": swap_is_char, "pairs": len(pairs),
                                  "pairs differing": len(bad)})
    for n in (5, 6):
        N, orbs, idx, sc = L.self_coincident_orbits(n)
        m = {}
        for k, o in sc:
            ab = o[0]
            m[k] = idx[(ab[1], ab[0])]
        out["class map under the swap"][f"level_{n}"] = m
    return out


def k10():
    out = {"lemma": L.amphichiral_checks(), "symmetries": L.symmetry_table(), "on banked polynomials": [], "class map under alpha": {}}
    rec = json.loads(REC1511.read_text(encoding="utf-8"))
    Ps = {tuple(map(tuple, o["orbit"])): sp.sympify(o["P(q,s)"], locals={"q": q, "s": s}) for o in rec["A"]["orbits"]}
    chars, N, orbs, idx = L.TC.orbit_table(3)
    for key, P in Ps.items():
        img = L.alpha_on_character(key[0], N)
        tgt = [k for k in Ps if img in k][0]
        out["on banked polynomials"].append({"s961 orbit": [list(c) for c in key], "alpha image orbit": [list(c) for c in tgt],
                                             "P_image(q, s) = P(1/q, s)": sp.simplify(sp.expand(Ps[tgt] - P.subs(q, 1 / q))) == 0})
    rows = {tuple(r["orbit"][0]): sp.sympify(r["P(q,s)"], locals={"q": q, "s": s}) for r in rec["C1"]["4"] if r["lam"] == "1"}
    P1, P10 = rows[(0, 5)], rows[(5, 5)]
    out["on banked polynomials"].append({"M4": "class 1 -> class 10", "P_10(q, s) = P_1(1/q, s)": sp.simplify(sp.expand(P10 - P1.subs(q, 1 / q))) == 0})
    out["all hold"] = all(v for x in out["on banked polynomials"] for k, v in x.items() if isinstance(v, bool))
    for n in (5, 6):
        N, orbs, idx, sc = L.self_coincident_orbits(n)
        out["class map under alpha"][f"level_{n}"] = {k: idx[L.alpha_on_character(o[0], N)] for k, o in sc}
    return out


def main():
    t0 = time.time()
    res = {}
    for name, fn in [("K1", k1), ("K2", k2), ("K3", k3), ("K4", k4), ("K5", k5), ("K6", k6), ("K7", k7), ("K8", k8), ("K9", k9), ("K10", k10)]:
        t = time.time()
        res[name] = fn()
        print(f"{name} done in {time.time() - t:.1f}s", flush=True)
    res["seconds"] = round(time.time() - t0, 1)
    return res


if __name__ == "__main__":
    out = main()
    txt = json.dumps(out, indent=1, sort_keys=True, default=str)
    if "--record" in sys.argv:
        (HERE / "controls_run.txt").write_text(txt + "\n", encoding="utf-8")
    print(txt[:4000])
