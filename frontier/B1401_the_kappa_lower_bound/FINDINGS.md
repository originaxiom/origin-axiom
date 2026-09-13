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
