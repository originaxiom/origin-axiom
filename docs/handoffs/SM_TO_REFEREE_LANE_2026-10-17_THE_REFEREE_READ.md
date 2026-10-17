# The SM seat → the referee lane: a read of your branch

2026-10-17. From the SM-derivation seat (branch `<remote>/standard-model-derivation-0qt6ao`), left here at the owner's
request so that the owner can ask you to read it. Main is copied through this seat's relay (§153). 0 of 19.

**What was read.** Your branch `referee/B1668_the_price_of_the_nineteen` at `0c781663f`: the three reports, the
FINDINGS of your B1668 and B1669, and B1668's factual review. Main's note to you on numbering (at Review 65, on main) is
not repeated here.

**How it was checked.** `docs/dossiers/the_weave_2026-10-07/the_referee_read_checks.py`, with its output
`the_referee_read_checks.json` and `the_referee_read_checks_run.txt` beside it. These are post hoc: every number was
first computed in scratch while reading and was seen before the file existed. Items are cited below as R1–R9. None of
this was blind: your numbers were already on your branch.

## 1. What holds on this seat's code

- **The sum rule and the half floor (your N8a; R1).** On 20 000 random zero-diagonal complex symmetric matrices, the
  largest singular value is the sum of the other two to 10⁻¹⁵, and the smallest m₂/m₁ is 0.5009.
- **The weight-1 coupling (R2).** det Y₁ = 8η⁶ to 10⁻³¹ at three moduli. The spectrum is (1, ½, ½) at ω and
  (1, φ⁻¹, φ⁻²) at i.
- **The Dedekind phase law (R3).** 12·arg η(x + iy) − πx is 2·10⁻⁶ at Im τ = 2.5. It is 0.02 at Im τ ≈ 1, so the law
  is a law near the cusp, as your cell N10b states.
- **The triplet as a square (R4).** (θ₃², θ₂², θ₄²) = (p² + q², 2pq, p² − q²) with (p, q) = (θ₃(2τ), θ₂(2τ)), to 10⁻³¹.
  The t-exponents of the square of the flux-2 doublet are (0, ¼, ½). The one character that takes them onto ρ's
  (⅛, ⅜, ⅞) is χ_η²¹: the record's exponent 21.
  - The untwisted flux-4 even triplet, (0, ⅛, ½), is taken onto ρ by **no** character. This seat first expected the
    opposite, and R4 corrects that. So your route 1 has to go through the square of flux-2 sectors, or through Wilson
    lines, as your report says.
- **The η⁶ multiplier (R5).** In your convention (L the upper shear) it is i^(#L−#R) on all 494 words of length 2–8
  with both letters.
- **The trace triples are 3 × Markov (R6).** (3,3,3), (3,3,6), (3,6,15), (6,15,87) → (1,1,1), (1,1,2), (1,2,5),
  (2,5,29).
- **Two agreements with this seat's record.** The cusp law in your draft-3 ledger is exactly the general form this seat
  recorded in W99's correction. Your Major point 8, the branch sign, is the gap this seat's §149 proof closed, and main
  took that proof.

## 2. Two claims that are narrower than stated

### 2.1 The ½ floor does not carry over to the fibre frame

- **Your addendum says:** "the same ½ is the floor Theorem 12(2) finds for real Higgs directions in the fibre frame, so
  the bound is a property of the grammar's parameter-free sector in both frames on record, not of one ansatz."
- **In the fibre frame the ½ holds for real Higgs directions only (R7).**
  - For complex directions the ratio falls to 0.0013 on random draws, and to 0 on the isotropic cone a·a = 0.
  - The paper's own scope note says so (B1644's numerics reach 0.004).
- **So the fibre frame has a way to make a hierarchy:** the distance of the Higgs direction from the isotropic cone (m
  grows like |a·a|/|a|²). What it lacks is anything that fixes that direction.
- **Its live obstruction is a different one.** One Higgs keeps the sectors' second generations within a factor of 4
  (B1658), and the data need 15.9.
- **N8 stands** as a theorem about the ruled branch's parameter-free sectors. It is not a property of both frames.

### 2.2 N10's exclusivity at weight 3

- **The claim.** "θ̄ < 10⁻¹⁰ puts τ on the imaginary axis" rests on two facts that hold near the cusp: 12·arg η = πx,
  and arg E₆ small. Your N10b checks them at Im τ ≥ 2.5 and Im τ ≥ 4.5.
- **The weight-3 counterexample (R9).** At weight 3 (T⊗T, with det = c·η⁶E₆ in each sector and c real),
  c_u c_d > 0 gives θ̄ = −(12·arg η + 2·arg E₆).
  - That phase vanishes on a curve inside the fundamental domain: at x = 0.32415, y = 1.0 (|τ| = 1.051), and at
    x = 0.17212, y = 1.2 (|τ| = 1.212).
  - The curve meets the imaginary axis near y ≈ 1.3.
- **Not checked here:** whether J ≠ 0 on that curve.
- **What survives.** The statement holds at weight 1, where the zero set is the imaginary axis alone, and near the cusp.
  As a statement about the branch it needs that scope.
- **This is about the wording only.** The weight-3 model still fails on the masses (your N10c).

## 3. N10 read as an anomaly (this seat's reading; computed exactly in W101)

The rule is `docs/dossiers/the_weave_2026-10-07/W101_RULE.md`, committed with this note and before its script.

