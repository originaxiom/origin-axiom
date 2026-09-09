# MEMO 185 — **THE NAIVE CYCLOTOMIC ROUTE TO `f_K` IS CLOSED, BY COMPUTATION**, and a route this bench floated one message earlier is withdrawn before it cost anything

**Date** 2026-09-09 · **Lane** outside bench · **Branch** `claude/outside-bench`
**Certificate** `certificates/cyclotomic_vs_fk.py` · **Output** `outputs/cyclotomic_vs_fk_out.txt`
**Gate 5** exact integer and `Fraction` arithmetic throughout. No measured value of any kind.

**Already-banked check (memo 153).** Terms searched: `inverted Habiro series`,
`cyclotomic expansion f_K`, `colored Jones table twist knots`, `Habiro series`, `naive route`,
`power series convergence`. **0 settled arcs matched** on either sweep. Admissible as new.

---

## 0. What this corrects, said first

One message before this memo, asked what a table of colored Jones polynomials
`J_{K,n}` for `n = 1..60` would buy, this bench gave three solid reasons and then added a
fourth, flagged at the time as **"untested, not promised"**:

> *"from `J_1 … J_60` one can solve triangularly for Habiro's cyclotomic coefficients
> `C_0 … C_59` exactly, and `F_K` is the inverted Habiro series. If that inversion is
> explicit, it is a route to `f_j` far past the `f_5` the Verma trace gives me — which is
> precisely the blocker memo 183 addendum 4 named."*

**That fourth reason is withdrawn.** The triangular solve is real and exact; what fails is the
step after it. The three others stand untouched and are restated in §5.

---

## 1. The claim, and why it is not settled by quoting anyone

Gukov–Manolescu (arXiv:1904.06057v2, p. 14, immediately after eq (22)) write:

> *"In contrast to what was claimed in [36], our new understanding is that `f_K` is not
> directly related to the cyclotomic expansion (just as the q-series `Ẑ_a` is not directly
> related to the Habiro series)."*

