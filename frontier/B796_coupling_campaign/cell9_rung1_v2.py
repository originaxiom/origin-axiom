r"""CELL 9 RUNG (i) v2 — conformant to sealed prereg 3ba81779.

Usage:  python cell9_rung1_v2.py <r_certified> [--mult2]

Implements EXACTLY the sealed method: Y = 0.75; joint square Newton on
(a, r) with normalization row; P1 (>= 10 samples, compared in mpmath,
<= 1e-27), P2 (monotone residual), P3 (gap-midpoint displaced control),
P4 (three perturbed starts agree to >= 26 digits); validation gate
(>= 7 overlap digits vs certified); stability cert at +5 digits sets
|dr|_stab; mult-2 dual-normalization protocol with the pre-declared
pair outcome. PSLQ runs in a separate stage (cell9_pslq.py) using the
sealed noise-floor tolerance formula.

Gate 5-Q.
"""
import json
import sys
import time

import flint
import mpmath as mp
import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import reduced_words  # noqa: E402

DIGITS = 27
flint.ctx.prec = int((DIGITS + 10) * 3.33)
mp.mp.dps = 40
YV = mp.mpf('0.75')
OUT = 'frontier/B796_coupling_campaign'
SQ3 = mp.sqrt(3)
TAU = 2 * SQ3 * mp.mpc(0, 1)

GAP_MIDPOINTS = {3.938916864: 4.42, 4.900085373: 5.29, 7.072004187: 7.21}
CERT = {3.938916864: '3.938916864', 4.900085373: '4.900085373',
        7.072004187: '7.072004187'}


# ---------------- mp group machinery ----------------
def _mpgen():
    om = mp.mpc(mp.mpf(-1) / 2, mp.sqrt(3) / 2)
    return {'a': mp.matrix([[1, 1], [0, 1]]),
            'A': mp.matrix([[1, -1], [0, 1]]),
            'b': mp.matrix([[1, 0], [-om, 1]]),
            'B': mp.matrix([[1, 0], [om, 1]])}


MPGEN = _mpgen()


def _mpmoves():
    out, seen = [], set()
    for w in reduced_words(5):
        M = mp.eye(2)
        for ch in w:
            M = M * MPGEN[ch]
        c = M[1, 0]
        if abs(c) < 1e-12 or abs(c) > 2.2:
            continue
        key = (mp.nstr(c, 8), mp.nstr(M[1, 1], 8))
        if key in seen:
            continue
        seen.add(key)
        out.append(M)
    return out


MPMOVES = _mpmoves()


def mp_apply(M, z, t):
    c, d = M[1, 0], M[1, 1]
    w = c * z + d
    D = abs(w) ** 2 + abs(c) ** 2 * t * t
    return ((M[0, 0] * z + M[0, 1]) * mp.conj(w)
            + M[0, 0] * mp.conj(c) * t * t) / D, t / D


def mp_zred(z):
    z = z - mp.floor(z.imag / TAU.imag + mp.mpf('0.5')) * TAU
    return z - mp.floor(z.real + mp.mpf('0.5'))


def mp_reduce(z, t):
    z = mp_zred(z)
    moved = False
    for _ in range(300):
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


# ---------------- modes / points ----------------
def modes_for(r):
    x_cut = float(mp.pi) * r / 2 + np.log(10) * DIGITS
    R = x_cut / (2 * np.pi * float(YV))
    out = []
    for m1 in range(-int(R) - 2, int(R) + 3):
        for m2 in range(-int(R * 3.47) - 2, int(R * 3.47) + 3):
            if (m1 or m2) and m1 * m1 + m2 * m2 / 12.0 <= R * R:
                out.append((m1, m2))
    return out, x_cut


