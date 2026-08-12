"""B1050 — the projective quotient is fully natural, and still not a selector.

SIX ARCS FOUND THE SAME WALL SEPARATELY AND NO CURATED SURFACE SAYS SO. B19, B21, B28, B30, B34 and
B35 each establish a different half of one fact -- that the projective / central-sign quotient of the
trace-map state space is sound in every sense one could ask for:

    B28  it is LEGITIMATE      the trace map is equivariant under the central sign action, and the
                               Fricke-Vogt invariant is preserved by it (but NOT by the antipodal map)
    B30  it is CANONICAL       the map descends polynomially to (u,v,w,r) = (x^2, y^2, z^2, xyz)
    B34  it is NATURAL         the sign action is Poisson for the Fricke-Goldman bracket
    B21  it is SYMPLECTIC      the half-step is ANTI-Poisson; its square is Poisson
    B35  it is TOPOLOGICAL     the sign action has order 3 over F_2, which is the period-3 return
    B19  its generator is PINNED  three inequivalent-looking conditions all give exactly {P, -P}

AND EVERY ONE OF THEM CARRIES THE VERDICT `STALLED`, because none of it derives the selector.

  B30: "It still does not select I=1/4; every value of c^2 has the same projective period-3 return."
  B34: "Goldman/WP naturality supports the quotient but does not derive the selector."
  B35: "Topology/lift-sign data explains the order-3 projective behavior, but it does not derive it."
  B28: "the decision to use that quotient as the selector remains a bridge criterion, not something
        derived from A1-A7."
  B19: "this condition itself is not derived from A1-A6."

THE SIXTH IS A DIFFERENT WALL AND IS NOT LUMPED WITH THEM. B21's negative is about SPACETIME --
"the natural symplectic dictionary exists; the physical spacetime dictionary does not" -- not about
the selector. It is in this row for the Poisson structure it establishes, and its own negative is
stated separately. Merging the two would be the error B1045 measured at 9 %.

RE-VERIFIED HERE BEFORE RESTORING (campaign step 5), and one correction was forced en route: the
invariant these arcs preserve is the TRACE-MAP normalisation I = x^2+y^2+z^2-2xyz-1, not the Markov
form x^2+y^2+z^2-xyz. A first pass used the latter, and the T-invariance check failed -- which is the
E1 convention collision the corpus already tracks, met live.
"""
import glob
import json
import pathlib
import re

import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def body(bid):
    return pathlib.Path(glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "FINDINGS.md"))[0]
                        ).read_text(encoding="utf-8")


def vd(bid):
    return json.loads(pathlib.Path(
        glob.glob(str(ROOT / "frontier" / f"{bid}_*" / "arc_verdict.json"))[0]).read_text())


def flat(s):
    return re.sub(r"\s+", " ", s)


x, y, z, c = sp.symbols("x y z c")
V = (x, y, z)

# The trace map and the central sign action, in the coordinates B28/B30 use.
T = (z, x, sp.expand(2 * x * z - y))
S = lambda sa, sb: (sa * x, sb * y, sa * sb * z)
# THE FRICKE-VOGT INVARIANT, TRACE-MAP NORMALISATION. See the module docstring: the Markov form
# x^2+y^2+z^2-xyz is NOT preserved by T, and a first pass used it. Two normalisations of one name.
I = x ** 2 + y ** 2 + z ** 2 - 2 * x * y * z - 1


def sub(F, e):
    return sp.expand(e.subs(dict(zip(V, F)), simultaneous=True))


def jac(F):
    return sp.Matrix([[sp.diff(f, v) for v in V] for f in F])


SIGNS = [(a, b) for a in (1, -1) for b in (1, -1)]

# ======================================================= 0. the wall is the ARCS' OWN VERDICT
WALL = ("B19", "B21", "B28", "B30", "B34", "B35")
for b in WALL:
    chk(f"{b}_body_verdict_token_is_STALLED", "**`STALLED`**" in body(b))
    chk(f"{b}_metadata_says_PROVED_which_is_the_L166_mismatch", vd(b).get("verdict") == "PROVED")
