#!/usr/bin/env python3
"""Self-contained post-run Cauchy-contour diagnostic for Row 1516's Laurent constant a_0.

Purpose:
  In first-run commit e163762c0 of verify_x_c2.py (committed at 29d4845da), every mathematical
  identity and integer count in Row 1516 (@ e40d0fb1) passed to 49-50 digits EXCEPT line 688
  (`max_a0_err < 1e-35`), because lines 488-490 extracted the Laurent constant term a_0 of
  K_s(u) = 1/u + a_0 + a_1 u + a_2 u^2 + ... via a 2-point symmetric average at r = 10^-6,
  whose O(r^2) = a_2 * 10^-12 truncation error cannot fall below 10^-35.

  Preserving commits 29d4845da and e163762c0 untouched in git history, this standalone script
  (zero imports from verify_x_c2.py or any seat/main module) evaluates:
    1. Planted negative control: wrong sign (-d_u log theta[c_s](0)) must fail with O(1) error.
    2. The exact 2-point r = 10^-6 stencil error (confirming O(10^-12) truncation).
    3. A 32-point Cauchy contour mean around |u| = 1/100 (confirming |a_0_cauchy - a_0_exact| < 10^-45).
    4. Explicit log10 error/magnitude diagnostics for the remaining Row 1516 checks whose booleans
       passed in verify_x_c2.py (`sigma_b` order-8 magnitude & 1/2 decay exponent, and Re(tau)=0
       channel-isotropy spreads on the 18 matter lines and 8 doublet lines).
"""
from __future__ import annotations

import json
import math
import pathlib
import sys
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 50
I = mp.mpc(0, 1)
PI = mp.pi

OUT_JSON = pathlib.Path(__file__).resolve().parent / "postrun_a0_cauchy_out.json"


def frac_part(x: Fraction) -> Fraction:
    return x - math.floor(x)


def theta_char(a: Fraction, b: Fraction, u: mp.mpc, tau: mp.mpc, n_lim: int = 16) -> mp.mpc:
    am = mp.mpf(a.numerator) / a.denominator
    bm = mp.mpf(b.numerator) / b.denominator
    terms = []
    for n in range(-n_lim, n_lim + 1):
        na = mp.mpf(n) + am
        terms.append(mp.exp(I * PI * tau * (na * na) + 2 * I * PI * na * (u + bm)))
    return mp.fsum(terms)


def theta_char_du0(a: Fraction, b: Fraction, tau: mp.mpc, n_lim: int = 16) -> mp.mpc:
    am = mp.mpf(a.numerator) / a.denominator
    bm = mp.mpf(b.numerator) / b.denominator
    terms = []
    for n in range(-n_lim, n_lim + 1):
        na = mp.mpf(n) + am
        terms.append((2 * I * PI * na) * mp.exp(I * PI * tau * (na * na) + 2 * I * PI * na * bm))
    return mp.fsum(terms)


def theta1(u: mp.mpc, tau: mp.mpc, n_lim: int = 16) -> mp.mpc:
    terms = []
    for k in range(-n_lim, n_lim):
        kh = mp.mpf(k) + mp.mpf(1) / 2
        sign = -1 if (k % 2 != 0) else 1
        terms.append(sign * mp.exp(I * PI * tau * (kh * kh) + 2 * I * PI * kh * u))
    return -I * mp.fsum(terms)


def theta1_du0(tau: mp.mpc, n_lim: int = 16) -> mp.mpc:
    terms = []
    for k in range(-n_lim, n_lim):
        kh = mp.mpf(k) + mp.mpf(1) / 2
        sign = -1 if (k % 2 != 0) else 1
        terms.append(sign * (2 * k + 1) * mp.exp(I * PI * tau * (kh * kh)))
    return PI * mp.fsum(terms)


