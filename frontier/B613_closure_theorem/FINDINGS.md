# B613 — THE CLOSURE THEOREM: the pairing layer is now a theorem

**Status: banked (frontier). Nothing to `CLAIMS.md` yet (candidate for
promotion at the next review — the proof is modular-data-axiomatic with
an exact verification suite). Lock `tests/test_b613_closure_theorem.py`
(fast, ~30 s). Run: `python3 closure_theorem.py`.**

## THE THEOREM

> Let (S, T) be modular data with S symmetric unitary, T diagonal
> unitary, C = charge conjugation with [C, T] = 0 and S² = ζC (a scalar
> phase; hence [S, C] = 0). Put R = T, L = S⁻¹T⁻¹S, and for a weld word
> w let W = ρ(w). If w is GHH-ANTI-PALINDROMIC (⟺ the once-punctured-
> torus bundle is AMPHICHIRAL, by B134/V123), then
>
>     conj(W) = Q⁻¹ Wᵀ Q,   Q = P·S·C,
>
> where P is the cyclic-rotation prefix realizing swap(w) = σ(rev(w)).
> Q commutes with C, hence preserves the odd space, and therefore the
> odd hearing spectrum is CONJUGATION-CLOSED AT EVERY LEVEL.

## The proof (three ingredients from the axioms)

- **I1:** conj(X) = C X⁻¹ C for X ∈ {R, L}. (R: conj(T) = T⁻¹ and
  [C,T] = 0. L: conj(L) = S T S⁻¹ since S̄ = S⁻¹; and C L⁻¹ C =
  S²(S⁻¹TS)S⁻² up to the ζ-phases which cancel in conjugation.)
  Hence conj(W) = C·(W_rev)⁻¹·C.
- **I2:** ρ(swap(x)) = S ρ(x)⁻¹ S⁻¹ (the S-conjugation swaps R ↔ L⁻¹;
  both directions verified). Hence (W_rev)⁻¹ = S⁻¹·ρ(swap(w))·S (same
  letter order).
- **I3:** R and L are SYMMETRIC (Lᵀ = L again by [C,T] = 0 through the
  ζ-cancelling conjugation), hence ρ(rev(u)) = ρ(u)ᵀ.
- Assembly: anti-palindromicity gives swap(w) = σ(rev(w)) with prefix P,
  so ρ(swap(w)) = P⁻¹ Wᵀ P, and conj(W) = C S⁻¹ P⁻¹ Wᵀ P S C = Q⁻¹WᵀQ.
  spec(Wᵀ) = spec(W), and Q preserves the C-grading. ∎

## The verification suite (all exact-numerical at 1e-11/1e-9)

Four levels (κ = 5, 7, 10, 12) × [the axioms incl. S² = ζC with the
phase computed; I1, I2, I3] all pass; the assembled identity holds for
all four amphichiral witnesses (RL, RRLL, RLRL, RRRLLL — each has
swap(w) = rev(w), so P = I, Q = SC) — 16/16; the three chiral controls
fail the identity with this Q — 12/12 (consistency; the theorem is
one-way: the CONVERSE — level-uniform closure ⇒ amphichiral — remains
empirical, supported 3/3 with B612's isolated accidental closures at
single levels).

## What this closes

B610's mechanism candidate and B611/B612's two refinement deaths resolve
into a proved statement: **the pairing layer of the hearing structure is
the object's amphichirality, as a theorem.** The three-layer picture now
reads: spectrum pairing = chirality (THEOREM, one direction), trace =
field (B601/B610 laws, empirical-exact), matrix elements = the
listener's coupling (the banked hearing laws).