# FIVE of the six name the SELECTOR. The sixth names a different wall and is kept separate.
SELECTOR = {
    "B30": "It still does not select `I=1/4`",
    "B34": "does not derive the selector",
    "B35": "it does not derive the selector",
    "B28": "not something derived from A1-A7",
    "B19": "this condition itself is not derived from A1-A6",
}
for b, phrase in SELECTOR.items():
    chk(f"{b}_says_it_does_not_derive_the_selector", phrase in flat(body(b)), phrase=phrase)
chk("B21s_negative_is_a_DIFFERENT_WALL__spacetime_not_the_selector",
    "the physical spacetime dictionary does not" in flat(body("B21"))
    and "does not derive the selector" not in flat(body("B21"))
    and "select `I=1/4`" not in flat(body("B21")))

# ============================================== 1. LEGITIMATE (B28) — equivariance and the control
chk("B28_the_trace_map_is_EQUIVARIANT_under_the_central_sign_action",
    all(tuple(sp.expand(a - b) for a, b in zip(sub(S(sa, sb), sp.Matrix(T)) if False else
                                               [sub(S(sa, sb), t) for t in T],
                                               [sp.expand(e.subs(dict(zip(V, T)), simultaneous=True))
                                                for e in S(sa * sb, sa)])) == (0, 0, 0)
        for sa, sb in SIGNS))
chk("B28_the_Fricke_Vogt_invariant_is_S_INVARIANT",
    all(sp.expand(sub(S(sa, sb), I) - I) == 0 for sa, sb in SIGNS))
# THE CONTROL, and it is what makes the quotient a quotient rather than a convenience: the global
# antipodal map does NOT preserve the invariant, so B26's flip is a central-lift ambiguity and not
# an arbitrary sign change.
chk("B28_CONTROL__the_ANTIPODAL_map_does_NOT_preserve_it",
    sp.expand(I.subs({x: -x, y: -y, z: -z}, simultaneous=True) - I) != 0,
    antipodal_image=str(sp.expand(I.subs({x: -x, y: -y, z: -z}, simultaneous=True))))
p3 = (0, 0, c)
for _ in range(3):
    p3 = tuple(sp.expand(e.subs(dict(zip(V, p3)), simultaneous=True)) for e in T)
chk("B28_upstairs_T_cubed_of_(0,0,c)_is_(0,0,-c)", p3 == (0, 0, -c), image=str(p3))
chk("B28_and_S(1,-1)_realises_exactly_that_flip",
    tuple(sp.expand(e.subs({x: 0, y: 0, z: c}, simultaneous=True)) for e in S(1, -1)) == (0, 0, -c))

# ================================================== 2. CANONICAL (B30) — the polynomial descent
u, v, w, r = x ** 2, y ** 2, z ** 2, x * y * z
img = [sp.expand(e) for e in T]
chk("B30_the_descent_to_(u,v,w,r)_reproduces_the_trace_map_EXACTLY",
    (sp.expand(img[0] ** 2 - w), sp.expand(img[1] ** 2 - u),
     sp.expand(img[2] ** 2 - (4 * u * w - 4 * r + v)),
     sp.expand(img[0] * img[1] * img[2] - (2 * u * w - r))) == (0, 0, 0, 0))
chk("B30_the_quotient_coordinates_satisfy_r_squared_equals_uvw",
    sp.expand(r ** 2 - u * v * w) == 0)
step = lambda q: (q[2], q[0], sp.expand(4 * q[0] * q[2] - 4 * q[3] + q[1]),
                  sp.expand(2 * q[0] * q[2] - q[3]))
o1 = step((0, 0, c ** 2, 0)); o2 = step(o1); o3 = step(o2)
chk("B30_the_half_return_is_a_LITERAL_period_3_orbit_downstairs",
    (o1, o2, o3) == ((c ** 2, 0, 0, 0), (0, c ** 2, 0, 0), (0, 0, c ** 2, 0)))

