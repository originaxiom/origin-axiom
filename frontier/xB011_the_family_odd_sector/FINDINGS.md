# xB011 — the owner's catch was right: B425's "√−3 cancels" is an AMPHICHIRALITY ARTEFACT, and xB009 tested the one object where the question is degenerate

**Status: banked (frontier, `sep16-branch`). Verdict PROVED.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE any cell ran** — sha256
`642ccf4ec840523d57684102d72548b1d5da3836fcac13859ae59ccf7d2b2484`, commit `4b16b19`.
Gate 5 untouched. Lock: `verification/reproduce.sh`, five cells.

## The catch

> *"have you checked the odd sector only for m004 or for the whole family of objects?"*

**m004 only.** xB009's O2 ran B425's Fox calculus on the figure-eight relator **alone**; O3/O4
compared **two** manifolds. Its headline — *"THE ODD SECTOR IS NOT THE DOOR"* — claimed the
**sector** from **one object**: the **E70** shape.

## The result against the sealed criteria

| cell | outcome |
|---|---|
| **F1** | **PASS** — a generic instrument, validated against B425's **exact** values at even **and** odd n, ratio ±1 |
| **F2** | the family table: **16 usable of 21** (5 excluded for `H₁` rank 2 — two cusps — **reported, not dropped**) |
| **F3** | **chiral ⟹ `√−3` SURVIVES, 8/8, no exception.** The converse is **FALSE** |
| **F4** | **PASS** — realness is **stable under lift change**, so not an artefact of the two-lift ℤ/2 |
| **F5** | **PASS** — and it **closes the hope**: `6₃` is also amphichiral and also real at every n |

## Three defects of this seat's own, caught by F1's controls before any verdict

1. **The un-normalised Fox determinant is not an invariant** — B425's own guard section says so.
   Wada normalisation added.
2. **The abelianisation is not the total exponent sum.** SnapPy's m004 relator `aaabABBAb` has
   exponent vector `(a:1, b:0)`, so `α` must send **a↦0, b↦1**. Computed from the relator kernel now.
3. **SnapPy's `SL2C` lift sends the m004 relator to `−I`, not `+I`** — so `Sym^odd ∘ ρ` **is not a
   representation** for that lift and every odd-n number from it is **void**. The lift is repaired
   over `𝔽₂`. This is xB009's O1 ℤ/2 biting in practice, and it is why the first numerical pass
   appeared to contradict B425. **B425 was right; the instrument was wrong.**

## What is actually true

**F3 — one way, and only one way.**

| | at n = 1…4 |
|---|---|
| **chiral (8)** | `√−3` **survives**, all of them, **no exception** |
| **amphichiral (8)** | real at **all** n: `m004` · real at **even only**: `m003`, `s955` · **complex everywhere**: `m206`, `m207`, `s957`, `s960`, `s961` |

> **CHIRAL ⟹ `√−3` SURVIVES.** The converse is **false**: amphichirality does **not** imply
> cancellation.

**So B425's *"`√−3` cancels in every determinant"* is an AMPHICHIRALITY ARTEFACT, not a general
fact** — and **xB009's headline was the over-reach the owner suspected: correct for m004, false as
a statement about the sector.** On chiral members the Eisenstein content survives, **at even n as
well as odd** — so the odd/even axis xB009 was testing was never the operative one. **Chirality is.**

## And the hope this arc raised, closed by its own control

F2 showed m004 as the **unique** member real at every n — 1 of 16 — which looked like a **second
selector**, arithmetic where xB007's only one (`H₁`) is homological. **F5 kills it.** m004 is the
only `H₁ = ℤ` member of its class, so realness might merely track knot-ness; testing other knot
complements gives **`6₃` amphichiral and real at every n, exactly like m004**, while every chiral
knot tested is complex.

> **Realness tracks AMPHICHIRALITY ∧ KNOT-NESS — both already in the record. m004 is not unique,
> and this is NOT a new selector.** xB007's finding that `H₁` is the only selector **stands**.

**A first draft of F3 printed *"chirality controls it"*** on the chiral column alone. The table does
not support that — five amphichiral members are complex everywhere — and the claim is narrowed to
the direction the data shows.

## Corrections this arc lands elsewhere (F4 of the seal)

* **B425** — its *"√−3 cancels in every determinant"* is **scoped**: true at `ρ_geo` of m004,
  **because m004 is amphichiral**, and false for chiral manifolds. B425's computations are **not**
  disputed; this arc **reproduced them exactly**, including at odd n, which B425 never ran.
* **xB009** — its headline generalised one object to a sector. **The m004 result stands** (confirmed
  here independently); **the sector claim does not.**

## Scope and unmeasured base rate

Census cutoff 6 tetrahedra, 21 members, **16 usable**; the class is infinite and this is a finite
sample. **The base rate of "chiral ⟹ survives" outside this class is measured only on the 10 knot
complements of F5** — it is not established as a general theorem here, only as a pattern without
exception in 16 + 10 cases. `creates_law` false; nothing to `CLAIMS.md`, F2 or Gate 5.

**Provenance.** `verification/family_odd.py` (F1–F5) → `reproduce.sh`. Cross-refs B425 (scoped
here, reproduced exactly), xB009 (headline corrected), xB007 (the population, the amphichirality
column, and the `H₁`-only-selector finding this arc confirms), B1136, E70.
