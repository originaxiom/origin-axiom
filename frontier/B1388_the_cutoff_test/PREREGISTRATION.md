# B1388 PREREGISTRATION — THE CUTOFF TEST: is cube~3.24's chiral index independent of where the cusps are cut off?

**Sealed 2026-09-27, before any height-dependent partition is computed. Seat: cc (the SM-derivation branch). Occasion: the owner's
"how do we continue bravely" — the first of three kill tests on the chirality mechanism (B1386, B1387).**

## The question

B1387 computed N(v₊) = ±2 for cube~3.24's cuspidal, isometry-invariant Higgs class v₊. It read each cusp's partition
∂⁺ = {ω_t > 0} from the *leading* Fourier shell of the harmonic form, i.e. at asymptotically large height (B1370 §1's
definition).

v₊ is cuspidal, so its Higgs field decays at every cusp, and the zero-mode problem is not Fredholm there: the 1-form Laplacian of a
hyperbolic cusp has continuous spectrum down to 0, and a decaying Higgs field does not change that. So the count is not canonically
defined on the complete manifold. It is χ(M_T, ∂⁺M_T) for a truncation at heights T = (T_c), set by whatever global geometry
completes the cusps. Since χ(M_T) = 0, N(T) = −Σ_c χ(∂⁺_{c,T_c}).

If χ(∂⁺_{c,T}) changes as T moves through the region where cusp c's horospherical torus is embedded, then the count depends on the
cutoff. In that case "protected chirality" is a property of a regularization, not of the manifold.

## Method (fixed now)

- **The form.** B1387's instrument (`frontier/B1387_the_index_computed/verification/harmonic_cusp_form.py`), unchanged, at
  K_n = 14, sample height τ = 0.10, chart seed 1, sample seed 1: the full expansion F_c = A_c + Σ c_k t K₁(2π|k|t) e^{2πik·x} at
  every cusp.
- **The torus functions.** For cusp c and chart height T,
  g_{c,T}(x) = ∂F_c/∂h at h = T = Σ_k c_k (−2π|k| T K₀(2π|k|T)) e^{2πik·x}, using every computed mode, and
  ∂⁺_{c,T} = {g_{c,T} > 0}.
- **The count.** χ(∂⁺_{c,T}) by B1386's Morse count (`the_open_cusp.morse_chi`, refined until complete), with its triangulated
  grid (`chi_grid`, n = 240) as cross-check wherever every critical value is at least 10⁻² of the maximum from zero.
- **The range.** The embedded range of cusp c is τ ≥ τ_emb(c) = 1/√A_max(c), where A_max(c) = 2 × the volume of cusp c's
  maximal individually-embedded neighbourhood (SnapPy's `cusp_neighborhood()`, `set_displacement(reach(c), c)`, `volume(c)`)
  and τ = T/√covol(Λ_c). The heights are a geometric grid of 40 values from τ_emb(c) to 20·τ_emb(c).
- **Transitions.** Every height interval on which the Morse count changes, or a critical value changes sign, is bisected to 10⁻⁶
  relative.

## BANKED IDENTITY:

Before any height-dependent number is read, the pipeline must reproduce inside itself B1387's asymptotic invariants and pattern.
- **Invariants, to 1%:**
  - the first-shell |c|·√covol = 1.00695 at cusps 0 and 3, with triple-phase cosine 0.370;
  - cusp 1's leading one-direction coefficient 1.789;
  - cusp 2's √3-shell (0.335, 0.335, 2.209).
- **The χ pattern (−1, 0, 0, −1)** of the leading shells.
- **The cusp lattice shapes**, equal to SnapPy's cusp shapes.

If any of these fails, the run stops and nothing below is read.

## PRIOR ART:

The design-time bank grep, `scripts/checks/already_banked.py`, was run on three queries:
- "cutoff truncation height partition index cusp";
- "regularization boundary condition chiral index cusp R23";
- "partition stable truncation horosphere".

No arc tests the cutoff dependence of the index. The one "cutoff" hit, B1233 R2, concerns the j-function, not this. The relevant
record is:
- B1351 §2(ii) with its R23 scoping (whole-torus and annular conventions against disc conventions);
- B1352's partitions (annular, fc R71's region-swap instrument);
- B1370 §1 (the partition defined by the leading mode, at large height only);
- B1386's L4 and B1387's instrument.

Main's paper (S17) names the boundary definition as the chirality section's open question.

## The two outcomes (fixed now)

- **STABLE.** For every cusp c, χ(∂⁺_{c,T}) takes one value at every height of [τ_emb(c), 20·τ_emb(c)], and that value equals the
  leading-shell value (−1, 0, 0, −1). Then N(T) = ±2 for every admissible truncation: every tuple of cutoffs inside the embedded
  cusp regions.
  - *Banked as:* the count is a property of the manifold and the class, not of where the cusps are cut, provided the cut lies in the
    cusp region.
  - The convention question (R23) then narrows to "does the global completion cut inside the embedded cusp region?"
- **UNSTABLE.** For some cusp c, χ(∂⁺_{c,T}) changes within [τ_emb(c), 20·τ_emb(c)]. Then N depends on the cutoff.
  - *Banked as NEGATIVE* for the physical reading of B1386/B1387 ("symmetry-protected chirality"), with the transition heights
    reported.
  - The mathematics of B1386/B1387 (the asymptotic partition, L4, the computed coefficients) stands.
  - The physical reading of sL-6/sL-7 is withdrawn pending a derivation of the cutoff.
- **Unresolvable transitions.** A transition that bisection cannot resolve, with a critical value within 10⁻⁶ of zero across the
  bracket, counts as **UNSTABLE**. That is the conservative choice.

## Declared prior

STABLE, about 55%.
- Cusps 1 and 2 are annular, with a leading shell 6.6 times dominated by one direction, and should stay annular.
- At cusps 0 and 3 the first shell leads with a critical gap of 0.13 asymptotically, but near τ_emb more modes contribute and a
  critical value could cross zero.

## Fence

The seat's frame, for the spin-0 half. This tests the cutoff dependence of the sign-partition count, not the sign-partition
convention itself, and not whether a global completion exists.
