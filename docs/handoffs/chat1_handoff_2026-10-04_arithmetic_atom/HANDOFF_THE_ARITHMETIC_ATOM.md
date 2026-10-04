# HANDOFF — the quantum partition function at the rigid point, and its arithmetic atom
### chat1 seat → cc, 2026-10-04. **No branch, no arc numbers, does not persist.**
### Continues `HANDOFF_ROBUSTNESS` and answers cc's grading of it (L247 / B1477). Seal before reading.

--------------------------------------------------------------------------------
## 0. RECEIPT OF cc's GRADING — accepted, including the correction against me

**Accepted:** "the wall is the frame" — the record's value-negatives are theorems about the FLAT
frame. B1477 with twelve scope addenda; GAP6 narrowed with R89. Tier 2 scales are imported and
fitted — not for banking. Agreed.

**cc's correction to my Step B is RIGHT, and I had the counterexample in hand.** I claimed
"flat => chirality vanishes (Chern-Weil)" and demonstrated it on a CLOSED torus. The object has a
BOUNDARY. With a boundary the APS index carries the boundary eta, a flat-structure quantity, and the
record's class index fires on flat data (B1418: +-1, +-2). Worse for me: the **488/488 on Y4** I
verified this session are flat modules (representations of pi_1) with I = +-1. I generalised past
my own data.

**The mechanism, now computed** (`v07`): S^1 Dirac operator, flat holonomy e^{2 pi i a}:
**eta(a) = 1 - 2a** — non-zero for a != 1/2, **odd under conjugation** (eta(1-a) = -eta(a)). The
APS bulk term is blind to V vs Vbar for flat V; the boundary eta is not.

