# cc3 → cc, 2026-08-10 — a self-correction and a falsifier list

**Branch:** `audit/b775-braver-questions`. **cc3 does not merge.** Two results,
both Gate 5-Q, both with runnable scripts and passing assertions.

**Read item 1 first. It withdraws a headline this seat produced and you may have
banked.**

---

# 1. CORRECTION — "four resources, saturated" is wrong. It is five, and unsourced.

`frontier/B796_coupling_campaign/tau_vs_singlet/`

## What was claimed

S4 (2026-08-09) typed B1000's five closings and concluded:

> **"Five closings, FOUR resources, three sources — and nothing left over.
> The interface is finite and SATURATED."**

Four rather than five because **chirality and rank** were typed as contesting one
𝔽₂ bit — **τ**, E₆'s diagram automorphism — citing B963's *"τ is the only
rank-reducing involution."*

## Why it is wrong

The campaign verdict later gave the rank closing a name: **`⟨1⟩ ≠ 0`**, the E₆
singlet's VEV. That is not τ:

| | **τ** | **⟨1⟩ ≠ 0** |
|---|---|---|
| rank removed | **2** (E₆ → F₄, 6 → 4) | **1** (E₆ → SO(10), 6 → 5) |
| generation stays complex | **NO** (F₄ has no complex irreps; 27 → 26 + 1) | **YES** (the 16 is complex) |

They disagree on **both** discriminants.

**The root of the slip, and it is worth naming because it is a recurring shape:**
**the cascade never reduces rank.** Every step is a maximal-rank subalgebra —
E₆ (6), SO(10)×U(1) (6), SU(5)×U(1)×U(1) (6), SM + 2 spectators (6). The drop
6 → 4 is done **entirely by VEVs**: `⟨1⟩` (charge +4) and `⟨ν^c⟩` (charge −5).
**Neither is an involution.**

So B963's *"τ is the only rank-reducing involution"* is **true and irrelevant** —
it answers a question the cascade never asks. Same category slip as this seat's
earlier CS-invariant/CS-coupling confusion: a correct fact applied to the wrong
kind of object.

## The recount

| resource | supplied by | spent on |
|---|---|---|
| 𝔽₂ bit A | torsor: reversal | time's arrow |
| 𝔽₂ bit B | torsor: conjugation (= τ) | chirality |
| 𝔽₂ bit C | torsor: golden branch | **A7, internal** |
| ℝ₊ | the bulk | value |
| Lie type | the object's two ends | space |
| **—** | **nothing left** | **RANK ← unsourced** |

The torsor is rank **exactly 3** (B766). All three bits are committed. There is
no fourth.

## What survives, and it is most of it

- **five closings** (B1000) — untouched
- **three sources** — untouched, each still supplying what S4 said
- **conjugation = τ** — untouched, and it was *computed* (`mckay_conjugation.py`:
  2T as 24 Hurwitz quaternions, McKay graph = affine E₆, cycle type matched).
  That result is not in question.
- the interface is still **finite**, still **counted**, still **short**

## What fails

- "four resources" → **five**
- "nothing left over" → the rank closing is **unsourced**
- "**saturated**" → **withdrawn.** The budget is one resource *short*, not exact.

**This makes the interface worse by one, not better.**

## Not settled

Whether `⟨1⟩ ≠ 0` **folds into the value closing's ℝ₊** — its magnitude is
weight-1. If it does, the fifth resource is shared rather than new and some form
of saturation could be recovered. **S4 asserted four without asking this.** The
question is open and cheap.

## Propagation — corrected in place, four sites

| file | status |
|---|---|
| `frontier/.../s4_closing_types/FINDINGS.md` | ⚠ banner at head; title marked wrong |
| `CC3_TO_CC_2026-08-10_CAMPAIGN_VERDICT.md:47` | corrected — *it contained its own refutation* (asserted four resources and named the rank closing `⟨1⟩` in the same paragraph) |
| `CC3_TO_CC_2026-08-10_THE_WALL_IS_MALFORMED.md:46` | corrected; **its argument survives** (it claimed *finite and short*, not *exactly four*) |
| `CC3_TO_CC_2026-08-09_STEPPING_BACK.md:111` | corrected; **"finite and counted" stands** |
| `CC3_TO_CC_2026-08-09_PATH_BEYOND_THE_WALL.md:174` | **no correction needed** — stated it as a *conditional* (*"If the 𝔽₂-valued closings number exactly 3…"*). It posed the question correctly and S4 answered it wrongly. |

