"""B1031 — the generation thread, collected: what is banked, what is graded, and the missing rung.

Occasioned by the owner's belief that *"we derive three generations"*. Every check below reads a
banked `arc_verdict.json` or a curated surface. No mathematics is asserted here; the arcs did it.

The finding this exists to pin: **`THE_LADDER.md` — the document whose stated purpose is "what the
programme does not yet contain, as rungs to climb", with the binding rule *"before saying 'the
object does not provide X', find X on this ladder; if X is not on it, X has not been checked"* —
contained the word "generation" ZERO times**, while 51 arcs mention generations in their verdicts,
including a banked NEGATIVE, a promoted THEOREM (P54), a positive cohomological count, and a WALL.
"""
import glob
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **detail):
    R["checks"][name] = {"pass": bool(ok), **detail}
    return ok


def verdict(bid):
    for p in glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json")):
        d = json.loads(pathlib.Path(p).read_text())
        return d.get("verdict"), (d.get("claim_one_line") or "")
    return None, ""


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def flat(s):
    return re.sub(r"\s+", " ", s.replace("\n> ", "\n"))


CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]

# ---------------------------------------------------- 1. the thread, arc by arc, from verdicts
THREAD = {
    "B298": ("NEGATIVE", "degree-2 trace field gives multiplicity 1 or 2, never 3 — seven routes"),
    "B302": ("PROVED", "the order-3 lives in the COMMENSURATOR as a hidden symmetry — located, not derived"),
    "B307": ("PROVED", "no hyperbolic knot has a cyclic-cubic trace field — the single-object route CLOSED"),
    "B335": ("PROVED", "the generation Z/3 is a deck transformation, hence an isometry: the three sheets are EXACTLY degenerate"),
    "B414": ("NEGATIVE", "the Z/3-generations reading fails its privilege test; core multiplicity is Z/2"),
    "B632": ("PROVED", "h1(M;27_rho) = 3 exactly over Q(omega) — a graded three-slot structure, NOT blocked by B307"),
    "B897": ("PROVED", "sealed: the 27 splits into three 9-blocks; su(3)' is a native flavor symmetry"),
    "B928": ("PROVED", "D2 carries the hierarchy; the eleven-sign twist, not the matter"),
}
for bid, (want, _) in THREAD.items():
    got, claim = verdict(bid)
    chk(f"verdict_{bid}_is_{want}", got == want, got=got, claim=claim[:200])

# The two that decide how strong the positive may be stated.
_, c632 = verdict("B632")
chk("b632_computes_h1_equals_three", "h¹(M;27_ρ)=3" in c632 or "h¹(M;27" in c632, claim=c632[:200])
_, c307 = verdict("B307")
chk("b307_closes_the_single_object_route",
    "closing the single-knot route to three symmetric generations" in c307)
_, c335 = verdict("B335")
chk("b335_makes_the_three_sheets_exactly_degenerate",
    "exactly degenerate" in c335 and "hierarchy is its breaking" in c335)

# ------------------------------------- 2. how the curated surfaces GRADE it (the decisive words)
claim = read("docs/THE_CLAIM.md")
chk("the_claim_grades_the_generation_structure_STRUCTURAL",
    re.search(r"the generation structure.*?\|\s*\*\*STRUCTURAL\*\*", flat(claim)) is not None)
chk("the_claim_defines_STRUCTURAL_as_a_named_debt",
    "A STRUCTURAL grade is a named debt inside a closed proof" in flat(claim))
# and DERIVED is reserved for other rows on the same table
chk("the_claim_reserves_DERIVED_for_z6_and_hypercharge",
    "**DERIVED** | B862" in flat(claim) and "**DERIVED / CLOSED** | B864" in flat(claim))

fw = read("docs/THE_FRAMEWORK.md")
chk("the_framework_says_three_generations_STRUCTURALLY",
    "three generations, structurally" in fw)
spec = read("docs/SM_SPECIFICATION_LEDGER.md")
chk("the_spec_ledger_grades_it_structural_count_matches",
    "**structural, count matches**" in spec)
chk("the_spec_ledger_marks_the_orbit_generation_bijection_unverified",
    "orbit↔generation bijection (solo, unverified)" in spec)

# --------------------------- 3. the circularity that must be declared, in the record's own words
chk("registerable_is_defined_as_the_generation_structure_surviving",
    "registerable means the 27's generation structure survives" in flat(fw))
lm = read("docs/LAW_MAP.md")
chk("b994_states_registerability_IS_chirality_an_input_the_object_lacks",
    "registerable = the generation stays chiral" in flat(lm)
    and "the endpoint is forced by an input the object does not have" in flat(lm))

