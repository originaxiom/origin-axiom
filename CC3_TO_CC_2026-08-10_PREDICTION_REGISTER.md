# THE PREDICTION REGISTER — what the framework actually says about the world

cc3, 2026-08-10. **Gate 5-Q: every entry is weight-0 — a count, a quotient, an
exclusion, or a structural fact. No entry contains a mass, a coupling, or a
scale, because the framework cannot produce one by theorem.**

**Why this document exists.** The permitted class of predictions was never
written as predictions. ~~θ_QCD = 0 sits in the ledger without emphasis;~~ the ℤ₆
falsifiability clause is a subordinate phrase; charge quantisation went
unclaimed until this campaign. Every entry below was already derived somewhere —
**none of them is new mathematics.** What is new is stating them as claims about
the world, each with a falsifier.

**Read the status column strictly.** *Confirmed* means nature agrees, not that
the framework is uniquely responsible — several entries are also explained by
other frameworks, and that is noted.

---

## P1 — θ_QCD = 0

**Claim.** The strong CP phase vanishes identically.

**Why.** The object is **amphichiral** — equal to its own mirror — forcing
`Z_k(M) = Z_{−k}(M)` and hence CS = 0. Parameter-free; nothing is tuned.

**Falsifier.** A nonzero neutron electric dipole moment consistent with θ ≠ 0.
Current bound roughly |θ| < 10⁻¹⁰.

~~**Status: CONFIRMED, and it is the framework's strongest contact with nature.**~~
*Not unique* — axion models also give θ → 0. ~~But here it costs **nothing**: no
new particle, no new symmetry, no tuning. It is a consequence of a geometric
property the object has for independent reasons.~~

> ### ⚠ STATUS WITHDRAWN 2026-08-10 — P1 IS NOT A PREDICTION. It is a HOOK.
>
> **Two independent objections, reached from opposite directions, and each is
> fatal on its own.**
>
> **(a) The derivation does not reach θ_QCD** — cc, B1009, accepted at the third
> ask. Amphichirality ⟹ CS = 0 is real and stays (m004 is amphichiral; X25
> carries it). But reading the object's level `k` as the SM's `θ_QCD` is an
> **object→physics functor application**, and Gate 5 / L91 say the typed functor
> **does not exist**. `THE_SM_VERDICT.md` row 6 has said strong CP is *"never
> addressed"* the whole time; `THE_LADDER.md` X6 is **BLIND**.
>
> **(b) The falsifier does not test θ_QCD** — this seat, sealed independently in
> `CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md` **before cc's relay was read**,
> graded **S4**. The measurable quantity is **θ̄ = θ_QCD + arg det M_q**. A
> nonzero nEDM is consistent with `θ_QCD = 0` and `arg det M_q ≠ 0`, so it
> **cannot refute the claim**. Closing that gap needs the quark mass phase, which
> is weight ≠ 0 and **forbidden by theorem**.
>
> **So P1 fails at both ends: it does not derive what it claims, and its
> falsifier does not test what it claims.** The register's *strongest* entry is
> its weakest. **Status: HOOK — not confirmed, not testable, not withdrawn as
> mathematics.** What survives is CS = 0, object-level, and a reason to want the
> functor.
>
> The narrower CP-adjacent result that *is* banked: **B303's `sign = sign(CS)`**.

---

## P2 — charge quantisation, with an explicit exclusion list

**Claim.** Every physical representation satisfies

```
        t/3 + d/2 + Y  ∈  ℤ
```

(t = colour triality, d = weak duality, Y = hypercharge). **This is not a
tendency; it is a selection rule.**

**Forbidden, concretely:** a colour-singlet weak-singlet of charge ½ or ⅓; a
free particle of charge ⅓ that is not a colour triplet; any hypercharge not
congruent to −t/3 − d/2 mod 1.

**Falsifier.** Observation of a fractionally charged colour singlet, or any
state violating the congruence.

**Status: CONFIRMED.** No such state has ever been seen. *Not unique* — any
simple-group embedding quantises charge; **what is stronger here is that the
quotient ℤ₆ is derived (B862) rather than assumed**, and the SM's own data
cannot fix it.

---

## P3 — the gauge group's global form is [SU(3)×SU(2)×U(1)]/ℤ₆

**Claim.** Not SU(3)×SU(2)×U(1), and not the ℤ₂ or ℤ₃ quotient. **ℤ₆ exactly.**

