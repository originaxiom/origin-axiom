# B524 — The two actionable next steps: the iwip certificate + the higher-rank Ptolemy

**Owner directive (2026-07-12): do the two actionable next steps properly** — the Bestvina–Handel iwip
certificate (the one open group-theory question from B523) and the higher-rank Ptolemy (where nonabelian
gauge could live, unlike DGG's abelian U(1)). Both done with **established tools**, validated before use,
rather than reimplementing algorithms and risking the very abelianization-as-proxy error the B523 thread was
about. Firewalled; nothing to `CLAIMS.md`.

## Part 1 — φ IS iwip, and F₄⋊_φℤ is word-hyperbolic (CERTIFIED)

Tool: **Coulbois' `train_track`** (a Bestvina–Handel implementation), in the `sage` env. The target is the
corrected Level-1 automorphism, relabelled a,b,A,B → a,b,c,d to avoid the inverse-letter clash:
**φ: a→abccd, b→acd, c→abcd, d→ac.**

**Discipline first — the tool was validated on known cases** (`iwip_certificate.py`):
`is_iwip` returns **True** on the Tribonacci a→ab,b→ac,c→a (known iwip) and **False** on both a→ab,b→b
(fixes ⟨b⟩) and Tribonacci+d→d (fixes ⟨d⟩) — known non-iwip. Only then applied to φ.

| certificate | result | consequence |
|---|---|---|
| φ ∈ Aut(F₄) | inverse exists (tool) + surjective/Hopfian (B523) | automorphism ✓ |
| **iwip** | `phi.is_iwip()` = **True** (Bestvina–Handel: irreducible train track, no periodic Nielsen paths) | fully irreducible ✓ |
| λ(φ) | **3.67621 = β = φ(1+√φ)** | the bootstrap eigenvalue is the dilatation |
| λ(φ⁻¹) | **3.0523 ≠ λ(φ)** | **NOT geometric** (a surface pA has λ(φ)=λ(φ⁻¹)) |
| index_list | [2,1,1] | (not the geometric n−1=3 single-index profile) |

**The load-bearing datum, independently verified (`verify_dilatation.py`).** Everything below rests on
λ(φ) ≠ λ(φ⁻¹), so it was checked by a method *independent of train_track's train-track construction* — pure
word-length growth: the inverse formula ψ is confirmed the genuine inverse (φ(ψ(g)) = ψ(φ(g)) = g for all g,
free-reduction), and |φᵏ(a)|^{1/k} → **3.6762**, |φ⁻ᵏ(a)|^{1/k} → **3.0523** (ratios flat to 4 digits by
k≈10). Note λ(φ⁻¹) = 3.052 ≠ the abelianization |M⁻¹|-Perron **2.272** — i.e. free cancellation genuinely
changes the count, so this is *not* an abelianization artifact (a subtlety flagged by chat1).

**Conclusions (now theorems, resting on the verified λ asymmetry):**
- **φ is NOT geometric** — a geometric iwip (surface pseudo-Anosov) satisfies λ(φ)=λ(φ⁻¹) (Handel–Mosher);
  ours differ, so φ is not induced by a homeomorphism of any surface-with-boundary. (Independently confirms
  chat3's "not a mapping class of Σ_{2,1}.")
- **F₄ ⋊_φ ℤ is word-hyperbolic** — non-geometric iwip ⟹ atoroidal (no periodic conjugacy class), so by
  **Brinkmann (2000)** the mapping torus group is hyperbolic. CAT(0)-cubulated (Hagen–Wise) and Menger-curve
  boundary (Kapovich–Kleiner) follow.
- **It is NOT a 3-manifold group — by Stallings, not by cd/ℤ².** *(Correction, owner-flagged: the cohomological-
  dimension and no-ℤ² arguments an earlier draft used are both invalid — a cusped 3-manifold group like the
  figure-eight complement has cd = 2, and a closed hyperbolic 3-manifold group is word-hyperbolic with no ℤ².
  Neither obstructs.)* The correct argument: by **Stallings' fibration theorem**, if F_n ⋊_φ ℤ were a
  3-manifold group, the manifold would fiber over S¹ with fibre carrying the free normal subgroup F_n — i.e. a
  compact surface **with boundary** — making φ its monodromy, hence **geometric**. φ is not geometric, so
  **F₄⋊_φℤ is not the fundamental group of any 3-manifold.** Consequently no volume / Chern–Simons / Dehn-
  filling layer, and the DGG bridge (which needs a hyperbolic 3-*manifold* input) does not apply to this object.

**Net Part 1:** the one open group-theory question is settled — **iwip: yes; word-hyperbolic: yes;
3-manifold group: no** — all resting on one independently-verified number, λ(φ⁻¹)=3.052 ≠ λ(φ)=3.676. The
"Level-1 spacetime" is a genuine negatively-curved (hyperbolic) group with a Menger-curve boundary carrying
the bootstrap β as its dilatation — but a *group*, not a manifold. The geometry language stops exactly here.

## Part 2 — higher-rank Ptolemy of the figure-eight: arithmetic enriches, gauge stays abelian

Tool: **SnapPy's `ptolemy` module** (sage engine), on 4₁ (N=2 tetrahedra, c=1 cusp). Tests chat1's question —
*does higher-rank DGG reach nonabelian gauge?* (`higher_ptolemy.py`):

| rank | boundary-unipotent reps | number fields | Ptolemy coords |
|---|---|---|---|
| SL(2) | **1** | ℚ(√−3) | 2 |
| SL(3) | **4** | ℚ(√−3) **and ℚ(√−7)** | 8 |
| SL(4) | *(deferred — the sage Gröbner engine ran >12 min over 20 coords × 3 obstruction classes; the ptolemy module recommends Magma at this rank)* | | 20 |

- **The representation/arithmetic content grows with rank:** SL(3) yields 4 reps (vs 1 at SL(2)) and brings in
  **ℚ(√−7)** alongside the figure-eight's ℚ(√−3). (The √−7 is a notable internal echo — it is exactly the
  order-3 torsion field of the held-breath law [[B479]]; arithmetic, firewalled.)
- **But the gauge group stays abelian at every rank.** The DGG 3d–3d theory has gauge group **U(1)^{N−c}=U(1)**
  at SL(2); the higher-rank theory T_K[M] (Dimofte–Gabella–Goncharov, *K-decompositions and 3d gauge theories*,
  2014) is built from tetrahedron theories glued by **abelian** gauging — gauge group **U(1)^{r_K}**, a product
  of U(1)'s, **abelian at every K**. The K-decomposition quiver grows (coords 2→8→20), but the gauge symmetry
  does not become nonabelian; SL(K)'s nonabelian structure lives in the *matter/quiver*, not the gauge group.

**Net Part 2:** the higher-rank route chat1 flagged as "where nonabelian gauge could live" does **not** reach
it — it enriches the *arithmetic* (more reps, bigger fields) while the gauge stays abelian U(1)^r. This
**extends T-NOGO-DGG (B490) to all ranks**: no rank of the DGG correspondence produces the SM's nonabelian
gauge; nonabelian gauge would require symmetry enhancement at special loci or a fundamentally different
construction, not higher K.

## Terminal state
DOOR B524 — **CLOSED (both actionable steps done).** Part 1: iwip + word-hyperbolic **certified** (tool
validated first), not a 3-manifold group — the group-theory question is fully settled. Part 2: higher-rank
Ptolemy enriches arithmetic (SL(3): 4 reps, +ℚ(√−7)) but the DGG gauge stays **abelian at all K** — the
no-go extends. The honest final picture: **the Level-1 object is a real hyperbolic group carrying β; it is
not a manifold, and no rank of the external bridge reaches nonabelian gauge.** Locks: `tests/test_b524.py`.
Reproducers: `iwip_certificate.py`, `higher_ptolemy.py` (sage env). Cross-refs: [[B523]] (the automorphism),
[[B490]] T-NOGO-DGG, [[B479]] (√−7 held-breath), [[B71]] (SL(3) figure-eight A-variety).
