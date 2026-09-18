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
