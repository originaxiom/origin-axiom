# B127 — Chirality, Fibonacci, arithmetic, and the object's proper name (V116)

Resolves the "threads 3 & 4 + Fibonacci" investigation, re-derived in-sandbox (verify-don't-trust). **Pursued through
chirality, topology, and arithmetic, the physics-bridge claim returns a clean, multiply-confirmed negative** — the
firewall (`philosophy/P007`) confirmed from a **third and fourth independent direction** (chirality; arithmetic). A
small set of clean MATH facts survive, and the strongest is the object's **proper name** (`knowledge/K010`). MATH and
physics enter as **different tiers**. Nothing to `CLAIMS.md`; P1–P16 and the functorial `Sym(W)→trace-ring` wall (B85)
untouched.

## The surviving MATH (verified)

- **M-1 — the golden substitution's fusion algebra is the Fibonacci/Yang–Lee fusion algebra.** `[[1,1],[1,0]]`
  (substitution) and `[[0,1],[1,1]]` (Fibonacci fusion) share char poly `λ²−λ−1`, Perron eigenvalue `φ` = the quantum
  dimension of `τ`. Real and known. The **categorification** (F/R matrices, braiding, central charge) is **not** a
  framework output.
- **M-2 — the metallic family is the achiral (CS=0) + imaginary-quadratic corner** of the once-punctured-torus
  bundles. The Chern–Simons invariant of `M_m² = R^m L^m` is **identically 0** (SnapPy `complex_volume`, machine zero,
  `m=1..6`), against a discriminating census **mix** (m003 CS=4.93, m006=−2.25, m004=0). Structural reason: `R^m L^m`
  is palindromic under reverse+swap (the swap conjugation sends `L^m R^m → R^m L^m`) — an orientation-reversing
  symmetry, hence amphichiral.
- **M-3 — `expansion ⊥ physical-(unitary)-topological-order`.** Metallic `m≥1` are hyperbolic → **non-unitary**
  complex-CS TQFT, and CS=0 → chiral central charge `c₋ = 0` → **non-chiral**. Physical anyons need a *unitary*
  modular category; chiral order needs `c₋≠0`. The metallic members are neither. The only member that could give
  unitary order is `m=0` (swap, `λ=1`, non-hyperbolic) — which has **no expansion**. *Sharper (new):*
  `λ_m = (m+√(m²+4))/2 < 2` **only for `m=1`**; a `2cos(π/(k+2))` quantum dimension is always `< 2`, so **only the
  golden case can be a quantum dimension at all** (`m≥2`: `λ_m>2` → no categorification — a one-line reason behind the
  tombstoned "only m=1 categorifies").
- **M-4 — the arithmetic trichotomy (decisive separation).** The framework's three faces live in arithmetically
  **disjoint** worlds: **fusion/substitution** `→ ℚ(√(m²+4))` (real; `m=1 → ℚ(√5) ⊂ ℚ(ζ5)`) = the quantum
  *dimension*; **manifold geometry** `→` imaginary quadratic (`m=1 ℚ(√−3)=ℚ(ζ3)`, `m=2 ℚ(i)`); **braiding/twist** `→`
  `ℚ(ζ5)`-phase. Since `gcd(3,5)=1`, `ℚ(ζ3) ∩ ℚ(ζ5) = ℚ`. So "figure-eight quantized = Fibonacci" **conflates** the
  substitution (`ζ5`) with the manifold (`ζ3`); the manifold's hyperbolic geometry plays **no role** in the Fibonacci
  link.

## The proper name (the strongest survivor — `knowledge/K010`)

The object is a **Schrödinger cocycle over the metallic-mean substitution subshift**, analyzed by its
**Kohmoto–Kadanoff–Tang trace map**; `κ = tr[A,B]` is its **Fricke–Vogt invariant**. The dictionary is exact and
computed: `I = κ − 2` vanishes precisely on the commuting/reducible locus, so
```
   κ = 2  (I=0)  =  commuting / abelian  =  periodic chain, AC spectrum [−2,2]   ("cancellation")
   κ > 2  (I>0)  =  irreducible          =  trace map hyperbolic (Damanik–Gorodetski horseshoe), Cantor spectrum
```
(the void Jacobian is hyperbolic with spectrum `{φ²,−1,φ⁻²}` (B124); the elliptic point is neutral — both verified).
So **"existence as non-cancellation" has an exact named translation: non-cancellation = Fricke–Vogt positivity =
hyperbolicity of the renormalization trace map = the Cantor spectrum of an aperiodic Schrödinger operator** (Sütő
1987; Damanik–Gorodetski). This is **emergent / condensed-matter** physics (aperiodic order, real and observed) — the
strongest honest "this is physics" the arc has produced — and it is **not** fundamental physics.

The three **BMR arithmetic** once-punctured-torus-bundle classes, named: `RL → ℚ(√−3)`, `RRLL → ℚ(i)`, `RRL → ℚ(√−7)`
(the `√−7` representative is **non-metallic** — refining the B125/B126 "exactly two" correction).

## The kills (first-class — tombstoned)

- **K-A/K-B — "det=−1 breaks chirality / selects the SM chiral structure": DEAD, and INVERTED.** Topologically
  `det=−1` is the orientation-**reversing symmetry** (the deck transformation of the orientation double cover) that
  makes `M_m²` amphichiral, and the chiral invariant (CS) is exactly the one that is **0**. The SM split is 8/7; the
  n=4 chiral/achiral split is 6/9 — different numbers. *(Scope: this inverts the **topological** chirality reading.
  B124's "det=−1 breaks chirality" was the **algebraic P-parity** of the tower — the `char(−M^h)` sectors,
  representation theory — which is orthogonal to the manifold's CS and stands unchanged.)*
- **K-C — "figure-eight quantized = the *physical* Fibonacci order / det=−1 selects the braiding chirality": DEAD**
  (four reasons: k=3 selected-not-forced; the native quantization is non-unitary → **Yang–Lee** side (`c=−22/5`), not
  the unitary Fibonacci (`c=+14/5`) invoked; CS=0 contradicts chirality selection; the `ζ5`-vs-`ζ3` arithmetic
  separation). The framework supplies only the **fusion rule** — shared by Fibonacci *and* Yang–Lee — never the
  braiding/twist/central charge.
- **K-D — "physical (unitary) topological order from the metallic family": DEAD** (M-3).
- **K-E — "a forced dimensionful scale or non-generic physical ratio": DEAD** (null test vs `α⁻¹`, `m_p/m_e`,
  `sin²θ_W`; all hyperbolic-unit invariants).

## One thin open thread (DORMANT, not recommended)

**T-1 (`speculations/S030`).** The non-unitary character points toward **Yang–Lee / Lee–Yang edge**
(non-equilibrium critical phenomena), *not* topological QC — but the framework supplies only the fusion rule (shared),
not the distinguishing braiding/central charge, and the manifold's `ζ3` doesn't match Yang–Lee's `ζ5`. Fusion-rule
only; **no computed bridge**. Record; do not pursue without a forced braiding/central-charge.

**Anchors:** B124 (the void Jacobian / algebraic P-parity — distinct from this topological chirality), B125/B126 (the
arithmetic members + the BMR correction), `knowledge/K007` (the KKT/quasicrystal background), `K010` (the naming),
`philosophy/P007`/`P008`. External: Kohmoto–Kadanoff–Tang 1983; Sütő 1987; Bellissard (gap labeling);
Damanik–Gorodetski (the Fibonacci-Hamiltonian horseshoe); Bowditch–Maclachlan–Reid 1995; Ostrik (Fibonacci
categorification).
