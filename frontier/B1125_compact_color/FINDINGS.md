# B1125 — V-2 COMPACT COLOR: NO-COMPACT-HOST — the object supplies the color ALGEBRA but not compact color; compactness is external

**Status: banked (frontier). Verdict PROVED (a typed NEGATIVE: NO-COMPACT-HOST,
exhaustive over the swept sign-lift torsor; deterministic re-run 164s, 0 compact hits
even pre-reverification; reproduces B1119's variant-A signature (5,3) exactly). Answers
C-AR1. Value-campaign cell V-2. Gate 5 untouched. Lock `tests/test_b1125_compact_color.py`.**

## The question (C-AR1)

B1114: at the A2 landing, E₆ ⊇ so(3,1) ⊕ su(3) (color) at the COMPLEX level. B1119: the
real-form host of the constructed lifts is E₆(2)/E₆(6) — color sl(3,ℝ) or su(2,1), NEITHER
compact. The sign-lifts form a torsor over a finite 𝔽₂-kernel; each element is a character
twist = potentially a different real form. **Does ANY kernel element, over both lattice
classes, give COMPACT su(3) color?** E₆(−26) = M(𝕆,ℂ) (max compact f₄ ⊃ compact su(3)) had
not been reached by any lift — the live candidate.

## THE ANSWER: NO-COMPACT-HOST (exhaustive, and it reaches the candidate form)

> **No element of the sign-lift torsor gives compact su(3) color.** Swept 48
> individually-verified elements (two Chevalley-automorphism constructions × both lattice
> classes; θ²=I enforced — found by falsification, naive "solutions" were not involutions).
> The union of real forms reached is characters **{−26, +2, +6}** — including
> **E₆(−26) = M(𝕆,ℂ) itself** — and in EVERY case the color factor is non-compact.

**THE DISCRIMINATING FACT (verified directly, not assumed).** The ad-invariant form
(corrected: ⟨e_r, e_{−r}⟩ = −1, the B1119 fix; a live negative control shows the wrong +1
form fails ad-invariance) restricted to the color A2 factor I2 is **always (5,3,0)** — a
split-basis property: the 2 coroots give a positive-definite (2,0) and each of the 3
positive-root hyperbolic planes {e_r, e_{−r}} gives (1,1), so (2,0)+(3,3) = (5,3). Compact
su(3) needs (0,8). **E₆(−26) IS reached (permute/class A), but its I2 stays (5,3)** because
θ fixes I2 pointwise there — the near-miss the classification checksum alone would have
mis-called a hit. This arc's methodological addition: the checksum (character ∈
{+6,+2,−14,−26,−78}) is NECESSARY BUT NOT SUFFICIENT; the **purity check** (is the form
one-sided on each θ-eigenspace, not just does the character land right) is what decides
compactness, applied uniformly to all 48 elements.

## What it means — and the SHARPENED open question (a LINEAR negative, not the last word)

The object supplies the color **ALGEBRA** su(3) (B1114) but no **LINEAR** sign-lift makes
it compact. This is a TYPE distinction, not a search failure: compact su(3) is the
anti-Hermitian real form {X : X† = −X} = signature (0,8), and **compact real forms are
given by an ANTILINEAR involution (a complex conjugation X ↦ −X†), never by a linear inner
twist.** So no element of the object's linear lift torsor could ever flip (5,3) to (0,8) —
and this arc's own **compact-involution control confirms the other side: fed the antilinear
compact conjugation, the machinery returns −78 (fully compact E₆).** The linear torsor is
therefore genuinely exhausted, and the missing ingredient is named exactly: a complex
conjugation.

**The object HAS one antilinear structure — the mirror** (amphichirality, 27 ↔ 27̄, the
Galois conjugation √−3 ↦ −√−3 of ℚ(√−3)). So the last residual is not closed but
**SHARPENED** into a decidable question — cell **V-2′ (the antilinear completion)**: does
the object's own **mirror-conjugation, restricted to I2, give (0,8)?** If yes, compact color
is the object's, supplied by its own amphichirality at a second level (the B1113
measurement-by-coupling pattern, now supplying a real structure not a dial); if no, compact
color is external even to the mirror-coupling — a deeper negative. Adelic reading (labeled):
the antilinear conjugation IS the real structure at the archimedean place, so "the observer
supplies compact color" = "the ∞-place supplies the conjugation" — the exact twin of B1114's
"the signature is the observer's." What is settled: compactness is a **second-level
(antilinear) closing**, never a first-level (linear) one.

## The honest fences

- **Exhaustive within the swept construction** (48 elements, both lattice classes, θ²=I
  verified, deterministic). A broader 12-candidate search (matched Weyl twists of
  hatch/I1) found only characters {+2,−2} — nothing new — so the two-class reading appears
  to exhaust the "swap hatch↔I1 via a matched Weyl twist" family.
- **3 of 4 B1119 controls reproduced EXACTLY** (split +6; compact −78; variant A +2 with
  color signature (5,3) — character AND signature). B1119's "variant B" (+6, su(2,1)) is
  reached here via the **permute/class B** family (character +6), not the antipodal family
  the memo's label suggested — a **construction-labeling nuance**, not a gap: character +6
  is reached, and its color is non-compact like all the rest. (Relayed to cc3, who own
  B1119, for label reconciliation.)
- The cited abstract embedding so(3,1) ⊕ su(3)-compact ⊂ E₆(−26) via so(9,1) is a
  DIFFERENT embedding of I2 and is NOT contradicted — the object's lift torsor simply lands
  on a color I2 that is not that compact one. Gate 5 untouched.
