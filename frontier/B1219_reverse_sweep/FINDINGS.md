# B1219 — CELL 0, THE REVERSE SWEEP: the direction the first instrument could not see, and three homonym traps declined

**Status: banked (frontier). Verdict PROVED** (the instrument, with a bite control that cannot go
stale; 45 off-surface arcs triaged; the campaign's gate discharged). **Cell 0 of the publication
campaign, which gates Cells 1–3.** `verification/reproduce.sh` → `REPRODUCES`. Gate 5 clean.

## Why the other direction was needed

`open_claim_sweep.py` (B1218) runs **surfaces → arcs**: it takes a claim of openness and asks
whether a settled arc already decided it. That direction **structurally cannot** find a banked
result that no surface mentions at all — there is no claim to match against. B1188 measured that
population; B985 measured the bias producing it (object-faces recover 79–100%, relation-faces
6–19%). This asks the other question of every settled arc: **does any live surface carry it?**

## Two failures of my own, both instructive, both fixed

**1. The first run returned ZERO off-surface arcs**, against B1188's known 132. The instrument was
wrong, not the corpus. `views/VERDICT_LEDGER.md` (1180 arcs), `THE_SPINE.md` (979) and
`CLOSED_DOORS.md` (528) are **generated per-arc enumerations** — every arc is in them by
construction, so counting that as "surfaced" makes the measurement return zero *by definition*.
**Being in a database dump is not being on a surface.** This is B1218's own tautology rule, which I
had applied once and failed to carry over.

**2. The positive control failed 0/5 — and the CONTROL was stale, not the instrument.** B1188's
five sharpest off-surface arcs (B279, B769, B786, B293, B552) did not flag. Diagnosis before
concluding anything: **all five are cited in `docs/GRAND_COMPUTATION_LEDGER.md` — which is B1188's
own remedy.** B1188 found them off-surface and then surfaced them there. The control was testing a
condition the corpus had since repaired.

> *That is the fix working, and it is the strongest evidence in this arc that the E53 programme is
> not theatre.*
>
> **Methodological note, because "the control must be wrong" is exactly how a broken instrument
> gets waved through:** this was not concluded on plausibility. It was concluded only after
> locating *which* surface cites each of the five and confirming it is a genuine thinking surface.

**3. The instrument was NON-DETERMINISTIC, and that was caught before it banked.** Two runs of
the same file over the same tree returned **45 and 46**. In-process it was perfectly stable (six
consecutive calls identical), so the variation was *between* processes: `toks()` returns a **set**,
and the score truncates to the twelve highest-IDF terms — so whenever terms tie on IDF, *which*
twelve survive depends on set iteration order, which Python randomises per process via
`PYTHONHASHSEED`. Fixed by breaking ties on the term itself. Five separate processes now agree
exactly. **A verifier that does not reproduce is worthless** — this is E52's own class (the
instrument ran and was wrong while its verdict stood), caught here by re-running rather than by
care. The same latent tie-break was hardened in B1218, where it affected only displayed terms
because that score sums over *all* shared terms rather than a truncation.

## The control that cannot go stale (planted targets)

A control keyed to named arcs decays as those arcs get surfaced. So the control is **planted**, in
the form codex's R028 certificate uses:

| plant | expectation | result |
|---|---|---|
| **A** — settled, object-facing claim whose vocabulary occurs on no surface (invented terms) | MUST flag | **flagged**, cover **0.42** |
| **B** — settled claim copied verbatim from a heavily-surfaced document | must NOT flag | **not flagged**, cover **1.00** |

Standing negative also holds: **B1141 and B1170**, demonstrably well-surfaced, do not flag.

*Stated honestly:* separation is 0.42 vs 1.00 with the bar at 0.55 — real, but **the bar is a
judgement, not a derived constant.** Ordinary English vocabulary is why a nonsense claim still
covers 42%.

## The result

**1032 settled arcs scanned → 45 off-surface**: **29 SURFACE-IT**, 10 INTERNAL (instrument arcs an
object-facing surface is right to omit), 6 SUPERSEDED (a later arc's text owns the result).

**Against the pre-registered expectation** (in `docs/PUBLICATION_CAMPAIGN.md`, written before the
run: *40–90 genuinely off-surface, at least one bearing on Cells 1–3*): **45 — inside the range, at
its low end.** Well below B1188's 132 for a reason this arc can name: much of that 132 was surfaced
into `GRAND_COMPUTATION_LEDGER.md` as B1188's remedy, and this sweep additionally clears any arc
whose *content* is carried even when its id is not cited. **45 is the residue after the previous
repair, not a contradiction of it.**

## THE GATE VERDICT — Cells 1–3 are NOT blocked

**No banked work was found that changes the design of Cell 1 (λ's gate), Cell 2 (the ℙ³
exhaustion) or Cell 3 (B632's symmetric texture).**

**Three homonym traps found and declined** — each looked like a hit on a cell and is not:

- **B603** *"weight purity … all single-generator L1 contractions are weight-forced"* — a
  **Lie-algebra grading weight**, not λ's **von Neumann weight** completing the tracial core.
- **B26** *"the proposed period-3 derivation of λ/h = 1 fails"* — λ here is a ratio in the
  **Fibonacci trace map's** period-3 orbit, not the type III_λ modular parameter.
- **B551** *"the species word is neither a coloring of the Fibonacci word nor Sturmian"* — the
  **species** word (complexity ≈3n), not the chain's **golden** word (Sturmian, n+1).

> Declining these is the arc's real product. Any one, taken on its name, would have redirected a
> cell onto a different object — the precise error the paper's own method section forbids.

## Two findings worth surfacing on their own merits

- **B551 CORROBORATES the paper's new §3** rather than threatening it: *"no rotation/winding
  mechanism can emit"* the ℚ(√φ) layer, which **requires substitutive inflation order** — exactly
  the substitution framing §3 uses for the entrance links. A negative about a neighbouring object
  that strengthens ours.
- **B342** (the object's ℤ/3 is the standard trimaximal symmetry; its TM2 prediction disfavoured)
  belongs on the **value-negative record** and **must never enter the paper** — it carries a
  measured comparison, and Gate 5 governs.

## Scope, honestly

The sweep reads the surfaces named in `SURFACES` and decides by citation plus lexical content
coverage. It cannot find a result whose vocabulary is wholly disjoint from every phrasing on a
surface, it does not adjudicate, and the bar is a judgement. All 29 were read; three were pursued
to their arcs and decided by hand. **The remaining 26 are triaged, not adjudicated** — surfacing
them is R53-3's continuing work, not this cell's claim.
