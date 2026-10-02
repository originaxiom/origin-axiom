"""B1514 -- post-run check (e): case (a) through level 6, computed directly (not a prediction; run after both sealed routes).
Record: case_a_levels_run.txt.

Why.  The sealed text (PREREGISTRATION Section 0) lists case (a), B1509's 10' through a Jordan block, as "the pullback (one per
level) and the projective triplet. B1513 read it."  B1513 computed the join on m004 (level 1) and the triplet on s961 (level 3).
P7 reads the law through level 6, so the remaining levels are computed here, by both routes:
  - B1509's join pulled back to M_n, n = 1..6: nu trivial on the fibre, nu(t_n) = (-1)^n, at q^2 - 34 q + 1 = 0;
  - the projective triplet pulled back to M_6 (s961 = M_3, so nu(t_6) = lam_3^2 = 1), at q^6 - 34 q^3 + 1 = 0.
Two primes per route (other primes for each route) and every root.

What is expected, and why (transfer).  On M_n the pulled-back module splits by Shapiro into deck-twisted parts V (x) chi.  At the
join's q, Q(q, s) = -q (s + 1)^2 (s^2 - 10 s + 1): its only root on the unit circle is s = -1 = mu, so every chi != 1 part of V, of
V* and of the trivial line is acyclic, and Lambda^2 rho_q (x) chi is acyclic for every unitary chi (T-HIGGS-BULK-ACYCLIC).  So
every class upstairs is a pulled-back class, and the triple product of pulled-back classes is n times B1513's zero.

Route L: B1513's independent_audit.member (the lifting criterion): the dimensions, [a_i ^ a_j] for all of H^1(W*), the mu-type
pairing and the cross terms [a_i ^ e f0].  Route T: B1513's higgs_lib with this arc's law_lib.coupling_tensor: h^1(V),
h^1(Lambda^2 W), the interior 10', and the up-type coupling on all of H^1(W*) against every 5'_H.
Positive control, both routes: B1510's +-i point (q^2 - 14 q + 1 = 0, nu(t) = i) pulled back to M_5 (nu(t_5) = i^5 = i; h^1(V)
stays 1, since of the fifth roots chi only chi = 1 puts i chi on a root of Q).  The coupling must be non-zero there."""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import law_lib as LT  # noqa: E402
import lift_route as LR  # noqa: E402
import census as CT  # noqa: E402

H, T = LT.H, LT.T
IA = LR.IA
RECORD = HERE / "case_a_levels_run.txt"
JOIN, TRIPLET6, CONTROL = "q**2 - 34*q + 1", "q**6 - 34*q**3 + 1", "q**2 - 14*q + 1"


# ============================================================================================ route T
def route_T(G, C, z, field, vals):
    """case (a)'s W = [[V, c], [0, 1]], V = nu rho_q with nu given on the generators; the up-type coupling on all of H^1(W*)"""
    rho = H.rho_mats(G, field)
    V = H.Module(G, {g: rho[g] * vals[g] for g in G.gens})
    cs, h1V = H.h1_basis(V)
    out = {"h1(V)": h1V}
    if h1V != 1:
        return out
    W = V.extension(cs[0].column())
    Wd = W.dual()
    tens, nh, na = LT.coupling_tensor(G, C, z, W.wedge2(), Wd, H.form_wedge(5))
    out.update({"h1(Lambda^2 W)": nh, "h1(W*)": na, "interior 10'": LT.interior_count(Wd),
                "Lambda^2 V acyclic": LT.h_data(V.wedge2())["h1"] == 0,
                "coupling zero on all of H^1(W*)": LT.all_zero(tens, field.dom), "symmetric": LT.symmetric(tens)})
    return out


def route_L(F, r, n, twist, label):
    res, _ = IA.member(F, IA.mn_mats(F, r), n, twist, label)
    return {"h1(V)": res["h(V)"]["h1"], "h1(Lambda^2 W)": res["h"]["Lambda2 W"]["h1"], "h1(W*)": res["h"]["W*"]["h1"],
            "Lambda^2 V acyclic": res["h"]["Lambda2 V"]["h1"] == 0,
            "B == 0 on H^1(W*)": res["B == 0 on H^1(W*)"], "mu-type pairing == 0": res["mu-type pairing == 0"],
            "cross terms [a_i ^ e f0] zero": all(str(v) == "0" for row in res["[a_i ^ e f0]"] for v in row),  # ModP shows an int
            "blocks check": res["blocks check (all products)"] and res["blocks check (cocycles and N)"],
            "B symmetric": res["B symmetric"]}


