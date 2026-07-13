# B564 — the SL(3) φ-fixed locus is entirely reducible (probation P2, LIVE)

Probation probe P2 (B562) resolved the **S031a full-locus** question at SL(3):
does the φ-fixed locus contain any irreducible representation? **No — it is entirely
reducible.** This confirms the B141 Item-4 conjecture and extends B142's principal-only
(Klein-4) result to the full locus. Adversarially verified (the probe's scripts were
independently reran and reproduced, including a caught solver-noise trap); the
discriminating factor is re-checked here (`tests/test_b564_sl3_reducible.py`).
Firewall-clean. (LIVE disposition — full theorem-promotion runs the standard §5 gate;
this cell banks the computed result + the mechanism.)

## The computation (symbolic elimination, no Gröbner blow-up)

The φ-fixed system A g⁻¹A g = g A g⁻¹ (with B = g⁻¹A g) on the SL(3) character variety:

1. **Trace collapse.** sympy.solve on Lawton coordinates forces all 8 non-commutator
   traces equal, t₁ = … = t₈ = c — so the fixed-**character** locus is a **1-dimensional
   curve**, not the 0-dimensional set the prereg expected (correction noted).
2. **Finite-order pinning.** In A's eigenbasis (μ² ≠ 1) the trace conditions force
   diag(B) = diag(B⁻¹) = (c,0,0); the commutator trace t₉ = tr[A,B] is φ-fixed **only**
   when the factor
     (μ−1)³(μ+1)³(μ²+1)(μ²+μ+1) = 0,
   i.e. μ ∈ {1, −1, ±i, ω, ω²} — **A has finite order** (roots of unity, orders 1,2,4,3;
   verified in the lock). At those finite-order points every φ-fixed intertwiner is
   **block-diagonal 1⊕2 (reducible)** (101 solutions at μ=i, 219 at μ=−1, all
   off-block ≲ 5×10⁻⁹ = machine noise).
3. **No irreducibles elsewhere.** generic μ (2, e^{0.9i}), μ = ω, and the unipotent c=3
   stratum yield **no φ-fixed representation at all**. (The μ=ω case-4 numerator root is
   spurious — c = 1+μ+1/μ = 0 there, degenerating the parametrization.)
4. **Trap caught.** An 8-trace-matching matrix looked irreducible (algebra dim 9) but t₉
   was unfixed (φ swaps the two commutator roots) and the numeric rank-9 was
   error-inflation — the true B is block-diagonal.

## Verdict

**The SL(3) φ-fixed locus is entirely reducible — no irreducible representation
anywhere.** The mechanism is clean: φ-fixedness pins A to **finite order**, and a
finite-order A forces the intertwiner B to split. This confirms B141 Item-4 and
extends B142 (principal Klein-4) to the full locus. Open continuation (registered): the
same elimination at SL(n≥4), and the standard §5 promotion gate for theorem status.
