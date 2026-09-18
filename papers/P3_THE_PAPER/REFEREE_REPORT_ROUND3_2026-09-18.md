# Referee report, round 3 — the project, not the projection

**Scope:** the whole repository, all branches, at 2026-09-18. Rounds 1 and 2 reviewed
`papers/P3_THE_PAPER/main.tex` against `origin/main`, then added one lane. That was too narrow, and
it made my summary wrong. This round corrects it.

**Finding in one line: the manuscript is a lossy projection of its own project, and the three results
I would most want a referee to see are not in it.**

---

## 0. Why this report exists

I treated `main` plus the paper as the work. `main` is **101 commits** — a curated line. The work
lives in four lanes of roughly three thousand commits each, and **two of them share no history with
`main` at all** (different root commits, no merge base). Reviewing the paper and calling it the
project was a methodological error on my part, and it produced a §6.2 summary in round 2 —
"seven routes, all negative" — that is simply false.

| lane | commits | root | last active | what it is |
|---|---|---|---|---|
| `main` | 101 | `1e72e062` | 09-17 | the curated line the paper is generated from |
| `sep16-branch` | 146 | `1e72e062` | 09-17 | the `xb` seat; sealed pre-registrations `xB019`–`xB023` |
| `claude/standard-model-derivation-0qt6ao` | 2967 | `517783f2` | 09-16 | the SM-derivation seat; the E₆ route and its capstone |
| `audit/physical-bridge-2026-09-05` | 2965 | `517783f2` | 09-16 | the codex/audit operator; the 4-D physical bridge |
| `claude/physics-seat-evaluation-8dkbrl` | 3001 | `517783f2` | 09-06 | physics-seat evaluation; dormant |

---

## 1. There is a Standard-Model-shaped chiral generation, and the paper does not report it

`claude/standard-model-derivation-0qt6ao`, **B1374 and B1375**, both 2026-09-16 — the day before the
submitted draft.

This is not "the index is non-zero on a cover". It is **all five charged sectors — Q, u^c, e^c, d^c,
L — firing together at ±1, with every other sector zero, anomaly-free**: a complete Standard-Model
generation, chiral, on the object's own cyclic tower.

| level | | generation-shaped backgrounds | net count |
|---|---|---|---|
| Y₂ = m206 | | 0 | — |
| Y₃ = s961 | nothing fires | 0 | — |
| Y₄ = t12839 | | **12 800** | exactly one, ±1 |
| Y₅ = o10_150696 | | **800** | exactly one, ±1 |
| Y₆ | | **67 200** | exactly one, ±1 |

**80 800 backgrounds, every one carrying exactly one net generation — never two, never three.**

### 1.1 What I verified myself

Everything below is my own code; SnapPy supplies the covers' presentations and nothing else.

**The tower's identity.** Y₂ ≅ m206, Y₃ ≅ s961, Y₄ ≅ t12839, Y₅ ≅ o10_150696 — all confirmed by
isometry — and all five H₁ groups exact: ℤ/5⊕ℤ, ℤ/4⊕ℤ/4⊕ℤ, ℤ/3⊕ℤ/15⊕ℤ, ℤ/11⊕ℤ/11⊕ℤ, ℤ/8⊕ℤ/40⊕ℤ.

**The non-split loci** (`r5_tower_loci.py`): characters enumerated as the kernel of the abelianised
relator matrix mod N, h¹ by my own Fox calculus over three prime fields with Nth roots of unity,
agreeing across all three. The counts reconcile with the record **exactly**:

| level | my loci | non-trivial | record | |
|---|---|---|---|---|
| Y₂ | 10 | **9** | 9 | ✔ |
| Y₃ | 32 | **31** | 31 | ✔ |
| Y₄ | 90 | **89** | 89 | ✔ |
| Y₅ (over 661 alone) | 246 | **245** | 241 + "4 spurious on 661" | ✔ |

That last row is the sharpest of the four: computing over the single prime 661 I get 245, and the
record says 241 after intersecting three primes, with **exactly four spurious on 661**. My
single-prime run reproduces their single-prime artefact.

**And on Y₄, B1374's finer statement, to the digit.** It says the 64 generation-carrying loci are
"χ of order 15 with χ(λ) = 1, or 30 with χ(λ) = −1". I get:

