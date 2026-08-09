r"""B1007 — an ARBITRARY-PRECISION Hejhal solver for Maass cusp forms on m004.

*** THIS FILE IS A FAILED ATTEMPT, KEPT AS A RECORD. DO NOT BUILD ON IT. ***

READ THIS FIRST
---------------
**A WORKING 25-DIGIT SOLVER IS ALREADY ON MAIN:**

    frontier/B878_maass_upper_window/branch_cell9_rung1_v2.py

It carries B922's own seal hash (169e9042), it is the script behind the 58.1-hour
run, and it already drives arb (flint.ctx.prec, acb.bessel_k, acb_mat LU, n ~ 1300).
This file was written WITHOUT READING IT. If you want high-precision Maass
eigenvalues on m004, go there.

WHAT THIS FILE'S ORIGINAL DOCSTRING CLAIMED, AND WHY IT WAS WRONG
-----------------------------------------------------------------
It claimed B922's 58.1 hours and B798's "4-5 ORDERS COSTLIER" were "measured
against arithmetic that is not what arb does", on the strength of these timings:

    dps    1000x K_ir(x)    200x200 acb_mat solve
     25         0.07 s              0.34 s
     50         0.10 s              0.48 s
    100         0.15 s              0.64 s

The timings are real. The conclusion does not follow, twice over:

  1. B798 EXPLICITLY priced "a different numerical stack (arb/mpmath Bessel, mp
     linear algebra)" -- it NAMED arb -- and the 58.1h run USED arb.
  2. B798's model has TWO terms: modes scale ~LINEARLY with precision (900 ->
     11250 at 100 digits) and the dense solve is CUBIC in modes (1953x). These
     timings hold the mode count FIXED and vary only dps, i.e. they measure the
     one term that was never the problem. Precision is cheap PER OPERATION; the
     cost is that precision DEMANDS MODES.

**B798's law AND its cost estimate both stand.**

WHY THE SOLVER BELOW DOES NOT WORK (diagnosed against the working source)
-------------------------------------------------------------------------
  a. NO COLUMN EQUILIBRATION. The working code divides each column by
     |Y*K(2pi|mu|Y)|, because "the truncation-edge dynamic range (~1e-32 at the
     real run) collapses to O(1), which arb's certified LU requires at n >~ 1300".
     The 1e26 blowup at M=40 below IS this, and the fix was already written down.
  b. NO RISEN-POINT FILTER. The working code keeps a point only if it MOVED and
     ts > Y*(1+1e-20). An unmoved point gives f(z,Y) = f(z,Y): a ZERO ROW.
  c. MODES BY COUNT, NOT RADIUS. The working code takes all |mu| <= R_cut with
     R_cut = (pi*r/2 + margin)/(2*pi*Y) -- the truncation set by where K_ir dies.
  d. Y = 0.28 here against the sealed Y = 0.75.
  e. THE CONCEPTUAL ERROR: g(r), the held-out-row residual, is a REFINEMENT
     indicator the working code uses inside an ALREADY-BRACKETED root. DETECTION
     is sigma_min of the COLUMN-NORMALIZED V(r), which DIPS at an eigenvalue.
     Searching with g(r) finds no sign change because g IS NOT BUILT TO HAVE ONE.

THE SETUP (from B792's own docstring, not re-derived)
----------------------------------------------------
m004 = Gamma \ H^3, Gamma = <A, B> the Riley holonomy,
    A = [[1,1],[0,1]],  B = [[1,0],[-w,1]],  w = (-1 + i sqrt3)/2,
cusp at infinity, cusp lattice Lam = Z + Z*tau with **tau = 2 sqrt3 i** (found
by B792's brute-force parabolic search; verified exact here).

A Maass cusp form with lambda = 1 + r^2 has the cusp expansion

    f(z,t) = sum_{0 != mu in Lam*} a_mu * t * K_{ir}(2 pi |mu| t) * e(<mu,z>)

with <mu,z> = Re(mu)Re(z) + Im(mu)Im(z) and Lam* the dual lattice. For
Lam = Z + 2sqrt3 i Z this gives **Lam* = Z + (i/(2 sqrt3)) Z**, exactly.

THE PRECISION ARCHITECTURE — the point of the rewrite
-----------------------------------------------------
The pullback is a **discrete** decision: which group element raises the height.
Double precision chooses it; **arb then applies it EXACTLY**, because every move
is a matrix over Z[w] (all 91 verified integral). So the double-precision
geometry does NOT cap the achievable precision. This is the same observation
cc3 made in C1 ("ascent only needs *a* height-raising element") turned into an
architecture.

Everything downstream of the choice -- the Moebius action, |mu|, K_{ir}, the
linear algebra -- is arb ball arithmetic, so the digits carry **rigorous error
bounds** rather than a convergence argument. That is stronger than the
instrument it replaces.

THE EIGENVALUE CONDITION
------------------------
Collocation: sample points (z_j, Y) below the fundamental domain, pull back to
(z*_j, t*_j), impose f(z_j, Y) = f(z*_j, t*_j). Normalising a_{mu_1} = 1 makes
this an inhomogeneous square system in the remaining coefficients; the system is
consistent only at an eigenvalue, so the residual of one held-out equation is a
real function g(r) with a sign change AT the eigenvalue. Refine by bisection.

VALIDATION GATE — non-negotiable, AND IT FIRED
----------------------------------------------
This solver must reproduce B922's banked r = 4.9000853730625213014795758 before
any of its output is used for anything. A new instrument that cannot recover a
known answer is not evidence about an unknown one.

IT DOES NOT REPRODUCE IT. M=40 gives g ~ 1e26; M=80 is smooth with no sign
change. Nothing this file produces enters any ledger, and nothing should.

Usage:  python3 arb_maass.py selftest
        python3 arb_maass.py refine <r_lo> <r_hi> [dps] [M]
"""
from __future__ import annotations

