# B856 — the hearing coupling obeys a period-5 law across the metallic family, and the sin²θ₁₂ reading is refuted on KIND

cc banking seat, 2026-08-02. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — B593's m = 1 value was banked; m = 2…20 are out-of-sample and were
predictions of nothing, so the honest footing is that they reproduce B593 exactly at m = 1 and the
period claim is checked against the group orders.


## 0. CORRECTIONS — applied 2026-08-02, same day, before this arc was pushed

**Five defects, found by self-audit and by an organ scan. Two are prior-art failures of exactly the
kind this repo's process finding names.**

**C1 — PRIOR ART: the observer-invariance is B641's, and B641 is stronger.** This arc reported
*"Re h is invariant across listener directions to 2.2×10⁻¹⁶."* **B641 (2026-07-16, sealed prereg
`b139e03a`, five gates at 60 digits) already banks**: *"Re(ζ⁻¹·ū M_odd u), ζ² = det, is
**ear-independent on ALL 360 elements** — max deviation **2.14×10⁻⁶⁰** over 360 × 6 exact ears."*
**Sixteen days earlier, at 44 more digits, over the whole group rather than one word family.**
And B641's **five-tone census** — |tone| ∈ {0, **1/(2φ)**, **1/2**, φ/2, **1**}, multiplicities
{90, 72, 120, 72, 6} — **contains this arc's Re h values as a subset.** This arc re-derived a
5-point section of a 360-element enumeration and read the section's local features as new laws.

**What survives as this arc's own:** that the **metallic family word RᵐLᵐ traverses those tones with
period 5**, and the **full modulus** |h|² ∈ {1/(φ√5), φ/√5, 1} with product 1/5. B641 normalises by
ζ and censuses |tone|; this arc does not normalise and tracks the family index. Related, not
identical — but the invariance and the tone values are **B641's, and are cited here as such.**

**C2 — h(5) = −1 is NOT an independent finding.** It is the **bare-weld value**: R⁵L⁵ acts as
**−I on the odd plane**, verified directly. Period-5 and h(5) = −1 were listed as two facts. **They
are one.** Double-counting outputs is the exact DOF inflation that killed 21 candidates, committed
in the arc arguing for DOF discipline.

**C3 — the mechanism was misattributed.** This arc implied the conjugation twist C drives the
collapse. It does not: the **untwisted** weld also has period 5, and the **2×2 block on the odd
plane itself** has period 5 while the full matrix has 15. **The collapse is the odd-plane
restriction.**

