# B8119 — finishing the 3d theory: **complete as a definition**, and one row was never searched

**Date:** 2026-08-21 · **Seat:** cc3, audit · **Lane:** MATHEMATICS. **Gate 5 untouched.**
**Owner-directed:** *"finish it."*

> **SCOPE.** Re-audits B8099's eleven rows against the corpus and **recomputes the state integral's
> saddle independently**. It does **not** re-derive `T[4₁]` or the state integral — both are read
> from B262 and B787, and B787's cell was **re-run in-sandbox**. **Claims no novelty.**

---

## ⚠ What is NOT finished — stated first, not last

1. **the cusp's CONTINUOUS spectrum -- B739/B8101's phi(s) is in hand; the spin-2 cusped test function is NOT**
2. **the step from Ray-Singer analytic torsion to the graviton determinant -- B8112 declined it**
3. **the n = 2 factor's convergence -- it sits AT the abscissa Re(s) = 2; conditionally convergent at best (B8113)**

**None of these was ever on B8099's checklist.** They are a rung **this seat added** (B8100–B8113).
**The checklist measures the theory's DEFINITION. These are its QUANTUM EVALUATION — and that is
where an actual new result would live.**

## The eleven rows, re-audited

| row | B8099 | now | why |
|---|---|---|---|
| classical solution | `PRESENT` | **PRESENT** | 2 regular ideal tetrahedra, verified (B8099) |
| cosmological constant | `PRESENT` | **PRESENT** | Lambda = -1 exactly (B259) |
| the action | `PRESENT` | **PRESENT** | forced (B1012) |
| boundary central charge | `PRESENT` | **PRESENT** | c = 6 sigma, derived twice (B1012; Brown-Henneaux) |
| complex CS action | `PRESENT` | **PRESENT** | purely real, CS = 0 (B8099) |
| the 3d-3d theory T[4_1] | `PRESENT` | **PRESENT** | U(1) + 2 chirals (B262) |
| state integral | `PARTIAL` | **PRESENT** | B787/D5: closed residue evaluation at b=1, Phi_b validated. B8099 NEVER SEARCHED B787 |
| matter spectrum | `AMBIGUOUS` | **RESOLVED** | B8118: it is T[4_1]'s 2 chirals; E6/27 is ARITHMETIC, not matter |
| E6 as a DYNAMICAL gauge | `MISSING` | **CLOSED NEGATIVE** | B8118 closes B262's wall #2 |
| E6 state integral | `MISSING` | **DISSOLVED** | no dynamical E6 => no such object for this manifold |
| the 4d lift | `MISSING` | **OUT OF SCOPE** | owner elected 'finish rather than lift'; B8099 proved 3d-3d cannot reach 4d |

**No row is left `PARTIAL`, `AMBIGUOUS` or `MISSING`.**

## ⚠ The row that was never searched — and it is mine

**B8099 marked the state integral `PARTIAL` — *"B262/B269 rungs, not a closed evaluation"* — and
mentions `B787` ZERO times.**

**B787's D5 cell computes the figure-eight state integral** in the Andersen–Kashaev / Mariño–Rella
normalisation, with **Faddeev's quantum dilogarithm validated** (functional-equation residual
`1.6×10⁻³⁰`), at the **self-dual point `b = 1` where the exact residue evaluation collapses to a
SINGLE term**, and its saddle matches `Vol(4₁)` to `3.9×10⁻³¹`. **That is a closed evaluation.**

> **`WORKING_RULES` §0 again — *"we lack X" is a hypothesis requiring a search* — and the seat that
> broke it is this one, in its own audit.**

## The theory is parameter-free in a strong sense

Recomputed here independently of B787: the saddle is the regular ideal tetrahedron `z = e^{iπ/3}`,
and

```
2 Im Li₂(e^{iπ/3}) = 2.029883212819307250042405     (= Vol(4₁), agreeing with SnapPy to 3.0×10⁻¹⁶)
                    = (3√3 / 2) · L(χ₋₃, 2)
```

**The classical action's entire content is an L-value, not a fitted constant. Nothing in the theory
is tuned.**

## Novelty is explicitly disclaimed

**DGG built `T[4₁]`. Andersen–Kashaev built the state integral. 2+1 gravity with `Λ < 0` is
standard.** What the corpus did is **assemble and verify** the combination for this manifold and
**remove an ambiguity of its own making**. **This seat claims no new theory.**

## A process failure caught by an exit code, recorded

The first run of this arc **failed a control and I nearly banked it**: I had suppressed `stderr` and
read the output through `tail`, which cut Section 1 from view. **The `SystemExit` was invisible.**

The failing control was itself a **false negative**: `str()` on a `SnapPy.Number` truncates to its
accuracy setting — `"2.0298832128"`, 11 digits — so a correct computation compared against a
crippled reference missed a `10⁻¹³` threshold by `1.9×10⁻¹¹`. **`float()` gives the full double and
the check passes at `3.0×10⁻¹⁶`.**

> **Two lessons, both worth a standing rule:** a **precision-truncating serialisation manufactures a
> negative** rather than hiding one; and **suppressing `stderr` while reading `stdout` through
> `tail` can hide a control failure completely.** Flagged to cc as possibly deserving an
> `ERROR_LEDGER` class — **not filed unilaterally**, since I cannot see the whole taxonomy from
> here.

## Artifacts

`closure.py` · `results.json` · `tests/test_b8119_3d_closure.py`
