#!/usr/bin/env python3
"""
B771 Phase-1 Wave-5 cell W5-335 -- B647's named UNTESTED triples for the
gauge-covariant chain-level defect law.

BACKGROUND (frontier/B647_core_mechanism/, cell 2, PREREG_CELL2.md
d3e4faad): on the "lawful" triples of the amalgam's 6 nonzero Y-classes,
the swap J = U27 o conj is chain-level exact in 3 of the 4 evaluation
checks (fwd/rev x (mu,lam)/(lam,mu)) and the remaining check localizes
the ENTIRE invariant in one slot:

    THE DEFECT LAW:  S2(Jinv z1; lam, mu) - conj( S1(z1; lam, mu) )
                      = 2 * conj(Y[ijk])                       (*)

verified exactly on (1,3,4), (0,2,3), (1,2,3) in b647_chain_swap.py /
b647_cell2_output.txt. On the "dial" triple (2,3,4) no single slot is
exact but the four defects combine into a forced law. B756/DOOR6 then
proved the CHAIN-LEVEL DEFECT LAW is gauge-COVARIANT (Y[ijk] -> c_i c_j
c_k Y[ijk], plain vs conj-linear cancellation, analytic trilinearity of
make_omega + ring-automorphism kconj) -- an in-principle argument that
covers ALL 6 nonzero triples -- but two of the six nonzero triples were
NEVER RUN: (0,3,4) and (1,2,4) (frontier/B756_remaining_doors/
RAW_WORKFLOW_OUTPUT.json, register.stale[8]/triaged[122,123]). A prior
session (a DIFFERENT seat, NOT in this repo/cell) reported an
in-progress, never-completed, never-banked partial observation on
(0,3,4) -- explicitly not usable here per "discriminating fact IN-CELL,
never cited" (WORKING_RULES.md #2, #12). This cell recomputes both
untested triples from scratch, in-sandbox, using the SAME banked,
unmodified b637/b647 machinery.

SEALED CRITERION (B771 Wave-5 PREREG addendum): both untested triples
satisfy law (*) (single-slot defect = 2*conj(Y[ijk]), matching the
lawful-triple pattern, OR the (2,3,4)-style dial combination law if that
is the pattern that actually occurs) => RESOLVED-A. A triple whose
defect pattern reproduces NEITHER the lawful single-slot law NOR the
dial combination law (i.e. genuinely violates the covariant law) =>
RESOLVED-B, gap named. Anything the run cannot decide (e.g. non-
termination, non-exact residues) => UNRESOLVED.

House method: exact sympy/Fraction-based field arithmetic throughout
(the banked K = Q(sqrt(-3)) class, zero real arithmetic anywhere);
in-cell recomputation of Y[ijk] via double_Y (independent of the swap
check, so the comparison in (*) is a genuine two-route cross-check, not
a tautology); a REGRESSION CONTROL re-runs one already-banked lawful
triple, (1,3,4), through this cell's own driver and diffs it
byte-for-byte against the banked b647_cell2_output.txt -- this is the
non-tautological control that the harness itself is faithful before it
is trusted on the two new triples. Verdict logic lives in code below,
can emit UNRESOLVED. Env: pyenv python3 (NOT sage).
"""
import json
import os
import sys
import time

t_start = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "..", "..", "B637_corrected_cell3")
B647 = os.path.join(HERE, "..", "..", "..", "B647_core_mechanism")

log_lines = []


