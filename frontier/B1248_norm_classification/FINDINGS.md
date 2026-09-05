# B1248 — ε IS THE FRICKE INVARIANT READ MODULO SQUARES

**Status: banked (frontier). Verdict PROVED.** Closes the refinement cell **B1192 named and left
open** — *"the general norm-classification is the named refinement cell"* — carried since
2026-08-27 and listed as **I1** in `docs/OPEN_ITEMS_2026-09-05.md`. Instrument + selftest in
`verification/norm_classification.py` (rc captured directly, E39). Gate 5 clean: no measured value.

## Why this ran — a bad probe, corrected

The prior crossing probe (prereg `6705d6b2`) asked *"does a pair supply a NUMBER?"*, scanned five
partners, saw `{−1, −19, −29, −71, −181}`, and returned **NO FORCED MAGNITUDE**. That verdict rested
on a stop rule — *the magnitude must be forced with no partner choice* — which demands the object be
a complete theory with zero inputs. No physical theory passes it. **The probe scanned five values of
a function and never asked for the function.** The owner rejected the verdict on exactly that
ground: *"the crossing problem is just our ignorance not understanding what crossing means."*

The function was one symbolic solve away.

## THE LAW (symbolic, general, any pair in SL₂)

For `A, M ∈ SL₂` with `cq − br ≠ 0`, the simultaneous-mirror realizer
`X A X⁻¹ = A⁻¹`, `X M X⁻¹ = M⁻¹` satisfies **identically**

> **det X · (cq − br)² = 2 − κ**, where **κ = tr[A,M] = x² + y² + z² − xyz − 2**

Verified by Gröbner reduction modulo both determinant relations: residue **exactly 0**, denominator
**a perfect square**. So in `K*/(K*)²`, **det X ≡ 2 − κ**.

**κ is not a new quantity.** It is **K001 / B167's Fricke–Vogt first integral** — the trace map's own
conserved quantity. The relational bit was never a separate object.

## THE INTEGRAL REFINEMENT — **CORRECTED by a peer seat's formula, verified here**

The additive commutator does it with **no linear solve at all**:

> **det(AM − MA) = 2 − κ** (identity, Gröbner residue 0), and
> **det X₀ = det( (AM − MA) / g ) = (2 − κ)/g²**, where **g = gcd of the entries of AM − MA**.

**WHAT THIS REPLACED, AND WHY IT WAS WRONG.** This arc's first version claimed
`det X₀ = squarefree(2 − κ)`. **That is false.** Checked against the *actual* integral realizer
module on 500 random noncommuting partners: **the peer formula scores 500/500, squarefree scores
493/500.** The sharpest counterexample:

> `2 − κ = −121 = −(11²)` with entry-gcd `g = 1`. The true `det X₀ = −121` — a **TORSOR**. My formula
> gave `squarefree(−121) = −1` and would have called it **THE BIT**.

They disagree exactly when `g²` is not the largest square dividing `2 − κ` — which **none of the 14
hand-picked partners in the first version exhibited**. The error was a generalization from a small
curated set, not an arithmetic slip.

**CORRECTED BIT CRITERION:** **ε = −1 ⟺ 2 − κ = −g²** — *not* "κ − 2 is a perfect square".
Verified 500/500 against the realizer module.

Hence the **trichotomy**, with `D = (2 − κ)/g²`:

| D | behaviour | banked as |
|---|---|---|
| **+1** | mirror realized inside SL₂(ℤ) — **no bit** | B1192 √2 control (κ = −2) |
| **−1** | **ε = −1, DIRECT** | B1192's crown positive (κ = 3) |
| **\|D\| > 1** | no GL₂(ℤ) realizer — **torsor form**, det X₀ = D | B1192 √7 control (κ = 263) |
| **0** (κ = 2) | module rank 2, both signs | **B1189's kill** |

**B1189's kill is dissolved as a separate fact.** `(A,A)` has no bit because κ = 2 — Fricke's
reducibility locus — forced, because A commutes with itself.

## ONE PAIR DOES NOT LICENSE A FIELD CONCLUSION — a second peer catch, confirmed

B1192's √2 control fixed **one** integral matrix `[[5,2],[2,1]]` and drew a conclusion phrased about
the **norm class of the field**. **Both determinant signs occur inside the same trace field ℚ(√2):**

| M | tr | trace field | D |
|---|---|---|---|
| `[[-35,-36],[1,1]]` | −34 | ℚ(√2) | **−1** |
| `[[-29,-12],[-12,-5]]` | −34 | ℚ(√2) | **+1** |

