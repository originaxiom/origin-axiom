# Origin Axiom — Method: verification without blindness

Governed by `GOVERNANCE.md` (the constitution). This is its **generative peer**: `GOVERNANCE.md` keeps us from
claiming too much; `METHOD.md` keeps us from *seeing* too little. The two are a complementary pair, like the
C/K guardrails (`GOVERNANCE §6.1`).

## The problem this fixes

The verification discipline is deflationary by design — verify-don't-trust, the HELD rule, null tests, the
one-way firewall, the MB6–MB12 guards, "dead is permanent." Pushed hard at the wrong moment it kills **hints,
bigger pictures, and new questions before they can grow** — a hint at birth looks like an overclaim. The repo's
machinery was asymmetric: ~6 institutionalized artifacts for rigor, **one** thin artifact for generativity
(`docs/OPEN_LEADS.md`, which admits only *decisions to run*). So the program was structurally biased toward
**false negatives**. `GOVERNANCE §6.1 (C)` already names half of this: "declaring victory-by-exhaustion …
silently kills live leads."

**The symmetric failure modes:**
- **over-verify → false negatives** (blind to real structure; an unearned "no").
- **over-generate → false positives** (numerology; an unearned "yes").

A healthy program sits *between* them. The fix is not to verify less — it is to verify **at the right stage**.

## The resolution: staged rigor

Rigor attaches at **promotion**, not at **birth**. A hint is recorded before it is judged. The heavy adversarial
battery is **forbidden before promotion and forbidden to skip at promotion**.

```
   observation ─► NOTICED ─► CHECKED ─┬─► PROMOTED   (to an OPEN_LEADS L#, or a candidate claim)
   (record it)   (H# + 1 line) (cheap) ├─► DORMANT   (cheap check inconclusive — parked, revivable)
                                       └─► KILLED    (ONLY via the full promotion gate → tombstone + residual-hint)
```

**Rigor is verdict-typed, not kill-typed, before promotion** (the load-bearing rule — without it "checked"
silently becomes "judged early"):

| stage | rigor tool that attaches | what a *negative* may do here |
|---|---|---|
| **NOTICED** (raw → registered in `docs/HINT_LEDGER.md`) | none — record-only | nothing; **a hint cannot be killed at birth** |
| **CHECKED** (one cheap sanity run) | a single reproduce/sanity pass + the MB8 null-case glance + MB12 vacuity glance | set a **diagnostic flag** only (`generic?`/`vacuous?`/`non-reproducing?`); route to **DORMANT**, never KILLED |
| **PROMOTED** (the real gate) | the full battery: multi-method cross-check + adversarial/refutation + independent recompute + null test + MB6 control + MB10/MB11 level-check + state-twice + the `GOVERNANCE §6` red-team lens + the HELD rule | *now* a negative is a first-class `TESTED-NEGATIVE` and may route to KILLED/tombstone |
| **VERIFIED → banked** | the existing `conditional → proven` gate + finding tiers + the `CLAIMS.md` code+test+doc triple | unchanged — the constitution governs |

Two corollaries:
- **The null result is also a hint.** Every `TESTED-NEGATIVE` carries a mandatory `residual-hint:` field and is
  re-entered as NOTICED before tombstoning. *(Worked precedent: B225's "2 = octahedral parent" was refuted **into**
  "prime 2 is universal to 2-bridge character varieties" — a stronger true statement born from a kill.)*
- **DORMANT is the pressure valve.** A failed *cheap* check parks a hint DORMANT (revivable); only the *full gate*
  produces DEAD. This stops the "checked → killed" leak.

**Generativity is added strictly *under* the existing rigor floor — never by lowering it.** The promotion gate
(HELD / null test / `→ proven`) is untouched.

## The seven anti-blindness rules

The generative twin of the anti-overclaim glossary (`GOVERNANCE §8`):

