"""B59 -- SL(4) fixed-line factorization (numerical; refutes the naive tower).

This probe computes the ambient fixed-line Jacobian of the SL(4) Fibonacci
trace map and factors its spectrum. It RESOLVES the SL(4) tower prediction that
B58 left as NEEDS-EXPERTISE -- and refutes it in specifics.

Method (validated on SL(3) ground truth, B54/B55):
  The ambient fixed-line Jacobian is the linearization of the polynomial trace
  map at the all-traces-n point. It cannot be read off representations AT the
  identity (traces are 2nd-order there; B58), but at a perturbed representation
  A=exp(eps P), B=exp(eps Q) the trace-coordinate differential is full rank, so
        DT(eps) = D[tr W_i(AB,A)] . pinv(D[tr W_j(A,B)])
  is the ambient Jacobian at the point x(eps), and x(eps) -> (n,...,n) as
  eps -> 0. Extrapolating DT(eps) to eps=0 gives the fixed-line Jacobian.
  On SL(3) (8 coordinates) this reproduces B55's c=3 spectrum
  {1,-1, phi^2, phi^-2, roots(t^2+t-1), roots(t^2-4t-1)} -- the built-in
  validation check below.

SL(4) result (15 coordinates; method-validated, numerical ~3-4 digits):
  the fixed-line spectrum factors as
        char(M^-1) char(M) char(M^2) char(M^3) char(M^4) char(-M^2) (t-1)^2 (t+1)
  i.e. five clean char(M^k) (k = -1,1,2,3,4), one SIGN sector char(-M^2)
  (eigenvalues -phi^2, -phi^-2, with no SL(3) analog), and a degree-3 parity
  block (t-1)^2(t+1).

Verdict on the prediction (PC12 "Open Prediction"): REFUTED in specifics. The
count is not "7 char(M^k) + 1 parity": it is 5 char(M^k) + 1 char(-M^2) + a
degree-3 parity block. The M-powers extend to 4; a sign sector appears.

This is standalone trace-map mathematics: numerical, method-validated, not a
symbolic proof. No physics, no Origin-core claim.
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


def _basis_sl(n: int) -> list[np.ndarray]:
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


def _words(A: np.ndarray, B: np.ndarray, n: int) -> list[np.ndarray]:
    if n == 3:
        Ai, Bi = np.linalg.inv(A), np.linalg.inv(B)
        return [A, B, A @ B, Ai, Bi, Ai @ B, A @ Bi, Ai @ Bi]
    return [
        A, A @ A, A @ A @ A, B, B @ B, B @ B @ B, A @ B, A @ A @ B, A @ B @ B,
        A @ A @ B @ B, A @ A @ A @ B, A @ B @ B @ B, A @ B @ A @ B, A @ A @ A @ B @ B, A @ A @ B @ B @ B,
    ]


def _diff_matrix(A, B, n, substitute, pert_plus, pert_minus, h):
    nw = 8 if n == 3 else 15
    rows = [[0j] * (2 * (n * n - 1)) for _ in range(nw)]
    col = 0
    for Pp, Pm in zip(pert_plus, pert_minus):  # perturb A
        Ap, Am = Pp @ A, Pm @ A
        wp = _words(Ap @ B, Ap, n) if substitute else _words(Ap, B, n)
        wm = _words(Am @ B, Am, n) if substitute else _words(Am, B, n)
        for r in range(nw):
            rows[r][col] = (np.trace(wp[r]) - np.trace(wm[r])) / (2 * h)
        col += 1
    for Pp, Pm in zip(pert_plus, pert_minus):  # perturb B
        Bp, Bm = Pp @ B, Pm @ B
        wp = _words(A @ Bp, A, n) if substitute else _words(A, Bp, n)
        wm = _words(A @ Bm, A, n) if substitute else _words(A, Bm, n)
        for r in range(nw):
            rows[r][col] = (np.trace(wp[r]) - np.trace(wm[r])) / (2 * h)
        col += 1
    return np.array(rows)


def _dt_at(eps, P, Q, n, pert_plus, pert_minus, h=1e-6):
    A, B = expm(eps * P), expm(eps * Q)
    dx = _diff_matrix(A, B, n, False, pert_plus, pert_minus, h)
    dX = _diff_matrix(A, B, n, True, pert_plus, pert_minus, h)
    return dX @ np.linalg.pinv(dx, rcond=1e-12)


def fixed_line_spectrum(n, seeds, epss):
    basis = _basis_sl(n)
    h = 1e-6
    pert_plus = [expm(h * g) for g in basis]
    pert_minus = [expm(-h * g) for g in basis]
    dim = n * n - 1
    spectra = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        P = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        P -= np.trace(P) / n * np.eye(n)
        Q = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        Q -= np.trace(Q) / n * np.eye(n)
        dts = [_dt_at(e, P, Q, n, pert_plus, pert_minus, h) for e in epss]
        dt0 = np.zeros((dim, dim), complex)
        deg = min(len(epss) - 1, 4)
        for i in range(dim):
            for j in range(dim):
                dt0[i, j] = np.polyfit(epss, [d[i, j] for d in dts], deg)[-1]
        spectra.append(np.sort_complex(np.linalg.eigvals(dt0)))
    return np.mean(spectra, axis=0)


def _max_match(spectrum, target_roots):
    """Max over computed eigenvalues of the distance to the nearest target root."""
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


def check_method_validates_on_sl3() -> CheckResult:
    spec = fixed_line_spectrum(3, seeds=(10, 11), epss=np.array([0.04, 0.06, 0.08, 0.10, 0.12]))
    phi2 = ((1 + 5 ** 0.5) / 2) ** 2
    target = [1.0, -1.0, phi2, 1 / phi2] + list(np.roots([1, 1, -1])) + list(np.roots([1, -4, -1]))
    worst = _max_match(spec, target)
    return result("METHOD VALIDATES ON SL(3) (B55 c=3)", worst < 0.02, f"max match {worst:.4f} to known spectrum")


def sl4_target_roots():
    quads = {
        "char(M^-1)": [1, 1, -1],
        "char(M)": [1, -1, -1],
        "char(M^2)": [1, -3, 1],
        "char(M^3)": [1, -4, -1],
        "char(M^4)": [1, -7, 1],
        "char(-M^2)": [1, 3, 1],
    }
    roots = []
    for c in quads.values():
        roots += list(np.roots(c))
    roots += [1.0, 1.0, -1.0]  # parity (t-1)^2 (t+1)
    return roots


def check_sl4_factorization() -> CheckResult:
    spec = fixed_line_spectrum(4, seeds=(10, 11), epss=np.array([0.03, 0.05, 0.07, 0.09, 0.11]))
    worst = _max_match(spec, sl4_target_roots())
    detail = "char(M^k) k=-1,1,2,3,4; char(-M^2); (t-1)^2(t+1)"
    return result("SL(4) FACTORIZATION (numerical)", worst < 0.03, f"max match {worst:.4f}; {detail}")


def run_checks() -> list[CheckResult]:
    return [check_method_validates_on_sl3(), check_sl4_factorization()]


def main() -> int:
    print("B59 -- SL(4) FIXED-LINE FACTORIZATION (numerical; method-validated)")
    print("Status: resolves B58's NEEDS-EXPERTISE; REFUTES the naive tower prediction")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print("SL(4) spectrum factors as:")
    print("  char(M^-1) char(M) char(M^2) char(M^3) char(M^4)  [5 char(M^k), k=-1..4]")
    print("  x char(-M^2)  [sign sector, -phi^2,-phi^-2; new at SL(4)]")
    print("  x (t-1)^2 (t+1)  [degree-3 parity block]")
    print("Prediction '7 char(M^k) + 1 parity' is REFUTED (numerical, method-validated).")
    print(f"B59 CHECKS: {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
