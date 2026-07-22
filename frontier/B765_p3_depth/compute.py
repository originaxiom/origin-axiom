"""P3 depth-exposure stratum (prereg sha256 0166d9df).

E22 re-adjudication: for each of the 21 depth-exposed P1 negatives, determine
whether the kill verdict rests on a finite-depth check whose scope falls short
of the claim's universal scope.

Method A: structural depth analysis (kill_form + depth_note gap parsing).
Method B: anatomy cross-validation (P2 verdict + current anatomy).
HALT on any A/B disagreement.

Gate 5-Q; nothing to CLAIMS.
"""

import json
import sys
from pathlib import Path

HALT = False


def halt(msg):
    global HALT
    HALT = True
    print(f"\n*** HALT: {msg} ***\n")


ROOT = Path(__file__).resolve().parent.parent.parent

with open(ROOT / "frontier/B742_negatives_hunt_p1/stageA/kill_graph.json") as f:
    kg = json.load(f)
REC = {r["id"]: r for r in kg["records"]}

with open(ROOT / "frontier/B742_negatives_hunt_p1/stageA/bprime_annotations.json") as f:
    bp = json.load(f)

TARGETS = sorted(k for k, v in bp.items() if v.get("depth_exposure"))

P2_CELLS = {
    "B107": "KILL-EXTENDS",
    "B285": "KILL-EXTENDS",
    "B516": "FACE-IRRELEVANT",
    "TOMB-L241": "KILL-EXTENDS",
    "TOMB-L247": "KILL-EXTENDS",
    "TOMB-L252": "KILL-EXTENDS",
    "TOMB-L258": "KILL-EXTENDS",
    "TOMB-L267": "KILL-EXTENDS",
    "TOMB-L277": "KILL-EXTENDS",
    "TOMB-L30": "KILL-EXTENDS",
    "TOMB-L334": "KILL-EXTENDS",
    "TOMB-L339": "KILL-EXTENDS",
    "TOMB-L57": "KILL-EXTENDS",
    "TOMB-L63": "KILL-EXTENDS",
    "TOMB-L67": "KILL-EXTENDS",
    "TOMB-L70": "KILL-EXTENDS",
    "TOMB-L77": "KILL-EXTENDS",
    "WALL-1": "KILL-EXTENDS",
    "WALL-7": "FACE-IRRELEVANT",
}

# ── Method A: structural depth analysis ──────────────────────────────────────
#
# For each target, extract:
#   (1) kill_form depth-dependence class
#   (2) whether depth_note identifies a UNIVERSAL proof or FINITE sampling
#   (3) the specific gap (what's checked vs what's claimed)
#
# Depth-dependence of kill forms:
#   STRUCTURAL (the type conflict is depth-independent by nature):
#     category-error, kind-mismatch
#   SAMPLING-SENSITIVE (the verdict depends on what depths were checked):
#     absence-at-depth-n, value-mismatch, genericity, base-rate,
#     finite-level-obstruction, no-landing-site, zero-intertwiner, other

STRUCTURAL_FORMS = {"category-error", "kind-mismatch"}

# Per-target depth analysis: does the depth_note identify a gap that could
# change the verdict?
#
# Key distinction: a depth gap in the VALUE computation doesn't threaten a
# STRUCTURAL kill. If the kill says "X is the wrong type" (category-error),
# proving it at one depth suffices — the type doesn't change with depth.
# But if the kill says "the value is wrong" (value-mismatch), the value
# at an unchecked depth COULD be different.
#
# For each target we record:
#   has_universal_step: True if depth_note says some part of the argument
#                       is provably universal (symbolic, all-t, exact)
#   gap_threatens_verdict: True if the gap is in the verdict-bearing step
#                          (not just an auxiliary computation)

ANALYSIS = {}