**C4 — the scope was wrong in both directions.** Period 5 and the |h|² golden set are **class**
properties — every two-block word family with equal growth rate collapses (RᵐLᵐ, LᵐRᵐ, R²ᵐL²ᵐ,
RᵐLᵐ⁺¹, Rᵐ⁺¹Lᵐ all 15→5), while three-block and unequal-growth families do not. **What is
specific is the phase quantization**: arg/(π/10) ∈ {3, −7, 7, −3, −10}, all integers, for
**balanced** words (#R = #L); the unbalanced ones give **thirds** and never integers.

**C5 — the resolvent identity, added and correctly scoped.** v₁, v₂ **are** the eigenvalues of
(I+M)⁻¹, with det(I+M) = Δ(−1) = det(4₁) = **5** — a standard fibered-knot identity, and it
**explains** the golden-point values from the Alexander polynomial. But: **det(I+M) = tr(M)+2 for
every M ∈ SL(2)**, so the eigenvalue **sum is always 1 and carries no information**; only the
product does, and `det(I+Mₘ) = m²+4` gives 5, 8, 13, 20, 29 while |h|²'s product stays **1/5
forever**. **The identity holds at m = 1 and fails at every m ≥ 2.** Also `φ²+1 = φ+2 = φ√5` are
the same number, so `v₁ = 1/(φ²+1)` is a rewriting, not a new formula.

**Net: the period-5 traversal and the |h|² product stand as this arc's contribution. The
observer-invariance and the tone values are B641's. One headline fact is deleted as double-counted,
the mechanism is corrected, and the scope is narrowed to phase quantization under balance.**

## 1. The law

B593 computed the coupling number `h = u₃† M_odd(g) u₃` at the **golden weld only** (g = RL). The
metallic family's bundle monodromy is the word **RᵐLᵐ** — SL(2,ℤ) trace **m² + 2**, which is B179's
banked metallic monodromy trace (3 golden, 6 silver, 11, 18, 27, …). The family law was **one loop
away from a banked arc** and had never been run.

| m mod 5 | h(m) | \|h\|² | arg/π |
|---|---|---|---|
| **1** | **1/(2φ) + i·sin(2π/5)/√5** | **1/(φ√5)** | +0.3 |
| 2 | −1/2 − 0.688190960236 i | φ/√5 | −0.7 |
| 3 | −1/2 + 0.688190960236 i | φ/√5 | +0.7 |
| 4 | 1/(2φ) − i·sin(2π/5)/√5 | 1/(φ√5) | −0.3 |
| **0** | **−1 exactly** | **1** | −1.0 |

Verified to m = 20. **B593's m = 1 value reproduces exactly.** `h₃` and `h₆` are complex conjugates
at every m. `|h|²` takes exactly three values — **1/(φ√5), φ/√5, 1** — and the two golden ones
**sum to exactly 1**.

## 2. Why the period is not trivial

**order(R) = order(L) = 15**, and the welded matrix **RᵐLᵐ has period 15** — verified directly. But

> **h(m) has period 5. The listener's θ-odd quadratic form collapses the period 15 → 5, a factor
> of 3.**

Had the generators had order 5, the periodicity would have been automatic and empty. They do not.
The collapse is a property of the θ-odd plane, not of the group.

**And the 5 is the programme's own 5.** B261 banks the AJ recursion at the golden root `q = ζ₅` as
**antiperiod 5**, with *"the period is exactly 5 = k+2 = det(4₁)."* Two independent period-5s now
agree — a quantum recursion on one face and a coupling form on another.

## 3. It is a COUPLING quantity, and that is the point

`M_odd` is the object's monodromy weld; `u` is the listener's direction. **Neither determines h
alone.** And measured here: **Re h is invariant across listener directions to 2.2×10⁻¹⁶** — the
observer's freedom moves the phase and not the real part.

This is the shape the framework requires and the corpus was missing: **the coupling FORCING a value
rather than carrying one.** Forcing costs no parameters. It also uses the whole structure — the
being face supplies `M_odd`, the hearing face supplies φ, the observer supplies u, and θ separates
odd from even.

## 4. The sin²θ₁₂ / JUNO reading — REFUTED ON KIND

A reading was proposed in which `Re h = 1/(2φ) = 0.309017` is the solar mixing angle
`sin²θ₁₂ = 0.307 ± 0.013`, with JUNO to decide. **It does not survive, and the repo's own register
already contains the reason.**

| quantity | value | vs 0.307 ± 0.013 | kind |
|---|---|---|---|
| `Re h = 1/(2φ)` | 0.309016994 | **+0.16 σ** — matches | **real part of an amplitude** |
| `\|h\|² = 1/(φ√5)` | 0.276393202 | **−2.35 σ** — excluded | **modulus squared** |

**`sin²θ` is a probability — it is |amplitude|². The kind-correct quantity is |h|², and it is
excluded at 2.35σ. The quantity that matches is the wrong kind.** The register itself calls
`1/(φ√5)` *"the kind-correct mixing number"*, so the programme had already noticed.

**Look-elsewhere:** the 1σ window [0.2940, 0.3200] contains **at least 17** natural candidates —
3/10, 4/13, 5/16, 5/17, 6/19, 7/22, 7/23, 8/25, 8/27, 9/29, 10/33, 11/35, plus 1/(2φ), (√5−1)/4,
1/π. A match in that window is worth ~nothing without a mechanism.

**The one thing that distinguishes this from the 21 dead DOF-0 candidates** is that `1/(2φ)` was
**computed** (B593, a hearing-law arc about parity and second-order amplitudes) rather than
searched. That is a real distinction — and it does not repair a kind error. **Computed and
mistyped is still mistyped.**

**Verdict: the family law stands; the neutrino reading does not.** No row waits on JUNO.

## 5. What this does NOT establish

- **No dictionary.** h is a quadratic form on a θ-odd plane in SU(3)₂ modular data. Nothing
  connects it to any physical observable, and §4 is what happens when a connection is asserted.
- **Not preregistered.** m = 1 was banked; the extension is new. Its footing is exact reproduction
  at m = 1 plus the independent group-order check on the period.
- **Does not show the period-5 is object-specific.** It is a property of SU(3)₂'s modular data and
  the metallic word; whether another family collapses differently is untested.
- **Nothing to `CLAIMS.md`.**

## Carried forward

1. **Test the period on other words** — is 15 → 5 special to RᵐLᵐ, or does any word's θ-odd form
   collapse? That decides whether the law is about the *family* or about the *plane*.
2. **The B261 convergence** — two period-5s from different faces. Whether they are the same 5
   is a computation, not an observation.
3. **A dictionary, or nothing.** Without a mechanism from a modular-data quadratic form to an
   observable, no value from this construction may be compared with a measurement.

`tests/test_b856_hearing_family.py`
