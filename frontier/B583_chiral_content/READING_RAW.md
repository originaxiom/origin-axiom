# B583 — THE CONTENT READING

*Reading seat, 2026-07-12 (of record; transcripts reference runs through 07-14). Verification status binds over headline status throughout: X3 is verified; X2 failed adversarial verification; X1's verification is still in progress and everything said of it below is provisional.*

---

## 1. The three computations

### X1 — the coupled mirror-double on the 27 (verdict: NO-REAL-FORM; **verification pending**)

**What was built.** A two-copy amalgam on the 27 of E6: copy-1 the figure-eight holonomy ρ(a)=exp(e_pr), ρ(b)=exp(ω f_pr); copy-2 its conjugate twisted by the θ-odd dial, c=exp(t·v4), v4 = BLOCKS[4][0]. The peripheral identification of the amalgam is exact and green: meridian shared (a2 = a1, since v4 is e_pr-highest so c commutes with A27), longitude inverted (L1·L2 = I), both longitudes peripheral. Gates hold at t ∈ {1, 1/2, 2}.

**What it produced.** The decider — reality of the coupled character — computed exactly in ℚ(√−3):

- tr₂₇(a1 b1) = (1295415 + 1011915·√−3)/2 — **non-real**, dial-independent (copy-1-internal, hence t-free; identical at t = 1, 1/2, 2).
- tr₇₈(a1 b1) = −(325640463 + 116870115·√−3)/2 — the adjoint independently non-real.
- Copy-swap law observed exactly: tr₂₇(a2 b2) = conjugate of tr₂₇(a1 b1); swap-symmetric words real (10/20 in the 27, 3/6 in the 78), non-symmetric words non-real.

By B578-D10 (E6 descent trivial, unconditional): real character iff real form. The character is not real, so **no real form descends**. The structural reason is clean: the natural antiholomorphic involution σ(x) = c·conj(x)·c⁻¹ *swaps* the two copies rather than fixing them — it stabilizes the configuration without fixing it. The reality locus in the dial is **empty for all t**.

**Audit binding.** The vreason field is a placeholder; verification has not completed. This cell must not bank until it does. The reading below uses it in the only way the brief permits — as the computed fact it currently is, flagged provisional.

### X2 — the σ-visible interference term (headline: **FAILED verification**)

**What was attempted.** Assembly of the interference amplitude X_m(u4) = Z_geo·conj(Z_conj) at one loop, k = 2, ħ_eff = π/7, using amphichirality (CS = 0) to fold the anti-geometric saddle into Z_geo², claiming a split into an exact signed torsion part 1/τ_m and a transcendental phase exp(i·14Vol/π).

**What the audit found — two independent, each sufficient to fail the cell:**

1. **Vol/CS role inversion.** The construction puts Vol into a unit-modulus phase and gives CS no role. In the standard semiclassical assignment — and in this repo's own banked precedent (B246: the CS action carries the phase; the volume-conjecture check is *real* growth in Vol) — Vol is the real growth/decay rate and CS the oscillation. With CS = 0 exact, the correct geometric-saddle phase is trivially 1, and Vol should contribute a real factor exp(±2Vol/ħ_eff) ≈ 8482 or 1.18×10⁻⁴. The cell's own setup contains the error visibly: it writes S0 = i·Vol and then uses exp(i·Vol/ħ) instead of exp(i·(i·Vol)/ħ) = exp(−Vol/ħ) — a dropped factor of i. This invalidates the "torsion × transcendental phase" headline, the interference table 2Re(X_m)/N², and the σ-visibility framing.
2. **Overclaimed transcendence.** "14Vol/π is transcendental" was asserted from a PSLQ null plus a failed nsimplify. What was computed is "no rational·π relation found by PSLQ to 60 digits." Transcendence of Vol(4₁) as a period is conjectural in the literature. Under the firewall rule (claim = exactly what was computed), the claim is retracted to the finite-precision null.

There is also a process finding: X2 ran a Route-B-like construction against the still-open chord question without its own preregistration and ahead of the registered Route A (L78) — out of the object's own committed run-order. X3 subsequently ran Route A properly.

