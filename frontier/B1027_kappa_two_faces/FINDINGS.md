# B1027 — κ = 2 IS THE FREE CHAIN: the founding sentence's "nothing" has three banked meanings, and the curated layer carried one

**Date:** 2026-08-11 · **Lane:** MATHEMATICS, exact. **Gate 5 untouched** — structural identity,
no measured value, nothing to `CLAIMS.md`.
**Band:** CONSOLIDATION REFRESH, B100–B499. **Files:** `compute.py` → `results.json` ·
lock `tests/test_b1027_kappa.py`.

**Scope, carried verbatim from B505 and not softened:** *"Form-level; **NOT** a B398 crossing."*
This is an identity between the object's own invariant and a model Hamiltonian's coupling
parameter. **It is not a physics value claim and does not touch the value wall.**

---

## 1. THE FINDING

`THE_FRAMEWORK`'s bridge equation says **κ = 2 ⟺ the cancellation completes ⟺ nothing** — the
formal content of the founding sentence. **Three further banked arcs say what κ = 2 *is*, and no
curated consolidation carries any of them.**

| arc | what κ = 2 is there | curated surface? |
|---|---|---|
| B309/B518 | the cancellation completes ⟺ **nothing** | ✅ restored by B1010 |
| **B160** | `κ = 2 + λ²` on the **transfer-matrix** form ⟹ κ = 2 ⟺ **λ = 0** | ❌ none |
| **B505** | `κ − 2 = 4λ²` — κ **is** the squared coupling of the **measured** (KKT/Sütő/Bellissard) quasicrystal chain; κ = 2 is **the free metal** | ❌ none |
| **B162** | across the foliated κ-sweep, **κ = 2 is the *unique* fiber with positive-measure spectrum**; every other κ gives a zero-measure set | ❌ none |

> ### The founding sentence's "nothing" is the **uncoupled chain** — and it is the one point in the whole κ-foliation whose spectrum is not a Cantor set.

## 2. THE RECONCILIATION — done first, because the two arcs disagreed on their face

B160 pins `κ = 2 + λ²`; B505 pins `κ − 2 = 4λ²`. **A restoration that quoted either without the
other would have banked a wrong constant.** Both were therefore re-derived from scratch here,
from the transfer matrices, importing nothing:

```
T_± = [[E ∓ a, −1], [1, 0]] ,      κ = tr[T₊, T₋]

a = λ    →  κ = 4λ² + 2      (B505's convention)
a = λ/2  →  κ =  λ² + 2      (B160's convention)
```

**They are ONE identity.** `κ(λ) → κ(λ/2)` carries the first to the second exactly — the factor 4
is precisely the ±λ vs ±λ/2 choice B505 flags in its own text. **Neither arc is wrong; the
collision is a normalisation, and it is now declared.**

**And the chain closes through two more arcs nobody had joined to these:**

- **B36:** the Fibonacci initial line has `I_FV = λ²/4` — verified here by substituting
  `x = (E−λ)/2, y = E/2, z = 1` into `x²+y²+z²−2xyz−1`.
- **B148:** `κ = 4·I_FV + 2` exactly.
- Compose: `κ = 4(λ²/4) + 2 = 2 + λ²` — **B160 re-derived from B36 + B148**, a third independent
  route to the same law.

## 3. TWO CONSEQUENCES THAT FELL OUT, neither previously stated

**(a) κ is independent of the spectral parameter.** `∂κ/∂E = 0` identically — E drops out of the
commutator trace. So κ is a property of the **coupling**, not of where in the spectrum you look.
That is what licenses reading it as *the* coupling coordinate rather than one observable among
many.

**(b) At κ = 2 the two letters become the same matrix.** `λ = 0` gives `T₊ = T₋ = [[E,−1],[1,0]]`,
so **no word in the two letters is distinguishable from any other** — the substitution carries no
information at all. *"The cancellation completes ⟺ nothing"* is, on this face, exactly the
statement that **the alphabet collapses**. Stated as a reading of the mathematics, not as a
result beyond it.

## 4. TWO FURTHER ABSENCES IN THE SAME REGION

Found by the same sweep, verified present in their arcs and absent from every curated surface:

- **B332** — *"the two arithmetic ends are the **product and the ratio of the founding
  substitution's two letters**: `R·L` has disc 5 (ℚ(√5), E₈) and `−R·L⁻¹ = g` has disc −3
  (ℚ(√−3), E₆)."* The two-ended structure — **Layer 1 of `THE_FRAMEWORK`** — derived directly
  from the two letters. *(B332's own note: it corrects a handoff's inverted labelling.)*
- **B180** — *"κ is literally one conserved quantity on both the character-variety and spectral
  faces."* The statement that the two faces share the invariant — the premise this arc's whole
  reconciliation rests on — is itself uncited.

## 5. WHAT IS NOT CLAIMED

- **No novelty.** The Fibonacci-Hamiltonian trace map and its Fricke–Vogt invariant are standard
  (Kohmoto–Kadanoff–Tang, Sütő, Bellissard, Damanik–Gorodetski). The content is the
  **reconciliation** of two banked normalisations and the **joining** of four arcs that were
  never joined.
- **No physics.** κ's identification with a model coupling is form-level. B505 says so; this arc
  repeats it rather than quietly dropping it.
- **B162 is cited, not re-verified.** Its positive-measure claim is a spectral-measure result
  this arc did not recompute; it is carried at B162's own grade.

---

**Verdict: PROVED.** Two banked normalisations of the same law reconciled from scratch before
either was restored; a third independent derivation found by composing B36 with B148; and the
founding sentence's κ = 2 identified, on the transfer-matrix face, as the free chain in which the
alphabet collapses.
