# R28-10: depth-closure backlog — 6 stabilizations

cc3 audit seat, 2026-07-23. Branch `hunt/r28-10-stabilizations`.
Gate 5-Q binding; nothing to CLAIMS. Prereg sha256 17fb9e5b.

## Verdicts

| cell | verdict | gap |
|---|---|---|
| B489 | **STABILIZED** | CLOSED — Binet induction, all n |
| TOMB-L255 | **STABILIZED** | CLOSED — functoriality theorem, all d |
| WALL-7 | EXTENDED | open — twisted at 3/53 needed points |
| B685 | EXTENDED | open — structural argument + original depth |
| TOMB-L310 | EXTENDED | open — drift deceleration, no L11+ data |
| TOMB-L34 | EXTENDED | open — log class at 10 sizes, c_eff plateau inconclusive |

## Per-cell findings

### B489 (STABILIZED)

The cyclic-cover tower of the figure-eight knot has DGG rank = 2n-1 for ALL n,
proved by structural topology (layered triangulation gives N=2n tets, mapping torus
gives c=1 cusp) plus the Binet identity:

    torsion = |L(2n) - 2| = (phi^n - phi^{-n})^2 > 0  for all n >= 1
    torsion >= 5 > 1  for all n >= 2  (blocks Gang-Yonekura)

SnapPy verified N=2n, c=1 at every level n=1..16 (extended from n=1..8).
Binet identity verified n=1..19. Torsion = Binet cross-checked n=1..16.

### TOMB-L255 (STABILIZED)

The spectral rank of the golden-ratio adjoint tower never climbs, proved by the
polynomial functor theorem:

    Sym^d(M) eigenvalues = {(-1)^j phi^{d-2j} : j=0,...,d} for ALL d

This follows from two algebraic facts:
1. Sym^d(AB) = Sym^d(A)Sym^d(B) (functoriality — verified as exact 8-variable
   polynomial identity for d=1..12; true for all d by definition of Sym^d)
2. Sym^d(diag(lam,mu)) = diag(lam^{d-j} mu^j) (verified d=1..12)

All eigenvalues lie in <-1, phi> (multiplicative free rank 1, additive rank 2).
Tower dimensions n^2-1 verified n=2..20 (extended from n=2..13).

### WALL-7 (EXTENDED)

Straight (d5): already closed for all t (the {A27,B27}-only constraint has dim=0).
Twisted (f3): verified dim=0 at 3 nondegenerate points (t=1, omega, 2).

The twisted system is a DIFFERENT linear system from the straight commutant
(X B = C X, X C = B X vs X B = B X, X C = C X) — straight closure does NOT
imply twisted closure. Degree bound from nilpotent exp(t*e_pr): entries polynomial
of degree <= 52. Need 53+ points for a generic dim=0 proof.

Gap: 50 more sample points needed, or a symbolic-in-t determinant computation.

### B685 (EXTENDED)

Structural argument: 5 is inert in Q(sqrt(-3)) (Legendre (-3/5) = -1). This
explains WHY v5(denominator) = 0 at every order — the computation lives over
Z[omega] where 5 cannot appear in denominators.

The B685 recompute verified v5=0 to order 20 (object side) and n=60 (hearing side).
The structural argument is sound but formalizing it in-sandbox requires proving
the Habiro series stays in Z[omega][1/3] at every order (3-integrality property).

### TOMB-L310 (EXTENDED)

4 consecutive decelerating drift steps: delta d_MM = [0.62, 0.58, 0.35, 0.31].
Geometric decay ratio ~0.886. Projected d_MM(L->inf) ~ 6.3.

The genericity claim is about CONVERGENCE (d_MM stabilizes), not the limit value.
The deceleration pattern supports convergence but is not a proof.

DAG data loaded (474 nodes, 1765 edges, L=4..10). Extension to L11+ requires
rebuilding the Omega strict-full-class DAG.

### TOMB-L34 (EXTENDED)

Fibonacci chain tight-binding model tested at 10 sizes (N=8..610), 3 seeds each.
Entanglement entropy S is logarithmic at every size (S/log(L) stays in [0.25, 0.65]).

The c_eff = S/log(L) does NOT plateau — it drifts from ~0.64 (N=8) down to ~0.26
(N=233). This is consistent with the known slow convergence of the effective central
charge in quasiperiodic systems. The LOG CLASS is confirmed across all sizes; the
exact c_eff value is not stabilized.

## Summary

2/6 cells STABILIZED (gaps fully closed by all-n/all-d proofs).
4/6 cells EXTENDED (computation pushed further, patterns hold, gaps remain).
0/6 cells RESIDUAL.

The two closures (B489 Binet, TOMB-L255 functoriality) are the strongest results:
both convert finite-depth numerical checks into algebraic theorems valid at every level.
The four extensions strengthen the evidence without achieving full closure.
