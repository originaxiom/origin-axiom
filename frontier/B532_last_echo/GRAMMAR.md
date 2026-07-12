# THE INTERACTION GRAMMAR

*B532 — The Last Echo. Campaign deliverable.*

The object is the substitution σ: a→abAAB, b→aAB, A→abAB, B→aA on the free
group F₄ = ⟨a, b, A, B⟩. This document assembles the object's self-interaction
grammar as computed across cells I0–I4.

---

## 1. The irreducible kernel

The kernel is **the four words themselves**: abAAB, aAB, abAB, aA.

Not the incidence matrix M (which doesn't determine the grammar or Rauzy fractal).
Not the characteristic polynomial (which doesn't determine M — multiple matrices
share x⁴−2x³−5x²−4x−1). Not the grammar (which doesn't determine image lengths).
The four words carry strictly more information than any single invariant.

**What the kernel generates (24 layers, by pure computation):**

| Layer | Derived from | Depth |
|---|---|---|
| M (incidence matrix) | σ | 1 |
| Grammar (7/16 adjacencies) | σ | 1 |
| Swap s, symplectic D | σ | 1 |
| Return-word induction engine | σ | 1 |
| Charpoly, Perron eigenvalue β | M | 2 |
| Frequencies (φ, 1, φ√φ, √φ)/S | M | 2 |
| M mod 2 (F₂⁴ structure) | M | 2 |
| Rauzy fractal | M + σ | 2 |
| GL(4,Z) conjugacy class | M | 2 |
| 7 canonical induced types | induction | 2 |
| Self-containment of σ(a) | induction | 2 |
| Gap labels (Bellissard) | frequencies | 3 |
| Decider/courier roles | grammar + freq | 3 |
| Entropy h = log β | β | 3 |
| Disc = −400, Galois = D₄ | charpoly | 3 |
| Spectral type (Pisot, pure discrete) | charpoly + σ | 3 |
| Six-phase clock (2×3) | M mod 2 + induction | 3 |
| Projection algebra | σ + freq | 3 |
| Two linear orbits on F₂⁴ | M mod 2 | 3 |
| Golden section (deciders:couriers = φ) | freq + roles | 4 |
| Period-3 absent from spectrum | charpoly + clock | 4 |

**What the observer must bring (2 inputs, 5 additional layers):**

| Observer input | Layers it unlocks |
|---|---|
| SL₂C structure (gauge) | character variety, 9D trace map, σ*-fixed points |
| Potential V (coupling) | Schrödinger operator, gap widths/slopes |

---

## 2. The grammar's structure

**7 allowed transitions** out of 16: ab, aA, bA, Aa, AA, AB, Ba.

**Roles:**
- Deciders {a, A}: branch (multiple outgoing transitions), weight β = φ(1+√φ)
- Couriers {b, B}: don't branch (b→A always, B→a always), weight β/φ
- Deciders : couriers = φ : 1 (the golden section)
- Every image starts with 'a' (the lightest decider seeds every new generation)

**The grammar is strict:** no letter but A ever repeats; a never touches B; b never
touches a. The 9 forbidden pairs encode constraints that propagate through the word.

---

## 3. The projection algebra (I2)

σ is **irreducibly 4-letter**: none of 7 binary partitions commute with σ. No
2-letter projection is dynamically compatible. The four letters are entangled.

**Two projections read golden values:**

| Projection | Frequency ratio | Exact value | Pisot? |
|---|---|---|---|
| {aA}\|{bB} (structural vs tunnel) | 1.618034 | φ | NO (|λ₂|=1.47) |
| {ab}\|{AB} (old vs new) | 0.786151 | 1/√φ | YES |
| {aB}\|{bA} (cross) | 0.945027 | not simple golden | NO (|λ₂|=1) |

5 of 7 projections are Pisot; all 7 are primitive and grammar-compatible.

---

## 4. The self-description (I3)

σ describes itself using its own alphabet. Each image word σ(g) is a factor of the
fixed-point word ω, with its own return induction:

| σ(g) | Returns | q | Self-contains? |
|---|---|---|---|
| σ(a) = abAAB | 4 | 1 | **YES** (canonical codes = σ) |
| σ(b) = aAB | 4 | 1 | no |
| σ(A) = abAB | 4 | 1 | no |
| σ(B) = aA | 5 | 1 | no |

**The self-containment:** when you study how ω returns to its own first image word
"abAAB," the return words form a substitution system isomorphic to σ. The object
literally contains itself in the description of its own first letter. This persists
at depth 2 (σ²(a) also self-contains). The other three letters do not.

**The asymmetry:** 'a' is the seed letter (ω starts with a), the lightest decider
(weight φ/S = 0.272), and the unique self-reproducing anchor. The self-description
is not symmetric — it has a single fixed point.

**Return word nesting:** every return word of every image word contains other image
words as substrings. The descriptions nest at every level.

**Two linear orbits on F₂⁴:** under M mod 2, {a,b} and {A,B} trace two disjoint
6-cycles with phase offset 4. The linear orbits (from Parikh homomorphism) and the
affine orbit (from the bispecial sequence) are different dynamics on the same space.

---

## 5. The spectral clock (I1)

**Period-3 is ABSENT from the spectrum.** The six-phase clock (period 6 = 2×3 from
the F₂⁴ phase map) splits into:
- Period-2: SPECTRAL (from λ₂ < 0, the negative contracting eigenvalue)
- Period-3: COMBINATORIAL (from x²+x+1 ≡ 0 mod 2, cube roots of unity over F₂)

Complex eigenvalue period ≈ 2.54 (irrational) — no period-3 in the spectrum. The
two clocks are algebraically interleaved but physically decoupled.

**Fixed-point variety:** two components:
- Generic irreducible FPs: isolated (dim = 0), kernel = 2 = gauge
- Trace-zero family (κ = −2): dim = 1 complex, kernel = 4

Chat1's golden FP (tr(b) = 1/φ, κ = 1): NOT FOUND after 3100 seeds. Status: UNVERIFIED.

---

## 6. The prediction form

The interaction grammar's answer to "what does the observer need to bring?"

**Given the four words alone:** 24 layers are forced. The grammar, frequencies,
spectral type, gap labels, six-phase clock, self-containment, projection algebra,
golden section — all computable, all determined.

**Given the four words + SL₂C:** the representation theory (character variety, trace
map, fixed points) is additionally forced. SL₂C is the observer's choice of gauge —
how to represent the free group in 2×2 complex matrices.

**Given the four words + potential V:** the Schrödinger spectrum (gap widths, slopes,
period-2 oscillation) is additionally forced. V is the observer's choice of coupling
— how to turn the word into a physical operator.

**The grammar does not predict which SL₂C or which V.** The observer's choice of
gauge and coupling is FREE — it is not determined by the object. What IS determined:
once the choice is made, the resulting structure is rigid.

---

## 7. Cross-seat verification ledger

| Claim | Source | CC verdict |
|---|---|---|
| GL(4,Z) conjugacy (pair sub) | handoff | CONFIRMED (corrected P) |
| Core hierarchy (5 polynomials) | handoff | NOT REPRODUCED |
| Gap = core fraction identity | handoff | NOT REPRODUCED |
| dim=0 at irreducible FPs | chat1 | PARTIALLY CONFIRMED |
| Golden FP at tr(b)=1/φ | chat1 | UNVERIFIED |
| Induction charpoly law | B530 handoff | CONFIRMED (7 types, 1549/1549) |
