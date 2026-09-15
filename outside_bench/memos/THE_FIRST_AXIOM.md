# Memo 224 — THE FIRST AXIOM: the theorem is real, it is on MAIN, it PRICES rather than discharges — and A3 is exactly the squaring

**Certificate:** `outside_bench/certificates/the_first_axiom.py` ·
**Output:** `outside_bench/outputs/the_first_axiom.txt` ·
**Seal:** `outside_bench/seals/THE_FIRST_AXIOM_PREREG.md`
(sha256 `f44223389d9f09861ed61cad19168e6f5149797f42652920c2f67f9f0b4da250`, committed before the
certificate was written)

**Occasion — the owner:** *"check new work from other branches, theres a theoreme about figure 8
being only with cusp that fixes first axiom."*

| cell | question | outcome |
|---|---|---|
| 1 | is the theorem on main, and does it say what it is cited for? | **A** |
| 2 | does it DISCHARGE the first axiom, or price it? | **A** |
| 3 | without A3, what do A1, A2, A4–A6 force over `GL(2,ℤ)`? | **A** |
| 4 | does the same code return the banked SL-level answer first? | **A** |

**C1–C4 all PASS.**

---

## 1. The theorem is real, and the owner's description of it is right

The first axiom is **`docs/UNIQUENESS_THEOREM.md` A1** — *"Two-record substrate. The state space is
`ℤ²` … **(Not one; not three.)**"* The theorem is **fork F9**, banked at **B1323 on `origin/main`,
2026-09-09** — four days old, and **not on a branch**. Quoted from the arc:

> *"does A1's "not one, not three" carry weight? | **ROBUST twice.**"*

**And the discriminator is exactly the cusp count the owner remembered:**

| substrate | carrier | bundle | **cusps** | field |
|---|---|---|---|---|
| **two records** `ℤ²` | `S₁,₁` | **m004** | **ONE** | **ℚ(√−3)** — the atom |
| three records `ℤ³` | `S₁,₂` | **m129, the Whitehead link** | **TWO** | ℚ(i) — the silver field |
| three records `ℤ³` | `T³` | — | **no hyperbolic structure at all** | — |

The toral half is a theorem, not a search: every `T³`-bundle over `S¹` has `χ = 0`, while a
finite-volume hyperbolic 4-manifold has `χ = 3·Vol/(4π²) > 0`. The arc's own summary sentence,
verified present:

> *"one record is nothing; two records are the golden ratio, the atom `ℚ(√−3)`, and an object that
> forgets its own handedness; three records are the plastic number on the torus, where there is no
> geometry at all, and the Whitehead link on the surface, where the handedness is remembered and the
> atom is gone."*

## 2. But it PRICES the first axiom — it does not discharge it

**CELL 2, from B1323's own fence, verified verbatim:**

> *"**Not claimed:** that the genesis is unconditional (UNIQUENESS §6 stands verbatim: **A1–A7 are
> not derived from anything weaker**…)"*

and its stated reach:

> *"that F9's ROBUST extends beyond **words of length 3** on the two punctured carriers (a longer
> enumeration or a proof is the next step if anyone wants the general statement)"*

> **So A1 remains an axiom.** What changed on 2026-09-09 is that it acquired a **computed price, and
> the price is the atom**: a third record buys the plastic number and loses `ℚ(√−3)`.
> **The axiom count stays 4 and memo 223's price stays 12.** F9 makes the axiom *defensible*, not
> *unnecessary* — and the two are different currencies, which is the same distinction the price
> ledger already turns on.

## 3. The branch sweep — and the one thing on a branch that WOULD move the count

All remote branches fetched and diffed against `origin/main`. Two moved today
(`<remote>/paper-verification-ufp0zn`, `audit/physical-bridge-2026-09-05`). The axiom-relevant find is
older and **unmerged**:

**`<remote>/physics-seat-evaluation-8dkbrl`, cell `T5_a6_audit` — "THE A6 RELABELING FEASIBILITY
AUDIT", verdict FEASIBLE.** It proposes re-typing the **orientation** axiom as the observer's
**closing #0**, on the finding that the class of *axiom-consumers before the object exists* is
**EMPTY** over a 1394-file sweep (629 files with hits, 4648 hit lines, bite control passed in both
directions). Under it:

> *"The axiom count at the entrance drops from three to two-plus-one-closing."*

**4 axioms → 3, and memo 223's price 12 → 11.** It is **proposed only** — *"no file outside this
cell directory was modified"* — and it has never landed on main.

**And it records exactly one missing datum:**

> *"the `GL(2,ℤ)`-level uniqueness statement — that **A1, A2, A4–A6 WITHOUT A3 force M up to the
> swap** (the matrix-level parent of the forcing, whose mapping torus is m000) — is **NOT computed
> anywhere in the record**. … Type: **a finite symbolic computation over `GL(2,ℤ)` monoid words**."*

## 4. CELL 3 — that computation, run. **A3 is the squaring.**

`A2` gives `GL(2,ℤ)`; `A3` is the restriction to `det = +1`, whose content the audit states as *"the
exclusion of the pure swap `S` from the primitive monoid"*. Dropping it means enumerating words over
`{L, R, S}`, keeping the mixed ones, and applying **A5** (torsion-free closure, `|det(B−I)| = 1`)
and **A6** (minimal hyperbolic complexity).

| | det | min `|trace|` | selected | dilatation |
|---|---|---|---|---|
| **with A3** (`{L,R}`, `det +1`) | +1 | **3** | `A = LR = [[2,1],[1,1]]` | `φ²` |
| **without A3** (`{L,R,S}`, `det ±1`) | **−1** | **1** | `M = L·S = [[1,1],[1,0]]` | **`φ`** |

