# B1400 — THE SIX SWEEPS, INTAKEN: the headline reproduces to the digit and is UNDERSTATED, and one absence survives a diacritic trap

**Incoming:** `chat1_SWEEPS_2026-09-12.zip` — a six-sweep audit report plus two scripts.
**Every number recomputed on this bench.** Nothing read from the report.

> **Verdict in one line: five sweeps reproduce, the headline finding reproduces *exactly* and
> turns out to be an UNDERSTATEMENT, one covered-term count is wrong and immaterial, and the
> absent-term list is right on `origin/main` while EIGHT of its sixteen terms are already present
> on this branch — work the auditing seat cannot see.**

---

## 1. SWEEP 6, the headline — REPRODUCES TO EVERY DIGIT

The claim: the 2T-surjection rate (`π₁(M) ↠ SL(2,3)`) declines with census depth, because
`OrientableCuspedCensus` is volume-ordered and every scan starts at index 0.

| slice | their mean vol | **mine** | their rate | **mine** |
|---|---|---|---|---|
| `[0:800]` | 4.183 | **4.183** | 34.25 % | **34.25 %** |
| `[20000:20800]` | 4.767 | **4.767** | 29.38 % | **29.38 %** |
| `[80000:80800]` | 5.650 | **5.650** | 21.12 % | **21.12 %** |

Exact on all six numbers. **And B993's cornerstone control reproduces exactly:** m004 has
**48 raw surjections**, `/|Aut(2T)| = 24` → **exactly 2**.

### 1.1 The confound I went looking for — and it is NOT there

Their `census_bias.py` returns `None` for any presentation with **more than 3 generators** and
silently skips it, while reporting neither `n` nor the skip count. Generator count correlates with
complexity, which is the very variable the finding is about, so a depth-dependent **skip rate**
could manufacture the decline. **Measured: `skipped = 0` at all three slices** — every one of the
2400 manifolds had ≤ 3 generators. The skip confound does not arise. Their number is clean.

### 1.2 But stratifying by generator count REFINES the finding, and the aggregate UNDERSTATES it

The generator *mix* does shift hard with depth, and the two strata behave completely differently:

| slice | all | **2-generator** | **3-generator** |
|---|---|---|---|
| `[0:800]` | 34.25 % (n=800) | **34.23 %** (n=745) | 34.55 % (n=55) |
| `[20000:20800]` | 29.38 % (n=800) | **28.72 %** (n=679) | 33.06 % (n=121) |
| `[80000:80800]` | 21.12 % (n=800) | **15.36 %** (n=534) | 32.71 % (n=266) |

Two-proportion `z`, front → deepest: **all `+5.87`**; **2-generator `+7.56`**;
**3-generator `+0.26`**. The 3-generator share grows `6.9 % → 15.1 % → 33.2 %`.

> ### The decline lives ENTIRELY in the 2-generator stratum. Among 3-generator groups the rate is FLAT (`z = +0.26`).
> So the aggregate `34 % → 21 %` is a **blend of a `34 % → 15 %` collapse with a flat `33 %`** — and
> because the non-declining 3-generator population *grows* with depth, it **props the aggregate up**.
> **Their finding is real and their number is right; the effect in the stratum where it acts is
> more than twice what the headline shows.**

**This sharpens their own standing note.** They wrote: *"Any property correlating with complexity is
systematically mis-estimated by the default iteration order… Slice at depth, or sample at random."*
Slicing at depth is necessary and **not sufficient** — a depth slice still mixes strata whose rates
move in different directions. **Stratify by presentation complexity as well as slicing at depth**,
or the aggregate hides both the size of the effect and the fact that one stratum has none.

### 1.3 Their reading of what it does to B993 is CORRECT, including the direction

B993's `~1 in 3` is measured on a 400-manifold sample — necessarily the front — and **B993 states
that sample in its own text** (`"400-manifold census sample"`, verified). So it is correctly
computed and correctly reported for its declared sample; the census-wide rate is lower; the atom is
**rarer** than the front suggests and m004 correspondingly **more** distinguished. **The bias runs
against the programme's own skepticism, which is the safe direction, and inflates nothing.** Their
self-assessment on this is accurate and is adopted.

### 1.4 The number they retract never reached us

They withdraw their own `|κ−2|` statistic (*"1 in 3427"*, measured on the front 4000) as
*"biased in the direction that flatters it and should not be quoted."* **Checked: `3427` appears as
a standalone number in zero files of our prose or verdicts.** Nothing to withdraw on our side.
Their Jørgensen result does not rest on it either — that is Callahan's theorem, as they say.

## 2. SWEEP 1 — EXACT

`CLAIMS.md`: **231 lines**; `"base rate"` **0**, `"prereg"` **0**, `"control"` **3**,
`"generic"` **4**. All five numbers reproduce. Their reading is right and is not a defect finding:
base-rate discipline lives in the arcs, and the register does not carry that provenance.