**What survives X2, undisputed.** Vol(4₁) = 2.0298832128193072500… (50 digits); ħ_eff = π/7 from k+h∨ = 14; CS = 0 exact by amphichirality (banked); all six exact torsion reciprocals 1/τ_m, bit-for-bit against B581, including the sign law — **1/τ_m > 0 iff m is θ-odd (m ∈ {4, 8})**, negative for θ-even {1, 5, 7, 11}; and the raw cos/sin/angle arithmetic. The defect is in the physical assembly, not the arithmetic.

### X3 — Route A, the level-2 θ-odd amplitude (**verified; the second unhearability theorem**)

**What was computed.** The row-0 (vacuum) filling covectors of ρ_level2(g_{p,q}) over 719 slopes (coprime p ∈ [−24,24], q ∈ [1,24]), against the exact 9-dim C3 rep (all gates green: Weyl 51840, S unitary/symmetric, S² = θ-flip, Verlinde integral, q-dims; gates run before touch in every code path).

**What it produced.**

- Singular values [13.292, 12.941, 12.008, 9.674, 9.348, 7.049, 0, 0, 0]: **rank exactly 6 = dim(θ-even)**, θ-odd projection 3.85×10⁻¹³.
- Control reproduced Q1 exactly: level-1 rank 2 = dim(θ-even), θ-odd projection 5.4×10⁻¹⁵.
- Every twist sector (q mod 6, the six dial slots) individually rank 6; no slot hears θ-odd.
- The three sine-kernel eigenvectors (eigenvalues {+i, −i, −i}) overlap the reachable span at ~10⁻¹⁴: the reachable span is the *exact* orthogonal complement of the sine-kernel's θ-odd home.
- The mechanism is a theorem, not a numeric: C = S² commutes with S and T and the vacuum is θ-fixed, so every filling covector is C-fixed = θ-even — **level-independent**.

**Audit binding.** Survived adversarial re-verification on every axis: verbatim rerun bit-for-bit; an independently coded Kac–Peterson builder reproducing gate residuals to many digits; and — beyond the cell's own evidence — an exact rational-arithmetic proof (no floats) that θ preserves h(λ) for all 9 primaries, θ(ρ) = ρ, and the vacuum is θ-fixed exactly. The rank-6 sharpening (fillings hear the *whole* θ-even 6-plane, none of θ-odd) stands. One minor procedural shortfall (MB13 documented by grep only, not an atlas query) — no substantive gap. Preregistered outcome table in ROUND1_TRANSCRIPT §3 was neutral; the computed branch was followed without overclaim.

---

## 2. The permitted comparison: which world does the meeting live in?

Had X1 identified a real form, step 3 would have computed the signature and named the world: the maximal compact subgroup of the identified real form of E6, together with the forced branching of the 27 under it — a computed fact, one line, no interpretation needed.

**That premise fails.** The character is not real, so — conditional on X1's pending verification — no real form descends, no maximal compact exists for this holonomy, and **no branching of the 27 is forced**. The coupled holonomy stays full E6(ℂ) and its 27 stays the complex chiral 27.

What this means for the compactness–chirality reconciliation question, stated honestly: this construction does not reconcile them — and the *way* it fails is itself the computed content. The mirror-double was the natural candidate for a meeting in which a real (hence potentially compact-restrictable) structure emerges from coupling a chiral object to its conjugate. Instead, the antiholomorphic involution swaps the copies rather than fixing them: the coupled object is σ-*stable* but not σ-*fixed*, and the obstruction is dial-independent (the witness trace is copy-1-internal, t-free; the reality locus is empty for every t). Chirality is not cancelled by meeting the mirror — it is doubled into a swap symmetry. This corroborates and sharpens B582: the 27 is chiral as a matter of structure, and at least along this coupling family the chirality survives the meeting intact. The negative is scoped: one construction, one dial direction (v4), one involution family. It closes this door; it does not close the question.

---

## 3. What X2 and X3 mean for the chord program

The chord program's open item was the interference cross-term — the chord's own number. The two cells answer from opposite sides.