import json
import math
import os
import sys

from flint import acb, acb_mat, arb, ctx

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- exact geometry -------------------------------------------------------
with open(os.path.join(HERE, "moves_eisenstein.json")) as fh:
    MOVES_EIS = json.load(fh)            # 91 matrices over Z[w], entries (a,b) = a + b*w


def eis(a: int, b: int) -> acb:
    """a + b*w with w = (-1 + i sqrt3)/2, exact in ball arithmetic."""
    s3 = arb(3).sqrt()
    return acb(arb(a) - arb(b) / 2, arb(b) * s3 / 2)


def moves_acb():
    return [[[eis(*MOVES_EIS[k][i][j]) for j in range(2)] for i in range(2)]
            for k in range(len(MOVES_EIS))]


def tau_exact() -> acb:
    """the cusp shape: 2 sqrt3 i"""
    return acb(arb(0), 2 * arb(3).sqrt())


def act(Mx, z: acb, t: arb):
    """Moebius action of [[a,b],[c,d]] on (z,t) in H^3. Returns (z', t')."""
    a, b = Mx[0]
    c, d = Mx[1]
    den = (c * z + d)
    nrm = (den.real ** 2 + den.imag ** 2) + (c.real ** 2 + c.imag ** 2) * t ** 2
    zt = ((a * z + b) * den.conjugate()
          + acb(a.real * c.real + a.imag * c.imag,
                a.imag * c.real - a.real * c.imag) * t ** 2) / acb(nrm)
    tp = t / nrm
    return zt, tp


def pullback(z: acb, t: arb, MV, itmax: int = 200):
    """Raise the height by repeated exact moves + lattice translation.

    The CHOICE of move is made on floats (a discrete decision); the move is then
    APPLIED exactly. Returns (z*, t*) in ball arithmetic.
    """
    tau = tau_exact()
    for _ in range(itmax):
        # lattice-reduce z (exact: subtract integer combinations of 1 and tau)
        n2 = int(round(float(z.imag) / float(tau.imag)))
        if n2:
            z = z - tau * acb(n2)
        n1 = int(round(float(z.real)))
        if n1:
            z = z - acb(n1)
        # pick the height-raising move on floats, then apply it exactly
        best, bt = None, float(t)
        for Mx in MV:
            zc, tc = act(Mx, z, t)
            ft = float(tc)
            if ft > bt * (1 + 1e-12):
                best, bt = Mx, ft
        if best is None:
            return z, t
        z, t = act(best, z, t)
    return z, t


