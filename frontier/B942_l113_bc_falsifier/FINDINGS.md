# B942 — L113, THE BC/CMR FALSIFIER: **OUTCOME YES.** The kill condition executes.

**Date:** 2026-08-07 · **Seat:** cc (banking) · **Lane:** MATHEMATICS. Gate 5
untouched; nothing to CLAIMS.
**Preregistration sha-256:** `48cd1ea291277f8c85637a9c817a554edc7bc4370bf7ec893bec223428ebc5a2`
— sealed, ledgered and pushed (`9d806a4e`) **before any cell ran**; re-verified at
banking against the file and the ledger row.

---

## The verdict, against the sealed criterion

> **OUTCOME YES** — the programme's β=1 system IS BC/CMR-type for K = ℚ(√−3). Then
> B849's verdict stands **unconditionally**, the chirality-as-Galois-label
> identification is refuted **at the level of group membership**, and **the kill
> condition executes.**

**All four cells return the YES branch.** The disclosed prior (OUTCOME YES, high) was
correct — which is the uncomfortable outcome, and the reason the prior was written down
before the computation rather than after.

> **MASTERPLAN v2, kill condition (locked, may not be moved — only executed):**
> *"L113 YES → the observer construction's foundation fails; Phase III restructures
> around the wreckage, honestly."*
>
> **It is hereby executed.** §5 states what falls, §6 what survives and on what
> argument, §7 what replaces it.

## 1. Cell 1 — the identification is not an open question; it is our own sentence

B851 framed step two as an open in-repo question: *is the programme's system actually
BC/CMR-type for K?* The answer did not require new mathematics — **B723 already said so
in its own text**, and the cell decides it by quotation:

| checked in `B723/FINDINGS.md` | result |
|---|---|
| names the **Bost–Connes/CMR system over ℚ(√−3)** | **YES** |
| names **Gal(K^ab/K)** as the label group | **YES** |
| names the **β=1** transition | YES |
| assigns **CHIRALITY** to the Galois/extremal-KMS label | YES |

B723's own words: *"in the Bost–Connes/CMR system over ℚ(√−3), TIME and CHIRALITY/VALUES
sit on OPPOSITE sides of the β=1 phase transition… the extremal states at β>1 carry the
**free-transitive Gal(K^ab/K) label** (the sheet/values)."*

**So the load-bearing assumption was never an assumption — it was an assertion, made
explicitly, and never tested.** That is worse than a gap and better than a mystery: it
means the falsifier applies directly, with nothing left to interpret.

## 2. Cell 2 — the group-membership fact, COMPUTED (not cited)

**Is complex conjugation an element of Gal(K^ab/K)?  NO.**

Two independent computations:

**(i) Field-level, symbolic.** √−3 = ω − ω̄ ∈ K. Every σ ∈ Gal(K^ab/K) fixes K
pointwise, hence fixes √−3. Conjugation sends √−3 ↦ −√−3 ≠ √−3. Therefore c ∉
Gal(K^ab/K). Verified symbolically.

**(ii) Finite membership tests, in fourteen layers of the cyclotomic sub-tower.**
For 3 | m, ℚ(ζ_m) ⊂ K^ab, Gal(ℚ(ζ_m)/ℚ) = (ℤ/m)\*, Gal(ℚ(ζ_m)/K) = {a ≡ 1 mod 3}, and
c = −1. Since −1 ≡ 2 mod 3, **c is in no layer's subgroup** — and the index is exactly
**2 in every layer**:

| m | 3 | 9 | 15 | 21 | 63 | 105 | 231 | 1155 | 15015 | 255255 |
|---|---|---|---|---|---|---|---|---|---|---|
| \|Gal(ℚ(ζ_m)/ℚ)\| | 2 | 6 | 8 | 12 | 36 | 48 | 120 | 480 | 5760 | 92160 |
| \|Gal(ℚ(ζ_m)/K)\| | 1 | 3 | 4 | 6 | 18 | 24 | 60 | 240 | 2880 | 46080 |
| index | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| c ∈ Gal(·/K)? | no | no | no | no | no | no | no | no | no | no |

**(iii) Where c actually lives.** The exact sequence

  1 → Gal(K^ab/K) → Gal(K^ab/ℚ) → Gal(K/ℚ) → 1

