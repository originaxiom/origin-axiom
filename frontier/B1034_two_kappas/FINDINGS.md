# B1034 — **κ names two quantities**, and one of them is exported by the certified core

**Date:** 2026-08-11 · **Lane:** the code sweep (`WORKING_RULES` §0 — *"grep the **code**, not
claim lines"*). Gate 5 untouched; zero anchors; **no mathematics disturbed** — both κ's are correct
and both stay; only the shared symbol was undeclared.
**Files:** `verify.py` → `results.json` (17 checks, incl. an MB12 type control) · lock
`tests/test_b1034_two_kappas.py` (7).

---

## 1. THE COLLISION

| | **κ #1 — the flow coupling** | **κ #2 — the bridge equation** |
|---|---|---|
| definition | `2·log(φ²)/√5 ≈ 0.8608` | `κ = tr[a,b]` |
| **type** | a fixed transcendental **constant** | a **coordinate** on the character variety |
| can it equal 2? | **never** | **`κ = 2` ⟺ the cancellation completes ⟺ *nothing*** |
| exported by | **`src/origin_axiom/mobius.py::KAPPA`** | — |
| banked as | **`CLAIMS.md` P15, P16** | B309, B518 (restored B1010, extended B1027) |
| carried on | the **proven register** | `LAW_MAP`, `THE_FRAMEWORK`, `ORIENTATION` |

**Until this arc, neither surface mentioned the other.**

A third locus uses it as physics: `docs/SESSION3_SYNTHESIS.md` — *"Coupling: g = κ = 0.8608"*.

## 2. WHY THIS IS THE WORST OF THE PASS'S FOUR E1 COLLISIONS

The refresh has now found four undeclared-convention collisions — `θ` naming three distinct
objects (B1026), `B62 = 2 × P33` (B1026), B939's transposed shadow-map prose (B1024), and this
one. **This is the most expensive of the four, for three reasons:**

1. **It spans the two most authoritative surfaces** — `CLAIMS.md`, the register of what is
   *proven*, and `LAW_MAP`, the register of the laws. Not two working notes.
2. **It lives in `src/`** — the package whose own docstring says it contains *"only the results
   labelled `proven` in `CLAIMS.md`"*. A reader who imports `origin_axiom` meets this κ first.
3. **The shared symbol carries the founding sentence.** *"κ = 2 ⟺ nothing"* is the programme's
   one-line statement of itself. A reader who attaches it to `origin_axiom.KAPPA` has attached the
   founding sentence to a number that is **≈ 0.86 and can never be 2**.

## 3. THE DISCRIMINATOR — they differ in **type**, not merely in value

This is what makes the finding a defect rather than a quibble about two constants that happen to
share a letter:

> **κ #1 is a constant. κ #2 is a function with a locus.**
> A constant cannot have a set on which it equals 2. `κ = 2` is not a *value* κ #1 fails to take —
> it is a *statement κ #1 cannot make*.

**The control (MB12), run before reading the result:** had the core's `KAPPA` been symbolic in the
character-variety coordinates, the type test would not have fired. The criterion can come out the
other way, and is locked as such.

## 4. WHAT WAS REPAIRED, AND WHAT WAS DELIBERATELY NOT

**Repaired — the declaration, on both surfaces:**

- `src/origin_axiom/mobius.py` now carries a block above `KAPPA` naming both quantities, their
  types, and the fact that nothing relates them.
- `CLAIMS.md` carries the same disambiguation beside P15/P16.
- `LAW_MAP` carries the row.

**NOT done — the rename.** Renaming touches the **certified core** and the **two claims it locks**,
plus `SESSION3_SYNTHESIS` and two test files. A drafting seat that renames a symbol inside the
proven register has edited that register without an owner decision. **Registered as L159** with the
three options stated and none endorsed — and with the note that whichever is chosen, *the type test
is the check that must survive*.

## 5. WHAT ELSE THE CORE SWEEP FOUND — and did not

`src/origin_axiom/` is **376 lines across 7 modules**, and it was read whole. Everything else
checked out:

- **P1–P16 map cleanly onto modules and locks.** `algebra` (P1/P2/P6/P11/P13), `statistics`
  (P3/P4/P5), `gluing` (P7), `topology` (P8/P10/P12, data for P9), `mobius` (P15/P16),
  `constants` (the SnapPy anchors for P9).
- **P14 is intentionally unused** and says so in two places — a numbering reservation, not a gap.
- **`topology.py` carries its own self-audit in the docstring** — the shape-parameter note
  recording that an earlier audit pass wrongly flagged the golden factor as an artifact, and why
  the `z → 1/z` cross-ratio change makes both factorisations genuine. *That is the discipline
  working: the code carries the correction the prose could have lost.*
- **`SELECTION_FILTERS` lists five, P10 says "the trace-3 sieve + four further filters"** — 1 + 4 =
  5, consistent, with only the sieve computational and the rest carried as named literature facts,
  exactly as the docstring says.

---

**Verdict: PROVED.** 17 mechanical checks; the collision confirmed by type, not by value; both
surfaces now declare the other; the rename left to its owner.

> **The campaign asked for exactly this.** *"Grep the code, not claim lines"* is `WORKING_RULES`
> §0, and the corpus's most expensive error (B1007) was a code-vs-prose mismatch. This is the first
> pass in this refresh to read the certified core, and the core was carrying a name the prose had
> already spent on something else.
