# B449 — the forcing boundary: the disc×disc adjudication, and the seam level as a conductor law

**Status: banked (frontier). Firewalled; nothing to `CLAIMS.md`. Adjudicates the 2026-07-07
forcing-chain handoffs (Chat-2 + Chat-1 concurrence) and runs their requested decisive check —
in its corrected form. Verdict: the disc×disc "generalization" is category-confused (retrofit
confirmed structurally, not probabilistically); the fig-8's ℚ(√−15) is RESTORED to forced status
(the banked B424 two-ended compositum); the genuine choice-boundary is exactly the banked L57.**

## What the handoffs asked

Chat-2 located a forcing boundary: the chain `word → abelianization → φ² → mapping torus → 4₁ →
hyperbolic structure → character variety → ℚ(√−3)` is canonical (each step a named construction
or Mostow), but "the seam field ℚ(√−15) = disc(trace)×disc(Alexander)" (−3 × 5 = −15) is
probably a small-number retrofit, with the sign structure breaking on controls (5₂: −23×−7 = +161
real; 6₁: 27). The requested falsification: *does 5₂'s actual seam sit at level 161?*

## The adjudication (exact, one screen)

1. **The requested test cannot run — and that IS the answer.** `Alexander(5₂) = 2t²−3t+2` has
   leading coefficient 2: **5₂ is not fibered.** No fibration ⇒ no monodromy ⇒ no dynamics end ⇒
   the formula's second factor names *nothing* for 5₂. Same for 6₁ (leading 2). "Level 161" is
   not a failed prediction; it is a non-sequitur. The sign-inconsistency Chat-2 caught is the
   symptom of this category confusion.
2. **Why the fig-8 works: its "Alexander disc" is secretly the dynamics disc.** For a fibered
   knot, Alexander = the char poly of the homological monodromy — verified exactly:
   `Alexander(4₁) = t²−3t+1 = charpoly([[2,1],[1,1]])`, disc 5 = the golden/dynamics field. So
   `disc(trace)×disc(Alexander)` for the fig-8 is really **disc(geometry) × disc(dynamics)** —
   the banked two-ended structure.
3. **Therefore ℚ(√−15) is NOT a coincidence — it is the banked B424 forcing, in-family.** The
   seam field is the compositum of the object's two ends; the seam **level 15 = the conductor of
   ℚ(√−3,√5)** (lcm of conductors 3 and 5). Chat-2 over-corrected: the retrofit is the
   *Alexander-polynomial phrasing*, not the fact.
4. **The in-family conductor law (the honest generalization), two points + a coherence witness:**
   - **golden (m=1):** geometry ℚ(√−3) (cond 3) × dynamics ℚ(√5) (cond 5) → compositum conductor
     **15** = the seam level ✓ (B424).
   - **silver (m=2):** geometry ℚ(i) (cond 4, B316 RRLL) × dynamics ℚ(√2) (charpoly t²−6t+1,
     disc 32; cond 8) → compositum **ℚ(ζ₈), conductor 8**. **Independent witness: B448's silver
     orbit gate — run the previous day for a different purpose — output `z⁴+16` → ℚ(ζ₈)**: the
     silver dynamics itself produced the conductor-8 field.
   - **bronze (m=3), the registered falsifiable prediction:** dynamics ℚ(√13) (charpoly
     t²−11t+1, disc 117 = 9·13; cond 13); geometry field of the R³L³ bundle ∈ {ℚ(√−3), ℚ(i)}
     (the B316 amphichiral floor) ⇒ predicted seam level **∈ {39, 52}**, decided by computing
     that bundle's invariant trace field. Registered, not run (the next cheap decisive test).
5. **The located boundary = the banked L57.** With the seam FIELD restored to forced, the genuine
   choice-candidates are exactly the representation/pairing/theta-characteristic — the program's
   already-named frontier (P62/C6: "forced within the named premise; the premise stays named").
   Both seats' "most important structural fact located this session" re-derives L57 from outside.
   Good convergence; nothing moved.

## Chat-1 residue items (third re-flag where needed)

- "SL(3)/D(3,3,4) survived every control" — adjudicated (B444/B445): *distinguished, not a
  fingerprint*; inherited from SL(2) arithmeticity.
- "The E₆ Hessian gives mass ratios" — **third re-flag: the cup product is banked ZERO**
  (B352 dps-100; B370 to third order). The named "mass matrix" vanishes identically.
- Kashaev/L-function probes — banked/queued (B419/B420; arg ≡ 0 vacuous; ratio-matching
  B322-dead). "Stop philosophizing, start computing" — concurred; the thermodynamic campaign is
  exactly that, with the falsifiability machinery the probes were missing.
- The forcing-chain positive (canonical through ℚ(√−3)) — agreed and now extended: canonical
  through the seam FIELD in-family; Chat-1's caveat stands ("which functor" is ours) and is
  recorded on the Concept Atlas laws card.

## Reproduce

```
python3 conductor_law.py    # the exact checks: fiberedness, Alexander=charpoly, conductors
pytest ../../tests/test_b449.py
```