**Register R80-1 forbids this bench from closing anything on that sentence.** An author's
stated expectation is evidence about what was known when it was written, never about what is
true — and *"our new understanding"* is exactly such a sentence. It is also, by the same rule,
evidence that the naive route was believed by competent people (it is [36]'s own conjecture)
until 2019, which is a reason to test it rather than to assume either way.

So the sentence is **not used**. It is tested, at the only two places it can be tested, with
exact arithmetic.

## 2. The objects, in GM's own conventions

GM eq (20)–(21), with `x = q^n`:

```
J_{K,n}(q) = Σ_{m≥0} C_m(q) (q^{n+1})_m (q^{1−n})_m
C_K(x,q)   = Σ_{m≥0} C_m(q) (qx)_m   (qx^{−1})_m
```

GM eq (22) is the Gukov–Mariño–Putrov conjecture with `f_K` sitting in the slot the Habiro
expansion gives `C_K`. **The naive reading — the one the floated route needs — is**

```
f_K(x,q)  =  C_K(x,q)   up to an overall monomial,
```

with `f_K = F_K/(x^{1/2} − x^{−1/2})` (GM eq (104)) and `F_K` for a torus knot given by GM
Thm 1.3. **`f_K` is not taken on trust either**: those blocks were verified at this bench in
`certificates/gm_thm13.py` against Park's large-colour Verma R-matrix (arXiv:2004.02087) — a
machine from a different paper, neither theorem used to derive the other.

## 3. Two preregistered cells, both resolved to B

### CELL A — `4₁`: is `C_K` even a series?

Fix the single monomial `x⁰q⁰` and count what each index `m` contributes to it.

* **A** — the partial sums stabilise → `C_K` is a genuine Laurent power series and nothing
  obstructs reading `f_j` off the `C_m` term by term.
* **B** — they do not → `C_K` is not a power series in `(x,q)` and no term-by-term route
  through it exists.

**Computed** (`C_m(4₁) = (−1)^m q^{−m(m+1)/2}`, forced by control C2 below):

| m | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|----|----|----|
| contribution to `x⁰q⁰` | +1 | +2 | +8 | +52 | +484 | +5064 | +57528 | +686588 |

with the odd `m` contributing `0, −2, −16, −152, −1536, −16946, −197616, −2407538`. The partial
sums run `1, 1, 3, 1, 9, −7, 45, −107, 377, −1159, 3905, −13041, 44487, −153129, 533459,
−1874079`. **A single monomial receives unboundedly many, unboundedly large contributions.**

> **CELL A → OUTCOME B.** `C_{4₁}(x,q)` is not a Laurent power series in `(x,q)`. This is
> exactly the structural reason GM state in words — *"there may be infinitely many
> contributions from the same monomial `x^u q^v`"* — now a computation rather than a citation.

### CELL B — `3₁`: where the obstruction is absent, is `C_K = f_K`?

On the trefoil `C_m(q) = q^m` (GM eq (24)), the index-`m` term starts at `q^m`, so each monomial
receives finitely many contributions and `C_K` **is** a genuine power series. The identification
can therefore be tested head on.

* **A** — `C_K(x,q) = λ · x^A q^B · f_K(x,q)` for some constant `λ` and monomial.
* **B** — no such `λ, A, B` exists.

**Computed.** The `x⁰` coefficient of `C_{3₁ˡ}` in `q`-orders `0 … 34`:

```
1, 1, 1, 2, 2, 4, 5, 7, 10, 13, 17, 24, 31, 40, 53, 69, 88, 113, 144, 183,
231, 290, 362, 453, 563, 696, 859, 1058, 1296, 1587, 1935, 2354, 2856, 3458, 4175
```

The `x⁰` coefficient of `f_{3₁}` from GM Thm 1.3 is supported on the **sparse** set of
exponents `1, 2, 3, 6, 8, 13, 16, 23, 27, 36, 41, 52, …` (and its negatives for the mirror),
and **every nonzero coefficient has absolute value exactly `1/2`.**

The argument is then two lines and needs no growth estimate. If `C_K = λ x^A q^B f_K`, every
nonzero coefficient of `C_K` has absolute value `|λ|/2` — **one** value. `C_K`'s `x⁰`
coefficients already take **32 distinct absolute values in the first 35 orders**.

> **CELL B → OUTCOME B.** No `λ, A, B` exists. It fails for **both** chiralities of `f_K`,
> hence for either `q`-orientation, so it is not a mirror-convention artifact.

## 4. Controls

| | control | result |
|---|---|---|
| C1 | eq (20) with GM eq (24)'s `C_m = q^m` reproduces the classical Jones polynomial of the left trefoil at `n=2` (`q + q³ − q⁴`, cited anchor) and `J_1 = 1` | PASSED |
| C2 | eq (20) with `C_m(4₁) = (−1)^m q^{−m(m+1)/2}` equals GM eq (166) exactly at `n = 1 … 8` | PASSED |
| C2b | GM eq (166) at `n=2` is the classical Jones polynomial of `4₁`, `q^{−2} − q^{−1} + 1 − q + q²` | PASSED |
| C3 | **the divergence detector returns FINITE on the trefoil** — contributions `1,0,0,0,…`, partial sums constant at `1` | PASSED |
| C4 | `f_K` here is GM Thm 1.3, verified in `gm_thm13.py` against an independent machine | PASSED |

C3 is the one that matters most (memo 164: *control passing is not instrument working*). A
detector that always answers "divergent" would prove nothing; this one answers "finite" on a
knot in the same family, run through the same code path.

## 5. Consequence for the download, stated plainly

**A table of `J_{K,n}` for `n = 1..60` does not unblock `f₆` and beyond.** Memo 183 addendum 4's
blocker survives. The three reasons that *are* good are unaffected:

1. **memo 184's stability fence goes from 8 coefficients to ~60.** The tail measurement is
   currently fenced at seven stabilised coefficients; `n` up to 60 raises that by an order.
2. **`K_{−1} = 4₁` and `K_1 = 3₁` are free controls.** Their tables can be checked against
   GM eq (166) and eq (24) — implemented and passing here — before any table is trusted.
3. **memo 184 addendum 1's family goes from 4 knots to 30**, `p = −14 … 15`.

**And the item that actually decides the erratum is still the quantum A-polynomial data**
(`fetch/FETCH_REQUEST_CEFF.md` §B''), not the colored Jones table.

## 6. What is NOT closed here — scope, stated so it is not overread

What dies is the **naive** route: `C_K` read as `f_K` up to a monomial, and any term-by-term
passage through `C_K`. **A non-naive relation is untouched and is a live open item.** Park,
*"Inverted state sums, inverted Habiro series, and indefinite theta functions"*
(arXiv:2106.03942), is exactly such a route by its title, and **this bench does not have it** —
it has been tracked since before this session as fetch item **B2** in
`fetch/FETCH_REQUEST_CEFF.md`. That is now the named follow-up, and its priority is below the
A-polynomial data.

Note also that GM themselves record a partial positive at §7.4 (p. 55):

> *"We could try to apply the Dehn surgery formula (106) to `C_K(x,q)` instead of `f_K(x,q)`
> … Interestingly, we get the right answer for the −1 surgery (the case of the Poincaré
> sphere), but not for other surgeries."*

**That sentence is UNTESTED at this bench.** By R80-1 it is not evidence; it is a named,
cheap, well-posed follow-up (§7 below).

## 7. Named follow-up

**F185-1.** Test GM §7.4 directly: run the `p/r = −1` Laplace collapse on
`(x^{1/2}−x^{−1/2})(x^{1/2r}−x^{−1/2r})C_{3₁}` and on the same with `f_{3₁}`, and compare both
to `Ẑ(Σ(2,3,5))`; then repeat at a second slope where GM say it should fail. Machinery exists:
`certificates/park_table3_repaired.py` carries the `assemble(P, r, a, ·)` transform, and this
memo's certificate carries `C_K`. What is missing is only the `Ẑ` targets and a settled
chirality convention. **Not done here; not claimed.**

## 8. A convention note, recorded because it will bite again

*"The cyclotomic coefficients of `4₁` are all 1"* is true in the basis
`∏_{j=1..m} (q^N + q^{−N} − q^j − q^{−j})` — the form used in `certificates/c2_habiro.py`,
where it is anchored against the classical Jones polynomial and is correct there. In **GM's
eq (20) basis** `(q^{n+1})_m (q^{1−n})_m`, the same knot has `C_m = (−1)^m q^{−m(m+1)/2}`,
because

```
(q^{n+1})_m (q^{1−n})_m = (−1)^m q^{m(m+1)/2} ∏_{j=1..m} (q^n + q^{−n} − q^j − q^{−j}).
```

Both are checked in the certificate. The two are not in conflict — they are different bases —
but **the `q`-valuation of `C_m` differs between them, and that valuation is exactly what
decides CELL A.** Reading "all coefficients are 1" into GM's eq (21) would have made `C_{4₁}`
look like a convergent series and hidden the obstruction. It is written down here so the next
seat does not walk into it.

---

## 9. Interpretive (labelled)

The shape of this result is worth naming. A route was floated, in the same session, in a
message to the owner, hedged but attractive. It was then checked against the primary source,
found to be contradicted by an author's sentence, and — because an author's sentence is not
evidence at this bench — **computed**. The computation agreed with the sentence and supplied
what the sentence lacked: a witness. Total cost, one certificate. The alternative was a
download prioritised for the wrong reason and a week spent inverting a triangular system into
an object that is not a series.

**The discipline that caught it is R80-1 read in the other direction.** R80-1 usually stops the
bench from *downgrading* something it computed because an author expected otherwise. Here it
stopped the bench from *upgrading* a hope, by requiring that GM's contrary sentence be tested
rather than either believed or dismissed. Both directions are the same rule.