# ====================================== 3. NATURAL and SYMPLECTIC (B34, B21) — the Poisson half
def nambu(f, g):
    gI = sp.Matrix([sp.diff(I, t) for t in V])
    return sp.expand(gI.dot(sp.Matrix([sp.diff(f, t) for t in V]).cross(
        sp.Matrix([sp.diff(g, t) for t in V]))))


chk("the_bracket_is_the_one_the_invariant_determines",
    (nambu(x, y), nambu(y, z), nambu(z, x))
    == (sp.expand(-2 * x * y + 2 * z), sp.expand(2 * x - 2 * y * z), sp.expand(-2 * x * z + 2 * y)))
chk("I_is_a_CASIMIR_by_construction", all(nambu(I, t) == 0 for t in V))
PAIRS = ((x, y), (y, z), (z, x))
T2 = tuple(sub(T, e) for e in T)
# B21's MECHANISM, made exact: anti-Poisson BECAUSE orientation-reversing. For a map preserving the
# invariant, the bracket transforms by det(DF) -- so the sign of the determinant IS the statement.
chk("B21_det_DT_is_MINUS_ONE__orientation_reversing", sp.simplify(jac(T).det()) == -1)
chk("B21_the_half_step_is_ANTI_Poisson_on_every_generator_pair",
    all(sp.expand(nambu(sub(T, f), sub(T, g)) + sub(T, nambu(f, g))) == 0 for f, g in PAIRS))
chk("B21_det_DT_squared_is_PLUS_ONE", sp.simplify(jac(T2).det()) == 1)
chk("B21_so_the_A_level_map_is_POISSON_on_every_generator_pair",
    all(sp.expand(nambu(sub(T2, f), sub(T2, g)) - sub(T2, nambu(f, g))) == 0 for f, g in PAIRS))
chk("B34_the_central_sign_action_is_POISSON_for_every_sign_pair",
    all(sp.expand(nambu(sub(S(sa, sb), f), sub(S(sa, sb), g)) - sub(S(sa, sb), nambu(f, g))) == 0
        for sa, sb in SIGNS for f, g in PAIRS))
chk("B34_and_every_sign_map_has_determinant_ONE__which_is_why",
    all(sp.simplify(jac(S(sa, sb)).det()) == 1 for sa, sb in SIGNS))

# ============================================================= 4. TOPOLOGICAL (B35) — the F_2 route
f2 = lambda s: ((s[0] + s[1]) % 2, s[0])
NZ = [(0, 1), (1, 0), (1, 1)]
chk("B35_the_sign_action_has_ORDER_3_on_the_nonzero_F2_characters",
    all(f2(f2(f2(s))) == s for s in NZ) and {f2(s) for s in NZ} == set(NZ)
    and f2((0, 0)) == (0, 0))
chk("B35_and_they_form_a_single_3_cycle",
    [(0, 1), f2((0, 1)), f2(f2((0, 1)))] == [(0, 1), (1, 0), (1, 1)])

# ================================================== 5. THE GENERATOR IS PINNED (B19) — exactly ±P
L = sp.Matrix([[1, 1], [0, 1]]); Rm = sp.Matrix([[1, 0], [1, 1]]); A = L * Rm
P = sp.Matrix([[0, 1], [1, 0]]); E = sp.eye(2)


def box(pred, B=2):
    out = set()
    for a in range(-B, B + 1):
        for b in range(-B, B + 1):
            for d in range(-B, B + 1):
                for e in range(-B, B + 1):
                    X = sp.Matrix([[a, b], [d, e]])
                    if X.det() == 0:
                        continue
                    if pred(X):
                        out.add(sp.ImmutableMatrix(X))
    return out


