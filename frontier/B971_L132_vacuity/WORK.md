# B971 — L132 settled: the anomaly check is VACUOUS on complete 27s, and the vacuity is TRIPLE

**Date:** 2026-08-08 · **Lane:** MATHEMATICS · Gate 5 untouched · nothing to `CLAIMS.md`.
**Relation to the scout:** `PRIOR_ART_ANOMALY.md` (same cell) reached the same verdict by a
different instrument (a 2047-subset map over the object's Levi). This file does not rely on it.
Everything below is recomputed from scratch by two mutually independent routes.

**Prior art, stated first (HOUSE RULE 5):** `B864_anomaly_ledger` (2026-08-03) already computed
this ledger over the E₆ chain. **This cell REPRODUCES B864; it does not discover.** What is new
here is (a) the *degree* of the vacuity, quantified, and (b) a precise scope-note on B864's
uniqueness headline.

---

## 0. Two routes, so that nothing load-bearing rests on a citation

| | route 1 — `su5_anomaly_verdict.py` | route 2 — `e6_weight_route.py` |
|---|---|---|
| builds the 27 from | SU(5) multiplets, 10 = Λ²(5) | a Weyl orbit of ω₁ from the E₆ Cartan matrix |
| hypercharge from | the unique traceless diag(a,a,a,b,b), 3a+2b=0 | fundamental-coweight gradings |
| branching | **CITED** pattern | **COMPUTED** — recovers 16+10+1 and the SU(5) content |
| abelian directions tested | the 3 SM-relevant ones (Y, χ, ψ) | **all six** e₆ Cartan coordinates |

Route 2's ω₆ orbit reproduces route 1's SU(5) content **exactly** — `{10, 5, 5̄, 5̄, 1, 1}` — and
route 2's ω₁ orbit is its conjugate. The ψ-grades come out `1/3, −2/3, 4/3` on blocks of size
`16, 10, 1`, i.e. **ratio (1 : −2 : 4)** — the standard normalisation, *computed from the Cartan
matrix*, not assumed.

---

## 1. THE LOAD-BEARING ARITHMETIC (COMPUTED, exact rationals)

### The hypercharge generator — derived, not assigned

The unique traceless SU(5) Cartan direction commuting with SU(3)×SU(2) is `diag(a,a,a,b,b)`
with `3a + 2b = 0`. Normalising `b = +1/2` (the single convention `Q_em = T₃ + Y`, **CITED**):

```
Y(5) = (−1/3, −1/3, −1/3, +1/2, +1/2)      sum = 0  ✓
```

The 10 is then **built** as Λ²(5): a state is an index pair `i<j` with `Y = Yᵢ + Yⱼ`, and its
SU(3)/SU(2) labels follow from which indices the pair uses:

| pair type | count | Y | rep | name |
|---|---|---|---|---|
| colour⊗colour (antisym 3⊗3 = 3̄) | 3 | −1/3 − 1/3 = **−2/3** | (3̄,1) | uᶜ |
| colour⊗weak | 6 | −1/3 + 1/2 = **+1/6** | (3,2) | Q |
| weak⊗weak (antisym 2⊗2 = 1) | 1 | 1/2 + 1/2 = **+1** | (1,1) | eᶜ |

### The 27, state by state (all left-handed Weyl)

| source | multiplet | dim | Y | χ | ψ |
|---|---|---:|---:|---:|---:|
| 16 / 10 | eᶜ (1,1) | 1 | 1 | −1 | 1 |
| 16 / 10 | Q (3,2) | 6 | 1/6 | −1 | 1 |
| 16 / 10 | uᶜ (3̄,1) | 3 | −2/3 | −1 | 1 |
| 16 / 5̄ | dᶜ (3̄,1) | 3 | 1/3 | 3 | 1 |
| 16 / 5̄ | L (1,2) | 2 | −1/2 | 3 | 1 |
| 16 / 1 | N (1,1) [ν_R] | 1 | 0 | −5 | 1 |
| 10 / 5 | D (3,1) *exotic* | 3 | −1/3 | 2 | −2 |
| 10 / 5 | H_u (1,2) *exotic* | 2 | 1/2 | 2 | −2 |
| 10 / 5̄ | Dᶜ (3̄,1) *exotic* | 3 | 1/3 | −2 | −2 |
| 10 / 5̄ | H_d (1,2) *exotic* | 2 | −1/2 | −2 | −2 |
| 1 / 1 | S (1,1) *E₆ singlet* | 1 | 0 | 0 | 4 |
| | **TOTAL** | **27** | | | |

Consistency (computed): `Σ₂₇ χ = 0`, `Σ₂₇ ψ = 0`.

### The four coefficients, written out

Conventions (**CITED**, stated): `T(3)=T(3̄)=1/2`, `T(2)=1/2`, `T(1)=0`, `A(3)=+1`, `A(3̄)=−1`.

**10 of SU(5):**
```
grav   Tr Y      = 6(1/6) + 3(−2/3) + 1(1)          = 1 − 2 + 1        = 0
[U1]³  Tr Y³     = 6(1/6)³ + 3(−2/3)³ + 1(1)³       = 1/36 − 8/9 + 1   = 5/36
[SU3]²Y          = 2·(1/2)(1/6)  +  1·(1/2)(−2/3)   = 1/6 − 1/3        = −1/6
[SU2]²Y          = 3·(1/2)(1/6)                     = 1/4              = 1/4
[SU3]³           = 2(+1) + 1(−1)                                       = +1
doublets                                                               = 3
```
**5̄ of SU(5):**
```
Tr Y   = 3(1/3) + 2(−1/2)         = 1 − 1            = 0
Tr Y³  = 3(1/27) + 2(−1/8)        = 1/9 − 1/4        = −5/36
[SU3]²Y = 1·(1/2)(1/3)                               = +1/6
[SU2]²Y = 1·(1/2)(−1/2)                              = −1/4
[SU3]³  = −1  ·  doublets = 1
```
**5 of SU(5)** is the exact negative of the 5̄ row: `0, +5/36, −1/6, +1/4, +1`, 1 doublet.
**Both singlets** (ν_R, S) are `(1,1)_0` → every coefficient `0`.

### The table

| piece | Tr Y | [U(1)]³ | [SU(3)]²Y | [SU(2)]²Y | [SU(3)]³ | doublets |
|---|---:|---:|---:|---:|---:|---:|
| 10 (in 16) | 0 | **+5/36** | **−1/6** | **+1/4** | **+1** | 3 |
| 5̄ (in 16) | 0 | **−5/36** | **+1/6** | **−1/4** | **−1** | 1 |
| 1 (in 16) | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 (in 10) | 0 | **+5/36** | **−1/6** | **+1/4** | **+1** | 1 |
| 5̄ (in 10) | 0 | **−5/36** | **+1/6** | **−1/4** | **−1** | 1 |
| 1 (E₆ singlet) | 0 | 0 | 0 | 0 | 0 | 0 |
| **COMPLETE 27** | **0** | **0** | **0** | **0** | **0** | **6 — even** |

All four SM anomaly coefficients vanish on the complete 27. The Witten SU(2) parity is even.
**Route 2 proves the stronger statement:** over the 27 as an E₆ Weyl orbit,

> **Σ_λ λ(H) ≡ 0 and Σ_λ λ(H)³ ≡ 0 identically in all six Cartan coordinates h₁…h₆.**

So it is not that the three SM-relevant directions happen to cancel — **every abelian direction in
all of e₆ is anomaly-free on a complete 27.** (Sanity: `Σ λ(H)² = 12·(quadratic form) ≠ 0`, so the
orbit is live and the vanishing is not an artefact of a degenerate construction.)

---

## 2. THE DISCRIMINATING QUESTION — cancellation, or separately zero?

**The answer is granularity-dependent, and both halves matter.**

**At SU(5)-irrep granularity there IS a genuine cancellation.** The 10 carries `+5/36` and the 5̄
carries `−5/36`; `−1/6` against `+1/6`; `+1/4` against `−1/4`; `+1` against `−1`. This is the
classic `A(10) + A(5̄) = 1 − 1 = 0`. A lone 10 is a *complete SU(5) multiplet* and is *anomalous* —
which is exactly the error B864 caught in Layer 5 and which this cell re-confirms as a live control.

**At SO(10)-irrep granularity each piece vanishes separately — no cross-talk at all:**

| piece | Tr Y | [U(1)]³ | [SU(3)]²Y | [SU(2)]²Y | [SU(3)]³ | doublets |
|---|---:|---:|---:|---:|---:|---:|
| **16** (SO(10) spinor) | 0 | 0 | 0 | 0 | 0 | 4 — even |
| **10** (SO(10) vector) | 0 | 0 | 0 | 0 | 0 | 2 — even |
| **1** (SO(10) singlet) | 0 | 0 | 0 | 0 | 0 | 0 |

> **There is no cancellation between the 16 and the 10+1.** The 16 is anomaly-free on its own —
> it is the SO(10) spinor — and the exotic sector contributes **exactly nothing** to cancel
> against.

**And the third layer, which is the sharpest.** The twelve exotics are `ν_R ⊕ (5+5̄) ⊕ S`, and:

```
exotic 12 is a REAL (vector-like) rep of SU(3)×SU(2)×U(1)?   True     (computed by pairing)
SM generation 15 is a REAL rep?                              False
complete 27 is a REAL rep?                                   False
```

A real representation contributes identically zero to every chiral anomaly. To show that this is
structural rather than numerical coincidence, I replaced the exotics' E₆ hypercharges by **free
parameters** `y₁` (the colour-triplet pair) and `y₂` (the doublet pair), keeping *only* the
vector-like pairing:

```
grav  = 0        [U1]³ = 0        [SU3]²Q = 0        [SU2]²Q = 0
```

— identically in `y₁, y₂`. **The four SM anomaly conditions carry zero information about the
exotic sector, for any vector-like charge assignment whatsoever.**

> **VACUITY IS TRIPLE.** (1) It vanishes on the complete 27. (2) It vanishes separately on each
> SO(10) block, so there is no 16↔exotic conspiracy to be impressed by. (3) The exotic sector is
> *invisible to the instrument* — the check cannot see the twelve exotics of L134 **at all**, at
> any charge assignment. L132 was never going to constrain them.

---

## 3. MB12 — the check CAN pass and CAN fail (so the vacuity is a property of the input)

Live controls through the identical code path:

| spectrum | Tr Y | [U(1)]³ | [SU(3)]²Y | [SU(2)]²Y | [SU(3)]³ | doublets | |
|---|---:|---:|---:|---:|---:|---:|---|
| lone SU(5) **10** | 0 | 5/36 | −1/6 | 1/4 | +1 | 3 | **FAILS** (incl. Witten: odd) |
| lone SU(5) **5̄** | 0 | −5/36 | 1/6 | −1/4 | −1 | 1 | **FAILS** |
| 27 minus eᶜ | **−1** | **−1** | 0 | 0 | 0 | 6 | **FAILS** |
| 27 minus the exotic 5 | 0 | −5/36 | 1/6 | −1/4 | −1 | **5** | **FAILS** (incl. Witten: odd) |
| 16 minus ν_R (= the 15) | 0 | 0 | 0 | 0 | 0 | 4 | passes |
| exotics only (12) | 0 | 0 | 0 | 0 | 0 | 2 | passes (vector-like) |

Route 2 confirms at weight level: dropping **any** of the three SO(10) blocks makes both the
linear and cubic conditions nonzero, and dropping a single weight makes the linear condition
nonzero in **27/27** cases. Same machinery on A₄'s **5** and **10** and A₂'s **3**: cubic
**not** identically zero.

**MB12 discharged both ways. The instrument is real; the vacuity is a property of the INPUT.**

---

## 4. DOES HYPERCHARGE FALL OUT? — the answer is NO, twice over

Writing the general abelian direction `Q = aY + bχ + cψ` and solving the linear conditions exactly:

**Over the COMPLETE 27:**
```
grav = 0      [U1]³ = 0      [SU3]²Q = 0      [SU2]²Q = 0     (identically in a,b,c)
⇒ solution space is 3-dimensional out of 3  ⇒  NO SELECTION AT ALL
```

**Over the COMPLETE 16** (SO(10) spinor):
```
grav    = 16c
[SU3]²Q = 2c
[SU2]²Q = 2c
[U1]³   = 10a²c + 240b²c + 16c³
⇒ c = 0 forced; cubic then vanishes identically
⇒ solution space {aY + bχ}, 2-dimensional  ⇒  ψ is killed, but Y is NOT selected over χ
```

**Over the chiral 15** (the SM generation, i.e. after deleting ν_R):
```
grav    = 5b + 15c
[SU3]²Q = 2c
[SU2]²Q = 2c
⇒ b = c = 0 forced  ⇒  solution space {aY}, 1-dimensional  ⇒  Y selected
```

This **reproduces B864's uniqueness** exactly (and reproduces its arithmetic: ψ over the full 27
`16−20+4 = 0` and `16−80+64 = 0`; ψ over the 16 `Tr = 16`, `Tr³ = 16`, `[SU(3)]² = 2`; χ over the
16 all zero; χ over the 15 `Tr = 5`, `Tr³ = 125` — **all four reproduced**).

