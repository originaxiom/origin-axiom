# PREREG — B8070: does the anomaly layer break the rank obstruction?

**Sealed before the compute is read.** Reproducer `anomaly_rank_descent.py`. This is L144's
never-run retry, narrowed to the one question that is decidable today.

## The obstruction, as the corpus states it

`docs/GUT_REQUIREMENTS_LEDGER.md` §D, verbatim:

> "**The centralizer of a set of semisimple elements contains a maximal torus, hence has full
> rank.** The measurement cascade computes centralizers of charges (torus elements). **Therefore
> every measurement in the cascade is rank-preserving, and no number of them can ever reach
> rank 4.**" … "this is **a theorem, not an estimate**."

E₆ has rank 6. The cascade lands on `su(3)⊕su(2)⊕u(1)³` — rank `2+1+3 = 6`. The SM has rank
`2+1+1 = 4`. Every crossing failure is attributed to this.

## The claim under test

**The theorem is about centralizers. Anomaly cancellation is not a centralizer.** It is a system
of linear equations on the abelian charge space, and linear equations can drop rank. B864 already
computed the equations — `grav = 5b+15c`, `[SU(3)]² = 2c`, `[SU(2)]² = 2c`, forcing `b = c = 0` —
but B864 never states what that does to the **rank**, and no arc has connected it to §D.

**The question:** does anomaly consistency carry `su(3)⊕su(2)⊕u(1)³` (rank 6) to
`su(3)⊕su(2)⊕u(1)_Y` (rank 4), and does the result carry the SM's detector signature
**(dim 12, Killing rank 11)** that every previous sweep failed to find?

## Declared outcomes — all live, no preferred result

| result | reading |
|---|---|
| abelian sector `3 → 1`, total rank **6 → 4**, signature **(12, 11)** | the rank obstruction is **escaped**, and the escape class is named: anomaly constraints are not centralizers. §D stands as stated *about centralizers* and is **too narrow as a bar on the programme**. The GUT ledger needs a row rewritten. |
| abelian sector `3 → 1` but signature **≠ (12,11)** | rank drops, but the algebra is not the SM's. Report the algebra found, name it, claim nothing further. |
| anomaly does **not** force `b = c = 0` under my own independent rebuild | B864 is wrong or I have mis-transcribed it. Stop, report the discrepancy, fix before anything else. |
| rank does **not** drop | §D survives contact with the anomaly layer, B167's door-map gets its first citation, and L144 closes negative. |

## Controls, which run before any result is read

1. **The §D theorem is verified TRUE on its own class**, not assumed. Compute centralizers of
   semisimple elements in the cascade and confirm they are rank-preserving. *If the theorem fails
   my own test, my test is wrong.* An escape only means something if the wall is real.
2. **The detector is validated on the known SM** — `su(3)⊕su(2)⊕u(1)` built explicitly must read
   (12, 11) before it is pointed at anything.
3. **`b = c = 0` is re-derived from scratch**, not imported from B864's `results.json`.
4. **False-positive control:** a deliberately wrong charge assignment must *fail* to give (12,11).
   If every assignment gives the SM signature, the detector is measuring nothing.
5. **Killing rank is computed from the Killing form's actual matrix rank**, not inferred from
   "abelian directions don't count".

## What this CANNOT establish, stated in advance

- **Not the generation number.** B864 §4: *"Nothing about values, generations, the real form, or
  spacetime."* Three generations is **not** tested here and must not be implied.
- **Not the re-anchoring.** Over the full 27 nothing is anomalous; anomaly alone does not force
  keeping the chiral core. That is G2 and it is open.
- **Not a real form.** B715 excludes every real form of E₆ (adjoint trace non-real). The result
  here is over the complex algebra unless explicitly shown otherwise.
- **No scale, no value, no GeV.** The scale-torsor theorem (B666 cellS) is terminal and is not
  being re-opened. This lane is `w = 0` only — ranks, dimensions, quantized charges.

## Banned (THE_RULE, carried forward)

"X is impossible" with no class · a type named from a dimension alone · "exhaustive" applied to a
sample · a negative before the detector has found the thing elsewhere · any claim of physical
identification (Gate 5).

**Required:** the class covered · what lies outside it · the control and where it appears · what
would falsify the conclusion.