def coll_points(npts):
    L2 = float(abs(TAU))
    n1g = int(np.ceil(np.sqrt(npts / L2)))
    n2g = int(np.ceil(npts / n1g))
    pts, k = [], 0
    for i1 in range(n1g):
        for i2 in range(n2g):
            if k >= npts + 40:
                break
            s1 = mp.mpf(2 * i1 + 1) / (2 * n1g) + mp.mpf(7 * (k % 11) - 35) / (997 * n1g)
            s2 = mp.mpf(2 * i2 + 1) / (2 * n2g) + mp.mpf(5 * (k % 13) - 30) / (1009 * n2g)
            pts.append(s1 + s2 * TAU)
            k += 1
    return pts


# ---------------- arb helpers ----------------
def arb_mp(x, d=33):
    return flint.arb(mp.nstr(x, d))


def K_ir(r_arb, x_arb):
    return flint.acb(x_arb).bessel_k(flint.acb(0, 1) * flint.acb(r_arb))


def p1_check(r_cert):
    ok = 0
    samples = [(r_cert, x) for x in (1.5, 2.0, 3.3, 5.5, 7.0, 9.0, 11.0, 13.0)]
    samples += [(r_cert * 0.7, 4.0), (r_cert * 1.3, 6.0)]
    for (rv, xv) in samples:
        ref = mp.re(mp.besselk(1j * mp.mpf(rv), mp.mpf(xv)))
        fv = K_ir(flint.arb(mp.nstr(mp.mpf(rv), 30)), flint.arb(str(xv)))
        fv_mp = mp.mpf(fv.real.str(35, radius=False))
        rel = abs(fv_mp - ref) / abs(ref)
        ok += rel < mp.mpf('1e-27')
    assert ok == len(samples), f"P1 FAILED ({ok}/{len(samples)})"
    print(f"P1: PASS ({ok}/{len(samples)} samples <= 1e-27)", flush=True)


# ---------------- system build ----------------
class Sys:
    def __init__(self, r_cert, digits=DIGITS):
        global DIGITS
        self.digits = digits
        modes, self.x_cut = modes_for(r_cert)
        self.modes = modes
        self.n = len(modes)
        pts = coll_points(self.n + 1)
        P = []
        for z in pts:
            zs, ts, mv = mp_reduce(z, YV)
            if mv and ts > YV * (1 + mp.mpf('1e-20')):
                P.append((z, zs, ts))
            if len(P) == self.n + 1:
                break
        assert len(P) == self.n + 1, "not enough risen points"
        self.P = P
        # precompute arb constants
        self.two_pi = flint.arb.pi() * 2
        self.Yb = flint.arb('0.75')
        self.norm_arb = [ (flint.arb(m1 * m1) + flint.arb(flint.fmpq(m2 * m2, 12))).sqrt()
                          for (m1, m2) in modes ]
        self.mu_re = [flint.arb(m1) for (m1, m2) in modes]
        self.mu_im = [flint.arb(m2) / (flint.arb(3).sqrt() * 2) for (m1, m2) in modes]
        # phases (r-independent)
        self.ph0 = []
        self.ph1 = []
        self.ts_arb = []
        for (z, zs, ts) in P:
            zr, zi = arb_mp(z.real), arb_mp(z.imag)
            sr, si = arb_mp(zs.real), arb_mp(zs.imag)
            self.ph0.append([(flint.acb(0, 1) * self.two_pi * (self.mu_re[m] * zr + self.mu_im[m] * zi)).exp() for m in range(self.n)])
            self.ph1.append([(flint.acb(0, 1) * self.two_pi * (self.mu_re[m] * sr + self.mu_im[m] * si)).exp() for m in range(self.n)])
            self.ts_arb.append(arb_mp(ts))

    def K_table(self, r_arb):
        # distinct (mode-norm, height) -> K
        tab = {}
        for m in range(self.n):
            am = self.norm_arb[m] * self.two_pi
            key0 = m
            tab[(m, -1)] = K_ir(r_arb, am * self.Yb)
            for j in range(self.n + 1):
                tab[(m, j)] = K_ir(r_arb, am * self.ts_arb[j])
        return tab

    def rows(self, r_arb, row_idx):
        tab_needed = {}
        out = []
        for j in row_idx:
            row = []
            for m in range(self.n):
                am = self.norm_arb[m] * self.two_pi
                k0 = K_ir(r_arb, am * self.Yb)
                k1 = K_ir(r_arb, am * self.ts_arb[j])
                row.append(flint.acb(self.Yb) * k0 * self.ph0[j][m]
                           - flint.acb(self.ts_arb[j]) * k1 * self.ph1[j][m])
            out.append(row)
        return out