s1 = box(lambda X: X * X == E and sp.simplify(X * L * X.inv() - Rm) == sp.zeros(2, 2))
s2 = box(lambda X: X * X == E and sp.simplify(X * A * X.inv() - Rm * L) == sp.zeros(2, 2))
s3 = box(lambda X: sp.simplify((L * X) ** 2 - A) == sp.zeros(2, 2))
chk("B19_the_three_conditions_have_IDENTICAL_solution_sets", s1 == s2 == s3)
chk("B19_and_that_set_is_exactly_P_and_minus_P",
    s1 == {sp.ImmutableMatrix(P), sp.ImmutableMatrix(-P)})
weak = box(lambda X: sp.simplify(X * L * X.inv() - Rm) == sp.zeros(2, 2))
chk("B19_while_the_WEAK_form_leaves_many_in_the_same_box", len(weak) > 2, n=len(weak))
chk("B19_states_its_own_caveat__the_condition_is_NOT_derived_from_the_axioms",
    "this condition itself is not derived from A1-A6" in flat(body("B19")))

# ======================================================================= 6. THE WALL ITSELF
# The sharp form, and it is PROVED rather than sampled: the quotient's period-3 return holds for
# SYMBOLIC c, so the quotient carries no information whatever about the invariant's value.
chk("THE_WALL__the_period_3_return_holds_for_SYMBOLIC_c_not_sampled_values",
    step(step(step((0, 0, c ** 2, 0)))) == (0, 0, c ** 2, 0))
chk("...and_for_particular_values_too_as_a_sanity_check",
    all(step(step(step((0, 0, k ** 2, 0)))) == (0, 0, k ** 2, 0)
        for k in (sp.Integer(1), sp.Rational(1, 2), sp.Integer(7))))
# What the selector WOULD have to pick out, made concrete: on the B26 line the invariant is c^2 - 1,
# so I = 1/4 is the single value c^2 = 5/4 -- and nothing in the quotient can see it.
Iline = sp.expand(I.subs({x: 0, y: 0, z: c}))
chk("the_invariant_on_the_B26_line_is_c_squared_minus_one", sp.expand(Iline - (c ** 2 - 1)) == 0)
chk("so_I_equals_one_quarter_is_the_single_value_c_squared_equals_five_quarters",
    sp.solve(sp.Eq(Iline, sp.Rational(1, 4)), c ** 2) == [sp.Rational(5, 4)])
chk("B30_states_exactly_this__every_value_of_c_squared_has_the_same_return",
    "every value of `c^2` has the same projective period-3 return" in flat(body("B30")))

# ================================================================= 7. what this arc wrote
lm = read("docs/LAW_MAP.md")
rows = [ln for ln in lm.splitlines()
        if "THE PROJECTIVE QUOTIENT IS FULLY NATURAL AND STILL NOT A SELECTOR" in ln]
chk("LAW_MAP_carries_the_wall_as_one_row", len(rows) == 1)
row = rows[0] if rows else ""
chk("the_row_is_graded_WALL", "**WALL**" in row)
chk("the_row_carries_STALLED_visibly_so_no_reader_meets_it_as_a_positive", "STALLED" in row)
chk("the_row_keeps_B21s_negative_SEPARATE", "spacetime" in row.lower())
chk("the_row_states_the_scope__does_not_DERIVE_a_selector_not_none_EXISTS",
    "no selector exists" in row and "not" in row)
# B27 is STALLED too and is deliberately NOT in this row -- its content is tower material.
chk("B27_is_STALLED_but_is_NOT_in_this_row",
    "**`STALLED`**" in body("B27") and "B27" not in row)
chk("B27s_content_is_the_SL3_trace_lift_not_the_quotient",
    "SL(3)" in vd("B27").get("claim_one_line", ""))

# TIGHTENED, and the reason is that the loose form PASSED BEFORE THE SECTION WAS WRITTEN. The
# ledger already contains the string "B0-B99" (its v3 by-band baseline table) and each of the six
# B-numbers (its per-row candidate table), so `"B0-B99" in led` and `all(b in led)` were satisfied
# by text this arc did not author -- a check that cannot fail is not a check. Anchored on the
# section heading this arc writes, and on the six appearing INSIDE it.
led = read("docs/consolidation/DEBT_LEDGER.md")
SEC = "### §B0–B99 — DISPOSITIONED"
chk("the_ledger_carries_the_B0_B99_DISPOSITION_section", SEC in led)
section = led.split(SEC, 1)[1] if SEC in led else ""
chk("and_names_the_six_restored_here_INSIDE_that_section", all(b in section for b in WALL))
chk("...and_marks_the_by_band_table_as_the_v3_BASELINE_not_a_live_count",
    "the v3 BASELINE, not a live count" in led)
