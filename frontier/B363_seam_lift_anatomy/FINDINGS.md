# B363 — the seam's lift anatomy: two-sided, class-bound (the L57 opener)

**Status: banked (frontier). Numerical tier (double precision; s = 0 vs |s| ≥ 1/2880 separated by ~10 orders;
the bright theta×theta side is EXACT via B358/B359). Maps the seam function on the lift torus — the first L57
computation on the "is the characteristic forced?" question. Firewalled; nothing to `CLAIMS.md`.**

## The question and the method

B358 showed the seam lives in the theta lift and vanishes in the canonical one. Any lift differs from a
canonical one by Heisenberg data — so the seam coefficient is a *function on the lift torus*, and its
vanishing locus is the shape L57 needs. Method: the 8-embedding numeric Galois transport (embeddings
`{1,19,31,49}` fixing `H` + the `√5`-flipping coset `{7,13,37,43}`), extracting `s` per table entry;
aggregate `S = Σ|s|` per lift configuration.

## The anatomy (four verdicts)

| configuration (pair (1,2)) | seam |
|---|---|
| canonical × canonical — RL frame (B358, exact) | **dark** (`s ≡ 0`) |
| canonical × canonical — **LR frame** | **dark** (`5.6e-16`) — the frame is not the carrier |
| **`X^aZ^b`·canonical × canonical, ALL 225 twists** | **dark, 0/225** — one-sided Heisenberg twists never light the seam |
| **theta × canonical, either slot order** | **dark** (`1.5e-15`, `6.8e-16`) |
| theta × theta (B358/B359, exact) | **BRIGHT** (44/49; the law of B361/B362) |

**Two structural lemmas fall out:**

1. **The Par-lemma (one line, necessity):** a Par-commuting lift makes every `tr(Par·P·Q)` **real**, and a
   real value has `r = s = 0` in `H` — so **Par-non-commutation is necessary** for any seam content. (This
   retro-explains B358's canonical null *a priori*.)
2. **Necessity is not sufficiency — the seam is TWO-SIDED:** the one-sided twists `X^aZ^b·W₁` are
   Par-non-commuting, yet all 225 are dark with a canonical partner; and even the full theta slot is dark
   against a canonical partner. **The seam requires the theta class in BOTH slots** — bilinear in the
   characteristic, in exact echo of `√−15 = √−3·√5` (both primes' quadratic data) and of the multiplicity
   theme (one twisted participant is never enough).

**The class layer:** the theta lift is *not* a Heisenberg twist of the canonical lift (offset support
scattered — verified); its quadratic multiplier `j(j−1)/2` has quadratic part `c = 2⁻¹ ≡ 8 (mod 15)`, a
**non-square** — the theta construction lives over the inequivalent quadratic-character class. The seam
class-structure (square-class × Jacobi data) is the precise object L57's forcing argument must address.

## L57, restated sharply

> Does the two-seed pairing geometry (theta structures on the shared boundary torus / the gluing frame)
> **force the theta class on both slots simultaneously?**

The bilinearity is encouraging for "forced": a theta structure on the *gluing* torus would naturally decorate
*both* boundary restrictions at once. That argument (or its refutation) is the remaining step — analytic, not
a scan.

## Tiers

Numerical (this probe's darks: double precision, margins ~10 orders; committed scan artifact
`lift_torus_scan.json`); EXACT anchors: the bright side and the canonical-RL dark (B358/B359). The Par-lemma
is elementary and stated as such. Nothing promotes; theta-sector mathematics pending L57's resolution.

**Provenance.** B358 (dichotomy), B359–B362 (the law), L57. Reproducer: `lift_torus.py`; test:
`tests/test_b363_seam_lift_anatomy.py`.
