"""STEP B's generator, the one decisive conjunction and its pre-written readings (the design's section 5, its section 9,
and main's rulings on the third and fourth reviews: generator_review_3/ and generator_review_4/MAIN_RULINGS.md; data-free).

PASS = S IN SUPPORT and X2 (p2 < 0.01/m) and K (K judged, C_ten > 0 and p_K < 0.01/m) and the CKM leg (p_CKM < 0.01/m and
its chi2_4 < 13.28 clause at an address the six support).  p2 is decided on the upper end of its two-sided 95%
Clopper-Pearson interval (a simulated rate); p_K and p_CKM are the exact likelihood-ratio bounds 2^-C_ten and 2^-bits_CKM
(Markov: C_ten = log2 q/p0 with q a sub-probability, bits_CKM = log2 p_post/p_marg with E_marg[p_post/p_marg] = 1; main's
ruling, 2026-10-30), capped at 1; m is the joint look ledger's count at the seal plus one, at least 53.  T's grades under every
clock of the card's menu are required: NEGATIVE under every clock makes the attempt NEGATIVE (the bar's final grade).

The readings use THE FINAL ATTACK's words (docs/THE_FINAL_ATTACK_2026-10-29.md, Outcomes):
- NO SUPPORT: not S;
- SUPPORT WITHOUT SPECIFICITY: S and not X2 ("random worlds are reached as often"), whatever K and the CKM leg say;
- PASS (breakthrough-grade): all four;
- otherwise S and X2 hold and K or the CKM leg fails: a READING that names the failed legs."""
from __future__ import annotations

import math
from itertools import product

LEGS = ("S", "X2", "K", "CKM")


def _p(x, name):
    if x is None or not isinstance(x, (int, float)) or math.isnan(x) or x < 0 or x > 1:
        raise ValueError("%s must be a probability bound in [0, 1], got %r" % (name, x))
    return float(x)


def legs(in_support: bool, p2_up: float, K_grade: str, C_ten: float, pK_up: float, pckm_up: float, ckm_clause: bool,
         m: int) -> dict:
    if not isinstance(m, int) or m < 53:
        raise ValueError("m is the joint look ledger's count at the seal plus one, at least 53; got %r" % (m,))
    if K_grade not in ("JUDGED", "UNJUDGED"):
        raise ValueError("K_grade must be JUDGED or UNJUDGED")
    g = 0.01 / m
    if K_grade == "UNJUDGED":
        k = False
    else:
        if C_ten is None or (isinstance(C_ten, float) and math.isnan(C_ten)):
            raise ValueError("C_ten is required when K is judged")
        k = (C_ten > 0) and (_p(pK_up, "p_K") < g)
    return {"S": bool(in_support), "X2": _p(p2_up, "p2") < g, "K": k, "K_grade": K_grade,
            "CKM": (_p(pckm_up, "p_CKM") < g) and bool(ckm_clause)}


def reading(L: dict, T_grades) -> str:
    """T_grades: the T1 grade ('NEGATIVE' or 'CONSISTENT') under every clock of the card's menu; required"""
    T_grades = tuple(T_grades)
    if not T_grades or any(g not in ("NEGATIVE", "CONSISTENT") for g in T_grades):
        raise ValueError("T's grades under every clock of the menu are required")
    if all(g == "NEGATIVE" for g in T_grades):
        return "NEGATIVE: T is NEGATIVE under every clock of the menu (the bar's final grade); the legs are reported"
    s, x, k, c = (L[n] for n in LEGS)
    unj = " (K UNJUDGED: the six lie outside the primary null's box, so K cannot pass)" if L.get("K_grade") == "UNJUDGED" else ""
    if not s:
        return ("NO SUPPORT: the frame does not contain our world's mixing at a rigid address (NOT FOUND unless the reach and "
                "resolution make it EXCLUDED); X2, K and the CKM leg are reported ungraded" + unj)
    if not x:
        return ("SUPPORT WITHOUT SPECIFICITY: reached, but random worlds are reached as often; a landscape that contains our "
                "world without explaining it, at this precision (a READING); K %s, the CKM leg %s" % (
                    "held" if k else "failed", "held" if c else "failed") + unj)
    if k and c:
        return ("PASS (breakthrough-grade): our world in the support with compression beyond the null's and the CKM predicted "
                "from the six's address with no new freedom (the decisive conjunction; a rarity screen, not a derivation)")
    failed = [n for n, v in (("compression (K)", k), ("the CKM leg", c)) if not v]
    return "SUPPORT WITH SPECIFICITY: a READING; the conjunction fails on %s" % " and ".join(failed) + unj


def p_exact(bits) -> float:
    """the exact likelihood-ratio bound 2^-bits as a probability bound in [0, 1]"""
    if bits is None or (isinstance(bits, float) and math.isnan(bits)):
        raise ValueError("bits required")
    return 1.0 if bits <= 0 else float(2.0 ** (-bits))


def table() -> list:
    rows = []
    for vals in product((True, False), repeat=4):
        L = dict(zip(LEGS, vals)); L["K_grade"] = "JUDGED"
        rows.append((vals, reading(L, ("CONSISTENT",))))
    return rows
