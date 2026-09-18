# xB023 ADDENDUM 1 (2026-09-18) — MEYERHOFF–OUYANG READ AT SOURCE: the cusp-basis correction is (1/3)ℤ, and the corollary that forces η = 0 provably cannot reach m003

**Beyond the seal.** `PREREGISTRATION.md` untouched (`277542e7…`). **The owner supplied the PDF.**

**R. Meyerhoff and M. Ouyang, *The η-invariants of cusped hyperbolic 3-manifolds*,
Canad. Math. Bull. 40(2) (1997) 204–213.** **UNREAD → READ-AT-SOURCE.** This was the register's
named blocker for L194 and it is now open.

---

## 1. WHAT THE PAPER ACTUALLY SAYS

**DEFINITION 2.1** defines `η(M)` for an oriented finite-volume cusped M with `h` cusps **after
fixing a meridian–longitude pair `(m_k, l_k)` at each cusp**, as a limit over Dehn fillings.

> **PROPOSITION 2.2.** *"`η(M)` differs only by **one-third of an integer** when different choices of
> the meridian-longitude pairs are made."*

**THAT IS L194's "CUSP-BASIS CORRECTION", QUANTIFIED.** The register has carried it as a conjecture
since 2026-09-02 and CGHN described it only as *"a chosen basis of homology at each cusp"*.
**It is `(1/3)ℤ`.**

For a knot or link **in S³** there is a canonical choice — the *topologically standard* pair, fixed
by `m_k = 0 ∈ H₁(N_k)` and `l_k = 0 ∈ H₁(S³ ∖ N_k)` — and **Proposition 2.3** makes `η` a well-defined
link invariant on that class.

> **PROPOSITION 2.4.** For `L ⊂ S³` hyperbolic with mirror `L*`: **`η(L*) = −η(L)`.**
>
> **COROLLARY 2.5.** *"If `L` is an **amphicheiral** hyperbolic knot or link, then `η(L) = 0`."*

**Corollary 2.5 is L194's missing step — and it carries a hypothesis: `L ⊂ S³`.**

## 2. WHAT THIS GIVES THE OBJECT, AND WHY IT CANNOT GIVE IT TO THE SISTER

**m004 = S³ ∖ 4₁**, and the figure-eight knot is amphichiral. **Corollary 2.5 applies and gives
`η(m004) = 0` — as a theorem, read at source.**

**m003 cannot be reached by it, and the reason is checkable rather than rhetorical.** A knot
complement in S³ has `H₁ ≅ ℤ`; an `h`-component link complement has `H₁ ≅ ℤʰ`. **Both are
torsion-free.** And `H₁(m003) = ℤ ⊕ ℤ/5` **has torsion**. **So m003 is not a knot or link complement
in S³, Corollary 2.5 is silent on it, and its sitting at `¼` contradicts nothing.**

> **This is a SECOND, INDEPENDENT explanation of the object's selection**, beside xB023's own (m004
> is the orientation double cover of the Gieseking manifold; 78/78 such covers at class zero against
> a 27.2 % base rate). The two do not compete: one is about a **free involution**, the other about
> **being an amphichiral knot in S³**. **m004 satisfies both. m003 satisfies neither.**

## 3. THE PREDICTION THIS MAKES — STATED BEFORE IT IS RUN

If Corollary 2.5 governs the `0`-vs-`¼` split, then **no quarter-class amphichiral cusped manifold
should be an amphichiral knot or link complement in S³.** The **necessary** condition is
torsion-free `H₁`, so:

> **PREDICTION: among the quarter-class amphichiral one-cusped census manifolds xB023 found
> (75 of them), NONE has `H₁ ≅ ℤ`.**

**KILL CONDITION, binding:** **if any quarter-class amphichiral manifold has `H₁ ≅ ℤ`**, then either
it is not an S³ knot complement despite the homology, **or the cusped relation between `η` and `cs`
carries slack the closed one does not** — and **either outcome must be reported as the headline**,
not absorbed.

**Controls:** the `0`-class side must be checked too — if *no* amphichiral manifold in either class
has `H₁ ≅ ℤ`, the test **discriminates nothing** and must be reported as vacuous. And `H₁ ≅ ℤ` is
**necessary, not sufficient**, for being a knot complement in S³; a member passing it is a
**candidate**, not a proof.

## 4. WHAT REMAINS OPEN REGARDLESS

`η` being well-defined only mod `(1/3)ℤ` (Prop 2.2) means **`3η` is well-defined mod `ℤ`** — so a
cusped analogue of APS's `3η ≡ 2cs + τ (mod 2)` would pin `2cs + τ` only **mod 1**, i.e. `cs` only
**mod ½**. **That is exactly the resolution SnapPy already has**, so the `0`-vs-`½` refinement stays
invisible and **L194's general cusp-local lemma is NOT closed by this reading.** What *is* closed is
the **object's own case**, twice over.


---

## 5. THE RESULT: THE KILL CONDITION FIRED. THE PREDICTION IN §3 IS REFUTED.

`verification/mo_corollary.py`, full one-cusped orientable census, **0 errors**:

| | amphichiral | with `H₁ ≅ ℤ` exactly |
|---|---|---|
| CS class **zero** | 106 | **14** (m004, s726, s912, t07734, t12071, t12587, …) |
| CS class **quarter** | 75 | **1** — **`o10_143849`** |

**§3 predicted NONE in the quarter class. There is one. The prediction is REFUTED and
Corollary 2.5 does NOT govern the `0`-vs-`¼` split.**

**The vacuity control passed** — 14 of the zero class do carry `H₁ ≅ ℤ`, so the predicate
discriminates and this is a real refutation, not a hollow one.

**The asymmetry is nonetheless real and large:** **13.2 %** of the zero class against **1.3 %** of
the quarter class. **That is a measured rate difference and NOT the claim that was made**, and it is
not promoted to one here.

### Why it failed — and §4 said so before the cell ran

**Corollary 2.5 gives `η = 0`, not `cs = 0`.** The step from `η` to `cs` in the **cusped** case is
exactly what **Proposition 2.2's `(1/3)ℤ` slack blocks**: `3η` is well-defined only mod `ℤ`, so a
cusped analogue of `3η ≡ 2cs + τ (mod 2)` pins `cs` only mod `½` — **the resolution SnapPy already
has.** §4 of this addendum stated that **before** the prediction was tested, and §3's prediction
**took the blocked step anyway.** The seal recorded both, so the failure is visible rather than
reconstructable.

**A residue worth one line, and not more:** `o10_143849` has `H₁ ≅ ℤ` — **necessary, not sufficient**
for being a knot complement in S³. Whether it actually is one is **unchecked**, and if it is not,
Corollary 2.5 never applied to it and the refutation is of this seat's inference rather than of any
reading of the paper. **Either way §3's prediction is dead as stated.**

### What survives, unaffected

- **`η(m004) = 0`**, by Corollary 2.5 applied to an amphichiral knot in S³ — **a theorem, read at
  source**.
- **m003 is not a knot or link complement in S³** (`H₁ = ℤ ⊕ ℤ/5` has torsion; S³ complements are
  torsion-free), so Corollary 2.5 is **silent** on it.
- **The cusp-basis correction is `(1/3)ℤ`** (Prop 2.2), retiring a conjecture the register carried
  since 2026-09-02.

**None of these is a physics result, and none is presented as one. L194 remains open.**
