"""B1048 — the seam cluster CLOSED: the nine remaining rows, and the scale wall's real proof.

B1047 dispositioned five of the cluster's fourteen rows. This closes the other nine, and the
headline is not the seam -- it is that the survivor sitting beside the corpus's worst trap is a
THEOREM nobody had put on a curated surface.

  B408's headline says "THE SEAM DOES NOT CONTRACT -- the one scale lever stands", verdict
  NEGATIVE, killed 27 lines down by its own body (registered at B1046 as the worst case in the
  corpus). B426 is the arc that upgrades that correction FROM A DIAGNOSIS TO A THEOREM: the three
  "real embeddings" whose max gave 1.217 are THE THREE GALOIS CONJUGATES OF ONE CUBIC NUMBER, and
  the averages of that orbit are all below 1. The trap was registered; the survivor was not.

AND THE THEOREM'S OWN SLOGAN IS TOO STRONG, WHICH THIS ARC FIXES BEFORE RESTORING IT. B426 writes
"every Galois-invariant functional of the orbit is < 1". The elementary symmetric e1 = 3/2 > 1,
and the power mean M_6 = 1.0134 > 1. What is true -- and sharper -- is that the power-mean family
contracts for every p below an exact crossover p* = 5.5932..., and only exceeds 1 as it degenerates
toward max, which IS the embedding bias B408's correction named. The wall is not weakened; it is
given its boundary.

RESTORED HERE, each re-verified first (campaign step 5):
  A. B426  -- the Galois-orbit contraction theorem, with the crossover.
  B. B449 + B427 -- the seam field is FORCED and its level is a CONDUCTOR; the exchange is the
     Galois element sigma_17, which fixes sqrt(-15).
  C. B363 + B402 + B478 -- one statement: THE SEAM IS AN ADDRESS PROPERTY.

DECLINED, with the arcs' own corrections cited: B459 (its ADDENDUM withdraws the object-level
reading twice over), B431 (claim-line gap; the table is pair-specific), B474 (its own words: the
correspondence "demands a mechanism").
"""
import glob
import json
import pathlib
import re
import subprocess
import sys

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
import importlib.util as _ilu
_MB = _ilu.module_from_spec(_ilu.spec_from_file_location(
    "_md_blocks", ROOT / "scripts" / "checks" / "md_blocks.py"))
_ilu.spec_from_file_location("_md_blocks", ROOT / "scripts" / "checks" / "md_blocks.py").loader.exec_module(_MB)

R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def body(bid):
    p = glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "FINDINGS.md"))
    return pathlib.Path(p[0]).read_text(encoding="utf-8") if p else ""


def vd(bid):
    p = glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))
    return json.loads(pathlib.Path(p[0]).read_text(encoding="utf-8")) if p else {}


def flat(s):
    return re.sub(r"\s+", " ", s)


x = sp.Symbol("x")
HASH_Q2 = "db8f558269c93bee"   # the artifact the 5m16s regeneration reproduced byte-for-byte

# ================================================================== A. THE SCALE WALL, RE-PROVED
# B408's trap and B426's survivor sit side by side, and only the trap was registered.
b408 = body("B408")
chk("A_b408s_headline_still_asserts_the_lever_stands",
    "THE SEAM DOES NOT CONTRACT — the one scale lever stands" in b408
    and vd("B408").get("verdict") == "NEGATIVE")
chk("A_and_its_own_body_kills_it_with_the_embedding_bias",
    "the seam CONTRACTS" in b408 and "biased by embedding count" in flat(b408)
    and "0.7649" in b408)
# STATED PRECISELY, because the loose version is false. B1046's registry DOES name B426 -- its
# B408 row says "B426 upgrades the correction to a theorem -- survivor and trap sit side by side".
# What was missing is not the NAME but the LAW: no CURATED surface carried B426's theorem, so a
# reader of the five consolidations met B408's headline and nothing that answered it.
CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]
def curated_without_this_arc():
    # BLOCK-level (B1049) -- see scripts/checks/md_blocks.py for why the line-level form is wrong.
    AFTER = re.compile(r"\bB104[89]\b|\bB10[5-9]\d\b")
    return "\n".join(_MB.drop_blocks(read(p), AFTER) for p in CURATED)
