# B591 — the chord's manifold, computed: the tone is the torsion

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; no SM
quantities. Owner directive 2026-07-14: run the Round-3 manifold cell (chat-1's
R3-B) as a computation, not a reframing. Locks
`tests/test_b591_chord_manifold.py`.**
Run: `python3 chord_manifold.py` (pyenv + snappy, ~1 min).

## M1 — the two lifts, homologically (exact SNF). THE HEADLINE.

H₁(torus bundle of φ) = ℤ ⊕ coker(φ − I):

| member | H₁(plain A-bundle) | H₁(mirror-twisted −A-bundle) |
|---|---|---|
| golden (tr 3) | **ℤ (trivial torsion)** | **ℤ ⊕ ℤ/5** |
| silver (tr 6) | ℤ ⊕ ℤ/2 ⊕ ℤ/2 | ℤ ⊕ ℤ/2 ⊕ ℤ/4 |
| bronze (tr 11) | ℤ ⊕ ℤ/3 ⊕ ℤ/3 | ℤ ⊕ ℤ/13 |

**The golden 5-tone's conductor det(A+I) = 5 is literally the first homology
of the chord's carrier.** More: the plain lift's torsion is det(A−I) and the
twisted lift's is det(A+I) — **B588's two Gauss conductors (t₊/t₋) are the two
lifts' torsion homologies.** Golden is the unique member whose plain bundle is
torsion-free (det(A−I) = −1, the unit) — its homological content lives
entirely in the mirror twist, the manifold-level face of "the entire golden
amplitude is θ-odd" (B584).

## M2 — the identity of the 5 (exact)

Δ₄₁(t) = char(A₁) = t² − 3t + 1;
**Δ(−1) = 5 = det(A₁+I) = |H₁(Σ₂(4₁))|** — the tone's conductor, the
Alexander determinant, and the branched double cover's homology are one 5.

## M3 — the branched double cover IS a mirror-pairing manifold: L(5,2)

4₁ = the 2-bridge knot b(5/2) ⇒ Σ₂(4₁) = L(5,2) **[CITED** standard**]**;
verified in-sandbox: SnapPy's cyclic double cover of the complement, filled
along the lifted meridian, has H₁ = ℤ/5 with a rank-1 π₁ presentation
(lens-space-sized). The classical "hold the object against its mirror image"
construction (the 2-fold cover) carries exactly the golden tone's arithmetic.

## M4 — the complement-double frame (exact Mayer–Vietoris)

H₁ of the closed double as a function of the cusp gluing g = [[a,b],[c,d]]:
H₁ = ℤ²/⟨μ₁ − aμ₂, bμ₂⟩. Computed: g = ±I → H₁ = ℤ; **g = ±A₁ → H₁ = 0 — the
monodromy-twisted double of the figure-eight complement is an integral
homology 3-sphere** (a Haken manifold whose JSJ decomposition has two hyperbolic 4₁ pieces — NOT a graph manifold; terminology corrected 2026-07-15: graph manifolds have only Seifert pieces).

## M5 — the geometry verdicts (computed where computable)

|tr(−A₁)| = 3 > 2 ⇒ the C-twisted bundle is **Sol** (Anosov; Thurston's
trichotomy, cited); it is not conjugate to the A₁ bundle (traces ±3) and not
hyperbolic — the census-name/volume/CS/trace-field questions have no
hyperbolic answers, as B586 stated; what they have instead is M1's torsion.
The complement-double contains an essential torus ⇒ a nontrivial JSJ decomposition (Haken; corrected 2026-07-15 — formerly mislabeled "graph manifold"), two
hyperbolic JSJ pieces, Gromov-norm volume 2 × 2.029883… (cited additivity).

## Reading (firewalled)

The chord's carrier is homologically marked by the tone it carries: ℤ/5
golden, |ℤ/2⊕ℤ/4| = 8 silver, ℤ/13 bronze — m²+4 throughout, the scale-field
discriminants (Path A's period moduli). The listener's 5 was never abstract
stage arithmetic only: it is the first homology of the mirror-twisted world,
the order of the branched double cover's torsion, and the Alexander
determinant — one integer wearing three hats. The two lifts whose agreement
defines chirality (B585) are distinguished by exactly the two conductors of
the sector-exchange theorem (B588).

## Anchors

B585 (the naming theorem — the −A₁ identification), B588 (t₊/t₋ conductors),
B584 (all-θ-odd golden), B586 (the geometry framing now made computational),
B204/L24 (m²+4 as the period modulus — the same integers), L76 (cover
torsion: |Res(Δ, t²−1)| = 5 is this 5).