**And it scopes it.** The step that gives the check its selective power is precisely the deletion
of **ν_R** — and under `Q = Y` that state is a **total SM singlet contributing 0 to every
coefficient**. The deletion that makes L132 bite is one the hypercharge conditions *cannot
themselves detect*; you only see it through the χ direction.

> **B864's headline scoped (not retracted):** "hypercharge is the unique gaugeable U(1)" is
> uniqueness **over the imported chiral 15**. Over the object's own complete 27 the solution
> space is 3-dimensional and hypercharge is not distinguished at all; over the complete 16 it is
> still 2-dimensional. The selective power lives in the truncation, not in the anomaly conditions.

---

## 5. VERDICT

> ### L132 is **VACUOUS** on complete 27s. CLOSED.
>
> Confirmed by two independent in-sandbox routes. The vacuity is **triple**: the coefficients
> vanish on the complete 27; they vanish separately on every SO(10) block; and they are
> identically blind to the exotic sector for arbitrary vector-like charges. Hypercharge does
> **not** fall out — not from the 27 (3-dim solution space), and not even from the 16 (2-dim).

### What would have to be true of the object's spectrum for the check to acquire content

Each condition below is what the computation above actually forces, in increasing strength:

1. **The spectrum must not be a union of complete E₆ irreps.** *Computed:* `Σλ(H) ≡ Σλ(H)³ ≡ 0`
   in all six e₆ Cartan coordinates on the 27. Any complete-multiplet spectrum, any abelian
   direction inside e₆ — automatically zero.
