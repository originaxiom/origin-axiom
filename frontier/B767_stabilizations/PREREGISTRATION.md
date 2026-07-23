# PREREG — R28-10: the depth-closure backlog (6 stabilizations)

cc3, 2026-07-23. Branch `hunt/r28-10-stabilizations`.
Gate 5-Q binding; nothing to CLAIMS.

## The 6 cells (B500 = R28-6, separate)

| cell | kill_form | gap | stabilization path |
|---|---|---|---|
| B489 | absence-at-depth-n | n=1..8; claim universal | Binet induction: N=2n, c=1 structural; torsion=(phi^n-phi^{-n})^2>0 |
| B685 | kind-mismatch | pointwise to n=60/order 20 | extend computation + structural denominator argument |
| TOMB-L255 | value-mismatch | n=2..13; sketch not proof | functoriality theorem: Sym^d is a functor, eigenvalue formula all d |
| TOMB-L310 | genericity | L<=10; 5-point inference | extend to L11+ or analytic recursion on level sizes |
| TOMB-L34 | genericity | one N, two seeds | extend to multiple Fibonacci lengths and seeds |
| WALL-7 | zero-intertwiner | twisted f3 3 points only | interpolation: degree-bound + enough sample points = proof |

## Method

Each cell gets an independent stabilization attempt. Three possible verdicts:

- **STABILIZED**: the gap is closed by a symbolic/inductive proof valid for all n/d/L.
  The kill is no longer underproved.
- **EXTENDED**: computation pushed beyond the original bound, pattern holds, but
  all-n proof not achieved. The kill is better-evidenced, not fully closed.
- **RESIDUAL**: neither fully stabilized nor meaningfully extended.
  The gap remains as identified in P3.

## Per-cell design

### B489 (Binet induction)
1. Prove N=2n: the layered triangulation of b++(RL)^n has one tet per monodromy
   letter (structural from the SnapPy once-punctured-torus-bundle construction).
2. Prove c=1: mapping torus of once-punctured torus always has 1 cusp (topological).
3. Prove DGG rank = N-c = 2n-1 for all n (from 1+2).
4. Prove |torsion| = L(2n)-2 = (phi^n - phi^{-n})^2 > 0 for all n>=1,
   and > 1 for all n>=2 (Binet formula, exact).
5. Verify inductively: extend SnapPy check from n=8 to n=16.

### TOMB-L255 (functoriality theorem)
1. State: Sym^d is a polynomial functor; Sym^d(AB) = Sym^d(A)Sym^d(B) for all d.
   Verify symbolically for d=1..12 (extending from d=1..6).
2. State: Sym^d(diag(lam,mu)) = diag(lam^{d-j}mu^j). Verify symbolically for d=1..12.
3. Conclude: for M with eigenvalues phi, -1/phi, every Sym^d(M) eigenvalue
   is (-1)^j phi^{d-2j}, lying in <-1,phi> (free rank 1), for ALL d.
4. Therefore multiplicative rank = 1, additive rank = 2, for all n.
   The spectral rank never climbs. QED.

### WALL-7 (interpolation argument)
1. Straight (d5) is already closed (proved for all t in the recompute).
2. Twisted (f3): extend from 3 sample points to 30+ points in K = Q(sqrt-3).
3. Degree bound: exp(t*e_pr) is polynomial of degree <= 26 in t (e_pr nilpotent).
   C27(t) rational of bounded degree. The determinant of the linear system is a
   polynomial/rational in t of bounded degree D.
4. If dim=0 at D+1 distinct t values, then dim=0 for all but finitely many t.
   Check the finitely many potential exceptions.

### B685 (denominator extension)
1. Extend the Habiro series computation beyond order 20 to order 40+.
2. Verify v3-only denominators hold at each extended order.
3. Note the structural argument: the trace field Q(omega) ramifies only at 3,
   so 5 cannot appear in denominators of invariants computed over Q(omega).
4. Verdict depends on whether the structural argument is formalizable.

### TOMB-L310 (depth extension)
1. Rebuild the Omega DAG from the banked CSV data (B159's node/edge files).
2. Extend the Myrheim-Meyer drift computation if computationally feasible.
3. Alternatively: fit the drift deceleration and bound the limit.

### TOMB-L34 (multi-size extension)
1. Extend to additional Fibonacci chain sizes: N=233, 377, 610, 987, 1597, 2584.
2. Multiple seeds at each N.
3. Check log-class plateau stability across N.

## Seal

sha256 of this file computed after writing, recorded outside the sealed file
per the named-algorithm convention.