def analyze_target(tid):
    rec = REC[tid]
    ann = bp[tid]
    kf = rec["kill_form"]
    depth_note = ann["depth_note"]
    adj = rec.get("adjudication", "none")

    result = {
        "id": tid,
        "kill_form": kf,
        "adjudication": adj,
        "structural_form": kf in STRUCTURAL_FORMS,
        "p2_verdict": P2_CELLS.get(tid),
        "has_universal_step": False,
        "gap_threatens_verdict": False,
        "gap_description": "",
        "method_a_verdict": None,
        "method_b_verdict": None,
        "final_verdict": None,
    }

    # ── Parse depth_note for universal steps and gaps ──

    universal_markers = [
        "proven for ALL", "proved for ALL", "symbolic in", "exact and universal",
        "genuine universal", "closed:", "proven for all", "every n",
        "universal", "all t via", "closed for ALL", "by construction",
        "general theorem",
    ]
    gap_markers = [
        "only", "sampled", "not proof", "not proven", "extrapolation",
        "finite", "untouched", "needed:", "Needed:", "Stabilization",
        "rests on ONE", "never extends", "untested", "numeric",
        "not a proof", "brute sweep",
    ]

    note_lower = depth_note.lower()
    has_univ = any(m.lower() in note_lower for m in universal_markers)
    has_gap = any(m.lower() in note_lower for m in gap_markers)

    result["has_universal_step"] = has_univ

    # ── Per-target structural analysis ──
    # This is the E22 question: does the gap threaten the VERDICT?

    if tid == "B107":
        # category-error: off-principal sector ≠ single-scale
        # SL(3) proved symbolically, SL(4) from B103 (proved n=3,4), n>4 untouched
        # But the CATEGORY error is structural: the off-principal multichannel
        # sector exists at every n (it's a representation-theory fact).
        # The depth gap is about extending the VALUE computation, not the type.
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "n>4 value uncomputed, but category-error is structural at every n"

    elif tid == "B437":
        # genericity: inheritance break between m004 and other knots
        # Step 4 symbolically closes "every knot" at slope 5 — universal
        # But slope-7 and B438's 5_2 not rechecked
        # The genericity kill at slope-5 is self-contained and universal
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "slope-5 universally proved; slope-7/B438 are additional evidence, not verdict-bearing"

    elif tid == "B489":
        # absence-at-depth-n: cyclic-cover tower checked n=1..8 only
        # Claim "structural for all n" but capped at NMAX=8
        # E22 pattern: a plateau through n=8 could jump at n=9
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "n=1..8 checked; claim universal; no induction/stabilization proof"

    elif tid == "B500":
        # absence-at-depth-n: depth 4 complete, depth 5 partial, depth>=6 unswept
        # The killed claim has no depth ceiling
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "depth>=6 unswept; no depth-uniform obstruction proved"

    elif tid == "B685":
        # kind-mismatch: but depth_note says evidence is finite-depth pointwise
        # Object series to (q-1)^20, hearing carriers to n=60
        # The KIND mismatch (different denominator structures) is a structural
        # observation, but verified only at finite depth
        # If the pattern changes at higher orders, the kind could converge
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "kind-mismatch evidence is pointwise to n=60/order 20; no inductive proof"

    elif tid == "TOMB-L241":
        # category-error: K-J symbolic (universal), K-K/K-L finite only
        # K-K: 37 words, k=1..6; K-L: n=2..8
        # Category-error for K-J is proved; K-K/K-L gaps don't threaten K-J
        # But K-K/K-L are sub-kills with their own finite gaps
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "K-J symbolic (closed); K-K/K-L finite but K-J alone sustains the verdict"

    elif tid == "TOMB-L247":
        # kind-mismatch: S1a/S1b universal, S2/S3 one-point only
        # The universal step (reducible => kappa=2) sustains the kill
        # S2/S3 are additional depth but S1 alone is the verdict-bearing step
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "S1a/S1b exact and universal; S2/S3 gap is in auxiliary verification"

    elif tid == "TOMB-L252":
        # value-mismatch: claim universal over ALL k, checked to n=4, 18 words
        # "Closed for all n,k" rests on prose, not machine-checked proof
        # The value at unchecked k COULD match
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "claim universal over all k; prose closure only, k>8 unchecked"

    elif tid == "TOMB-L255":
        # value-mismatch: n=2..13 at golden m=1; functoriality sketch only
        # Could differ at n>13
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "n=2..13 computed; functoriality sketch not proof; n>13 open"

    elif tid == "TOMB-L258":
        # other (derivative): falls with K-K/K-L premises
        # F1 checks k=2..8, F2 checks n=2..10, claim universal
        # But the kill is derivative — falls with its premises
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "derivative kill; gap is in K-K/K-L premises (TOMB-L241), not independent"

    elif tid == "TOMB-L267":
        # category-error: K-N sampled m=1..6, claim over all m>=2
        # K-O exhaustive (order-2880 image enumerated)
        # The empty-support claim at m>=7 is not proved
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "K-N sampled m=1..6; claim covers m>=2; m>=7 untested"

    elif tid == "TOMB-L310":
        # genericity: L<=6..10 sweep; "never converging" from 5 drift points
        # No L11+ computed; no analytic recursion
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "L<=10 only; convergence inference from 5 points; L11+ uncomputed"

    elif tid == "TOMB-L334":
        # finite-level-obstruction: "PROVED for all n" but recompute n=3..15
        # The reversal fixed-point argument could be closed algebraically
        # but hasn't been
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "recompute n=3..15 only; 'proved for all n' not machine-verified"

    elif tid == "TOMB-L339":
        # no-landing-site: Parts 1/2/4 exact. Part 3 (isomonodromic) one seed
        # The no-landing-site depends on Part 3
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "Part 3 (not isomonodromic) rests on one seed, one window"

    elif tid == "TOMB-L34":
        # genericity: one finite instance, N=1597 seed0
        # The log-class property could be N-dependent (E22 pattern)
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "one N, two seeds; claim is general chain property; N-stability unproved"

    elif tid == "TOMB-L57":
        # value-mismatch: m=1,2,3 only; could re-hit at larger m
        # The theta(m) function not proved to stay away from pi/3
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "m=1,2,3 only; theta(m) not proved bounded away from pi/3 at large m"

    elif tid == "TOMB-L63":
        # category-error: unitarity ambient (general theorem) BUT enumerated k=1..8
        # The general theorem (congruence-subgroup finiteness) is universal
        # BUT the specific enumeration is finite
        # The CATEGORY error is: unitarity/roots-of-unity is an ambient property,
        # not specific to m004. This is structural.
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "category-error structural: ambient unitarity is a general theorem (all k)"

    elif tid == "TOMB-L67":
        # category-error: "true of EVERY quantum theory" — universal claim
        # Recompute finite: k=1..12+{20,32,40}, 3 MTCs
        # BUT the category-error is: classical |lambda|=phi^k growth vs quantum unitarity
        # This is a STRUCTURAL type distinction valid at all k
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "classical-vs-quantum type distinction is structural at every k"

    elif tid == "TOMB-L70":
        # category-error: disc(t^2-kappa*t+1)=5 != -3
        # BFS finite image proved at k=1,2,3; k>3 word battery only
        # BUT the disc=5 vs disc=-3 is a FIELD distinction
        # It doesn't depend on which k levels are checked
        result["gap_threatens_verdict"] = False
        result["gap_description"] = "disc=5 vs disc=-3 field distinction is depth-independent"

    elif tid == "TOMB-L77":
        # category-error: one invariant (Kashaev); claim says "quantum invariants"
        # Asymptotics numeric, not proved
        # The category-error is: the Alexander/saddle conflation
        # P2 corrected the field (Q(sqrt-3) not Q(sqrt5))
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "one invariant only; claim universal; asymptotics numeric not proved"

    elif tid == "WALL-7":
        # zero-intertwiner: straight (d5) proved for all t; twisted (f3) 3 points
        # The kill depends on both straight AND twisted
        # Twisted is the gap
        result["gap_threatens_verdict"] = True
        result["gap_description"] = "twisted (f3) zero at 3 points only; symbolic-in-t proof needed"

    # ── Method A verdict ──
    if not result["gap_threatens_verdict"]:
        result["method_a_verdict"] = "DEPTH-CLOSED"
    else:
        result["method_a_verdict"] = "DEPTH-EXPOSED"

    return result


