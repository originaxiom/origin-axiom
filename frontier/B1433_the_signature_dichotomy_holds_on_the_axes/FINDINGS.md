# B1433 — THE SIGNATURE DICHOTOMY HOLDS ON THE AXES AND ON THE TWO PURE PLANES, NOT ON THE TORUS: every direction that mixes a split charge with a compact one has 48 generic-complex eigenvalues, exactly

cc, 2026-10-01. Chain link C29 reads "zero generic-complex on C". An outside audit of the structure paper (August
2026, received in a seat checkpoint and read in full on 2026-09-30) gave a counter-example, x₈ + x₁₄. Recomputed here
on main's own E₆ frame (B854, executed read-only), exactly.
**Verdict: PROVED. C29's last clause is false as written and is corrected in place; the dichotomy of the four axes
stands.**

## Computed (`verification/mixed_directions.py`; record `mixed_directions.json`)

Characteristic polynomial of ad(x) on the 78-dimensional adjoint over ℚ, factored; real roots of each factor counted by
Sturm; purely imaginary roots counted by Sturm on g, where f(t) = g(t²).

| direction | zero | real | imaginary | generic complex |
|---|---|---|---|---|
| x₈, x₁₆ | 30 | 48 | 0 | 0 |
| x₁₄, x₂₂ | 12 | 0 | 66 | 0 |
| x₈ + x₁₆ | 30 | 48 | 0 | 0 |
| x₁₄ + x₂₂ | 12 | 0 | 66 | 0 |
| x₈ + x₁₄, x₈ + x₂₂, x₁₄ + x₁₆, x₁₆ + x₂₂ | 12 | 0 | 18 | **48** |
| x₈ + 2x₁₄ | 12 | 0 | 18 | **48** |
| 2x₈ + 3x₁₄ + 5x₁₆ + 7x₂₂ | 12 | 0 | 18 | **48** |

The first two rows are B898's census, re-derived. The mixed characteristic polynomial is t¹² · f₆³ · f₁₂ · f₁₂′³: the
sextic has six purely imaginary roots, the two degree-12 factors have no real and no purely imaginary root.

## Why, in one line

The four charges commute, so they have joint eigenvectors. On a joint eigenvector a split charge contributes a real
number and a compact charge an imaginary one. Of the 78 joint weights, 12 are zero, 18 are purely compact, and 48 have
both parts non-zero; a combination with a non-zero split and a non-zero compact coefficient therefore has 48
eigenvalues that are neither real nor imaginary. The counts add up on the axes: 30 = 12 + 18 and 66 = 18 + 48.

## Joint centralisers (`verification/joint_centralizers.py`)

z(x₈) = z(x₁₆) = z(x₈, x₁₆) has dimension 30; every other subset of the four charges, and the whole torus, has joint
centraliser of dimension 12. No subset of the four has a centraliser of dimension 14.

## What changes

- **C29** (THEOREM_LEDGER), **T-SIGDICH** (THEOREM_REGISTRY), the LAW_MAP row and the structure-paper skeleton: the
  clause "zero generic-complex on C" becomes "none on the four axes or on the split and compact planes; 48 on every
  direction mixing the two". B898 carries an addendum.
- **The lock.** `tests/test_b898_census.py::test_no_generic_complex_anywhere_on_C` tested the four axes under a name
  that said "anywhere". It is renamed for what it tests; the mixed directions are locked in `tests/test_b1433_*`.
- **Not affected:** the four-column concordance, the type-twin statement, the paper (its wording was already
  axis-restricted, `scripts/checks/paper_chain_table.py`).

## The error class

B898's script classified the four axes and its prose quantified over the torus. A green test under a universal name
was read as the universal statement. ERROR_LEDGER: a claim's quantifier exceeding its computation (E54's twin on the
positive side).

## Registered

- The chain's C25 says a second measurement lands on su(3) ⊕ su(2) ⊕ u(1)³, dimension 14. No joint centraliser of the
  four charges has dimension 14, and the audit reports 14 only on two hyperplanes of the torus. Which elements C25
  quantifies over is to be read from B892 and stated in the link. Lead registered.
