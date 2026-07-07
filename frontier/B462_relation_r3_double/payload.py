#!/usr/bin/env python3
"""B462 R3a' payload — the phi-scan for the chiral control (5_2) + the mixed glue.

Two pairing types per prereg:
  sesquilinear  H(phi) = <Z(Mbar), rho(phi) Z(N)>  = the mirror-double  M u_phi Nbar
  bilinear      B(phi) = Z(M)^T rho(phi) Z(N)      = the same-orientation double M u_phi N

Forced structures (adjudicated in-session BEFORE reading, verified here on 5_2):
  F-a  TT-zero: Kirby-Melvin symmetry J_{r-n} = J_n + tw(r-n)^2 = -tw(n)^2 (odd r)
       forces the T^2 pairing to vanish for ANY 0-framed knot (both pairing types).
  F-b  bilinear ST = TS: transpose invariance of a scalar (any Z) — forced.
  F-c  4_1: sesquilinear = bilinear identically (Z real, amphichirality) — the
       reason the 4_1 mirror-double payload was CUT by theorem.
LIVE observables: the sesquilinear ST vs TS split for the CHIRAL 5_2 (Z complex),
and the H vs B (mirror-double vs same-double) gap — zero for 4_1 by F-c.
"""
import os
import sys

import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B441_child_wrt"))
import wrt as B441
from masbaum import masbaum_cj, gates
from phi_scan import qd, smat, tdiag, tau_from_vector

mp.mp.dps = 30
WORDS = ['', 'T', 'TT', 'S', 'ST', 'TS', 'STS']


def zvec(r, cj):
    q = mp.e**(2j * mp.pi / r)
    return [qd(n, r) * cj(n, q) for n in range(1, r)]


def rho(r, word):
    n = r - 1
    S = smat(r)
    T = tdiag(r)
    M = [[mp.mpf(1) if i == j else mp.mpf(0) for j in range(n)] for i in range(n)]
    def mul(A_, B_):
        return [[sum(A_[i][k] * B_[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    for ch in word:
        if ch == 'S':
            M = mul(M, S)
        elif ch == 'T':
            M = mul(M, [[T[i] if i == j else 0 for j in range(n)] for i in range(n)])
    return M


def pair(ZA, ZB, M, sesqui):
    n = len(ZA)
    left = [mp.conj(z) for z in ZA] if sesqui else ZA
    return complex(sum(left[i] * sum(M[i][j] * ZB[j] for j in range(n)) for i in range(n)))


def table(r, cjA, cjB, label):
    ZA, ZB = zvec(r, cjA), zvec(r, cjB)
    print(f"  -- {label}, r={r} --")
    for w in WORDS:
        M = rho(r, w)
        H = pair(ZA, ZB, M, True)
        B = pair(ZA, ZB, M, False)
        aH = float(mp.arg(mp.mpc(H))) if H else 0.0
        aB = float(mp.arg(mp.mpc(B))) if B else 0.0
        print(f"    {w or 'id':4s}  |H|={abs(H):11.6f} argH={aH:+8.4f}   "
              f"|B|={abs(B):11.6f} argB={aB:+8.4f}   |H|-|B|={abs(H)-abs(B):+.6f}")


def km_symmetry_check(cj, name):
    """F-a precondition on a general (chiral) knot: J_{r-n} = J_n at q=e^{2pi i/r}."""
    worst = 0
    for r in (5, 7, 9):
        q = mp.e**(2j * mp.pi / r)
        worst = max(worst, max(abs(cj(r - n, q) - cj(n, q)) for n in range(1, r)))
    print(f"  KM symmetry J_(r-n)=J_n for {name}: max dev {float(worst):.2e}")
    return worst < 1e-18


if __name__ == '__main__':
    if not gates():
        sys.exit(1)
    cj52 = masbaum_cj(2)
    print("\n== F-a precondition on the chiral knot ==")
    ok = km_symmetry_check(cj52, "5_2 (Masbaum p=2)")
    print(f"  => TT-zero is {'FORCED for 5_2 too' if ok else 'NOT forced — investigate'}")

    print("\n== the 5_2 doubles (mirror-double H vs same-double B) ==")
    for r in (5, 7, 9):
        table(r, cj52, cj52, "5_2 u_phi 5_2")

    print("\n== the mixed control 4_1 u_phi 5_2 ==")
    for r in (5, 7, 9):
        table(r, B441.cj_fig8, cj52, "4_1 u_phi 5_2")

    print("\n== F-c verification: 4_1's H = B identically (the CUT-by-theorem, checked) ==")
    for r in (5, 7, 9):
        ZA = zvec(r, B441.cj_fig8)
        dev = max(abs(pair(ZA, ZA, rho(r, w), True) - pair(ZA, ZA, rho(r, w), False)) for w in WORDS)
        print(f"  r={r}: max |H-B| over words = {dev:.2e}")
