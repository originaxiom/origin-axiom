# B1642 — THE ZERO MODES' RESIDUE AT THE PUNCTURE IS A COMPUTED COUPLING, BUT NOT THE GOLDEN ONE: the SU(2)-invariant pairing of the weave's zero modes, read at the fibre's puncture, gives Y_pq = ε_pqr κ_r θ_r²/(2πη³) — antisymmetric (the pairing is), so its masses are (1, 1, 0) at every τ, with the θ-triplet itself the massless direction; the golden coupling is the symmetric cubic, which these zero modes do not produce

> *Audited 2026-10-15 by main (P-152, B1655): a FEATURE PRESENTED AS FAILURE: rank two with an exact massless direction; "no flavour structure" withdrawn. The grades, the corrected wording and the checks are in `frontier/B1655_main_audits_its_negatives/FINDINGS.md`.*

**Verdict: NEGATIVE as sealed.** R4 fails; R1, R2, R3, R5 and R6 hold. cc (main), 2026-10-13. Sealed `55bd29ab7` before
the run (and before the SM seat's W59, the same question by another route). No data. **0 of 19.** POINT_REGISTER slot
Q3, first arc (P-088).

## 0. Seen first

As sealed: `VERDICT topic-sweep /residue|puncture|zero mode|overlap|Yukawa|Szeg|duplication/: 128 of 1413 arcs on main match (NEGATIVE 19, OPEN 16, PROVED 92, RETRACTED 1)`.
None computes couplings as residues of the zero modes. Also read before the seal:
- B308, B323, B881 and B884;
- B1636–B1641;
- the SM seat's W21, W41, W49 and its commits to c5f343d14 (W56, W57, the Wilson-line correction, W59 announced);
- Barger, arXiv:2609.09262 (abstract).

**Literature:** Jacobi's duplication identities; θ₁′(0) = 2η³; couplings localized at points of an internal space.

## 1. The sealed run (`verification/residue_coupling.py`, unchanged; `residue_coupling.json`, `residue_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **R1** | Fᵀ ε F = 0 | 99% | **HOLDS** (exactly 0) |
| **R2** | Fᵀ ε C F = c θ_r(0)θ_r(z)/θ₁(z), (i, j, k) → (θ₂, θ₄, θ₃), c = (±1, −1, i) | 85% | **HOLDS** to 10⁻⁴⁰: c = −1, −1, i at all 20 points |
| **R3** | the residues c θ_r²/(2πη³) | 85% | **HOLDS** to 10⁻⁴⁰; θ₂θ₃θ₄ = 2η³ to 10⁻⁴⁰ |
| **R4** | Y's singular values equal the golden coupling's; 1 : φ⁻¹ : φ⁻² on the tick's axis | 85% | **FAILS.** The diagonal is 0, but the singular values are (1, 1, 0) at every random τ and every axis point; the largest difference from the golden coupling's is 0.48 |
| **R5** | each entry carries the third block's character | 90% | **HOLDS:** (+1, −1) for θ₂, (−1, +1) for θ₄, (−1, −1) for θ₃ |
| **R6** | control: B = diag(1, 2) does not factor | 90% | **HOLDS:** misfits 0.74, 0.16, 0.019 |

## 2. Why R4 failed (post-seal, labelled; `post_seal_residue.py`, `post_seal_residue.json`)

- **Y is antisymmetric, for the plainest reason.** The SU(2)-invariant pairing ε is an antisymmetric form, so
  F_qᵀ ε F_p = −F_pᵀ ε F_q for any two vectors, and Y_qp = −Y_pq. The vanishing diagonal (R1) is the same fact.
  Equivalently, the quaternion units anticommute: C_q⁻¹C_p = −C_p⁻¹C_q.
- **Checked at three random τ:**
  - Y + Yᵀ = 0 exactly;
  - Y = [v]×, the cross-product matrix of the vector v of its entries, with |v_r| = |θ_r²|/|2πη³| to ten digits;
  - the singular values are (|v|, |v|, 0), and Y v = 0.
- **The derivation's error was mine, and elementary.** The preregistration called the coupling "zero-diagonal
  symmetric" and carried B1636's sum rule over to it, but an antisymmetric pairing gives an antisymmetric matrix. The
  sealed cell R4 caught it, which is what a seal is for. The identities (R1–R3, R5) were right. Filed as an E1 instance
  (a property assumed, not derived), ERROR_LEDGER.

## 3. What it says

- **The first coupling on the record computed with no free coefficient.** It is the zero modes' own SU(2)-invariant
  pairing, read at the fibre's puncture by a Higgs that carries parity:
  Y_pq = ε_pqr κ_r θ_r(τ)²/(2πη(τ)³), with κ = (−1, −1, i) up to the blocks' labels.
- **Its spectrum is (1, 1, 0) at every τ:** one exactly massless state along the θ-triplet itself, and two degenerate
  massive ones.
  - A flat Wilson line does not change this. It enters the theta factors, but the antisymmetry comes from the pairing
    itself.
  - So this residue alone gives no hierarchy beyond one massless generation, and no golden pattern.
- **The golden coupling is the other cubic.** On the multiplicity space M (the imaginary quaternions, W49), the cube
  group's true invariant is ε_pqr, and the zero modes produce it. The symmetric c_pqr = |ε_pqr| is only a semi-invariant,
  with the sign character (B1641 O3: η⁶'s character). So the golden coupling needs an extra sign-carrying factor that
  these zero modes and this pairing do not supply.
- **Where a symmetric piece could come from** (registered, not computed):
  - a Higgs carrying the sign character as well as parity;
  - a non-holomorphic (Hermitian) pairing in the bulk of the fibre — the SM seat's W59 route;
  - a second Higgs at the puncture.

  In the literature antisymmetric flavour couplings are familiar, from SO(10)'s 120 or the Zee coupling. That is
  context, not a claim.
- **For the free-number count:** this coupling has no free number besides τ and the Higgs's overall size. It is the
  wrong pattern, but it shows a coupling can be computed rather than allowed. The count stays 0 of 19.

## 4. Disclosed

- The Higgs's localization at the puncture and its coupling through the residue are hypotheses. The arc tested what
  follows from them.
- Zero Wilson line.
- The post-seal script reuses the sealed instrument's definitions unchanged (the text before its first cell).

## 5. Files

`verification/residue_coupling.py` (sealed, unchanged), `residue_coupling.json`, `residue_run.txt`,
`post_seal_residue.py`, `post_seal_residue.json`; the lock `tests/test_b1642_the_zero_modes_residue.py`.