```
(order, χ(longitude)) -> {(1,+1):1, (2,-1):1, (3,+1):8, (5,+1):4,
                          (6,-1):8, (10,-1):4, (15,+1):32, (30,-1):32}
```

32 + 32 = **64**, with precisely the order/longitude pairing claimed.

**The cusp condition.** B1374 explains that a generation needs χ² = 1 on the peripheral subgroup and
that "the tower's null-homologous lifted longitude grants it and the siblings' meridians deny it".
Confirmed: on Y₄ and Y₅ the peripheral curve in question has all exponent sums zero, so χ = 1 on it
is **forced at every locus**; on Y₂ and Y₃ it is not.

### 1.2 The mechanism — and why the answer is one and not three

> **h¹(χ²) = 1 at every non-split locus, on every level.** Y₂: 10/10. Y₃: 32/32. Y₄: 90/90.
> Y₅: 246/246. Never 2, never 3.

That is the whole reason the count is one. Each firing sector contributes n(V) − n(V*) = 1 − 0,
because there is exactly **one** interior class. A locus with h¹ = 3 would give three generations;
there is no such locus anywhere on the tower.

And the firing signature the record reports on all 80 800 backgrounds — **(a₀,a₁,t₀,r₁) = (0,1,1,0)
for V against (0,2,1,2) for V\*** — is *exactly* the signature I computed independently on the m010
witness in round 2 §6. The instrument I verified is the instrument this runs on.

### 1.3 What I did not verify

The 80 800 count itself, the one-per-background law across all of them, and the exact ℚ(ζ₆₀)/ℚ(ζ₁₃₂)
re-derivations. I verified the scaffolding, the loci, the mechanism and the instrument — not the
enumeration.

### 1.4 What the manuscript does with it

Seven words: *"on the object's own degree-four cyclic cover t12839"*, inside a list of ±1 values.
The strings `12 800`, `80 800`, `one generation`, `generation-shaped` appear **nowhere in
main.tex**.

---

## 2. The lane's own capstone says more than the paper does

`docs/THE_VERDICT_OF_THE_OBJECT_2026-09-16.md`, same lane. Its one-paragraph verdict is
**"the figure-eight knot complement fixes the Standard Model's structure and withholds its
chirality"**, with **"the count is 0 of 19"** — zero of the Standard Model's free parameters — and
every line naming the arc that proves it.

What it lists as fixed *from the object alone*: E₆ (B1268); the 27 with its **single** cubic coupling
(B1276); **the Standard Model sitting in E₆ in exactly one way up to conjugacy** — "120 A₂'s, 720
pairs, three hypercharges, all one orbit" (B1366); the SM centraliser SU(2)_β × U(1)² and the
13-dimensional double centraliser (B1269, B1364); U(1)_η with its charge table (B1365); the hollow
tree-level texture (B1273, B1361).

Two of those I can check and both hold: **E₆ has exactly 120 A₂ subsystems** (1440 ordered pairs at
120°, ÷12; and 120 by direct enumeration), and the **hollow-texture identity σ₁ = σ₂ + σ₃** I
verified numerically in round 1. I have *not* verified the "all one orbit" part, which is the load
of B1366.

**Why this matters for the manuscript.** §6's scope note says the colour frame and the
Standard-Model shaping are inputs because *"our sources do not agree here, and we adopt the weakest
reading"*. B1366, dated the day before the draft, appears to settle that disagreement in the
*strong* direction — one conjugacy class. If B1366 holds, the paper is hedging against a question
its own project has answered, and understating its best structural result.

The capstone also carries three chirality theorems the paper does not state as such: closed closings
vector-like by χ(Q;L) = 0 plus Poincaré duality (B1351); point-localised matter cannot split the
Higgs doublets from the exotic triplets, so **every apex design decays the proton** — 9 300
configurations, no exception (B1367); and bulk matter with the SM unbroken is never a chiral
generation (B1368). None verified by me.

---

## 3. And there is a computed reason why the object itself returns zero

`sep16-branch`, **xB021**, 2026-09-17 — the draft's own date. Pre-registration sealed and **pushed
before `verification/` existed**, with a binding kill condition that did not fire.

