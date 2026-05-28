# A conditional uniqueness theorem for the Origin Axiom core

**Status:** formalization of conditional claim **C1** (`../CLAIMS.md`). This is a
*conditional* result — true given the minimal record axioms A1–A6 below, which are
motivated but not laws of nature. It is **not** a derivation of the substrate from
nothing (that direction is mapped dead — see `../PROGRESS_LOG.md` Phase C and the
frontier obstruction maps). Every computational lemma is locked by
`../tests/test_uniqueness_theorem.py`.

**One line:** the minimal record axioms force the persistent sector
`A = LR = [[2,1],[1,1]]` *up to the order convention `LR` vs `RL`*; from `A` the
entire proven core P1–P16 follows as exact consequences.

---

## 1. The axioms

We model a system of **records** — nonnegative integer counts that can be
transferred but not destroyed (the non-cancellation principle in its minimal
combinatorial form). The axioms below state what "minimal record-transfer system"
means precisely.

| # | Axiom | Formal content |
|---|---|---|
| **A1** | **Two-record substrate.** | The state space is `ℤ²` — a *pair* of integer record-counts. (Not one; not three.) |
| **A2** | **Reversible integer transfer.** | Updates are linear maps `ℤ² → ℤ²` invertible over `ℤ`, i.e. elements of `GL(2,ℤ)` (`det = ±1`). |
| **A3** | **Orientation-preserving.** | `det = +1`, i.e. the update monoid lies in `SL(2,ℤ)`. |
| **A4** | **Primitive one-channel update.** | An elementary update changes exactly one record as a function of the other, by a unit increment. These are exactly the two primitive shears `L = [[1,1],[0,1]]` and `R = [[1,0],[1,1]]`. |
| **A5** | **Torsion-free closure.** | The first *mixed* persistent sector — a product of both primitive moves — closes to a torsion-free mapping torus (trivial `H₁` torsion). |
| **A6** | **Minimality.** | Among admissible closures, take the one of minimal nontrivial complexity (equivalently: minimal hyperbolic trace). |

A5 and A6 are two routes to the same conclusion (see §3); either alone suffices
for the forcing. They are listed separately because each is independently
motivated — A5 by the topology (the once-punctured-torus bundle / figure-eight
side, P8–P10), A6 by the algebra (first hyperbolic class).

**A7 (the residual choice).** The axioms A1–A6 are symmetric under swapping the
two records, hence under `L ↔ R`. They therefore fix the persistent sector only
**up to the order `LR` vs `RL`**. Choosing `L`-before-`R` is the one irreducible
labeled input — see §5. It is not eliminable by any matrix-level axiom; it is the
smallest piece of inserted structure in the whole construction.

---

## 2. The first mixed closure

Generalize the primitive shears to `Lₐ = [[1,a],[0,1]]`, `R_b = [[1,0],[b,1]]`
(A4 fixes `a = b = 1`; we keep them free to *see* what the axioms select). The
first mixed persistent sector is

```
B(a,b) = Lₐ · R_b = [[1 + ab, a], [b, 1]].
```

Exact identities (locked by `test_mixed_closure_form`, `test_det_trace_and_torsion_formulas`):

```
det B(a,b)      = 1                  (A2/A3 automatic)
trace B(a,b)    = 2 + ab
det(B(a,b) − I) = −ab.
```

The mapping torus `M_B` of `B` acting on the 2-torus has
`H₁(M_B) = ℤ ⊕ coker(B − I)`, and when `det(B − I) ≠ 0` the group
`coker(B − I)` is finite of order `|det(B − I)| = ab` (its torsion).

---

## 3. The forcing (A1–A6 ⟹ ab = 1)

**Route A5 (torsion-free).** `H₁(M_B)` is torsion-free iff `coker(B − I) = 0` iff
`|det(B − I)| = ab = 1`. Over positive integers (A1–A4 give nonnegative counts and
primitivity, so `a, b ≥ 1`), the unique solution is `a = b = 1`.

**Route A6 (minimal hyperbolic trace).** `B` is hyperbolic iff `|trace B| > 2`,
i.e. `ab ≥ 1`; the trace `2 + ab` is then minimized at `ab = 1`, giving trace `3`.
Trace `2` is parabolic (the shears themselves), so `3` is the *first* hyperbolic
trace in `SL(2,ℤ)`. Again `a = b = 1`.

Both routes converge. Concretely, on the `12 × 12` positive grid (locked by
`test_grid_144_collapses_to_1`):

```
all 144 positive mixed closures B(a,b) are hyperbolic  (trace 2+ab ≥ 3 > 2)
the torsion-free filter ab = 1 leaves exactly ONE:  (a,b) = (1,1).
```

The 144 → 1 collapse is the quantitative content of the forcing.

The selected matrix (locked by `test_selected_matrix_is_A`) is