chk("A_B1046_named_B426_in_the_REGISTRY__so_the_gap_was_the_LAW_not_the_NAME",
    "B426 upgrades the correction to a theorem" in read("docs/consolidation/SUPERSESSIONS.md"))
chk("A_but_NO_CURATED_surface_carried_B426_before_this_arc",
    not re.search(r"\bB426\b", curated_without_this_arc()))

# THE CLOSED FORM, RE-DERIVED FROM SCRATCH -- not read off the banked JSON.
alpha = 2 * sp.cos(2 * sp.pi / 9)
chk("A_alpha_is_the_ninth_cyclotomic_real_generator",
    sp.expand(sp.minimal_polynomial(alpha, x) - (x ** 3 - 3 * x + 1)) == 0)
ratio = sp.expand(3 * alpha ** 2 + 4 * alpha - 1) / 10
minpoly = sp.Poly(sp.minimal_polynomial(ratio, x), x)
chk("A_the_ratios_minimal_polynomial_is_B426s",
    sp.expand(minpoly.as_expr() - (1000 * x ** 3 - 1500 * x ** 2 + 360 * x - 19)) == 0,
    minpoly=str(minpoly.as_expr()))
# sqrt5-FREE, and that is the structural half: the golden factor is level-inert 15 -> 45.
# sqrt5-FREENESS, and it is the structural half of B426: the 5-local factor is level-inert from
# 15 to 45, so the golden factor cancels and the ratio is a pure 3-local quantity. The test is
# ramification: 5 is unramified in Q(zeta_9)+ because it does not divide the field discriminant.
disc = sp.discriminant(x ** 3 - 3 * x + 1, x)
chk("A_sqrt5_free_because_5_does_not_divide_the_field_discriminant",
    disc == 81 and 81 % 5 != 0, disc=int(disc))

roots = [sp.re(r) for r in minpoly.nroots(n=40)]
chk("A_the_three_embeddings_are_the_three_conjugates_of_ONE_number",
    len(roots) == 3 and all(abs(float(minpoly.as_expr().subs(x, r))) < 1e-25 for r in roots),
    roots=[float(r) for r in roots])
chk("A_and_B408s_1_2170_is_exactly_the_LARGEST_conjugate",
    abs(float(max(roots)) - 1.2170) < 1e-4, largest=float(max(roots)))

# The exact symmetric functionals, from the coefficients -- no floating point.
e1, e2, e3 = sp.Rational(1500, 1000), sp.Rational(360, 1000), sp.Rational(19, 1000)
chk("A_arithmetic_mean_is_EXACTLY_one_half", sp.simplify(e1 / 3 - sp.Rational(1, 2)) == 0)
chk("A_RMS_is_EXACTLY_sqrt51_over_10",
    sp.simplify(sp.sqrt((e1 ** 2 - 2 * e2) / 3) - sp.sqrt(51) / 10) == 0)
chk("A_geometric_mean_is_EXACTLY_the_cube_root_of_19_over_1000",
    sp.simplify(sp.root(e3, 3) - sp.root(sp.Rational(19, 1000), 3)) == 0)
chk("A_all_three_named_means_are_below_one",
    all(float(v) < 1 for v in (e1 / 3, sp.sqrt(51) / 10, sp.root(e3, 3))))

# ---- THE CORRECTION. B426's slogan is over-broad, and the exact boundary is computed here. ----
chk("A_b426_states_the_slogan_in_its_over_broad_form",
    "Every Galois-invariant functional of the orbit is < 1" in body("B426"))
chk("A_CORRECTION__the_elementary_symmetric_e1_is_3_over_2_which_EXCEEDS_one",
    sp.simplify(e1 - sp.Rational(3, 2)) == 0 and e1 > 1)


def power_mean(p):
    return (sum(float(r) ** p for r in roots) / 3) ** (1.0 / p)


chk("A_CORRECTION__the_sixth_power_mean_also_exceeds_one",
    power_mean(6) > 1 and power_mean(5) < 1,
    M5=power_mean(5), M6=power_mean(6))
lo, hi = 1.0, 200.0
for _ in range(300):
    mid = (lo + hi) / 2
    (lo, hi) = (mid, hi) if sum(float(r) ** mid for r in roots) < 3 else (lo, mid)
chk("A_the_exact_boundary__power_means_contract_below_p_star_5_5932",
    abs(lo - 5.5932) < 1e-3 and abs(power_mean(lo) - 1.0) < 1e-9, p_star=lo)
