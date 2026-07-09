# The map of the object — one object, many faces, from a two-arrow root

**Draft map, 2026-07-09. The candidate spine for the program's synthesis paper. Thesis stated
*honestly*: a substitution σ on two letters is a natural common root from which the figure-eight
knot, the Markov spine, the metallic means, once-punctured-torus bundles, and their quantizations
all descend as *faces of one object*. This is a DICTIONARY, not a derivation: most layers are
classical and are cited, not claimed; the program's contribution is the assembly plus one or two
specialist-gated bridges. The table's third column is the honesty mechanism — every row is labeled
CLASSICAL / ASSEMBLY / NOVEL-GATED / PROGRAM.**

## The root

    σ :  a → ab ,  b → a          (the minimal self-reference; the Fibonacci substitution)

Two facts about σ are *genuinely forced* (no choice): its Perron eigenvalue is the golden ratio φ,
and its incidence (abelianization) matrix is the golden matrix X₁ = [[1,1],[1,0]]. Everything below
is a face of what σ generates — but the descent has one honest subtlety, stated up front so the
diagram does not overclaim:

**The square/half step (real structure, not forcing).** X₁ has **det −1** — it is orientation-
*reversing*, the "half." The figure-eight monodromy is its **square** X₁² = A₁ = [[2,1],[1,1]]
(det +1, orientation-preserving). The object needs an orientation-preserving monodromy, so the
bundle sees X₁²; σ's own matrix is the orientation-reversing half, and that det −1 = the norm
residue N(φ) the program tracks. So "σ forces the figure-eight" is precisely "σ's half, squared."

## The descent (diagram)

    σ  (a→ab, b→a)  ── the Fibonacci substitution
    │
    ├─ eigenvalue ──────────▶  φ  (golden mean)  ──deform (σₘ: a→aᵐb)──▶  λₘ  (metallic means)
    │
    ├─ incidence matrix ────▶  X₁=[[1,1],[1,0]]  (det −1, the HALF)
    │                              │ square
    │                              ▼
    │                          A₁=[[2,1],[1,1]]  (det +1, figure-eight monodromy)
    │                              │ mapping torus (once-punctured-torus fiber)
    │                              ▼
    │                          4₁  figure-eight knot complement  ═══ the geometric object
    │                              ├─ holonomy trace field ─────▶  ℚ(√−3)  (Eisenstein / Bianchi)
    │                              ├─ Weil quantization @ level N ▶  cat maps W₁,W₂ ; seam form @15
    │                              └─ σₘ half-turn on char. variety ▶ held-breath torsion / residue
    │
    ├─ iteration on the Fricke/Markov cubic ▶  the Markov spine  (1, 2, 5, 13, 194, …)   [Cohn]
    │
    └─ one-parameter deformation σₘ ────────▶  metallic family Aₘ=RᵐLᵐ
                                                  ▶ bundles m004 / m136 / s464 ▶ SL(n) A-varieties

## The layer table (layer · what it is · classical source · status)

