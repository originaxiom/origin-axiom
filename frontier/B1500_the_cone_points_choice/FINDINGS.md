# B1500 — THE CONE POINT'S CHOICE: completing the cusps of a member of m004's class as cone points does not remove the end's choice. The cusp point's link is the cusp torus, whose first homology is not zero, so the point is not Witt. A well-defined, self-dual count there needs one Lagrangian line per point (Cheeger's ideal boundary condition), the same datum as a Dehn-filling slope. Proved and checked with own code: a charged sector's net chirality on the completed space is a sum over cusp points of −1, 0 or +1 (lower middle, Lagrangian or upper middle perversity), whatever the Higgs field. Charge-blind choices give zero. On this completion a count is a count of chiral cusp points, one unit each, and the frame's far-up count only says where the modes sit.

**Date:** 2026-09-29 · **Seat:** cc (the SM-derivation branch) · **Occasion:** the owner's go on the sL-8 pass. After B1399 the pass
asked what every completion of a free cusp does. B1392's first candidate, "a conical point at each free cusp", had never been
worked out. · **Status:**
- PROVED: the theorem of §2, from the intersection homology of isolated singularities (Goresky–MacPherson), Cheeger's ideal boundary
  conditions and the duality of perversities.
- COMPUTED: every statement is checked by a new instrument on ten members: simplicial intersection homology of the compactified
  manifold, built from SnapPy's ideal triangulation.
- Not sealed. The question is decided by a theorem, as for B1396.

**Fence:** the frame's abelian Higgs classes (cuspidal, B1395) and its charged sectors; the completion is the one-point
compactification; the physical reading is Pantev–Wijnholt's (net chirality = the index of the Higgs-deformed complex). · **Price:**
unchanged, 0 of 19 · **Numbering:** B1500. This branch's range B1350–B1399 is used up and main holds B1400–B1431 (§8).

## 0. Seen from above

Since B1392 the record has known that the frame's chirality is an end effect. Whatever completes a free cusp decides the count.
- **The known completions** each either kill the count or make it an input:
  - a filling (B1351) and a fixed wall (B1393) are vector-like;
  - a flip wall carries its mirror (the lane's R25);
  - caps and sources carry a charge-odd datum that is put in by hand (B1395–B1397).
- **The one candidate never worked out** was the plainest: add one point at the end of each cusp. This arc works it out.
- **The point is not ordinary.** Its neighbourhood is a cone over the cusp torus, and the torus has two independent loops.
  Mathematically that makes the point "not Witt": the L² theory there is not unique. To get a well-defined count that pairs
  particles with antiparticles, one must choose a line of loops at each point. That is the same datum as a Dehn-filling slope.
  The cone point and the filling are one choice seen two ways.
- **What the choice does, exactly.**
  - Each point contributes −1, 0 or +1 to a charged sector's net chirality, according to the choice (lower, Lagrangian, upper).
  - Nothing else matters: not the Higgs class, not the coupling, not the shape of the Higgs field at the cusp.
  - A choice that ignores the sign of the charge gives zero, like every other charge-blind completion.
  - A chiral completion is a choice that flips with the charge. It gives one unit per point, of one sign.
- **In the architecture's terms.** On this completion chirality is carried by the points where a structure ends, one unit per point
  at most, and set by a datum the geometry does not supply. The end law (sL-8) is now a precise question: which datum does each
  charged sector get at each cusp point? Only the local physics at the point can say.

## 1. The setting

- **The compactification.** M is a cusped hyperbolic 3-manifold with compact core Q and k cusps. Q^ is its one-point
  compactification: one point p_c added at the end of each cusp c. It is a compact 3-dimensional pseudomanifold with isolated
  singular points. The link of p_c is the cusp torus T_c.
- **Not Witt.** For a 3-dimensional pseudomanifold with isolated singular points, the Witt condition asks that the links' middle
  homology vanish. Here H_1(T_c) = ℤ², so every cusp point fails it.
- **The ideal boundary conditions.**
  - On such spaces the L² de Rham theory needs, at each non-Witt point, a choice between lower and upper middle perversity or a
    self-dual intermediate. The intermediate is a Lagrangian subspace of the link's middle cohomology (Cheeger's ideal boundary
    conditions). Albin–Leichtnam–Mazzeo–Piazza prove the resulting operator Fredholm, and the self-dual choices give Poincaré
    duality ("Cheeger spaces"). Banagl's Lagrangian structures are the sheaf-theoretic form.
  - In H_1(T_c) every line is Lagrangian for the intersection form. A rational line is a slope.
