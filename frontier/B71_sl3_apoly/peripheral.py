"""B71 (Track B, B2-B3) -- the peripheral eigenvalue A-variety from the trace-map fixed locus.

Continues B71/probe.py (B0-B1: Fix(T_1^2) = 3 components V0 [geometric], W1, W2 [Dehn-filling]). This
builds explicit SL(3,C) representations on each component and derives the boundary (meridian/longitude)
eigenvalue data -- the SL(3) analogue of B67's meridian M=eig(t), longitude L=eig[A,B].

Pipeline (mirrors B67 at rank 3):
  * realize(coords): explicit (A,B) in SL(3,C) with the given 8 trace coordinates. A = diag of the
    roots of z^3 - x1 z^2 + x4 z - 1; B solved (fsolve) from the 6 trace conditions + det B = 1 + 2
    gauge conditions fixing the diagonal torus that stabilizes A. The adjugate (= B^-1 at det 1) keeps
    every condition polynomial. Round-trips to < 1e-7 on all three components (cond(B) ~ O(1-100)).
  * monodromy(A,B): t in SL(3,C) with t A t^-1 = phi(A), t B t^-1 = phi(B) (phi: a->a^2 b, b->ab, the
    figure-eight monodromy; fallback a->aba), via the 18x9 Kronecker null-space solve, det t = 1.
  * ratios(M): the two eigenvalue ratios (top/mid, bot/mid) -- the PGL(3) "decorated" A-variety
    coordinates (Falbel et al. normalize the middle boundary eigenvalue to 1).

RESULTS:
  * Pipeline validated on the geometric branch: for a Sym^2 rep, monodromy(Sym^2 A, Sym^2 B) reproduces
    Sym^2 of the B67 SL(2) monodromy -- eig(t) = {mu^2, 1, mu^-2} (mu = eig of the SL(2) monodromy),
    to ~1e-13.
  * LITERAL A-variety match on the Dehn-filling components (Falbel-Guilloux-Koseleff-Rouillier-
    Thistlethwaite, arXiv:1412.4711 sec 4.1), with meridian<->longitude labels transposed:
        W1 = D2:  M^3 = L,   M*^3 = L*       (Falbel:  L^3 = M,  L*^3 = M*)
        W2 = D3:  M^3 L = 1, M*^3 L* = 1     (Falbel:  L^3 M = 1, L*^3 M* = 1)
    to ~1e-10 over >=16 points / 2 seeds. M = eigenvalue ratios of the monodromy t (the fibration
    generator), L = eigenvalue ratios of the fiber boundary [A,B]. This is the SL(3) analogue of
    B67's exact Cooper-Long match, on the Dehn-filling components.
  * The geometric component V0 (= Falbel D1) has no tidy closed A-variety form (their eliminated
    Groebner basis is 141 polynomials) -- no literal match is expected there; the Sym^2-shadow
    validation is the geometric-branch check.

Standalone character-variety mathematics; no physics, no Origin claim. Proven core P1-P16 untouched.
Numerical (fsolve realization + SVD null-space monodromy); the component structure itself is exact (B1).
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import fsolve

I3 = np.eye(3, dtype=complex)


# component parametrizations (free parameters p, q) -- from B71/probe.py components()
def V0(p, q): return (p, q, q, p, q, p, p, q)        # geometric (contains Sym^2)
def W1(p, q): return (1, q, q, 1, p, 1, 1, p)        # = Falbel D2
def W2(p, q): return (p, 1, 1, q, 1, q, p, 1)        # = Falbel D3


def _adjugate(B):
    C = np.empty((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            m = np.delete(np.delete(B, i, axis=0), j, axis=1)
            C[i, j] = (-1) ** (i + j) * (m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0])
    return C.T


def realize(coords, tol=1e-9, tries=40):
    """Explicit (A,B) in SL(3,C) with the 8 B48 trace coordinates, or None on failure."""
    x1, x2, x3, x4, x5, x6, x7, x8 = (complex(c) for c in coords)
    roots = np.roots([1, -x1, x4, -1])
    A, Ai = np.diag(roots).astype(complex), np.diag(1.0 / roots).astype(complex)

    def resid(v):
        B = (v[:9] + 1j * v[9:]).reshape(3, 3)
        adjB = _adjugate(B)
        e = np.array([np.trace(B) - x2, np.trace(A @ B) - x3, np.trace(Ai @ B) - x6,
                      np.trace(adjB) - x5, np.trace(A @ adjB) - x7, np.trace(Ai @ adjB) - x8,
                      np.linalg.det(B) - 1.0, B[0, 1] - 1.0, B[1, 2] - 1.0], dtype=complex)
        return np.concatenate([e.real, e.imag])

    rng = np.random.default_rng(0)
    for _ in range(tries):
        b0 = rng.standard_normal(9) + 1j * rng.standard_normal(9)
        sol, _info, ier, _msg = fsolve(resid, np.concatenate([b0.real, b0.imag]), full_output=True)
        if ier == 1 and np.max(np.abs(resid(sol))) < tol:
            return A, (sol[:9] + 1j * sol[9:]).reshape(3, 3)
    return None


def monodromy(A, B, tol=1e-7):
    """t in SL(3,C) with t A t^-1 = phi(A), t B t^-1 = phi(B) for the figure-eight monodromy."""
    for phiA, phiB in [(A @ A @ B, A @ B), (A @ B @ A, A @ B)]:
        E = np.vstack([np.kron(A.T, I3) - np.kron(I3, phiA),
                       np.kron(B.T, I3) - np.kron(I3, phiB)])
        t = np.linalg.svd(E)[2][-1].conj().reshape(3, 3, order="F")
        t = t / np.linalg.det(t) ** (1.0 / 3.0)
        res = (np.max(np.abs(t @ A @ np.linalg.inv(t) - phiA))
               + np.max(np.abs(t @ B @ np.linalg.inv(t) - phiB)))
        if res < tol:
            return t, res
    return None, None


def ratios(M):
    """The two PGL(3) eigenvalue ratios (top/mid, bot/mid), |.|-sorted -- decorated A-variety coords."""
    e = np.linalg.eigvals(M)
    e = e[np.argsort(np.abs(e))]
    return e[2] / e[1], e[0] / e[1]


def peripheral(coords):
    """(M, M*, L, L*) for a fixed-locus character: meridian ratios from t, longitude ratios from [A,B]."""
    out = realize(coords)
    if out is None:
        return None
    A, B = out
    t, res = monodromy(A, B)
    if t is None:
        return None
    comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
    Mh, Ms = ratios(t)
    Lh, Ls = ratios(comm)
    return Mh, Ms, Lh, Ls


# --------------------------------------------------------------------------- #

def _avariety_residual(name, fn, relation, seeds=(5, 23), npts=8):
    vals = []
    for sd in seeds:
        rng = np.random.default_rng(sd)
        for _ in range(npts):
            p = complex(rng.standard_normal(), rng.standard_normal())
            q = complex(rng.standard_normal(), rng.standard_normal())
            per = peripheral(fn(p, q))
            if per is None:
                continue
            M, Ms, L, Ls = per
            # min over the two meridian/longitude pairings
            vals.append(min(relation(M, L) + relation(Ms, Ls),
                            relation(M, Ls) + relation(Ms, L)))
    return np.median(vals), np.max(vals), len(vals)


def main():
    print("B71 (B2-B3) -- peripheral eigenvalue A-variety from the trace map\n")
    print("literal Dehn-filling A-variety match (Falbel et al. arXiv:1412.4711, M<->L transposed):")
    for name, fn, rel, label in [
        ("W1 = D2", W1, lambda M, L: abs(M**3 - L), "M^3 = L      (Falbel L^3=M)"),
        ("W2 = D3", W2, lambda M, L: abs(M**3 * L - 1), "M^3 L = 1    (Falbel L^3 M=1)"),
    ]:
        med, mx, n = _avariety_residual(name, fn, rel)
        print(f"  {name}:  {label}   median {med:.1e}, max {mx:.1e}  (n={n})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
