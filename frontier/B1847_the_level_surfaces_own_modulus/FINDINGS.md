# B1847 — the level surface's own modulus (P-727; data-free)

*Main, 2026-11-06, at the owner's choice ("P-727: the level surface"), after B1846. The question: what conformal shape
does the metric itself give the fibre, read on the harmonic level surface Σ_s = {θ = s}? B1846 placed the read-out's
weight on the tube. This arc reads the metric's own τ there, beside the three object-native readings that disagree
(P-723). Every number below is computed by a script in `verification/`, with its committed output. No measured number is
read, no held-out quantity is computed, and nothing is compared with data. 0 of 19.*

## 1. The instrument

- **What is computed.** The conformal modulus of a level surface, from its shape in ℍ³ and its fibre group alone.
- **Why the plain 3D shape suffices.** In 3D the hyperbolic metric is conformal to the Euclidean one. So the surface's
  conformal class, and with it τ, can be read from its Euclidean shape in upper half-space.
- **The three energies.** Take the harmonic functions on Σ with periods (1, 0) and (0, 1) on the fibre group's
  generators x, y. Their Dirichlet energies E give Im τ = 1/E₂₂ and Re τ = −E₁₂/E₂₂, and det E = 1 exactly, a free check.
- **The fundamental piece.** The fibre group F = ⟨x, y⟩ (χ = 0, [x, y] the fibre's cusp translation) preserves Σ. Its
  Ford domain cut by Σ is a fundamental piece: a strip above a floor, with side pairings by F's face elements.
- **The mesh.** A structured column mesh, with a column at every floor node. Each paired arc carries its nodes and their
  exact images, so every pairing is node to node, and there are no holes. Pairings and vertex cycles are tracked by a
  union-find that carries the period offsets: an inconsistent cycle is detected.
- **The energies.** The cotangent Laplacian on the triangles' 3D positions.
- **The comparison.** τ is reduced to the standard fundamental domain, so it can be compared without fixing a marking.

## 2. The control: a Fuchsian group of known τ (`stage_a_control.py`, `stage_a_control_run.txt`)

- **The group.** Jorgensen's normal form, built from B1667's Fricke traces of τ₀ (P-723's stage A). Its traces and
  determinants hold to 10⁻¹², and [A, B] is z ↦ z + 2.
- **Second-order convergence** at three resolutions: the error falls by about 4 per doubling, and det E − 1 falls with it.
- **Richardson extrapolation** recovers τ₀ = 0.23 + 1.41i and −0.31 + 1.07i to better than 2 × 10⁻⁴.
- **A curved copy agrees.** The same mesh, mapped by a 3D inversion into a curved surface, converges to the same τ. This
  tests the cotangent path on curved triangles.
- **A failure, disclosed.** A first mesh, which dropped triangles by a centroid test, left holes along the arcs and
  stalled at an error of 3 × 10⁻³. It was replaced by the column mesh.

## 3. m004: the metric's loop of shapes (`stage_b_modulus.py`, `stage_b_m004_run.txt`)

- **The surface.** The level surface is a graph v(u, t) over the strip. It is tabulated by Newton continuation, with φ
  evaluated by exact pullback, and spot-checks to |φ − s| ≤ 3.5 × 10⁻⁹ on the domain (the maximum over the levels; Review 76). It never folds there
  (|∂φ/∂v| ≥ 0.47).
- **The pairings.** On m004 they land on the surface to 1.8 × 10⁻⁸ and on the floor to 10⁻⁵. No vertex cycle is
  inconsistent. [Review 76: on the excursion they land on the floor's interpolant to 4.4–6.5 × 10⁻⁴ at the narrowest
  faces, at both resolutions, because the check reads an interpolated floor. The paired nodes themselves sit at exact
  heights.]
- **Reduced τ, Richardson from (120, 80) and (240, 160):**

| s | τ(Σ_s) | the check |
|---|---|---|
| 0 | −0.5000 + 1.12438i | σ-fixed level: Re τ = ½, forced |
| ¼ | i (0.0003 + 1.0000i) | two symmetries: the square torus, forced (asserted; it holds numerically to about 10⁻⁵, and no script exhibits the isometries; Review 76) |
| ½ | +0.5000 + 1.12439i | the half-shift: the same point as s = 0 |
| ¾ | i | forced |
| 1 | the s = 0 point (−0.4995 + 1.12438i, at (120, 80)) | the loop closes in moduli space: a consistency check, since Σ₁ = Σ₀ in M (Review 76) |

- **The new number.** The golden Teichmüller axis passes exactly through i and has its apex at ½ + (√5/2)i = ½ + 1.11803i.
  The metric's loop also passes through i, but its symmetric level sits at Im τ = 1.12438, **0.57 % above the Teichmüller
  apex**, far outside the error of about 10⁻⁴. The pleated and tetrahedron readings of m004 are both the hexagonal point,
  Im τ = 0.866.
- **So on the golden member, the metric's own reading tracks the Teichmüller geodesic closely, but is not it.**

## 4. The excursion member L⁶RLR

- **The level surface folds near the tube.** At fixed (u, t), a line crosses Σ₀ 3 to 5 times per period below t ≈ 0.5,
  in two windows of u (`fold_scan.py`, `fold_*.txt`).
  - The cause: θ vanishes on the tube's core and is nearly constant across the tube. So Σ₀ twists around the core like a
    helicoid, and a graph v(u, t) cannot describe it.
  - The graph method's first run at s = 0 failed its own checks (det E − 1 = 0.19; pairings 5 × 10⁻² off the floor),
    localised to the fold windows by a per-face diagnostic. **No number from it is used.**
  - At s = ¼ no line ever folds. At s = ½ two lines fold marginally below t = 0.40, beneath that level's floor (≥ 0.757; `exc_s0.5_full_run.txt`).
- **A second instrument, for folded surfaces** (`stage_c_general.py`):
  - marching tetrahedra on the exact level, in a grid periodic in u;
  - vertices projected onto the exact level, to ≤ 10⁻¹³;
  - the floor clipped and projected onto the exact sphere intersections;
  - pairings imposed node-to-segment through a KKT system.
- **It is validated two ways:**
  - on m004 at three grids (`gen_m004_40_run.txt`, `gen_m004_80_run.txt`, `gen_m004_120_run.txt`), it converges to the graph method's −½ + 1.12438i (−0.49986 + 1.12444i at the finest;
    det E − 1 = 2.0 × 10⁻⁴);
  - on the excursion at s = ¼, it agrees with the graph method to about 10⁻⁴. These are two meshings, not two independent
    methods: they share φ, the fibre group's face list, the cotangent energy and the τ formula (Review 76). (−0.372174 + 1.008394i against the
    Richardson −0.37218 + 1.00851i).
