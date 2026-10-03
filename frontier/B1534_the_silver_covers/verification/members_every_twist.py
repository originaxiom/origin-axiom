#!/usr/bin/env python3
"""B1534 control K10 (before the seal): the members of m135 and m136 at every twist kappa in C*, not only at the twists
sm:B1530 read.  It reads which characters are members (h^1(V_eta) >= 1), never a term T(nu, chi, c).  Writes
members_every_twist.json and members_every_twist_log.txt.

By sm:B1529's Lemma F (the fibre's four-term sequence), for nu = (u, kappa) with H^0(F; u (x) rho) = 0,
    h^1(Gamma; nu (x) rho) = dim ker(T_C(u) - kappa),   T_C(u) = S0 on C = H^1(F; u (x) rho)  (a 4 x 4 matrix),
so nu is a member exactly when kappa^5 is an eigenvalue of T_C(u) (nu^5 = (5u, kappa^5) = (u, kappa^5): every fibre
character here has order dividing 4).  The seal's Lemma Q needs the eigenvalues that are roots of unity.

Route T (sm:B1529's fibre_lib, banked, at 320 bits): T_C(u) for every fibre character u of both states; its characteristic
polynomial p_u; the order of vanishing of p_u at 1 and at -1 (with margins); the quotient q_u = p_u / ((x - 1)^m1 (x + 1)^m2)
(remainder checked); every root of q_u at 60 digits with its distance from the unit circle; and, for any root on the circle,
the least n <= 240 with root^n = 1.
Route E (sm:B1530's exact_lib over Q(zeta_24), banked): h^1(nu (x) rho) exactly at every x = kappa' in mu_24, every u.
The two are compared at all of mu_24 (route T's g_at(T_C(u), x) against route E's h^1)."""
import json
import sys
import time
import warnings
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

import mpmath as mp
from flint import acb, acb_poly

warnings.filterwarnings("ignore")
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import silver_lib as SL  # noqa: E402

S, E = SL.S, SL.E
FT = S.load(S.B1529, "fibre_lib", "b1529_fibre_lib")
LOG = []
ON_CIRCLE = mp.mpf(10) ** -20        # | |root| - 1 | below this is on the unit circle
ORDER_TOL = mp.mpf(10) ** -20        # | root^n - 1 | below this is n-th root of unity


def say(s):
    print(s, flush=True)
    LOG.append(s)


def to_mp(z):
    return FT.mp_of_acb_scalar(z)


def poly_div_linear_power(p, r, m):
    """p / (x - r)^m for an acb_poly p and acb r, with the largest remainder coefficient relative to p's largest"""
    q = p
    worst = mp.mpf(0)
    top = max(abs(to_mp(c)) for c in p.coeffs())
    for _ in range(m):
        q, rem = divmod(q, acb_poly([-r, acb(1)]))
        for c in rem.coeffs():
            worst = max(worst, abs(to_mp(c)) / top)
    return q, worst


def route_t(sign, word):
    mp.mp.dps = 60
    mats = FT.hyperbolic_mats(sign, word)
    FL = S.family()
    G, img = FL.word_group(sign, word)
    chars, D = FL.torsion_characters(img)
    fm = FT.FibreModule(sign, img, mats, D)
    rows = []
    for u in chars:
        i, j = int(u[0] * D), int(u[1] * D)
        TC, slot, cond = fm.T_C(i, j)
        h0 = fm.fibre_invariants(i, j)
        p = FT.charpoly(TC)
        m1, z1, n1 = FT.order_at(p, acb(1))
        m2, z2, n2 = FT.order_at(p, acb(-1))
        q, rem1 = poly_div_linear_power(p, acb(1), m1)
        q, rem2 = poly_div_linear_power(q, acb(-1), m2)
        coeffs = [to_mp(c) for c in reversed(q.coeffs())]          # highest degree first, for polyroots
        roots = mp.polyroots(coeffs, maxsteps=400, extraprec=400) if len(coeffs) > 1 else []
        rts = []
        for z in roots:
            dist = abs(abs(z) - 1)
            order = None
            if dist < ON_CIRCLE:
                for n in range(1, 241):
                    if abs(z ** n - 1) < ORDER_TOL:
                        order = n
                        break
            rts.append({"root": mp.nstr(z, 25), "| |root| - 1 |": mp.nstr(dist, 5), "on the circle": bool(dist < ON_CIRCLE),
                        "order (n <= 240)": order})
        g1 = FT.g_at(TC, acb(1))[0]
        g2 = FT.g_at(TC, acb(-1))[0] if m2 else 0
        rows.append({"u": [str(u[0]), str(u[1])], "H0(F)": h0, "slot": slot, "slot conditioning": mp.nstr(cond, 3),
                     "am at 1": m1, "am margins at 1 (zero, nonzero)": [mp.nstr(z1, 3) if z1 is not None else None,
                                                                        mp.nstr(n1, 3) if n1 is not None else None],
                     "am at -1": m2, "am margins at -1 (zero, nonzero)": [mp.nstr(z2, 3) if z2 is not None else None,
                                                                          mp.nstr(n2, 3) if n2 is not None else None],
                     "g at 1": g1, "g at -1": g2, "division remainder (rel)": mp.nstr(max(rem1, rem2), 3),
                     "other roots": rts, "TC": TC, "i, j, D": (i, j, D)})
    return rows, fm, D