chk("nothing_in_this_row_reached_CLAIMS_md",
    not any(re.search(rf"\b{b}\b", read("CLAIMS.md")) for b in WALL))

# ============================== 8. L166 — measured precisely, because the first count was loose
import subprocess as _sp
def _body_token(bid):
    """The arc's OWN verdict, read from the window that follows its `## Verdict` heading.

    Two forms are in use and both must be handled: a fenced block (`NEEDS_VALIDATION`) and a
    bold-backtick line (**`STALLED`**). ANCHORING ON THE HEADING is what makes this precise -- a
    free-floating bold match is how a first pass produced two artifacts (B823, B1026 have no
    verdict block at all, and incidental bold text was read as one). No heading, no token.
    """
    b = body(bid)
    m = re.search(r"^##\s*Verdict\s*$", b, re.M)
    if not m:
        return None
    window = b[m.end():m.end() + 400]
    m2 = re.search(r"```(?:text)?\s*\n([A-Z][A-Z0-9_\-]+)", window) \
        or re.search(r"\*\*`([A-Z][A-Z0-9_\-]+)`\*\*", window)
    return m2.group(1) if m2 else None

STALLED12 = [13, 14, 16, 18, 19, 21, 27, 28, 30, 33, 34, 35]
NEEDS2 = [48, 50]
chk("L166_twelve_arcs_body_verdict_is_STALLED",
    all(_body_token(f"B{n}") == "STALLED" for n in STALLED12), n=len(STALLED12))
chk("L166_and_two_read_NEEDS_VALIDATION",
    all(_body_token(f"B{n}") == "NEEDS_VALIDATION" for n in NEEDS2))
chk("L166_all_fourteen_carry_PROVED_in_metadata",
    all(vd(f"B{n}").get("verdict") == "PROVED" for n in STALLED12 + NEEDS2))
chk("L166_all_fourteen_are_in_B0_B99", all(n < 100 for n in STALLED12 + NEEDS2))
# THE CORRECTION: the positive-vocabulary tokens are NOT contradictions, and a first count of 24
# lumped them in. Checked, so the registry's number cannot drift back to the loose one.
POSITIVE = {"B51": "PRODUCES-PROOF-MODULE", "B54": "PRODUCES-PROOF-MODULE",
            "B55": "PRODUCES-PROOF-MODULE", "B57": "PRODUCES-PROOF-MODULE",
            "B59": "RESOLVED", "B60": "PRODUCES-RESULT", "B62": "CONFIRMED",
            "B63": "PROVES", "B64": "PROVEN"}
chk("L166_the_nine_POSITIVE_vocabulary_arcs_are_NOT_contradictions",
    all(_body_token(b) and _body_token(b).startswith(v.split("-")[0]) for b, v in POSITIVE.items()),
    tokens={b: _body_token(b) for b in POSITIVE})
chk("L166_and_the_two_regex_ARTIFACTS_have_no_verdict_block_at_all",
    _body_token("B823") is None and _body_token("B1026") is None)
# THE SHARP EDGE, and it lands on this refresh's own output.
AFTER = re.compile(r"\bB1050\b|\bB10[5-9]\d\b")
import importlib.util as _ilu
_s = _ilu.spec_from_file_location("_mb", ROOT / "scripts" / "checks" / "md_blocks.py")
_MB = _ilu.module_from_spec(_s); _s.loader.exec_module(_MB)
CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]
pre = "\n".join(_MB.drop_blocks(read(p), AFTER) for p in CURATED)
curated14 = [n for n in STALLED12 + NEEDS2
             if re.search(rf"\bB{n}\b", pre) or re.search(rf"B{n}_", pre)]