- **The three choices at a point, as allowable chains.** In a triangulation where p_c is a vertex:
  - lower: a simplex through p_c is allowed only in degree 3;
  - upper: allowed in degrees ≥ 2;
  - Lagrangian L: allowed in degrees ≥ 2, and a 2-chain through p_c must cross the link in a cycle whose class lies in L.
- **The frame's charged sectors.** A charge-q sector with Higgs class ω lives in the deformed complex d + qTω. For a cuspidal class
  (ω = 0 on every cusp torus: the frame's dynamical Higgs field, B1395) this is the de Rham complex of a rank-one flat bundle L_{qT}.
  That bundle is trivial near every cusp point.

## 2. The theorem

**Theorem.** Choose at each cusp point p_c one of lower (ε_c = −1), upper (ε_c = +1) or a Lagrangian line (ε_c = 0). For every
cuspidal Higgs class ω and every coupling qT:
- (i) χ(IH(Q^; L_{qT})) = Σ_c ε_c;
- (ii) with lower at every point, IH = (1, b₁, b₁ − k, 1) untwisted; with upper, (1, b₁ − k, b₁, 1); so χ = −k and +k;
- (iii) the charge-conjugate sector's complex is dual to the charge-q complex with the dual choice at each point (lower ↔ upper,
  L ↔ L). So a choice that ignores the sign of the charge is self-dual at every point and gives 0. A net chirality needs the choice
  to flip with the charge, and each point then contributes one unit.

*Proof.*
- (ii) Use the formula for isolated singularities: IH_i equals the homology of the complement below the perversity's cut, the
  homology of Q^ above it, and the image between them at the cut.
  - Here χ(Q) = 0, so b₂(Q) = b₁ − 1. By half lives, half dies, H_1(∂Q) → H_1(Q) has rank k and H_2(∂Q) → H_2(Q) has rank k − 1.
    Also H_2(Q^) = H_2(Q, ∂Q), which has rank b₁ by Lefschetz duality.
  - Lower: IH = (1, b₁, (b₁ − 1) − (k − 1), 1).
  - Upper: IH = (1, b₁ − k, b₁, 1).
- (i) for untwisted coefficients.
  - The contributions to χ are local at each point. Mayer–Vietoris over Q and the cones, with χ(Q) = χ(T) = 0, gives
    χ(IH(Q^)) = Σ_c χ(IH(cone T_c)). The cone over T contributes 1 − 2 = −1 in lower perversity (IH = H_0 and H_1 of the torus),
    +1 in upper (H_0 only), and 0 for a Lagrangian line (H_0 and H_1/L).
  - A self-dual choice at every point gives a Poincaré-duality theory in odd dimension, whose Euler characteristic is 0.
- (i) with the twist.
  - χ of the intersection chain complex is Σ(−1)ⁱ dim IC_i, where IC_i is the space of allowable chains with allowable boundary.
  - Take each simplex through p_c based at p_c. The twist then enters only the coefficient of the face opposite p_c, which never
    passes through p_c.
  - So the constraints defining IC_i (the coefficients on faces through p_c, and the Lagrangian condition on the link) do not see
    the twist. Hence dim IC_i and χ are independent of ω and of qT. The groups themselves do change (§4).
- (iii) The dual of the twisted complex of L is the complex of L*, and L*_{qT} = L_{−qT}. Intersection homology of perversity p̄ is
  dual to that of the complementary perversity, and the annihilator of a line in the symplectic H_1(T) is the line itself. ∎

**The physical reading** (Pantev–Wijnholt: N_χ = h¹, N_χ̄ = h² of the charged complex; the net chirality is the index). On the
cone-completed space a charged sector's net chirality is −Σ_c ε_c.
- It is independent of the Higgs field, which decides only where the modes sit: at its zeros in the bulk, or at the cusp points.
- For a generic twist the homology sits in one degree (§4). With lower perversity at every point there are exactly k chiral modes,
  one per cusp point, and the conjugate sector has k of the other chirality.

