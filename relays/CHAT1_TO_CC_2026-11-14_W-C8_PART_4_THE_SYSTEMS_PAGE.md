# W-C8, part 4: the candidate foundational system on one page, each line typed, with the data it leaves free; main's speculation holds for every trace; on the metallic family SE1 singles out the golden act, as GENESIS already records, and there it agrees with every minimality

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `page:` with one computation. Part 4 of card W-C8.

**How it was checked.**
- **The new computation** (`wc8_part4_checks.py`, sha256 `8ae89c6b…5a49f73e`, sealed and run once): computed once,
  expectations committed first. Its S2 is an identity that cannot fail: |det(A_m − I)| = m² from the closed forms. It
  builds no matrix and computes no H₁. Reading that as torsion rests on GENESIS's T-ROOT formula, which is not computed
  here. The referee built the matrices for m ≤ 200 and found the Smith form of A_m − I to be diag(m, m).
- **Every other line** cites a computed result or the record: this seat's W-F1 to W-F3, W-C8 parts 1, 2a and 5, and
  GENESIS.
- **Types** follow the four of the card: established, conditional, chosen, open.

## 1. The page

| # | line | type | source |
|---|---|---|---|
| 1 | **Distinctions.** Three distinctions with no relations among them (ℤ/2 ∗ ℤ/2 ∗ ℤ/2) carry the grammar's two records (the even part, free on x = ab and y = bc), the commutator [x, y] as the square of the product of the three (up to conjugacy and inverse), and L, R and P as re-descriptions of the three | the facts established; reading them as the layer under GENESIS § 2 is **open** | W-F1 A2, A5 |
| 2 | **Their face.** Of the two pure faces, all mirrors and all half-turns, only all half-turns lets an aperiodic history run; its even part is the once-punctured torus | established within the move sequences computed (length up to four); the finiteness of the all-mirror face in full is a standard fact not computed; the two mixed faces are **open** | W-F2 |
| 3 | **The scar.** tr[x, y] = −2, which in the traces (X, Y, Z) = (tr x, tr y, tr xy) is Fricke's cubic X² + Y² + Z² = XYZ. Its point fixed by every move is the quaternion point, where the Pauli triple gives [x, y] = −I | the identities established; the quaternion point as the common point is the record's (W2) | W-F1 A2; the record |
| 4 | **The puncture.** The scar never heals. On a fibre cone point (sphere orders 4 to 12; every finite fibre order by hand) the record's sector modules cannot be formed, and a character's gap reduces to the invariant-vector term | **conditional**: strengthened if a chiral count is required; otherwise **chosen**. The odd sphere orders (3, 5, …) are not computed, and W-F1 counts them alive | W-F3 |
| 5 | **The act and the tick.** A hyperbolic word A; for the metallic acts, a tick J_m with J_m² = A_m and det −1. For odd m, J_m acts on the mark's line (m, 2) mod N by λ = m·2⁻¹, with λ² = −1, and K acts by −λ. Since λ ≠ ±1, the hand of ±J_mⁿKᵉ is (−1)ⁿ⁺ᵉ | the scalars and the hand law established for every odd m, by hand, with m = 1 to 11 computed; the normaliser as ±J_mⁿKᵉ found by search for m = 1 to 5 only, **open** beyond | W-C8 part 1 |
| 6 | **The slope.** s(χ) = u_χ(μ), with u_χ(λ) = 1, for characters trivial on μ | established on the orientable levels (B1438); the record's recipe cannot be formed on the non-orientable levels | the record; W-C8 part 2a |
| 7 | **The index.** I(V) = n(V) − n(V* ⊗ w), with twisted duality h²(V) = h¹_rel(V* ⊗ w) | duality established on levels 1 to 8: levels 1 and 2 from part 5, levels 3 to 8 from part 2a. The index is 0 on every doublet at golden levels 1, 3 and 5 (post hoc 2, not blind), and also at level 2. "Non-zero only on orientable levels" is **open** beyond the levels computed | W-C8 parts 2a and 5 |
| 8 | **Selection among metallic acts.** The bundle of LᵐP (the tick bundle) has H₁ torsion ℤ/m, and that of its square LᵐRᵐ (the metallic root) has (ℤ/m)². So SE1 (torsion-free) holds exactly at m = 1, the golden act | the facts are the record's (GENESIS § 4, the metallic-family paragraph; B126; T-ROOT); this note's S2 is the matching identity; SE1 itself is **chosen** (POSTULATED in GENESIS) | GENESIS § 4; this note, S2; W-C8 part 5 |
| 9 | **The orientation.** Of m004 and m000, take the orientable one | **chosen** (SE2) | GENESIS § 4 |

