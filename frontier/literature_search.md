# Literature search — SL(n) character varieties of once-punctured torus bundles, adjoint action at the trivial connection

**Date:** 2026-06-03. **Question:** has anyone computed the linearized spectrum (the
fixed-line / trace-map Jacobian, B59–B66) of the adjoint action at the **trivial flat
connection** for once-punctured torus bundles with pseudo-Anosov monodromy at **SL(n)**?
Such a result would either confirm the `char(M^k)` tower or supply the missing
multiplicity formula. **Exploratory; uncommitted; no claim promotion.**

---

## Bottom line

1. **No paper computes our exact object verbatim** — the trace-map fixed-line Jacobian
   spectrum at the *trivial* flat connection, SL(n), for these bundles. The trivial
   connection is the most degenerate point of the character variety; the literature on
   these bundles works at the **geometric (discrete-faithful / boundary-unipotent)**
   connection or at *non-trivial* reducible representations. **So the trivial-connection
   tower may be a genuinely under-studied angle.**

2. **But the representation-theoretic framework that governs the tower is established**,
   and three results bear directly on the missing multiplicity formula:
   - the **principal `SL(2) -> SL(n)` (symmetric-power) embedding** is exactly how higher-rank
     invariants of these manifolds are built (Menal-Ferrer–Porti; Kozai);
   - **adjoint Reidemeister torsion for SL(n) factors as a product of `PGL_2`-torsions with
     multiplicities given by the EXPONENTS of the Lie algebra** (Ishibashi–Mizuno 2026) —
     for `sl(n)` the exponents are `1,2,...,n-1`, i.e. the decomposition
     `sl(n) = ⊕_{k=1}^{n-1} Sym^{2k}` (Kostant). **This is the most likely source of the
     `char(M^k)` multiplicity formula.**
   - **deformations of reducible SL(n) reps of FIBERED 3-manifolds via the principal
     embedding** are controlled by **monodromy eigenvalue conditions** with an explicit
     component-dimension formula (Kozai) — the closest structural match to the tower.

3. The tower's `char(M^k)` factorization is, in standard language, the **twisted
   Reidemeister torsion / twisted Alexander polynomial** of the bundle: its coefficients
   are sums of eigenvalues of the monodromy acting on the twisted homology of the fiber
   (Yamaguchi). The `char(M^k)` roots are exactly those monodromy eigenvalues.

---

## Most relevant references (ranked)

1. **Kenji Kozai, "Deformations of reducible SL(n,C) representations of fibered 3-manifold
   groups," arXiv:1509.07487.** THE closest match. Surface bundle `M_φ` over `S^1`; reducible
   SL(n) reps obtained by composing an SL(2,C) rep with the irreducible (principal/symmetric-
   power) `SL(2,C) -> SL(n,C)`; deformability controlled by **conditions on the eigenvalues of
   `φ_*`** (pseudo-Anosov: `1` not an eigenvalue of the induced map on homology). Under those
   conditions the rep lies in a component of dimension **`(n+1+k)(n-1)`** (`k` = #boundary
   components; once-punctured torus fiber ⇒ `k=1`). This is the tower's setup — fibered +
   principal embedding + monodromy eigenvalues — from the **deformation/obstruction** side.
   **Read in full; its eigenvalue conditions and dimension count are where our `char(M^k)`
   multiplicities should be derivable.** (Treats reducible reps that are limits of
   irreducibles — closely related to, but not literally, the trivial connection.)

2. **Ishibashi–Mizuno, "Adjoint Reidemeister torsion of 3-manifolds with torus boundary for
   semisimple algebraic groups," arXiv:2603.00816 (2026).** Defines adjoint torsion for
   semisimple `G`, extending Porti's SL(2). Key: for cusped hyperbolic manifolds the adjoint
   torsion is a **product of `PGL_2`-torsions over the simple `PGL_2`-modules of `g`, with
   multiplicity = the EXPONENTS of `g`** (Kostant/Steinberg). For `sl(n)`: exponents
   `1,2,...,n-1`. **This is a concrete candidate multiplicity rule for the tower.** Caveat:
   explicit computation only for the **figure-eight knot complement** at boundary-unipotent
   connections — *not* once-punctured torus bundles, *not* the trivial connection.

