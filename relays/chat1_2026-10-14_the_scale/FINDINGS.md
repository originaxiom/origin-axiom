# The weave sees the quantised level but does not fix the hierarchy; at a genuine cusp the field's size is the curvature's (post hoc), not a free ℝ₊

> **2026-10-15, the audit of the negatives** (`../chat1_2026-10-15_audit/AUDIT_OF_THE_NEGATIVES.md`, auditor C).
> - "Does not fix the hierarchy" holds with k and σ as independent couplings in the classical action. Frameworks where
>   the levels lock (chiral gravity, c = 24k) are untested.
> - "Every amphichiral thread sits at 0" holds to length 18.

chat1, 2026-10-14. This check covers the premises of chat1's answer to the owner's scale question.
- **Sealed** at `c1986e33d` (sha256 78fa6de2…) before any code.
- **The script** `the_scale_check.py` was committed at `87f3904b3` before its one run. Its output is `run.txt` and
  `the_scale_check.json` (`1baa2090e`).
- **Instruments.** SnapPy 3.3.2, the record's `b++` convention. sympy, exact.
- **Every cell held as sealed.**
- **One post hoc computation**, labelled: `post_hoc_pointwise.py`, committed at `3482a8936`, before its one run; output
  at `28bb46c83`. It corrects the seal's reading of K4, not a cell.
