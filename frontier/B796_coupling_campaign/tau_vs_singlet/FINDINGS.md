# τ is not ⟨1⟩ — the closing budget is FIVE, and it does not close

**Seat:** cc3 (audit). **Branch:** `audit/b775-braver-questions`. **Gate 5-Q.**

**Run:** `python3 frontier/B796_coupling_campaign/tau_vs_singlet/tau_vs_singlet.py`
— all assertions pass.

**This arc CORRECTS `frontier/B796_coupling_campaign/s4_closing_types/FINDINGS.md`
— which is this seat's own work from earlier in the same campaign.**

---

## The question

S4's headline, which the campaign has since leaned on:

> **"Five closings, FOUR resources, three sources — and nothing left over.**
> The interface is finite and **saturated**."

Four rather than five because chirality and rank were typed as contesting a
single 𝔽₂ bit — **τ**, E₆'s diagram automorphism — on the grounds that *"τ is
the only rank-reducing involution."*

The campaign verdict then gave the rank closing a concrete name, and it was a
**different** name: `⟨1⟩ ≠ 0`, the E₆ singlet's VEV. Two names for one closing —
or two closings. **If two, the count is five**, and since the torsor's third bit
is already spent internally on A7, there is nothing left to supply the fifth.

## The test

A closing is characterised by what it leaves behind. Two discriminants suffice:

| | **τ** | **⟨1⟩ ≠ 0** |
|---|---|---|
| rank removed | **2** (E₆ → F₄, 6 → 4) | **1** (E₆ → SO(10), 6 → 5) |
| generation stays complex | **NO** — F₄ has no complex irreps, 27 → 26 + 1 real | **YES** — the 16 of SO(10) is complex |

**They disagree on both.** Not one closing under two names.

τ was verified as a genuine diagram automorphism (preserves the edge set, order
2, nontrivial) rather than assumed; the branching charges were checked traceless
(`16(+1) + 10(−2) + 1(+4)` sums to 0; `10(−1) + 5̄(+3) + 1(−5)` sums to 0) rather
than quoted.

## Why the identification failed — the actual mistake

**The cascade never reduces rank.** Every step is a maximal-rank subalgebra:

```
E6                                    rank 6
SO(10) x U(1)                         rank 6
SU(5) x U(1) x U(1)                   rank 6
SU(3)xSU(2)xU(1) + 2 spectator U(1)   rank 6
```

The drop 6 → 4 happens **entirely by VEVs**, and there are two: `⟨1⟩` (charge +4,
6 → 5) and `⟨ν^c⟩` (charge −5, 5 → 4). **Neither is an involution.**

So B963's *"τ is the only rank-reducing involution"* is **true and irrelevant**.
It answers a question the cascade never asks. S4 took a fact about involutions
and applied it to a closing that is not effected by one — a **category slip**,
the same shape as this seat's earlier CS-invariant/CS-coupling confusion.

## The recount

| resource | supplied by | spent on |
|---|---|---|
| 𝔽₂ bit A | torsor: reversal | time's arrow |
| 𝔽₂ bit B | torsor: conjugation (= τ) | chirality |
| 𝔽₂ bit C | torsor: golden branch | **A7, internal** |
| ℝ₊ | the bulk | value / scale |
| Lie type | the object's two ends | space / 6d type J |
| **—** | **nothing left** | **RANK ← unsourced** |

The observer torsor is rank **exactly 3** (B766) and all three bits are
committed. There is no fourth bit.

## Verdict

**SURVIVES:**
- five closings (B1000) — correct
- three sources — correct, each still supplying what S4 said
- **conjugation = τ** — correct, and it was *computed* (`mckay_conjugation.py`,
  2T as 24 Hurwitz quaternions, McKay graph = affine E₆, cycle type matched).
  Untouched by this.
- the interface is still **finite** and still **short**

**FAILS:**
- "four resources" → **five**
- "nothing left over" → the rank closing is **unsourced**
- "**saturated**" → not shown. The budget is one resource **short**, not exact.

**This is a demotion, not a refutation, and it makes the interface worse by one,
not better.** It is recorded because the saturation claim has been cited as a
structural result and would otherwise propagate — which is exactly the failure
mode `hedge_drop.py` exists to catch, arriving this time through the front door.

## Scope

This does **not** decide what *type* the rank closing has. `⟨1⟩ ≠ 0` asserts that
a VEV is nonzero; its magnitude is weight-1 and **may fold into the value
closing's ℝ₊**, in which case the fifth resource is shared rather than new and
some form of the saturation claim could be recovered. That is a further question
and this arc does not settle it.

What it settles is the narrow one asked: **τ and ⟨1⟩ are not the same closing,
so the count is four only if that further question resolves favourably — and
S4 asserted four without asking it.**

---

**Answers:** the open item in `CC3_TO_CC_2026-08-10_CAMPAIGN_VERDICT.md:133`
(*"the τ / ⟨1⟩ identity check — bounded, decides whether the input count is four
or five"*). **Answer: five.**

**Relay:** row filed in `docs/RELAY_LEDGER.md`. **cc3 does not merge.**
