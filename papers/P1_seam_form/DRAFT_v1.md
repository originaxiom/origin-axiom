# The seam form: light and darkness in the divisor lattice of two clocks

**Complete draft v1 — 2026-07-08. Full prose with the narrative voice drafted (CC's rendering
of the owner's register, for the owner's final revision). This paper has NOT yet been through
its own literature gate or adversarial panel — those are the remaining steps before it reaches
the standard of the pilot (Paper 4). Claims traceable to the banked record (CLAIMS.md: S1–S12).
Novelty language is provisional pending the gate.**

---

## Abstract

Fix the two quantized cat maps W₁, W₂ of the golden and silver monodromies at level
N = 15 = tr(A₁A₂). Watch their interaction through the parity operator Par (the quantized
orientation-reversal): the *seam form* (a,b) ↦ tr(Par·P_a·Q_b), P_a and Q_b the spectral
projectors of W₁ and W₂, takes exactly **44 distinct values, all lying in ℚ(√5, √−3)**. A value's
four Galois channels {1, √5, √−3, √−15} vanish only when their cyclotomic support is empty, and
the possible vanishing patterns are exactly the **five** that realize the subfield lattice of the
Klein-four Galois group — with populations 120/20/20/10/70. Seventy points are *dark* (all four
channels gone), and fifty-four of those seventy sit at quantum closure. The whole architecture —
the light and the dark, and the commutator trace alongside them — **factors through the divisor
lattice of the two operator clocks**: two functions on the thirty-six cells (gcd(x,20), gcd(y,12)).
The proportions of light and darkness are the divisor arithmetic of the clocks that measure them.

---

## 1. Introduction

An interaction is easy to write down and hard to see. Two operators, a product, a trace — the
recipe is three symbols long, and it hides everything. This paper is about one interaction seen
clearly: two quantized cat maps, watched through a single involution, and the exact proportions
of light and darkness that come out. The surprise is not that structure appears — an arithmetic
object will always have structure — but that the structure is *arithmetic all the way down*: the
proportions of what survives and what cancels turn out to be the divisor lattice of the two
clocks by which the operators keep time. Nothing is fitted. The seam form is a shadow, and the
shape of the shadow is a fact about the number 15 = 3·5.

The two objects are the Weil / Hannay–Berry quantizations W₁, W₂ of the golden and silver
monodromies A₁ = [[2,1],[1,1]], A₂ = [[5,2],[2,1]] — the unique parabolic pair of the metallic
family (Paper 4) — at the level N = 15 that is their own product trace. The involution is Par,
the quantized image of −I, with det Par = −1: the operator through which orientation is read.
The seam form is what the pair looks like through Par. Section 2 defines it and states its
values; Section 3 proves the lemma the rest of the paper turns on — that a channel can only
vanish where its support is empty; Sections 4 and 5 read off the selection rules and the dark
locus; Sections 6 and 7 give the spectral fingerprint and the master theorem. The honesty
protocol is Paper 4's: classical material is cited, the one deferred step is named, and every
number carries a reproducer.

---

## 2. The seam form

Let ζ = e^{2πi/15}. On ℂ[ℤ/15]: the twist D = diag(ζ^{j(j−1)/2}), the unitary DFT F,
W_R = (F D F*)*, W_L = D, and W_m = W(R^m L^m) — the quantized cat map of A_m at level 15. Par is
the parity operator (Par ψ)(x) = ψ(−x). The orders are ord(W₁) = 20, ord(W₂) = 12; write P_a
(a ∈ ℤ/20) and Q_b (b ∈ ℤ/12) for the spectral projectors of W₁ and W₂.

**Definition (the seam form).** The seam form of the pair is (a,b) ↦ tr(Par·P_a·Q_b).

**Theorem S1 (values).** The seam form takes exactly 44 distinct values, all in ℚ(√5, √−3). Its
four Galois channels — the coordinates in the basis {1, √5, √−3, √−15} of ℚ(√5,√−3), the isotypic
pieces under Gal(ℚ(√5,√−3)/ℚ) ≅ (ℤ/2)² — are the natural coordinates for everything below.

