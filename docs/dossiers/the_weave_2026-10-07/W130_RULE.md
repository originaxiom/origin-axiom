# W130 — GENESIS PF1 on the field's rest state: on the shared fibre, does the principle forbid a field from resting at zero? Every flat datum the record forces, read through non-abelian Hodge; the size of the field that is forced; its square root; and the control with the hole closed (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's choice (2026-10-22), the first of three tests after W129.** W128 found that consistency forces the
  field's kind but not its existence: that rests on one empirical bit, that the particles are massive. In physics the
  Higgs mechanism is itself a frustrated cancellation, a field that cannot rest at zero.
- **The owner's reframing.** The field is not the remainder. It is where the remainder lives, and the field's
  non-cancellation generates it.
- **The question.** Read GENESIS PF1 on a field's rest state: does the principle forbid the zero?
- **The record's prior work (read first).**
  - P024's passage: a bare end admits no finite description, so the end must carry a field.
  - W70 and W71: the audit lane's condensate carries the Higgs's charges locally. A field-free flat end gaps every
    channel only by giving up the dictionary, the R-symmetry or U(1)_em.
  - W75: at a genuine cusp the field is the uniformization in the log frame, with pointwise size 1/(2R) and no free
    number.
  - W81: the lane's condensate (ad(P) ⊗ S) and the ordinary uniformizing Higgs field (End E ⊗ K) are different types,
    and the identification was withdrawn. This arc keeps that distinction.

## The object

- **The rest state of a field on the fibre, by non-abelian Hodge** (Hitchin 1987; Simpson 1990 for punctured curves).
  - Every flat SL(2, ℂ) datum on the shared fibre, the once-punctured torus F, with tame monodromy at the puncture,
    has a unique energy-minimizing (harmonic) metric.
  - With it the datum becomes a Higgs bundle (E, Φ) solving Hitchin's equation F_h + [Φ, Φ*_h] = 0.
  - Φ is the field at rest. Φ = 0 exactly when the datum is unitary (Narasimhan–Seshadri; Mehta–Seshadri at the
    puncture).
- **GENESIS PF1, read on the rest state.**
  - Cancellation completes when Φ = 0, a field resting at nothing.
  - The equation says the curvature equals −[Φ, Φ*], the field's failure to commute with its own conjugate. That is
    GENESIS §1's mathematical form, a commutator that does not cancel, appearing in the field's rest equation.
- **The field the geometry forces: the uniformizing Higgs bundle** on F at its complete hyperbolic metric (curvature
  −1), at every τ.
  - E = K^{1/2} ⊕ K^{−1/2}, with the metric diag(y, 1/y) on the frames (dz^{1/2}, dz^{−1/2}).
  - Φ = c·N dz with N = [[0, 0], [1, 0]].
- **The doublet as the field's square root.**
  - Every non-zero nilpotent element of sl(2, ℂ) is −h ⊗ ε(h, ·) for a doublet h, unique up to sign; the nilpotent
    cone is ℂ²/±1.
  - For the uniformizing Φ, h is a section of E ⊗ K^{1/2} = K ⊕ O.
- **The control: the hole closed.** The torus without its puncture has χ = 0. Its uniformization is flat and
  F_h = 0, so a nilpotent Φ must vanish.

## Weave or thread

**WEAVE-type.**
- The shared fibre at every point of its Teichmüller space, the τ-line every move acts on.
- Every flat datum the record forces on it:
  - the geometry, at the fibre's hyperbolic point with Markov triple (3, 3, 3), its images under the moves, and
    other Fuchsian points;
  - the quaternion common point ρ_Q;
  - the matter's 𝕎 = ρ_Q ⊗ χ_p;
  - the triplet's image group on the weave's surface.