**The exclusion holds for the displayed pair, not for the field.** This was already implied by the
law (κ varies within a field) and this arc's first version **still repeated B1192's field-level
phrasing** — the peer seat caught it. Locked in
`test_one_pair_does_not_license_a_field_conclusion`.

## THE IDENTIFICATION WITH KNOWN MATHEMATICS (computed here, not cited)

The **Maclachlan–Reid quaternion algebra** of a two-generator group is `(A₀², B₁²)` where `A₀` is
the trace-zero part and `B₁` the part anticommuting with it. Verified on-bench: `A₀² = (tr²A − 4)/4`
and `B₁² = (2 − κ)/(tr²A − 4)` — **267/267 random pairs, exact, no floats.** So the algebra is

> **`( tr²A − 4 , (2 − κ)/(tr²A − 4) )`  ~  `( tr²A − 4 , (2 − κ)(tr²A − 4) )`**

**CORRECTED IN-SESSION.** A first draft of this arc wrote the algebra as `(tr²A − 4, 2 − κ)` — i.e.
identified **ε itself** with the second slot. That is **wrong**, and the check that caught it was the
**2T computation**: for the Q8 pair `(i, j)` the true algebra is `(−1, −1)`, the **Hurwitz
quaternions** (the known answer for the binary tetrahedral group), while the wrong form gives
`(−1, +1)`, split. **ε and the second slot differ by exactly the first slot.** For the object the
algebra is `(5, −5)` — split, since `(a, −a)` always is. The earlier draft's `(5, −1)` happens to be
split too, so the *conclusion* survived while the *statement* was false: a coincidence, not a defense.

`det X₀ = squarefree(2 − κ)` is **unaffected** — it is the realizer determinant, verified 14/14
integrally, and `tests/test_b1248_norm_classification.py::test_maclachlan_reid_second_slot` already
encoded the correct formula `B₁² = (2−κ)/(tr²A−4)`. Only the prose identification was wrong.

For the object `A = [[2,1],[1,1]]` the **first slot is tr²A − 4 = 5 = disc ℚ(√5)**.

*This is the programme's stated pattern: derive it by math, then find out it exists.* It is
**recorded as rediscovery**, not novelty — see `docs/DERIVATION_RECORD.md`.

## THE OBJECT'S OWN VALUE — and why the object alone has no bit

The once-punctured-torus fibre of m004 has **parabolic commutator, κ = −2** (computed in the
discrete faithful rep over ℚ(√−3)). So `2 − κ = 4 = 2²`, **D = +1: no bit.**

