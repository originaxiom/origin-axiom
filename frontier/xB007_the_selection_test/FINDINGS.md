# xB007 — THE LEAD FAILED ITS FIRST TEST, and failing it proved something better: the character variety is STRUCTURALLY BLIND to what separates the object from its sister

**Status: banked (frontier, seat branch `sep16-branch`). Verdict PROVED.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE any cell ran** — sha256
`3c4bd90bf39f2328058897b901a0f8985c9829a63bb2b8d4d8d9b637bb2f8592`, committed `0e3cde6`.
Gate 5 untouched. Lock: `verification/reproduce.sh`, six cells, each asserting its mathematics.

## The headline, in the form the seal demanded

xB005 Addendum 1 flagged the node's ℤ/3 as *"the first item in this cluster that is not a
commensurability invariant … the right **type** of object for the record's open 'which member of
the class?' questions"*, priced as **a lead at 0.58 bits and nothing more**. The seal named the
expected outcome and made it inconvenient for this seat:

> *"if T4 returns B, then the handle xB005 Addendum 1 flagged does not do the job it was flagged
> for, and the honest report is that the lead failed its first test … This arc will say that in its
> headline, not a footnote."*

> ### **T4 returned B. The lead failed its first test.**

The node's ℤ/3 does **not** break the m003/m004 tie. But the *reason* it fails is worth more than
the lead was: **it cannot break it, and neither can anything else computed on the character
variety.**

## The result against the sealed criteria

| cell | sealed criterion | outcome |
|---|---|---|
| **T1** | population ≥ 5, every volume an integer multiple of `v₀` | **PASS** — **21** members, all integer multiples |
| **T2** | class-invariant battery has **zero** separation power | **PASS** — 1 distinct value each, as the cited theorem requires |
| **T3** | the non-class-invariant separator table | computed; **`H₁` is the only selector** |
| **T4** | does anything but `H₁` break the m003/m004 tie — and does the node? | tie broken by `sym` and the bundle sign; **the node: NO** |
| **T5** | price it honestly whichever way it goes | **outcome B**, reported in the headline |
| **T6** | *(beyond the seal)* **why** | the character variety factors through `PSL(2,ℤ)` |

## T1 — the population, and an independent control on it

`v₀ = vol(H³/PGL(2,O₃))` is **derived, not hardcoded**: `L(χ₋₃,2)` by Hurwitz zeta, cross-checked
against a direct partial sum to 30 digits. **A first draft used `mp.nsum` on the period-3 character
sum and it silently mis-converged** — 0.7725 against the true 0.78130 — which poisoned `v₀` and
made *every* member fail the integrality filter, m004 included. It was caught by re-deriving
**B680's banked identity** as the control:

> `vol(m004) = (3√3/2)·L(χ₋₃,2)` — **re-derived here independently and holding to 28 digits.**

By **Maclachlan–Reid** the invariant trace field `ℚ(√−3)` *is* the commensurability class, so the
population is the census manifolds (tetrahedra ≤ **6**, the reported cutoff) whose shape field is
`ℚ(√−3)`: **21 members**, every volume an integer multiple of `v₀` (24, 48, 60, 72). *This is the
same 21 as xB002's widened B1136 family, `s955`–`s961` included — an independent arrival on the
same set.*

## T2 — the control that the diagnosis is about TYPE

Invariant trace field, arithmeticity, quaternion algebra: **one distinct value each across all 21.**
Zero separation power, exactly as the cited theorem requires. The programme's arithmetic handles are
not weak — they are **categorically incapable** of pointing at a member.

## T3 — and `H₁` is the only selector

| | m004's value | unique in the population? |
|---|---|---|
| volume | 24·v₀ | no (m003) |
| **`H₁`** | **ℤ** | **YES** |
| cusps, tetrahedra, \|sym\|, amphichirality, node order | 1, 2, 8, True, 3 | no |

**B1136's separator `['h1_is_Z']` is confirmed at the commensurability level**, which is stronger
than the shape-field family it was established on.

## T4 — the decisive cell, and a false positive of this seat's own, caught

