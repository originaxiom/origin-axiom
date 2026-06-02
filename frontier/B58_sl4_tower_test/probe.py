"""B58 -- SL(4) factor-count tower test (attempt; verdict NEEDS-EXPERTISE).

This probe attempts to test the SL(n) factor-count tower prediction recorded in
PC12's DRAFT_NOTE_SKELETON: at the identity representation, the rank-two SL(4,C)
Jacobian should factor into a parity block plus 7 degree-2 char(M^k) factors
(degree 15). It does NOT resolve the prediction. It establishes two things
rigorously and records the precise obstruction.

What is confirmed:
  (1) The SL(4) forward-chain Cayley-Hamilton recursion
        tau_k = e1 tau_{k-1} - e2 tau_{k-2} + e3 tau_{k-3} - tau_{k-4}
      at the identity representation (e1=4, e2=6, e3=4) has characteristic
      polynomial (r-1)^4. Hence the fixed-line derivative sequences are CUBIC in
      k -- the natural step up from SL(3)'s (r-1)^3 / quadratic (B55). The
      derivative-polynomial degree is n-1.
  (2) The fixed-line point (all traces = n) is the IDENTITY representation,
      where the representation->trace map is first-order degenerate (d tr(W) = 0,
      since tr of an sl(n) tangent vector is 0); the trace functions are
      second-order there. Demonstrated numerically.

Consequence (the obstruction): a representation-based numerical Jacobian cannot
recover the ambient fixed-line trace-map Jacobian (the object that factors as
char(M^k) for SL(3), B54/B55), because every representation realizing the
fixed-line point is the degenerate identity. The B55-style ambient construction
requires the explicit SL(4,C) 15-trace-coordinate generating set (Procesi /
second fundamental theorem for SL(4) invariants) AND the substitution's action on
all 15 coordinates via the SL(4) trace identities. That construction is NOT built
here.

Verdict: NEEDS-EXPERTISE. The 7-factor tower prediction is UNTESTED -- neither
confirmed nor refuted. No claim is promoted; the prediction stays recorded as a
prediction in PC12. No physics, no framing.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import sympy as sp


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def result(name: str, ok: bool, detail: str = "") -> CheckResult:
    return CheckResult(name=name, ok=ok, detail=detail)


def print_result(item: CheckResult) -> None:
    status = "OK" if item.ok else "FAIL"
    suffix = f" -- {item.detail}" if item.detail else ""
    print(f"{item.name}: {status}{suffix}")


def check_identity_recursion() -> CheckResult:
    """SL(4) identity-representation forward recursion has characteristic (r-1)^4."""
    r = sp.symbols("r")
    e1, e2, e3 = 4, 6, 4  # elementary symmetric of eigenvalues all = 1
    charpoly = r**4 - e1 * r**3 + e2 * r**2 - e3 * r + 1
    ok = sp.factor(charpoly) == (r - 1) ** 4
    return result("SL(4) IDENTITY RECURSION = (r-1)^4", ok, "e1=4,e2=6,e3=4; quadruple root")


def check_cubic_derivative_sequences() -> CheckResult:
    """Quadruple root => the recursion annihilates cubics (derivative seqs are cubic in k)."""
    k, a, b, c, d = sp.symbols("k a b c d")
    p = a + b * k + c * k**2 + d * k**3
    # recursion residual: p_k - 4 p_{k-1} + 6 p_{k-2} - 4 p_{k-3} + p_{k-4}
    residual = (
        p
        - 4 * p.subs(k, k - 1)
        + 6 * p.subs(k, k - 2)
        - 4 * p.subs(k, k - 3)
        + p.subs(k, k - 4)
    )
    ok = sp.expand(residual) == 0
    return result("CUBIC DERIVATIVE SEQUENCES (degree n-1)", ok, "fourth difference of a cubic vanishes")


def check_identity_degeneracy(seed: int = 0, eps: float = 1e-6) -> CheckResult:
    """At the identity rep, tr(word) is first-order stationary (so reps cannot probe the fixed line)."""
    rng = np.random.default_rng(seed)

    def rand_sln(n: int = 4) -> np.ndarray:
        m = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        return m - np.trace(m) / n * np.eye(n)  # traceless => sl(n)

    x, y = rand_sln(), rand_sln()

    def word(A: np.ndarray, B: np.ndarray) -> np.ndarray:
        return A @ A @ B @ A @ np.linalg.inv(B)  # a representative mixed word

    def tr_at(t: float) -> complex:
        A = np.eye(4) + t * x
        B = np.eye(4) + t * y
        return np.trace(word(A, B))

    first = abs((tr_at(eps) - tr_at(-eps)) / (2 * eps))
    second = abs((tr_at(eps) - 2 * tr_at(0) + tr_at(-eps)) / eps**2)
    ok = first < 1e-3 and second > 1.0
    return result(
        "IDENTITY-REP DEGENERACY (traces 2nd-order)",
        ok,
        f"d/de tr(W)~{first:.1e} (~0), d2/de2 tr(W)~{second:.3g} (nonzero)",
    )


def run_checks() -> list[CheckResult]:
    return [
        check_identity_recursion(),
        check_cubic_derivative_sequences(),
        check_identity_degeneracy(),
    ]


def main() -> int:
    print("B58 -- SL(4) FACTOR-COUNT TOWER TEST (attempt)")
    print("Status: NEEDS-EXPERTISE -- mechanism confirmed; 7-factor prediction UNTESTED")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print("Confirmed: SL(4) identity recursion (r-1)^4, cubic derivative sequences;")
    print("           fixed-line point is the degenerate identity representation.")
    print("Obstruction: the ambient 15-coordinate SL(4,C) trace map (Procesi generators +")
    print("             substitution action) is required and is NOT built here.")
    print(f"B58 MECHANISM CHECKS: {'OK' if ok else 'FAIL'}  (prediction verdict: NEEDS-EXPERTISE)")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