The field ℚ(√5,√−3) is the compositum of the two ends of the object: √5 from the golden
(spherical, E₈) end, √−3 from the hyperbolic (E₆) end. The seam is where they meet, and its
values speak both languages at once.

---

## 3. The channel-vanishing lemma

Everything downstream rests on one observation, and it is the honest heart of the paper.

**Lemma S5 (channel vanishing = empty support).** A Galois channel of the seam form vanishes at
(a,b) if and only if the cyclotomic support of the corresponding character sum is empty. Vanishing
is never an accident of magnitude; it is forced by which cyclotomic frequencies the character can
carry. Two channels of a value are therefore not free to vanish independently — their supports are
governed by the same residue data, and the joint pattern is constrained.

*Sketch.* Each channel is a Galois-isotypic component of the character sum tr(Par·P_a·Q_b); by
the equivariance of the Weil representation under the Galois action on level-15 roots of unity
(the same mechanism that gives Coste–Gannon's Galois symmetry in rational conformal field
theory), the component is a sum over a residue class and vanishes exactly when that class carries
no surviving frequency. ∎

The lemma is why the dark locus is a *theorem* and not a table. Light is the generic case; a
point goes dark only when arithmetic forbids every channel at once, and forbidding is a
congruence condition, not a coincidence.

---

## 4. The selection rules: the subfield lattice

**Theorem S6 (five patterns).** Exactly five vanishing patterns occur across the 240 points:
none vanish (*free*), {√−3,√−15} vanish, {√5,√−15} vanish, {√5,√−3,√−15} vanish, all four vanish
(*dark*). These are precisely the five nodes of the subfield lattice of ℚ(√5,√−3): the whole
field, its three quadratic subfields ℚ(√5), ℚ(√−3), ℚ(√−15), and the rational floor. The
populations are:

| pattern | channels that vanish | surviving field | count |
|---|---|---|---|
| free | none | ℚ(√5,√−3) | 120 |
| rs | √−3, √−15 | ℚ(√5) | 20 |
| qs | √5, √−15 | ℚ(√−3) | 20 |
| qrs | √5, √−3, √−15 | ℚ (rational) | 10 |
| dark | all four | 0 | 70 |

The number 44 of distinct values and the five patterns are two faces of the same fact: the seam
form is *even* under the Galois group, and its vanishing set is a union of subfield strata.
Among the three quadratic subfields, **√−15 dies first** — it is the seam level's own field, and
it is the channel that vanishes in every non-free pattern.

---

## 5. The dark locus

**Theorem S7 (darkness concentrates at closure).** Of the seventy dark points, **fifty-four sit
at quantum closure** — the addresses (j,l) where [W₁ʲ, W₂ˡ] = I. Darkness is not scattered; it
pools where the two operators commute.

This is the paper's cleanest image. Where the interaction vanishes entirely — where the object,
watched through Par, shows nothing — is overwhelmingly where the two motions have come into
phase and their commutator has died. The light is the interference; the dark is the silence
after the two clocks agree. Sixteen of the seventy dark points lie *off* closure, and those
sixteen are the paper's one genuinely open residue (Section 8).

---

## 6. The spectral fingerprint and the cornerstone

**Theorem S2 (spectral invariants).** The seam operator carries the framing fingerprint
σ₁ = σ₂ = 1/24 — the central-charge signature c/24 of the quantization, independent of the pair.

**Theorem S3 (the cornerstone).** The distinguished quadratic subfield of the seam is ℚ(√−15) —
the field of the level itself. It is the first channel to vanish and the last structure to survive
the reduction to the rational floor: the cornerstone the other three subfields are set against.

