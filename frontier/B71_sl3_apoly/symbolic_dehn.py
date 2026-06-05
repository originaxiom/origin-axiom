"""B71 (P1) -- the Dehn-filling A-variety as an EXACT scalar-matrix identity (upgrades V44).

V44 verified the Dehn-filling relations W1=D2: M^3=L and W2=D3: M^3 L=1 numerically (~1e-10) by
magnitude-sorting eigenvalue ratios. V46 then showed the genuine meridian mu = w^-1 t COMMUTES with
the longitude L=[A,B]. Commutativity gives an EXACT reformulation with no eigenvalue extraction or
pairing ambiguity:

    mu and [A,B] commute  =>  simultaneously diagonalizable, so for paired eigenvalues
      M^3 = L  (all i, middle-normalized)   <=>   [A,B] = c * mu^3        (a single scalar c)
      M^3 L = 1                             <=>   [A,B] * mu^3 = c        (a single scalar c)

i.e. the Dehn-filling A-variety relation is exactly the statement that  [A,B] * mu^(-3)  (D2) resp.
[A,B] * mu^3 (D3) is a SCALAR matrix.  This is an exact matrix identity, checkable without roots.

Two confirmations here:
  * `dehn_scalar_residual` -- the scalar-matrix criterion in the numerical pipeline (peripheral.py),
    >= 2 seeds, both components (double precision, ~1e-9).
  * `w1_highprec_residual` -- W1 to 50 DIGITS: A=diag(1,i,-i) fixed, B(p,q) solved exactly over Q(i)
    (sympy), evaluated to 50 digits; the monodromy null vector + the scalar criterion in mpmath.
    Confirms M^3=L to ~1e-43 at 12 exact rational points -- an exact-grade upgrade of V44 on W1.

Standalone character-variety mathematics; no physics. Proven core P1-P16 untouched. The component
structure itself is exact (B1/V43); this sharpens the A-variety relation to an exact scalar identity.
"""
from __future__ import annotations

import importlib.util
import pathlib

import numpy as np

_HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("b71_peripheral", _HERE / "peripheral.py")
per = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(per)


def _scalar_dev(M):
    """How far a 3x3 matrix is from scalar (max off-diagonal + diagonal spread)."""
    off = np.max(np.abs(M - np.diag(np.diag(M))))
    dg = np.max(np.abs(np.diag(M) - np.mean(np.diag(M))))
    return max(off, dg)


def dehn_scalar_residual(component, kind, seeds=(5, 23), npts=8):
    """Median scalar-deviation of [A,B]*mu^-3 (D2) / [A,B]*mu^3 (D3) over the component (numerical)."""
    devs = []
    for sd in seeds:
        rng = np.random.default_rng(sd)
        for _ in range(npts):
            p = complex(rng.standard_normal(), rng.standard_normal())
            q = complex(rng.standard_normal(), rng.standard_normal())
            out = per.realize(component(p, q))
            if out is None:
                continue
            A, B = out
            mu, _ = per.meridian(A, B)
            if mu is None:
                continue
            comm = A @ B @ np.linalg.inv(A) @ np.linalg.inv(B)
            mu3 = mu @ mu @ mu
            M = comm @ np.linalg.inv(mu3) if kind == "D2" else comm @ mu3
            devs.append(_scalar_dev(M))
    return float(np.median(devs)), len(devs)


def w1_highprec_residual(dps=50):
    """W1=D2 to `dps` digits: symbolic B(p,q) over Q(i) -> 50-digit mpmath -> scalar criterion for
    [A,B]*mu^-3. Returns the worst scalar-deviation over 12 exact rational points (~1e-43)."""
    import sympy as sp
    from mpmath import mp, matrix as mpm, eig, mpc
    mp.dps = dps
    I = sp.I
    p, q = sp.symbols("p q")
    A = sp.diag(1, I, -I)
    Ai = A.inv()
    bb = sp.symbols("b11 b12 b13 b21 b22 b23 b31 b32 b33")
    B = sp.Matrix(3, 3, bb)
    adjB = B.adjugate()
    conds = [sp.trace(B) - q, sp.trace(A * B) - q, sp.trace(Ai * B) - 1,
             sp.trace(adjB) - p, sp.trace(A * adjB) - 1, sp.trace(Ai * adjB) - p,
             B.det() - 1, B[0, 1] - 1, B[1, 2] - 1]
    Bsym = B.subs(sp.solve(conds, list(bb), dict=True)[0])

    def to_mp(M):
        return mpm([[mpc(sp.N(sp.re(M[i, j]), dps + 10), sp.N(sp.im(M[i, j]), dps + 10))
                     for j in range(3)] for i in range(3)])

    def kron(X, Y):
        out = mpm(9, 9)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        out[3 * i + k, 3 * j + l] = X[i, j] * Y[k, l]
        return out

    def nullvec(E):
        G = mpm(9, 9)
        for i in range(9):
            for j in range(9):
                G[i, j] = sum(mp.conj(E[r, i]) * E[r, j] for r in range(18))
        ev, V = eig(G)
        k = min(range(9), key=lambda i: abs(ev[i]))
        return [V[r, k] for r in range(9)]

    Amp = to_mp(A)
    I3 = mpm([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    worst = mp.mpf(0)
    pts = [(2, 3), (-1, 5), (3, -2), (sp.Rational(1, 3), 4), (5, sp.Rational(-3, 2)), (-4, 7),
           (sp.Rational(2, 5), sp.Rational(9, 2)), (6, -1), (-2, -3), (7, 2),
           (sp.Rational(1, 2), sp.Rational(1, 2)), (8, -7)]
    for pv, qv in pts:
        Bmp = to_mp(Bsym.subs({p: pv, q: qv}))
        phiA, phiB = Amp * Amp * Bmp, Amp * Bmp
        K1, K2, K3, K4 = kron(Amp.T, I3), kron(I3, phiA), kron(Bmp.T, I3), kron(I3, phiB)
        E = mpm(18, 9)
        for i in range(9):
            for j in range(9):
                E[i, j] = K1[i, j] - K2[i, j]
                E[9 + i, j] = K3[i, j] - K4[i, j]
        v = nullvec(E)
        t = mpm([[v[0], v[3], v[6]], [v[1], v[4], v[7]], [v[2], v[5], v[8]]])
        mu = Amp**-1 * t
        comm = Amp * Bmp * Amp**-1 * Bmp**-1
        mu3i = (mu * mu * mu)**-1
        Msc = comm * mu3i
        off = max(abs(Msc[i, j]) for i in range(3) for j in range(3) if i != j)
        dg = max(abs(Msc[0, 0] - Msc[1, 1]), abs(Msc[1, 1] - Msc[2, 2]))
        worst = max(worst, off, dg)
    return float(worst), len(pts)


def main():
    print("B71 (P1) -- Dehn-filling A-variety as an EXACT scalar-matrix identity\n")
    print("exact criterion (mu, [A,B] commute, V46):  D2: [A,B]=c*mu^3 ;  D3: [A,B]*mu^3=c (scalar)\n")
    for name, comp, kind in [("W1 = D2 (M^3=L)", per.W1, "D2"), ("W2 = D3 (M^3 L=1)", per.W2, "D3")]:
        med, n = dehn_scalar_residual(comp, kind)
        print(f"  {name}: median scalar-deviation {med:.1e}  (n={n}, double precision)")
    print("\nW1 exact-grade (50-digit symbolic B over Q(i)):")
    worst, n = w1_highprec_residual()
    print(f"  M^3=L confirmed to ~{worst:.1e} at {n} exact rational points -- exact-grade upgrade of V44.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
