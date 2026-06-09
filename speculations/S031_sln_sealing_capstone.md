# S031 — The SL(n) sealing capstone: prove the metallic trace map fixes only the `Sym^{n−1}` image

**Status: `OPEN` — tier: MATH (a genuine mathematics target, EXPLICITLY NOT a physics bridge).** Recorded here as the
natural closure of the firewall arc, not as a physics reading. Nothing promotes to `../CLAIMS.md`; P1–P16 untouched.
*(This entry is the one MATH item in `speculations/`; it carries no firewalled physics overlay — it is filed here
because it is the open continuation of B129, the tower-sealing investigation.)*

## The conjecture

> **For all `m ≥ 1` and `n ≥ 2`, the metallic SL(n) trace map fixes *only* the `Sym^{n−1}` image of its SL(2) fixed
> point.** Equivalently: the SL(n) once-punctured-torus character variety carries no off-sublocus genuine irreducible
> fixed conjugacy class of the metallic monodromy — the only fixed irreducible content is the principal `Sym^{n−1}`
> embedding of the SL(2) Fibonacci datum.

> **Reframe (B140/V129) — this is a RIGIDITY statement, not field-sealing; the φ-fixed content is RATIONAL.** The
> object is the discrete fixed locus of the **single** map `φ_m` (`det[[m,1],[1,0]] = −1`, see the object note below).
> Its unique irreducible fixed point is the **rational** principal `Sym^{n−1}` of the SL(2) point `(0,0,0)` (verified
> m=1,2): SL(2) `(trA,trB,trAB)=(0,0,0)` (κ=−2), SL(3) trace coords `(−1,−1,−1)`, commutator `3`. So "sealed in the
> SL(2) trace field `K_m` (ℚ(√−3) at m=1)" is **true but loose** — `K_m` is the **`φ²`-geometric-bundle** field; the
> φ-fixed content is **ℚ** (a tighter seal, ℚ ⊂ `K_m`). The real content is **uniqueness/rigidity of the principal
> fixed point**; the field-sealing is a loose corollary. This reframes the open converse (B138's hard half) as a
> rigidity problem (the `K003` Dickson/Chebyshev flavor), **not** a field question — and a cleaner target. *(B129's
> 0-escape conclusion stands: ℚ ⊂ ℚ(√−3). B129 S1a's exact ℚ(√−3) `Sym²` was the `φ²`-bundle rep, not the φ-fixed
> point — a φ-vs-φ² calibration.)* **Retracted (never banked):** "non-principal φ-fixed points carry ℚ(√−3)" /
> "the converse routes to Heusener–Muñoz–Porti" — there are **no** non-principal irreducible φ-fixed points (verified),
> so the converse is rigidity, not an HMP classification.

Proving this upgrades B129 from **computer-assisted-strong** (m=1; SL(3); 427 off-sublocus points, max deviation
`1.2e-6`, 0 escapes; the principal-route arithmetic exact) to **proved for all m, n**.

## Why it is plausible (the B129 evidence)

- **Exact at the principal locus (m=1, SL(3)):** the `Sym²` image is irreducible (algebra `= M₃`) yet every trace lies
  in ℚ(√−3) — SL(2) data reparametrized, no new field (`../knowledge/K012`, B129 S1a).
- **Empty off the sublocus (m=1, SL(3)):** the root-find over the 4-dim bulk lands only on the reducible sublocus +
  degenerate trivial/central reps; no fixed point escapes ℚ(√−3) (B129 S1b).
- **Structural reason to expect it:** climbing the tower is the principal `SL(2)→SL(n)` embedding (`K003`/`K005`); a
  fixed point of the lifted map that is *not* the lift of an SL(2) fixed point would be new content the embedding does
  not obviously supply, and B129 finds none.
- **Extended to m=2 (B137/V126):** the SL(3) sealing now holds for **both arithmetic metallic members** — m=1 in
  ℚ(√−3) (B129) and **m=2 (silver) in ℚ(i)** — among irreducible off-sublocus fixed points, 0 escapes from `K_m` (2
  seeds each). *(En route, a verify-don't-trust catch: the **reducible** locus fakes escapes — its `κ` is not in `K_m`
  — so escapes must be counted only among irreducible (algdim=9) points; method note **MB7**, `../REPRODUCIBILITY.md`.
  m≥3 has non-quadratic `K_m`; SL(n≥4) needs SL(4) trace coordinates — both still open.)* *(B140/Item 5: the
  `φ²`-geometric-bundle trace fields are m=1→ℚ(√−3), m=2→ℚ(i) — imaginary quadratic, the two arithmetic members — and
  m≥3→higher-degree; this is a **structural** fact about the `φ²` bundles, not a compute limit, and is a **different
  object** from the `φ`-fixed content above. Note `[[m,1],[1,0]]² = RᵐLᵐ`, so the `φ²` bundles **are** the `RᵐLᵐ`
  once-punctured-torus bundles, and `(m,m)` is a cyclic palindrome ⟹ every metallic bundle is amphichiral, B134/`K011`.)*

- **Principal-image direction PROVED (B138/V127):** the *easy half* — the principal `Sym^{n−1}` image of an SL(2) rep
  over `K` is a `K`-sealed fixed point for **every n** (because `Sym^d` is ℤ-defined: `Sym^d(g)`'s entries are integer
  polynomials in g's, so `g∈SL(2,K) ⟹ Sym^{n−1}(g)∈SL(n,K)` and all word-traces ∈ K). Verified n=2..5, m=1 (ℚ(√−3))
  and m=2 (ℚ(i)). What remains is the **converse** (nothing *else* escapes `K_m`, all n) — the hard half.
- **SL(4) bulk: OPEN, intractable in-session (B138).** The B137-style off-sublocus root-find at SL(4) times out with a
  faithful 340-word separating residual, and under-pins the character with a lighter one; needs a complete SL(4)
  trace-coordinate set (Lawton-for-SL(3) analogue) or a symbolic component analysis (NEEDS-EXPERTISE).
- **Object note (B138, sharpened B140 — the `φ` vs `φ²` mechanism):** S031 is about the **discrete** fixed points of
  `φ_m(A,B)=(A^m B,A)` (B129/B137), *not* B71's positive-dimensional **geometric** components (V0/W1/W2). The principled
  reason: the metallic incidence `N=[[m,1],[1,0]]` has **`det = −1`** (orientation-reversing) and **`N² = RᵐLᵐ`**
  (verified). So the **single** `φ_m` (det −1) has **isolated/discrete** fixed points (S031's object — verified SL(2):
  2 points), while `φ_m²` (det +1, `= RᵐLᵐ`, the **bundle**) has a **positive-dimensional** fixed locus (B71's
  geometric character variety — verified SL(2): a curve). A generic `φ²`-component point has continuous traces (no
  number field) and does not test sealing — which is why B138's `realize_bundle_rep` check returned "OTHER".

## What a proof needs (the obstruction)

A general-`n` argument for the **converse** — that the metallic monodromy's fixed conjugacy classes on the SL(n)
character variety are exactly the `Sym^{n−1}` images (the forward direction is B138). Candidate routes: (i) a
representation-theoretic rigidity argument (the principal `Sym^{n−1}`
is the unique irreducible fixed locus because the monodromy's action on the higher trace coordinates is generated by
the SL(2) data — the same flavour as the `K003` Dickson/Chebyshev structure); (ii) an explicit Lawton-coordinate
fixed-point analysis at SL(3) made symbolic in `m`, then an induction on `n`. The known walls are the absence of an
SL(n≥4) character-variety classification (`S025`/B115) and the saddle (non-attracting) nature of the fixed points
(B129 method bug B2 — root-find, don't iterate).

## Boundary

This is **mathematics on the tower** — there is **no remaining physics-bridge content**. The physics reading (the
firewall confirmed from inside the tower; `../philosophy/P007` sixth direction) is already banked at the B129 level; a
proof of S031 sharpens the *math*, not the firewall. It sits alongside the project's other open MATH prizes (the
functorial `Sym(W)→trace-ring` wall B85; the `μ_d` plethysm `K003`/B103), distinct from all firewalled `S`-entries.

**Anchors:** B129/V118 (`../knowledge/K012`; the m=1/SL(3) evidence), `K003`/`K005` (the Dickson tower / principal
SL(2)), `K001` (Lawton/Fricke coordinates), `S025` (the off-principal higher-rank obstruction), B115 (no SL(n≥4)
classification). External: Lawton (SL(3) trace coordinates, 2007).
