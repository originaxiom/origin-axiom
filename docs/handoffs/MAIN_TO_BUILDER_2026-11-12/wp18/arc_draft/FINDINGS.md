# B[[N]] — The parent algebra: what the ladder's rule gives, what the lattice glue gives, and what each is given

*Main, 2026-11-12 (S306p). The first step of the plan's package WP-1.8: is the gauge parent forced by the moves, or
supplied? Exact arithmetic, 19 checks. No measured number is read. 0 of 19.*

## 1. The answer first

- **The parent is supplied.** Nothing here derives E₈ from the register, and neither of the two routes on the record
  claims to.
- **The ladder's rule** gives the three rungs whose diagrams are E₆, E₇ and E₈, and E₈ is the one of the three that
  holds the others. That one algebra must hold every rung is the rule's own clause, adopted by a ruling.
- **The agy lane's lattice glue** is correct as arithmetic, and it is less of a choice than its note says, and more
  of one:
  - **Less:** the glue itself is not chosen. Given two copies of the lattice D₄, the ways of gluing them to an even
    self-dual lattice are six, one for each permutation of D₄'s three non-zero classes, and every one of the six is
    E₈.
  - **More:** three things are given before that. The lattice D₄ for the register; two copies of it; and that the
    whole be even and self-dual. The lane's note names the second and the third. The first is the lane's premise and
    is not verified on main.
- **So the package's question has its second answer:** "the parent, declared", as one line of the input budget. What
  this arc adds is what exactly the line holds.

## 2. What was computed

| | statement | how |
|---|---|---|
| 1 | the quotients of the moves by the N-th power of T have orders 6, 12, 24, 60 at N = 2, 3, 4, 5 | by enumerating cosets in the presented group; they are the orders of PSL(2, ℤ/N) |
| 2 | at N = 6 the quotient is infinite | a representation by motions of the plane over the Eisenstein integers, with S of order 2, ST of order 3, T of order 6, whose image holds a translation; and the coset enumeration does not close within 3,000 |
| 3 | the lifts at N = 3, 4, 5 have orders 24, 48, 120 | counted in SL(2, ℤ/N) |
| 4 | the diagram of E₈ holds those of E₇ and E₆; E₇ holds E₆; neither holds E₈ | connected pieces of the diagrams, compared as graphs |
| 5 | D₄ has 24 roots and four classes; the three non-zero ones have norm 1 and add to one another | vectors of norm 2, listed block by block and again by listing every integer vector with coordinates from −2 to 2; the class of a sum |
| 6 | the classes of two copies have 35 subgroups of order four; the norm vanishes on six; the six are the graphs of the six permutations of the three non-zero classes | enumerated |
| 7 | each of the six gives an even lattice of determinant 1 with 240 roots | roots counted in the cosets; the determinant by the index |
| 8 | two copies alone: 48 roots, determinant 16. With the diagonal vector class: 112 roots, determinant 4. The lane's chain is the identity permutation: 112 roots with integer coordinates and 128 with half-integers | the same count |

**Why 240 roots and determinant 1 is E₈.** The even self-dual lattice of rank 8 is unique. That is a standard
theorem and is cited, not proved here.

## 3. What it means for the foundation

| item | as it stands | what this arc shows |
|---|---|---|
| F-MC, the rule R1 | the rungs are the quotients by the powers of T, finite for N = 2 to 5; the container E₈ is adopted by the ruling, not derived | the rungs and the end at 5 are recomputed. The container is the largest of three nested diagrams; that there be a container is the adopted clause |
| F-MC, the rule R2 | invariance under every move selects a self-dual lattice only for one scalar theta series | consistent with it: self-duality is one of the three things the glue is given, and nothing on the record earns it |
| the lanes' parent (the map's node for it) | a compact E₈ theory, supplied | supplied, with its three givens named |
| the field's genesis, FK15 | open | not touched |

The foundation is not changed in this arc.

## 4. What is not shown

- **That the register carries the lattice D₄.** It is the lane's premise. On main the quaternion point has the group
  of 24 units that are D₄'s roots; that is a resemblance and no derivation.
- **Why two copies,** and why self-dual.
- **The embedding and the fields.** The rule fixes neither (the foundation's fork FK11), and the glue fixes neither.
- **The lane's code** was not run. Its statements were read through main's mask and computed again from them.

## Seen first

`python3 scripts/checks/topic_sweep.py` for the glue of lattices, self-dual lattices and the container: 8 of 1,643
arcs match and 5 register rows. Of the arcs, B1752 and B1754 are the foundation's versions 1.57 and 1.58, which hold
the ladder's rule in its merged wording with the web seat's correction that the rungs' groups form no chain; B155 has
a glue of another lattice; none computes the glue of two copies of D₄. Of the rows, P-463 notes that the record names
two different E₈'s alike, the container and a chain inside E₁₀. B997 holds the count of the lifts' orders, and B1859
corrected its uniqueness clause.

**The literature:** not searched. Two standard facts are used and named: the triangle groups (2, 3, N) are finite
exactly below 6; the even self-dual lattice of rank 8 is unique.

## Disclosed

- **The glue chain is the agy lane's** (its relay of 2026-11-07), read through the mask. Its own label says that E₈
  remains a supplied premise.
- **The count of six gluings is main's addition** and was not in the note.
- **One of main's planted checks did not do what its name said** and was replaced before the run that is kept.

## Reproduce

```
python3 -B frontier/B[[N]]_[[slug]]/verification/the_parent_on_main.py
python3 -m pytest -q frontier/B[[N]]_[[slug]]/verification/
```
