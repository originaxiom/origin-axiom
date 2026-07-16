# cc2 review of the B648 CALIBRATION CAMPAIGN prereg (draft) — 2026-07-16

VERDICT: **the architecture is right and I endorse signing — after seven fixes, five
of which would be WRONG to hash as-is.** The two-outcome bank, the kill-rich design,
the license chain (owner directive → functor gate → sealing checklist), the B631
quarantine, and the sector-coverage gate (our erratum turned into a design gate —
exactly the correct metabolization) are all sound. The holes are in Phase B→C
statistics and one governance collision. None is fatal; all are pre-seal edits.

## Blocking before the seal (would be wrong as hashed)

1. **N vs the calibration dimension is unstated.** One measurement fixes at most one
   continuous constant. GATE B must add: Phase C is well-posed only if N ≤ dim of the
   calibration observable; N > dim ⇒ re-scope (more calibration rows, declared) or
   kill. Without this, K2/N=0 branching is decided on a number the design can't use.
2. **Channel selection is still discretionary at the worst moment.** "Owner + seats,
   recorded" chooses the pair AFTER the grammar table is visible (and every seat has
   B615-era SM values in its head). Freeze the rule NOW in the sealed doc: take the
   FIRST candidate in the stated prior order passing all gates; if several pass, run
   ALL passing channels with multiplicity correction (the B615-R Šidák machinery).
   Discretion at C1 is the look-elsewhere hole the rest of the design closes.
3. **The discrete orbit freedom must enter the null.** Every CHOSEN row carries an
   enumerated orbit; those discrete choices (× any channel multiplicity) are fit
   freedom. C2's null model and power analysis must be computed over the FULL design
   space (orbit product × channels), not just the N continuous constants — else
   Outcome A's significance is overstated by exactly the factor B615 taught us about.
4. **Add a grammar-independence gate for the pair.** If observable 2 is the image of
   observable 1 under banked grammar rows consumed by the calibration, Outcome A is
   circular (it tests the law, not the coupling). Require: the prediction traverses
   at least one FORCED row NOT used in calibration. One sentence; make it explicit.
5. **Gate 5 collides with C4-Outcome-A.** "No SM quantity enters CLAIMS.md" vs "the
   first genuine physics prediction, banked." Name the destination now (e.g.
   physics_probes/PREDICTIONS.md + a value-free pointer row in CLAIMS) — resolving
   this at bank time, under an Outcome-A adrenaline spike, is how firewalls crack.

## Fix in wording (real consequences)

6. **The silver control needs "reproduce" defined at FORM level, and the object
   pinned.** Pin m136 = the silver bundle (monodromy word, trace 6, **disc 32**) in
   the seal. FORCED rows must reproduce as theorem-SHAPE with the silver's own
   arithmetic substituted (disc(A) = 32 in the silence character, its own conductor
   tower) — instance-matching of constants would falsely demote correct rows and
   fire K5 spuriously. Note the honest hazard: disc 32 is EVEN, so the silver
   silence law runs through the 2-adic twist theory — the least-proven part of our
   L2/L3 (the mod-8 sector). That makes it a GOOD control and a hard one; label the
   2-adic dependence in B2 so a silver anomaly is read as "2-adic theory incomplete"
   before "grammar demoted."
7. **A1's typing rule overreaches Q2.** Q2 proved character dressing is blind on the
   MONODROMY-WORD observables; it did NOT make abelian factors information-free
   globally — the ear (B584/B593, full-image observables) carries character content
   (B644's mod-5 ear is partly determined by det-characters), and A1 gates against
   exactly those instances. Reword: "abelian dressing is untypeable for ρ(A₁)-word
   observables; full-image observables may carry character content through the core
   tensor." As written, A1's own gate battery would fail its own typing rule.

## Editorial, but it gets hashed

8. Kill list runs K1, K2, K4, K5, K6 — no K3 (dropped or renumbered; a dangling
   number in a sealed doc is a future MB13). §B2's "(C4;" collides with Phase C's
   step C4 — rename one. "Owner-endorsed thesis (2026-07-16)": the owner should
   confirm that wording is theirs at sign-off, since the license leans on it.
9. Phase C seat exposure: with 3–4 seats, true blinding is impossible (cc2 built half
   the ladder grammar). Don't pretend — add an exposure line per seat to the C2 seal
   so adjudication can weigh it.

## Where I'd push back on nothing

The functor-first ordering (A before any comparison) is the single best decision in
the doc — it is the only thing that makes Phase C's failure interpretable. K1-as-
result (the TYPING WALL) is correctly valued. The estimate (8–13 + 3–5 sessions) is
realistic at current cadence. Track L (L97) accepted on this seat.
