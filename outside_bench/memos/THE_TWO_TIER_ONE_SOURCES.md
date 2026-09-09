# MEMO 192 — **BOTH TIER-1 SOURCES ARRIVE**: the cross-seat dispute is settled in the other seat's favour, with a caveat they should have; and the primary source *partially reopens* what memo 191 closed

**Date** 2026-09-09 · **Lane** outside bench · **Branch** `claude/outside-bench`
**Certificate** — the checkable parts are verified inline in `outputs/tier1_checks_out.txt`
**Gate 5** exact symbolic arithmetic. No measured value. §1 is a reading of a primary source, labelled as such.

---

## 1. `hep-th/0109152` — the cross-seat dispute: **the other seat is RIGHT**

The other seat's audit (`audit/physical-bridge-2026-09-05`) states that B1355 *"over-excludes the
broader exceptional-group construction"* because *"Acharya–Witten explicitly include the E₇ → E₆
route."* This bench refused to repeat that as established without the paper. **The paper is now
read.**

**Acharya–Witten §2.3, "Generalization"**, listing *"the cases most relevant for grand
unification"*, states verbatim:

> *"For `G = SO(10)`, to get chiral fields in the **16**, `Ĝ` should be `E₆`. … **For `G = E₆`,
> to get 27's, `Ĝ` should be `E₇`.**"*

> **The claim is CONFIRMED. B1355 over-excludes, and the correction stands.** This bench was
> wrong to withhold judgement only for want of the file, and right to withhold it until the file
> came.

### The caveat that belongs with it — the very next sentence

> *"A useful way to describe the topology of `X` in these examples is not clear."*

**Acharya–Witten name the `E₇ → E₆` route and say in the same breath that they cannot describe
the topology of the resulting seven-manifold.** So the route is *asserted to exist*, not
*constructed*. The other seat's own wording — *"its new curved cone remains a candidate, but
transferring 'one chiral 27' requires an actual model/spectrum identification"* — is **exactly
right, and the primary source agrees with it.** Nothing here upgrades a candidate to a spectrum.

### And a finding for *their* open item, which they did not ask for

Their list of what remains includes: *"the three-spinor spectrum leaves an anomalous extra
`U(1)`."* **That `U(1)` is structural to the Acharya–Witten construction, not an artefact of
their realization.** The construction requires a simply-laced `Ĝ` of rank one more than `G`,
containing `G × U(1)`, whose Lie algebra decomposes as

```
ĝ  =  g ⊕ o ⊕ r ⊕ r̄
```

where **`o` is the `U(1)`** and **`r` transforms as `R` under `G` with charge 1 under that
`U(1)`**. AW then note for `SO(2k)` that although `2k` is a real representation, *"the massless
`2k`'s obtained from the construction are charged under the `U(1)`; under `SO(2k) × U(1)` the
representation is complex"* — **the charge is what makes the spectrum chiral at all.**

> **The extra `U(1)` is not a defect to be removed. It is the mechanism.** Any completion has to
> live with it, for every `G/Ĝ` pair including `E₇ → E₆`. That locates their open item rather
> than solving it, and it says a completion that works by *deleting* the `U(1)` is deleting the
> source of the chirality.

## 2. `arXiv:1809.10148` — memo 191's input confirmed at source, three ways

| | checked | result |
|---|---|---|
| the central charge | GM §10.2's `c = 13 − 6(p + 1/p)` vs **CCFGH eq (3.9)** `c = 1 − 6(1−p)²/p` | **identical**, verified symbolically |
| the shape | **eq (5.7)**: `χ(M_{1,s}; τ) = Ψ_{p,p−s}(τ) / η(τ)` | **the character IS a false theta over `η`** — exactly the shape memo 191 measured, now from the source |
| the normalisation | **eq (5.8)**: `Z^{(unred)}_a(q) = Z_a(q)/(q;q)_∞` | **third independent confirmation** of GM Remark 3.8 / GPV (6.50) |
| the parameter | **Table 3**: `Σ(2,3,5) ↔ 30+6,10,15 ↔ M_{1,1}⊕M_{1,11}⊕M_{1,19}⊕M_{1,29}` | `p = 30`, **exactly what memo 191 used** |

**Memo 191's `c_eff = 1` now has an exact structural reason rather than a measured one:** the
singlet character is `Ψ/η`, and `η` supplies the `1`. Nothing in memo 191 is withdrawn.

## 3. **But §5.2 partially reopens what memo 191 §3(b) closed — and this must be said plainly**

Memo 191 concluded that `c_eff = 6` is *"not reachable by choosing a different 3-manifold in this
family"*, because `Ẑ^unred = (false theta)/(q)_∞` forces `1`. **That conclusion was measured on
Brieskorn spheres.** CCFGH **§5.2, "Hyperbolic `M₃` and non-`C₂`-cofinite log-VOAs"**, says the
hyperbolic case is a *different class*:

> *"hyperbolic 3-manifolds have at least one `SL(2,C)` flat connection `α_geom` … such that
> `Im CS(α_geom) ≠ 0`. This necessarily violates the condition (5.12) and … we expect hyperbolic
> 3-manifolds to be related to logarithmic vertex algebras which are **not `C₂`-cofinite**."*

with Miyamoto's theorem behind it: **a `C₂`-cofinite VOA has all conformal dimensions and central
charge rational.** They even suggest the condition deserves the name *"`C₂`-cofiniteness for
3-manifolds."*

> **So the `(false theta)/(q)_∞` shape — and with it memo 191's `c_eff = 1` — is established for
> the class where the `(1,p)` singlet applies, and the primary source expects hyperbolic
> manifolds to lie OUTSIDE that class.** Memo 191 §3(b)'s *"answered, negatively, and
> structurally"* must be read as **answered for the rational-`CS`, `C₂`-cofinite family**, not for
> `m004`.

**This is a partial reopening of the door memo 191 closed, and it comes from the source memo 191
was resting on.** It does not restore the `c_eff = 6` hope — nothing here says `6` is reachable —
but it removes the claim that the obstruction is general.

**And it makes Q11's third question sharper still.** CCFGH's own open list includes: *"It would be
interesting to compute … the q-series invariants `Z_a(M₃)` for hyperbolic 3-manifolds and test the
conjecture in §5, namely whether in such cases `Z_a(M₃)` are related to characters of logarithmic
vertex algebras which are not `C₂`-cofinite."* **That is Q11's question, asked by the authors, and
listed by them as open.**

## 4. Where this leaves the two lanes

* **The other seat**: their E₇→E₆ correction is confirmed; the topology caveat and the structural
  `U(1)` are relayed as findings, not as objections.
* **This lane**: memo 191's inputs are confirmed at source; memo 191 §3(b)'s scope is narrowed to
  the `C₂`-cofinite family; and the hyperbolic case is now known to be **open in the literature,
  named as open by the authors themselves, in two separate papers** (GM §10.2 and CCFGH §5.2 + §9).

## 5. Named follow-up

**F192-1.** CCFGH §5.2's condition (5.12) is checkable on `m004` from data this bench already
holds — `Im CS(α_geom) ≠ 0` is the complex volume. Confirming it puts `m004` explicitly in the
non-`C₂`-cofinite class rather than by expectation, and that is the first step of any honest
answer to Q11(c) from this side.
