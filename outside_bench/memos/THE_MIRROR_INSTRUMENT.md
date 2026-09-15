# MEMO 164 — THE MIRROR INSTRUMENT: **NOT ADOPTED**, AND THE REASON IS THE FINDING

**Banked 2026-08-30.** Seal `seals/MIRROR_CLASS_PREREG.md`, pushed before building.
Certificate `certificates/closure_claim_sweep.py`; output vendored.
Owner-directed: *"build the mirror class."*

**VERDICT: the instrument is BUILT and NOT ADOPTED.** Its control passes and **its sweep does not
survive adjudication** — 5 of the top 5 flags are false, and **it misses the one real instance it
was built to catch.**

---

## 1. WHAT WAS BUILT, AND THE FOUR CORRECTIONS ON THE WAY

Deliberately `B1218`'s method with the poles reversed: same claim units, same IDF. Four successive
designs, **each killed by the binding control or by adjudication, none by me noticing first**:

| v | discriminator | how it died |
|---|---|---|
| **v1** | pool = arcs whose **verdict** is not settled | control fired on **neither** side. `B990` — the arc that *is* the live route — is **`PROVED`** and titled *"SHARPENED, NOT CLOSED"*. **A verdict field does not encode whether a route is live.** Same failure `B1213` found in the paper's claim base: reading metadata where content carries the signal |
| **v2** | pool = arcs whose **text** carries a live-route phrase | control passed; sweep returned **60**, dominated by my own `INDEX.md` and register rows. **`B1218`'s tautology and self-citation filters, which I did not carry over** — and `B1219` had recorded that exact slip ("applied once and not carried over"). I repeated it |
| **v3** | + require a live arc to **outrank** the best closing arc | 60 → 32 → 25, still topped by the paper's normalisation no-go matching **`B991`, the arc that proves it** |
| **v4** | + **clause-scope** the live phrase near shared terms (`B1210`'s own remedy) | **no change.** `B991` *is* clause-adjacent: its paragraph says **"STAYS OPEN"** about a different sub-question |

---

## 2. WHY IT FAILS — a structural reason, not a tuning problem

**Arc claim records are paragraph-scale and each mixes closures with live routes.** `B991` closes the
normalisation question *and* says "STAYS OPEN" about something else. `B1220` closes λ *and* says "two
routes". **Liveness is not an arc-level property**, so no arc-level predicate can carry it — and
`B1210`'s clause-scoping fixes *citation verbs*, which attach to a citation site, but liveness
attaches to nothing.

**And then the decisive fact:**

> **The instrument misses the passage it was built for.** The paper's actual *"What is permanent"*
> paragraph is **not** among the 25. Only my synthetic control and my own memo *quoting* it appear.

**Why it misses is the finding.** The paper says:

> *"The finite labels will not reduce further either: an invariant selector cannot pick a point of
> its own orbit, so a finite menu is the terminal state and not a deficiency."*

That names `B990`'s **lemma** — invariant selector, orbit, point. **It never names the route it
forecloses**: integral orbits, `G(ℤ)`, the VEV direction, Route A. My synthetic control *did* name
them, which is why the control passed and the real passage does not.

> **A drifted permanence claim characteristically omits the vocabulary of the route it forecloses.
> The drift and the undetectability have the same cause.** Term-overlap cannot find it, because the
> terms that would find it are exactly what the drift leaves out.

**That also explains why three seats independently built instruments for the *other* polarity.** An
"open" claim names the thing that is open — it is detectable by construction. **A "closed" claim
need not name what it closes.** The mirror class is not merely unhunted; on this substrate it is
**structurally harder to hunt**, and that asymmetry has been invisible because nobody tried.

---

## 3. WHAT WOULD WORK — the constructive half

The mirror class needs **route-level records**, not arc-level ones: a register of live routes, each
with a state and the claims it would contradict. Then a permanence claim is checked against *routes*,
not against text.

**The corpus's nearest existing thing is `docs/OPEN_LEADS.md` and `docs/OPEN_PROBLEMS.md`** — which
*are* route-level, carry states, and are already maintained. **Matching permanence claims against
open-register entries is the design I would try next**, and it is a different instrument from this
one, not a fifth tuning of it.

**Recommended, and not done here:** that build is a cell of its own, and after four failed
discriminators in one sitting the honest move is to report rather than start a fifth.

---

## 4. WHAT IS AND IS NOT DELIVERED

- **Delivered:** the class is named, its one live instance is known **by reading** (memo 163), the
  reason it resists instrumentation is diagnosed, and the substrate that would work is named.
- **Not delivered:** a working detector. **The instrument is banked as NOT ADOPTED** and should not
  be run as though it worked. Its control passing is not sufficient — the seal said the sweep must
  also survive adjudication, and it did not.
- **The paper's drift stands exactly where memo 163 left it**, found and confirmed by hand, now
  contradicted by four discharged hypotheses.

## 5. FENCES

- The 25 flags are **not** reported as findings; 5 of the top 5 were adjudicated false and the rest
  are not claimed either way.
- **Control passing ≠ instrument working.** This cell is the counter-example, and it is worth
  keeping for that alone: a two-sided control on a *synthetic* positive can pass while the real
  positive is missed, because the synthetic one was written by the same hand that wrote the detector.
  **That is a new lesson and it applies to every control this bench has built.**
- Gate 5 untouched: text only.