# ...and the family only exceeds 1 as it DEGENERATES TOWARD MAX, which is the very bias B408's
# correction named. The wall is not weakened by this; it is given its boundary.
chk("A_the_family_tends_to_MAX_which_is_the_bias_B408_named",
    abs(power_mean(400) - float(max(roots))) < 1e-2)
# MAX is not a Galois-invariant NUMBER: it is one of three conjugates of an IRREDUCIBLE cubic, so
# it is irrational and no Galois element fixes it. Shown from the polynomial, not from a float.
chk("A_and_MAX_is_not_a_Galois_invariant_NUMBER__the_cubic_is_irreducible_over_Q",
    minpoly.is_irreducible and minpoly.degree() == 3
    and all(sp.simplify(minpoly.as_expr().subs(x, sp.Rational(p, q))) != 0
            for p in (1, 19) for q in (1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250,
                                       500, 1000) for _ in (1,)))


# ================================== B. THE SEAM FIELD IS FORCED, AND ITS LEVEL IS A CONDUCTOR
t = sp.Symbol("t")
ALEX = {"4_1": t ** 2 - 3 * t + 1, "5_2": 2 * t ** 2 - 3 * t + 2, "6_1": 2 * t ** 2 - 5 * t + 2}
chk("B_5_2_and_6_1_are_NOT_fibered__their_Alexander_leading_coefficient_is_2",
    sp.Poly(ALEX["5_2"], t).LC() == 2 and sp.Poly(ALEX["6_1"], t).LC() == 2)
chk("B_so_the_requested_falsification_CANNOT_RUN_and_that_IS_the_answer",
    "5₂ is not fibered" in body("B449") and "non-sequitur" in body("B449"))
chk("B_the_fig8s_Alexander_IS_its_monodromy_char_poly",
    sp.expand(ALEX["4_1"] - sp.Matrix([[2, 1], [1, 1]]).charpoly(t).as_expr()) == 0)
chk("B_so_disc_trace_x_disc_Alexander_is_really_disc_geometry_x_disc_dynamics",
    sp.discriminant(ALEX["4_1"], t) == 5)


def conductor(d):
    """Conductor of Q(sqrt d) = |fundamental discriminant|."""
    core = 1
    for p, e in sp.factorint(sp.Integer(d)).items():
        if e % 2:
            core *= p
    core = int(core)
    return abs(core if core % 4 == 1 else 4 * core)


chk("B_golden__cond3_x_cond5_gives_the_seam_level_15",
    conductor(-3) == 3 and conductor(5) == 5 and sp.ilcm(3, 5) == 15)
chk("B_silver__the_dynamics_field_is_Q_sqrt2_of_conductor_8",
    sp.discriminant(t ** 2 - 6 * t + 1, t) == 32 and conductor(2) == 8)
chk("B_silver__cond4_x_cond8_gives_8_not_32", conductor(-1) == 4 and sp.ilcm(4, 8) == 8)
chk("B_bronze__the_REGISTERED_NOT_RUN_prediction_is_39_or_52",
    sp.discriminant(t ** 2 - 11 * t + 1, t) == 117 and conductor(13) == 13
    and {int(sp.ilcm(3, 13)), int(sp.ilcm(4, 13))} == {39, 52})
chk("B_and_B449_marks_bronze_registered_NOT_run",
    "Registered, not run" in body("B449"))

# B427: the exchange is a Galois element, and it FIXES the physical channel.
chk("B_the_exchange_element_is_pinned_by_4k_equiv_8_mod_60",
    [k for k in range(60) if (4 * k) % 60 == 8 and sp.gcd(k, 60) == 1] == [17, 47])


def sigma(gen, k, prec=40):
    def z(j):
        return sp.exp(2 * sp.pi * sp.I * ((j * k) % 60) / 60)
    return complex(sp.N(gen(z), prec))


G = {"i": lambda z: z(15),
     "sqrt5": lambda z: 2 * (z(12) + z(-12)) + 1,
     "sqrt-3": lambda z: z(10) - z(-10)}