| # | layer | what it is | classical source (cite) | status |
|---|---|---|---|---|
| 1 | the generator | σ: a→ab, b→a — the Fibonacci substitution; incidence matrix X₁ | Fogg, *Substitutions in Dynamics* (2002); Pytheas-Fogg | **CLASSICAL** |
| 2 | the scale | φ = Perron eigenvalue of X₁; the metallic means λₘ | Dirichlet; standard | **CLASSICAL** |
| 3 | the half / square | X₁ (det −1) is orientation-reversing; X₁² = A₁ the figure-eight monodromy; det X₁ = N(φ) = −1 | companion matrices (classical); the "half-matrix, det = −1 = norm" framing is the program's (T-NORM, B469) | **ASSEMBLY** |
| 4 | the 3-manifold | figure-eight complement 4₁ = mapping torus of A₁ on the once-punctured torus (b++RL) | Thurston; standard punctured-torus-bundle fact | **CLASSICAL** |
| 5 | the arithmetic | invariant trace field ℚ(√−3); 4₁ is the arithmetic manifold of PSL₂(O₃) | Maclachlan–Reid, *Arithmetic of Hyperbolic 3-Manifolds* | **CLASSICAL** |
| 6 | the Markov spine | σ-iteration ↔ Markov triples on the Fricke cubic; the /3 walk 1,2,5,13,194,… | **Cohn 1955**; Aigner (2013); Reutenauer (2019); Goldman (2003) | **CLASSICAL** (T-CHAIN/T-COHN: the metallic-spine framing is the program's assembly) |
| 7 | the metallic family | σₘ: a→aᵐb; Aₘ = RᵐLᵐ = [[m²+1,m],[m,1]], trace m²+2; bundles m004/m136/s464 | punctured-torus bundles (Guéritaud 2006, volumes); metallic means (de Spinadel) | **ASSEMBLY** (the family as the object's spine; individual bundles classical) |
| 8 | the quantized layer | Weil / Hannay–Berry quantization of A₁,A₂ at level N; cat maps W₁,W₂ | Hannay–Berry (1980); Kurlberg–Rudnick (2000) | **CLASSICAL** (the quantization); the seam construction is program's — see 9 |
| 9 | the seam form | the ℚ(√5,√−3)-projection of tr(Par·P_a·Q_b) @15; broken subfield-lattice (ℚ(√−15) absent) | building blocks: Kurlberg–Rudnick; Ladisch (2023); Dong–Lin–Ng (2015) | **NOVEL-GATED** (B491: APPEARS-NOVEL / NEEDS-SPECIALIST; standard Galois can't produce the vanishing) |
| 10 | the residue | norm (const −1), two-register parity (level-alternating), word-det (three-valued −μ₃) | units of norm −1 (Dirichlet); Jacobi parity; each register classical | **ASSEMBLY** (three distinct orientation invariants with coincidence conditions; the reading is program's) |
| 11 | the held breath | σₘ-fixed characters ⊇ order-d torsion; d=3 → ℚ(√−7), d=5 → degree-4 over ℚ(√5) | mechanism prior art: **Cantat 2009** (fixed-curve → field); Goldman; BGMW (2022) | **NOVEL-GATED** (B491: APPEARS-NOVEL / NEEDS-SPECIALIST; ⊇ only, field corrected) |
| 12 | the WRT / anyon layer | SU(2)_k invariants; Fibonacci anyons; c = 7/10 (first N=1 SCFT) | quantum topology (RT/Witten); standard | **CLASSICAL** (the SM/anyon readings were killed — firewalled, B483/B484) |
| 13 | the higher-rank tower | SL(n) figure-eight A-varieties; degree = rank (n∈{3,4}); the metallic Jacobian | Cooper–Long (SL2 A-poly); HMP/Falbel (SL3) | **PROGRAM** (banked B67–B95; needs its own novelty gate before any claim) |
| 14 | **the assembly itself** | the observation that 1–13 are faces of ONE object with common root σ | — (this is the paper's thesis) | **ASSEMBLY** (the program's actual contribution) |

## What the paper can honestly claim

- **The spine:** these independently-studied objects are one object, and σ is a natural common root.
  That is a synthesis/dictionary built almost entirely from *classical* pieces (rows marked CLASSICAL),
  each cited. Whether this *full* assembly appears in one place already is itself un-checked — the
  synthesis needs its own literature gate before it is called new; parts of it (Fibonacci ↔ golden
  matrix, Markov ↔ modular) are certainly classical, and a survey may connect more than we know.
- **The load-bearing novelty** is exactly two specialist-gated bridges — the seam broken-lattice (9)
  and the held-breath field law (11) — plus the assembly (14). Everything else is a citation.
- **The rigorous anchor** is Paper 4 (the metallic family / Markov stage), which cleared adversarial
  review; this map hangs P4 and the specialist notes under one picture.
- **What it must NOT claim:** "everything is *forced* from two arrows." The descent has genuine
  choices (the square/half step; which quantization level; which deformation), and most layers are
  classical facts about famous objects. The honest verb is "is a face of," not "is derived from."

## Status
This is the map — the diagram + the layer/source/novelty table — as the first concrete piece of the
synthesis paper. It is deliberately table-first: the third column forces the classical/novel split
that dense prose kept blurring. Next step (if the framing is right): commit each CLASSICAL row's
citation, and let the two NOVEL-GATED rows stay specialist-gated rather than written up as theorems
in-house. Reproducers/anchors: T-NORM/T-CHAIN/T-COHN (registry); B469/B479 (residue, held breath);
B358–B367/B459 (seam); Paper 4 (metallic family).

## Figures (grounded; `papers/map_figures/gen_map_figures.py`)

Each figure plots only values verified in-script (assertions fail loud on any wrong number):

- **`mapfig1_gauss_spine`** — the Gauss map G(x)={1/x} with the metallic means as its constant-CF
  fixed points (golden [0;1̄], silver [0;2̄], bronze, copper) on the diagonal. The program's spine =
  the periodic (measure-zero) orbits of the same map that governs BKL era transitions. *[KNOWN]*
- **`mapfig2_cover_tower`** — the self-interaction (cyclic-cover) tower of the figure-eight (B489):
  volume = n·vol(4₁) exact (covering), and H₁ torsion = |L(2n)−2| = 1,5,16,45,121,320,841,2205
  (Fox–Weber), with the n=2 value = det(4₁) = 5. *[KNOWN]*
- **`mapfig3_broken_lattice`** — the seam form's realized surviving-fields: the subfield lattice of
  ℚ(√5,√−3) with the **ℚ(√−15) node struck out** (never realized) plus a zero (dark) stratum;
  populations 120/20/20/10/70 from B459. *[NOVEL-GATED]*

## Novelty gate (adversarial lit-gate, 2026-07-09) — the honest verdict for the paper

Ran the deep-research prior-art harness (100 agents) against every canonical reference on both sides.

**(a) Every pairwise link is textbook-classical — CITE, don't claim.** With sources to use:
- R/L-word coding of once-punctured-torus-bundle monodromy in SL(2,ℤ); MCG = SL(2,ℤ); Farey cutting
  sequences — **Floyd–Hatcher (1982); Series (1985); Cannon–Dicks (2002); Dicks–Sakuma (2010)** (they
  call it a "well-known fact").
- **(golden matrix)² = RL = [[2,1],[1,1]] = figure-eight monodromy = Arnold cat map** (confirmed here:
  RL = X₁²). Stated verbatim in **Cannon–Dicks ("the square of RM is RL")** and **Dehornoy (2024),
  "The cat-bat map, the figure-eight knot, and the five orbifolds" (arXiv:2409.06543)**.
- figure-eight = the RL punctured-torus bundle — **Thurston; Guéritaud (2006)**.
- Markov spectrum ↔ modular torus ↔ continued fractions / cutting sequences — **Cohn (1955); Series
  (1985)**; Christoffel words ↔ Markoff numbers — **Frobenius (1913); Reutenauer (2019)**.
- metallic means via the substitution B→A, A→AⁿB with eigenvalue the metallic mean — classical.

**(b) The FULL assembly does NOT exist in one place — APPEARS-NOVEL as an organizing synthesis.** Every
canonical source contains *only its own facet*: the topology references (Cannon–Dicks, Dicks–Sakuma,
Lackenby, Guéritaud, Dehornoy) have zero Markov/Fibonacci/metallic/cat-map content; the Markov/Christoffel
monograph (Reutenauer, Aigner, Series, Cohn) has zero hyperbolic-geometry/torus-bundle/figure-eight
content. No single source assembles more than the pairwise links under the substitution root.

**(c) The metallic RᵐLᵐ family as the σₘ deformation, tied to BOTH the Markov/modular story AND the
quantized-cat-map story — APPEARS-NOVEL / NEEDS-SPECIALIST.** No source found. Sanity check on a same-titled
false lead (arXiv:2602.09769, "Metallic mean quasicrystals"): its matrix is the abelianization [[0,1],[1,n]]
(trace n), NOT the bundle monodromy (trace m²+2) — a different object, confirming ours is the right one.

**So the paper's honest shape:** a survey whose bricks are all classical (cited), whose *assembly* under
σ is the organizing contribution, and whose one specialist-gated novel bridge is the metallic-family
deformation tying the Markov/modular and cat-map layers together — alongside the two already-gated cores
(seam broken-lattice, held-breath field). **Before writing: read Dehornoy (2024) and Cannon–Dicks (2002)
in full** — they are the closest front-end prior art (cat-map ↔ figure-eight), and the paper must be built
*against* them, not over them. Caveat: a few lit-gate sub-agents ran while the safety classifier was down;
the load-bearing claims (Dehornoy scope, the (golden)²=RL identity, the classical links) were independently
re-checked here.
