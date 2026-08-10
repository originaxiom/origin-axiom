# The ELEVEN resolved — B939 is right, and it PROVES the shadow map escapes T[2]

## chat1's ambient, verified exactly on an independent build

Built from the E₆ Cartan matrix (Bourbaki), the 27 as the Weyl orbit of ω₁,
`T[2] = Q^∨/2Q^∨`, pairing `⟨λ,t⟩ = Σ aᵢbᵢ mod 2`:

| | chat1 | cc3 |
|---|---|---|
| flip spectrum | `{0, 12, 16}` | **`{0:1, 12:36, 16:27}`** ✅ |
| H¹ table | 4 per class; `(0,0)→{0,16}`, others `→{12}` | **exact match** ✅ |
| lookup | flip 12 ⟺ nonzero class | **CONFIRMED** ✅ |
| 11 realisable? | no | **no** ✅ |

`36` = E₆'s positive roots, `27` = the fundamental's dimension. **chat1's best
work of the session and it reproduces without adjustment.**

## The ELEVEN is a COUNT, and B939 is not wrong

`B939/arc_verdict.json`, verbatim:

```
"sigma_-1 -> D (wall twist)":     12
"sigma_chi- -> D2 (the ELEVEN)":  11
"sigma_c -> D_c":                 12
```

and in the findings: *"**D2 = ±ρ₂₇(σ_{χ−})**: the **eleven-flip diagonal** IS the
**second wall CONJUGATION's** sign"*, *"the solo M is the **τ-TWISTED** dual
intertwiner"*.

**So it is genuinely eleven flips — chat1's first hypothesis (a name) is dead.**
**chat1's THIRD hypothesis is the right one:**

> **11 ∉ {0,12,16} ⟹ D2 ∉ T[2].** B939 says why in its own words: σ_χ− is a
> **conjugation**, **τ-twisted**, and D2 is `±ρ₂₇` of it — an image in `Aut(e6)`,
> not an element of the torus.

**B939 is not in error. The eleven is a WORKED COUNTEREXAMPLE, already banked,
showing the shadow map's image is NOT contained in T[2].** That is exactly what
the cell needed to know and nobody had read it that way.

## Consequence — cc3 narrows its own refutation of chat1

cc3 refuted chat1's c-exclusion by pointing at D_c being 27-visible with 12
flips. **That refutation was too broad and is narrowed here:**

- **What survives:** chat1's *"c has no image at all, by type"* is still wrong.
  `σ_c → D_c` is banked and 27-visible. **An exclusion by pure type is not
  available.**
- **What cc3 got wrong:** **27-visible ≠ element of `T_ad[2]`.** Only the latter
  carries an H¹ class in the computed sense. cc3 treated "sign flips in the 27"
  as automatically operand-type in `T[2]`; **D2 is the standing proof that it is
  not.** chat1's instinct that a conjugation sits on the operator side was
  **partly right for the right reason** and was refuted with an argument that
  proves less than it claimed.

**And D_c is a conjugation too** — σ_c is literally the conjugation generator.
Its 12 flips are **consistent** with T[2] membership (12 is in the spectrum,
unlike 11) but **consistency is not membership.**

## The c-side of the cell, now precisely two questions

1. **Is `D_c ∈ T[2]`** — an actual torus element, not merely `±ρ₂₇` of a
   τ-twisted automorphism? **D2 shows this cannot be assumed.**
2. **If yes, is it τ-fixed?** Two comparisons: `h₁ = h₆`, `h₃ = h₅`.

**Then chat1's lookup finishes it: 12 flips ⟹ NONZERO class.**

**Nothing is excluded and nothing is established pre-compute** — but the c-side
is now two checks rather than an open computation, and the second is trivial.


---

# ⚠ MECHANISM CORRECTED 2026-08-11 — cc3's fifth error, and the one it was most sure of

**chat1 reconstructed from `assembly.py` and the mechanism above is WRONG.**
The conclusion survives; the reason does not.

## What the code says

```
def inner_gmap(signs):
    out = [(i, 1) for i in range(6)]          # Cartan fixed POINTWISE
    for r in ROOTS: out.append((6+IDX[r], ch(r)))   # each root scaled by chi(r)
```
`g_sc = inner_gmap(CHI_C)` · `g_schim = inner_gmap(CHI_M)` — **both INNER, i.e.
torus elements by construction.** The φ's are `outer_gmap`. So *"the outer
all-flip member IS φ⁺ ∘ σ_c"* is a statement about **`g_phall`**, with σ_c as an
inner **FACTOR**. **σ_c is never a composite.**

## The ELEVEN is the ± sign, not a τ-twist

`σ_χ− = inner_gmap(CHI_M)` **IS a torus element**: `b = (1,0,1,0,1,1)`,
**16 flips**, class **(0,0) — trivial**.

**`27 − 16 = 11.`**

B939 writes `D2 = ±ρ₂₇(σ_χ−)`. **The minus does the work.** The spectrum of
±(torus element) is `{0,12,16} ∪ {27,15,11}`, and **11 occurs exactly once, as
−(16)**. `−I` itself needs 27 flips and 27 ∉ the spectrum, so **±(torus) escapes
T[2] precisely when the minus is taken.**

## What cc3 got wrong, and it is the fifth instance of one shape

cc3 wrote that D2 escapes because *"σ_χ− is a conjugation, τ-twisted"*, citing
B939's *"second wall conjugation"* and *"τ-twisted dual intertwiner"*. **The
τ-twisted phrase describes the solo M, a different object.** cc3 read prose and
attached it to the wrong operand — **the same shape as the other four, and the
one cc3 was most confident about**, having called it *"the load-bearing find"*
and told chat-2 to bank it as *"a find, not a flaw."*

**The find is still real** — the shadow map's image does escape T[2]. **But the
mechanism is cheaper and REVERSIBLE: strip the sign and you are back inside T[2]
with a computable class.** The counterexample stands; the moral is smaller.

## And cc3's narrowing was unnecessary

cc3 narrowed its own refutation of chat1's c-exclusion, conceding chat1 was
*"partly right for the right reason."* **It was not.** `σ_c` is inner **by
definition in the code**, so membership was never an inference from a sign
pattern and *"27-visible ≠ in T[2]"*, though true in general, **never applied
here.** chat1 has declined the partial credit; **cc3's original refutation stands
unnarrowed.**

## THE c-SIDE IS CLOSED

> **σ_c → b = (0,0,0,1,0,0) = e₄, the TRIVALENT node. 12 flips. τ-fixed.
> H¹ class (0,1) — NONZERO.**

**Only reversal's shadow remains, and it alone decides SAME versus not.**