puts c **outside the kernel and on top of it**: c restricted to K is the nontrivial
element of Gal(K/ℚ) ≅ ℤ/2. **The ℤ/2 the object needs is the QUOTIENT; the label group
the SSB produces is the KERNEL.** This is the whole finding in one line.

## 3. Cell 3 — all four escape hatches, each computed and each closed

**(a) The object-level route — could m004's own arithmetic carry the system instead?**
**NO**, and reconfirmed here independently of B736's banked NEGATIVE. The BC/CMR
symmetry breaking at β = 1 **is** the pole of ζ_K at s = 1. Computed:

| ε | ε·ζ_K(1+ε) |
|---|---|
| 10⁻⁶ | 0.604600359726 |
| 10⁻⁸ | 0.604599793795 |
| 10⁻¹⁰ | 0.604599788135 |

against the class-number formula 2πh/(w√|d|) = 2π/(6√3) = **0.604599788078** — agreement
to 6 × 10⁻¹¹. A finite level (m004 is congruence at (2)³ = (8), image order 2560 —
B734/B736) has a **finite** Dirichlet sum for a partition function: entire, no pole,
**no phase transition, therefore no SSB.** The object cannot host the system at any
finite level; the transition is an artifact of the infinite tower.

**(b) The quotient route — is there a canonical ℤ/2 quotient of Gal(K^ab/K) to serve as
the sheet?** **NO.** ℤ/2 quotients ↔ index-2 subgroups ↔ quadratic extensions of K.
Counted layer by layer (2^r − 1 for 2-rank r): **0, 0, 0, 1, 1, 1, 1, 1, 1, 3, 3, 7, 15,
31** — non-decreasing, with five strict rises, and unbounded because the 2-rank grows
with the number of primes dividing m. **Infinitely many ℤ/2 quotients, none
distinguished by the arithmetic.** A sheet label would have to be *chosen* — which is
precisely what a canonical identification cannot do.

**(c) The anti-automorphism route — could c act on the labels from outside the group?**
Computed: on the cyclotomic tower the ambient group is **abelian**, so conjugation
σ ↦ cσc⁻¹ acts by the **identity**. c does not even permute the labels there. What c
*does* do is swap the two **cosets** of Gal(K^ab/K) in Gal(K^ab/ℚ) — a ℤ/2 at the
ℚ-level, not a label in the K-level torsor. **This is a repair, not a rescue**, and §7
takes it as such.

**(d) The archimedean route — is there a real place whose ℤ/2 could host the sheet?**
**NO.** K is imaginary quadratic: signature (r₁, r₂) = **(0, 1)** — zero real places. The
conjugate pair of embeddings is a ℤ/2 of Gal(K/ℚ), i.e. **again the quotient**.

**Every hatch leads back to the same place: the ℤ/2 exists, one level up.**

## 4. Cell 4 — one label cannot carry both

CMR's action on extremal KMS states is **free and transitive** (B851 quotes four separate
statements of it from the source). Free + transitive ⟹ the label set is a **torsor under
the full group** Gal(K^ab/K), an infinite profinite group. Chirality is a **ℤ/2** (B713).

A ℤ/2-valued function on such a torsor is exactly a choice of index-2 subgroup. By cell
3(b) there are infinitely many and none canonical. So assigning **both** chirality and
values to "the Galois label" either

- **collapses the torsor to ℤ/2**, contradicting free-transitivity, or
- **requires an arbitrary choice**, contradicting canonicity.

**Both horns are fatal to the identification as stated.**

## 5. EXECUTING THE KILL CONDITION — what falls

**RETRACTED** (B723, and anything downstream that leans on it):

1. **"CHIRALITY = the extremal-KMS / Galois-embedding label."** Refuted at the level of
   group membership. The label group does not contain the element chirality is supposed
   to be.
2. **"Choosing a sheet = breaking the c-swap," read as the β=1 SSB.** The SSB breaks
   Gal(K^ab/K). c is not in Gal(K^ab/K). **The β=1 transition cannot produce the c-swap,
   at any temperature, by this mechanism.**
3. **"Measurement = the cooling through β=1" as an account of chirality.** It may still
   be an account of *values* (§6); it is not an account of the sheet.

