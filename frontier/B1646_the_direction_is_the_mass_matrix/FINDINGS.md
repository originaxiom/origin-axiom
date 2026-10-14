# B1646 — THE DIRECTION IS THE MASS MATRIX: a Higgs in M maps its direction one-to-one onto the two massive generations' symmetric mass matrix; a symmetric potential puts it on the isotropic cone or the real locus, never between; nothing on the record fixes it

**Verdict: PROVED.** Every cell holds as sealed. cc (main), 2026-10-14. Sealed `0bbbb6cab` before the run. No data.
**0 of 19.** POINT_REGISTER P-115.

## 0. Seen first

As sealed: `VERDICT topic-sweep /vacuum alignment|flavon potential|isotropic cone|Higgs's direction|complex triplet|mass matrix of the second|Takagi|Cabibbo.*zero|first generation.*mix/: 2 of 1417 arcs on main match (NEGATIVE 1, PROVED 1); 10 other lanes match`
— B1644 and B1645.
- The SM seat's W56 (pinned d7d41817) was read before the seal. Its setting has free coefficients, and it concludes
  that a field selecting only the Higgs's direction cannot make the fit predictive.
- Here the coefficients are fixed by the residue, so the direction is the only freedom; this arc measures that freedom.

**Seen late** (after the run, disclosed; Review 63 found that sealed sweeps miss older vocabulary, P-123):
`VERDICT topic-sweep /\bvev\b|vacuum expectation|Yukawa hierarchy|inter-generation|flavon|vacuum direction|vacuum alignment|rank.one Yukawa|massless (first )?generation|two massless/: 38 of 1419 arcs on main match`.
Two bear directly on this arc:
- **B990** (PROVED, the E₆ era): "an orbit invariant is constant on the orbit, so it cannot pick a point". D4 is an
  instance of that law. The symmetric potential picks an orbit type (the cone or the real locus) and leaves the point
  within it free; on the real locus the angle u stays flat.
- **B308** (NEGATIVE): "E6 fixes the coupling but not the texture". The reading here reaches the same verdict in the
  weave's setting: the coupling is fixed, and the texture is the direction, which is free.

