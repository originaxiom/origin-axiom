# B1401 — |κ−2| AS A LOWER BOUND ON J: all five values confirmed, and the bound is ATTAINED on a parabolic meridian in every one

**Incoming (relay):** *"|κ−2| is a genuine invariant and a lower bound on J — m004 = 1 (attained, per
Callahan), m009 = √2, m003 = 4, v2873 = 3√3, m202 = 7."* Plus: the 3-generator values are
**withdrawn entirely**.

**All five recomputed here on the geometric holonomy. All five exact.** And the verification does
more than confirm: it supplies the **logical link** the relay states as two separate claims, and it
finds the bound **attained in all five cases**, not only at m004.

---

## 1. The five values — EXACT

| manifold | cusps | `|κ−2|` measured | claimed | |
|---|---|---|---|---|
| **m004** | 1 | `1.000000000` | 1 | ✓ |
| **m009** | 1 | `1.414213562` | `√2` | ✓ |
| **m003** | 1 | `4.000000000` | 4 | ✓ |
| **v2873** | 1 | `5.196152423` | `3√3` | ✓ |
| **m202** | **2** | `7.000000000` | 7 | ✓ |

All on the default 2-generator presentation, `κ = tr[a,b]`. (m202 is **two**-cusped — worth noting
since the other four are one-cusped.)

## 2. The two claims are ONE claim: the bound FOLLOWS from the invariance

Jørgensen: for non-elementary discrete `⟨A,B⟩`, `|tr²A − 4| + |tr[A,B] − 2| ≥ 1`, and

> `J(G) = inf over GENERATING PAIRS of ( |tr²A − 4| + |tr[A,B] − 2| )`.

**If `κ` is pair-independent**, then every pair contributes `|tr²A − 4| + |κ−2|`, and since
`|tr²A − 4| ≥ 0`:

> `J(G) = |κ−2| + inf |tr²A − 4| ≥ |κ−2|`  — **the lower bound is a corollary of the invariance,
> not a second fact.**

And **equality requires `|tr²A − 4| = 0`, i.e. `tr A = ±2`, i.e. `A` PARABOLIC.** That is the whole
content of "attained".

## 3. Invariance — holds, and MY FIRST READING OF IT WAS WRONG

`verification/b1401_kappa_values.py` first reported `|κ−2|` **varying** across generating pairs
(m004: 1 vs 3; m009: √2 vs 4; v2873: 3√3 vs 9), which would have refuted the invariance claim.
**That reading is WITHDRAWN.** The offending pair was `(a²b, b)`, which is **not an elementary
Nielsen move**: `⟨a²b, b⟩` contains `a²` and `b`, not necessarily `a`, so it need not generate the
same group at all. And `κ = tr[a,b]` is **conserved by the Markov/Vieta moves** (Fricke–Vogt) — the
very conservation this bench used in B1347's stratum classifier. **So a differing `κ` is evidence of
a different Nielsen class, not evidence against invariance.**

Redone with genuine Nielsen moves only — 12 equivalent pairs per manifold:

| manifold | `|κ−2|` | spread over 12 pairs |
|---|---|---|
| m004 | 1.000000000 | `6.0e−15` |
| m009 | 1.414213562 | `4.0e−15` |
| m003 | 4.000000000 | `2.7e−15` |
| v2873 | 5.196152423 | `5.1e−13` |
| m202 | 7.000000000 | `4.4e−15` |

**Constant to machine precision in every case.**

**The scope that must be stated, because it is exactly E72's hazard.** Nielsen-invariance is not the
same as invariance over *all* generating pairs: a group can carry Nielsen-**inequivalent** generating
pairs, and if one of those had a smaller `|κ−2|` the bound would fail. **E72's own instance is two
κ's on two different groups** (B309's meridian pair vs B448's fibre pair). So the right statement is
**"invariant of the Nielsen class"**, and the bound is rigorous modulo *no inequivalent class having a
smaller κ*. Weak supporting evidence: the three non-Nielsen pairs sampled all gave **larger** values
(3, 4, 9 against 1, √2, 3√3) — consistent with the default class being the minimiser, though those
pairs may not be generating pairs at all.

