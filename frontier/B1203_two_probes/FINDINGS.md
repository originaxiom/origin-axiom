# B1203 — TWO PROBES, BOTH NEGATIVE FOR THE PROPOSER: the c-filter cuts nothing, the climb adds nothing (and B148 already knew)

**Status: banked (frontier). Verdict NEGATIVE** (both probes refute what they were built to test —
one of them my own proposal from an hour earlier, the other caught as a duplicate by the instrument
banked two commits ago). `verification/reproduce.sh` → `REPRODUCES`. Gate 5 clean.

## PROBE 1 — c-equivariance as a forcing filter: REFUTED, cut of exactly zero

**The proposal (mine, this session)**: MENU-1 enumerated 11,720 type-respecting maps under a *type*
law only, with no symmetry requirement; since the campaign had just proved that everything —
saddle, obstruction, boundary, shape — is organized by the one involution c, requiring
**c-equivariance** looked like a forcing principle that could cut the menu *before* looking.

**The probe**: cloud's enumerator was fetched and **re-run here — W₁ = 11,720 reproduced
independently** (median gap 3.53e−5, min 1.63e−9). Then the filter was applied. **All 17 tier-1
atoms are real**; c is complex conjugation, which fixes every real number; and {+, −, ×, ÷, √}
preserve reality. **Therefore every tier-1 menu value is already c-fixed and the filter retains
11,720 of 11,720 — a cut of exactly zero.**

**The structural reason, which is the useful part**: B1168's law says object-canonical ⟺ mirror-even
∧ dimensionless. The menu is built entirely from object-canonical atoms, so **it lies wholly inside
the c-even class already**. Requiring what every candidate already satisfies selects nothing.
**Consequence, and it narrows the search**: the forcing theorem the value arm needs **cannot come
from c-equivariance at any tier built from real atoms** — and at a tier admitting ω, the filter's
effect is merely to project back onto the real menu, which is not a selection either. *The forcing
principle must distinguish **within** the mirror-even class; a symmetry the class already respects
can never do it.*

## PROBE 2 — climbing the founding principle: the climb preserves κ, and B148 banked it first

**The owner's question**: the founding rule a→ab, b→a produced the object and its obstruction κ; the
same κ later governed the *relational* bit one level up (B1195/GC-24). Can we keep climbing —
introduce the principle again at each level — and get new mathematics?

**The computation**: reading the climb literally — if the level-1 "letters" are two objects (X, Y),
the principle sends **(X, Y) → (XY, X)** — the Fricke coordinates transform as
(x, y, z) ↦ (z, x, xz − y), and **κ = x² + y² + z² − xyz − 2 is preserved identically, at every rung
(verified to six), and by the whole K₄ of founding rules.** Bite controls discriminate:
(X,Y) → (X², Y) and (X,Y) → (XY, XY) do **not** preserve it.

**So the answer to the question is: the climb is a SYMMETRY of the founding obstruction, not a
generator of new invariants.** Climb as many levels as you like and you meet the same κ. That is
*why* three independently banked results all say "one level, then fixed": cloud's first-beat law
(*the second beat adds no invariant*), B566-S4 (*measurement-of-measurement collapses once, then is
fixed*), and the quine build's count (*external bits = exactly 1, not one per level*). **There is
one bit and not a tower of bits because the ladder's own step conserves the invariant that would
have to change for a new bit to appear.**

**AND THE HONEST PART**: this is **not new** — `frontier/B148_kappa_fricke_metallic/FINDINGS.md`
already banks it: *"The Dehn twists τ_a:(x,y,z)→(x,z,xz−y) and τ_b:(x,y,z)→(z,y,yz−x) both preserve
κ."* The map computed here is τ_a in the substitution's own coordinates. The mathematics is
classical (Fricke; κ is the Out(F₂)-invariant of the rank-2 SL₂ character variety) and was banked in
this corpus long ago. **What is new is only the reading** — that this banked invariance is the
mechanism behind the three "terminates at one" results and behind the single-bit uniqueness. An
interpretation joining banked facts, not a theorem.

## THE INSTRUMENT'S FIRST LIVE CATCH — on its author, within the hour

B1202 built `already_banked.py` because the register had four times called open what the corpus had
proved. Writing this arc, I ran it on my own claim before banking. **It surfaced B148 immediately.**
Without it this would have been the **fifth** instance of the class — and the first one committed by
the seat that had just built the cure. The check works, its threshold is tuned correctly, and its
value is now demonstrated rather than argued.

## What both probes leave

The value arm's forcing theorem cannot be **c-equivariance** (Probe 1: the class already satisfies
it) and cannot be **iteration of the founding principle** (Probe 2: the step conserves κ). Both
candidates were symmetries — and *a symmetry the admissible class respects cannot select within it.*
**The forcing principle, if it exists, must break a symmetry rather than impose one.** That is a
genuine narrowing of where to look, bought with two clean negatives.

## Fences

W₁ = 11,720 is cloud's number, reproduced here. Probe 2's identity is B148's, re-derived in new
coordinates and credited. The "why there is one bit" reading is interpretive and labelled as such:
it explains banked results, it does not prove them. Neither probe touches a measured value.
