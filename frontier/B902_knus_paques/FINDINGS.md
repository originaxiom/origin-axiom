# B902 — M5: the Knus–Paques difference class — the vacuum and charge fields are INVERSE classes; their composition is the split algebra

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** exact (two symbolic cube certificates + composition); local scans as discovery, not evidence

## The question (M5 / W4's deliverable)

The three cubics — μ (the charge cubic), B888's generic weight cubic (field
≅ K), and B888's vacuum weight cubic (field ≇ K) — share the resolvent
ℚ(√77). Cubic algebras with a fixed quadratic resolvent form a group
(Knus–Paques); the difference class of the two matter fields is W4's
registered "misalignment datum."

## The construction

For each cubic (depressed y³ + py + q, disc = 77s²) the Lagrange-resolvent
Kummer element α = (−27q + 3s·√−231)/2 ∈ F = ℚ(√77, √−3), computed exactly
(4-vector arithmetic over the basis (1, √77, √−3, √−231)). Twist set
ζ₆ᵃ·ε₇₇ᵇ (ε₇₇ = (9+√77)/2, the fundamental unit; a mod 3 since ζ₆³ = −1 ~ 1).
Local scans (8 clean primes p ≡ 1 mod 3 with 77, −3 QRs and p coprime to all
denominators, all four embeddings — the earlier run's p = 13 pollution
diagnosed and excluded) were used for DISCOVERY; the proofs are exact.

## The theorem (exact certificates)

1. **α_μ · α_vac = γ₁³ with γ₁ = (73008/7)·(1 + √−3)** — verified by
   symbolic cubing.
2. **α_generic · α_vac = γ₂³ with γ₂ = (30901351219200/13)·(1 + √−3)** —
   verified likewise.
   (Both certificates are rational multiples of ζ₆: they live entirely in
   the cyclotomic line ℚ(√−3), never touching √77 — the annihilation is
   witnessed inside the θ-side quadratic alone.)
3. Hence **α_μ / α_generic = (γ₁/γ₂)³** — the charge and generic classes are
   EQUAL (the control: same field, B888 — the machinery is calibrated), and

> **[α_vac] = [α_μ]⁻¹ in F*/(F*)³ — the vacuum field and the charge field
> sit in mutually INVERSE Kummer classes, with no unit twist needed. Under
> the Knus–Paques group law on cubic algebras with resolvent ℚ(√77):
> vacuum ⊕ charge = the identity — the two matter fields ANNIHILATE,
> composing to the split algebra.**

The misalignment datum is thus not a generic offset: the two fields are
each other's group-law mirror — the most symmetric nontrivial relation the
ℤ/3 admits. (Both being genuine non-Galois cubic fields, neither class is
trivial; being inverse says their "sum" carries no field content at all.)

Local scan summary (discovery record): the surviving twist was (0,0) —
trivial twist — in exactly the convention that proved out (ratio for the
same-field pair, product for the vacuum pairings), with 32 clean
embedding-tests each; every other twist died.

## Files

- `difference_class.py` → `results.json` (alphas, scans, the two γ
  certificates under `cube_proofs`)
- Locks: `tests/test_b902_kp.py` (recompute γᵢ³ = the products exactly)

## Depends on

B866 (μ), B888 (the two weight cubics + shared resolvent), B886 (the pencil
factors). Registered follow-up: none — W4's datum is delivered.
