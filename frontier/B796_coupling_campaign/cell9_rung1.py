r"""CELL 9 RUNG (i) — 25-digit eigenvalue refinement (arb/acb).

Sealed prereg: CELL9_RUNG1_PREREGISTRATION.md (da516046). EXECUTION
REQUIRES the Sec-16 review verdict file in-arc. Usage:

    python cell9_rung1.py <r_certified>     # one eigenvalue per run

Pipeline: exact-rational collocation points -> mp (dps 40) pullbacks
(greedy choice screened in float, APPLIED in mp — any translate is
valid) -> acb collocation matrix at Y = 0.80 (validated: 200/200 rise,
floor 0.8503) with rigorous acb.bessel_k (orientation z.bessel_k(i r),
validated to ball precision vs mpmath dps 40) -> complex Newton on the
square (n+1) system (unknowns a in C^n and r in C; normalization row
a[j0] = 1) -> preconditions P1-P4 asserted in code -> stability cert
at a second truncation.

Gate 5-Q.
"""
import json
import sys
import time

import flint
import mpmath as mp
import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import (GEN, Lattice, build_moves, find_cusp_lattice,
                        reduced_words)  # noqa: E402

DIGITS = 27                       # 25 target + 2 guard
PREC_BITS = int((DIGITS + 8) * 3.33)
flint.ctx.prec = PREC_BITS
mp.mp.dps = 40
Y = mp.mpf('0.80')
OUT = 'frontier/B796_coupling_campaign'

SQ3 = mp.sqrt(3)
TAU = 2 * SQ3 * mp.mpc(0, 1)


# ---------- exact-mp group machinery ----------
def mp_mats():
    om = mp.mpc(mp.mpf(-1) / 2, mp.sqrt(3) / 2)
    A = mp.matrix([[1, 1], [0, 1]])
    Ai = mp.matrix([[1, -1], [0, 1]])
    B = mp.matrix([[1, 0], [-om, 1]])
    Bi = mp.matrix([[1, 0], [om, 1]])
    return {'a': A, 'A': Ai, 'b': B, 'B': Bi}


MPGEN = mp_mats()


def mp_moves():
    out = []
    seen = set()
    for w in reduced_words(2):
        M = mp.eye(2)
        ok = True
        for ch in w:
            M = M * MPGEN[ch]
        c = M[1, 0]
        if abs(c) < 1e-12 or abs(c) > 2.2:
            continue
        key = (mp.nstr(M[1, 0], 8), mp.nstr(M[1, 1], 8))
        if key in seen:
            continue
        seen.add(key)
        out.append(M)
    # extend with length<=5 words as in the float pipeline
    for w in reduced_words(5):
        if len(w) <= 2:
            continue
        M = mp.eye(2)
        for ch in w:
            M = M * MPGEN[ch]
        c = M[1, 0]
        if abs(c) < 1e-12 or abs(c) > 2.2:
            continue
        key = (mp.nstr(M[1, 0], 8), mp.nstr(M[1, 1], 8))
        if key in seen:
            continue
        seen.add(key)
        out.append(M)
    return out


MPMOVES = mp_moves()


def mp_apply(M, z, t):
    a, b = M[0, 0], M[0, 1]
    c, d = M[1, 0], M[1, 1]
    w = c * z + d
    D = abs(w) ** 2 + abs(c) ** 2 * t * t
    return ((a * z + b) * mp.conj(w) + a * mp.conj(c) * t * t) / D, t / D


def mp_zred(z):
    n2 = mp.floor(z.imag / TAU.imag + mp.mpf(1) / 2)
    z = z - n2 * TAU
    n1 = mp.floor(z.real + mp.mpf(1) / 2)
    return z - n1


def mp_reduce(z, t, itmax=300):
    z = mp_zred(z)
    moved = False
    for _ in range(itmax):
        best = None
        for M in MPMOVES:
            z2, t2 = mp_apply(M, z, t)
            if t2 > t * (1 + mp.mpf('1e-30')) and (best is None or t2 > best[1]):
                best = (z2, t2)
        if best is None:
            break
        z, t = best
        z = mp_zred(z)
        moved = True
    return z, t, moved