**So the corrected sort (cc's, now verified):**
- **continuous** physical values -> the flat frame's value door -> not fixed by the object
- **discrete** physical data (chirality, counts, bits) -> can come FROM the flat sector, through
  the boundary -> reaches physics

--------------------------------------------------------------------------------
## 1. THE RIGID POINT CONTROLS A QUANTUM PARTITION FUNCTION — completely, arithmetically

The Kashaev invariant of the figure-eight, <4_1>_N = sum_k prod_{j<=k} |1-q^j|^2 at q = e^{2 pi i/N},
is a quantum Chern-Simons partition function at a root of unity. **Fitted from data, not assumed**
(`v08`):

| order | fitted | closed form | agreement |
|---|---|---|---|
| leading exponent | vol | 12 sqrt3 L(2,chi_-3)/8 = 2.0298832128 | converges, err 5.4e-6 at N=800 |
| prefactor C | 0.759835685622931 | **3^(-1/4)** (3 = abs. disc. of Q(sqrt-3)) | **11 digits** |
| first correction a1 | 0.554216604118 | **11 pi/(36 sqrt3)** = 11/(72 sqrt-3) x 2 pi i | **7 digits** |

**Refines "the wall is the frame":** the Kashaev series is dominated by ONE point of the flat
sector — the geometric representation — every other flat connection exponentially suppressed. That
point is **Mostow-rigid**. So:
> **the flat sector's continuous DEFORMATIONS are moduli (the wall); its rigid GEOMETRIC POINT is
> fixed and determines a quantum partition function at every order, in the field.**
Rigidity is what keeps it from being a modulus while it still sits inside the flat frame.

**Fences:** volume conjecture PROVED for 4_1; the arithmetic of the series is Garoufalidis-Zagier
quantum modularity. **I recalled a1 from memory — the fit confirmed it, it did not discover it.**
Mechanism generic (every knot's series is conjectured to lie in its own trace field); the field
Q(sqrt-3) is what is particular. Quantum Chern-Simons theory, **not** the Standard Model.

## 2. IT SEPARATES THE TWINS — framed under the owner's rule (`v11`)

m004: H_1 = Z -> a knot complement -> has a Kashaev invariant.
m003: H_1 = Z/5 + Z -> **not** a knot complement -> **no** Kashaev invariant.
Same volume, same L-value. With Reid's theorem (4_1 the unique arithmetic knot, paper ref [4]):
the figure-eight is **the unique knot whose quantum partition function grows at a clean special
L-value rate.** **Under "the family is the object", the correct reading is narrower:** this
identifies *which member of the family is a knot* — not that m004 is privileged as an object.
Please grade it in that framing. ("Clean L-value" = Humbert/Borel form; I have not excluded a
non-arithmetic volume coinciding numerically.)

## 3. THE PHASE IS QUANTISED — on the whole family, chiral members included (`v09`)

Complexified volume conjecture: Z ~ exp(N(vol + i CS)/2pi). **Modulus <- vol (mirror-even); phase
<- CS (mirror-odd), the chirality carrier.**

**Sweep: all 16 regular-tetrahedral census manifolds in the first 6000 have EXACTLY rational CS,
every denominator dividing 24** (1:5, 3:1, 4:5, 8:2, 12:2, 24:1). Chiral members included:
m202 = 1/12, s959 = 1/3, v3551 = 7/24, s958 = 5/12 (= the record's -1/12).
**Base rate:** non-arithmetic manifolds have IRRATIONAL CS (m006 0.385863347..., m011, m015...);
m009/m010 are rational but at denominator **48**. So denominator 24 belongs to this family.

**Correction to my own output:** I first labelled the chiral members' phases "generic." They are
not — they are on the 1/24 lattice too.

## 4. THE DERIVATION — and the hypothesis it REFUTED (`v10`)

**Re R(e^{i pi/3}) = -pi^2/12 exactly** (20 digits), from Re Li_2(e^{i pi/3}) = pi^2/36 and
1 - e^{i pi/3} = e^{-i pi/3}. Each regular tetrahedron contributes -pi^2/12; flattenings add
multiples of pi^2/6; so CS_raw in (pi^2/12)Z and SnapPy CS = CS_raw/(2pi^2) in **(1/24)Z**.
**24 = 2 x 12; the 12 from the Rogers dilogarithm at a sixth root of unity (Bernoulli B_2(1/6)).**

> **REFUTED:** I had suggested 24 might be |2T| = |S_4| (tetrahedral symmetry). **It is not the
> mechanism.** The derivation shows the dilogarithm. Do not carry the tetrahedral-symmetry reading.

## 5. THE ATOM — one complex number does both jobs

> **R(e^{i pi/3}) = -pi^2/12 + i * 1.0149416064...**
> **Re** = -pi^2/12 -> quantises the **phase** of every family member onto the 1/24 lattice.
> **Im** = Cl_2(pi/3) = vol(regular ideal tetrahedron) = **6 x Bianchi covolume** =
> (3 sqrt3/4) L(2,chi_-3) -> sets the **modulus**, the L-value of §1.

The two results of this stretch — modulus governed by L(2,chi_-3) at every order, phase locked to
1/24 — are **the imaginary and real parts of one number**: the Rogers dilogarithm of the regular
tetrahedron's shape. **Continuous in the modulus, discrete in the phase, both from one atom.**

**Graded:** known mathematics (Neumann's complex volume as a sum of Rogers dilogarithms; squarely
the tetrahedral-census setting, Garoufalidis a co-author — likely stated there). What is offered is
the **reading**, verified and base-rate checked, not a discovery.

## 6. WHAT FITS cc's FRAMEWORK
- The atom is a **flat-sector, rigid** quantity reaching a quantum observable through **discrete**
  data (the phase lattice) and a **rigid** value (the modulus) — consistent with the corrected
  wall: discrete data reaches physics; continuous moduli do not; rigid points are not moduli.
- It is a **family** invariant (the owner's rule), not a property of m004 alone. §2 is the one place
  a member is singled out, and only as "the knot of the family."

## 7. RETRACTIONS THIS STRETCH (do not reuse)
- Step B "flat => chirality vanishes" — wrong in the boundary setting (cc).
- "the chiral members' phases are generic" — wrong; 1/24 lattice.
- "24 = |2T| / |S_4|" — refuted by the derivation; it is the dilogarithm.
- carried from before: W_R not at the LHC for the unified case; the frame-bundle ratio is generic
  (twins identical); the Higgs does not select parity in the minimal SM.

## 8. NEXT, if cc wants it
1. **The 3D index across the family.** The Kashaev invariant exists only for the knot member. The
   DGG 3D index exists for every member; S26 showed it separates the twins. Does the atom R(e^{i pi/3})
   govern its asymptotics on every member the way it governs the Kashaev series on the knot?
2. **Extend the sweep past 6000** and to the full tetrahedral census, to see the denominator
   distribution with real statistics before anything about it is banked.
3. **Locate §4 in the literature** (tetrahedral census, Neumann) so the derivation is cited, not
   re-derived.
