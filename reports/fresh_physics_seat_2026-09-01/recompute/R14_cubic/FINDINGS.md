# R14 — B884, the invariant cubic on the 27 (Ring R2 recomputation)

Cell: `reports/fresh_physics_seat_2026-09-01/recompute/R14_cubic/` — 2026-09-01.

## Verdict: MATCH (all three banked numbers, exact; plus the charge-forced addendum, upgraded to symbolic in my frame)

| banked (B884) | mine (blind, own construction) | verdict |
|---|---|---|
| dim of e6-invariant subspace of Sym³(27) = 1 (nullspace dim exactly 1) | 1 — two independent routes: (i) exact Freudenthal character decomposition Sym³(27) = 3003 ⊕ 650 ⊕ **1**; (ii) exact nullspace of the invariance system (78 own generators) on the weight-zero cubic space | MATCH |
| 45 weight-zero triples, support 45/45, every coefficient ±1 | 45 unordered zero-sum weight triples (all squarefree, none repeated); unique nullvector has support **45/45**, coefficients exactly **{−1,+1}** in my unit-structure-constant weight basis | MATCH (convention note below) |
| Yukawa support = 11 coupled cells, 275 zeros, 286 cells; pieces [1,1,1,2,2,2,3,3,3,3,6] | pieces sizes {1,1,1,2,2,2,3,3,3,3,6} (11 pieces), 286 unordered piece-triples, **11** coupled / **275** zero — and *exactly*, not numerically: in my frame each verdict is symbolic. Cell shapes {1,3,3}×3, {1,2,2}×3, {2,3,6}×3, {3,3,3}, {3,6,6} = the arc's `results.json` coupled list exactly | MATCH |

Addendum claim (2026-08-04, "support is PURELY charge-forced") also recomputed: the set of
286 cells admitting any zero-sum Cartan-weight triple is exactly the 11-cell support —
both directions hold, verified **exactly** (my frame), vs. the arc's sampled-at-scale
numeric route (their residual exactness note is discharged in my frame; their frame's
per-cell symbolic vanishing remains their priced follow-up).

## Blind-first protocol (what was read when)

**Before writing code**: only the header of `frontier/B884_yukawa_support/FINDINGS.md`
(§1–§3 through the support table — claim + banked numbers: dim 1; 45/45 ±1; 11/275/286;
piece sizes [1 | 3,3,2,2 | 6,3,3,2,1,1]), plus the R14 task card. No arc scripts, no
`results.json`, no B854/B883 code.

**After my runs**: rest of FINDINGS.md (addendum), `yukawa_support.py` lines 30–90
(their pipeline: 45 triples → sympy nullspace over all 72 root-vector generators of the
B854 Chevalley rep), `results.json`, `arc_verdict.json`, PROGRESS_LOG lines ~11295–11315
(memo 48 context for "6615→4→1").

## My construction (independent of B854/B883)

`r14_characters.py` (exact, Fractions; ~33 s):
- E6 Cartan matrix (Bourbaki), own weight-system generator; 27 = V(ω₁), 27 weights all
  multiplicity 1 (Freudenthal); roots from V(ω₂): 72, positive 36.
- Zero-sum unordered triples among the 27 weights: **45**, all with 3 distinct indices
  (so any invariant is automatically squarefree); ordered count 270 (= 6·45).
- Greedy highest-weight stripping with exact Freudenthal multiplicities:
  Sym³(27) = V(3ω₁) ⊕ V(ω₁+ω₆) ⊕ V(0) = 3003 ⊕ 650 ⊕ 1 → **dim Inv = 1**.
- Controls: Sym²(27) = 351' ⊕ 27bar → trivial mult 0 (no quadratic invariant);
  planted-positive: dim Inv(Sym³(27⊕27bar)) = **2** > 1 — the method can return ≠1.

`r14_explicit.py` (exact, < 1 s):
- Own trinification frame: 27 vars A(3×3)⊕B(3×3)⊕C(3×3), candidate
  I = det A + det B + det C − tr(ABC): 45 monomials, coefficients {±1}, squarefree.
