# Adversarial review verdict — Papers 1 & 2 (2026-07-05)

*Four independent INTERNAL reviewers (AI assistant seats; no external referee — see PROVENANCE.md §0), each instructed to break the papers, not approve them: (1) a
from-scratch correctness recompute, (2) a journal-readiness referee, (3) a reproducibility /
claims-integrity audit, (4) a hostile novelty / prior-art referee. This document records their
verdict honestly and in full. It is not encouraging; it is accurate.*

## The one-line answer

**No — the papers do not withstand adversarial scrutiny as novel research papers today.** Not
because the mathematics is wrong (it isn't) or unreproducible (it is reproducible), but because
**the novelty is largely unestablished and much of it is standard**, and the private vocabulary
and the √−15 framing disguise that. The math is a correct, machine-checked worked example inside
known frameworks; the papers present it as more.

## What is solid (confirmed by independent recompute)

- **Every one of the 8 sampled claims recomputed and confirmed exactly.** No false theorem was
  found. Specifically: the order law `ord(W₁@15)=20=π(15)/2`; the split `1/12 = 1/16 + 1/48` and
  the slot constant `(0,0,−1/12,−1/12)`; the CRT factorization `C = C₃·C₅` (0/240 mismatches at
  the CRT-*forced* multiplier `(2,2)` — not a fitted parameter); the root-of-unity gate `142/142,
  0 violations`; `ℚ(√5,√−3)` = Hilbert class field of `ℚ(√−15)`; `5F₂ⱼ² = |det(A²ʲ−I)| = #Fix`;
  the geometric torsion `−3` (independently recomputed with a different Sym² basis); and
  `⟨4₁⟩₅ = 46+2√5`.
- **Every cited lock exists and passes green** (~103 test functions, 0 failures, 0 skips, and —
  notably — no SnapPy/Sage needed for these two papers). The arithmetic is exact (ℚ(ζ₆₀), no
  floating point), and where tested the from-scratch generator scripts regenerate the banked
  numbers bit-for-bit.

## What is wrong or overclaimed (must fix regardless of the path)

1. **A real arithmetic error** [fixed]. `frontier/B425_geometric_torsion/geometric_torsion.py`
   stated "disc ℚ(√5) = −5" (lines 21, 348). **disc ℚ(√5) = +5**; the value −5 is the dynamical
   zeta `ζ₁ = 2−L₄`, a torsion value, not a discriminant. This makes Paper 2's anchoring pairing
   *"two computed discriminants, 5 and −3"* **asymmetric**: the Eisenstein side (`−3 = disc ℚ(√−3)`)
   is genuine, but the golden side conflates a torsion value (−5) with a discriminant (+5). The
   code is fixed; **the paper's pairing framing must be corrected to state the asymmetry honestly.**
2. **"Three methods agree"** (P2 Thm 4b) overstates: the artifact computes **one** method
   (Fox/Wada); V30/V31 are banked cross-references, not re-verified here.
3. **Entropy inconsistency** (P2): the abstract says `4 log φ`, §2 says `2 log φ`. The cat map `A`
   has topological entropy `2 log φ`; `4 log φ` is the *trace-map flow's* Lyapunov exponent — a
   different system. The abstract attributes to "the cat map's dynamics" the number that is *not*
   the cat map's entropy. Must disambiguate.
4. **Conjecture-as-theorem** (P1 Thm 6, "existence law, general N"): stated with a "Theorem … ∎"
   but proved only by derive-and-test at finitely many levels. Must be restated as a conjecture
   verified at the listed levels, or proved.
5. **Mislabeled claim altitude** (P1 §9): "T1–T11 = claims P59–P68" is false — only T1–T9 are
   promoted ledger claims; **T10 (class-field) and T11 (no-scale/no-frame) are frontier-locked,
   not proven P-claims**, yet presented at the same altitude.
6. **Unsupported census** (P1 Thm 6): "census-confirmed at 243 and 625" — the cited lock only
   covers up to 81/125/225. Drop or add.
7. **"Machine-verified" overstates the suite** (both): most cited locks are recorded-constant
   regression guards, not live recomputes (only ~6–7 recompute inside the test). Reproduction
   from scratch requires the `frontier/B*/*.py` generators, which the papers don't point to.
8. **Physics vestiges** (both): the Standard-Model-mass-ratio clause (P2 Thm 5) and the
   scale/"mixing frame" language have no antecedent in a pure-math paper and read as an abandoned
   physics program. Cut or recast as purely mathematical remarks.

## The deeper problem — novelty (the hostile referee's prior art)

The adversarial novelty referee named concrete prior art for nearly every load-bearing object:

- **The "seam" `tr(Par·P_a·Q_b)` is a discrete Wigner function** (Grossmann–Royer parity form;
  on the torus, Rivas–Ozorio de Almeida; Wootters). Renamed, not new.
- **Theorem 2's "twist invariant" is the theta characteristic / two-lifts fact** (Gurevich–Hadani
  canonical Weil-representation program; Mumford's *Tata Lectures on Theta*).
- **"Value theory" is Kurlberg–Rudnick's matrix-element program** (they have papers literally
  titled *value distribution for eigenfunctions of desymmetrized quantum maps*).