## 3. What it settles, and what it does not

**Settled.**
- **B1392's first candidate** is decided. A cone point completed without regard to the sign of the charge gives nothing, like the
  filling (B1351) and the fixed wall (B1393). The conical completion is chiral only with a choice that flips with the charge. That
  choice is one more charge-odd datum supplied from outside the geometry, as B1395 found for every other completion.
- **One unit per point.**
  - A chiral cone point carries exactly one unit per charged sector.
  - Three from cone points needs three chiral points, with any others cancelling.
  - B1399's pointer, a single hexagonal cusp whose √3 shell gives 0 or ±3, is a statement about the open cusp's far-up count. No
    single cone point can carry it.
- **The far-up count and the completed count are different things.**
  - The frame's rule (B1387–B1399) is the far-up count of the open cusp, which is not Fredholm (B1392).
  - Completing each cusp as a point gives Σε, whatever the Higgs field.
  - B1399's verdict is unaffected: it is a statement about the frame's rule, and it stands.
- **sL-8, made precise.** The end law, if the ends are points, is an assignment of lower, Lagrangian or upper to each charged sector
  at each cusp point, consistent with charge conjugation and anomaly-free. The geometry does not make it. The local physics at the
  point must.

**Not settled.**
- **Which choice physics makes.** In M-theory, chiral matter at conical singularities is localized there, and Witten's anomaly
  inflow fixes its anomaly (Acharya–Witten; Witten 2001). Whether a cusp point is such a singularity, and what it carries, needs a
  local G₂ model whose ADE locus is a cone over the cusp torus. The record has none: its local models (B1084, B1353–B1360) have
  smooth loci through the apex, with sphere links.
- **The anomaly constraint on the choices.** If the choice at a point follows the sign of a charge under some U(1) direction at that
  point, the count is a sum of sign rules, one per cusp. B1398's analysis would then apply per point. That rule is an assumption,
  not derived here.

## 4. Verification (own code)

`verification/cone_point_ih.py`, run record `cone_point_ih_run.txt`, data `cone_point_ih.json`.
- **The instrument.**
  - It builds the first barycentric subdivision K' of SnapPy's ideal triangulation: a simplex is a chain of faces inside one
    tetrahedron, identified across the gluings. The ideal vertices are the cusp points.
  - It computes intersection homology over F_p (p = 2³¹ − 1) by allowable chains, for any choice at each point. A Lagrangian line is
    imposed as a link cocycle whose kernel on H_1(T) is the line.
  - It twists by the rank-one local system t^ω of a cuspidal class, with t random. The classes are computed as H¹(Q^) on the
    triangulation, and the cocycle is carried to K' by potentials inside each tetrahedron, checked consistent across gluings.
- **Ten members:** m004, m003, cube~3.24, and seven of B1399's census covers: of v2873, s959, o10_150685, o10_150688, o10_150729 and
  o10_150724, and the hexagonal cover of o10_150704. They have 1 to 5 cusps and 2 to 90 tetrahedra.
- **Every check passes:**
  - d² = 0, twisted and untwisted.
  - χ(Q^) = k.
  - The cuspidal dimension (H¹(Q^)) equals b₁ − k and matches B1399's independent solver on every census member.
  - Lower = (1, b₁, b₁ − k, 1) and upper = (1, b₁ − k, b₁, 1) on all ten.
  - Every mixed lower/upper pattern gives χ = Σε: all 2^k patterns for k ≤ 3, three patterns for k = 4 and 5.
  - A Lagrangian line at every point gives χ = 0, two random lines per member. A Lagrangian at one point with lower/upper elsewhere
    gives Σε with that point counting 0.
  - Twisted by two random cuspidal classes each, the lower, upper and mixed χ are unchanged on every member that has cuspidal
    classes.
- **The twist is not vacuous.** It changes the groups completely. On eight of the nine members with cuspidal classes a generic twist
  puts all of the homology in one degree:
  - lower = (0, k, 0, 0) and upper = (0, 0, k, 0): one mode per cusp point;
  - on cube~3.24, twisted by B1387's class v₊, lower = (0, 4, 0, 0);
  - on the o10_150688 cover the twisted groups keep two vector-like pairs, with lower = (0, 3, 2, 0). χ is unchanged there too.