def bilinear_channels(ax: Fraction, bx: Fraction, ay: Fraction, by: Fraction,
                      u: mp.mpc, tau: mp.mpc, n_lim: int = 16) -> dict[str, mp.mpc]:
    T = 2 * tau
    X0 = theta_char(ax, bx, u, T, n_lim)
    X1 = theta_char(ax, bx, u + tau, T, n_lim)
    Y0 = theta_char(ay, by, u, T, n_lim)
    Y1 = theta_char(ay, by, u + tau, T, n_lim)
    t1 = theta1(u, tau, n_lim)
    t1_tau = theta1(u + tau, tau, n_lim)
    den = I * mp.exp(-I * PI * tau / 2 - I * PI * u) * t1
    ph_x = mp.exp(I * PI * (mp.mpf(bx.numerator) / bx.denominator))
    ph_y = mp.exp(I * PI * (mp.mpf(by.numerator) / by.denominator))
    ph_xy = mp.exp(I * PI * (mp.mpf((bx + by).numerator) / (bx + by).denominator))
    b00 = (X0 * Y0) / t1
    b01 = ph_y * (X0 * Y1) / den
    b10 = ph_x * (X1 * Y0) / den
    b11 = ph_xy * (X1 * Y1) / t1_tau
    return {
        "1": b01 - b10,
        "i": -I * (b01 + b10),
        "j": -(b00 + b11),
        "k": I * (b00 - b11),
    }


def bilinear_residues(ax: Fraction, bx: Fraction, ay: Fraction, by: Fraction,
                      tau: mp.mpc, n_lim: int = 16) -> dict[str, mp.mpc]:
    T = 2 * tau
    X0 = theta_char(ax, bx, mp.mpc(0), T, n_lim)
    X1 = theta_char(ax, bx, tau, T, n_lim)
    Y0 = theta_char(ay, by, mp.mpc(0), T, n_lim)
    Y1 = theta_char(ay, by, tau, T, n_lim)
    th1p = theta1_du0(tau, n_lim)
    ph_x = mp.exp(I * PI * (mp.mpf(bx.numerator) / bx.denominator))
    ph_y = mp.exp(I * PI * (mp.mpf(by.numerator) / by.denominator))
    ph_xy = mp.exp(I * PI * (mp.mpf((bx + by).numerator) / (bx + by).denominator))
    emt2 = mp.exp(-I * PI * tau / 2)
    emt = mp.exp(-I * PI * tau)
    r00 = (X0 * Y0) / th1p
    r01 = ph_y * (X0 * Y1) / (I * emt2 * th1p)
    r10 = ph_x * (X1 * Y0) / (I * emt2 * th1p)
    r11 = ph_xy * (X1 * Y1) / (-emt * th1p)
    return {
        "1": r01 - r10,
        "i": -I * (r01 + r10),
        "j": -(r00 + r11),
        "k": I * (r00 - r11),
    }


def w177_c_inf(lam: Fraction) -> mp.mpf:
    lm = mp.mpf(lam.numerator) / lam.denominator
    return -2 * PI * mp.log(2 * PI) - 2 * PI * mp.euler - PI * (mp.digamma(lm) + mp.digamma(1 - lm))


def w177_series(lam: Fraction, mu: Fraction, tau: mp.mpc, n_terms: int = 60) -> mp.mpf:
    lm = mp.mpf(lam.numerator) / lam.denominator
    mm = mp.mpf(mu.numerator) / mu.denominator
    im_t = mp.im(tau)
    re_t = mp.re(tau)
    c0 = w177_c_inf(lam)
    acc = []
    for n in range(-n_terms, n_terms + 1):
        nl = mp.mpf(n) + lm
        anl = abs(nl)
        rho = mp.exp(-2 * PI * anl * im_t)
        phi = 2 * PI * (nl * re_t - mm)
        P_val = (1 - rho * rho) / (1 - 2 * rho * mp.cos(phi) + rho * rho)
        acc.append((P_val - 1) / anl)
    return c0 + PI * mp.fsum(acc)


