# B1601 — THE COMMON POINT IS THE GEOMETRY MOD 3: on every odd-trace thread to length eight the fibre's holonomy reduces to the weave's common point at exactly one prime of its trace field, of norm three, and on no even-trace thread does it — W3's forced cover is each thread's own congruence cover at that prime

**Verdict: PROVED** (a weave result; the law on the census of every thread to length eight, the lemma general) — M1, M2,
M3 hold; M4 holds with two disclosed sign-orbit splits. Scope: every primitive word in L and R with both letters to
length eight, up to rotation and the exchange of L and R, either sign (37 geometries: 16 of odd trace, 21 of even);
the fibre's trace ideal (tr a, tr b, tr ab) at the geometric point. cc (main), 2026-10-07. Sealed `3c56a10f1` before
any word of length eight but one was computed. Toward the derivation: a structural fact of the weave, not a count. No
physical quantity. **0 of 19.**

**Credit.** The SM seat for W2–W3 (the common point and 2T on every odd-trace thread) and for the census whose pattern
posed the question; B1423 for the door (3 ramified in ℚ(√−3), residue field 𝔽₃); B1600 for the Fricke maps.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /quaternion point|common point|mod 3|modulo 3|congruence cover|congruence subgroup|trace ideal|Markov surface|SL\(2, ?F_?3\)|binary tetrahedral|residue field/: 24 of 1372 arcs on main match (NEGATIVE 4, OPEN 1, PROVED 18, RETRACTED 1)`
— B354, B448, B794, B1423, B997/B1402, B1600. Seen before the seal: the six odd-trace words to length six and
LLLLLLLR at norm 3; LLR (8) and LLRR (64); the lemma on all 37 words. A hypothesis killed before the seal (meeting ⟹
content) is on the preregistration. **Literature:** the Markov surface as the parabolic character variety (Goldman);
reduction of integral representations (standard); Bowditch–Maclachlan–Reid (±LR, ±L²R² the arithmetic bundles).

## 1. The law

**T-COMMON-POINT-MOD-3** (census law to length eight; the existence lemma proved). Let w be a primitive word in L and R
with both letters, M = ±w its thread, (x, y, z) = (tr a, tr b, tr ab) the fibre's traces at the geometric point, K =
ℚ(x, y, z) and I = (x, y, z) ⊂ O_K. Then x, y, z are algebraic integers, and

- **odd trace:** I is **one prime of residue degree one above 3** — norm exactly 3, multiplicity one, no other prime:
  the fibre's holonomy reduces modulo that prime to the quaternion point a ↦ i, b ↦ j (the origin of the Markov
  surface over 𝔽₃, where trace zero means order four) and modulo no other prime to anything but a point with a
  non-zero trace;
- **even trace:** I is a **power of one prime above 2** (norms 4, 8, 64, 1024 occur), where the origin is the trivial
  representation; nothing above 3.

| | sealed prediction | prior | result |
|---|---|---|---|
| **M1** | the nine unseen odd-trace words of length eight: one prime of degree one above 3, norm 3 | 70% | **HOLDS** 9/9 — with the seven seen, **16/16**: traces 3, 5, 7, 9, 11, 13, 15, 17, 19, 25, 25, 27, 29, 29, 37, 39; fields of degree 2 to 38; every valuation of x, y, z at the prime exactly 1 (`meets_odd_8.json`) |
| **M2** | the eighteen unseen even-trace words other than LLLLRRRR: nothing above 3 | 70% | **HOLDS** 18/18 — with LLR and LLRR, **20/20**: norms 4 (eight words), 8 (seven), 64 (five); each one prime above 2 |
| **M3** | LLLLRRRR (linear part the identity) prime to 3 | 50% | **HOLDS**: norm 1024 = 2¹⁰, one prime above 2; its four primes above 3 all have residue degree four — there is no 𝔽₃-point for the geometry to land on |
| **M4** | integral traces and one matched component on all 37 | 85% | **HOLDS with two disclosed splits**: integral 37/37; the cusp shape matched exactly one irreducible component on 35/37; on LLLRLRLR and LLLRRLRR it matched two, the two being mirror images (u ↦ −u) carrying the geometric point's sign orbit, and both give the same ideal (norm 4, one prime above 2) |

**Corollary (the forced cover is a congruence cover).** The reduction of the holonomy modulo the prime of norm three
is a homomorphism π₁(M) → SL(2, 𝔽₃) = 2T whose restriction to the fibre is the quaternion point; its extension over
the base is W3's τ (unique up to the sign, which dies in A₄). So the kernel of π₁(M) → PSL(2, 𝔽₃) = A₄ is W3's forced
cover: **on every odd-trace thread the forced A₄ cover is the thread's own principal congruence cover at a prime of norm
three** — on m004 at (√−3), where 3 ramifies (B1423); on +LLLR, where two A₄ quotients exist, the forced one. The
weave's common structure is each thread's geometry seen modulo 3.

## 2. The lemma (proved; `linear_part_8.json`)

The Fricke maps L: (x, y, z) ↦ (x, z, xz − y) and R: (x, y, z) ↦ (z, y, yz − x) have at the origin the linear parts
dL = a quarter turn about the x-axis and dR = a quarter turn about the y-axis (checked symbolically): the signed
permutation action of the moves on the three lines x ↔ (1, 0), y ↔ (0, 1), z ↔ (1, 1) — W1's parity action with signs,
W4's triplet. They generate the rotation group of the cube, S₄ (order 24, the weave's group on the triplet with L and R;
the seat's O_h with the sign). For a word w, dφ_w(0) ∈ S₄ has determinant one; its image in S₄/V₄ = S₃ is the parity
permutation, so by the parity lemma (B1600) **odd trace ⟺ dφ_w(0) is a third turn about a body diagonal**, with fixed
axis (±1, ±1, ±1) — and x² + y² + z² = 3 on it: **isotropic for the quadratic part of the Markov surface exactly in
characteristic three.** Over 𝔽₃ the parabolic Markov surface has exactly one point, the origin (enumerated), so wherever
a thread's trace field has a degree-one prime above 3 at which the traces are integral, the geometry lands on the common
point; the lemma's isotropic axis is what makes the origin a degenerate fixed point modulo 3 and forces a geometric fixed
point into it. For even trace the fixed space of dφ_w(0) over 𝔽₃ carries no isotropic vector (20 of 21 words: a
coordinate axis or a face diagonal), except LLLLRRRR, where dφ(0) = I and M3 shows the geometry still does not meet.
What is proved: the lemma and the one-point count over 𝔽₃. What is a census law: that odd trace always supplies a
degree-one prime above 3 with the traces in it, that it supplies exactly one, with multiplicity one and nothing else,
and that even trace never does. The theorem is open.

## 3. W5 (`w5_four_at_the_common_point.py`, exact)

At the common point the frames' own module, the four (H ↦ gHg*), is diagonal in the basis (1, i, j, k): Ad(i) = (1, +1,
−1, −1), Ad(j) = (1, −1, +1, −1), Ad(k) = (1, −1, −1, +1), Ad(−1) = I. **The four at the common point is the trivial line
plus the three parity lines** — B1493's "the generation is the trivial line" and W4's triplet are the two parts of one
module (the seat's "matches the quaternion axes", stated on the four).

## 4. The seat's census, four cells on main (`../B1600_the_weave_verified/verification/forced_cover.py`)

W3's forced A₄ cover built from SnapPy's presentation (the surjection π₁ → A₄ whose composite to ℤ/3 is the thread's
map to ℤ mod 3; the regular right action, twelve sheets) and the four read at every sign character with B1492's stacked
instrument: **+LR** (m004): 4 cusps, H₁ = ℤ⁴ ⊕ (ℤ/2)², 64 sign characters, **24 members, each (h¹, r¹, n) = (1, 0, 1)**;
**−LR** (m003, SnapPy's `b+-LR`): H₁ = ℤ⁴ ⊕ ℤ/5, 16 sign characters, **6 members, each (4, 0, 4)**; **+LLLR** (two A₄
quotients, the forced one chosen): 16 sign characters, **none**; **−LLLR**: 64, **none**. The SM seat's census rows at
order two reproduced exactly (HARVEST row 913). So the seat's pattern — content on the forced cover only on ±LR — stands
on main's code for the four threads read; and this arc shows what it is not: the mod-3 meeting is universal on odd
trace, so ±LR is not singled out by it. What singles ±LR out among odd-trace threads remains arithmeticity
(Bowditch–Maclachlan–Reid), unexplained.

## 5. Disclosed

- **Post-seal changes to the instrument, all mechanical, none to a criterion:** (i) the lex Gröbner basis replaced by
  grevlex + FGLM (the same ideal, the same basis; the lex run stalled at length eight); (ii) PARI's stack raised, then the
  full `nfinit` replaced — it factors a discriminant of hundreds of digits and stalled — by an order maximal at the
  primes of gcd(N(x), N(y), N(z)), of the denominators and at 2 and 3, with the ideal read off prime decompositions
  and valuations (`idealadd` is undefined in a non-maximal order and returned a fraction, which an `int()` turned into
  an infinite loop — found by a stack dump); (iii) the Möbius map sending the puncture's fixed point to infinity was
  singular when the point was already there; (iv) when the fixed-point scheme is not in shape position even over the
  primitive element (LLLLRRRR), each non-origin factor is treated on its own. The seven seen odd words and LLR, LLRR
  give the same numbers under every version (the full-`nfinit` even census, 21/21, is kept in `stalled_runs/`).
- SnapPy's bundle names: `b++w` is the orientable bundle with monodromy +w and `b+-w` the one with −w (`b-+LR` is
  non-orientable, with no A₄ quotient); only `b++w` is used for the identification, the ideal being the same for both
  signs; the controls of §4 use `b+-LR`, `b+-LLLR` for −LR, −LLLR.
- Rotation and L ↔ R are quotiented; reversal is not (a redundancy; the ideal is the same).
- The seat's census zeros on +LLLR, −LLLR are reproduced at order two only; its orders three and four are not re-run.
- Not blind to the seat's census, to B1423 or to the pattern on the seven seen words.

## 6. Files

`verification/meets.py` (final; the sealed hash on `ARTIFACT_HASHES.txt`), `meets_odd_8.json`, `meets_even_8.json`,
`linear_part_8.json`, `w5_four_at_the_common_point.py`, `w5.json`, the run logs, `stalled_runs/`;
`../B1600_the_weave_verified/verification/forced_cover.py` and its four outputs; `adoption/amend.py` (GENESIS v1.25).
Test: `tests/test_b1601_the_common_point_is_the_geometry_mod_3.py`.

**Addendum (S82, 2026-10-07).** The items named W5 (§3) and W7 (§1) here collide with the SM seat's W5–W10, which were on its lane before this arc landed; on `docs/THE_WEAVE.md` and GENESIS from v1.26 they are **WM1** and **WM2**. The content is unchanged.
