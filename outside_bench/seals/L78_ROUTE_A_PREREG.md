# SEAL — L78 ROUTE A: the level-2 filling span, and what a non-vacuum observer reaches

**Sealed before computing.** Object: the E₆ level-2 modular theater (nine primaries);
the Dehn-filling covectors of `docs/OPEN_LEADS.md` L78 ("Route A"); and the successor
question B583's X3 named but did not compute.

## Why this seal exists

L78 is carried in `docs/OPEN_LEADS.md` as **"OPEN — Round 2 first," ★★★★.**
`frontier/B583_chiral_content/FINDINGS.md` §X3 states the answer in prose —
*"Level 2: rank exactly 6 = dim(θ-even) over 719 slopes (θ-odd projection 4e-13) …
L78 resolves"* — and the arc's lock `tests/test_b583_content.py` tests **only the
level-1 mechanism** (a 3×3 theater). **The level-2 number has no lock and no code
in the arc directory.** This seal reproduces it and then asks the question X3's own
conclusion makes next.

## The instrument

The level-2 stage is rebuilt from the E₆ Cartan matrix on this bench: W(E₆) by BFS
over simple reflections, the nine level-2 integrable weights, Kac–Peterson `S` at
k+h^∨ = 14, `T` from h(λ) = (λ,λ+2ρ)/28 and c = 78/7. `C := S²`. `θ-even :=` the
+1 eigenspace of `C`; `θ-odd :=` the −1 eigenspace.

Filling covector for a coprime slope (p,q): `e_seed · ρ(g_{p,q})`, with `g_{p,q} ∈
SL(2,ℤ)` carrying first column (p,q) and `ρ` the (S,T) representation, the word
obtained by continued fraction.

## CELL 1 — does B583 X3's level-2 number reproduce?

**Observed:** the rank of the stacked vacuum-seeded covectors `e₀ · ρ(g_{p,q})` over
all coprime (p,q) with 1 ≤ q ≤ 30, |p| ≤ 30, by SVD at a stated threshold.

- **Outcome A:** rank = 6.
- **Outcome B:** rank ≠ 6.

## CELL 2 — could Route A ever have fired its positive outcome?

**Observed:** whether all three of `e₀C = e₀`, `[C,S] = 0`, `[C,T] = 0` hold, and
whether `(e₀ ρ(g))C = e₀ ρ(g)` holds for every `g` in the generated word set.

- **Outcome A:** all hold.
- **Outcome B:** at least one fails.

## CELL 3 — the θ-odd reach of a non-vacuum observer (the new computation)

X3's own conclusion is *"the state's chiral content requires non-vacuum observer
states."* It did not compute how much such a state reaches.

**Observed:** for each of the nine primary seeds `e_i`, and for each seed of the form
`(e_i − e_{C(i)})/√2` with `i ≠ C(i)`, the **dimension of the projection of
span{seed · ρ(g_{p,q})} onto the θ-odd 3-space**, over the same slope set.

- **Outcome A:** at least one seed has θ-odd reach ≥ 1.
- **Outcome B:** every seed has θ-odd reach 0.

## Controls (all must pass before any cell is read)

- **C1 — the banked level-1 number.** The same routine in the 3-dim level-1 theater
  must return rank **2** (B580 Q1's banked value, 576 slopes there).
- **C2 — the stage's own gates,** run before any cell: |W(E₆)| = 51840; `S`
  symmetric and unitary; `S²` a permutation matrix; `(ST)³ = S²`; Verlinde fusion
  coefficients non-negative integers; quantum dimensions from the S-column matching
  the independent q-Weyl-dimension formula.
- **C3 — MB12 transversality (the instrument must be able to report a non-zero).**
  A seed placed **inside** the θ-odd 3-space must return θ-odd reach ≥ 1. If it
  returns 0, the instrument cannot detect θ-odd at all and **no cell may be read**
  (memo 164: control passing is not instrument working — this is the control that
  tests whether it *works*, not whether it *passes*).
- **C4 — slope-set sufficiency.** The reported ranks must be stable as the slope
  set grows (report the rank at three nested slope sets).

## Declared priors

- CELL 1: **Outcome A** expected (B583 states it; this is a reproduction).
- CELL 2: **Outcome A** expected — and if it holds, the consequence belongs to the
  interpretation section, not here.
- CELL 3: **no prior declared.** The arithmetic is not known to this bench.

## Interpretation is not preregistered

Per bench rule #21, the outcomes above state only what will be **observed**. What any
of them means for L78's status, for B583's headline, or for the chirality gap in
`WHAT_WOULD_COUNT.md` §4A.1 is written only after the numbers are in.
