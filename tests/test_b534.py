"""Locks for B534 — the Dark Hyperbola (exact, zero floats in decisive tests).

Theta-lift seam: W1 = diag(zeta^{n(n-1)/2}), W2 = F W1^-1 F^-1, Par: n -> -n.
p*T(j,l) = sum_{n,k} zeta^{E},  E = j*n(n-1)/2 - l*k(k-1)/2 + 2nk  (mod p).
T = 0 <=> the count vector of E is constant (group-ring kernel).
"""

import numpy as np
import sympy as sp
import pytest


def count_vector(p, j, l):
    n = np.arange(p)
    Tn = (n * (n - 1) // 2) % p
    E = (j * Tn[:, None] - l * Tn[None, :] + 2 * np.outer(n, n)) % p
    return np.bincount(E.ravel(), minlength=p).astype(np.int64)


def is_dark(p, j, l):
    c = count_vector(p, j, l)
    return bool(np.all(c == c[0]))


def abs_sq(p, j, l):
    """|p*T|^2 when rational, else None."""
    c = count_vector(p, j, l)
    ac = [int(np.dot(c, np.roll(c, -d))) for d in range(p)]
    off = ac[1:]
    if all(v == off[0] for v in off):
        return ac[0] - off[0]
    return None


# ── Theorem 1: the dark hyperbola ──

@pytest.mark.parametrize("p", [3, 5, 7, 11, 13])
def test_dark_hyperbola_exact(p):
    """dark set == {jl = -4 mod p} \\ {(2, p-2)}, exactly."""
    dark = {(j, l) for j in range(p) for l in range(p) if is_dark(p, j, l)}
    claim = {(j, l) for j in range(p) for l in range(p)
             if (j * l) % p == (-4) % p and not (j == 2 and l == p - 2)}
    assert dark == claim
    assert len(dark) == p - 2


@pytest.mark.parametrize("p", [5, 7, 11, 13])
def test_survivor_magnitude(p):
    """|p*T(2, p-2)|^2 = p^3, i.e. |T| = sqrt(p), exactly."""
    assert abs_sq(p, 2, p - 2) == p**3


def test_active_magnitude_one():
    """At p=7, every active non-survivor point has |p*T|^2 = p^2 (|T| = 1)."""
    p = 7
    for j in range(p):
        for l in range(p):
            if is_dark(p, j, l) or (j, l) == (2, p - 2):
                continue
            assert abs_sq(p, j, l) == p * p, (j, l)


# ── Theorem 2: power-set magnitudes ──

def test_powerset_exact_15():
    """N=15 exact over Z[zeta_15]: |T|^2 in {0,1,3,5,15}, all 225 points."""
    N = 15
    x = sp.Symbol('x')
    phi15 = sp.Poly(sp.cyclotomic_poly(15, x), x)
    n = np.arange(N)
    Tn = (n * (n - 1) // 2) % N
    mags = set()
    for j in range(N):
        for l in range(N):
            E = (j * Tn[:, None] - l * Tn[None, :] + 2 * np.outer(n, n)) % N
            c = np.bincount(E.ravel(), minlength=N)
            ac = [int(np.dot(c, np.roll(c, -d))) for d in range(N)]
            poly = sp.Poly([ac[(-e) % N] for e in range(N - 1, -1, -1)], x)
            red = poly.rem(phi15)
            assert red.degree() <= 0, f"non-rational |T|^2 at {(j, l)}"
            r = int(red.as_expr()) if red.degree() == 0 else 0
            assert r % (N * N) == 0
            mags.add(r // (N * N))
    assert mags == {0, 1, 3, 5, 15}


# ── Theorem 3: asymptotic darkness ──

def test_darkness_crossing_31():
    prod = 1.0
    crossing = None
    for p in sp.primerange(3, 100):
        prod *= 1 - (p - 2) / p**2
        if crossing is None and prod < 0.5:
            crossing = p
    assert crossing == 31


# ── Theorem 4: the tower torsion law ──

def test_tower_det_law():
    """det(A1^n - I) = 2 - L(2n), n = 1..12."""
    A1 = sp.Matrix([[2, 1], [1, 1]])
    for n in range(1, 13):
        assert (A1**n - sp.eye(2)).det() == 2 - sp.lucas(2 * n)


def test_lucas_identities_symbolic():
    """L(2n) = L(n)^2 - 2(-1)^n and L(n)^2 - 5F(n)^2 = 4(-1)^n in Z[x,y]."""
    x, y = sp.symbols('x y')
    assert sp.expand((x + y)**2 - 2 * x * y - (x**2 + y**2)) == 0
    assert sp.expand((x + y)**2 - 5 * (x - y)**2 / 5 - 4 * x * y) == 0


def test_odd_even_split():
    """odd n: L(2n)-2 = L(n)^2; even n: L(2n)-2 = 5 F(n)^2, n = 1..12."""
    for n in range(1, 13):
        if n % 2 == 1:
            assert sp.lucas(2 * n) - 2 == sp.lucas(n)**2
        else:
            assert sp.lucas(2 * n) - 2 == 5 * sp.fibonacci(n)**2


def test_h1_seam_level_exact():
    """Smith(A1^4 - I) = diag(3, 15): H1 torsion of b++(RL)^4 = Z/3 + Z/15."""
    from sympy.matrices.normalforms import smith_normal_form
    A1 = sp.Matrix([[2, 1], [1, 1]])
    S = smith_normal_form(A1**4 - sp.eye(2))
    assert (abs(S[0, 0]), abs(S[1, 1])) == (3, 15)
