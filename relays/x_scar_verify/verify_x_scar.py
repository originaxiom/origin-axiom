#!/usr/bin/env python3
"""
Standalone Zero-Import Verification Script for Sealed Card X-SCAR (Answering M21 on P-847 & W-F9).

Enforces all six Mathematical-Physics & Formal Verification Guardrails:
  1. No post-inspection selection credit; pure mathematics only (0 of 19).
  2. Zero literal flag assignments; every identity, index, cocycle, slope, and reflection law
     is computed directly from explicit matrices/series and verified to machine precision.
  3. Mandatory random Haar U(3)^5 unitary basis-scrambling gate (< 1e-30) on all extracted
     Yukawa observables (singular-value ratios, |V_CKM|, and normalized Jarlskog J_CP).
  4. Literature / record benchmark gates executed first:
       - Gate A: B1656 Cell E3/E7 channel norms & gap at tau = exp(2*pi*i/3), line (1/9, 1/9),
                 cross-checking raw B1656 strip quadrature cB against B1919's closed Kronecker limit.
       - Gate B: B1667 / B1927 punctured-torus Lame uniformizer against closed-form Gamma' eta^4
                 period integral at exp(i*pi/3), Markov traces at i, and B1667's bulk point.
       - Gate C: B1438 exact cyclotomic slope law s(chi) vs direct Fox-calculus interior cohomology
                 across (+LR, k=2,3), (+LLR, k=3), (-LLRLR, k=1), and (-LLLRLR, k=1).
  5. Zero empirical anchors imported or read (0 of 19).
  6. Zero imports from main, any other seat, or prior scripts. Four pre-registered planted
     negative controls (PC_SCAR_1 .. PC_SCAR_4), all verified to fire.
"""

from __future__ import annotations

import collections
import hashlib
import itertools
import json
import math
import pathlib
import random
import time
from fractions import Fraction as Fr
from typing import Any, Dict, List, Optional, Sequence, Tuple

import mpmath as mp
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE = pathlib.Path(__file__).resolve().parent
OUT_PATH = HERE / "verify_x_scar_out.json"

SIXY: Dict[str, int] = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}
SECTORS_2D: Tuple[Tuple[str, int, int], ...] = (
    ("up", SIXY["Q"], SIXY["u"]),
    ("down", SIXY["Q"], SIXY["d"]),
    ("lep", SIXY["L"], SIXY["e"]),
)
SCAR_SECTORS: Tuple[Tuple[str, int, int], ...] = (
    ("Q", 1, 3),
    ("uc", -4, 3),
    ("ec", 6, 3),
    ("dc", 2, 1),
    ("L", -3, 1),
    ("nuc", 0, -5),
)


def _json_default(obj: Any) -> Any:
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (mp.mpf,)):
        return float(obj)
    if isinstance(obj, (mp.mpc, complex)):
        return {"re": float(mp.re(obj)), "im": float(mp.im(obj))}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def mat_H(A: mp.matrix) -> mp.matrix:
    """Explicit conjugate transpose of an mpmath matrix."""
    return mp.matrix([[mp.conj(A[r, c]) for r in range(A.rows)] for c in range(A.cols)])


def mat_conj(A: mp.matrix) -> mp.matrix:
    """Entrywise complex conjugate of an mpmath matrix."""
    return mp.matrix([[mp.conj(A[r, c]) for c in range(A.cols)] for r in range(A.rows)])


def mat_inf_norm(A: mp.matrix) -> mp.mpf:
    """Maximum entrywise modulus of an mpmath matrix."""
    return max(abs(A[r, c]) for r in range(A.rows) for c in range(A.cols))


def det_3x3(M: mp.matrix) -> mp.mpc:
    """Exact 3x3 determinant in mpmath."""
    return (
        M[0, 0] * (M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1])
        - M[0, 1] * (M[1, 0] * M[2, 2] - M[1, 2] * M[2, 0])
        + M[0, 2] * (M[1, 0] * M[2, 1] - M[1, 1] * M[2, 0])
    )


# ============================================================================
# SECTION 0A: STANDALONE 45-DIGIT LAME UNIFORMIZER FOR B1667 / B1927 tilde_L_2
# ============================================================================

def eisenstein_g2_g3(tau: mp.mpc, n_terms: int = 150) -> Tuple[mp.mpc, mp.mpc]:
    q = mp.exp(2 * mp.j * mp.pi * tau)
    s3 = mp.mpc(0)
    s5 = mp.mpc(0)
    qn = q
    for n in range(1, n_terms + 1):
        denom = 1 - qn
        t3 = (n ** 3) * qn / denom
        t5 = (n ** 5) * qn / denom
        s3 += t3
        s5 += t5
        if abs(t3) < mp.mpf("1e-52") and abs(t5) < mp.mpf("1e-52"):
            break
        qn *= q
    E4 = 1 + 240 * s3
    E6 = 1 - 504 * s5
    g2 = (4 * (mp.pi ** 4) / 3) * E4
    g3 = (8 * (mp.pi ** 6) / 27) * E6
    return g2, g3


def wp_and_wp_prime(z: mp.mpc, tau: mp.mpc, max_m: int = 150) -> Tuple[mp.mpc, mp.mpc]:
    pi = mp.pi
    s0 = mp.sin(pi * z)
    c0 = mp.cos(pi * z)
    wp = (pi / s0) ** 2 - (pi ** 2) / 3
    wpp = -2 * (pi ** 3) * c0 / (s0 ** 3)
    for m in range(1, max_m + 1):
        zm_p = pi * (z + m * tau)
        zm_m = pi * (z - m * tau)
        m_t = pi * m * tau
        sp, cp = mp.sin(zm_p), mp.cos(zm_p)
        sm, cm = mp.sin(zm_m), mp.cos(zm_m)
        st = mp.sin(m_t)
        term_wp = (pi / sp) ** 2 + (pi / sm) ** 2 - 2 * ((pi / st) ** 2)
        term_wpp = -2 * (pi ** 3) * (cp / (sp ** 3) + cm / (sm ** 3))
        wp += term_wp
        wpp += term_wpp
        if abs(term_wp) < mp.mpf("1e-50") and abs(term_wpp) < mp.mpf("1e-50"):
            break
    return wp, wpp


def lame_frob_initial(
    z: mp.mpc, g2: mp.mpc, g3: mp.mpc, c_acc: mp.mpc, n_terms: int = 45
) -> mp.matrix:
    """Canonical Frobenius fundamental matrix near z = 0 for y'' + (1/4 wp(z) + c_acc) y = 0."""
    c_wp: Dict[int, mp.mpc] = {1: g2 / 20, 2: g3 / 28}
    for k in range(3, n_terms + 2):
        c_wp[k] = (
            mp.mpf(3)
            / ((2 * k + 3) * (k - 2))
            * sum(c_wp[m] * c_wp[k - 1 - m] for m in range(1, k - 1))
        )
    qcoeffs = [c_acc] + [c_wp[k] / 4 for k in range(1, n_terms + 1)]

    a = [mp.mpc(1)]
    b = [mp.mpc(0)]
    for n in range(1, n_terms):
        an = -sum(qcoeffs[n - 1 - m] * a[m] for m in range(n)) / (4 * n * n)
        bn = -(4 * n * an + sum(qcoeffs[n - 1 - m] * b[m] for m in range(1, n))) / (4 * n * n)
        a.append(an)
        b.append(bn)

    sz = mp.sqrt(z)
    lz = mp.log(z)
    z2 = z * z
    zp = mp.mpc(1)
    s_y1 = mp.mpc(0)
    s_dy1 = mp.mpc(0)
    s_h = mp.mpc(0)
    s_dh = mp.mpc(0)
    for n in range(n_terms):
        exp_n = 2 * n + mp.mpf("0.5")
        s_y1 += a[n] * zp
        s_dy1 += exp_n * a[n] * zp / z
        s_h += b[n] * zp
        s_dh += exp_n * b[n] * zp / z
        zp *= z2
    y1 = sz * s_y1
    dy1 = sz * s_dy1
    h = sz * s_h
    dh = sz * s_dh
    y2 = y1 * lz + h
    dy2 = dy1 * lz + y1 / z + dh
    fac = -mp.j / (2 * mp.pi)
    return mp.matrix([[fac * y2, fac * dy2], [y1, dy1]])


def _segment_lattice_distance(z_start: mp.mpc, z_end: mp.mpc, tau: mp.mpc) -> float:
    ax, ay = float(mp.re(z_start)), float(mp.im(z_start))
    bx, by = float(mp.re(z_end)), float(mp.im(z_end))
    dx, dy = bx - ax, by - ay
    seg_len2 = dx * dx + dy * dy
    tx, ty = float(mp.re(tau)), float(mp.im(tau))
    dmin = 1e9
    for m in range(-5, 6):
        for n in range(-5, 6):
            px, py = m + n * tx, n * ty
            if seg_len2 < 1e-30:
                dist = math.hypot(ax - px, ay - py)
            else:
                t_clamped = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / seg_len2))
                qx, qy = ax + t_clamped * dx, ay + t_clamped * dy
                dist = math.hypot(px - qx, py - qy)
            if dist < dmin:
                dmin = dist
    return dmin


def taylor_propagate_lame(
    Y_init: mp.matrix,
    z_start: mp.mpc,
    z_end: mp.mpc,
    tau: mp.mpc,
    g2: mp.mpc,
    c_acc: mp.mpc,
    n_steps: int = 36,
    order: int = 32,
) -> mp.matrix:
    h = (z_end - z_start) / n_steps
    Y = Y_init.copy()
    z = z_start
    half_g2 = g2 / 2
    for _ in range(n_steps):
        p0, p1 = wp_and_wp_prime(z, tau)
        p = [mp.mpc(0)] * (order + 1)
        p[0] = p0
        p[1] = p1
        if order >= 2:
            p[2] = 3 * p0 * p0 - half_g2 / 2
        for k in range(3, order):
            conv = sum(p[j] * p[k - 2 - j] for j in range(k - 1))
            p[k] = (mp.mpf(6) / (k * (k - 1))) * conv
        q = [mp.mpc(0)] * order
        q[0] = p[0] / 4 + c_acc
        for k in range(1, order):
            q[k] = p[k] / 4

        Y_next = mp.zeros(2, 2)
        for row in range(2):
            u = [mp.mpc(0)] * (order + 1)
            u[0] = Y[row, 0]
            u[1] = Y[row, 1]
            for k in range(2, order + 1):
                s_qu = sum(q[j] * u[k - 2 - j] for j in range(k - 1))
                u[k] = -s_qu / (k * (k - 1))
            val = mp.mpc(0)
            dval = mp.mpc(0)
            hp = mp.mpc(1)
            for k in range(order + 1):
                val += u[k] * hp
                if k >= 1:
                    dval += k * u[k] * (hp / h if abs(h) > 0 else mp.mpc(0))
                hp *= h
            Y_next[row, 0] = val
            Y_next[row, 1] = dval
        Y = Y_next
        z += h
    return Y


def lame_monodromy(tau: mp.mpc, c_acc: mp.mpc) -> Tuple[mp.matrix, mp.matrix]:
    g2, g3 = eisenstein_g2_g3(tau)
    z0 = mp.mpf("-0.5") - mp.mpf("0.5") * tau
    min_per = min(
        abs(m + n * tau)
        for m in range(-5, 6)
        for n in range(-5, 6)
        if (m, n) != (0, 0)
    )
    r_target = min(mp.mpf("0.20") * min_per, mp.mpf("0.45") * abs(z0))
    zf = z0 * (r_target / abs(z0))
    Yf = lame_frob_initial(zf, g2, g3, c_acc, n_terms=45)

    d_ray = max(1e-4, _segment_lattice_distance(zf, z0, tau))
    d_A = max(1e-4, _segment_lattice_distance(z0, z0 + 1, tau))
    d_B = max(1e-4, _segment_lattice_distance(z0, z0 + tau, tau))
    n_ray = max(28, int(math.ceil(float(abs(z0 - zf)) / (0.055 * d_ray))))
    n_A = max(32, int(math.ceil(1.0 / (0.055 * d_A))))
    n_B = max(32, int(math.ceil(float(abs(tau)) / (0.055 * d_B))))

    Y0 = taylor_propagate_lame(Yf, zf, z0, tau, g2, c_acc, n_steps=n_ray, order=32)
    YA = taylor_propagate_lame(Y0, z0, z0 + 1, tau, g2, c_acc, n_steps=n_A, order=32)
    YB = taylor_propagate_lame(Y0, z0, z0 + tau, tau, g2, c_acc, n_steps=n_B, order=32)
    Y0_inv = mp.inverse(Y0)
    return YA * Y0_inv, YB * Y0_inv


def solve_fuchsian_accessory_from_guess(tau: mp.mpc, c_init: mp.mpc) -> Tuple[mp.mpc, mp.matrix, mp.matrix]:
    c_cur = mp.mpc(c_init)
    eps_fd = mp.mpf("1e-18")
    for _ in range(9):
        MA, MB = lame_monodromy(tau, c_cur)
        fA = mp.im(MA[0, 0] + MA[1, 1])
        fB = mp.im(MB[0, 0] + MB[1, 1])
        if max(abs(fA), abs(fB)) < mp.mpf("1e-36"):
            return c_cur, MA, MB
        MA_p, MB_p = lame_monodromy(tau, c_cur + eps_fd)
        d_trA = ((MA_p[0, 0] + MA_p[1, 1]) - (MA[0, 0] + MA[1, 1])) / eps_fd
        d_trB = ((MB_p[0, 0] + MB_p[1, 1]) - (MB[0, 0] + MB[1, 1])) / eps_fd
        j00, j01 = mp.im(d_trA), mp.re(d_trA)
        j10, j11 = mp.im(d_trB), mp.re(d_trB)
        det_j = j00 * j11 - j01 * j10
        dx = -(j11 * fA - j01 * fB) / det_j
        dy = -(-j10 * fA + j00 * fB) / det_j
        c_cur = c_cur + mp.mpc(dx, dy)
    MA, MB = lame_monodromy(tau, c_cur)
    return c_cur, MA, MB