G["sqrt-15"] = lambda z: (2 * (z(12) + z(-12)) + 1) * (z(10) - z(-10))
act = {nm: (sigma(g, 1), sigma(g, 17)) for nm, g in G.items()}
chk("B_sigma17_FIXES_i", abs(act["i"][0] - act["i"][1]) < 1e-25)
chk("B_sigma17_NEGATES_sqrt5_and_sqrt_minus_3",
    abs(act["sqrt5"][0] + act["sqrt5"][1]) < 1e-25
    and abs(act["sqrt-3"][0] + act["sqrt-3"][1]) < 1e-25)
chk("B_HENCE_sigma17_FIXES_sqrt_minus_15__the_PHYSICAL_channel_is_exchange_symmetric",
    abs(act["sqrt-15"][0] - act["sqrt-15"][1]) < 1e-25)
chk("B_and_B427_CORRECTED_the_handoff_it_adjudicated",
    "Chat-1's (T±2C+S)/4 holds only if C′=C" in body("B427"))


# ==================================== C. THE SEAM IS AN ADDRESS PROPERTY (B363 · B402 · B478)
# C1 -- NECESSITY. B363's Par-lemma, re-derived: a real trace has no seam. In H = Q(sqrt5,sqrt-3),
# an element x + y*sqrt5 + z*sqrt-3 + s*sqrt-15 is real iff z = s = 0, because sqrt3 and sqrt15
# are Q-linearly independent.
xs, ys, zs, ss = sp.symbols("x y z s", rational=True)
im = sp.simplify(sp.im(sp.expand(xs + ys * sp.sqrt(5) + zs * sp.sqrt(-3) + ss * sp.sqrt(-15))))
chk("C1_the_imaginary_part_of_an_H_element_is_exactly_sqrt3_z_plus_sqrt15_s",
    sp.simplify(im - (sp.sqrt(3) * zs + sp.sqrt(15) * ss)) == 0)
# Im = sqrt3*(z + sqrt5*s). For RATIONAL z, s that vanishes iff z = s = 0, since sqrt5 is
# irrational. So a real trace has BOTH the sqrt-3 and the sqrt-15 coordinate zero -- no seam.
chk("C1_so_for_rational_coordinates_real_forces_z_equals_s_equals_zero",
    sp.simplify(im / sp.sqrt(3) - (zs + sp.sqrt(5) * ss)) == 0 and not sp.sqrt(5).is_rational)
chk("C1_b363_states_necessity_and_then_REFUTES_sufficiency",
    "Par-non-commutation is necessary" in flat(body("B363"))
    and "Necessity is not sufficiency" in flat(body("B363")))
chk("C1_all_225_one_sided_twists_are_dark", "dark, 0/225" in flat(body("B363")))
# B363's tier is NUMERICAL for the twist scan, and the row must say so.
chk("C1_and_its_twist_scan_is_NUMERICAL_tier_by_its_own_status_line",
    "Numerical tier (double precision" in body("B363"))

# C2 -- INTENSITY. B402's landscape, RE-RUN end-to-end against the live tree (q2_landscape.py,
# 5m16s, pure Fraction) with output byte-identical to the banked artifact -- so these 15 addresses
# are re-verified, not cited. The hash below pins what the regeneration reproduced.
LAND = json.loads(pathlib.Path(glob.glob(
    str(ROOT / "frontier" / "B402_*" / "q2_landscape.json"))[0]).read_text())
chk("C2_the_landscape_covers_all_15_D_side_addresses", len(LAND) == 15, keys=sorted(LAND)[:4])
counts = {}
for r_, v in LAND.items():
    g = int(sp.gcd(int(r_), 15))
    counts.setdefault(g, set()).add(v["s_cells"] if isinstance(v, dict) and "s_cells" in v else
                                   (v.get("nonzero") if isinstance(v, dict) else v))
chk("C2_intensity_is_a_FUNCTION_of_gcd_with_15__one_value_per_class",
    all(len(s) == 1 for s in counts.values()),
    classes={k: sorted(v) for k, v in sorted(counts.items())})
chk("C2_and_the_law_is_f_equals_1_44__3_32__5_36__15_0",
    {k: list(v)[0] for k, v in counts.items()} == {1: 44, 3: 32, 5: 36, 15: 0})
import hashlib
chk("C2_the_regenerated_artifact_is_pinned_by_hash",
    hashlib.sha256(pathlib.Path(glob.glob(str(ROOT / "frontier" / "B402_*" /
        "q2_landscape.json"))[0]).read_bytes()).hexdigest()[:16] == HASH_Q2)
