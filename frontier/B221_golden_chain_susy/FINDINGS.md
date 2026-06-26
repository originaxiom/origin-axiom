# B221 — the golden chain's emergent CFT is SUPERSYMMETRIC: the exact anchor (c=7/10 = the first N=1 SCFT)

**Date:** 2026-06-26. **Status:** the thing that was hiding in plain sight, made exact. B220 reproduced the
golden (Fibonacci-anyon) chain CFT as `c=7/10` and I called it "a dimensionless number." It is the **tricritical
Ising model `M(4,5)` = the first member of the N=1 *superconformal* minimal series** — so the object's
**multiplicity** (golden, the unique anyon-realizable mean, B218) produces, by interaction alone, an **emergent
supersymmetric** theory. This file proves the identity by exact arithmetic and records two further glossed facts.
Firewall: dimensionless CFT / rep-theory only — a 2d *superconformal* symmetry of the emergent critical chain,
**not** a scale or spacetime SUSY (see `speculations/S040`). **Nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger
**V224**.

## (1) `c = 7/10` by three exact, agreeing derivations — the SUSY identity

```
  GKO coset   M(4,5) = (SU(2)₂ × SU(2)₁)/SU(2)₃ :   c₂ + c₁ − c₃ = 3/2 + 1 − 9/5 = 7/10
  Virasoro minimal model M(4,5):                    c(p=4) = 1 − 6/(4·5)     = 7/10
  N=1 SUPERCONFORMAL minimal series (m=3):          c = (3/2)(1 − 8/(3·5))   = 7/10   ← the SUSY identity
```

All three are exact `Fraction` equalities. The third is the decisive one: `c=7/10` is the `m=3` member of the
N=1 superconformal series `c=(3/2)(1−8/(m(m+2)))` (Friedan–Qiu–Shenker), i.e. the **lowest unitary
superconformal minimal model**. And the coset denominator `SU(2)₃` is exactly the **Fibonacci/golden level** (the
golden anyon `τ` is the spin-1 primary of `SU(2)₃`, `d=φ`), so the golden anyon sits *inside* the construction of
its own emergent SUSY CFT.

## (2) The operator content — and where the supercurrent lives

The 6 tricritical-Ising primaries (Kac formula `h_{r,s}=((5r−4s)²−1)/80`):
```
  h ∈ {0, 1/10, 3/5, 3/2, 7/16, 3/80}
```
The **`h=3/2`** primary is the **supercurrent `G`** — the generator of the emergent SUSY. (B222/Act I hunts it in
the finite-size spectrum; its presence is *the* signature distinguishing "`c=7/10` CFT" from "`c=7/10`
superconformal".) The GKO coset reproduces these weights mod 1 (`{0,1/10,3/5,1/2,7/16,3/80}`) via the branching
`l∈{0,1,2}`, `l'∈{0,1,2,3}`, `ε=(l+l′) mod 2`, `h=h₂(l/2)+h₁(ε/2)−h₃(l'/2)` — the golden `SU(2)₃` structure
producing the TCI content.

## (3) The golden quantum dimension
`d₁(SU(2)₃) = sin(3π/5)/sin(π/5) = 2cos(π/5) = (1+√5)/2 = φ` (exact, sympy) — the same golden fingerprint that
B218's Jones-index selection singled out, now seen as the level whose coset *is* the SUSY CFT.

## (4) `content = multiplicity` — L39 and the multiplicity were never separate
For the metallic family `RᵐLᵐ = [[1+m², m],[m, 1]]`:
```
  content(RᵐLᵐ) = gcd(b, c, a−d) = m       and       RᵐLᵐ ≡ I (mod m)
```
So L39/B219's period-controlling **content is the multiplicity `m`** — the same invariant as B212's
congruence-trivialization modulus and B204's `gcd(a,b)`. (And `t−2 = det(γ−I) = |H₁|` of the closed bundle; the
golden object `m=1` has WRT period 5.) One invariant, four names across four findings.

## Honest status / tiers
- the SUSY identity `c=7/10` = coset = N=1 superconformal, the 6 primaries, the `φ` quantum dimension, and
  `content=m`: **all `[exact]`** (exact rational / exact symbolic; pytest-locked).
- the physics (golden chain → tricritical Ising / its emergent SUSY) is **classical** (Friedan–Qiu–Shenker;
  Feiguin et al. 2007; Huijse–Schoutens). Contribution = the in-sandbox identification + the `content=m`
  unification; **novelty UNCHECKED**.
- the *reading* "this is the object's SUSY / content from interaction with the outside" is firewalled to
  `speculations/S040` — **not** banked here.

## Reproduction
- `python coset_check.py` (pyenv) — the four exact blocks.
- `tests/test_b221_golden_chain_susy.py` — 5 exact locks.

## Net
The golden chain's emergent CFT is **the first N=1 superconformal minimal model** — multiplicity selects golden
(B218) and golden's interaction produces emergent **supersymmetry** (`c=7/10`), with the golden `SU(2)₃` level
sitting inside the coset that builds it. The supercurrent `h=3/2` is the Act-I (B222) target; the lattice/external
question is Act II (B223); the firewalled reading is `S040`. (`B218 → B220 → B221`; `content=m` ties `B204/B212/B219`.)
