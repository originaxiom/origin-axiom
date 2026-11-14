# W-F5: the puncture is not a separate input. A cone point is a relation among the three distinctions, which line 1 excludes; every such relation kills a line of the system; and on line 3's cubic the scar has finite order only at the common point

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free), by hand with computed checks.
This note closes card W-F5 (`relays/cards/CHAT1_W-F5_the_cone_point_is_a_relation_among_the_distinctions.md`,
e65cee8a6).

**How it was checked.** Argued by hand for every K; not independently checked. Computed once, on this seat's own code; expectations committed first.
- **The sealed run.** The script (sha256 `09d3e0a4…49fa7d5`, pushed at e65cee8a6) was run once; its output was
  committed (5a79bd051) before it was read. All five expectations were met as coded.
- **Method:**
  - F3 used exact ranks over two prime fields (1000003 and 998244353), and the two give the same counts;
  - F4 and F5 used 40-digit arithmetic;
  - the Fox-calculus helpers are W-C8 part 2a's, taken by text.
- **Two controls registered where something exists:** F3's class on the scar at K = ∞, and F4's finite orders on the
  cone level sets.

## 1. The results

O_K = ⟨a, b, c | a², b², c², (abc)^K⟩; K = ∞ is W₃, the three distinctions with no relations. A fibre cone point of
order k (W-F3) is K = 2k, since aλa = (abc)⁻² (W-F1 A2).

| line | result |
|---|---|
| F1 | H₁(O_K) is (ℤ/2)³ for K even and K = ∞, and **(ℤ/2)² for K odd** (K = 2 to 13). **The parity character (each distinction ↦ −1) exists exactly for K even or ∞** |
| F2 | In W₃, (abc)² = x(xy)⁻¹y. So for odd K, abc = ((abc)²)^((1−K)/2) lies in ⟨x, y⟩, and with it c = x⁻¹(abc) and a = (abc)y⁻¹. **The records generate all of O_K: the split of the distinctions into records, an even part of index 2, is lost** |
| F3 | **For every finite K = 2 to 13 and every character, no class is non-zero on the scar.** For odd K there is **no class at all** (H¹(O_K; χ) = 0 for all 4 characters). For even K, 2 classes, both of the parity character and both zero on λ (their value on abc is not defined on classes, since χ(abc) = −1 and a coboundary takes −2 there). At K = ∞, 5 classes, 3 of them non-zero on λ; the class c = (1, 0, 0) for χ = (−1, −1, 1) has c(λ) = 2, as derived by hand |
| F4 | On 2,000 random points of Fricke's cubic X² + Y² + Z² = XYZ (line 3: tr[x, y] = −2), [x, y] + I is a non-zero nilpotent: max \|tr[x, y] + 2\| is 2·10⁻³⁶, and \|[x, y]ⁿ − I\| ≥ 0.74 for n = 1 to 24. **At the origin, [x, y] = −I.** Control: on the cone level sets tr[x, y] = −2 cos(π/k), k = 2 to 6 (200 points each), [x, y]^(2k) = I |
| F5 | At the common point λ = −I, so λᵏ = I in SL(2, ℂ) **exactly for even k** (k = 1 to 12); in PSL(2, ℂ), λ = 1 |

## 2. By hand, for every K

