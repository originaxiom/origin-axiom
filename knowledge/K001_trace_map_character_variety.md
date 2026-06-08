# K001 — The trace map and the character variety

> **Explainer** (`GOVERNANCE.md`). Self-contained; standard material cited to the literature, the project's own use
> cited by `B`/`V` number (no re-proof). Nothing here promotes to `../CLAIMS.md`; never a premise in a proof.

## The object

Fix the free group on two generators, `F₂ = ⟨A, B⟩`. A representation `ρ: F₂ → SL(2,ℂ)` is just a choice of two
matrices `(ρ(A), ρ(B))`; the space of all of them is `SL(2,ℂ)²`. We almost never care about a representation itself,
only about it **up to conjugacy** (`ρ ∼ gρg⁻¹`), because conjugate representations are "the same" geometrically. The
quotient — taken in the careful (GIT) sense that keeps it an algebraic variety — is the **`SL(2,ℂ)` character variety**
of `F₂`, written `X(F₂)`.

## Fricke coordinates

The classical **Fricke–Vogt theorem** says `X(F₂)` is astonishingly simple: it is just `ℂ³`, coordinatized by the
three traces
```
   x = tr ρ(A),   y = tr ρ(B),   z = tr ρ(AB).
```
Every conjugation-invariant polynomial function of `(ρ(A), ρ(B))` is a polynomial in `(x, y, z)`; the trace of *any*
word reduces to one via the `SL(2)` trace identities (`tr(UV) + tr(UV⁻¹) = tr U · tr V`, `tr(U⁻¹) = tr U`). So the
character variety of `F₂` is the affine 3-space of triples `(x, y, z)`. The single relation that records "these three
traces came from two matrices" is encoded in the commutator trace
```
   κ := tr ρ([A,B]) = x² + y² + z² − xyz − 2,
```
the **Fricke / Markov** cubic. Level sets of `κ` are the relative character varieties; `κ = 2` is the locus where the
commutator is parabolic/trivial (the reducible and boundary strata).

## The trace map

An automorphism of `F₂` (an element of `Out(F₂) ≅ GL(2,ℤ)` at the level of abelianization) sends words to words, hence
permutes representations, hence acts on `X(F₂) = ℂ³` — and because traces are polynomial, it acts by a **polynomial
automorphism of `ℂ³`**, the **trace map**. The generators act by elementary moves; the one this project lives on is
```
   T(x, y, z) = (z, x, xz − y),
```
a polynomial shear that preserves `κ`. Iterating `T` is a discrete dynamical system on `ℂ³`; its fixed points,
periodic points, and linearizations are the trace ring's geometry. The mapping-class group of the once-punctured
torus is exactly this `GL(2,ℤ)` acting by trace maps, which is why the figure-eight monodromy (`K004`) appears here as
a specific word.

## How the project uses it

- `B67` realizes the **figure-eight A-polynomial** as the fixed-point set of the trace map (the `SL(2)` story), and
  `B71` does the `SL(3)` analogue (the character variety as `Fix(T₁²)`).
- `B103` is the structural pivot: for the `SL(n)` trace map, the linearization at the trivial fixed point — the
  "tower" — factors through the **abelianization** `N ∈ GL(2,ℤ)` of the monodromy word, so its characteristic
  polynomial is a **class function** of `N` (a polynomial in `tr N`, `det N`). That is what makes the tower the same
  for all metallic and non-metallic seeds with the same `(trace, det)` (`K008`).
- The `κ = x² + y² + z² − xyz − 2` cubic is the project's recurring landmark: the **void** fixed point sits at
  `κ = +2` (B109), the geometric/parabolic cusp at `κ = −2` (B69/B101), and `κ` is conserved along the flow (it is
  the Sütő invariant of the quasicrystal reading, `K007`).

## What this is and is not

The character variety is a *moduli space of flat connections on a surface*, and the trace map is the *mapping-class
group acting on it*. That is the whole arena. It is **not** spacetime, and "time" in "trace-map flow" means
iteration-count of a monodromy (the firewall, `K006`; the two-headed-time reading is fenced in `../philosophy/P006`).

**Anchors:** B67, B71 (the variety as a fixed-point set), B103 (the tower as a class function of the abelianization),
B109 (the trace map at the void). External: Fricke–Klein; Vogt 1889; Goldman, *Trace coordinates on Fricke spaces*
(2009); Cantat–Loray on the dynamics of the Markov/Fricke surface.
