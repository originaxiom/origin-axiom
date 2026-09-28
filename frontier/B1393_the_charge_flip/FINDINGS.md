# B1393 — THE CHARGE FLIP: the seat's count is an index only because the frame's end condition flips with the charge. When both charges see the same condition, the net chirality is one Betti number taken at q and at −q, and it is zero except at isolated couplings. On cube~3.24's cuspidal twist it is exactly zero at every real coupling: every twisted class restricts injectively to the cusps, and the Fox matrix drops rank only at the primitive cube roots of unity. So B1387's +2 is made entirely by the flip at the free cusps. The physical-bridge rounds say the same from the source side. The one computed completion that keeps a count carries a boundary flux sign(q)·k (R24). A free wall is its mirror (R25). Smoothed cores leave light pairs (R30–R31). sL-8's question becomes: what at a free cusp knows the sign of q·∂_hF?

**Date:** 2026-09-28 · **Seat:** cc (the SM-derivation branch) · **Occasion:** sL-8's completion question after B1392, and the
harvest, by citation, of the physical-bridge rounds: R23–R26 and R30–R31 as main's B1413 grades them, and R32–R34 and R54 as the
audit lane grades them (read here, not re-run). · **Status:**
- PROVED: the lemma. It is elementary: Poincaré–Lefschetz duality with local coefficients, plus semicontinuity along the coupling.
- COMPUTED, exact: cube~3.24's cuspidal twist on two presentations; the determinantal divisor over ℤ[t]; the jump points over three
  primes.
- HARVESTED: the physical-bridge rounds, quoted at the grades main (R23–R31) or the lane (R32–R34, R54) gives them.

**Not sealed.** The lemma decides the generic outcome; the computation checks it and locates the exceptions; nothing was chosen on its
result. **Fence:** the seat's frame; spin-0; the abelian Higgs twist; flat-twist cohomology (the algebraic counts), not the spectral
problem, which B1392 treats. · **Price:** unchanged, 0 of 19 · **Numbering:** B1393.

## 0. Seen from above

B1351 takes the net count of a charged sector from Pantev–Wijnholt: N_q = χ(M, ∂⁺M; L_q). Here ∂⁺ is the part of the boundary where
q·f increases outward, so for the opposite charge it is the complement. B1392 showed that the count lives at the free cusps and needs
a completion there. This arc asks what that flip does, and finds that it does everything.
- **The lemma.** An index formula computes net chirality only when the condition flips with the charge. Otherwise the net chirality
  is the same Betti number at q and −q, zero away from isolated couplings, however large the Euler characteristic of the pair.
- **The computation.** On cube~3.24's cuspidal twist, the seat's showcase, the charge-blind count is exactly zero at every real
  coupling. No twisted class is interior. B1387's +2 therefore comes from the flip alone.
- **The physical-bridge rounds.** They reach the same place from the other side. The only completion computed to keep a count supplies a
  charge-odd datum at the ends, and every smooth, free or filled completion is vector-like or mirrored.

## 1. The lemma

**Setting.**
- X is a compact oriented 3-manifold with boundary (a truncation M_T), and ω is a closed real 1-form.
- L_q is the flat real line bundle with monodromy exp(q∫ω). The operator d + qω∧ is d on L_q, conjugated by a local primitive.
- The charge-q sector carries relative conditions on A_q ⊂ ∂X and absolute conditions on B_q = ∂X ∖ A_q. The two parts meet in
  circles.
- n_q = dim H¹(X, A_q; L_q) is the sector's number of chiral multiplets in the frame (B1351).
- The net chirality of charge q is ν_q = n_q − n_{−q}.

**Lemma (the charge flip).**
- **(a) Duality.** dim H^k(X, A; L_q) = dim H^{3−k}(X, B; L_{−q}). This is Poincaré–Lefschetz duality with local coefficients for the
  triad (X; A, B), with L_q* = L_{−q}. On harmonic representatives it is the Hodge star, which carries d + qω to the adjoint of
  d − qω and exchanges relative and absolute conditions.
