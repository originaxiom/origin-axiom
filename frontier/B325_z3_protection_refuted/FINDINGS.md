# B325 — Chat-2's "symmetry obstruction" refuted: the light degeneracy is accidental, the CRUX stays Level 3

**Status: banked (frontier). Verify-don't-trust on the load-bearing *new* claim of the Chat-2 handoff (its Part 2).
Firewalled; nothing to `CLAIMS.md`.** Chat-2's Part 1 (the exact ω-circulant) is confirmed and banked as **B324**
(structure, not values — both seats agree). Its **Part 2** — a "firewall-sharpening" that would relocate the CRUX from
Level 3 to Level 4 — is a representation-theory error, and it matters because relocating the CRUX would misdirect the
specialist.

## The claim
Chat-2: the two light eigenvalues `(1, ω²)` are **ℤ/3-protected**; the E₆ cubic is ℤ/3-invariant (`a+b+c≡0 mod 3`); "a
ℤ/3-invariant operator cannot lift a ℤ/3-protected degeneracy," so the cubic **cannot** split the light masses; the
hierarchy therefore requires ℤ/3-**breaking** from the index-12 embedding (Level 4), with the cubic as "messenger, not
source" → the CRUX relocates to Level 4.

## Why it is wrong
1. **The two light modes are *different* irreps.** The generation ℤ/3 acts as the **regular representation** =
   `trivial ⊕ ω ⊕ ω²` — three *distinct* 1-dim irreps. The light eigenvectors are the `ω`-mode and the `ω²`-mode:
   **different irreps, not a single 2-dim irrep.** Wigner's "a symmetric perturbation cannot lift a degeneracy" applies
   only *within* one irrep. Two distinct 1-dim irreps carry **no** such protection.
2. **A ℤ/3-invariant operator *can* split them.** By Schur, a ℤ/3-invariant (circulant) operator is diagonal on the
   irreps with *arbitrary* scalars — it can give the `ω` and `ω²` modes different eigenvalues. Demonstrated: a generic
   complex ℤ/3-invariant circulant has two **distinct** light singular values (e.g. `[0.70, 2.56, 4.95]`). So a
   ℤ/3-invariant cubic mass matrix generically **splits** the light masses.
3. **The overlap degeneracy is accidental.** The equal light magnitudes of *our* matrix `α·J + ω·P` come from the single
   perturbation being a **unit** (`|ω|=1`), not from ℤ/3-protection. A different ℤ/3-invariant circulant is not
   degenerate.
4. **Overlap ≠ physical mass.** Chat-2 conflates the SL(2) *overlap* matrix `tr(aᵢbⱼ⁻¹)` (degenerate) with the physical
   E₆-*cubic* mass matrix (unknown, a different, generically-split circulant). The overlap's accidental degeneracy does
   not transfer.

## Verdict
The light degeneracy is **not ℤ/3-protected** — it is accidental (`|ω|=1`), and a ℤ/3-invariant cubic **can** lift it.
**The CRUX does *not* relocate to Level 4; it stays the Level-3 E₆-cubic computation** — which is *not* obstructed from
producing the hierarchy. (`OPEN_PROBLEMS.md` should *not* be changed to relocate the CRUX; Chat-2's Part-2 relocation
rests on the error above.) The exact ω-circulant (Part 1 / B324) stands as a structural result.

## The honest note
The multi-seat discipline working: Chat-2's Part 1 was bold-and-checkable-and-true (B324), and this seat verified it.
Part 2 was bold-and-checkable-and-false — a rep-theory slip (treating two distinct irreps as a protected degeneracy),
caught by computation. The `α·J + ω·P` structure is real; the "obstruction" built on its accidental degeneracy is not.
Ironically it is itself a level/structure confusion of the kind Chat-1's four-level framework (B323) was meant to
prevent.

## The fence
Elementary representation theory (the ℤ/3 regular rep; Schur) + explicit circulant singular values (numpy). The mass /
Yukawa interpretation is firewalled and CRUX-gated. Nothing to `CLAIMS.md`.

`z3_protection_refuted.py` (pyenv) · `tests/test_b325_z3_protection_refuted.py`. Related: **B324** (the exact
ω-circulant — Part 1, confirmed), **B323** (the four-level framework), **B321** (`|ω|=1` accidental degeneracy),
**OPEN_PROBLEMS.md** (the CRUX — stays Level 3, the E₆ cubic), **B307** (the multiplicity wall). Lit: Wigner (symmetric
perturbations / degeneracy); Schur's lemma.
