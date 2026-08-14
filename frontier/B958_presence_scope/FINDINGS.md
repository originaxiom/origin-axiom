# B958 — THE PRESENCE SIDE: scoped, one consistency test passed, and an honest deferral

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS. Gate 5 untouched.
**Owed since:** B946 §6 and B948 §4 — the solo seat's §LXXXIII–LXXXVI + §XCII, two-prime and
unread by any other seat, their one genuinely new recent contribution.

---

## 1. The finding that came before the verification

**The repo contains no independent construction of M12 (the "invisible 12").**

B909's `mixed` leg reports *"the Killing-perp/invisible 12 with zero torus-invariance
defects, full-rank charge actions, M12∩core = 0, and the SMT-block kernel-4 fingerprint —
the §LVIII identification's data verified."* But it verified that **by running the incoming
material**, not by rebuilding on this bench. `frontier/B909_frame_arc/` ships
`cmt_correct.py` and `results.json` — no frame or M12 construction.

> **So the invisible 12 has never been independently constructed here.** That is the same
> shape as today's other findings: **B950** found we compared against a target we never
> wrote down; this finds we verified data we never independently built.

## 2. What I did run — a genuine frame-independent test, and it passed

The presence side claims M12 is **colour-blind** (every su(3) weight (0,0)) with **dim 12**.
That imposes a constraint independent of any frame choice: **M12 must sit inside the
centralizer of colour su(3) in e₆.**

Computed exactly on **our own** instrument (`e6_centralizer.py`, full Chevalley bracket
table, no incoming code):

| quantity | value |
|---|---|
| dim e₆ | 78 |
| stacked ad-matrix rank over the A₂ generators | **62** |
| **dim Z(su(3)_colour)** | **16** |

Cross-checks against the standard structure: e₆ ⊃ su(3)×su(3)×su(3), so Z(su(3)_C) =
su(3)⊕su(3) = 8 + 8 = **16**. ✅

**Consistency requires 12 ≤ 16 — and it holds.** This is a real constraint that could have
failed: a colour-blind 12-dimensional space cannot exist if the colour centralizer were
smaller than 12. It is **not** a verification of the presence side; it is one necessary
condition, met.

## 3. Why I am deferring the rest rather than attempting it

A genuine verification requires independently reconstructing:

1. **the frame** — the orthogonal charge frame (§XLIX–LVIII / B909);
2. **the floor** — su(3) ⊕ the four charges, dim 12;
3. **M12** — the Killing-perp, dim 12;

and only then testing the seven claims: [M12,M12] escaping by exactly 4 into the torus;
[floor, M12] = 12 with **zero** escape; not a module over the FMT so(10) (escape 50); centre
0; twelve multiplicity-one colour-blind weight lines; closure under exactly W_frame with
three free orbits; and the **orbit↔generation bijection**.

> **Reconstructing their frame wrongly would produce a false verification or a false
> refutation — either of which is worse than an honest deferral.** This is a proper sealed
> cell with a substantial build, not a check that can be folded into another arc's tail.

**It therefore remains OWED.** B946 verified §LXXXII only; B948 did not discharge it; this
arc does not either. What this arc adds is that the debt is **larger than it looked** —
it requires a build, not a read — and that one necessary condition has now been checked
against our own e₆ rather than assumed.

## 4. Registered

- **L135 — BUILD THE FRAME INDEPENDENTLY.** Before the presence side can be verified or
  refuted, this bench needs its **own** construction of the frame, the floor and M12. That
  build is worth having regardless of the presence side's fate: it would let every future
  frame-arc claim be checked here instead of run from incoming code, and it closes the
  "verified data we never built" gap this arc names. **Prerequisite for discharging the
  presence-side debt.**

## 5. Honest limits

- §2's test is **necessary, not sufficient**, and is stated as such.
- The claim that Z(su(3)_C) = su(3)⊕su(3) is standard; the **dimension 16 was computed
  here**, and the standard structure is used only as a cross-check.
- Nothing about the solo seat's claims is confirmed or denied by this arc.

---

**Verdict: SCOPED + one necessary condition met.** The presence side stays **owed**; the
repo turns out to lack an independent M12 construction at all; and the honest next step is
**L135 — build the frame here**, which is worth doing whatever the presence side turns out
to be.
