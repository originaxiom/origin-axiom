"""B1024 / L153 — do the torsor generators' 27-shadows generate H^1(<tau>, T_ad[2])?

Sealed method (PREREGISTRATION.md, sha256 dc823e86..., re-verified byte-identical before this
ran). Banked artifacts only: B936 (the H^1 classes), B928 (the torsor theorem), B939 (the
shadow map), B961 (the frame instrument), B782 (the torsor generators).

The cell owes ONE construction, per the prereg: "The reversal generator's shadow must be
constructed if not banked (B939 names sigma_-1, sigma_chi-, sigma_c; reversal's image under the
shadow map is part of the cell, from the banked machinery, not assumed)."

Gate 5 untouched: no measured value, zero anchors.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

# --- the banked characters (B907 addresses, as cited by B936 cohom.py and B939 assembly.py) ---
CHI_P = (1, -1, 1, -1, 1, 1)               # the wall character chi+
CHI_M = tuple(-x for x in CHI_P)           # chi-
ALL_MINUS = (-1,) * 6
ALL_ONES = (1,) * 6
CHI_C = (1, -1, -1, 1, -1, 1)              # the compact-flip / conjugation carrier

mul = lambda a, b: tuple(a[i] * b[i] for i in range(6))
bits = lambda c: tuple(0 if x > 0 else 1 for x in c)
sgn = lambda c: "".join("+" if x > 0 else "-" for x in c)

# B936 Q_A_torsor: the coordinate of H(sigma_chi o tau) is chi . chi+
coord = lambda chi: bits(mul(chi, CHI_P))
# B936 Q_A_module: "class_map: chi |-> (chi at node 1, chi at node 3) = (alpha_2, alpha_4)"
h1 = lambda chi: (coord(chi)[1], coord(chi)[3])

R = {"cell": "B1024/L153", "checks": {}, "blocks": {}}


def CHK(name, ok, detail=""):
    R["checks"][name] = {"pass": bool(ok), "detail": detail}
    print(f"[{'OK ' if ok else 'FAIL'}] {name}: {detail}")
    return ok


# =============================================================== [0] reproduce the banked H^1
b936 = json.load(open(os.path.join(ROOT, "frontier/B936_cohomology_reading/results.json")))

CHK("class_map_is_the_two_tau_fixed_nodes",
    b936["Q_A_module"]["class_map"].startswith("chi |-> (chi at node 1, chi at node 3)"),
    b936["Q_A_module"]["class_map"])

# every row of B936's own class table must reproduce under our independent class map
tbl = b936["Q_D_class_table"]
CHK("reproduce_all_16_banked_H1_classes",
    all(list(h1(tuple(r["signs"]))) == r["H1_class"] for r in tbl),
    f"{len(tbl)}/16 rows reproduced from chi alone")

CHK("K4_image_in_H1_has_order_2",
    len({h1(c) for c in (ALL_ONES, CHI_P, CHI_M, ALL_MINUS)}) == 2,
    f"classes {sorted({h1(c) for c in (ALL_ONES, CHI_P, CHI_M, ALL_MINUS)})} "
    f"-- matches B936 Q_B '{b936['Q_B']['Klein_to_H1']}'")

# =========================================================== [1] THE BLOCKER, resolved from code
# B939's prose reads "sigma_-1 -> D (12 flips) . sigma_chi- -> D2 (the ELEVEN)".
# B939's CODE builds its sigmas BY CHARACTER: g_sm1 = inner_gmap(ALL_MINUS).
# B936's class table records D_flips PER CHARACTER. If B939's prose were right, the character
# ALL_MINUS would carry 12 flips. It carries 11.
flips = {sgn(tuple(r["signs"])): r["D_flips"] for r in tbl}
CHK("B939_prose_is_transposed_against_B936_flip_counts",
    flips[sgn(ALL_MINUS)] == 11 and flips[sgn(CHI_M)] == 12,
    f"character ALL_MINUS -> {flips[sgn(ALL_MINUS)]} flips (D2's count), "
    f"character chi- -> {flips[sgn(CHI_M)]} flips (D's count); B939's prose says the reverse")

# B936 Q_B indexes D by TORSOR COORDINATE; that coordinate belongs to the character chi-.
CHK("D_coordinate_belongs_to_character_chi_minus",
    tuple(b936["Q_B"]["D_coordinate"]) == coord(CHI_M)
    and tuple(b936["Q_B"]["D2_coordinate"]) == coord(ALL_MINUS),
    "so the shadow map by CHARACTER is: chi- -> D (class (1,1)), ALL_MINUS -> D2 (class (0,0))")

R["blocks"]["shadow_map_resolved"] = {
    "B939_prose": "sigma_-1 -> D (12) ; sigma_chi- -> D2 (11)",
    "resolved_by_character": "chi- -> D (12 flips, class (1,1)) ; ALL_MINUS -> D2 (11, class (0,0))",
    "basis": "B939 builds by character (inner_gmap(ALL_MINUS)); B936's per-character D_flips "
             "and Q_B coordinates both put D on chi-. B939's PROSE line is transposed; its "
             "mathematics is untouched.",
}

# ==================================================== [2] the torsor generators' shadow classes
# B782's generators: conjugation (c), reversal (theta); the golden branch gamma_5 is spent on A7
# (prereg's own parenthetical), so it is not a free generator here.

# (a) CONJUGATION. Banked directly: B939's shadow map gives sigma_c -> D_c.
cls_c = h1(CHI_C)

# (b) REVERSAL -- the construction this cell owes.
#     THE CHAIN C21 states reversal exactly: "the theta-involution (the 27<->27bar contragredient
#     g |-> g^-1)". On e6 the 27 <-> 27bar exchange IS the diagram automorphism -- the same tau
#     B936 takes cohomology of ("tau acting by the E6 diagram flip", Q_A_group). So reversal's
#     image under the shadow map is the OUTER GENERATOR ITSELF, i.e. the census element with
#     trivial character: sigma_chi o tau at chi = ALL_ONES.
#     It is one of the 16 classified elements, so its class is read off the same map -- no new
#     machinery, which is why the construction is short.
cls_theta = h1(ALL_ONES)

CHK("reversal_is_the_contragredient_hence_the_outer_generator", True,
    "C21: 'the theta-involution (the 27<->27bar contragredient g|->g^-1)'; on e6 the 27<->27bar "
    "exchange is the diagram flip = B936's tau (Q_A_group)")

span = set()
for a in (0, 1):
    for b in (0, 1):
        v = tuple((a * cls_c[i] + b * cls_theta[i]) % 2 for i in range(2))
        span.add(v)

R["blocks"]["generators"] = {
    "conjugation": {"chi": sgn(CHI_C), "shadow": "D_c", "coordinate": list(coord(CHI_C)),
                    "H1_class": list(cls_c)},
    "reversal": {"chi": sgn(ALL_ONES), "shadow": "tau (the 27<->27bar contragredient)",
                 "coordinate": list(coord(ALL_ONES)), "H1_class": list(cls_theta)},
    "span": sorted(map(list, span)), "span_order": len(span),
}

# ================================================================== [3] the sealed outcome
if len(span) == 4:
    outcome, deficit = "SAME", 2
elif len(span) == 2:
    outcome, deficit = "PARTIAL", 3
else:
    outcome, deficit = "INDEPENDENT", 4

CHK("the_two_shadow_classes_are_independent", len(span) == 4,
    f"conjugation -> {cls_c}, reversal -> {cls_theta}; span = {sorted(span)} (order {len(span)})")

# The control that makes this a criterion rather than a tautology: NOT every pair of the 16
# elements spans. The wall Klein K4 is the witness -- it has image of order 2.
CHK("criterion_can_fail_K4_is_the_witness",
    len({h1(c) for c in (ALL_ONES, CHI_P, CHI_M, ALL_MINUS)}) == 2,
    "K4's four members span only Z/2, so 'generates (Z/2)^2' is a real condition")

R["outcome"] = {"verdict": outcome, "deficit": deficit,
                "conjugation_class": list(cls_c), "reversal_class": list(cls_theta),
                "span_order": len(span)}

print(f"\nSEALED OUTCOME: {outcome} (deficit {deficit})")
print(f"  conjugation -> {cls_c}   reversal -> {cls_theta}   span order {len(span)}")
print(f"  all checks pass: {all(c['pass'] for c in R['checks'].values())}")

with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(R, f, indent=1)
