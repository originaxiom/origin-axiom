# B160 — the metallic-quasicrystal bridge: independent rediscovery + bronze + the κ-sweep lead

**Date:** 2026-06-17. **Status:** a cross-session handoff re-derived the project's quasicrystal bridge
`κ = tr[A,B] = 2 + λ²` from scratch and converged on the **identical firewall**. The bridge itself is **already
banked** (K007, K010, B107/V94, B124, B127, B148/V137, S023) — so this is **corroboration, not new physics**.
What this stage adds, all verified here: (i) the explicit **transfer-matrix** realization of the headline,
re-proved symbolically; (ii) an **independent bronze (m=3)** trace map + Cantor spectrum (a fresh data point
for S023's "distinct metallic quasicrystals"); (iii) a genuinely new structural lead — the **κ-sweep** linking
the quasicrystal regime (κ>2, K007) to the **figure-eight hyperbolic** point (κ=−2, B67) through one foliated
monodromy. **Emergent/condensed-matter mathematics, not fundamental physics**; nothing to `../../CLAIMS.md`;
P1–P16 untouched. Ledger V154. Reproducers `INDEP_verify.py`, `bronze_indep.py`, `kappa_symbolic.py`,
`make_sure.py`, `fib_spectrum.py`, `silver.py`.

## §0 — Firewall (state first; identical to K010)

`κ = tr[A,B]` is a **scale-free** conserved invariant: `κ = 2 + λ²` is the **coupling of a tight-binding
chain**, not a vacuum energy or a constant of nature; the spectrum is the allowed energies of *one particle in
a fixed quasicrystal*, not a particle spectrum (no fields, no masses). The framework is achiral/phase-trivial
(CS=0, B127). This is the **physics of aperiodic matter** (real, observed: quasicrystals, fractal electronic
spectra) — a **bridge** the project's mathematics sits *exactly on*, **not a crossing**: no new physics is
derived from the self-generation axiom. The mass-spectrum reading is **dead** (B107/B: the SL(3) tower is one
golden scale `±φᵏ`; S015 killed). Nothing here promotes to `CLAIMS.md`.

## §1 — The headline is already banked; the handoff is independent corroboration

A fresh cross-session worker (no repo access) reconstructed, end to end and verified:
`κ = tr[A,B] = 2 + λ²` ⟹ the **Fibonacci Hamiltonian** (1D quasicrystal) ⟹ **zero-measure Cantor spectrum**
(Sütő 1987; Damanik–Gorodetski), extended to silver, and — importantly — it arrived at the **same
bridge-not-crossing firewall**. Every piece is the repo's existing banked content:

| handoff claim | already banked as |
|---|---|
| metallic trace map = KKT/Fibonacci trace map | **B107/A** (verified, `fibonacci_map_matches_B67`) |
| `κ = tr[A,B] = x²+y²+z²−xyz−2` conserved ∀m = Sütő invariant | **B107/A, B148/§1, K010** |
| `κ = 2 + λ²` (coupling); `κ = 4·I_FV + 2` | **B148/V137, K010** |
| metallic family = distinct quasicrystals (golden/silver/bronze) | **S023, K007** |
| zero-measure Cantor spectrum, horseshoe renormalization | **K010, B124, B127** (Damanik–Gorodetski) |
| "the crossing stays shut" (one golden scale, not a mass spectrum) | **B107/B** (the headline negative) |

**Verified here (our own from-scratch script, `INDEP_verify.py`):** the generic Fricke identity
`tr[A,B] = x²+y²+z²−xyz−2` (so `κ` really is the punctured-torus commutator-trace invariant); and for the
explicit transfer matrices `A=[[E−λ,−1],[1,0]]`, `B=[[E,−1],[1,0]]`, the structural collapse
`z = tr(AB) = xy − 2` ⟹ Fricke `→ (x−y)²+2`, `x−y=−λ` ⟹ **`tr[A,B] = λ²+2`, independent of E** — all
**symbolic, exact**. The Fibonacci and silver trace maps conserve their Fricke invariants (symbolic); the
spectrum measure decays geometrically to zero (grid-stable: golden ratio 0.759, silver 0.779). This **pins the
explicit transfer-matrix form** of B107's identification (which was tagged POSTULATED at the
character-variety level) and corroborates it independently. **The value is robustness — two independent AI
sessions, no shared context, the same bridge and the same firewall — not novelty.**

## §2 — Bronze (m=3): a new verified data point (`bronze_indep.py`)

