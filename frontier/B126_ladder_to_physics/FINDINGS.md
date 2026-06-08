# B126 — The ladder to physics: how far does the metallic rigidity propagate? (V115)

A foundational-question investigation, run with a five-agent literature fleet + direct computation. **Question:** the
metallic object is maximally rigid at the *classical* character-variety level (Level 1) — does that rigidity
**propagate** up the ladder to physics (quantize → 3d N=2 theory `T[M]` → 4d → particle content), or does the
determination **dilute**? **Answer:** it propagates **exactly two floors, provably**, then hits a *nameable* wall. So
we lack no *concept* — we lack the one thing no 3-manifold can supply. MATH / number-theory tier; the physics
*readings* are firewalled (`speculations/S029`, `philosophy/P007`, `PHYSICS_BRIDGE_MAP.md`). Nothing to `CLAIMS.md`;
P1–P16 and the functorial `Sym(W)→trace-ring` wall (B85) untouched.

## Computed in-house (verify-don't-trust)

### (A) The homology torsion *is* the metallic parameter

`H₁(M_m) = ℤ ⊕ (ℤ/m)²` for the orientable metallic bundle `M_m² = R^m L^m`. **Proof:** the mapping-torus homology
is `ℤ ⊕ coker(φ_* − I)` with `φ_* = M_m²` on `H₁(fiber)=ℤ²`; the Smith normal form of `M_m² − I = m·M_m =
[[m²,m],[m,0]]` has invariant factors `(m, m)`, so `coker = ℤ/m ⊕ ℤ/m`. Confirmed by SnapPy for `m=1..7` (`m=1`: `ℤ`
— the figure-eight has no torsion; `m=2`: `ℤ/2⊕ℤ/2⊕ℤ`; …). The metallic `m` **is** the order of the homology
torsion — structural, no free choices. *(The physics reading — `H₁` torsion ↦ one-form/center symmetry of `T[M]` —
is the firewalled `S029`.)*

### (B) Arithmetic ⟺ A-polynomial simplicity (family-specific)

On the **geometric component** of the bundle character variety (`Fix` of the monodromy trace map, built from the
Dehn-twist trace maps `T_a, T_b` on Fricke coordinates), the degree of the commutator coordinate `κ = tr[a,b]` over
`ℚ(z)` is **`[1, 1, 3, 3, 7, 6]`** for `m=1..6` (computed exactly here for `m≤4`; `m=5,6` recorded). `κ` is
**rational in the parameter** exactly for the two **arithmetic** members (`m=1,2`, B125), with a sharp jump at the
arithmetic boundary `m=2/3`. **Honest scope (load-bearing):** this is a **family-specific observation, not a law.**
The literature has **no** "arithmetic ⟺ simple A-polynomial" theorem — arithmetic manifolds routinely have
complicated A-polynomials; the only genuine link is Mahler-measure ↔ Dedekind-zeta (an analytic *size*, not a
*degree*). So this is a real correlation within the `R^m L^m` family, offered as such, not generalized.

## The ladder map (literature-grounded — the answer to the foundational question)

**Rigidity propagates exactly two floors, then dies at a nameable wall.**

- **Floor 1 — arithmetic → quantization (PROVED, for our exact family).** The invariant trace field determines the
  **field** in which the perturbative quantum series lives — a *theorem*: the Dimofte–Garoufalidis series has
  coefficients in the invariant trace field (arXiv:1202.6268, 1511.05628), and the **1-loop conjecture** (1-loop term
  = adjoint Reidemeister torsion, an element of the trace field) is **proven for all once-punctured-torus bundles**
  (Yoon, arXiv:2110.11003) and 2-bridge knots incl. `4₁` (arXiv:2411.03801). The finest grading — which Habiro
  module the invariant lives in — is the `K₃`/Bloch-group class of the trace field (Garoufalidis–Scholze–Wheeler–
  Zagier, arXiv:2412.04241). *In-house confirmation of the adjoint torsion is Sage-gated in SnapPy; cited instead.*
  **Caveat:** this trace-field-valuedness is *universal* (every number field), so imaginary-quadratic / Bianchi
  fields are **not** "quantum-special" in the literature — `ℚ(√−3)` appears only because `4₁` is the simplest
  example. Any "the metallic family is quantum-special" claim would be **new and unsupported**; the one untested door
  is whether the `K₃`/Bloch-group grading has special structure on `ℚ(√−3)`, `ℚ(i)`.

