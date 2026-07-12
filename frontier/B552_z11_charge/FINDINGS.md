# B552 — The ℤ/11 conserved charge on the observer flow (chat-2 cell, verified)

From the FRONTIER_CAMPAIGN_CELL1 charge-transport artifact (chat-2), verified
here exactly (`verify.py`).

## The base charge

coker(I − M) ≅ **ℤ/11**: SNF(I − M) = diag(1,1,1,11) (VERIFIED). A primitive
left generator over 𝔽₁₁, in letter order (a,b,A,B), is
  **χ = (1, 3, 6, 7) mod 11,   χM ≡ χ.**
Every substitution image carries its source's charge (VERIFIED):
  Q(abAAB)=1+3+6+6+7≡1=Q(a); Q(aAB)=1+6+7≡3=Q(b);
  Q(abAB)=1+3+6+7≡6=Q(A); Q(aA)=1+6≡7=Q(B).

## Transport across the whole observer flow (B540's 12 nodes)

chat-2's claim: for every observer incidence matrix A_u of the 12-node flow,
SNF(I − A_u) = diag(1,…,1,11), so every node carries the SAME ℤ/11 torsion
type, and the return-word Parikh maps transport the charge along every flow
edge (A_s P = P A_t). Reproduced here for the census systems; the full
12-node sweep is chat-2's computation, consistent with B540's flow.

## Reading (firewalled)

A single ℤ/11 invariant is conserved by σ and preserved across every way of
observing the object — a conserved "charge" of the substitution, transported
unchanged through the observer flow. Pure algebra (Smith normal form over ℤ);
nothing to CLAIMS as physics. The 11 is disc-adjacent (disc = −400; 11 is the
first prime where the charpoly x⁴−2x³−5x²−4x−1 has a specific factorization
type — noted, not interpreted). Locks: tests/test_b552.py.

## Addendum (B553): charge–clock decoupling

The double-clock 2-cycle of the observer flow (B540) has TRIVIAL ℤ/11
holonomy (= 1 mod 11): the charge space is 1-dimensional at every node, so any
node-preserving holonomy scales χ by a unit and acts as the identity on the
charge line. The conserved charge does NOT couple to the clock — two
independent structures on the same object.
