# E14 — Categorical / initial-object

> **Phase C frontier probe.** Logged observation, not a claim
> (`../../GOVERNANCE.md` §5). See `../README.md` for ground rules.

## The mechanism

Does the question *"is nothing unstable?"* even admit a sharp formal definition?
If "nothing" has a precise mathematical characterization, perhaps that
characterization itself has structural properties that force emergence — i.e.,
the formal object is *not* a fixed point of its own definition.

This is the **most foundational** path in the survey: it asks whether the rest
of the program is even formulating its question well. If "nothing" is not
formally well-defined, every E* path is reaching for an unspecified target. If
"nothing" *is* well-defined, the resulting definition either does or does not
force emergence — and that answer matters for every other path.

## Candidate formal characterizations of "nothing"

Four standard frameworks each offer a clean candidate:

1. **Set theory.** The empty set `∅`. Unique by extensionality. The free union /
   axiom of empty set / replacement give a perfectly determined object.
2. **Category theory.** The **initial object** `0` of a category: the unique
   (up to unique iso) object with exactly one morphism `0 → X` to every other
   `X`. In **Set**, `0 = ∅`; in **Top**, the empty space; in **Vect**, the zero
   vector space; in many categories, `0` exists and is unique.
3. **Type theory.** The **empty type** `⊥` (or `0`): a type with no
   constructors. Functions `⊥ → A` are unique-trivial (the *ex falso* eliminator).
   Negation is defined as `¬A := A → ⊥`.
4. **Homotopy type theory.** `⊥` is the empty type at every homotopy level. It
   has no points, no paths, no higher cells; trivial homotopy structure.

## The probe (formal analysis, no code)

Walk through each characterization and check:

(a) Is the candidate *well-defined* — does it exist, and is it unique up to
    canonical isomorphism?
(b) Does the characterization carry *structure* that would force emergence —
    i.e., is the formal "nothing" a stable fixed point of its own definition, or
    is it forced into having more than zero content?
(c) What does the answer require from the *containing framework* in which the
    characterization is stated?

The probe is purely conceptual — references and reasoning only, no computation.
See `FINDINGS.md` for the result.

## Prior literature

- Lawvere & Rosebrugh, *Sets for Mathematicians* — initial objects and the
  empty set.
- Mac Lane, *Categories for the Working Mathematician* — initial / terminal
  duality.
- Univalent Foundations Program, *Homotopy Type Theory* — the empty type and
  negation.
- Awodey, *Category Theory* (2nd ed.) — the initial/terminal object as the
  canonical formalisation of "nothing" and "everything."

No primary reference in the literature attempts to derive emergence *from* the
initial-object structure itself — which is itself diagnostic (see `FINDINGS.md`).
