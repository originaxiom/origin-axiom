# B261 — the golden-root AJ operator: two ends, one recursion

**Status: banked observation (frontier). FIREWALLED — quantum topology / arithmetic, NOT physics. Nothing to
`CLAIMS.md`.** The B260 next stone (the lead all three step-back readers converged on). `golden_root_aj.py`
(pyenv, mpmath + sympy).

## The setup
The Coulomb branch (A-polynomial) **quantizes** to the colored-Jones recursion: the quantized A-polynomial
annihilates `J_N` and its classical limit `q→1` *is* the A-polynomial (AJ conjecture, **proved for `4₁`**,
Garoufalidis). So the Coulomb branch is the *classical shadow* of the colored-Jones recursion (B260's through-line,
now substantiated by a theorem). This probe evaluates that recursion at the golden/E₈ root `q=e^{2πi/5}`.

## The result — the two ends are two *regimes* of one operator
| regime | limit | behavior | end |
|---|---|---|---|
| **Kashaev / volume** | `q=e^{2πi/N}`, `N→∞` *together* | `J_N` grows **exponentially**, `(2π/N)log\|J_N\| → Vol=2.0299` | **hyperbolic / E₆ / ℚ(√−3)** (B258) |
| **golden root** | `q=ζ₅=e^{2πi/5}` **fixed** | coefficients `Q=q^N` are **period-5**; recursion degenerates to finite; `J_N` **periodic** | **spherical / E₈ / ℚ(√5)** |

**Computed (golden root):** `[N]J_N(4₁;ζ₅) = {1,−2,−2,1,0 | −1,2,2,−1,0}` — **antiperiod 5** (`f(N+5)=−f(N)`),
period 10. Bounded and integral; extends B240's `{1,−2,−2,1}` to the full period. The exponential (volume) growth
is *gone* — the golden/E₈ end is the bounded/periodic regime. The period is exactly **5 = k+2 = det(4₁)** = the
E₈ "5" cascade, now appearing as the *period of the quantum recursion*.

## The classical side, same point
The Coulomb branch at the golden meridian `M²=ζ₅`: `u = 2cos(2π/5) = 1/φ = (√5−1)/2`, so
> `L + 1/L = u²−u−4 = −(2+√5) = −φ³ ∈ ℚ(√5)`.

The golden meridian root forces the **longitude into the golden field** — the Coulomb-branch avatar of the E₈ end,
exact (`φ³=2+√5` verified).

## Why this is the payoff
One AJ operator carries **both ends of the transition**: exponential (hyperbolic/E₆/Vol) at the Kashaev limit,
periodic (spherical/E₈/ℚ(√5)) at the golden root. The golden root is special because `5 = k+2 = det` makes the
recursion's period exactly 5 and lands the classical longitude in ℚ(√5). This is the **quantum realization of the
two-ended unification** (B258), now from the Coulomb-branch/AJ side (B260) — the deepest single-object statement of
the arc: geometry, arithmetic, quantum, and the Coulomb branch are four views of one recursion with two regimes.

It is *not* a step toward the SM (the recursion is a knot invariant; no gauge group, no scale) — it is the
two-ended structure made maximally concrete. The honest signal stands: the object resolves into its two ends on
every face, forced by the "5" and by Niven (B249).

Anchors: B240 (golden integrality, the `{1,−2,−2,1}` seed), B258 (the two ends / quantum mirror), B260 (Coulomb
branch + AJ through-line), B250 (Vol). Lit: Garoufalidis (AJ conjecture, `4₁`); Habiro (cyclotomic colored Jones);
Kashaev / Murakami (volume conjecture).