def main():
    t0 = time.time()
    out = {"started": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "states": {}}
    say(f"B1534 K10, the members at every twist, {out['started']}")
    allok = True
    for state in ("-LLRR", "+LLRR"):
        st = SL.setup(state)
        rows, fm, D = route_t(st["sign"], st["word"])
        # ------------------------------------------------------------ route E at every x in mu_24, and the comparison
        hitsE, disagree = [], []
        for r in rows:
            u = (Fraction(r["u"][0]), Fraction(r["u"][1]))
            for jj in range(24):
                x = Fraction(jj, 24)
                ch = SL.char(st, u, x)
                h1 = E.Cohomology(st["G"], st["rho"].twist(ch)).h1
                gT = FT.g_at(r["TC"], FT.root_of_unity(jj, 24))[0]
                if h1 >= 1:
                    hitsE.append([r["u"], str(x), h1])
                if gT != h1:
                    disagree.append([r["u"], str(x), "E", h1, "T", gT])
        # ------------------------------------------------------------ the verdict for this state
        unit_roots_other = [(r["u"], z["root"], z["order (n <= 240)"]) for r in rows for z in r["other roots"]
                            if z["on the circle"]]
        minus_one = [r["u"] for r in rows if r["am at -1"] > 0]
        nearest = min((mp.mpf(z["| |root| - 1 |"]) for r in rows for z in r["other roots"]), default=None)
        rec = {"name": st["name"], "D": D,
               "rows": [{k: v for k, v in r.items() if k != "TC"} for r in rows],
               "route E: h1 >= 1 on mu_24 at": hitsE, "routes T and E disagree on mu_24 at": disagree,
               "comparisons": 24 * len(rows),
               "every u has eigenvalue 1": all(r["am at 1"] >= 1 for r in rows),
               "u with eigenvalue -1": minus_one,
               "other roots on the unit circle": unit_roots_other,
               "nearest other root to the circle": mp.nstr(nearest, 5) if nearest is not None else None,
               "H0(F) != 0 at": [r["u"] for r in rows if r["H0(F)"] != 0]}
        ok = (not disagree and not unit_roots_other and rec["every u has eigenvalue 1"] and not rec["H0(F) != 0 at"])
        rec["holds"] = ok
        allok &= ok
        out["states"][state] = rec
        say(f"{state} ({st['name']}, D = {D}): eigenvalue 1 at every u {rec['every u has eigenvalue 1']}; "
            f"eigenvalue -1 at {minus_one}; other roots on the circle {unit_roots_other}; nearest other root to the circle "
            f"{rec['nearest other root to the circle']}; route E hits on mu_24 {hitsE}; T vs E disagreements {disagree} "
            f"({rec['comparisons']} comparisons)")
        for r in rows:
            say(f"   u = ({r['u'][0]}, {r['u'][1]}): am(1) = {r['am at 1']}, g(1) = {r['g at 1']}, am(-1) = {r['am at -1']}, "
                f"g(-1) = {r['g at -1']}, other roots "
                f"{[(z['root'][:14], z['| |root| - 1 |']) for z in r['other roots']]}")
    out["holds"] = allok
    out["seconds"] = round(time.time() - t0)
    say(f"K10 holds: {allok} ({out['seconds']} s)")
    (HERE / "members_every_twist.json").write_text(json.dumps(out, indent=1, default=str))
    (HERE / "members_every_twist_log.txt").write_text("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
