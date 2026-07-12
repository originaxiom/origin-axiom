# B551 — The inflation-order boundary theorem (chat-2 fusion death, verified)

Processes chat-2's "bravery cycle" fusion block verify-don't-trust. The
seductive claim "self-organized golden systems measurably carry ℚ(√φ)"
(fusing B543's species chain with B544's emergence results) DIED TWICE with
proofs, all independently reproduced here (`verify.py`, exact).

## Death 1 — the species word is NOT a coloring of the Fibonacci word

The case-fold projection π({a,A}→a, {b,B}→b) of the σ₄ fixed point contains
the factor **'aaa'** (first at position 16) — FORBIDDEN in the Fibonacci
word. So π(W₄) is not in the Fibonacci subshift, and no sliding-block code of
any radius lifts a 2-letter golden word to the species word. The frequency
coincidence f_a+f_A = 1/φ was a decoy. (Matches B532 GRAMMAR.md's own "NO"
on the {aA}|{bB} pairing.) VERIFIED.

## Death 2 — the old/new factor is non-Sturmian

The old/new projection π({a,b}→x, {A,B}→y) has letter frequency degree-4
(f_x = τ²(τ−1) = 0.4401370) yet complexity
p(1..8) = **(2, 4, 7, 10, 14, 17, 20, 23)** ≈ 3n, not n+1 — VERIFIED EXACTLY
to the digit. So it is NOT the mechanical (Sturmian) word of its slope, and
NO rotation-class self-organization (FK ground states at any winding, circle
maps at any Ω) can emit it. Rotation mechanisms produce degree-4 SLOPES; they
never produce the species LANGUAGE.

## The gem: the species word is a radius-1 coloring of its old/new shadow

VERIFIED: the map (old/new)_{i−1}, (old/new)_i, (old/new)_{i+1} → (species)_i
is single-valued, using **exactly 7 windows**. The full 4-letter object is a
nearest-neighbour decoration of its own binary old/new shadow.

## THE BOUNDARY THEOREM-LET

> **The object's degree-4 (ℚ(√φ)) layer requires SUBSTITUTIVE (inflation)
> order, not merely quasiperiodic (winding) order.** Emergent golden
> quasiperiodicity (Aubry/FK, mode-locking) carries only the ℚ(φ) shadow; the
> ℚ(√φ) layer lives in the inflation structure and is reachable physically
> only by instantiating the substitution itself.

## Consequences (banked)

1. The B544 emergence words DO NOT lift — the fusion claim, had it been
   asserted, would have been FALSE. Prevented error, logged as prevented.
   **B544 is SCOPED**: its FK/circle-map golden order is the CARRIER
   (Sturmian) self-organizing; it carries ℚ(φ), NOT the degree-4 ℚ(√φ) layer.
2. The 2b revival condition SHARPENS: "emergent golden order" → "emergent
   INFLATION order" (self-similar growth hierarchies, not incommensurate
   windings). No known physical candidate today; parked with the condition.
3. **B543 is STRENGTHENED**: the fabricated species chain is confirmed the
   non-shortcut-able route to the degree-4 layer.
4. Anti-numerology clause (on record before anyone steps on it): an FK chain
   at winding 0.44014 WOULD have degree-4 gap labels in ℤ+ℤ(τ³−τ²) — but that
   is the generic module of an ARBITRARY slope and fails CONTROLLED (a
   silver-slope chain does the same). Object-specific degree-4 = the species
   language, nothing less.

Locks: tests/test_b551.py.
