# B951 — L132 SCOUTED BEFORE COMPUTING: the cell is at high risk of vacuity, and its "arrival" half is textbook

**Date:** 2026-08-08 · **Seat:** cc (banking), from an adversarial scouting panel.
**Lane:** MATHEMATICS. Gate 5 untouched.
**Why:** the `seal-provenance` gate now requires a design-time prior-art grep. This is that
grep, run at literature scale, **before** L132 computes anything.

---

## The verdict

**L132 as posed would have produced a vacuous check and a textbook result.** Scouting cost
one panel; computing first would have cost a day and banked a rediscovery.

## 1. The anomaly check is probably VACUOUS — and that is now L132's real gate

**E₆ has no symmetrised third-order Casimir, so it is anomaly-free as a gauge group**
(Okubo 1977 names it explicitly). The panel computed all conditions on a complete **27**:
13 U(1) cubic/mixed/gravitational conditions, both [SU(3)]²U(1) and [SU(2)]²U(1) for all
three u(1)s, and the Witten parity (6 doublets, even). **Every one vanishes identically.**

> **If the object's charges form complete 27s, the anomaly check CANNOT FAIL.**

Per **MB12** (the programme's own vacuity rule: check the criterion can pass *and* can
fail), **establishing non-vacuity is the prerequisite, not the result.** It is cheap: does
the object's spectrum form complete 27s? If it does not, anomaly cancellation becomes a
real constraint and is informative. If it does, there is nothing to test.

## 2. The target algebra is CLASSIFIED STRUCTURE — verified here independently

The panel identifies `su(3)⊕su(2)⊕u(1)³` as exactly the **A₂+A₁ Levi subalgebra of e₆**.
**Re-derived on this bench rather than accepted:**

> A Levi from a node subset S is `h ⊕ (roots in span S)`. For A₂+A₁: 6 + 2 = **8 roots**.
> dim = rank + roots = 6 + 8 = **14**. Semisimple part su(3)⊕su(2) = **11**.
> Centre = rank − |S| = 6 − 3 = **3**.
>
> **dim 14, derived 11, centre 3 — exactly B892's three numbers.**

Borel–de Siebenthal (1949) / Dynkin (1952). **So arriving at su(3)⊕su(2)⊕u(1)³ from E₆ is
not a discovery.** This deflates B892's headline a second time: B950 corrected "the
Standard Model algebra" (it is dim 14, not 12); this arc adds that the thing arrived at is
a *classified* Levi, catalogued 77 years ago.

**What survives of B892 is the route, not the destination** — that the object's own
superselection charges pick out *this* Levi. Whether that route is novel is a separate
question from whether the endpoint is.

## 3. The centralizer argument for Y does NOT transplant from su(5) to e₆

| ambient | centralizer of su(3)⊕su(2) | consequence |
|---|---|---|
| **su(5)** | **1-dimensional** | this *is* the Georgi–Glashow textbook definition of hypercharge |
| **e₆** | **9-dimensional** (su(3)⊕u(1)) | "the u(1) commuting with colour and isospin" **does not single out Y** |

So an extra input is required to identify Y in E₆ — and in the literature it is **always**
the choice of the SU(5)/SO(10) subgroup. **That choice IS the identification.**

## 4. Q1's forcing is much weaker than the folklore

- **Minahan–Ramond–Warner**: anomalies alone give **two** hypercharge solutions.
- **Babu–Mohapatra**: quantisation follows only if ν is **Majorana**.
- **Foot–Lew–Volkas**, decisively: charge **de-quantises in the three-generation SM with
  massless neutrinos** — the forcing is a **one-generation** statement.
- **Lohitsiri–Tong** recast it as x³+y³=z³ but **assume** Y is quantised.
- Anomaly conditions are **homogeneous**, so they can **never** fix Y's normalisation —
  only ratios.

**B950's ledger said "the hypercharges are the SM's only computed value-level structure".
That stands, but it must be qualified**: forced *up to normalisation*, *per generation*,
and *given assumptions the object may not supply*.

## 5. Q3 — IT HAS BEEN DONE, and close to home

> **Todorov, JHEP 04 (2021) 164 — "Superselection of the weak hypercharge…"**, verbatim:
> *"we promote the exactly conserved weak hypercharge to a superselection rule: Y commutes
> with all observables and all symmetry transformations… the centralizer of Y in so(10) is
> g = u(2) ⊕ u(3)."*

That is `su(3)⊕su(2)⊕u(1)⊕u(1)` — **the SM algebra plus one extra abelian factor, from a
centralizer construction.** Structurally **L132's own move**, one u(1) short, in so(10)
rather than e₆. Also: **Krasnov 2021** gives a commutant characterisation of all of G_SM;
**Todorov–Dubois-Violette** derive the SM symmetry from **J₃(𝕆)** via Borel–de Siebenthal —
and this programme's own build **is** M(𝕆,ℂ) (P70/B904). **The octonionic-Jordan route to
the SM is occupied literature.**

## 6. What L132 could honestly claim, if run

Only two things:

1. **A stated-in-advance principle** selecting which u(1) is hypercharge *from the object's
   own measurement structure* — and meaningful **only if fixed before looking at which
   combination gives the right answer**, else it is postdiction.
2. **If the spectrum does NOT form complete 27s**, anomaly cancellation becomes a genuine
   constraint and the result is informative.

Everything else is **reproduced**, never predicted. Named traps: do not claim Y's
normalisation; do not claim "hypercharge falls out" if an SU(5)/SO(10) subgroup was chosen
— **including implicitly by reading standard branching tables, since that choice *is* the
identification**; do not treat commutant-derivation-of-Y as a novel genre.

## 7. The panel's own honesty caveat, carried

**Control passed** before any null was trusted (Geng–Marshak PRD 39 (1989) 693 retrieved,
all 170 citing works enumerated; the E₆ vocabulary surfaced by citation weight —
London–Rosner, Hewett–Rizzo, Langacker, Slansky). Databases reached: INSPIRE-HEP (primary),
arXiv, ar5iv full text, OpenAlex, zbMATH. **MathSciNet NOT reached** (302 auth wall) — no
claim rests on it. **The Q3 null is NOT certified**: the octonion/Jordan literature is
large, fast-moving and partly outside INSPIRE's core indexing. Read it as *"not found by
this sweep"*, never *"does not exist"*.

---

**Verdict: L132 AMENDED, not run.** Its non-vacuity gate is now the prerequisite; its
"arrival" half is classified structure; its centralizer argument does not transplant; and
its nearest prior art (Todorov 2021) does structurally the same move one algebra down. The
scouting cost one panel and saved a rediscovery — which is the entire point of the
`seal-provenance` gate adopted hours earlier.
