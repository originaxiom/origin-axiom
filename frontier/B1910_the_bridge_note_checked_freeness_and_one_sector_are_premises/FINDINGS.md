# B1910 — The agy lane's bridge note on P-321, checked: freeness and a single sector are premises, and each is named (P-321; the last part of P-747)

**Verdict: PROVED** (both halves of the note hold exactly, each with the premise it needs named). cc (main), 2026-11-13
(S306p). Main's own code; the lane's note (relay of 2026-11-07) was read through the mask and its code was not run. No
data. **0 of 19.**

## 1. The answer first

- **Half 1, the quaternion point and the carrier.** The quaternion point, tr ρ([a, b]) = −2 (the input of GENESIS GM4), cannot
  be carried by the abelian carrier ℤ²: there [a, b] = 1, so its trace is +2 in every two-dimensional representation, the
  non-diagonalisable ones included. It **can** be carried by a carrier that is not free: the integral Heisenberg group
  H₃(ℤ) = F₂/γ₃(F₂), through its quotient Q₈ ⊂ SU(2) (i, j satisfy [[i, j], i] = [[i, j], j] = 1, and [i, j] = −1). So the
  point excludes ℤ² but does not by itself force the free group: narrowing to F₂ needs its own premise, that iterated
  commutators do not cancel. In SL(2, ℤ), the free group's image, [[L, R], L] = [[5, −1], [11, −2]] is not the identity, so
  F₂ does not factor through H₃. **With that premise named, GM4's reading holds:** with GM3 and the surface category only the
  once-punctured torus remains, without the step R57 rejected.
- **Half 2, the prime.** In the finite Heisenberg group H(p), both orientation-reversing moves, the swap (a, b) ↦ (b, a) and
  the tick's LP (a, b) ↦ (ab, a), send [a, b] to a conjugate of [a, b]⁻¹, so they carry the p-dimensional irreducible with
  central character ζ to the one with ζ̄. Exactly, for p = 2, 3, 5, 7: **a single irreducible sector is kept by both moves
  exactly when p = 2** (ζ = −1, and iZ, iX are Q₈ in SU(2)); the pair ρ_ζ ⊕ ρ_ζ̄, of dimension 2p, is kept at every p. So
  "the prime is 2" holds under the premise of a single irreducible sector, and not without it. A move of determinant +1 keeps
  the central character and selects nothing (the control).
- **By the record's rule on selections** (B1905's draft, from B1204): the pick of p = 2 is a finite classification with a
  membership test (which irreducibles a move keeps), under a declared premise (one sector). It is scoped as such.

## 1a. Seen first

`VERDICT topic-sweep /P-321|GM4|L239|abelian carrier|Heisenberg|the prime is 2/: 7 of 1648 arcs on main match (PROVED 7);
12 register rows match (DONE 5, QUEUED 7)`. What bears on it: B1680 (the common point in targets of higher rank: the record
swap and the tick fix the odd-p Heisenberg points only up to complex conjugation), B1707 (the transvection lemma, P-211),
B478 (a Heisenberg clock translation), and GENESIS GM4 with R57's rejected step. **Literature:** the Heisenberg group's
irreducible representations of dimension p (clock and shift; Stone–von Neumann), and that the free nilpotent group of class
2 on two generators is H₃(ℤ); standard.

## 2. A reading beside the note, not a result

The central character of an odd-p sector reads the determinant of a move: a move of determinant −1 sends ζ to ζ̄, one of
determinant +1 keeps it. So a weight built from such a sector does tell histories with an even number of ticks from those
with an odd number, but only after one of the pair ζ, ζ̄ is picked, and that pick is a choice of hand. At p = 2, where the
record's point sits, the character is blind to the determinant. This sharpens main's question on the hand (whether a derived
weight reads the parity of the ticks): such a weight exists among the odd-p sectors, and what it needs is the pick of one
of a conjugate pair. It is close to B1680's statement and claims nothing new.

## 3. The checks (`verification/the_bridge_note_on_main.py`, exact, sympy)

25 checks, none failing: the six of half 1; for each of p = 2, 3, 5, 7 the two moves' central characters, the single
sector and the pair (and at p = 2 the Q₈ form); two controls with a move of determinant +1.

## Files

- `verification/the_bridge_note_on_main.py` → `the_bridge_note_on_main.json`, `_run.txt`.
- The lock: `verification/test_b1910_the_bridge_note.py`.

## Reproduce

```
cd frontier/B1910_the_bridge_note_checked_freeness_and_one_sector_are_premises/verification && python3 -B the_bridge_note_on_main.py
```