- **A cone point is a relation among the distinctions.** λᵏ = 1 holds exactly when (abc)^(2k) = 1, because
  aλa = (abc)⁻². The three distinctions "with no relations among them" (line 1 of W-C8 part 4's page) exclude it.
- **For odd K:**
  - The relation K(a + b + c) has odd coefficients, so the parity character does not factor through it (F1).
  - F2's identity uses only (abc)^K = 1.
  - Every character has χ(abc) = ±1 with χ(abc)^K = 1, so χ(abc) = 1. Then the relator gives K·c(abc) = 0, so
    c(abc) = 0 (characteristic prime to K).
- **For every finite K,** c(λ) = χ(a)·c((abc)⁻²) = −χ(a)(1 + χ(abc))·c(abc). This is 0 when χ(abc) = −1. When
  χ(abc) = 1 it is 0 because K·c(abc) = 0.
- **On line 3's cubic:**
  - If [x, y] has finite order, it is diagonalisable with roots of unity ζ, ζ⁻¹ as eigenvalues. Then tr = −2 forces
    ζ = −1, so [x, y] = −I.
  - Then xy = −yx, which forces tr x = tr y = tr xy = 0: the origin, the common point.
  - Everywhere else on the cubic, [x, y] is −I times a non-trivial unipotent, so it has infinite order.
  - The cone points' level sets, tr[x, y] = −2 cos(π/k), are other cubics. Off the common point, choosing line 3's
    cubic is choosing the puncture.
- **Counting.**
  - The trivial character has no class, since H₁ is 2-torsion.
  - For a character with two −1's, the cocycles on those two generators form a plane. At finite K, where
    χ(abc) = 1, it is cut to the coboundary line, so there is no class. At K = ∞ it is left whole: one class, with
    c(λ) = −2χ(a)c(abc) ≠ 0.
  - A character with one −1 has no class.
  - The parity character, when it exists, has 3 − 1 = 2 classes.

## 3. What it means for the system

- **Line 4 (the puncture) is no longer a separate input.** It is contained in line 1, and it follows from line 3 off
  the common point. The opposite of line 4 is a relation (abc)^K = 1 among the distinctions, and every such relation
  kills a line of the system:
  - **odd K:** the parity character dies, the records stop being an even part of index 2 (line 1), and no class exists
    at all;
  - **even K:** the records stop being free ([x, y]^(K/2) = 1, line 1), and the frame's matter dies: no class on the
    scar here; W-F3 and W-F4 for the 3-dimensional objects, oriented or not.
  - At even K the records' loss of freeness is the relation restated, so it is no independent reason. The reason the
    counterexamples give for line 1's "no relations" on abc is that the classes on the scar die. That holds on the
    face for every finite K (here), and on the 3-dimensional objects at even K (W-F3, W-F4). At odd K the parity
    split dies as well. Relations on other words (the triangle faces, (ab)ᵏ = 1 and the like) are W-F7's.
- **The common point is the one exception, and it is the record's distinguished point.**
  - There the scar heals in two steps ([x, y]² = I). That is compatible with every even fibre cone order, and in
    PSL(2, ℂ) with the closed torus.
  - So nothing computed at the common point alone can tell the puncture from an even cone point. W-F1's hand at the
    common point is blind to the puncture.
  - The puncture is forced by line 3 only away from that point.
- **For the page (W-C8 part 4, § 1):**
  - line 4 moves from "conditional" to "derived from line 1 (and from line 3 off the common point)";
  - line 1's "no relations on abc" moves from stated to justified by counterexamples. Every relation (abc)^K kills
    the classes on the scar, and at odd K the parity split too; W-F3 and W-F4 cover the 3-dimensional objects at
    even K;
  - line 1's reading as the layer under GENESIS § 2 stays open.

## 4. Typed

| statement | how checked |
|---|---|
| F1 to F5 on the K, points and orders named | computed once; expectations committed first; F3 in two prime fields, F4 and F5 in 40 digits |
| F1 to F3 for every K (over a field of characteristic prime to 2K) | not independently checked (by hand) |
| on Fricke's cubic, finite order only at the origin | not independently checked (by hand); computed once on 2,000 points |
| line 4 is contained in line 1, and implied by line 3 off the common point | not independently checked (by hand) |
| every relation (abc)^K kills a line of the system | for odd K and for the face's classes: not independently checked (by hand), and computed once for K up to 13. For the 3-dimensional objects at even K: W-F3 and W-F4 (fibre orders 2 to 6 computed once; every order not independently checked (by hand)) |
| the common point cannot tell the puncture from an even cone point | not independently checked (by hand); computed once (F5) |

## 5. Not computed

- Relations on words other than powers of abc (W-F7).
- The 3-dimensional orbifolds at odd K, built with the tick's lift to W₃. Their classes restrict to zero on the face
  (H¹(O_K; χ) = 0 for every character, and, by the long exact sequence, for modules built from characters), so none
  is non-zero on λ. The classes themselves are not computed.

## 6. Files

`relays/chat1_2026-11-14_wf5/`: `wf5_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf5_checks_out.txt`,
`wf5_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied. The referee also recomputed
F1, F3 (over ℚ, at K = 3, 4, 5 and ∞), F4 and F5 independently on its own code; the numbers agree.

0 of 19.
