# THE ASSUMPTION LEDGER — the far bank decomposed, and the one condition we can compute fails on the object

*Outside bench, memo 235, 2026-09-18. Seal `seals/THE_ASSUMPTION_LEDGER_PREREG.md`
(sha256 `3fd9117e0da47d50c0cda3db9ff420d60c0625c53d2e8e314a30ca8a8d519fd0`, committed `e657e0d8`
**before** the certificate). Certificate `certificates/the_assumption_ledger.py`, output
`outputs/the_assumption_ledger_out.txt`, **exit 0, four controls PASS**. Every number from that
certificate (#20).*

---

## 0. THE ARTIFACT THAT NEARLY SHIPPED AS THE HEADLINE

**The first run returned OUTCOME A** — A4 failing for m004 but **holding for v2873 (b₁ = 2) and
t12835 (b₁ = 3)**, an earned redirect to two of B1330's best-case objects. It would have been the
best result of the session.

**It was an artifact.** The run tested only the **cusp count** before applying the `(1,0)` filling.
B1273's construction is the 3-fold **cyclic branched cover of S³ along the knot**, obtained by
filling the **lifted meridian** — and that requires a **knot complement in S³, i.e. `H₁ = ℤ`
exactly**. Of the seven candidates **only m004 qualifies**; the rest carry torsion or extra rank, so
a cover still exists but the ambient is not S³ and `(1,0)` is **not canonically the meridian**. The
filling was a *choice*, not the construction.

**What exposed it:** t12833's filled volume came back **negative, −1.370e−05** — the numerical
signature of a degenerate filling. The frame test now sits in the certificate **with this history in
the source**, not silently corrected.

---

## 1. THE DECOMPOSITION

The assumed package — G₂-MSSM §I.B + `THE_DESTINATION_LEDGER` item 1 + B1355:

> *a compact G₂ manifold **X** containing an observable three-manifold **Q** carrying an E₆
> singularity, with **isolated conical points on Q at which chiral matter is supported**, three of
> them permuted by ℤ/3.*

| # | atomic condition | on | tag | status |
|---|---|---|---|---|
| A1 | Q admits the E₆ (2T) normal structure | Q | COMPUTABLE | the record has it |
| A2 | chirality needs the ADE locus through **isolated non-orbifold conical points** | X | LITERATURE | Witten; Acharya–Witten; Acharya–Gukov |
| A3 | the flat/orbifold class cannot supply A2 | X | SETTLED | B1259, B1353 |
| **A4** | **Joyce–Karigiannis needs `b₁(Q) > 0`** | Q | **COMPUTABLE** | **computed below** |
| A5 | TCS is non-chiral | X | LITERATURE | BCHS 2019 |
| **A6** | sum rule: `b₂(X) ≥ 2` with the ℤ/3 moving harmonic forms | **X** | **GENUINELY OPEN** | **not computable — X is not constructed** |
| A7 | the permuting ℤ/3 is the object's own, 2T/Q₈ | Q | SETTLED HERE | memo 233 v2 |
| A8 | the ℤ/3's fixed-point structure on Q | Q | COMPUTABLE | reported, not assumed |
| A9 | on a **closed** Q, H¹-based net chirality vanishes ⟹ chirality can come **only** from A2's points | Q | SETTLED | B1260, B1267, B1351 |

**A6 is the honest residue.** It is the condition that would decide the matter, and it lives on an
object nobody has built. The ledger's value depends on that tag staying honest.

---

## 2. THE RESULT — **OUTCOME B**

| candidate | why in the set | frame | A4 |
|---|---|---|---|
| **m004** | the object | **REACHED** | **FAILS** — Y₃ has `H₁ = ℤ/4 ⊕ ℤ/4`, **`b₁ = 0`**, vol 2.93e−12 (flat) |
| m003 | the sister | does not reach | `H₁ = ℤ/5 ⊕ ℤ` |
| **m202, s959** | **cell 8's 4/4 witnesses** | does not reach | `ℤ⊕ℤ` · `ℤ/3⊕ℤ⊕ℤ` |
| **v2873, t12833, t12835** | **B1330's best-case set** | does not reach | `ℤ/6 ⊕ ℤ` each |

**Frame reaches 1 of 7. A4 holds for none.**

---

## 3. THE PART THAT IS ACTUALLY USEFUL, AND IT IS NOT THE FAILURE

The redirect discussion — *"use m202 or s959 instead, they score 4/4"* — has never priced this:

> **Cell 8's witnesses and B1330's best-case set are NOT knot complements in S³. So B1273's closing
> construction — the record's own route to a compact carrier — DOES NOT TRANSFER TO THEM.**

Redirecting to those objects does not merely trade predicates. **It costs the closing construction.**
That price was invisible until the frame condition was written down, and it belongs in any future
comparison of m004 against its alternatives.

---

## 4. CONTROLS — four, all PASS

| # | control | what it did |
|---|---|---|
| **K1** | `b₁(Y₃) = 0` reproduced on the rebuilt environment, matching the three banked routes (Smith form on F(2,6); the Alexander module; SnapPy's filled cover) | `H₁ = ℤ/4 ⊕ ℤ/4`, vol 2.93e−12 |
| **K2** | the routine **returns `b₁ > 0`** on m003 (1), m125 (2), m129 (2) | memo 164 — it can distinguish |
| **K3** | #38 discipline on every condition | applied |
| **K4** | population printed before any verdict, seven candidates named individually | the B1197 vacuity trap |

*Environment note: the container was recycled mid-session — repo, PDFs, SnapPy and sympy all gone.
Everything had been pushed and `git ls-remote` confirmed the exact tip, so nothing was lost; rebuilt
by re-clone plus SnapPy 3.3.2 / sympy 1.14.0. **K1 exists to catch precisely a drifted rebuild.***

---

## 5. THE FENCE — stated in the seal before the run, and it governs every line above

**A failed necessary condition closes the route FOR THAT OBJECT, never the route itself.**
`b₁(Q) = 0` says **Joyce–Karigiannis cannot resolve that locus**. It says nothing about whether some
other construction can, and **nothing about the G₂ route as such**. Any sentence of the form *"the G₂
route is closed"* is forbidden output of this cell.

**I-26 UNEARNED** — no generation count is licensed. **X is not constructed** — every statement here
is a condition *on* a closing, never a property *of* one. No value.

**Gate 5 untouched. Nothing promotes to `CLAIMS.md`.**
