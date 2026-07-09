# The seam form — [FROZEN INTERNAL NOTE, NOT PUBLICATION-READY]

**⚠ FROZEN (2026-07-09) as an internal note.** After three adversarial re-panel rounds, this write-up
still carries framing/labelling defects (documented in `SCRUTINY_P1P3_round3.md`); solo iteration did
not converge. It is retained as an internal record only. **The verified mathematics lives in the cited
B-nodes** (the seam bank B358–B367, B459, B474); do not circulate this as a paper. P4 is the only paper
that cleared the gauntlet.

**Complete draft v4 — 2026-07-09. v4 corrects a MAJOR defect the re-panel (round 2) confirmed: the
object must be defined as the ℚ(√5,√−3)-isotypic *projection* (Galois average) of the seam trace, not
the raw trace itself — the raw trace tr(Par·P_a·Q_b) lies in ℚ(ζ₆₀) and is non-real at all 49 support
points (CC-verified). All downstream results (30 values, 49 support, channels, selection rule, dark
locus) hold verbatim for the projection. v3 folded in the prior-art assessment (B491): the selection
rule is APPEARS-NOVEL / NEEDS-SPECIALIST, with the Dong–Lin–Ng signed-permutation argument in §8. v2
(2026-07-08) revised after the first panel: v1 mis-stated the value count (a channel-support size, 44,
was reported as the number of distinct
values), mislabeled the realized field-set as the full subfield lattice (ℚ(√−15) is in fact never
realized, and the zero stratum was omitted), conflated the value torus with its Fourier dual, and
marked a still-open lemma as proved. All four are corrected here, with the exact numbers recomputed
at revision. Full prose in the owner's register. NOT yet through its own literature gate or a
re-panel. Claims traceable to the banked record (CLAIMS.md: S1–S12; B358–B367, B459, B468, B474).**

---

## Abstract

Fix the two quantized cat maps W₁, W₂ of the golden and silver monodromies at level
N = 15 = tr(A₁A₂). Watch their interaction through the parity operator Par (the quantized
orientation-reversal): the seam trace (a,b) ↦ tr(Par·P_a·Q_b), with P_a, Q_b the spectral
projectors of W₁ and W₂, lives in the cyclotomic field ℚ(ζ₆₀). Its **ℚ(√5,√−3)-isotypic
projection** — the Galois average over Gal(ℚ(ζ₆₀)/ℚ(√5,√−3)), which we call the *seam form* — is
defined on a 49-point support of the (a,b) order grid and takes exactly **30 distinct values, all
in ℚ(√5, √−3)**. (The raw trace is non-real and degree-8 over ℚ; it is the biquadratic *shadow* of
the interaction that carries the structure below.) Fourier-transforming its four Galois
channels {1, √5, √−3, √−15} to the dual torus ℤ/20 × ℤ/12, a channel vanishes only where its
cyclotomic support is empty, and the joint vanishing pattern realizes exactly **four surviving
fields plus the zero stratum**: the full field ℚ(√5,√−3) (120 points), ℚ(√5) (20), ℚ(√−3) (20),
the rational floor ℚ (10), and **0** — the *dark* locus — at 70 points. The one quadratic subfield
that is **never** realized is ℚ(√−15), the field of the level itself: its channel dies in every
nontrivial pattern. So the selection rule is not the whole subfield lattice, but the lattice *with
the √−15 node deleted and a zero stratum adjoined* — a broken lattice, and the break is the
seam-level's own field. Of the 70 dark points, 54 sit at quantum closure ([W₁ʲ,W₂ˡ]=I). The whole
architecture — the light, the dark, and the commutator trace beside them — **factors through the
divisor lattice of the two operator clocks**: two functions on the thirty-six cells (gcd(x,20),
gcd(y,12)). The proportions of light and darkness are the divisor arithmetic of the clocks that
measure them.

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
monodromies A₁ = [[2,1],[1,1]], A₂ = [[5,2],[2,1]] — the first two members of the metallic family
(Paper 4) — at the level N = 15 that is their own product trace. The matrices A₁, A₂ are
hyperbolic (Anosov); it is their *commutator* whose trace governs the interaction. The involution
is Par, the quantized image of −I, with det Par = −1: the operator through which orientation is
read. The seam form is what the pair looks like through Par.

