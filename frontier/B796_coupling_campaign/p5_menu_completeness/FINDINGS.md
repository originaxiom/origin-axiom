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

---

# STEPS 2 AND 3 — and step 2 has a live problem

## Step 3: the menu is COMPLETE

A₄ = su(5) has all marks 1, so **no** Borel–de Siebenthal subalgebras. The Levis
are exactly two:

| | dim | in menu? |
|---|---|---|
| SU(4)×U(1) = A₃+U(1) | 16 | yes |
| **the SM** = A₁+A₂+U(1) | 12 | yes |

**Enumerated: 2. Banked: 2. Step 3's menu is complete** — and the winner is the
*smaller* option, because SU(4)×U(1) fails registerability. **At step 3 the
registerability filter is doing the work, not the ranking.**

## Step 2: the menu is INCOMPLETE, and the omission is MATERIAL

| | dim | in menu? |
|---|---|---|
| **SO(8)×U(1)** = D₄+U(1) | **29** | **NO — ABSENT** |
| SU(5)×U(1) = A₄+U(1) | 25 | yes — **the banked winner** |
| Pati–Salam = A₁+A₁+A₃ | 21 | yes |
| SU(2)×SU(4)×U(1) = A₁+A₃+U(1) | 19 | NO |
| SU(2)²×SU(3)×U(1) | 15 | NO |

> **SO(8)×U(1) has dimension 29. The banked winner has 25. The larger option is
> absent from the menu.**

And it is a legitimate wall for this construction: `so(10) ⊃ so(8) ⊕ so(2)` is
the centralizer of a generic element of that so(2), so it is exactly the kind of
subalgebra B964's adjoint-Higgs reading produces.

**This is B861's own stated failure mode, live:** *"A chain missing from the
classification breaks uniqueness silently."*

## What decides it — and it is not run

Under *"maximal residual symmetry among **registerable** options"*, SO(8)×U(1)
displaces SU(5)×U(1) **iff it is registerable.** So the cascade's step 2 turns
entirely on one untested question:

> **Does the 16 stay chiral under SO(10) → SO(8)×U(1)?**

The decomposition is `16 → 8_s(+1) ⊕ 8_c(−1)`. Both 8_s and 8_c are **real**
representations of SO(8), so the chirality question is whether the U(1) grading
alone makes the pair complex — which it may, since the conjugate is
`8_s(−1) ⊕ 8_c(+1)` and the two are exchanged only by an outer automorphism
(SO(8) triality), not by an inner one.

**I have not computed this and I am not asserting either answer.** Two outcomes:

- **registerable** → SO(8)×U(1) wins step 2, and the banked chain
  E₆ → SO(10)×U(1) → SU(5)×U(1) → SM **is not the cascade's output.** That would
  be a serious correction to B861, and downstream to B862's ℤ₆, B863's
  termination, and content-ledger rows 1, 3 and 11.
- **not registerable** → the omission is immaterial like step 1's, and **P5 is
  discharged across the whole chain** by enumeration.

## Net, stated carefully

| step | menu | verdict |
|---|---|---|
| 1 | **incomplete** (3 absent) | **discharged** — all omissions strictly smaller than the winner |
| 2 | **incomplete** (3 absent) | **OPEN — one omission is LARGER than the winner** |
| 3 | **complete** | discharged |

**This is what P5 was for.** B861 called menu completeness the spine and the
single external dependency; the spine has now been tested at all three steps,
and it bears weight at two of them. **The third is one bounded computation from
being decided in either direction**, and that computation — the chirality of
`16 → 8_s(+1) ⊕ 8_c(−1)` under SO(8)×U(1) — is the highest-value item in the
content campaign.

**Not claimed:** that the cascade is wrong. B861 may well have excluded
SO(8)×U(1) for a reason recorded elsewhere, and I did not find such a reason in
its FINDINGS. **The claim is that the menu does not list it and the arc does not
say why**, which under B861's own framing is exactly the silent break it warned
about.

---

# WITHDRAWN — the step-2 omission is IMMATERIAL. My claim was wrong, and the error was mine.

The owner asked to sweep before running the chirality computation, in case P5
was being misformulated. **It was.** The check took minutes and the claim above
would have been a serious false alarm against B861.

## My error, exactly

I ranked the step-2 candidates **by dimension** and concluded SO(8)×U(1) at 29
displaces SU(5)×U(1) at 25. But B861's rule is not "maximal dimension". It is:

> **"Maximal residual symmetry among REGISTERABLE options"**

**Registerability is a filter applied FIRST; the ranking only orders what
survives it.** I compared dimensions across the filter instead of within it.

## And SO(8)×U(1) fails the filter

B860's criterion, as B861 states it: the generation *"remains chiral as a
multiset **after the θ-odd abelian factors are stripped**."* Applying it:

| candidate | 16 → | after stripping U(1) | verdict |
|---|---|---|---|
| **SU(5)×U(1)** | 10(+1) + 5̄(−3) + 1(+5) | {**10**, **5̄**, 1} — two complex | **chiral ✓** |
| **SO(8)×U(1)** | 8_s(+1) + 8_c(−1) | {8_s, 8_c} — **both real** | **vector-like ✗** |
| Pati–Salam | (4,2,1) + (4̄,1,2) | both complex | chiral ✓ |

**SO(8)'s three 8-dimensional representations are all self-conjugate.** So once
the abelian factor is stripped, SO(8)×U(1)'s generation is vector-like and it is
**not registerable** — the identical failure mode B861 already records twice:
Sp(8) at step 1 (*"the 27 restricts to the traceless Λ²(8) of C₄, self-dual — no
chiral matter at all"*) and SU(4)×U(1) at step 3 (*"whose generation collapses to
vector-like — B860"*).

**The omission cannot change the winner.** It would have been filtered before
ranking.

## Corrected verdict — P5 is discharged at all three steps

| step | menu | omissions | verdict |
|---|---|---|---|
| 1 | incomplete (3 absent) | all strictly **smaller** than the winner | **discharged** |
| 2 | incomplete (1 larger, 2 smaller) | the larger one **fails registerability** | **discharged** |
| 3 | **complete** | — | **discharged** |

> **P5 — menu completeness, the cascade's single external dependency — is
> discharged across the whole chain.** Not by proving the menus complete (two of
> three are not), but by proving every omission immaterial: smaller than the
> winner, or filtered out before ranking.

Together with the confluence result retiring the ranking rule, **the cascade's
imports are now discharged.** Content-ledger rows 1, 3 and 11 lose their
`GIVEN-P5` qualifier at the level of the enumeration.

## What remains, honestly

- **Regular subalgebras only.** The enumeration covers centralizer-type
  (Levi/Borel–de Siebenthal) walls. B932's T2 argues that is exhaustive for this
  construction; I cite it, I did not re-prove it. B861's menu contains Sp(8), an
  S-subalgebra, so the menu was never purely centralizer-derived.
- **A documentation gap survives.** B861's menu does not list SO(8)×U(1) and does
  not say why. It is correctly excluded — but by a filter the arc applies
  elsewhere and does not apply here on the page. **One line would close it**, and
  the arc should carry it, because the next person to enumerate will find the
  same gap and may not check the filter before publishing, as I did not.

## The process point, which is the durable part

**I found a real gap and drew a wrong conclusion from it in the same breath.**
The gap (menu incompleteness) is genuine and worth recording. The conclusion
(material, breaks uniqueness) was wrong because I applied the programme's rule
without its first clause.

**The owner's instruction to sweep before computing is what caught it.** Had I
gone straight to the chirality computation as I proposed, I would have computed
the right thing for the wrong reason and reported a break that does not exist.
