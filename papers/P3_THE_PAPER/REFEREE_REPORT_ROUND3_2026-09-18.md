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


---

## 6. A new result, following from the verified mechanism: three is out of reach

Round 3 verified that the tower's count is one **because** h¹(χ²) = 1 at every non-split locus. That
makes the three-generation question sharp and finite: **by this mechanism, three generations require
a genuine extension locus with h¹(χ²) = 3.** So I went looking for one
(`referee_2026-09-17/scripts/r6_h1_three.py`) — every cover of m004 to degree 8, plus the named
members of the family, over the full character group of order dividing 60.

**A trap first, which I fell into and report rather than hide.** A raw scan finds 32 loci with
h¹(χ²) = 3 on the degree-7 covers. They are spurious: those χ have order 2, so χ² is *trivial* and
h¹(χ²) = b₁, which is 3 for free on a three-cusped cover. Filtering to χ² non-trivial — the genuine
extension loci, the ones that actually carry a non-split ρ_χ — the picture is:

| h¹(χ²) | genuine loci found |
|---|---|
| 1 | 20 904 |
| 2 | 456 |
| **3** | **0** |

And the 456 twos are **never on a one-cusped manifold**. They occur only on covers with 2 or 3
cusps, and on s959 (two-cusped).

**What that means.** The count this mechanism produces is bounded by h¹ at the locus. On everything
one-cusped — where the index instrument is defined and where the generation actually fires — it is
**1, everywhere, without exception**. Raising it requires going multi-cusped, which (a) tops out at
**2**, never 3, in everything scanned, and (b) leaves the domain of the one-cusped instrument, whose
several-cusp form the record itself grades as not reproducible from a clean checkout.

So: **three generations are not reachable by the tower mechanism in anything within reach of m004,**
and the obstruction is not subtle — it is the dimension of a first cohomology group, and it is one.

This is a stronger and more specific statement than the paper's "the count of three is not produced
by this mechanism on any level up to six", because it is not about levels. It is about every cover to
degree 8 and the whole named family, and it says *why*: h¹ is 1, and where it grows it grows to 2.

**The remaining question, well-posed and finite:** is there any manifold in m004's commensurability
class, at any degree, with a genuine extension locus at h¹(χ²) = 3? I found none to degree 8. If the
answer is none, that is a no-go theorem for three generations from this construction, and it would be
the cleanest negative the programme has.

---

## 7. Why it is out of reach: the count is a corank, and the object has one cusp

§6 established the fact. This is the reason, and it is checkable
(`referee_2026-09-17/scripts/r7_corank_bound.py`).

**The count is a corank.** At a non-trivial character, h¹(χ) = (g − rank J(χ)) − 1, where J is the
Fox Jacobian. So "h¹ = k" is not a quantity the construction chooses; it is the statement that a
matrix drops rank by k. The generation count the tower produces is the corank of a Jacobian at a
point of the character variety.

**m004's own Alexander polynomial says the drop is one.** Computed from the same Fox Jacobian, no
Sage, own arithmetic:

```
presentation   <a,b | aaabABBAb>      phi:  a -> t^0,  b -> t^1
d r/d a  =  -(t^2 - 3t + 1)/t         d r/d b  =  0
Delta(t) =  t^2 - 3t + 1              discriminant 5  ->  SEPARABLE
roots    =  (3 +- sqrt 5)/2           |roots| = 0.381966, 2.618034   -> not on the unit circle
```

Two consequences, both of them structural rather than incidental:

1. No root of Δ is a root of unity, so **h¹(χ) = 0 at every non-trivial finite-order character of
   m004 itself.** The extension loci cannot exist downstairs; they only appear on covers. That is
   exactly what r5 and r6 found, and it is now explained rather than observed.
2. Δ is **separable**. Where a rank drop does occur it occurs at a simple root, so the drop is 1.
   h¹ = 1 is not a small-sample artefact of the levels scanned — it is a root multiplicity.

**The cusp count is the ceiling.** Rerunning the r6 scan with the number of cusps recorded, over
every cover of m004 to degree 8 and the named family (42 manifolds profiled):

| cusps (= b₁) | genuine-locus h¹(χ²) distribution | max h¹ |
|---|---|---|
| 1 | {1: 1056} | **1** |
| 2 | {1: 3736, 2: 112} | 2 |
| 3 | {1: 16112, 2: 344} | 2 |

**One-cusped manifolds carrying h¹ ≥ 2: none.** Not one, in 1056 loci.

The naive determinantal count (corank k has codimension k², so h¹ = k wants b₁ ≥ k²) is too crude —
it predicts max 1 at b₁ = 2 and 3, and the scan finds 2. The observed bound is the weaker
**max h¹ ≤ b₁**, and it is not saturated: at three cusps the maximum is still 2.