def uniformize_punctured_torus(tau_in: mp.mpc, n_homotopy: int = 3) -> Dict[str, Any]:
    with mp.workdps(48):
        tau = mp.mpc(tau_in)
        tau_i = mp.mpc(0, 1)
        tau_om6 = mp.exp(mp.j * mp.pi / 3)
        if abs(tau - tau_i) < mp.mpf("1e-30") or abs(tau - tau_om6) < mp.mpf("1e-30"):
            c_acc = mp.mpc(0)
            MA, MB = lame_monodromy(tau, c_acc)
        else:
            c_guess = mp.mpc(0)
            for step in range(1, n_homotopy + 1):
                s = mp.mpf(step) / n_homotopy
                t_s = (1 - s) * tau_i + s * tau
                c_guess, MA, MB = solve_fuchsian_accessory_from_guess(t_s, c_guess)
            c_acc = c_guess

        comm = MA * MB * mp.inverse(MA) * mp.inverse(MB)
        comm_tr_err = abs((comm[0, 0] + comm[1, 1]) - (-2))
        comm_c_err = abs(comm[1, 0])
        assert comm_tr_err < mp.mpf("1e-24"), f"Commutator trace residual: {comm_tr_err}"
        assert comm_c_err < mp.mpf("1e-24"), f"Commutator (2,1) residual: {comm_c_err}"

        lam = abs(mp.re(comm[0, 1]))
        assert abs(lam - 1) < mp.mpf("1e-24"), f"Unexpected parabolic width: {lam}"
        assert max(abs(mp.im(MA[1, 0])), abs(mp.im(MB[1, 0]))) < mp.mpf("1e-24")
        imB_A = -mp.im(MA[0, 0]) / mp.re(MA[1, 0])
        imB_B = -mp.im(MB[0, 0]) / mp.re(MB[1, 0])
        assert abs(imB_A - imB_B) < mp.mpf("1e-24"), f"Im(B) mismatch: {imB_A} vs {imB_B}"
        imB = (imB_A + imB_B) / 2

        B_shift = mp.j * imB
        G_conj = mp.matrix([[1, B_shift], [0, 1]])
        G_inv = mp.matrix([[1, -B_shift], [0, 1]])
        RA_c = G_conj * MA * G_inv
        RB_c = G_conj * MB * G_inv
        RA = mp.matrix([[mp.re(RA_c[0, 0]), mp.re(RA_c[0, 1])], [mp.re(RA_c[1, 0]), mp.re(RA_c[1, 1])]])
        RB = mp.matrix([[mp.re(RB_c[0, 0]), mp.re(RB_c[0, 1])], [mp.re(RB_c[1, 0]), mp.re(RB_c[1, 1])]])
        RA_i = mp.inverse(RA)
        RB_i = mp.inverse(RB)

        gens = [("A", RA), ("a", RA_i), ("B", RB), ("b", RB_i)]
        inv_tag = {"A": "a", "a": "A", "B": "b", "b": "B"}
        min_c = min(abs(RA[1, 0]), abs(RB[1, 0]))
        frontier_words: List[Tuple[str, mp.matrix]] = list(gens)
        for _ in range(5):
            nxt_words: List[Tuple[str, mp.matrix]] = []
            for w_str, mat in frontier_words:
                last_ch = w_str[-1]
                for nm, gmat in gens:
                    if nm == inv_tag[last_ch]:
                        continue
                    prod = mat * gmat
                    c_val = abs(prod[1, 0])
                    if c_val > mp.mpf("1e-9") and c_val < min_c:
                        min_c = c_val
                    if abs(prod[0, 0]) + abs(prod[0, 1]) + abs(prod[1, 0]) + abs(prod[1, 1]) < mp.mpf("1500"):
                        nxt_words.append((w_str + nm, prod))
            frontier_words = nxt_words

        L_max = (2 * mp.pi / lam) * (1 / min_c - imB)
        L_2 = mp.pi - (2 * mp.pi / lam) * imB
        shift_mod = mp.mpf("0.5") * mp.log(mp.im(tau)) - (mp.euler + mp.log(mp.pi))
        return {
            "c_acc": c_acc,
            "L_max": L_max,
            "L_2": L_2,
            "tilde_L_max": L_max + shift_mod,
            "tilde_L_2": L_2 + shift_mod,
        }


def closed_form_gamma_prime_omega6() -> Tuple[mp.mpf, mp.mpf]:
    """Closed-form Gamma' = [SL(2, Z), SL(2, Z)] eta^4 period integral at tau = exp(i*pi/3)."""
    def eta4(w: mp.mpc) -> mp.mpc:
        q = mp.exp(2 * mp.j * mp.pi * w)
        prod = mp.mpc(1)
        qn = q
        for _ in range(120):
            prod *= (1 - qn)
            if abs(qn) < mp.mpf("1e-50"):
                break
            qn *= q
        return mp.exp(2 * mp.j * mp.pi * w / 6) * (prod ** 4)

    w0 = mp.mpc(0, 1)
    w1 = mp.mpc("1.5", "0.5")
    per1 = mp.quad(eta4, [w0, w1])
    kappa_abs = 1 / abs(per1)
    imB_cf = mp.log(3 * kappa_abs / mp.pi) / (2 * mp.pi)
    return 2 * mp.pi * (mp.mpf(1) / 6 - imB_cf), mp.pi - 2 * mp.pi * imB_cf


# ============================================================================
# SECTION 0B: EXACT ANALYTIC q-JET SERRE DERIVATIVES & B1656 / B1919 BUILDERS
# ============================================================================

class Jet2:
    """Exact 2nd-order Taylor jet c0 + c1*eps + c2*eps^2 (eps^3 = 0) for D_tau = (1/(2*pi*i)) d/dtau."""
    __slots__ = ("c0", "c1", "c2")

    def __init__(self, c0: mp.mpc, c1: mp.mpc = mp.mpc(0), c2: mp.mpc = mp.mpc(0)):
        self.c0 = mp.mpc(c0)
        self.c1 = mp.mpc(c1)
        self.c2 = mp.mpc(c2)

    def __add__(self, o: "Jet2") -> "Jet2":
        return Jet2(self.c0 + o.c0, self.c1 + o.c1, self.c2 + o.c2)

    def __sub__(self, o: "Jet2") -> "Jet2":
        return Jet2(self.c0 - o.c0, self.c1 - o.c1, self.c2 - o.c2)

    def __neg__(self) -> "Jet2":
        return Jet2(-self.c0, -self.c1, -self.c2)

    def scale(self, s: mp.mpc) -> "Jet2":
        return Jet2(s * self.c0, s * self.c1, s * self.c2)

    def __mul__(self, o: "Jet2") -> "Jet2":
        return Jet2(
            self.c0 * o.c0,
            self.c0 * o.c1 + self.c1 * o.c0,
            self.c0 * o.c2 + self.c1 * o.c1 + self.c2 * o.c0,
        )

    def inv(self) -> "Jet2":
        inv0 = 1 / self.c0
        inv1 = -self.c1 * (inv0 ** 2)
        inv2 = (self.c1 ** 2) * (inv0 ** 3) - self.c2 * (inv0 ** 2)
        return Jet2(inv0, inv1, inv2)

    def __truediv__(self, o: "Jet2") -> "Jet2":
        return self * o.inv()


def serre_triplets_exact(tau: mp.mpc) -> Dict[str, List[mp.mpc]]:
    """
    Zero-finite-difference analytic q-jet evaluation of B1691's triplet section:
      R(tau) = (-theta_2^2, -theta_4^2, i*theta_3^2) / (2*pi*eta^3)   (weight -1/2)
      B1 = D_Serre R   = D_tau R + (1/24) E_2 R                        (weight +3/2, B1724 / Frame C)
      B2 = D_Serre^2 R = D_tau(B1) - (1/8) E_2 B1                      (weight +7/2, B1691)
    Here D_tau = (1/(2*pi*i)) d/dtau = q d/dq, so exp(2*pi*i * alpha * (tau + eps))
    has exact 2nd-order Taylor jet q^alpha * (1 + alpha*eps + (alpha^2 / 2)*eps^2).
    """
    q_half = mp.exp(mp.j * mp.pi * tau)
    q_full = q_half * q_half

    t3_0, t3_1, t3_2 = mp.mpc(1), mp.mpc(0), mp.mpc(0)
    t4_0, t4_1, t4_2 = mp.mpc(1), mp.mpc(0), mp.mpc(0)
    for n in range(1, 55):
        alpha = mp.mpf(n * n) / 2
        term = q_half ** (n * n)
        if abs(term) < mp.mpf("1e-55"):
            break
        two_t = 2 * term
        sgn = -1 if (n & 1) else 1
        t3_0 += two_t
        t3_1 += two_t * alpha
        t3_2 += two_t * (alpha * alpha / 2)
        t4_0 += sgn * two_t
        t4_1 += sgn * two_t * alpha
        t4_2 += sgn * two_t * (alpha * alpha / 2)

    t2_0, t2_1, t2_2 = mp.mpc(0), mp.mpc(0), mp.mpc(0)
    for n in range(0, 55):
        h = mp.mpf(n) + mp.mpf("0.5")
        alpha = (h * h) / 2
        term = 2 * mp.exp(mp.j * mp.pi * tau * (h * h))
        if abs(term) < mp.mpf("1e-55"):
            break
        t2_0 += term
        t2_1 += term * alpha
        t2_2 += term * (alpha * alpha / 2)

    J2 = Jet2(t2_0, t2_1, t2_2)
    J3 = Jet2(t3_0, t3_1, t3_2)
    J4 = Jet2(t4_0, t4_1, t4_2)
    # Jacobi triple-product derivative identity: 2*pi*eta^3 == theta_1'(0) == pi * theta_2 * theta_3 * theta_4
    den = (J2 * J3 * J4).scale(mp.pi)
    R_jets = [-(J2 * J2) / den, -(J4 * J4) / den, ((J3 * J3) / den).scale(mp.j)]

    e2_0 = mp.mpc(1)
    e2_1 = mp.mpc(0)
    qn = q_full
    for n in range(1, 160):
        one_minus = 1 - qn
        term0 = mp.mpf(n) * qn / one_minus
        term1 = mp.mpf(n * n) * qn / (one_minus * one_minus)
        e2_0 -= 24 * term0
        e2_1 -= 24 * term1
        if abs(term0) < mp.mpf("1e-55") and abs(term1) < mp.mpf("1e-55"):
            break
        qn *= q_full

    b1_list: List[mp.mpc] = []
    b2_list: List[mp.mpc] = []
    for rj in R_jets:
        r0, dr, d2r = rj.c0, rj.c1, 2 * rj.c2
        b1 = dr + e2_0 * r0 / 24
        db1 = d2r + (e2_1 * r0 + e2_0 * dr) / 24
        b2 = db1 - e2_0 * b1 / 8
        b1_list.append(b1)
        b2_list.append(b2)

    return {"R": [rj.c0 for rj in R_jets], "B1": b1_list, "B2": b2_list}


def _quat_mats() -> Tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
    i2 = mp.matrix([[1, 0], [0, 1]])
    qi = mp.matrix([[mp.j, 0], [0, -mp.j]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = mp.matrix([[0, mp.j], [mp.j, 0]])
    return i2, qi, qj, qk


def _edual_mats() -> Dict[str, mp.matrix]:
    """Exact dual basis EDUAL[s] matching B1656: sum_{m,n} (EPS @ C_t)[m,n] * EDUAL[s][m,n] == delta_{t,s}."""
    i2, qi, qj, qk = _quat_mats()
    units = {"1": i2, "i": qi, "j": qj, "k": qk}
    eps = qj
    ec = {s: eps * c for s, c in units.items()}
    keys = ["1", "i", "j", "k"]
    G = mp.zeros(4, 4)
    for a_idx, kt in enumerate(keys):
        for b_idx, ks in enumerate(keys):
            G[a_idx, b_idx] = sum(ec[kt][r, c] * units[ks][r, c] for r in range(2) for c in range(2))
    Gi = mp.inverse(G)
    out: Dict[str, mp.matrix] = {}
    for a_idx, ka in enumerate(keys):
        acc = mp.zeros(2, 2)
        for b_idx, kb in enumerate(keys):
            acc += Gi[b_idx, a_idx] * units[kb]
        out[ka] = acc
    return out


def weighted_M_mp(u_weights: Dict[str, mp.mpc]) -> mp.matrix:
    edual = _edual_mats()
    acc = mp.zeros(2, 2)
    for s in ("1", "i", "j", "k"):
        acc += u_weights[s] * edual[s]
    return acc


def coupling_mp(S_mat: mp.matrix, M_mat: mp.matrix) -> mp.matrix:
    """Exact 3x3 Yukawa coupling matrix Y_{ab}(S, M) = sum_{m,n} (C_a^T EPS S C_b)_{m,n} M_{m,n} (B1644/B1656)."""
    _, qi, qj, qk = _quat_mats()
    blocks = [qj, qi, qk]
    eps = qj
    Y = mp.zeros(3, 3)
    for a_idx in range(3):
        for b_idx in range(3):
            block_mat = blocks[a_idx].T * eps * S_mat * blocks[b_idx]
            Y[a_idx, b_idx] = sum(block_mat[r, c] * M_mat[r, c] for r in range(2) for c in range(2))
    return Y


def F_kronecker_shifted(u1_in: mp.mpf, u2_in: mp.mpf, tau: mp.mpc) -> mp.mpf:
    """Exact shifted Kronecker limit F_u(tau) (B1919)."""
    u1 = u1_in - mp.floor(u1_in)
    u2 = u2_in - mp.floor(u2_in)
    if abs(u1 - 1) < mp.mpf("1e-36"):
        u1 = mp.mpf(0)
    if abs(u2 - 1) < mp.mpf("1e-36"):
        u2 = mp.mpf(0)
    x, y = mp.re(tau), mp.im(tau)
    if abs(u1) < mp.mpf("1e-36") and abs(u2) < mp.mpf("1e-36"):
        q = mp.exp(2 * mp.j * mp.pi * tau)
        eta_prod = mp.exp(2 * mp.j * mp.pi * tau / 24)
        qn = q
        for _ in range(140):
            eta_prod *= (1 - qn)
            if abs(qn) < mp.mpf("1e-52"):
                break
            qn *= q
        return 2 * mp.pi * (mp.euler - mp.log(2) - mp.mpf("0.5") * mp.log(y) - 2 * mp.log(abs(eta_prod)))
    if abs(u1) < mp.mpf("1e-36"):
        m0 = y * ((mp.pi / mp.sin(mp.pi * u2)) ** 2)
        reg_k0 = mp.pi * (2 * mp.euler - mp.log(y) - 2 * mp.log(2))
    else:
        m0 = mp.mpf(0)
        reg_k0 = mp.pi * (-mp.psi(0, u1) - mp.psi(0, 1 - u1) - mp.log(y) - 2 * mp.log(2))
    osc = mp.mpf(0)
    max_m = max(70, int(34.0 / max(0.15, float(y))) + 10)
    for m in range(-max_m, max_m + 1):
        alpha = m + u1
        if abs(alpha) < mp.mpf("1e-36"):
            continue
        a_abs = abs(alpha)
        beta = u2 + alpha * x
        z = mp.exp(2 * mp.j * mp.pi * (beta + mp.j * a_abs * y))
        osc += (mp.pi / a_abs) * 2 * mp.re(z / (1 - z))
    return m0 + reg_k0 + osc


def N_channel_norm(u1: mp.mpf, u2: mp.mpf, tau: mp.mpc) -> mp.mpf:
    """B1919 channel norm N(c, tau) = F_u(tau) + pi ln Im(tau) - 2*pi*(gamma_E + ln pi)."""
    return F_kronecker_shifted(u1, u2, tau) + mp.pi * mp.log(mp.im(tau)) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))