```
B(1,1) = L · R = A = [[2, 1], [1, 1]],
```

with characteristic polynomial `t² − 3t + 1` and eigenvalues `φ²`, `φ⁻²`
(locked by `test_eigenvalues_are_phi_squared_and_inverse`).

---

## 4. Statement of the theorem

> **Theorem (conditional uniqueness of the persistent sector).**
> Under axioms A1–A6, the first mixed persistent record-transfer sector is forced,
> up to the order convention of A7, to be
> `A = LR = [[2,1],[1,1]]` ∈ `SL(2,ℤ)`, with trace `3`, determinant `1`,
> characteristic polynomial `t² − 3t + 1`, and eigenvalues `φ²`, `φ⁻²`.
>
> **Corollary.** Given `A`, the proven core **P1–P16** follows as exact
> consequences (each independently locked by a test in `../tests/`): the Fibonacci
> / Ising / Zimm–Bragg coincidences (P2–P5), the Lorentzian phase-space form (P6),
> the gluing and torsion identities (P7–P8), the figure-eight selection (P9–P10),
> the `sl(2,ℝ)` closed form of `log A` (P11), the gluing-equation factorization
> (P12), isospectrality (P13), and the Möbius generating vector field and derived
> potential (P15–P16).

The result is therefore: **A1–A7 ⟹ A ⟹ {P1,…,P16}.** It is conditional — its
truth rests on accepting A1–A7 as the meaning of "minimal record-transfer system,"
not on deriving them. This is exactly the status of `C1`.

---

## 5. The order choice is load-bearing (A7), not cosmetic

A1–A6 cannot distinguish `LR` from `RL`. The two are `SL(2,ℤ)`-conjugate via the
record-swap `P = [[0,1],[1,0]]`, so they share trace, determinant, eigenvalues,
and translation length. They are the *same free homotopy / conjugacy class*.

But they are **not** the same as *based* objects, and the difference is visible
the moment `A` acts on the upper half-plane `H` as a Möbius transformation. Locked
by `test_order_choice_LR_vs_RL_conjugate_but_distinct_mobius_poly`:

| sector | Möbius fixed-point polynomial | roots |
|---|---|---|
| `A = LR` | `τ² − τ − 1` | `φ`, `−1/φ` |
| `RL` | `τ² + τ − 1` | `1/φ`, `−φ` |
| `K = LAL⁻¹` | `τ² − 3τ + 1` | `φ²`, `φ⁻²` |

The **golden polynomial `τ² − τ − 1`** — the one that generates the derived
potential `V` (P15/P16), the one shared with the Fibonacci charpoly, the fusion
rule, and the attractor (the "six faces") — is specifically the fixed-point
polynomial of `A = LR` *with this order*. Swap the order and the middle sign
flips (`τ² + τ − 1`); conjugate within the class and the whole polynomial moves
(`τ² − 3τ + 1`). The polynomial is a **based** invariant, not a class invariant.

Consequence for the theorem: the uniqueness is honestly *up to order*, and the
order choice A7 is the minimal inserted structure that selects the golden vacuum
`φ` over its mirror. This is not a weakness of the statement — it isolates, to a
single binary choice, where the specific number `φ` (rather than `−φ` or `φ²`)
enters.

---

## 6. What this does and does not establish

**Does:**
- Reduces "why `A = [[2,1],[1,1]]`?" to seven explicit, individually-motivated
  axioms, with the algebra (144 → 1, trace 3, the φ-spectrum) machine-checked.
- Pinpoints the single irreducible choice (order) and shows it is exactly what
  selects the golden polynomial — connecting the "based-invariant" fact to the
  uniqueness statement.
- Provides a self-contained, claim-bounded result in discrete dynamics with exact
  downstream consequences in topology (P8–P10) and number theory (P12, the
  discriminants, the "six faces").

**Does not:**
- Derive A1–A7 from anything weaker. (Attempts to derive even `L, R` from a
  count-substrate stalled — `frontier`/`paths` Phase C; the substrate, positivity,
  primitivity, and order remained inserted.) The result is conditional, and stays
  labeled `conditional` (C1) — not `proven`.
- Touch the field-theoretic lift. The promotion of `V` to a Lagrangian field
  theory (`frontier/B6`–`B9`) involves further inserted choices (kinetic term,
  dimension) and is **out of scope here by design.** This document stops at the
  exact, conditional, finite statement.

---

## 7. Relation to the claims ledger

This theorem is the precise statement and proof-of-the-algebra behind **C1**
("`L` and `R` are forced as the primitive record moves"), extended to force the
sector `A` itself. C1 remains **conditional**; `../tests/test_uniqueness_theorem.py`
upgrades its evidence from prose to a machine-checked computation. The corollary's
"⟹ P1–P16" half is already proven (those claims have their own tests); only the
axioms→A half is conditional.