## 2. The data the page leaves free

| free datum | type |
|---|---|
| the sheet of the orientation cover (SE2); reading it as the records' hand is W-F1 § 2's reading | chosen |
| the order at the scar, V against V* | **open**. The SM seat's candidate system calls it the one free bit every route ends in; that is its reading, not checked here. W-F3 shows the frame's gaps need the puncture. It does not show that the open end fixes this order |
| three distinctions rather than more | chosen: the opposite, four or more, is alive (W-F1 A1) |
| the end parameter L̃ (B1921) | **open**, a continuous datum. B1921: "It removes no input"; L̃ "is as free as L was" |
| the point τ, unless an average over the weave replaces it | **open**. B1924 has made first runs of the read-out on the whole: OPEN, no limit proved, a second computation owed. This seat has not read it. The agy-exp lane's warnings on the measure (W-F3 § 5) stand until main says how B1924 orders the histories. This seat also derived by hand, without computing it: with the shift entering the lattice argument as (m + u₁)τ + (n + u₂), near a cusp where u₁ is an integer the Kronecker limit grows linearly in Im τ, which is not integrable against hyperbolic area. When the shift enters as a character instead, the m = 0 terms grow linearly for every shift |
| the frame itself, the identification of geometry with physics | **open**: unearned (GENESIS § 5) |

## 3. Main's tagged speculation (M19), tested

- **"The eigenvalue field of a hyperbolic act A equals ℚ(√N), N = det(A + I), exactly when tr A − 2 is a square (the
  metallic traces)."** It holds for every trace:
  - **Computed:** for every trace t from 3 to 20,000 (S1). The referee recomputed this independently with a different
    test.
  - **By hand, for t ≥ 3:** t² − 4 = (t − 2)(t + 2). So, when t + 2 is not a square, the fields agree exactly when t − 2
    is a square. For t − 2 = m² with m ≥ 1, t + 2 = m² + 4 is never a square, because (k − m)(k + m) = 4 forces m = 0.
  - **For t ≤ −3:** N < 0, so ℚ(√N) is imaginary. Both sides of the claim fail, and it still holds.
  - **The control** (t + 2 in place of t − 2) fails, but it is weak: it already fails at t = 3.
  - **The condition reads the trace only.** A trace of the form m² + 2 need not make A conjugate to A_m. For example,
    [[5, 4], [1, 1]] has trace 6 and is not conjugate to A₂.
- **"The tick acting as a square root of −1 mod N needs m odd."** It holds:
  - computed for m = 1 to 200 (S3);
  - for every m by hand: for even m, 4 divides N, and −1 is not a square mod 4.

## 4. The question: does any clause other than minimality make the golden act the only one?

- **On the metallic family, SE1 does.** This is the record's answer, not this note's finding. GENESIS § 4 already says
  that SE1 selects m = 1 there, and that SE1 is "one more selector of it, and, like the others, a chosen one". GENESIS
  also lists other selectors of m = 1 that are not minimality (B218, B224, B228, B251).
- **But on this family SE1 agrees with every minimality.** Least m, least trace and least torsion all pick m = 1.
  GENESIS also records a reading of SE1 as "the least remainder". Under that reading SE1 *is* a minimality.
- **So whether SE1 counts as a clause other than minimality depends on the reading.**
  - As GENESIS states it, SE1 is a vanishing condition, kept apart from minimality.
  - It differs from least trace only off the family: m003 against m004.
- **Where it shows in this seat's computations (part 5).**
  - **Alike for golden and bronze:**
    - the tick's mark and the hand law (part 1; computed for odd m ≤ 11, by hand for every odd m);
    - the free-cusp frame;
    - the bar on the record's sector modules at the tick's level;
    - twisted duality;
    - the cone point.
  - **Different:** the class-index frame at the root's own level. It is empty at the golden root, which is torsion-free,
    and fires at the bronze root.

## 5. Files

`relays/chat1_2026-11-14_wc8/`: `wc8_part4_checks.py` (sealed), `SCRIPT_SHA256_part4.txt`, `wc8_part4_out.txt`.

This note was read by one session before it was pushed, and its corrections are applied.

0 of 19.