Derived independently (not inherited): the metallic-`m` substitution `a → aᵐb, b → a` gives word recursion
`s_{k+1}=s_kᵐ s_{k-1}` and matrix recursion `M_{k+1}=M_{k-1} M_kᵐ`. For **m=3**, Cayley–Hamilton
(`M_k³=(b²−1)M_k − bI`) yields the **bronze trace map**
`(a,b,c) ↦ (b,  (b²−1)c − ab,  (b²−1)(bc−a) − bc)`, which **matches the actual transfer matrices** (numeric)
and **conserves the Fricke invariant `κ = a²+b²+c²−abc−2`** (symbolic, Δ=0). Word-length ratio → `(3+√13)/2`
(the bronze mean), and the spectrum measure decays geometrically to zero at its **own** rate (~0.719, distinct
from golden 0.759 / silver 0.779) — a zero-measure Cantor spectrum (ground truth: Damanik–Killip–Lenz, every
Sturmian potential `λ≠0`). This is an explicit, verified realization of S023's "distinct metallic quasicrystals"
for m=3. **[symbolic + numeric]**

## §3 — The genuine increment: the κ-sweep (one monodromy, three worlds)

`κ = tr[A,B]` is the *coordinate* on the character variety, and the figure-eight/golden monodromy is **one
fixed automorphism foliated over `κ`** (the Dehn-twist trace moves preserve `κ`, B148). The Hermitian
quasicrystal is only the slice `κ = 2 + λ² ≥ 2` (real coupling). Sliding `κ` along the same map:

- **κ > 2** (real λ): Hermitian metallic quasicrystal, hyperbolic renormalization, Cantor spectrum — **K007/K010** (banked).
- **κ = 2** (λ=0): periodic crystal, AC band `[−2,2]` — **K010 dictionary** (banked).
- **κ < 2** (imaginary λ): non-Hermitian / PT-symmetric quasicrystal — a real research area, **OPEN here**.
- **κ = −2** (λ = 2i): **the complete hyperbolic structure on the figure-eight knot complement** — verified here:
  `2 + (2i)² = −2`, and the commutator becomes a genuine **parabolic** (trace −2, single Jordan block
  `(C+I)²=0`, *not* the central `−I`) = the cusp of the once-punctured-torus fiber (cf. **B67**). **[symbolic]**

So one object's boundary invariant interpolates between a **condensed-matter quasicrystal spectrum** (κ>2) and
a **3-manifold hyperbolic geometry** (κ=−2), bridged by non-Hermitian aperiodic operators. **Both endpoints are
established, independent mathematics** (Sütő; Thurston) confirmed here to lie on the same foliated map — this is
a **mathematical** bridge (no firewall crossing: the κ=−2 end is geometry, the κ>2 end is spectral theory).

**Honestly open (exploratory, not banked as findings → `docs/OPEN_LEADS.md`):** whether the Cantor structure
*persists* into ℂ for κ<2 (a cross-session numeric sweep saw the spectrum lift off the real axis continuously,
`max|Im E| ≈ 0.91|λ|`, with a first method that failed on measure-zero sets and a corrected
direct-diagonalization that passed its Hermitian sanity check — but Cantor-persistence was **not** established);
and whether the κ=−2 complex spectrum **encodes** the hyperbolic geometry (completely open — two true facts
about one `κ` value is not an encoding). These need their own verification; **no claim**.

## Verification ledger
| claim | status | artifact |
|---|---|---|
| generic Fricke `tr[A,B]=x²+y²+z²−xyz−2` | **SYMBOLIC** | INDEP_verify.py |
| transfer-matrix `z=xy−2`, `tr[A,B]=2+λ²`, E-independent | **SYMBOLIC** | INDEP_verify.py, make_sure.py, kappa_symbolic.py |
| Fibonacci + silver trace maps conserve Fricke invariant | **SYMBOLIC** | INDEP_verify.py |
| golden/silver spectrum → 0 (ratio 0.759 / 0.779), grid-stable | NUMERIC + GRID; ESTABLISHED (Sütő; DKL) | fib_spectrum.py, silver.py |
| bronze m=3 trace map (Cayley–Hamilton), conserves κ, spectrum→0 (~0.719) | **SYMBOLIC + NUMERIC** | bronze_indep.py |
| κ=−2 ⟺ λ=2i; commutator parabolic = figure-eight cusp | **SYMBOLIC** | INDEP_verify.py |
| κ<2 Cantor persistence; κ=−2 geometric encoding | **OPEN** (exploratory) | — (OPEN_LEADS) |

## Anchors
K007 (Fibonacci-Hamiltonian quasicrystal), K010 (the named object + firewall), B107/V94 (the KKT
identification + the headline negative), B124/B127 (horseshoe + Fricke–Vogt dictionary + CS=0), B148/V137
(`κ=4I+2` pinned, the SL(2,ℤ) MCG action), S023 (distinct metallic quasicrystals), B67 (figure-eight from the
trace map). Ledger V154. External: Kohmoto–Kadanoff–Tang (1983); Sütő (1987); Damanik–Killip–Lenz (Sturmian);
Damanik–Gorodetski; Thurston (figure-eight hyperbolic structure).

## Reproduction
`python frontier/B160_quasicrystal_bridge_corroboration/INDEP_verify.py` (the headline, symbolic) and
`bronze_indep.py` (the new m=3 data point). The four handoff scripts (`kappa_symbolic.py`, `make_sure.py`,
`fib_spectrum.py`, `silver.py`) reproduce the golden/silver numerics.