**The corpus shape this instantiates** — and it is the one the repo already catalogues —
is **right object, wrong level**. The Galois picture is the right object. Gal(K^ab/K) is
the wrong level for chirality. The error is imported from the ℚ case, where complex
conjugation genuinely *is* in the symmetry group (−1 ∈ Ẑ\* under the cyclotomic
character) — B851 diagnosed exactly this, and the computation confirms the diagnosis was
right.

## 6. What survives — argued, not assumed

**The values/torsor clause is NOT refuted by this arc, and it is NOT hereby certified
either.** What cell 4 shows is that the *torsor* structure is consistent with a
free-transitive Gal(K^ab/K) action; what it does not show is that B700/B701's
simply-transitive torsor **is** that torsor. That identification has exactly the same
logical shape as the one just killed — asserted, not demonstrated — and it must not now
be waved through because its sibling died.

> **NEW OPEN LEAD (registered): is B700/B701's simply-transitive torsor the CMR torsor —
> i.e. is its structure group Gal(K^ab/K)?** Until computed, the values clause is
> **UNEARNED, not refuted.** Treating "the surviving half" as established would repeat
> this arc's error one clause over.

**Also standing, untouched:** the type-classification facts across β=1, the B736
obstruction, the B734 congruence result, and the observation that *no single state
carries both* time and label — that last one is now more interesting, not less (§7).

## 7. THE REPLACEMENT — what the computation actually says

The two data the observer construction wanted are **both real and both present**, but they
sit at **two different levels of one tower**:

| datum | lives in | produced by |
|---|---|---|
| **values** (the torsor basepoint) | Gal(K^ab/K) — the **kernel** | the β=1 SSB (if the torsor identification is earned — §6) |
| **chirality** (the sheet, ℤ/2) | Gal(K/ℚ) — the **quotient** | **not by any thermal transition** |

**The consequence is sharp and worth stating plainly: the object's c-swap is not
thermodynamic.** Gal(K/ℚ) is the field's own ℤ/2. It is present at every temperature, it
is not broken at β = 1, and no cooling produces it. If chirality is a symmetry breaking
at all, it is broken **arithmetically — in passing from ℚ to K — not thermally.**

This is not a consolation prize dressed as a result. It is a **falsifiable relocation**:
the sheet is now predicted to be a ℚ-vs-K phenomenon, temperature-independent, and that
prediction is testable against the banked structure (the two embeddings, the c-swap of
B713, the amphichirality/θ material, and the standing distinction between c and θ).
**Phase III restructures around this**, as the kill condition requires.

## 8. Honest limits

1. **The cyclotomic sub-tower is a sub-tower.** Cell 2(ii) proves c ∉ Gal(ℚ(ζ_m)/K) in
   fourteen layers; the *field-level* argument 2(i) is what proves it for the full K^ab,
   and it is a one-line consequence of the definition. No claim is made about the
   structure of Gal(K^ab/K) beyond membership and index.
2. **Cell 3(c)'s triviality is computed on the cyclotomic tower**, where the ambient
   group is abelian. Over the full K^ab (non-abelian over ℚ) the conjugation action on
   Gal(K^ab/K) need not be trivial. **That does not affect the verdict** — c is outside
   the group either way — but the sentence "c acts by the identity" is scoped to the
   layers computed, and is not asserted for K^ab.
3. **No CMR theorem is re-proved here.** Their statements are used as B851 verified them;
   what this arc computes is our own side of the identification.
4. **The values clause is left open, deliberately** (§6). This arc kills one clause and
   refuses to certify its neighbour.

## 9. Files

`PREREGISTRATION.md` (sealed, hash above) · `b942_cells.py` (four cells, exact +
mpmath) · `results.json` · locks `tests/test_b942_l113.py` (seal-integrity first, then
one lock per cell, then the kill-condition-execution lock).

---

**Verdict: OUTCOME YES. The sharpest falsifier the programme owns was aimed at its own
observer construction, fired, and hit.** The chirality-as-Galois-label identification is
retracted; the values clause is demoted from assumed to open; the sheet is relocated to
Gal(K/ℚ), where it is arithmetic rather than thermal.