- **(b) The flip.** Suppose A_{−q} = B_q.
  - Then ν_q = h¹ − h² of the single pair (X, A_q; L_q), which is −χ(X, A_q) + h⁰(X, A_q; L_q) − h⁰(X, B_q; L_{−q}).
  - This is topological: minus B1351's N_q, up to the two h⁰ terms. Those terms vanish whenever the twist is non-trivial, as in every
    charged sector of a non-zero Higgs class.
- **(c) Blind.** Suppose A_{−q} = A_q = A.
  - Then ν_q = h¹(X, A; L_q) − h¹(X, A; L_{−q}): one Betti number at two couplings.
  - Along the real family s ↦ L_s, each coboundary matrix (Fox or cellular) has maximal rank off the common zeros of its maximal
    minors. That set is real-analytic in s, so it is discrete unless it is all of ℝ. Hence h¹(X, A; L_s) is one constant off a
    discrete set, the same for s > 0 and s < 0.
  - So ν_q = 0 except on a discrete set of couplings, whatever χ(X, A) is.
  - The same holds for any condition the two charges share, in particular main's interior-image count (B1297). Its identity
    I(V*) = −I(V) (T1) is (a) in that setting.
- **(d) Sealed ends.** These are the case with nothing to flip (B1392): the Higgs field is tangent to the far cusp tori, and the end
  contributes 0.

*Proof.*
- (a) is the duality stated, applied with L_q* = L_{−q}.
- (b): n_{−q} = h¹(X, B_q; L_{−q}) = h²(X, A_q; L_q) by (a) with k = 2. Then h¹ − h² = −χ + h⁰ − h³, and
  h³(X, A_q; L_q) = h⁰(X, B_q; L_{−q}) by (a) with k = 3. Finally χ(X, A; L) = χ(X, A), since L has rank one.
- (c) is the semicontinuity stated: h¹ = dim X¹ − rank δ¹ − rank δ⁰ on a cochain model whose matrices are analytic in s. ∎

**What it means.** An index formula computes net chirality only for a condition that flips with the charge. The frame's partition
flips (∂⁺_{−q} = ∂⁻_q), which is why B1351's χ is the frame's count. A completion that treats the two charges alike is vector-like
away from isolated couplings.

## 2. Computed: cube~3.24's cuspidal twist (`verification/charge_flip.py`, about 20 s; record `charge_flip_run.txt`)

**The twist.** The Higgs field in the cuspidal class v₊ (B1386) twists by L_t: g ↦ t^{v₊(g)}, with t = e^q. Charge −q is L_{1/t}.
The computation is Fox calculus on SnapPy's presentation of π₁ (8 generators, 7 relators, b₁ = 5), with v₊ read off as the classes
vanishing on all eight peripheral curves.

**A. The twisted numbers, exact over ℚ.**
- Definitions: a_k = h^k(M; L_t); r₁ = rank(H¹(M; L_t) → H¹(∂M; L_t)); n = a₁ − r₁ is main's interior image.
- Main's charge-blind index is I = n(L_t) − n(L_{1/t}).
- The check: r₁ + r₁* = t₁ = 8 (the annihilator property, B1297).

| t | a₁ | a₂ | r₁ | n | a₁ at 1/t | r₁ at 1/t | n at 1/t | I |
|---|---|---|---|---|---|---|---|---|
| 2, 3, 5, 3/2, 7/3, 11/4 | 4 | 4 | 4 | 0 | 4 | 4 | 0 | 0 |

**B. Where a₁ can jump.**
- The Fox matrix has rank 3 over ℚ(t), and every 4-minor vanishes identically, so a₁ = 4 generically.
- The gcd of its 1 960 maximal-rank minors is **9(t² + t + 1)²**, up to units. It has no positive real root.
- Hence, for every real coupling q ≠ 0:
  - a₁ = a₁* = 4;
  - r₁ + r₁* = 8 with r₁ ≤ 4 and r₁* ≤ 4, which forces r₁ = r₁* = 4;
  - so n = n* = 0 and I = 0.
