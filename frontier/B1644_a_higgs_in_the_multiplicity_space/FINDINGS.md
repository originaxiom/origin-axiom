# B1644 — A HIGGS IN THE MULTIPLICITY SPACE: the zero modes' coupling to a Higgs in the adjoint of the quaternion structure is symmetric with a non-zero diagonal, as derived; but Jacobi's identity makes the theta triplet isotropic, so det Y(a) = 0 for every Higgs direction and every τ — one generation is exactly massless, and the other two have a ratio set by the Higgs's direction (at least ½ for real directions, down to 0.004 for complex ones)

> *Audited 2026-10-15 by main (P-152, B1655): a FEATURE PRESENTED AS FAILURE: the exact zero is the pattern a light first generation needs; "golden impossible" is leading order at one τ. The grades, the corrected wording and the checks are in `frontier/B1655_main_audits_its_negatives/FINDINGS.md`.*

**Verdict: NEGATIVE as sealed.** S1 and S2 hold exactly. S3b fails: the light state is exactly massless, not suppressed
by |q|. The read-outs S3a and S3c came out as stated below; the golden spectrum is impossible. cc (main), 2026-10-14.
Sealed `8fa3d82ba` before the run. No data. **0 of 19.** POINT_REGISTER P-110 (path 1).

## 0. Seen first

