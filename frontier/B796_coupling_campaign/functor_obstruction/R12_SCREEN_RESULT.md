# R12/R13 — the eligibility screen, run. **R12 self-refutes. R13 survives and does the whole job.**

**cc3, 2026-08-11.** Instrument: `eligibility_screen.py`. **Gate 5-Q: screening
instrument, no claim, nothing to CLAIMS.md.** Measured values are filter inputs,
not derivation outputs.

---

## What was proposed

After the fourth crossing failed **methodologically clean** (B1027: sealed before
data contact, prior MISS declared and held, zero anchors consumed, all eleven
requirements cited — **missed at 11.4σ and 38.0σ**), cc3 proposed two new gates:

- **R12 — eligibility.** The object's forced values are **quantized** to the
  8-element θ-even set (B1011, resolution bound `Re χ_V(M)/dim V`). Before sealing
  a crossing, check the target lies in that set to within its own error. If not,
  don't spend the cell.
- **R13 — base rate.** With 8 values in [0,1], "close" is cheap. Price any reported
  margin against the probability a **random** target does as well.

## What the run says

**Base rate (200k uniform draws, absolute distance to nearest forced value):**

| within | P(random target lands there) |
|---|---|
| 1 % | **14.1 %** |
| 3 % | **41.9 %** |
| 5 % | **64.5 %** |
| 10 % | **89.1 %** |
| mean gap | **0.0467** |

*(cc3 quoted 52.3 % at 5 % in relay earlier tonight; that was a relative-gap
metric. The absolute figure above is the one the instrument computes, and it makes
the same point harder.)*

**Whole list, one declared map per type, no selection** — angles→`cos`, matrix
elements→`|V|`, ratios→`r` or `1/r`:

| target | mapped | nearest | gap | R12 pass? | P(random better) |
|---|---|---|---|---|---|
| \|V_ub\| | 0.0038 | 0.0 | 0.0038 | no | **5.4 %** |
| m_e/m_mu | 0.0048 | 0.0 | 0.0048 | no | 6.8 % |
| \|V_td\| | 0.0086 | 0.0 | 0.0086 | no | 12.1 % |
| θ₁₃ PMNS | 0.9888 | 1.0 | 0.0112 | no | 15.8 % |
| sin²θ_W | 0.2312 | 0.25 | 0.0188 | no | 26.4 % |
| **\|V_us\| (B929)** | 0.2243 | 0.25 | 0.0257 | no | **36.0 %** |
| θ₁₂ PMNS | 0.8348 | 0.809 | 0.0258 | no | 36.2 % |
| **m_u/m_d** | 0.4700 | 0.5 | 0.0300 | **YES** | 41.9 % |
| \|V_cb\| | 0.0410 | 0.0 | 0.0410 | no | 55.1 % |
| **quark δ₁₃ (B1027)** | 0.3616 | 0.4045 | 0.0429 | **YES** | **57.3 %** |
| **δ_CP PMNS** | 0.9563 | 1.0 | 0.0437 | **YES** | 58.3 % |
| m_s/m_d | 0.0513 | 0.0 | 0.0513 | no | 65.3 % |
| m_mu/m_tau | 0.0595 | 0.0 | 0.0595 | no | 70.2 % |
| θ₂₃ PMNS | 0.6561 | 0.809 | 0.1530 | no | 99.7 % |

---

## FINDING 1 — **R12 WOULD NOT HAVE BLOCKED B1027.** The proposed fix fails on the case that motivated it.

**B1027's target PASSES R12.** `cos(68.8°) = 0.3616`, gap to `φ/4 = 0.4045` is
0.0429; propagated through `cos`, the 4.5° error bar is ±0.073. **Gap < σ ⟹
eligible.** The gate cc3 designed to catch the fourth crossing **licenses it.**

## FINDING 2 — and the reason is structural: **R12 rewards imprecision.**

**All three passes are the three loosest-measured quantities on the list**
(δ_CP ±40°, quark δ₁₃ ±4.5°, m_u/m_d ±10 %). Meanwhile the **five sharpest gaps in
the table all FAIL** — `|V_ub|`, `m_e/m_μ`, `|V_td|`, `θ₁₃`, `sin²θ_W`, whose
targets sit 5–26 % on the base rate, i.e. **genuinely close**, are rejected
because their error bars are small.

> **"Gap within the target's own 1σ" is a test of the EXPERIMENT'S precision, not
> of the OBJECT'S agreement.** It admits badly-measured targets and excludes
> well-measured ones. **It is the wrong criterion and it is inverted.**

## FINDING 3 — **R13 alone does the entire job, and grades correctly.**

The base-rate column ranks the table the way agreement actually runs.
**B929 → 36.0 %. B1027 → 57.3 %.** Both crossings performed **worse than a coin
flip against noise**, and R13 says so without reference to any error bar.

It also shows the near-miss trap in the open: **δ_CP PMNS looks like a hit**
(0.9563 vs 1.0) and is **beaten by a random target 58 % of the time**. That is the
same class of coincidence chat-2 priced at zero in M11 (`ln2/2 = 0.3466`,
`ln2/log φ² = 0.7202`) and chat1 pre-priced in its §7 — **three seats flagged this
shape independently and none of them had the base rate that makes it worthless.**

---

## THE REVISED PROPOSAL

**Withdraw R12 as posed. Bank R13.**

> **R13 — no crossing may report a margin without the quantized base rate beside
> it.** A crossing whose target is beaten by a random target more than ~30 % of
> the time is **not evidence**, whatever σ it quotes.

**And the replacement for R12 is a different question**, not an error-bar test:

> **R12′ — does the target's map form get declared before the target is chosen?**
> The screen ran ONE map per type. Trying `sin`, `sin²`, `tan`, or the inverse
> ratio for each of 14 targets is **56 trials**, and at a 41.9 % hit rate for a 3 %
> gap **something will always land.** The freedom is in the MAP, not in the value.

## What this does NOT settle

- **Channel.** `FORCED` is the **coupling** channel's set (B1011). R10/B1016
  require a crossing to declare its channel; **this screen applies per channel and
  cc3 holds only this one.** A different channel's set changes every row.
- **The 8 values themselves.** Taken from B1011 as banked. Not re-derived here.
- **Selection.** The whole list is printed precisely so that **choosing a row after
  reading it is visible as post-hoc selection (E29)** and must be priced as such.
  **cc3 selects nothing.**
