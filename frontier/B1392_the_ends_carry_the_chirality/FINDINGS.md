# B1392 — THE ENDS CARRY THE CHIRALITY: in the seat's frame, a cusp where the Higgs class does not vanish is sealed. The Higgs field grows like the height there, the deformed problem is well-posed, and the end adds nothing to either count. A cusp where the class vanishes (B1369's free cusp) keeps the cusp's continuum, whose bottom is zero, and it carries the whole count. So a non-zero count forces an unsealed end, and the problem on the complete manifold is then not Fredholm: chirality and a well-posed problem exclude each other. sL-8's completion question concerns exactly the free cusps where the count lives, the ends where the Higgs field dies off and the broken gauge symmetry comes back at infinity.

**Date:** 2026-09-27 · **Seat:** cc (the SM-derivation branch) · **Occasion:** sL-8's first question ("which count does the physics
use?"), sharpened after the four kill tests. · **Status:**
- PROVED: the canonical representative, the growth dichotomy, the zero count's end contributions and the no-go.
- COMPUTED: the cusp algebra, exact (sympy), and the members' peripheral ranks.

The two spectral steps (Persson's criterion, Weyl's theorem) are cited in kind. **Fence:** the seat's frame; spin-0; the spectral
statements for the charged sectors' Witten-deformed form Laplacian. · **Price:** unchanged, 0 of 19 · **Numbering:** B1392.

## 0. Seen from above

B1388 found that the seat's count depends on where the cusps are cut, and blamed the continuum at the cusps: the problem on the
complete manifold is not Fredholm. B1369 found that a chiral generation needs a free cusp, one on which a Higgs class can vanish. This
arc joins the two and shows they are the same phenomenon.

For a Higgs class v and a cusp c there are two cases.
- **Sealed** (v does not vanish on the cusp torus). The canonical harmonic representative is α_c + (exponentially small), α_c the flat
  form of v on the torus.
  - Its norm grows like h·|α_c|.
  - The deformed Laplacian's potential T²|ω|² grows like h², and the Hessian term is smaller by a factor √2/(h|α_c|).
  - So the end adds no essential spectrum (Persson), and at large height the cut torus carries no Higgs zero and no boundary critical
    point: the end contributes **0** to the count.
- **Unsealed** (v vanishes on the cusp: B1369's free cusp, B1386's cuspidal case). The Higgs field is exponentially small up the cusp.
  - The deformation is a relatively compact perturbation there (Weyl), so the undeformed continuum survives.
  - For 1-forms that continuum is **[0, ∞)**: Δ(hˢ dx) = −s² hˢ dx on the L² borderline Re s = 0. This derives B1388's premise.
  - All of the count comes from such ends (B1387's leading-mode partitions; B1388's Morse boundary formula).

**The no-go.**
- If v seals every cusp, the deformed problem is Fredholm and its index is the signed number of Higgs zeros, which Morse's boundary
  formula makes 0.
- So N ≠ 0 needs an unsealed cusp, and there the problem is not Fredholm. In this frame, **chirality and a well-posed problem on the
  complete manifold exclude each other.**
