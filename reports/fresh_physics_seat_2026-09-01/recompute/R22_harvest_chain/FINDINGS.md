# R22 — B1148 memo 48, the carrier-harvest nullspace chain 6615 → 4 → 1 (Ring R3 recomputation)

Cell: `reports/fresh_physics_seat_2026-09-01/recompute/R22_harvest_chain/` — 2026-09-01.
Code: `r22_chain.py` (exact: sympy/QQ + Fractions; the one 16470-unknown direct nullspace done mod two
large primes, all other nullspaces over QQ). Output: `r22_chain.out` (11 s total).

## Verdict: MATCH on 6615 and on 1 (both exact, own construction, incl. the survivor's structure);
## MATCH-with-convention-note (E23) on the 4 — it is the Sym³ count; the same rung in the full ordered tensor is 9.

| rung (B1148 FINDINGS line 20 / memo 48) | banked | mine (blind) | verdict |
|---|---|---|---|
| π₁ alone: invariant trilinears on Ψ×Ψ×27, Ψ = C²⊗27 | **6615** | **6615** four ways: (i) exact sl₂ Clebsch count from my own decomposition Ψ = 6·V₂+15·V₁+6·V₀, 27 = 6·V₁+15·V₀; (ii) **direct nullspace on the full 78732-dim ordered tensor** (16470 weight-zero unknowns, 19710 equations, rank 9855, mod 10⁹+7 and mod 998244353); (iii) block-exact fixed space of the **actual figure-eight holonomy** a=[[1,1],[0,1]], b=[[1,0],[−ω,1]] over ℚ(ω) = 6615; (iv) block-exact fixed space of the finite **2T** image (quaternion units) = 6615 | MATCH |
| + trinification gauge su(3)³ | **4** ("memo 35 × the unique ε") | joint (sl₂ on C² and 27, su(3)³ on the 27s) direct nullspace on Ψ⊗Ψ⊗27: **9** in the full ordered tensor; its 27-symmetric part has dim **4** (= ε ⊗ {det A, det B, det C, tr ABC}); Inv_{su(3)³}(Sym³27) = 4, Inv_{su(3)³}(27^{⊗3}) = 9 (3 determinants + 6 orderings of the trace) | MATCH under memo 35's Sym³ convention; **9 ≠ 4** if the rung is read as "full tensor, no symmetry assumed" |
| + full e₆ | **1**, 270 ordered triples, survivor automatically symmetric | **1** (78 own e₆ generators = stabilizer of the cubic in gl(27)); 270 ordered weight-zero triples, none with a repeated index; survivor support 270/270, coefficients {−1,+1}, **automatically symmetric**, equals the cubic I as a tensor (ratio set {1}); with the C² slots: joint nullspace dim 1, survivor = **ε ⊗ I** exactly, antisymmetric under Ψ↔Ψ | MATCH (also = R14 `r14_fulltensor`) |

## Blind-first protocol (what was read when)