As sealed: `VERDICT topic-sweep /adjoint|triplet Higgs|Higgs in T|multiplicity|flavon|vacuum direction|family space/: 73 of 1414 arcs on main match (NEGATIVE 13, OPEN 4, PROVED 55, RETRACTED 1)`
— in the weave era B1601, B1614 and B1641; none couples the zero modes to an adjoint Higgs. Also read before the seal:
B1642 and its addendum (W61, the audit lane's residue audit), B1641, B1643, and the SM seat's C0, W56 and W60.
**Literature:** the SU(2) invariant ψᵀ ε σ_a χ; flavour from a vacuum direction in a family space; Jacobi's
θ₃⁴ = θ₂⁴ + θ₄⁴.

**A disclosed fix.** The sealed instrument crashed in cell S2 before writing any output: a numpy float cannot multiply
an mpmath matrix. The run that counts used `adjoint_higgs_fixed.py`, which differs from the sealed file in one line (the
direction's three components cast to floats) and a comment. The sealed file is unchanged; the lock checks the
difference. The crash's output is kept (`adjoint_run_crash_before_output.txt`).

## 1. The sealed cells (`verification/adjoint_higgs_fixed.py`; `adjoint_higgs.json`, `adjoint_run.txt`)

| cell | prediction | prior | result |
|---|---|---|---|
| **S1** | the residues equal the hand table; symmetric; non-zero diagonal | 85% | **HOLDS exactly**: difference 0.0, antisymmetric part 0.0; smallest diagonal entry 0.32 of the largest |
| **S2** | linear in the direction | 95% | **HOLDS** to 2·10⁻¹⁶ |
| **S3a** | read-out: the distance to 1 : φ⁻¹ : φ⁻² over 400 directions and 8 values of τ | — | 0.381966 = 1/φ² everywhere: the smallest singular value is 0 at every direction and τ, so golden is impossible |
| **S3b** | along a = i near the cusp the light mass scales as \|q\| (slope −π) | 60% | **FAILS:** ln(s_min/s_max) is between −37 and −43 at every y, numerical zero; the light state is exactly massless |
| **S3c** | read-out at τ = 4i: hierarchical directions; the rank of (a, τ) → spectrum | — | Every direction has spectrum (1, m, 0), with m near ½ for these; the map has rank 1 |

## 2. Why the light state is exactly massless (post-seal, labelled; `post_seal_adjoint.py`, `post_seal_ratio.py`)

- **The identity.** Symbolically, for Y(a) = a_i Y(i) + a_j Y(j) + a_k Y(k) with the hand table,
  **det Y(a) = (R_i² + R_j² + R_k²) · (a·a) · (R·a).**
- **Jacobi kills the first factor.** With the weave's R's, R_i = −θ₂²/(2πη³), R_j = −θ₄²/(2πη³) and
  R_k = iθ₃²/(2πη³), we get R·R ∝ θ₂⁴ + θ₄⁴ − θ₃⁴ = 0 by Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴. The theta triplet is an isotropic
  vector, to 10⁻¹⁶ at every τ checked, so det Y(a) = 0 for every direction, real or complex, and every τ.
- **The control bites.** With random R's (not isotropic), the smallest singular value reaches 0.9 of the largest.
- **The middle ratio m = m₂/m₃** over 600 directions per τ, across the fundamental domain and toward the cusp, with
  the weave's R's:
  - real directions: m ∈ [0.500000, 0.996] — never below ½;
  - complex directions: m ∈ [0.004, 0.985].

## 3. What it says

- **A Higgs in M is the first coupling on the record with flavour structure.** It is the datum the three routes found
  missing (B1642, W61, the audit lane): symmetric, with a non-zero diagonal, no free coefficient but the Higgs's
  direction.
- **One generation is exactly massless, forced by Jacobi's identity.** That holds for every Higgs direction and every
  τ: a rank-2 leading-order coupling, the pattern a light first generation needs, here forced rather than chosen.
- **The other two have a ratio set by the direction alone.**
  - Real directions keep it at or above ½, so they cannot give the observed hierarchy (m_c/m_t ≈ 0.004, m_s/m_b ≈ 0.02,
    m_μ/m_τ ≈ 0.06; context, not a test).
  - Complex directions reach 0.004.
- **The golden spectrum is impossible here,** since one mass is zero.
- **For the count:** per sector the free data are the Higgs's complex direction (4 real numbers) and a scale, against
  the sector's two non-zero masses. Leptons and quarks, with CKM mixing from misaligned directions, need their own count
  before any crossing (B1643's C3).

## 4. Owed (POINT_REGISTER)

- Prove the bound m ≥ ½ for real directions, and find whether m reaches 0 for complex ones.
- Ask what fixes the Higgs's direction: the potential, or the cusp's unit (path 4).
- Count a quark model (τ, two directions, scales) against the 10 quark numbers, with the massless first generation as a
  leading-order prediction, before any sealed crossing.
- The adjoint Higgs at the puncture still needs the audit lane's parent map (P-108).

## 5. Files

`verification/adjoint_higgs.py` (sealed, unchanged), `adjoint_higgs_fixed.py` (one cast), `adjoint_higgs.json`,
`adjoint_run.txt`, `adjoint_run_crash_before_output.txt`, `post_seal_adjoint.py` and `.json`, `post_seal_ratio.py` and
`.json`; the lock `tests/test_b1644_a_higgs_in_the_multiplicity_space.py`.

## Addendum (2026-10-14): verified on an independent seat's instruments

The SM seat's W63 (its rule first, one run; HARVEST_LEDGER row 1117) recomputed this arc's coupling on its own theta
routines by two routes (contour and duplication, to 10⁻³⁰) and reproduced its numbers. Its one failed clause was the
square root's branch, which it predicted before the run: W21's continued branch is the one used here. Credit: the SM seat.

## Seen late (2026-10-21, Review 66; P-123)

> *Seen late.* This arc's sweep, in its own words, missed older arcs on its subject (vocabulary drift; the topic sweep now expands aliases, R65-6). B1443 (PROVED: the orbit's coupling tensor, each member coupling to its own Higgs class), B308 (NEGATIVE: the inter-generation Yukawa hierarchy not forced; E₆ fixes the coupling, not the texture) and B632 (PROVED: h¹(M; 27) = 3, a three-slot cohomological generation structure).
> B308 is the older form of this arc's finding that the coupling's texture is not forced. No cell changes.
