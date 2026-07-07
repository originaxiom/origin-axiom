# B453 — Ethogram E1: reproduction — the identical child, the isolated cover, the Lucas launder

**Status: banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md` (PR #596, before
computation). Verdict: forced/laundered throughout (knot channel — no p-values per prereg);
one sharpening of the banked record (identity, not just shared invariants); one honest
UNDECIDED. Novelty column: lit-gate running at bank time — no novelty claimed pending it.**

## E1a — the sterility statement (assembly, labeled)

The surgery lineage terminates at generation 2: the child is closed ⇒ Weil-rigid ⇒ no moduli,
no cusp, no filling channel (assembled from banked B435/B443). The organism reproduces exactly
once by surgery. The Agol backdrop (stated, not observed): every closed hyperbolic 3-manifold
has a fibered finite cover — the lineage continues *virtually* by THEOREM; the probe's open
question was only the degree.

## E1b — the ℤ/5 cover of the child (the decisive cell; SnapPy, `covers.py`)

- **Gates PASS**: vol(cover) = 4.906844 = 5.000× vol(child) exactly; H₁(child) = ℤ/5 ✓.
- **The child's π₁ has exactly ONE proper subgroup of index ≤ 6** — the ℤ/5 kernel.
  (SnapPy enumerates ALL covers, not just cyclic: none at degrees 2, 3, 4, 6.) Ethologically:
  reproductive isolation — the child's only low-degree move is the single abelian cover.
- **b₁(ℤ/5 cover) = 0**: H₁ = ℤ/11 ⊕ ℤ/11 — no free part. Degree 5 does NOT fiber; the
  virtual-fibering degree is **> 6: UNDECIDED-AT-DEGREE-6** (the prereg's honest bin; the
  budget capped the scan).
- **The Lucas launder (exact)**: |H₁(cover)| = 121 = **L₅²** — and this is the banked
  B437/Alexander mechanism surfacing at the cover: |∏ₖΔ_{4₁}(ζ₅ᵏ)| = 121 (verified exactly);
  control: the 6₁ child's cover gives (ℤ/31)², and |∏ₖΔ_{6₁}(ζ₅ᵏ)| = 961 = 31² ✓. The
  reproduction channel's one move produces torsion the whitelist already predicts.

## E1-SHARPENING — the two parents have the IDENTICAL child

**4₁(5,1) ≅ 5₂(5,1) — rigorously isometric (SnapPy `is_isometric_to`: True).** The banked
record (B440/B443) had them as tier-2 "commensurability-shared" (same volume, same −283 field,
same 4 vacua, same torsion 121); the truth is stronger: **they are the same manifold.** Two
distinct organisms, one and the same offspring — the ultimate form of the no-heredity fact on
the reproduction card (S055): the child not only carries no parent-unique marks, it cannot even
be assigned a parent. (Correction hygiene: in-session, an isometry test against m003(−3,1) was
briefly mislabeled "Meyerhoff"; m003(−3,1) is the Weeks manifold — the banked "child = the
Meyerhoff manifold" identification is untouched.)

## E1c — the parent cover-field table (assembled from banked B448 + B235)

| cover degree k | geometric invariant trace field (B235) | character-variety fields beyond geometric (B448 orbit tower, T₁-period-2k) |
|---|---|---|
| 1 | ℚ(√−3) | ℚ(√−3) (the discrete-faithful pair) |
| 2 | ℚ(√−3) | **ℚ(√−7)** (the chirality field) |
| 3 | ℚ(√−3) | ℚ(√−3) (the period-6 partner) |

Reconciliation (the GATE, textbook — Maclachlan–Reid): the geometric invariant trace field is
commensurability-rigid (constant up the tower), while covers' character varieties acquire new
components with new fields (fewer relations upstairs). No tension; two invariants. The table is
the only NEW-MATH-eligible piece and is held at observation grade (B448 already refuted one
field-tower extrapolation — no law is claimed from three rows).

## Controls
5₂(5,1): identical (it IS the same manifold — the control collapsed into the sharpening).
6₁(5,1): different volume (2.68), same qualitative profile (one ℤ/5 cover, b₁=0, torsion =
its own Alexander law) — the behavior pattern is class-generic; only the labels differ.

## Bins
Forced/laundered across the board: the cover's torsion launders through the banked Alexander
mechanism; the isolation profile is shared by the control; the sharpening (identity of the
children) strengthens a banked negative. UNDECIDED-AT-DEGREE-6 on the virtual-fibering degree,
reported as such. No H1.

## Reproduce
```
python3 covers.py     # gates + the cover survey + controls (~2 min)
# the isometry + Lucas checks: see tests/test_b453.py
```
