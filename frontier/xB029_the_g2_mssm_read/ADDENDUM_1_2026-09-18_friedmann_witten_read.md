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

---

## 7. THE RESULT — `verification/fw_read.py`, `verification/fw_f3.py`

### F2 — what survives: `T_O = −log|Tor H₁(Q)|`, and `π₁` never enters

FW's recipe is chain-level algebra. For a rational homology 3-sphere, after removing the free
homology, what survives is `ℤᵐ --∂--> ℤᵐ` with `det ∂ ≠ 0` and `H₁ = coker ∂`.

- **Calibration on FW's own case** (`m = 1`, `∂ = (q)`), `q = 2, 3, 5, 7, 99, 316`: returns
  **`−log q`** every time — **exactly `T_O(S³/Z_q) = log(1/q)`**.
- **400 random square integer boundary maps, `m = 1…6`: `|det ∂| = |coker ∂|` on 400 of 400**, zero
  mismatches.

> **`T_O = −log|Tor H₁(Q)|` holds for every rational homology 3-sphere. Nothing in the argument
> mentions `π₁`.** xB029's inference is **upgraded**: it is not a guess from one example, it is FW's
> own definition evaluated in general. **For the record's closed tower members
> `T_O = −log(L₂ₙ − 2)`.**

### F3 — the hypothesis BITES, and this seat's sealed prediction is REFUTED

§6 predicted **`b₁ = 0` everywhere — "the conclusion survives where the hypothesis does not."**
**It does not survive.**

For a degree-`d` cyclic cover of a `ℚHS³`, `b₁ = Σ_{χ ≠ 1, χᵈ = 1} dim H¹(Q; ℂ_χ)`, so **`b₁ > 0` IS a
zero mode.** Every admissible degree `≤ 33` measured; the rest marked **UNMEASURED and not scored**.

| member | `\|H₁\|` | hyperbolic | zero modes found (degree, `b₁`) |
|---|---|---|---|
| **calibration** `Σ₂ = L(5,2)`, **finite `π₁`** | 5 | no (lens) | **none** — degree 5 measured ✓ |
| `n=3` | 16 | yes, vol 4.32210 | none; degrees 2, 4 **all measured** |
| `n=4` | 45 | yes, vol 7.02850 | none; degrees 3, 5, 15 **all measured** |
| **`n=5`** | 121 | **yes, vol 4.68603** | **(11, `b₁`=10)** — all measured |
| **`n=6`** | 320 | **yes, vol 7.32772** | **(2,1) (4,1) (8,5) (10,1) (20,1)**; degree 40 unmeasured |
| **`n=7`** | 841 | **yes, vol 9.88228** | **(29, `b₁`=28)** — all measured |
| `n=8` | 2205 | yes, vol 12.35091 | none in degrees 3,5,7,15,21; **35, 105 unmeasured** |

**Three of six hyperbolic members carry abelian zero modes.** At `n=5` and `n=7` the effect is total —
`b₁ = 10 = 11−1` and `b₁ = 28 = 29−1`, i.e. **every** non-trivial character of that quotient has
`dim H¹ = 1`.

> **FW's sentence — *"For a three-manifold `Q` with finite fundamental group, and a non-trivial
> irreducible representation `ω_i`, there are no zero modes"* — genuinely NEEDS its hypothesis.
> Drop finite `π₁` and the statement is FALSE, demonstrably, on manifolds in this record's own
> tower.** This does not refute Friedmann–Witten, whose statement carries the hypothesis. **It
> refutes the transfer of their framework to a hyperbolic `Q` — which is what xB029 did.**

### A defect in this addendum's own first pass, recorded rather than overwritten

**F3 v1 reported a FALSE NEGATIVE.** It printed *"max b1 = 0"* for `n = 5` and `n = 7`, whose `|H₁|`
are `11²` and `29²` — so their **only** cyclic-cover degrees are 11 and 29, **both above v1's search
bound of 8**. Those rows were **unmeasured, not negative**, and `max(…, default=0)` printed a zero for
them. **The two members that carry the sharpest zero modes are exactly the two v1 scored as clean.**
v2 enumerates admissible degrees from `H₁` itself and marks the unreachable ones UNMEASURED.

---

## 8. THE VERDICT, AND WHAT L225 IS NOW

| | |
|---|---|
| **`T_O = −log\|Tor H₁(Q)\|`** | **SURVIVES** — chain-level algebra, `π₁`-independent, calibrated against FW's own answer (F2) |
| **the exact tower arithmetic** (`L₂ₙ − 2`, growth `log α`, crossing `n = 88`) | **UNTOUCHED** — it is mathematics and xB029's `FINDINGS.md` stands |
| **carrying the G₂ threshold framework to a hyperbolic `Q`** | **DEAD.** FW assume **finite `π₁`**; hyperbolic manifolds violate it; and the violation is **not benign** — zero modes are exhibited on three members (F3) |
| **L225's physics-facing half** | **RETRACTED.** Not graded down — **retracted** |

**The `T_λ` term, which xB029 already flagged as uncomputed, is now known to be worse than
uncomputed on this class: for the characters exhibited in F3 it is not even DEFINED by FW's eq. (3.1),
which requires no zero modes. It needs their `K_i` correction (3.3)–(3.5), and that is a different
computation from the one xB029 gestured at.**

**Gate 5 absolute. Nothing to `CLAIMS.md`. No value, no generation count, no physics reading.**

## 9. SCORING, AND THE CLASS THIS MAKES THREE OF

§6 predicted: F2 holds **(correct)** · **F3 passes — WRONG, it fired** · "the headline is the defect in
§3, not whatever F2 and F3 return" **(held, and the cells made the defect worse rather than milder)**.
**One of two, on the cell that mattered.**

**This is the MISMATCHED HYPOTHESIS class for the third time in three days** — B1239 applying
Kawauchi's *closed*-manifold theorem to cusped manifolds; xB023 Addendum 1's necessary-not-sufficient
proxy; and now xB029 carrying Friedmann–Witten's *finite-`π₁`* framework to hyperbolic manifolds.
**R58-1 (minting the class) remains sequenced behind B1376, which has not landed.** The instance is
appended to that item rather than the class being minted out of order. **What distinguishes this
instance: the hypothesis was in the CITED paper, not the citing one, and reading only the citing paper
is what hid it. The register's own rule — a CITED-UNREAD statement may not carry a load-bearing step
alone — would have caught it, and xB029 recorded Friedmann–Witten as CITED-UNREAD in the same commit
in which it leaned on them.**
