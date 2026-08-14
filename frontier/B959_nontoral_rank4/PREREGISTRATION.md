# B959 PREREGISTRATION — L133: IS THERE A RANK-4 CENTRALIZER IN E₆ THAT KEEPS THE 27 COMPLEX?

**Date sealed:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS.
Gate 5 untouched. **Register:** L133, as amended by B955's scouting.

**BANKED IDENTITY:** before any new number is read, the pipeline must reproduce B958's
computation on the same instrument — **dim Z(su(3)_colour) in e₆ = 16** (stacked ad-rank 62
of 78) — and abort if it does not.

**PRIOR ART:** discharged by **B955** (this cell's own scouting panel), which established
at design time: the E₆ → SU(5) two-27-VEV route is **standard** and must never be claimed
as novel; abelian holonomy is rank-preserving **necessarily** for a knot complement
(H₁ = ℤ); ℤ₃×ℤ₃ and Heisenberg are **not importable** into a knot group; π₁(m004) **does**
have A₄, D₅, S₅ images; and **Keurentjes's exhaustive E₆ scan returns unbroken ranks
{6, 2, 0} — rank 4 never occurs.** Borel (Tôhoku 1961) supplies the torality theorem.

## The question

L133 needs a rank-reducing mechanism that is not θ and preserves the 27's complexity. B955
closed the abelian route and left one hatch: **non-abelian finite images** (A₄, D₅, S₅).
Every such image's centralizer is contained in the centralizer of its elementary abelian
subgroups, so the cell reduces to:

> **Does E₆ contain a subgroup whose centralizer has rank 4 AND on which the 27 stays
> complex?**

**The hinge, stated before computing.** A centralizer drops below rank 6 only if the
subgroup is **non-toral** (not inside any maximal torus) — otherwise it contains that torus.
E₆'s torsion primes are {2, 3}, so non-toral elementary abelian 2- and 3-subgroups are *not
excluded a priori*. Meanwhile the **outer** involution route reaches rank 4 immediately
(F₄, dim 52; and C₄ = sp(8), dim 36 — both rank 4). So there are exactly two ways down, and
the cell tests both.

## The cells

1. **Banked-identity gate.** Reproduce dim Z(su(3)_c) = 16. Abort on failure.
2. **Inner involutions.** Confirm that every inner involution's fixed subalgebra has rank 6
   (it contains a Cartan). Establishes that single inner elements can never help.
3. **The outer route and the reality test.** Both outer-involution fixed subalgebras have
   rank 4. **Restrict the 27 to each and determine whether it stays complex.** For F₄ the
   expected branching is 27 → 26 + 1; for C₄ = sp(8), 27 → Λ²₀(8). **If both are self-dual,
   every rank-4 subalgebra reachable this way makes the 27 real** — and since a real
   representation stays real on restriction to any subalgebra, that would be a **no-go
   covering the whole outer route at once.**
4. **The non-toral inner route.** Determine whether E₆ admits a **non-toral** elementary
   abelian 2-subgroup, and if so compute its centralizer's rank and the 27's reality there.

## The two outcomes (fixed now)

- **OUTCOME FOUND** — some subgroup of E₆ has a rank-4 centralizer on which the **27 remains
  complex**. Then the group theory permits what L133 needs, and the question moves to
  whether π₁(m004)'s A₄/D₅/S₅ images realize that embedding. L133 stays open and becomes a
  representation-theoretic search.
- **OUTCOME NO-GO** — every route to rank 4 makes the 27 real. Then **no centralizer
  construction whatsoever — measurement, holonomy, or finite image — can deliver chiral
  matter at the Standard Model's rank**, and L133 closes as a theorem rather than an
  absence. **This would convert the programme's four independent negatives into one
  structural statement**, and is the more valuable outcome.

No third outcome. If the banked-identity gate fails, that is an INSTRUMENT FAILURE and no
verdict is read.

## The disclosed prior

**NO-GO, moderately favoured.** Three reasons, all stated before compute: (i) B955's
strongest datum is that the nearest exhaustive E₆ scan finds ranks {6, 2, 0} and **never
4**; (ii) the same trade-off — rank bought at the cost of chirality — has already appeared
**twice independently** (B953's θ-even/θ-odd split; B956's closure ladder), and a pattern
recurring at two levels is the signature of a theorem rather than a coincidence; (iii) the
outer route lands in F₄ and C₄, and **both are groups whose representations are famously
self-dual.**

**FOUND is the convenient answer and must clear the higher bar.** A NO-GO closes the
programme's central structural question against its own hopes, which is precisely why the
prior is written down first.

## Files (after sealing)

`b959_cells.py` → `results.json`; `FINDINGS.md` verbatim against these criteria; locks in
`tests/test_b959_nontoral.py` (seal-integrity first, then the banked-identity
reproduction, then one lock per outcome branch).
