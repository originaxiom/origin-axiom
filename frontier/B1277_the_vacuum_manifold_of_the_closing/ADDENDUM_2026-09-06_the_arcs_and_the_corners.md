# Addendum (2026-09-06) — THE ARCS AND THE CORNERS: the two fixed arcs of each inversion end at four corners of the cusp torus; the corners lie on the zero set of the θ-odd Higgs field's radial component, but the partition they sit on is annular — χ(∂⁺M) = 0, by the object's own symmetries

**Prompted by the owner:** *"do the two Fix(θ) arcs give χ(∂⁺M) ≠ 0? Arcs cut corners."* Part (e) of this arc closed
L204 with χ(M, ∂⁺M) = 0 without looking at the fixed arcs. Here they are looked at.
`verification/arcs_and_corners.py` (SnapPy for the holonomy and the symmetry group; the rest exact or on a
480 × 480 grid; `SELFTEST: PASS`; run record `verification/arcs_and_corners_run.txt`).

## 1. The eight isometries on the cusp torus, with their translation parts

SnapPy gives the linear parts only (all four sign patterns diag(±1, ±1) on (μ, λ), each twice). The horoball
pattern of the cusp — the centres γ(∞) and sizes 1/|c|² of 11 097 holonomy elements (words to length 9, the cusp
sent to ∞, the longitude made real: t_μ = i, t_λ = 2√3) — has **sixteen** affine symmetries, twice too many: the
pattern alone carries a spurious order-4 translation. The genuine eight are the candidates N that **normalize the
holonomy group**, tested on both generators by the horoball dictionary (h ∈ Γ iff h(∞) is a pattern centre reached
by a word w with (T_m w)⁻¹h a lattice translation). In coordinates x along λ, y along μ (both mod 1):

| cusp map (μ, λ) | translation parts | what it is on the torus | in M |
|---|---|---|---|
| (+, +) | (0, 0), **(½, 0)** | identity; the half-translation T along the longitude | the period-2 symmetry |
| (−, +) | (¼, ½), (¾, ½) | glides along λ by a quarter with a half-shift in μ, **order 4, no fixed points** | the amphichiral rotoreflections |
| (+, −) | (¼, ½), (¾, ½) | glides along μ by a half, order 2, **no fixed points** | orientation-reversing involutions without a fixed surface |
| (−, −) | (0, 0), (½, 0) | rotations by π with **four fixed points each** | the two inversions θ, θ′ = θT |

The corners: θ fixes (0, 0), (0, ½), (½, 0), (½, ½); θ′ fixes (¼, 0), (¼, ½), (¾, 0), (¾, ½). Each inversion's fixed
set in M is two arcs (a circle minus two points of the knot), and each arc's two ends are two of these four corners
— **the arcs do cut the corners**: the cusp torus modulo θ is the pillowcase whose four cone points are exactly
these. No isometry is a reflection: the μ-reversing and λ-reversing involutions are glides, so no fixed circles
are forced on the torus and no totally geodesic surface bounds on the cusp.

## 2. The θ-odd Higgs field at the cusp: the allowed modes

The b₁ class (dual to the meridian) is odd under every μ-reversing isometry (ε = the (μ, μ) entry of the cusp map)
and even under the rest; its harmonic representative φ obeys σ*φ = ε(σ)φ, so the radial component g = φ(∂_r) on
the cusp torus obeys g∘σ = ε(σ)g for all eight σ. Writing g = Σ c_{k,l} e^{2πi(kx + ly)}, the constraints
c_{Ak} = ε e^{−2πi(Ak)·b} c_k select the allowed Fourier orbits; the slowest-decaying allowed one dominates at large
cusp height and decides ∂⁺.

| orbit (k along λ, l along μ) | decay rate | allowed dimension |
|---|---|---|
| (±1, 0) | 0.289 | **0** (killed by T: k must be even) |
| **(±2, 0)** | 0.577 | **1** — the leading mode |
| (±3, 0) | 0.866 | 0 |
| (0, ±1) | 1.000 | 0 (killed by the order-4 glides) |
| (±1, ±1) | 1.041 | 0 |
| (±2, ±1) | 1.155 | 1 — the first mixed mode, twice the leading rate |

**The leading allowed mode is g ∝ sin(4πx)**: a pure longitude mode. Its zero set is the four meridian circles
x ∈ {0, ¼, ½, ¾} — **through all eight corners** (symmetry residuals 10⁻¹⁵). {g > 0} is two annuli, {g < 0} two
annuli: **χ(∂⁺M) = χ(∂⁻M) = 0.** At the corners g = 0 with |∇g| maximal: the zero set is smooth there; the corners
are ordinary points of the sign-change circles, not vertices of a disc decomposition.

## 3. The answer

**No.** The arcs' corners lie on the zero set of the Higgs field's radial component, as the owner's picture has
it, but the object's symmetries force the leading sign pattern at the cusp to be the pure longitude mode
sin(4πx), whose regions are annuli. A disc — hence χ(∂⁺M) ≠ 0 and a net chiral zero mode — would need a mixed
mode (k, l both non-zero) to lead; the first allowed one, (±2, ±1), decays twice as fast and is never dominant.
Part (e)'s closure of L204 stands, now with the arcs and the corners accounted for.

**Caveat, stated:** the argument uses the symmetry-allowed mode structure; it assumes the (±2, 0) coefficient of
the object's actual harmonic form is non-zero (generic — the isometry group D₄ is fully used, and no further
symmetry could force it to vanish). If it vanished by accident, the (±2, ±1) mode would lead and cut the torus into
eight rectangles, χ(∂⁺M) = ±4 — a computation of the harmonic 1-form's cusp coefficients would settle it; it is not
run here. The non-abelian θ-odd E₆ deformation (B1268) reduces, Cartan component by Cartan component, to the same
mode analysis with the same parities, so the same annular partition follows for each charged sector.

## Verification

`verification/arcs_and_corners.py` (~1 min; SnapPy required), run record `verification/arcs_and_corners_run.txt`;
lock `tests/test_b1277_the_arcs_and_the_corners.py` (skips without SnapPy). Feeds on: SnapPy's symmetry group and
holonomy of m004 (D₄, cusp shape 2√3 i), B1268 (the θ-odd deformation and the cusp bound), part (e) of this arc
(the Alexander zero modes), Pantev–Wijnholt (χ(M, ∂⁺M)). The affine actions are derived from the holonomy, not
read off a picture; the sixteen-versus-eight discrepancy of the horoball pattern is the control that the
normalization test is needed.