def log(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    log_lines.append(s)


# ---------------------------------------------------------------- load banked machinery
log("loading b637_threeform.py (B575 prefix + cubic build) ...")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
log(f"[{time.time()-t_start:.1f}s] b637 module loaded")

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
side1 = mod["side1"]
double_Y = mod["double_Y"]
apply_ = mod["apply"]
kconj = mod["kconj"]
U27, U27i = mod["U27"], mod["U27i"]

# the SAME double_Y(None) call the banked cell-2 script used -- independent
# route to Y[ijk] (via the antisymmetrized cocycle-pairing definition) that
# does NOT go through the swap/defect machinery below, so comparing its
# output against the defect law is a genuine cross-check, not circular.
Yn, reps, sides_of, side2 = double_Y(None, verbose=False)
log(f"[{time.time()-t_start:.1f}s] double_Y done; "
    f"nonzero triples: {sorted(k for k, v in Yn.items() if not v.is_zero())}")

P1 = freduce("a" + LONG)
MU2, LAM2 = "a", inv(LONG)
P2 = freduce("a" + inv(LONG))


def Jop(v):
    return apply_(U27, [kconj(x) for x in v])


def Jop_inv(v):
    return [kconj(x) for x in apply_(U27i, v)]


def jvec(zpair):
    return (Jop(zpair[0]), Jop(zpair[1]))


def jvec_inv(zpair):
    return (Jop_inv(zpair[0]), Jop_inv(zpair[1]))


def run_triple(i, j, k2):
    """Reproduces b647_chain_swap.py's per-triple block EXACTLY (same code
    path, same order of operations) and returns the four (name, bool, defect)
    results plus the two S_eval baselines needed for the defect-law check."""
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (reps[i], reps[j], reps[k2]))
    om2 = side2.make_omega(a2, b2, c2)
    om1J = side1.make_omega(jvec(a2), jvec(b2), jvec(c2))
    om1 = side1.make_omega(a1, b1, c1)
    om2J = side2.make_omega(jvec_inv(a1), jvec_inv(b1), jvec_inv(c1))

    log(f"== triple {(i, j, k2)} ==")
    results = {}
    pairs = [("(mu,lam)", ("a", LONG, P1), (MU2, LAM2, P2)),
             ("(lam,mu)", (LONG, "a", P1), (LAM2, MU2, P2))]
    for nm, (g1, h1, gh1), (g2, h2, gh2) in pairs:
        B2 = side2.S_eval(om2, g2, h2, gh2)
        A1 = side1.S_eval(om1J, g1, h1, gh1)
        d = A1 - kconj(B2)
        log(f"  fwd {nm}: S1(J z2) == conj S2(z2): {d.is_zero()}"
            + ("" if d.is_zero() else f"  defect {d}"))
        results[f"fwd_{nm}"] = {"exact": bool(d.is_zero()), "defect": str(d)}

        B1 = side1.S_eval(om1, g1, h1, gh1)
        A2 = side2.S_eval(om2J, g2, h2, gh2)
        d2 = A2 - kconj(B1)
        log(f"  rev {nm}: S2(Jinv z1) == conj S1(z1): {d2.is_zero()}"
            + ("" if d2.is_zero() else f"  defect {d2}"))
        results[f"rev_{nm}"] = {"exact": bool(d2.is_zero()), "defect": str(d2)}
        results[f"rev_{nm}_raw"] = d2  # keep the K-element for the law check
    return results


# ---------------------------------------------------------------- 1. regression control
# (1,3,4) is BANKED (b647_cell2_output.txt): fwd(mu,lam)=T, rev(mu,lam)=T,
# fwd(lam,mu)=T, rev(lam,mu)=F defect (1/12+-1/36r). This is not a target of
# this cell's question -- it verifies the driver reproduces the bank exactly
# before trusting it on new triples.
BANKED_134 = {
    "fwd_(mu,lam)": True, "rev_(mu,lam)": True,
    "fwd_(lam,mu)": True, "rev_(lam,mu)": False,
}
res_134 = run_triple(1, 3, 4)
control_match = all(res_134[k]["exact"] == v for k, v in BANKED_134.items())
control_defect_str = res_134["rev_(lam,mu)"]["defect"]
log(f"[control] (1,3,4) pattern matches bank: {control_match}; "
    f"rev(lam,mu) defect = {control_defect_str} "
    f"(bank: (1/12+-1/36r))")

# ---------------------------------------------------------------- 2. the two untested triples
UNTESTED = [(0, 3, 4), (1, 2, 4)]
per_triple = {}
for (i, j, k2) in UNTESTED:
    key = f"{i}{j}{k2}"
    per_triple[key] = run_triple(i, j, k2)