- **The readings that hold** (reduced τ):

| level | the metric's τ(Σ_s) | the Teichmüller reading at the same symmetric point | the gap |
|---|---|---|---|
| s = ½, the anti-apex (the middle of R L R) | ½ + 1.5904i (Re ½ to 6 × 10⁻⁶ at the finest mesh and 7 × 10⁻⁷ after Richardson, forced; det E − 1 = 2.8 × 10⁻⁴; one method) | ½ + 1.3693i (√(15/8)) | +16 % |
| s = ¼ | −0.3722 + 1.0085i (two methods) | — | — |
| s = 0, the tube (the apex) | **not yet computed** (§ 5) | 3.6515i (√(40/3)) | — |

- On m004 the same comparison at its apex gave +0.57 %. The metric's reading moves further from the Teichmüller reading on
  the member that has a run.


## 5. What this decides, and what it does not

- **Decided: the metric gives the fibre a definite conformal shape at every level, and it is a fourth reading.** It is
  neither the Teichmüller point, nor the pleated layer, nor the tetrahedron.
  - On m004 it stays close to the Teichmüller geodesic: it passes through i with it, and sits 0.57 % above its apex.
  - On the excursion member it departs further: +16 % at the anti-apex.
- **Not decided: the value at the tube.**
  - At s = 0 the level surface twists around the tube's core like a helicoid.
  - The core lies on a face of the fibre group's fundamental piece: its axis points sit on an F-sphere, to a
    penetration of 8 × 10⁻¹⁴, under both sphere searches (`sphere_complete.py`, `sphere_complete_run.txt`).
  - So the piece near the tube is a thin, twisted strip pressed against a face.
  - Both instruments fail their own checks there, so no number is reported.
  - The general mesher's tube runs are disclosed in `gen_exc_s0_80_run.txt` (det E = 7.1) and
    `gen_exc_s0_deepgrid_UNTRUSTED_run.txt` (det E − 1 = 3.1 × 10⁻²). The latter's settings fail the s = ¼ control
    (`gen_exc_s025_deepgrid_FAILED_run.txt`, det E = 2.44), so it is not used. [Review 76: the two logs were left
    uncommitted at the landing; they are committed now.] **P-727 stays open for this one value.**
