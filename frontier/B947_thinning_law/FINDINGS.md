# B947 — L130: is the thinning law a LAW? **OUTCOME SPECIAL** — 5 of 7, and the seal's own gloss was wrong

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS. Gate 5 untouched.
**Preregistration sha-256:** `610fa7119c6a…` — sealed, ledgered and pushed **before compute**.
Prior disclosed as **SPECIAL, moderately favoured**; LAW named as the convenient answer
required to clear the higher bar. **It did not.**

---

## The verdict, against the sealed criterion

> **OUTCOME SPECIAL** — the pattern fails for **at least one** non-excluded family.

**Two fail: `mu_charge` and `kappa_compact`.** The criterion fired exactly as written.

**Banked-identity gate: PASSED** (B946's V-table factorisations reproduced inside the
pipeline before any new number was read).

**Vacuity exclusion: EMPTY.** No family had total prime support ≤ 3, so **nothing was
excluded** — the pre-declared exclusion rule could not have been used to shape the result.

## The table

| family | leading | constant | mid-only primes | holds? |
|---|---|---|---|---|
| **V** (hierarchy) | {953} | {2,3} | 13, 17, 1129, 421493 | ✅ |
| **W** (mixing²) | {953} | {5} | 3, 367, 677 | ✅ |
| **d_S** (twist) | {2,3} | {953} | 5, 11, 35257 | ✅ |
| **d_A** (twist) | {2,3} | {953} | 23 | ✅ |
| **m_S** (flip mass) | {2,3} | {20417473} | 11, 71, 151, 349 | ✅ |
| **μ** (charge cubic) | {2,3,5,7,11} | {13} | **—** | ❌ |
| **κ** (compact cubic) | {2,3,5,7,11,31} | {19} | **—** | ❌ |

## Where the seal was imprecise, and what I am NOT banking

The prereg's SPECIAL branch read: *"Then **V is special**, the thinning is about V alone,
and B946's law-shaped phrasing must be narrowed **to V** in LAW_MAP."*

**That gloss is not what the data says.** **Five** families hold the pattern, not one. The
*criterion* (≥ 1 live failure ⟹ SPECIAL) fired correctly and its verdict stands; but its
editorial description of what SPECIAL would mean was **written too crudely at seal time**,
and I am not banking a conclusion the computation contradicts.

**What I do bank, honoring the commitment:** B946's law-shaped phrasing **is** narrowed —
the thinning is **not** a law over the value layer as B946's LAW_MAP row implied. What
replaces it is scoped to the five families that hold it, with the two failures named.

## The observation I am flagging as POST-HOC, not claiming

The 5/2 split is not scattered. The five that hold are the **value families** — hierarchy,
mixing overlap, the two twists, the flip mass. The two that fail are the **pencil cubics**
— μ (charge) and κ (compact) — which are structural/geometric objects rather than value
families, and which fail in the *same way*: **fat leading coefficient, empty mid-only set.**

> **This was seen after the results and is therefore POST-HOC.** It is registered, not
> claimed. If it is real it needs its own sealed cell with the value/pencil partition
> declared in advance — which is exactly what this cell could not do, having declared only
> a per-family pass/fail. **Registered as L137.**

The temptation here is obvious: a 5/2 split along a meaningful line reads like a discovery,
and re-describing SPECIAL as "the thinning law holds on the value layer and fails on the
pencils" would convert a failed prediction into a success story. That would be
post-hoc rescue, and the seal exists to prevent exactly it.

## Honest limits

1. The pattern's definition (|P_lead| ≤ 2, |P_const| ≤ 2, |P_mid_only| ≥ 1) was fixed in the
   seal. It is one reasonable formalisation of "thin extremes, fat middle" and not the only
   one; a different threshold could move borderline families. None here is borderline —
   the two failures have **empty** mid-only sets and leading supports of size 5 and 6.
2. Seven families is a small sample; the split is 5/2, not 50/50, but no significance claim
   is made.
3. This does not disturb B946: its **exact arithmetic** (e₃/λ⁴ = 27, λ forced, the
   degree-graded residue for V) is untouched. What is narrowed is only the **generalisation**
   B946 offered from V to the value layer.

---

**Verdict: OUTCOME SPECIAL.** The thinning is not a law over the banked families; it holds
for five and fails for two. The disclosed prior was correct, the convenient answer did not
clear the bar, B946's LAW_MAP phrasing is narrowed as committed — and the structured
appearance of the failure is registered as **L137, post-hoc**, rather than banked as a
finding.
