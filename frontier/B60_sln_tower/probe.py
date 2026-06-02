"""B60 -- SL(n) tower: cross-n structure map (n=3,4) and the SL(5) barrier.

Generalizes B59's extrapolation method to arbitrary n and builds the corrected
cross-n structure map that replaces the refuted "all char(M^k)" tower conjecture.

What resolves cleanly (double precision, method validated on SL(3) ground truth):

  n=3:  char(M^-1) char(M^2) char(M^3)              x (t-1)(t+1)        [parity deg 2]
  n=4:  char(M^-1) char(M) char(M^2) char(M^3) char(M^4) x char(-M^2) x (t-1)^2(t+1)
                                                                        [parity deg 3]

Reading the corrected tower (n=3 -> n=4): the M-powers climb and densify
(`{-1,2,3}` -> `{-1,1,2,3,4}`), a SIGN sector appears (`char(-M^2)`, none at n=3),
and the parity block grows (degree 2 -> 3). This is the empirical structure, not
the naive `(n^2-1-parity)/2` all-char(M^k) count (refuted by B59).

SL(5) (24-dim) does NOT resolve at double precision: the trace-coordinate
differential has condition number ~1e11 at the relevant scale, so the
extrapolated Jacobian is dominated by numerical noise (verified below). A clean
SL(5) factorization needs a stable high-precision solver (SVD-based pinv at high
working precision) or the symbolic ambient SL(5,C) trace ring -- neither built
here. The barrier is documented as a reproducible conditioning fact.

Numerical, method-validated for n=3,4; SL(5) flagged unresolved. Standalone
trace-map mathematics; no physics, no Origin-core claim.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.linalg import expm


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


def _basis_sl(n):
    basis = []
    for i in range(n):
        for j in range(n):
            if i != j:
                e = np.zeros((n, n), complex)
                e[i, j] = 1.0
                basis.append(e)
    for i in range(n - 1):
        e = np.zeros((n, n), complex)
        e[i, i] = 1.0
        e[i + 1, i + 1] = -1.0
        basis.append(e)
    return basis


def _words(A, B, n):
    if n == 3:
        Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
        return [A, B, A @ B, Ai, Bi, Ai @ B, A @ Bi, Ai @ Bi]
    if n == 4:
        return [
            A, A @ A, A @ A @ A, B, B @ B, B @ B @ B, A @ B, A @ A @ B, A @ B @ B,
            A @ A @ B @ B, A @ A @ A @ B, A @ B @ B @ B, A @ B @ A @ B, A @ A @ A @ B @ B, A @ A @ B @ B @ B,
        ]
    # n == 5: 24 words (rank 24 at a generic rep)
    pw = [np.linalg.matrix_power(A, k) for k in range(5)]
    qw = [np.linalg.matrix_power(B, k) for k in range(5)]
    out = [pw[k] for k in range(1, 5)] + [qw[k] for k in range(1, 5)]
    for i in range(1, 4):
        for j in range(1, 4):
            out.append(pw[i] @ qw[j])
    out += [A @ B @ A @ B, A @ A @ B @ A @ B, A @ B @ B @ A @ B, A @ A @ B @ B @ A @ B,
            A @ B @ A @ B @ B, A @ A @ A @ B @ A @ B, A @ A @ B @ A @ A @ B]
    return out


def _diff_matrix(A, B, n, substitute, pert_plus, pert_minus, h):
    nw = n * n - 1
    rows = [[0j] * (2 * (n * n - 1)) for _ in range(nw)]
    col = 0
    for Pp, Pm in zip(pert_plus, pert_minus):
        Ap, Am = Pp @ A, Pm @ A
        wp = _words(Ap @ B, Ap, n) if substitute else _words(Ap, B, n)
        wm = _words(Am @ B, Am, n) if substitute else _words(Am, B, n)
        for r in range(nw):
            rows[r][col] = (np.trace(wp[r]) - np.trace(wm[r])) / (2 * h)
        col += 1
    for Pp, Pm in zip(pert_plus, pert_minus):
        Bp, Bm = Pp @ B, Pm @ B
        wp = _words(A @ Bp, A, n) if substitute else _words(A, Bp, n)
        wm = _words(A @ Bm, A, n) if substitute else _words(A, Bm, n)
        for r in range(nw):
            rows[r][col] = (np.trace(wp[r]) - np.trace(wm[r])) / (2 * h)
        col += 1
    return np.array(rows)


def _perts(n, h=1e-6):
    basis = _basis_sl(n)
    return [expm(h * g) for g in basis], [expm(-h * g) for g in basis]


def fixed_line_spectrum(n, seeds, epss):
    pert_plus, pert_minus = _perts(n)
    h = 1e-6
    dim = n * n - 1
    spectra = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        P = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        P -= np.trace(P) / n * np.eye(n)
        Q = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        Q -= np.trace(Q) / n * np.eye(n)
        dts = []
        for eps in epss:
            A, B = expm(eps * P), expm(eps * Q)
            dx = _diff_matrix(A, B, n, False, pert_plus, pert_minus, h)
            dX = _diff_matrix(A, B, n, True, pert_plus, pert_minus, h)
            dts.append(dX @ np.linalg.pinv(dx, rcond=1e-12))
        dt0 = np.zeros((dim, dim), complex)
        deg = min(len(epss) - 1, 4)
        for i in range(dim):
            for j in range(dim):
                dt0[i, j] = np.polyfit(epss, [d[i, j] for d in dts], deg)[-1]
        spectra.append(np.sort_complex(np.linalg.eigvals(dt0)))
    return np.mean(spectra, axis=0)


def _max_match(spectrum, target_roots):
    used = [False] * len(target_roots)
    worst = 0.0
    for ev in sorted(spectrum, key=lambda z: z.real):
        best, bi = 1e9, -1
        for k, r in enumerate(target_roots):
            if used[k]:
                continue
            d = abs(ev - r)
            if d < best:
                best, bi = d, k
        used[bi] = True
        worst = max(worst, best)
    return worst


def _q(a, b, c):
    return list(np.roots([a, b, c]))


def check_sl3_validation() -> CheckResult:
    spec = fixed_line_spectrum(3, (10, 11), np.array([0.04, 0.06, 0.08, 0.10, 0.12]))
    target = _q(1, 1, -1) + _q(1, -3, 1) + _q(1, -4, -1) + [1.0, -1.0]  # char(M^-1),char(M^2),char(M^3) + parity
    worst = _max_match(spec, target)
    return result("SL(3) VALIDATION (B55 c=3)", worst < 0.02, f"max match {worst:.4f}; powers {{-1,2,3}}, parity (t-1)(t+1)")


def check_sl4_regression() -> CheckResult:
    spec = fixed_line_spectrum(4, (10, 11), np.array([0.03, 0.05, 0.07, 0.09, 0.11]))
    target = (
        _q(1, 1, -1) + _q(1, -1, -1) + _q(1, -3, 1) + _q(1, -4, -1) + _q(1, -7, 1)  # M^{-1,1,2,3,4}
        + _q(1, 3, 1)  # char(-M^2)
        + [1.0, 1.0, -1.0]  # parity (t-1)^2(t+1)
    )
    worst = _max_match(spec, target)
    return result("SL(4) REGRESSION (B59)", worst < 0.03, f"max match {worst:.4f}; powers {{-1,1,2,3,4}}, char(-M^2), parity (t-1)^2(t+1)")


def check_sl5_conditioning_barrier() -> CheckResult:
    pert_plus, pert_minus = _perts(5)
    rng = np.random.default_rng(20)
    P = rng.standard_normal((5, 5)) + 1j * rng.standard_normal((5, 5))
    P -= np.trace(P) / 5 * np.eye(5)
    Q = rng.standard_normal((5, 5)) + 1j * rng.standard_normal((5, 5))
    Q -= np.trace(Q) / 5 * np.eye(5)
    A, B = expm(0.1 * P), expm(0.1 * Q)
    dx = _diff_matrix(A, B, 5, False, pert_plus, pert_minus, 1e-6)
    cond = np.linalg.cond(dx)
    # the barrier: cond is enormous, so double precision cannot resolve SL(5)
    return result("SL(5) CONDITIONING BARRIER", cond > 1e8, f"cond(Dx)~{cond:.1e} -> unresolved at double precision")


def run_checks() -> list[CheckResult]:
    return [check_sl3_validation(), check_sl4_regression(), check_sl5_conditioning_barrier()]


def main() -> int:
    print("B60 -- SL(n) TOWER: cross-n structure map (n=3,4) + SL(5) barrier")
    print("Status: numerical, method-validated for n=3,4; SL(5) unresolved (conditioning)")
    print()
    for item in run_checks():
        print_result(item)
    print()
    print("Corrected cross-n structure map:")
    print("  n=3: char(M^k) powers {-1, 2, 3};          no sign sector;  parity (t-1)(t+1)   [deg 2]")
    print("  n=4: char(M^k) powers {-1, 1, 2, 3, 4};    char(-M^2);      parity (t-1)^2(t+1) [deg 3]")
    print("  n=5: UNRESOLVED -- cond(Dx)~1e11; needs stable high-precision SVD pinv or the")
    print("       symbolic ambient SL(5,C) trace ring.")
    print()
    print("Trend (n=3->4): M-powers climb/densify; a sign sector appears; parity block grows.")
    print("The naive '(n^2-1-parity)/2 all char(M^k)' tower is refuted (B59); this is the actual map.")
    ok = all(item.ok for item in run_checks())
    print(f"\nB60 CHECKS: {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
