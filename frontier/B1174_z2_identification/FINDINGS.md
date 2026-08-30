# B1174 — THE ℤ/2-IDENTIFICATION CELL (R50-3): not one torsor — ONE SHARED INVOLUTION. The literal four-way identification is refuted; the mirror = chirality = Gal(K/ℚ) is proved as the shared leg of both V₄'s

**Status: banked (frontier). Verdict NEGATIVE** (the hypothesis as posed — *the four program ℤ/2's are ONE
involution* — is refuted), with the **proved substance** carried as the productive content (the B1157
shape). This was the register's Q1 = B1169's S1, **double-discovered** (the sweep and the meditation found
it independently), and R50-3 by assignment. `verification/reproduce.sh` → `REPRODUCES` (exact cyclotomic +
SnapPy numeric). Gate 5 clean.

## The question and the four candidates

Are these one involution? **B942**'s chirality ℤ/2 (= the quotient Gal(K/ℚ), K=ℚ(√−3) — B942 computed c ∉
Gal(K^ab/K), c generates the quotient); **B957**'s value torsors (B700: structure group ℤ/2 over a
*quadratic character field* — ℚ(√5) in cell 1, ℚ(√−7) in cell 2); **B1168**'s mirror bit (the
orientation-parity law's odd side); **S068 row 1**'s genus-ℤ/2 of ℚ(√−15) vs the breath/orientation bit.

## PROVED — one shared involution, four names

**c = the mirror = chirality = Gal(K/ℚ)'s generator**, verified:
- **The mirror acts on traces as complex conjugation** (SnapPy: the reversed m004's holonomy traces are the
  conjugates, verified on a, b, ab) — so on the trace field K=ℚ(√−3)⊂ℂ the mirror IS c, the Galois
  generator. This welds **B1168's bit to B942's quotient**: one involution, theorem-grade.
- **c is a leg of BOTH V₄'s**, located exactly: in the **branch V₄** = Gal(ℚ(ζ₁₂)/ℚ), c = (z↦z¹¹): fixes
  √3, flips √−3 — *the orientation leg*; the K-fixing leg (z↦z⁷, flips √3) is **B1067's form-class swap** —
  so **B1164's census is grounded leg-by-leg** (bit 1 = c = orientation/chirality; bit 2 = the √3 swap).
  In the **meeting V₄** = Gal(ℚ(√−3,√5)/ℚ), c flips √−3 and fixes √5 — a leg again.

## REFUTED — the other ℤ/2's are provably different legs, each by an exact field action

- **B957's value torsor (cell 1)**: its swap is √5 ↦ −√5 — but **c is trivial on ℚ(√5)** (real field). The
  value swap is *not* c. **The mechanism is the parity law at the field level: c acts nontrivially on a
  quadratic field iff the field is IMAGINARY** — the real/metallic hearing ladder is mirror-even, so no
  hearing-side ℤ/2 can be the orientation. (Cell 2's ℚ(√−7) is imaginary — c does act there — but a shared
  action on one field is not a canonical torsor isomorphism; and B957's own verdict was already a category
  difference.)
- **S068 row 1's genus-ℤ/2 of ℚ(√−15)**: its generator must fix √−15, hence flips BOTH √−3 and √5 — while c
  flips only √−3 and *moves* √−15. **Distinct legs of the same meeting V₄; no canonical iso** — the row's
  own clean-negative condition fires, with the constructive residue (the genus bit is the c·(√5-swap)
  composite, not c).

**The one-line theorem: NOT ONE TORSOR — ONE SHARED INVOLUTION.** The program's ℤ/2's organize as two V₄'s
(branch/ζ₁₂ and meeting/√−3·√5) sharing exactly the c-leg; everything the observer's *orientation* touches
is the c-leg; the value/genus/form-class bits are the other legs, provably not c.

## Consequences (each routed)

- **B1169's S1 — PARTIALLY PROMOTED** (dated addendum in B1169): the chain *mirror = chirality = Gal(K/ℚ)*
  is now proved; S1's remaining gap is precisely the **QP-4 leg** (expressing the no-self-closure
  obstruction as a cohomology class and comparing it to c's class) — open, named.
- **B1166's C4 — constructively resolved**: cloud's "the three (ℤ/2)² presentations are one torsor" fails
  as stated (B1166's √3-vs-√5 candidate now a theorem-grade refutation) **but the right statement exists**:
  *the presentations share the c-leg*. Relayed to cloud (their C4 amendment) + codex (the B1024 frame-V₄
  leg now has a target: is the frame ⟨c,r⟩'s value-kernel θ=cr the k=5/k=7-type leg?).
- **B1161's bypass-door label — sharpened, still SUPPORTED-CONJECTURAL**: the W₀ marking (H↪ℂ) breaks the
  full branch V₄, and its **c-component is exactly the orientation bit** — the identification's c-half is
  now proved; the full identity still awaits the QP-4-class comparison.
- **S068 row 1 — closed** (clean negative with residue); row 2 (does the ℤ/2 act on a banked dynamical
  object — the mod-15 congruence shadow) stays open, unblocked by this cell.

## Fences

**A bug caught before banking** (narrated honestly): the first leg-(2) implementation used `subs` on a
non-Symbol expression, which silently misfired and printed a wrong V₄ table; caught by hand-checking the
k=11 row against z⁷ = −z arithmetic, re-implemented with exact reduction mod Φ₁₂ = z⁴−z²+1 and load-bearing
asserts. The MB12/vacuous-check class, self-caught in-cell. The SnapPy trace check is numeric (1e-9); the
conjugate-rep fact it witnesses is standard (orientation reversal conjugates holonomy). All Galois
arithmetic exact. No firewall crossing; Gate 5 clean (Galois actions on named surds; no measured value).
kill_graph routed (the literal hypothesis; hatch = the QP-4-class comparison + the ℚ(√−7) partial bridge).