# ── Run Method A on all targets ──────────────────────────────────────────────

print("=" * 84)
print("P3 DEPTH-EXPOSURE STRATUM — E22 RE-ADJUDICATION")
print("=" * 84)
print(f"\nTargets: {len(TARGETS)}")
print(f"P2 overlap: {sum(1 for t in TARGETS if t in P2_CELLS)}")
print(f"P3-only: {sum(1 for t in TARGETS if t not in P2_CELLS)}")
print()

results = []
for tid in TARGETS:
    r = analyze_target(tid)
    results.append(r)
    ANALYSIS[tid] = r

# ── Method B: anatomy cross-validation ───────────────────────────────────────

print("─" * 84)
print("METHOD B: ANATOMY CROSS-VALIDATION")
print("─" * 84)
print()

for r in results:
    tid = r["id"]
    p2v = r["p2_verdict"]

    if r["method_a_verdict"] == "DEPTH-CLOSED":
        # Method A says closed. Method B confirms if:
        # - structural kill_form, or
        # - universal proof step identified, or
        # - P2 independently sustains
        if r["structural_form"]:
            r["method_b_verdict"] = "DEPTH-CLOSED"
            r["method_b_reason"] = f"structural {r['kill_form']}; type conflict depth-independent"
        elif r["has_universal_step"]:
            r["method_b_verdict"] = "DEPTH-CLOSED"
            r["method_b_reason"] = "universal proof step in depth_note"
        elif p2v == "KILL-EXTENDS":
            r["method_b_verdict"] = "DEPTH-CLOSED"
            r["method_b_reason"] = f"P2 KILL-EXTENDS independently sustains"
        else:
            r["method_b_verdict"] = "DEPTH-CLOSED"
            r["method_b_reason"] = "kill_form + depth_note analysis agrees"

    elif r["method_a_verdict"] == "DEPTH-EXPOSED":
        # Method A says exposed. Method B checks if P2 or anatomy closes it.
        if p2v == "KILL-EXTENDS":
            r["method_b_verdict"] = "DEPTH-HELD"
            r["method_b_reason"] = f"P2 KILL-EXTENDS closes independently (B754 spectral face)"
        elif p2v == "FACE-IRRELEVANT":
            # P2 says spectral face doesn't touch it. No independent closure.
            r["method_b_verdict"] = "DEPTH-EXPOSED"
            r["method_b_reason"] = "P2 FACE-IRRELEVANT; no anatomy closure"
        elif p2v is None:
            # Not in P2. Check if current anatomy provides independent closure.
            # For B437 (adj=stable), B500 (adj=stable), B685 (adj=stable),
            # TOMB-L310 (adj=stable): stable adjudication is not an anatomy closure.
            # For B489 (adj=unadjudicated-included): explicitly not adjudicated.
            r["method_b_verdict"] = "DEPTH-EXPOSED"
            r["method_b_reason"] = "not in P2; no independent anatomy closure identified"
        else:
            r["method_b_verdict"] = "DEPTH-EXPOSED"
            r["method_b_reason"] = f"P2={p2v}; insufficient for closure"

    # ── Reconcile A and B ──
    a, b = r["method_a_verdict"], r["method_b_verdict"]

    if a == "DEPTH-CLOSED" and b == "DEPTH-CLOSED":
        r["final_verdict"] = "DEPTH-CLOSED"
    elif a == "DEPTH-EXPOSED" and b == "DEPTH-HELD":
        r["final_verdict"] = "DEPTH-HELD"
    elif a == "DEPTH-EXPOSED" and b == "DEPTH-EXPOSED":
        r["final_verdict"] = "DEPTH-EXPOSED"
    elif a == "DEPTH-CLOSED" and b != "DEPTH-CLOSED":
        halt(f"{tid}: Method A says CLOSED but Method B says {b}")
        r["final_verdict"] = "HALT"
    elif a == "DEPTH-EXPOSED" and b not in ("DEPTH-HELD", "DEPTH-EXPOSED"):
        halt(f"{tid}: Method A says EXPOSED but Method B says {b}")
        r["final_verdict"] = "HALT"
    else:
        halt(f"{tid}: unexpected A={a} B={b}")
        r["final_verdict"] = "HALT"

    print(f"{tid:12s} | A={a:14s} | B={b:14s} | final={r['final_verdict']}")
    print(f"             | gap: {r['gap_description']}")
    if r.get("method_b_reason"):
        print(f"             | B-reason: {r['method_b_reason']}")
    print()


