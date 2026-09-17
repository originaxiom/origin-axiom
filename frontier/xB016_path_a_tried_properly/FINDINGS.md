> **ADDENDUM 1, 2026-09-17 — READ IT BEFORE THIS FILE.** The owner said *"go for proper p3"*, and
> P3's three soft edges were settled. **Two settle in this arc's favour, the third against two of
> its own cells.** **P7**: the census extended to degree 10 — **87 covers, 19 with no torsion at
> all, none exceeding the cyclic limit** — P3 strengthens. **P8**: the mechanism §3 withdrew is now
> **PROVED** — `φ(a) = 0`, `a` is loxodromic (§3's `|tr| > 2` test was the **wrong criterion**),
> and `systole(M_n) = 1.0870701450` **exactly, for every n**, so the tower does not converge to the
> universal cover. **P9**: the literature returned **after** banking and **confirms §2 (doubly),
> corrects the `1/(6π)` attribution (it is Bergeron–Venkatesh *Conjecture* 1.3, not a theorem), and
> WITHDRAWS both §4's *"`k` must be even"* and §6's recommendation to re-open Route 3** — nothing
> couples `k` and `σ`, and `η = 0` for complex Chern–Simons leaves no framing anomaly to cancel
> against. **The verdict is unchanged — Path A does not cross — and Route 3 is now closed by
> citation (Witten arXiv:1001.2933 eq. 2.2) rather than left open.** Where this file and the
> addendum disagree, **the addendum is right.**

# xB016 — PATH A, TRIED PROPERLY: three routes attempted, all three closed, and the one worth re-opening is blocked by missing bookkeeping rather than by a theorem

**Seat `xb`, `sep16-branch`, 2026-09-17. PREREGISTRATION sealed `56447437…` and PUSHED at `89cdf7d`
before `verification/` existed. Verdict: PROVED (Path A does not cross), with P2 and P3 delivering
the preregistered negatives and P3 — the cell this seat declared it could not call — coming back
on the declared prior.**

Gate 5 absolute: no value, no generation count, no physics reading, nothing to `CLAIMS.md`.

---

## 0. Why this arc exists

> *"lets verify parh A once more, so were sure we dine it priperly and were sure it doesnt cross,
> and we tried right way"*

**Path A had been wrong twice in this seat's hands, and both times the failure was the same:
the conclusion was asserted, not attempted.** xB014 killed it on a sort-order error (withdrawn by
its own Addendum 1 after the owner asked *"u sure about extremality"*). xB015 then showed the
*reason* xB014 gave for non-crossing — *"the wall is dimensionful"* — was **also** wrong. Neither
arc ever ran a crossing attempt. **This one does.**

**What "crossing" means was fixed in the seal before anything ran:** deriving a numerical value for
`c` or `σ` — the framework's one continuous dimensionless anchor (A2, B1015) — from the object's own
data with no new input. **Constraining `k` is not crossing**, because `k` is not the free anchor.

---

## 1. P1 — the tower, re-derived from scratch

| n | vol/vol(m004) | CS | \|tors\| | predicted | log\|t\|/vol |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 1 | — |
| 2 | 2 | 0 | 5 | 5 | 0.396436 |
| 3 | 3 | 0 | 16 | 16 | 0.455295 |
| 4 | 4 | 0 | 45 | 45 | 0.468828 |
| 5 | 5 | 0 | 121 | 121 | 0.472519 |
| 6 | 6 | 0 | 320 | 320 | 0.473617 |
| 7 | 7 | 0 | 841 | 841 | 0.473961 |
| 8 | 8 | 0 | 2205 | 2205 | 0.474072 |

Torsion `= L_n²` (n odd) `/ 5F_n²` (n even), **8 of 8**. Volume `= n·vol(m004)`, **8 of 8**. Limit
rate `log φ² / vol(m004) = 0.474127597116`. **xB014 reproduces exactly.**

**And one column xB014 never computed: `CS_n = 0` at every rung** — forced, not observed, by xB015's
K4 (the tower is covers of a `CS = 0` base, and CS is multiplicative). That zero is what makes the
next cell's arithmetic possible at all.

---

## 2. P2 — ROUTE 1, the rate route: the crossing attempt Path A had never made

With `CS_n = 0`, the action along the tower is `S_n = −n·Vol·σ` — **linear in n**. And
`log|H₁(M_n)_tors| ≈ n·log φ²` — **also linear in n**. The `n` cancels:

> `log|tors| / (−S) → log φ² / (Vol·σ) = 0.474127597… / σ`

**So an identification of `log|H₁ tors|` with `−S` — entropy equals action — would fix**

> **`σ = 0.4741275971155`  and  `c = 6σ = 2.8447655827`** — **REFUTED below; never a live claim**
> *(registered in `RETRACTED_PHRASES.md` row 12, so it can never be re-derived as a discovery)*

**The seal printed both numbers in advance, precisely so they could never be presented as a
discovery.** They are a candidate, and the cell's job was to find whether the identification is
licensed.

**It is not — and the status of that judgement is stated exactly.** Torsion does enter a complex
Chern–Simons partition function, but as **Ray–Singer torsion at one loop**, in the fluctuation
determinant rather than in the on-shell action; and a **cusped hyperbolic manifold has no horizon**,
so there is no Bekenstein–Hawking area to count and no Cardy regime to sit in. Reading a **homology
count** as a **state count** is a category error, not a missing theorem.

> **FLAGGED, NOT HIDDEN: the paragraph above is this seat's argument from the structure of the
> theory, NOT a citation.** A literature check was in flight when this arc banked and is not
> reflected here. **If it returns a licence, P2 is wrong and this arc owes an addendum.** The
> preceding session established that three of four citations this seat would have given from memory
> were wrong, so an unchecked argument is labelled as one.

> **`σ = 0.4741…` and `c = 2.8448` are recorded here as a REFUTED CANDIDATE.** They are not a
> prediction of this programme and must never be cited as one. Any future arc that re-derives them
> should find this row first.

---

## 3. P3 — ROUTE 2, the blind cell: the rate is the TOWER's, not the object's

**This was the one cell the seal said this seat could not call.** Measuring
`log|H₁ tors| / vol` over **every** cover of m004 to degree 8:

| degree | #covers | min rate | max rate | median | #with trivial torsion |
|---|---|---|---|---|---|
| 2 | 1 | 0.396436 | 0.396436 | 0.396436 | 0 |
| 3 | 1 | 0.455295 | 0.455295 | 0.455295 | 0 |
| 4 | 2 | 0.000000 | 0.468828 | 0.234414 | 1 |
| 5 | 4 | 0.000000 | 0.472519 | 0.068294 | 1 |
| 6 | 11 | 0.090203 | 0.473617 | 0.132145 | 0 |
| 7 | 9 | 0.000000 | 0.473961 | 0.185729 | 4 |
| 8 | 10 | 0.000000 | 0.474072 | 0.135305 | 1 |

**Across all 38 covers the rate runs from 0.000000 to 0.474072, median 0.135305, and 7 of the 38
have no torsion at all.** Five sit within 0.01 of the cyclic limit — and each of those five was
**verified by isometry**, not assumed, to be a cyclic-tower member `b++(LR)ⁿ` at n = 4, 5, 6, 7, 8.

> **`0.4741275971` is not a number m004 *has*. It is a number one *tower* over m004 has.** The same
> manifold supports covers whose rate is anything down to zero.

**The declared prior was right, and this kills Route 1 a second time without needing the licensing
argument at all.**

**And the comparison that puts it in scale.** The asymptotic torsion-growth rate associated with a
hyperbolic 3-manifold is `1/(6π) = 0.053052` — **quoted from memory and not yet verified against a
source**, so it is a scale marker here and **nothing is concluded from it**. The cyclic tower gives
`0.474128` — **different by a factor of about 8.9.** Path A chose the tower that gives the biggest number.
**That is what a selection effect looks like**, and neither xB014 nor xB015 had checked it.

**A mechanism claim this cell tried to make and WITHDREW.** A first draft said the cyclic tower
fails to converge to the universal cover *because it keeps the fibre*. To support it this seat
measured the systole along the tower; SnapPy returned nothing beyond n = 4, and the draft read that
as *"the systole grows"*. **It was a swallowed exception** — `length_spectrum` raises
`RuntimeError("The Dirichlet construction failed")` on these covers, and a bare `except` turned a
failure into a data point. **The measurement is void, the mechanism is not established here, and the
claim is withdrawn.** P3's conclusion does not depend on it: the measured spread is what proves
tower-dependence, and it stands alone. *(Fourth self-caught error of this seat in two arcs, and the
same shape as E5/E56: an instrument's silence read as a number.)*

*Honest scope:* the range is degree ≤ 8, so *"no cover exceeds 0.474128"* is a **measurement over
that range**, not a supremum theorem.

---

## 4. P4 — ROUTE 3, what the mod-½ indeterminacy forces, and the gap it exposed

For a cusped manifold `cs` is well defined only modulo `½`, and the indeterminacy is **essential**
(Neumann: there is no consistent definition well defined modulo `2π²` for cusped manifolds). Under
`cs → cs + ½` the action shifts by `−k/2`, so `exp(2πiS)` picks up `(−1)^k`:

> **In the level normalisation, well-definedness of `exp(2πiS)` forces `k` to be EVEN.**

**By this arc's own sealed definition that is NOT a crossing** — it constrains `k`, and `k` is not
the free anchor. It is reported as what it is.

**But the cell found something the seal did not anticipate, and it is a gap in the record rather
than a result.** B1012's `b1012_verify.py` carries `CS` as a **bare sympy symbol**. Its algebra —
`S = −CS·k − Vol·σ`, `∂S/∂k = −CS` — is **normalisation-free**, and **no arc in the record pins
which CS enters the k-coupling**: SnapPy's `cs` (mod ½), Neumann's `CS = 2π²cs` (mod `π²`), or a
level-normalised `CS/2π`. They differ by factors of `2π²`, and the statement above holds in **one**
of them. In Neumann's normalisation the same shift gives `exp(−iπ²k)`, not a root of unity for any
`k ≠ 0` — so that normalisation cannot be the one the exponentiated weight uses, **which is itself a
constraint the record has never written down.**

> **No quantization claim can be read off the record as it stands.** Pinning the normalisation of
> the k-coupling is a **prerequisite** for any future crossing attempt through this route. It is
> owed work, not a result of this arc.

---

## 5. P5 — B290's precedent, turned on this arc's own temptation

B290 banked *"the filling `n` is NOT the level `k`"*: the filling coefficient is a topological
Dehn-surgery integer, the level a quantum root-of-unity parameter `q = e^{2πi/(k+2)}`; **independent
axes**, so the identification is *"a formal substitution, not an identity."*

Re-derived here in this arc's own variables, in the form that bites:

> `S(M; k, σ) = −CS(M)·k − Vol(M)·σ` is **linear in both levels**, with the object supplying only
> the **coefficients**. `∂S/∂k = −CS(M)` and `∂S/∂σ = −Vol(M)` are invariants of M; `∂²S/∂k² = 0`.
> **An invariant of M can determine the coefficient of a level. It cannot determine the level,
> because the level is not a function of M.**

That kills identifying the tower index `n` with `k`, **and** it kills identifying xB015's ℤ/12 CS
index with `k`. **This arc makes neither identification.** It is also the general reason Path A was
never going to cross by this shape of argument — and it was already in the record, banked, for over
a year.

---

## 6. P6 — the verdict

| route | outcome |
|---|---|
| **Route 1** — the rate route (entropy = action) | **FAILS TWICE**: unlicensed (P2, a category error) **and** tower-dependent (P3) |
| **Route 2** — genericity of the rate | the rate is the **tower's**; m004's covers span 0 → 0.474072, 7 of 38 with no torsion |
| **Route 3** — quantization | constrains **`k`** (even), not `σ`; and exposes an **unpinned normalisation** in the record |

> **PATH A DOES NOT CROSS. `σ` is untouched by everything here.** This time that is a result of
> three attempts, each with its own kill condition, not an assertion.

**Which route a future seat should re-open, and what it needs.** **Route 3** — the only one that
produced a real constraint rather than a coincidence, and it is blocked by **missing bookkeeping,
not by a theorem**. Pin the normalisation of the k-coupling and the well-definedness of `exp(2πiS)`
becomes a genuine equation relating the level to the framing anomaly `exp(2πi c/24)` — **the only
place in this entire structure where `c` appears in an equation rather than as a free anchor.**
That is a crossing *candidate*. **Routes 1 and 2 are closed and should not be re-run.**

---

## 7. What this arc does NOT claim

Not that `σ = 0.4741…` or `c = 2.8448` is a prediction — they are a **refuted candidate**, printed
in advance by the seal · not that a constraint on `k` is a crossing · not that `0.474128` is a
supremum (measured to degree 8) · no identification of any topological integer with `k` (B290
forbids it, and P5 re-derives why) · no physics reading, no identification (E82's class), nothing
to `CLAIMS.md`.

**Locks / artifacts:** `verification/path_a.py` (P1–P6), `verification/path_a.json`,
`verification/path_a.out`, `verification/reproduce.sh`.
