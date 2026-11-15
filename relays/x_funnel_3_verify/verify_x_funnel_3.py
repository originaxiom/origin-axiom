#!/usr/bin/env python3
"""
Standalone Zero-Import Verifier for Card X-FUNNEL-3 (0 of 19).

Verifies:
  Part 3A: Two-route Kronecker division cancellation sum_{w in P_5} ln det'(-Delta_{tau, qw}) = 2 ln 5
           for all non-divisible charges q in {1, 2, 3, 4, 6}, plus Raabe B_2 cusp-slope inversion on O_4.
  Part 3B: 24-point shifted-lattice Epstein Z(tau; qw; 3) and character-winding E*(tau; qw; 3) sublattice
           identities, AST-verified target-free critical-point search on untwisted V_Cas(tau; 0) via
           modified Newton minimization / full Newton root-finding from generic unspecial initial moduli,
           and the Raabe-Epstein holonomy sign-flip theorem on P_5 and m004's root orbit O_4.
  Part 3C: Parameter-free compactified Weil-Petersson operator expectation <H_hat_f>_WP over F via
           8-node and 12-node Gauss-Legendre quadrature in (x, u = 1/y), Haar basis-scrambling gate,
           and planted controls (PC_FUNNEL3_ZeroCharge, PC_FUNNEL3_FlippedSupertrace,
           PC_FUNNEL3_ReflectionSymmetricOrbit).

Empirical firewall: 0 of 19. Zero measured Standard Model numbers read, imported, or compared.
"""

from __future__ import annotations

import ast
import hashlib
import inspect
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

import mpmath as mp
import numpy as np


P5_ALL_24: List[Tuple[Fraction, Fraction]] = [
    (Fraction(i, 5), Fraction(j, 5))
    for i in range(5)
    for j in range(5)
    if (i, j) != (0, 0)
]

O4_M004: List[Tuple[Fraction, Fraction]] = [
    (Fraction(1, 5), Fraction(2, 5)),
    (Fraction(2, 5), Fraction(4, 5)),
    (Fraction(4, 5), Fraction(3, 5)),
    (Fraction(3, 5), Fraction(1, 5)),
]

O4_REFL_SYM_CONTROL: List[Tuple[Fraction, Fraction]] = [
    (Fraction(1, 5), Fraction(2, 5)),
    (Fraction(1, 5), Fraction(3, 5)),
    (Fraction(4, 5), Fraction(2, 5)),
    (Fraction(4, 5), Fraction(3, 5)),
]

ALLOWED_IMPORTS: Set[str] = {
    "__future__",
    "ast",
    "fractions",
    "hashlib",
    "inspect",
    "json",
    "math",
    "mpmath",
    "numpy",
    "pathlib",
    "typing",
}


def f2m(fr: Fraction) -> mp.mpf:
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def verify_source_isolation_and_no_embedded_tau_star() -> Dict[str, Any]:
    src = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src)
    mods: Set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                mods.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.level > 0:
                mods.add("<relative>")
            elif node.module:
                mods.add(node.module.split(".")[0])
    disallowed = sorted(mods - ALLOWED_IMPORTS)

    # Guardrail 1 AST / source check on the Casimir potential functions:
    # Verify that no orbifold target coordinates (sqrt(3), 0.866025...) appear anywhere
    # inside the definitions of the Eisenstein/Epstein or Casimir potential functions.
    pot_funcs = [
        eisenstein_untwisted_bessel,
        eisenstein_char_fast,
        epstein_shifted_fast,
        v_cas_untwisted_xy,
        v_cas_orbit_tau,
    ]
    banned_tokens = ("sqrt(3)", "0.866", "866025", "tau_star")
    embedded_hits: List[str] = []
    for fn in pot_funcs:
        fn_src = inspect.getsource(fn)
        for tok in banned_tokens:
            if tok in fn_src:
                embedded_hits.append(f"{fn.__name__}:{tok}")

    return {
        "imported_top_modules": sorted(mods),
        "disallowed_imports_count": len(disallowed),
        "zero_imports_from_main_or_other_relays": len(disallowed) == 0,
        "embedded_target_coordinate_hits_count": len(embedded_hits),
        "zero_embedded_target_coordinates_in_potentials": len(embedded_hits) == 0,
    }


# ============================================================================
# SECTION 1: PART 3A — TWO-ROUTE KRONECKER DIVISION CANCELLATION
# ============================================================================

def eta_dedekind_mp(tau: mp.mpc) -> mp.mpc:
    return mp.exp(1j * mp.pi * tau / 12) * mp.qp(mp.exp(2j * mp.pi * tau))


def log_det_route_a_theta(tau: mp.mpc, a_fr: Fraction, b_fr: Fraction) -> mp.mpf:
    """Route A: Odd-characteristic theta product ln det'(-Delta_{tau,(a,b)}) = 2 ln |theta_{a+1/2,b+1/2}(0|tau)/eta(tau)|."""
    al = f2m(a_fr) + mp.mpf(1) / 2
    be = f2m(b_fr) + mp.mpf(1) / 2
    m0 = int(round(-float(al)))
    y_f = max(float(mp.im(tau)), 0.4)
    k_span = max(28, int(math.ceil(math.sqrt((mp.mp.dps * math.log(10.0) + 24.0) / (math.pi * y_f)))) + 4)
    s = mp.mpc(0)
    for dm in range(-k_span, k_span + 1):
        n = mp.mpf(m0 + dm) + al
        s += mp.exp(mp.pi * 1j * tau * (n * n) + 2j * mp.pi * n * be)
    return 2 * mp.log(abs(s / eta_dedekind_mp(tau)))


