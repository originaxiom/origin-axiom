# Philosophical paths (P1–P5)

These five paths argue that "nothing being unstable" produces "something" through
**non-mathematizable** reasoning — linguistic, logical-metaphysical, anthropic,
process-theoretic, or apophatic. They are real positions in the philosophy of
existence; they are not, however, claims-bearing artifacts the way E1–E20 are.

They live here, separately registered, **for three reasons**:

1. To be exhaustive: a survey that excludes the philosophical paths because they
   are hard to formalize is dishonest, especially given that the original Origin
   Axiom intuition (the user's) is itself philosophical before it is mathematical.
2. To be governed: the rest of the project is bound to a strict claim-vs-frontier
   distinction. If we let philosophical arguments mingle with claims-bearing work,
   the discipline of `../GOVERNANCE.md` collapses. Separation preserves both.
3. To be useful: a precise statement of why a philosophical argument *cannot* be
   reduced to a mathematical mechanism is itself informative about the path-space.

**No content here promotes to `../CLAIMS.md`.** A philosophical path that gets
mathematized would gain a new E-tag and migrate to a `paths/E*/` directory.

## The five paths

### P1 — Negation-as-creation (linguistic)

*"To define 'nothing' presupposes something to delineate from."* The argument is
about language and reference. To say "there is nothing" is to make a statement; a
statement exists; therefore the very utterance contradicts its content. Heidegger
("nothing nothings"), Carnap (the elimination of metaphysics through logical
analysis of language), and the later Wittgenstein circle around this.

*Why it lives here, not in `paths/E*/`:* the argument is about the *use* of the
word "nothing." Mathematizing it (e.g., as Tarski-style truth conditions) either
trivializes it (empty type is a perfectly well-defined object) or imports
phenomenology that mathematics cannot capture.

*Relevance to the program:* if P1 is right, the very question "why is there
something rather than nothing?" is malformed — and the mathematizable program
(E1–E20) is trying to answer a question that does not, strictly, exist. That
would be a *negative* contribution but a real one.

### P2 — Gödelian / undecidability

*"'Nothing exists' is undecidable in any sufficiently expressive system."* In any
formal system rich enough to encode arithmetic, there are statements that are true
but unprovable. The argument: "absolutely nothing exists" is such a statement —
not because it is true, but because *any* sufficiently rich formal system whose
elements include possible-worlds-like objects cannot decide it.

*Why it lives here:* the argument leans on Gödel's theorems metaphorically. A
genuine mathematization would require specifying the formal system in which the
statement lives, at which point it migrates to E18 (bootstrap/consistency) or E14
(formal). The metaphorical version belongs here.

*Relevance:* shares territory with E18; P2 is the *philosophical* gloss of what
E18 tries to do *mathematically*.

### P3 — Anthropic / observer-required

*"Only observable universes are observed; nothing-universes never are."* If there
is no observer (because nothing exists), then "there is nothing" is never
*observed* to be the case. The universe we find is selected by the condition that
it contains observers.

*Why it lives here:* canonical anthropic arguments are mathematizable (Bayesian
selection effects, multiverse measures), but **the strong "nothing-cannot-be-
observed" form** is a metaphysical move about observation itself, not a
calculation. The mathematizable forms have a separate slot in E20 / Class K
discussions if we ever go there.

*Relevance:* anthropic arguments are well-known to be unable to *select* between
universes that all admit observers. Recording P3 here keeps that lesson visible.

### P4 — Process (Whitehead)

*"Reality is occasions of experience; non-occurrence is itself occurrence."* In
Whitehead's process philosophy, the fundamental units are not substances but
*events*; "nothing happening" is itself a happening (no-happening qualifies as an
occasion). Hence the void is impossible because to-be-void is to-be-an-occasion.

*Why it lives here:* Whitehead is dense and the formal apparatus (his "actual
occasions," "prehensions") is not mathematics in the testable sense. Some
contemporary work (e.g., process-relational physics) attempts mathematization but
the core argument is philosophical.

*Relevance:* P4 is, of the five, the closest in *spirit* to the user's original
intuition ("self-reference forces existence"). If any philosophical path were to
migrate to a mathematizable form, it would be P4 → E-something.

### P5 — Apophatic / theological

*"The unnamable precedes naming."* In apophatic theology (the Ein Sof of
Kabbalah, the Tao of Taoism, Pseudo-Dionysius's negative theology) the ground of
reality is precisely what cannot be named. Naming "nothing" makes it a name, hence
not-nothing; the unnamable persists.

*Why it lives here:* by construction not amenable to mathematics. Recording it is
honesty about the historical breadth of the question, not an attempt to use it.

*Relevance:* the user's transcript explicitly engaged this territory (the
ancient-creation-stories thread). P5 is registered so that engagement is not
silently lost when the project shifts to formalisms.

---

## How a philosophical path could ever leave this register

Only by being mathematized. If, e.g., somebody writes down a precise formal system
in which "absolutely nothing" is provably undecidable in Gödel's sense, P2
migrates to a new E-tag. Until then, philosophical arguments stay here, argued
rather than computed, and clearly outside the claims layer.

---

## Companion documents (the architecture)

This `philosophy/` folder holds the **motivation** layer (P000–P006 below + P1–P5 above + the foundations doc).
The **evolving speculative ideas** live one room over in `../speculations/` (the catalog `S001…S021`, the live
exercise, the tombstones); the **narrative** is in `../story/`; the one-page map is `../ARCHITECTURE.md`.

- `METALLIC_FOUNDATIONS.md` (here) — *why aim the theorem at the family, not the seed* (the "not-nothing → a
  self-generating family" rationale; the source material for **P000**).
- `P000`–`P006` (here) — the foundational philosophical layer (what-is-not-nothing; architecture-not-furniture;
  necessity-given-chosen-premises; dead-ends-as-boundaries; expansion-is-interaction-born; laws-and-states;
  two-headed-time), distinct from the P1–P5 argument register above.
- `../speculations/PHYSICS_EXERCISE.md` — the deliberate "*assume it is the final theory*" exercise (the tiered
  MASTER), whose only legitimate output is the ranked calculation pointers. Its earlier long-form draft and the
  six adjudicated "paths to physics" are archived at `../speculations/archive/`.
- **No content here promotes to `../CLAIMS.md`; the physics chapter stays CLOSED.**