- This holds exactly, not just at the sampled couplings. **At every coupling, every twisted class of the Higgs twist restricts
  injectively to the cusps, and no class is interior.**

**C. The lemma's two cases on one disc D in cusp 0 (t = 2).**
- Charge flip: ν = h¹(M, D; L_t) − h¹(M, ∂M ∖ D; L_{1/t}) = 5 − 4 = **1 = −χ(M, D)**.
- Charge blind: ν = h¹(M, D; L_t) − h¹(M, D; L_{1/t}) = 5 − 5 = **0**.
- Both relative groups come from the pair sequences.

**D. Second method.** On SnapPy's unsimplified presentation (49 generators, 48 relators; the same group through a different complex),
the numbers at t = 2 and 3/2 are the same.

**E. At the jump points.** Take t a primitive cube root of unity (the unitary order-3 twists along v₊), over F₇, F₁₃ and F₁₉:
a₁ = 6, r₁ = 4 and n = 2, for t and t⁻¹ alike. So I = 0 there too (B1297's T4, characters).

**Reading.** B1387's +2 is not an interior quantity. With a charge-blind condition cube~3.24's cuspidal twist gives 0 (the L² or
interior-image count, a wall with a fixed condition, a Dehn filling). The +2 is produced by the flip at the free cusps.

*Remark (cited in kind).*
- With B1392's canonical representative the primitive F is bounded on M. So e^{qF} is a bounded gauge transformation from d + qω to
  the flat bundle L_q with a quasi-isometric metric.
- If the interior image is the reduced L² cohomology for this bundle, the deformed Laplacian on the complete manifold has no L²
  harmonic 1-form on cube~3.24 at any coupling. That identification is Zucker's (Invent. Math. 70, 1982) and Mazzeo–Phillips's (Duke
  60, 1990) for trivial coefficients on the ends, and L_q is trivial on every end here.
- Then every candidate mode is in the continuum at the free cusps, as B1392 found.

## 3. The physical-bridge rounds, placed (by citation)

R23–R31 carry main's B1413 grades (the lane at 5e063851). R32–R34 and R54 carry the audit lane's own grades: they were read here at
8c5edc33 and aff8a569 and not re-run (RELAY_LEDGER).

| round | grade | what it says | in this arc's terms |
|---|---|---|---|
| R23 | PROVED-BY-SEAT within its setup | The charged differential is a two-flavour mass-Dirac operator. Bulk anomaly descent cancels a localized charge only by transporting it to the outer boundary. | The cusps carry the anomaly (B1389). |
| R24 | PROVED-BY-SEAT, topological | In R15's positive-source class the total mass-eigenline flux through the rounded source boundary is sign(q)·k. "Not a three-family selector". | A datum odd in q: the flip, supplied by sources. |
| R25 | PROVED-BY-SEAT within the free/product-collar ansatz | A free wall gives index −k opposite the interior +k: a mirror sector. | Interior plus wall is the blind count, 0. |
| R26 | conditional on R18/R19 | Bounded perturbations preserve the sourced sector (three odd, zero even). | The flip survives small smooth changes. |
| R30–R31 | CONDITIONAL; PROVED-BY-SEAT in the stated class | Smooth resolved cores with absolute boundary data have no zero modes at finite width for the two non-trivial C₃-compatible m202 characters. Strong shrinking wells give light opposite-chirality pairs. | Smoothing the sources makes them blind. |
| R32 | authored analytic argument with exact finite controls (the lane's grade) | "The actual C3 action fixes each of the three proper source arcs pointwise." The singular three/zero kernel is the regular C₃ representation, so each invariant projection keeps one mode; resolved cores keep the partners together. | The sources sit where B1390 puts every order-3 fixed set (cusp-to-cusp arcs), and their three is the regular representation: B1390's pullback three. |
| R33–R34, R54 | path-local authored analysis (the lane's grade) | Allowed interactions for the opposite-chirality partners exist (a Spin(10)-invariant mirror Yukawa with a charge-four phase-locking scalar; a non-zero four-fermion term), "not yet mirror removal". R54: both charged sides participate, with no mirror-only gap. | A fourth destination for the mirror, gapped by interactions, is open and not achieved. |

The two records agree. In every computed completion a count survives only where the ends carry charge-odd data (the sources). Every
smooth, free or filled completion is vector-like or mirrored.

## 4. What this settles, and what it does not

**Settled.**
1. The flip lemma.
2. On cube~3.24 the cuspidal twist has no interior class at any real coupling. So the +2 is made by the flip.
3. Charge-blind completions are vector-like away from isolated couplings, and exactly so on cube~3.24's twist. These are the Dehn
   filling (B1351 (i)), a wall with a fixed condition, and the L² or interior-image count.

**Not settled: what physical datum at a free cusp knows sign(q·∂_hF).**
- The computed candidates are the lane's sources (R24). There the count is k, not selected to three, and conditional on R18/R19.
  Placed on the fixed arcs of an order-3 isometry, their three is the regular representation (R32). The frame alone does not supply
  them.
- The mirror and the anomaly have four possible destinations:
  - to infinity, with the cusp left open (B1392's continuum);
  - into a wall (R25's mirror);
  - into the sources' inflow (R23);
  - a gap from interactions, where the lane has allowed terms but no mirror-only gap (R33–R34, R54). An anomalous mirror cannot be
    gapped alone (B1389).
- Each is to be sealed before it is computed. sL-8's rule stands: none may be chosen because it rescues a count. 0 of 19.

## 5. Fences

- **The frame's.** Spin-0; the abelian Higgs twist; flat-twist cohomology, not the spectral problem.
- **The L² reading.** The remark in §2 is cited in kind.
- **Part E.** Computed over three primes. The characteristic-zero value over ℚ(ω) agrees except at finitely many primes, and three
  agree.

## 6. Prior art (swept before banking)

Swept: this branch at 89221dde, origin/main at 987c0c8f, and the audit lane at aff8a569 (its R33–R54 reports). The sweep used git grep
for "charge flip", "charge-blind", "same boundary condition", "Poincaré dual", "vector-like" and "mirror". No arc or round states the
flip/blind dichotomy for the Higgs twist or computes the charge-blind count on the frame's twist.
- **B1351 (i)** (the closed half, verified on main in B1411) and **B1260 (1)**: closed implies vector-like. This is the blind case
  with ∂X = ∅.
- **Main's B1297.**
  - The interior-image index.
  - T1 (I(V*) = −I(V)) and T3 (self-dual implies 0).
  - T5 (only cusp-invariant systems can be chiral), which is the flat-twist form of B1392's sealed ends.
  - "The whole chirality lives in the boundary map."
- **R27** (main's B1413): the index is zero by theorem on geometric finite twists.
- **The physical-bridge rounds**, as in §3.
- **The literature: the domain-wall rule.** The chirality at an interface is set by the sign of the mass jump, so a closed or doubled
  geometry carries mirrors:
  - Jackiw–Rebbi, Phys. Rev. D 13 (1976) 3398;
  - Callan–Harvey, Nucl. Phys. B 250 (1985) 427;
  - Kaplan, Phys. Lett. B 288 (1992) 342;
  - the APS form in Fukaya et al., arXiv:2001.03318, as main's R25 reader cites it.

The lemma is this rule in the frame's homological language, and no novelty is claimed for it. What is new here is the application:
the flip identified as the frame's source of the count, and cube~3.24's charge-blind count computed exactly.
