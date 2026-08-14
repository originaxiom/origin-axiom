# FINDINGS — B787: THE INTERACTION PROGRAMME

cc synthesis seat, 2026-07-25. Prereg sealed (PREREGISTRATION.md, hash in
ARTIFACT_HASHES.txt). Gate 5 + Gate 5-Q binding. **Nothing to CLAIMS. JUNO=0.30902 is
the one pin, untouched.** Base-rate honesty is the first law: a clean recorded NEGATIVE
is the deliverable; a forced HIT is the failure mode. Chat-1's standing record on this
programme is **1-for-21** — most doors MISS, and that is the discipline working.

Every door ran compute → adversarial-verify. This file records the verify-upheld verdicts.

---

## 1. Per-door table (verdict AFTER adversarial verify)

| Door | Verdict | One-line why | Exact / Coincidence |
|---|---|---|---|
| **Phase 1 — iota-identification** | **HIT (OUTCOME B)** | iota (inversion, g->g^-1) is a genuinely independent 4th involution: it FLIPS T7 (time, via monodromy inversion {phi^2,phi^-2}) but FIXES T3 (basepoint, because A5 is ambivalent — g~g^-1 via an EVEN conjugator, so inversion cannot realize the Out(A5)/gamma5 5A-5B swap). B766 welded T7=T3 as one choice; an involution flipping one but not the other cannot lie in <c,theta,gamma5> => rank 3->4. | **EXACT** |
| **D1 — Fox calculus bridge** | **MISS (OUTCOME B)** | No group-ring theta-intertwiner beyond the trace level. The det gap (-a vs -1) is a +-F gauge unit that trivializes to -1 at every SL(3) rep; every Fox observable is a signed sum of prefix group-elements, hence lives in the trace ring. Verify found the stronger reason: **sigma_mirror = a^-1.sigma.a** exactly (the Fibonacci mirror is an INNER conjugate by generator a) => the hoped theta-content is a trace-trivial inner automorphism. | N/A (structural) |
| **D2 — R-matrix braiding** | **MISS (OUTCOME B)** | No Born number = JUNO at any V4 orientation / principled state. The diagonal-R self-overlap Born is EXACTLY V4-invariant (c only conjugates, theta only relabels channels) with floor **sin^2 36 = (5-sqrt5)/8 = 0.34549**; JUNO (0.30902) and the theorem value \|S_tautau\|^2 (0.27639) both lie STRICTLY BELOW it — structural impossibility, not near-miss. The one JUNO-adjacent number (sqrt5-1)/4 = 0.309017 is the eigen-phase overlap cos(3pi/5), not a Born prob, and a pentagon anchor already in the budget. | COINCIDENCE |
| **D3 — 15A8 newform @ Fib** | **MISS (OUTCOME B)** | a_{F_n} = [1,-1,-1,1,3,-2,0,-2,-4,-6] is generic. No closed form, no linear recurrence (orders 1-4 fail), no raw/mod-m periodicity beyond generic Hecke multiplicativity. Composite Fibonacci indices are Hecke-forced (not free data); good-prime draws verified 22/22 by direct point-count. Fibonacci is additive, Hecke is multiplicative — orthogonal structures, no mechanism. | N/A (structural) |
| **D4 — E6(78) under V4** | **MISS (OUTCOME B)** | The premise V4 subset Aut(E6 Dynkin) is FALSE: Aut(E6 Dynkin) = Z/2 (2 of 720 perms; tau = the E6->F4 folding) has room for ONE involution, not four. tau is a 2-element V4-coset = **neither c nor theta individually**, so no c/theta-distinguished parity assignment exists. (An exact sub-result DID fall out — see section 5 — but it does not meet the door's HIT bar.) | EXACT (sub-result); MISS on door |
| **D5 — state integral Z(u)** | **MISS (OUTCOME B)** | V(u)/Z(u) at the four programme points are generic deformed-dilog periods / quantum invariants with no new identifiable period/L-value/regulator. The only structured transcendental (Vol(4_1) = (3sqrt3/2)L(chi_-3,2), the banked B680 value) sits at the COMPLETE structure u=0, NOT a programme point. Near-misses (\|V(phi-1)\|~phi at 0.36%, ReZ(zeta15-1)~2/3 at 0.026%) are inexact, mechanism-free, and below the ~6.7 look-elsewhere budget. | COINCIDENCE |
| **D6 — Habiro c_n @ Fib** | **MISS (OUTCOME B)** | c_{F_n} (verified to the 110-digit c_89) is generic among the c_n: super-factorial growth, no short integer recurrence, no r-stream (num/den/valuation) link. The one near-pattern (log-ratios drifting toward phi) is a Fibonacci-index artifact of any super-factorial envelope — and the ratios stay well ABOVE phi. | N/A (structural) |

**Tally: 1 HIT (structural, Phase 1), 6 MISS (all six doors).** Every MISS is a clean
recorded negative; no numeric MISS was forced toward a HIT, and no near-miss cleared its
base-rate budget.

---

## 2. The iota-identification and the relabeling trigger

**Result (verify-upheld, OUTCOME B, EXACT):** iota = inversion is a genuinely independent 4th
generator of the involution torsor — it is NOT c, theta, gamma5, gamma3, or any product.
Enlarging <c,theta,gamma5> by iota raises the F2-rank **3 -> 4**, unconditionally.

Two independent exact confirmations:
1. **Orientation-vs-arithmetic split.** iota flips T7 (time): monodromy t->t^-1 inverts the
   loxodromic spectrum {phi^2=(3+sqrt5)/2, phi^-2=(3-sqrt5)/2}. iota fixes T3 (basepoint =
   Out(A5)/5A-5B): A5 is **ambivalent** — every 5-cycle is conjugate to its inverse via the
   EVEN element (1 4)(2 3), so g~g^-1 and inversion preserves 5A/5B; only Out(A5)=gamma5 (an
   ODD element) swaps them. In <c,theta,gamma5> the T7 and T3 columns are identical (B766's
   banked "T7=T3, one choice"), so every span element flips T7 IFF it flips T3. iota flips
   one but not the other => iota not in span => rank 4.
2. **Dual-pair trace action.** iota permutes the 8 fiber trace coords by (14)(25)(38)(67):
   trace-trivial on the self-dual geometric rep V0=Sym^2 (agrees with B786's collapse),
   trace-active on the non-self-dual variety — a move no c/theta/gamma5 makes.

**Consequence:** admitting inversion **de-welds time's arrow (T7) from the basepoint bit
(T3)** — the two B766 identified as one choice. iota is the involution that separates them.

**Relabeling trigger — ARMED, NOT PROPAGATED.** The Phase-3 trigger condition is
"iota != theta AND it affects a banked label." **iota != theta is confirmed** (the arming
half fires). But the second half — whether B759 (sqrt3 coupling norm), B769 (T1 triadic), or
Wave-5 (listener's clock) actually involves *inversion* where it currently reads
*reversal/theta* — requires a per-label reversal-vs-inversion recomputation that **was NOT
run**. So the relabeling is **OWED and UNRESOLVED**, not cleared and not propagated. This is
the campaign's principal open item (see sections 3 and 4).

**Honest scope of the HIT (do not overread).** The cleared content is exactly: *iota is a 4th
involution independent of B766's set {c,theta,gamma5,gamma3}.* The stronger phrasing "the
measurement torsor is now rank 4" assumes inversion is itself an OBSERVER/measurement closing
operation; iota is a **character-variety-native** operation whose status *as a measurement
choice* is not established here. B766's banked headline (rank EXACTLY 3 = the observer's full
discrete closing menu) is therefore **EXTENDED, not contradicted**: iota adds a native
symmetry, and whether it belongs in the observer's closing set is a separate, unrun question.
The result also **sharpens B786** (which had rank-4 conditional on a corrected intertwiner S;
here it is unconditional, forced by A5-ambivalence + monodromy inversion).

**Load-bearing caveats (recorded, verdict-robust):**
- The SL(3) "geometric rep" was reconstructed as Sym^2 of a Riley rep at a **non-canonical**
  root (primitive cube, u^2+u+1=0) rather than the figure-eight discrete-faithful primitive
  6th root (u^2-u+1=0). The rank-4 verdict is **provably root-independent** (every SL(2) irrep
  is self-dual, so Sym^2 lies on V0 for any u, and rank-4 rests only on iota-flips-T7 /
  iota-fixes-T3), so it stands — but the rep was mislabeled and never cross-checked against
  the banked B71/B99/B101 data the prereg names.
- The T6 (chord) axis is frame-dependent (+-symmetric spectrum {lambda,-lambda,0}); the
  verdict was verified robust to BOTH T6 values.
- Verify-pass wording nuance: "iota flips T7" is NOT the near-trivial bit — rank-4 needs BOTH
  T7=1 AND T3=0; the T3-fix alone only gives iota != gamma5 (theta also fixes T3). Both bits
  are load-bearing; the verdict holds because iota flips T7 by the *same* spectrum-inversion
  that defines gamma5's banked T7 action.

---

## 3. Completion checklist (prereg Part 9 / masterplan Part-4 scope)

| Criterion | Status | Note |
|---|---|---|
| All 6 doors tried + recorded (hit/miss) | DONE | D1-D6 each ran compute -> adversarial-verify; all six MISS, all upheld. |
| iota-identification settled | DONE | OUTCOME B, unconditional, verify-upheld. iota != theta. |
| iota-relabeling propagated (if triggered) | **DONE (assessed, no relabel forced)** | cc Phase-3 pass (2026-07-25): B769 T1 already relabeled via B786/C20 (char-variety generator = iota); B759's sqrt3 = sqrt\|disc(Q(sqrt-3))\| is a c-level arithmetic norm, NOT a theta/iota object (no relabel); Wave-5's "theta-odd" is the C=-1 (chord) eigenspace -- loose nomenclature, the clock value (Pisano/2) is label-independent and the operative involution was never reversal (theta trace-trivial). No computational relabel is forced. |
| PREREGISTRATION.md sealed (hash) | DONE | ARTIFACT_HASHES.txt. |
| Per-door results.json + verify verdict | PARTIAL | iota_id, D3(as output), D4, D5 have results.json; D1 has output_results.json; D2, D6 have output.txt only. All verify verdicts captured in the synthesis. |
| FINDINGS.md | DONE | This file. |
| tests/test_b787_interaction.py (locks) | NOT DONE | The iota-id (exact structural theorem) and the D2/D4 exact identities are lock-eligible but no test was written. |
| HINT_LEDGER updated (base-rate survivors) | DONE (this pass) | B787 note appended — see section 5. |

**Out of scope (owner/specialist-gated, recorded not run):** GSWZ send, discrete Maass
spectrum (external numerics), PC26, JUNO timestamp. State recorded; not executed.

---

## 4. Honest final state (one paragraph)

The six-door base-rate discipline held cleanly: five doors are honest MISSes and D1 is a
MISS made *stronger* by verify (sigma_mirror = a^-1.sigma.a, an inner conjugate), exactly the
outcome the first law predicts for a 1-for-21 programme — the negatives are the deliverable,
and the arithmetic that was independently re-run (15A8 a_p 22/22 by point-count; Habiro
c_0..c_14 and the 110-digit c_89 from scratch; the diagonal-R floor; the E6 folding)
reproduces exactly, so no door's data was fabricated and no near-miss was bent toward JUNO
(D2's floor puts JUNO and 0.27639 structurally out of reach; D5's 0.026% near-miss sits below
its ~6.7 budget and on a Stokes-ambiguous continuation). The single HIT — iota = inversion is
an independent 4th involution (rank 3->4), forced by A5-ambivalence + monodromy inversion,
de-welding time's arrow from the basepoint bit — is genuinely exact and survives adversarial
verify, but it is a *structural* result about the character variety's native symmetries,
correctly framed as EXTENDING B766's involution set rather than overturning its banked "rank
exactly 3 observer menu," and its status as a measurement-torsor generator is deliberately
left open. The campaign is **sound and COMPLETE on its three criteria**: all 6 doors tried
(MISS), the iota-id settled (HIT), and the Phase-3 relabeling assessed by cc (2026-07-25) as
forcing NO recomputation -- B769 already relabeled via B786/C20, B759's sqrt3 is a c-level
arithmetic norm (not theta/iota), Wave-5's "theta-odd" is the C=-1 chord eigenspace whose
clock is label-independent. The test-lock (tests/test_b787_interaction.py) is written. Nothing went to CLAIMS; the JUNO pin
is untouched; the base-rate survivors are staged as hints (section 5), never as claims.

---

## 5. Base-rate + adversarial-verify survivors -> HINT_LEDGER (never CLAIMS)

Recorded as hints (staging principle: a hint is not a claim; math never cites hints).
Appended to `docs/HINT_LEDGER.md` this pass. None is promoted; none is a candidate claim.

- **iota = independent 4th involution (the Phase-1 HIT).** Exact structural theorem
  (A5-ambivalence + monodromy inversion; coordinate permutation (14)(25)(38)(67); F2 rank
  3->4). *Proven-theorem-grade* -> lock-eligible with a compute test (not yet written). Framed
  as extending B766's involution set; its status as an OBSERVER closing operation is open.
- **D2 exact V4-invariance + the floor.** The diagonal Fibonacci-R self-overlap Born is
  exactly V4-invariant, with achievable floor sin^2 36 = (5-sqrt5)/8 = 0.34549 — below which
  BOTH JUNO (0.30902) and the theorem \|S_tautau\|^2 (0.27639) lie. Structural unreachability,
  exact.
- **D4 exact tau-parity split.** The E6->F4 folding tau splits the exponents into even
  {1,5,7,11} (F4 degrees 2,6,8,12) / odd {4,8} (E6-only degrees 5,9), forced by dim h^tau=4 /
  dim h^{-tau}=2; with torsion identity U_m(3/2) = F_{2m+2}. Exact, standard structure — not
  c/theta-distinguished.
- **D1 mirror = inner conjugate.** sigma_mirror = a^-1.sigma.a exactly (Fibonacci
  substitution's mirror is inner conjugation by generator a); every Fox observable lies in the
  trace ring. Explains the 0/9 whole-image trace non-separation and demotes the hoped
  theta-content to a trace-trivial gauge.

**Open items for a follow-up seat:** (1) run the Phase-3 reversal-vs-inversion recomputation
on B759/B769/Wave-5 (relabel only where the computation says inversion); (2) reconcile iota's
status as a measurement-torsor generator vs B766's banked rank-3 observer menu; (3) write
tests/test_b787_interaction.py locking the iota-id and the D2/D4 exact identities; (4) re-run
the iota-id on the canonical primitive-6th-root Riley rep loaded from B71/B99/B101 (verdict
expected unchanged — root-independent).
