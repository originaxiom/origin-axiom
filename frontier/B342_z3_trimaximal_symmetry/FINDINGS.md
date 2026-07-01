# B342 — the ℤ/3 *is* the trimaximal symmetry (abstract group theory + the honest data comparison)

**Status: banked (frontier) as abstract `[MATH]` + an honest data observation. The physical (lepton-flavor) reading is
`[LEAP]`, firewalled to `speculations/S048`. Nothing to `CLAIMS.md`.** Chat-2 pushed the CP-redirect to a lepton-mixing
(TBM/TM2) reading. This probe banks **only** what is verifiable and firewall-safe: the standard group theory, plus the
one comparison Chat-2 didn't run.

## The verified group theory (standard — Harrison–Perkins–Scott / textbook)
1. **ℤ/3 → democratic mixing.** The cyclic-ℤ/3 DFT matrix `F[j,k] = ω^{jk}/√3` has `|F[j,k]|² = 1/3` everywhere.
2. **The magic column.** `(1,1,1)/√3` is the ℤ/3-**invariant** eigenvector (trivial rep) and equals **TBM's middle
   column**.
3. **The TM2 correlation.** Preserving the middle column (TM2) forces `|U_e2|² = 1/3`, i.e.
   `sin²θ₁₂ = 1/(3cos²θ₁₃)` → `θ₁₂ = 35.7°` (at `θ₁₃ = 8.57°`). *(An identity of TM2, not a fit.)*

## The honest data comparison (the check that must accompany the claim)
Observed `θ₁₂ = 33.4°`. **TM2 → 35.7° (off 2.3°); TM1 → 34.3° (off 0.9°).** **Current data favours TM1 over TM2.** So the
object's *would-be* pattern — TM2, selected by its ℤ/3 preserving the middle/magic column — is **falsifiable and currently
disfavoured**. Chat-2 reported TM2's ~2° agreement without running TM1; the honest state is that TM1 fits ~1° better.

## Verdict (firewall held)
The object's geometric ℤ/3 *is* the trimaximal (magic) symmetry — a **math fact**, and a standard one. **IF** one
identified it with the physical lepton flavor symmetry (an unforced `[LEAP]`, firewalled to S048), it would select **TM2**
— which **current data disfavours** vs TM1. This is *symmetry, not magnitude*: no continuous mixing angle is derived or
fitted here (that would be numerology, the two-lines rule). B322 already null-tested the PMNS angles → chance. Nothing to
`CLAIMS.md`.

## The fence
Exact linear algebra of the ℤ/3 DFT + the TM1/TM2 correlation identities (numpy). `θ₁₃`, `θ₁₂` are used **only** in the
correlation/comparison, never derived. No physics claim. Nothing to `CLAIMS.md`.

`z3_trimaximal_symmetry.py` (pyenv) · `tests/test_b342_z3_trimaximal_symmetry.py`. Firewalled reading:
`../../speculations/S048_lepton_mixing_symmetry.md`. Related: **B324/B335** (the object's ℤ/3, degenerate/phase),
**B285/B318** (the CP-sign ℤ/2), **B322** (PMNS null test), **B330/K020** (the CP sign is a Galois orbit, `±` not forced).
Lit: Harrison–Perkins–Scott (TBM); TM1/TM2 trimaximal mixing (standard flavor phenomenology).
