# B908 — the I-exactness pin: three legs, two closed — I = −1 IS THE LEIBNIZ SIGN

**Date:** 2026-08-05 · **Seats:** cc (banking) + computation agent (leg 3) ·
**Status:** ALL THREE LEGS CLOSED — I = −1 EXACTLY (round 2 of the register loop).

## The reduction (DESIGN.md)

I = −1 ⟺ v := ∏(row couplings) + ∏(col couplings) = 0, with u, v ∈ ℚ by the
K₃,₃ argument: the coupling graph is connected complete bipartite (verified on
the banked incidence — every cross-pair shares exactly one atom, the sides
partition the nine), its bipartition is unique, so every Galois σ preserves or
swaps the pencils and t = I + 1/I ∈ ℚ.

## Leg 2 — the congruences (closed)

I ≡ −1 at all SEVEN full-tower primes (40123, 40639, 40693, 40897, 40903,
40927, 40939), atom-rescaling invariance gated at each (`leg2_results.json`).

## Leg 3 — the mechanism (the agent's delivery, banking-verified)

Exact theory anchors over ℚ (`DRAFT_LEG3.md` §0, no floats anywhere):

1. **Leibniz in grid coordinates**: relabeling the 3×3 cells by (even
   transversal, odd transversal) turns det's six terms into exactly the three
   grid-rows (+1) and three grid-columns (−1): **det = Σ_rows∏ − Σ_cols∏** —
   a rows+cols cubic is det-type iff I = −1.
2. **The 16-vs-4 dichotomy (non-circular)**: a rows+cols-supported cubic with
   nonzero coefficients has gl₉-stabilizer dim **16 (sl₃⊕sl₃) iff I = −1**,
   dim 4 otherwise — proven exactly over ℚ with controls (det → 16;
   permanent → 4; random → 4; random-forced-to-I=−1 → 16).
3. **Uniqueness**: the 16-dim stabilizer annihilates a 1-dim space of cubics
   (exact over ℚ) — any cubic it stabilizes is ∝ det.

On the object (mod-p, structural at 40123 AND 40639, support at all 7): the
restricted cubic on the nine colorless atoms has stabilizer dim **16** with
the controls behaving; an explicit det-frame sends the six couplings to
(+1,+1,+1,−1,−1,−1); the grid transpose J gives cub(J·,J·,J·) = −cub on all
165 multisets; **the support is EXACTLY the two pencils in characteristic 0**
(159/159 zero-sum certificates at each of 7 primes). The pencil-swapping
involution is a FRAME symmetry (not Galois — Galois preserves both pencils,
pinned by the S-line; P_R and P_C are separately rational, sharpening leg 1).

> **The mechanism: the row pencil is the even transversals, the column pencil
> the odd ones — I = −1 is the determinant's orientation parity, one −1 per
> line. The program's signature sign is the Leibniz sign.**

## THE CLOSURE (round 2, banking-verified): I = −1 EXACTLY

Route (a) direct (`leg3_exact.py`, `DRAFT_EXACT.md`) — and the route-discovery
is a theorem of independent worth:

> **The four torus generators R₈, R₁₄, R₁₆, R₂₂ commute exactly over ℚ on the
> 27, and every labeling's operator span equals theirs — the nine colorless
> atoms are joint eigenlines of ONE RATIONAL commuting family. The tower field
> never enters the atom lines** (mod-p reduction confirmed at all 7 primes,
> 252/252; then exact).

The nine atom lines built exactly in characteristic 0; the banked cubic
restricted; all six couplings exact; the support = exactly the two pencils;

> **P_R = −P_C as exact integers (106 digits each): v = 0 identically,
> I = −1 EXACTLY, no height bound.**

Jewels in the constants: the S-line coupling c_S = **−disc(μ)** exactly; the
two non-S rows share one coupling constant (one Galois orbit of six); the
hidden correlation B(ρ) = −3w(ρ)² with w ∈ K. Remaining naming caveat (the
agent's, honest): the identification of the char-0 configuration with the
banked pipeline uses mod-p reduction at the 7 primes — simplicity forces the
lines; the reduction was verified at all seven.

## Files

`DESIGN.md`, `leg2_results.json`, `leg3_mechanism.py`, `leg3_results.json`,
per-prime states, `DRAFT_LEG3.md`. Locks: `tests/test_b908_pin.py`.
