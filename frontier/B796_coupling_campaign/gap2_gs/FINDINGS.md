# GAP 2 — the Green–Schwarz sweep, and a correction to my own tension

cc3, 2026-08-10. Gate 5-Q. Structure only.

## The sweep result: the corpus has nothing

Searched `frontier/*/*.md` and `docs/*.md` on `origin/main`:

| term | files |
|---|---|
| axion | **0** |
| 2-form / two-form / B-field | **0** |
| anomaly inflow | **0** |
| Stückelberg | **0** |
| F ∧ F | **0** |
| *(control)* Chern–Simons | **75** |

**Zero Green–Schwarz-adjacent material, against 75 files on Chern–Simons.** So
the answer to *"would repo research help?"* is **no, for finding an existing
treatment.** It is genuinely absent — not hidden under other vocabulary, which
was the specific reason I expected a hit.

## And my "live tension" was a conflation — withdrawn

I flagged, as gap 2's opening question, that *"the object has CS = 0 exactly, so
the same property giving θ_QCD = 0 may forbid the mechanism removing the
anomalous U(1)s."* **That is a category confusion and I withdraw it.**

The 75 files make the distinction plain. The corpus's Chern–Simons object is the
**invariant of the 3-manifold** — a *number*:

> *"the Chern–Simons invariant of `RᵐLᵐ` is identically 0"*
> *"a pure element of ℂ/4π²ℤ entering the 3d–3d partition function **only** as a
> dimensionless exponent"*

Green–Schwarz needs a **4d action term** — an axion coupling `a·tr(F∧F)` with a
shift symmetry. **A number that vanishes and a term in a Lagrangian are different
objects.** CS(M) = 0 does not obstruct GS, and I should not have suggested it
did. The check I called "the first thing to do" was worth doing precisely because
it dissolved my own framing rather than confirming it.

*(What would be a real connection: 3d–3d, where the 3-manifold's data determines
the 4d theory, so CS data could feed in. That is a construction question, not the
identity I implied, and it is not addressed anywhere in the corpus either.)*

## What this leaves, exactly

**Gap 2 is genuinely unaddressed, and the repo cannot help.** The framework uses
*"an anomalous U(1) cannot be gauged"* as a **selection principle** — a statement
about which subgroup *is* the gauge group. Physics has a **mechanism** for the
same fact. **The corpus has the selection principle and not the mechanism, and
nothing in it bears on the difference.**

Whether that matters depends on a question the campaign can now state cleanly:

> **Is "anomalous ⟹ not gauged" legitimate as a selection principle, or does it
> require a mechanism that removes the anomalous factors from the spectrum?**

- **If legitimate**, gap 2 closes with a citation and a scope note, and the rank
  resolution stands as it is.
- **If a mechanism is required**, the framework needs GS-like structure it has
  never looked for, and that is a genuine new obligation — the first one this
  campaign has generated rather than discharged.

**This is a literature question, not a repo question.** It is standard material
(anomalous U(1)s in GUT and string constructions), it is well-posed, and it is
the only item in the campaign that cannot be settled from inside the corpus.

## Recommendation

**Do not compute here.** The next step is a bounded literature read on anomalous
U(1)s — specifically whether "not gaugeable" is used in the field as a selection
principle or always accompanied by a removal mechanism — and then one scope note
in the ledger either way.

**And record the negative:** the sweep itself is worth banking. *"The corpus
contains no Green–Schwarz material"* is a fact a future seat should not have to
rediscover, and the 75-file Chern–Simons control is what makes the absence
meaningful rather than an artefact of searching the wrong words.

---

# THE LITERATURE READ — the answer is the second branch

Run 2026-08-10 on the owner's go. **This is the only item in the campaign that
could not be settled from inside the corpus.**

## The question, as posed

> Is *"an anomalous U(1) cannot be gauged"* legitimate as a **selection
> principle**, or does removing an anomalous U(1) require a **mechanism**?

## The literature says: a mechanism, and it is standard

