# P5 AT STEP 1 — the menu IS incomplete, and the winner is UNAFFECTED

cc3, 2026-08-10. Gate 5-Q. Structure only.

## Why P5 became the whole question

The content ledger grades three rows **DERIVED-GIVEN-P5** — the gauge algebra,
charge quantisation (via B862), and the termination theorem. And the confluence
result retired the ranking rule, so **P5 is the cascade's only remaining
external import.** B861 states the risk precisely:

> *"**Menu completeness (P5) is still the imported spine.** A chain missing from
> the classification **breaks uniqueness silently.** This is now the cascade's
> single external dependency."*

## Why it is decidable, not a survey

The cascade's walls are **centralizers of semisimple elements** (B964: the
construction *is* an adjoint Higgs mechanism, and the unbroken group is the
centralizer). A centralizer of a semisimple element is always a **full-rank
regular** subalgebra — a Levi, or Borel–de Siebenthal. That set is finite and
obtained by node-deletion from the **extended Dynkin diagram**. So the question
is an enumeration.

Everything below is computed from the Cartan data; **no table of subalgebras is
consulted.**

## The enumeration at step 1

Deleting prime-mark nodes from Ẽ₆ (Borel–de Siebenthal) and single nodes from E₆
(Levi) gives **six** maximal-rank regular subalgebras:

| subalgebra | dim | in B861's menu? |
|---|---|---|
| **SO(10)×U(1)** = D₅+U(1) | **46** | yes — **the winner** |
| SU(6)×SU(2) = A₅+A₁ | 38 | yes |
| **SU(6)×U(1)** = A₅+U(1) | **36** | **NO** |
| Sp(8) = C₄ *(an S-subalgebra, not regular)* | 36 | yes |
| **SU(2)×SU(5)×U(1)** = A₁+A₄+U(1) | **28** | **NO** |
| SU(3)³ = A₂+A₂+A₂ | 24 | yes |
| **SU(2)×SU(3)²×U(1)** = A₁+A₂+A₂+U(1) | **20** | **NO** |

**B861's step-1 menu is incomplete. Three regular options are absent.**

## But the failure mode does not fire

B861's stated risk is that *a missing chain breaks uniqueness silently.* Here it
does not, and the reason is dimensional:

> **All three absent options have dim 36, 28, 20 — every one strictly below the
> winner's 46.**

And that is not a coincidence to be checked case by case. `D₅+U(1)` is **the
maximal-dimension maximal-rank regular subalgebra of E₆**, which the enumeration
establishes outright. **Under the rule "maximal residual symmetry", the winner
is determined by the enumeration itself, not by the menu.** A menu that omits
strictly smaller options cannot change a maximum.

**So P5 at step 1 is discharged for the winner** — not by proving the menu
complete, but by proving the omissions immaterial, which is the weaker and
sufficient statement.

## What is discharged and what is not

**Discharged:** step 1's winner does not depend on menu completeness. Rows 1, 3
and 11 of the content ledger inherit that for their first step.

**NOT discharged:**

- **Steps 2 and 3.** The same enumeration must be run on D₅ and A₄. The script
  does both; the analysis here covers step 1 only, and **I will not claim the
  chain until all three are done.**
- **S-subalgebras.** The enumeration covers *regular* subalgebras, which is what
  centralizers give. B861's menu itself includes one S-subalgebra (Sp(8)), so
  the menu is not purely centralizer-derived, and **the S-subalgebra side is not
  enumerated here.** B932's T2 argues centralizers are Levi-type, which would
  make this exhaustive — but that is a citation, not a computation I ran.
- **Registerability.** The three absent options were never tested for it. They
  do not need to be for the winner, but a complete menu would list them.

## The honest summary

**The menu is incomplete and it does not matter at step 1.** B861 was right to
flag P5 and right to call it the spine; what nobody had done is check whether
the spine bears weight. At step 1 it does, for a reason stronger than the
original argument: the winner is the dimensional maximum over the *complete*
enumeration, so no omission could have displaced it.

Reproduce: `python3 p5.py` (enumerates all three steps from the Cartan data).