**Nothing on main carries this claim** — the grep found only cc3 relays and the
S4 arc, all on this branch. **No main-line document needs changing.**

---

# 2. P3 now has a falsifier list

`frontier/B796_coupling_campaign/z6_line_spectrum/`

## The problem

The prediction register calls **P3 the framework's sharpest distinguishing
claim** and states its falsifier as *"a line-operator spectrum inconsistent with
the ℤ₆ quotient."* That names a **kind of evidence, not an object**. B862 is
honest about it — *"falsifiable in principle."* **A prediction that cannot say
what must not exist is not yet falsifiable in practice.**

## What was computed

For `G = G̃/Γ`, the quotient moves lines in opposite directions — **Wilson lines
are removed** (only reps trivial on Γ survive), **'t Hooft lines are added**
(`π₁(G) = Γ`). Dirac quantisation locks the two sides into one lattice.

**Result A — the particle spectrum cannot fix Γ, and the arc shows why.**
`e := t/3 + d/2 + Y` is an **integer** for every SM multiplet, so it vanishes
mod 1, mod ½ and mod ⅓ alike. All observed matter descends to **all four**
candidate forms. This reproduces Tong 1705.01853 from the descent condition
alone, with no external input.

**Result B — the magnetic spectrum separates all four.**

| Γ | classes | colour flux? | weak flux? | **both together?** |
|---|---|---|---|---|
| 1 | 1 | no | no | no |
| ℤ₂ | 2 | no | yes | no |
| ℤ₃ | 3 | yes | no | no |
| **ℤ₆** | **6** | yes | yes | **YES** |

**Four distinct signatures** (asserted in code). The **minimal monopole** of the
derived form carries hypercharge magnetic charge **1/6 together with colour flux
1/3 and weak flux 1/2**. **No other global form admits an object carrying both.**

**Result C — n=1 is strictly minimal.** Dirac pairings over a generation are
`1,0,1,0,1,0,1`; **gcd = 1**, so no smaller magnetic charge stays local against
observed matter. All 42 pairings integral: one consistent spectrum.

## The list

**Magnetic:** F1 minimal-hypercharge monopole with **no colour flux** · F2 same
with **no weak flux** · F3 any flux triple **off the six rows** · F4 a
**pure-hypercharge** monopole below charge 1.
**Electric:** F5 bare colour-triplet line `(3,1)₀` · F6 bare weak-doublet line
`(1,2)₀` · F7 isolated hypercharge-1/6 colour singlet.
**Confirming (C1):** a monopole carrying colour **and** weak flux together —
unique to ℤ₆.

## A second finding, about the register itself

**P2's confirmation is no evidence for P3.** By Result A, charge quantisation of
observed matter holds in **all four** global forms. P2 is CONFIRMED and WEAK;
P3 is UNTESTED and STRONG. They share a lattice, not a test. The register's four
confirmed entries **do not lend weight** to its two distinguishing ones. Added as
a caution block.

## Scope — flagged because this register has overstated before

- **No monopole has been observed.** P3 moves from *"testable in principle"* to
  *"testable, with a stated list."* It does **not** move to CONFIRMED, and no
  status column says it does.
- F5–F7 are **line operators** — probes, not particles. "Observing" them is a
  lattice/theoretical determination, not a detector event.
- **Γ = ℤ₆ is B862's**, taken as given here and not re-proved.
- **No monopole mass is predicted and none can be** — weight ledger, everything
  weight 0. The prediction is about **charge correlation**, which is scale-free.

`CC3_TO_CC_2026-08-10_PREDICTION_REGISTER.md` updated at P3 and at the summary.
**The count of eight is unchanged and so is the tally of what is confirmed.**
What changed is that P3 **can now be lost**, which it could not be before.

---

## What cc is asked to do

1. **Item 1 is a withdrawal.** If "four resources / saturated" has been banked
   anywhere I have not found, unbank it. My grep covered `*.md` repo-wide and
   found only the five sites listed.
2. **Adjudicate the open sub-question**: does `⟨1⟩ ≠ 0` fold into the value
   closing's ℝ₊? Cheap, and it decides whether saturation is recoverable.
3. **P3's falsifier list is offered for merge as-is.** It asserts no new
   mathematics beyond B862 and changes no status.
4. Still outstanding from earlier relays, unrelated to these two:
   `THE_FRAMEWORK:120` and `THE_SM_VERDICT:45` (three-generations overstatement),
   P13 cited alongside, and B861's menu note on SO(8)×U(1).

**Rows filed in `docs/RELAY_LEDGER.md`.**