def log_det_route_b_polylog(tau: mp.mpc, a_fr: Fraction, b_fr: Fraction) -> mp.mpf:
    """Route B: Direct Bernoulli-B_2 polylogarithmic spectral sum with zero calls to theta or Dedekind eta."""
    af = f2m(a_fr % 1)
    bf = f2m(b_fr % 1)
    y = mp.im(tau)
    b2_af = af * af - af + mp.mpf(1) / 6
    tot = -2 * mp.pi * y * b2_af
    n_max = int(mp.mp.dps * 2.4 / (2.0 * math.pi * max(float(y), 0.4))) + 12
    for n in range(0, n_max + 1):
        if n == 0 and (a_fr % 1 == 0):
            tot += 2 * mp.log(abs(1 - mp.exp(2j * mp.pi * bf)))
        else:
            z1 = mp.exp(2j * mp.pi * ((mp.mpf(n) + af) * tau + bf))
            tot += 2 * mp.log(abs(1 - z1))
        if n >= 1:
            z2 = mp.exp(2j * mp.pi * ((mp.mpf(n) - af) * tau - bf))
            tot += 2 * mp.log(abs(1 - z2))
    return tot


def run_part_3a() -> Dict[str, Any]:
    with mp.workdps(48):
        moduli = [
            mp.mpc(f2m(Fraction(17, 100)), f2m(Fraction(131, 100))),
            mp.mpc(f2m(Fraction(-31, 100)), f2m(Fraction(23, 10))),
            mp.mpc(f2m(Fraction(13, 100)), mp.mpf(5)),
        ]
        charges = [1, 2, 3, 4, 6]

        route_a_vs_b_max_diff = mp.mpf(0)
        for a_fr, b_fr in P5_ALL_24:
            da = log_det_route_a_theta(moduli[0], a_fr, b_fr)
            db = log_det_route_b_polylog(moduli[0], a_fr, b_fr)
            route_a_vs_b_max_diff = max(route_a_vs_b_max_diff, abs(da - db))

        two_ln_5 = 2 * mp.log(mp.mpf(5))
        kronecker_max_err_a = mp.mpf(0)
        kronecker_max_err_b = mp.mpf(0)
        for tau in moduli:
            for q in charges:
                sa = sum(log_det_route_a_theta(tau, q * a, q * b) for a, b in P5_ALL_24)
                sb = sum(log_det_route_b_polylog(tau, q * a, q * b) for a, b in P5_ALL_24)
                kronecker_max_err_a = max(kronecker_max_err_a, abs(sa - two_ln_5))
                kronecker_max_err_b = max(kronecker_max_err_b, abs(sb - two_ln_5))

        # On m004's 4-point orbit O_4, check non-trivial tau variation and Raabe B_2 cusp slope:
        o4_vals = [
            sum(log_det_route_b_polylog(tau, a, b) for a, b in O4_M004)
            for tau in moduli
        ]
        o4_tau_spread = max(abs(v1 - v2) for v1 in o4_vals for v2 in o4_vals)

        # Raabe B_2 supertrace check:
        # Untwisted STr_0 = 24 + 4 - 90 = -62; on O_4, average of B_2({q*a})/B_2(0) is -1/5 for gcd(q,5)=1:
        b2_0 = mp.bernpoly(2, mp.mpf(0))
        b2_o4_ratio = sum(mp.bernpoly(2, f2m(a)) for a, _ in O4_M004) / (4 * b2_0)
        str_b2_untw = Fraction(24 + 4 - 90, 1)
        str_b2_o4_exact = Fraction(24, 1) + Fraction(4 - 90, 1) * Fraction(-1, 5)  # +206/5

        # Planted control PC_FUNNEL3_ZeroCharge:
        # Take q = 5 (divisible by 5!) on shifted 15-torsion coset w_3 + P_5 where w_3 = (1/3, 2/3):
        # 5 * (w_3 + w) == 5 * w_3 == (2/3, 1/3) mod 1, which does NOT cancel to 2 ln 5 and varies strongly with tau!
        w3 = (Fraction(1, 3), Fraction(2, 3))
        q5_vals = [
            sum(log_det_route_b_polylog(tau, 5 * (w3[0] + a), 5 * (w3[1] + b)) for a, b in P5_ALL_24)
            for tau in moduli
        ]
        pc_zero_charge_tau_spread = max(abs(v1 - v2) for v1 in q5_vals for v2 in q5_vals)
        pc_zero_charge_dev_from_2ln5 = max(abs(v - two_ln_5) for v in q5_vals)

    e1_passed = bool(
        route_a_vs_b_max_diff < mp.mpf("1e-39")
        and kronecker_max_err_a < mp.mpf("1e-39")
        and kronecker_max_err_b < mp.mpf("1e-39")
        and o4_tau_spread > mp.mpf(1)
        and abs(b2_o4_ratio - f2m(Fraction(-1, 5))) < mp.mpf("1e-40")
        and str_b2_untw < 0 < str_b2_o4_exact
        and pc_zero_charge_tau_spread > mp.mpf(5)
    )
    return {
        "E1_Kronecker_Division_Cancellation_passed": e1_passed,
        "route_a_vs_route_b_24pt_max_diff": float(route_a_vs_b_max_diff),
        "kronecker_2ln5_max_err_route_a": float(kronecker_max_err_a),
        "kronecker_2ln5_max_err_route_b": float(kronecker_max_err_b),
        "o4_4pt_sum_tau_spread": float(o4_tau_spread),
        "raabe_b2_o4_ratio": float(b2_o4_ratio),
        "effective_b2_supertrace_untwisted": str(str_b2_untw),
        "effective_b2_supertrace_o4": str(str_b2_o4_exact),
        "PC_FUNNEL3_ZeroCharge_tau_spread": float(pc_zero_charge_tau_spread),
        "PC_FUNNEL3_ZeroCharge_dev_from_2ln5": float(pc_zero_charge_dev_from_2ln5),
    }


# ============================================================================
# SECTION 2: PART 3B — EPSTEIN SUBLATTICE, UNBIASED CRITICAL SEARCH & SIGN FLIP
# ============================================================================

