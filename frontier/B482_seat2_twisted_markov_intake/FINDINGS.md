# B482 — intake/verification of seat-2's twisted-Markov-spectrum handoff (2026-07-08)

**Verify-don't-trust pass on the incoming handoff. Nothing banked as novelty (lit-gate W0
governs that). Math verdicts below; the two items that touch the paper (A2, B3) verified in
full, the spinoff arithmetic (A1/A3/A4/A5) recorded as novelty-BLOCKED pending W0, and the
B1 "banked error" claim flagged as a DISCREPANCY, not applied.**

## VERIFIED — and directly strengthens P4 (the metallic-family paper)
- **A2 Two-Teeth (headline).** The twisted (det −1) Markov spectrum ∩ (0,3) = {√5, 2√2} =
  {μ(X₁), μ(X₂)} — golden and silver, nothing else. Spot-verified: the negative-Pell
  filter v² − D_m t² = −4 (D_m = 9m²−4) is solvable only for m = 1 (odd branch) and m = 2
  (content-2 branch); all Markov m ≥ 3 up to 5741 give unit norm +1 → fail. Matches
  seat-2's machine-check (m ≤ 20000). **This is a SECOND, independent characterization of
  the (1,2) critical pair** — spectral/Pell, unrelated to the commutator polynomial that
  singles it out in P4. Value to P4: the paper's central object is now distinguished by two
  unrelated invariants. **Novelty UNVERIFIED — lit-gate (Cusick–Flahive; Sarnak reciprocal
  geodesics; non-orientable spectrum lit) before any priority claim.**
- **B3 Unified symmetric-pair commutator.** tr[A,B] = 2 − gap²/(det A·det B) for symmetric
  A,B of ANY determinant (gap = M₁₂−M₂₁, M = AB). VERIFIED symbolically. This GENERALIZES
  P4's Lemma 2.2 (the det +1 case, bodies A_m, gap = mn(n−m)) and unifies it with the
  det −1 letters (X_m, gap = m−n) as one mechanism. Value to P4: Lemma 2.2 becomes a
  special case; the transpose mechanism is one law across both parities.
- **A6 gcd + indefinite Hurwitz.** (1, d, d²+1) solves z²−x²−y² = d·xyz for every d ≥ 1
  (VERIFIED symbolically) — contrast the classical definite Hurwitz (only d ∈ {1,3}). gcd
  Vieta-invariance is one line. Clean spinoff result.

## RECORDED — spinoff arithmetic, novelty BLOCKED pending W0 lit-gate
A1 (Descent Lemma), A3 (level trichotomy + N-law, two open cells c ∈ {28,40}), A4 (five
certified integral Hasse failures c ∈ {−14,2,6,22,26}), A5 (realizability invariant +
phantoms at c = 28). The PROOFS are elementary and machine-checked (seat-2); the MATH is
sound. But A4/A5 carry **HIGH prior-art collision risk** (Ghosh–Sarnak for Hasse failures;
Bourgain–Gamburd–Sarnak / Loughran–Mitankin for the lifting/strong-approx phenomena behind
phantoms). Per seat-2's own Part E: these belong to a **standalone non-orientable Markoff
arithmetic paper, a spinoff asset, NOT the origin spine** — and no novelty language until
W0 clears. Recorded here as intake; not banked as results.

## FLAGGED — B1 "banked λ error": DISCREPANCY, not applied
Seat-2 claims banked λ_chain = 2.1775291199 is wrong from digit 7 (true spine
2.177528751053). **But the repo's banked λ_chain = 1.57705744122666946** (P4 drafts,
CLAIMS.md, registry) — a DIFFERENT number. Seat-2's value (2.1775…) does not appear in the
repo. So the numerical correction cannot be applied blindly: it targets a value that is not
what is banked (their λ_spine ≠ the repo's per-letter λ_chain; registry records a
λ_CC = λ_Chat2^φ relation between the two families). **The METHODOLOGICAL half of B1 is
already done:** P4 v6 + registry line 60 already use height-bounded-exclusion language and
dropped "non-algebraic to degree N" (the P4 panel caught it). Action: reconcile the two λ
families before any re-bank; do NOT overwrite the banked value on seat-2's number alone.

## Firewall
Seat-2 confirms (Part E): nothing here crosses math→physics. A2's golden–silver convergence
is a THIRD mathematical characterization of an already-special pair — interpretive, NOT
evidence for any physics thesis. Firewall intact. Reproducers: `verify_seat2.py`
(A2 Pell filter, B3 symbolic, A6 Hurwitz).