# ------------------------------------------------- 4. the typing wall — the limit on the positive
chk("the_typing_wall_zeroes_the_coupling_for_identical_families",
    "zero coupling for identical families" in flat(lm))

# --------------------------------------------------------------- 5. THE FINDING: the missing rung
ladder = read("docs/THE_LADDER.md")
chk("the_ladder_states_its_binding_rule",
    'before saying "the object does not provide X", find X on this ladder' in flat(ladder))
chk("the_ladder_now_carries_a_generation_rung", "generation" in ladder.lower())
chk("the_generation_rung_is_X33_in_the_BOUNDED_section",
    re.search(r"\*\*X33\*\*.*generation", flat(ladder)) is not None)
# it must carry BOTH halves — the positive and the theorem that bounds it
gen_rung = re.search(r"\*\*X33\*\*.*?\n", flat(ladder) + "\n")
gr = gen_rung.group(0) if gen_rung else ""
for token in ("B632", "B307", "B897", "B335", "B298"):
    chk(f"the_rung_cites_{token}", token in gr)

# how many arcs actually speak to it — the size of what the ladder was silent about
n = 0
for p in sorted(glob.glob(str(ROOT / "frontier" / "B*" / "arc_verdict.json"))):
    if re.search(r"generation", json.loads(pathlib.Path(p).read_text()).get("claim_one_line") or "",
                 re.I):
        n += 1
chk("the_thread_is_large_not_a_stray_mention", n > 40, arcs_mentioning_generations=n)

# B302 — the arc that LOCATES the Z/3 — was on no curated surface at all.
# SCOPED, for the second time in two arcs: the X33 rung this arc writes CITES B302, so an
# unscoped search would report "carried" because the finding was recorded. Measured against the
# curated surfaces with this arc's own rung removed. (B1030 hit the identical hazard; recording it
# twice is the point — a metric invalidated by its own output is the shape of the coverage error
# this refresh already had to retract.)
without_x33 = "\n".join(
    re.sub(r"\|\s*\*\*X33\*\*.*", "", read(p)) for p in CURATED)
chk("b302_was_carried_by_no_curated_surface_before_this_rung",
    not (re.search(r"\bB302\b", without_x33) or re.search(r"B302_", without_x33)))
chk("b302_is_now_cited_by_the_new_rung", "B302" in read("docs/THE_LADDER.md"))

R["arcs_mentioning_generations"] = n
R["answer"] = {
    "derived": "NO. The programme's own one-page claim grades the generation structure "
               "**STRUCTURAL**, which it defines as 'a named debt inside a closed proof' — the "
               "grade it reserves from DERIVED (the ℤ₆ form, the hypercharge direction) and "
               "THEOREM (termination). SM_SPECIFICATION_LEDGER grades it 'structural, count "
               "matches', with the orbit↔generation bijection marked UNVERIFIED.",
    "what_is_banked": "Three-ness appears twice, honestly: B632 computes h¹(M;27_ρ) = 3 exactly "
                      "over ℚ(ω) — a graded three-slot cohomological structure, explicitly NOT "
                      "blocked by B307 — and B897's sealed cell splits the 27 into three 9-blocks "
                      "with su(3)' acting as a native flavor symmetry. B335 adds that the "
                      "generation ℤ/3 is a deck transformation, hence an ISOMETRY: the three "
                      "sheets are exactly degenerate and a hierarchy is its BREAKING.",
    "what_is_closed": "B298 (NEGATIVE): the object's degree-2 trace field gives multiplicity 1 or "
                      "2 across seven routes, never 3. B307 (THEOREM, promoted to P54): no "
                      "hyperbolic knot has a cyclic-cubic trace field, so a symmetric "
                      "three-generation triple is arithmetically impossible in a SINGLE hyperbolic "
                      "knot — the three must be relational (B302: the commensurator's hidden ℤ/3, "
                      "which LOCATES it and does not derive it).",
    "the_circularity_to_declare": "The cascade's selection principle is 'maximal residual symmetry "
                                  "among REGISTERABLE options', and registerable is DEFINED as 'the "
                                  "27's generation structure survives' — B994: 'registerable = the "
                                  "generation stays chiral … the endpoint is forced by an input the "
                                  "object does not have.' So generation structure is partly a "
                                  "FILTER ON the cascade, not solely an output of it.",
    "the_wall": "The typing wall (1′): an alternating family tensor ⊗ the symmetric E₆ cubic = "
                "ZERO coupling for identical families. Three slots exist; a Yukawa-type family "
                "tensor at that level does not.",
    "the_defect": "THE_LADDER — 'what the programme does not yet contain', binding rule 'if X is "
                  "not on it, X has not been checked' — contained the word 'generation' ZERO "
                  "times, while 51 arcs speak to it. Repaired here as rung X33 (BOUNDED).",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
