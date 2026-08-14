# B869 — G4 closed: the false-positive control PASSES — the cascade rule is not an SM-generator, and the SM endpoint is jointly caused by the rule AND the 27's content class

cc banking seat, 2026-08-03. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — a control arc in the referee queue; its footing is exact finite
computations with two-outcome endpoint claims, run by ONE generic engine with no per-start
hand-tuning.

## 0. The critic's question

If the selection principle (B861: maximal residual symmetry among registerable options) lands on
the SM from *any* start, then "E₆ → SM" carries no information about E₆ and the derivation is
vacuous. G4 demanded the control: run the same rule from other starts and count endpoints.

## 1. The engine

One uniform machine. su(n) content lives in exterior-power labels: Λᵖ(V)* ≅ Λⁿ⁻ᵖ(V) for SU(n),
so conjugation is p ↦ n−p and branching under s(u(k)+u(n−k)) is Λᵖ → ⊕ₐ Λᵃ⊗Λᵖ⁻ᵃ — no special
cases. Sym² labels added for the negative control; D-type entries carry Borel–de Siebenthal menus
and spinor branch tables. **A canonicalization bug was caught by the E6 run itself**: Λⁿ(n) and
Λ⁰(n) are the same trivial rep but distinct labels, so uncanonicalized conjugation manufactured
spurious chirality out of singlets and the chain overshot the SM. Fixed at the label-creation
layer; the banked chain then reproduced exactly.

**The engine re-derives every banked verdict internally** (consistency, not new content):
- B859's repair: at the so(10) node, so(8)×u(1) is **top-dim (30) and NOT registerable** — the
  option that broke the handoff's cascade dies by chirality, not conformality.
- B861 step 2/3: Pati–Salam registerable but loses on dim; **su(4)×u(1) top-dim (18) and dead**.
- B863's termination: at su(3)+su(2), **both** descents non-registerable — terminal.
- B861's chain: E6 → so(10)+u(1) → su(5)+2u(1) → su(3)+su(2)+3u(1). Exact.

## 2. Cell 1 — eligibility census (all simple starts, rank ≤ 8)

**21 of 31 die at step 0**: −1 ∈ W ⟹ every rep self-conjugate ⟹ no chiral generation *exists*
(A₁, all B, all C, D-even, G₂, F₄, **E₇, E₈**). Eligible: A₂–A₈, D₅, D₇, **E₆** — E₆ is the
**unique exceptional chiral start**, full stop.

## 3. Cell 2 — endpoint census

| start | generation | endpoint |
|---|---|---|
| su(5) | 10 ⊕ 5̄ (Georgi) | **SM core** + 1 u(1) |
| su(6) | 15 ⊕ 2·6̄ | **SM core** + 2 u(1) |
| su(7) | 21 ⊕ 3·7̄ | **SM core** + 3 u(1) |
| su(8) | 28 ⊕ 4·8̄ | **SM core** + 4 u(1) |
| so(10) | 16 | **SM core** + 2 u(1) |
| E₆ | 27 | **SM core** + 3 u(1) |
| **so(14)** | 64 | su(3)+su(2)+**su(2)** + 3 u(1) — **NOT the SM** |
| **su(6), Sym² family** | 21 ⊕ 10·6̄ | su(3) + 3 u(1) — **no weak sector at all** |

The A-chain starts funnel one rung at a time (su(8)→su(7)→su(6)→su(5)→SM): each Λ²-family is the
next one down plus vector-like padding, which the registerability strip discards. **Prior art,
named:** this is Georgi's SU(N) family reduction (1979, *Towards a grand unified theory of
flavor*) and the survival hypothesis (vector-like pairs decouple) — the registerability criterion
is a theorem-form of it, and the funnel is *expected*, not a discovery of this arc.

**The two controls do the G4 work:**
- **so(14)**: the rule protects an extra su(2) to the end (maximal residual symmetry strips one
  so(4) factor but the surviving su(2) rides the chiral content down). Endpoint SM×su(2) ≠ SM.
- **Sym² family**: same algebra as a funneling start (su(6)), different content class — lands on
  su(3)+dials, **no su(2)**. The rule can output a world with color and no weak interaction.

## 4. Verdict — and what it reclassifies

**G4 PASSES: the machinery is not an SM-generator regardless of input.** The endpoint depends on
the start (so(14)) and on the generation's content class (Sym²). What IS robust: **every
Λ²-type/spinorial family start funnels to the SM core** — the 27's own class.

So the claim decomposes, and the decomposition is the honest shape of the flagship:
1. **object → E₆ ⊕ 27** — object-specific, banked elsewhere (the fold; the atom; E20/B727), NOT
   established by the cascade;
2. **27-content + registerability → SM** — this cascade, robust within the 27's content class,
   with the Georgi funnel as prior art and the two controls as the non-vacuity certificate.

The cascade never selected E₆ and never needed to. The false-positive worry dissolves because the
rule provably does not output the SM universally — and the choice it *cannot* make (which
generation content) is exactly the choice the object makes (the 27), which is the point.

**One echo, locked:** the E₆ endpoint carries exactly **3 u(1)s** — B864's ledger: hypercharge Y
(the unique gaugeable direction) plus the two anomalous dials ψ, χ. The engine's dial count and
the anomaly ledger's agree.

## 5. What this arc does NOT establish

- The canonical-family choice for A-starts (minimal anomaly-free chiral set from ≤2-index irreps)
  is an input; A₂/A₃/A₄ have no such family (Λ² self-dual or under-sized) and are excluded from
  Cell 2 — eligible at step 0, untested beyond it. Other exotic families untested.
- Menu completeness (P5) is still the cascade's external import — this arc inherits it.
- Nothing here reaches values, three-ness, or the real form. Gate 5 untouched.

`tests/test_b869_false_positive.py`