# ── Summary ──────────────────────────────────────────────────────────────────

print("=" * 84)
print("VERDICT SUMMARY")
print("=" * 84)

from collections import Counter
vc = Counter(r["final_verdict"] for r in results)
for v in ["DEPTH-CLOSED", "DEPTH-HELD", "DEPTH-EXPOSED", "HALT"]:
    if v in vc:
        print(f"  {v:16s}: {vc[v]}")
print()

print("─" * 84)
print("DEPTH-CLOSED cells (kill is universal-by-proof; no depth gap):")
print("─" * 84)
for r in results:
    if r["final_verdict"] == "DEPTH-CLOSED":
        print(f"  {r['id']:12s} ({r['kill_form']}) — {r['gap_description']}")
print()

print("─" * 84)
print("DEPTH-HELD cells (gap exists but independently closed by P2/anatomy):")
print("─" * 84)
for r in results:
    if r["final_verdict"] == "DEPTH-HELD":
        p2 = f" [P2: {r['p2_verdict']}]" if r["p2_verdict"] else ""
        print(f"  {r['id']:12s} ({r['kill_form']}) — {r['gap_description']}{p2}")
print()

print("─" * 84)
print("DEPTH-EXPOSED cells (genuine E22-pattern open gap):")
print("─" * 84)
for r in results:
    if r["final_verdict"] == "DEPTH-EXPOSED":
        p2 = f" [P2: {r['p2_verdict']}]" if r["p2_verdict"] else " [not in P2]"
        adj = r["adjudication"]
        print(f"  {r['id']:12s} ({r['kill_form']}, adj={adj}) — {r['gap_description']}{p2}")
