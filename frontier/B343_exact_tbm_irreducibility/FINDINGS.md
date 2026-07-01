# B343 — the object forces *exact TBM* (θ₁₃=0), not TM2; irreducibility is the one reason for every silence

**Status: banked (frontier). Verify-don't-trust on the Chat-2 handoff (2026-07-01) — its three-step self-correction,
verified at the landing. Corrects B342/S048's "would-be TM2" reading. Firewalled; nothing to `CLAIMS.md`.** Chat-2
retracted its own TM2 claim twice (CC's data catch → "TM2 disfavoured"; then "did I identify the right symmetry?" →
this), and landed on a cleaner, verified statement.

## The correction chain (all verified here)
1. **The neutrino residual symmetry is the object's own 2-torsion Klein group.** The `(ℤ/4)²` congruence torsion (B326)
   has 2-torsion `{(0,0),(0,2),(2,0),(2,2)}` = the **Klein four-group `ℤ₂×ℤ₂`** — structurally TBM's neutrino residual
   symmetry.
2. **The deck ℤ/3 acts on it irreducibly.** `Φ₃ = x²+x+1` reduced **mod 2** is irreducible over `𝔽₂`; the deck **3-cycles**
   the three nonzero Klein elements `{(1,0)→(0,1)→(1,1)→(1,0)}` and **fixes none**.
3. **The charged-lepton ℤ/3 doesn't select a column either.** `T = diag(1,ω,ω²)` does **not** normalise the neutrino
   Klein `{1,S,U,SU}` (`T S T⁻¹ ∉` it). *(B342 read the charged-lepton ℤ/3 as if it fixed a neutrino column — a conflation
   of the two sectors; corrected.)*
4. **TM1 vs TM2 needs selecting one `ℤ₂`; the ℤ/3 cycles all three → selects none → the full Klein survives → exact
   TBM.** Full unbroken Klein residual ⇒ `U = U_TBM` exactly: **`θ₁₃ = 0`**, `sin²θ₁₂ = 1/3`. And `θ₁₃ = 0` is
   **experimentally excluded** (observed `8.57°`).

## Verdict — the TM2 claim retracted; the same wall, reached from flavor
The object forces **exact TBM** (the symmetric point, `θ₁₃=0`), **not TM1 and not TM2**. The **TM2 selection is
retracted** (it was a double under-specification: charged-lepton-vs-neutrino sector + never computing the residual
symmetry). So the object is *not* betting on the disfavoured column — it bets on the symmetric limit and **hands the
entire TBM-breaking (θ₁₃'s size *and* its direction) to the world.** This is the program's familiar wall — *symmetry the
object's, deviation external* — now reached from the flavor side.

## The unification (the genuinely new content)
**One arithmetic property explains every silence:** the deck ℤ/3 acts **irreducibly** — `Φ₃` irreducible **mod 2** (on the
Klein group) and **mod 4** (on the full torsion, B326). That single irreducibility is why the object is
- **mass-blind** (can't order the light generations, B326/B335),
- **split-blind** (`n₁=n₂`, can't split them, B327/B329),
- **direction-blind** (can't select a TBM-breaking direction, here).

Irreducibility is the arithmetic form of "symmetric, therefore magnitude- and direction-blind."

## Surviving falsifiable content (firewalled)
`[LEAP]` (the identification object-torsion-Klein = neutrino flavor symmetry is unforced): **lepton mixing is
TBM-structured** — large, near-TBM — which is **observed** (leptons mix large, unlike the near-diagonal quarks); the
deviation `θ₁₃` (size and direction) is **external**. Symmetry: predicted and correct. Deviation: external.

## The firewall (held)
Exact group theory (the Klein 2-torsion, the irreducible ℤ/3, `T` not normalising the neutrino Klein, exact-TBM from full
Klein). No continuous value derived or fitted. The physical identification is `[LEAP]` (S048); nothing to `CLAIMS.md`.

## The fence
sympy (`Φ₃` mod 2 irreducibility, the deck 3-cycle, `T`–`S` commutator) + numpy (`U_TBM`). No physics values. Nothing to
`CLAIMS.md`.

`exact_tbm_irreducibility.py` (pyenv) · `tests/test_b343_exact_tbm_irreducibility.py`. Corrects: **B342** (the TM2
reading) and **`speculations/S048`** (updated). Related: **B326** (the `(ℤ/4)²` torsion, `Φ₃` irreducible), **B327/B329**
(`n₁=n₂`), **B335** (mass-blind by isometry), **B330/K020** (Galois symmetrization). Lit: Harrison–Perkins–Scott (TBM);
the TBM Klein group `ℤ₂×ℤ₂` and TM1/TM2 residual-symmetry breaking (standard flavor theory).
