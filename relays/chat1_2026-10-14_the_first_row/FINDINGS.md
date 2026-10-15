# The first row: at leading order the record gives |U_e1|² = 1 or at most ½, and nature's 0.675 lies in the gap

> **2026-10-15, the audit of the negatives** (`../chat1_2026-10-15_audit/AUDIT_OF_THE_NEGATIVES.md`, auditor B). The arithmetic holds.
> - **"chat1's floated escape is closed" is wrong as worded.** It is closed only for one condensate per leg.
>   - With both condensates on one leg the coupling has rank 3 in general. With 8 free real parameters it fits the
>     whole first row and Δm²₂₁/Δm²₃₁ at τ = i, 1.5i and ω: a fit, not a prediction.
>   - On a cubic surface of Higgs directions it keeps a massless ν₁ off R, with |U_e1|² across [0, 1].
>   - Nature does not require a massless ν₁.
> - **The headline holds only as scoped:** one fibre, one τ, one coupling point, one R, one condensate per leg, and the
>   Hodge–Riemann metric. Each of these reaches the gap:
>   - couplings at different fixed points: B1651's U6, squared, gives 0.653, 0.620 and 0.591;
>   - two moduli: R(i) against R(ω) gives 0.825;
>   - the one-leg placement;
>   - T-NORM.
> - **§4's "RL as the charged leptons' residual and B1649's leading order cannot both hold" is wrong as worded.**
>   - R(ω) is an isotropic eigenline of RL, with eigenvalue ω. What is incompatible is TM1's ⅔ row assignment.
>   - "Only 9.7° off R" is a minimum: TM1's own line needs 17–31°.
> - **§5's P-128 reading** ("a Dirac pairing would be lifted") is contradicted in its lifting half by main's later,
>   firewalled finding: at a point, no flat line lifts the zero.

chat1, 2026-10-14, evening. The second of the three cheap checks chat1 proposed after the owner's "continue".
- **Sealed** at `53b7f3f88` (sha256 81ca4a63…) before any code.
- **The script** `first_row.py` was committed at `f549a9433` before its one run (506 s). Its output, `run.txt` and
  `first_row.json`, was committed unread at `208e5dce7`.