- **Triangulation independence.** On m004 and m003 the second barycentric subdivision K'' (1 152 tetrahedra for m004) gives the same
  groups as K'.
- **The run.** About 36 s for all ten.

## 5. Local models with a torus link (checked, not used in §2)

`verification/local_models_check.py`, record `local_models_check_run.txt`. What M-theory would need at a cusp point is a G₂ cone
whose ADE locus is a cone over a torus. Two checks by own code:
- **Harvey–Lawson's cone** {|z₁| = |z₂| = |z₃|, z₁z₂z₃ ∈ ℝ⁺} in ℂ³.
  - It is special Lagrangian: ω and Im Ω vanish on it to 10⁻¹⁵. So it is associative in ℝ⁷ = ℝ ⊕ ℂ³.
  - Its link is the hexagonal torus: metric (1/3)[[2, 1], [1, 2]], shape e^{iπ/3}.
  - Its three smoothings each collapse one of the link's three shortest circles, the A₂ roots.
- **The G₂ cone over the nearly Kähler S³ × S³** (= SU(2)³/diag).
  - The torus fixed by diagonal conjugation by an element of U(1) is U(1)³/U(1).
  - In the normal metric it is hexagonal too (Gram [[2/3, −1/3], [−1/3, 2/3]]).
  - That is the singular locus of a cyclic quotient, which is A-type.
  - A non-abelian group such as E₆'s 2T has a finite centraliser, so it fixes no torus this way.
- These are pointers for the sealed census that follows (B1501), not results about the frame. Both point at hexagonal cusps, where
  B1399 found the only odd counts.

## 6. The arithmetic face (noted, not used)

3 is the unique ramified prime of ℚ(√−3), with residue field 𝔽₃, and SL(2, 𝔽₃) = 2T gives E₆ by McKay (B266; main's B1423). An
index-3 shell's free ℤ/3 of translations is ℤ[ω]/(√−3), the additive group of the same residue field. That is recorded as a pointer
only: by §2 no single cone point carries a three.

## 7. Prior art and fences

- **The sweep.** On this branch, main (`987c0c8f`) and the audit lane (`aff8a569`), fetched 2026-09-29, there are no hits for
  intersection homology, perversity, non-Witt, Cheeger's ideal boundary conditions, Banagl, stratified Morse theory, Harvey–Lawson,
  special Lagrangian, J-holomorphic or nearly Kähler.
  - The conical-point completion is B1392's own candidate.
  - "A filling slope picks a Lagrangian line" appears in B293, in another context.
  - The audit lane's reviews cite Acharya–Witten and Witten's inflow for the curved-cone candidate (B1355).
- **The literature, cited and not re-derived.**
  - Goresky–MacPherson, intersection homology (the isolated-singularity formula; duality of complementary perversities);
  - Cheeger, "On the Hodge theory of Riemannian pseudomanifolds" (1980), and his ideal boundary conditions;
  - Banagl, "Extending intersection homology type invariants to non-Witt spaces" (Mem. AMS 2002);
  - Albin, Leichtnam, Mazzeo, Piazza, "Hodge theory on Cheeger spaces" (arXiv:1307.5473);
  - Harvey–Lawson, "Calibrated geometries" (1982);
  - Pantev–Wijnholt (arXiv:0905.1968), for the charged complex.
- **Fences.**
  - Abelian, cuspidal Higgs classes and the frame's charged sectors.
  - The completion is the one-point compactification with its ideal boundary conditions. Other completions are as before.
  - The physical reading is Pantev–Wijnholt's.
  - Nothing here selects a choice, a local model or a three. No physics crossed. 0 of 19.

## 8. Numbering

This branch's reserved range B1350–B1399 is used up. The alias table's "next arc B1400" (written 2026-09-28) was never checked
against main, which had already banked B1400–B1431. No arc was numbered with it. This arc takes B1500. The branch asks main to reserve
B1500–B1599, recorded in `docs/SM_SEAT_ALIAS_TABLE.md`. The slip is logged as an E54 instance.

## Files

- `verification/cone_point_ih.py`, `cone_point_ih.json`, `cone_point_ih_run.txt`: the intersection-homology instrument and its
  run on ten members.
- `verification/local_models_check.py`, `local_models_check_run.txt`: the Harvey–Lawson and S³ × S³ checks.