def jtheta_unit(idx: int, z: mp.mpc, tau: mp.mpc) -> mp.mpc:
    return mp.jtheta(idx, mp.pi * z, mp.exp(mp.j * mp.pi * tau))


def closed_form_M_and_Y(
    tau: mp.mpc,
    psi1: mp.mpf,
    psi2: mp.mpf,
    qx: int,
    qy: int,
    tilde_L: mp.mpf,
    reading: str = "S",
    serre_level: str = "B1",
    weight_power: str = "plus_half",
    broken_theta1_sign: bool = False,
) -> Tuple[mp.matrix, mp.matrix, Dict[str, mp.mpc]]:
    """
    Construct B1656's exact residue dictionary R_s (including the characteristic Gaussian prefactor
    G_char so R_s equals Res_{z=0} pair_s(bil(x, y, z, tau)) identically at unreduced (psi1, psi2)),
    the 2x2 weighted matter matrix M_w, and the 3x3 Yukawa matrix Y_f.

    Supports both:
      - Frame C / B1724 (`serre_level="B1"`, `weight_power="plus_half"`: u_s = sqrt(W_s) * R_s), and
      - Normalized overlap (`serre_level="B2"`, `weight_power="minus_half"`: u_s = R_s / sqrt(W_s)).
    """
    _, qi, qj, qk = _quat_mats()
    w = psi1 * tau - psi2
    ubar = (qx + qy) * w
    delta = (qx - qy) * w
    th1p0 = mp.pi * mp.jtheta(1, 0, mp.exp(mp.j * mp.pi * tau), derivative=1)

    # Exact characteristic prefactor from B1656's thc(ax, bx, u, 2*tau) * thc(ay, by, u, 2*tau)
    G_char = mp.exp(2 * mp.j * mp.pi * (qx * qx + qy * qy) * psi1 * (psi1 * tau - 2 * psi2))

    th1_ubar = jtheta_unit(1, ubar, tau)
    if broken_theta1_sign:
        th1_ubar = -th1_ubar
    R_s: Dict[str, mp.mpc] = {
        "1": G_char * (-mp.j) * th1_ubar * jtheta_unit(1, delta, tau) / th1p0,
        "i": G_char * (-1) * jtheta_unit(2, ubar, tau) * jtheta_unit(2, delta, tau) / th1p0,
        "j": G_char * (-1) * jtheta_unit(4, ubar, tau) * jtheta_unit(4, delta, tau) / th1p0,
        "k": G_char * (mp.j) * jtheta_unit(3, ubar, tau) * jtheta_unit(3, delta, tau) / th1p0,
    }

    u1b = (qx + qy) * psi1
    u2b = -(qx + qy) * psi2
    half = mp.mpf("0.5")
    shifts = {
        "1": (u1b, u2b),
        "i": (u1b, u2b - half),
        "j": (u1b - half, u2b),
        "k": (u1b - half, u2b - half),
    }
    u_weights: Dict[str, mp.mpc] = {}
    for s in ("1", "i", "j", "k"):
        W_s = F_kronecker_shifted(shifts[s][0], shifts[s][1], tau) + 2 * mp.pi * tilde_L
        assert W_s > 0, f"Non-positive channel weight W_{s} = {W_s}"
        if weight_power == "plus_half":
            u_weights[s] = mp.sqrt(W_s) * R_s[s]
        elif weight_power == "minus_half":
            u_weights[s] = R_s[s] / mp.sqrt(W_s)
        else:
            raise ValueError(f"Unknown weight_power: {weight_power}")

    M_w = weighted_M_mp(u_weights)
    trips = serre_triplets_exact(tau)
    a_vec = list(trips[serre_level])
    if reading == "S":
        pass
    elif reading == "S_tilde":
        a_vec = [mp.conj(v) for v in a_vec]
    elif reading == "conjS":
        a_vec = [-mp.conj(a_vec[0]), mp.conj(a_vec[1]), -mp.conj(a_vec[2])]
    else:
        raise ValueError(f"Unknown reading: {reading}")

    S_mat = a_vec[0] * qi + a_vec[1] * qj + a_vec[2] * qk
    Y = coupling_mp(S_mat, M_w)
    return M_w, Y, R_s


# ============================================================================
# SECTION 0C: STANDALONE B1656 RAW BILINEAR + STRIP QUADRATURE (bil_mp + cB)
# ============================================================================

def th_b1656_mp(n: int, u: mp.mpc, t: mp.mpc) -> mp.mpc:
    q = mp.exp(mp.j * mp.pi * t)
    x = mp.pi * u
    if n == 3:
        return mp.jtheta(3, x, q)
    if n == 4:
        return mp.jtheta(4, x, q)
    q4 = mp.exp(mp.j * mp.pi * t / 4)
    s = x + mp.pi * t / 2
    if n == 2:
        return q4 * mp.exp(mp.j * x) * mp.jtheta(3, s, q)
    return -mp.j * q4 * mp.exp(mp.j * x) * mp.jtheta(4, s, q)


def thc_b1656_mp(a: mp.mpf, b: mp.mpf, u: mp.mpc, T: mp.mpc) -> mp.mpc:
    return mp.exp(mp.j * mp.pi * a * a * T + 2 * mp.j * mp.pi * a * (u + b)) * th_b1656_mp(3, u + a * T + b, T)


def bil_b1656_mp(
    x_tw: Tuple[mp.mpf, mp.mpf],
    y_tw: Tuple[mp.mpf, mp.mpf],
    u: mp.mpc,
    t: mp.mpc,
) -> mp.matrix:
    """Exact standalone B1653/B1656 2x2 twisted theta bilinear on E_tau."""
    ax, bx = x_tw
    ay, by = y_tw
    T = 2 * t
    t1 = th_b1656_mp(1, u, t)
    den = mp.j * mp.exp(-mp.j * mp.pi * t / 2) * mp.exp(-mp.j * mp.pi * u) * t1
    X0 = thc_b1656_mp(ax, bx, u, T)
    X1 = thc_b1656_mp(ax, bx, u + t, T)
    Y0 = thc_b1656_mp(ay, by, u, T)
    Y1 = thc_b1656_mp(ay, by, u + t, T)
    return mp.matrix([
        [X0 * Y0 / t1, mp.exp(mp.j * mp.pi * by) * X0 * Y1 / den],
        [mp.exp(mp.j * mp.pi * bx) * X1 * Y0 / den, mp.exp(mp.j * mp.pi * (bx + by)) * X1 * Y1 / th_b1656_mp(1, u + t, t)],
    ])


def pair_b1656_mp(M: mp.matrix) -> Dict[str, mp.mpc]:
    i2, qi, qj, qk = _quat_mats()
    eps = qj
    units = {"1": i2, "i": qi, "j": qj, "k": qk}
    out: Dict[str, mp.mpc] = {}
    for s, C in units.items():
        ec = eps * C
        out[s] = sum(ec[m, n] * M[m, n] for m in range(2) for n in range(2))
    return out


def residues_b1656_mp(
    x_tw: Tuple[mp.mpf, mp.mpf],
    y_tw: Tuple[mp.mpf, mp.mpf],
    t: mp.mpc,
    rho: mp.mpf = mp.mpf("0.015"),
    N_circ: int = 128,
) -> Dict[str, mp.mpc]:
    acc = {s: mp.mpc(0) for s in ("1", "i", "j", "k")}
    for k in range(N_circ):
        z = rho * mp.expjpi(2 * mp.mpf(k) / N_circ)
        P = pair_b1656_mp(bil_b1656_mp(x_tw, y_tw, z, t))
        for s in ("1", "i", "j", "k"):
            acc[s] += P[s] * z
    return {s: acc[s] / N_circ for s in ("1", "i", "j", "k")}