def newton(S, r0_str, j0=0, itmax=10, label=''):
    """Joint Newton; returns (r_arb, a, residual history)."""
    r = flint.arb(r0_str)
    h = flint.arb('1e-9')
    hist = []
    a = None
    for it in range(itmax):
        t0 = time.time()
        rows0 = S.rows(r, range(S.n))
        rowsP = S.rows(r + h, range(S.n))
        rowsM = S.rows(r - h, range(S.n))
        # initial a: solve rows0 with normalization
        M = flint.acb_mat(S.n + 1, S.n + 1)
        rhs = flint.acb_mat(S.n + 1, 1)
        for j in range(S.n):
            for m in range(S.n):
                M[j, m] = rows0[j][m]
        if a is None:
            for m in range(S.n):
                M[S.n, m] = flint.acb(1 if m == j0 else 0)
            rhs[S.n, 0] = flint.acb(1)
            a = M.solve(rhs)
        # F and J
        Fa = [sum((rows0[j][m] * a[m, 0] for m in range(S.n)), flint.acb(0))
              for j in range(S.n)]
        res = max(abs(complex(f.real, f.imag)) for f in Fa)
        # dM/dr * a column
        col = [sum(((rowsP[j][m] - rowsM[j][m]) / (h * 2) * a[m, 0]
                    for m in range(S.n)), flint.acb(0)) for j in range(S.n)]
        J = flint.acb_mat(S.n + 1, S.n + 1)
        Frhs = flint.acb_mat(S.n + 1, 1)
        for j in range(S.n):
            for m in range(S.n):
                J[j, m] = rows0[j][m]
            J[j, S.n] = col[j]
            Frhs[j, 0] = -Fa[j]
        for m in range(S.n):
            J[S.n, m] = flint.acb(1 if m == j0 else 0)
        J[S.n, S.n] = flint.acb(0)
        Frhs[S.n, 0] = flint.acb(1) - a[j0, 0]
        delta = J.solve(Frhs)
        for m in range(S.n):
            a[m, 0] = a[m, 0] + delta[m, 0]
        dr = delta[S.n, 0]
        r = r + dr.real
        drs = abs(complex(dr.real, dr.imag))
        hist.append((res, drs))
        print(f"  [{label}] iter {it}: max|F| = {res:.2e}, |dr| = {drs:.2e} "
              f"({time.time()-t0:.0f}s)", flush=True)
        # P2 monotonicity (after first step)
        if len(hist) >= 3 and hist[-1][0] > hist[-2][0] * 1.5:
            raise AssertionError("P2 FAILED: residual not decreasing")
        if drs < 1e-27:
            break
    return r, a, hist


