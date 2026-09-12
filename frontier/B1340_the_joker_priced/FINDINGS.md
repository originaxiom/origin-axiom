# B1340 — THE JOKER PRICED: chirality is not free, and what it buys is not what was asked for

**Date:** 2026-09-12 · **Seat:** cc (this bench) · **Lane:** PHYSICS (algebra layer).
**Depends on:** B864 (the anomaly ledger), B1283 / B1303 (the SM closing's Z′), P9 of the falsifier register.
**P0 — the quantifier, stated before computing:** this computes over the **algebra** (E₆ and its
representations) and over the **declared family torus**. It says nothing about m004, the index, or
any manifold. Conclusions bank at the algebra layer.

---

## The order

> *"what if we use a one joker card — chirality 3 as an input, see if we complete the program, and
> understand the source as we go?"*

So: **grant C3** — three chiral generations — as a declared, priced input, spend it, and read the bill.

---

## 0. The price of the card, stated before spending it

C3 is not a small input and it is not the record's to give. The object's own fixed-locus theorem
gives |det(A − I)| ∈ {0, 4} across the census — **3 never occurs**. The card is therefore an
*import*, not a discount: it buys structure the chain does not supply, and every consequence below
inherits that debt. The register should carry C3 as an input, not as a result.

## 1. Two falsifiers this bench proposed, both vacuous — owned

Before the real test, this bench proposed two checks and both are dead on arrival:

* **anomalies over the full 27 cannot fail.** E₆ is an anomaly-safe group (`T-ANOMALY-REALIZED`,
  B864(1)): every cubic Casimir vanishes, so every U(1) ⊂ E₆ is anomaly-free on a 27 whatever else
  is true.
* **SM anomalies over N chiral generations cannot fail either.** They are **linear in N**, and one
  generation already cancels (B864(3), the textbook miracle). 3 × 0 = 0.

Recorded so they are not proposed a third time. The coefficient that *can* fail is the **cubic of a
family-non-universal direction**: it carries Σᵢ fᵢ³, which is cubic and not linear in the family
charges, so the multiplicity does **not** divide out.

## 2. The measured result — the record's anomaly check carries zero bits

The paper, §8 (`main.tex:775`): the ninth closing's tree-level vacuum leaves *"a family-non-universal
Z′, **anomaly-free by the conjugate generations***", on 19 624 vacua that come *"all in mirror pairs,
**vector-like**"* (`main.tex:772–774`). B1303 verifies it as check (h): cubic **−20250** from the 27s,
**+20250** from the 27̄s, total 0.

`verification/b1340_joker_zprime.py` rebuilds the whole table from the E₆ branching
(E₆ ⊃ SO(10) × U(1)_ψ ⊃ SU(5) × U(1)_χ × U(1)_ψ), independently reproduces P9's charge list and
B1303's −20250, and then asks the question the corpus has not asked. Five pre-registered questions,
all PASS:

| | question | answer |
|---|---|---|
| Q1 | does the from-scratch branching reproduce B1303's −20250? | **yes** (positive control) |
| Q2 | does the record's Z′ survive deletion of the mirrors? | **no** — cubic −20250 on 3 × 27; **five of six** coefficients non-zero on 3 × 16 |
| Q3 | how many bits does the anomaly check on the record's vacuum carry? | **zero** |
| Q4 | what *is* anomaly-free once the mirrors are gone? | the family part is **forced** to (0, t, −t) |
| Q5 | is the record's (−10, 5, 5) of that shape? | **no** |

**Q3 is the load-bearing one and it is a vacuity finding about the record, not about the joker.**
On a vector-like spectrum all six anomaly coefficients vanish **identically as polynomials** in all
six parameters (a, b, c, f₁, f₂, f₃) — X and X̄ cancel in every odd-power trace. So *every*
SM-commuting direction is anomaly-free there. "Anomaly-free" on the 19 624 vacua is **not evidence
of anything**; the check cannot fail. B1303's own positive control (`a27['cubic'] != 0`) is the only
failable line in it, and B1303's code already half-names this in a comment about E₆ safety — what
was not drawn is that the *total* is therefore uninformative.

## 3. What the joker actually buys: a forced shape

Chirality is what turns 0 = 0 into a constraint. Over three chiral generations, writing the
SM-commuting direction as q = aY + bχ + cψ + fᵢ:

* **grav** ⇒ Σ fᵢ = 0 (the E₆ part is traceless, so only the family torus contributes);
* **cubic** ⇒ Σ fᵢ³ = 0 (the E₆ part is safe, so again only the family torus contributes);
* and Σ f = 0 ⇒ Σ f³ = 3 f₁f₂f₃, so **some fᵢ = 0**.

> **THEOREM (Q4, verified two ways — by solver on all six conditions, and as a polynomial identity).**
> Over a chiral spectrum the family part of any anomaly-free U(1)′ has the shape **(0, t, −t)** up to
> permutation: **one generation exactly neutral, the other two exactly opposite.**

It holds on **both** readings of "three chiral generations" — three full 27s, and three 16s with the
exotics paired off. On the 16, ψ is constant, so the effective family charge is gᵢ = fᵢ + c; the
solver returns three branches in each case and every one has the shape.

**This is a genuine purchase.** It is the first place in the record where the anomaly conditions do
work rather than pass trivially, and it is a one-parameter family where the record had six free
parameters.

## 4. What the joker costs: P9

The record's family part is **(−10, 5, 5)**: Σf = 0 ✓ but f₁f₂f₃ = −250 ≠ 0 ✗. **It is not of the
forced shape.** So the paper's Z′ is precisely the thing chirality forbids.

And the difference is not a rescaling. P9 says the distinguished generation is neutral and *"the
other two generations **equal**."* Chirality forces the other two to be **opposite**. That is a
falsifiable difference in the flavour structure of the predicted Z′ — a Z′ with two equal
family charges is excluded on a chiral spectrum, whatever its mass.

**Consequence for the falsifier register.** P9 is the register's one entry *"whose regime the
object's own vacuum names."* Its anomaly freedom is **conditional on the spectrum being
vector-like** — which is the record's own description of the 19 624 vacua, and is exactly what the
Standard Model is not. The programme therefore holds P9 and C3 in tension: it cannot have the
observed chirality and this Z′. That is not a refutation of P9 — the vacuum is what it is — but P9's
status line should carry the condition, because a reader will otherwise take "anomaly-free" to mean
"anomaly-free on the physical spectrum", and it is not.

## 5. The forwarded report, claim by claim

`verification/b1340_report_audit.py`. Six claims checked on the branching table, three dispositions
against the record:

| claim | verdict |
|---|---|
| anomaly cancellation automatic | **half right, wrong reason** — automatic on the record's vacuum because **vacuous** (§2); under C3 it is live, forces (0,t,−t), and **kills** the record's Z′ |
| charge quantisation earned | **genuine but not bought by the joker** — Y is a simple-group generator, traceless on the 27; the statement holds on the vector-like spectrum already |
| symmetric Yukawa from the cubic | **correct** — Sym²(27) ⊃ 27̄, so one symmetric λ_ijk feeds every mass |
| three Higgs doublet pairs | **correct** — one (H_u, H_d) per 27, three 27s |
| m_b/m_τ = 1 a win, m_s/m_μ = 1 a break | **these are the same equation.** d^c and L sit in the *same* SU(5) 5̄, so 10·5̄·5̄_H gives M_d = M_e^T — one matrix equation yielding m_b/m_τ, m_s/m_μ **and** m_d/m_e at once. The report banks one and disowns another from a single relation. Separating them needs a non-minimal Higgs sector (Georgi–Jarlskog); **the record supplies none** |
| V_CKM = I a break | **contingent, and in tension with the report's own C6.** V_CKM = I needs M_u ∝ M_d: one 27³ invariant *and* one VEV direction in family space. With three doublet pairs the VEVs carry family indices and proportionality fails. The "break" is an artefact of an assumption the report's own win contradicts |
| proton decay dominantly K⁺ν̄ | **imported.** That is the SUSY dimension-5 signature; without superpartners it is e⁺π⁰. `GUT_REQUIREMENTS_LEDGER` row 5 records proton decay as *not addressed / absent*, and supersymmetry appears only as **one fork** of P9's regime, never as a commitment |
| "the CKM Grassmannian coordinate **IS** I-13" | **right in kind, wrong in force, and empty as stated.** I-13 is the *master* identification; a Grassmannian coordinate read as V_CKM is an **instance** of it (as I-18, I-23, I-29 are) — an instance **inherits** the debt and needs its own row, it does not **pay** the row. And if V_CKM = I, as the same report asserts, there is no non-trivial CKM matrix for a coordinate to identify. The two claims cannot both be load-bearing |

So the report's "complete skeleton" does not survive contact: one of its wins is vacuous, one is
textbook, one of its breaks is an artefact, its two mass relations are one relation, its proton-decay
signature is imported, and its identification claim is an unregistered instance of an unearned row.
What is *left standing* is real and is §3: the cubic is symmetric, the doublets are there, and the
anomaly conditions — once chirality is granted — force a shape.

## 6. What this does to the chain

The joker was spent to see whether it *completes the programme*. It does not. It buys one forced
structure (§3) and it costs one prediction (§4), and both of those are downstream of an input the
object does not supply (§0). **The net movement on the chain is zero rungs and one sharpened
edge**: the record now knows that its Z′ is a vector-like artefact, and knows the exact shape any
replacement must have.

The general lesson generalises past the Z′ and is worth carrying: **on a vector-like spectrum every
consistency check that is odd in the charges is vacuous.** Any future "it is anomaly-free" /
"it is consistent" claim made on the 19 624 vacua must state whether the check could have failed.