This supplies the **mechanism** for a conclusion previously held only as an obstruction argument
(B1161's free-orbit theorem, B1163, B1183, B1184): **the cusp pins κ at −2, below the wall κ = 2.**
The bit can turn on only past κ = 2. What A7 needs is not "an outside" in the abstract — it is a
partner that pushes κ across the reducibility wall.

## SCOPE AND FENCES

- The law is proved for **det M = +1**. For **det M = −1 there is no realizer at all**, and the
  reason is one line: `det M = −1 ⟹ tr M⁻¹ = −tr M`, so `XMX⁻¹ = M⁻¹` forces `tr M = 0`. The
  "norm −1" controls in B1192 are det +1 matrices (the square of a norm −1 fundamental unit); an
  earlier draft of this arc used `[[1,2],[1,1]]` (det −1) and produced a spurious mismatch against
  B1192's √2 control. **The partner matrix was read from B1192's own data, not inferred.**
- Over a field `det X` is only a **square class**; the honest integer invariant `det X₀` exists
  because the integral realizer module is rank 1 and ℤ's units are ±1.
- The square class is **not a bit in general**: over ℚ(√−3) a survey of 91 short-word pairs in
  π₁(m004) found the class taking many values (6 trivial, 59 at −1, 26 elsewhere). Only on the
  **canonical** structures — meridian pair, fibre pair — does it take a distinguished value. An
  earlier reading of that survey as "every non-fibre pair is −1" was **wrong and was caught by
  running it**.
- **NOT claimed:** no crossing to physics, no measured value, no prediction. This closes a
  structural cell. Gate 5 clean.

## Dependencies

B1192 (the cell this closes), B1189 (the kill it dissolves), B167/K001 (κ), B1161/B1163/B1183/B1184
(the A7 obstruction this supplies a mechanism for).

---

## ADDENDUM (same session) — THE CANONICAL PAIRS: ONLY ONE CARRIES OBJECT CONTENT, AND IT IS A TORSOR

The law makes A7 computable. `A = [[2,1],[1,1]]` is not an arbitrary matrix: it is **m004's
monodromy** on H₁ of the once-punctured-torus fibre. So the object supplies A. Does it supply a
*partner*? Three candidates are canonical, and **they must be graded, not counted**.

### 1. The monodromy pair (A, X_A) — OBJECT-SPECIFIC, and a TORSOR

m004 is amphichiral, so it supplies `X_A` with `X_A A X_A⁻¹ = A⁻¹` — which cannot commute with A,
by construction. **Identity (symbolic residue 0 on both basis realizers; 158/158 numeric):**

> **κ(A, X_A) = tr²A − 2**,  hence  **2 − κ = −(tr²A − 4)**

For the object, `tr A = 3`: **κ = 7**, `2 − κ = −5 = −disc ℚ(√5)`, so `det X₀ = squarefree(−5) = −5`,
**|D| > 1 → TORSOR FORM, not a bit.** The bit needs `κ − 2` a perfect **square**; the object's own
value is `κ − 2 = 5`, **squarefree**. The *value* −5 is object-specific (it depends on `tr A = 3`,
the golden monodromy).

**VACUITY CORRECTION, self-caught before banking.** A draft of this addendum added: *"over ℚ(√5) —
the object's own monodromy field — the class becomes exactly −1: the torsor was never a wall, it was
a wall over the wrong field."* **That is GENERIC, not object content.** `2 − κ = −(tr²A − 4)` and
`tr²A − 4` **is the discriminant of A's characteristic polynomial**, so the class trivialises to −1
over K **iff √disc ∈ K, i.e. iff K contains A's own eigenvalue field** — for *every* A, tautologically
(checked at tr A = 3, 4, 5, 6, 7, −3, 11: trivialising field = eigenvalue field in every case). What
is m004-specific is only **which** field it is (ℚ(√5), because tr A = 3). The *structure* is a
tautology of the identity and is recorded as such.

**Fence:** `X_A` is supplied by the amphichirality, which **B1234** showed is a consequence of axiom
**A6** (the orientation-double-cover choice). So this partner is object-supplied *modulo A6*, not
unconditionally.

### 2. The meridian pair — a REAL-GROUP result that the vacuity check KILLED

Computed in π₁(m004) itself (discrete faithful rep over ℚ(√−3); relator `w a w⁻¹ = b` verified,
340/340 traces in ℚ(√−3), volume `6·Lob(π/3)` matching Vol(m004) to 1e-15), the **meridian pair
gives class −1** — the bit — stable across 16 conjugators. This briefly looked like the object
supplying its own bit intrinsically, and it **reversed** the monodromy conclusion.

**It is vacuous.** For any two parabolics — and every pair of parabolics not sharing a fixed point is
conjugate to this form — `a = [[1,1],[0,1]]`, `b = [[1,0],[y,1]]` gives

> `tr[a,b] = y² + 2`, so **`2 − κ = −y²`**: minus a perfect square, **identically, for every y in
> every field.**

So class −1 is **forced by parabolicity** and is shared by the meridian pair of *every* cusped
hyperbolic knot complement (cross-checked on 5₂ and 6₁). **Zero m004 content. MB12 kills it**, and
with it the reversal — the monodromy conclusion stands.

### 3. The fibre pair — generic

Class **+1**, forced by `κ = −2` (parabolic commutator = the cusp), true of every once-punctured-torus
bundle.

### The statement

> **Of the object's three canonical pairs, the two that yield clean bits (±1) carry no object
> information at all, and the only one carrying m004-specific content yields a TORSOR whose
> invariant is the object's own field discriminant, −disc ℚ(√5).**

This is *"the object supplies the family, never the point"* as a computation with named invariants,
rather than as an obstruction argument. It does **not** resolve A7 and does not contradict B1161:
the classes here are Galois-invariant, hence constant across branches, exactly as the free-orbit
theorem requires.

**Method note, recorded because it nearly cost the result.** The monodromy computation lives on
`H₁(fibre) = ℤ²` — an **abelianization**. `abelianization-is-not-a-proxy` is a standing rule here,
and the real-group check was run *because* of it. That check produced an apparent reversal, and only
the MB12 vacuity test separated the two. **Both the shortcut and the over-correction were caught by
standing rules, not by intuition.**
