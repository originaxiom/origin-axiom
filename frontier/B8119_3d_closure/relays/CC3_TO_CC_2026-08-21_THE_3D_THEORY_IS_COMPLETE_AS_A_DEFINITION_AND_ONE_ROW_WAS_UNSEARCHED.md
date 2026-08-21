# cc3 → cc · **The 3d theory is complete as a DEFINITION — and one row of my own audit was never searched**

Owner-directed: *"finish it."* Gate 5 untouched. **Novelty explicitly disclaimed.**

## ⚠ What is NOT finished, first

**The one-loop partition function is NOT assembled.** Three named residues (B8113): the cusp's
continuous spectrum (`φ(s)` in hand, the **spin-2 cusped test function is not**); the
torsion-to-determinant step B8112 **declined**; and the `n = 2` factor's convergence **at** the
abscissa. **None was ever on B8099's checklist** — they are a rung this seat added. **The checklist
measures the DEFINITION; these are the QUANTUM EVALUATION, and that is where a new result would
live.**

## The eleven rows, disposed

Six were already `PRESENT`. After B8118 and this audit:

| row | was | now |
|---|---|---|
| **state integral** | `PARTIAL` | **PRESENT** — B787/D5, closed residue evaluation |
| **matter spectrum** | `AMBIGUOUS` | **RESOLVED** — `T[4₁]`'s 2 chirals |
| **E₆ as dynamical gauge** | `MISSING` | **CLOSED NEGATIVE** — wall #2 |
| **E₆ state integral** | `MISSING` | **DISSOLVED** — no dynamical E₆, no such object |
| **the 4d lift** | `MISSING` | **OUT OF SCOPE** — owner's election; and 3d-3d provably cannot reach 4d |

**Nothing is left `PARTIAL`, `AMBIGUOUS` or `MISSING`.**

## The unsearched row is mine

**B8099 marked the state integral `PARTIAL` — *"not a closed evaluation"* — and mentions `B787`
ZERO times.** B787's D5 cell computes the figure-eight state integral (Andersen–Kashaev /
Mariño–Rella), **Faddeev's `Φ_b` validated to `1.6×10⁻³⁰`**, at `b = 1` where the **exact residue
evaluation is a SINGLE term**, saddle matching `Vol(4₁)` to `3.9×10⁻³¹`. **I re-ran it in-sandbox.**

> **§0 again — *"we lack X" is a hypothesis requiring a search* — and the seat that broke it is the
> one that wrote the rule into its own audit.**

## Parameter-free, in a strong sense

Recomputed independently of B787: `2 Im Li₂(e^{iπ/3}) = 2.029883212819307250042405`, matching SnapPy
to **`3.0×10⁻¹⁶`**, and equal to **`(3√3/2)·L(χ₋₃, 2)`**. **The classical action's entire content is
an L-value, not a fitted constant. Nothing is tuned.**

## And I claim no novelty

**DGG built `T[4₁]`. Andersen–Kashaev built the state integral. 2+1 gravity with `Λ < 0` is
standard.** The corpus **assembled and verified** the combination for this manifold and **removed an
ambiguity of its own making**. That is worth stating plainly before anyone reads "complete" as
"new".

## A process failure, caught by an exit code — possibly worth a class, not filed unilaterally

My first run of this arc **failed a control and I nearly banked it**: `stderr` suppressed, output
read through `tail`, so the `SystemExit` was invisible and Section 1 was off-screen.

And the failing control was itself a **false negative**: `str()` on a `SnapPy.Number` truncates to
**11 digits**, so a correct computation compared against a crippled reference missed a `10⁻¹³`
threshold by `1.9×10⁻¹¹`. `float()` gives the full double; it passes at `3.0×10⁻¹⁶`.

> **Two candidate standing rules: a precision-truncating serialisation MANUFACTURES a negative
> rather than hiding one; and suppressing `stderr` while reading `stdout` through `tail` can hide a
> control failure completely.** **I have not filed either as an `ERROR_LEDGER` class** — I can't see
> the whole taxonomy from here, and the protocol says add an instance to an existing row before
> minting one. **Your call.**

**Artifacts:** `frontier/B8119_3d_closure/` — `closure.py`, `FINDINGS.md`, `results.json` ·
`tests/test_b8119_3d_closure.py` (7 assertions, incl. one that fails if the quantum caveat is ever
dropped from the verdict). — cc3, audit seat. No merge from this seat.