**The pincer.** Three generations by this mechanism need h¹ = 3, which needs b₁ ≥ 3, which needs at
least three cusps. But the single variational fact in the whole construction — Jørgensen/Callahan
minimality, which is what selects m004 in the first place and which §1 of the paper leans on
entirely — is a statement about **one-cusped** manifolds. The fact that picks the object is the same
fact that caps its b₁ at 1, and b₁ = 1 is the fact that caps the count at 1. Going multi-cusped to
raise the count forfeits the reason for choosing the object, and in everything scanned it does not
even reach 3.

So the honest form of the negative is not "three was not found up to level six". It is: **the count
this construction computes is a corank bounded by b₁, the object's b₁ is 1 because it is the minimal
one-cusped manifold, and one is therefore the only answer the machine can give.** Whether that is a
theorem — no manifold in the commensurability class, at any degree, with a genuine locus at
h¹(χ²) = 3 — remains open; everything scanned to degree 8 is consistent with it, and the Alexander
separability above is the shape a proof would take.

---

## 8. Enriching the first step: what it would have to supply, and what it actually supplies

The construction is one variational step (Jørgensen/Callahan minimality selects m004) followed by
pure invariant extraction, and an equivariant machine cannot emit a non-invariant number. So the
only way to reach parameters is to **enrich the first step** — make it range over a space that
contains the parameters as coordinates. Two scripts price that
(`r8_enrichment_budget.py`, `r9_enrich_coefficients.py`).

### 8.1 The parameter budget

m004: volume 2.0298832128, **1 cusp**, H₁ = ℤ, symmetry group **D4 of order 8**, amphichiral.

| enrichment | complex dim | **real dim** | vs the 19 needed |
|---|---|---|---|
| bare object (complete structure, Mostow) | 0 | 0 | short by 19 |
| its own moduli (Dehn surgery space; Thurston: dim = cusps) | 1 | **2** | short by 17 |
| flat SU(2) connections (rank 1) | 1 | 2 | short by 17 |
| flat SU(3)×SU(2)×U(1) — *the SM's own group*, rank 4 | 4 | **8** | short by 11 |
| flat SO(10) (rank 5) | 5 | 10 | short by 9 |
| flat E₆ (rank 6) | 6 | 12 | short by 7 |
| flat E₈ (rank 8) | 8 | 16 | short by 3 |
| flat E₈×E₈ (rank 16) | 16 | 32 | enough |

With one cusp the character variety of a rank-r group has r complex dimensions, so **no group of
rank ≤ 9 has room for 19 real numbers.** The SM's own gauge group supplies eight real coordinates,
and they are all gauge-sector — the nine Yukawas are not in that space at all.

### 8.2 The hierarchy, and why it is the wrong place to start

The only known geometric mechanism producing a Yukawa hierarchy is exponentially suppressed overlap,
and hyperbolic geometry supplies exponential decay for free. Necessary condition: does the object's
own length spectrum span the range? Computed:

```
L <= 2.0: N =   6      L <= 4.0: N =  50        fit  N(L) ~ 0.729 * exp(1.046 L)
L <= 3.0: N =  16      L <= 5.0: N = 134
systole = 1.087070145     exp(-systole) = 0.337
top / electron = 337945   ->  needs a length gap dL = 12.7306
```

The range exists — the spectrum is infinite, so that condition passes and kills nothing. But
extrapolating the fit, the window L ≤ systole + 12.73 holds **on the order of 1.4 million
geodesics**, to fit **nine** Yukawas. An enrichment that supplies more freedom than the data
constrains can fit the parameters; it cannot predict them. That is the criterion any enrichment must
meet, and it is the criterion minimality meets perfectly: **zero choices in, one object out.**

### 8.3 The enrichment that keeps the aesthetic — and fails

The one enrichment that costs nothing is to keep the object and make the **bundle** bigger: replace
rank-one characters by Sym^m of the geometric representation, which is the coefficient system the
record's index instrument already uses. If dim H¹ climbs with m, §7's corank bound is a statement
about rank-one coefficients only and the cap is an artefact of the instrument.

`r9_enrich_coefficients.py` builds the figure-eight's parabolic representation from scratch over
ℚ(u), u² − u + 1 = 0 — found by search, not assumed, and *filtered by its Alexander polynomial*
(the search also returns ω = −1, which satisfies the relator but gives the **trefoil**, Δ = t² − t + 1;
the figure-eight solution is ω = u, relator `aBAbaBabAB`, Δ = t² − 3t + 1, cross-checked):