def eisenstein_untwisted_bessel(tau: mp.mpc, s_int: int = 3) -> mp.mpf:
    x, y = mp.re(tau), mp.im(tau)
    s = mp.mpf(s_int)
    half = mp.mpf(1) / 2
    t1 = 2 * mp.zeta(2 * s_int) * (y ** s)
    t2 = 2 * mp.sqrt(mp.pi) * mp.gamma(s - half) / mp.gamma(s) * mp.zeta(2 * s_int - 1) * (y ** (1 - s))
    pref = 8 * (mp.pi ** s) / mp.gamma(s) * mp.sqrt(y)
    n_max = int((mp.mp.dps * 2.4 + 18.0) / (2.0 * math.pi * max(float(y), 0.4))) + 8
    bes = mp.mpf(0)
    for n in range(1, n_max + 1):
        sig = sum(mp.mpf(d) ** (1 - 2 * s_int) for d in range(1, n + 1) if n % d == 0)
        bes += (mp.mpf(n) ** (s - half)) * sig * mp.cos(2 * mp.pi * n * x) * mp.besselk(s - half, 2 * mp.pi * n * y)
    return t1 + t2 + pref * bes


def eisenstein_char_fast(tau: mp.mpc, a_fr: Fraction, b_fr: Fraction, s_int: int = 3) -> mp.mpf:
    if (a_fr % 1 == 0) and (b_fr % 1 == 0):
        return eisenstein_untwisted_bessel(tau, s_int)
    x, y = mp.re(tau), mp.im(tau)
    s = mp.mpf(s_int)
    half = mp.mpf(1) / 2
    af = f2m(a_fr % 1)
    bf = f2m(b_fr)
    k0 = ((-1) ** (s_int - 1)) * ((2 * mp.pi) ** (2 * s_int)) / mp.factorial(2 * s_int) * mp.bernpoly(2 * s_int, af) * (y ** s)
    thresh = mp.mp.dps * 2.4 + 20.0
    k_max = int(thresh / (2.0 * math.pi * max(float(y), 0.4) * 0.2)) + 8
    m_span = 16
    tot = k0
    for k in range(1, k_max + 1):
        for m in range(-m_span, m_span + 1):
            ma = mp.mpf(m) + af
            ang = 2 * mp.pi * k * (bf - ma * x)
            if abs(ma) < mp.mpf("1e-35"):
                term = mp.sqrt(mp.pi) * mp.gamma(s - half) / mp.gamma(s) * (y ** (1 - s)) * (mp.mpf(k) ** (1 - 2 * s_int))
            else:
                z = 2 * mp.pi * k * y * abs(ma)
                if float(z) > thresh:
                    continue
                term = (2 * (mp.pi ** s) / mp.gamma(s)) * mp.sqrt(y) * ((abs(ma) / k) ** (s - half)) * mp.besselk(s - half, z)
            tot += 2 * mp.cos(ang) * term
    return tot


def epstein_shifted_fast(tau: mp.mpc, a_fr: Fraction, b_fr: Fraction, s_int: int = 3) -> mp.mpf:
    x, y = mp.re(tau), mp.im(tau)
    s = mp.mpf(s_int)
    half = mp.mpf(1) / 2
    af = f2m(a_fr % 1)
    bf = f2m(b_fr % 1)
    thresh = mp.mp.dps * 2.4 + 20.0
    m_span = 22
    l_max = int(thresh / (2.0 * math.pi * max(float(y), 0.4) * 0.2)) + 8
    tot = mp.mpf(0)
    for m in range(-m_span, m_span + 1):
        ma = mp.mpf(m) + af
        if abs(ma) < mp.mpf("1e-35"):
            if abs(bf) < mp.mpf("1e-35"):
                tot += 2 * mp.zeta(2 * s_int) * (y ** s)
            else:
                tot += (mp.hurwitz(2 * s_int, bf) + mp.hurwitz(2 * s_int, 1 - bf)) * (y ** s)
        else:
            tot += mp.sqrt(mp.pi) * mp.gamma(s - half) / mp.gamma(s) * (y ** (1 - s)) * (abs(ma) ** (1 - 2 * s_int))
            for l in range(1, l_max + 1):
                z = 2 * mp.pi * l * abs(ma) * y
                if float(z) > thresh:
                    continue
                ang = 2 * mp.pi * l * (bf + ma * x)
                term = (2 * (mp.pi ** s) / mp.gamma(s)) * mp.sqrt(y) * ((mp.mpf(l) / abs(ma)) ** (s - half)) * mp.besselk(s - half, z)
                tot += 2 * mp.cos(ang) * term
    return tot


def v_cas_untwisted_xy(x: mp.mpf, y: mp.mpf, supertrace_sign: int = -62) -> mp.mpf:
    """
    4D one-loop Casimir energy density at zero holonomy (w = 0):
    V_Cas(tau; 0) = -(STr_0 / (2 pi^3)) E(tau; 3), with fixed-multiplet STr_0 = 24 + 4 - 90 = -62.
    """
    return -(mp.mpf(supertrace_sign) / (2 * (mp.pi ** 3))) * eisenstein_untwisted_bessel(mp.mpc(x, y), 3)


def v_cas_orbit_tau(tau: mp.mpc, orbit: List[Tuple[Fraction, Fraction]]) -> mp.mpf:
    """
    4D one-loop Casimir energy density averaged over a torsion orbit for the fixed multiplet:
      24 real vector modes at q = 0,
       4 real scalar doublet modes at q = 3,
      90 real chiral fermionic modes: 36 at q=1, 18 at q=-4, 18 at q=2, 12 at q=-3, 6 at q=6.
    """
    e0 = eisenstein_untwisted_bessel(tau, 3)
    acc = mp.mpf(0)
    for a, b in orbit:
        str_w = (
            24 * e0
            + 4 * eisenstein_char_fast(tau, 3 * a, 3 * b, 3)
            - (
                36 * eisenstein_char_fast(tau, 1 * a, 1 * b, 3)
                + 18 * eisenstein_char_fast(tau, -4 * a, -4 * b, 3)
                + 18 * eisenstein_char_fast(tau, 2 * a, 2 * b, 3)
                + 12 * eisenstein_char_fast(tau, -3 * a, -3 * b, 3)
                + 6 * eisenstein_char_fast(tau, 6 * a, 6 * b, 3)
            )
        )
        acc += -str_w / (2 * (mp.pi ** 3))
    return acc / len(orbit)


