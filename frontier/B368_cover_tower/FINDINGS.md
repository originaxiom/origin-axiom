# B368 (W2.4, corrected scope) — the cover tower: the seam sees the deck equivariantly

**Status: banked (frontier). The corrected question answered exactly: cover pairing = base pairing ∘ the
deck's exponent action (ψ³-relabeling) — structure, not new values; the wall extends up the tower.
Campaign W2.4. Firewalled; nothing to `CLAIMS.md`.**

## The corrected premise (the refutation that re-scoped this probe)

The original registration identified the golden seed's 3-fold fiber cover with the m=4 metallic seed via
the equal trace 18. That identification is **false** (verified exactly, twice independently): the
fixed-point binary forms are `(8,−8,−8)` (content 8, primitive discriminant **5**) for `(RL)³` vs
`(4,−16,−4)` (content 4, primitive discriminant **20**) for `R⁴L⁴`, and primitive discriminants are
conjugacy invariants. The genuine k-fold fiber cover of the golden bundle has monodromy `(RL)^k`, with
theta lift the k-th **power** of the golden lift, `W₁^k`.

## The deck identity (forced by projector algebra, verified exactly)

For gcd(k, 20) = 1 the eigenprojectors obey `P_a(W₁^k) = P_{k⁻¹a mod 20}(W₁)`, so against any partner the
cover-pair table must be the base-pair table relabeled by the deck's action on exponents. Verified exactly
for k = 3 against the banked B367 (1,2) table, **all 240 cells** (`deck_identity_exact: True`):

> `t_cover(a, b) = t_base(7a mod 20, b)` — **the seam sees the ℤ/3 deck equivariantly.** Covers create no
> new seam content against a fixed partner, and the form is not blind to the deck either: it transforms by
> the exact ψ³-style relabeling `a ↦ 3a` of eigenvalue exponents.

Corollaries, all exact: the cover's exponent list is `3·K1 mod 20 = {0,2,3,5,7,8,12,13,15,17,18}`
(matching the relayed independent list — that cross-session datum is now verified); the cover-pair value
multiset equals the base's 14-value set {±1/48, ±1/60, ±1/80, ±1/120, ±1/160, ±1/240, ±1/480}.

## The trace-18 twins at the seam level

`(RL)³` and `R⁴L⁴` have equal trace and equal lift order (20) but different exponent lists — and against
the same partner (m=2) their seam forms differ completely: the cover carries the base's 14 values; the
m=4 seed pair carries {±1/120, ±1/240, ±1/480} (banked B367). **Equal trace, different seam** — the
finer-than-trace statement now exact at the seam level.

## The tower singles

`W₁^k` for k = 2,3,4,5: every eigenprojector readout `tr(Par·P_a)`, H-projected, has zero √−3 and √−15
coefficients — **the single-object wall extends up the cover tower** (consistent with B369: these are
single monodromies built from golden blocks).

## Gate-C reading (firewalled)

The generation-deck channel through cyclic fiber covers yields **structure (equivariance), not
multiplicity of values**: a ℤ/3 deck does not manufacture three seam-distinct sectors from one seed — the
three "generations-as-cover-sheets" reading finds the sheets carrying relabeled copies of one form. This
constrains Gate C from below, in the same direction as the banked generation walls; nothing here is a
physics statement.

**Provenance.** The refutation certificate (relayed + independently verified, PROGRESS_LOG 2026-07-03);
B367 (banked tables, machinery); B369 (the readout construction; single-object wall context); B358 (engine).
Reproducer: `cover_tower.py` (~6 min); locks: `tests/test_b368_cover_tower.py`.
