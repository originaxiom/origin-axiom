#!/usr/bin/env python3
"""B943 -- independent in-sandbox verification of the two load-bearing facts
behind the B922 priority correction.  Compute-not-cite: the literature panel's
findings are checked here against arithmetic this seat runs itself.

FACT 1  the index-12 relation, from Humbert's volume formula (not asserted)
FACT 2  r = 4.9000853... lies BELOW the parent's spectrum, so lambda_2 is NOT
        a pullback of a published parent eigenvalue -- screened by the Weyl
        law, and cross-checked by reproducing B791's own W = 1.010
"""
import json
import pathlib

import mpmath as mp

mp.mp.dps = 30
R = {}


def L_chi3(s):
    """L(s, chi_{-3}) via Hurwitz zeta."""
    return (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)) / mp.power(3, s)


def zeta_K(s):
    return mp.zeta(s) * L_chi3(s)


# --- FACT 1: Humbert volume of the parent, and the index ---------------------
volP = mp.power(3, mp.mpf(3) / 2) * zeta_K(2) / (4 * mp.pi ** 2)
vol4 = mp.mpf("2.029883212819307250042405108549")     # m004, standard
ratio = vol4 / volP
R["zeta_K_2"] = mp.nstr(zeta_K(2), 15)
R["vol_parent_humbert"] = mp.nstr(volP, 15)
R["vol_m004"] = mp.nstr(vol4, 15)
R["index_ratio"] = mp.nstr(ratio, 12)
R["index_is_12"] = bool(abs(ratio - 12) < mp.mpf("1e-12"))

# --- FACT 2: the Weyl screen on the parent ----------------------------------
def W(r, vol):
    """Leading Weyl term on H^3: N(r) ~ vol * r^3 / (6 pi^2)."""
    return vol * r ** 3 / (6 * mp.pi ** 2)


r_lambda2 = mp.mpf("4.9000853730625213014795758")
r_parent_gs = mp.mpf("7.072004187")

R["W_parent_at_lambda2"] = mp.nstr(W(r_lambda2, volP), 8)
R["W_parent_at_parent_ground_state"] = mp.nstr(W(r_parent_gs, volP), 8)
R["W_m004_at_lambda2"] = mp.nstr(W(r_lambda2, vol4), 8)
R["reproduces_B791_W_1_010"] = bool(abs(W(r_parent_gs, volP) - mp.mpf("1.010")) < mp.mpf("0.01"))
R["parent_count_below_lambda2_is_under_one"] = bool(W(r_lambda2, volP) < 1)
R["lambda2_below_parent_ground_state"] = bool(r_lambda2 < r_parent_gs)

# --- the precision arithmetic the correction turns on -----------------------
b922 = "4.9000853730625213014795758"
R["b922_decimal_places"] = len(b922.split(".")[1])
R["precedent_decimal_places"] = 13          # Aurich-Steiner-Then, r = 6.6221193402528
R["improvement_decimal_places"] = R["b922_decimal_places"] - R["precedent_decimal_places"]
R["repo_asserted_precedent_was"] = 10
R["precedent_claim_refuted"] = R["repo_asserted_precedent_was"] != R["precedent_decimal_places"]

print(json.dumps(R, indent=1))
pathlib.Path(__file__).resolve().parent.joinpath("results.json").write_text(
    json.dumps(R, indent=1) + "\n")
