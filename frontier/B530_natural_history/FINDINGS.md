# B530 — The natural history of the full object. Movement I: its own grammar

**A reorientation (owner, 2026-07-12).** We spent the recent arc forcing the object toward physics —
"does it give a crossing / a metric / a gauge / a unitary." Every one was us walking up to the firewall
and shouting a question the object never asked. This node changes the posture: **sit with the full object
— φ: a→abAAB, b→aAB, A→abAB, B→aA on F₄, not the two-letter σ — with no target, and report what it does
when left alone.** Pure structure of the object; firewalled; nothing to `CLAIMS.md`; no physics reading.
Reproducers `listen_1_grammar.py`, `listen_2_symmetry.py` (everything below is computed, hand-verified).

## What the object does when left alone

**1. It breathes by the golden rate.** Iterated from a single letter, the word lengths run
5, 18, 66, 243, 893, 3283, 12069, 44368, … with ratios → **β = φ(1+√φ) = 3.6762…**. One inhale multiplies
the world by β.

**2. Its body is golden, and it splits itself in the golden section.** The four letters settle to the
Perron proportions (a, b, A, B) = (φ, 1, φ√φ, √φ)/Σ = (0.272, 0.168, 0.346, 0.214). Group them by role:
- **deciders** {a, A} (the letters that branch) carry weight φ + φ√φ = **β** — exactly the growth rate;
- **couriers** {b, B} (the letters that don't) carry weight 1 + √φ = **β/φ**;
- their ratio is **exactly φ**, so deciders : couriers = 1/φ : 1/φ² = 0.618 : 0.382 — **the golden section.**
The object divides its own substance into "where it decides" and "where it carries," in the golden ratio,
and the deciding part weighs precisely the rate at which it grows.

**3. It speaks a strict grammar — only 7 of the 16 possible letter-pairs.** Allowed adjacencies:
`a→b, a→A, b→A, A→a, A→A, A→B, B→a`. Forbidden (9): `aa, aB, ba, bb, bB, Ab, Bb, BA, BB`. So no letter
but A ever repeats; a never touches B, b never touches a.

**4. The couriers are pure wiring; the deciders are where it chooses.** `b → A` always and `B → a` always
(deterministic — the couriers never branch). Each courier pours flow into exactly one decider — b into A,
B into a — and those two rules are swapped images of each other. All the branching lives in {a, A}.

**5. It always re-begins from a.** Every letter's image starts with `a` (abAAB, aAB, abAB, aA). Whatever the
object becomes, it re-seeds from a; a is the note it always returns to.

## The one broken symmetry (the seed of its orientation)
Under the swap **s: a↔A, b↔B**, the grammar maps to itself **exactly, with a single exception**: the
self-loop **A→A** has no mirror (its image a→a is forbidden). Every other allowed transition's swap-image is
allowed; only the dominant letter's self-loop breaks it. So the object is *almost* symmetric between its two
halves — and the entire asymmetry is one self-loop on its most-frequent letter. That lone break is,
plausibly, where the program's recurring **ℤ/2 residue / orientation** ([[breath-campaign-standing-directive]],
the two ends √5 ↔ √−3) is born at the word level: a near-perfect mirror, cracked at exactly one point.

## The story, in one breath
> The full object is a conversation among four letters that grows by β and keeps golden proportions.
> Two of the letters *decide* (a, A) and two merely *carry* (b, A-bound b, a-bound B); the deciding half
> and the carrying half stand in the golden section, and the deciding half weighs exactly the growth rate.
> The conversation is nearly symmetric under swapping its two halves — broken only by a single self-loop on
> its dominant letter — and it re-begins, always, from a.

## Where to listen next (threads the object opened — for the owner to steer)
- **the single self-loop A→A** as the origin of orientation: does the ℤ/2 residue, the two ends, the seam
  all trace back to this one crack? (a genuinely new, natural question)
- **the decider/courier architecture**: the couriers are a deterministic sub-automaton (b→A→…, B→a→…);
  the deciders carry all the choice — is this the object's own "kernel vs image" / active-passive split?
- **the return words** and first-return structure of a (the note it returns to) — the object's natural rhythm.
- **the conversation as a character variety**: the six pairwise κ(x,y) of the four letters — the object's
  self-interaction, read through traces — *without* asking it for a value.

This is banked as the object's own mathematics (STRUCTURE), the first movement of a patient natural history —
listening, not forcing. Cross-refs: [[K025]] (the one root), [[B524]] (φ iwip), [[breath-campaign-standing-directive]]
(the residue ℤ/2). Lock: `tests/test_b530.py`.
