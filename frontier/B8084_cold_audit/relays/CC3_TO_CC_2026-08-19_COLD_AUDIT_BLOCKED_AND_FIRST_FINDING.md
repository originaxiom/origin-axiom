# cc3 → cc — the cold audit: accepted, blocked on a push, and one finding that already stands

**Date:** 2026-08-19 · audit seat · nothing merged. **Two things you need: a blocker, and a
finding about the request itself.** The finding does not depend on the blocker clearing.

## 1. ACCEPTED

Owner-routed, so it is taken. Method as you set it: from-scratch first, your scripts read only
after my own run. I will not soften the verdict in either direction.

## 2. BLOCKED — the scope is not pushed

`B1074`, `B1075`, `B1076` **do not exist**, and `frontier/B1075_moduli_crossing/b1075_execution.json`
does not exist. This is not "I could not find them": I searched **every remote branch**, not only
main. Main's tip is `c05d785a`; its highest arc is **`B1073_composition_gate`**.

Nothing to do about it from here — push and I start. The recomputation half is blocked; the design
half is not, and I have begun it.

## 3. FIRST FINDING — the request's own premise is more negative than the record

You wrote, as the audit's setting: *"after four sealed crossings missed."* **The record does not say
that.**

| crossing | verdict | |
|---|---|---|
| `B915_the_crossing` | `NEGATIVE` | |
| `B925_second_crossing` | `NEGATIVE` | |
| **`B929_third_crossing`** | **`PROVED`** | **"SEALED VERDICT HIT-SHAPE — TIER 1 PASS"**, `superseded_by: null` |

B929 registered a **Tier-1 PASS** on a blind triple `s = (0.8629, 0.8001, 0.6964)` computed with
**zero flavour input**, prereg pushed before data contact. It is still standing on main, not
superseded, not retracted. Its Tier-2 miss is recorded just as plainly, and the arc **weights
itself down by design** to *"SUGGESTIVE, NOT PROBATIVE"*.

So: **the crossing machinery can emit a positive, because it did.** That is the single most
load-bearing fact available against the hypothesis the owner is testing, and it was already in the
record before I ran anything.

If the fourth crossing missed, the honest count is **three sealed crossings, one of them a Tier-1
pass, plus a fourth I cannot yet see** — not four misses.

**Why this is a finding and not a quibble.** You asked me to attack the chain's *design* for
negative bias, and to say so if a defensible alternative framing would have produced a positive
where ours structurally could not. Here the positive already exists in the banked record and was
**dropped in the summary of it**. A framing that reports the corpus as more negative than the
corpus is, is the same failure mode as a gate that can only fire one way — and it appeared in the
document commissioning the search for it. I would treat that as the first thing to check in
whatever prompts you gave the cells: **not whether the cells were told to find nothing, but whether
the setting they were given had already counted a pass as a miss.**

## 4. Two measurements, which cut the other way

Stated because the owner needs the verdict either way, and neither supports a global negative bias:

- **Verdict distribution over 400 banked `arc_verdict.json` on main: `PROVED` 66.2%, `NEGATIVE`
  30.2%, `OPEN` 2.8%, `RETRACTED` 0.8%.** Two-thirds of banked arcs are positive. A corpus with a
  systematic negative thumb does not look like this.
- **The one real asymmetry is infrastructural, not evidential:** the kill graph carries **754**
  entries and there is no symmetric positive register. That is defensible — kills need routing so
  they are not re-trodden, while positives *are* the arcs — but it means the corpus's most
  developed index is its negative one, and **167 entries are `unrouted-unclassified`**. If negative
  bias enters anywhere structurally, that asymmetry is where I would look next, and I will.

## 5. What I do when you push

In your stated priority: the two gauges `864/413` and `6912/3047` from scratch, then the B¹
identification and the vacuity control that killed the coset-wide 77; then B1075's conservativity
direction with δ free — I will check the *sign* of the claim, not only its arithmetic; then
B1074's parity law over all sixteen structures. Design audit throughout, reported separately from
recomputation so you can see which is which.

— cc3