def grad_hess_xy(fn, x: mp.mpf, y: mp.mpf, h: mp.mpf) -> Tuple[mp.mpf, Tuple[mp.mpf, mp.mpf], mp.matrix]:
    f00 = fn(x, y)
    fxp = fn(x + h, y)
    fxm = fn(x - h, y)
    fyp = fn(x, y + h)
    fym = fn(x, y - h)
    fxpp = fn(x + h, y + h)
    fxpm = fn(x + h, y - h)
    fxmp = fn(x - h, y + h)
    fxmm = fn(x - h, y - h)
    gx = (fxp - fxm) / (2 * h)
    gy = (fyp - fym) / (2 * h)
    hxx = (fxp - 2 * f00 + fxm) / (h * h)
    hyy = (fyp - 2 * f00 + fym) / (h * h)
    hxy = (fxpp - fxpm - fxmp + fxmm) / (4 * h * h)
    return f00, (gx, gy), mp.matrix([[hxx, hxy], [hxy, hyy]])


def modified_newton_minimize(fn, x_init: Fraction, y_init: Fraction) -> Dict[str, Any]:
    x, y = f2m(x_init), f2m(y_init)
    h = mp.mpf("1e-9")
    for _ in range(28):
        f0, (gx, gy), hess = grad_hess_xy(fn, x, y, h)
        gnorm = mp.sqrt(gx * gx + gy * gy)
        if gnorm < mp.mpf("1e-24"):
            break
        ev, _ = mp.eigh(hess)
        hess_mod = hess.copy()
        min_ev = min(ev[0], ev[1])
        if min_ev <= mp.mpf("1e-6"):
            shift = -min_ev + mp.mpf(10)
            hess_mod[0, 0] += shift
            hess_mod[1, 1] += shift
        step = mp.lu_solve(hess_mod, mp.matrix([-gx, -gy]))
        alpha = mp.mpf(1)
        while alpha > mp.mpf("1e-8"):
            xn, yn = x + alpha * step[0], y + alpha * step[1]
            if yn > mp.mpf("0.5") and fn(xn, yn) < f0:
                x, y = xn, yn
                break
            alpha /= 2
    f_fin, (gx, gy), hess = grad_hess_xy(fn, x, y, h)
    ev, _ = mp.eigh(hess)
    return {
        "x": float(x),
        "y": float(y),
        "val": float(f_fin),
        "grad_norm": float(mp.sqrt(gx * gx + gy * gy)),
        "hess_eigs": [float(ev[0]), float(ev[1])],
        "hess_det": float(ev[0] * ev[1]),
    }


def newton_critical_root(fn, x_init: Fraction, y_init: Fraction) -> Dict[str, Any]:
    x, y = f2m(x_init), f2m(y_init)
    h = mp.mpf("1e-9")
    for _ in range(18):
        _, (gx, gy), hess = grad_hess_xy(fn, x, y, h)
        if mp.sqrt(gx * gx + gy * gy) < mp.mpf("1e-24"):
            break
        step = mp.lu_solve(hess, mp.matrix([-gx, -gy]))
        x += step[0]
        y += step[1]
    f_fin, (gx, gy), hess = grad_hess_xy(fn, x, y, h)
    ev, _ = mp.eigh(hess)
    return {
        "x": float(x),
        "y": float(y),
        "val": float(f_fin),
        "grad_norm": float(mp.sqrt(gx * gx + gy * gy)),
        "hess_eigs": [float(ev[0]), float(ev[1])],
        "hess_det": float(ev[0] * ev[1]),
    }


