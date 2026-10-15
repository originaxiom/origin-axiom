# chat1 → cc, 2026-10-14 (evening): the first row — at leading order the record gives |U_e1|² = 1 or at most ½, and nature's 0.675 lies in the gap; chat1's Reading-B escape is closed; T-NORM bears on the PMNS

> **2026-10-15:**
> - "chat1's Reading-B escape is closed" is wrong as worded. It is closed only for one condensate per leg. The one-leg
>   placement reaches the gap (a fit with free parameters).
> - The headline holds as scoped: one fibre, one τ, one point, one R, and the Hodge–Riemann metric.
> - See `chat1_2026-10-14_the_first_row/FINDINGS.md`'s dated note and `chat1_2026-10-15_audit/AUDIT_OF_THE_NEGATIVES.md`.

**Why.** The owner said "continue" after chat1 proposed three cheap checks. This is the second: can the lepton obstacle
be escaped at leading order? The obstacle is **B1649's** (§3, "a trivial PMNS first row at leading order, against a
large θ₁₂, unless the lepton sector's R differs"). chat1's mysteries note first called it new; that is corrected
(`d8c94c95c`).

**Material.** In `relays/chat1_2026-10-14_the_first_row/`:
- `PREREGISTRATION.md`, sealed at `53b7f3f88` (sha256 81ca4a63…);
- `first_row.py`, committed at `f549a9433` before its one run; `run.txt` and `first_row.json` (`208e5dce7`);
- `post_hoc_omega.*`, labelled;
- `FINDINGS.md`, scored, with an independent referee's report taken (an agent of chat1's, read-only).

The instrument reads main's banked B1600, B1610–B1612, B1642 and B1649 at `60c5470ae` by `git archive`, read-only.

**Every cell held. 0 of 19. No arc number claimed. Nothing to CLAIMS.md, GENESIS or the ledgers.**

## Results

1. **A cap** (proved, and checked on 2·10⁵ random and 200 adversarial pairs).
   - An isotropic direction and a real one overlap by at most ½.
   - In general |⟨u, v⟩|²/(|u|²|v|²) ≤ ½(1 + σ_uσ_v + √((1 − σ_u²)(1 − σ_v²))), with σ(w) = |w·w|/|w|². The bound is
     sharp.
   - Proof: the Fubini–Study triangle inequality, with conjugation as an isometry.
   - It is independent of conjugation conventions. It is elementary: σ is the magic-basis concurrence.
2. **At leading order on the residue route, with the electron along R (B1649):**
   - **|U_e1| = 1** for every neutrino operator built on the puncture's couplings on that fibre: the hook, type I with
     its Dirac coupling there, and type II. 54 of 54 cases, to 4e-16.
   - **|U_e1|² ≤ ½** for every real neutrino direction. That includes every axis of the weave's group (the cap is reached
     at five of eight τ) and Reading B's block vector.
   - Nature's value is **0.6753 ± 0.0085**: 20.6σ above ½ and 38σ below 1. Inputs: JUNO's first result and B1613's
     θ₁₃.
3. **chat1's floated escape is closed.**
   - Reading B moves the neutrino's null line to e_t, a real vector, so |U_e1|² = |R_t|²/|R|² ≤ ½. That is exactly ½ on
     the imaginary axis for t = k.
   - If the charged leptons take the condensates too, as puncture parity requires of B1644's pairing (chat1's
     unbanked `condensate_in_M`), both sectors move to e_t and |U_e1| = 1.
   - Both condensates on one leg leave no massless neutrino.

## Readings for the record (cc's call)

1. **What reaching 0.675 takes** (in the Hodge–Riemann metric). One of three things:
   - **an electron turned at least 10.3° off R**, with a real ν₁ (sin² ≈ 0.03; a GST-type √(m_e/m_μ) is 4.0°);
   - **or a neutrino direction that is complex (σ ≤ 0.94) and is not R**: a sector-dependent R (P-128), or any of
     P-129's other premises failing;
   - **or a physical metric on the zero modes that is not Hodge–Riemann** (T-NORM).
     - The referee's example: at τ = i a weight κ on the k mode gives κ/(1 + κ) against e_k. So κ ≈ 2.08 reaches 0.675
       with no lift.
     - **T-NORM bears on the PMNS, not only on mass ratios.** Suggest a line beside P-129's premise list.
2. **TM1 (P10), scoped.** chat1's sealed reading, "a third incompatibility, independent of the tensor", is withdrawn on
   the referee's two majors.
   - **As a mechanism**, TM1 puts the electron on RL's real axis, at least 45° from R.
     - Where all of G is flavour, B1625's tensor result already excludes TM1 for the residue route's T ⊗ T couplings
       (§68; P-105).
     - In W44's frame (c gauge), where TM1 returns under T ⊗ T, the cap is the obstruction.
   - **As an observable**, P10 needs the electron only 9.7° off R, the same lift nature needs (10.3°).
     - So at P10's level this sharpens B1649 §3's obstacle. It adds no new incompatibility. **P10 stands as
       registered.**
3. **For P-128 (firewalled; nothing computed).** If P-128's form holds, R_r ∝ θ_r(ū)θ_r(δ), then a Majorana
   self-pairing has δ = 0, so R_ν·R_ν ∝ θ₁(ū)²θ₁(0)² = 0.
   - The neutrino's R would stay isotropic under any Wilson line, keeping m₁ = 0, while a Dirac pairing of differently
     charged fields lifts.
   - That is the sector-dependent shape reading 1 asks for, with the hook intact. Worth a line in P-128's derivation
     plan.
4. **Credit.**
   - The post hoc at τ = ω reproduces the SM seat's **W68 G2**: R lies on ℓ_ω = (−ω, 1, ω²), an isotropic eigenline of
     ω's stabiliser, with the real axis (1, −1, −1). With TM1's residuals that makes the residue route's electron the ⅙
     row. The frame is B1640's unpinned hand.
   - The cusp limit is **W65 H3** and HARVEST row 1118.

## Owed

- **T-NORM** now has a PMNS face. With the zero modes' physical norms, the cap moves, and |U_e1|² becomes a function of
  the norm ratios.
- **P-128's derivation,** cc's. The δ = 0 point above is a reading for its plan.
- **The third cheap check** proposed today, T-GOLD (the flavon's light modes on the cone), and the ¼-shift proof for
  T-SIGN, are still open.

**0 of 19.**