2. **It must not even be a union of complete SO(10) irreps.** *Computed:* 16, 10 and 1 each
   vanish separately. So a mere reshuffling of SO(10) blocks is not enough — **the deletion must
   split an SO(10) multiplet.**
3. **The deleted set must not be vector-like.** *Computed:* the exotic 12 is a real SM rep and
   contributes zero for arbitrary `y₁, y₂`. Deleting a real subset preserves vanishing of the
   hypercharge conditions.
4. **A handedness assignment per state is required** for the functional to be defined at all; a
   vector-like spectrum gives zero regardless of completeness.
5. **Even then, the check does not select the Standard Model.** It selects a 1-dimensional abelian
   direction only *relative to whichever truncation was imported* — and the truncation is the
   input carrying all the content. (The scout's map counts 156 distinct truncations of the 27 each
   admitting a unique anomaly-free u(1); that enumeration is the scout's, not re-run here.)

**In one line:** L132 acquires content **iff** something *deletes states from inside an SO(10)
multiplet in a non-vector-like way*. That is a property of a deletion operation, and this cell
makes no claim about whether the object has one — that is the scout's question, answered in
`PRIOR_ART_ANOMALY.md` and not re-litigated here.

---

## 6. LABELLING — COMPUTED vs CITED

**COMPUTED in-sandbox (exact rationals throughout):** the hypercharge generator; the 10 as Λ²(5)
with all labels derived from indices; all four SM anomaly coefficients per SU(5) irrep, per SO(10)
irrep, for the 15 and for the 12; `[SU(3)]³`; the Witten doublet parity; the 27 as an E₆ Weyl
orbit; the identical vanishing of the linear and cubic weight sums in all six Cartan coordinates;
the SO(10) and SU(5) branchings via coweight grading; the complexity of the 27 (ω₁ and ω₆ orbits
have different weight sets); the vector-like/real character of the exotic 12; the exotic-blindness
in free `y₁,y₂`; the solution-space dimensions 3 / 2 / 1 over the 27 / 16 / 15; all MB12 controls.

**CITED, not re-derived:** the anomaly-coefficient normalisations `T(3)=T(2)=1/2`, `A(3)=+1`; the
convention `Q_em = T₃ + Y`; the E₆→SO(10)→SU(5) branching *pattern* in route 1 — **which route 2
then computed independently**; and, as background only, that the `A_n (n≥2)` series are the only
simple algebras with a nonzero symmetric cubic invariant (the E₆ case is computed here, not cited).

## 7. WHAT THIS CELL DOES NOT ESTABLISH

- It does **not** refute B864. It reproduces B864's arithmetic and adds a scope-note.
- It makes **no** claim about whether the object supplies a truncation.
- It says nothing about values, generations, the real form, or spacetime.
- No literature search was run from this cell; the scout's §4 null remains uncertified.
- The 2047-subset enumeration is the scout's and was not re-run.

**Reproduce:** `python su5_anomaly_verdict.py`, `python e6_weight_route.py`, `python merge_work.py`
(sympy, exact; outputs `work.json`, `e6_weight_route_out.json`, `*_out.txt`).