- **Theorem 3 is the standard Gauss-sum evaluation** of a metaplectic×Heisenberg trace.
- **P2 Theorem 4a is the Lefschetz zeta of the cat map, re-indexed** (the "E₆ grading" supplies
  six integers and nothing more).
- **P2 Theorem 4b reproduces Porti's known adjoint torsion** (value −3), which the program's own
  novelty audit (R6) already rates KNOWN.

So the honest residue of candidate-novelty is thin: **P1 has at most one card — the existence law
(Theorem 6) — conditional on a specialist confirming it is not an immediate corollary of the
standard evaluation; P2 has no new theorem** (the two torsions are individually standard; the
pairing, once the disc error is corrected, is asymmetric and restates §2's two known facts).

## The verdict per paper

- **Paper 1** — mathematically sound; the stronger of the two. Its honest destination is a **short
  computational note** whose single claimed contribution is the existence law, submitted to
  Experimental Mathematics *after*: fixing the mis-quantified theorems, stripping the private
  vocabulary ("seam", "brightness", "value theory") and the repo jargon, writing out Theorem 3's
  Gauss-sum evaluation, completing ~20–35 references with a real prior-art positioning against the
  quantum-cat-map / Wigner literature, and — decisively — a **specialist confirming the existence
  law is new**. Estimate: several focused weeks *plus* the specialist read.
- **Paper 2** — no theorem core. Its honest destination is an **expository survey** ("the
  figure-eight across dynamics, arithmetic, and quantum topology: a dictionary"), no novelty
  claimed, physics vestiges cut, everything re-attributed — **or** a short note "Two E₆ adjoint
  torsions of the figure-eight" *if* the pairing survives specialist scrutiny (it is currently
  weakened by the disc asymmetry). Estimate: 4–8 weeks *plus* the scope decision and the specialist
  read.

## The single framing liability spanning both

The `√5·√−3 = √−15`, class-number-2 = amphichiral-`ℤ/2` motif is *true* (genus theory of disc −15)
but presenting it as an "organizing principle" rather than a decorative identity is exactly the
small-number coincidence a hostile referee reads as numerology — and the repeated "no physical
interpretation is asserted" disavowals read as a firewall around an abandoned ambition. Both lower
trust. The papers are more defensible with the motif demoted to a remark and the disavowals
removed.

## Honest bottom line

The program produced **correct, reproducible mathematics** — that survived a from-scratch
recompute and a lock audit. It did **not** produce, in these two drafts, **established novelty** —
the adversary named the prior art, and the one surviving candidate (P1's existence law) needs a
specialist. The path is: **fix the concrete errors (done for the code; pending for the prose),
deflate the vocabulary, recast P1 as a short note and P2 as a survey, and get a real specialist
novelty read before anything is posted.** That read — not more computation, and not more editing —
is the gate. The discipline that ran this program is exactly the discipline that should govern its
exit: claim only what survives scrutiny, and this review is that scrutiny, applied to the papers
themselves.

*Provenance: four independent adversarial subagent reviews, 2026-07-05, each recomputing/attacking
from scratch. The B425 disc(√5) code error is fixed in this pass; the prose corrections and the
recast decision are recorded here for the owner.*
