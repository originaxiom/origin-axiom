# The SL(n) figure-eight: a metallic trace-map tower and a Dehn-filling A-polynomial family

**Internal paper skeleton (draft, Phase E).** Status: a structured outline of the publishable content,
with the **proof-status of each piece explicit**. Internal only — **no promotion to `CLAIMS.md` without
the GOVERNANCE §5 gate; `EXPERT_OUTREACH.md` dormant; the external novelty check (below) is the gate
before any external claim.** Backed by the V1–V68 locking tests.

## The object

All results concern **one object**: the figure-eight knot's character variety, realized as the fixed
locus `Fix(T_1²)` of the (squared) metallic trace map `T_1` on SL(n,C) trace coordinates (the figure-eight
is the once-punctured-torus bundle with monodromy `φ = [[2,1],[1,1]] = M²`). Two faces:
- a **dynamical** face (the trace-map Jacobian — Thread 1), and
- a **geometric/peripheral** face (the cusp A-variety — Threads 2–3).
B77 showed these faces are **distinct** (not unified through the eigenvalue spectrum).

## Thread 1 — the metallic trace-map tower  *(dynamics)*

The `(n²−1)`-dimensional fixed-line Jacobian `J(m)` of the metallic trace map factors over the **Dickson
catalog** `char(±Mᵏ) = t² ∓ L_k t + (−1)^k`, `L_k = tr([[m,1],[1,0]]^k)`:

| `n` | factorization | proof status |
|---|---|---|
| 3 | `char(M⁻¹)char(M²)char(M³)(t−1)(t+1)` | **PROVED** (symbolic, all `m`; B54/B64) |
| 4 | `char(M⁻¹)char(M)char(M²)char(M³)char(M⁴)char(−M²)(t−1)²(t+1)` | **PROVED from first principles** (B80/V62, CRT/F_p over ℚ[m]) |
| 5,6 | (the `n=5,6` rows) | **STRUCTURAL** (B62 opposition-involution `θ=−w0`; numerically corroborated) |

- The **parity grading** (even-`|k|` P-symmetric, odd-`|k|` P-antisymmetric) is **PROVED** (B64) and is
  the same `−w0` of `A_{n−1}` that grades the W_N charge-conjugation (B74) — pure invariant theory.
- The **first-principles `n≥5` proof** is reduced (B85) to **one symbolic step**: assembling the bounded
  rank-1 `e₂/Λ²` closure (B70, bidegree `≤(3,3)`) into the exact trace map `σ`, where `Dσ` is canonical
  by construction. Numerical routes are **dead** (B84: pinv-limit non-convergence at the doubly-degenerate
  `char(M²)²` sector); Λ² functoriality (B85) is real but doesn't break the degeneracy.

## Thread 2 — the figure-eight A-polynomial  *(geometry)*

The trace-map fixed locus reproduces the published figure-eight character-variety data **exactly**:
- **SL(2):** the Cooper–Long A-polynomial `A(M,L)=M⁴L²+(−M⁸+M⁶+2M⁴+M²−1)L+M⁴`, derived exactly from
  `Fix(T_1²)` (B67). **VERIFIED (exact).**
- **SL(3):** the Falbel Dehn-filling A-variety (`W1=D2: M³=L`, `W2=D3: M³L=1`); the geometric component
  `V0` has no tidy form (matches Falbel's 141-poly). **computer-assisted, matches Falbel** (B71).

## Thread 3 — degree=rank and the `Aₙ` family  *(geometry / the main new result)*

On the **principal Dehn-filling component** `{tr A=tr A⁻¹=1}`:
- the matrix law **`[A,B] = (−1)ⁿ⁻¹ μⁿ`** (meridian `μ=A⁻¹t`, longitude `[A,B]`; B77/V60), and
- its **peripheral eigenvalue A-variety** **`L = (−1)ⁿ⁻¹ Mⁿ`** (B83/V66) — the figure-eight
  Dehn-filling A-polynomial:

| `n` | A-variety | status |
|---|---|---|
| 3 | `L=+M³` | Falbel (known) |
| **4** | **`L=−M⁴`** | **NEW** (the first SL(4) figure-eight A-polynomial from the trace map) |
| 5 | `L=+M⁵` (predicted) | principal SL(5) component not numerically locatable (B78) |

So the **`Aₙ` family `L=(−1)ⁿ⁻¹Mⁿ` (n≥3)** unifies Cooper–Long (SL(2)) and Falbel (SL(3)) and extends to
SL(4). **Mechanism:** the exponent = rank = the **principal component's Falbel filling slope**; the sign
`(−1)ⁿ⁻¹` is fixed by `det`; the meridian eigenvalues are generic. The full derivation of "slope = rank"
is the external-framework item (below). **high-precision-numerical** (`n=3,4`).

## Novelty positioning (internal — the gate before any external claim)

- **Known:** SL(2) Cooper–Long; SL(3) Falbel (`M³=L`); the metallic trace-map machinery is largely
  `STANDARD_REPACKAGE` (Lawton; Baake–Grimm–Roberts).
- **`APPARENTLY_NEW` — pending an external literature check** (the rule is no external contact, so this
  cannot be closed here):
  1. the **`Aₙ` family / the SL(4) A-polynomial `L=−M⁴`** — natural in the **Bergeron–Falbel–Guilloux**
     SL(n)/PGL(n) figure-eight framework, but I am not aware of it being stated; it is an `n≥3`
     phenomenon (A0: SL(2) degenerate), **not** `Sym^{n−1}` of an SL(2) filling. **The #1 thing to check.**
  2. the **CRT/F_p first-principles tower proof** (B80) as a technique;
  3. the **parity-graded Dickson factorization** + the opposition-involution sector structure (B62/B64).

## Open / future work
- The **general-`n` tower from first principles** — the bounded `e₂/Λ²` symbolic closure (B85); the
  lynchpin.
- The **"slope = rank" mechanism** — the BFG-framework derivation.
- The **principal SL(5) Dehn-filling rep** — needs the symbolic SL(5) trace-map (B78 numerics walled out).
- The **external literature check** (novelty item 1) — the gate before any claim.

## What is explicitly NOT here
The **physics chapter is closed** (V65/B82): every bridge (anyons V28, quasicrystals V29, j=1728
V34/V53, higher-spin V56, cusp/quantum-group V58) reduced to invariant theory of `sl(n)`. This is
**low-dimensional topology + invariant theory**, not physics.
