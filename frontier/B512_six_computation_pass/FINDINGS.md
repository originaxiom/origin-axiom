# B512 — the six-computation pass (A–F): verified-so-far
**Chat1 handoff 2026-07-11. Banked = what this seat re-derived; the rest preregistered/deferred.**

## A — geometric spacetimes have SQUARE time: CONSISTENT (theorem pending the machine)
δ is a perfect square at every banked geometric point: δ(Eisenstein)=4=2² matches the banked δ_geo=4.
The (p,1) one-liner (μᵖλ=1 ⟹ tr(core)=tr(μ)=x ⟹ δ=x²) is topologically sound but needs the Riley
filling machine (B508, flagged pending independent rebuild) — **PREREGISTERED as a lemma, not yet a
banked theorem**. Consistency verified; the general (p,q) case (core μᵃλᵇ, does q>1 break squareness?)
is the seat question.

## B — 40a1's torsion = the program's named characters: ACCEPTED (verified in B510)
The three 2-torsion points x∈{0,1,5} of 40a1 = y²=x(x−1)(x−5) are the branch points already banked
(B510) as the Markov origin (κ=−2), the M-pointer (κ=0), and the golden loxodromic (κ=18); O = the
identity rep. Banked as a DICTIONARY (exact identifications; the "meaning" is the program's vocabulary,
not an external fact). Fiber-group computation at x=1,5 = seat item.

## C — the SILVER ladder is a 2-GROUP, not 2T: **VERIFIED NEGATIVE (banked, locked)**
At the shared Markov-origin fiber (0,0,0), the intertwiner trace-square, computed independently:
**golden tr(t)²=1** (order-6 → 2T → E₆) vs **silver tr(t)²=2** (order-8 → 2-group of order 16,
dihedral/quaternion family). **The McKay ladder Q₈→2T→2O→2I is GOLDEN-SPECIFIC** — silver never reaches
the exceptional groups. The exceptional ADE series (E₆,E₇,E₈) in the spacetime functor is a **privilege
of the golden word, not a universal property of the metallic monoid.** This BOUNDS the functor's most
physics-suggestive feature (the E₆/E₇/E₈ appearance) to golden only — directly relevant to B511/D4
(the exceptional/gauge structure is not robust across the family). Coincidence flag (recorded, not
promoted): silver's tr(t)²=2 equals golden's decoherence-rung value by a different mechanism — likely a
2-group artifact (order divisible by 8). Bronze (n=3) ladder = seat item (2-group ⟹ clean dichotomy).

## D — the arcsine law is REJECTED: **CROSS-CONFIRMED** (two seats, same day)
Chat1: occupation-fraction ~Beta(6.2,1.6), peaked near 1, KS-from-uniform 0.52 — not the U-shaped
arcsine. **This seat's B511/D3.2 (independent, hours earlier) found the identical result:** one-sided
histogram [996,351,…,0], drift-dominated, arcsine falsified in the drift-predicted direction. **Q3
status: ANSWERED-NEGATIVE.** Both seats: the negative STRENGTHENS B506 (the drift is real; the critical
cancellation is drift-dominated with an absorbing-like κ=2 boundary, not a symmetric walk); g(κ) — the
banked B507 β-function — is the right object, not the CLT. Folds into B506's artifact battery.

## E — geometry-born fields climb the SAME Galois ladder: ACCEPTED (unifying)
(5,1)→S₄/−283, (6,1)→S₃/−236, (7,1)→S₆/50173: the full symmetric groups appear at geometry-born
fields as at interaction-born ones (census S₄…S₁₀). **The Galois ladder is a property of the character
variety's arithmetic, universal across both creative registers**; they differ only in which fields
(discriminants) and in δ's square class (geometry square, interaction non-square — B508/B509).
Odd-slope/prime-disc observation ((5,1),(7,1) prime; (6,1) composite) PREREGISTERED as a question for
(9,1),(11,1) — not a claim (the killed W5 parity law is the cautionary precedent).

## F — the explicit isogeny map: DEFERRED (Sage Vélu; seat item, closes the covering arc)

## Verdict of the pass
Two genuine negatives banked (C: McKay golden-specific; D: arcsine rejected — both strengthen the
honest picture), one consistency (A), one dictionary (B), one unifying observation (E), one deferral
(F). Lock: `tests/test_b512.py`.