Three domains appear below, and the paper's first job is to keep them apart, because v1 did not.
(i) The *value torus*: the (a,b) grid of projector indices, on which the seam form takes its 30
values. (ii) The *dual torus*: the Fourier transform ℤ/20 × ℤ/12 of the four channels, on which
the 240 vanishing patterns and the dark locus live. (iii) The *divisor lattice*: the 36 cells
(gcd(x,20), gcd(y,12)) through which the commutator trace and the pattern-tier factor. Section 2
defines the form and states its values on (i); Section 3 proves the channel-vanishing lemma;
Sections 4 and 5 read the selection rule and the dark locus on (ii); Sections 6 and 7 give the
spectral fingerprint and the master theorem on (iii). The honesty protocol is Paper 4's:
classical material is cited, the one deferred step is named, and every number carries a reproducer.

---

## 2. The seam form

Let ζ = e^{2πi/15}. On ℂ[ℤ/15]: the twist D = diag(ζ^{j(j−1)/2}), the unitary DFT F,
W_R = (F D F*)*, W_L = D, and W_m = W(R^m L^m) — the quantized cat map of A_m at level 15. Par is
the parity operator (Par ψ)(x) = ψ(−x). The orders are ord(W₁) = 20, ord(W₂) = 12; write P_a
(a ∈ ℤ/20) and Q_b (b ∈ ℤ/12) for the spectral projectors of W₁ and W₂.

**Definition (the seam trace and the seam form).** The *seam trace* of the pair is
s̃(a,b) = tr(Par·P_a·Q_b) ∈ ℚ(ζ₆₀). The Galois group Gal(ℚ(ζ₆₀)/ℚ(√5,√−3)) ≅ (ℤ/2)² acts on it;
the **seam form** is the ℚ(√5,√−3)-isotypic projection s(a,b) = (1/4) Σ_{γ ∈ Gal(ℚ(ζ₆₀)/ℚ(√5,√−3))}
γ·s̃(a,b) — the average that lands in the biquadratic field. Everything below is about s.

**Theorem S1 (values).** The raw seam trace s̃ is non-real at all 49 support points (a degree-8 element
of ℚ(ζ₆₀)); its projection s is supported on the same 49 points of the (a,b) grid (a ranges over
{0,1,4,5,6,9,11,14,15,16,19}, b over {0,1,2,3,4,5,7,8,9,10,11}, with 49 of the pairs occurring),
and on those 49 points s takes exactly **30 distinct values, all nonzero, all in ℚ(√5, √−3)**.
Its four Galois channels — the coordinates in the basis {1, √5, √−3, √−15} of ℚ(√5,√−3), the
isotypic pieces under Gal(ℚ(√5,√−3)/ℚ) ≅ (ℤ/2)² — are the natural coordinates for everything
below. (Their per-channel nonzero supports are 32, 45, 28, and 44 of the 49 points; the last
number, 44 — the √−15-channel support — is *not* the count of distinct values, a conflation
corrected from v1.)

The field ℚ(√5,√−3) is the compositum of the two ends of the object: √5 from the golden
(spherical, E₈) end, √−3 from the hyperbolic (E₆) end. The seam is where they meet, and its
values speak both languages at once.

---

## 3. The channel-vanishing lemma

Everything downstream rests on one observation, and it is the honest heart of the paper.

**Observation S5 (channel vanishing = empty support; verified, not yet proved per channel).** A
Galois channel of the (Fourier-transformed) seam form vanishes at a dual-torus point (x,y) if and
only if the cyclotomic support of the corresponding character sum is empty. Vanishing is never an
accident of magnitude; it is forced by which cyclotomic frequencies the character can carry. Two
channels of a value are therefore not free to vanish independently — their supports are governed by
the same residue data, and the joint pattern is constrained.

*Status.* This is verified exhaustively on all 240 dual-torus points (reproducer below) and is the
mechanism behind every selection rule in the paper, but a per-channel derivation from the
cyclotomic support — turning the verified statement into a theorem — is **the paper's central open
problem** (Section 8). It is stated here as an Observation, not with a proof mark.