chk("L166_SIX_of_the_fourteen_are_ALREADY_on_a_curated_surface",
    sorted(curated14) == [13, 14, 16, 18, 33, 48], curated=sorted(curated14))
chk("L166_and_FOUR_of_those_were_put_there_by_THIS_REFRESH_via_B1026",
    all(re.search(rf"\bB{n}\b", [ln for ln in read("docs/LAW_MAP.md").splitlines()
                                  if "THE ONE INVOLUTION (B1026)" in ln][0])
        for n in (13, 14, 16, 18)))
chk("L166_is_registered_with_the_corrected_count",
    "FOURTEEN ARCS SAY `PROVED`" in read("docs/OPEN_LEADS.md")
    and "The first count was 24 and it was wrong" in read("docs/OPEN_LEADS.md"))
chk("L166_prices_the_decision_and_does_NOT_build_a_gate",
    "Deliberately not built here" in read("docs/OPEN_LEADS.md")
    and not (ROOT / "scripts" / "checks" / "verdict_consistency.py").exists())

R["answer"] = {
    "the_finding": "Six arcs found the same wall separately, and no curated surface said so. The "
                   "projective / central-sign quotient of the trace-map state space is LEGITIMATE "
                   "(B28: the map is equivariant under the sign action and the Fricke-Vogt "
                   "invariant is preserved by it but NOT by the antipodal map), CANONICAL (B30: it "
                   "descends polynomially to (u,v,w,r) = (x², y², z², xyz)), NATURAL (B34: the sign "
                   "action is Poisson), SYMPLECTIC (B21: the half-step is anti-Poisson, its square "
                   "Poisson), TOPOLOGICAL (B35: the sign action has order 3 over F₂, which IS the "
                   "period-3 return) and its generator is PINNED (B19: three inequivalent-looking "
                   "conditions all give exactly ±P). Every one of the six carries the verdict "
                   "STALLED, because none of it derives the selector.",
    "the_wall_stated_sharply": "The quotient carries NO information about the invariant's value. "
                               "B30's control is the proof: the period-3 return holds for SYMBOLIC "
                               "c, not merely for sampled values — verified here symbolically. On "
                               "the B26 line the invariant is c² − 1, so I = 1/4 is the single "
                               "value c² = 5/4, and nothing in the quotient can distinguish it.",
    "the_scope_that_travels": "The wall is 'does not DERIVE the selector', NOT 'no selector "
                              "EXISTS'. Six routes to naturality all stop in the same place; that "
                              "is a statement about these routes, and it is what makes an eighth "
                              "attempt at the same route wasted rather than impossible.",
    "the_sixth_is_a_different_wall": "B21's negative is about SPACETIME — 'the natural symplectic "
                                     "dictionary exists; the physical spacetime dictionary does "
                                     "not' — and not about the selector. It is in this row for the "
                                     "Poisson structure it establishes, and its own negative is "
                                     "stated separately. Merging them would be the keyword error "
                                     "B1045 measured at 9 %.",
    "the_correction_forced_en_route": "The invariant these arcs preserve is the TRACE-MAP "
                                      "normalisation I = x²+y²+z²−2xyz−1, not the Markov form "
                                      "x²+y²+z²−xyz. A first pass used the latter and the "
                                      "T-invariance check failed — the E1 convention collision the "
                                      "corpus already tracks, met live rather than read about.",
    "the_mechanism_made_exact": "B21 says the half-step is anti-Poisson 'because it is "
                                "orientation-reversing'. Made exact here: for a map preserving the "
                                "invariant, the bracket transforms by det(DF), so the SIGN OF THE "
                                "DETERMINANT IS THE STATEMENT — det DT = −1, det DT² = +1, and "
                                "det DS = +1 for all four sign pairs, which is why the sign action "
                                "is Poisson and the quotient descends.",
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\n%d checks; ALL PASS: %s" % (len(R["checks"]), R["all_pass"]))