**Theorem S4 (the exchange identity).** The half-monodromy exchange σ: W₁ ↔ W₂ (the Dehn-filling
pair, the Gieseking deck action) acts on the seam values by an explicit involution; the seam form
is symmetric under it up to the orientation sign carried by Par.

---

## 7. The master theorem: two functions on the divisor lattice

Here the spine's promise is paid.

**Theorem S9 (the divisor-lattice factorization).** Both maps on the order torus ℤ/20 × ℤ/12 —
the commutator trace κ_q(j,l) = tr[W₁ʲ, W₂ˡ] and the *tier* of the seam form (its vanishing
pattern) — factor through the divisor pair (gcd(x,20), gcd(y,12)). Each is single-valued on the
thirty-six divisor cells. The commutator trace factors as κ_q = ε(jl)·χ₅, where ε ∈ {3,−1} is the
quaternionic parity (from the mod-3 image Q₈) and χ₅ ∈ {5,1} is the mod-5 closure bit. The seam
tier factors by the same even-function mechanism (Cohen/McCarthy (r,s)-even functions; Serre's
ℚ-class principle) applied channel-wise.

**Theorem S10 (the magnitude law).** |κ_q(j,l)|² = #Fix([A₁ʲ, A₂ˡ] acting on (ℤ/15)²) — Howe's
formula. The divisors of 15 in the table are Howe's fixed-point counts at level 15; verified on
all 25 of the 5×5 principal window.

The master table — thirty-six cells, each carrying its κ_q value and its tier — is the paper's
final object, printed in full in the appendix. It is the answer to the spine: the light and the
dark of the interaction, and the commutator that measures how far the operators are from
commuting, are the *same* two functions, and both are read off the greatest common divisors of
the exponents with the two clock orders. The proportions of light and darkness are the divisor
arithmetic of the clocks.

That the factorization mechanism is classical (even functions; ℚ-classes) is stated plainly:
what is ours is the specific N = 15 seam, its five-pattern subfield-lattice selection rule, the
dark-locus/closure concentration, and the joint reading of κ_q and the tier on one lattice.

---

## 8. What we could not locate, and what remains open

The classical shelf: Weil-representation character values (Howe; Thomas), the CRT factorization
(Kurlberg–Rudnick), Galois equivariance (Coste–Gannon; Bantay), the even-function class
(Cohen; McCarthy), and the ℚ-class principle (Serre). Against that shelf, our search did not
locate: the explicit 44-value seam form at any composite level; the five-pattern subfield-lattice
selection rule; the dark-locus/closure concentration (54 of 70); or the joint (κ_q, tier)
divisor-lattice factorization. These are stated as ours, scoped, and *pending this paper's own
literature gate.*

Open: (i) the **cyclotomic-support step** — deriving each cell's tier from its support is verified
on all 240 points but not yet proven per channel; it is the paper's central open problem. (ii) The
**sixteen off-closure dark points** — the dark locus is not exhausted by the closure set, and the
residue is unexplained. (iii) The **seam at other levels** — whether the subfield-lattice selection
rule survives at levels other than 3·5, and how it degrades when a prime goes trivial.

---

## Appendix A: the master table

(The 36-cell table (gcd(x,20), gcd(y,12)) ↦ (κ_q, tier), printed in full as in Paper 4 §4.3;
reproducer `B474_tier_commutator_law/cross_table.py`, exact at p = 61, ℚ(ζ₆₀).)

## Appendix B: reproducibility

Per-claim script map: S1–S4/S11 (the seam bank B358–B367, B449); S5–S7 (`verify_patterns.py`,
B459/B468); S8/S12 (`br1_br2.py`, B469); S9/S10 (`cross_table.py`, `kq_verify.py`, B474/B472).
Each carries a lock re-run at draft. The Klein-four count correction (an earlier float miscount
of the dark set as 53 rather than the exact 70) is recorded in the corrections ledger.

---
*MSC 81Q50, 11L05, 11R18, 57K32, 11F27. Companion to Paper 4 (the Markov stage). Repository URL at packaging.*
