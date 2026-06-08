# The ladder to physics — literature map (five-agent survey, B126)

Firewalled; a **citation map**, not a claim. The result of a five-agent literature survey supporting the B126 "how
far does rigidity propagate?" investigation. Each rung is tagged `[THEOREM] / [CONSTRUCTION] / [CONJECTURE] /
[NO-RESULT]`. Nothing here promotes to `../CLAIMS.md`.

## Rung 1 — quantization: arithmetic → the field of the quantum invariant (PROVED, incl. our family)

- `[THEOREM]` the Dimofte–Garoufalidis perturbative series of an ideal triangulation has **coefficients in the
  invariant trace field** — **arXiv:1202.6268**; "...adjoined a root of unity" — **arXiv:1511.05628**.
- `[CONJECTURE→PROVED for us]` the **1-loop conjecture** (1-loop term = adjoint Reidemeister torsion, an element of
  the trace field): **proven for all once-punctured-torus bundles** — Yoon **arXiv:2110.11003**; and for 2-bridge
  knots incl. `4₁` — **arXiv:2411.03801**.
- `[THEOREM]` quantum modularity of `4₁` (Garoufalidis–Zagier **arXiv:2111.06645**); the matrix invariant is indexed
  by the boundary-parabolic flat connections; the finest grading = the **`K₃`/Bloch-group class** of the trace field
  (Garoufalidis–Scholze–Wheeler–Zagier **arXiv:2412.04241**).
- `[CONSTRUCTION]` state-integral / 3D-index factorize into holomorphic blocks indexed by the flat connections, q-series
  in the trace field (Garoufalidis–Kashaev **arXiv:1304.2705**); resurgence/Stokes from CS values of flat connections
  (Garoufalidis–Gu–Mariño **arXiv:2012.00062**).
- **Caveat:** the trace-field-valuedness is **universal** (every number field) — imaginary-quadratic / Bianchi fields
  are **not** quantum-special in the literature; `ℚ(√−3)` appears only because `4₁` is the simplest example. A
  "metallic family is quantum-special" claim would be **new/unsupported**; the one untested door is the `K₃`/Bloch
  grading on `ℚ(√−3)`, `ℚ(i)`.

## Rung 2 — the 3d theory `T[M]`: rigid, and `M` selects its IR phase

- `[CONSTRUCTION]` `T[4₁]` = two ideal-tetrahedron theories glued ≈ `U(1)` + 2 chirals, no CS — a concrete small
  **rank-1 abelian** 3d N=2 SCFT; vacua = the three flat connections = the A-polynomial (DGG **arXiv:1108.4389**,
  **1112.5179**; all-flat-connections correction **arXiv:1405.3663**).
- `[CONSTRUCTION]` Mostow rigidity ⇒ `T[M]` has **no marginal couplings / no conformal manifold**.
- `[THEOREM-level]` `M` **selects the SUSY phase**: no irreducible `SL(2,ℂ)` flat connection ⇒ SUSY spontaneously
  broken; `4₁` has them ⇒ **unbroken SUSY, gapped vacua** (Cho–Gang–Kim **arXiv:2007.01532**; Gang–Yonekura
  **1803.04009**).
- `[CONSTRUCTION]` `H₁(M)` torsion ↦ the **one-form/center symmetry + line-operator spectrum / polarization** of `T[M]`
  (Aharony–Seiberg–Tachikawa; "Generalized global symmetries of `T[M]`" **arXiv:2511.13696**, JHEP04(2021)232). →
  fenced reading `S029`.

## Rung 3 — 3d → 4d: the determination is LOST here

- `[ESTABLISHED]` a 3-manifold's native output is **3d**; the 4d theory it touches is data of a **2-dimensional
  boundary surface `∂M`**, not of `M` (DGG **1108.4389**; "3d-3d revisited" **1405.3663**).
- `[ESTABLISHED]` class-S 4d N=2 comes from a **Riemann surface** (dim 2); the once-punctured torus gives **N=2\*** (=
  N=4 SYM + adjoint mass), `4₁`'s 3-manifold appearing only as a **duality wall / monodromy** inside it (Gaiotto
  **0904.2715**; Terashima–Yamazaki **1103.5748**; Cecotti–Córdova–Vafa **1110.2115**).
- `[ESTABLISHED]` geometric Langlands = S-duality of **4d N=4 SYM** (Kapustin–Witten **hep-th/0604151**). **Honest
  ceiling: N=4 SYM / N=2\*** — non-chiral, no generations, **not the Standard Model**.

## Rung 4 — SUSY breaking + particle masses: orthogonal input

- `[NO-RESULT]` no mechanism lets manifold topology select a SUSY-breaking vacuum or fix the breaking *scale* — it is
  flux/landscape data (Douglas **hep-th/0405189**; **arXiv:2007.04327**). Geometry fixes only the *existence* of
  unbroken SUSY (special holonomy).
- `[ESTABLISHED]` Mostow rigidity ⇒ "no marginal couplings," but **not** "determined masses": masses are *relevant*
  parameters (puncture data, Coulomb vevs, breaking scales), none of them manifold invariants.

## Arithmetic-classification corrections (used in the B125/K009 fix)

- `[THEOREM]` there are exactly **three** cyclic commensurability classes of arithmetic once-punctured-torus bundles
  (Bowditch–Maclachlan–Reid, Math. Ann. 302 (1995) 31–60). The figure-eight `m004` and its sister `m003` are **two
  distinct bundles in one class** (both `ℚ(√−3)`). So "the two arithmetic members of the `R^m L^m` family" (`m=1`
  `ℚ(√−3)`, `m=2` `ℚ(i)`, B125) is a **family-restricted** statement — *not* the global count of two. (Corrects the
  inherited "exactly two arithmetic punctured-torus bundles" framing.)
- `[NO-RESULT]` there is **no** "arithmetic ⟺ simple A-polynomial" theorem; arithmetic manifolds routinely have
  complicated A-polynomials. The only link is Mahler-measure ↔ Dedekind-zeta (analytic size, not degree). So the
  B126(B) correlation is a genuine **family-specific** observation, not a law (Hoste–Shanahan; Champanerkar; Calegari
  **math/0510416**: OPT-bundle trace fields have no real places and unbounded degree).

## The one-line verdict

Rigidity propagates **two floors** (the quantization's number field; the 3d theory's rigidity + SUSY phase), and is
**lost** at the 3d→4d boundary and the SUSY scale. The object is a maximal probe of the geometry↔QFT correspondence
with a **provable ceiling at N=4 SYM** — see `../frontier/B126_ladder_to_physics/FINDINGS.md`, `../philosophy/P007`,
`S029`.
