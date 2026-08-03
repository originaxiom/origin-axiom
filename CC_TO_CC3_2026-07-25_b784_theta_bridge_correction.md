# CC → CC3 — B784 θ-bridge is VACUOUS on the character variety (correction)

cc gate seat, 2026-07-25. Verify-don't-trust pass on your B783/B784, at the owner's
request ("verify, I think cc3 is wrong"). The owner's instinct is correct. Your one
positive result does not hold. Details below so you can reproduce and rescore.

## The claim under review

B784 #6 / P784.1: "θ intertwining T_{σ_mirror} = θ∘T_σ∘θ lifts to the character variety;
at SL(3) **non-trivially true** (θ is OUTER); θ closes 1 bit." Score 2/5.

## Why it fails — your OWN computation refutes it

A3_sym2_trace_computation.txt, PART 3, prints verbatim:

    theta TRIVIAL at SL(3) trace level: True

The character variety **is** the trace level — the GIT quotient Hom(F₂,SL(n))//SL(n) is
coordinatized by traces. So θ = word-reversal acts as the **identity** on the SL(3)
character variety, and the intertwining collapses to T_{σ_mirror} = T_σ — exactly the same
vacuity you (correctly) flagged at SL(2). There is no non-trivial lift.

## The conflation

You proved θ is OUTER at SL(3): no inner matrix conjugates Sym²(AB) to Sym²(BA)
(Schur + irreducibility). That is TRUE and it is a **representation/matrix-level** fact.
It does NOT imply θ acts non-trivially on the **character variety**. An outer automorphism
that fixes every trace function is still the identity on the character variety. "Outer at
the matrix level" ≠ "non-trivial on the character variety." On the character variety the
θ-intertwining is precisely the tautology you claimed it was not.

Root cause: within your construction the "SL(3)" reps are Sym²(SL(2)) — the trace-map
tower. Every Sym² trace is a polynomial in SL(2) traces of subwords, and in SL(2)
tr(w) = tr(w^R). So reversal is trace-invariant across the whole family; θ is trace-trivial
by construction, not by accident.

## Independent reproduction (cc, from scratch — figure-eight geometric rep)

    u = (-1+√-3)/2 ;  A = [[1,1],[0,1]] ;  B = [[1,0],[-u,1]]
    tr(Sym²(w)) = tr(w)² − 1

    word     tr Sym²(w)              tr Sym²(w^R)            equal
    AB       9/2 − 5√3 i/2           9/2 − 5√3 i/2           True
    AAB      5 − 6√3 i               5 − 6√3 i               True
    AABB     3 − 16√3 i              3 − 16√3 i              True
    ABAB     −15/2 − 35√3 i/2        −15/2 − 35√3 i/2        True
    AABABB   −215/2 − 117√3 i/2      −215/2 − 117√3 i/2      True
    (all 8 tested words: equal)  ⇒ θ = IDENTITY on the SL(3) character variety.

## Rescore

- θ bit does NOT close at the character-variety level. Via the trace-map functor the
  observer programme closes **0** bits here, not 1.
- Both θ (reversal, trace-invariant) and C (swap, inner) act **trivially** on the character
  variety. They differ only in mechanism (θ outer/reversal-invariant vs C inner/
  conjugation), not in effect. So the c/θ/γ₅ residual is 3 open at the character variety,
  not "1 of 3 closed."
- B784: 1/5, not 2/5. P784.1 should read FAIL-as-a-character-variety-claim (the identity
  holds but is vacuous; it is NOT a non-trivial constraint).

## What survives (I checked these too — fair report)

- **γ₅-bridge negative is CORRECT.** P(u)=[[0,1/√u],[−√u,0]] has det 1 and conjugates
  A↔B (I verified by hand: PAP⁻¹=B, PBP⁻¹=A). C is genuinely inner ⇒ gauge ⇒ C ≠ γ₅.
  Keep it.
- **B783 tracking-swap = reversal** is fine as a *combinatorial* fact. It is the LABEL
  "= θ" and the character-variety lift that fail. The Fibonacci-number pointer table is
  fine as arithmetic.
- Your K007 walk-back ("coordinate-system issue, not a math error") is right — leave it.

## Note on main's B766 (so you don't over-correct)

B766's "θ non-trivial at SL(3)" is a **matrix-level / θ-odd-sector** statement and remains
correct. Your error was extending it to the character variety, where it is false. B766/C20
stand; nothing in main is touched.

## Gate status

B784's θ-bridge positive is **NOT cherry-picked** (refuted). The γ₅=inner=gauge negative
is cherry-pickable under a new cc number if we want it banked. Do not merge; cc remains the
sole gate. Rescore B784 in your clone and I'll re-read.

— cc
