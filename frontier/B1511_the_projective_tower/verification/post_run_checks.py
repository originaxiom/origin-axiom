"""B1511 post-run checks (written and run after tower_census_run.txt; not predictions, not sealed). Record: post_run_checks_run.txt.

(a) The order-2 orbit's polynomial is B1509's Q at q^3: P_{O2}(q, s) = Q_monic(q^3, s), read from the record and checked symbolically.
(b) The Part-C2 pairs that are not self-coincident and were reported UNRESOLVED (all at lam = 1): the common factor left after q and
    q - 1, recomputed over GF(p) at the run's three primes, is q^2 + q + 1 (roots the primitive cube roots of unity, no positive
    root).  Reported per pair.
(c) The structural reason Theorem F's last bullet fails: P_nu(q, s) = P_{nu^-1}(q, s) coefficientwise over GF(p), for every character
    of T_n at levels 2-6 (one prime per level), so every twisted polynomial is real.  The self-coincident UNRESOLVED pairs of Part C2
    (M5's eigenline orbits, M6's order-8 orbits) are exactly those where the reality argument of Theorem F was used; their gcd being
    the whole polynomial is this reality.  No root of theirs and no count is computed here (that is the next arc's sealed question).
(d) The order-2 triplet's three members agree at every prime-root pair and exactly (read from the record), and the M6 rows agree with
    Shapiro (D6)."""
import json
import sys
from pathlib import Path

import flint
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import tower_lib as T  # noqa: E402
import tower_census as TC  # noqa: E402

q, s = T.Q, T.S_


def check_a(rec):
    O2 = [o for o in rec["A"]["orbits"] if o["orders"] == [2]][0]
    P = sp.sympify(O2["P(q,s)"], locals={"q": q, "s": s})
    target = T.Q_MONIC.subs(q, q ** 3)
    return {"orbit": O2["orbit"], "P_O2(q,s) = Q_monic(q^3, s)": sp.simplify(sp.expand(P - target)) == 0,
            "Q_monic(q^3, s)": str(sp.expand(target))}


def check_b(rec):
    out = {}
    for n_str, res in rec["C2"].items():
        n = int(n_str)
        un = [p for p in res["pairs"] if not p["no_common_root_other_than_0_1"] and p["orbit5_index"] != p["orbit_index"]]
        if not un:
            out[n] = {"pairs": 0}
            continue
        chars, N, orbs, idx, pairs = TC.classify_pairs(n)
        rows = []
        all_cyclo = True
        for p in res["primes"]:
            mp = T.ModP(p, N)
            cache = {}
            phi3 = flint.nmod_poly([1, 1, 1], p)
            for pr in un:
                k, l = pr["orbit_index"], pr["lam"]
                for kk, ll in [(k, l)] + [tuple(x) for x in pr["partners"]]:
                    if (kk, ll) not in cache:
                        cache[(kk, ll)] = flint.nmod_poly(T.f_polys_modp(mp, orbs[kk][0], n, (ll,))[ll], p)
                g = cache[(k, l)]
                for kk, ll in pr["partners"]:
                    g = g.gcd(cache[(kk, ll)])
                rest, mq, m1 = TC.strip(g, p)
                is_phi3 = rest.degree() == 2 and rest == phi3 * flint.nmod_poly([rest.coeffs()[-1]], p)
                all_cyclo = all_cyclo and is_phi3
                rows.append({"p": p, "orbit_rep": pr["orbit_rep"], "lam": pr["lam"], "rest": str(rest), "is_q^2+q+1": is_phi3})
        out[n] = {"pairs": len(un), "every_rest_is_q^2+q+1_at_every_prime": all_cyclo, "rows": rows}
    return out


def check_c():
    out = {}
    for n in (2, 3, 4, 5, 6):
        chars, N = T.characters(n)
        mod = (N * 4) // __import__("math").gcd(N, 4)
        p = TC.primes_for(mod, 1)[0]
        mp = T.ModP(p, N)
        pts = list(range(1, 32 * n + 2))
        pairs = [(ab, ((-ab[0]) % N, (-ab[1]) % N)) for ab in chars if ((-ab[0]) % N, (-ab[1]) % N) > ab]
        bad = set()
        for r in pts:                      # all 32n + 1 interpolation points: an identity of the scaled coefficient polynomials
            B = mp.blocks_at(r)
            for ab, inv in pairs:
                if (ab, inv) in bad:
                    continue
                if mp.charpoly_H1(mp.level(B, ab, n)) != mp.charpoly_H1(mp.level(B, inv, n)):
                    bad.add((ab, inv))
        out[n] = {"prime": p, "pairs_nu_nu^-1": len(pairs), "pairs_differing": len(bad),
                  "P_nu = P_nu^-1 identically over GF(p)": not bad}
    return out


def check_d(rec):
    pts = [pt for pt in rec["A"]["points"] if pt["orbit"] == [[0, 2], [2, 2], [2, 0]] and pt["lam"] == "-1"]
    pt = pts[0]
    exact = {m: (c["W1"]["c1"]["I"], c["W2"]["c1"]["I"], c["W1"]["c1"]["I_L2"], c["W1"]["c1"]["data(a0,a1,t0,r1)"])
             for m, c in pt["exact_counts"].items()}
    modp = sorted({(m, c["W1"]["c1"]["I"], c["W2"]["c1"]["I"], c["W1"]["c1"]["I_L2"]) for r in pt["mod_p"] for m, c in r["counts"].items()})
    shapiro = []
    for row in rec["B"]:
        s961 = [p for p in rec["A"]["points"] if p["orbit"] == row["orbit"] and p["lam"] == row["lam3"]][0]
        s_vals = sorted({v["I"] for r in s961["mod_p"] for v in list(r["counts"].values())[0]["W1"].values()})
        m6_vals = sorted({v for x in row["rows"] for v in x["W1"].values()})
        shapiro.append({"orbit": row["orbit"], "lam3": row["lam3"], "h1_M6": sorted({x["h1_M6"] for x in row["rows"]}),
                        "shapiro_h1": row["shapiro_h1_M6 = h1(lam3) + h1(-lam3)"], "W1_s961": s_vals, "W1_M6": m6_vals})
    return {"triplet_point": pt["g0"], "positive_roots": pt["positive_roots"], "fibre": pt["fibre"], "exact": exact,
            "mod_p_rows": len(pt["mod_p"]), "mod_p_values": modp,
            "D6_shapiro": shapiro,
            "D6_all_agree": all(x["h1_M6"] == [x["shapiro_h1"]] and x["W1_M6"] == x["W1_s961"] for x in shapiro)}


def main():
    rec = json.loads((HERE / "tower_census_run.txt").read_text(encoding="utf-8"))
    return {"a_O2_is_Q_at_q_cubed": check_a(rec), "b_C2_lam1_common_factor": check_b(rec),
            "c_P_nu_equals_P_nu_inverse": check_c(), "d_triplet_and_shapiro": check_d(rec)}


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt[:3000])
    if "--record" in sys.argv:
        (HERE / "post_run_checks_run.txt").write_text(txt + "\n", encoding="utf-8")
