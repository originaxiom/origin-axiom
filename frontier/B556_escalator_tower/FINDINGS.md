# B556 — The Escalator Tower: T(M) = [[M, M],[M², M]]  (HYPOTHESIS + verified core)

Processes chat-2's "escalator" handoff verify-don't-trust. The computational
core is VERIFIED EXACTLY; the tower-as-physics-ladder reading is banked as a
labeled HYPOTHESIS so it is not lost or re-derived. Owner-directed: run the
escalator to its end and treat it seriously.

## VERIFIED FACTS (locked, tests/test_b556.py)

1. **T(F) = M₄ verbatim.** With F = [[1,1],[1,0]] (golden Fibonacci matrix),
   T(F) = [[F, F],[F², F]] EQUALS the σ₄ incidence matrix M₄ exactly (not up
   to permutation — literally). Same charpoly x⁴−2x³−5x²−4x−1. **This is
   B517's intertwining theorem** — B517 proved M₄ = [[F, C],[D, F]] with
   (C, D) = (F, F²) the golden-specific coupling; the escalator is that functor
   with C=M, D=M². So level 1 is a grounded FACT, not a coincidence.
2. **Rung 2:** T(M₄) is 8×8, charpoly degree 8 IRREDUCIBLE, Perron =
   10.724751772 (= β(1+√β), matching the self-similar law to all digits).
   √λ₂ ∉ ℚ(τ): the field genuinely doubles 4 → 8.
3. **The tower** (rungs 0–4): sizes 2,4,8,16,32; charpoly degrees 2,4,8,16,32,
   ALL irreducible; Perrons φ, 3.676, 10.725, 45.847, 356.28.
4. **The λ-law:** λ_{n+1} = λ_n(1+√λ_n) reproduces every Perron exactly
   (λ₀=φ). Each rung is the square-root extension of the previous Perron;
   field degree = 2^{n+1}.

## The closure (why coupling is the ONLY escalator)

Three alternative "climb" routes are closed:
- induction saturates in ℚ(τ) — BANKED (B533/B535 census saturation);
- the return-word flow has a fixed point (σ refines to itself) — BANKED (B540);
- covering functor non-escalating (13×13 lift, Perron unchanged) — chat-2's
  NEW claim, NOT independently verified here (needs their cover construction).
So (modulo the third) coupling via (M, M²) is the only degree-raising operation.

## THE HYPOTHESIS (labeled — not a claim)

> **One rule — couple X to itself through (X, X²) — applied to itself forever.
> Rung 0 = the golden layer (nature RELAXES into it: FK, circle maps, E₈'s φ).
> Rung 1 = the species layer (reachable only by BUILDING — the species chain,
> B543/B546, gap labels at 3.9×10⁻⁸). Rung 2+ = coupled layers no one has
> built, each naming its field (degree 2^{n+1}), its Perron (the λ-law), and a
> buildable Hamiltonian (an 8-coupling chain at rung 2 whose gap labels would
> live in the degree-8 field).** The rule is the origin gesture (a → a·a²)
> operating on whole systems instead of letters.

Physics contact so far: rung 0 confirmed (universality: E₈, gap labels), rung 1
built (the species chain). Rung 2 is the next experiment candidate BEHIND the
species chain — an 8-letter substitution carrier realizing T(M₄).

## HONEST BOUNDARIES (so this stays trustworthy)

- Rung 0→1 (T(F)=M₄) is a FACT (B517).
- The iteration rule T at rung ≥ 2 is the CANONICAL self-similar continuation
  — natural and exact, but a **CHOICE** (other couplings are conceivable).
  Under this rule the rung-2 field-doubling is a COMPUTED FACT, not a
  conjecture. Stated as such.
- The physics-ladder reading is HYPOTHESIS; each rung carries a falsifiable
  membership test (its field) and a device (its chain) — that is what keeps it
  from regress mysticism, but it is not banked as physics.
- **Lit-gate MANDATORY before novelty language:** coupled / graph-directed
  substitutions, block-matrix Pisot towers, and self-similar substitution
  hierarchies have a literature (Queffélec; Fogg; graph-directed IFS;
  Frank–Sadun fusion). Queue on the cost-tiered script before claiming the
  functor or the tower is new.

## Next steps (recorded so we don't re-derive)
1. Write the explicit rung-2 8-letter substitution carrier (chat-2: images
   σ₄(j)₁·σ₄²(j)₂), verify its incidence = T(M₄), and add to the experiment
   ladder behind B555.
2. Lit-gate the functor + tower.
3. Verify (or refute) the covers-non-escalating closure claim (needs the lift).

Locks: tests/test_b556.py.