**X3 (verified) is a structural no-go for the vacuum-row route.** The θ-odd 3-space — the sine-kernel's home, where the chord's σ-visible content lives — is machine-orthogonal to everything any Dehn filling can produce from the vacuum row, at level 2 exactly as at level 1, and by the C = S² argument at every level. The rank being exactly 6 makes it sharp in both directions: fillings hear all of θ-even and none of θ-odd. No slope, no twist sector, no level raises the vacuum row into the odd space. If the chord number exists as an amplitude, it is not extractable from vacuum-row closed-manifold invariants. Candidate remaining probes are the ones this theorem does not cover: non-vacuum rows (covectors seeded at a non-θ-fixed primary), and boundary data that is not C-fixed by construction.

**X2 (failed) does not currently supply the number, but it localizes what a correct Route B must contain.** The salvageable exact content is the torsion sign dichotomy — 1/τ_m positive precisely on the θ-odd blocks {4, 8} — which is B581's relative-i squaring to a relative sign and survives the audit untouched. A rebuilt cross-term must put Vol in the real channel (with CS = 0, the saddle phase is trivially 1, and the real factor exp(±2Vol/ħ_eff) is large/small, not oscillatory), which changes the character of the answer: the interference at u4 = 0 would be a *real, signed, exponentially weighted* quantity rather than a point on the unit circle. The derivative structure dX/du4|₀ = X₀·[(2/ħ)·dS0/du4 − dlogτ_m/du4] remains the right skeleton — dS0/du4 = C1 (the banked Q4 cusp pairing, nonzero at level 2) — but its headline conclusion must be re-derived inside the corrected assembly before anything about u4-dependence is claimed. The transcendence statement is retracted to its computed form: no rational·π relation to 60 digits by PSLQ.

Reading the two together, outcome-neutrally: the program now has one theorem saying where the chord's number is *not* (vacuum-row filling amplitudes, any level) and one audited failure saying what the direct assembly must repair before it can say where it *is*. Both are progress of the same kind — the reachable/unreachable boundary of the θ-odd content is being drawn exactly.

---

## 4. Continuation map

**X1 (blocking):**
- Complete the pending verification (the vreason is a placeholder; nothing banks before it lands). On survival, bank as NO-REAL-FORM with the B578-D10 dependency stated, the swap-involution mechanism as the structural reason, and the empty reality locus scoped to the v4 dial family.
- Widening (post-bank, optional): other dial directions (θ-even blocks; non-highest θ-odd vectors, where c would *not* commute with A27 and the shared-meridian gate becomes a real constraint), and other antiholomorphic involution families — the emptiness is proved for this family only.

**X2 (rebuild, not bank):**
- Redo the one-loop assembly with the standard saddle assignment: CS → phase (trivially 1 here), Vol → real rate exp(±2Vol/ħ_eff); carry the exact 1/τ_m table and the θ-parity sign law over unchanged; preregister the falsifiers this time and state the claim as exactly what is computed.
- The still-open exact scalar: dlogτ_m/du4 via a deformed-family twisted-Alexander run — unchanged by the audit, still the missing piece of the derivative.
- Retract "transcendental" to the 60-digit PSLQ null wherever the number appears.

**X3 (bank + extend):**
- Bank as the second unhearability theorem, with the exact-rational θ/h backbone included (it is the rigorous core). Record the L78/Route-A resolution in OPEN_LEADS — X3 *is* the registered Route A, run in order, closing the process concern raised against X2.
- Extension with the most leverage: non-vacuum-row filling covectors (seed at a θ-swapped primary pair; the C = S² argument does not protect those rows), and a symbolic promotion of the level-independence claim from "MTC theorem verified numerically" to an exact statement in the banked C3 framework.
- Note the disclosed radius sensitivity for reproducers: rank stabilizes to 6 from sweep radius 6 up (rank 5 at radius 4 is undersampling, not structure).

**Process:** on banking, update PROGRESS_LOG + CHANGELOG + CAMPAIGN_STATUS in the same PR; the X1 null and the X3 theorem bank with identical care — the no-real-form result and the unhearability result are both walls drawn exactly, and walls are content.