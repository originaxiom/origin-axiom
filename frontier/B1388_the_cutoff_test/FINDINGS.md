# B1388 — THE CUTOFF TEST (kill test 1, sealed): UNSTABLE. The sealed count on cube~3.24 depends on where the cusps are cut, so, as sealed, the physical reading of B1386/B1387 is retired. After the seal, the anatomy: the sealed count (a relative index at the cut) and the signed number of Higgs zeros are different things that agree only far up the cusps. B1387's +2 is exactly minus the signed number of Higgs zeros on the whole manifold. All six zeros near the Eisenstein cusps lie on the surface equidistant from them, three of them exactly where the two cusp neighbourhoods first touch. So on every cut that respects the manifold's symmetry no zero is lost and the zero count stays +2, while the relative index still dips to −4 in a thin window.

**Date:** 2026-09-27 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's "how do we continue bravely"; the answer
adopted was to try to break the one positive result before building on it · **Seal:** `PREREGISTRATION.md`, committed and pushed
at 68c1b809 before any height-dependent partition was computed; sha256 in `docs/SEAL_LEDGER.md` · **Status:** NEGATIVE, as sealed,
for the physical reading; the mathematics of B1386/B1387 unchanged; the post-seal anatomy (§3) is unsealed and banked as computation,
not as a verdict · **Fence:** the seat's frame, spin-0 half · **Price:** unchanged, 0 of 19 · **Numbering:** B1388.

## 0. Seen from above

**The sealed question.** B1387 computed N(v₊) = ±2 by reading each cusp's partition ∂⁺ = {ω_t > 0} at asymptotically large height.
The sealed question was whether the count survives moving the cut through the region where each cusp's torus is embedded.

**It does not.** The sealed run's record, with the partition's Euler characteristic recomputed from the full harmonic form at every
cut height:

