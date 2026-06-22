# B192 — SL(n≥3) higher-rank Lyapunov spectra: the "parity law" REFUTED (recorded negative)

**Date:** 2026-06-22; **CORRECTED 2026-06-23** after independent adversarial verification. **Status:** Masterplan
III, Track D (L20/B166). **The original headline — a metallic Lyapunov-spectrum "parity law" (symmetric iff `n`
even, realizing V29, special to the metallic cocycle) — is REFUTED.** It was an artifact of cherry-picked energies
plus a rigged control. This file now records the honest negative + the verify-don't-trust catch. **Firewall-side:**
emergent non-Hermitian math (`K010`); nothing to `../../CLAIMS.md`; P1–P16 frozen. Ledger V185 (corrected). Reproducer
`sln_higher_rank.py` (`ALL CHECKS PASS` — the checks now *verify the refutation*).

## What was claimed, and why it's wrong

The original B192 claimed the metallic SL(n) transfer cocycle's full Lyapunov spectrum is **symmetric (±-paired /
symplectic) iff `n` is even** and **asymmetric iff `n` is odd** — directly realizing V29 ("symplectic form exists iff
`n` even") — and that this even-`n` symmetry is **special to the metallic cocycle** (`163×` vs a generic SL(n)).
Independent verification broke all three load-bearing legs:

- **D1 [STANDS] — sum = 0.** The full QR-flag Lyapunov spectrum sums to 0 (det=1, the SL(n) structure) for n=3,4,5.
  This is true and trivial.
- **D2 [REFUTED] — there is no parity law.** The symmetry defect at the **cherry-picked** energies `(1.3, 2.1, −1.7)`
  (where n=4 read 0.003 "symmetric") **inverts on a fair broad energy grid**:

  | n | 2 | 3 | 4 | 5 | 6 |
  |---|---|---|---|---|---|
  | defect (cherry) | 0.00 | 0.22 | **0.003** | 0.11 | 0.07 |
  | defect (fair grid) | 0.00 | **0.03** | **0.34** | 0.41 | **0.50** |

  On the fair grid the defect **grows monotonically with n** — no even/odd alternation; n=4 (even) is *more*
  asymmetric than n=3 (odd); n=6 (even) is *not* symmetric. The "law" was a property of three hand-picked energies.
- **D3 [REFUTED] — not special to the metallic cocycle.** A **random potential in the same companion** matches
  metallic on the fair grid (n=4: random 0.337 vs metallic 0.344; n=6: 0.509 vs 0.503). So the (energy-dependent)
  approximate ±-symmetry is a **structural property of the nearest-neighbour transfer/companion matrix** — its
  eigenvalues come in reciprocal pairs `(λ, 1/λ)` at the relevant energies — present for random/periodic potentials
  too. The original "163×" compared metallic-at-cherry-energy against a **dense-Gaussian** SL(n) matrix (which has
  *no* transfer-matrix structure) — apples-to-oranges; against the matched same-companion control the ratio is ~1×.

## What survives

- **D1** (sum=0).
- **B166's original results STAND** (they are B166, not B192): SL(n≥3) is intrinsically **non-Hermitian** via the
  exact symplectic obstruction (every odd-`n` antisymmetric form is degenerate, V29), and the naive SL(3) cocycle
  shows **no clean SL(2)-style Cantor thinning** (B166's recorded negative). V29 holds **at the algebra level** — it
  is simply **not realized as a Lyapunov-spectrum parity** (the would-be realization is the refuted claim).
- The rigorous higher-rank non-Hermitian spectral theory stays **NEEDS-SPECIALIST** (no ground truth).

## The lesson (verify-don't-trust)

Two methodological traps, both caught by an independent verifier re-deriving on a *fair* energy grid with a *matched*
control: **(1) energy cherry-picking** — reading a "law" off three special energies where the companion happens to
sit in its reciprocal-pairing regime; **(2) a rigged control** — a dense-Gaussian SL(n) "generic" baseline that
lacks the transfer-matrix structure, inflating the apparent specialness. The honest fix needs an **energy-averaged**
diagnostic and a **same-structure** (random-potential) control. This is the third verify-don't-trust self-correction
of the Masterplan III batch (with B189's framing fix and B190's degree/monotonicity fixes).

## Anchors
`B166_sln_aperiodic` (V29 + the no-Cantor-thinning negative — the standing results that survive), `B109` (the
center-manifold link), `B60`/`B61`/`B107` (the tower / golden scale), `docs/OPEN_LEADS.md` L20 (reverted to B166's
CHARACTERIZED status; the B192 parity-law addition removed). External: QR-flag / Oseledets Lyapunov spectrum;
reciprocal-pair eigenvalues of nearest-neighbour transfer matrices (the actual cause of the energy-dependent
approximate symmetry); symplectic cocycles ⟹ ±-symmetric spectra (the *genuine* statement, which the metallic
companion does not satisfy as a law).

## Reproduction
`python frontier/B192_sln_higher_rank/sln_higher_rank.py` — D1 sum=0; D2 the cherry→fair inversion (no parity law);
D3 the random-potential match (not metallic-special); D4 what survives (V29 at the algebra level / B166). Prints
`ALL CHECKS PASS` (the checks verify the refutation). Fast locks in `tests/test_b192_sln_higher_rank.py` (3 tests).
