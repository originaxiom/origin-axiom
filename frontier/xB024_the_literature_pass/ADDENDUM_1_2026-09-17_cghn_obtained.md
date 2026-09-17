# xB024 ADDENDUM 1 (2026-09-17) — CGHN OBTAINED: the UNREACHABLE grade was WRONG, and the closed case closes

**Beyond the seal.** `PREREGISTRATION.md` untouched (`9880dc01…`). Cell `C1`–`C2`,
`verification/cghn_chain.py`, run after the arc was banked, at the owner's instruction *"go for it"*.

---

## 1. THE PROCESS CORRECTION, FIRST, BECAUSE IT IS THE MOST USEFUL THING HERE

xB024's banked `FINDINGS.md` graded **CGHN UNREACHABLE** after two failed routes. **That was wrong.**
The paper was **freely available the whole time** — on **Project Euclid's open Experimental
Mathematics archive**, and as **`snappaper3.pdf` on Neumann's Columbia preprints page**, *the same
page that had already supplied Neumann–Reid one cell earlier*. The first attempt failed only
because WebFetch's reader could not parse the PDF binary; extracting it locally with `pypdf` worked
immediately — exactly as it had for Kawauchi one arc before.

> **"UNREACHABLE" described this seat's SEARCH, not the source.** A negative access result needs the
> same controls as a negative measurement: **try the author's own page, try the journal's open
> archive, and parse the bytes yourself before concluding the door is shut.**

**And the arc's banked headline is amended by this.** xB024 reported *"NO new insight"* — a verdict
reached **while CGHN was wrongly believed out of reach.** With CGHN in hand the pass yields three
real things, below. The original headline stands for the six targets it covered; **it does not stand
for T1**, and this addendum says so rather than leaving the banked sentence to be read as final.

## 2. B1239's TWO QUOTATIONS ARE EXACT

**CGHN §5A, verbatim:**

> *"This leads to an invariant `cs(M)` of a hyperbolic 3-manifold M in `ℝ/(1/2)ℤ`. If M is closed the
> Chern–Simons invariant is well defined modulo 1, but Snap and SnapPea still only compute modulo
> 1/2. This is no real loss, since the Chern–Simons invariant of a closed manifold M modulo 1 can
> also be computed from the first homology of M together with the eta-invariant `η(M)`…"*

**CGHN §5B, verbatim:**

> *"The relation of `η(M)` to `cs(M)` for a **compact** 3-manifold M is* `3η(M) ≡ 2cs(M) + τ (mod 2)`
> *(see [Atiyah et al. 1975]), where `τ` is the number of 2-primary summands of `H₁(M;ℤ)`. Thus
> `η(M)` completely determines `cs(M)` if M has known homology."*

**Both of B1239's quotations are exact and correctly attributed** to Atiyah–Patodi–Singer,
*Spectral asymmetry and Riemannian geometry, II*, Math. Proc. Cambridge Philos. Soc. **78**:3 (1975)
405–432. **T1's sealed prediction — "the record's use is CORRECT" — is CONFIRMED.**

**A false alarm of this seat's, recorded:** an intermediate pass reported *"Atiyah: 0 hits"* and
began to treat the attribution as suspect. **That was a text-extraction artifact** — the PDF renders
the name as `A tiy ah, P ato di and Singer`. **Caught and corrected before it was used for
anything.** Second time in two arcs that a "defect in the record" dissolved on closer reading.

## 3. WHAT MEYERHOFF–OUYANG ACTUALLY REQUIRES — L194's guess, confirmed by a readable source

**CGHN §5B, verbatim:**

> *"There is also a cusped version of this: **Meyerhoff and Ouyang [1997] extended the definition of
> `η(M)` to cusped M for which one has chosen a basis of homology at each cusp.**"*

and on provenance:

> *"A formula for `η(M(p,q))` … was given in [Meyerhoff and Neumann 1992], where it was proved
> 'locally' … It was proved globally in [Ouyang 1997]."*

**GRADE: SECONDARY.** This is CGHN *describing* MO. **MO itself remains UNREAD and is cited for
nothing.** But L194's register entry has, since 2026-09-02, spoken of a *"cusp-basis correction"* as
a conjecture about the definition. **CGHN confirms it: MO's cusped `η` requires a chosen basis of
homology at each cusp.**

## 4. THE CHAIN THAT CLOSES IN THE CLOSED CASE

| step | source | grade |
|---|---|---|
| `3η ≡ 2cs + τ (mod 2)`, `τ` = # 2-primary summands of `H₁` | **CGHN §5B** | **READ-AT-SOURCE** |
| `η` odd under orientation reversal, isometry-invariant ⇒ `η = 0` for closed amphichiral | standard | **NOT SOURCED HERE — the one unsourced link, and it is named** |
| ⇒ `2cs + τ ≡ 0 (mod 2)` | — | derivation |
| free orientation-reversing involution ⇒ `Fix = ∅` ⇒ `σ = 0` ⇒ `Tor H₁ ≅ A⊕A` ⇒ **`τ` even** | **Kawauchi I + III** (xB023) | **READ-AT-SOURCE** |
| ⇒ **`cs ≡ 0 (mod 1)`** | — | derivation |

> **A CLOSED hyperbolic 3-manifold carrying a FREE orientation-reversing involution has `cs ≡ 0`
> mod 1 — not merely mod ½.** Both substantive ingredients are read at source; neither is
> paraphrased.

## 5. C1 — AND A VACUOUS PASS OF THIS SEAT'S, CAUGHT AND REMOVED

On the **46** closed manifolds built to carry a free orientation-reversing involution:

- **`τ` EVEN: 46 of 46** — the Kawauchi step, measured.
- **`cs`: UNAVAILABLE for 46 of 46** — `ValueError: The Chern-Simons invariant isn't currently known.`

**The first version of this cell PASSED on that.** Its condition was `zero + errors == total`, which
**passes when every measurement fails.** That is this record's own **test-vacuity** class, written by
the seat that has spent the session catching it elsewhere. **The condition now gates only on the
half actually measured, and the `cs` half is reported UNTESTED.**

**The cause is in CGHN itself (§5B):** Snap obtains these invariants only by **bootstrapping along
chains of hyperbolic drillings and fillings**, and for a manifold not so linked it *"cannot
compute"* them. The closed census covers built here are exactly such manifolds. **The literature
predicted the instrument failure.**

**FENCE:** SnapPy reads `cs` mod ½ (CGHN §5A), so even where `cs` were available this run could not
see the mod-1 conclusion. **The mod-1 result is a READ-AT-SOURCE DERIVATION, not a measurement, and
is not claimed as one.**

## 6. WHAT THIS STILL DOES NOT DO

**It does not close L194.** L194's open half is **cusped**; the chain above is closed-case only, and
the cusped `η` it would need is **Meyerhoff–Ouyang, still unread**. xB023's seal declared this
before any cell ran and it remains true.
