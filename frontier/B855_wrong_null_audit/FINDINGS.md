# B855 — the wrong-null audit: the programme's genericity controls were family members, and so was the fix I proposed

cc banking seat, 2026-08-02. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — an audit of controls already used; its footing is that every number here is
recomputed.

## 0. The error, including mine

A genericity verdict is only as good as its null. The corpus has repeatedly concluded
*"object-specific"* or *"generic"* by comparing m004 against **m003** — which B803 already
establishes is **commensurable** with it. Since the invariant trace field is a commensurability
invariant (Reid), any property downstream of it is shared **by theorem**, and the comparison could
not have come out otherwise.

**I flagged that, proposed m129 as the genuine non-commensurable null, and was wrong.**

## 1. The family has TWO rows, and m129 is in the second one

Humbert covolumes recomputed here: `covol PSL(2,O₋₃) = 0.169156934401608938`,
`covol PSL(2,O₋₁) = 0.305321864725739672`.

| manifold | field | volume | **index** | |
|---|---|---|---|---|
| **m004** | ℚ(√−3) | 2.029883212819307 | **12** | GOLDEN, m = 1 — the object |
| m003 | ℚ(√−3) | 2.029883212819307 | **12** | the sister |
| m206 | ℚ(√−3) | 4.059766425638615 | **24** | used as a B723 witness |
| **m136** | ℚ(i) | 3.663862376708876 | **12** | **SILVER, m = 2** |
| **m129** | ℚ(i) | 3.663862376708876 | **12** | **the null I proposed** |
| m135 | ℚ(i) | 3.663862376708876 | **12** | |

> **m129 is index 12 in PSL(2,O₋₁) — the silver's class-mate.** It is a valid control for the
> golden row and for nothing else. **The family has two rows, and the repo has no registered null
> non-commensurable with both.**

## 2. Two corrections to the record, verified directly

**m003 is amphichiral.** `is_amphicheiral() = True`, computed. `B296/VERDICTS.md` describes it as a
*"non-amphichiral control"* in the line concluding that the CS sign law is *"object-specific, not a
SnapPy convention artifact."* The control is mislabelled on the axis the verdict turns on, **and**
it is commensurable.

**No knot complement is commensurable with 4₁.** By Reid, the figure-eight is the **unique**
arithmetic knot complement in S³, and commensurability preserves arithmeticity. Yet **B438, B440,
B443** and `docs/CAMPAIGN_STATUS.md` assert *"{4₁, 5₂} … a commensurability class"* and *"the
forced child inherits its parent's commensurability class."*

**That error inverts in the dangerous direction.** A property shared with 5₂ is shared across
*non-commensurable* manifolds — which is the corpus's **strongest genericity evidence**. Filing it
as *"commensurability-shared"* recodes it as forced, and thereby protects it from the genericity
reading it actually supports.

The genuinely interesting fact underneath is narrower and better: at slope 5 **only**, two
non-commensurable parents give the same child, `4₁(5,1) ≅ −5₂(5,1)` (B467's `f3_wall.py`).

## 3. What a valid null looks like

Different invariant trace field from **both** rows. Candidates, with `amphichiral` computed:

| candidate | field (reported) | amphichiral |
|---|---|---|
| m009 / m010 | ℚ(√−7) | **False** |
| m015 = 5₂ | cubic, disc −23 | **False** |
| m022 / m023 | disc 697 | — |
| m039 / m040 | cubic, disc −44 | — |

Amphichirality matters independently: if a verdict turns on an orientation-odd property, the null
must be matched on amphichirality **as well as** non-commensurable, or the comparison confounds two
variables. **m003 fails both conditions at once**, which is how it produced clean-looking results.

## 4. A bug in this arc, caught before banking

The first version of this script **overrode each computed volume with a hardcoded class value keyed
on the field** — which would have forced every row to index 12 *by construction* and made the whole
audit vacuous. Caught and fixed; the corrected run is strictly more informative, since m206 comes
back at **index 24** rather than a manufactured 12.

Same defect family as the rest of this session: the artifact computing something narrower or other
than the criterion states.

## 5. Reported by the scan, NOT verified here

Recorded so they are not mistaken for computed results in this arc. Each needs independent
recomputation before it moves anything:

- **B289/B296's CS sign law** reportedly holds 164/164 on **m136** and 168/168 on **m135**
  (non-commensurable with m004), with m003's 0/156 being a peripheral-basis artifact that becomes
  116/116 under `A = ±[[−1,−1],[0,1]]`. If so, *"object-specific"* fails and the real discriminator
  is **amphichirality plus an aligned basis**.
- **B290's π/√3** reportedly equals `2π/|τ|`, real for **any rectangular cusp** — so
  rectangular-cusp-specific, with only the *value* being m004's.
- **B723's witnesses** m006/m007 reportedly have invariant trace field `x³+2x−1` (disc −59, degree
  3, non-arithmetic), **not ℚ(√−3)** as that arc states.

## 6. Honest direction of the net

**These corrections mostly deflate.** *"Object-specific"* becomes *"class-specific"* or
*"rectangular-cusp-specific"*; the 5₂ mislabel was concealing genericity rather than manufacturing
it. That is the direction the arithmetic runs, and it is not inverted here to be agreeable.

**The constructive half is equally real: the programme has never had a valid control, so
"generic vs specific" has essentially never been tested.** Every such verdict in the corpus can now
be re-run against a null that can actually decide — which is a larger, cheaper, and more
informative programme than the one it replaces.

## Carried forward

1. **Re-run the genericity verdicts against a two-row-valid null.** Highest value: B727's
   *"decisive"* control label, B289/B296, B282.
2. **Correct the 5₂ polarity** in B438, B440, B443 and `CAMPAIGN_STATUS` — and re-read what those
   arcs actually established once "commensurability-shared" is removed.
3. **Independently recompute** the three §5 items.

`tests/test_b855_wrong_null.py`