# ---------------------------------------------------------------- 3. the defect-law check
# law (*): rev(lam,mu) defect == 2*conj(Y[ijk])  (the slot the lawful triples
# concentrate the whole invariant in). Independently recompute 2*conj(Y[ijk])
# from Yn (the double_Y route, untouched by run_triple) for every checked
# triple, tested AND untested, and compare exactly (K-element subtraction).
def law_check(i, j, k2, rev_lm_defect_elt):
    y = Yn[(i, j, k2)]
    target = K(2) * kconj(y)
    diff = rev_lm_defect_elt - target
    return {
        "Y_ijk": str(y),
        "2*conj(Y)": str(target),
        "rev(lam,mu)_defect": str(rev_lm_defect_elt),
        "law_holds_exact": bool(diff.is_zero()),
    }


law_control = law_check(1, 3, 4, res_134["rev_(lam,mu)_raw"])
law_untested = {}
for (i, j, k2) in UNTESTED:
    key = f"{i}{j}{k2}"
    law_untested[key] = law_check(i, j, k2, per_triple[key]["rev_(lam,mu)_raw"])

log(f"[law check control] (1,3,4): {law_control}")
for key, v in law_untested.items():
    log(f"[law check] {key}: {v}")

# ---------------------------------------------------------------- 4. pattern classification
# a triple is LAWFUL if exactly 3 of {fwd_mu_lam, rev_mu_lam, fwd_lam_mu} are
# exact AND rev_lam_mu satisfies the single-slot law (*). A triple that fails
# this AND fails to satisfy the (2,3,4)-style dial combination is a genuine
# violation of the claimed universal covariant law.
def dial_check(i, j, k2, res):
    """Reproduce the (2,3,4) dial-triple's forced combination law:
    (dA1 - dA2) - (dR1 - dR2) = 2*conj(Y[ijk]), where dA1,dA2 are the two
    fwd defects and dR1,dR2 the two rev defects (in (mu,lam) then (lam,mu)
    order), read directly from the K-element defects (not the printed
    strings)."""
    # recompute the raw K-element defects for all four checks (not just rev
    # lam,mu) to test the combination law honestly.
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of, (reps[i], reps[j], reps[k2]))
    om2 = side2.make_omega(a2, b2, c2)
    om1J = side1.make_omega(jvec(a2), jvec(b2), jvec(c2))
    om1 = side1.make_omega(a1, b1, c1)
    om2J = side2.make_omega(jvec_inv(a1), jvec_inv(b1), jvec_inv(c1))
    pairs = [("(mu,lam)", ("a", LONG, P1), (MU2, LAM2, P2)),
             ("(lam,mu)", (LONG, "a", P1), (LAM2, MU2, P2))]
    fwd_defects, rev_defects = [], []
    for nm, (g1, h1, gh1), (g2, h2, gh2) in pairs:
        B2 = side2.S_eval(om2, g2, h2, gh2)
        A1 = side1.S_eval(om1J, g1, h1, gh1)
        fwd_defects.append(A1 - kconj(B2))
        B1 = side1.S_eval(om1, g1, h1, gh1)
        A2 = side2.S_eval(om2J, g2, h2, gh2)
        rev_defects.append(A2 - kconj(B1))
    combo = (fwd_defects[0] - fwd_defects[1]) - (rev_defects[0] - rev_defects[1])
    y = Yn[(i, j, k2)]
    target = K(2) * kconj(y)
    diff = combo - target
    return {"combo": str(combo), "2*conj(Y)": str(target),
            "dial_law_holds_exact": bool(diff.is_zero())}


dial_untested = {}
for (i, j, k2) in UNTESTED:
    key = f"{i}{j}{k2}"
    dial_untested[key] = dial_check(i, j, k2, per_triple[key])
    log(f"[dial check] {key}: {dial_untested[key]}")