- **Not decided: whether this reading is the frame's.** The level surface's modulus is metric-native given harmonic
  time. Which modulus the frame's couplings take is a reading (P-723), and this arc adds a fourth to the menu without
  ranking the four.
- **No coupling, ratio or scale was computed. No value is compared with data.**

## 6. Disclosures

- **Instrument errors caught by the integrity checks and fixed before any reading:**
  - a circle-translate sign;
  - the first mesh's holes;
  - a surface table reaching below the domain;
  - a fold-test window centred on the wrong sheet;
  - a graph parametrization used where the surface folds.
- **A grid extended below a level's floor exposes missing small spheres.** The general mesher therefore keeps only the
  component connected to the cusp. Its s = ¼ result was taken with the grid bottom at 0.33. That is below that level's floor (0.787;
  `exc_s0.25_full_run.txt`), but above the heights where the missing small faces matter. [Review 76: the sentence
  first said "above", which contradicted itself.]
- **The graph method's floor nodes now sit at exact heights.** The readings moved by at most 10⁻⁶.

## Seen first

- **Swept:**
  - `VERDICT topic-sweep /conformal modulus|level surface|period matrix|Dirichlet energ/: 2 of 1593 arcs on main match (PROVED 1, no verdict file 1); 2 register rows match (QUEUED 2)`.
    The arcs are B1846 and this one; the rows are P-723 and P-727.
  - `VERDICT topic-sweep /harmonic (map|form|function)/: 0 of 1591 arcs`, before B1846.
  - `VERDICT topic-sweep /helicoid|level surface folds|surface folds/: 1 of 1593 arcs on main match (PROVED 1)`. The
    match is this arc.
- **Read:** B1846 (harmonic time), P-723 (the three readings), B1667 (the uniformising monodromy) and B1295.
- **What the sweep found:** nothing on the record computes a level surface's conformal modulus.
- **The literature:**
  - conformal invariance of the 2D Dirichlet energy;
  - the period-matrix form of a torus's modulus;
  - Jorgensen's normal form for punctured-torus groups;
  - the cotangent Laplacian (classical).

## 7. A ruling asked of main on the way (B1012; the owner: "Main rules on B1012 first")

- **The question.** The web seat asked which theory R2's scale weight comes from: the volume conjecture's single
  holomorphic block, or B1012's full complex Chern–Simons theory.
- **They are pieces of one theory**, the full amplitude being built from holomorphic and antiholomorphic blocks.
- **The math does not choose between them; a premise does.** A chiral amplitude takes the single block. The record's hand
  bit argues for that, without deriving it.
- **Under that premise, R2's form is not the block's value at level 5.** By `kashaev_block.py` (knot invariants only;
  no scale is computed):
  - the exact Kashaev invariant ⟨4₁⟩₅ is 46 + 2√5 = 50.472;
  - R2's leading exponential exp(5 Vol/2π) is 5.030;
  - the proven asymptotic 3^(−1/4) N^(3/2) exp(N Vol/2π) (Andersen–Hansen; named, not re-derived) holds only as N grows:
    the exact-to-asymptotic ratio is 1.18 at N = 5 and 1.007 at N = 80.
- **So R2 stays CHOSEN.** The ruling is relayed in `docs/handoffs/CC_TO_CHAT1_2026-11-06_THE_RULING_ON_B1012.md`
  (harvest row 1602).