| cusp | embedded range (τ = height/√covol) | χ(∂⁺) on the sealed grid, as the cut rises | first changes in each bracket, bisected |
|---|---|---|---|
| 0 (Eisenstein) | [0.0895, ∞) | +4, +8, +2, −1 | 0.0986, 0.1053, 0.1867 |
| 3 (Eisenstein) | [0.0895, ∞) | +4, +8, +2, −1 | 0.0986, 0.1053, 0.1867 (cusp 0's to 10⁻⁴: the swap, unimposed) |
| 1 | [0.1266, ∞) | 0 throughout | none |
| 2 | [0.1791, ∞) | 0 in the reliable range | a spurious one at τ ≈ 2.77, a symmetry-killed shell's numerical residue (§2) |

The sealed criterion reads this as **UNSTABLE**: the count moves under admissible cuts. Cutting cusp 0 below 0.1867, with the others
high, gives N = −1, −7, −6 or −3 instead of +2 (§3.5).

**After the seal: what actually moves (§3).** Two counts must be told apart.
- **The relative index** −χ(∂⁺M_T). This is the seat's frame and the sealed quantity.
- **The Higgs-zero count**, minus the signed number of zeros of ω inside M_T. Morse's boundary formula gives it exactly from data on
  the cut.

The two agree far up every cusp, so B1387's +2 is minus the signed number of Higgs zeros on the whole cusped manifold. At a finite
cut they part.
- **The relative index changes wherever ∂_hF has a critical point on its zero level.** Off the rotation axes those are tangencies:
  the Higgs field turns tangent to the cut without vanishing. That happens at 0.0986, 0.1053 and 0.1867, the three bisected
  transitions, where the field's horizontal part is 0.11–0.44 of its maximum.
- **The zero count changes only where a Higgs zero crosses the cut.**
- **Six zeros sit in the Eisenstein cusp regions, all on the surface equidistant from cusps 0 and 3.**
  - Three lie on the rotation axes, one per axis, at the axis midpoint (τ = 0.1034; indices +1, −1, +1). There the horizontal
    gradient vanishes by symmetry, so tangency and zero coincide and both counts move together. The sealed grid stepped over this:
    a finer scan shows χ = +7 on (0.0986, 0.1034).
  - Three, an orbit of the rotation, lie exactly where the neighbourhoods of cusps 0 and 3 first touch (τ_joint = 0.1790950; index
    −1 each). The offset is 8·10⁻⁶ in height at mode cut-off 14 and 6·10⁻⁸ at cut-off 20.
  - Their indices sum to −2, which is −N.
- **A cut that respects the manifold's symmetry never loses a zero.** Such a cut takes cusps 0 and 3 at the same height, which the
  joint embedding forces to be at least τ_joint. On every such cut the zero count is +2. The relative index is −4 on
  [0.1791, 0.1867) and +2 above.
- **A cut that breaks the symmetry moves both counts.**

**What this does and does not say.**
- *As sealed,* the reading "the manifold protects a chiral index of two" is retired: the seat's count moves with the cut. The
  physical readings of sL-6 and sL-7 are withdrawn pending a derivation of the cutoff.
- *It keeps* B1386's L4, B1387's coefficients and the asymptotic partition, and gives B1387's number an intrinsic meaning: the number
  of index-1 Higgs zeros minus the number of index-2 ones, on the complete manifold.
- *It does not reinstate anything.* That the zero count survives on symmetric cuts was found after the seal. Choosing that definition
  because it survives would be choosing the question after seeing the answer. Which count the physics uses, and whether the
  completion respects the symmetry, is registered as sL-8 and must be settled on its own terms.
- *It sharpens R23 into an exact dichotomy with a computed consequence.* A count at a cut is either the index of a boundary problem,
  which here sees the cut, or a count of localized modes at Higgs zeros, which here does not on symmetric cuts. The completion is
  where that is decided, and it is the first place in the chain where physics is unavoidable rather than optional.

## 1. The seal

- **Sealed:** `PREREGISTRATION.md` at 68c1b809, before any height-dependent partition was computed.
- **Declared prior:** STABLE, about 55%.
- **The criterion:**
  - STABLE: every cusp's χ(∂⁺_{c,T}) constant on [τ_emb(c), 20 τ_emb(c)] and equal to the leading-shell value;
  - UNSTABLE otherwise;
  - an unresolvable transition counts as UNSTABLE.
- **The consequence, fixed in advance:** NEGATIVE for the physical reading of B1386/B1387, with the transition heights reported,
  and the physical readings of sL-6 and sL-7 withdrawn.
- **What the seal did not fix, and the anatomy supplies:**
  - *The ranges.* They are individual ones: each cusp's own maximal neighbourhood, the others shrunk. A single-cusp cut with the
    others high is a genuine truncation, so the verdict stands; the joint constraint is in §3.5.
  - *The count.* It is the relative index, which is the frame as sealed.
  - *The resolution.* The bisection finds the first change inside each grid bracket. The finer scan of §3.3 lists every change.

## 2. Computed (the sealed test)

`verification/cutoff_test.py` is the sealed test (record `cutoff_test_run.txt`). `verification/cutoff_checks.py` holds the checks
that separate the harmonic form from the truncation (record `cutoff_checks_run.txt`).

- **The banked identity, reproduced first.** B1387's asymptotic invariants to 1%, the χ pattern (−1, 0, 0, −1), and the cusp shapes.
- **The embedded ranges** (SnapPy's cusp neighbourhoods at each cusp's own reach, the other cusps shrunk).
  - Maximal volumes: 36√3, 18√3, 9√3 and 36√3 (62.354, 31.177, 15.588, 62.354).
  - So τ_emb = 0.0895, 0.1266, 0.1791, 0.0895.
- **The scan.** Forty heights per cusp over [τ_emb, 20 τ_emb]. Each partition is counted by B1386's Morse count, completed, with
  the grid agreeing wherever the partition is resolved. A field so close to one direction that its critical points are not isolated
  is decided by the grid, and flagged. Every change is bisected to 10⁻⁶.
- **The Eisenstein transitions are the harmonic form's, not the truncation's.**
  - *Resolution.* Raising the mode cut-off from 14 to 20 (fit residual 3·10⁻⁵ → 6·10⁻⁷) leaves the transitions at 0.0986/0.0984,
    0.1053/0.1052 and 0.18668/0.18669.
  - *The swap.* Cusp 3's coefficients are fitted independently, and its transitions agree with cusp 0's to 10⁻⁴ (0.18669
    against 0.18668). The swap symmetry is never imposed.
  - *Accuracy at the deciding height.* At τ = 0.187 the neglected modes are below e^{−2π·20·0.187} ≈ 10⁻¹⁰ of the leading term.
  - *An independent reading* (check (b)). At τ = 0.12 and 0.15, the torus function is also read without cusp 0's own coefficients:
    each point is pulled into the manifold and F is taken from another cusp's expansion, at heights 0.104 and above. It agrees with
    cusp 0's expansion to 1.8·10⁻⁵ and 4.3·10⁻⁵ of its maximum. All 8100 signs agree, and so does χ (+2).
- **Cusp 2's high transition is an artefact** (check (c)). Cusp 2's first shell is killed exactly by the order-3 translation (B1386
  S4); the solve returns it at 6.7·10⁻⁶ (cut-off 14) and 8.4·10⁻⁸ (cut-off 20). It decays as e^{−2π·1.075τ}, against the leading
  √3-shell's e^{−2π·1.861τ}, so far up the residue must dominate.
  - As solved, cusp 2 has a transition at τ = 2.765 at cut-off 14. At cut-off 20 the transition has moved out of the range.
  - With the killed shell set to its exact value, zero, cusp 2 is annular (χ = 0) throughout its range, at both cut-offs.

## 3. After the seal: the anatomy (unsealed; `verification/higgs_zeros.py`, record `higgs_zeros_run.txt`)

### 3.1 Two counts, and the identity between them

Let V = ∇F on the truncation M_T (χ(M_T) = 0), and at the cut over cusp c let f = F(·, T) and g = ∂_hF(·, T).

**Morse's boundary formula** (Morse 1929; Pugh 1968) is Ind V + Ind ∂₋V = χ(M_T), where ∂₋V is the tangential projection of V on
the part of the cut where V points inward. That projection is ∇f up to a conformal factor, and it is non-zero where V is tangent to
the cut. So, exactly and with no correction term:

  Σ over the zeros of ω in M_T of their indices = Σ_c Φ_c(T_c), where Φ_c(T) = Σ over the critical points of f with g > 0 of their
  indices.

- Φ_c changes only when a Higgs zero crosses the cut.
- χ(∂⁺_{c,T}) = χ({g > 0}) changes when g has a critical point on its zero level.
- The two agree whenever ∇f points out of {g > 0} all along {g = 0}. That holds at large height: there the leading shell gives
  f = a(h)φ and g = a′(h)φ with a·a′ < 0, and φ has no critical point on its zero level (B1387's gap 0.13).

**Theorem A (the asymptotic count is a zero count).** For a cuspidal Higgs class whose leading shells have no critical point on
their zero level, the seat's asymptotic count N = −Σ_c χ(∂⁺_c) equals minus the signed number of zeros of ω on the complete cusped
manifold: the number of Morse-index-1 zeros minus the number of Morse-index-2 zeros. (Harmonicity leaves no index 0 or 3.) For
cube~3.24's v₊ this is +2.

### 3.2 The zeros

A direct search solves dF = 0 by Newton in (s, t, h), seeded on a grid over each cusp's range, at mode cut-offs 14 and 20. Every
zero passes the harmonicity check: at a zero, Δ_hyp F = h²·tr Hess F, so the Euclidean Hessian is traceless (to 10⁻¹⁶). Each zero
is pulled into the manifold and its height over the other Eisenstein cusp is read, which identifies zeros seen from two charts.

| zeros | where | τ | indices | identification |
|---|---|---|---|---|
| three | on the three axes of the rotation R, one each | 0.1034 | +1, −1, +1 | the axis midpoint. All three sit at τ = 0.10340 ± 5·10⁻⁶ at cut-off 20 (0.1033–0.1037 at 14). Where the containing tetrahedron shows both cusps, the heights over cusps 0 and 3 agree to 7·10⁻⁶ at cut-off 20 (3·10⁻⁴ at 14). Each axis carries exactly one zero: dF/dh along it changes sign once in [0.0895, 0.40] |
| three | an R-orbit | 0.1790950 | −1 each | where the neighbourhoods of cusps 0 and 3, grown together, first touch: the midpoints of the shortest orthogeodesics between them. Offset from the touching points ≤ 8·10⁻⁶ at cut-off 14 and ≤ 6·10⁻⁸ at 20, and at 20 the heights over the two cusps agree to 10⁻⁷; \|dF\| there falls from 4·10⁻⁶ to 10⁻⁷ of scale |

- **The two charts see the same six.** Each Eisenstein chart finds all six, index sum −2.
- **The total.** The indices sum to −2, which is −N, so these six carry the whole count. Any further zeros, in the thick part, which
  was not searched, would cancel in pairs.
- **Cusp 1** has no zeros in its range.
- **Cusp 2's zeros are spurious.** Its expansion shows zeros far up: at τ ≈ 2.5–2.75 at cut-off 14, and at 3.4–3.5 at 20. They move
  up as the killed shell's residue shrinks (6.7·10⁻⁶ → 8.4·10⁻⁸) and vanish when that shell is set to its exact value, zero. This is
  the same artefact as cusp 2's spurious χ transition.
  - Above τ ≈ 1.2 the residue competes with a leading shell that is nearly one-directional, so cusp 2's Morse count is unreliable
    there. Four of its twelve searches are incomplete, and the count jumps between 1.21 and 1.58.
  - With the killed shell zeroed there are no zeros at all in cusp 2's range, so the zero count there is its asymptotic 0.

**What symmetry explains and what it does not.** Every isometry preserves v₊ (ε = +1), so dF at a fixed point lies in the
fixed directions.
- On an axis of R, dF points along the axis. A zero there is one condition, dF/dh = 0.
- At a point fixed by one of the involutions (each swaps cusps 0 and 3), dF points along that involution's axis. A zero there is again
  one condition.
- A point fixed by both R and an involution has no fixed direction, so a zero there is forced. The axis midpoints would be such points
  if each involution reverses each axis. That is not checked here.
- Nothing in Isom(M) = D₃ forces the orbit zeros onto the touching points. The coincidence is observed to 6·10⁻⁸ and sharpens with
  resolution. A hidden symmetry of this arithmetic manifold is the natural suspect. **Open.**

### 3.3 Every change of the two counts (cusp 0; cusp 3 identical)

A fine scan at cut-off 14 (sixteen heights around the brackets, both counts) together with the zero census:

| height (cut-off 14; 20) | event | Δχ (relative index) | ΔΦ (zero count) | \|∇ₓF\| / max there |
|---|---|---|---|---|
| 0.0986 (0.0984) | tangency: an R-orbit of saddles of g off the axes | +3 | 0 | 0.405 |
| 0.1033–0.1037 (0.1034) | the three axis zeros | +1, −1, +1 | +1, −1, +1 | 0, by symmetry |
| 0.1053 (0.1052) | tangency: two R-orbits of maxima of g | −6 | 0 | 0.335–0.437 |
| 0.1791 | the orbit zeros, at the touching points | 0 | −3 | 0 |
| 0.1867 | tangency: an R-orbit of saddles of g | −3 | 0 | 0.108 |

So as the cut rises:
- the relative index χ(∂⁺₀) runs +4, +7, +8, +2, +2, −1;
- the zero count Φ₀ runs +1, +1, +2, +2, −1, −1.

They agree on (0.1053, 0.1791) and above 0.1867. They differ by three or six elsewhere, by the tangencies.

- **Off the axes,** a zero crosses the cut transversally to the partition, so χ does not see it. A tangency is not a zero, so Φ does
  not see it.
- **On the axes** the two coincide.

The sealed grid (ratio 1.08) put the first tangency and the axis zeros in one bracket, which is why it recorded +4 → +8 there.

### 3.4 The two counts side by side (cusp 0; cusp 3 identical)

| cut τ | 0.095 | 0.100 | 0.104 | 0.120 | 0.183 | 0.250 |
|---|---|---|---|---|---|---|
| Φ₀ (Higgs zeros, Morse) | +1 | +1 | +2 | +2 | −1 | −1 |
| χ(∂⁺₀) (relative index) | +4 | +7 | +8 | +2 | +2 | −1 |

At τ = 0.183 the orbit zeros sit just below the cut. They are counted by Φ, and the relative index has not yet made its tangency
transition.

### 3.5 Admissible cuts

The neighbourhoods of cusps 0 and 3 can be grown together only to volume 9√3 each, where they touch (τ_joint = 0.1790950). So a cut
is admissible only if τ₀·τ₃ ≥ τ_joint² = 0.03207, and each τ ≥ 0.0895, with cusps 1 and 2 small. Equal cuts below 0.1791 overlap.
This corrects the pre-anatomy draft: its "−16" and "−8", and "−4" below 0.1791, were not truncations.

| admissible cut | relative index N_rel | zero count N_zero |
|---|---|---|
| symmetric, τ₀ = τ₃ ≥ 0.1867 | +2 | +2 |
| symmetric, τ₀ = τ₃ ∈ [0.1791, 0.1867) | −4 | +2 |
| cusp 0 at τ₀ ∈ (0.1053, 0.1867), cusp 3 high | −1 | −1 below 0.1791, +2 above |
| τ₀ ∈ (0.1034, 0.1053) | −7 | −1 |
| τ₀ ∈ (0.0986, 0.1034) | −6 | 0 |
| τ₀ ∈ [0.0895, 0.0986) | −3 | 0 |

Cusps 1 and 2 contribute 0 to both counts at every admissible height.

## 4. The statements

**Theorem (the cutoff dependence, sealed and computed).** On cube~3.24 the seat's count N(T) = −χ(∂⁺M_T) of the class v₊ depends on
where the cusps are cut within admissible truncations.
- χ at cusps 1 and 2 is 0 at every admissible height.
- χ at cusps 0 and 3 is:
  - −1 for τ > 0.1867;
  - +2 on (0.1053, 0.1867);
  - +8 on (0.1034, 0.1053);
  - +7 on (0.0986, 0.1034);
  - +4 on [0.0895, 0.0986).
- N = +2 exactly when both Eisenstein cusps are cut above 0.1867.

*Evidence:* §2, refined by §3.3.

**Theorem A (proved; §3.1).** The asymptotic count is minus the signed number of Higgs zeros on the complete manifold.

**Proposition B (computed; §3.2).** v₊'s Higgs field has six zeros in the Eisenstein cusp regions, all on the surface equidistant
from cusps 0 and 3.
- Three sit at the midpoints of R's axes (+1, −1, +1).
- Three sit at the points where the two cusp neighbourhoods first touch (−1 each).
- They sum to −N. The touching-point coincidence is observed, not proved.

**Corollary C (computed; §3.5).** On every admissible cut that respects the isometries, the zero count is +2. On the same cuts the
relative index is −4 in [0.1791, 0.1867). Asymmetric cuts move both.

## 5. What it means

- **The brave test came back negative, and the negative is banked as sealed.** The seat's count, a relative index at the cut, moves
  with the cut. The physical reading of B1386/B1387 is retired as sealed.
- **The negative has an anatomy, and it is informative.**
  - Far up the cusps the relative index and the zero count agree. There B1387's +2 is intrinsic: two more index-1 than index-2
    zeros of the Higgs field on the complete manifold.
  - Down the cusps they part.
    - The relative index sees the cut, through tangency.
    - The zero count sees only the zeros. On this member every zero near the Eisenstein cusps sits on the surface equidistant from
      them, so no symmetric cut ever reaches one.
- **This is exactly R23, made computable.** Main's paper (S17) asks for the boundary definition. Here the two candidate definitions
  are written down, shown to agree asymptotically, and shown to differ by a computed amount at a finite cut. Which one a physical
  completion realises is sL-8, and must be settled on its own terms.
- **What is not claimed.** The zero count's stability on symmetric cuts is post-seal and is not a verdict. Neither count is a
  protected (Fredholm) index on the complete manifold: the prereg's premise, the continuum at the cusps, stands. No physics is
  crossed.
- **The other two tests come after the definition.** Until sL-8 says which count is physical, a spectrum per completion (test 2) or a
  level (test 3) cannot be read.

> **Currency (2026-09-27, B1392): the premise derived and generalised.**
> - The 1-form continuum at a cusp starts at 0 (Δ(hˢ dx) = −s² hˢ dx on the L² borderline). The count is carried only by cusps where
>   the Higgs class vanishes, which are exactly the ends that keep this continuum.
> - A class sealing every cusp is Fredholm with N = 0.
> - So the cut dependence found here is the general situation, not a feature of cube~3.24. `frontier/B1392_the_ends_carry_the_chirality`.

## 6. Fences

- **The frame.** The seat's, spin-0 half. The sealed test concerns the relative index. The zero count is a second definition,
  introduced after the seal.
- **Numerical.** Double precision; not certified.
  - The transitions are confirmed by refinement and by the unimposed swap.
  - The zeros are confirmed by refinement (cut-offs 14 and 20), by the harmonicity check, by the cross-chart heights and by Morse's
    count.
  - The touching-point and midpoint coincidences are numerical.
- **The zero census.** It covers the embedded cusp regions only. The thick part was not searched, and the six zeros found account for
  the total.
- **Admissibility.** Computed from SnapPy's cusp neighbourhoods. The joint constraint is between cusps 0 and 3, with cusps 1 and 2
  shrunk. Cusps 1 and 2 contribute nothing at any height.
- **The motivation.** The owner's "continue bravely". Nothing rests on a philosophical premise.

## 7. Files

- `PREREGISTRATION.md` — the seal.
- `verification/cutoff_test.py`, `verification/cutoff_test_run.txt` — the sealed test.
- `verification/cutoff_checks.py`, `verification/cutoff_checks_run.txt` — the checks (resolution, other-chart reading, cusp 2's
  residue).
- `verification/higgs_zeros.py`, `verification/higgs_zeros_run.txt` — the anatomy (post-seal): the joint embedding, the zeros and
  their identification (with cusp 2's residue test), the axes, the touching points, Morse's count against the relative index, and
  the transition points.
- `verification/fine_scan.py`, `verification/fine_scan_run.txt` — both counts at sixteen heights around the brackets (§3.3).
- `tests/test_b1388_the_cutoff_test.py` — the lock.
  - At τ = 0.15 and 0.25 the relative index is +2 and −1 at both Eisenstein cusps, and cusp 1 is annular.
  - At τ = 0.183 Morse's count is −1 while the relative index is +2.
  - The orbit zeros sit at the joint touching height.
