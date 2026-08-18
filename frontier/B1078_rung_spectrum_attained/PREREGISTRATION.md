# PREREGISTRATION — B1078 (post-hoc, and labelled as such)

**This arc was NOT preregistered.** It began as an exploratory probe of B1075's rung
spectrum and the structure was found before the controls were written. Recording that
plainly is the point of this file; a post-hoc registration that pretends to be a prior one
is worse than none. Cf. B874, which carries the same honest label.

## Why it is nonetheless checkable

A preregistration exists to stop the author choosing the test after seeing the answer. Here
that protection comes from a different direction: **every control is falsifiable by the
banked corpus, not by this arc.** None of them can be tuned, because none of their target
values were chosen here.

| control | fails if | fixed by |
|---|---|---|
| the sixteen coordinate subsets reproduce `{12, 30, 78}` | the charge build differs from B1075's | **B1075** |
| exactly 6 weights, total multiplicity 18, vanish on the (8,16)-plane | the arrangement picture is wrong (`12+18 = 30` is forced) | **B874 §1** |
| the plane cubic generates `K = ℚ[x]/(x³−12x−5)` | the enhancement is not B866's | **B866** |
| three faithful primes give the same flat lattice | reduction is not faithful | internal, ≥2 primes |
| every independently banked rung value lies in the spectrum | the enumeration is incomplete | **B866, B874, B892, B1075** |
| dimensions account to 78 | the decomposition is not a decomposition | arithmetic |

The last row is the strongest: `12 + 18 + 12 + 36 = 78` is not a number this arc chose.

## Declared outcomes, before the flats were enumerated

| result | reading |
|---|---|
| the spectrum is `{12,30,78}` | the paper's Remark `rem:spectrumscope` is right and the sample was representative |
| the spectrum is strictly larger but smaller than eleven | the bound is not tight; report which values are missing and why |
| the spectrum is all eleven | the bound is **tight**; the paper may restore attainment, and `thm:smt`'s 14-locus occurrence stops being an assumption |
| the spectrum contains something **outside** the eleven | Theorem `thm:rungspec` is **false**; that is the finding, and it outranks everything else here |

The fourth row is the one that would have killed the paper's theorem. It did not fire.

## Controls against my own known failure modes

1. **No headline may be a printed constant** (E43). The eleven values are read out of a
   computed dict; the exponent 16 on the plane cubic is read off `charpoly(Q)`, not asserted
   from `46 − 30`.
2. **Every control targets the claim.** Each row above names the arc that would falsify it.
3. **Quantifier stated first.** The ALGEBRA layer, over `C`. Nothing about class, sisters, rows.
4. **No absence without search.** The 46's absence from B1075's sample was a hypothesis; the
   search found it is an *arithmetic* absence — the cubic is irreducible over ℚ.

## Scope declared in advance

Steps (1) and (2) are exact over ℚ. The flat enumeration is exhaustive **at three faithful
primes** and is **not** a ℚ̄ certificate: mod-p reduction can only *add* linear dependencies
among the weights, so a flat could in principle be coarser than its ℚ̄ counterpart. That
residue is registered, not hidden. Gate 5: no physical identification.
