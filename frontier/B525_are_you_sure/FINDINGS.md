# B525 — THE "ARE YOU SURE" CAMPAIGN: adversarial re-audit of the program's negatives

**Owner directive (2026-07-12, non-negotiable):** *"you keep making mistakes over and over. launch an are-you-sure
campaign on most of your negative results and their roots."* A 61-agent adversarial Workflow presumed every
load-bearing NEGATIVE unsound until it survived attack by 5 skeptics carrying distinct failure-mode lenses
(backwards-argument · necessary-not-sufficient · proxy-for-object · control-invalid/untested-gap ·
generic-overclaim — the seat's *own* repeated errors), each recomputing the root in-sandbox where feasible,
then a strict judge. Full synthesis: `synthesis.txt`. Firewalled.

## Verdict: 4 CONFIRMED · 2 SHAKY · 3 CRACKED
| negative | verdict | why |
|---|---|---|
| **PHYS-REFUTED** (master) | **CONFIRMED** | recomputed under all 5 lenses: h(−15)=2, units {±1} for d<−4, the ℤ/2-on-invariants Galois inference runs the *right* way, empirical nulls hold. **The object still does not produce physics.** |
| **SIG-GENERIC** | **CONFIRMED** | the full signature table is exact ((2,1)→(3,1); totally-real→(4,0); x⁴+1→(2,2)); tetranacci control genuine. |
| **NOT-3MFD** | **CONFIRMED** | φ∈Aut(F₄) re-derived by independent inverse; λ(φ)=3.676 ≠ λ(φ⁻¹)=3.052 seed-consistent. The just-fixed Stallings argument holds. |
| **NOVELTY-COROLLARY** | **CONFIRMED** | held-breath = Cantat corollary; the elementary derivation reproduces (ℚ(√17) control; d=5,7 fields). |
| **DGG-ABELIAN** | **SHAKY** | rep counts recompute, but "abelian at every K" is a bare citation (DGG 2014), not computed → anchor to a specific theorem and/or finish SL(4). |
| **GATES-SEALED** | **SHAKY** | Gate C's *conclusion* (ℤ/3 = trinification, not generation) is correct on the sound ground (module rank 2, 2∤3), but `verify_gates.py` *posits* T=companion(Φ₃) and the Fix=0 / no-eig-1 legs are backwards → re-derive the deck action from the geometry. |
| **B519-NOCROSS** | **CRACKED** | necessary-not-sufficient (below). |
| **C3-CONE** | **CRACKED** | proxy-for-object bug (below). |
| **CHILD-NOTSHORT** | **CRACKED** | census-completeness error (below). |

## The meta-pattern (the campaign's most valuable output)
Every crack is **one error in three faces: a necessary / cited / proxied condition read as a sufficient
verdict.** The reliable **tell**: the load-bearing line was *asserted / cited / posited / logged-as-timeout*,
**not computed**. Every negative whose certificate genuinely recomputed its own discriminating fact (the 4
CONFIRMED) survived; every one where it did not (the 3 cracked + 2 shaky) fell. This is the standing rule
going forward — see [[abelianization-is-not-a-proxy]] (extended): **a negative is only as sound as the
in-sandbox computation of its *discriminating* fact.**

## The three cracks — and the corrections applied this session
1. **B519-NOCROSS → the "no external crossing" headline is RETRACTED.** The B1 refutation conflated
   Bellissard gap-labeling (necessary: constrains allowed IDS *values* of gaps that open) with a guarantee of
   *which* gaps **open** — the falsifiable content of B518 Tier B is the 2×2 opening pattern, on which
   gap-labeling is silent (Thue–Morse is the textbook fail-to-open case). **B1 is now a LIVE falsifiable
   external candidate**; only the weaker absorbing-loop / model-confirms-model caveat deflates its
   *fundamentalness*. Corrected in [[B519]] VERDICT + docs/CLOSURE_2026-07-11. B2 needs its own re-argument.
2. **C3-CONE → conclusion survives, certificate fixed, nugget retracted.** `c3_malament.py`'s sign convention
   sent zero eigenvalues to "spacelike", mislabelling the det-0 TM verb "(3,1) proper" and driving a buggy
   cone-preservation reading. Fixed to a degeneracy-flagged **signature** classifier; the conclusion (four
   different causal types → no single cone → Malament n/a) rests only on the signatures and holds. The nugget
   "causal ⟺ evolution verb" is **retracted** (it rode the buggy percentages).
3. **CHILD-NOTSHORT → KILL downgraded to PROVISIONAL.** Only **115 of 150** words were actually analyzed
   (26 of the 141 logged lines are bare `TIMEOUT` — no factor/galois/−283 check); **35 unchecked**, not 9.
   0/115 is suggestive but not the depth-5 exhaustion the prereg's KILL requires. Corrected in [[B500]];
   reopen = re-run the 35 (𝔽_p Gröbner or longer timeout).

## The two shaky — follow-ups (not errors, but citation/posit, not computation)
- **DGG-ABELIAN:** convert "abelian U(1)^{r_K} at every K" from a DGG-2014 citation into a cited
  proposition, and/or complete the deferred SL(4) Ptolemy (Magma). Affects [[B524]]/[[B526]].
- **GATES-SEALED:** rewrite `verify_gates.py` to derive the rank-2 ω-multiplication deck action from the
  figure-eight commensurator geometry and replace the backwards Fix=0 leg with the real discriminator
  (module rank 2, 2∤3; the 𝔢₆ = 24⊕27_ω⊕27̄_ω² conjugate-eigenspace grading). Conclusion unaffected.

## Bottom line
**The master negative stands: the object does not produce physics** (CONFIRMED, recomputed). But three
supporting negatives were unsound as banked, and the owner's instinct was exactly right — the errors are one
recurring blind spot (necessary/cited/proxied → sufficient), catchable by one rule: **compute the
discriminating fact, never assert it.** The most consequential correction: the program does **not** have
"zero external crossings" — **B1 (the mixed-chain gap-opening pattern) is a genuinely falsifiable external
prediction**, the closest thing to a lab-runnable test the corpus contains. Locks updated:
`tests/test_b523.py`, `tests/test_b500_kill.py`. Cross-refs: [[B519]] [[B500]] [[B523]] [[B524]] [[B526]]
docs/CLOSURE_2026-07-11.