The three bits act on the Chern–Simons invariant in ℝ/½ℤ: A5 (knot-ness) `x ↦ x + ¼`; A6
(orientation, the squaring) and A7 (the LR/RL order) both `x ↦ −x`. I verified the group theory
directly:

```
|<A5,A6,A7>| = 4     stabiliser of CS = 0 : order 2     orbit of 0 : {0, 1/4}
orbit-stabiliser: 2 x 2 = 4        A6, A7 fix 0 ;  A5 moves it
```

**So the two bits the manuscript calls *withheld* and *relational* are exactly the object's own
stabiliser** — and a fixed point cannot report on its own stabiliser. 9 of 12 banked negatives are
instances of this shape; the 3 misses are named and are all arithmetic.

And a detail the lane does not draw out, which I checked: the orbit **{0, ¼} is exactly
{CS(m004), CS(m003)}**. m003 is the sibling that §2 of the paper says is separated from m004 by the
Chern–Simons invariant and by nothing else the construction uses. The orbit direction *is* the
knot-ness bit. That is a genuinely elegant closing of §2's loop, and it is not in the paper.

---

## 4. Verification ledger for this round

| claim | status |
|---|---|
| tower identities Y₂–Y₅ and all five H₁ | **verified** |
| non-split locus counts, four levels, against the record | **verified, incl. the 4 spurious on 661** |
| Y₄'s 64 loci with the order/longitude pairing | **verified** |
| h¹(χ²) = 1 at every locus, every level | **verified** |
| the cusp/T5 condition forced on Y₄, Y₅, denied on Y₂, Y₃ | **verified** |
| firing signature (0,1,1,0)/(0,2,1,2) | **verified** (round 2, on m010) |
| E₆ has 120 A₂ subsystems | **verified** |
| hollow texture σ₁ = σ₂ + σ₃ | **verified** (round 1) |
| xB021 orbit–stabiliser, and orbit = {CS(m004), CS(m003)} | **verified** |
| the 80 800 count; one-per-background law; exact ℚ(ζ) runs | not verified |
| B1366 "all one orbit"; B1351; B1367; B1368 | not verified |

---

## 5. Revised verdict

**On the paper as submitted:** rounds 1 and 2 stand. The mathematics I could check is correct, the
packaging defects of round 2 §2 remain, and the framing objection stands.

**On the project:** my earlier answers were drawn from the projection and two of them were wrong.

- *"Seven routes, all negative"* — **wrong**. The tower route is positive.
- *"Nothing new about the Standard Model"* — true of the paper, **false of the project**.
- *"The three is not the limit of anything built"* — still true, and now better: the mechanism that
  *does* make chirality makes **one**, and the reason is h¹ = 1 at every locus.

**What stays true and matters.** The generations fire on **non-semisimple** backgrounds — exactly
the admissibility question the paper itself grades with a prior against — and B1374/B1375 fence
themselves identically ("no physics reading, no value, no three"). The capstone's own verdict is
"0 of 19". xB021 calls itself "a diagnosis, not a door". **This is still not derived physics**, and
nobody in the project claims it is.

But the honest description of the project is no longer "a careful negative". It is: *the object
fixes E₆, the 27 and one cubic coupling, and (pending B1366) a unique Standard-Model embedding; it
withholds chirality, and there is now a computed reason why — the withheld bits are its own
stabiliser; and on its tower, on non-semisimple backgrounds, exactly one chiral generation appears,
never three.*

**My single strongest recommendation, superseding everything in rounds 1 and 2:** the paper is not
reporting its own project. Three results dated 09-16 and 09-17 — the tower's generation, the
capstone's uniqueness of the embedding, and the stabiliser diagnosis — are absent, reduced to a
parenthetical, or superseded-but-hedged. Whatever else is done to this manuscript, it should be
brought level with the work it comes from.

---

*Reproductions for this round: `referee_2026-09-17/scripts/r5_tower_loci.py` (loci, h¹, orders,
cusp condition), plus the round-2 scripts. SnapPy is used for presentations and isometries only;
all characters, Fox calculus, ranks, cohomology and group theory are this referee's own code.*
