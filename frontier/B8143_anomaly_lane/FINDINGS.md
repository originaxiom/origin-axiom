# B8143 — the anomaly lane: B1160's theorem is right, its fence is load-bearing, and here is the witness

**Arc dated:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** structure only. No measured quantity is asserted as derived; hypercharge *ratios* are
group-theoretic structure, per B950's registration of L132.

## Why this lane at all

This programme has three standing no-gos, and Paper IV catalogues them: **scale is closed** (Mostow
plus the covering ladder), **orbit-to-point is closed** (an invariant cannot select within its own
orbit), and **trace-field inputs are family-level**. **Anomaly cancellation is the one lane where
all three are silent** — it is a Diophantine condition on *dimensionless* charges, so the scale
no-go cannot reach it; its solution set is a set of rational points, not an orbit; and it consumes
representation content, not the trace field. That is why the anomaly lane was recorded as *live and
unrun*. B1160 is that lane firing.

## B1160's core theorem: reproduced exactly

| step | B1160 | this bench |
|---|---|---|
| three linear conditions | `Yl=−3Yq`, `Ye=6Yq`, `Yu+Yd=−2Yq` | **identical** |
| cubic on the 2-plane | `−18(t−3)(t+3)` | **identical** |
| roots | `t=±3` → SM and its `u↔d` swap | `(1/6,−2/3,1/3,−1/2,1)` ✓ |

**The load-bearing theorem is correct as stated.**

## Finding 1 — a branch its chart cannot see

Solved with **no normalisation** over the full 5-dimensional charge space. The system has **three**
branches, not two:

```
{Yq =  Yu/2, …}   the u↔d-swapped SM
{Yq = −Yu/4, …}   the SM
{Yq = 0, Yd = −Yu, Yl = Ye = 0}   ← a ONE-PARAMETER VECTOR-LIKE family
```

B1160 sets `Yq = 1`, which excludes `Yq = 0` by construction. **This is exactly B864's recorded
"three lines" — hypercharge, the `u↔d` swap, and the vector-like direction — confirmed
independently.**

**Not damaging:** the third branch is non-chiral and is no candidate hypercharge. **But it changes
the honest statement:** anomalies *alone* leave three branches; it takes **chirality** to reduce to
the two SM lines, and B1160's normalisation supplies that second ingredient silently.

## Finding 2 — the shaping is genuinely free, and here is the counterexample

B1160 fences *"the SM-shaping is observer-paid."* **That fence is not a caution. It is a theorem
with an explicit witness.**

**Rigidity is a dimension count.** With `n` charges, 3 linear conditions, 1 cubic and 1 overall
scale, the solution set has dimension `n − 5`. So `n = 5` is exactly the rigidity threshold — **the
SM's five field types are precisely the number that lets anomalies determine the charges.** Below
it the system is over-determined; above it the charges are not determined at all.

Enumerating **every** 5-field content over `{(3,2), (3̄,1), (1,2), (1,1)}` that passes the Witten
condition, keeping only solutions isolated up to scale with **no sterile (zero-charge) field**:

| states | content | charges |
|---:|---|---|
| **13** | **(3,2)+(3̄,1)+(1,2)+2×(1,1)** | **(1/2, −1, −3/2, 2, 1)** |
| 15 | (3,2)+2×(3̄,1)+(1,2)+(1,1) | (1/6, −2/3, 1/3, −1/2, 1) — **the SM** |

All four anomaly conditions vanish exactly for the 13-state content in `Fraction` arithmetic; four
doublets, so Witten is satisfied; every field is charged; the solution is isolated up to scale.

> **The Standard Model is NOT the minimal rigid chiral anomaly-free content over this alphabet.**

## The decisive question this opens

**Is the 13-state content realisable inside the object's 27, with charges in its `u(1)³` lattice?**

- **If yes** — the object does not force the SM shape, and the hypercharge result is weaker than its
  headline reads: the shaping carries the content.
- **If no** — the 27's own content *together with* anomalies forces the SM shape, which is
  **stronger** than B1160 and would move the shaping from observer-paid to object-forced.

Either outcome settles what B1160 explicitly leaves open, and it is a finite exact computation on
weight data that already exists in the cloud/cc stack. **Not attempted here** — this seat does not
have the 27's trinification decomposition in hand.

## ⚠ Two instrument errors of mine

- **The first search asked the wrong question.** "Does an anomaly-free solution *exist*?" is almost
  always yes once there are enough free charges. The question had to be **rigidity**, not existence.
- **The first chirality test was too weak.** It only required that *some* `(3,2)` be charged, so two
  contents with a **neutral** `(3,2)` and neutral singlets passed as "chiral". Tightened to require
  every field charged; both dropped out and the census fell from four contents to two.

## SCOPE

- **Not claimed:** that B1160 is wrong — its core theorem is reproduced exactly and is correct.
- **Not claimed:** novelty for the anomaly-forces-hypercharge fact, which B1160 itself labels standard.
- **Not claimed:** that the 13-state content is realisable in the 27. That is the open question.