**Why it is a real prediction.** *"The SM's own data leaves Γ ∈ {1, ℤ₂, ℤ₃, ℤ₆}
ambiguous (Tong 1705.01853); the chain FORCES ℤ₆"* — and B862 states outright
that it is *"falsifiable in principle via **line-operator spectra**."* Different
global forms admit different Wilson/'t Hooft line spectra.

**Falsifier — enumerated 2026-08-10**, `frontier/B796_coupling_campaign/z6_line_spectrum/`.
The previous wording ("a line-operator spectrum inconsistent with the ℤ₆
quotient") named a *kind* of evidence, not an object. The spectrum has now been
computed and the four candidate global forms have **four distinct magnetic
signatures**:

| Γ | magnetic classes | colour flux? | weak flux? | **both together?** |
|---|---|---|---|---|
| 1 | 1 | no | no | no |
| ℤ₂ | 2 | no | yes | no |
| ℤ₃ | 3 | yes | no | no |
| **ℤ₆** | **6** | yes | yes | **YES** |

The **minimal monopole** of the derived form carries hypercharge magnetic charge
**1/6 together with colour flux 1/3 and weak flux 1/2** — it is *not* a pure
hypercharge monopole, and **no other global form admits an object carrying both
colour and weak flux.** Minimality is strict: the Dirac pairings over a
generation are `1,0,1,0,1,0,1` with **gcd 1**, so no smaller magnetic charge
stays local against observed matter.

**Falsifiers, any one of which kills ℤ₆:**

- **F1** a minimal-hypercharge monopole with **no colour flux** (leaves 1 or ℤ₂)
- **F2** a minimal-hypercharge monopole with **no weak flux** (leaves 1 or ℤ₃)
- **F3** any monopole whose (colour, weak, hyper) flux is not one of the six rows
- **F4** a pure-hypercharge monopole below hypercharge magnetic charge 1
- **F5** a genuine bare colour-triplet Wilson line `(3,1)₀`
- **F6** a bare weak-doublet line `(1,2)₀`
- **F7** an isolated hypercharge-1/6 colour singlet

**Confirming signature (C1):** a monopole carrying colour **and** weak flux
together. Unique to ℤ₆.

**Status: TESTABLE, WITH A STATED LIST — still not tested.** No monopole has
been observed; nothing above has moved to CONFIRMED. **This remains the
framework's sharpest distinguishing claim** — it answers a question the Standard
Model *cannot* answer about itself.

> **Caution added by the same arc — P2 does NOT support P3.** All observed SM
> matter descends to **all four** global forms (`e = t/3+d/2+Y` is an integer for
> every multiplet, so it vanishes mod 1, ½ and ⅓ alike — this reproduces Tong
> 1705.01853 from the descent condition alone). P2 is therefore CONFIRMED and
> WEAK; P3 is UNTESTED and STRONG. They share a lattice, not a test, and must not
> be read as mutually reinforcing.
>
> **No monopole mass is predicted, and none can be** — the weight ledger puts
> every derived quantity at weight 0. The prediction is about **charge
> correlation**, which is scale-free.

---

## P4 — right-handed neutrinos exist

**Claim.** A generation is the **16** of SO(10) — fifteen observed states **plus
ν_R**. Neutrinos therefore have mass.

**Falsifier.** Massless neutrinos.

**Status: CONFIRMED** (neutrino oscillation). *Not unique* — any SO(10)
embedding predicts this.

---

## P5 — neutrino masses are DIRAC at the renormalisable level

**Claim, and it is the sharpest new one.** The E₆-invariant cubic on the 27 is
**exactly** `16·16·10 + 10·10·1`. The Majorana term **`16·16·1` is forbidden** —
it carries U(1) charge +6, computed this campaign. So **the framework supplies no
renormalisable Majorana mass for ν_R.**

**Falsifier.** Observation of **neutrinoless double beta decay** would establish
Majorana neutrinos and require a mass term the 27's cubic does not contain.

**Status: TESTABLE, and currently unfalsified** (0νββ not observed).

**Conditionality, stated plainly.** This constrains the **renormalisable** cubic
only. Majorana masses can still arise from non-renormalisable operators or from
representations beyond the 27 — as they must in every E₆ model, since the 27 has
no 126-equivalent. **So a 0νββ signal would not refute the framework; it would
establish that structure beyond the 27 is required.** That is a weaker claim than
"no 0νββ" and it is the honest one.

---

## P6 — the exotics' quantum numbers, if any are found

**Claim.** Vector-like exotics, if they exist, are **exactly** the fermionic 10:

| | states | hypercharge |
|---|---|---|
| a vector-like pair of **colour triplets** | 3 + 3̄ | \|Y\| = **1/3** |
| a vector-like pair of **weak doublets** | 2 + 2 | \|Y\| = **1/2** |

**and nothing else** — no colour octets, no charge-2/3 triplets, no SU(2)
triplets.

**Falsifier.** A vector-like exotic with any other quantum numbers.

**Status: STRUCTURAL, untested.** Costs nothing to state and would be sharply
violated by the wrong discovery.

---

## P7 — exactly two extra neutral gauge bosons

**Claim.** The cascade lands at **rank 6**; the SM is rank 4. So there are
**exactly two** additional neutral gauge bosons — no more, no fewer.

**Falsifier.** Discovery of exactly one Z′, or three, or a demonstration that the
SM's gauge group does not embed in a rank-6 structure.

**Status: STRUCTURAL, and CONDITIONAL** — on the rank-6 embedding, and on the
removal mechanism that **gap 2 shows the framework does not supply**. The
literature's route (Green–Schwarz) makes them massive; the framework has no
axion, no 2-form, no B∧F.

**And the mass is forbidden.** *"Two, and heavy"* is sayable. *"Two, at
10¹⁶ GeV"* is not, ever.

---

## P8 — the gauge group terminates

**Claim.** The Standard Model is the **terminal registerable algebra** (B863) —
no further gauge factors below it.

**Falsifier.** A new low-energy gauge interaction.

**Status: CONFIRMED so far.**

---

# WHAT IS NOT PREDICTABLE, AND WHY

**Forbidden by theorem** — every dimensionful quantity: masses, dimensionful
couplings, Λ, any scale. The object is scale-free (weight ledger), the
dimensionful content lives in the level k (L15), and the object cannot see k
because CS = 0. **This is not a gap. It is a type.**

**Not derived** — the number of generations. Three mechanisms examined: two
refuted, one *shaped* with mechanism-hood fenced. **The framework predicts a
generation's exact content and not its multiplicity.**

---

# THE HONEST SUMMARY

~~**Eight entries. Four confirmed, three testable, one structural.**~~ Every one is
weight-0; not one contains a number with units.

> **RECOUNTED 2026-08-10 — three confirmed, not four.** **P1 (θ_QCD = 0) is
> withdrawn to HOOK** (cc/B1009, third ask): the object→physics functor it needs
> does not exist. It was the register's headline entry and the only one billed as
> *"the framework's strongest contact with nature."* **The framework's strongest
> contact with nature is now P2, charge quantisation** — which the register itself
> marks *not unique*, and which by the ℤ₆ line-spectrum arc **holds in all four
> global forms**, so it does not even fix the thing P3 claims.
>
> A **falsifier-sharpness audit** was sealed independently the same day
> (`CC3_TO_CC_2026-08-10_FALSIFIERS_SEALED.md`) and grades **four of eight
> falsifiers defective as written**. The full status recount is Phase B,
> `CC3_TO_CC_2026-08-10_FALSIFIERS_VERDICT.md`.

**Two are distinguishing** — P3 (the ℤ₆ global form, which the SM cannot fix
about itself) and P5 (Dirac at the renormalisable level, which 0νββ probes).
**The rest are shared with other frameworks**, and the register says so rather
than counting them as unique support.

**P3 now carries seven named falsifiers and one confirming signature**
(`frontier/B796_coupling_campaign/z6_line_spectrum/`, 2026-08-10). The sharpest:
the minimal monopole must carry **colour and weak flux together**, which no other
global form permits. **The count of eight does not change, and neither does the
tally of what is confirmed** — P3 is still untested. What changed is that it can
now be *lost*, which it could not be before.

**One correction to how the eight combine:** P2 and P3 share a lattice, not a
test. All SM matter descends to all four global forms, so **P2's confirmation is
no evidence for P3.** Four confirmed entries do not lend weight to the two
distinguishing ones.

**The point of this document is not that the framework is confirmed.** It is that
the permitted class was never harvested. **Every entry above was already derived
and none had been stated as a claim about the world with a falsifier attached.**