# ---- the dual lattice -----------------------------------------------------
def dual_lattice(M: int):
    """Lam* = Z + (i/(2 sqrt3)) Z, ordered by |mu|, first M nonzero mu."""
    s3 = arb(3).sqrt()
    inv = 1 / (2 * s3)
    out = []
    R = int(math.ceil(math.sqrt(M))) + 6
    for m in range(-R, R + 1):
        for n in range(-4 * R, 4 * R + 1):
            if m == 0 and n == 0:
                continue
            mu = acb(arb(m), arb(n) * inv)
            out.append((float(abs(complex(float(mu.real), float(mu.imag)))), m, n))
    out.sort()
    return [(m, n) for _, m, n in out[:M]]


def mu_of(m: int, n: int) -> acb:
    s3 = arb(3).sqrt()
    return acb(arb(m), arb(n) / (2 * s3))


# ---- the collocation matrix ----------------------------------------------
def term(mu: acb, z: acb, t: arb, r: arb) -> acb:
    """t * K_{ir}(2 pi |mu| t) * exp(2 pi i <mu,z>)"""
    absmu = (mu.real ** 2 + mu.imag ** 2).sqrt()
    x = acb(2 * arb.pi() * absmu * t)
    K = acb.bessel_k(acb(arb(0), r), x)
    ph = 2 * arb.pi() * (mu.real * z.real + mu.imag * z.imag)
    return acb(t) * K * acb(ph.cos(), ph.sin())


def build_system(r: arb, M: int, Y: arb, MV, pts):
    """Rows: automorphy at each sample point. Columns: coefficients a_mu.
    Column 0 is normalised to 1 and moved to the RHS."""
    L = dual_lattice(M)
    rows, rhs = [], []
    for (z, zs, ts) in pts:
        row = []
        for k, (m, n) in enumerate(L):
            mu = mu_of(m, n)
            v = term(mu, z, Y, r) - term(mu, zs, ts, r)
            if k == 0:
                rhs.append([-v])
            else:
                row.append(v)
        rows.append(row)
    return acb_mat(rows), acb_mat(rhs), L


def sample_points(nQ: int, Y: arb, MV):
    """nQ points on the horosphere at height Y, with their pullbacks."""
    tau = tau_exact()
    pts = []
    for j in range(nQ):
        u = arb(2 * j + 1) / arb(2 * nQ)
        v = arb(2 * ((j * 7) % nQ) + 1) / arb(2 * nQ)
        z = acb(u) + tau * acb(v)
        zs, ts = pullback(z, Y, MV)
        pts.append((z, zs, ts))
    return pts


def g_of_r(r_str: str, M: int, dps: int, Yf: float = 0.28, extra: int = 3):
    """Residual of held-out equations at r. Sign change AT an eigenvalue."""
    ctx.dps = dps + 15
    r = arb(r_str)
    Y = arb(Yf)
    MV = moves_acb()
    pts = sample_points(M - 1 + extra, Y, MV)
    A, b, L = build_system(r, M, Y, MV, pts)
    n = M - 1
    Asq = acb_mat([[A[i, j] for j in range(n)] for i in range(n)])
    bsq = acb_mat([[b[i, 0]] for i in range(n)])
    a = Asq.solve(bsq)
    res = b[n, 0]
    for j in range(n):
        res -= A[n, j] * a[j, 0]
    return res


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "selftest":
        ctx.dps = 40
        print("geometry:")
        print(f"  moves (exact Z[w])   : {len(MOVES_EIS)}")
        print(f"  tau                  : {tau_exact()}")
        print(f"  |Lam*| first 5       : {dual_lattice(5)}")
        print(f"  K_ir sample          : {acb.bessel_k(acb(arb(0), arb('4.9')), acb(3))}")
        MV = moves_acb()
        z = acb(arb('0.31'), arb('0.44'))
        zs, ts = pullback(z, arb('0.28'), MV)
        print(f"  pullback t: 0.28 -> {ts}")
    elif cmd == "g":
        r = sys.argv[2]
        M = int(sys.argv[3]) if len(sys.argv) > 3 else 12
        dps = int(sys.argv[4]) if len(sys.argv) > 4 else 30
        print(f"g({r}) M={M} dps={dps} = {g_of_r(r, M, dps)}")


if __name__ == "__main__":
    main()
