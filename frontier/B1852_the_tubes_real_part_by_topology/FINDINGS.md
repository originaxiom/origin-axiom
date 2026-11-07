# B1852 — THE TUBE'S REAL PART, BY TOPOLOGY: THE METRIC'S OWN τ AT THE TUBE IS 0 + 6.15(15) i (the real number Review 76 owed)

**Verdict: PROVED (data-free; exact integer matrices, with B1847's numerics identifying the fibre).** cc (main),
2026-11-07, S306k, at the owner's "continue". B1846 put the level surface through the tube on a reflection locus: "one
real number is owed (Review 76)". B1847 measured Im τ(Σ₀) = 6.15 ± 0.15 and left Re τ unresolved near the tube. 0 of 19.

## 1. The argument

- **Where τ can lie.** The excursion member's monodromy φ = L⁶RLR is a cyclic palindrome. Its isometry σ reverses
  fibre and circle (B1846). In the mapping torus σ(x, t) = (Jx, 1 − t), with J a det −1 involution such that
  J φ J⁻¹ = φ⁻¹.
  - σ fixes two fibres: one acted on by J, the other by φJ.
  - On each, σ is anticonformal, so that fibre's τ lies on its involution's reflection locus.
- **The two classes.** The det −1 involutions of GL(2, ℤ) form two conjugacy classes:
  - J ≡ I mod 2: the class of diag(1, −1), reflection loci reducing to Re τ = 0;
  - J ≢ I mod 2: the class of τ ↦ 1 − τ̄ and τ ↦ 1/τ̄, reducing to Re τ = ½ or ∣τ∣ = 1.
  Above ∣τ∣ = 1, the class alone decides the reduced real part.
- **The computation** (`verification/fixed_fibre_classes.py`, exact; every reversing involution with entries up to 14):

| word | reversing involutions | the two fixed fibres | B1847's numerics |
|---|---|---|---|
| m004 (LR), the control | 12 | both ≢ I: both at Re ½ | s = 0 at −0.5000, s = ½ at +0.5000 |
| **L⁶RLR, the read-out member** | 4 | **opposite classes: one at Re 0, one at Re ½** | anti-apex (s = ½) Re ½ to 7 × 10⁻⁷; tube (s = 0) −0.016 and −0.048 |
| L¹⁰RLR | 4 | opposite classes | none |
| L⁵RLR | 4 | both at Re ½ | none |

- **Which fibre is which** is not decided by the algebra. B1847's anti-apex sits at Re ½ to 7 × 10⁻⁷, so it is the
  ≢ I fibre, and the tube is the other σ-fixed level.
- **So the tube's level surface has reduced Re τ = 0 exactly.** B1847's direct readings at s = 0 (−0.016 and −0.048,
  near the degenerate core) agree.

## 2. The result

- **The metric's own τ at the tube is τ(Σ₀) = 0 + 6.15(15) i.** The real part is exact, by topology; the imaginary part
  is B1847's.
- **It differs from the record's other readings in its real part as well as its height.**
  - The Teichmüller apex is ½ + 3.65i (B1845: Re ½ exactly).
  - The pleated and tetrahedron readings are 2.87 and 2.58 in height.
- **A pattern, observed in four words and not proved:** the opposite-class case occurs for the words with an even run
  (L⁶, L¹⁰). Words whose runs are all odd put both fixed fibres at ½.
- **What it does not do.** It does not decide which of the four readings is the read-out's τ (P-714). It computes no
  coupling, scale or ratio, and compares nothing with data.

## Seen first

- **Swept:** `VERDICT topic-sweep /reflection locus|Re τ = 0|σ-fixed|reversing involution/: 2 of 1598 arcs on main match (PROVED 2); 13 register rows match (DECLINED 1, DONE 5, QUEUED 7)`. B1846 and B1847 name the reflection locus and leave the real part owed. No arc classifies the fixed
  fibres' involutions.
- **The literature:** the two conjugacy classes of det −1 involutions in GL(2, ℤ) are standard: involutions of the
  torus up to isotopy; anti-holomorphic involutions of the modular curve. The cut-and-paste picture of the mapping torus
  is standard. Both are named, not re-derived; the classes are checked here by brute force.

## 3. Disclosed

- **The identification of the tube as the Re-0 fibre rests on B1847's anti-apex numerics,** at 7 × 10⁻⁷ against the
  alternatives 0 and ½. It does not rest on a combinatorial assignment of involution to word position. Main's first
  draft assigned the classes to positions directly. The mapping-torus formula shows that the assignment depends on where
  the word is cut, so that claim is withdrawn and the result stands on the numerics.
- **That σ's fixed levels are s = 0 and s = ½ is B1846's normalisation** (θ∘σ = −θ + c, c = 0).

## Dated addendum (2026-11-07, S306l; the web seat's relay 991d7e2ac, harvest row 1614)

- **Main's own check** (`verification/addendum_k_family.py`, exact): on L⁶R(LR)^k for k = 1..5, every reversing
  involution puts σ's two fixed fibres in opposite classes (4, 4, 2, 2 and 2 of them). SnapPy's systoles are 0.18486980,
  0.18519963, 0.18521766, 0.18521832 and 0.18521828, matching the seat's table.
- **The seat's independent instrument** puts the tube at Re τ = 0 and the anti-apex at Re ½ for every k, to 3 × 10⁻⁹. Its
  values:
  - k = 1: τ(Σ₀) = 0 + 6.14916(41)i, inside this arc's 6.15 ± 0.15;
  - the sealed k → ∞ estimate: 0 + 6.06526(57)i.
  These are the seat's computations. Main has recomputed neither the k ≥ 2 values nor the limit (P-739).
- **The even-run pattern, sharpened to a per-centre rule.**
  - **The rule:** a σ-fixed fibre at the middle of an even run carries the class ≡ I mod 2 (Re 0). One at the middle
    letter of an odd run carries the class ≢ I (Re ½).
  - **Its prediction holds exactly:** L²R², L⁴R² and L²R⁴, with two even-run centres, put both fibres at ≡ I. L³R³,
    with two odd-run centres, puts both at ≢ I (`addendum_k_family.py`).
  - **Why it works:** in the mapping torus the cut lies in the middle of the product region, not at the gluing seam.
    So the fibre fixed by D (≡ I), the reverser of the linear palindrome read from an even run's middle, is the cut's
    own fibre.
  - **Its standing:** it holds in thirteen words and is not proved in general (P-740).