3. **Menal-Ferrer–Porti, "Higher dimensional Reidemeister torsion invariants for cusped
   hyperbolic 3-manifolds," arXiv:1110.3718 (J. Topol. 2014);** and **"Local coordinates for
   SL(n,C) character varieties of finite volume hyperbolic 3-manifolds," arXiv:1111.4338.**
   Builds the higher-rank invariants via `Sym^{n-1} ∘ holonomy` (the principal embedding) — the
   same symmetric-power scaffold as the tower, but at the **geometric** connection. Confirms
   `sl(n) = ⊕ Sym^{2k}` is the right decomposition; the `log τ_n ~ -n^2 Vol/4π` asymptotic is
   the torsion analog of the tower's growth.

4. **Y. Yamaguchi, "Reidemeister torsion, twisted Alexander polynomial and fibered knots,"
   arXiv:math/0311155.** Identifies the Reidemeister torsion of a fibered 3-manifold with
   Wada's twisted Alexander polynomial; its coefficients are symmetric functions of the
   **monodromy eigenvalues on the twisted homology of the fiber**. This is the precise classical
   meaning of our `char(M^k)` factorization. (See also Dunfield–Friedl–Jackson, arXiv:1108.3045,
   for the systematic twisted-Alexander computations.)

5. **Tran–Yamaguchi, "Adjoint Reidemeister torsions of once-punctured torus bundles,"
   arXiv:2109.07058.** Adjoint (`SL(2)`) torsion of exactly our manifolds — verifies the
   Gang–Kim–Yoon vanishing identity for all tunnel-number-one once-punctured torus bundles. SL(2)
   only and at the non-trivial connection, but the manifold family is identical to ours.

6. **(twisted-Alexander tangent action, higher rank)** arXiv:2411.04431, "Projective Rigidity
   of Once-Punctured Torus Bundles via the Twisted Alexander Polynomial": proves the twisted
   Alexander polynomial **equals the induced monodromy action on the tangent space of the
   `F_2` character variety into PGL(4,R)** (via the LHS spectral sequence). A higher-rank
   tangent-space-action result for our bundles — structural, no explicit eigenvalue table, and
   PGL(4) rather than general SL(n)/trivial connection.

## Reducible-representation / local-structure thread (supports the multiplicity formula)

- **Ben Abdelghani–Heusener and Heusener–Medjerab**, "Deformations of reducible representations
  of knot groups into SL(n,C)" (arXiv:1402.4294) and **"On the local structure of the SL(n,C)-
  representation variety of knot groups"** (arXiv:2404.09548): smoothness at reducible reps
  requires **`λ^{2j}` not an eigenvalue of the monodromy for `2 ≤ j ≤ n`** — the `λ^{2j}` are
  exactly the locations of the higher `char(M^k)` factors. The component structure there is the
  obstruction-theory shadow of our spectrum.

## Foundations the tower already stands on

- **Lawton**, "Minimal Affine Coordinates for SL(3,C) Character Varieties of Free Groups"
  (arXiv:0709.4403) + "Algebraic Independence ..." (arXiv:0807.0798): the SL(3,C) character
  variety of `F_2` is the `C^9` hypersurface with 9 trace generators — the coordinate ring PC12/
  the tower uses.
- **Sikora**, "SL_n-character varieties as spaces of graphs" (arXiv:math/9806016) and "Character
  Varieties" (arXiv:0902.2589): all SL(n) trace relations from a single local graph relation —
  the general-`n` trace-identity backbone for the symbolic trace ring (our B58 open task).
- **Bonahon–Wong quantum trace** (skein algebra ↪ quantum torus) and the SL(n)/stated-skein
  generalizations (e.g. arXiv:2403.12424 "A quantum trace map for 3-manifolds") — the quantum
  side of the trace map, relevant to the AJ/B68 direction.

## Physics side (3d–3d correspondence)

- **Dimofte–Gaiotto–Gukov**, "3d-3d Correspondence Revisited" (arXiv:1405.3663) — *all* flat
  connections (incl. non-geometric/abelian) enter the 3d theory; SL(N) Chern–Simons.
- **Gang et al.**, "Superconformal index and 3d-3d correspondence for mapping cylinder/torus"
  (arXiv:1305.0937) and "3d-3d correspondence for mapping tori" (arXiv:1911.08456, JHEP 2020) —
  the once-punctured-torus-bundle case explicitly, as `SL(2,C)` CS on the mapping torus. Higher-
  rank `SL(N)` is the natural extension; the partition function organizes the contributions of
  flat connections (including, in principle, the trivial one).

---

## What this says about our missing multiplicity formula