* Words to length 4: `det −1, |trace| 1` — 12 words; `det +1, |trace| 3` — 14 words. The global
  minimum is `|trace| = 1`, at `det = −1`.
* Two matrices attain it; **up to the A7 swap (conjugation by `S`) they are ONE class.**
* `char(M) = t² − t − 1` (the golden ratio), `char(M²) = t² − 3t + 1` (`φ²`), and
  **`M² = LR = A` exactly.**

> ### **A3's entire matrix-level content is that it replaces the golden matrix by its square.**
> The paper says this in words — *"The squaring is not cosmetic: it **is** the orientation axiom.
> The un-squared matrix gives a non-orientable manifold of exactly half the volume"* — and **this is
> the `GL(2,ℤ)`-level forcing behind that sentence**, which the T5 audit correctly recorded as
> absent from the record. It is now computed: **one class, up to the one symmetry A7 already
> names.**

**CELL 4 first, deliberately:** the same enumerator, restricted to `det = +1`, returns
`A = LR, |trace| 3` — `UNIQUENESS_THEOREM` §3's banked answer — before the new case is trusted.
*(memo 154: run the corpus's own applicable check before believing a bespoke one.)*

## 5. What this does NOT do

* **It does not adopt the relabel and does not change any axiom count.** It supplies the datum the
  audit named; whether that licenses re-typing orientation as a closing is **main's call**.
* **It computes matrices, not manifolds.** That `M`'s mapping torus is the **Gieseking manifold
  m000**, and that m004 double-covers it at twice the volume, is **inherited from the record**
  (B749/F5; the paper's own sentence, verified present) and **labelled inherited** — no SnapPy
  identification is claimed here. **(C3.)**
* **It does not extend F9.** B1323's *"length 3"* reach is quoted, not widened.

## 6. Two things the sweep found that the record should not lose

* **`codex/seat-r001` holds a REFUTATION and an OPEN row against a stronger reading of "m004 is the
  only one":** **OA-C1103 REFUTED** — over the exactly-certified `ℚ(√−3)` cusped family (corrected
  size **112**), `H₁ = ℤ` does **not** uniquely isolate m004; `o10_150700` is one-cusped, in the
  family, with `H₁ = ℤ`. **OA-C1134 OPEN** — two one-cusped witnesses `o9_41001`, `o9_41009`
  *numerically* share m004's cusp shape `2√3 i`, and the comparison used a `1e-6` tolerance, so the
  row waits on an **exact peripheral certificate**.
  > **So "the figure-eight is the only one with a cusp" is TRUE in F9's sense (two records versus
  > three) and FALSE as an isolation claim inside the one-cusped `ℚ(√−3)` census.** The two are
  > different statements and the record holds both. **Reid's uniqueness** — m004 is the unique
  > arithmetic **knot** complement — is narrower still, and `knot in S³` is itself an input: the T5
  > audit lists *"Reid/knot-in-S³"* among the **orientation consumers**.
* **F9's own successor is registered:** `FRESH_EYES` **Q15 — *is there a carrier that keeps the atom
  and remembers the bit?*** Two records keep `ℚ(√−3)` and forget handedness; three remember
  handedness and lose the atom. **Nothing found so far does both.**

## 7. Operational

**C4 fired once and was right to.** The first version of the F9 needle used typographic quotes
`U+201C/U+201D` where the arc uses **straight** ones; the run **failed** rather than passing a
quotation this bench had mistyped. That is the control doing its job, and it is recorded here rather
than quietly repaired.

*Gate 5 untouched. Nothing promotes. No arc retracted.*
*Every number above comes from `outside_bench/outputs/the_first_axiom.txt`.*

---

# ADDENDUM 1 (2026-09-13) — **THE IDENTIFICATION IN §1 IS SUPERSEDED** (memo 225)

The owner named the theorem: **Jørgensen**. This memo's §1 identified the owner's *"theorem about
figure 8 being only with cusp"* as **fork F9 / B1323, on main**. **That identification is wrong.**
The theorem is **Jørgensen's inequality (1976) + Callahan (2009) Cor. 2.4** — *"the only orientable
hyperbolic 3-manifold with `J = 1` is the figure-eight complement"* — and it **is on a branch**
(`<remote>/paper-verification-ufp0zn`, arc **B1345**, 2026-09-12). The owner's *"new work from other
branches"* was exactly right; the sweep in §3 landed one theorem short.

**Everything else in this memo stands**: F9 is real, it is on main, it prices A1 rather than
discharging it, the branch sweep's A6-relabeling find is unchanged, and **CELL 3's computation is
untouched**.

**And CELL 3 gains a second, independent confirmation.** It found that dropping `A3` moves the
forced matrix from `A = LR` to `M = L·S`, `M² = A` — the un-squared golden matrix, whose mapping
torus is **m000**. Memo 225 finds that **`J = 1` holds for BOTH m000 and m004**, which is exactly why
Callahan's hypothesis reads *orientable*. **A `GL(2,ℤ)` monoid enumeration and a 1976 discreteness
bound select the same pair `{m000, m004}` and leave the same single choice — orientation.**

**What changes about the axioms:** Jørgensen + Callahan discharge **A1, A2, A4, A5, A6** at once
given orientability — far more than F9's pricing of A1 — and **leave orientation exactly where it
was**. *Nothing here changes memo 223's price of 12.*