Also matched: B632 (a canonical invariant vev in the 27) and B1443 (a deck orbit's diagonal coupling tensor).

**Literature:**
- the two quartic invariants of a complex SO(3) triplet and their real and isotropic vacuum alignments;
- Takagi's factorisation;
- the Coleman–Weinberg form Σ m⁴ ln m².

## 1. The sealed run (`verification/direction_mass_matrix.py`, unchanged; `direction_mass_matrix.json`, `direction_mass_matrix_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **D1** | the frame is unitary; U†Y(a)U is the block form, to 1e-12, at 9 τ × 20 complex a | 95% | **HOLDS:** 5.6·10⁻¹⁶ and 8.4·10⁻¹⁶ |
| **D2** | a ↦ M₂(a) has full rank; Y(L⁻¹K) has K's masses and a zero third one, to 1e-12 | 95% | **HOLDS:** the smallest singular value of L is ½ of the largest at every τ; the masses agree to 7.0·10⁻¹⁶ |
| **D3** | s₁s₂ = \|R\|²\|a·a\|; s₁² + s₂² = 2\|R\|²\|a\|² + 2\|a·R̄\|² − \|a·R\|², to 1e-12 | 95% | **HOLDS:** 6.6·10⁻¹⁵ and 1.3·10⁻¹⁵ over 1,800 directions |
| **D4** | λ₂ > 0: the minima are on the cone (defect < 1e-4, m < 1e-3); λ₂ < 0: on the real locus, m ∈ [½, 1]; none in between | 95% | **HOLDS:** see below |
| **D5** | [f(S, P) − f(S, 0)]/P² = −(2 ln S + 1) within 1% | 90% | **HOLDS:** worst relative error 1.3·10⁻⁵ |
| **D6** | m(e_k) = ½ on τ = iy; m(e_i) = m(e_j) = 0.6096 at τ = i; then toward 1 and ½ | 90% | **HOLDS:** see below |

**D4 in full** (30 BFGS starts per λ₂; m read at τ = i and at a random τ):

| λ₂ | defect \|a·a\|/\|a\|² | m at τ = i | m at the random τ | minima with 10⁻³ < m < 0.45 |
|---|---|---|---|---|
| −0.5 | 1.0000 | 0.500–0.939 | 0.500–0.953 | 0 |
| −0.1 | 1.0000 | 0.500–0.809 | 0.500–0.927 | 0 |
| 0.1 | 7·10⁻⁹–1.5·10⁻⁷ | ≤ 1.04·10⁻⁷ | ≤ 1.12·10⁻⁷ | 0 |
| 0.5 | 1.7·10⁻⁹–4.5·10⁻⁸ | ≤ 3.7·10⁻⁸ | ≤ 4.2·10⁻⁸ | 0 |
| 1.0 | 3·10⁻⁹–2.9·10⁻⁸ | ≤ 2.2·10⁻⁸ | ≤ 2.5·10⁻⁸ | 0 |

On the real locus, m spreads over [½, 1] because the potential does not fix the angle u. That angle is a flat direction
of the symmetric potential, which only the coupling to R can lift.

**D6 in full** (the units as Higgs directions on τ = iy):

| y | m(e_i) | m(e_j) | m(e_k) |
|---|---|---|---|
| 1 | 0.609612 | 0.609612 | 0.5 |
| 2 | 0.885816 | 0.504971 | 0.5 |
| 4 | 0.994732 | 0.500009 | 0.5 |
| 8 | 0.999990 | 0.500000 | 0.5 |

## 2. What it says

- **The direction is the 2–3 mass matrix.**
  - In the frame (R/|R|, R̄/|R|, n) fixed by τ, the coupling of a Higgs in M is zero on R. It maps span(R̄, n) to
    span(R, n) by M₂(a) = [[2(a·R̄), |R|(a·n)], [|R|(a·n), −(a·R)]].
  - The map a ↦ M₂(a) is a linear bijection onto the complex symmetric 2 × 2 matrices.
  - So every symmetric mass matrix for the two massive generations comes from exactly one Higgs direction.
  - B1644's coupling therefore predicts, per sector, exactly two things: the massless generation along R(τ), and that
    the 2–3 block is symmetric (left and right rotations tied). Nothing else.
  - The six real numbers of the Higgs's direction are the block's six. τ enters only through |R| and the frame.
- **Nothing on the record drives the direction near the cone.**
  - A potential symmetric under SO(3) on M and a phase gives one extreme or the other: the cone (m = 0, one massive
    generation) or the real locus (m between ½ and 1).
  - The zero modes' own loop changes only the coefficient that decides between them (P² = |R|⁴|a·a|²).
  - The quaternion units, read as directions, give m ≥ ½. At the cusp they give 1 and ½, and e_k gives ½ exactly
    because of Jacobi's identity. So the simplest reading of the cusp's unit as a vector in M (P-113) gives no
    hierarchy.
- **P-115 answered for this route:**
  - a small non-zero m₂/m₃ is a free number per sector: the |a·a|² coefficient (tree plus loop), set near zero, where
    U(3) symmetry makes the setting technically natural but not derived;
  - the Higgs's direction in M is not fixed by anything computed.
- **For the count (P-116):**
  - Per sector the route spends six real direction parameters to reproduce a general symmetric 2–3 block, against the
    block's two masses and its rotation.
  - If the up and the down sectors share the fibre, they share R(τ) and hence the massless state. That bears on the
    first generation's mixing, the next arc's question.

## 3. Owed (POINT_REGISTER)

- P-116, the quark count: with a common R the first generation is massless in both sectors and aligned, so its
  leading-order mixing must be read before any crossing.
- P-113 beyond the simplest reading: FK10's unit with per-component units (W46).
- The parent map for the adjoint Higgs at the puncture (P-108).

## 4. Files

`verification/direction_mass_matrix.py` (sealed, unchanged), `direction_mass_matrix.json`,
`direction_mass_matrix_run.txt`; the lock `tests/test_b1646_the_direction_is_the_mass_matrix.py`.
