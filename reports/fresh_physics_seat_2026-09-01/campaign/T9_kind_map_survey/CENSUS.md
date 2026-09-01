# T9 CENSUS — every series-like object in the committed corpus

Method: repo-wide sweep of `frontier/*/FINDINGS.md` (1,191 arc directories) on an
extended token set — GC-12's tokens (WRT / Habiro / q-series / eta-quotient /
Kashaev / state-integral / false-theta / Zhat / Nahm / quantum-dilogarithm)
PLUS `generating function`, `graded character`, `theta series/function`,
`partition function`, `colored Jones`, `Rogers`, `q-expansion`, `q^` — and a
filename sweep of committed verification/data files (`*theta*`, `*qseries*`,
`*character*`, `*kashaev*`, `*habiro*`, `*index*`). Every hit directory
inspected; every entry below carries its location. Machine-run results in
`survey_results.json`; full instrument log in `survey_output.txt`.

## A. Genuine formal q-series with computable coefficients (16 entries, 4 classes)

### Class A1 — the B666/B672 modular-flavor stream family (12 series, ONE family)
Banked machine-readable at
`frontier/B666_leads_campaign/cellW33/cellW33_doublet_streams.json`; recognized
in `frontier/B672_grading_hunt/FINDINGS.md` (301 coefficients per component,
two verification routes).

| series | prefactor | first kind-map violation |
|---|---|---|
| `Y^(5)_2hat.comp1 = q^{2/5}(q;q)G(q)(q;q)^9` | `q^{2/5}` | K-ii: n=1 coefficient **−9** |
| `Y^(5)_2hat.comp2 = q^{3/5}(q;q)H(q)(q;q)^9` | `q^{3/5}` | K-ii: n=1 coefficient **−10** |
| `Y^(5)_2hat'.comp1` (η^{24/5}·quintic in F₁,F₂) | `q^{1/5}` | K-ii: n=2 coefficient **−108** |
| `Y^(5)_2hat'.comp2` | `q^{4/5}` | K-ii: n=2 coefficient **−378** |
| F₁ stream (42 terms, rational) | — | K-ii: n=1 coefficient **3/5** (non-integer) |
| F₂ stream (42 terms, rational) | — | K-ii: n=1 coefficient **−2/5** (non-integer) |
| sextet row1 `F₁⁵+2F₂⁵` (20 terms) | untyped | K-ii: n=4 coefficient **−5** |
| sextet row2 `2F₁⁵−F₂⁵` | untyped | K-ii: n=9 coefficient **−5** |
| sextet row3 `F₁⁴F₂` | untyped | K-iii (no c datum) + K-iv (bounded coeffs, c_eff ≈ 0) |
| sextet row4 `F₁³F₂²` | untyped | K-iii + K-iv (same) |
| sextet row5 `F₁²F₂³` | untyped | K-ii: n=5 coefficient **−1** |
| sextet row6 `F₁F₂⁴` | untyped | K-ii: n=1 coefficient **−1** |

The 2hat doublet was reconstructed in this cell from the Rogers–Ramanujan
product identities and matched the banked integer streams 60/60 per component
before use (then extended to 400 terms). Provenance: object-side (the golden
object's Sym^25 modular-flavor data).

### Class A2 — B724's GGM rotated 3D-index of 4₁ (MISSED by GC-12's sweep)
`frontier/B724_seeing_readjudication/FINDINGS.md`, Path-1 GGM row:
`Ind = 1 − 8q − 9q² + 18q³ + 46q⁴ + 90q⁵ + …` (recomputed there from
arXiv:2007.10190 eq (80)). A genuine object-side q-series — the 3D index is
defined from m004's own ideal triangulation — invisible to GC-12's keyword set
(its token is "3D-index"). First kind-map violation: K-ii at n=1 (**−8**).

### Class A3 — the fiber-torus theta families of B364/B365/B366 (MISSED by GC-12's sweep)
`frontier/B364_theta_polarization/FINDINGS.md` (also B365, B366): the
triangular family `f_j(z,τ) = Σ_{n≡j(15)} e(E(n)τ+nz)`, `E(n) = n(n−1)/30`,
and the square family `E'(n) = n²/15` — level-15/30 theta q-series of the
object's own fiber torus, banked as analytic identities; coefficients (all
units) computed in this cell on the q^{1/30} and q^{1/15} grids. Pass K-i and
K-ii and K-v; fail **K-iii** (no central-charge datum — a bare partial theta is
not presented as a character of anything) and **K-iv** (bounded coefficients:
c_eff ≈ 0 — ZERO cusp-boson units, not six).