def run_part_3b() -> Dict[str, Any]:
    with mp.workdps(44):
        tau_test = mp.mpc(f2m(Fraction(13, 100)), f2m(Fraction(7, 5)))
        e_untw = eisenstein_untwisted_bessel(tau_test, 3)

        # Direct 2D lattice cross-check of E(tau; 3):
        lat_sum = mp.mpf(0)
        y_t = mp.im(tau_test)
        for k in range(-36, 37):
            for l in range(-36, 37):
                if k == 0 and l == 0:
                    continue
                lat_sum += (y_t ** 3) / (abs(k * tau_test + l) ** 6)
        bessel_vs_direct_lattice_diff = abs(e_untw - lat_sum)

        # Sublattice identities across charges q in {1, 2, 3}:
        shifted_sublattice_max_rel_err = mp.mpf(0)
        char_sublattice_max_rel_err = mp.mpf(0)
        for q in (1, 2, 3):
            s_ep = sum(epstein_shifted_fast(tau_test, q * a, q * b, 3) for a, b in P5_ALL_24)
            s_ch = sum(eisenstein_char_fast(tau_test, q * a, q * b, 3) for a, b in P5_ALL_24)
            target_ep = mp.mpf(5 ** 6 - 1) * e_untw
            target_ch = (mp.mpf(1) / mp.mpf(625) - mp.mpf(1)) * e_untw
            shifted_sublattice_max_rel_err = max(shifted_sublattice_max_rel_err, abs(s_ep - target_ep) / abs(target_ep))
            char_sublattice_max_rel_err = max(char_sublattice_max_rel_err, abs(s_ch - target_ch) / abs(target_ch))

        # Unbiased critical-point search on untwisted V_Cas(tau; 0) from generic initial points:
        min_run_1 = modified_newton_minimize(lambda x, y: v_cas_untwisted_xy(x, y, -62), Fraction(37, 100), Fraction(94, 100))
        min_run_2 = modified_newton_minimize(lambda x, y: v_cas_untwisted_xy(x, y, -62), Fraction(23, 100), Fraction(117, 100))
        saddle_run = newton_critical_root(lambda x, y: v_cas_untwisted_xy(x, y, -62), Fraction(8, 100), Fraction(107, 100))

        # Planted control PC_FUNNEL3_FlippedSupertrace (+62 boson-dominated flips minimum to strict maximum!):
        _, _, hess_flipped = grad_hess_xy(
            lambda x, y: v_cas_untwisted_xy(x, y, +62),
            mp.mpf(repr(min_run_1["x"])),
            mp.mpf(repr(min_run_1["y"])),
            mp.mpf("1e-9"),
        )
        ev_flipped, _ = mp.eigh(hess_flipped)
        pc_flipped_hess_eigs = [float(ev_flipped[0]), float(ev_flipped[1])]

        # Holonomy sign-flip trajectory on O_4 and P_5 across heights 1, 3/2, 5/2, 5, and asymptotic check at y = 12:
        heights = [Fraction(1, 1), Fraction(3, 2), Fraction(5, 2), Fraction(5, 1)]
        v_o4_traj: List[float] = []
        v_p5_traj: List[float] = []
        for h_fr in heights:
            tau_h = mp.mpc(f2m(Fraction(13, 100)), f2m(h_fr))
            v_o4_traj.append(float(v_cas_orbit_tau(tau_h, O4_M004)))
            v_p5_traj.append(float(v_cas_orbit_tau(tau_h, P5_ALL_24)))

        y_asymp = mp.mpf(12)
        v_o4_y12 = v_cas_orbit_tau(mp.mpc(f2m(Fraction(13, 100)), y_asymp), O4_M004)
        str_o4_b6 = f2m(Fraction(142166, 3125))
        exact_asymp_coeff_o4 = -(2 * mp.zeta(6) / (2 * (mp.pi ** 3))) * str_o4_b6
        asymp_o4_rel_err = abs((v_o4_y12 / (y_asymp ** 3)) - exact_asymp_coeff_o4) / abs(exact_asymp_coeff_o4)

    same_min = max(abs(min_run_1["x"] - min_run_2["x"]), abs(min_run_1["y"] - min_run_2["y"]))
    iso_hess_diff = abs(min_run_1["hess_eigs"][0] - min_run_1["hess_eigs"][1])
    strictly_decreasing_o4 = all(v_o4_traj[idx] > v_o4_traj[idx + 1] for idx in range(len(v_o4_traj) - 1))

    e2_passed = bool(
        shifted_sublattice_max_rel_err < mp.mpf("1e-34")
        and char_sublattice_max_rel_err < mp.mpf("1e-34")
        and bessel_vs_direct_lattice_diff < mp.mpf("1e-5")
        and same_min < 1e-12
        and min_run_1["grad_norm"] < 1e-24
        and min_run_1["hess_eigs"][0] > 1.0
        and iso_hess_diff < 1e-6
        and saddle_run["grad_norm"] < 1e-24
        and saddle_run["hess_det"] < -1.0
        and pc_flipped_hess_eigs[1] < -1.0
        and v_o4_traj[0] < 0.0
        and strictly_decreasing_o4
        and asymp_o4_rel_err < mp.mpf("1e-12")
    )
    return {
        "E2_Epstein_Sublattice_and_Holonomy_SignFlip_passed": e2_passed,
        "bessel_vs_direct_lattice_36_diff": float(bessel_vs_direct_lattice_diff),
        "shifted_sublattice_max_rel_err": float(shifted_sublattice_max_rel_err),
        "char_sublattice_max_rel_err": float(char_sublattice_max_rel_err),
        "untwisted_minimizer_from_037_094": min_run_1,
        "untwisted_minimizer_from_023_117": min_run_2,
        "untwisted_saddle_from_008_107": saddle_run,
        "PC_FUNNEL3_FlippedSupertrace_hess_eigs": pc_flipped_hess_eigs,
        "holonomy_sign_flip_v_cas_o4_heights_1_1p5_2p5_5": v_o4_traj,
        "holonomy_sign_flip_v_cas_p5_heights_1_1p5_2p5_5": v_p5_traj,
        "o4_asymptotic_y12_coeff_rel_err": float(asymp_o4_rel_err),
    }


# ============================================================================
# SECTION 3: PART 3C — COMPACTIFIED WEIL-PETERSSON OPERATOR EXPECTATION
# ============================================================================

def erfcx_f64(x: float) -> float:
    if x < 25.0:
        return math.exp(x * x) * math.erfc(x)
    inv2 = 1.0 / (x * x)
    return (1.0 / (math.sqrt(math.pi) * x)) * (
        1.0 + inv2 * (-0.5 + inv2 * (0.75 + inv2 * (-1.875 + inv2 * 6.5625)))
    )


def erfc_integral_f64(alpha: float, beta: float, u0: float, thresh: float = 42.0) -> float:
    xm = alpha * u0 - beta / u0
    xp = alpha * u0 + beta / u0
    edge_exp = (alpha * u0) ** 2 + (beta / u0) ** 2
    if xm >= 0.0:
        if edge_exp > thresh:
            return 0.0
        return (math.sqrt(math.pi) / (2.0 * alpha)) * math.exp(-edge_exp) * (erfcx_f64(xm) + erfcx_f64(xp))
    if 2.0 * alpha * beta > thresh:
        return 0.0
    part1 = 2.0 * math.exp(-2.0 * alpha * beta)
    part2 = 0.0 if edge_exp > thresh else math.exp(-edge_exp) * (erfcx_f64(xp) - erfcx_f64(-xm))
    return (math.sqrt(math.pi) / (2.0 * alpha)) * (part1 + part2)