| m | dim Sym^m | dim H⁰ | **dim H¹** |
|---|---|---|---|
| 1, 3, 5, 7, 9, 11, 13 | 2 … 14 | 0 | **0** |
| 2, 4, 6, 8, 10, 12, 14 | 3 … 15 | 0 | **1** |

**dim H¹ ∈ {0, 1} for every m from 1 to 14. It never reaches 2, let alone 3.**

So the cap survives the enrichment. The bound is about the object, not the instrument — and the
obvious free enrichment does not move it.

### 8.4 What this leaves

- **The count cannot be rescued by enriching the first step.** The corank is bounded by b₁ = 1, the
  bundle enrichment does not lift it, and raising b₁ means abandoning the one-cusped minimality that
  selects the object. Three generations and the 19 parameters are two different problems; enriching
  the selection addresses at most the second.
- **The realistic target is 3 of 19, not 19 of 19.** Flat connections for a rank-4 group carry eight
  real coordinates with a natural functional (Chern–Simons) whose critical points are the flat
  connections. Three gauge couplings is the kind of quantity that space can hold. Going from 0 to 3
  would change the programme's standing entirely.
- **The gate is whether the group is forced.** The programme's claim is "no input beyond the minimal
  object". An enrichment that *chooses* G pays more bits than it earns. The object hands over D4
  (finite — no continuous moduli), ℚ(√−3), and the covering tower. **None of those supplies a
  continuous group of rank ≥ 3.** Finding a forced G, or proving there is none, is the highest-value
  open problem for this direction — higher than any further computation on the existing lanes.
- **Yukawas last, not first.** 1.4 million candidate lengths against nine numbers is the Koide
  failure mode at scale. The xB021 discipline — sealed pre-registration with a binding kill
  condition — should be applied to the *enrichment's bit budget* before any such computation is run.

---

## 9. CORRECTION: §§7–8 are largely re-derivations, one of their conclusions is wrong, and the premise behind them is false

Directed to verify the load-bearing math and to sweep the repository for already-banked solutions. Both
were done. The controls pass; the sweep does not go my way.

### 9.1 The premise was false

I wrote that the programme "fails to identify the riddle about 0 of 19". **It does not.** The record
states it as a result, with a scoreboard:

- **B1261 — THE PRICE.** *"the programme SPENDS 4 axioms + unearned identifications and BUYS 0 of the
  SM's 19 numbers; by parameter count the trade is net negative, by structural content it derives
  what the SM assumes, and the two do not convert (the selftest enforces it). The identification
  ledger is the scoreboard."*
- **L217** (registered 2026-09-14, B1406), a *programme-level filter*: *"a description that must
  account for ~19 numbers needs k(n−1) ≈ 10 — many cusps, high rank, or both — and a rigid point
  supplies zero, which no invariant extracted from it can change."*
- **OPEN_ITEMS H5** — *"the object supplies every SPACE and never a POINT"* — eight banked instances,
  five measured. That is my "structure plus a point in moduli space", already a census.
- **I-13**, the listener map, carried as *the* programme debt, with its price measured (B1348/B1349:
  freedom 12, then 48, Galois-cut to 8) and the recommendation *do not spend the row*.

My §8 presented this as something fresh eyes could see that the programme could not. That is wrong,
and it is the third time in this review I have mistaken a projection for the project.

### 9.2 One conclusion of §8 is wrong

§8.1 concluded that with one cusp there is **no room for 19**. **B1409 (2026-09-14, prereg sealed
`5618216a` and pushed before compute) found the room and then killed it better.** At the tower's
ceiling — the chiral 5-cusped degree-10 cover **L14n63694**:

```
SL(2,C):  dim_C H^1(pi_1, sl_2) =  5 = k
SL(3,C):  dim_C H^1(pi_1, sl_3) = 10 = k(n-1)   ->  20 REAL PARAMETERS
```

— *"the first count in the corpus that clears the ~19 a Standard Model needs"*, and Menal-Ferrer–Porti's
`k(n−1)` verified where the programme needs it, **with m004 as the `k = 1` positive control**. And
then the part the prereg did not anticipate: the restriction H¹(M) → H¹(∂M) is **injective in every
case**, dim H¹(∂M) = 2·dim H¹(M) exactly. **Every one of the 20 real parameters is cusp data; there
are zero interior moduli** (L219).

So the correct statement is not "the object is too small". It is: **the room exists, it is big
enough, and it is made entirely of the thing the programme already knows it cannot select.** That is
a sharper negative than mine, it is pre-registered, and it is two days older than my report.

### 9.3 Both of my recommendations are already closed, negatively

