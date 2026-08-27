# THE TOWER COUNTED — every shell of the dark tower has a closed form, proved: ACTIVE p^{2e−1} + (p−1)²p^{2e−2}, SHELL-a (p−1)p^{2(e−a)−1}, SURVIVOR 1, DARK the exact remainder — symbolic identities (induction for the geometric sum, grand total p^{2e}, e = 2 collapsing to memo 87) verified at twelve depths
## (outside bench, 2026-08-27; eighty-ninth memo; memo 88's "noted, not asserted" fence discharged)

### THE CLOSED FORMS (`certificates/dark_tower_counts.py`; asserts GREEN; derivations in the docstring)
For N = pᵉ, the classifier of memos 87/88 partitions the p^{2e} points as:
- **ACTIVE** (|T| = 1): p^{2e−1} + (p−1)²p^{2e−2} — the ν(l) ≥ 1 block
  entire, plus the affine-bijection count in the unit-l block.
- **SHELL a** (|T| = p^{a/2}, 1 ≤ a ≤ e−1): **(p−1)p^{2(e−a)−1}** — from
  the (t, s) parametrization of the j ≡ 2 mod pᵃ, l ≡ −2 mod pᵃ
  sub-block, minus its ν(α) > a diagonal.
- **SURVIVOR**: 1, forced to (2, pᵉ−2).
- **DARK**: the exact remainder, in closed form
  (p−1)p^{2e−1} − (p−1)²p^{2e−2} − p(p^{2e−2}−1)/(p+1) − 1.

### THE PROOFS (all symbolic, machine-checked)
- The shell geometric sum **proved by induction** (base C(1) = (p−1)p and
  step C(m) − C(m−1) = (p−1)p^{2m−1}, both plain power identities — a
  complete proof, not an instance check).
- **Grand total ≡ p^{2e}** as a symbolic identity in (p, e).
- **e = 2 collapses exactly to memo 87's formulas** (including the dark
  count (p−2)p² + (p−1)).
- Numeric confirmation against the classifier at **twelve (p,e) depths** —
  the seven point-verified ones (memos 87/88) plus (3,5), (5,5), (7,4),
  (11,3), (13,3) — every shell, every depth, exact.

> **The dark tower is now fully quantitative: given the classifier (whose
> derivation is memos 87/88's and which is point-verified against T
> itself at seven depths), every census question about the tower has a
> closed-form answer for all (p, e) — including the darkness fraction
> (p−1)/p·(1 − 1/p + O(p⁻²)) per unit-l block and the exponentially
> thinning shells (p−1)p^{2(e−a)−1} that make the survivor's thread the
> measure-zero spine of the structure. Unchanged and honest: the
> classifier-for-all-e remains derivation-plus-instances; the
> exponent-echo hook remains a hook. Relayed to cc with memos 87/88.
> Gate 5 untouched.**

### Certificates
`certificates/dark_tower_counts.py`; output
`outputs/dark_tower_counts_out.txt` (in-lane rerun byte-identical).