**Anomalous U(1)s are not simply "not gauged". They are gauged, the anomaly is
cancelled by Green–Schwarz, and the gauge boson becomes MASSIVE:**

- *"The anomaly is cancelled via a generalization of the Green–Schwarz
  mechanism."*
- *"In addition to canceling the anomaly, the Green–Schwarz mechanism will give a
  **mass for the U(1) vector superfield**."*
- *"A necessary consequence in four dimensions is that the (quasi)anomalous gauge
  symmetry is **broken**."*
- *"The **B∧F coupling** has the effect of rendering massive the corresponding
  pseudoanomalous U(1), and **all** pseudoanomalous U(1)'s in D=4 string
  compactifications become massive in this way."*
- and the U(1) *"may survive as a **global** rather than a local symmetry."*

**So the standard treatment is a four-step process** — gauge it, cancel by GS,
eat the axion, survive as global — **and every step needs structure the corpus
does not have: an axion, a 2-form, a B∧F coupling. All three sweep to zero.**

## The nuance, recorded because it is real and cuts slightly the other way

The conventional "gauge anomalies must cancel or the theory is inconsistent" is
itself qualified in the literature:

> *"According to conventional wisdom, gauge anomalies are a sign of
> inconsistency and must necessarily cancel… but it is an **oversimplified**
> point of view. What is important is not whether a gauge symmetry is
> represented trivially or not, but whether the resulting quantum theory is
> **unitary**."*

with the chiral Schwinger model (Jackiw–Rajaraman) and the subcritical string as
worked counterexamples. **So "anomalous ⟹ inconsistent" is not absolute.** It
remains the working rule for four-dimensional chiral gauge theories, and no
source suggests the framework's usage is covered by the exceptions — but the
exceptions exist and an honest ledger should not overstate the obligation.

## Verdict on gap 2

**The framework's usage is not the standard one, and the gap is real.**

| | |
|---|---|
| **the framework** | *"an anomalous U(1) cannot be gauged"* → used to **select** which subgroup is the gauge group |
| **the literature** | the U(1) **is** gauged; GS cancels the anomaly; the boson becomes **massive**; it survives as a **global** symmetry |

These differ in a way that matters for this campaign specifically. The
framework's rank resolution (Phase 2b) reads: *chiral matter ⟹ two u(1)s
anomalous ⟹ not gaugeable ⟹ rank 4.* The literature's version reads: *chiral
matter ⟹ two u(1)s anomalous ⟹ **GS makes them massive** ⟹ rank 4 **at low
energy**, with two massive Z′s and two global symmetries.*

**The conclusion — rank 4 — survives. The route does not.** And the literature's
route predicts **objects**: two massive gauge bosons and two global U(1)s. The
framework's route predicts nothing, because it removes the factors by
definition rather than by dynamics.

## The obligation this creates — the campaign's first

1. **The framework needs GS-like structure** (axion / 2-form / B∧F) or an
   argument that its situation falls under the unitarity exceptions. **It has
   neither, and has never looked.**
2. **Scope note owed on Phase 2b.** The rank resolution should read *"rank 4
   given the chiral truncation **and** a removal mechanism for the anomalous
   factors, which the framework does not supply"* — not *"rank 4 given the
   chiral truncation."*
3. **A prediction is available if the structure is found.** Two massive Z′s is
   a physical consequence, and the programme has almost no consequences of that
   kind. **This is the one place today's work points at something observable**,
   and it is exactly where the firewall discipline applies: it would need a
   sealed prereg before any mass is estimated, and the weight ledger says the
   framework cannot supply the scale anyway.

## Honest summary

Gap 1 was already counted and now has a name. **Gap 2 is real, is external, and
the campaign generated it rather than discharging it** — which is the correct
outcome for the one question that had to leave the corpus to be answered.

Sources: the GS/massive-U(1) statements are standard across the string
phenomenology literature (Type I vacua, heterotic orbifolds, D-brane models);
the unitarity qualification is from Bilal's *Lectures on Anomalies* and the
chiral-Schwinger-model line.