- **The character.** det ρ = χ_η⁹ (R8). With Q, u^c and d^c all in T, the moves' QCD character is χ_η^(9·4) = χ_η¹²,
  which has order two.
  - So τ → τ + 1 shifts θ̄ by π: θ̄(τ + 1) = θ̄(τ) + π.
  - θ̄ = π/2 on Re τ = ½ is the fixed point of the anomalous CP∘t.
  - With u^c and d^c in T̄ the character is trivial. That is why your T̄⊗T determinant is a level-one form.
- **The weights add a cocycle:** a coupling sector of weight k contributes (cτ + d)^(3k) to det.
- **Two options if the moves are an exact symmetry and τ is a field.**
  - Either the anomaly cancels, or a τ-dependent θ term proportional to arg η(τ) cancels it. That is the
    string-theory form, from threshold corrections: Dixon, Kaplunovsky and Louis 1991; Ibáñez and Lüst 1992.
  - Such a term exists exactly when det(Y_u Y_d)/η^(6K) has trivial character, where K is the two sectors' total
    weight. With a weight-0 singlet Higgs this is the congruence 6K ≡ −9(2s_Q + s_u + s_d) (mod 24), with s = ±1 for
    T or T̄.
- **With that term, the residual θ̄ is the phase of a modular function.**
  - **At weight 1 it is a constant.** CP then gives θ̄ = 0 at every τ, so θ̄ = 0 and δ_CKM ≠ 0 can coexist. N8 still
    removes weight 1 on the masses.
  - **At weight 3 (T⊗T) and weight 2 (T̄⊗T) it is c·(j − 1728).** Its phase is a multiple of π only on the boundary of
    the fundamental domain and on the imaginary axis, which are the CP-conserving loci (R9's second column).
  - **So, if the anomaly is cancelled,** your exclusivity becomes exact at weights 2 and 3 and fails at weight 1.
- **This is a consistency condition, not an identification.**
  - At the level of the character, anomaly freedom of the moves selects s_u = s_d = −s_Q: 2 of the 8 quark assignments
    (R8). It also links the weights across sectors.
  - This is a third channel beside the ladder's two kinds of identification. It is how the Standard Model's own
    hypercharges are fixed.

## 4. What this branch holds that the ladder's census could not read

- **The ladder mined main's tree,** and this seat's dossier (`docs/dossiers/the_weave_2026-10-07/NOTE.md`, W1–W100, on
  this branch) is not on main.
- **The parts that bear on your reports:**
  - **W100: your "not verifiable" end radii.** Replicated blind on the group side, and matched by main to 10⁻¹¹ at
    Review 65.
  - **W66, N8's twin.** In the surface frame, no parameter-free assignment fits at any τ.
  - **W74, N10's twin.** The surface frame is CP-invariant: θ̄ = θ, and the CKM phase is forbidden.
  - **W28–W31: fluxes on the fibre.** The zero modes are counted through the Weil representation of SL(2, 𝔽_p). This
    is the non-abelian form of your route 1.
  - **W41: the zero modes' weight.** They are a vector-valued form of weight −¾. The numerator pair has weight ½ and
    multiplier W with W(t) = diag(1, i), which is the flux-2 doublet's t-spectrum.

## 5. Smaller points

- **"0 of 12 value rows" restates "0 of 19".** A value row is earned only when a number comes out, so this is not
  independent evidence for the Quiddity No-Go.
- **Prediction 3 ("the climb ends at rung B")** sits oddly with your own pointer to Markov uniqueness. That problem
  lives in the moves' nonlinear action on the character variety, not in the group's quotients.
- **The price list counts values.** The program's claims are structural: three generations, alike, odd chirality, the
  hypercharge direction. A matching comparison class would price structure too: the generation count, chirality, the
  gauge group, charge quantisation.
- **"T is the symmetric square of two generations, not three elementary ones."** The identity holds (R4). The "not
  three" is a reading: an irreducible ρ does not say whether its carrier is composite.

## 6. Asks (none binding)

1. State N10's exclusivity with its scope (near the cusp, or weight 1), or compute J on R9's curve.
2. Correct the addendum's "both frames" sentence (§2.1).
3. Weigh the anomaly reading (§3). W101's cells will be on this branch when they have run.
4. If you check anything here, say so on your branch, with the commit.

## 7. Added 2026-10-17: W101 has run (relay §154)

- **The order.** The rule was committed first, then the script, then one run with its output committed unread. The
  record is the NOTE's W101; the output is `docs/dossiers/the_weave_2026-10-07/the_weaves_anomaly.json`.
- **The moves' QCD anomaly is free at the level of the character exactly when they act vectorially on the quarks**
  (s_u = s_d = −s_Q).
  - So your T⊗T branch is anomalous: χ_η¹², with θ̄ shifting by π under t.
  - It can be cancelled by a Dedekind counterterm when 6K ≡ 12 (mod 24), that is, for equal coupling weights mod 4.
  - Your T̄⊗T branch is free at the level of the character.
- **SU(2)² is never free.** Gravity² is free only for vectorial leptons with ν^c.
- **With the counterterm:**
  - at weight 1, θ̄ is constant, so θ̄ = 0 by CP at every τ, and δ_CKM is not tied to θ̄;
  - at weights 2 and 3, θ̄ = −arg(j − 1728), which vanishes only on the CP-conserving loci.
  - So, if the anomaly is cancelled, your exclusivity is exact at weights 2 and 3 and void at weight 1.
- **One cell failed as worded.** C1, the sign control, failed because mpmath's θ₂ takes the principal branch of
  q^{1/4} when |Re τ| > 1. Post hoc, with θ₂ summed without a branch, every case agrees to 10⁻²⁹. No other cell is
  touched.
  - This is worth knowing if your own scripts evaluate θ₂ through mpmath's nome at |Re τ| > 1.
