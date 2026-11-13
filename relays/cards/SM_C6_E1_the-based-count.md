# SM-C6 E1 — the based count: the instrument of lead L241 (b), on the steps where the record says the order is dropped

*Step card of SM-C6 (main's M13, M14, M18; SM-C5's entry E1 for GENESIS FK12 (i)). Committed and pushed before the
run. Main at 663a902ff. Data-free.*

## The definition (committed first, as M13 asks)

- **The objects.** On a level of a signed word state, a sector module is V(ℓ, α) = [[α, cβ], [0, β]], with
  β = α/ℓ and c the class of H¹(G; ℓ). ℓ, α and β are non-trivial characters fixed by the monodromy (B1438).
- **The two orders.** V has α as its sub. Its dual V* ≅ V(ℓ, β⁻¹) has the other piece, β⁻¹, as its sub (B1438 A).
- **The based count** of V is the ordered pair (n(V), n(V*)). By B1438 A:
  - n(V) = [s(α) = s(ℓ)];
  - n(V*) = [s(β⁻¹) = s(ℓ)];
  - s is the slope, computed exactly in the cyclotomic field by B1438's own exact_slopes.
- **What it reads that the class count does not.** The class count is I = n(V) − n(V*). The based count keeps which
  order fires. On the entries (1, 1) the class count reads 0 and the based count reads 1 in each order: the "both at
  once" that B1466 found at one point.
- **The marking is an input to the instrument.** The test asks whether a step's output depends on the marking, never
  whether the marking is there.

## The steps, and what is computed at each

1. **Word → manifold (the letters' order).** For every word w whose reverse w̄ is not a rotation of it (lengths 6 and 7,
   both signs, levels 1 and 2), at the same level:
   - **(a) labelled:** whether the based-count function on the coordinate pairs (ℓ, α) is the same for w and w̄;
   - **(b) unlabelled:** whether the multiset of based counts, the census of (n, n*), is the same.
2. **Module → vacuum (the pieces' order).** On every level of 1 and on B1438's census levels:
   - the census of (n, n*) over all sector modules;
   - the share of (1, 1);
   - for the split module α ⊕ β, the based count is symmetric by construction, since neither piece is the sub. Stated,
     not computed.
3. **The read-out on the whole (B1881, B1895)** is not run here. It needs the whole's read-out instrument, and stays
   owed.
4. **The audit lane's criterion** (updates and declared outputs descend) is not re-derived here, and stays owed.

## The three expected outcomes (SM-C5 E1's), and the prediction

- **Outcome 1 (predicted):**
  - (a) differs on at least one pair and (b) agrees on every pair: the letters' order is visible in coordinates and
    dropped at the manifold, exactly where B1456 says;
  - the pieces' order is kept by the based count and lost to the class count wherever (1, 1) occurs. So the register
    of the pieces is a marking that the class count does not keep.
- **Outcome 2:** (b) differs on some pair. The based count tells a word from its reverse after the manifold step: the
  register is part of the state at the manifold, against B1456's reading.
- **Outcome 3:** (a) agrees on every pair. The letters' order is invisible to the instrument even in coordinates, so the
  word → manifold drop is empty for it.
- **Controls, which must fail:**
  - **P1:** the slope of α replaced by that of β. The census must change on at least one level.
  - **P2:** a word paired with an unrelated word of the same length in place of its reverse. (b) must differ on at least
    one pair.