**Before writing code**: `frontier/B1148_carrier_harvest/FINDINGS.md` lines 1–60 (the memo table + through-line;
the claim and the numbers 6615 / 4 / 1 / 270 / "6 doublets + 15 singlets" / "24 spinor×doublet + 30 spinor×singlet"),
`b1148_results.json` (same numbers, one line per memo), `verification/reproduce_new.sh` (provenance only — the
certs are NOT in this tree, they sit on `origin/claude/outside-bench @ d3c99640`), PROGRESS_LOG 11240–11320 for
context, and R14's FINDINGS (its sl3³ control = 4, full-tensor e6 = 1). The π₁ action on the 27 is nowhere
defined in the committed arc; I pinned it from the banked shape (27 = 6 doublets + 15 singlets under the A1 the
holonomy closes through; C² = the holonomy's fundamental; π₁ Zariski-dense in SL(2,ℂ)) — and the number 6615
then falls out, which pins the convention independently of the cert.

**After my runs**: `d3c99640:outside_bench/certificates/uniqueness_chain.py`, `outputs/uniqueness_chain_out.txt`,
`memos/UNIQUENESS_CHAIN.md`, `memos/YUKAWA_COUNT.md` (memo 35). Diff below.

## My construction (independent of the arc's crystal/Chevalley frame)

- 27 in the trinification frame A,B,C ∈ 3×3, cubic I = det A + det B + det C − tr(ABC) (45 monomials, ±1).
  e₆ := stabilizer of I in gl(27), computed as an exact 2475×729 nullspace: **dim 78**. su(3)³ := the explicit
  24 generators (A→X₁A−AX₂, B→X₂B−BX₃, C→X₃C−CX₁), checked to kill I and to lie in the 78.
- The A1: su(2) in the upper-left corner of X₁. Under it 27 = **6·(2) + 15·(1)** (H-weights {±1:6, 0:15}) — the
  same shape the arc asserts for its root-sl₂ (the cert's `assert dict(wts27)=={1:6,0:15,-1:6}`); all root sl₂'s
  of e₆ are conjugate, so this is the same stratum. Ψ = C²⊗27 under the diagonal sl₂: weights
  {±2:6, ±1:15, 0:12} → 6·V₂ + 15·V₁ + 6·V₀ (24 spinor×doublet + 30 spinor×singlet slots, as banked).
- Trilinears := the full ordered tensor Ψ⊗Ψ⊗27 (54·54·27 = 78732), no symmetry assumed anywhere.
- 27⊗27⊗27 direct nullspaces on the 270 weight-zero ordered triples (and the 45 unordered ones for Sym³):
  su(3)³ → 9 / 4, e₆ → 1 / 1.

## Controls

- **Planted-positive for the uniqueness (e₆ → 1)**: the identical pipeline with the 24 su(3)³ generators only
  returns **9** (full) / **4** (Sym³) — the check can fail and does when the algebra is cut.
- **Finite-image control**: 2T-invariants in V₆ = 1 vs sl₂ = 0 (the degree-6 binary-tetrahedral invariant), so
  replacing SL(2) by its finite 2T image WOULD change the count at spin ≥ 3; the blocks that occur here
  (spin ≤ 5/2) are below that threshold — which is why π₁, 2T and sl₂ all give 6615 (all three computed).
- Two independent primes for the 16470-unknown direct nullspace; QQ-exact everywhere else.

## Diff against the cert (after-phase reading)

1. **6615**: the cert computes rung 1 by **Clebsch counting** from the sl₂ content (Ψ|_diag = 6·1 + 15·½ + 6·0,
   27 = 6·½ + 15·0), **not** by a direct nullspace; the FINDINGS phrase "by DIRECT full-tensor nullspace" applies
   only to rung 3. My cell supplies the direct 78732-space nullspace (6615, two primes) plus the fixed space of the
   *actual* holonomy generators (block-exact over ℚ(ω)), so the "Zariski-density CITED-standard" step is now also
   checked concretely for this representation: π₁-fixed = SL(2)-fixed = 6615.
2. **4**: the cert does not compute rung 2; it reuses memo 35's `dim Inv_sym³(27) under sl₃³ = 4` times ε. That is
   a **Sym³** number. In the full ordered tensor the same rung is **9** (= ε ⊗ {3 dets + 6 orderings of tr ABC});
   4 is exactly its 27-symmetric part (computed, `sym_part_rank`). So the chain as printed mixes conventions:
   6615 (full tensor) → 4 (Sym³) → 1 (full tensor). The honest all-full-tensor chain is **6615 → 9 → 1**.
   Neither changes the theorem (endpoint 1, survivor ε⊗C, automatic symmetry) — but "the trinification gauge cuts
   to 4 ... no symmetry assumed" is not what was computed. Per E23 a resolved convention mismatch → MATCH with note,
   flagged for the arc's prose.
3. **1**: cert's rung 3 = exact nullspace on 270 ordered triples over the 72 root generators of its Chevalley
   frame; mine = 78 stabilizer generators in the trinification frame; both dim 1, both automatically symmetric.
   I add: survivor support 270/270 with coefficients ±1 and equal to I; with the C² slots the joint survivor is
   ε⊗I exactly and antisymmetric under fermion exchange (memo 47's shape, here as an output).

## Typed residue

None blocking. The one datum not in this tree (the cert's explicit sl₂ embedding) was pinned from the banked
shape and then confirmed against the cert; conjugacy of root-sl₂'s in e₆ makes the two frames equivalent.

## Files

- `r22_chain.py` / `r22_chain.out` — everything above, one run (~11 s).
- Nothing outside this directory was modified. Gate 5: no measured SM values used anywhere.
