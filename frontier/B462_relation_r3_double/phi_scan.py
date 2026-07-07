#!/usr/bin/env python3
"""B462 (Relation R3) — the phi-scan WRT pairing for the double, with the B441 gate.

Conventions (fixed here, validated by the gate): level r, colors n=1..r-1;
S_{nm} = sqrt(2/r) sin(pi n m / r); T_{nn} = exp(2 pi i (n^2 - 1)/(4r) - 2 pi i c/24-ish)
absorbed into the standard T = zeta_{4r}^{n^2-1} phase times the global anomaly, which the
GATE calibrates: my (Z, S, T, framing) must reproduce B441's tau_r(4_1(5,1)) before any
phi-scan value is read.
"""
import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B441_child_wrt"))
import wrt as B441

mp.mp.dps = 40


def smat(r):
    return [[mp.sqrt(mp.mpf(2)/r) * mp.sin(mp.pi * n * m / r) for m in range(1, r)] for n in range(1, r)]


def tdiag(r):
    # T_{nn} = exp(2 pi i ((n^2-1)/(4r)))  (the anomaly phase handled by the gate calibration)
    return [mp.e**(2j * mp.pi * (mp.mpf(n*n - 1) / (4*r))) for n in range(1, r)]


def qd(n, r):
    return mp.sin(n * mp.pi / r) / mp.sin(mp.pi / r)


def zvec(r, cj):
    """Z_n = qd(n) * J_n — B441's weighting (its d2 = qd^2 splits as vector x unknot-vector)."""
    q = mp.e**(2j * mp.pi / r)
    return [qd(n, r) * cj(n, q) for n in range(1, r)]


def tau_from_vector(r, p):
    """tau_r(K(p,1)) = <U, T^p Z>/<U, T U> with U_n = qd(n) — B441's F_L/F_U exactly."""
    Z = zvec(r, B441.cj_fig8)
    U = [qd(n, r) for n in range(1, r)]
    T = tdiag(r)
    FL = sum(U[n] * Z[n] * T[n]**p for n in range(r-1))
    FU = sum(U[n] * U[n] * T[n] for n in range(r-1))
    return FL / FU


def pairing(r, phi_word, cjA=None, cjB=None):
    """<Z(Mbar), rho(phi) Z(M)> at level r; phi_word over {'S','T'}."""
    cjA = cjA or B441.cj_fig8
    cjB = cjB or B441.cj_fig8
    ZA = zvec(r, cjA)
    ZB = zvec(r, cjB)
    S = smat(r)
    T = tdiag(r)
    n = r - 1
    # rho(phi) as a matrix product
    import copy
    rho = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(n)] for i in range(n)]
    def matmul(A_, B_):
        return [[sum(A_[i][k] * B_[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    for ch in phi_word:
        if ch == 'S':
            rho = matmul(rho, S)
        elif ch == 'T':
            rho = matmul(rho, [[T[i] if i == j else 0 for j in range(n)] for i in range(n)])
    ZAc = [mp.conj(z) for z in ZA]   # Z(Mbar) = conjugate vector
    val = sum(ZAc[i] * sum(rho[i][j] * ZB[j] for j in range(n)) for i in range(n))
    return complex(val)


if __name__ == '__main__':
    print("== GATE: reproduce B441's tau_r(4_1(5,1)) ==")
    ok = True
    for r in (5, 7, 9, 11):
        mine = complex(tau_from_vector(r, 5))
        theirs = complex(B441.wrt(B441.cj_fig8, 5, r))
        match = abs(mine - theirs) < 1e-20 * max(1, abs(theirs)) or abs(mine - theirs) < 1e-12
        ok &= match
        print(f"  r={r}: mine={mine:.10f}  B441={theirs:.10f}  match={match}")
    if not ok:
        print("GATE FAILED - no phi-scan values read.")
        sys.exit(1)
    print("GATE PASSED.\n")
    print("== the phi-scan (fig-8 double), levels r=5..9 ==")
    WORDS = ['', 'T', 'TT', 'S', 'ST', 'TS', 'STS']
    for r in (5, 7, 9):
        row = []
        for w in WORDS:
            v = pairing(r, w)
            row.append(f"{w or 'id'}: {abs(v):.6f} @ {float(mp.arg(mp.mpc(v))):+.4f}")
        print(f"  r={r}: " + " | ".join(row))
    print("\n== the 5_2 payload + mixed control live in payload.py (Masbaum gates in masbaum.py) ==")
