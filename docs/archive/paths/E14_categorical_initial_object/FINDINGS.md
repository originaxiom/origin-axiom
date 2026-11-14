# E14 — Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Result

(a) **All four candidates are well-defined.** `∅`, the initial object `0`, the
empty type `⊥`, and the empty topological space are each unique (up to canonical
isomorphism) and supported by every standard foundational framework. There is no
formal obstruction to defining "nothing" in any of them.

(b) **None of the four characterizations forces emergence.** Each is defined
*precisely by* having no internal structure:

- `∅` has no elements; the axiom of empty set asserts existence; nothing else
  follows from extensionality alone.
- The initial object `0` is characterised by a *universal property* about
  morphisms *out* of it (there is exactly one). That property says nothing
  about morphisms *into* it (there are none, except from `0` itself) — i.e.,
  `0` is, by construction, a sink, not a source.
- The empty type `⊥` has no constructors; functions out are unique-trivial
  (*ex falso quodlibet*); there is no inhabitant to act on. Negation
  `¬A := A → ⊥` exists, but `⊥` itself has nothing to negate.
- The empty space `(∅, {∅})` is the unique topological space at the bottom of
  the lattice; continuous maps out are unique-trivial.

In all four frameworks the formal "nothing" is a *stable terminal endpoint of
the definition*. It is exactly as empty as it is supposed to be. The categorical
universal property of an initial object *makes "nothing" maximally well-defined
precisely by making it minimally structured.*

(c) **But the containing framework is not nothing.** To say "`0` is the initial
object" presupposes a category. To say "`⊥` is the empty type" presupposes a
type theory. The *characterization* lives inside a richer meta-framework; the
*characterised object* is empty. **This is the mathematizable form of the
philosophical path P1** (negation-as-creation): to define "nothing" is to do so
within "something," and the framework, not its empty object, is where the
content lives.

## What this means for the Origin Axiom program

The mechanism *"nothing is unstable, so something must exist"* requires
something the four formal characterizations do not supply: a **dynamics or
physical principle** under which the empty object is not a fixed point. Pure
formal characterization gives a perfectly stable empty object; it is the
extra ingredient — a Hamiltonian, an action, a measure, a process — that would
make it unstable. **The selection mechanism cannot come from formalism alone.**

This precisely identifies what every other E* path is responsible for
supplying. E11 (entropic) proposes counting; E5 (Vilenkin) proposes quantum
tunneling; E9 (SSB) proposes a potential; E18 (bootstrap) proposes
consistency. Each must specify *the extra ingredient* that turns the
well-defined empty object into an unstable one. E14 cannot do that on its own.

It is also worth recording: the empty object plays a real role in the
*framework's* arithmetic — `¬A := A → ⊥` defines negation in type theory; the
absence of an inhabitant of `⊥` is what makes consistency meaningful. The
empty object is *useful* without being *generative*. It earns its keep by
making "absence" expressible.

## Verdict

**`STALLED`**

The probe terminates with a clean characterization and a clean negative
result. *"Nothing"* admits four standard formal definitions. **None of those
definitions, by themselves, forces emergence.** The unconstructed step is the
same one Phase B probes named in their own contexts: a *physical or dynamical*
principle external to the formalism is required to make the empty object
unstable; the categorical / type-theoretic level supplies the *target* but not
the *force*.

This finding bounds the rest of the program: every E* probe must supply that
extra ingredient explicitly; appeals to pure formalism are insufficient.
