# B841 — PREREGISTRATION: the provenance pass over the 167 routed kills

cc banking seat, 2026-08-01. **Sealed before the fan-out.** Gate 5 absolute; nothing to `CLAIMS.md`.

## What B836 deliberately did not do

B836 routed 167 `NEGATIVE`-verdict arcs into the kill graph with **every judgement field unset**,
because `fact_computed` asserts that the kill's **discriminating computation is in the repository** —
B799 showed the flag carries real information, B525 exists to protect it, and **setting it
mechanically would fabricate exactly the signal it is for.**

This pass sets it — under a design that makes fabrication *checkable*.

## The safety property, and it is the whole point

> **A reader may not assert `fact_computed = true` without producing a RESOLVABLE POINTER —
> `path` (and line, where meaningful) — to the computation. Every pointer is then verified
> mechanically against the filesystem.**

B741 did exactly this by hand and existence-checked **48/48**. A fabricated or mistaken pointer
**fails the check**, so the flag cannot be inflated by confident prose.

**And the discipline B741 established is binding here:** *"located but the located computation is
itself a citation" = NOT-LOCATED.* A pointer to a line that cites a paper is **not** a computation.

## The rubric, fixed here

For each arc, the reader returns:

- **`fact_computed`** ∈ {`true`, `false`, `undetermined`}
  - `true` — the discriminating computation is in the repo **and a resolvable pointer is given**
  - `false` — the discriminating fact is asserted, cited, or proxied, not computed here
  - `undetermined` — the arc's own text does not make the discriminating fact identifiable
- **`pointer`** — required and non-empty **iff** `fact_computed = true`; a repo-relative path
- **`kill_form`** — one of the ten banked forms, or `other`
- **`why`** — one sentence naming the discriminating fact

**`undetermined` is a first-class outcome, not a failure.** Forcing a binary here is what produces
inflated provenance.

## Verification, applied to every returned record before any write

1. **Every `true` pointer must resolve** on the filesystem. Unresolvable → **downgraded to
   `undetermined`** and counted.
2. `kill_form` must be in the banked taxonomy.
3. `fact_computed = true` with an empty pointer → **downgraded**.

**Downgrades are reported as a rate**, because that rate is the measurement of whether the fan-out
inflates provenance.

## Two-outcome

- **The pass lands** — the pointer-resolution rate is high, and the 167 records get real
  `fact_computed` values with the `true`s each backed by a checked path.
- **The pass is untrustworthy** — a substantial share of `true`s cite paths that do not resolve.
  Then **the flags are NOT written**, the fan-out is reported as having failed its own safety check,
  and B836's unset state stands. **This is a real branch: it is exactly how a scaled provenance pass
  goes wrong, and B836 refused to run one without it.**

## Pre-stated expectation

I expect **`false` to dominate** — these are arcs whose kill was recorded as a verdict headline, and
B801/B833 found the corpus's negatives are largely *stated*, not *computed*. I expect
**`true` ≲ 35 %** and a **pointer-resolution rate ≳ 90 %**. If `true` comes back a majority, that is
either a genuinely well-computed corpus or an inflating panel, and **the resolution rate is what
distinguishes them** — which is why it is measured rather than assumed.