- **One labelled post hoc check**, `post_hoc_omega.py` and its output (`96bb88613`).
- **An independent referee** (an agent of chat1's, read-only) re-derived the bound, re-ran the cells and checked the
  seal. No blocker. Its two major points change the readings below (§ Referee).
- **Every cell held as sealed. 0 of 19. No arc number claimed. Nothing to CLAIMS.md, GENESIS or the ledgers.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q0 (controls) | TM1's column reproduced; R isotropic; the units' frame consistent | 97% | **HOLDS.** Column error 2.5e-16. \|R·R\|/\|R\|² ≤ 5.7e-16 (numpy) and ≤ 8.6e-32 (mpmath). f_L ⊥ f_R to 2e-17; σ_B of the three axes is 1. Every generator is real up to a scalar in the frame (≤ 5e-16) |
| F1 | the bound on 2·10⁵ random pairs and 200 adversarial maximisations; sharp at 25 points | 99% | **HOLDS.** Largest random excess −4.7e-10. Adversarial +1.7e-12, which is square-root round-off near σ = 1. Sharp pairs attain the bound to 4e-16 |
| F2 | the invariant symmetric form on T is unique and unitary up to scale | 90% | **HOLDS.** One solution; singular values equal to 1e-16; invariant under all 96 elements to 2.5e-15 |
| F3 | TM1's neutrino line is real; RL's basis is (real, isotropic, isotropic); the ⅔ sits on the real one | 92% | **HOLDS.** σ_B = 1.000 for the line; (1e-15, 1e-15, 1.0) for RL's basis; entry 0.6667 on the real vector |
| F4 | **the cap:** the largest overlap of R̂ with a real unit vector is ½ at every τ; TM1's line against R̂ is ≤ ½ in all 24 frames | 97% | **HOLDS.** ½ to 3e-16 at all 8 τ. Over all 24 frames, TM1's line against R̂ is at most ½ + 2e-16 |
| F5 | one fibre, every neutrino operator built on the puncture's couplings: \|U_e1\| = 1 | 96% | **HOLDS, 54 of 54 cases.** \|1 − \|U_e1\|\| ≤ 4e-16; \|U_e2\|, \|U_e3\| ≤ 3.6e-15; m_e/m_τ ≤ 1.2e-16; m₁/m₃ ≤ 1.6e-16 (the hook, type I, type I + II) |
| F6 | Reading B (conditional): ν₁ = e_t, rank 2, \|U_e1\|² = \|R_t\|²/\|R\|² ≤ ½; both sectors give 1 | 92% | **HOLDS.** m₁/m₃ ≤ 2e-32; smallest m₂/m₃ 1.4e-3; null line e_t to 3e-16; largest \|U_e1\|² 0.5000; both sectors \|U_e1\| = 1 to 2e-16 |

## The read-outs

- **TM1's line against R̂ in W49's labelling.**
  - On τ = iy it is the same in all four sign classes. It equals the hand value (θ₃⁴ + θ₄⁴)/(4θ₃⁴) to 4e-16.
  - Values: 0.270 at y = 0.6, **⅜ at τ = i**, 0.493 at 2i, and → ½ at the cusp.
  - Off the axis it depends on the sign class. At ω it is ⅙ in two classes and ½ in two.
- **Over all 24 frames**, the range per τ runs from 0 (at i) to at most ½.
- **|R_t|²/|R|²**, which is Reading B's |U_e1|².
  - For t = k it is ½ on the whole imaginary axis, as θ₂⁴ + θ₄⁴ = θ₃⁴ requires.
  - For t = i it falls from 0.46 (y = 0.6) to 0 at the cusp. For t = j it rises from 0.04 to ½.
  - At ω all three are ⅓.
- **Both condensates on one leg,** sym(Y(a)·AB). The smallest singular ratio lies between 2e-5 and 0.31: rank 3. There is
  no massless neutrino, so the hook does not survive that placement.
- **The weave's 13 real axes against R̂.** The largest overlap is exactly ½ at i, 1.5i, 2i, 4i and ω, and 0.498 to
  0.4999 elsewhere. The cap is reached; it is never passed.
- **The data line.**
  - |U_e1|² = (1 − 0.3092)(1 − 0.02248) = **0.6753 ± 0.0085**: 20.6σ above ½ and 38.2σ below 1.
  - With the electron along R, ν₁ needs σ ≤ 0.937 (0.943 for TM1's ⅔).
  - With a real ν₁, the electron must turn at least 10.26° off R (9.74° for ⅔).
- **Post hoc** (labelled; `post_hoc_omega.json`). At τ = ω, in the frame where RL fixes ω (class (+, +, +)):
  - R is exactly one of RL's isotropic eigenlines, with overlap 1.000.
  - RL's real axis, the one TM1 gives the electron, is another line.
  - Near the cusp R tends to L's isotropic eigenline in every class.
  - Both facts are on the SM seat's record already: W68 G2, "all three weight −½ sections lie on ℓ_ω = (−ω, 1, ω²)",
    the real axis being (1, −1, −1); and W65 H3 with HARVEST row 1118 for the cusp. This reproduces them; it is not
    new.

## What it shows

1. **A cap.** **[MATH, proved and checked]**
   - An isotropic direction and a real one overlap by at most ½: |⟨u, v⟩|²/(|u|²|v|²) ≤ ½.
   - In general the overlap is at most ½(1 + σ_uσ_v + √((1 − σ_u²)(1 − σ_v²))), and the bound is sharp.
   - It does not depend on which side of a mass term is conjugated, since σ is unchanged by conjugation.
   - The bound is elementary. σ is the concurrence of the magic basis (Hill–Wootters), and the isotropic-against-real
     case is circular against linear polarisation. Its use here is the content.
2. **At leading order on the residue route the first row is 1 or at most ½.** **[MATH, given the premises below]**
   - |U_e1|² = 1 for every neutrino operator built on the puncture's couplings on the electron's fibre: the hook
     (Weinberg-shaped), type I with its Dirac coupling at the puncture, and type II.
   - |U_e1|² ≤ ½ for every real neutrino direction. That includes every axis of the weave's group (the cap is reached at
     five of the eight τ) and Reading B's block vector e_t.
   - **chat1's floated escape is closed.** Reading B moves the neutrino to e_t. If only the neutrinos see the
     condensates, |U_e1|² ≤ ½. If both sectors do, as puncture parity requires of B1644's pairing, both move to e_t
     and |U_e1| = 1 again.
   - Nature's 0.675 lies strictly between.
3. **What reaching 0.675 takes.** **[MATH, in the Hodge–Riemann metric]** One of three things:
   - **an electron turned at least 10.3° off R** with a real ν₁: a charged-lepton lift of that angle (sin² ≈ 0.03).
     For scale only, a Gatto–Sartori–Tonin-type angle √(m_e/m_μ) is 4.0°;
   - **or a neutrino direction that is complex, with σ ≤ 0.94, and is not R.** A sector-dependent R does this
     (P-128). So does any of P-129's other premises failing: a bulk Higgs's overlaps, an R′ from another spin-structure
     assignment, or a leading order beyond the residue;
   - **or a physical metric on the zero modes that is not the Hodge–Riemann one** (T-NORM).
     - The cap holds in the metric where the bilinear and Hermitian forms are compatible.
     - The referee's example: at τ = i a weight κ on the k mode gives |U_e1|² = κ/(1 + κ) against e_k, so κ = 2 gives ⅔
       and κ ≈ 2.08 gives 0.675, with no lift at all.
     - **So T-NORM bears on the PMNS, not only on the mass ratios.**
4. **TM1 (P10), scoped.** **[READING]** This withdraws the preregistration's reading, "a third incompatibility,
   independent of the tensor".
   - **As a mechanism.** TM1 puts the electron on RL's real axis, at least 45° from R.
     - Where all of the weave's group is flavour, B1625's tensor result already excludes TM1 for the residue route,
       whose couplings are T ⊗ T (the record's §68 answer; P-105: T̄ ⊗ T is degenerate on the fibre).
     - In W44's frame, where c is gauge and TM1 returns under T ⊗ T, the cap is the obstruction. RL as the charged
       leptons' residual and B1649's leading order cannot both hold.
   - **As an observable.** P10's relation (|U_e1|² = ⅔, |U_μ1| = |U_τ1|) needs the electron only 9.7° off R with TM1's
     real ν₁. That is the same size of lift nature's value needs (10.3°).
     - So at P10's level the cap sharpens B1649 §3's obstacle. It adds no new incompatibility.
     - P10 stands as registered.
   - **At ω** (post hoc; W68's G2). In the frame where RL fixes ω, R is one of RL's isotropic eigenlines. With TM1's
     residuals the residue route's electron would then be the ⅙ row, not the ⅔ row.
     - Which frame is right is B1640's unpinned hand. In two other sign classes RL acts hyperbolically, and in one its
       eigenline is R(ω + 1).
5. **For P-128.** **[READING; firewalled; nothing computed]** Suppose P-128's form holds, R_r ∝ θ_r(ū)θ_r(δ), with ū and
   δ the half-sum and half-difference of the paired fields' charges.
   - **A Majorana self-pairing has δ = 0.** Then R_ν·R_ν ∝ θ₁(ū)²θ₁(0)² = 0.
   - So the neutrino's R would stay isotropic under any Wilson line, keeping m₁ = 0 and the hook.
   - A Dirac pairing of fields with different charges would be lifted.
   - That is exactly the shape §3 asks for: a sector-dependent direction, with the lightest neutrino still massless. It
     rests on a derivation that is cc's (P-128).

## Premises (each a fence)

- **B1649 applied to leptons**, "by the same reading" (its §3): the charged leptons on the electron's fibre, the same R.
- **The Hodge–Riemann pairing as the physical metric** (W49 M3). The referee checked it directly: the HR form on T is
  4·I₃ in TB's coordinates, and the group is unitary to 2e-15. T-NORM is not tested (§3).
- **The units' frame in B1612's coordinates.** It is fixed up to 6 labellings and 4 sign classes. The cap holds in all 24.
  The read-outs depend on the frame (B1640's hand).
- **F5's type I** assumes the Dirac coupling at the puncture on the same fibre. "The hook" and "type II" are labels
  for sums of B1645's Y(a), not derivations.
- **F6 assumes** the generation index is the block space 3_B. The both-sectors variant also uses the two-condensate
  parity rule from chat1's `condensate_in_M`, which is not banked.
- **Index conventions.** Which index of the charged leptons' matrix is the doublet's does not matter, since B1649's
  kernel is two-sided.
  - B1649's `mixing()` takes left singular vectors (R̄). F5 takes right singular vectors (R).
  - Each is consistent on its own and gives |U_e1| = 1. Mixing the two conventions would give 0.

## Referee (an agent of chat1's, read-only)

**Verdict.** "the mathematics, numbers and code are sound and every cell holds for the right reason. But the TM1 'third
incompatibility' is a statement about mechanism and depends on the frame; at P10's observable level it is B1649 §3's
obstacle again."

- **Major 1. Independence from the tensor.** Taken. §4 is scoped: in B1625's frame the tensor already excludes TM1 for
  the residue route; the cap is the operative obstruction only in W44's frame.
- **Major 2. TM1's mechanism against P10's observable.** Taken. §4 now separates them: a turn of at least 45° for the
  mechanism, 9.7° for the observable.
- **Minor.**
  - The post hoc result is W68 G2, and the cusp limit is W65 H3 and row 1118: credited.
  - Several cells are true by construction (σ_B of R in the frame; F4 given F1–F3; F6's null line): noted.
  - "One of two things" was not exhaustive: §3 now names T-NORM and P-129's premises.
  - The convention wording and the unlisted premises are now in § Premises.
  - The concurrence anchor was added.
- **Verified by the referee.**
  - The proof is complete.
  - The bound is attained on an 11 × 11 grid; 3·10⁵ random and 300 adversarial pairs in ℂ², ℂ³ and ℂ⁵ show no
    violation above 1e-13.
  - The cap holds in all 24 frames. All numbers check, and JUNO's value is confirmed at source.
  - The numpy R equals B1649's R_of and the kernel of Y_of to 3e-16.
  - The seal is intact.
  - No earlier overlap bound, and no earlier B1649-against-TM1 statement, was found on main, the SM seat or the audit
    branches.

## Fence

- **Object.** The leading order on the residue route. The weave's group on T from main's banked B1611/B1612 at
  `60c5470ae`. Reach: the record's candidate neutrino directions, on an 8-point τ grid and the imaginary axis.
- **Not tested.**
  - Any lift. P-128's Wilson line (cc's, firewalled). T-NORM. H-RES. The parent map (P-108). Inverted ordering: a real
    massless ν₃ against an isotropic electron is allowed by the cap, since |U_e3|² ≈ 0.02.
- No value. **0 of 19.**

## Files

`PREREGISTRATION.md` (sealed), `first_row.py` (its one run), `run.txt`, `first_row.json`; post hoc `post_hoc_omega.py`,
`post_hoc_omega.json`, `post_hoc_omega_run.txt`.