## 4. THE BOUND IS ATTAINED IN ALL FIVE, not just at m004

`verification/b1401_parabolic_and_bound.py`. Attainment needs a parabolic generator, so: is there one?

| manifold | `|tr(meridian)|` | parabolic? | `|κ−2|` on `(mer, a)` | on `(mer, b)` | default |
|---|---|---|---|---|---|
| m004 | 2.000000 | **yes** | 1.000000 | 1.000000 | 1.000000 |
| m009 | 2.000000 | **yes** | 1.414214 | 1.414214 | 1.414214 |
| m003 | 2.000000 | **yes** | 4.000000 | 4.000000 | 4.000000 |
| v2873 | 2.000000 | **yes** | 5.196152 | 5.196152 | 5.196152 |
| m202 | 2.000000 | **yes** | 7.000000 | 7.000000 | 7.000000 |

**Every one has a parabolic meridian, and a meridian-containing pair reproduces the default `κ`
exactly.** So on that pair the Jørgensen sum is `0 + |κ−2| = |κ−2|`, giving `J ≤ |κ−2|`; with §2's
`J ≥ |κ−2|`:

> ### `J = |κ−2|` exactly, attained, for all five — **provided the meridian pair generates.**
> That proviso is the one unproved step. It is **known for m004** (Callahan, which the relay cites),
> and for the other four the κ-match is *consistent with* Nielsen-equivalence to the default pair but
> does not prove it — equal κ is necessary, not sufficient.

**This is stronger than the relay claimed.** They said *lower bound*; the computation says the bound
is **reached** on a parabolic-meridian pair in all five. So, modulo the generating step, these are the
**Jørgensen numbers themselves**: `J(m009) = √2`, `J(m003) = 4`, `J(v2873) = 3√3`, `J(m202) = 7`.

**One detail that matters and is easy to miss:** the **default presentation pair does not attain `J`
for m004** — its sum is `3.605551 + 1 = 4.605551`, well above `1`. The infimum is genuinely over
pairs, and the minimiser is the parabolic one. Anyone re-deriving `J` from the default presentation
will get the wrong number.

## 5. Where this meets the banked record

`|κ−2| = 1` on m004's **meridian** pair is **B309's banked "unit obstruction"** (`κ−2 = ω²`,
`|κ−2| = 1`), which B1345 already identified as the same fact as `J(m004) = 1` seen from the other
side. This arc adds *why* the two coincide: the meridian is parabolic, so the `|tr²−4|` term drops
and the Jørgensen sum collapses onto `|κ−2|`. **The unit obstruction is the Jørgensen number because
the meridian is parabolic** — one sentence that was implicit and is now explicit.

## 6. The 3-generator withdrawal

The relay withdraws its 3-generator values entirely. **Nothing here depends on them:** all five
manifolds above carry **2-generator** presentations (verified), so no 3-generator quantity enters any
number in this arc. Recorded so the withdrawal is not mistaken for a gap.

## 7. Fences

Nothing reaches `CLAIMS.md`, F2 or Gate 5. **No value is compared to any measurement** — these are
invariants of manifolds, not couplings, and no physical reading is proposed. The Jørgensen-number
identifications in §4 are stated **with their unproved step named**.

---

# ADDENDUM 1 — THE GENERATING STEP, CLOSED FOR FOUR OF FIVE; AND §4's "ALL FIVE" IS CORRECTED

§4 left one proviso: *"provided the meridian pair generates."* That proviso is now discharged for
**four** of the five — **and for m202 the pair I actually used turned out NOT to generate**, so §4's
"attained for all five" was, as written, unsupported for one manifold. Corrected below.

## 1. The meridian words settle three immediately

