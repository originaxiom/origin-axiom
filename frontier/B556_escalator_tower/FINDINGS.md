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

## PROOF UPGRADE (chat-2 audit, verified 2026-07-12): the doubling is a THEOREM

B556 banked the field-doubling from numerics. It is now PROVED exactly (three
verified misses from the chat-2 audit):

**Miss A — the norm-sign argument (rung 2, one line):** β (the rung-1 Perron)
has N(β) = product of the quartic's roots = **−1 < 0** (the constant term of
x⁴−2x³−5x²−4x−1). A square y² ∈ ℚ(τ) has N(y²) = N(y)² ≥ 0. Contradiction ⟹
√β ∉ ℚ(τ) ⟹ the field DOUBLES at rung 2. (At rung 2 the SIGN does the work;
higher rungs also fail by magnitude.)

**Miss B — the determinant telescope (all rungs):** for the commuting-block
escalator, det T(M) = det(M²−M³) = det(M)²·det(I−M), so
  **dₙ₊₁ = dₙ²·eₙ,  eₙ := det(I−Mₙ)** — verified exactly through rung 4:
  dₙ = −1, −1, −11, −97889, −1.8×10¹⁷;  eₙ = −1, −11, −809, −18845089, −2.3×10²⁰.
**Every eₙ is NEGATIVE (verified rungs 0–4)**, so the norm-sign proof of Miss A
fires at EVERY rung: field-doubling is PROVED at rungs 1→2→3→4→5. The all-n
tower now rests on exactly TWO clean, per-rung-checkable conjectures:
irreducibility (CC-verified 0–4) and negativity of eₙ (verified 0–4). The
"hypothesis" acquired an exact per-rung engine.

**Miss C — the charge tower (the ℤ/11 governs the tower):** e₁ = det(I−M₄) =
**−11 = the B552 base charge** (coker(I−M₄) = ℤ/11). By the telescope, every
rung's determinant is built from the eₖ below. The **charge tower**
|eₙ| = **1, 11, 809, 18845089, 228654672055316545291** (809 and 18845089 prime;
e₄ = 11²·1459·597049·2169349081), and **coker(I−Mₙ) = ℤ/|eₙ| is CYCLIC at every
verified rung** (SNF: a single non-trivial invariant factor). B552's isolated
ℤ/11 is the foundation stone of this second sequence.

## Cover-closure spec logged (for B557 E4)
chat-2 supplied the cover construction for the closure leg I flagged unverified:
M-invariant mod-2 plane basis χ₁=(0,1,1,0), χ₂=(1,0,1,1) on (a,b,A,B); cosets =
F₂²; BFS Schreier transversal; 13 generators (16 (coset,letter) pairs − 3 tree
edges); abelianized lift column (c,g) = R(c) + scan(φ(g), start c) − R(c+χ(g)),
R(c)=scan of φ(rep_c) from 0. Expected: charpoly degrees (2)(4)(7), Perron = β
unchanged (non-escalating). Verification deferred to B557 E4 (closure cell).

## NEW (2026-07-12): ONE fixed cubic generates the whole charge tower

The charge tower eₙ = det(I−Mₙ) is generated by a SINGLE fixed cubic applied
multiplicatively over each rung's spectrum:
  **eₙ₊₁ = ∏_{λ ∈ spec(Mₙ)} (1 − 2λ + λ² − λ³) = det(I − 2Mₙ + Mₙ² − Mₙ³)** —
verified exact through rung 4 (−11, −809, −18845089, −2.3×10²⁰). The cubic
g(x) = 1−2x+x²−x³ is exactly the doubling's (1−μ)²−μ³ factor
(from μ → μ(1±√μ)). So ALL the charge-tower primes (11, 809, 1459, 597049,
2169349081, …) come from one cubic evaluated over the growing spectra.

**ONE doubling, TWO towers.** The same eigenvalue-doubling μ → μ(1±√μ) produces
both towers: the ANALYTIC tower (Perron/field, λ_{n+1}=λ_n(1+√λ_n), degrees
2→4→8→16→32) is the + branch's top; the ARITHMETIC tower (charge, cyclic
coker) is the product of (1−both branches). The object's depth has two faces of
one operation.

**Curio (hint-ledger):** disc(x³−x²+2x−1) = **−23** — the same discriminant
flagged in B554 as the h=3 counterexample to "minimality forces h=1." The
charge cubic lives in a class-number-3 field. Possibly meaningful, possibly
coincidence; recorded, not claimed.