def main() -> int:
    char_shifts = {
        "k": (Fraction(0), Fraction(0)),
        "j": (Fraction(0), Fraction(1, 2)),
        "i": (Fraction(1, 2), Fraction(0)),
        "1": (Fraction(1, 2), Fraction(1, 2)),
    }
    test_cases = [
        (Fraction(2, 7), Fraction(1, 5), Fraction(-5, 11), Fraction(3, 7), mp.mpc("0.19", "1.43")),
        (Fraction(3, 8), Fraction(5, 12), Fraction(1, 9), Fraction(-2, 5), mp.mpc("-0.23", "1.77")),
        (Fraction(1, 13), Fraction(4, 9), Fraction(2, 11), Fraction(1, 6), mp.mpc("0.31", "2.11")),
        (Fraction(-3, 10), Fraction(2, 7), Fraction(4, 15), Fraction(-1, 8), mp.mpc("0.09", "1.61")),
    ]

    max_2pt_err = mp.mpf(0)
    max_cauchy32_err = mp.mpf(0)
    max_wrong_sign_err = mp.mpf(0)

    n_pts = 32
    rad_cauchy = mp.mpf(1) / 100
    circle_pts = [rad_cauchy * mp.exp(2 * I * PI * mp.mpf(m) / n_pts) for m in range(n_pts)]
    rad_2pt = mp.mpf("1e-6")

    for ax, bx, ay, by, tau in test_cases:
        aS = ax + ay
        bS = bx + by
        R_s = bilinear_residues(ax, bx, ay, by, tau)
        P_pos = bilinear_channels(ax, bx, ay, by, rad_2pt, tau)
        P_neg = bilinear_channels(ax, bx, ay, by, -rad_2pt, tau)
        P_circle = [bilinear_channels(ax, bx, ay, by, z, tau) for z in circle_pts]

        for s, (al_s, be_s) in char_shifts.items():
            c_a = aS + al_s
            c_b = bS / 2 + be_s
            a0_exact = theta_char_du0(c_a, c_b, tau) / theta_char(c_a, c_b, mp.mpc(0), tau)
            a0_2pt = ((P_pos[s] / R_s[s] - 1 / rad_2pt) + (P_neg[s] / R_s[s] + 1 / rad_2pt)) / 2
            a0_cauchy = mp.fsum(P_circle[m][s] / R_s[s] for m in range(n_pts)) / n_pts
            max_2pt_err = max(max_2pt_err, abs(a0_2pt - a0_exact))
            max_cauchy32_err = max(max_cauchy32_err, abs(a0_cauchy - a0_exact))
            max_wrong_sign_err = max(max_wrong_sign_err, abs(a0_cauchy - (-a0_exact)))

    control_fired = bool(max_wrong_sign_err > mp.mpf("1e-1"))
    if not control_fired:
        sys.stderr.write("PLANTED CONTROL FAILED TO FIRE\n")
        return 2

    # Additional diagnostics for Row 1516 checks whose booleans passed in verify_x_c2.py
    reps = set()
    for N in range(1, 13):
        for i in range(N):
            for j in range(N):
                p1, p2 = Fraction(i, N), Fraction(j, N)
                reps.add(min((p1, p2), (frac_part(-p1), frac_part(-p2))))

    order8_nonint = [
        w for w in sorted(reps)
        if frac_part(6 * w[0]) == Fraction(1, 2) and (12 * w[1]).denominator != 1
    ]
    matter_zero_lines = [
        w for w in sorted(reps)
        if (12 * w[0]).denominator == 1 and (12 * w[0]).numerator % 2 == 1
        and (12 * w[1]).denominator == 1 and (12 * w[1]).numerator % 2 == 1
    ]
    doublet_zero_lines = [
        w for w in sorted(reps)
        if (24 * w[0]).denominator == 1 and (24 * w[0]).numerator % 2 == 1
        and (24 * w[1]).denominator == 1 and (24 * w[1]).numerator % 2 == 1
    ]

    tau_b1 = mp.mpc("0.13", "1.9")
    sigma_b_min_abs = mp.mpf("1e9")
    sigma_b_exp_err = mp.mpf(0)
    for p1, p2 in order8_nonint:
        aS, bS = -3 * p1, 6 * p2
        Lam, Lam_p = frac_part(aS + Fraction(1, 2)), frac_part(aS)
        M_val = frac_part(Fraction(1, 2) - bS / 2)
        sb1 = 2 * (w177_series(Lam, frac_part(2 * M_val), 2 * tau_b1) - w177_series(Lam_p, frac_part(2 * M_val), 2 * tau_b1))
        sigma_b_min_abs = min(sigma_b_min_abs, abs(sb1))
        sb6 = 2 * (w177_series(Lam, frac_part(2 * M_val), 2 * mp.mpc("0.13", "6.0")) - w177_series(Lam_p, frac_part(2 * M_val), 2 * mp.mpc("0.13", "6.0")))
        sb7 = 2 * (w177_series(Lam, frac_part(2 * M_val), 2 * mp.mpc("0.13", "7.0")) - w177_series(Lam_p, frac_part(2 * M_val), 2 * mp.mpc("0.13", "7.0")))
        fitted_E = -mp.log(abs(sb7 / sb6)) / (2 * PI)
        sigma_b_exp_err = max(sigma_b_exp_err, abs(fitted_E - mp.mpf("0.5")))

    tau_re0 = mp.mpc("0", "2.2")
    max_re0_matter_spread = mp.mpf(0)
    for p1, p2 in matter_zero_lines:
        for qsum in (-3, 3):
            aS, bS = qsum * p1, -2 * qsum * p2
            Lam, Lam_p = frac_part(aS + Fraction(1, 2)), frac_part(aS)
            M_val = frac_part(Fraction(1, 2) - bS / 2)
            vals = [
                w177_series(Lam, M_val, tau_re0),
                w177_series(Lam, frac_part(M_val - Fraction(1, 2)), tau_re0),
                w177_series(Lam_p, M_val, tau_re0),
                w177_series(Lam_p, frac_part(M_val - Fraction(1, 2)), tau_re0),
            ]
            max_re0_matter_spread = max(max_re0_matter_spread, max(vals) - min(vals))

    max_re0_doublet_spread = mp.mpf(0)
    for p1, p2 in doublet_zero_lines:
        aS, bS = -6 * p1, 12 * p2
        Lam, Lam_p = frac_part(aS + Fraction(1, 2)), frac_part(aS)
        M_val = frac_part(Fraction(1, 2) - bS / 2)
        vals = [
            w177_series(Lam, M_val, tau_re0),
            w177_series(Lam, frac_part(M_val - Fraction(1, 2)), tau_re0),
            w177_series(Lam_p, M_val, tau_re0),
        ]
        max_re0_doublet_spread = max(max_re0_doublet_spread, max(vals) - min(vals))

    payload = {
        "row": 1516,
        "commit_read": "e40d0fb1",
        "purpose": "Resolve 2-point O(r^2) stencil bug on Laurent constant a_0 in e163762c0 via 32-point Cauchy contour mean",
        "control_wrong_sign_fired": control_fired,
        "two_point_r_1e_6_err_log10": int(mp.floor(mp.log10(max_2pt_err + mp.mpf("1e-50")))),
        "cauchy_32pt_r_1e_2_err_log10": int(mp.floor(mp.log10(max_cauchy32_err + mp.mpf("1e-50")))),
        "cauchy_a0_passes_1e_45": bool(max_cauchy32_err < mp.mpf("1e-45")),
        "order8_nonint_lines": [f"({w[0]}, {w[1]})" for w in order8_nonint],
        "sigma_b_order8_min_abs_log10": int(mp.floor(mp.log10(sigma_b_min_abs))),
        "sigma_b_exp_err_log10": int(mp.floor(mp.log10(sigma_b_exp_err + mp.mpf("1e-50")))),
        "re0_matter_18_lines_spread_log10": int(mp.floor(mp.log10(max_re0_matter_spread + mp.mpf("1e-50")))),
        "re0_doublet_8_lines_spread_log10": int(mp.floor(mp.log10(max_re0_doublet_spread + mp.mpf("1e-50")))),
        "all_pure_math_claims_reproduced": bool(
            max_cauchy32_err < mp.mpf("1e-45")
            and sigma_b_min_abs > mp.mpf("1e-2")
            and sigma_b_exp_err < mp.mpf("1e-8")
            and max_re0_matter_spread < mp.mpf("1e-45")
            and max_re0_doublet_spread < mp.mpf("1e-45")
        ),
    }
    OUT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
