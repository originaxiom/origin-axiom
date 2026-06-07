# B107 — the physics-connection audit (the headline is a NEGATIVE)

> **⚠ FIREWALL — POSTULATED.** Every physical reading on this page is **POSTULATED and quarantined**, firewalled
> to `../../paths/philosophical/PHYSICS_RESONANCES.md`. **Nothing here reaches `CLAIMS.md`; the physics chapter
> stays CLOSED; P1–P16 are untouched.** The *mathematics* (the trace-map invariant A, the golden spectrum B) is
> standard and verified; what this stage banks is the honest **classification** of what the physics does and —
> mostly — does **not** license. The headline result is a **negative** (B): the tower is not new physics.

**Status:** `computer-assisted` (A, B reproduced symbolically this session) + `audit` (C–E are classifications,
not computations). Banks the CC-web "physics-connection exploration" as a first-class **dead-end log**: taking
the physics seriously produced an exact literature anchor (A), a precise why-not-new-physics mechanism (B), two
corrected overclaims (C), confirmed citations (D), and one open fork (E). Script `probe.py`; test
`tests/test_b107_physics_connection_audit.py`.

## A — VERIFIED (structural): the quasicrystal anchor
The SL(2) **metallic trace map** `φ_m: a → aᵐb, b → a` **is** the Kohmoto–Kadanoff–Tang / Fibonacci-Hamiltonian
trace map. On Fricke coordinates `(x,y,z) = (tr A, tr B, tr AB)`, Cayley–Hamilton (`Aᵏ = S_{k-1}(x)A − S_{k-2}(x)I`,
`S` the Chebyshev-U-like sequence) gives the induced map
```
   x' = tr(Aᵐ B)     = S_{m-1}(x) z − S_{m-2}(x) y
   y' = tr(A)         = x
   z' = tr(A^{m+1} B) = S_m(x)   z − S_{m-1}(x) y
```
- **`m=1`** is exactly `(x,y,z) → (z, x, xz − y)` — the half-trace form of the standard Fibonacci trace map
  `T(x,y,z)=(2xy−z,x,y)`, matching B67's `T₁`. *(verified, `fibonacci_map_matches_B67`.)*
- For **every `m`** the commutator trace `κ = tr[A,B] = x² + y² + z² − xyz − 2` is **conserved** — Sütő's
  spectral invariant / the Fricke–Vogt invariant. *(verified symbolically `m=1..4`, deviation `≡ 0`.)*

So our tower lives on a **known quasicrystal object**. **Cite:** Sütő (J. Stat. Phys. 56, 1989);
Damanik–Gorodetski–Yessen (Invent. Math. 206, 2016, the Fibonacci Hamiltonian); **Roberts (Physica A 228,
1996** — the metallic-mean trace maps already a studied family); the `3r−3` minimal trace-coordinate dimension
for a rank-`r` free group (here `r=2 → 3` coordinates). The content of A is the **identification**, not a new
theorem.

## B — VERIFIED (the headline NEGATIVE): genericity / single scale
Every SL(3) **Fibonacci (`m=1`) tower eigenvalue is `±φᵏ`** (`φ` = golden ratio). The tower factors as
`∏_d Sym^d(M_1)` (B103, proved `n=3,4`); `M_1 = [[1,1],[1,0]]` has eigenvalues `{φ, −1/φ}`, so each `Sym^d`
eigenvalue is `(−1)^j φ^{d−2j}`. The 8 SL(3) eigenvalues are exactly
```
   {  1,  −1,  φ²,  φ⁻²,  φ³,  −φ,  φ⁻¹,  −φ⁻³ }   ( k ∈ {−3,…,3}, sign ±1 )   [verified]
```
— a **single geometric scale `log φ`** (the Fibonacci spectral-RG inflation exponent) dressed by signs and
integer powers. A physical fluctuation spectrum is the **Hessian of an action**, generically **not** one
geometric ratio; a "spectrum" that collapses to one number under signs/powers is **re-presented moduli-space
monodromy, not new physics**. **This is the decisive negative** — the reason the tower, however suggestive, is
not a spectrum of masses/dimensions.