| manifold | `meridian(0)` | argument |
|---|---|---|
| **m004** | `ab` | `a⁻¹·(ab) = b`, so `⟨ab, a⟩ = ⟨ab, b⟩ = ⟨a,b⟩` — **PROVED** |
| **m009** | `ab` | same — **PROVED** |
| **v2873** | `BA` `= (ab)⁻¹` | `⟨(ab)⁻¹, x⟩ = ⟨ab, x⟩` — **PROVED** |
| m003 | `ABABB` | `a` occurs twice; not immediate |
| m202 | `bbAbA` | not immediate |

## 2. THE CORRECTION: m202's meridian pairs provably do NOT generate

A **necessary** condition: `⟨P, x⟩ = π₁` forces the images of `P` and `x` to generate `H₁`. Computed
from exponent vectors against the abelianised relators:

| manifold | pair | index in `H₁` | verdict |
|---|---|---|---|
| m003 | `(mer, a)` | 1 | allows |
| m003 | `(mer, b)` | **2** | **FORBIDS** |
| **m202** | `(mer, a)` | **3** | **FORBIDS** |
| **m202** | `(mer, b)` | **2** | **FORBIDS** |

> **So for m202 both meridian pairs fail a necessary condition.** The pair §4 exhibited is not a
> generating pair, contributes nothing to the infimum, and yields **no** upper bound on `J`.
> **§4's claim of attainment "in all five" is withdrawn as stated.**

## 3. …and attainment is RECOVERED, from other parabolics

The meridian is not the only parabolic: on a cusp the whole peripheral subgroup is parabolic, and
m202 has **two** cusps. Searching meridians and longitudes on every cusp:

| manifold | parabolic | pair | `H₁` test | `|κ−2|` | generation |
|---|---|---|---|---|---|
| **m202** | `longitude(0) = 'bba'` | `(bba, b)` | passes | **7.000000** | **PROVED**: `b⁻²·(b²a) = a` |
| **m202** | `meridian(1) = 'bbAb'` | `(bbAb, b)` | passes | 7.000000 | **PROVED**: `b⁻²·(bbAb)·b⁻¹ = a⁻¹` |
| m003 | `longitude(0) = 'ABAbab'` | `(lon, a)` and `(lon, b)` | both pass | 4.000000 | not proved |
| m003 | `meridian(0) = 'ABABB'` | `(mer, a)` | passes | 4.000000 | not proved |