- Stabilizer of I in gl(27), computed exactly with NO ansatz beyond the rigorous
  multidegree block-decomposition (diagonal / cyclic / anticyclic sectors decouple):
  nullspace dims 24 + 27 + 27 = **78** = dim e6 (sl3³ ⊕ (3,3,3) ⊕ (3̄,3̄,3̄), the
  trinification construction); all 78 generators annihilate I exactly; the mixed
  ansatz (δA←B, δB←A) control gives 0.
- Weight-zero cubic monomials under the 6 Cartans: **45** (matches the character count).
  Exact nullspace of the invariance system over the 78 generators: **dim 1**, support
  45/45, integer-primitive coefficients {−1,+1}, and the nullvector equals I up to scale.
- **Planted-positive control** (uniqueness claims need one): the same pipeline under the
  24 sl3³ generators only returns nullspace dim **4** (= span of det A, det B, det C,
  tr ABC) — the check can fail, and detects the extra invariants when the algebra is cut.
- SM grading: 11 pieces (Q=6, D=3 from A; three doublets 2 and three singlets 1 from B;
  three antitriplets 3 from C), 286 cells; cubic hits **11**; charge-allowed cells = **11**
  and identical to the support.

`r14_fulltensor.py` (exact, ~1 s):
- No-shape-assumption endpoint: 27⊗27 = 351' ⊕ 351 ⊕ 27bar (mult of 27bar = 1), hence
  **dim Inv(27⊗27⊗27) = 1** for the full ordered tensor cube — the unique trilinear
  invariant is automatically the symmetric cubic.

## Convention notes (E23)

- **Frame**: banked coefficients live in the B854 Chevalley weight basis; mine in my own
  trinification weight basis. Both are weight bases with unit structure constants, and in
  both the unique invariant is 45/45 with coefficients ±1. The frame-invariant content
  (dim 1; 45 zero-sum triples; squarefree; 11/275/286 support; charge-forced) matches
  number-for-number. "±1 in the banked frame" is confirmed as the same phenomenon in an
  independent unit frame; I did not rebuild B854's specific basis.
- **Prose vs bank**: B884 FINDINGS §3 prose says "the **two** [2,3,6] up/down-Yukawa
  shapes"; the banked `results.json` coupled list contains **three** cells of unordered
  shape {2,3,6} (their [3,2,6], [2,3,6], [2,3,6]) — as does mine (Q·H_u-type, Q·H_d-type,
  Q·L-type against the three antitriplets). The prose sentence undercounts its own bank
  by one cell shape (it lists 10 of the 11 cells); the banked numbers (11 coupled) are
  right. Cosmetic prose slip, not a discrepancy in the banked numbers.
- **"6615 → 4 → 1"** (task card wording): that chain is memo 48 / B1148's full-tensor
  route (π1-invariant trilinears 6615, gauge cuts to 4, then 1, survivor automatically
  symmetric), not B884's own pipeline (B884 solves the 45-unknown nullspace directly).
  The 6615 stage needs that arc's π1/holonomy instrument, which I did not re-run (the
  typed missing datum, were it my brief: the π1 action on 27⊗27⊗27). The two ends I can
  check shape-free both match: my sl3³-only control gives exactly **4** invariants (the
  natural "gauge stage" count), and the full-tensor endpoint is **1** (`r14_fulltensor.py`).

## Files

- `r14_characters.py` / `.out` — character/Freudenthal route (exact; dim Inv = 1; 45 triples; controls).
- `r14_explicit.py` / `.out` — explicit exact route (stabilizer 78; nullspace 1; 45/45 ±1; sl3³ control = 4; cells 11/275/286; charge-forced check).
- `r14_fulltensor.py` / `.out` — full ordered tensor cube: dim Inv = 1, no shape assumption.
- Nothing outside this directory was modified. Gate 5: no measured SM values used anywhere.
