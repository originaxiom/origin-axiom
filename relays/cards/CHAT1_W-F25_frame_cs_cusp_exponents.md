# Card W-F25: frame C's cusp exponents, a read-out with no τ and no measure

**Seat:** the web seat (chat1). **Opened:** 2026-11-15, under the author's ruling of that morning (frame C's outputs may
be computed and printed; no data, no comparison). **Kind:** `result:` (data-free) and a proposal. **Not blind:** it is
designed after W-F24's output (b58678161) was read, and after the big run's negative was seen (status file).

## Why

W-F24 found the following:
- At a fixed point of order 5, every sector ratio of frame C falls exponentially with Im τ, at slopes between about 1.3
  and 5.2 per unit of height.
- The fibre average and the arithmetic form of the mean lose at most a factor of about 3.
- So the read-out on the whole is, in effect, the frame at the measure's typical height. **The measure is the choice of
  τ in another form.**

If log F ≈ A − πE·Im τ at large height, the exponents E are the frame's own hierarchy, with no τ and no measure. They
are read where both letters' fixed points lie: L fixes ∞ and R fixes 0, one cusp class.

## The proposal

The read-out is the vector of cusp exponents E_k = −lim (1/π) d log r_k / d Im τ, one per sector ratio and reading. The
hierarchy's one overall scale is then a single height. It is not fixed by the frame, and is typed as an open parameter.
What the frame then states without any parameter are the ratios E_k / E_l.

## Method

- **The frame:** W-F24's (this seat's transcription; the canonical end; Theorem 90's weight; L₂; S and S̃).
- **Where it is evaluated:** at all 24 points of order 5, at heights 2 to 10 in steps of 1, at Re τ = 0 and 0.25.
- **Also with the constant end**, L₂ = 0.9 − ½ log Im τ (B1924's), to see whether the exponents depend on the end.
- **The local slopes** are finite differences of log r over each unit step. A ratio below 1e-12 is unresolved in double
  precision (B1940) and is not used.

## Expectations (committed with this card, before any output at heights above 6 or at Re τ = 0.25 is computed)

- **Y1.** At the mark, for every sector ratio, the local slope converges: the last two resolved unit steps differ by less
  than 3 %.
- **Y2.** The limit does not depend on Re τ: Re τ = 0 and 0.25 agree to within 2 %.
- **Y3.** It does not depend on the end: the canonical and the constant end agree to within 2 %.
- **Y4.** At the mark, each limit E_k is within 2 % of a rational with denominator at most 50. This is a prediction from
  the order-5 characteristics; the denominator is a guess.
- **Reported:**
  - E_k at every point of order 5;
  - the fibre's mean exponent;
  - the scale-free ratios E_k / E_l at the mark, with no comparison with anything measured.
- **Plant:** a synthetic ratio exp(−π·(7/5)·Im τ) × (1 + 0.3 e^(−Im τ)) run through the same slope estimator gives 7/5
  within 1 % and is identified as 7/5 by the rational search.
