# B778 FINDINGS — THE CLEANUP WAVE (partial: 5 of 7; 2 pending next pass)

*2026-07-24. Workflow wf_04cb8ebd-024 ran 5 of 7 cells to completion before the pass
ended; the remaining 2 (CL-W4115, CL-LATIN) never started and are queued for the next
pass. Of the 5 completed: 2 were agent-verified in-run (CL-DARKHYP, CL-W3082); 3 had
their verifier interrupted, so **cc self-verified them directly** (deterministic re-run
+ hand-check of the discriminating fact) before banking. Machine table
partial_results.json.*

## Banked (5)

| cell | verdict | result | verification |
|---|---|---|---|
| **CL-DARKHYP** | **RESOLVED-A → THEOREM** | the N=p² dark-hyperbola law PROVEN all-p: the θ-lift Weil seam T(j,l) has magnitude spectrum EXACTLY {0,1,√p,p}, via completing the square → 1-var ℤ/p² Gauss sum, with exact valuation stratification counts. The dropped Wave-2 cell, now closed. | agent-verified in-run (independent float spectrum + pointwise classifier at p=5, zero mismatches); count identity 63+6+1+11=81=3⁴ hand-checked. |
| **CL-W3082** | **RESOLVED-B → EXTERNAL** | W3-082c confirmed honest EXTERNAL: the Kim H³ arithmetic-CS bridge is genuinely NEEDS-SPECIALIST (uncomputed, self-flagged in LAW_MAP); reframed to the exact class-group fact **Sylow₂(Cl(−8899))=ℤ/2** computed in-cell. The trace-negative does not lift to a loaded wall; the loaded positive is not established. | agent-verified in-run. |
| **CL-W5139** | **RESOLVED-A** | dead RESOLVED-B verdict-branch stripped from W5-139; the block emits RESOLVED-A cleanly and **genus(A₃)=41 reproduced** (the metallic sequence (3,1,41) stands). | cc self-verified: deterministic re-run (71s, genus=41, B=20); RH hand-check 2g−2=80=4B. |
| **CL-W5100** | **RESOLVED-A** | decorative par_split_diff chord check stripped (it was a relabeled trace invariant — fails the B774 self-test); **D₀ convergence stands** (golden 0.4562, silver 0.4645, reproduces the W5-100 pins). | cc self-verified: deterministic re-run, pins reproduced exactly. |
| **CL-H133** | **RESOLVED-B → HARDENS** | cc3's chord-suspect resolved: at level 4 (where Z₄=Tr ρ(A₁)=0), the θ-odd sector is ALSO zero (tr_even=0 AND tr_odd=0 independently, from SEPARATE traces) — a GENUINE structural zero, NOT the W4-304 cancellation pattern (there tr_odd=1/4 was hidden; here everything vanishes). **H133's death hardens at the chord level.** | cc self-verified: deterministic re-run (VERDICT RESOLVED-B, all sectors 0 at level 4); the W4-304 contrast confirmed by hand. |

## Pending the next pass (2)
- **CL-W4115**: strip the fabricated "adjoint 7,815…" string from W4-115c + re-verify the
  cover-torsion/charge wall on real data (extend the charge tower to n≥10). Never ran.
- **CL-LATIN**: the P2W2-LATIN non-current block — is its 3-valuedness forced or measured?
  Never ran.

Both are re-queued (the honest downgrade / carry states stand until then: W4-115c's
wall-hardening is banked-provisional, LATIN's is RESOLVED-B/downgraded).

## Note on the chord-suspect count
Combined with B774 (12/12 load-bearing walls hardened) and cc3's independent audit,
**H133 — the one new chord-suspect either seat surfaced beyond B774's top-12 — also
HARDENS.** The blind-projection problem remains W4-304-isolated: every chord-checked
wall except that one is a genuine zero.

Gate 5 / Gate 5-Q clean. Nothing to CLAIMS; the one-number pin untouched.

---

## COMPLETION (2026-07-24): the 2 pending cells resolved by direct computation — B778 now 7/7

The agent quota was spent, so cc completed CL-W4115 and CL-LATIN by DIRECT computation
(no agents) + hand-verification. Both land RESOLVED-B, both cross-checked two ways.

| cell | verdict | result |
|---|---|---|
| **CL-W4115** | **RESOLVED-B** | The fabricated "adjoint 7,815" string STRIPPED — direct recomputation shows the essential adjoint (t²−5t+1) content is [3,21,108,525,2523], no 7, no 815 (fabricated); the chord "1,5,19,71" is REAL (odd-n √(Res/2)). The wall HARDENS on the **verified field-disjointness mechanism**: chord Q(√3), adjoint Q(√21), charge Q(√5) are three DISTINCT fields (disc 12/21/5), so no value-collision law relates chord/adjoint to the charge tower; the lone T(5)=121=11² hit is an isolated abelian-Q(√5) coincidence (content ≡0 mod 11 at n=5,10, period 5). W4-115c's RESOLVED-B stands on real data, fabrication removed. |
| **CL-LATIN** | **RESOLVED-B** | The P2W2-LATIN downgrade CONFIRMED with a computed mechanism, by TWO independent routes: (a) the cell's full E6₂ rebuild + T1–T4 forcing-candidate test (T2 Galois fails: "|.| not Galois-equivariant"); (b) cc's direct amplitude-Galois test — {A1,A2,A3}=(2/√7)sin(2πk/7) is NOT Galois-closed (minpoly 7x³−7x²+1 has roots {A1,A2,**−A3**}). |·|'s absolute value is the **non-Galois step** — the SAME step as the mirror (P2W2-MIRROR). The Latin square is exact + Z/3-current-row-forced, but the non-current block rests on |·|, not fusion/Galois forcing. |

**A cross-arc unification (recorded):** CL-LATIN and P2W2-MIRROR share one root — the
absolute value |·| on modular data is the non-Galois step in BOTH. The mirror is
non-Galois (anti-diagonal axis map) and the hearing Latin square is not fully forced,
for the same reason: |S| discards the Galois sign that would close the orbit.

**B778 is now 7/7 complete.** Gate 5 / Gate 5-Q clean; nothing to CLAIMS.
