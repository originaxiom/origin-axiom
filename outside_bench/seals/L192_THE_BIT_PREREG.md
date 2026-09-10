# PREREGISTRATION — L192: does the object's ℤ/2 fix the CP-conservation BIT?

**Sealed before any computation. Bench: the outside bench. Date 2026-09-10.**

## 0. Why this, and the standing of the question

`docs/OPEN_LEADS.md` L192 (registered 2026-08-31, B1226), ★★★, **never run**. Its own text:

> Box D — β-odd, dimensionless: θ_QCD, δ_CKM, δ_PMNS — is the only box where the object has an
> output at all, and that output is `CS`, forced 2-torsion by amphichirality (B1224): **one bit**.
> Every probe ever fired into box D demanded a *continuous value* from that bit-valued channel …
> **3/3 asked for a value; 0/3 asked the bit.**

Corpus exhausted first (`already_banked.py`, terms stated): *"2-torsion subgroup mirror odd invariant
amphichiral"*, *"cannot count only a bit chirality"*, *"A[2] value group torsion chirality"*,
*"generation number impossible amphichiral theorem"*, *"mirror-odd quantum invariant twist family"*.
The settled arcs those return (B1183, B1201, B1166, B1241) are read and none asks L192's question.
The `2-torsion` grep returns B152, B1224, B928/B938/B939, `THE_END_TO_END_CHAIN` and L119 — the
2-torsion *fact* is banked many times; **the bit-level CP question is not**.

## 1. The three preconditions L192 itself sets, and how each is met

**(a) B813 is the governing theorem.** B813: *"The direct CS(m004) = θ_QCD dictionary is refuted on
type: a fixed PSL(2,ℂ) geometric invariant cannot fill the coefficient slot of `e^{iθW(A)}`, whose
functional slot a Chern–Simons object already occupies."* **This construction does not re-enter that
slot, and here is why.** B813 forbids an *element-to-element* map: a real number CS being written
into a coefficient. What is compared here is a map **between two two-element groups**, each obtained
as the 2-torsion subgroup `A[2]` of a circle:

  * object side — `A = ℝ/½ℤ`, the value group of Chern–Simons; `A[2] = {0, ¼}`;
  * phase side — `A' = ℝ/ℤ`, the value group of a CP-odd angle; the CP-even locus is the fixed set
    of `φ ↦ −φ`, which is `A'[2] = {0, ½}`.

No real number is placed in any coefficient. B813's slot is untouched, and a homomorphism of
2-element groups is not a value dictionary. **If a reader judges that this still re-enters the slot,
the cell fails and is recorded as failing.**

**(b) The criterion must be able to FAIL in both directions (MB12).** A bit that cannot come out
"CP-violating" is vacuous. The bite control L192 itself names is **m003**, the sibling that sits at
the other element. This is the strongest available control precisely because m003 is **also
amphichiral**: it is not chirality that puts the object at 0.

**(c) Gate 5 absolute.** The object side is computed and written down **before** any measured
physical value is named anywhere in the output. The certificate prints the object side, then the
type audit, and names a measured quantity only in a clearly-labelled interpretive section at the end.

## 2. THE CELLS — two outcomes each, fixed now

**CELL 1 — is the bit well-defined and non-vacuous?**
Compute `CS mod ½` for every amphichiral manifold in the working census and read off `A[2]`.
* **A** — every amphichiral manifold lands on the same element (all 0, or all ¼). Then the bit
  carries no information, the channel is vacuous, and **L192 closes NEGATIVE**.
* **B** — amphichiral manifolds occupy **both** elements. The bit is non-vacuous: amphichirality
  forces membership in `A[2]` but does **not** force which element.

**CELL 2 — where does the object sit?**
* **A** — the object sits at the non-trivial element (¼).
* **B** — the object sits at the identity (0).

**CELL 3 — is the object's element forced by anything in its own class, or is it a fact about the
object?** Test: among amphichiral census manifolds, is 0 the majority, the minority, or is
membership predicted by another banked invariant (trace field, volume, cusp count)?
* **A** — some banked invariant predicts the element; the bit is then a restatement of that invariant.
* **B** — no banked invariant predicts it; the element is independent data.

## 3. CONTROLS, fixed now

* **C1 — the theorem must bite.** Every amphichiral manifold in the census must satisfy `2·CS = 0`
  in `ℝ/½ℤ`. A single violation kills B1224's theorem and the whole cell.
* **C2 — non-vacuity of the theorem.** At least one amphichiral manifold must have `CS ≠ 0`;
  otherwise the theorem is compatible with "CS is always 0" and says nothing.
* **C3 — the converse must FAIL.** B152 banked m208 as chiral with `CS = 0`. The certificate must
  reproduce a chiral manifold at 0, so that `CS = 0 ⇒ amphichiral` is seen to be false and the bit is
  not silently used as a chirality detector.
* **C4 — arithmetic.** `CS` is read at stated precision and the 2-torsion classification must be
  robust: the distance from the nearest element of `A[2]` must be below the stated tolerance by a
  margin printed with the result, not asserted.

## 4. WHAT THIS CANNOT DELIVER, stated before it is run

It cannot give a value of `θ_QCD`, `δ_CKM` or `δ_PMNS`; B813 forbids the value dictionary and
nothing here recovers it. It cannot connect the bit to a Lagrangian term. It cannot establish that
any SM phase *inherits* the object's bit — that needs a dictionary B813 shows cannot be the naive
one, and **no such dictionary is proposed here**. A positive result is a statement about the
object's box-D output and its type, and nothing more.

**Gate 5 untouched. No measured value is used as input anywhere in the computation.**