### Class A4 — the (E6)₁ characters as committed corpus artifacts
`frontier/B1190_close_loop_batch2/verification/gc6_l154_bridge.py` computes
Θ_E6/η⁶ (and the h=2/3 modules) from the E6 root lattice; re-derived
independently in this cell. Passes **K-i, K-ii, K-iii, K-iv** (c_eff ≈ 5.996,
the six-unit band) — and fails **K-v**, the anti-numerology clause: it is built
from the E6 root lattice, not from m004 data. Its K-v discharge is exactly
B1228's one remaining identification (nominated type vs geometric connection).

## B. NOT-COMPARABLE (series-like by name only; no formal q-expansion exists)

| object | location | why not a q-series |
|---|---|---|
| WRT invariants τ_r(4₁(5,1)) | `frontier/B441_child_wrt/` | per-r algebraic numbers in ℚ(ζ_{4r}) |
| Kashaev ⟨4₁⟩_N / J_N tower | `frontier/B384_kashaev_bridge/`, `B1116_asymptotic_channel/`, `B246_quantum_volume/` | N-indexed algebraic numbers at roots of unity + a growth rate (→ Vol); the Habiro sum does not converge as a formal power series |
| Habiro/GSWZ element Φ(h)Φ(−h) | `frontier/B685_generation_terminal/`, `B800_habiro_integrality/`, `B839_b685_residue/` | perturbative ħ-expansion at the hyperbolic saddle; content is 3-adic denominator valuations |
| Andersen–Kashaev state integral | `frontier/B1090_partition_bridge/` | continuum Faddeev quantum-dilogarithm integral |
| golden colored-Jones values [N]·J_N at e^{2πi/5} | `frontier/B240_golden_jones_integrality/` | a 4-number table at one root of unity |
| generic-q skein tower (quantum trace map) | `frontier/B205_metallic_quantum_trace_map/` | finite Laurent polynomials per word (B672's candidate C1, dead there with exact first mismatches) |
| zeta-quotient spectral identities | `frontier/B737_candidate_zero/`, `B754_p2_spectral/` | Selberg-type zeta data, no q |
| Verlinde fusion / boundary entropy | `frontier/B492_verlinde_boundary_lens/` | fusion integers and quantum dimensions |
| finite character tables | `frontier/B646_wave2_integration/.../n1_character.py`, `B1212_two_replies/verification/` | finite-group / finite-module character values, not q-graded |
| Hecke palette {1,2,8}; E6 centralizer cubics | `frontier/B762*/`, `B854*/`, `B866*/` | discrete invariant tuples / Lie-bracket computations (GC-12 already corrected this false lead) |

Tokens that returned zero series-bearing hits: `false theta`, `Zhat`,
`q-expansion` (as an artifact), `Nahm` (only B685's killed assumed-datum
route). `theta` hits outside A3 (B353/B358/B359/B534/B584/B639) are matrices,
numeric identities at fixed τ, or Lie-theoretic involutions — no banked
q-expansion.

## The census verdict on GC-12's claim

GC-12 (B1191): *"exactly one banked object-side artifact that is even
syntactically a q-series (B672's doublet); every other candidate is not a
q-series at all."*

- **REFUTED as a count**: the corpus holds one q-series FAMILY of about twelve
  streams (including a second doublet, 2hat', and six sextet rows GC-12 never
  listed) plus at least two further genuine banked series classes its keyword
  sweep missed — B724's 3D-index and the B364-66 fiber-torus thetas — plus the
  stage-side (E6)₁ characters sitting inside B1190's own verification artifact.
  (GC-12's own caveat 1 anticipated exactly this failure mode.)
- **CONFIRMED in operative content**: nothing the sweep adds survives the
  kind-map either — the enlarged census is exactly as empty as the small one
  (0/16 pass; every failure on a named condition; see FINDINGS.md).