- **Floor 2 — rigidity → rigidity of `T[M]` (ESTABLISHED).** Mostow–Prasad rigidity (`M` has no moduli) ⇒ `T[M]` has
  **no marginal couplings / no conformal manifold** — a real, established consequence. And `M` genuinely **selects the
  SUSY phase**: when `M` has no irreducible `SL(2,ℂ)` flat connection, SUSY is spontaneously broken; `4₁` *has*
  irreducible flat connections ⇒ **unbroken SUSY, gapped massive vacua** (Cho–Gang–Kim, arXiv:2007.01532). The `H₁`
  torsion of (A) controls the **one-form/center symmetry and line-operator spectrum** of `T[M]` (DGG arXiv:1108.4389;
  Aharony–Seiberg–Tachikawa; the "Generalized global symmetries of `T[M]`" line, arXiv:2511.13696). `T[M]` itself is a
  concrete small **rank-1 abelian** 3d N=2 SCFT (two ideal tetrahedra; ≈ `U(1)` + 2 chirals), whose vacua reproduce
  the three flat connections / the A-polynomial — i.e. exactly the trace-map structure of this whole program.

- **The wall (where determination is LOST).** Two independent leaks, both nameable:
  1. **3d → 4d.** A 3-manifold's native output is *3d*. The 4d theory it can touch is data of a **2-dimensional
     boundary surface `∂M`**, *not* of `M`; the once-punctured torus gives 4d **N=2\*** (= N=4 SYM + adjoint mass),
     and `4₁`'s 3-manifold appears only as a *duality wall / monodromy* inside it (Terashima–Yamazaki arXiv:1103.5748;
     class-S: Gaiotto arXiv:0904.2715). The honest ceiling is **N=4 SYM / N=2\*** (geometric Langlands, Kapustin–Witten
     hep-th/0604151) — non-chiral, no generations, **not the Standard Model**.
  2. **The SUSY-breaking *scale* and particle masses** are *orthogonal input* — no mechanism lets manifold topology
     select a SUSY-breaking vacuum or scale (it is flux/landscape data). "No moduli" ⇒ "no marginal couplings," but
     **not** "determined masses" (masses are *relevant* parameters from puncture data, vevs, breaking scales).

**Conclusion.** We don't lack a concept or a computation. We lack precisely what a 3-manifold cannot carry: the
2d-boundary / decompactification data that fixes the 4d theory, and the orthogonal SUSY-breaking input that fixes the
scales. The metallic object is a **maximally rigid probe** of the geometry↔QFT correspondence whose determination
**provably reaches two floors and provably stops** — a sharp, honest, citable result, and the firewall reasserted one
level higher with a name on it (`philosophy/P007`).

## What this reframes (the wrong question / the right one)

"How do we bridge to fundamental physics?" is the wrong question — the ceiling is *provably* N=4 SYM. The right,
answerable questions are: **(i)** how far does the rigidity propagate? (two floors, wall named — answered here); and
**(ii)** is the object's *arithmetic* special in the quantization? (the trace-field-valuedness is universal/proven;
the `K₃`/Bloch grading on `ℚ(√−3)`, `ℚ(i)` is the one genuinely-untested door — DORMANT, `S027`-adjacent, MAGMA-heavy).

**Anchors:** B125 (the arithmetic members `m=1,2`), B107/K006/K007 (the firewall, the 3d-3d dictionary), the
five-agent literature map (`speculations/LADDER_LITERATURE.md`). External (load-bearing): Dimofte–Garoufalidis
1202.6268/1511.05628; Yoon 2110.11003; Garoufalidis–Zagier 2111.06645; Garoufalidis–Scholze–Wheeler–Zagier
2412.04241; Cho–Gang–Kim 2007.01532; DGG 1108.4389; Gaiotto 0904.2715; Terashima–Yamazaki 1103.5748; Kapustin–Witten
hep-th/0604151; Bowditch–Maclachlan–Reid 1995 (the *three* arithmetic commensurability classes — see the B125/K009
correction). Firewalled readings: `speculations/S029` (center symmetry), `philosophy/P007` (the reframe).