def y_ref_zak_f64(tau: complex, a: float, b: float, ql: int, qr: int) -> np.ndarray:
    qh = -(ql + qr)
    tau1, tau2 = tau.real, tau.imag
    u0 = 1.0 / math.sqrt(6.0)
    u_split = math.sqrt(tau2)
    thresh = 42.0
    k_max = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * tau2)) / 3.0)) + 3
    l_quad = int(math.ceil(math.sqrt(thresh * 6.0 / (math.pi * tau2)))) + 4
    l_riem = int(math.ceil(math.sqrt(thresh / math.pi))) + 3

    def f_prim(u_val: float, b_val: float) -> float:
        if b_val == 0.0:
            return 2.0 * u_val
        bv_u = b_val / u_val
        if bv_u * bv_u > thresh:
            return 0.0
        return 2.0 * math.exp(-(bv_u * bv_u)) * (u_val - math.sqrt(math.pi) * b_val * erfcx_f64(bv_u))

    y_mat = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        c_l = (i + 0.5 + ql * a) / 3.0
        zak_ang = -2.0 * math.pi * (ql * b / 3.0) * (i + 0.5)
        zak_ph = complex(math.cos(zak_ang), math.sin(zak_ang))
        for j in range(3):
            c_r = (j + 0.5 - qr * a) / 3.0
            acc = 0.0j
            for k in range(-k_max, k_max + 1):
                n = (j - i) - 3 * k
                na = float(n) + qh * a
                delta_k = na / 3.0
                xi0 = (c_l + c_r - k) / 2.0
                x0 = na * tau1 + qh * b
                ang0 = math.pi * delta_k * ((qr - ql) * b - 3.0)
                base_phase = complex(math.cos(ang0), math.sin(ang0))
                if abs(na) > 1e-14:
                    alpha = math.sqrt(math.pi * tau2) * abs(na)
                    l_lin = int(math.ceil(thresh / (2.0 * math.pi * tau2 * abs(na)))) + 3
                    l_max_na = max(l_lin, l_quad)
                    sub = 0.0j
                    l_center = int(round(xi0))
                    for dl in range(-l_max_na, l_max_na + 1):
                        l = l_center + dl
                        beta = math.sqrt(math.pi * tau2) * abs(l - xi0)
                        iv = math.sqrt(tau2) * erfc_integral_f64(alpha, beta, u0, thresh)
                        if iv != 0.0:
                            ang = 2.0 * math.pi * (l - xi0) * x0
                            sub += iv * complex(math.cos(ang), math.sin(ang))
                    acc += base_phase * sub
                else:
                    sub1 = 0.0j
                    l_center = int(round(xi0))
                    for dl in range(-l_riem, l_riem + 1):
                        l = l_center + dl
                        beta = math.sqrt(math.pi * tau2) * abs(l - xi0)
                        iv = math.sqrt(tau2) * (f_prim(u_split, beta) - f_prim(u0, beta))
                        if iv != 0.0:
                            ang = 2.0 * math.pi * (l - xi0) * x0
                            sub1 += iv * complex(math.cos(ang), math.sin(ang))
                    sub2 = 0.0j
                    m_center = int(round(-x0))
                    for dm in range(-l_riem, l_riem + 1):
                        m = m_center + dm
                        mx = m + x0
                        if abs(mx) > 1e-14 and math.pi * mx * mx <= thresh:
                            ang = 2.0 * math.pi * m * xi0
                            sub2 += (
                                (tau2 / (math.pi * mx * mx))
                                * math.exp(-math.pi * mx * mx)
                                * complex(math.cos(ang), math.sin(ang))
                            )
                    acc += base_phase * (sub1 + sub2)
            y_mat[i, j] = zak_ph * acc
    return y_mat


def y_ref_zak_mp_check(tau: mp.mpc, a_fr: Fraction, b_fr: Fraction, ql: int, qr: int) -> mp.matrix:
    """Independent 40-digit unfolded 2D Gaussian lattice check of y_ref_zak_f64 at bulk tau."""
    qh = -(ql + qr)
    tau2 = mp.im(tau)
    a, b = f2m(a_fr), f2m(b_fr)
    half = mp.mpf(1) / 2
    y_mat = mp.zeros(3, 3)
    for i in range(3):
        c_l = (mp.mpf(i) + half + ql * a) / 3
        zak_ph = mp.exp(-2j * mp.pi * (ql * b / 3) * (mp.mpf(i) + half))
        for j in range(3):
            c_r = (mp.mpf(j) + half - qr * a) / 3
            acc = mp.mpc(0)
            for k in range(-9, 10):
                n = (j - i) - 3 * k
                na = mp.mpf(n) + qh * a
                delta_k = na / 3
                for m in range(-18, 19):
                    mb = mp.mpf(m) + qh * b
                    om = na * tau + mb
                    om_sq = abs(om) ** 2
                    if om_sq == 0:
                        continue
                    gauss = mp.exp(-mp.pi * om_sq / (6 * tau2))
                    phase = mp.exp(mp.pi * 1j * (mp.mpf(m) * (c_l + c_r - k) + delta_k * ((qr - ql) * b - 3)))
                    acc += (tau2 / (mp.pi * om_sq)) * gauss * phase
            y_mat[i, j] = zak_ph * acc
    return y_mat


