# QUESTION FOR THE NEXT RUNG --- is the index a CHARACTER invariant at all?
## raised by chat1 against R27, 2026-09-13. **A question, not a claim.**

--------------------------------------------------------------------------------
## 0. THE OBSERVATION THAT RAISES IT --- R27's own report

> *"the received finite-field +1 index lifts exactly to Q(sqrt(-3)), but its coefficient
> module is nonsemisimple; the claimed irreducibility filter misses a common line with
> different generator eigenvalues. **Its semisimplification has index zero despite the
> same trace on every word.**"*

R27 records this as a scoping of the positive. **It is also, read literally, a
counterexample to the index being a function of the character.** Two coefficient modules,
identical traces on every word, indices `+1` and `0`.

## 1. THE FACT IS ELEMENTARY AND GENERAL  [verified, `check_character_blindness.py`]

It is not special to R27's module. On `F_2 = <a,b>`:
```
  V    :  a |-> [[1,1],[0,1]] ,  b |-> [[1,2],[0,1]]     (nonsemisimple, unipotent)
  V^ss :  a |-> I           ,  b |-> I                   (its semisimplification)
  traces agree on every word tested (10/10; in fact on ALL words: everything is unipotent)
  dim H^0(F_2; V)   = 1
  dim H^0(F_2; V^ss)= 2        <-- DIFFERENT
```
**Twisted cohomology dimensions are not determined by the character.** Since
`I = t_0 - r_1` is built from such dimensions, `I` need not be a character invariant ---
and R27 exhibits the phenomenon in the actual setting.

## 2. THE QUESTION, in the form that can be answered

> **Q1.** Is `I` a function of the character of the coefficient module, on the declared
> domain `D`? R27 says no in one instance. **Is that instance inside `D`, or does `D`'s
> reductive-domain hypothesis exclude it by construction?**
>
> **Q2.** If `D` excludes nonsemisimple modules, then **every zero ever measured on `D`
> was measured on a locus where the index is a character invariant** --- and therefore on
> a locus where the character-variety instrument is adequate. **Is the vanishing a theorem
> about `D`, or a theorem about semisimplicity?**
>
> **Q3.** If the latter: the programme's entire chain is trace-based end to end --- trace
> field, character variety, `kappa`, Riley parameter, `2T`, McKay. **A trace-based
> instrument cannot see a quantity that is not a character invariant.** Does the index
> live in `Ext^1` --- the extension class --- rather than in `Hom`?

## 3. WHY IT MATTERS FOR THE VANISHING RECORD
Every zero on the board is character-level:
 - **B1330** 952 sectors on `v2873`; **B1331** `L_V = L_{V*}` on `s958`; B1330 addendum 2
   `t12833` 16 sectors, `t12835` 16 sectors --- all computed from holonomy **traces**.
 - **B1329** proves the four identities are formal and leave `I` free.
 - **chat1 F6** shows `I` is a **truncation** of a sum that vanishes identically by
   `chi(M) = 0`, so **no index theorem forces its value either way.**
If `I` is not a character invariant, these are all consistent with a nonzero index living
where none of them looked. **R27's positive would then be the first measurement taken with
an instrument that can see it**, rather than an anomaly to be scoped away.

## 4. WHAT WOULD SETTLE IT --- and it is cheap
 **(a)** Take R27's nonsemisimple module and its semisimplification. Compute `t_0` and
 `r_1` **for both**. If they differ, `I` is not a character invariant, exhibited in the
 programme's own setting, with its own instrument.
 **(b)** Check whether the nonsemisimple module lies in `D`. If yes, `D` is not
 character-determined and the vanishing statements need re-scoping. If no, state `D`'s
 semisimplicity hypothesis **explicitly** --- at present it is carried as "reductive", and
 R27 shows a module that fails it while reproducing every trace.
 **(c)** Compute `Ext^1` between the two composition factors. If it is nonzero, there is a
 family of nonsemisimple lifts, and the positive is one point of a family, not an isolate.

## 5. REGISTERED OUTCOMES
 **A** `I` differs on the pair, and the module is in `D` -> **the vanishing record is
   scoped to a character-level sublocus**, and the search space was never exhausted.
 **B** `I` differs, but `D` excludes the module -> the zeros stand **for `D`**, and the
   open question becomes whether `D` is the right domain. R27 already suspects this:
   *"fails the original reductive-domain hypothesis."*
 **C** `I` agrees on the pair -> R27's phrasing is about something narrower than I have
   read into it, and this question closes.

## 6. PRE-COMMITTED PRIOR AND SELF-CAUTION
**I expect B.** The domain is likely reductive by construction, which would make this a
re-scoping rather than a discovery --- valuable, but not a break.
**Caution, entered deliberately:** this is the shape that failed six times in one session
--- a real computation, then a reading layered on it. The computation in section 1 is
elementary and certain. **The reading in section 3 is not, and must be gated by (a)-(c)
before it is used for anything.** The question is offered because R27's sentence contains
its own counterexample, not because the conclusion is attractive.
