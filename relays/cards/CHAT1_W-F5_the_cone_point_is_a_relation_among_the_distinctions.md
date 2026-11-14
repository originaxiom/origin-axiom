# Card W-F5: the cone point is a relation among the distinctions; the odd sphere orders; where the scar can heal

**Seat:** the web seat (chat1). **Kind:** `result:` (data-free), mostly by hand, with computed checks. **Committed
before any work of it.** It serves the foundations' goal (status file, ruling of 2026-11-14).

## Why this card

- W-F3 left the odd sphere orders K = 3, 5, … of S²(2, 2, 2, K) uncomputed, since they have no torus double cover.
- W-C8 part 4's page types line 4 (the puncture) as conditional on a chiral count. It types line 1 (three distinctions
  with no relations) and line 3 (the scar, tr[x, y] = −2) separately.
- The question here: are lines 1, 3 and 4 independent inputs? Or does the puncture follow from the others, and where
  does it fail to?

## The questions

1. A cone point of order K at the product of the three distinctions is the relation (abc)^K = 1. For odd K, does the
   parity character (each distinction ↦ −1) survive? Do the records x = ab and y = bc still form a subgroup of index
   2? Can any class be non-zero on the scar?
2. Does "no relations among the distinctions" (line 1) already contain the puncture (line 4)?
3. On line 3's cubic, X² + Y² + Z² = XYZ (tr[x, y] = −2), at which points can the scar [x, y] have finite order, so
   that a cone point is compatible?

## Method

- By hand, with these computed checks:
  - the abelianisation of O_K = ⟨a, b, c | a², b², c², (abc)^K⟩ for K = 2 to 13 (Smith form);
  - the word identity behind question 1 in W₃;
  - H¹(O_K; χ) over a prime field for every character at odd K = 3 to 11, with each class's value on abc;
  - random points of the cubic in SL(2, ℂ), with a control on the cone level sets tr[x, y] = −2 cos(π/k).
- Expectations in the script's header, sha256 recorded, committed and pushed before the one run.

## Not in scope

Relations other than powers of abc (the triangle-group faces belong to W-F7). Any frame value or measured datum.