def main():
    t0 = time.time()
    out = {"join pulled back to M_n": [], "triplet on M_6": [], "control: +-i point pulled back to M_5": []}
    groups = {}

    def group(n):
        if n not in groups:
            G = H.FibredGroup(n)
            groups[n] = (G,) + G.fundamental()[:2]
        return groups[n]
    # ---------------------------------------------------------------- the join on M_1..M_6
    for n in range(1, 7):
        G, C, z = group(n)
        sign = (-1) ** n
        for (p, roots) in CT.primes_with_roots(JOIN, [2], 2, 2 ** 23 - 7 * 104729 - 31 * n):
            for r in roots:
                field = T.Field("gf", p=p, r=r)
                dom = field.dom
                vals = {"x": dom.one, "y": dom.one, "t": dom.convert(sign)}
                out["join pulled back to M_n"].append({"route": "T", "level": n, "p": p, "q": r, **route_T(G, C, z, field, vals)})
        for (p, roots) in LR.primes_for(JOIN, [2], 2, 2 ** 23 - 9 * 104729 - 37 * n):
            F = IA.ModP(p, f"GF({p})")
            for r in roots:
                out["join pulled back to M_n"].append({"route": "L", "level": n, "p": p, "q": r,
                                                       **route_L(F, r, n, (1, 1, 1 if sign == 1 else p - 1), f"join M{n}")})
        print(f"[{time.time() - t0:7.1f}s] join on M{n} done", flush=True)
    # ---------------------------------------------------------------- the triplet on M_6
    G, C, z = group(6)
    for (p, roots) in CT.primes_with_roots(TRIPLET6, [2], 2, 2 ** 23 - 11 * 104729):
        for r in roots:
            field = T.Field("gf", p=p, r=r)
            dom = field.dom
            for (a, b) in H.TRIPLET:
                vals = {"x": dom.convert((-1) ** (a // 2)), "y": dom.convert((-1) ** (b // 2)), "t": dom.one}
                out["triplet on M_6"].append({"route": "T", "member": [a, b], "p": p, "q": r, **route_T(G, C, z, field, vals)})
    for (p, roots) in LR.primes_for(TRIPLET6, [2], 2, 2 ** 23 - 13 * 104729):
        F = IA.ModP(p, f"GF({p})")
        for r in roots:
            for (a, b) in IA.TRIPLET:
                tw = (1 if a % 4 == 0 else p - 1, 1 if b % 4 == 0 else p - 1, 1)
                out["triplet on M_6"].append({"route": "L", "member": [a, b], "p": p, "q": r,
                                              **route_L(F, r, 6, tw, f"triplet {a, b} M6")})
    print(f"[{time.time() - t0:7.1f}s] triplet on M6 done", flush=True)
    # ---------------------------------------------------------------- the positive control on M_5
    G, C, z = group(5)
    for (p, roots) in CT.primes_with_roots(CONTROL, [4], 2, 2 ** 23 - 17 * 104729):
        iota = T.gf_root_of_unity(p, 4)
        for r in roots:
            field = T.Field("gf", p=p, r=r, iota=iota)
            dom = field.dom
            vals = {"x": dom.one, "y": dom.one, "t": dom(iota)}
            out["control: +-i point pulled back to M_5"].append({"route": "T", "p": p, "q": r, **route_T(G, C, z, field, vals)})
    for (p, roots) in LR.primes_for(CONTROL, [4], 2, 2 ** 23 - 19 * 104729):
        F = IA.ModP(p, f"GF({p})")
        iota = IA.sqrt_m1(p)
        for r in roots:
            out["control: +-i point pulled back to M_5"].append({"route": "L", "p": p, "q": r,
                                                                  **route_L(F, r, 5, (1, 1, iota), "control M5")})
    print(f"[{time.time() - t0:7.1f}s] control on M5 done", flush=True)
    # ---------------------------------------------------------------- the readings
    zeros = out["join pulled back to M_n"] + out["triplet on M_6"]
    ctl = out["control: +-i point pulled back to M_5"]

    def zero_row(row):
        if row["route"] == "T":
            return (row["h1(V)"] == 1 and row["h1(Lambda^2 W)"] == 1 and row["h1(W*)"] == 2 and row["interior 10'"] == 1
                    and row["Lambda^2 V acyclic"] and row["coupling zero on all of H^1(W*)"] and row["symmetric"])
        return (row["h1(V)"] == 1 and row["h1(Lambda^2 W)"] == 1 and row["h1(W*)"] == 2 and row["Lambda^2 V acyclic"]
                and row["B == 0 on H^1(W*)"] and row["mu-type pairing == 0"] and row["cross terms [a_i ^ e f0] zero"]
                and row["blocks check"] and row["B symmetric"])

    def control_row(row):
        if row["route"] == "T":
            return row["h1(V)"] == 1 and not row["coupling zero on all of H^1(W*)"]
        return row["h1(V)"] == 1 and not row["B == 0 on H^1(W*)"] and row["blocks check"]
    out["summary"] = {
        "readings (zeros), route T / route L": [sum(r["route"] == "T" for r in zeros), sum(r["route"] == "L" for r in zeros)],
        "levels of the join read": sorted({r["level"] for r in out["join pulled back to M_n"]}),
        "primes, route T / route L": [sorted({r["p"] for r in zeros + ctl if r["route"] == "T"}),
                                      sorted({r["p"] for r in zeros + ctl if r["route"] == "L"})],
        "case (a) through level 6: one 5'_H, the 10' coupling zero on all of H^1(W*), both routes": all(zero_row(r) for r in zeros),
        "positive control on M_5 non-zero, both routes": bool(ctl) and all(control_row(r) for r in ctl),
    }
    out["seconds"] = round(time.time() - t0, 1)
    if "--record" in sys.argv:
        RECORD.write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(json.dumps(out["summary"], indent=1))
    return out


if __name__ == "__main__":
    main()
