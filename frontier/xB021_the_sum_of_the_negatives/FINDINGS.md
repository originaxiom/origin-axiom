# xB021 — THE SUM OF THE NEGATIVES: the object is a fixed point, and a fixed point cannot report on its own stabiliser

**Seat `xb`, `sep16-branch`, 2026-09-17. PREREGISTRATION sealed `42c442a2…` and PUSHED at `210bb0e`
before `verification/` existed, with a **binding kill condition** on the audit and the **honest limit
declared in advance**. Verdict: PROVED (a diagnosis, not a door).**

Gate 5 absolute: no value, no generation count, no physics reading, nothing to `CLAIMS.md`.

---

## 0. The instruction

> *"the sum of all negatives should clarify the riddle for us and help us understand why our question
> might be ill posed. maybe there's a mechanism to make them interact and have what we need emerge"*

## 1. S1 — the negatives have one shape, and it is computed

The three bits act on `CS ∈ ℝ/½ℤ` — **each action established, not assumed**:

| bit | action | source |
|---|---|---|
| **A5** (the `−I` / knot-ness bit) | `x ↦ x + ¼` | xB015 K6 — 494/494 words, 50 digits |
| **A7** (the `LR`/`RL` order bit) | `x ↦ −x` | xB018 C5 — 240/240 words, 40 digits |
| **A6** (orientation / the squaring) | `x ↦ −x` (complex conjugation) | xB020 H2 — derived |

> **`|⟨A5, A6, A7⟩| = 4`. The STABILISER of the object's value `CS = 0` is of order 2 and is exactly
> `{A6, A7}`. The ORBIT of `0` is `{0, ¼}`. Orbit–stabiliser: `4 = 2 × 2`.
> **A5 is the orbit direction; A6 and A7 are the stabiliser.**

Not an analogy — a computed orbit–stabiliser decomposition.

## 2. S2 — the audit, with its misses listed

**9 of 12** banked negatives are instances of *"the thing asked about is in the stabiliser."*
The kill condition (fewer than half) does not fire.

**And the three that DO NOT fit are named, as the seal required** — xB013 Add.1 (selection among an
infinite family), xB017 (the Bianchi base rate), xB017 Add.2/3 (the orbifold's covering theory).
**What they have in common is itself informative: every miss is ARITHMETIC.** The hypothesis covers
the CS-facing negatives and nothing else — **exactly the scope the seal named in advance.**

## 3. S3 — why the question is ill-posed

The object is **defined** as the fixed point: A3 and A6 make it orientable and minimal, and that is
what puts it at `CS = 0` (xB020: orientation double covers are 2-torsion **by construction**; xB019:
the squaring buys exactly this).

> **A fixed point cannot report on its own stabiliser.** Asking *"what does the object tell us about
> A6 or A7?"* is not **hard** — it is **empty**, because those are precisely the transformations
> under which the object does not move.
>
> **So the walls are not obstacles standing in front of an answer. They are the shape of the
> stabiliser, seen from inside the fixed point.**

**Scope:** this covers questions whose answer would have to be carried **by the stabiliser acting on
`CS`**. It does **not** cover the arithmetic questions (S2's three misses), nor anything about
volume, `H₁` or the trace field.

## 4. S4 — the mechanism, and its honest limit

**If the information is in the orbit, work with the orbit.** The ladder is real and measured:

| locus | values of `CS` realised |
|---|---|
| the object | **1** — `{0}` |
| the 2-torsion orbit (the sisters, via A5) | **2** — `{0, ¼}` |
| **the family** (xB015, B1186's 112 with mirrors) | **12** — surjective onto ℤ/12, against a 1.51 % base rate |

> **1 → 2 → 12. The orbit does carry what the point does not.** That is the mechanism the instruction
> asked for, and it is real.

**AND THE LIMIT, declared in the seal and not softened here.** xB016 already established that **an
index cannot fix the free anchor**: `σ` is a **continuous** parameter of complex Chern–Simons and
**nothing couples it to `k`** (Witten arXiv:1001.2933 eq. 2.2; Gukov hep-th/0306165 §1.1). The orbit's
content is **topological — an integer mod 12 — and a value is not an integer mod 12.**

> **The orbit has information. It does not, so far, have the answer.** *"The orbit carries what the
> point does not"* must not be read as *"the orbit carries what we need."*

## 5. S5 — what this does not do

It derives **no value** — no `σ`, no `c`, no coupling. It does **not replace B1234**, which already
found the mirror upstream of eight walls; **it extends that from one stabiliser element to the whole
stabiliser**, and supplies the orbit–stabiliser count that makes it theorem-shaped rather than a
join. It does not cover the arithmetic negatives.

> **It re-poses a question. That is its entire content, and calling it more would be the exact
> failure this session has corrected four times.**

## 6. S6 — verdict

**The sum of the negatives has one shape, computed not asserted.** The question is ill-posed because
it asks a fixed point to report on its stabiliser. The mechanism is to move to the orbit, and the
orbit is real — **1 → 2 → 12**. The limit is that an index is not a value.

**A DIAGNOSIS, NOT A DOOR.**

**AXES HELD FIXED, named as the rule requires:** **`CS` only** — volume, `H₁` and the trace field are
not analysed as group actions, and the three arithmetic negatives fall outside · **the three bits
only**; B1083's `C`/`P` torsor is not re-derived · the negatives audited are **this seat's arcs plus
cited older ones**; the record's full negative inventory is **not swept**.

**Locks / artifacts:** `verification/fixed_point.py` (S1–S6), `verification/fixed_point.json`,
`verification/fixed_point.out`.