**m202 is therefore PROVED after all** — via the *longitude* (or the second cusp's meridian), not the
first meridian. **m003 remains the one open case:** three candidate pairs pass the necessary
condition and reproduce `κ = 4`, but none has a word from which the missing generator is immediately
recoverable (`ABABB` and `ABAbab` each contain `a` more than once), so generation is **not proved**.

## 4. The corrected statement, with the two directions kept apart

The two bounds have *different* status and §4 bundled them:

**UPPER, `J ≤ |κ−2|` — now ESTABLISHED for four of five** (m004, m009, v2873, m202), by exhibiting a
parabolic **generating** pair whose Jørgensen sum is `0 + |κ−2|`. Conditional for **m003** only.

**LOWER, `J ≥ |κ−2|` — still conditional for four of five.** It needs `κ` constant over *all*
generating pairs, not merely the Nielsen class (§3's E72 caveat), and nothing here touches that.

**The exception, and it is the interesting one: m004 needs neither proviso.** Jørgensen's inequality
gives `J ≥ 1` **unconditionally**, and `|κ−2| = 1`, so the lower bound is free:

> ### `J(m004) = 1` is fully established, with no open premise. It is the only one of the five that is.
> That is exactly because m004 sits at the **floor** of Jørgensen's inequality — which is what makes
> B309's `|κ−2| = 1` a *unit* obstruction rather than merely a small one, and why m004 is the case
> Callahan could settle.

For the other four the honest form is: **`J ≤ |κ−2|` (proved, except m003), with equality if and only
if no Nielsen-inequivalent generating pair carries a smaller `κ`.**

## 5. What I got wrong, plainly

§4 said "attained in all five, provided the meridian pair generates". Two defects: the proviso was
stated once but needed **per manifold**, and for m202 it is **false** for the pair I used. The fix
strengthens the result for four manifolds and isolates m003 — but the original sentence asserted
more than the computation supported, and the abelianisation test that caught it is three lines long
and should have been in §4.

---

# ADDENDUM 2 — L206 (m003) ATTEMPTED AND **NOT SETTLED**: three methods, three diagnosable failures

Addendum 1 left m003 as the single open case. **It is still open.** This records what was tried, why
each failed, and what the failures narrow — a bounded negative is worth more than a silent one.

## 1. What was tried

| method | outcome | why |
|---|---|---|
| **Coset enumeration** (Todd–Coxeter, sympy `FpGroup.index`) | **did not terminate** — not even on the m004 **control**, where the answer is index 1 | Todd–Coxeter terminates only at **finite** index, and is slow on 2-generator 1-relator hyperbolic groups even then |
| **One-way Nielsen BFS** on matrices | **control passed** (m004 at depth 1–2); m003 **exhausted at depth 7**, 232K pairs | the holonomy is discrete and faithful, so matrix equality *is* word equality — the method is sound, the reach was short |
| **Bidirectional Nielsen search** | **control passed**; m003: **no meeting point at Nielsen distance ~12**, 28.7K pairs each side | Nielsen moves are invertible, so half-depth `d` covers distance `2d` |

## 2. What the failure narrows — this is the useful part

> **If m003's `(mer,a)`, `(mer,b)`, `(lon,a)` or `(lon,b)` is a generating pair at all, its Nielsen
> distance from `(a,b)` EXCEEDS 12.**

For contrast, on the manifolds that are settled the pairs are **immediate**: m004's sit at Nielsen
distance **1 and 2**; m202's longitude pair is a one-line word identity (`b⁻²(b²a) = a`). **m003 is
not merely unlucky — it is structurally different**, and the possibility that its parabolic pairs
simply **do not generate** (as m202's meridian pairs provably do not) is live. The `H₁` index test
allows them, but that is necessary-only.

## 3. THE METHODOLOGICAL FINDING — E75 again, and raising precision made it WORSE

The bidirectional search **failed its own m004 control on the first run**, which is the only reason
the bug was caught. Diagnosis, run rather than guessed: `a·b` and the meridian **are the same
matrix** — they differ by `3.3e−16` — and the pivot agreed. But the key used **`mp.nstr(x, 14)`,
which prints *significant* digits**, so the near-zero entries printed their full noise mantissa:

```
key(a*b) : ... ('-3.3869186896553e-82', ...) ('6.2894787754431e-16', '1.0')
key(mer) : ... ( '1.102397795803e-82',  ...) ('9.211786308461e-16', '1.0')
```

**Two copies of one matrix, two different keys.** And the earlier **float** version had worked
precisely because `np.round` rounds **absolutely**, sending both to `0.0`.

> **Raising the precision from float64 to 80 digits made the bug worse, not better** — more precision
> means more noise digits printed. Fixed by rounding **absolutely** (`round(float(...), 10)`), after
> which the control passes and the ball *shrinks* from 8731 pairs to 1960, the excess having been
> duplicates of the same pair under noise-distinct keys.

**This is E75's third instance and its second mechanism.** The class was diagnosed as rounded keys
and `argmax` pivots flipping at boundaries; this adds **relative (significant-digit) formatting of
near-zero values**, which is the same disease with the opposite cure to the intuitive one.

## 4. What would settle it — named, not attempted

**Refute** rather than prove: if both words lie in a proper finite-index subgroup, generation is
**decisively** refuted. Low-index subgroups of `π₁(m003)` correspond to covers, and membership is
"the word fixes the basepoint" in the permutation representation. **SnapPy's `cover_info()` does not
expose that permutation rep** (checked — `m003` has 2 covers of index 4 and the object carries only
base/type/degree), so this needs another route: a coset table from another system, or constructing
the permutation reps directly from the presentation.

**Or prove:** push the bidirectional search past distance 12, which costs roughly `5.5×` per extra
half-depth — or find a parabolic in the peripheral subgroup whose reduced word contains one generator
exactly once, which would close it in one line as m202's longitude did.
