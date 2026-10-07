# The three-orbit: on the only three-ended companion in the family, the three one-generation members are one orbit of the symmetry that cycles the ends

cc (the SM-derivation seat), 2026-10-07. **Structure and proofs only. No count is computed here; the counts quoted are
main's B1492, cited, not re-derived.** Written for the owner's question of 2026-10-07: "what if the three generations
dont emerge at once or in one place, but as a process in more steps". The owner's rule of the same day: "interaction
between objects in relationship should produce reality, not single objects alone".

## 1. What main read (B1492, cited)

On L8a15, +LLLR's three-ended companion (this seat's companions note; main's B1491 identified it), main read this seat's
frame at the eight sign characters, with the cusp decomposition of every count (main's relay of 2026-10-07, "your
companions read under seal"):
- **The members.** Exactly three characters carry an interior class. Each is trivial on no end, its class is dead on every
  end, and each reads (I(W₁), I(Λ²W₁)) = (−1, −1): one generation.
- **The rest.** The three characters trivial on exactly one end carry a boundary-type class reading (0, 0). The trivial
  character carries three boundary-type classes reading (0, 0). One more character, trivial on no end, has h¹ = 0.

Main's summary: on every object read, one end, three or five, the count at a member is one.

## 2. What this note adds

**Proposition A (one state has three ends).** Among the generated states, exactly one has a companion with three ends:
+LLLR.
- A state's companion has |2 − tr φ| ends (the companions note, Proposition 1).
- For a positive word in L and R of length n using both letters, tr ≥ n + 1, attained by Lⁿ⁻¹R.
- With the sign + the companion has tr − 2 ends; with the sign − it has tr + 2 ≥ 5. So three ends needs the sign + and
  trace 5, hence length at most 4. Among those words only LLLR, up to rotation and the swap, has trace 5.
- Checked by `three_orbit.py` for every word to length 8: the least trace at length n is n + 1, and the only word of
  trace 5 is LLLR.

**Proposition B (the three members are one orbit).** The deck group of L8a15 over +LLLR is ℤ/3. It is the group of the
three fixed points of L³R, acting by translation, and it cycles the three ends. It permutes the eight sign characters
in four orbits:
1. the trivial character, trivial on every end;
2. one fixed character, trivial on no end: the restriction of +LLLR's fibration sign, main's character with h¹ = 0;
3. **one orbit of three characters trivial on no end: main's three members, each reading (−1, −1);**
4. one orbit of three characters, each trivial on exactly one end (one per end): no interior class.

*Proof.*
- A character fixed by the deck group extends to +LLLR, because H²(ℤ/3; ℂ*) = 0.
- +LLLR has H₁ = ℤ ⊕ ℤ/3, so its only non-trivial sign character is the fibration sign. Hence exactly one non-trivial
  sign character of L8a15 is fixed.
- Orbits of ℤ/3 have one or three elements. So the other six characters fall into two orbits of three. The deck action
  preserves the set of ends on which a character is trivial, up to the cycling of the ends.
- `three_orbit.py` computes the same orbits from SnapPy's isometries of L8a15, under each of the four isometries that
  cycle the three ends. □

**So the three generations on the three-ended companion are one generation carried around the three ends.** No
character carries more than one, and the three that carry one are the steps of a single orbit: τ, τ², τ³ = 1, with τ
the symmetry that comes from the fixed points of +LLLR's monodromy. The same argument on any companion with a prime
number d of ends puts its non-pulled-back members in orbits of exactly d.
- On m003's five-ended companion, main's 25 members (15 trivial on one end, 10 on two) are five orbits of five.
- Main read six characters trivial on no end there with h¹ = 0. One of them is the fixed restriction of m003's
  fibration sign, and the other five are one orbit.

## 3. What it would mean, and what it does not show

- **The reading (a hypothesis, not a result).** Suppose the physical generations of a state are the deck orbit of a
  one-generation member on its companion. Then their number is the number of ends, |2 − tr φ|. Three then selects
  exactly one state of the family, +LLLR.
- **What it assumes.** That the generations are summed over the orbit. That is a rule the genesis would have to supply.
  It is GENESIS FK14's question (are generations ends?) asked one step further (are they an orbit of members over the
  ends?). It is not derived here.
- **What it leaves out.**
  - The members are sign characters, and their one generation is the b0 one (main: "the one generation there is the b0
    one").
  - Characters of order 4 and 8 on the companions, where b0 = 0, are main's next read.
  - An exact ℤ/3 makes the three generations alike. The observed generations differ in mass, so a reading of this kind
    needs the symmetry broken, and nothing here breaks it.
- **What would test it.**
  - Main's read of L8a15 at orders 4 and 8: does any member there read more than one, or break the orbit pattern?
  - The companion of a state with four ends (m136's, deck group (ℤ/2)²), where orbits need not all have the same size.
  - The same orbit question on the levels of +LLLR.

## Files

- `three_orbit.py` → `three_orbit.json` (SnapPy; structure only; a minute).
