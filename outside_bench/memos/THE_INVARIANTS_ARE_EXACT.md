# Memo 218 — L72's LEVEL-2 INVARIANTS, EXACTLY — AND THE UNIQUENESS RESIDUAL REACHES NONE OF THEM

**Seal:** `outside_bench/seals/L72_EXACT_INVARIANTS_PREREG.md`, sha256
`4621857a643e631fbb6d1ceeb2bcee450aa58122db4f50947236cb301082b6a3`, committed before the
certificate was written.
**Certificate:** `outside_bench/certificates/l72_exact_invariants.py` ·
**Output:** `outside_bench/outputs/l72_exact_invariants.txt`
**Outcomes: CELL 1 = A · CELL 2 = A · CELL 3 = A · CELL 4 = A.** Controls C1–C3 all pass.

---

## 0. What was left

Memo 211 left L72 with one residual, in the cell's own words: *"uniqueness-up-to-gauge of the
level-2 F-symbols (constructed + verified, **not classified**)."* Memo 211 closed its
**Galois** half and named the rest as literature-gated. **Two things under it turned out to
be settleable here.**

## 1. CELL 1 — the invariants are exact, and they are cubic

`P2W5-L72` reports the E₆ level-2 colored invariants of 4₁ as **floats**. Computed here in
`ℤ[ζ₇] = ℤ[x]/Φ₇(x)`, with no floating point anywhere in the cell:

| N | spin | `J_N(ζ₇)` exactly | minimal polynomial over ℚ | degree |
|---|---|---|---|---|
| 1 | 0 | `1` | `x − 1` | 1 |
| 3 | 1 | `−2z⁵ + z⁴ + z³ − 2z² + 3` | **`x³ − 10x² + 17x − 1`** | 3 |
| 5 | 2 | `2z⁵ + z⁴ + z³ + 2z² + 2` | **`x³ − 3x² − 4x − 1`** | 3 |

**And they generate the same cubic field**, identified by discriminant: `ℚ(ζ₇)⁺` has
generator `x³ + x² − 2x − 1`, disc **49**; the N = 3 minimal polynomial has disc **8281 =
49 · 13²** (ratio a rational square) and the N = 5 one has disc **49 exactly** (ratio 1).

> **The object's E₆ level-2 colored invariants of the figure-eight live in `ℚ(ζ₇)⁺`, the
> real cyclotomic cubic of discriminant 49.** The invariant that carries the **E₆ adjoint**
> — the cell's own note places the 78 at spin 2, N = 5 — is a root of
> **`x³ − 3x² − 4x − 1`, discriminant 49 on the nose.**

## 2. CELL 2 — the floats were right

Evaluated at 30 digits: `1.0000000000000`, `2.0881460000204`, `−0.6920214716301`, each with
imaginary part `1.2e−35`. **Agreement with the cell's printed values at every printed
digit**, and the vanishing imaginary parts confirm what the exact form already says — the
values are real, because Habiro's product is symmetric under `q → q⁻¹`.

## 3. CELL 3 — the residual reaches nothing the cell reports

`J_fig8`'s entire body, quoted by the certificate, is five lines of `q` and `N`. **F-symbol
and associator tokens inside it: none.** The colored invariants are computed from Habiro's
closed form alone.

And across the cell's seventeen stored keys, `D_object` holds the only reported knot
numbers; `C_level2` stores **counts** of F-symbols (2646) and **verification residuals**, not
a quantity anything downstream consumes; every other stored value —
`A_modular_data`, `E_principal_index`, `F_CS_basepoint`, `G_deformation`, `H_CS_theta_even`,
`I_wall` — comes from the Weyl sum, SnapPy, or Fox calculus.

> **The uniqueness residual is real as a statement about the CATEGORY and inert for every
> NUMBER the cell reports.** It qualifies the claim *"these are the F-symbols"*; it does not
> touch a single computed invariant.

## 4. CELL 4 — the field is not the object's charge field, and the Galois type is why

A reader may hope the level-2 invariants land in `K`, the object's trialitarian cubic from
memo 204. Both sides computed:

| | polynomial | disc | Galois group |
|---|---|---|---|
| **K** | `x³ − 12x − 5` | 6237 = 3⁴·7·11, squarefree part **77** | disc not a square ⇒ **S₃, non-cyclic** |
| **ℚ(ζ₇)⁺** | `x³ + x² − 2x − 1` | **49** | disc a square ⇒ **C₃, cyclic** |

> **Not isomorphic, and not by accident of coefficients: by Galois type.** `K`'s
> non-cyclicity is exactly what memo 204 used to make the object **⁶D₄** — the same fact
> that killed B882's triality now also separates the object's charge field from the field its
> quantum invariants live in. **7 divides both discriminants, and that is the whole of the
> resemblance.**

## 5. Controls

- **C1** — Habiro's form reproduces the **Jones polynomial of 4₁** at N = 2 **exactly** in
  `ℤ[q, q⁻¹]` (difference identically 0). The cell checked this numerically at a generic
  value; it is exact here.
- **C2** — the tail-vanishing claim: the `j = N` factor is identically zero for N = 1, 3, 5,
  so the cell's loop running one step past the standard sum changes nothing.
- **C3 (MB12)** — the minimal-polynomial routine returns **6** for `ζ₇` and **1** for a
  rational, so "degree 3" is a finding and not the only answer it can give.

## 6. What is left of L72, stated exactly

| | |
|---|---|
| phase 1 — the principal torsion | **DONE**, memo 210 |
| phase 2 — the 6j at levels 1–2 | **sound, independently reproduced** (memo 211); its stale artifact regenerated (memo 216) |
| the uniqueness residual | **narrowed to a categorical footnote**: Galois ambiguity closed (memo 211), and **no reported number depends on it** (here). What remains is *"does modular data determine a rank-3 modular tensor category"* — **literature, unread here, and not cited** |
| phase 3 — CS along the θ-odd direction | **WALLED / EXTERNAL** by the cell's own computation |

> **INTERPRETIVE.** L72 has no computable content left on this bench. Its one open clause is
> a citation, and the clause now qualifies nothing anyone has used.