## C — CORRECTED OVERCLAIM (banked explicitly, like V90/V91)
Two physics write-ups made the **same category error**: *tower eigenvalues = operator anomalous-dimensions /
masses*, and *torsion = masses*. **These are NOT the 3d-3d dictionary.** The tower/torsion are the **linearized
monodromy on the tangent to the moduli space**; masses are the **fluctuation Hessian** (operator content),
which the moduli-space monodromy does **not** determine. **Withdrawn; off the table for promotion; do not
re-chase.**

**What IS real and citable** (moduli-space level only): `M_SUSY(T[M]) ≅ M_flat(M; G_C)` (vacua = flat
connections), and the **three flat-connection types ↔ three vacuum branches** (trivial ↔ unbroken, geometric ↔
Higgs, Dehn-filling ↔ Coulomb) — exactly the three trace-map fixed-point classes B106 computed. Two further
"coincidences" dissolve under inspection: the `z=φ` "shape" is the **same single scale** (`z²−z−1` = char poly
of `M`), and `τ=0` at SL(3) is the generic `(t−1)` **parity factor** (every `det=−1` monodromy carries it), not
a special vacuum.

## D — CITATIONS (confirmed)
- `arXiv:1305.0937` = **Gang–Koh–Lee–Park**, *Superconformal Index and 3d-3d Correspondence for Mapping
  Cylinder/Torus* (the once-punctured-torus bundle, monodromy `φ ∈ SL(2,ℤ)`) — **confirmed**.
- **DGG** (Dimofte–Gaiotto–Gukov): `arXiv:1108.4389` (*Gauge Theories Labelled by Three-Manifolds*),
  `arXiv:1112.5179` (*3-Manifolds and 3d Indices*) — **confirmed**.

## E — OPEN (the one live fork)
The tower / torsion / degree=rank all live **on or near the principal component** (`tr A = tr A⁻¹ = 1` →
principal `Sym^{n−1}` → **SL(2)-determined**, hence the single golden scale of B). The genuinely *irreducible*
SL(n) reps **off** that component are **multichannel quasiperiodic systems** not reducible to a single
Fibonacci chain (the literature's "coupled aperiodic ladders," understudied). **The tower does not touch them**;
if independent spectral content exists, it is there. Flagged as a **future probe** — explicitly **not** the dead
spectral claims of C.

## Addition 3 — the D1 data confirms the non-principal thesis (the bridge B ↔ E)
B106's **D1** found the Dehn-filling Jacobian neutral eigenvalues are **roots of unity** (`±i, −1` SL(4)
principal; `ω, ω²` secondary) — **algebraically independent of `φ`** (V93: seed-stable, gauge-noise gate
passed). This is the **data** validating the thesis: the **tower** is single-scale (`±φᵏ`, SL(2)-determined —
section B, confirmed); the **Dehn-filling** sector **breaks** the single-scale pattern (roots of unity `≠ φᵏ` —
confirmed). *The non-principal sector is where any independent content would live — predicted by E, exhibited by
D1.* The per-eigenvector scalars `c = {1, 1, −1, i}` (B106 D4) are the additional structure; whether the
opposition involution `θ = −w₀` **predicts** them is the open **c→θ** check (a *math* test linking D1/D4 to the
`ρ_n` catalog target — the central goal — not a physics claim).

## Verdict
A physics exploration **banked as a negative**: the metallic tower is a **known quasicrystal trace map** (A)
carrying **one golden scale** (B) — re-presented moduli-space monodromy, **not** a spectrum of new physics. The
only citable physics is the **moduli-space-level** `M_SUSY ≅ M_flat` and the three-branch ↔ three-fixed-point
correspondence (C); the mass/dimension identifications are **withdrawn category errors** (do not re-chase). The
one live fork is the **off-principal multichannel** sector (E), where B106's root-of-unity data (Addition 3)
shows the single-scale pattern breaks. **Physics POSTULATED/firewalled throughout; nothing to `CLAIMS.md`;
P1–P16 untouched.**

```bash
python frontier/B107_physics_connection_audit/probe.py
python -m pytest tests/test_b107_physics_connection_audit.py -q
```
Physics POSTULATED + firewalled to `paths/philosophical/PHYSICS_RESONANCES.md`; no `CLAIMS.md` promotion; the
physics chapter stays CLOSED; proven core P1–P16 untouched.