- **Revised after an independent referee** (chat1's agent, read-only). Its findings are taken in the text below and
  in `THE_SCALE.md`.
- **0 of 19.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q0 (control) | b++LR = m004 with Vol 2.0298832128 and CS = 0; Guéritaud–Futer on all 745 threads; all geometric | 95% | **HOLDS.** Identify gives m004. \|CS\| = 2.9e-15. No Guéritaud–Futer violation and no failure; all 745 are "all tetrahedra positively oriented" |
| K1 | at least 80% of threads have CS ≢ 0 mod π² | 90% | **HOLDS: 690 of 745 (92.6%).** Their action S = −CS·k − Vol·σ depends on the quantised level k |
| K1b | swap-symmetric threads have 2·CS ≡ 0 | 95% | **HOLDS, 55 of 55** |
| K2 | mirror pairs: equal Vol, opposite CS | 97% | **HOLDS on all 745** (Vol to 1e-9, CS to 1e-6). SnapPy's own orientation reversal agrees (read-out) |
| K3 | Vol(L^aR^b) < 2v₈ = 7.3277 for a, b ≤ 25 | 95% | **HOLDS.** The maximum is 7.2651, at a = b = 25 |
| K3b | Vol(L^aR^b) strictly increasing in a and in b | 85% | **HOLDS, no violation** |
| K4a | h = diag(L⁻¹, L) solves Hitchin's equation for θ = E₁₂ dz/z; unique in the ansatz | 97% | **HOLDS, exactly.** The ansatz gives a₁ = −1, a₂ = 1, c₁ = c₂ only. The reduction was checked against the direct computation at four exponent sets; only the first solves |
| K4b | the residue's operator norm in h is 1/L | 97% | **HOLDS:** 1/L |
| K4c | the horocycle \|z\| = r has length 4π/L, so \|Res\|_h = length/4π | 97% | **HOLDS, exactly** |
| K4d | sign control: this convention uniformises (curvature −4); the opposite gives +4 | 97% | **HOLDS.** The cusp metric solves the uniformising equation in this convention and not in the opposite one. The round metric does the reverse |
| K4e | semisimple control: flat metric, constant norm \|λ\| | 97% | **HOLDS** |

**Read-outs (no prior).**
- **Only the swap-symmetric threads have CS = 0.** All 55 swap-symmetric threads have CS = 0 exactly; none has π²/2.
  No other thread has 2·CS ≡ 0. To length 12, then, the threads that cannot see k are exactly the amphichiral ones:
  LR, LLRR, LLLRRR, LLRLRR, …
- **The size of CS.** |CS| has median 0.78 and maximum 2.27, against a lattice of π² = 9.87. For example,
  CS(LLR) = −0.41123 = −π²/24 to 12 digits.
- **Vol(L^aR^a)** for a = 1, 2, 3, 5, 10, 25 is 2.0299, 3.6639 (= v₈ exactly), 4.8138, 6.0670, 6.9548, 7.2651. It is
  still 0.063 below 2v₈ at a = 25, and Guéritaud–Futer's bound is sharp.
  - **Credit.** B207 Part 3 had already banked that the metallic volumes Vol(L^mR^m) are bounded and tend to about 2v₈,
    with silver equal to v₈. B207 was on the seal's seen-first list. The seal's line "no other thread's volume … has been
    looked at" is true of what chat1 read before the run, not of the record.
- **The harmonic metric is anisotropic on End₀.** In h, the sl₂ directions E₁₂, H, E₂₁ have operator norms L⁻¹, 1, L.

## What it shows

1. **The weave is not blind to k.**
   - B1012's equivalence, blindness to k ⟺ CS = 0, holds thread by thread. On the weave CS = 0 picks out a small set:
     the 55 swap-symmetric threads of 745 (7.4%) to length 12. The root is one of them.
   - That CS = 0 occurs only on swap-symmetric threads is empirical to length 12, not a theorem.
   - The other 690 see the quantised level, in mirror pairs ±CS.
   - So "the scale term is invisible to the object in principle" holds for m004 and the amphichiral threads, not for the
     weave. That is `THE_LAMBDA_POSITION.md` §1's wording; B1012's own is "relocated to a place the object cannot see in
     principle".
2. **Seeing k does not fix the hierarchy.**
   - In S = −CS·k − Vol·σ, k multiplies the parity-odd CS and σ multiplies the parity-even Vol. k is an integer.
     σ = ℓ/4G = c/6 is the continuous one, and it carries the hierarchy (B1015's A2).
   - **Credit.** The record made this point on 2026-08-10: B1023's blocker 2, and B1015's addendum v2. B1012 proves
     blindness in k only, and ∂S/∂σ = −Vol ≠ 0. The addendum withdrew "the level the observer can set and the object
     cannot" and marked A2 HELD-PENDING-L154. L154 carries an internal candidate, σ = 1 (c = 6 = c((E₆)₁)), UNDECIDED
     (B1034).
   - **[MATH]** Guéritaud–Futer's bound gives Vol < 2n·v₈ for every thread with n syllable pairs. Adding 2 to an
     exponent keeps both n and the mod-2 class. So every mod-2 class holds infinitely many threads of bounded volume, and
     weighting the weave by its own action, Σ e^{−σ·Vol/π}, diverges at every σ in every such class.
   - The check confirms the instrument against the bound: L^aR^b climbs to 7.265 and does not pass 2v₈ = 7.328.
   - **[READING]** That route cannot select σ. By the seal's own fence, K3 "does not show that nothing fixes σ". A2's
     status is unchanged: HELD-PENDING-L154. What the weave adds concerns L154, in both directions.
     - **It opens.** B1064's first leg ("amphichirality deletes the quantized sector") does not hold on the weave: the
       690 chiral threads keep that sector. That is the mechanism B1064 named as missing.
     - **It costs.** B1228's "k = 1 by inventory" rested on the root's blindness, so on the weave k = 1 becomes a choice
       with consequences.
     - See `THE_SCALE.md` §3 and §5.
3. **At a genuine cusp the residue shrinks, but the field does not.**
   - **[MATH]** For a nilpotent residue, the harmonic metric is exactly h = diag(L⁻¹, L) in the model. The residue's
     norm in h is 1/L, which is the horocycle's length divided by 4π. By Simpson's estimates the same holds up to a
     bounded factor for every tame harmonic bundle with that residue. It decays into the cusp and is zero at the
     puncture.
   - **[MATH, post hoc]** (`post_hoc_pointwise.py`, written after the run and labelled.) The field is the 1-form
     θ = Res·dz/z, and dz/z grows into the cusp: on a unit vector of the complete metric it is L/2. The two factors
     cancel exactly. **The field's pointwise norm is ½ everywhere in the cusp**, and the uniformising Higgs field's is
     constant too.
   - This is the split the audit lane's cusp condensate already shows: its coordinate field q = E/(2√y) decays, while
     the physical q̂ = E/2 is covariantly parallel.
   - A semisimple residue (a puncture opened past κ = −2) has constant residue norm |λ| (K4e). So its field's pointwise
     norm grows into the cusp like |λ|·L/2. This was the referee's catch, checked by hand from K4e and the post hoc
     factor L/2.
   - Off the cone, then, the cut re-enters: that is where m₂ lives (O5).
   - **[READING, given H-RES; the field in M, a flavon]** The field's size is not a free ℝ₊. Non-abelian Hodge fixes
     the field from the thread and τ.
     - On the cone its pointwise size is ½ in the model. In general it stays of order one (Simpson's bounds).
     - **Withdrawn:** the seal's reading "set by where the cusp is cut". It took the residue's norm in h for the field's
       size, and the post hoc computation shows the two differ.
     - On the cone the field brings no scale of its own. Off the cone the departure's size depends on the cut.
   - The model metric is not unique: diag(1/(L+b), L+b) also solves, with pointwise norm L/(2(L+b)) → ½. K4a's
     uniqueness holds only within its power-law ansatz.
4. **The mass ratios on record are not yet in a physical normalisation.** **[OPEN]**
   - **[MATH]** In h, the sl₂ directions of End₀ (= M) have operator norms L⁻¹, 1, L (read-out).
   - **[MATH]** B1644–B1649's rank and kernel statements do not depend on any inner product, so they survive: the
     massless first generation, V = 1 ⊕ U(2), the five zeros.
   - B1645–B1646's sizes and ratios were read in the theta and quaternion frame, with its Euclidean product. Under
     H-RES the physical normalisation would be the zero modes' L² norms in (h, g), and off the cone it depends on the
     cut. That has not been checked.

## Fence

- **Frame and object.**
  - The threads are b++ words, length 2 to 12 (745), and L^aR^b for a, b ≤ 25.
  - The local model is the punctured disc.
  - Reach: *members* for the threads; *class* for the local model (Simpson's theorem carries it to every tame harmonic
    bundle with a nilpotent residue, up to bounded factors).
- **Not tested:**
  - any value of c;
  - any 4D statement;
  - H-RES;
  - whether the end's depth is forced (FK10);
  - the electroweak condensate's size;
  - the recomputation in point 4.
- **A correction to the seal's text.** Its fence says the electroweak condensate's size is "still unsourced (B1017)".
  That is a misattribution: B1017's unsourced slot is the *direction* of E₆'s VEV ⟨1⟩, the rank closing. The audit
  lane reports the condensate's physical q̂ = E/2 as covariantly parallel, and says no measured Higgs scale is
  determined.
- No value, no count. **0 of 19.**
