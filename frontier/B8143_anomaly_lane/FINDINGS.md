# B8143 — the anomaly lane: B1160's theorem is right, and its shaping fence is TOO CONSERVATIVE

> ## ⚠ CORRECTED 2026-08-26 — THE 13-STATE WITNESS IS DEAD, AND THE CONCLUSION REVERSES
>
> **Steps 2–3 omitted the pure `[SU(3)]³` anomaly.** My "13-state counterexample" has
> `[SU(3)]³ = +2 − 1 = +1`, not zero. **It is not anomaly-free. The witness is dead and the claim
> built on it — "the SM is not the minimal rigid chiral content" — is WITHDRAWN.** I banked it,
> relayed it, and reported it before catching this.
>
> **Redone with the full anomaly set, the result reverses:**
>
> - `[SU(3)]³` forces `2·n_(3,2) = n_(3̄,1)` — **one quark doublet requires exactly two
>   anti-triplets**. The SM quark sector, forced by a single condition.
> - Over the SM-visible alphabet: **252 contents, 222 killed by `[SU(3)]³` alone, exactly TWO
>   survive** — both 15 states, both with charges **`(1/6, −2/3, 1/3, −1/2, 1)`**, and the second is
>   the conjugate of the first. **The SM generation is the unique rigid chiral anomaly-free 5-field
>   content, up to conjugation, with its hypercharge forced.**
> - **Robustness, honestly:** extending the alphabet with adjoints gives 7 survivors, and with
>   `(3,3)` gives 14. **Uniqueness is alphabet-dependent. Minimality is not — the SM is the smallest
>   survivor in every alphabet tested.**
>
> **This STRENGTHENS B1160, opposite to my first report.** Its fence — "the SM-shaping is
> observer-paid" — is more conservative than it needs to be at the rigidity threshold.
>
> **How it was caught:** tracing whether the 13-state content could sit inside the 27 forced me to
> write down what the 27 actually contains, which surfaced `(3,1)` as distinct from `(3̄,1)` — a
> distinction that matters **only** for `[SU(3)]³`, the condition I had left out.
>
> **The lesson, in a new costume:** I checked that my solutions satisfied the conditions I had
> written down, and never checked that I had written down *all* the conditions.

---

# (superseded) B8143 — B1160's fence and the 13-state witness

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

---

## Step 6 — how much of "hypercharge falls out" is object-specific?

The corrected result forces the SM **shape and charges**. So: what input did that consume?

**Everything it used:** the gauge group `SU(3)×SU(2)×U(1)`; a list of small reps; the five anomaly
conditions including `[SU(3)]³`; the Witten parity condition; the rigidity threshold `n = 5` (a
dimension count); a chirality convention.

**Object-specific tokens in executable code — `E₆`, the `27`, `m004`, the trace field, roots,
weights: NONE.** One token appears in *prose*: a comment noting that the 27 contains `(3,1)`. **That
is why I noticed `(3,1)` differs from `(3̄,1)` — which is exactly what surfaced my missing `[SU(3)]³`
condition — but it is not a term in any equation**, the alphabet is the generic small-rep list, and
the extended alphabets go beyond the 27. Recorded because my own control fired on it.

> **The charges are forced generically** — B1160 says so itself (*"standard GUT model-building"*).
> **The shape is forced generically too** — this arc. **Neither is object-specific.** What *is*
> object-specific is only that the object supplies a rank-3 abelian sector in which an SM-shaped
> 15-plet is **available**.
>
> **The object supplies the arena. The anomalies supply the content.**

**Why it matters:** a result that comes out identically for anyone starting from `SU(3)×SU(2)×U(1)`
**corroborates the Standard Model but is not evidence *for* the object.** This is the B996 lesson —
*"reaching E₆ is generic; specialness lives in the grammar"* — one level further down, now at the
matter content.

**Not a refutation.** B1160 fences this itself. This quantifies the fence, and extends it from the
charges to the shape.

**Novelty: none claimed** for the uniqueness result, which is very likely known in the model-building
literature. The claim is the scoping conclusion only.
