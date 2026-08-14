#!/usr/bin/env python3
"""B852 -- the pressure function, hyperbolic vs parabolic.

NOT PREREGISTERED. These numerics were run exploratorily in scratch BEFORE the write-up, and
the arc says so rather than authoring a seal after the fact. Its footing is the EXACT POSITIVE
CONTROL below (the doubling map has a closed-form pressure), not a commitment nobody made.

The claim to DEMONSTRATE (not assert): a uniformly hyperbolic system has real-analytic pressure
and therefore CANNOT exhibit a phase transition. B451 computed the transfer operator of a
HORSESHOE. So its instrument was structurally incapable of finding the thing the reframe needs,
and "no transition found" was guaranteed by the choice of model, not by the object.

Method: transfer operator  (L_s f)(x) = sum_i |psi_i'(x)|^s f(psi_i(x))  over inverse branches,
discretised by Chebyshev collocation; P(s) = log(leading eigenvalue).

POSITIVE CONTROL: the doubling map has P(s) = (1-s) log 2 EXACTLY. If the discretisation does not
reproduce that closed form, no number below means anything.
"""
import numpy as np


def cheb_nodes(n, a=0.0, b=1.0):
    k = np.arange(n)
    x = np.cos(np.pi * (2 * k + 1) / (2 * n))          # Chebyshev-Gauss on [-1,1]
    return a + (b - a) * (x + 1) / 2


def collocation_matrix(branches, s, n, a=0.0, b=1.0):
    """Matrix of L_s in the Lagrange basis on Chebyshev nodes.

    (L_s f)(x_j) = sum_i w_i(x_j) f(psi_i(x_j)), and f(psi_i(x_j)) is obtained by barycentric
    interpolation from the nodal values -- so the operator becomes a dense matrix.
    """
    x = cheb_nodes(n, a, b)
    # barycentric weights for Chebyshev-Gauss nodes
    k = np.arange(n)
    bw = (-1.0) ** k * np.sin(np.pi * (2 * k + 1) / (2 * n))

    def interp_row(y):
        d = y - x
        exact = np.isclose(d, 0, atol=1e-14)
        row = np.zeros(n)
        if exact.any():
            row[np.argmax(exact)] = 1.0
            return row
        w = bw / d
        return w / w.sum()

    M = np.zeros((n, n))
    for j, xj in enumerate(x):
        for psi, dpsi in branches:
            y = psi(xj)
            if not (a - 1e-12 <= y <= b + 1e-12):
                continue
            M[j] += abs(dpsi(xj)) ** s * interp_row(y)
    return M


def pressure(branches, s, n=48, a=0.0, b=1.0):
    M = collocation_matrix(branches, s, n, a, b)
    ev = np.linalg.eigvals(M)
    lead = max(ev.real[np.abs(ev.imag) < 1e-8], default=None)
    if lead is None or lead <= 0:
        lead = np.max(np.abs(ev))
    return float(np.log(lead))


# ---------------------------------------------------------------------------
# Model 1 -- UNIFORMLY HYPERBOLIC (the B451 class). Exact answer known.
# doubling map T(x) = 2x mod 1;  psi_0 = x/2, psi_1 = (x+1)/2, |psi'| = 1/2
# ---------------------------------------------------------------------------
DOUBLING = [(lambda x: x / 2, lambda x: 0.5),
            (lambda x: (x + 1) / 2, lambda x: 0.5)]

# ---------------------------------------------------------------------------
# Model 2 -- PARABOLIC (the cusp class). Farey map: indifferent fixed point at 0.
# psi_0(x) = x/(1+x), psi_1(x) = 1/(1+x); both |psi'| = 1/(1+x)^2
# ---------------------------------------------------------------------------
FAREY = [(lambda x: x / (1 + x), lambda x: 1.0 / (1 + x) ** 2),
         (lambda x: 1 / (1 + x), lambda x: 1.0 / (1 + x) ** 2)]



# ---------------------------------------------------------------------------
# Model 3 -- the CONTROL THAT ISOLATES THE PARABOLIC POINT.
# The Gauss map is the Farey map's jump transformation: the SAME continued-fraction
# dynamics with the indifferent fixed point induced away. It is not a free choice of
# control -- it differs from Farey in exactly the feature under test.
# psi_n(x) = 1/(n+x),  |psi_n'| = 1/(n+x)^2
# ---------------------------------------------------------------------------
def gauss_branches(N=120):
    return [((lambda n: (lambda x: 1.0 / (n + x)))(n),
             (lambda n: (lambda x: 1.0 / (n + x) ** 2))(n)) for n in range(1, N + 1)]


def has_plateau(branches, ss=(1.0, 1.2, 1.5), n=48, tol=1e-2):
    """A phase transition shows as P == 0 on a RANGE, not at a point."""
    return all(abs(pressure(branches, s, n=n)) < tol for s in ss)


def second_difference(f, s, h=1e-3):
    return (f(s + h) - 2 * f(s) + f(s - h)) / h ** 2


if __name__ == "__main__":
    print("=" * 74)
    print("POSITIVE CONTROL -- doubling map, exact P(s) = (1-s) log 2")
    print("=" * 74)
    worst = 0.0
    for s in [0.2, 0.5, 0.8, 1.0, 1.5, 2.0]:
        got = pressure(DOUBLING, s, n=32)
        exact = (1 - s) * np.log(2)
        worst = max(worst, abs(got - exact))
        print(f"  s={s:4}  P={got:+.12f}  exact={exact:+.12f}  err={abs(got-exact):.2e}")
    print(f"  worst error: {worst:.2e}  -> control {'PASSES' if worst < 1e-9 else 'FAILS'}")

    print()
    print("=" * 74)
    print("MODEL 1 (uniformly hyperbolic): is P analytic?  second difference should be ~0")
    print("=" * 74)
    for s in [0.6, 0.9, 1.0, 1.1, 1.4]:
        d2 = second_difference(lambda t: pressure(DOUBLING, t, n=32), s)
        print(f"  s={s:4}  P''~{d2:+.3e}   P={pressure(DOUBLING, s, n=32):+.9f}")

    print()
    print("=" * 74)
    print("MODEL 2 (parabolic / Farey): looking for a PLATEAU at P=0")
    print("=" * 74)
    for n in (32, 48, 64):
        row = []
        for s in [0.2, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.5]:
            row.append((s, pressure(FAREY, s, n=n)))
        print(f"  n={n}: " + "  ".join(f"s={s}:{p:+.5f}" for s, p in row))