*Why it should hold.* Two distinct roles of the Galois action must be kept apart (they are, in §8).
First, the *decomposition* into four channels is Galois-isotypic: each channel is a component of the
seam trace under Gal(ℚ(ζ₆₀)/ℚ(√5,√−3)), and this splitting is Galois-equivariant in the standard sense.
Second, the *vanishing* of a channel is a separate question — and, as §8 records, it is **not** produced
by the standard signed-permutation Galois action on modular data (which never sends a nonzero entry to
zero). What we observe is that a channel, being a sum over a cyclotomic residue class, vanishes exactly
when that class carries no surviving frequency; turning this "should" into a per-channel theorem — a
support/vanishing criterion, not an equivariance statement — is what remains.

The Observation is why the dark locus is a *structural* fact and not a table. Light is the generic
case; a point goes dark only when arithmetic forbids every channel at once, and forbidding is a
congruence condition, not a coincidence.

---

## 4. The selection rule: a broken subfield lattice

**Theorem S6 (five patterns; four fields and the dark stratum).** Exactly five vanishing patterns
occur across the 240 dual-torus points. Written as the set of channels that vanish, with the
surviving field and the count:

| pattern | channels that vanish | surviving field | count |
|---|---|---|---|
| free | none | ℚ(√5,√−3) | 120 |
| rs | √−3, √−15 | ℚ(√5) | 20 |
| qs | √5, √−15 | ℚ(√−3) | 20 |
| qrs | √5, √−3, √−15 | ℚ (rational) | 10 |
| dark | all four | 0 | 70 |

These realize four of the five nodes of the subfield lattice of ℚ(√5,√−3) — the whole field, the
two quadratic subfields ℚ(√5) and ℚ(√−3), and the rational floor — **together with the zero
stratum**. The fifth lattice node, **ℚ(√−15), is never realized**: the pattern in which only the
√−15 channel survives (√5, √−3 dead, √−15 alive) does not occur at any of the 240 points. The
√−15 channel instead *dies in every nontrivial pattern* — it is the first channel to go and the
one that never survives alone. So the selection rule is the subfield lattice **with the ℚ(√−15)
node deleted and a zero stratum adjoined**: a broken lattice, and the break is exactly the field
of the level, ℚ(√−15).

*(Correction from v1, recorded for the reader: v1 called the five patterns "precisely the five
nodes of the subfield lattice, including ℚ(√−15)." That is wrong twice over — ℚ(√−15) is never a
surviving field, and the zero stratum, present at 70 points, is not a subfield-lattice node. The
broken-lattice-plus-zero statement above is the corrected and, we think, more pointed one.)*

---

## 5. The dark locus

**Theorem S7 (darkness concentrates at closure).** Of the seventy dark points, **fifty-four sit
at quantum closure** — the addresses (j,l) where [W₁ʲ, W₂ˡ] = I. Darkness is not scattered; it
pools where the two operators commute.

This is the paper's cleanest image. Where the interaction vanishes entirely — where the object,
watched through Par, shows nothing — is overwhelmingly where the two motions have come into phase
and their commutator has died. The light is the interference; the dark is the silence after the
two clocks agree. Sixteen of the seventy dark points lie *off* closure, and those sixteen are the
paper's one genuinely open residue (Section 8).

---

## 6. The spectral fingerprint and the cornerstone

**Theorem S2 (spectral invariants).** The seam operator carries the framing fingerprint
σ₁ = σ₂ = 1/24 — the central-charge signature c/24 of the quantization, independent of the pair.

**Theorem S3 (the cornerstone).** The distinguished quadratic subfield of the seam is ℚ(√−15) —
the field of the level itself. It is the first channel to vanish and the node the reduction is set
against: the one quadratic subfield that never survives, so that the surviving fields form the
lattice *around* it.

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
formula. Verified on the 5×5 principal window (all 25 cells) at level 15; the general 36-cell
statement is asserted on that verified window and the even-function factorization, with the
full-torus check flagged as remaining.

The master table — thirty-six cells, each carrying its κ_q value and its tier — is the paper's
final object, printed in full in the appendix. It is the answer to the spine: the light and the
dark of the interaction, and the commutator that measures how far the operators are from
commuting, are the *same* two functions, and both are read off the greatest common divisors of the
exponents with the two clock orders. The proportions of light and darkness are the divisor
arithmetic of the clocks.