- A generic class seals every cusp (every cusp's peripheral rank is ≥ 1 on all 100 members computed). Chirality needs the special
  classes that vanish on free cusps: 86 free cusps on 35 of the 99 arithmetic census members plus cube~3.24.

**What this says about sL-8.** The count is carried by the ends where the Higgs field dies off, which are the ends where the gauge
symmetry it breaks is restored at infinity. That is where B1389 said the anomaly must be carried. sL-8's first question is therefore
not decided by a better analysis of the complete manifold, since there is none: its answer is whatever completes the free cusps.

## 1. The theorem

Let M be a cusped finite-volume hyperbolic 3-manifold with cusp coordinates (x, y, h) and metric (dx² + dy² + dh²)/h² in each end.
Let v ∈ H¹(M; ℝ).

**Lemma 1 (the canonical representative).** v has exactly one harmonic representative ω whose primitive is bounded in every cusp.
Near cusp c it is α_c + (exponentially small), α_c the flat (constant-coefficient) form of v|_{T_c}.
*Proof.*
- **The start.** Take a closed ω₀ representing v with ω₀ = α_c on each end. The form α_c is closed and co-closed (§2), so δω₀ is
  compactly supported. Its integral is 0: α_c has no dh-component, so no flux through the horospheres.
- **Solving.** The function Laplacian of a finite-volume hyperbolic 3-manifold has 0 as an isolated eigenvalue (its essential spectrum
  is [1, ∞)). So ΔF = −δω₀ has a solution F ∈ L². It is harmonic on the ends, so it equals a constant plus exponentially small terms
  there: the harmonic functions of h alone are h⁰ and h², and only h⁰ is L² (§2). Then ω = ω₀ + dF.
- **Uniqueness.** Two such representatives differ by dE with E harmonic and bounded, so L², so constant. ∎

For a cuspidal v this is B1387's L² form.

**Theorem (the ends carry the chirality).** For a charged sector, let Δ_T be the Witten-deformed Hodge Laplacian of d_{Tω}, T > 0.
1. **(sealed)** If α_c ≠ 0:
   - |ω|_g = h|α_c|(1 + o(1)) and |∇ω|_g = √2·h|α_c|(1 + o(1)), so Δ_T's potential T²|ω|² − O(T|∇ω|) → ∞ up the cusp, and the end
     contributes no essential spectrum (Persson);
   - at large height the cut torus's function f = F(·, T) has gradient α_c + o(1) ≠ 0, so the end holds no Higgs zero and its term
     Φ_c in Morse's boundary formula (B1388, Theorem A) is 0.
2. **(unsealed)** If α_c = 0:
   - ω is exponentially small up the cusp, so Δ_T − Δ_0 there is a decaying zeroth-order term and the end keeps Δ_0's essential
     spectrum (Weyl);
   - on 1-forms this reaches 0: the continuum [0, ∞) of §2.
3. **(the no-go)**
   - If every cusp is sealed, Δ_T is Fredholm for large T. Its index is the signed number of Higgs zeros (Witten's localization,
     with confining ends), and that number is Σ_c Φ_c = 0.
   - If N ≠ 0, some cusp is unsealed, and Δ_T is not Fredholm. ∎

*Remarks.*
- (3) uses Witten's localization with confining ends. The cusp ends lack bounded geometry, so Dai–Yan's theorem (arXiv 2005.04607,
  which needs injectivity radius > 0 and lim inf |∇f| > 0) does not apply verbatim. The step is cited in kind.
- On a free cusp the count is the leading-mode partition's −χ(∂⁺_c) (B1351 (ii), B1387) or Φ_c at a cut (B1388). Both are data of
  the unsealed end.

## 2. Computed (`verification/ends.py`, about two minutes; record `ends_run.txt`)

**The cusp, exact (sympy):**

| quantity | result |
|---|---|
| a dx + b dy (constants) | closed and co-closed; \|ω\|² = h²(a² + b²) |
| co-closed forms c(h) dh | c = C h, i.e. d(C h²/2) |
| Δ hˢ | −s(s − 2) hˢ; harmonic for s = 0, 2; L² up the cusp only s = 0 |
| \|∇ω\|² for ω = a dx + b dy | 2h²(a² + b²); \|∇ω\|/\|ω\|² = √2/(h√(a² + b²)) → 0 |
| Δ_H(hˢ dx) | −s² hˢ dx; δ(hˢ dx) = 0; L² borderline Re s = 0, where −s² = ν²: the continuum [0, ∞) |

**The members** (per cusp, the rank of its peripheral image in H₁(M; ℚ); B1369's instrument, SnapPy's fundamental group):
- The 99 arithmetic census members of B1390 and cube~3.24 have 169 cusps, and the minimum peripheral rank is 1. So a generic class
  seals every cusp.
- There are 86 free cusps on 35 members. That is B1369's 83 on the family, less t06828's one (non-arithmetic, B1390), plus cube~3.24's
  four.
- On cube~3.24 (b₁ = 5, ranks 2, 1, 1, 2) the classes vanishing on all four cusps are the cuspidal line, v₊ (B1386). It is unsealed
  everywhere, which is why its count is carried entirely by its cusps.

## 3. What this settles, and what it does not

**Settled.**
- **The frame's chirality is an end effect.** Sealed ends are inert and well-posed, and the count lives in the free cusps' asymptotic
  data.
- **So there is no Fredholm version of the count** on the complete manifold to appeal to. sL-8's first question ("which count?") has
  no answer internal to the complete manifold. Any definite count is a statement about what completes the free cusps.
- **The same ends restore the broken gauge symmetry at infinity** (the Higgs field vanishes there). They are where B1389's anomaly
  must be carried.

**Not settled.** What the completion is. Candidates to test, none chosen here:
- a conical point at each free cusp, the one-point compactification, where chiral matter could localise as at the Higgs zeros (both
  are points where the Higgs field vanishes);
- a physical wall at a cut, whose boundary modes B1388's relative index counts;
- a Dehn filling. Closed members are vector-like (B1351), so a smooth filling kills the count.

sL-8's rule stands: none may be chosen because it rescues a count. 0 of 19.

## 4. Fences

- **The frame's.** Spin-0; the charged sectors' Witten-deformed form Laplacian.
- **The spectral steps** (Persson, Weyl, Witten's localization with confining ends) are standard and cited in kind. The algebra they
  rest on is computed exactly.
- **Numerical.** None: the ranks are exact over ℚ.

## 5. Prior art (swept before banking)

Both branches were swept: this one at 8f9ebc3f (B1391), origin/main at 987c0c8f. The sweep used git grep for "Fredholm", "continuous
spectrum", "essential spectrum", "Persson", "sealed" and "unsealed" (the last two occur only in the sense of a sealed test).
- **B1388** states the non-Fredholm premise for cube~3.24's v₊.
- **B1369** proves that a generation needs a free cusp.
- **B1351 (ii) and R23** give the count and its conventions.
- **No arc** relates the two, derives the continuum, or shows that a class sealing every cusp is vector-like.
- **The literature:**
  - Dai–Yan (2020; well-tame Witten deformation on non-compact manifolds, relative cohomology of a pair);
  - Golénia–Moroianu (Trans. AMS 364, 2012; the essential spectrum of form Laplacians on conformally cusp manifolds);
  - Mazzeo–Phillips (Duke 60, 1990; Hodge theory on hyperbolic manifolds);
  - Helffer–Nier and Le Peutrec (the Witten Laplacian with boundary).

*(Currency 2026-09-28, B1393.) The sealed ends are the flat-twist form of main's B1297 T5 (only cusp-invariant local systems can be
chiral), a parallel this section missed. B1393 shows the count at the free cusps is made by the charge flip. With one condition for
both charges it vanishes, and on cube~3.24's cuspidal twist it vanishes at every real coupling.*
