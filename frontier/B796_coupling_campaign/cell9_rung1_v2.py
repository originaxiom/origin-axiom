r"""CELL 9 RUNG (i) — conformant to sealed prereg v3 (169e9042).

Usage:  python cell9_rung1_v2.py <r_certified> [--mult2]

Sealed method v3: Y = 0.75; DAMPED BRACKETED SECANT on the held-out
row residual g(r) with the regular n x n normalized solve; P1 (10
decimal-string samples vs mpmath dps 60, <= 1e-27); P2 strict from
iteration 2; P3 gap-midpoint with divergence/abort = PASS; P4 three
starts >= 26 digits; gate >= 7 overlap digits; stability cert +5
digits. lam_1 (mult 2) is DEFERRED to rung (i-b) per v3 D-3 and is
REFUSED by this script. PSLQ in a separate sealed stage.

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
flint.ctx.prec = int((DIGITS + 45) * 3.33)  # +45 guard digits: arb LU ball growth near the (by-design) nearly singular M(r)
mp.mp.dps = 40
YV = mp.mpf('0.75')
OUT = 'frontier/B796_coupling_campaign'
SQ3 = mp.sqrt(3)
TAU = 2 * SQ3 * mp.mpc(0, 1)

SHAKEDOWN = False
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
    # all (r, x) as DECIMAL STRINGS so both sides evaluate at the SAME
    # point (float literals like 3.3 differ from decimal 3.3 by ~4e-17
    # in binary — the shakedown caught exactly that)
    rs = mp.nstr(mp.mpf(str(r_cert)), 20)
    r07 = mp.nstr(mp.mpf(str(r_cert)) * mp.mpf('0.7'), 20)
    r13 = mp.nstr(mp.mpf(str(r_cert)) * mp.mpf('1.3'), 20)
    samples = [(rs, x) for x in ('1.5', '2.0', '3.3', '5.5', '7.0',
                                 '9.0', '11.0', '13.0')]
    samples += [(r07, '4.0'), (r13, '6.0')]
    for (rv, xv) in samples:
        with mp.workdps(60):  # reference must out-precision the 1e-27 bar
            ref = mp.re(mp.besselk(1j * mp.mpf(rv), mp.mpf(xv)))
            fv = K_ir(flint.arb(rv), flint.arb(xv))
            fv_mp = mp.mpf(fv.real.str(40, radius=False))
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
        # k0 cache: the height-Y Bessel factor is row-independent.
        # COLUMN EQUILIBRATION (exact): each column is divided by its
        # Y-term magnitude |Y*K(2pi|mu|Y)| — g's root is invariant
        # under column scaling (M D)(D^-1 a) = e keeps g = row_n a
        # unchanged — and the truncation-edge dynamic range (~1e-19 at
        # shakedown, ~1e-32 at the real run) collapses to O(1),
        # which arb's certified LU requires at n >~ 1300.
        k0c = [K_ir(r_arb, self.norm_arb[m] * self.two_pi * self.Yb)
               for m in range(self.n)]
        scale = [(flint.acb(self.Yb) * k0c[m]).abs_lower()
                 for m in range(self.n)]
        out = []
        for j in row_idx:
            row = []
            for m in range(self.n):
                k1 = K_ir(r_arb, self.norm_arb[m] * self.two_pi
                          * self.ts_arb[j])
                e = (flint.acb(self.Yb) * k0c[m] * self.ph0[j][m]
                     - flint.acb(self.ts_arb[j]) * k1 * self.ph1[j][m])
                row.append(e / scale[m])
            out.append(row)
        return out


def newton(S, r0_str, j0=0, itmax=14, label='', check_norm=False):
    """METHOD v2.1 (amendment filed for Sec-16): scalar SECANT on the
    held-out-row residual g(r) = row_{n-1}(r) . a(r), where a(r) solves
    the REGULAR n x n system [rows 0..n-2; normalization e_j0] = e_n.
    The n x n matrix stays invertible AT the eigenvalue (the
    normalization row replaces the deficient direction), avoiding the
    bordered-Newton arb-certification failure at the root. Secant
    converges superlinearly; P2 monotonicity applies to |g|."""
    def g_of(r_arb):
        pass_marker = None
        rows0 = S.rows(r_arb, range(S.n))
        M0 = flint.acb_mat(S.n, S.n)
        rhs0 = flint.acb_mat(S.n, 1)
        for j in range(S.n - 1):
            for m in range(S.n):
                M0[j, m] = rows0[j][m]
        for m in range(S.n):
            M0[S.n - 1, m] = flint.acb(1 if m == j0 else 0)
        rhs0[S.n - 1, 0] = flint.acb(1)
        a = M0.solve(rhs0)
        # j0-validation bound: fires ONLY on the main run's first solve
        # (validating j0 is a per-target static property; the statistic
        # is legitimately volatile across r — 4.2e6 at the root vs
        # 6.7e9 at a 1e-7-perturbed start at digits-14). The
        # symmetry-zero pathology it catches sits at ~1e12+.
        if check_norm and not g_of.checked:
            amax = max(abs(complex(a[m, 0].real, a[m, 0].imag))
                       for m in range(0, S.n, max(1, S.n // 200)))
            g_of.checked = True
            assert amax < 1e9, (
                f"NORMALIZATION SUSPECT: ||a||_inf ~ {amax:.1e} with "
                f"a[j0] = 1 — choose a different j0")
            print(f"  [j0-check] ||a||_inf = {amax:.1e} (< 1e9) OK",
                  flush=True)
        gval = sum((rows0[S.n - 1][m] * a[m, 0] for m in range(S.n)),
                   flint.acb(0))
        return gval, a

    g_of.checked = False
    r_center = mp.mpf(r0_str)
    BR = mp.mpf('0.01')          # hard bracket [D-1]
    CAP = 1e-3                   # step damping [D-1]
    r0 = flint.arb(r0_str)
    r1 = r0 + flint.arb('1e-9')
    g0, a0 = g_of(r0)
    hist = [abs(complex(g0.real, g0.imag))]
    a_last, r_last = a0, r0
    for it in range(itmax):
        t0 = time.time()
        g1, a1 = g_of(r1)
        gm0 = complex(g0.real, g0.imag)
        gm1 = complex(g1.real, g1.imag)
        if gm1 == gm0:
            break
        dr_c = gm1 * (float((r1 - r0).mid())) / (gm1 - gm0)
        if abs(dr_c) > CAP:      # damping
            dr_c = dr_c / abs(dr_c) * CAP
            print(f"  [{label}] step capped at {CAP}", flush=True)
        r2 = r1 - flint.arb(repr(dr_c.real))
        # hard bracket
        if abs(mp.mpf(r2.str(25, radius=False)) - r_center) > BR:
            raise AssertionError(
                f"BRACKET EXIT: iterate left [center +- {BR}] — basin "
                f"escape, run aborted (logged)")
        drs = abs(dr_c)
        hist.append(abs(gm1))
        dt_it = time.time() - t0
        print(f"  [{label}] iter {it}: |g| = {abs(gm1):.2e}, "
              f"|dr| = {drs:.2e} ({dt_it:.0f}s)", flush=True)
        if it == 0 and dt_it > 1500:
            print(f"  [{label}] C8 CHECKPOINT: iteration > 25 min — the "
                  f"4-8 h/eigenvalue estimate must be revised before the "
                  f"second target", flush=True)
        # strict P2 from iteration 2 [D-1]
        if it >= 2 and hist[-1] >= hist[-2]:
            raise AssertionError("P2 FAILED: |g| non-decreasing")
        r0, g0 = r1, g1
        r1 = r2
        a_last, r_last = a1, r1
        conv = 1e-13 if SHAKEDOWN else 1e-27
        if drs < conv:
            break
    return r_last, a_last, hist


def run(r_cert, mult2=False):
    assert abs(r_cert - 3.938916864) > 1e-6, (
        "lam_1 (mult 2) is DEFERRED to rung (i-b) per sealed v3 D-3 — "
        "refused")
    assert not mult2, (
        "--mult2 pair protocol is the superseded v2 procedure; deferred "
        "to rung (i-b)")
    t00 = time.time()
    print(f"=== CELL 9 RUNG (i) v2: target r = {r_cert} "
          f"(prereg v3 169e9042) ===", flush=True)
    p1_check(r_cert)
    S = Sys(r_cert)
    print(f"n = {S.n} modes, x_cut = {S.x_cut:.1f}, Y = 0.75, "
          f"prec = {flint.ctx.prec} bits", flush=True)

    # C8 v2 (data-driven, after the symmetry-zero abort): normalization
    # mode = the LARGEST-|a| mode of the certified double-precision
    # eigenvector (the lowest-|mu| mode (0,1) is an exact symmetry zero
    # for these forms — they live on the even-m2 sublattice).
    J0_MODE = {4.900085373: (0, 2), 7.072004187: (0, 4)}
    tgt = J0_MODE[r_cert]
    j0_low = S.modes.index(tgt)
    print(f"normalization mode j0 = {j0_low} = mode {tgt} "
          f"(certified max-|a| mode)", flush=True)
    r_fin, a_fin, _ = newton(S, CERT[r_cert], j0=j0_low, label='main',
                             check_norm=True)
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
        rv, _, _ = newton(S, rp, j0=j0_low, itmax=6, label=f'P4{eps}')
        vals.append(rv.str(32, radius=False))
    d1 = abs(mp.mpf(vals[0]) - mp.mpf(vals[1]))
    d2 = abs(mp.mpf(vals[0]) - mp.mpf(vals[2]))
    p4bar = mp.mpf('1e-12') if SHAKEDOWN else mp.mpf('1e-26')
    assert d1 < p4bar and d2 < p4bar, "P4 FAILED"
    print(f"P4: PASS (spread {mp.nstr(max(d1, d2), 3)})", flush=True)

    # P3: gap-midpoint displaced control [D-2: divergence/abort = PASS]
    try:
        rd, _, _ = newton(S, str(GAP_MIDPOINTS[r_cert]), j0=j0_low,
                          itmax=5, label='P3')
        ddist = abs(mp.mpf(rd.str(32, radius=False)) - mp.mpf(r_str))
        assert ddist > mp.mpf('1e-20'), \
            "P3 FAILED: displaced start converged to target"
        print(f"P3: PASS (displaced end {mp.nstr(ddist, 3)} from target)",
              flush=True)
    except AssertionError as e:
        if 'P3 FAILED' in str(e):
            raise
        print(f"P3: PASS (displaced run aborted cleanly: {e})", flush=True)
    except ZeroDivisionError:
        print("P3: PASS (displaced run: singular solve = no false root)",
              flush=True)

    # stability cert at +5 digits
    global DIGITS
    print("stability cert (+5 digits) ...", flush=True)
    old_digits, old_prec = DIGITS, flint.ctx.prec
    DIGITS = DIGITS + 5
    flint.ctx.prec = int((DIGITS + 45) * 3.33)  # +45 guard digits: arb LU ball growth near the (by-design) nearly singular M(r)
    S2 = Sys(r_cert, digits=DIGITS)
    j0b = S2.modes.index(tgt)  # same data-driven mode as the main run
    r2, _, _ = newton(S2, r_str[:20], j0=j0b, itmax=5, label='cert')
    DIGITS, flint.ctx.prec = old_digits, old_prec
    dstab = abs(mp.mpf(r2.str(34, radius=False)) - mp.mpf(r_str))
    stab_bar = mp.mpf('1e-11') if SHAKEDOWN else mp.mpf('1e-26')
    print(f"|dr|_stab = {mp.nstr(dstab, 3)}  (require < {stab_bar})", flush=True)
    ok_stab = dstab < stab_bar

    result = {'r_certified': r_cert, 'r_refined': r_str,
              'r_stability': r2.str(34, radius=False),
              'dr_stab': mp.nstr(dstab, 5), 'stab_ok': bool(ok_stab),
              'n_modes': S.n, 'Y': 0.75, 'digits': 27,
              'gate_overlap_digits': agree, 'prereg': '169e9042'}

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

    result['shakedown'] = bool(SHAKEDOWN)
    result['digits_actual'] = DIGITS
    tag = '_SHAKEDOWN' if SHAKEDOWN else ''
    with open(f"{OUT}/cell9_rung1_v3_{r_cert:.4f}{tag}.json", 'w') as f:
        json.dump(result, f, indent=1)
    print(f"TOTAL {time.time()-t00:.0f}s — saved", flush=True)



def enable_shakedown():
    """Mini-instance: digits=14, thresholds scaled. Output labeled
    SHAKEDOWN — exercises the full pipeline; results NEVER bankable."""
    global DIGITS, SHAKEDOWN
    DIGITS = 14
    flint.ctx.prec = int((DIGITS + 45) * 3.33)
    SHAKEDOWN = True
    print("### SHAKEDOWN MODE: digits=14, thresholds scaled, "
          "results not bankable ###", flush=True)


if __name__ == '__main__':
    if '--shakedown' in sys.argv:
        enable_shakedown()
    run(float(sys.argv[1]), mult2='--mult2' in sys.argv)