1. **Record before you judge** — a noticed hint gets an `H#` (in `docs/HINT_LEDGER.md`) *before* any assessment.
2. **Kill at promotion, not at birth** — only the full gate may produce KILLED; cheap checks flag or park DORMANT.
3. **A hint is not an overclaim** — a *labeled* hint cannot breach the firewall; the error is an *unlabeled* hint
   asserted as a result, not the hint's existence.
4. **The null result is also a hint** — every `TESTED-NEGATIVE` carries `residual-hint:` and re-enters NOTICED.
5. **Generic / vacuous is a flag, not a death** — MB8/MB12 at CHECKED set a flag and route DORMANT; they kill
   only at the full gate.
6. **Periodically widen** — the WIDEN/QUESTION cadences fire (see below); *zero* new NOTICED hints between WIDENs
   is itself the **rut-alarm** (the program may be in a deflationary tunnel).
7. **Symmetric honesty** — just as "we proved physics" is forbidden, "this hint is worthless" asserted *without
   running the gate* is forbidden. Both are **unearned verdicts about the state of evidence** (the generative twin
   of the C/K guardrails). *(Worked precedent: S041's "NCG: no shared data" was an unearned negative — it actually
   shares primes {2,3}; caught and corrected, ledger H10.)*

## The two cadences (standing rules in `ROADMAP.md`)

Fire **per ~10 banked results**, piggybacked on the gate-completion / `PROGRESS_LOG.md` action so they cannot lapse:

- **WIDEN** — the L37 "agreed-then-dropped" audit made standing + cross-finding synthesis: every banked result
  since the last WIDEN gets a synthesis touchpoint (`docs/STRATEGIC_SYNTHESIS.md` / the relevant `SYNTHESIS.md`);
  resurface dropped patterns; a **mandatory DORMANT sweep** (re-touch the oldest DORMANT hints — promote or
  tombstone, or the register becomes a roach motel); and a **standing physics-parallels prompt** ("which verified
  results have known parallels in frameworks we haven't examined?" — keeps the framework search L46/S041 live).
- **QUESTION** — the completeness critic, internalized from the chat1/chat2 cross-checks: a fixed prompt-set
  ("what modality/connection haven't we tried? the adjacent unasked question to each banked result? what would a
  skeptic say is missing?"). Output → new `QUESTION`-type rows in `docs/HINT_LEDGER.md`.

## This protocol's own failure modes (named, so it stays honest)

- **The deflationary culture rejects the transplant** (highest risk) — the ledger quietly acquires a high
  admission bar and re-collapses into OPEN_LEADS. *Antibodies:* the `GOVERNANCE §6.2` constitutional edit + the
  rut-alarm (rule 6).
- **DORMANT roach motel** — hints check in, never out. *Antibody:* the mandatory DORMANT sweep in WIDEN.
- **Bureaucracy creep** (the very thing the owner fears) — *Antibody:* NOTICED is one line; resist states beyond
  the five; if the ledger is ever more effort than the hint is worth, the protocol failed its own leanness test.
- **Staging boundary blurs** — someone runs the heavy battery on a NOTICED hint "to be safe," re-importing the
  false-negative reflex. *Antibody:* the attachment table is **normative** — over-verifying a hint is a protocol
  violation, symmetric to under-verifying a claim.
- **Hint inflation lowers the gate** — sunk-cost pressure to promote. *Antibody:* the promotion gate is **never**
  softened (the non-negotiable above).

## Anchors
`GOVERNANCE.md` (§6 red-team, §6.1 C/K, §6.2 the staging principle, §8 anti-overclaim glossary);
`docs/HINT_LEDGER.md` (the register); `docs/OPEN_LEADS.md` (the decision-to-run ledger hints promote into);
`ROADMAP.md` (the WIDEN/QUESTION standing rules); `REPRODUCIBILITY.md` (MB6–MB12); `speculations/GOVERNANCE.md`
(the HELD rule + status enum the gate reuses); `papers/VALIDATION_LEDGER.md` (the rigor counterpart);
`papers/CANDIDATES.md` PC05 (the methodology paper — this is its generative half).