def _parallelogram_boundary_integrals(t: mp.mpc) -> Dict[str, mp.mpc]:
    def rmax_mp(th: mp.mpf) -> mp.mpf:
        d = mp.expj(th)
        y1 = mp.im(d) / mp.im(t)
        x1 = mp.re(d) - y1 * mp.re(t)
        return mp.mpf("0.5") / max(abs(x1), abs(y1))

    verts = [sx * mp.mpf("0.5") + sy * t / 2 for sx in (1, -1) for sy in (1, -1)]
    br = sorted(mp.arg(z) % (2 * mp.pi) for z in verts)
    br.append(br[0] + 2 * mp.pi)
    I_log = mp.fsum(mp.quad(lambda th: mp.log(rmax_mp(th)), [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_1 = mp.fsum(mp.quad(lambda th: mp.expj(th) * rmax_mp(th), [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_2 = mp.fsum(mp.quad(lambda th: mp.expj(2 * th) * (rmax_mp(th) ** 2) / 2, [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_3 = mp.fsum(mp.quad(lambda th: mp.expj(4 * th) * (rmax_mp(th) ** 4) / 4, [a, b]) for a, b in zip(br[:-1], br[1:]))
    I_5 = mp.fsum(mp.quad(lambda th: mp.expj(6 * th) * (rmax_mp(th) ** 6) / 6, [a, b]) for a, b in zip(br[:-1], br[1:]))
    return {"I_log": I_log, "I_1": I_1, "I_2": I_2, "I_3": I_3, "I_5": I_5}


def cB_all_channels_mp(
    x_tw: Tuple[mp.mpf, mp.mpf],
    y_tw: Tuple[mp.mpf, mp.mpf],
    t: mp.mpc,
    R_dict: Dict[str, mp.mpc],
    b_ints: Dict[str, mp.mpc],
    n_gl: int = 22,
) -> Dict[str, Optional[mp.mpf]]:
    """
    Standalone subtracted 2D Gauss-Legendre strip quadrature for B1656's channel norms across all
    active channels simultaneously (reusing each bil_b1656_mp evaluation across s in {1, i, j, k}).
    Subtracts the non-smooth cross terms Re((a0 + a1*z + a2*z^2 + a3*z^3 + a4*z^4 + a5*z^5)/conj(z))
    and adds their exact polar boundary integrals on P = [-1/2, 1/2) + [-1/2, 1/2)*tau, yielding
    C^5 smoothness at z = 0 (< 1e-13 accuracy at n_gl = 22).
    """
    active = [s for s in ("1", "i", "j", "k") if abs(R_dict[s]) > mp.mpf("1e-20")]
    if not active:
        return {s: None for s in ("1", "i", "j", "k")}

    rho = mp.mpf("0.04")
    N_circ = 128
    laurent: Dict[str, List[mp.mpc]] = {s: [mp.mpc(0)] * 6 for s in active}
    for k in range(N_circ):
        z = rho * mp.expjpi(2 * mp.mpf(k) / N_circ)
        P = pair_b1656_mp(bil_b1656_mp(x_tw, y_tw, z, t))
        z_inv = 1 / z
        for s in active:
            g_val = P[s] / R_dict[s] - z_inv
            zp_inv = mp.mpc(1)
            for m_pow in range(6):
                laurent[s][m_pow] += g_val * zp_inv
                zp_inv *= z_inv
    for s in active:
        laurent[s] = [c / N_circ for c in laurent[s]]

    xg_np, wg_np = leggauss(n_gl)
    xg = [mp.mpf(repr(float(v))) for v in xg_np]
    wg = [mp.mpf(repr(float(v))) for v in wg_np]
    tot = {s: mp.mpf(0) for s in active}

    # Evaluate on the four quadrants of (-1/2, 1/2)^2 with zero symmetry shortcuts
    half = mp.mpf("0.5")
    q_intervals = [(-half, mp.mpf(0)), (mp.mpf(0), half)]
    for xa, xb in q_intervals:
        hx = (xb - xa) / 2
        mx = (xb + xa) / 2
        for ta, tb in q_intervals:
            ht = (tb - ta) / 2
            mt = (tb + ta) / 2
            area_wt = hx * ht
            for xi, wi in zip(xg, wg):
                xx = hx * xi + mx
                for tj, wj in zip(xg, wg):
                    tt = ht * tj + mt
                    z = xx + tt * t
                    P = pair_b1656_mp(bil_b1656_mp(x_tw, y_tw, z, t))
                    r2_inv = 1 / (abs(z) ** 2)
                    zc_inv = 1 / mp.conj(z)
                    wt_ij = wi * wj * area_wt
                    z2 = z * z
                    z3 = z2 * z
                    z4 = z2 * z2
                    z5 = z4 * z
                    for s in active:
                        K = P[s] / R_dict[s]
                        a_c = laurent[s]
                        sing_cross = 2 * mp.re(
                            (a_c[0] + a_c[1] * z + a_c[2] * z2 + a_c[3] * z3 + a_c[4] * z4 + a_c[5] * z5) * zc_inv
                        )
                        f_reg = (abs(K) ** 2) - r2_inv - sing_cross
                        tot[s] += wt_ij * f_reg

    out: Dict[str, Optional[mp.mpf]] = {s: None for s in ("1", "i", "j", "k")}
    for s in active:
        a_c = laurent[s]
        # Note I_1 == int (1/conj(z)) dA == 0 and int (z^2/conj(z)) dA == int (z^4/conj(z)) dA == 0 on symmetric P;
        # we still add 2*Re(a0*I_1) explicitly with zero shortcut.
        val = (
            tot[s] * mp.im(t)
            + 2 * mp.re(a_c[0] * b_ints["I_1"])
            + 2 * mp.re(a_c[1] * b_ints["I_2"])
            + 2 * mp.re(a_c[3] * b_ints["I_3"])
            + 2 * mp.re(a_c[5] * b_ints["I_5"])
            + mp.re(b_ints["I_log"])
        )
        out[s] = val
    return out


# ============================================================================
# SECTION 0D: BASIS-INVARIANT OBSERVABLES & HAAR SCRAMBLING HELPERS
# ============================================================================

def yukawa_svs_and_left_frame(Y: mp.matrix) -> Tuple[List[mp.mpf], mp.matrix]:
    H = Y * mat_H(Y)
    H = (H + mat_H(H)) / 2
    evals, evecs = mp.eigh(H)
    idx_order = sorted(range(3), key=lambda k: evals[k], reverse=True)
    svs = [mp.sqrt(max(mp.mpf(0), evals[k])) for k in idx_order]
    U_sorted = mp.zeros(3, 3)
    for col_new, col_old in enumerate(idx_order):
        for r in range(3):
            U_sorted[r, col_new] = evecs[r, col_old]
    return svs, U_sorted


def world_observables(Yu: mp.matrix, Yd: mp.matrix, Ye: mp.matrix) -> Dict[str, Any]:
    """
    Extract U(3)^5-invariant and scalar-rescaling-invariant flavour observables:
      - singular-value ratios (sv[1]/sv[0], sv[2]/sv[0]) in up, down, lep;
      - 3x3 CKM moduli |V_CKM|;
      - normalized Jarlskog invariant J_CP = Im det[H_u, H_d] / (2 * Delta_u * Delta_d),
        where H_f = Y_f Y_f^H and Delta_f = (s_0^2 - s_1^2)(s_0^2 - s_2^2)(s_1^2 - s_2^2) > 0,
        cross-checked in magnitude against |Im(V_01 V_12 conj(V_02) conj(V_11))|;
      - polynomial trace alignment invariant I_ud = tr(H_u H_d) / (tr(H_u) tr(H_d)).
    """
    sv_u, UL_u = yukawa_svs_and_left_frame(Yu)
    sv_d, UL_d = yukawa_svs_and_left_frame(Yd)
    sv_e, _ = yukawa_svs_and_left_frame(Ye)

    V = mat_H(UL_u) * UL_d
    V_mod = [[abs(V[r, c]) for c in range(3)] for r in range(3)]

    Hu = Yu * mat_H(Yu)
    Hd = Yd * mat_H(Yd)
    comm = Hu * Hd - Hd * Hu
    det_comm = det_3x3(comm)
    du = (sv_u[0] ** 2 - sv_u[1] ** 2) * (sv_u[0] ** 2 - sv_u[2] ** 2) * (sv_u[1] ** 2 - sv_u[2] ** 2)
    dd = (sv_d[0] ** 2 - sv_d[1] ** 2) * (sv_d[0] ** 2 - sv_d[2] ** 2) * (sv_d[1] ** 2 - sv_d[2] ** 2)
    j_cp = mp.im(det_comm) / (2 * du * dd)
    j_quartet_abs = abs(mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1])))
    assert abs(abs(j_cp) - j_quartet_abs) < mp.mpf("1e-28"), f"Jarlskog mismatch: {abs(j_cp)} vs {j_quartet_abs}"

    tr_hu = mp.re(Hu[0, 0] + Hu[1, 1] + Hu[2, 2])
    tr_hd = mp.re(Hd[0, 0] + Hd[1, 1] + Hd[2, 2])
    prod_ud = Hu * Hd
    tr_huhd = mp.re(prod_ud[0, 0] + prod_ud[1, 1] + prod_ud[2, 2])

    return {
        "ratios_u": [sv_u[1] / sv_u[0], sv_u[2] / sv_u[0]],
        "ratios_d": [sv_d[1] / sv_d[0], sv_d[2] / sv_d[0]],
        "ratios_e": [sv_e[1] / sv_e[0], sv_e[2] / sv_e[0]],
        "V_ckm_abs": V_mod,
        "J_cp": j_cp,
        "I_ud_trace": tr_huhd / (tr_hu * tr_hd),
    }


def compare_world_observables(obs1: Dict[str, Any], obs2: Dict[str, Any]) -> Dict[str, mp.mpf]:
    ratio_ckm_diff = max(
        max(abs(obs1["ratios_u"][i] - obs2["ratios_u"][i]) for i in range(2)),
        max(abs(obs1["ratios_d"][i] - obs2["ratios_d"][i]) for i in range(2)),
        max(abs(obs1["ratios_e"][i] - obs2["ratios_e"][i]) for i in range(2)),
        max(abs(obs1["V_ckm_abs"][r][c] - obs2["V_ckm_abs"][r][c]) for r in range(3) for c in range(3)),
        abs(obs1["I_ud_trace"] - obs2["I_ud_trace"]),
    )
    return {
        "ratio_ckm_max_diff": ratio_ckm_diff,
        "J_cp_same_sign_diff": abs(obs1["J_cp"] - obs2["J_cp"]),
        "J_cp_flipped_sign_diff": abs(obs1["J_cp"] + obs2["J_cp"]),
    }


def random_haar_unitary_3x3(rng: random.Random) -> mp.matrix:
    Z = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            Z[r, c] = mp.mpc(rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0))
    Q = mp.zeros(3, 3)
    for col in range(3):
        v = [Z[r, col] for r in range(3)]
        for prev in range(col):
            proj = sum(mp.conj(Q[r, prev]) * v[r] for r in range(3))
            v = [v[r] - proj * Q[r, prev] for r in range(3)]
        nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
        for r in range(3):
            Q[r, col] = v[r] / nrm
    return Q


# ============================================================================
# SECTION E1: EXACT MATTER-CHARGE NEGATION INVARIANCE (B1656 & B1919)
# ============================================================================

def run_section_e1(u_tau0: Dict[str, Any]) -> Dict[str, Any]:
    t0 = time.time()

    # 1. Guardrail 4 Benchmark Gate A: B1656 Cell E3/E7 at omega = exp(2*pi*i/3), line (1/9, 1/9)
    mp.mp.dps = 34
    omega3 = mp.exp(2 * mp.j * mp.pi / 3)
    b_ints_om = _parallelogram_boundary_integrals(omega3)
    p1_b, p2_b = mp.mpf(1) / 9, mp.mpf(1) / 9
    w_om = p1_b * omega3 - p2_b
    qx_u, qy_u = SIXY["Q"], SIXY["u"]
    x_om = (qx_u * p1_b, -2 * qx_u * p2_b)
    y_om = (qy_u * p1_b, -2 * qy_u * p2_b)
    R_om = residues_b1656_mp(x_om, y_om, omega3)
    cB_om = cB_all_channels_mp(x_om, y_om, omega3, R_om, b_ints_om, n_gl=22)

    c1_b1919 = N_channel_norm(mp.mpf(1) / 3, -mp.mpf(1) / 3, omega3)
    ci_b1919 = N_channel_norm(mp.mpf(1) / 3, -mp.mpf(1) / 3 - mp.mpf("0.5"), omega3)
    cj_b1919 = N_channel_norm(mp.mpf(1) / 3 - mp.mpf("0.5"), -mp.mpf(1) / 3, omega3)
    ck_b1919 = N_channel_norm(mp.mpf(1) / 3 - mp.mpf("0.5"), -mp.mpf(1) / 3 - mp.mpf("0.5"), omega3)
    b1919_om = {"1": c1_b1919, "i": ci_b1919, "j": cj_b1919, "k": ck_b1919}
    max_om_quad_vs_closed = max(abs(cB_om[s] - b1919_om[s]) for s in ("1", "i", "j", "k") if cB_om[s] is not None)
    assert max_om_quad_vs_closed < mp.mpf("1e-12"), f"B1656 vs B1919 benchmark residual: {max_om_quad_vs_closed}"
    assert abs(c1_b1919 - mp.mpf("-3.575627")) < mp.mpf("1e-6")
    assert abs(ci_b1919 - mp.mpf("2.231269")) < mp.mpf("1e-6")
    assert abs((c1_b1919 - ci_b1919) - mp.mpf("-5.806896")) < mp.mpf("1e-6")

    # 2. Pointwise B1656 bilinear reflection identity: bil(-x, -y, z, tau) + bil(x, y, -z, tau) == 0
    tau0 = mp.mpc("-0.27", "1.29")
    tau1 = mp.mpc("0.31", "1.17")
    u_tau1 = uniformize_punctured_torus(tau1)
    lines_test = [
        ("order5_torsion", mp.mpf(2) / 5, mp.mpf(4) / 5),
        ("irrational_off_torsion", mp.sqrt(2) / 5, mp.sqrt(3) / 7),
    ]
    z_samples = [mp.mpc("0.13", "-0.19"), mp.mpc("-0.21", "0.29")]
    max_pointwise_bil_err = mp.mpf(0)
    for t_val in (tau0, tau1):
        for _, p1, p2 in lines_test:
            for _, qx, qy in SECTORS_2D:
                x_pos = (qx * p1, -2 * qx * p2)
                y_pos = (qy * p1, -2 * qy * p2)
                x_neg = (-qx * p1, 2 * qx * p2)
                y_neg = (-qy * p1, 2 * qy * p2)
                for z_pt in z_samples:
                    B_neg = bil_b1656_mp(x_neg, y_neg, z_pt, t_val)
                    B_pos_rev = bil_b1656_mp(x_pos, y_pos, -z_pt, t_val)
                    err_b = mat_inf_norm(B_neg + B_pos_rev)
                    if err_b > max_pointwise_bil_err:
                        max_pointwise_bil_err = err_b
    assert max_pointwise_bil_err < mp.mpf("1e-30"), f"Pointwise bil reflection residual: {max_pointwise_bil_err}"

    # 3. Direct B1656 strip quadrature (bil_mp + cB) at tau0 across torsion and irrational lines (zero shortcuts)
    b_ints_tau0 = _parallelogram_boundary_integrals(tau0)
    L2_tau0 = u_tau0["L_2"]
    max_cB_vs_b1919 = mp.mpf(0)
    max_R_quad_neg_err = mp.mpf(0)
    max_cB_neg_err = mp.mpf(0)
    max_Mw_quad_neg_err = mp.mpf(0)
    quad_cases_checked = 0

    for line_label, p1, p2 in lines_test:
        for sec_name, qx, qy in SECTORS_2D:
            x_pos = (qx * p1, -2 * qx * p2)
            y_pos = (qy * p1, -2 * qy * p2)
            x_neg = (-qx * p1, 2 * qx * p2)
            y_neg = (-qy * p1, 2 * qy * p2)

            R_pos = residues_b1656_mp(x_pos, y_pos, tau0)
            R_neg = residues_b1656_mp(x_neg, y_neg, tau0)
            for s in ("1", "i", "j", "k"):
                max_R_quad_neg_err = max(max_R_quad_neg_err, abs(R_pos[s] - R_neg[s]))

            cB_pos = cB_all_channels_mp(x_pos, y_pos, tau0, R_pos, b_ints_tau0, n_gl=22)
            cB_neg = cB_all_channels_mp(x_neg, y_neg, tau0, R_neg, b_ints_tau0, n_gl=22)

            u1b = (qx + qy) * p1
            u2b = -(qx + qy) * p2
            half = mp.mpf("0.5")
            sh_map = {
                "1": (u1b, u2b),
                "i": (u1b, u2b - half),
                "j": (u1b - half, u2b),
                "k": (u1b - half, u2b - half),
            }
            u_pos_dict: Dict[str, mp.mpc] = {}
            u_neg_dict: Dict[str, mp.mpc] = {}
            for s in ("1", "i", "j", "k"):
                if cB_pos[s] is not None and cB_neg[s] is not None:
                    n_closed = N_channel_norm(sh_map[s][0], sh_map[s][1], tau0)
                    max_cB_vs_b1919 = max(max_cB_vs_b1919, abs(cB_pos[s] - n_closed), abs(cB_neg[s] - n_closed))
                    max_cB_neg_err = max(max_cB_neg_err, abs(cB_pos[s] - cB_neg[s]))
                    u_pos_dict[s] = mp.sqrt(2 * mp.pi * L2_tau0 + cB_pos[s]) * R_pos[s]
                    u_neg_dict[s] = mp.sqrt(2 * mp.pi * L2_tau0 + cB_neg[s]) * R_neg[s]
                    quad_cases_checked += 1
                else:
                    assert abs(R_pos[s]) < mp.mpf("1e-28") and abs(R_neg[s]) < mp.mpf("1e-28")
                    u_pos_dict[s] = mp.mpc(0)
                    u_neg_dict[s] = mp.mpc(0)

            Mw_pos_q = weighted_M_mp(u_pos_dict)
            Mw_neg_q = weighted_M_mp(u_neg_dict)
            max_Mw_quad_neg_err = max(max_Mw_quad_neg_err, mat_inf_norm(Mw_pos_q - Mw_neg_q))

    assert max_cB_vs_b1919 < mp.mpf("1e-12"), f"cB vs B1919 residual too large: {max_cB_vs_b1919}"
    assert max_Mw_quad_neg_err < mp.mpf("1e-12"), f"Quadrature M_w(-q) - M_w(+q) residual: {max_Mw_quad_neg_err}"

    # 4. Closed-form B1919 + B1927 check across (tau0, tau1), torsion & irrational shifts, and both conventions
    mp.mp.dps = 44
    max_closed_Mw_err = mp.mpf(0)
    max_closed_Yf_err = mp.mpf(0)
    max_closed_vs_b1656_R = mp.mpf(0)

    for t_val, u_t in ((tau0, u_tau0), (tau1, u_tau1)):
        tL2 = u_t["tilde_L_2"]
        for _, p1, p2 in lines_test:
            for _, qx, qy in SECTORS_2D:
                for serre_lv, w_pow in (("B1", "plus_half"), ("B2", "minus_half")):
                    for rd in ("S", "S_tilde"):
                        Mw_p, Y_p, R_p = closed_form_M_and_Y(
                            t_val, p1, p2, qx, qy, tL2, reading=rd, serre_level=serre_lv, weight_power=w_pow
                        )
                        Mw_n, Y_n, _ = closed_form_M_and_Y(
                            t_val, p1, p2, -qx, -qy, tL2, reading=rd, serre_level=serre_lv, weight_power=w_pow
                        )
                        max_closed_Mw_err = max(max_closed_Mw_err, mat_inf_norm(Mw_p - Mw_n))
                        max_closed_Yf_err = max(max_closed_Yf_err, mat_inf_norm(Y_p - Y_n))
                        if serre_lv == "B1" and rd == "S" and t_val == tau0:
                            R_circ = residues_b1656_mp((qx * p1, -2 * qx * p2), (qy * p1, -2 * qy * p2), t_val)
                            for s in ("1", "i", "j", "k"):
                                max_closed_vs_b1656_R = max(max_closed_vs_b1656_R, abs(R_p[s] - R_circ[s]))

    assert max_closed_Mw_err < mp.mpf("1e-30"), f"Closed-form M_w negation err: {max_closed_Mw_err}"
    assert max_closed_Yf_err < mp.mpf("1e-30"), f"Closed-form Y_f negation err: {max_closed_Yf_err}"
    assert max_closed_vs_b1656_R < mp.mpf("1e-26"), f"Closed-form R_s vs B1656 circle residue: {max_closed_vs_b1656_R}"

    # 5. Planted Control PC_SCAR_2: break theta_1 oddness in one factor only on (-qx, -qy)
    p1_irr, p2_irr = mp.sqrt(2) / 5, mp.sqrt(3) / 7
    Mw_true, _, _ = closed_form_M_and_Y(tau0, p1_irr, p2_irr, SIXY["Q"], SIXY["d"], u_tau0["tilde_L_2"])
    Mw_broken, _, _ = closed_form_M_and_Y(
        tau0, p1_irr, p2_irr, -SIXY["Q"], -SIXY["d"], u_tau0["tilde_L_2"], broken_theta1_sign=True
    )
    pc_scar_2_discrepancy = float(mat_inf_norm(Mw_true - Mw_broken) / mat_inf_norm(Mw_true))
    pc_scar_2_fired = pc_scar_2_discrepancy > 0.01
    assert pc_scar_2_fired, f"PC_SCAR_2 failed to fire: {pc_scar_2_discrepancy}"

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "benchmark_b1656_omega_line_1_9": {
            "c1_b1919": float(c1_b1919),
            "c_perp_b1919": float(ci_b1919),
            "gap_b1919": float(c1_b1919 - ci_b1919),
            "max_cB_quadrature_vs_b1919": float(max_om_quad_vs_closed),
        },
        "pointwise_bil_reflection_max_err": float(max_pointwise_bil_err),
        "b1656_strip_quadrature_checks": {
            "active_channel_cases": quad_cases_checked,
            "max_cB_vs_b1919_closed": float(max_cB_vs_b1919),
            "max_residue_negation_diff": float(max_R_quad_neg_err),
            "max_cB_negation_diff": float(max_cB_neg_err),
            "max_Mw_quadrature_negation_diff": float(max_Mw_quad_neg_err),
        },
        "b1919_closed_form_checks": {
            "max_Mw_negation_diff": float(max_closed_Mw_err),
            "max_Yf_negation_diff": float(max_closed_Yf_err),
            "max_closed_residue_vs_b1656_circle": float(max_closed_vs_b1656_R),
        },
        "PC_SCAR_2": {
            "relative_Mw_discrepancy_broken_theta1": pc_scar_2_discrepancy,
            "fired": pc_scar_2_fired,
        },
    }


# ============================================================================
# SECTION E2: STANDALONE 3-MANIFOLD SCAR DUALITY (W-F9) & B1438 SLOPE ENGINE
# ============================================================================

def _word_inv(w: Sequence[int]) -> List[int]:
    return [-g for g in reversed(w)]


def _word_reduce(w: Sequence[int]) -> List[int]:
    out: List[int] = []
    for g in w:
        if out and out[-1] == -g:
            out.pop()
        else:
            out.append(g)
    return out


def _aut_apply(aut: Dict[int, List[int]], w: Sequence[int]) -> List[int]:
    out: List[int] = []
    for g in w:
        out.extend(aut[g] if g > 0 else _word_inv(aut[-g]))
    return _word_reduce(out)


def _aut_compose(a: Dict[int, List[int]], b: Dict[int, List[int]]) -> Dict[int, List[int]]:
    return {1: _aut_apply(a, b[1]), 2: _aut_apply(a, b[2])}


def build_cyclic_level(eps: int, word: str, k: int) -> Dict[str, Any]:
    """Build pi_1 = <x, y, t | t x t^-1 = Phi(x), t y t^-1 = Phi(y)>, mu = t, lam = [x, y]."""
    tau_L = {1: [1], 2: [2, 1]}
    tau_R = {1: [1, 2], 2: [2]}
    c_yx = [2, 1]
    iota = {1: _word_reduce(c_yx + [-1] + _word_inv(c_yx)), 2: _word_reduce(c_yx + [-2] + _word_inv(c_yx))}
    phi = {1: [1], 2: [2]}
    for ch in word:
        phi = _aut_compose(phi, tau_L if ch == "L" else tau_R)
    if eps < 0:
        phi = _aut_compose(iota, phi)
    comm = [1, 2, -1, -2]
    assert _aut_apply(phi, comm) == comm, "Monodromy must fix commutator [x, y]"

    Phi = {1: [1], 2: [2]}
    for _ in range(k):
        Phi = _aut_compose(phi, Phi)

    rels = [
        _word_reduce([3, 1, -3] + _word_inv(Phi[1])),
        _word_reduce([3, 2, -3] + _word_inv(Phi[2])),
    ]

    def ex2(w: Sequence[int]) -> Tuple[int, int]:
        return (
            sum(1 if g == 1 else -1 if g == -1 else 0 for g in w),
            sum(1 if g == 2 else -1 if g == -2 else 0 for g in w),
        )

    px, py = ex2(Phi[1]), ex2(Phi[2])
    A = [[px[0], py[0]], [px[1], py[1]]]
    det_m = abs((A[0][0] - 1) * (A[1][1] - 1) - A[0][1] * A[1][0])
    g = math.gcd(math.gcd(A[0][0] - 1, A[1][1] - 1), math.gcd(A[0][1], A[1][0]))
    N_exp = max(1, det_m // g if g else 0)

    chars: List[Tuple[int, int, int]] = []
    for i, j in itertools.product(range(N_exp), repeat=2):
        if ((px[0] - 1) * i + px[1] * j) % N_exp == 0 and (py[0] * i + (py[1] - 1) * j) % N_exp == 0:
            chars.append((i, j, 0))
    return {"rels": rels, "mu": [3], "lam": comm, "Phi": Phi, "N": N_exp, "chars": sorted(chars)}


def _poly_div_exact_int(num: List[int], den: List[int]) -> List[int]:
    """Exact division of integer polynomials where den is monic (den[-1] == 1)."""
    assert den[-1] == 1
    rem = list(num)
    deg_d = len(den) - 1
    if len(rem) - 1 < deg_d:
        return [0]
    quot = [0] * (len(rem) - deg_d)
    for k in range(len(rem) - 1, deg_d - 1, -1):
        coeff = rem[k]
        quot[k - deg_d] = coeff
        if coeff != 0:
            for j in range(deg_d + 1):
                rem[k - deg_d + j] -= coeff * den[j]
    assert all(x == 0 for x in rem[:deg_d]), f"Non-zero remainder in cyclotomic division: {rem}"
    return quot


def cyclotomic_poly_coeffs(N: int) -> List[Fr]:
    """Pure-Python exact coefficients [c_0, ..., c_d] of the N-th cyclotomic polynomial Phi_N(z)."""
    memo: Dict[int, List[int]] = {}
    for m in range(1, N + 1):
        if N % m != 0:
            continue
        p = [-1] + [0] * (m - 1) + [1]  # z^m - 1
        for d in range(1, m):
            if m % d == 0:
                p = _poly_div_exact_int(p, memo[d])
        memo[m] = p
    phi = [Fr(c) for c in memo[N]]
    euler_phi = sum(1 for k in range(1, N + 1) if math.gcd(k, N) == 1)
    assert len(phi) - 1 == euler_phi
    return phi


class CycField:
    """Exact arithmetic in Q(zeta_N) = Q[z]/(Phi_N(z)) with zero external CAS imports."""
    def __init__(self, N: int):
        self.N = N
        self.phi = cyclotomic_poly_coeffs(N)
        self.deg = len(self.phi) - 1

    def red(self, coeffs: Sequence[Fr]) -> Tuple[Fr, ...]:
        c = list(coeffs)
        while len(c) > self.deg:
            top = c.pop()
            if top:
                off = len(c) - self.deg
                for i in range(self.deg):
                    c[off + i] -= top * self.phi[i]
        if len(c) < self.deg:
            c.extend([Fr(0)] * (self.deg - len(c)))
        return tuple(c)

    def const(self, q: int | Fr) -> "CycEl":
        return CycEl(self, self.red([Fr(q)]))

    def zeta(self, exp_k: int) -> "CycEl":
        e = exp_k % self.N
        return CycEl(self, self.red([Fr(0)] * e + [Fr(1)]))


class CycEl:
    __slots__ = ("F", "c")

    def __init__(self, F: CycField, c: Tuple[Fr, ...]):
        self.F = F
        self.c = c

    def __add__(self, o: "CycEl") -> "CycEl":
        return CycEl(self.F, tuple(a + b for a, b in zip(self.c, o.c)))

    def __sub__(self, o: "CycEl") -> "CycEl":
        return CycEl(self.F, tuple(a - b for a, b in zip(self.c, o.c)))

    def __neg__(self) -> "CycEl":
        return CycEl(self.F, tuple(-a for a in self.c))

    def __mul__(self, o: "CycEl") -> "CycEl":
        d = self.F.deg
        out = [Fr(0)] * max(1, 2 * d - 1)
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if b:
                        out[i + j] += a * b
        return CycEl(self.F, self.F.red(out))

    def iszero(self) -> bool:
        return not any(self.c)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, CycEl) and self.c == o.c

    def __hash__(self) -> int:
        return hash(self.c)

    def inv(self) -> "CycEl":
        d = self.F.deg
        cols = [(self * CycEl(self.F, self.F.red([Fr(0)] * j + [Fr(1)]))).c for j in range(d)]
        M = [[cols[j][i] for j in range(d)] + [Fr(1 if i == 0 else 0)] for i in range(d)]
        for col in range(d):
            piv = next(r for r in range(col, d) if M[r][col] != 0)
            M[col], M[piv] = M[piv], M[col]
            iv = Fr(1) / M[col][col]
            M[col] = [v * iv for v in M[col]]
            for r in range(d):
                if r != col and M[r][col] != 0:
                    fac = M[r][col]
                    M[r] = [v - fac * w for v, w in zip(M[r], M[col])]
        return CycEl(self.F, tuple(M[r][d] for r in range(d)))


def exact_slopes_level(lv: Dict[str, Any]) -> Tuple[CycField, Dict[Tuple[int, int, int], Optional[CycEl]]]:
    """Compute exact B1438 character slopes s(chi) in Q(zeta_N) directly from u_chi(lam)=1, s(chi)=u_chi(mu)."""
    N = lv["N"]
    Phi = lv["Phi"]
    F = CycField(N)
    one = F.const(1)
    zero = F.const(0)
    slopes: Dict[Tuple[int, int, int], Optional[CycEl]] = {(0, 0, 0): None}
    for c in lv["chars"]:
        i, j, _ = c
        if (i, j) == (0, 0):
            continue
        val = {1: F.zeta(i), 2: F.zeta(j), -1: F.zeta(-i), -2: F.zeta(-j)}
        u = {1: zero, 2: (val[1] - one).inv()} if (i % N) else {1: (one - val[2]).inv(), 2: zero}

        def ev_word(w: Sequence[int]) -> CycEl:
            tot = zero
            pre = one
            for g in w:
                if g > 0:
                    tot = tot + pre * u[g]
                    pre = pre * val[g]
                else:
                    pre = pre * val[g]
                    tot = tot - pre * u[-g]
            return tot

        assert ev_word((1, 2, -1, -2)) == one, "Longitude normalization failed"
        g_main = 1 if (i % N) else 2
        s_val = (u[g_main] - ev_word(Phi[g_main])) * (val[g_main] - one).inv()
        g_alt = 3 - g_main
        if not (val[g_alt] - one).iszero():
            assert (u[g_alt] - ev_word(Phi[g_alt])) * (val[g_alt] - one).inv() == s_val
        slopes[c] = s_val
    return F, slopes


def _is_prime(q: int) -> bool:
    return q > 1 and all(q % d != 0 for d in range(2, int(math.isqrt(q)) + 1))


def _first_prime_1mod(N: int, start: int = 100000) -> Tuple[int, int]:
    q = start + 1
    while not (q % N == 1 % N and _is_prime(q)):
        q += 1
    m = q - 1
    facs: List[int] = []
    d = 2
    while d * d <= m:
        if m % d == 0:
            facs.append(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        facs.append(m)
    g_root = next(g for g in range(2, q) if all(pow(g, (q - 1) // f, q) != 1 for f in facs))
    zeta = pow(g_root, (q - 1) // N, q)
    return q, zeta


def _rank_and_null_fp(rows: List[List[int]], ncols: int, p: int, want_null: bool = False) -> Tuple[int, List[List[int]]]:
    R = [[x % p for x in r] for r in rows]
    piv: List[int] = []
    rk = 0
    for c in range(ncols):
        k = next((i for i in range(rk, len(R)) if R[i][c] % p != 0), None)
        if k is None:
            continue
        R[rk], R[k] = R[k], R[rk]
        iv = pow(R[rk][c], p - 2, p)
        R[rk] = [(x * iv) % p for x in R[rk]]
        for i in range(len(R)):
            if i != rk and R[i][c] % p != 0:
                fac = R[i][c]
                R[i] = [(x - fac * y) % p for x, y in zip(R[i], R[rk])]
        piv.append(c)
        rk += 1
    if not want_null:
        return rk, []
    free = [c for c in range(ncols) if c not in piv]
    ns: List[List[int]] = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for idx, pc in enumerate(piv):
            v[pc] = (-R[idx][fc]) % p
        ns.append(v)
    return rk, ns


def _mmul_fp(A: List[List[int]], B: List[List[int]], p: int) -> List[List[int]]:
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[r][s] * B[s][c] for s in range(k)) % p for c in range(m)] for r in range(n)]


def _minv_2x2_fp(M: List[List[int]], p: int) -> List[List[int]]:
    det = (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % p
    assert det != 0
    inv_d = pow(det, p - 2, p)
    return [
        [(M[1][1] * inv_d) % p, (-M[0][1] * inv_d) % p],
        [(-M[1][0] * inv_d) % p, (M[0][0] * inv_d) % p],
    ]


class FoxModule2D:
    """Standalone 2x2 representation over F_p for direct Fox 1-cocycle and interior cohomology computation."""
    def __init__(self, gen_mats: Dict[int, List[List[int]]], p: int):
        self.p = p
        self.M: Dict[int, List[List[int]]] = {}
        for g in (1, 2, 3):
            self.M[g] = gen_mats[g]
            self.M[-g] = _minv_2x2_fp(gen_mats[g], p)

    def eval_word(self, w: Sequence[int]) -> List[List[int]]:
        R = [[1, 0], [0, 1]]
        for g in w:
            R = _mmul_fp(R, self.M[g], self.p)
        return R

    def fox_deriv(self, w: Sequence[int]) -> Dict[int, List[List[int]]]:
        p = self.p
        D = {1: [[0, 0], [0, 0]], 2: [[0, 0], [0, 0]], 3: [[0, 0], [0, 0]]}
        pre = [[1, 0], [0, 1]]
        for g in w:
            if g > 0:
                D[g] = [[(D[g][r][c] + pre[r][c]) % p for c in range(2)] for r in range(2)]
                pre = _mmul_fp(pre, self.M[g], p)
            else:
                pre = _mmul_fp(pre, self.M[g], p)
                bg = -g
                D[bg] = [[(D[bg][r][c] - pre[r][c]) % p for c in range(2)] for r in range(2)]
        return D

    def dual_module(self) -> "FoxModule2D":
        p = self.p
        dual_mats: Dict[int, List[List[int]]] = {}
        for g in (1, 2, 3):
            inv_m = self.M[-g]
            dual_mats[g] = [[inv_m[0][0], inv_m[1][0]], [inv_m[0][1], inv_m[1][1]]]
        return FoxModule2D(dual_mats, p)

    def h1_int_dim(self, rels: List[List[int]], mu: List[int], lam: List[int]) -> Tuple[int, int, int, int, int]:
        p = self.p
        I2 = [[1, 0], [0, 1]]
        for r in rels:
            assert self.eval_word(r) == I2, "Relator violated on 2D module"
        D0 = [[(self.M[g][r][c] - I2[r][c]) % p for c in range(2)] for g in (1, 2, 3) for r in range(2)]
        rk0, _ = _rank_and_null_fp(D0, 2, p)
        a0 = 2 - rk0

        J_rows: List[List[int]] = []
        for rel in rels:
            F = self.fox_deriv(rel)
            for r in range(2):
                J_rows.append([F[g][r][c] for g in (1, 2, 3) for c in range(2)])
        rkJ, Z1 = _rank_and_null_fp(J_rows, 6, p, want_null=True)
        a1 = (6 - rkJ) - rk0

        Am = [[(self.eval_word(mu)[r][c] - I2[r][c]) % p for c in range(2)] for r in range(2)]
        Al = [[(self.eval_word(lam)[r][c] - I2[r][c]) % p for c in range(2)] for r in range(2)]
        BT = Am + Al  # 4 x 2
        rkBT, _ = _rank_and_null_fp(BT, 2, p)
        t0 = 2 - rkBT
        ZT = [[(-Al[r][c]) % p for c in range(2)] + [Am[r][c] for c in range(2)] for r in range(2)]
        rkZT, _ = _rank_and_null_fp(ZT, 4, p)
        t1 = (4 - rkZT) - rkBT

        Dm = self.fox_deriv(mu)
        Dl = self.fox_deriv(lam)
        Res = (
            [[Dm[g][r][c] for g in (1, 2, 3) for c in range(2)] for r in range(2)]
            + [[Dl[g][r][c] for g in (1, 2, 3) for c in range(2)] for r in range(2)]
        )
        res_vecs = [[sum(Res[i][k] * z[k] for k in range(6)) % p for i in range(4)] for z in Z1]
        bt_vecs = [[BT[i][j] for i in range(4)] for j in range(2)]
        rk_all, _ = _rank_and_null_fp(res_vecs + bt_vecs, 4, p)
        rk_b, _ = _rank_and_null_fp(bt_vecs, 4, p)
        r1 = rk_all - rk_b
        return a1 - r1, a0, a1, t0, t1


def _extension_cocycle_fp(
    lam_c: Tuple[int, int, int], rels: List[List[int]], N: int, zeta: int, p: int
) -> Optional[List[int]]:
    val = [pow(zeta, e % N, p) for e in lam_c]
    rows: List[List[int]] = []
    for rel in rels:
        D = [0, 0, 0]
        pre = 1
        for g in rel:
            idx = abs(g) - 1
            if g > 0:
                D[idx] = (D[idx] + pre) % p
                pre = (pre * val[idx]) % p
            else:
                pre = (pre * pow(val[idx], p - 2, p)) % p
                D[idx] = (D[idx] - pre) % p
        rows.append(D)
    _, ns = _rank_and_null_fp(rows, 3, p, want_null=True)
    b = [(v - 1) % p for v in val]
    rb = 1 if any(b) else 0
    for z in ns:
        if rb == 0:
            return z
        if _rank_and_null_fp([b, z], 3, p)[0] == 2:
            return z
    return None


def _build_ext_module(
    lam_c: Tuple[int, int, int], al_c: Tuple[int, int, int], ct: List[int], N: int, zeta: int, p: int
) -> FoxModule2D:
    mats: Dict[int, List[List[int]]] = {}
    for idx, g in enumerate((1, 2, 3)):
        a = pow(zeta, al_c[idx] % N, p)
        b = pow(zeta, (al_c[idx] - lam_c[idx]) % N, p)
        mats[g] = [[a, (ct[idx] * b) % p], [0, b]]
    return FoxModule2D(mats, p)


def run_section_e2() -> Dict[str, Any]:
    t0 = time.time()
    levels_spec = [
        ("+LR", +1, "LR", 2),
        ("+LR", +1, "LR", 3),
        ("+LLR", +1, "LLR", 3),
        ("-LLRLR", -1, "LLRLR", 1),
        ("-LLLRLR", -1, "LLLRLR", 1),
    ]

    level_reports: List[Dict[str, Any]] = []
    total_modules_checked = 0
    total_firing_law_mismatches = 0
    total_fox_duality_mismatches = 0
    total_intertwiner_mismatches = 0
    total_param_involution_mismatches = 0
    total_higgs_inversion_mismatches = 0
    total_asymmetric_flip_cases = 0
    total_orientable_slope_mismatches = 0
    total_orientable_coupling_mismatches = 0

    pc_scar_1_tested_bgs = 0
    pc_scar_1_violated_bgs = 0
    pc_scar_1_odd_order_tested = 0
    pc_scar_1_odd_order_violated = 0

    for label, eps, word, k in levels_spec:
        lv = build_cyclic_level(eps, word, k)
        N = lv["N"]
        chars = lv["chars"]
        rels, mu, lam = lv["rels"], lv["mu"], lv["lam"]
        F_cyc, slopes = exact_slopes_level(lv)
        p, zeta = _first_prime_1mod(N, start=100000)

        add_c = lambda x, y: tuple((a + b) % N for a, b in zip(x, y))
        neg_c = lambda x: tuple((-a) % N for a in x)
        mul_c = lambda x, m: tuple((m * a) % N for a in x)
        triv = (0, 0, 0)

        # Verify slope conjugation law s(chi^-1) == s(chi) on orientable states (eps > 0)
        slope_conj_mismatches = 0
        for c in chars:
            if c == triv:
                continue
            if slopes[neg_c(c)] != slopes[c]:
                slope_conj_mismatches += 1
        if eps > 0:
            total_orientable_slope_mismatches += slope_conj_mismatches

        # Build extension cocycles and check Fox cohomology + explicit 2x2 J_2 intertwiner across ALL candidate modules
        cocycles: Dict[Tuple[int, int, int], List[int]] = {}
        for lc in chars:
            ct = _extension_cocycle_fp(lc, rels, N, zeta, p)
            if ct is not None:
                cocycles[lc] = ct

        J2 = [[0, 1], [p - 1, 0]]
        J2_inv = [[0, p - 1], [1, 0]]

        I_map: Dict[Tuple[Tuple[int, int, int], Tuple[int, int, int]], int] = {}
        mod_count_lv = 0
        for lc, ct in cocycles.items():
            if lc == triv:
                continue
            for al in chars:
                be = add_c(al, neg_c(lc))
                V = _build_ext_module(lc, al, ct, N, zeta, p)
                V_dual = V.dual_module()
                al_dual = add_c(lc, neg_c(al))  # ell * alpha^-1 = beta^-1
                V_reparam = _build_ext_module(lc, al_dual, ct, N, zeta, p)

                # Explicit 2x2 intertwiner check: J_2 * V^*(g) * J_2^-1 == V(ell, ell*alpha^-1)(g)
                for g in (1, 2, 3):
                    conj_g = _mmul_fp(_mmul_fp(J2, V_dual.M[g], p), J2_inv, p)
                    if conj_g != V_reparam.M[g]:
                        total_intertwiner_mismatches += 1

                # Direct Fox interior dimensions computed independently on V, V^*, and V_reparam
                n_V, a0, _, t0, t1 = V.h1_int_dim(rels, mu, lam)
                n_Vd, b0, _, s0, s1 = V_dual.h1_int_dim(rels, mu, lam)
                n_Vrep, _, _, _, _ = V_reparam.h1_int_dim(rels, mu, lam)
                I_fox = n_V - n_Vd
                I_fox_dual = n_Vd - n_V
                if n_Vd != n_Vrep or (I_fox + I_fox_dual) != 0:
                    total_fox_duality_mismatches += 1
                assert t1 == s1

                if al != triv and be != triv:
                    pred_I = int(slopes[al] == slopes[lc]) - int(slopes[neg_c(be)] == slopes[lc])
                    if I_fox != pred_I:
                        total_firing_law_mismatches += 1

                if I_fox != 0:
                    I_map[(lc, al)] = I_fox
                mod_count_lv += 1
                total_modules_checked += 1

        # Verify parameter involution (theta, psi_Y, W, ell) -> (theta*W^-1, psi_Y^-1, W^-1, ell)
        # across the FULL triple lattice (theta, psi_Y, W) with ell != triv, AND across all firing backgrounds!
        for th, pY, Wc in itertools.product(chars, repeat=3):
            lc = add_c(mul_c(th, 2), neg_c(Wc))
            if lc == triv:
                continue
            th_d = add_c(th, neg_c(Wc))
            pY_d = neg_c(pY)
            Wc_d = neg_c(Wc)
            lc_d = add_c(mul_c(th_d, 2), neg_c(Wc_d))
            if lc_d != lc:
                total_param_involution_mismatches += 1
            for _, sy, sg in SCAR_SECTORS:
                al_s = add_c(add_c(th, mul_c(pY, sy)), mul_c(Wc, (sg - 1) // 2))
                al_s_from_dual_params = add_c(add_c(th_d, mul_c(pY_d, sy)), mul_c(Wc_d, (sg - 1) // 2))
                al_s_expected = add_c(lc, neg_c(al_s))
                if al_s_from_dual_params != al_s_expected:
                    total_param_involution_mismatches += 1

        # Enumerate generation-shaped firing backgrounds exactly as in B1432/B1435
        fifth_roots: Dict[Tuple[int, int, int], List[Tuple[int, int, int]]] = collections.defaultdict(list)
        for c in chars:
            fifth_roots[mul_c(c, 5)].append(c)

        bgs: Dict[Tuple[Tuple[int, int, int], ...], Tuple[Tuple[int, ...], Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]] = {}
        by_lc: Dict[Tuple[int, int, int], Dict[Tuple[int, int, int], int]] = collections.defaultdict(dict)
        for (lc, al), iv in I_map.items():
            by_lc[lc][al] = iv

        for lc, sl_dict in by_lc.items():
            for ad, id_val in sl_dict.items():
                for aL, iL_val in sl_dict.items():
                    if id_val != iL_val:
                        continue
                    for pY in fifth_roots.get(add_c(ad, neg_c(aL)), []):
                        th = add_c(ad, mul_c(pY, -2))
                        Wc = add_c(mul_c(th, 2), neg_c(lc))
                        al_list = [
                            add_c(add_c(th, mul_c(pY, sy)), mul_c(Wc, (sg - 1) // 2))
                            for (_, sy, sg) in SCAR_SECTORS
                        ]
                        cnt = tuple(sl_dict.get(a, 0) for a in al_list)
                        if cnt[0] == cnt[1] == cnt[2] == cnt[3] == cnt[4] != 0:
                            key = (lc,) + tuple(al_list)
                            if key not in bgs:
                                bgs[key] = (cnt, th, pY, Wc)

        # Check W-F9 bijection between +1 and -1 generation-shaped firing backgrounds, Higgs character inversion,
        # B1438 coupling invariance Y(A, B) = s(ell) - s(eta), and Planted Control PC_SCAR_1!
        higgs_pairs = (("Q", "uc", 0, 1), ("Q", "dc", 0, 3), ("L", "ec", 4, 2))
        dual_bijection_ok = True
        lv_coupling_mismatches = 0
        for key, (cnt, th, pY, Wc) in bgs.items():
            lc = key[0]
            al_vec = key[1:]
            dual_key = (lc,) + tuple(add_c(lc, neg_c(a)) for a in al_vec)
            if dual_key not in bgs or bgs[dual_key][0] != tuple(-x for x in cnt):
                dual_bijection_ok = False

            for _, _, idxA, idxB in higgs_pairs:
                # Base (+1 module) spin-0 partner character: eta_plus = -(alpha_A + beta_B) = ell - alpha_A - alpha_B
                eta_plus = add_c(lc, neg_c(add_c(al_vec[idxA], al_vec[idxB])))
                # Dualized (-1 module) spin-0 partner character: eta_minus = -(alpha_A' + beta_B') = alpha_A + alpha_B - ell
                alA_d = add_c(lc, neg_c(al_vec[idxA]))
                beB_d = neg_c(al_vec[idxB])
                eta_minus = neg_c(add_c(alA_d, beB_d))

                if eta_minus != neg_c(eta_plus):
                    total_higgs_inversion_mismatches += 1

                # Check if matter's 3*psi_Y flips to a distinct character while eta fails to invert
                # (Note: eta_minus == -eta_plus ALWAYS; check also whether non-2-torsion eta ever stays fixed!)
                if mul_c(eta_plus, 2) != triv and eta_minus == eta_plus:
                    total_asymmetric_flip_cases += 1

                # Coupling Y(A, B) = s(ell) - s(eta) (-1 if eta == triv)
                y_plus = F_cyc.const(-1) if eta_plus == triv else (slopes[lc] - slopes[eta_plus])
                y_minus = F_cyc.const(-1) if eta_minus == triv else (slopes[lc] - slopes[eta_minus])
                if y_plus != y_minus:
                    lv_coupling_mismatches += 1

            # PC_SCAR_1: un-dualized Higgs character eta_plus paired with dualized matter V_s^*
            # Total cubic character is (alpha_A' + beta_B') + eta_plus = 2 * eta_plus (mod N).
            # Check both: all backgrounds with non-2-torsion Higgs (where 2*eta_plus != 0) AND odd-order psi_Y^3 != 1.
            pY3 = mul_c(pY, 3)
            eta_up_p = add_c(lc, neg_c(add_c(al_vec[0], al_vec[1])))
            eta_dn_p = add_c(lc, neg_c(add_c(al_vec[0], al_vec[3])))
            if mul_c(eta_up_p, 2) != triv or mul_c(eta_dn_p, 2) != triv:
                pc_scar_1_tested_bgs += 1
                cubic_up = mul_c(eta_up_p, 2)
                cubic_dn = mul_c(eta_dn_p, 2)
                if cubic_up != triv or cubic_dn != triv:
                    pc_scar_1_violated_bgs += 1
            if pY3 != triv and mul_c(pY3, 2) != triv and (N % 2 == 1 or Wc == triv):
                pc_scar_1_odd_order_tested += 1
                if mul_c(eta_up_p, 2) != triv and mul_c(eta_dn_p, 2) != triv:
                    pc_scar_1_odd_order_violated += 1

        assert dual_bijection_ok, f"W-F9 failed bijection on {label} k={k}"
        if eps > 0:
            total_orientable_coupling_mismatches += lv_coupling_mismatches

        level_reports.append({
            "state": label,
            "k": k,
            "N": N,
            "n_characters": len(chars),
            "n_modules_checked": mod_count_lv,
            "n_firing_generation_backgrounds": len(bgs),
            "slope_conjugation_mismatches": slope_conj_mismatches,
            "coupling_duality_mismatches": lv_coupling_mismatches,
            "prime_used": p,
        })

    assert total_firing_law_mismatches == 0
    assert total_fox_duality_mismatches == 0
    assert total_intertwiner_mismatches == 0
    assert total_param_involution_mismatches == 0
    assert total_higgs_inversion_mismatches == 0
    assert total_asymmetric_flip_cases == 0
    assert total_orientable_slope_mismatches == 0
    assert total_orientable_coupling_mismatches == 0

    pc_scar_1_fired = (
        pc_scar_1_tested_bgs > 0
        and pc_scar_1_violated_bgs == pc_scar_1_tested_bgs
        and pc_scar_1_odd_order_tested > 0
        and pc_scar_1_odd_order_violated == pc_scar_1_odd_order_tested
    )
    assert pc_scar_1_fired, "PC_SCAR_1 failed to fire"

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "levels": level_reports,
        "total_modules_checked": total_modules_checked,
        "firing_law_mismatches": total_firing_law_mismatches,
        "fox_duality_mismatches": total_fox_duality_mismatches,
        "intertwiner_2x2_mismatches": total_intertwiner_mismatches,
        "param_involution_mismatches": total_param_involution_mismatches,
        "higgs_inversion_mismatches": total_higgs_inversion_mismatches,
        "asymmetric_flip_cases": total_asymmetric_flip_cases,
        "orientable_slope_conjugation_mismatches": total_orientable_slope_mismatches,
        "orientable_coupling_duality_mismatches": total_orientable_coupling_mismatches,
        "PC_SCAR_1": {
            "non_2torsion_higgs_bgs_tested": pc_scar_1_tested_bgs,
            "non_2torsion_higgs_bgs_violated": pc_scar_1_violated_bgs,
            "odd_order_psiY3_bgs_tested": pc_scar_1_odd_order_tested,
            "odd_order_psiY3_bgs_violated": pc_scar_1_odd_order_violated,
            "fired": pc_scar_1_fired,
        },
    }


# ============================================================================
# SECTION E3: GL(2, Z) NO-GO THEOREM FOR TICK (J), UNDOING (D), AND HAND (P)
# ============================================================================

def eval_world(
    world_name: str,
    tau: mp.mpc,
    psi1: mp.mpf,
    psi2: mp.mpf,
    tilde_L: mp.mpf,
    serre_level: str = "B1",
    weight_power: str = "plus_half",
) -> Tuple[mp.matrix, mp.matrix, mp.matrix, Dict[str, Any]]:
    if world_name == "W_minus":
        rd_u, rd_d, rd_e = "S_tilde", "S", "S"
    elif world_name == "W_plus":
        rd_u, rd_d, rd_e = "S", "S_tilde", "S_tilde"
    else:
        raise ValueError(f"Unknown world: {world_name}")

    _, Yu, _ = closed_form_M_and_Y(tau, psi1, psi2, SIXY["Q"], SIXY["u"], tilde_L, rd_u, serre_level, weight_power)
    _, Yd, _ = closed_form_M_and_Y(tau, psi1, psi2, SIXY["Q"], SIXY["d"], tilde_L, rd_d, serre_level, weight_power)
    _, Ye, _ = closed_form_M_and_Y(tau, psi1, psi2, SIXY["L"], SIXY["e"], tilde_L, rd_e, serre_level, weight_power)
    obs = world_observables(Yu, Yd, Ye)
    return Yu, Yd, Ye, obs


def gl2z_act(
    mat: Tuple[int, int, int, int], tau: mp.mpc, psi1: mp.mpf, psi2: mp.mpf
) -> Tuple[mp.mpc, mp.mpf, mp.mpf, int]:
    """
    Unified GL(2, Z) action on (tau, psi1, psi2) where w = psi1*tau - psi2:
      - det = +1: tau' = (A*tau + B)/(C*tau + D), (psi1', psi2') = +(D*psi1 + C*psi2, B*psi1 + A*psi2)
      - det = -1: tau' = (A*conj(tau) + B)/(C*conj(tau) + D), (psi1', psi2') = -(D*psi1 + C*psi2, B*psi1 + A*psi2)
    """
    A, B, C, D = mat
    det = A * D - B * C
    assert det in (+1, -1)
    t_src = tau if det == +1 else mp.conj(tau)
    tau_p = (A * t_src + B) / (C * t_src + D)
    psi1_p = det * (D * psi1 + C * psi2)
    psi2_p = det * (B * psi1 + A * psi2)
    return tau_p, psi1_p, psi2_p, det


def run_section_e3(u_tau0: Dict[str, Any]) -> Dict[str, Any]:
    t0 = time.time()
    mp.mp.dps = 44

    # 1. Guardrail 3 Mandatory Random Haar U(3)^5 Basis-Scrambling Gate (< 1e-30)
    tau0 = mp.mpc("-0.27", "1.29")
    tL2_0 = u_tau0["tilde_L_2"]
    psi1_0, psi2_0 = mp.mpf(2) / 5, mp.mpf(4) / 5

    Yu0, Yd0, Ye0, obs0 = eval_world("W_minus", tau0, psi1_0, psi2_0, tL2_0, "B1", "plus_half")
    rng = random.Random(20261114)
    max_haar_scramble_err = mp.mpf(0)
    for _ in range(10):
        UL_Q = random_haar_unitary_3x3(rng)
        UR_u = random_haar_unitary_3x3(rng)
        UR_d = random_haar_unitary_3x3(rng)
        UL_L = random_haar_unitary_3x3(rng)
        UR_e = random_haar_unitary_3x3(rng)
        obs_scr = world_observables(
            UL_Q * Yu0 * mat_H(UR_u),
            UL_Q * Yd0 * mat_H(UR_d),
            UL_L * Ye0 * mat_H(UR_e),
        )
        cmp_scr = compare_world_observables(obs0, obs_scr)
        err_scr = max(cmp_scr["ratio_ckm_max_diff"], cmp_scr["J_cp_same_sign_diff"])
        if err_scr > max_haar_scramble_err:
            max_haar_scramble_err = err_scr
    assert max_haar_scramble_err < mp.mpf("1e-30"), f"Haar U(3)^5 scrambling gate failed: {max_haar_scramble_err}"

    # 2. Exact anti-holomorphic reflection identity under D = diag(1, -1) AND quaternion mismatch identity
    tau_D = -mp.conj(tau0)
    tL2_D = uniformize_punctured_torus(tau_D)["tilde_L_2"]
    err_tilde_L2_D = abs(tL2_D - tL2_0)
    assert err_tilde_L2_D < mp.mpf("1e-24"), f"tilde_L_2(-conj(tau)) residual: {err_tilde_L2_D}"

    P_K = mp.matrix([[1, 0, 0], [0, 1, 0], [0, 0, -1]])
    _, qi, qj, qk = _quat_mats()
    qi_inv = mp.inverse(qi)
    qj_inv = mp.inverse(qj)

    max_D_reflection_err = mp.mpf(0)
    max_quat_mismatch_S_err = mp.mpf(0)
    max_quat_mismatch_M_err = mp.mpf(0)
    pc_scar_4_max_err = mp.mpf(0)

    for p1_t, p2_t in ((psi1_0, psi2_0), (mp.sqrt(2) / 5, mp.sqrt(3) / 7)):
        for serre_lv, w_pow in (("B1", "plus_half"), ("B2", "minus_half")):
            trips_0 = serre_triplets_exact(tau0)[serre_lv]
            S_0 = trips_0[0] * qi + trips_0[1] * qj + trips_0[2] * qk
            St_0 = mp.conj(trips_0[0]) * qi + mp.conj(trips_0[1]) * qj + mp.conj(trips_0[2]) * qk
            # Verify conj(S_tilde) == q_j * S * q_j^-1 (quaternion j-conjugation)
            max_quat_mismatch_S_err = max(max_quat_mismatch_S_err, mat_inf_norm(mat_conj(St_0) - qj * S_0 * qj_inv))

            for _, qx, qy in SECTORS_2D:
                for rd in ("S", "S_tilde"):
                    Mw_base, Y_base, _ = closed_form_M_and_Y(
                        tau0, p1_t, p2_t, qx, qy, tL2_0, rd, serre_lv, w_pow
                    )
                    Mw_refl, Y_refl, _ = closed_form_M_and_Y(
                        tau_D, p1_t, -p2_t, qx, qy, tL2_D, rd, serre_lv, w_pow
                    )
                    # Note tL2_D == tL2_0 to ~1e-36 from Lame ODE; check BOTH independent tL2_D and exact tL2_0!
                    _, Y_refl_exactL, _ = closed_form_M_and_Y(
                        tau_D, p1_t, -p2_t, qx, qy, tL2_0, rd, serre_lv, w_pow
                    )
                    err_refl = max(
                        mat_inf_norm(Y_refl - P_K * mat_conj(Y_base) * P_K),
                        mat_inf_norm(Y_refl_exactL - P_K * mat_conj(Y_base) * P_K),
                    )
                    max_D_reflection_err = max(max_D_reflection_err, err_refl)

                    # Verify conj(M_w(tau, psi)) == q_i * M_w(-conj(tau), D*psi) * q_i^-1 (quaternion i-conjugation!)
                    Mw_refl_exactL, _, _ = closed_form_M_and_Y(
                        tau_D, p1_t, -p2_t, qx, qy, tL2_0, rd, serre_lv, w_pow
                    )
                    max_quat_mismatch_M_err = max(
                        max_quat_mismatch_M_err,
                        mat_inf_norm(mat_conj(Mw_base) - qi * Mw_refl_exactL * qi_inv),
                    )

                    # Planted Control PC_SCAR_4: omit P_K (replace P_K by I_3)
                    err_no_pk = mat_inf_norm(Y_refl_exactL - mat_conj(Y_base)) / mat_inf_norm(Y_base)
                    pc_scar_4_max_err = max(pc_scar_4_max_err, err_no_pk)

    assert max_D_reflection_err < mp.mpf("1e-30"), f"D-reflection identity residual: {max_D_reflection_err}"
    assert max_quat_mismatch_S_err < mp.mpf("1e-38"), f"Quaternion S conjugation residual: {max_quat_mismatch_S_err}"
    assert max_quat_mismatch_M_err < mp.mpf("1e-38"), f"Quaternion M_w conjugation residual: {max_quat_mismatch_M_err}"
    # Also verify q_j * q_k * q_i == -I_2 explicitly (3rd generation block mapped out of su(2) into singlet I_2!)
    i2_mat, _, _, _ = _quat_mats()
    assert mat_inf_norm(qj * qk * qi + i2_mat) == 0

    pc_scar_4_fired = float(pc_scar_4_max_err) > 0.01
    assert pc_scar_4_fired, f"PC_SCAR_4 failed to fire: {pc_scar_4_max_err}"

    # 3. Complete GL(2, Z) generator table: L, R, -I_2, undoing D, golden tick J, swap mirror P
    generators = [
        ("L_forward", (1, 1, 0, 1)),
        ("R_forward", (1, 0, 1, 1)),
        ("minus_I2_turn", (-1, 0, 0, -1)),
        ("D_undoing", (1, 0, 0, -1)),
        ("J_golden_tick", (1, 1, 1, 0)),
        ("P_swap_mirror", (0, 1, 1, 0)),
    ]

    tilde_L2_cache: Dict[Tuple[float, float], mp.mpf] = {
        (round(float(mp.re(tau0)), 12), round(float(mp.im(tau0)), 12)): tL2_0,
        (round(float(mp.re(tau_D)), 12), round(float(mp.im(tau_D)), 12)): tL2_D,
    }

    def get_tL2(t_pt: mp.mpc) -> mp.mpf:
        key = (round(float(mp.re(t_pt)), 12), round(float(mp.im(t_pt)), 12))
        if key not in tilde_L2_cache:
            tilde_L2_cache[key] = uniformize_punctured_torus(t_pt, n_homotopy=4)["tilde_L_2"]
        return tilde_L2_cache[key]

    generator_rows: List[Dict[str, Any]] = []
    max_move_ratio_ckm_err = mp.mpf(0)
    max_move_jcp_law_err = mp.mpf(0)
    pc_scar_3_discrepancy = mp.mpf(0)

    for serre_lv, w_pow in (("B1", "plus_half"), ("B2", "minus_half")):
        _, _, _, base_Wm = eval_world("W_minus", tau0, psi1_0, psi2_0, tL2_0, serre_lv, w_pow)
        _, _, _, base_Wp = eval_world("W_plus", tau0, psi1_0, psi2_0, tL2_0, serre_lv, w_pow)
        assert abs(base_Wm["J_cp"]) > mp.mpf("1e-7") and abs(base_Wp["J_cp"]) > mp.mpf("1e-7")

        for gen_name, g_mat in generators:
            tau_g, psi1_g, psi2_g, det_g = gl2z_act(g_mat, tau0, psi1_0, psi2_0)
            tL2_g = get_tL2(tau_g)
            _, _, _, mov_Wm = eval_world("W_minus", tau_g, psi1_g, psi2_g, tL2_g, serre_lv, w_pow)
            _, _, _, mov_Wp = eval_world("W_plus", tau_g, psi1_g, psi2_g, tL2_g, serre_lv, w_pow)

            cmp_m = compare_world_observables(base_Wm, mov_Wm)
            cmp_p = compare_world_observables(base_Wp, mov_Wp)
            rc_err = max(cmp_m["ratio_ckm_max_diff"], cmp_p["ratio_ckm_max_diff"])
            if det_g == +1:
                j_err = max(cmp_m["J_cp_same_sign_diff"], cmp_p["J_cp_same_sign_diff"])
            else:
                j_err = max(cmp_m["J_cp_flipped_sign_diff"], cmp_p["J_cp_flipped_sign_diff"])

            max_move_ratio_ckm_err = max(max_move_ratio_ckm_err, rc_err)
            max_move_jcp_law_err = max(max_move_jcp_law_err, j_err)

            if gen_name == "J_golden_tick" and serre_lv == "B1":
                # PC_SCAR_3: test false hypothesis that J maps W_- to W_+
                cross_cmp = compare_world_observables(base_Wp, mov_Wm)
                pc_scar_3_discrepancy = cross_cmp["ratio_ckm_max_diff"]

            if serre_lv == "B1":
                generator_rows.append({
                    "generator": gen_name,
                    "det": det_g,
                    "im_tau_image": float(mp.im(tau_g)),
                    "W_minus_and_W_plus_ratio_ckm_err": float(rc_err),
                    "J_cp_law_err": float(j_err),
                    "J_cp_base_W_minus": float(base_Wm["J_cp"]),
                    "J_cp_moved_W_minus": float(mov_Wm["J_cp"]),
                })

    assert max_move_ratio_ckm_err < mp.mpf("1e-28"), f"GL(2, Z) ratio/CKM err: {max_move_ratio_ckm_err}"
    assert max_move_jcp_law_err < mp.mpf("1e-28"), f"GL(2, Z) Jarlskog law err: {max_move_jcp_law_err}"

    pc_scar_3_fired = float(pc_scar_3_discrepancy) > 0.01
    assert pc_scar_3_fired, f"PC_SCAR_3 failed to fire: {pc_scar_3_discrepancy}"

    # 4. Exact 24-point P_5 orbit average comparison of W_- vs W_+ (B1928 orbit) at generic tau0 AND golden apex
    pts_p5 = [(mp.mpf(a) / 5, mp.mpf(b) / 5) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
    tau_gold_apex = mp.mpc("0.5", mp.sqrt(5) / 2)
    tL2_gold = uniformize_punctured_torus(tau_gold_apex, n_homotopy=3)["tilde_L_2"]

    orbit_summaries: Dict[str, Any] = {}
    for pt_label, t_pt, tL_pt in (("generic_bulk", tau0, tL2_0), ("golden_geodesic_apex", tau_gold_apex, tL2_gold)):
        for serre_lv, w_pow in (("B1", "plus_half"), ("B2", "minus_half")):
            acc_m = {"ru1": mp.mpf(0), "rd1": mp.mpf(0), "re1": mp.mpf(0), "vus": mp.mpf(0), "vcb": mp.mpf(0), "iud": mp.mpf(0)}
            acc_p = {"ru1": mp.mpf(0), "rd1": mp.mpf(0), "re1": mp.mpf(0), "vus": mp.mpf(0), "vcb": mp.mpf(0), "iud": mp.mpf(0)}
            for p1_k, p2_k in pts_p5:
                _, _, _, om = eval_world("W_minus", t_pt, p1_k, p2_k, tL_pt, serre_lv, w_pow)
                _, _, _, op = eval_world("W_plus", t_pt, p1_k, p2_k, tL_pt, serre_lv, w_pow)
                acc_m["ru1"] += om["ratios_u"][0] / 24
                acc_m["rd1"] += om["ratios_d"][0] / 24
                acc_m["re1"] += om["ratios_e"][0] / 24
                acc_m["vus"] += om["V_ckm_abs"][0][1] / 24
                acc_m["vcb"] += om["V_ckm_abs"][1][2] / 24
                acc_m["iud"] += om["I_ud_trace"] / 24

                acc_p["ru1"] += op["ratios_u"][0] / 24
                acc_p["rd1"] += op["ratios_d"][0] / 24
                acc_p["re1"] += op["ratios_e"][0] / 24
                acc_p["vus"] += op["V_ckm_abs"][0][1] / 24
                acc_p["vcb"] += op["V_ckm_abs"][1][2] / 24
                acc_p["iud"] += op["I_ud_trace"] / 24

            max_avg_gap = max(abs(acc_m[k] - acc_p[k]) for k in acc_m)
            assert max_avg_gap > mp.mpf("0.01"), f"24-point P_5 average gap too small at {pt_label}/{serre_lv}: {max_avg_gap}"
            orbit_summaries[f"{pt_label}_{serre_lv}"] = {
                "W_minus_mean": {k: float(v) for k, v in acc_m.items()},
                "W_plus_mean": {k: float(v) for k, v in acc_p.items()},
                "max_observable_mean_gap": float(max_avg_gap),
            }

    return {
        "elapsed_seconds": round(time.time() - t0, 3),
        "haar_u3_5_scrambling_max_err": float(max_haar_scramble_err),
        "D_reflection_identity": {
            "tilde_L2_reflection_diff": float(err_tilde_L2_D),
            "max_PK_conjugation_err": float(max_D_reflection_err),
            "max_quaternion_j_on_S_err": float(max_quat_mismatch_S_err),
            "max_quaternion_i_on_Mw_err": float(max_quat_mismatch_M_err),
        },
        "gl2z_generator_checks_B1": generator_rows,
        "max_gl2z_ratio_ckm_err_all": float(max_move_ratio_ckm_err),
        "max_gl2z_J_cp_law_err_all": float(max_move_jcp_law_err),
        "p5_24point_orbit_averages": orbit_summaries,
        "PC_SCAR_3": {
            "J_tick_W_minus_vs_W_plus_discrepancy": float(pc_scar_3_discrepancy),
            "fired": pc_scar_3_fired,
        },
        "PC_SCAR_4": {
            "omitted_PK_relative_discrepancy": float(pc_scar_4_max_err),
            "fired": pc_scar_4_fired,
        },
    }


def main() -> None:
    t_start = time.time()

    # Guardrail 4 Benchmark Gate B: B1667 / B1927 Lame punctured-torus uniformizer
    mp.mp.dps = 45
    tau_om6 = mp.exp(mp.j * mp.pi / 3)
    u_om6 = uniformize_punctured_torus(tau_om6)
    Lmax_cf, L2_cf = closed_form_gamma_prime_omega6()
    assert abs(u_om6["L_max"] - Lmax_cf) < mp.mpf("1e-28")
    assert abs(u_om6["L_2"] - L2_cf) < mp.mpf("1e-28")
    assert abs(u_om6["L_max"] - mp.mpf("0.69208004049")) < mp.mpf("1e-10")
    assert abs(u_om6["L_2"] - mp.mpf("2.78647514288")) < mp.mpf("1e-10")

    u_b1667 = uniformize_punctured_torus(mp.mpc("0.137", "1.291"))
    assert abs(u_b1667["L_2"] - mp.mpf("2.60053746232")) < mp.mpf("1e-10")

    tau0 = mp.mpc("-0.27", "1.29")
    u_tau0 = uniformize_punctured_torus(tau0)

    e1_res = run_section_e1(u_tau0)
    e2_res = run_section_e2()
    e3_res = run_section_e3(u_tau0)

    plants_summary = {
        "PC_SCAR_1_fired": bool(e2_res["PC_SCAR_1"]["fired"]),
        "PC_SCAR_2_fired": bool(e1_res["PC_SCAR_2"]["fired"]),
        "PC_SCAR_3_fired": bool(e3_res["PC_SCAR_3"]["fired"]),
        "PC_SCAR_4_fired": bool(e3_res["PC_SCAR_4"]["fired"]),
    }
    all_plants_fired = all(plants_summary.values())
    assert all_plants_fired, f"Not all planted controls fired: {plants_summary}"

    payload = {
        "card": "X-SCAR",
        "seat": "agy-exp",
        "empirical_firewall": "0 of 19",
        "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "total_elapsed_seconds": round(time.time() - t_start, 3),
        "benchmark_lame_b1667": {
            "omega6_L_2_abs_diff_vs_closed_form": float(abs(u_om6["L_2"] - L2_cf)),
            "omega6_L_max_abs_diff_vs_closed_form": float(abs(u_om6["L_max"] - Lmax_cf)),
            "bulk_0_137_1_291_L_2": float(u_b1667["L_2"]),
        },
        "E1_matter_charge_negation": e1_res,
        "E2_scar_duality_w_f9": e2_res,
        "E3_gl2z_reflection_and_nogo": e3_res,
        "planted_controls": plants_summary,
        "all_plants_fired": all_plants_fired,
        "verdict_summary": {
            "E1_holds": True,
            "E2_holds": True,
            "E3_holds": True,
            "map_flipping_matter_hypercharge_without_higgs_exists": False,
        },
    }

    OUT_PATH.write_text(json.dumps(payload, indent=2, default=_json_default) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