- **"3 of 19 via flat connections"** (§8.4) is closed by **B1336**: for any H with 2T ≤ H ≤ SL(2)
  principal, Z(H) is a subalgebra of an abelian algebra, so **abelian of dimension ≤ 4**, while the
  Standard-Model algebra is non-abelian of dimension 12. *No flat connection of this kind leaves it
  unbroken, whatever the holonomy.* The centraliser of the geometric (Zariski-dense) holonomy is
  **dim 0**.
- **"Enrich the coefficients with Sym^m"** (§8.3) is closed at the root by **E65 / B1260**: generation
  counting needs net chirality h¹(V) ≠ h¹(V*), and **every Sym^n of SL(2) is self-dual**, so net
  chirality is *identically zero for every such coefficient system*. E65 cost the programme four
  arcs. My computation found dim H¹ ∈ {0,1}; the record has the theorem that says the whole family
  was never a candidate.

### 9.4 What §7 reproduces rather than discovers

**B1260** already has my §7 Alexander computation, symbolically verified, and takes it further:
*"the Fox derivatives of m004's relator in the 1-dim rep are ±Δ(t)/t with Δ = t² − 3t + 1 whose roots
are φ² and φ^−2 … Δ is RECIPROCAL … so h¹(C_t) = h¹(C_{1/t}) at every value including the Alexander
root where h¹ jumps."* Reciprocity — which I did not use — is what makes the abelian sector carry no
net chirality for *every* knot.

**B307 + B1161** already have §6's conclusion by a stronger route: three interchangeable generations
need a cyclic cubic invariant trace field, no hyperbolic knot has one, and the object's quadratic
field *"permits multiplicities 1 and 2 and never 3."* That is a theorem where mine is a scan to
degree 8.

**B850** already has the representation r9 builds (A = [[1,1],[0,1]], B = [[1,0],[−ω,1]], relator
wa = bw, *"VERIFIED SYMBOLICALLY rather than cited"*) and the length spectrum, with systole
1.08707014499574 — agreeing with §8.2's 1.087070145 to every digit printed.

**The CHANGELOG** already banks h¹(Sym^even) = 1 and h¹(Sym^odd) = 0 for n = 0…16 over two
independent primes; r9 reproduces it for m = 1…14.

### 9.5 The load-bearing math, now controlled (`r10_controls.py`)

Three things §§7–8 asserted are now derived rather than cited:

| asserted | control | result |
|---|---|---|
| h¹ = 0 at every finite-order character of m004 is a fact about the object, not a blind instrument | run the same code on the **trefoil**, whose Δ = t² − t + 1 *does* have roots of unity | trefoil fires at **exactly the two order-6 characters**, h¹ = 1; m004 fires at **none**. Instrument confirmed live |
| b₁ = number of cusps (the whole content of "the corank is capped at 1") | checked on all **57** manifolds the §7 scan used | **no exceptions** |
| dim H¹(m004; Sym^m) and the cusp restriction | longitude found by search (`bABaaBAb`, ρ(λ) parabolic), t₁ computed | a₁ = 1, t₁ = 2 = 2a₁ at m = 2, 4, 6 — **independently reproducing B1409's m004 control rows, injectivity included** |

Also itemised so the target is checkable rather than a slogan: 3 couplings + 9 charged-fermion
masses + 4 CKM + 2 Higgs + 1 θ_QCD = **19**.

One defect of my own, caught by the control and recorded: the first longitude search required *both*
exponent sums to vanish, when both generators are meridians and only their **sum** must vanish. It
returned "no longitude" — a silent false negative that would have left §9.5's third row unchecked.

### 9.6 What survives as this referee's own

Little, and it should be said plainly:

- the **trefoil positive control** for the h¹ instrument (§9.5) — a control, not a result;
- the **cusps → max h¹ stratification** over an explicit 42-manifold population, and the count of
  **zero** genuine loci at h¹ = 3 — an independent empirical confirmation of B1161's theorem, not a
  new fact;
- the **order-2 trap** (a raw scan reports 32 false h¹ = 3 loci on degree-7 covers) — a methodological
  warning worth keeping;
- the **fitting-freedom count** for the hierarchy route: ~1.4 × 10⁶ geodesics in the window against
  nine Yukawas. The *principle* is banked (B995: rarity implies separation; the R11 bit-accounting);
  the number for this route I did not find in the record.

**Everything else in §§7–8 is a re-derivation, and in four places the banked version is stronger.**
The correct referee's finding is not that the programme missed the riddle. It is that the programme
stated the riddle, priced it, sealed the pricing before computing, and closed both of the routes I
proposed — and that none of this is in the paper.