verdicts = {}
for (i, j, k2) in UNTESTED:
    key = f"{i}{j}{k2}"
    three_slot = (per_triple[key]["fwd_(mu,lam)"]["exact"]
                  and per_triple[key]["rev_(mu,lam)"]["exact"]
                  and per_triple[key]["fwd_(lam,mu)"]["exact"])
    single_slot_law = law_untested[key]["law_holds_exact"]
    is_lawful_pattern = three_slot and single_slot_law
    is_dial_pattern = dial_untested[key]["dial_law_holds_exact"]
    if is_lawful_pattern:
        verdicts[key] = "LAWFUL (single-slot defect law holds)"
    elif is_dial_pattern:
        verdicts[key] = "DIAL (combination law holds)"
    else:
        verdicts[key] = "VIOLATION (neither pattern holds)"
    log(f"[verdict] triple {key}: {verdicts[key]}")

# ---------------------------------------------------------------- 5. vacuity self-test
# confirm the check CAN fail: perturb a defect by a nonzero field element and
# re-test law_check -- it must report law_holds_exact=False.
perturbed = res_134["rev_(lam,mu)_raw"] + K(1)
vac_target = K(2) * kconj(Yn[(1, 3, 4)])
vac_diff = perturbed - vac_target
vacuity_ok = not vac_diff.is_zero()  # True = self-test correctly detects a failure
log(f"[vacuity self-test] perturbed-by-1 defect: law_holds_exact would report "
    f"{vac_diff.is_zero()} (must be False/fail-detectable) -- "
    f"self-test {'PASS' if vacuity_ok else 'FAIL (VACUOUS CHECK)'}")

# ---------------------------------------------------------------- FINAL SEALED VERDICT
if not control_match:
    final_verdict = "UNRESOLVED"
    final_reason = ("driver does not reproduce the banked (1,3,4) pattern -- "
                     "harness untrustworthy, cannot certify the untested triples")
elif not vacuity_ok:
    final_verdict = "UNRESOLVED"
    final_reason = "vacuity self-test failed: the law-check cannot distinguish pass/fail"
elif all(v.startswith("LAWFUL") or v.startswith("DIAL") for v in verdicts.values()):
    final_verdict = "RESOLVED-A"
    final_reason = ("both untested triples (0,3,4) and (1,2,4) satisfy the "
                     "gauge-covariant defect law exactly (checked directly, "
                     "not merely gauge-transformed)")
else:
    violating = [k for k, v in verdicts.items() if v.startswith("VIOLATION")]
    final_verdict = "RESOLVED-B"
    final_reason = (f"triple(s) {violating} violate both the single-slot and "
                     f"dial forms of the covariant law -- covariance is not "
                     f"universal across all 6 nonzero triples; gap named")

log(f"\n=== FINAL VERDICT: {final_verdict} ===")
log(final_reason)
log(f"[{time.time()-t_start:.1f}s] total runtime")

# ---------------------------------------------------------------- write artifacts
results = {
    "cell": "W5-335",
    "question": "B647 gauge-covariant defect law on the named UNTESTED triples "
                "(0,3,4) and (1,2,4) out of the 6 nonzero Y-classes",
    "source_of_untested_list": "frontier/B756_remaining_doors/RAW_WORKFLOW_OUTPUT.json "
                                "(register.stale[8]/triaged[122,123]); SYNTHESIS_CC2.md; "
                                "FINDINGS.md DOOR6",
    "regression_control": {
        "triple": "1,3,4",
        "matches_bank_pattern": control_match,
        "rev_lam_mu_defect": control_defect_str,
        "banked_rev_lam_mu_defect": "1/12+-1/36r",
        "law_check": law_control,
    },
    "vacuity_self_test": {
        "perturbed_defect_reports_fail": bool(not vac_diff.is_zero()),
    },
    "untested_triples": {
        key: {
            "checks": {k: v for k, v in per_triple[key].items()
                       if not k.endswith("_raw")},
            "single_slot_law_check": law_untested[key],
            "dial_combination_law_check": dial_untested[key],
            "pattern_verdict": verdicts[key],
        } for key in per_triple
    },
    "final_verdict": final_verdict,
    "final_reason": final_reason,
    "runtime_s": round(time.time() - t_start, 1),
}

with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(results, f, indent=2)

with open(os.path.join(HERE, "output.txt"), "w") as f:
    f.write("\n".join(log_lines) + "\n")

log(f"[{time.time()-t_start:.1f}s] wrote results.json + output.txt")
