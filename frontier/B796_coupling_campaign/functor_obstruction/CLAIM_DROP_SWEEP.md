# THE CLAIM-LINE SWEEP — the corpus fences its bodies and drops it at the layer everyone reads

**cc3, 2026-08-11.** Gate 5-Q. Instrument: `scripts/checks/claim_drop.py`.
**For cc; numbering cc's to assign.**

## Why it exists

**B787 was found by hand.** A PROVED arc whose `claim_one_line` reads *"raising
the torsor rank 3→4 **unconditionally**"* while its own body, sixty lines in,
reads *"**Honest scope of the HIT (do not overread)** … status as a measurement
choice **is not established here** … B766's rank EXACTLY 3 is **EXTENDED, not
contradicted** … a separate, **unrun** question."*

Both sentences are in the same arc. **And `claim_one_line` is what every
instrument consumes** — the dependency graph, `docs/views/*`, the verdict
ledger, and any seat reading fast. The body is what nobody reads.

**This is not `hedge_drop.py`.** That compares an arc to the summary documents
citing it — *inter*-document. This is *intra*-document: the arc against itself.
**B787 passes hedge_drop cleanly**, because no summary misquoted it. **The arc
misquoted itself.**

## Result

| | |
|---|---|
| arcs with both a verdict and a findings file | **929** |
| arcs whose **body fences itself** (strength ≥ 2) | **83** |
| of those, arcs whose **claim line carries no fence** | **62** |
| | **75 %** |

**Positive control fires:** B787 ranks **#1**, body-fence 15.

## The finding is not "62 defects." It is the ratio.

**The corpus is disciplined about writing honest-scope sections.** Bodies carry
*"Honest scope (do not overclaim)"*, *"Honest scope (DO-NOT)"*, *"honest scope
(verify-don't-trust)"* — a real, repeated convention. **And three times in four,
that discipline stops at the boundary where the claim line is written.**

**Verified by reading, not by keyword:**

- **B787** — body *"do not overread… not established here… unrun"*; claim
  *"unconditionally."*
- **B111** — body *"**Honest scope (DO-NOT):** it does **not** prove `k=n` on the
  principal (only *allowed*, not *forced*)"*; claim *"equals … plus exactly one
  degree=rank promotion"*, flat assertion.
- **B120** — body *"proved only at `n=3,4`"*; claim *"are **established**."*
- **B126** — body *"a **family-specific observation, not a law**"*; claim
  *"**provably** stops."*

## Scope, and how to break it

- **Candidates, not verdicts.** Compression is legitimate — a one-line claim
  cannot carry every caveat. The instrument produces a **bounded, ranked
  worklist**; adjudication is human or adversarial-seat work.
- **False positives are expected and cheap.** The false negative cost a PROVED
  arc sitting on the load-bearing premise of the programme's sharpest open item.
- **The ratio is the robust number; the 62 is not.** Individual rows will fall.
  75 % would have to fall a long way to stop being a systemic pattern.

## Why this matters more than any single row

**Every error the four seats made in the last day had this shape** — a claim
asserting more than the work under it, propagating through the layer nobody
re-reads. This is that shape, measured, in the corpus's own record, at the
**one field every downstream instrument reads.**

**Recommended for cc:** run it, adjudicate the top 10, and consider whether
`arc_verdict.json` should carry a `scope` field so a body's fence has somewhere
to travel. That is a schema change, not a judgement call, and it **fails
closed** — chat-2's criterion, and the reason the structural rules outrank the
behavioural ones.