- The claim (the field's existence and its size) is about all of them at once.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| H0 | the instrument, exact (sympy): on the upper half plane with the curvature −1 metric, F_h = diag(−1, 1)/(4y²) dz̄∧dz and [Φ, Φ*_h] = \|c\|² diag(1, −1)/y² dz̄∧dz, so Hitchin's equation holds iff \|c\|² = ¼; Φ = 0 is not a solution | 90% |
| H1 | which forced data force a non-zero field (exact). The geometry: at (3, 3, 3), its images under words in the moves' automorphisms to length 6, and five other Fuchsian points from the Markov-type equation x² + y² + z² = xyz, every generator trace is real and greater than 2 and tr[A, B] = −2, so no point is unitarizable and Φ ≠ 0 at all of them. The quaternion point has tr[a, b] = −2 too, but is unitary (in SU(2)), so Φ = 0: the puncture's −1 alone does not force the field. Its puncture holonomy is −I, while the geometry's is −1 times a unipotent ≠ I. 𝕎 and the triplet's image group (order 96) are unitary, so Φ = 0 | 95% |
| H2 | the size is the remainder (exact). \|Φ\| = ½ pointwise (in curvature −1 units, 1/(2R)), the same at every point and every τ. The parabolic degree of K^{1/2} is (i/2π)∫F = Area/(4π) = −χ/2 = ½, and ∫\|Φ\|² dA = Area/4 = π·deg = π/2, with Area = 2π\|χ\| = 2π (the modular torus Γ′: six modular triangles, exactly) | 90% |
| H3 | the control (exact): with the flat metric (the hole closed, χ = 0), F_h = 0 and Hitchin's equation forces c = 0. A non-nilpotent abelian Φ = a·diag(1, −1) dz solves it for every a, so the closed torus has no floor and no forced field | 95% |
| H4 | the doublet (exact). Every nilpotent [[p, q], [r, −p]] ≠ 0 equals −h ⊗ ε(h, ·) with h = (a, b), a² = q, b² = −r, ab = −p, and h is unique up to sign. For the uniformizing Φ, √c·h = (0, √c) in K ⊕ O, which vanishes nowhere, with \|√c·h\|² = \|c\| = \|Φ\| = ½ | 95% |
| H5 | the read-out: the table of forced data (unitary or not, the field forced or not, its size); the doublet; and a READING by hand on which group the field lives in, whether it couples to the chiral three (B1651), and what it does and does not supply for W128's empirical bit | — |

## What the outcomes mean (fixed now)

- **H0 to H4 hold.** Then GENESIS PF1, read on the rest state, forbids the zero of exactly one field: the geometry's
  own Higgs field, the fibre's uniformization.
  - Its non-commutation with its own conjugate is the hole's curvature.
  - Its size is fixed at ½ in curvature units, at every point and every τ. Its integral is π times the parabolic
    degree −χ/2.
  - With the hole closed, it must vanish.
  - The matter's flat data carry no field at rest. The quaternion point shows that the puncture's −1 alone is not
    enough: the field lives in the unipotent part of the geometry's puncture holonomy, the cusp.
  - Its square root is a nowhere-vanishing doublet, of the fibre's SL(2), not of the weak SU(2).
  - **So the principle does force a field not to rest at zero.** Whether that supplies W128's empirical bit (non-zero
    masses) depends on two links this arc does not supply:
    - the dictionary between the fibre's SL(2) and the weak SU(2) (GENESIS FK11), with W81's type distinction kept;
    - the field's coupling to the chiral three, which B1651 places at the puncture.
  - Both are named in the read-out as open.
- **H0 fails.** The instrument's conventions are wrong. It is recorded, and nothing in H2 to H4 is read until it is
  resolved post hoc.
- **H1 fails.** Some forced datum is not where it was predicted. It is recorded with the datum, and the reading
  follows the data.
- **H3 fails.** The hole would not be what forces the field. That is recorded, and it would undercut the reading.

## What stays out

- Any four-dimensional potential, the size of v, and the scale.
- The couplings, which are B1651's and B1654's. The dictionary.
- The family of the field over the τ-line and its end at the modular cusp. In particular whether the field's
  coefficient, a section of the Hodge bundle λ, relates to GENESIS FK10's unit λ¹² ≅ O(δ) is a lead named here, not
  tested.

## Seen before the rule (disclosed)

- **Read:** P024 and its correction and addendum; W70, W71, W75 (with chat1's ½) and W81; main's B1651 and its audit
  B1655; W22 (the odd spin structure, the only one every move fixes).
- **By hand:**
  - H0's curvature and commutator, giving |c|² = ¼. This agrees with W75's ½.
  - The nilpotent square root in H4.
  - The degree arithmetic in H2.
  - That the quaternion point has commutator trace −2.
- **Not run:** no script, and no census of the moves' images or of other Fuchsian points.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