Cao–Meyerhoff: m003 and m004 are *exactly* the two minimum-volume orientable cusped hyperbolic
3-manifolds. They tie on volume, cusps, tetrahedra, symmetry-group **order**, amphichirality,
monodromy **word**, and **node order**. They differ on `H₁`, symmetry-group **type** (`D4` vs
`ℤ/2 ⊕ ℤ/4`, both order 8), and the bundle **sign**.

**A first draft returned OUTCOME A here, and it was wrong.** `bundle_words` scanned only the `b++`
prefix, so m003 came back `word = None` and T4 read `None ≠ 3` as *"the node breaks the tie"* — an
outcome A manufactured by this seat's own incomplete search, **against its own declared prior**.
B995's rule applies and was applied: *an unexpected positive against a declared negative prior is
exactly when to be most suspicious.* All four prefixes are scanned now:

> **m003 = `b+-LR`, m004 = `b++LR` — the SAME monodromy word, and the SAME node order 3.**

## T6 — beyond the seal: why nothing on that layer can ever break it

Added after the false positive was caught, because *"it did not work"* is worth much less than
*"it cannot work, and here is why."* Three exact steps:

1. **They differ exactly by `−I`.** m004's monodromy is `φ = LR = [[2,1],[1,1]]` (trace 3); m003's
   is `−φ` (trace −3). The difference is the **elliptic involution**.
2. **`H₁` sees that sign.** `H₁ = ℤ ⊕ coker(φ_*−I)`: `det(φ_*−I) = −1` gives **ℤ** (m004),
   `det = 5` gives **ℤ/5 ⊕ ℤ** (m003) — both reproducing SnapPy exactly. So **`H₁ = ℤ`, knot-ness,
   is precisely `det(φ_*−I) = ±1`: the homological shadow of the monodromy's sign.**
3. **The character variety does not.** `−I` induces `a ↦ a⁻¹`, `b ↦ b⁻¹`, and
   `tr(a⁻¹) − tr(a) = tr(b⁻¹) − tr(b) = tr(a⁻¹b⁻¹) − tr(ab) = 0` identically (verified
   symbolically). **`−I` acts trivially; the trace-map action factors through `PSL(2,ℤ)`.**

> **The character variety quotients by exactly the datum that separates the object from its sister.**

## What this costs, and what it buys

**Costs.** The handle does not select, and no character-variety invariant will. **This scopes
xB003, xB004 and xB005 — all three live on that layer.** Whatever selects m004 is not there. This
seat's own lead is priced down to a **diagnosis** and no further.

**Buys — and this is the real result.** *"Knot-ness selects the member"* (xB002's `SCOPE_NOTE_L1`)
has always read like an arbitrary extra input smuggled into a minimality story. It is not:

> **Knot-ness is the one homological datum the object's own character-variety layer is blind to.**

The selection is not arbitrary and it is not free — it happens **exactly at the seam** between what
the trace-map layer sees and what it quotients away. That is a mechanism where the record had a
label, and it is a sharper statement of the premise's limit than *"minimality ties"*.

**Not claimed:** that `H₁` is a *derivation* of the object rather than an input. It remains an
input; T6 says **which** input and **why nothing on that layer can supply it**. The symmetry-group
type also breaks the tie and passes the E33 control (independent of `H₁` across the population),
but it is **not a selector** — `D4` recurs on m203, m412, s596.

## Scope and bounded recall

Census cutoff **6 tetrahedra**, stated not hidden; the commensurability class is infinite and the
population is a finite sample of it. A manifold outside the cutoff is outside this arc's claim. No
arc re-verdicted, `creates_law` false, nothing to `CLAIMS.md`, F2 or Gate 5. No value, no
generation count, no physics reading.

**Provenance.** `verification/selection_test.py` (T1–T6) → `verification/reproduce.sh`. Cross-refs
B680 (the volume identity, re-derived here as a control), B1136 (the separator, confirmed one level
up), xB002 `SCOPE_NOTE_L1`, xB005 Addendum 1 (the lead this arc tests and fails), B995 (the rule
that caught the false positive), Maclachlan–Reid, Cao–Meyerhoff, Reid, Neumann–Reid.