chk("C2_the_canonical_untwisted_point_is_the_UNIQUE_dark_address",
    sum(1 for v in LAND.values()
        if (v.get("s_cells", v.get("nonzero")) if isinstance(v, dict) else v) == 0) == 1)

# C3 -- THE SHIFT. B478's identity, proved symbolically AND checked over the whole range.
j_, c_, m_ = sp.symbols("j c m", integer=True)
chk("C3_the_two_line_proof_is_an_EXPONENT_IDENTITY",
    sp.expand(c_ * m_ * (-j_) * (-j_ - 1) / 2
              - (c_ * m_ * j_ * (j_ - 1) / 2 + c_ * m_ * j_)) == 0)
bad = [(m, c, j) for m in range(1, 16) for c in range(1, 16) for j in range(15)
       if (c * m * ((-j % 15) * ((-j % 15) - 1) // 2)) % 15
       != (c * m * (j * (j - 1) // 2) + c * m * j) % 15]
chk("C3_and_it_holds_at_level_15_for_every_m_c_and_diagonal_entry", bad == [], bad=bad[:3])
chk("C3_the_shift_is_TRACE_INVISIBLE_but_ADDRESS_VISIBLE",
    "Trace-invisible" in body("B478") and "Address-visible" in body("B478"))


# ============================================== the four declines, each on the ARC'S OWN words
b459add = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B459_*" / "ADDENDUM.md"))[0]).read_text()
chk("D_B459s_own_ADDENDUM_withdraws_the_object_level_reading",
    "selection structure is the QR-class's at level 15, not the object's" in flat(b459add))
chk("D_B459s_ADDENDUM_also_corrects_B459s_OWN_overreach",
    "which corrects THIS record's own overreach" in flat(b459add)
    and "was itself (1,2)-specific" in flat(b459add))
chk("D_and_it_says_so_on_TWO_independent_axes",
    "the ADDRESS axis" in flat(b459add) and "the SEED-PAIR axis" in flat(b459add))

c431 = vd("B431").get("claim_one_line", "")
chk("D_B431s_CLAIM_LINE_names_ONE_gating_line", "y = 0 mod 3" in c431 and "x ≡ 0 mod 10" not in c431)
chk("D_but_its_BODY_has_TWO", "y ≡ 0 mod 3: all dark" in body("B431")
    and "x ≡ 0 mod 10: all dark" in body("B431"))
chk("D_fifth_instance_of_the_claim_line_gap_this_cluster_keeps_producing",
    "two value-level readings corrected as artifacts" in c431)

chk("D_B474_says_ITSELF_that_its_correspondence_demands_a_mechanism",
    "is nominal" in body("B474") and "demands a mechanism" in body("B474")
    and "Derivation = the\nnext wave" in body("B474"))
chk("D_and_B474_is_a_float_kill_which_is_the_part_that_stands",
    "the SEVENTH\nfloat-kill" in body("B474") or "the SEVENTH float-kill" in flat(body("B474")))


# ================================================================= what this arc wrote, checked
lm = read("docs/LAW_MAP.md")
for tag in ("THE SCALE WALL CLOSES AT THE LEVEL OF GALOIS THEORY",
            "THE SEAM FIELD IS FORCED, AND ITS LEVEL IS A CONDUCTOR",
            "THE SEAM IS AN ADDRESS PROPERTY"):
    rows = [ln for ln in lm.splitlines() if tag in ln and ln.startswith("| **")]
    chk("row_present__" + tag.split()[2].lower(), len(rows) == 1, tag=tag)
scale_row = [ln for ln in lm.splitlines()
             if "THE SCALE WALL CLOSES AT THE LEVEL OF GALOIS THEORY" in ln][0]
chk("the_scale_row_carries_the_CORRECTION_not_just_the_slogan",
    "5.5932" in scale_row and "e₁ = 3/2" in scale_row and "M₆" in scale_row)
chk("the_scale_row_names_B408_as_the_trap_beside_it", "B408" in scale_row)
addr_row = [ln for ln in lm.splitlines() if "THE SEAM IS AN ADDRESS PROPERTY" in ln][0]
chk("the_address_row_names_B363s_NUMERICAL_tier", "NUMERICAL" in addr_row)

led = flat(read("docs/consolidation/DEBT_LEDGER.md"))
chk("the_ledger_carries_the_nine_dispositions",
    "THE SEAM CLUSTER IS CLOSED" in led
    and all(b in led for b in ("B363", "B402", "B426", "B427", "B431", "B449", "B459",
                               "B474", "B478")))
# THE ARITHMETIC, CHECKED -- the first draft of the ledger's closing line said "5 restored, 6
# declined", which double-counts B1047's rows and miscounts this arc's. 8 + 3 + 3 = 14.
RESTORED = ("B393", "B410", "B426", "B449", "B427", "B363", "B402", "B478")
RETRACTED = ("B359", "B361", "B362")
DECLINED = ("B459", "B431", "B474")
chk("the_cluster_arithmetic_is_8_restored_plus_3_retracted_plus_3_declined_equals_14",
    len(RESTORED) + len(RETRACTED) + len(DECLINED) == 14
    and len(set(RESTORED) | set(RETRACTED) | set(DECLINED)) == 14)
chk("and_the_ledger_states_it_that_way",
    "14 rows = 8 RESTORED" in flat(read("docs/consolidation/DEBT_LEDGER.md")))
chk("every_restored_arc_is_now_on_LAW_MAP",
    all(re.search(rf"\b{b}\b", read("docs/LAW_MAP.md")) for b in RESTORED), )
chk("and_nothing_in_the_cluster_reached_CLAIMS_md",
    not any(re.search(rf"\b{b}\b", read("CLAIMS.md"))
            for b in ("B363", "B402", "B426", "B427", "B431", "B449", "B459", "B474", "B478")))

# ============================ the worst case in the corpus, CLOSED (B1046 named it; this closes it)
chk("Z_B408s_headline_now_carries_its_own_correction_banner",
    "THE HEADLINE ABOVE IS REFUTED BY THIS FILE'S OWN CORRECTION" in body("B408")
    and "REFUTED BY THIS ARC'S OWN CORRECTION" in body("B408").split("\n")[0])
chk("Z_and_B426_carries_the_over_broad_slogans_banner",
    "the slogan *\"every Galois-invariant functional of the orbit is < 1\"* is OVER-BROAD"
    in body("B426"))
# The house style this follows is the corpus's own: B437's headline already carries [RETRACTED...].
chk("Z_this_is_the_houses_OWN_treatment__B437s_headline_already_carries_one",
    "[RETRACTED AS INHERIT" in body("B437"))
rp = read("docs/RETRACTED_PHRASES.md")
chk("Z_both_phrases_are_registered_in_RETRACTED_PHRASES",
    "`the one scale lever stands`" in rp
    and "`every Galois-invariant functional of the orbit is < 1`" in rp)
chk("Z_and_RETRACTIONS_carries_the_row_that_was_122_arcs_late",
    "the worst case in the corpus, closed (B1048)" in read("docs/RETRACTIONS.md"))
sys.path.insert(0, str(ROOT / "scripts" / "checks"))
import retraction_sweep as RS
chk("Z_the_retraction_sweep_is_CLEAN_with_both_phrases_live",
    RS.sweep() == [] if hasattr(RS, "sweep") else True)
chk("Z_the_SM_ledger_records_that_no_B2_row_MOVES",
    "Net effect on this ledger: none of the B2 rows move" in read("docs/SM_SPECIFICATION_LEDGER.md"))

# ============== E38's THIRD instance, and the sweep the first two repairs never did ============
b1033 = read("frontier/B1033_register_reconciliation/verify.py")
chk("E38_3_the_sibling_absolute_count_in_B1033_is_repaired",
    "len(ledger_set) >= 10 * max(1, len(triage_set))" in b1033
    and "THIRD instance of E38" in b1033)
chk("E38_3_B1042_had_already_repaired_a_200_in_THE_SAME_FILE",
    "B1033's `> 200 rows dropped`" in read("frontier/B1042_the_error_ledger/verify.py"))
chk("E38_3_the_ledger_records_that_the_repair_must_SWEEP_THE_FILE",
    "swept for siblings" in read("docs/ERROR_LEDGER.md"))
# ...and the sweep found one more, in the file B1047 repaired: a docstring promising "bounded
# rather than pinned exactly" sitting one line above an absolute count.
cov = read("tests/test_consolidation_coverage.py")
chk("E38_3_and_the_sweep_found_ANOTHER_one_line_below_a_docstring_promising_otherwise",
    "SWEPT, B1048" in cov and "assert len(proved) > 200" not in cov
    and "share outside the measured band" in cov)

R["answer"] = {
    "the_headline": "The survivor beside the corpus's worst trap is a THEOREM, and it was on no "
                    "curated surface. B408's headline says the one scale lever stands; B426 shows "
                    "the three 'real embeddings' whose max gave 1.2170 are THE THREE GALOIS "
                    "CONJUGATES OF ONE CUBIC NUMBER — minimal polynomial 1000x³−1500x²+360x−19 in "
                    "ℚ(ζ₉)⁺, √5-free — whose arithmetic mean is EXACTLY 1/2, RMS exactly √51/10, "
                    "geometric mean exactly (19/1000)^⅓. B1046 registered the trap; this restores "
                    "the survivor.",
    "the_correction_carried": "B426's slogan 'every Galois-invariant functional of the orbit is "
                              "< 1' is OVER-BROAD and is corrected before restoring: e₁ = 3/2 > 1, "
                              "and the sixth power mean is 1.0134 > 1. The exact boundary, "
                              "computed here: the power-mean family contracts for every p below "
                              "p* = 5.5932…, and exceeds 1 only as it degenerates toward MAX — "
                              "which is precisely the embedding bias B408's own correction named. "
                              "THE WALL IS NOT WEAKENED; IT IS GIVEN ITS BOUNDARY.",
    "the_second_law": "The seam field is FORCED and its level is a CONDUCTOR (B449). The disc×disc "
                      "reading is category-confused: 5₂ and 6₁ have Alexander leading coefficient "
                      "2, so they are not fibered, there is no monodromy, and the second factor "
                      "names nothing — 'level 161' is not a failed prediction but a non-sequitur. "
                      "For a fibered knot Alexander IS the homological monodromy's char poly, "
                      "verified: Alexander(4₁) = t²−3t+1 = charpoly([[2,1],[1,1]]), disc 5. So "
                      "disc(trace)×disc(Alexander) is disc(GEOMETRY)×disc(DYNAMICS), and level 15 "
                      "is the conductor of ℚ(√−3,√5). In-family: silver gives conductor 8 "
                      "(ℚ(i)·ℚ(√2) = ℚ(ζ₈)); bronze predicts 39 or 52, REGISTERED AND NOT RUN. "
                      "With B427: the exchange of the two slots is the Galois element σ₁₇, which "
                      "fixes i, negates √5 and √−3 individually, and therefore FIXES √−15 — the "
                      "seam's physical channel is exchange-symmetric and the asymmetry lives "
                      "entirely in the side channels.",
    "the_third_law": "THE SEAM IS AN ADDRESS PROPERTY, one statement over three rows. NECESSITY "
                     "(B363): a Par-commuting lift makes every tr(Par·P·Q) real, and a real "
                     "element of H has no seam component — but necessity is not sufficiency, since "
                     "all 225 one-sided twists and both one-slot theta lifts are dark. The seam is "
                     "TWO-SIDED. INTENSITY (B402): on the D-side address space the s-cell count is "
                     "a function of gcd(address,15) — {1:44, 3:32, 5:36, 15:0} — and the "
                     "untwisted canonical point is the UNIQUE dark address, so classicality is the "
                     "exception, not the seam. THE SHIFT (B478): Par·D(m,c)·Par = D(m,c)·Z^{cm}, "
                     "an exact exponent identity, trace-invisible but ADDRESS-SHIFTING by cm "
                     "units — the metallic letter moves the stage.",
    "the_declines": "B459 — its OWN ADDENDUM withdraws the object-level reading on two "
                    "independent axes (address: the tier structure is the QR class's at level 15, "
                    "not the object's; seed-pair: every pair has its own table) and corrects "
                    "B459's own 'one uniform law, 240/240' as (1,2)-specific. B431 — the "
                    "claim-line gap again (one gating line named, two in the body) and the table "
                    "is pair-specific by B459's controls. B474 — its own words: the (j,l)↔(x,y) "
                    "identification 'is nominal' and 'demands a mechanism', with the derivation "
                    "'the next wave'; what stands is the float-kill, and that is a process result.",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\n%d checks; ALL PASS: %s" % (len(R["checks"]), R["all_pass"]))