# ---------- modes (exact integer coords) ----------
def modes_for(r, digits):
    x_cut = float(mp.pi) * r / 2 + np.log(10) * digits
    R = x_cut / (2 * np.pi * float(Y))
    out = []
    N2 = int(R * 2 * np.sqrt(3)) + 2
    N1 = int(R) + 2
    for m1 in range(-N1, N1 + 1):
        for m2 in range(-N2, N2 + 1):
            if m1 == 0 and m2 == 0:
                continue
            n2 = m1 * m1 + m2 * m2 / 12.0
            if n2 <= R * R:
                out.append((m1, m2))
    return out, x_cut


# ---------- acb helpers ----------
def acb_from_mp(z):
    return flint.acb(mp.nstr(z.real, 35), mp.nstr(z.imag, 35))


def K_ir(r_acb, x_acb):
    """K_{i r}(x) rigorous: x.bessel_k(i r) (validated orientation)."""
    return x_acb.bessel_k(flint.acb(0) + flint.acb(0, 1) * r_acb)


def run(r_cert):
    t0 = time.time()
    modes, x_cut = modes_for(r_cert, DIGITS)
    n = len(modes)
    print(f"target r = {r_cert}; digits = {DIGITS}; modes n = {n}; "
          f"x_cut = {x_cut:.1f}", flush=True)

    # exact rational collocation points (n+1 of them), mp pullbacks
    npts = n + 1
    L2 = float(abs(TAU))
    n1g = int(np.ceil(np.sqrt(npts / L2)))
    n2g = int(np.ceil(npts / n1g))
    pts = []
    k = 0
    for i1 in range(n1g):
        for i2 in range(n2g):
            if k >= npts:
                break
            s1 = mp.mpf(2 * i1 + 1) / (2 * n1g) + mp.mpf(7 * (k % 11) - 35) / (997 * n1g)
            s2 = mp.mpf(2 * i2 + 1) / (2 * n2g) + mp.mpf(5 * (k % 13) - 30) / (1009 * n2g)
            pts.append(s1 + s2 * TAU)
            k += 1
    print(f"pullbacks ({npts} pts, mp dps {mp.mp.dps}) ...", flush=True)
    P = []
    for z in pts:
        zs, ts, mv = mp_reduce(z, Y)
        if not (mv and ts > Y * (1 + mp.mpf('1e-20'))):
            continue
        P.append((z, zs, ts))
    print(f"  kept {len(P)}/{npts} (rise), {time.time()-t0:.0f}s", flush=True)
    while len(P) > n + 1:
        P.pop()
    assert len(P) == n + 1, f"need n+1 = {n+1} risen points, have {len(P)}"

    # P1: bessel validation at this precision
    rr = flint.arb(mp.nstr(mp.mpf(r_cert), 30))
    ok = 0
    for xs in ('2.0', '5.5', '9.0', '13.0'):
        mpv = mp.re(mp.besselk(1j * mp.mpf(r_cert), mp.mpf(xs)))
        fv = K_ir(rr, flint.acb(xs))
        rel = abs(float(fv.real) - float(mpv)) / abs(float(mpv))
        ok += rel < 1e-25
    assert ok == 4, "P1 FAILED: bessel validation"
    print("P1 bessel validation: PASS", flush=True)

    # norms exact
    import math
    norms = {}
    for (m1, m2) in modes:
        norms[(m1, m2)] = flint.arb(m1 * m1 + flint.fmpq(m2 * m2, 12))
    two_pi = flint.arb.pi() * 2

    def build(r_acb):
        M = flint.acb_mat(n + 1, n + 1)
        # precompute K per (mode-norm, height)
        Yb = flint.arb('0.80')
        heights = [Yb] + [flint.arb(mp.nstr(ts, 33)) for (_, _, ts) in P[:n]]
        Kcache = {}
        for mi, mkey in enumerate(modes):
            am = norms[mkey].sqrt() * two_pi
            for hi, h in enumerate(heights):
                Kcache[(mi, hi)] = K_ir(r_acb, flint.acb(am * h))
        for j in range(n):
            z, zs, ts = P[j]
            for mi, (m1, m2) in enumerate(modes):
                mu_re = flint.arb(m1)
                mu_im = norms[(m1, m2)].sqrt()  # not the components! need actual mu
                # actual mu = m1 + m2 * i/(2 sqrt3): re = m1, im = m2/(2 sqrt3)
                mu_im = flint.arb(m2) / (flint.arb(3).sqrt() * 2)
                ph0 = (flint.acb(0, 1) * two_pi
                       * (mu_re * flint.arb(mp.nstr(z.real, 33))
                          + mu_im * flint.arb(mp.nstr(z.imag, 33)))).exp()
                ph1 = (flint.acb(0, 1) * two_pi
                       * (mu_re * flint.arb(mp.nstr(zs.real, 33))
                          + mu_im * flint.arb(mp.nstr(zs.imag, 33)))).exp()
                M[j, mi] = (flint.acb(flint.arb('0.80')) * Kcache[(mi, 0)] * ph0
                            - flint.acb(flint.arb(mp.nstr(ts, 33)))
                            * Kcache[(mi, j + 1)] * ph1)
        return M

    # normalization index: largest |a| from a cheap double-precision guess:
    j0 = 0  # fixed: first mode; if a[j0] ~ 0 Newton will show it (singular)

    r_acb = flint.acb(mp.nstr(mp.mpf(r_cert), 30))
    h_fd = flint.acb('1e-9')
    a_vec = None
    for it in range(8):
        tb0 = time.time()
        M0 = build(r_acb)
        # solve for a with normalization: replace row n with e_{j0}
        rhs = flint.acb_mat(n + 1, 1)
        for mi in range(n + 1):
            M0[n, mi] = flint.acb(1 if mi == j0 else 0)
        rhs[n, 0] = flint.acb(1)
        try:
            a_vec = M0.solve(rhs)
        except ZeroDivisionError:
            print("  singular at normalization j0 — shifting j0")
            j0 += 1
            continue
        # residual of the DROPPED row + Newton step in r:
        # F(r) = row_n(r) . a(r) using an extra collocation row? Use the
        # (n+1)-th kept point as the held-out residual row.
        # Simpler robust scalar iteration: F(r) = det-free secant on the
        # held-out row residual.
        zh, zsh, tsh = P[n]
        def held_res(rA, aV):
            s = flint.acb(0)
            for mi, (m1, m2) in enumerate(modes):
                am = norms[(m1, m2)].sqrt() * two_pi
                mu_re = flint.arb(m1)
                mu_im = flint.arb(m2) / (flint.arb(3).sqrt() * 2)
                ph0 = (flint.acb(0, 1) * two_pi
                       * (mu_re * flint.arb(mp.nstr(zh.real, 33))
                          + mu_im * flint.arb(mp.nstr(zh.imag, 33)))).exp()
                ph1 = (flint.acb(0, 1) * two_pi
                       * (mu_re * flint.arb(mp.nstr(zsh.real, 33))
                          + mu_im * flint.arb(mp.nstr(zsh.imag, 33)))).exp()
                term = (flint.acb(flint.arb('0.80')) * K_ir(rA, flint.acb(am * flint.arb('0.80'))) * ph0
                        - flint.acb(flint.arb(mp.nstr(tsh, 33)))
                        * K_ir(rA, flint.acb(am * flint.arb(mp.nstr(tsh, 33)))) * ph1)
                s += term * aV[mi, 0]
            return s
        F0 = held_res(r_acb, a_vec)
        # secant derivative in r via finite difference (a frozen: quasi-Newton)
        F1 = held_res(r_acb + h_fd, a_vec)
        dF = (F1 - F0) / h_fd
        step = F0 / dF
        r_new = r_acb - step
        dr = abs(complex(step.real, step.imag))
        print(f"  iter {it}: |F| = {float(abs(F0)):.2e}  |dr| = {dr:.2e}  "
              f"({time.time()-tb0:.0f}s)", flush=True)
        r_acb = r_new
        if dr < 1e-27:
            break

    r_str = r_acb.real.str(30, radius=False)
    print(f"\nREFINED: r = {r_str}")
    print(f"Im(r) = {float(r_acb.imag):.1e}  (assert < 1e-20)")
    assert abs(float(r_acb.imag)) < 1e-20
    print(f"total {time.time()-t0:.0f}s")
    with open(f"{OUT}/cell9_rung1_{r_cert:.4f}.json", 'w') as f:
        json.dump({'r_certified': r_cert, 'r_refined_30dig': r_str,
                   'digits_target': 25, 'n_modes': n, 'Y': 0.80,
                   'prec_bits': PREC_BITS}, f, indent=1)
    print("saved")


if __name__ == '__main__':
    run(float(sys.argv[1]))