That the factorization mechanism is classical (even functions; ℚ-classes) is stated plainly: what
is ours is the specific N = 15 seam, its broken-lattice selection rule (four fields plus zero, with
ℚ(√−15) absent), the dark-locus/closure concentration, and the joint reading of κ_q and the tier
on one lattice.

---

## 8. What we could not locate, and what remains open

The classical shelf: Weil-representation character values (Howe; Thomas; and, at odd composite level,
the explicit formulas of Ladisch and of Strömberg), the Hecke/CRT factorization from the real-quadratic
eigenvalue field (Kurlberg–Rudnick), the general Galois symmetry of modular data (Coste–Gannon; Bantay;
Dong–Lin–Ng), the even-function class (Cohen; McCarthy), and the ℚ-class principle (Serre). Against that
shelf, our search — an adversarial prior-art assessment run after this paper's panel — did not locate:
the explicit 30-value seam form at any composite level; the broken-lattice selection rule with ℚ(√−15)
systematically absent; the dark-locus/closure concentration (54 of 70); or the joint (κ_q, tier)
divisor-lattice factorization. The verdict is **APPEARS-NOVEL / NEEDS-SPECIALIST**, and one structural
observation sharpens it: the general Galois symmetry of modular data (Dong–Lin–Ng) acts by a *signed
permutation* G_σ = σ(s)s⁻¹, which can never send a nonzero matrix entry to zero — so the systematic
vanishing of the √−15 channel is **not** an instance of the standard Galois-equivariance mechanism, and
the selection rule is a distinct phenomenon. This is a negative-existence verdict over the canonical
references; a specialist in Weil-representation Galois theory should confirm no CRT/Galois-descent
argument in less-indexed literature explains the √−15 absence.

Open: (i) the **cyclotomic-support step** (Observation S5) — deriving each cell's tier from its
support is verified on all 240 dual-torus points but not yet proved per channel; it is the paper's
central open problem. (ii) The **sixteen off-closure dark points** — the dark locus is not
exhausted by the closure set, and the residue is unexplained. (iii) The **seam at other levels** —
whether the broken-lattice selection rule survives at levels other than 3·5, and how it degrades
when a prime goes trivial. (iv) The **full-torus S10 check** — Howe's magnitude law is verified on
the 5×5 principal window; the remaining cells are asserted via the factorization, not yet
exhaustively checked.

---

## Appendix A: the master table

(The 36-cell table (gcd(x,20), gcd(y,12)) ↦ (κ_q, tier), printed in full as in Paper 4 §4.3;
reproducer `B474_tier_commutator_law/cross_table.py`, exact at p = 61, ℚ(ζ₆₀).)

## Appendix B: reproducibility

Per-claim script map: S1–S4/S11 (the seam bank B358–B367, B449; the 30-value/49-support count, the
per-channel supports {32,45,28,44}, and the ℚ(√5,√−3)-projection definition recomputed at revision via
`B358_seam_certification` + `B367_value_map` — the raw trace's degree-8/non-real status confirmed at all
49 points); S5–S6 (`B459_klein_four_verification/verify_patterns.py` — the five patterns, counts
120/20/20/10/70, the two laws, and the never-realized ℚ(√−15) node, all reproduced at revision);
**S7's dark-locus/closure concentration (54 of 70) is NOT produced by verify_patterns.py** (which
computes only the patterns and their counts); it is the intersection of the 70-point dark set with the
commutator-closure locus [W₁ʲ,W₂ˡ]=I, and requires its own reproducer — flagged here as a step to be
committed with the paper, not yet part of the reproduced set. S8/S12 (`br1_br2.py`,
B469); S9/S10 (`cross_table.py`, `kq_verify.py`, B474/B472). Each carries a lock re-run at draft. The
v1→v4 corrections (30 distinct values not 44; the broken lattice with ℚ(√−15) absent and the zero
stratum present; the value-torus / dual-torus separation; Observation S5 demoted from proved to the
central open problem; and — v4 — the seam form redefined as the ℚ(√5,√−3)-projection, since the raw
trace is degree-8/non-real) are recorded in the
corrections ledger. The earlier float miscount of the dark set as 53 rather than the exact 70 is
also recorded there.

---
*MSC 81Q50, 11L05, 11R18, 57K32, 11F27. Companion to Paper 4 (the Markov stage). Repository URL at packaging.*
