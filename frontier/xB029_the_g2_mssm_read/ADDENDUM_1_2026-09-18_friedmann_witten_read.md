# xB029 ADDENDUM 1 (2026-09-18) — FRIEDMANN–WITTEN READ AT SOURCE: the torsion formula carries a hypothesis the record's object VIOLATES, and this seat did not check it before registering L225

**Beyond the seal.** `PREREGISTRATION.md` untouched (`b41a1a5e…`). **`FINDINGS.md` untouched** — it is
banked at `12673f28` and this addendum does not revise it; it grades the one inference it flagged.

**T. Friedmann and E. Witten, *Unification Scale, Proton Decay, And Manifolds Of G₂ Holonomy*,
hep-th/0211269v2, Adv. Theor. Math. Phys. 7 (2003) 577–617.** **CITED-UNREAD → READ-AT-SOURCE.**
Obtained from arXiv — **freely available, no gate.** It is Acharya et al.'s ref. [7] and the actual
origin of the threshold formula xB029 built on.

## 1. WHY THIS WAS THE NEXT THING

L225 as registered said, in its own words:

> *"(i) `T_O = −log|Tor H₁|` is **xB029's inference from one worked example, not the source's
> statement** … **Until (i) is settled at source this lead supports nothing.**"*

**It is now settled at source, and it did not settle the way the flag anticipated.** The flag was
about whether the *formula* generalises. **The real defect is a hypothesis on the MANIFOLD.**

## 2. WHAT FRIEDMANN–WITTEN ACTUALLY ASSUME — verbatim, §3

> *"We further assume that the first Betti number of `Q` vanishes, `b₁(Q) = 0`. … This means that, in
> expanding around the trivial `SU(5)` connection on `Q`, there are no zero modes for gauge fields.
> Such zero modes would lead to massless chiral superfields in the adjoint representation of
> `SU(5)`."*
>
> *"Instead, we assume that that there is a nontrivial **FINITE fundamental group `π₁(Q)`** and first
> homology group `H₁(Q)`. A typical example … is a lens space, `Q = S³/Z_q`."*
>
> *"Having a finite and nontrivial first homology makes it possible to break `SU(5)` to the standard
> model subgroup `SU(3)×SU(2)×U(1)` by a discrete choice of flat connection in the vacuum."*

And, in §3.1:

> *"**For a three-manifold `Q` with finite fundamental group**, and a non-trivial irreducible
> representation `ω_i`, there are no zero modes."*

Their result, §3.4, which is Acharya et al.'s (A9) with `G ↔ 5`:

> **`T_O = −log q`, `T_ω = log(4 sin²(5πw/q))`.** *(Provenance confirmed.)*

And the derivation of `T_O`, Appendix A, verbatim:

> *"the lens space has a cell decomposition in which the chain group `C_k` is isomorphic to `ℤ` for
> `k = 0,…,3`. The only non-trivial boundary operator is `∂_{2→1} : C₂ → C₁`, which equals
> multiplication by `q`. To compute `T_O(S³/Z_q)`, **relative to a basis of the integral homology, we
> should first remove subgroups of the chain groups that generate the homology** … Then the
> Reidemeister torsion … is defined as an **alternating sum of logarithms of the boundary maps**; in
> the present case, this reduces to `−log ∂_{2→1} = log(1/q)`."*

## 3. THE DEFECT, NAMED

**Every hyperbolic 3-manifold has INFINITE `π₁`** — it is a torsion-free lattice in `PSL(2,ℂ)`.
**The record's object, its whole tower, and every closed member xB029 measured are therefore OUTSIDE
A STATED HYPOTHESIS of the paper that supplies the torsion formula.**

**xB029 checked the wrong fence.** It declared and measured **compactness** (`b₁ = 0`, which the closed
members **do** satisfy — that hypothesis is met). It **never looked at `π₁`**, because it read the
formula in the citing paper and not the hypotheses in the cited one.

> **This is the MISMATCHED HYPOTHESIS class — the error this seat proposed minting as R58-1 and has
> not yet minted.** It is the same shape as B1239 applying Kawauchi's closed-manifold theorem to
> cusped manifolds, and the same shape as xB023 Addendum 1's necessary-not-sufficient proxy.
> **Three times in three days, and this time in the arc that flagged the risk in the abstract while
> committing it in the concrete.**

## 4. WHAT THE CELLS MUST NOW DECIDE — sealed before they exist

**F1 — documentary**, §2 above: the quotations, and the provenance `(A9) ← FW §3.4`. No prediction; it
is a transcription and stands or falls on the quotes.

**F2 — WHAT SURVIVES: is `T_O = −log|Tor H₁(Q)|` true independently of `π₁`?** FW's own recipe is
**chain-level algebra**: remove the free homology, take the alternating sum of logs of the boundary
maps. For a rational homology 3-sphere the surviving complex is `ℤᵐ --∂--> ℤᵐ` with `det ∂ ≠ 0`, and
`H₁ = coker ∂`.
*Prediction, sealed:* `|det ∂| = |coker ∂| = ∏(elementary divisors)` **identically**, so
**`T_O = −log|Tor H₁(Q)|` for EVERY rational homology 3-sphere, hyperbolic or not — `π₁` finiteness is
NOT required for this term.** Calibration: `m = 1, ∂ = (q)` must return `−log q`, FW's own answer.
*Kill:* any mismatch, and the `T_O` generalisation falls with the rest.

**F3 — DOES THE HYPOTHESIS FAILURE BITE IN PRACTICE?** FW need *no zero modes* — `H¹(Q; ω) = 0` — and
guarantee it only for finite `π₁`. For a closed hyperbolic `Q` the guarantee is gone; **whether the
conclusion still holds is measurable.** For a finite abelian character `χ` of `H₁(Q)`,
`b₁(Q_d) = Σ_{χᵈ=1, χ≠1} dim H¹(Q; ℂ_χ)` over the degree-`d` cyclic cover, so **`b₁ > 0` in any cyclic
cover is exactly a zero mode.** Measured on the closed tower members, with a **lens space carried as
the finite-`π₁` calibration, which must give `b₁ = 0` throughout.**
*Prediction, sealed:* **`b₁ = 0` everywhere in range — the conclusion SURVIVES the hypothesis
failing**, for the abelian characters tested.
*Kill:* one cyclic cover with `b₁ > 0` means zero modes are real on the hyperbolic side, the simple
torsion formula needs FW's `K_i` correction there, **and L225 dies rather than being graded down.**
*Fence declared now:* **abelian characters are NOT all of FW's `ω_i`.** FW's statement covers **every
non-trivial irreducible representation**; F3 tests **only the abelian ones**. **A pass is therefore
strictly weaker than FW's hypothesis and must be reported at that width.**

## 5. WHAT THIS ADDENDUM CANNOT DO

It cannot un-register L225's over-reach; it can only grade it. **It does not claim a hyperbolic `Q` is
admissible in the G₂ construction** — FW assume it is not, and nothing measured here overturns an
author's stated assumption. **Gate 5 absolute. Nothing to `CLAIMS.md`.**

## 6. THE SEAT'S PRIOR

F2 holds · **F3 passes, and the honest reading is "the conclusion survives where the hypothesis does
not", which is WEAKER than "the hypothesis was unnecessary"** · and **the headline of this addendum is
the defect in §3, not whatever F2 and F3 return.**