The convergent picture: our `char(M^k)` tower is the **monodromy spectrum on the twisted
(co)homology of the fiber with coefficients in `sl(n)`**, and the natural organizing principle is

```
sl(n) = ⊕_{k=1}^{n-1} Sym^{2k}(C^2)      (Kostant; principal SL(2)->SL(n)),
exponents of sl(n) = 1, 2, ..., n-1.
```

Two concrete, testable hypotheses for the multiplicity formula:

- **(H1, exponents)** Ishibashi–Mizuno: the adjoint torsion factors over the principal-`PGL_2`
  modules with multiplicity = exponents. Re-expressed for the bundle, this predicts the
  `char(M^k)` multiplicities from how the monodromy acts on each `Sym^{2k}` block (eigenvalues
  `λ^{2k}, λ^{2k-2}, ..., λ^{-2k}`) **combined with** the rank-2 `H^1(F_2)=C^2` factor (the two
  generators). This coupling is exactly what B66 measured and what makes the naive
  "`max(n-d,1)`" wrong (B66 refuted it).
- **(H2, deformation dimension)** Kozai: the component dimension `(n+1+k)(n-1)` and the `λ^{2j}`
  eigenvalue conditions encode the same data from the obstruction side.

**Action items for the tower:**
1. **Read Kozai arXiv:1509.07487 in full** — same setup; its eigenvalue conditions + dimension
   count are the most likely closed form for our multiplicities.
2. **Test B66 against the `sl(n)=⊕Sym^{2k}` / exponent prediction.** Compute the monodromy
   spectrum on `H^1(F_2; Sym^{2k})` for `M=[[1,1],[1,0]]`, sum over `k=1..n-1`, and compare the
   resulting `char(M^j)` multiplicities to B66's SL(6) data (`|k|=3` ⇒ 2, etc.). If they match,
   the formula is the Kostant/exponent decomposition — and B66's refutation of `max(n-d,1)` is
   explained.
3. **The trivial-connection computation looks novel** relative to this literature (which sits at
   the geometric/non-trivial-reducible connections). If the tower's trivial-connection spectrum
   is reproduced by the `Sym^{2k}` framework, that is the bridge; if it differs, the discrepancy
   (the singular trivial point vs the smooth geometric one) is itself the interesting content.

---

## Sources

- [Kozai, Deformations of reducible SL(n,C) reps of fibered 3-manifold groups](https://arxiv.org/abs/1509.07487)
- [Ishibashi–Mizuno, Adjoint Reidemeister torsion for semisimple algebraic groups](https://arxiv.org/abs/2603.00816)
- [Menal-Ferrer–Porti, Higher dimensional Reidemeister torsion (cusped hyperbolic)](https://arxiv.org/abs/1110.3718)
- [Menal-Ferrer–Porti, Local coordinates for SL(n,C) character varieties](https://arxiv.org/pdf/1111.4338)
- [Yamaguchi, Reidemeister torsion, twisted Alexander polynomial and fibered knots](https://arxiv.org/pdf/math/0311155)
- [Tran–Yamaguchi, Adjoint Reidemeister torsions of once-punctured torus bundles](https://arxiv.org/pdf/2109.07058)
- [Projective rigidity of once-punctured torus bundles via twisted Alexander](https://arxiv.org/pdf/2411.04431)
- [Ben Abdelghani–Heusener, Deformations of reducible reps of knot groups into SL(n,C)](https://arxiv.org/pdf/1402.4294)
- [On the local structure of the SL(n,C)-representation variety of knot groups](https://arxiv.org/pdf/2404.09548)
- [Lawton, Minimal affine coordinates for SL(3,C) character varieties of free groups](https://arxiv.org/abs/0709.4403)
- [Sikora, SL_n-character varieties as spaces of graphs](https://arxiv.org/pdf/math/9806016)
- [A quantum trace map for 3-manifolds (Bonahon–Wong lineage)](https://arxiv.org/abs/2403.12424)
- [Dimofte–Gaiotto–Gukov, 3d-3d Correspondence Revisited](https://arxiv.org/abs/1405.3663)
- [Gang et al., Superconformal index and 3d-3d for mapping cylinder/torus](https://arxiv.org/abs/1305.0937)
- [3d-3d correspondence for mapping tori (JHEP 2020)](https://arxiv.org/pdf/1911.08456)
- [Baker–Petersen, Character varieties of once-punctured torus bundles (tunnel number one)](https://arxiv.org/abs/1211.4479)
