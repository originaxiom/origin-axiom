# B872 — the coset leg VERIFIED: 32 = 16 ⊕ 16̄ at every enhancement point, on two independent legs — and the charge splits REAL

cc banking seat, 2026-08-03. The last "theirs" item of B866's boundary, now verified on this
seat's fully independent build. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 1. What was claimed

At each distinguished charge (B866's S₃ triple), the centralizer is so(10)⊕u(1) (type banked,
B866 addendum) and **the 32-dim complement of the centralizer in e₆ is the spinor pair
16 ⊕ 16̄** — the generation pair. The type was verified on both seats; the coset stayed theirs.

## 2. LEG A — exact over ℤ (root combinatorics of the regular so(10)⊕u(1))

Delete the long-arm end node of E₆: the 40 zero-coefficient roots form **D₅** (diagram
verified); the 32 complement roots carry u(1)-charge = the deleted-node coefficient, exactly
**±1, 16 each**; each 16 is a **single Weyl(D₅) orbit** through a **fork-node fundamental
weight** — the spinor — and the two charges land on the **two different fork nodes**: 16 vs 16̄.

## 3. LEG B — at all three Galois roots, 40 digits, certified

At t = 13× the banked cubic roots (the normalization certificate `cubic_modp_check.py`, §5):

| quantity | root 1 | root 2 | root 3 |
|---|---|---|---|
| kernel / center | 46 / 1 | 46 / 1 | 46 / 1 |
| ad(z) split of the 32 | 16 / 16 | 16 / 16 | 16 / 16 |
| commutant of each half | **1 / 1** | 1 / 1 | 1 / 1 |
| B(W₊,W₊) (rel.) | 5×10⁻³⁶ | 8×10⁻³⁷ | 4×10⁻³⁶ |
| rank B(W₊,W₋) | **16** | 16 | 16 |
| spectral gap | 10⁴¹ | 10⁴⁰ | 10⁴⁰ |

Commutant dim 1 = **absolute irreducibility** (generic-vector cyclicity would NOT prove it;
the commutant does — computed by the certified generic-pair method: kernel of two random
combinations, then every candidate certified against all 46 generators). Isotropic halves with
nondegenerate cross-pairing ⟹ W₋ ≅ W₊* — the 16̄. Dim 16 + irreducible pins {16, 16̄} among
so(10) irreps. **Galois-consistent across all three roots.**

## 4. A correction made BY the locks, kept for the record: the charge splits REAL

ad(z) on the 32 has **real** spectrum ±q at every root (q² > 0) — the charge is a split-torus
direction, as it must be in the **split real form e6(6)** this build carries. An earlier draft
of this arc claimed a compact u(1) (spectrum ±iω): that was a mis-diagnosis from the first
crashed runs, which sat at the WRONG stratum (unscaled roots, kernel 30, where "z" was not
central and the eigensplit was garbage). The commit-gating lock caught the stale claim before
banking. The compact-vs-split question for the physical charge is a **layer-8 (real form)
question and is not probed by this arc**. With B875: the same 32 carries two compatible readings — the ±q charge eigenspaces (this arc) and the triality foreign sectors V_j⊕V_k.

## 5. The normalization certificate (a THIRD derivation of the cubic)

`cubic_modp_check.py`, mod 2⁶¹−1: the fresh build's det₄₈ along the pencil has radical
= **banked(t/13)** exactly (µ = 1/13, consistent at every degree) — today's deterministic
build carries the solo seat's ρ-normalization, and the enhancement points sit at **13× the
banked roots**. Using banked roots unscaled lands on the generic 30-stratum silently — the
trap is now certified, not just remembered.

## 6. What this does NOT establish

- Nothing about which of 16/16̄ is "matter" — the labels are a charge-sign convention.
- The generations reading stays a signature (B866) with a structure (B875); THE DESCENT
  (B876, queued) is the deciding computation.
- Numerics at 40 digits with 40-order gaps and per-item certificates, not exact field
  arithmetic; the exact-ℚ(ρ) pass remains the solo seat's queued cell (their (b)).

`tests/test_b872_coset.py`