## 3. SWEEP 3 — the finding REPRODUCES, their hypothesis was wrong, and they say so

**Arcs never mentioned anywhere: 0.** (My counts: 1226 arcs with a verdict id, 1359 distinct arc-ids
in arc text, against their 1240 / 1386 — the difference is the **commit**, not the method: this
clone carries branch-only arcs. The finding is identical.) Credit where due: they had predicted
orphans, found none, and recorded *"My hypothesis was wrong and the corpus is better connected than
I guessed."*

## 4. SWEEP 4 — VERIFIED on all five claims

| claim | required text | present? |
|---|---|---|
| P53 | "among the ten exceptional fillings" | **yes** |
| P48 | "imaginary-quadratic trace fields" (floor −4) | **yes** |
| P10 | "**not** an independent proof" + NEEDS-SPECIALIST | **yes**, verbatim |
| P43 | dated `CORRECTED 2026-07-15` | **yes** |
| P46 | dated `SPLIT 2026-07-15` | **yes** |

Their conclusion — the register already declares its comparison classes and demotes itself — holds.
**No action, as they say.**

## 5. SWEEP 5 — 12 of 13 covered counts exact; the absent list right on main; EIGHT already entered here

**A tooling correction of mine first.** I initially re-ran with `git grep -ilw` and got `L-space = 0`
against their 16. `-w` fails on **hyphenated** terms; with their `-il` it is exactly **16**. Their
flag was right and mine was wrong — recorded because it is the same shape of error as the sweep it
was checking.

**COVERED: 12 of 13 reproduce exactly.** One differs: **Bianchi — they report 29, measured 115.**
Immaterial to the finding (covered on either count) but it is an error in their table.

**ABSENT: all 16 confirmed at 0 on `origin/main`.** But:

> ### EIGHT of the sixteen are ALREADY PRESENT on this branch — the territory has been entered.

| term | files on this branch | supplied by |
|---|---|---|
| Kronheimer | 3 | **B1343** |
| ADHM | 2 | **B1343** |
| Nakajima | 2 | **B1343** |
| quiver variety | 1 | **B1343** |
| elliptic surface | 2 | **B1343** |
| minimal resolution | 1 | **B1343** |
| Minahan–Nemeschansky | 1 | (views) |
| **waist size** | 2 | **B1345** |

**And the precedent they cite for the yield has already paid out.** They write: *"`waist size` was 0
files, and behind it was Adams 2002 + Callahan 2009 — a uniqueness theorem for the object."* B1345
used exactly Adams 2002 waist size and Callahan 2009 uniqueness, and found that **`J(m004) = 1` IS
B309's already-banked "unit obstruction"** seen from the other side. So the blind-spot thesis is
sound *and* its most cited example is spent.

**This is a cross-seat visibility problem, not an error by either side:** they audit `origin/main`,
which is correct and conservative; the answering work sits unmerged on this branch. It is the same
class as **E71** (branch-local numbering) and **E53** (a banked result not reaching the surfaces) —
a seat cannot audit what has not landed.

### 5.1 A near-miss of my own, recorded rather than quietly dropped

Their list includes `"Jorgensen inequality"` at 0 files. I read that as an **E54 false absence**,
because `"Jørgensen"` with the Danish **ø** returns **9 files on `origin/main`** — the exact shape of
the E54 instance already in the ledger (a figure-eight search covering the ﬁ ligature but not the
digit spelling). **I was wrong, and checked before reporting it: all nine hits are
ANDERSEN–JØRGENSEN** (arXiv:1206.2552 — TQFT, Gauss sums, growth rates), **a different person from
Troels Jørgensen** of the Kleinian-group inequality. Their absence claim holds at **topic** level,
not merely as a phrase. **E72 shape — one name, two people** — and the lesson cuts both ways: the
diacritic check was the right instinct and the attribution check was what made it honest.

## 6. SWEEP 2 — the located facts verify

B993 **states its own 400-manifold sample in-arc** (verified); B1330's **952 in-domain sectors**
(verified) were on **v2873**, which our own B1346 F1 table records as **PROTECTED** (verified). Their
observation that a sample-size column next to `CLAIMS.md` rows "would be cheap" is a fair, cheap
suggestion and is left to the register's owner.

## 7. What this arc changes, and what it does not

**Changes:** the census-bias finding is **adopted and sharpened** — stratify by presentation
complexity, not only by depth, because the aggregate mixes a collapsing stratum with a flat one and
understates the effect by better than a factor of two. **B993 is not corrected** — it is correct for
its declared sample, and the bias runs in the safe direction.

**Does not change:** nothing here touches `CLAIMS.md`, F2 or Gate 5. No value is read against any
measurement. The eight now-present terms are a **visibility** note, not a claim that the blind spot
is closed — B1343's own verdict is that deriving those faces is *free and therefore evidentially
empty*, and B1345's Jørgensen number is a **re-derivation** of B309, not a new result. **The
territory has been entered; it has not yet paid.**