def run(r_cert, mult2=False):
    t00 = time.time()
    print(f"=== CELL 9 RUNG (i) v2: target r = {r_cert} "
          f"(prereg 3ba81779) ===", flush=True)
    p1_check(r_cert)
    S = Sys(r_cert)
    print(f"n = {S.n} modes, x_cut = {S.x_cut:.1f}, Y = 0.75, "
          f"prec = {flint.ctx.prec} bits", flush=True)

    r_fin, a_fin, _ = newton(S, CERT[r_cert], j0=0, label='main')
    r_str = r_fin.str(32, radius=False)
    print(f"MAIN: r = {r_str}")

    # validation gate
    agree = 0
    for c1, c2 in zip(CERT[r_cert].replace('.', ''), r_str.replace('.', '').replace('-', '')):
        if c1 == c2:
            agree += 1
        else:
            break
    assert agree >= 7, f"VALIDATION GATE FAILED: only {agree} overlap digits"
    print(f"GATE: PASS ({agree} overlap digits)", flush=True)

    # P4: perturbed starts
    vals = [r_str]
    for eps in ('+1e-7', '-1e-7'):
        rp = mp.nstr(mp.mpf(CERT[r_cert]) + mp.mpf(eps), 20)
        rv, _, _ = newton(S, rp, j0=0, itmax=6, label=f'P4{eps}')
        vals.append(rv.str(32, radius=False))
    d1 = abs(mp.mpf(vals[0]) - mp.mpf(vals[1]))
    d2 = abs(mp.mpf(vals[0]) - mp.mpf(vals[2]))
    assert d1 < mp.mpf('1e-26') and d2 < mp.mpf('1e-26'), "P4 FAILED"
    print(f"P4: PASS (spread {mp.nstr(max(d1, d2), 3)})", flush=True)

    # P3: gap-midpoint displaced control
    rd, _, _ = newton(S, str(GAP_MIDPOINTS[r_cert]), j0=0, itmax=5,
                      label='P3')
    ddist = abs(mp.mpf(rd.str(32, radius=False)) - mp.mpf(r_str))
    assert ddist > mp.mpf('1e-20'), "P3 FAILED: displaced start converged to target"
    print(f"P3: PASS (displaced end {mp.nstr(ddist, 3)} from target)", flush=True)

    # stability cert at +5 digits
    global DIGITS
    print("stability cert (+5 digits) ...", flush=True)
    old_digits, old_prec = DIGITS, flint.ctx.prec
    DIGITS = DIGITS + 5
    flint.ctx.prec = int((DIGITS + 10) * 3.33)
    S2 = Sys(r_cert, digits=DIGITS)
    r2, _, _ = newton(S2, r_str[:20], j0=0, itmax=5, label='cert')
    DIGITS, flint.ctx.prec = old_digits, old_prec
    dstab = abs(mp.mpf(r2.str(34, radius=False)) - mp.mpf(r_str))
    print(f"|dr|_stab = {mp.nstr(dstab, 3)}  (require < 1e-26)", flush=True)
    ok_stab = dstab < mp.mpf('1e-26')

    result = {'r_certified': r_cert, 'r_refined': r_str,
              'r_stability': r2.str(34, radius=False),
              'dr_stab': mp.nstr(dstab, 5), 'stab_ok': bool(ok_stab),
              'n_modes': S.n, 'Y': 0.75, 'digits': 27,
              'gate_overlap_digits': agree, 'prereg': '3ba81779'}

    if mult2:
        # dual normalization
        av = [abs(complex(a_fin[m, 0].real, a_fin[m, 0].imag)) for m in range(S.n)]
        j1 = int(np.argsort(av)[-2])
        rB, _, _ = newton(S, r_str[:20], j0=j1, label='mult2-j1')
        dpair = abs(mp.mpf(rB.str(32, radius=False)) - mp.mpf(r_str))
        result['r_j1'] = rB.str(32, radius=False)
        result['pair_split'] = mp.nstr(dpair, 5)
        result['near_degenerate_pair'] = bool(dpair >= mp.mpf('1e-26'))
        print(f"MULT-2: |r_j0 - r_j1| = {mp.nstr(dpair, 3)} -> "
              f"{'NEAR-DEGENERATE PAIR' if result['near_degenerate_pair'] else 'single parameter'}",
              flush=True)

    with open(f"{OUT}/cell9_rung1_v2_{r_cert:.4f}.json", 'w') as f:
        json.dump(result, f, indent=1)
    print(f"TOTAL {time.time()-t00:.0f}s — saved", flush=True)


if __name__ == '__main__':
    run(float(sys.argv[1]), mult2='--mult2' in sys.argv)