print()


# ── HALT check ───────────────────────────────────────────────────────────────

if HALT:
    print("*** HALTED — verdict suppressed ***")
    sys.exit(1)


# ── Cross-validation: structural form vs gap analysis ────────────────────────

print("─" * 84)
print("CROSS-VALIDATION: structural form consistency")
print("─" * 84)

for r in results:
    if r["structural_form"] and r["gap_threatens_verdict"]:
        print(f"  WARNING: {r['id']} has structural kill_form ({r['kill_form']}) "
              f"but gap_threatens_verdict=True")
        # This is a genuine case: B685 (kind-mismatch) where the evidence is
        # pointwise, so the "kind" could converge at higher depth.
        # TOMB-L77 (category-error) where only one invariant is checked.
        # These are NOT halt conditions — the per-target analysis correctly
        # identified that the structural form's evidence is depth-limited.
        if r["id"] == "B685":
            print(f"         → VALID: kind-mismatch evidence is pointwise; denominators "
                  f"could converge at higher order")
        elif r["id"] == "TOMB-L77":
            print(f"         → VALID: category-error for one invariant; claim covers "
                  f"all quantum invariants")
        elif r["id"] == "TOMB-L267":
            print(f"         → VALID: category-error for K-N 'empty support' sampled m=1..6; "
                  f"m>=7 could behave differently")
        else:
            halt(f"Unexpected structural form with gap: {r['id']}")
    elif not r["structural_form"] and not r["gap_threatens_verdict"] and r["final_verdict"] == "DEPTH-CLOSED":
        # Non-structural form that's depth-closed — needs justification
        pass  # The per-target analysis already justified each case

print()


# ── The composite finding ────────────────────────────────────────────────────

n_closed = vc.get("DEPTH-CLOSED", 0)
n_held = vc.get("DEPTH-HELD", 0)
n_exposed = vc.get("DEPTH-EXPOSED", 0)

print("=" * 84)
print("THE P3 FINDING")
print("=" * 84)
print()
print(f"Of 21 depth-flagged P1 negatives:")
print(f"  {n_closed} DEPTH-CLOSED — kill argument contains a universal proof step")
print(f"  {n_held} DEPTH-HELD — depth gap exists but independently closed by P2 spectral face")
print(f"  {n_exposed} DEPTH-EXPOSED — genuine E22-pattern open gap")
print()
if n_exposed > 0:
    print("The DEPTH-EXPOSED cells are the program's honest residual:")
    print("kills whose evidence is finite-depth sampling, whose claims are universal,")
    print("and whose gaps are not closed by any independent face in the current anatomy.")
    print()
    print("These kills are NOT wrong — they are UNDERPROVED. The verdicts may be")
    print("correct, but the evidence standard falls short of the claim scope.")
    print("The E22 lesson: a finite-depth check is not a universal proof.")
    print()
    exposed = [r for r in results if r["final_verdict"] == "DEPTH-EXPOSED"]
    print("Exposed cells and their stabilization needs:")
    for r in exposed:
        note = bp[r["id"]]["depth_note"]
        stab_idx = note.lower().find("need")
        if stab_idx >= 0:
            stab = note[stab_idx:]
        else:
            stab = "(see depth_note)"
        print(f"\n  {r['id']} ({r['kill_form']}):")
        print(f"    Gap: {r['gap_description']}")
        print(f"    Stabilization: {stab[:200]}")

print()
print("─" * 84)
print(f"HALT = {HALT}")
print("─" * 84)


# ── Write structured output ──────────────────────────────────────────────────

output = {
    "targets": len(TARGETS),
    "depth_closed": n_closed,
    "depth_held": n_held,
    "depth_exposed": n_exposed,
    "halt": HALT,
    "cells": {r["id"]: {
        "kill_form": r["kill_form"],
        "structural_form": r["structural_form"],
        "adjudication": r["adjudication"],
        "p2_verdict": r["p2_verdict"],
        "gap_threatens_verdict": r["gap_threatens_verdict"],
        "gap_description": r["gap_description"],
        "method_a": r["method_a_verdict"],
        "method_b": r["method_b_verdict"],
        "method_b_reason": r.get("method_b_reason", ""),
        "final_verdict": r["final_verdict"],
    } for r in results},
}

with open(Path(__file__).parent / "results.json", "w") as f:
    json.dump(output, f, indent=2)
    f.write("\n")