def random_haar_u3_np(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    return q * (d / np.abs(d))[np.newaxis, :]


def extract_wp_observables(m1: np.ndarray, m2: np.ndarray) -> Dict[str, Any]:
    h1 = 0.5 * (m1 + m1.conj().T)
    h2 = 0.5 * (m2 + m2.conj().T)
    e1, q1 = np.linalg.eigh(h1)
    e2, q2 = np.linalg.eigh(h2)
    s1 = np.sqrt(np.maximum(e1, 0.0))
    s2 = np.sqrt(np.maximum(e2, 0.0))
    r1 = s1 / s1[2]
    r2 = s2 / s2[2]
    vmix = np.abs(q1.conj().T @ q2)
    cm = h1 @ h2 - h2 @ h1
    icp = float(np.imag(np.trace(cm @ cm @ cm)) / 6.0)
    d1 = float((e1[1] - e1[0]) * (e1[2] - e1[1]) * (e1[2] - e1[0]))
    d2 = float((e2[1] - e2[0]) * (e2[2] - e2[1]) * (e2[2] - e2[0]))
    j_wp = icp / (d1 * d2) if abs(d1 * d2) > 1e-30 else 0.0
    s13 = float(vmix[0, 2])
    c13 = math.sqrt(max(1.0 - s13 * s13, 1e-30))
    s12 = float(vmix[0, 1]) / c13
    s23 = float(vmix[1, 2]) / c13
    c12 = math.sqrt(max(1.0 - s12 * s12, 0.0))
    c23 = math.sqrt(max(1.0 - s23 * s23, 0.0))
    denom = s12 * s23 * s13 * c12 * c23 * c13 * c13
    sin_delta = abs(j_wp) / denom if denom > 1e-30 else 0.0
    return {
        "sec1_ratios_s1s3_s2s3": [float(r1[0]), float(r1[1])],
        "sec2_ratios_s1s3_s2s3": [float(r2[0]), float(r2[1])],
        "sec1_light_doublet_splitting": float(1.0 - r1[0] / r1[1]),
        "V_abs": [[float(vmix[r, c]) for c in range(3)] for r in range(3)],
        "V33": float(vmix[2, 2]),
        "V12": float(vmix[0, 1]),
        "V23": float(vmix[1, 2]),
        "V13": float(vmix[0, 2]),
        "I_CP_WP": icp,
        "J_WP": float(j_wp),
        "abs_sin_delta_WP": float(sin_delta),
    }


def wp_integrate_orbit(
    orbit: List[Tuple[Fraction, Fraction]],
    n_gl: int,
    u_l: np.ndarray | None = None,
    u_r1: np.ndarray | None = None,
    u_r2: np.ndarray | None = None,
) -> Tuple[float, np.ndarray, np.ndarray]:
    xs, ws = np.polynomial.legendre.leggauss(n_gl)
    orbit_f = [(float(a), float(b)) for a, b in orbit]
    vol = 0.0
    acc1 = np.zeros((3, 3), dtype=complex)
    acc2 = np.zeros((3, 3), dtype=complex)
    for ix in range(n_gl):
        x = 0.5 * float(xs[ix])
        wx = 0.5 * float(ws[ix])
        um = 1.0 / math.sqrt(1.0 - x * x)
        for iu in range(n_gl):
            u = 0.5 * um * (float(xs[iu]) + 1.0)
            wu = 0.5 * um * float(ws[iu])
            tau = complex(x, 1.0 / u)
            hb1 = np.zeros((3, 3), dtype=complex)
            hb2 = np.zeros((3, 3), dtype=complex)
            for af, bf in orbit_f:
                y1 = y_ref_zak_f64(tau, af, bf, 1, -4)
                y2 = y_ref_zak_f64(tau, af, bf, 1, 2)
                if u_l is not None and u_r1 is not None and u_r2 is not None:
                    y1 = u_l @ y1 @ u_r1.conj().T
                    y2 = u_l @ y2 @ u_r2.conj().T
                hb1 += (y1 @ y1.conj().T) / len(orbit_f)
                hb2 += (y2 @ y2.conj().T) / len(orbit_f)
            acc1 += wx * wu * (hb1 / float(np.real(np.trace(hb1))))
            acc2 += wx * wu * (hb2 / float(np.real(np.trace(hb2))))
            vol += wx * wu
    return vol, acc1 / vol, acc2 / vol


def run_part_3c() -> Dict[str, Any]:
    # Cross-check float64 Poisson-erfc vs 40-digit unfolded Gaussian sum at bulk tau:
    with mp.workdps(42):
        ym_mp = y_ref_zak_mp_check(mp.mpc("0.13", "1.7"), Fraction(1, 5), Fraction(2, 5), 1, -4)
    ym_f64 = y_ref_zak_f64(0.13 + 1.7j, 0.2, 0.4, 1, -4)
    f64_vs_mp_err = max(abs(ym_f64[r, c] - complex(ym_mp[r, c])) for r in range(3) for c in range(3))

    vol8, m1_8, m2_8 = wp_integrate_orbit(O4_M004, 8)
    vol12, m1_12, m2_12 = wp_integrate_orbit(O4_M004, 12)
    obs8 = extract_wp_observables(m1_8, m2_8)
    obs12 = extract_wp_observables(m1_12, m2_12)

    vol12_err = abs(vol12 - math.pi / 3.0)
    quad_conv_diff = max(
        abs(obs8["sec1_ratios_s1s3_s2s3"][0] - obs12["sec1_ratios_s1s3_s2s3"][0]),
        abs(obs8["sec1_ratios_s1s3_s2s3"][1] - obs12["sec1_ratios_s1s3_s2s3"][1]),
        abs(obs8["V12"] - obs12["V12"]),
        abs(obs8["V23"] - obs12["V23"]),
        abs(obs8["V13"] - obs12["V13"]),
    )

    # Gate_Haar_WP: 10 end-to-end quadrature trials with random (U_L, U_R1, U_R2) at every (tau, w)!
    haar_spec_mix_max_diff = 0.0
    haar_icp_max_rel_diff = 0.0
    for trial in range(10):
        ul = random_haar_u3_np(3000 + 3 * trial)
        ur1 = random_haar_u3_np(3001 + 3 * trial)
        ur2 = random_haar_u3_np(3002 + 3 * trial)
        _, m1_h, m2_h = wp_integrate_orbit(O4_M004, 8, ul, ur1, ur2)
        obs_h = extract_wp_observables(m1_h, m2_h)
        haar_spec_mix_max_diff = max(
            haar_spec_mix_max_diff,
            abs(obs_h["sec1_ratios_s1s3_s2s3"][0] - obs8["sec1_ratios_s1s3_s2s3"][0]),
            abs(obs_h["V12"] - obs8["V12"]),
            abs(obs_h["V23"] - obs8["V23"]),
            abs(obs_h["V13"] - obs8["V13"]),
        )
        haar_icp_max_rel_diff = max(
            haar_icp_max_rel_diff,
            abs(obs_h["I_CP_WP"] - obs8["I_CP_WP"]) / abs(obs8["I_CP_WP"]),
        )

    # Distinct left-handed Haar control (must scramble mixing by > 0.2):
    ul_bad1 = random_haar_u3_np(9301)
    ul_bad2 = random_haar_u3_np(9302)
    obs_bad = extract_wp_observables(ul_bad1 @ m1_8 @ ul_bad1.conj().T, ul_bad2 @ m2_8 @ ul_bad2.conj().T)
    pc_haar_distinct_ul_v_diff = max(
        abs(obs_bad["V_abs"][r][c] - obs8["V_abs"][r][c]) for r in range(3) for c in range(3)
    )

    # Planted control PC_FUNNEL3_ReflectionSymmetricOrbit: kills I_CP_WP across x <-> -x!
    _, m1_sym, m2_sym = wp_integrate_orbit(O4_REFL_SYM_CONTROL, 8)
    obs_sym = extract_wp_observables(m1_sym, m2_sym)

    e3_passed = bool(
        f64_vs_mp_err < 1e-13
        and vol12_err < 1e-12
        and quad_conv_diff < 1e-3
        and obs12["sec1_light_doublet_splitting"] > 0.03
        and obs12["V33"] > 0.9999
        and 1.0 > obs12["V12"] > obs12["V23"] > obs12["V13"] > 0.0
        and obs12["abs_sin_delta_WP"] > 0.5
        and obs12["sec1_ratios_s1s3_s2s3"][0] > 0.3
        and haar_spec_mix_max_diff < 1e-13
        and haar_icp_max_rel_diff < 1e-11
        and pc_haar_distinct_ul_v_diff > 0.2
        and abs(obs_sym["I_CP_WP"]) < 1e-18
    )
    return {
        "E3_WeilPetersson_ParameterFree_Operator_passed": e3_passed,
        "f64_vs_mpmath42_entry_max_err": float(f64_vs_mp_err),
        "wp_vol_12node_abs_err": float(vol12_err),
        "quadrature_8_vs_12_max_diff": float(quad_conv_diff),
        "wp_12node_o4_observables": obs12,
        "wp_8node_o4_observables": obs8,
        "controls_3c": {
            "Gate_Haar_WP_spec_mix_max_diff_10_trials": float(haar_spec_mix_max_diff),
            "Gate_Haar_WP_icp_max_rel_diff_10_trials": float(haar_icp_max_rel_diff),
            "PC_Haar_WP_distinct_UL_v_diff": float(pc_haar_distinct_ul_v_diff),
            "PC_FUNNEL3_ReflectionSymmetricOrbit_I_CP_WP": float(obs_sym["I_CP_WP"]),
            "PC_FUNNEL3_ReflectionSymmetricOrbit_abs_sin_delta": float(obs_sym["abs_sin_delta_WP"]),
        },
    }


def main() -> None:
    ast_info = verify_source_isolation_and_no_embedded_tau_star()
    res_3a = run_part_3a()
    res_3b = run_part_3b()
    res_3c = run_part_3c()

    all_controls_passed = bool(
        ast_info["zero_imports_from_main_or_other_relays"]
        and ast_info["zero_embedded_target_coordinates_in_potentials"]
        and res_3a["PC_FUNNEL3_ZeroCharge_tau_spread"] > 5.0
        and res_3b["PC_FUNNEL3_FlippedSupertrace_hess_eigs"][1] < -1.0
        and res_3c["controls_3c"]["Gate_Haar_WP_spec_mix_max_diff_10_trials"] < 1e-13
        and res_3c["controls_3c"]["Gate_Haar_WP_icp_max_rel_diff_10_trials"] < 1e-11
        and res_3c["controls_3c"]["PC_Haar_WP_distinct_UL_v_diff"] > 0.2
        and abs(res_3c["controls_3c"]["PC_FUNNEL3_ReflectionSymmetricOrbit_I_CP_WP"]) < 1e-18
    )
    stage_3_passed = bool(
        all_controls_passed
        and res_3a["E1_Kronecker_Division_Cancellation_passed"]
        and res_3b["E2_Epstein_Sublattice_and_Holonomy_SignFlip_passed"]
        and res_3c["E3_WeilPetersson_ParameterFree_Operator_passed"]
    )

    payload: Dict[str, Any] = {
        "card": "X-FUNNEL-3",
        "empirical_firewall": "0 of 19",
        "source_isolation_and_guardrail1_ast_check": ast_info,
        "part_3a_kronecker_cancellation": res_3a,
        "part_3b_epstein_and_holonomy_sign_flip": res_3b,
        "part_3c_weil_petersson_operator": res_3c,
        "all_planted_controls_passed": all_controls_passed,
        "stage_3_gate_passed": stage_3_passed,
    }

    out_dir = Path(__file__).resolve().parent
    out_json = out_dir / "verify_x_funnel_3_out.json"
    out_txt = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    out_json.write_text(out_txt, encoding="utf-8")
    digest = hashlib.sha256(out_json.read_bytes()).hexdigest()
    (out_dir / "OUTPUT_SHA256.txt").write_text(f"{digest}  verify_x_funnel_3_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
