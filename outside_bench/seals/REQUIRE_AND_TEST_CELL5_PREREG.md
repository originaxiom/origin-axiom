# PREREGISTRATION — CELL 5: fork F9 past its declared depth bound

*Outside bench, 2026-09-14. Sealed before the extension runs. Gate 5 untouched.*

## Why this cell — the record names the next step and no arc has taken it

`frontier/B1323_the_genesis_upgrades/FINDINGS.md` §5, **"Not claimed"**, verbatim:

> that F9's ROBUST extends beyond **words of length 3** on the two punctured carriers (**a longer
> enumeration or a proof is the next step if anyone wants the general statement**)

and its scope line:

> the statement **"the atom or the remembered bit, not both"** is a computed fork over the enumerated
> set, **not a theorem about all carriers**

This is the "change the 0.6 %" item: **eight arcs of 1246 test the axiom forks**, and F9 is the newest
of them, banked 2026-09-09 with its own bound stated. Extending it is the cheapest real increase in
that fraction available.

## THE INSTRUMENT IS THE ARC'S OWN

Per memo 154 — *run the corpus's own applicable checks before building a bespoke instrument* —
`frontier/B1323_the_genesis_upgrades/verification/u1_substrate_count.py :: part_c(maxlen)` is used
**unmodified**. It is already parameterised by `maxlen` and already computes the verdict this cell
needs: `F9_surface_verdict` = FRAGILE if any three-record bundle keeps ℚ(√−3), else ROBUST, with
`keepers_of_Q(sqrt-3)` naming them.

**Dependency note, declared:** the arc's `shape_field` needs `python-flint`, which was absent from this
container and was **installed** (0.9.0) rather than substituted, so the arc's own code runs unaltered.

## P — the predicate

**P_atom = the three-record bundle's shape field lies in ℚ(√−3)** — the atom. F9's claim is that no
three-record carrier keeps it.

## THE EXTENSION

`part_c(maxlen=5)` on the two punctured carriers with H₁ = ℤ³: **S₁,₂** (6 generators: a, b, c and
inverses) and **S₀,₄** (4 generators). Words of length 2…5 — against B1323's 2…3. Word counts:
S₁,₂ 6²+6³+6⁴+6⁵ = **9324**; S₀,₄ 4²+4³+4⁴+4⁵ = **1360**. Freely-reducible words are skipped by the
arc's own filter, as at depth 3.

## THE TWO OUTCOMES

- **OUTCOME A — F9 SURVIVES TO LENGTH 5.** No three-record bundle at depth ≤ 5 keeps ℚ(√−3). B1323's
  bound moves from 3 to 5; *"the atom or the remembered bit, not both"* holds over a population
  roughly **32× larger**, and is still not a theorem.
- **OUTCOME B — F9 IS FRAGILE.** Some bundle at depth 4 or 5 keeps ℚ(√−3). **A three-record carrier
  keeps the atom, and B1323's fork is refuted at depth.** The keeper is named, its census identity,
  volume, cusps, symmetry group and chirality reported, and A1's *"not one, not three"* loses its
  computed price.

Both are reportable. B1323 recorded a prior of ROBUST and earned it at depth 3; this cell states no
prior of its own beyond that.

## CONTROLS

| # | control | catches |
|---|---|---|
| N1 | **the depth-3 run must reproduce B1323 exactly** — four classes: m129 (abC, vol 3.663862, 2 cusps), s780 (acB, 5.33349), t12047 (aB, 7.327725, 4 cusps), o9_44206 (aaB, 8.929318, 4 cusps), verdict ROBUST, keepers [] | a changed instrument, a changed dependency, or a changed census silently altering the baseline |
| N2 | the S₁,₁ control returns **m004** (word a·B), one cusp | the carrier machinery mis-wired |
| N3 | the depth-5 population must **strictly exceed** the depth-3 population on both carriers, and both counts printed | an extension that did not actually extend — the B1197 vacuity trap in its subtlest form |
| N4 | `all_in_Q(sqrt-3)` must be shown able to return **True** — run it on m004's own shapes, which are in ℚ(√−3) | a keeper test that can never fire, which would make OUTCOME A vacuous (#164: control passing is not instrument working) |

**N4 is the one that matters.** F9's verdict is an absence. An absence computed by a predicate that
cannot return True is not evidence.

## WHAT THIS CELL MAY NOT CONCLUDE

That F9 is ROBUST for **all** word lengths, or for carriers other than S₁,₂ and S₀,₄ — B1323's own
scope line is kept verbatim, with only the number 3 replaced by 5. The closed genus-2 carrier remains
out of frame (A5b). Nothing about physics. No value.
