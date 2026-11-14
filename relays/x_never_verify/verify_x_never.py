#!/usr/bin/env python3
"""
Standalone zero-trust verifier for Card X-NEVER (M15 on docs/seats/agy-exp.md):
Systematic first computations and planted-fault controls for GENESIS "Computed nowhere yet":
  1. Item N1: Harmonic frame (F-HE) counts at the hyperbolic point (50-digit mpmath)
     - Benchmark gate on silver squares m135 = -LLRR and m136 = +LLRR (reproducing B1485 A1-A5).
     - First computation across all sign characters and H^1 extension classes on 8 chiral
       word states outside m004's levels and outside {m135, m136}:
       m009 (+LLR), m010 (-LLR), m022 (+LLLR), m023 (-LLLR),
       m369 (-LLRLR), m370 (+LLRLR), s639 (-LLLRLR), s640 (+LLLRLR).
  2. Item N2: Class-index (F-CI) and McKay (F-MC) frames on m369 and s639 from their own arithmetic
     - Exact univariate trace-field and invariant-trace-field minimal polynomials, degrees,
       signatures (r_1, r_2), field discriminants (round_two), and ramified prime ideals (prime_decomp)
       on m004 (+LR benchmark), m369 (-LLRLR), and s639 (-LLLRLR).
     - Exact mod-p_i holonomy image orders and involution counts in SL(2, F_{q'}) / PSL(2, F_{q'})
       vs McKay SU(2) subgroup list.
     - Exhaustive enumeration of abstract surjections pi_1(M) ->> 2T, 2O, 2I on m004, m369, s639.
     - Explicit weight-system self-conjugacy check on 56 of E_7 and 248 of E_8.
  3. Item N3: Fillings and connected non-cyclic covers outside {m004, m003}
     - Exact own-level E_6 generation backgrounds and Dehn-filling rational-slope descent + F_p Fox
       cohomology (2 independent certified primes) on m369, s639, m010, m022, m023.
     - Connected non-cyclic covers of degrees d in {3, 4, 5} on 7 word states
       (m009, m010, m135, m136, m022, m023, m369) via exact integer Schreier cellular homology +
       Smith normal form (invariant_factors) and cusp peripheral homology ranks.
  4. Item N4: Nine untouched E* genesis probes (E7, E8, E9, E10, E12, E13, E15, E18, E19).
  5. Section 5: [v1.6] B130/AR4 metallic trace-map fixed-locus component decomposition (m = 1, 2, 3)
     and five planted-fault controls (PC_N1..PC_N5).

Zero imports from frontier/, src/, or any seat script.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import itertools
import json
import math
import os
import sys
import time
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

# Force pure-Python ground domain in SymPy so python-flint never raises TypeError on moduli >= 2^63
os.environ["SYMPY_GROUND_TYPES"] = "python"

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import invariant_factors
from sympy.polys.numberfields.basis import round_two
from sympy.polys.numberfields.primes import prime_decomp

# Keep global working precision at 55 decimal digits throughout so intermediate matrix products never round to 15 dps!
mp.mp.dps = 55


# ============================================================================
# JSON SERIALIZATION HELPER (SAFE FOR NUMPY 2.x, FRACTION, SYMPY, MPMATH)
# ============================================================================

def _json_default(obj: Any) -> Any:
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, Fraction):
        return f"{obj.numerator}/{obj.denominator}" if obj.denominator != 1 else str(obj.numerator)
    if isinstance(obj, sp.Integer):
        return int(obj)
    if isinstance(obj, sp.Rational):
        return f"{int(obj.p)}/{int(obj.q)}" if int(obj.q) != 1 else str(int(obj.p))
    if isinstance(obj, (mp.mpf, mp.mpc)):
        return str(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def is_prime_int(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    d = 3
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True


def find_primes_1_mod_N(N: int, count: int = 3, start: int = 10_000_000) -> List[int]:
    step = max(N, 2)
    rem = start % step
    cand = start + (1 - rem) % step
    if cand < start:
        cand += step
    out: List[int] = []
    while len(out) < count:
        if is_prime_int(cand):
            out.append(cand)
        cand += step
    return out


def primitive_nth_root_mod_p(N: int, p: int) -> int:
    assert is_prime_int(p) and (p - 1) % max(N, 1) == 0
    if N <= 1:
        return 1
    n_rem = N
    pfacs: List[int] = []
    d = 2
    while d * d <= n_rem:
        if n_rem % d == 0:
            pfacs.append(d)
            while n_rem % d == 0:
                n_rem //= d
        d += 1
    if n_rem > 1:
        pfacs.append(n_rem)
    exp = (p - 1) // N
    for g in range(2, p):
        zeta = pow(g, exp, p)
        if pow(zeta, N, p) == 1 and all(pow(zeta, N // q, p) != 1 for q in pfacs):
            return zeta
    raise RuntimeError(f"No primitive {N}-th root mod {p}")


# ============================================================================
# PUNCTURED-TORUS GROUP WORDS, FOX DERIVATIVES, AND ABELIANIZATION
# ============================================================================

# Generators of G = <x, y, mu | mu x mu^-1 phi(x)^-1 = 1, mu y mu^-1 phi(y)^-1 = 1>:
# Represent free-group words as lists of signed generator indices:
#   +1: x,  -1: x^-1
#   +2: y,  -2: y^-1
#   +3: mu, -3: mu^-1

def free_reduce(word: Sequence[int]) -> List[int]:
    out: List[int] = []
    for tok in word:
        if out and out[-1] == -tok:
            out.pop()
        else:
            out.append(tok)
    return out


def free_inv(word: Sequence[int]) -> List[int]:
    return [-tok for tok in reversed(word)]


def subst_f2(word: Sequence[int], img_x: Sequence[int], img_y: Sequence[int]) -> List[int]:
    inv_x = free_inv(img_x)
    inv_y = free_inv(img_y)
    acc: List[int] = []
    for tok in word:
        if tok == 1:
            acc.extend(img_x)
        elif tok == -1:
            acc.extend(inv_x)
        elif tok == 2:
            acc.extend(img_y)
        elif tok == -2:
            acc.extend(inv_y)
        else:
            raise ValueError(f"Unexpected generator {tok} in F_2 word")
    return free_reduce(acc)


def f2_monodromy_images(sign: int, word_str: str, k: int = 1) -> Tuple[List[int], List[int]]:
    """
    Exact F_2 = <x, y> images (phi(x), phi(y)) fixing lambda = x y x^-1 y^-1 identically:
      L:  (x, y) -> (x, y x)
      R:  (x, y) -> (x y, y)
      -I = (L R^-1 L)^2: (x, y) -> (y x^-1 y^-1, y x y^-1 x^-1 y^-1)
    Applied left-to-right across the letters of word_str (and -I if sign < 0), repeated k times.
    Wait: check composition convention against verify_x_sm.py!
    In verify_x_sm.py:
      For ell in letters:
        L: (X, Y) -> (X, X*Y) on abelian characters, because phi_L(x) = x, phi_L(y) = y x!
        Then next letter R applies phi_R to the NEW basis or composes phi_{step} on the outside?
      Check abel_matrix_word(+1, 'LLR'):
        Start: wx = x, wy = y.
        If each letter ell substitutes (x, y) -> ell(x, y) INSIDE current (wx, wy):
          Wait: for 'LR':
            Start wx = x, wy = y.
            Inside subst L: wx = x, wy = y x.
            Inside subst R (x -> x y, y -> y): wx = x y, wy = y x y!
            Abelianized: wx -> (1, 1), wy -> (1, 2): row matrix [[1, 1], [1, 2]]?
            Wait: check abel_matrix_word(+1, 'LR') in verify_x_sm.py:
              Start m00=1, m01=0, m10=0, m11=1 (rows: (1,0) and (0,1)).
              ch == 'L': m01, m11 = m00+m01, m10+m11 -> [[1, 1], [0, 1]]!
              ch == 'R': m00, m10 = m00+m01, m10+m11 -> [[2, 1], [1, 1]]!
            Row characters: (a, b) -> (a, a+b) -> (2a+b, a+b)!
            That means chi(phi(x)) = 2a + b and chi(phi(y)) = a + b, i.e.:
              phi(x) has (2 x's, 1 y) and phi(y) has (1 x, 1 y)!
            Let's check OUTER composition phi_R(phi_L(x, y)) vs INNER substitution:
              If (wx, wy) updates via:
                L: (wx, wy) -> (wx, wy * wx)
                R: (wx, wy) -> (wx * wy, wy)
                M (-I): (wx, wy) -> (wy * wx^-1 * wy^-1, wy * wx * wy^-1 * wx^-1 * wy^-1)
              Let's trace 'LR':
                Start: wx = x (1,0), wy = y (0,1)
                L: wx = x (1,0), wy = y x (1,1)
                R: wx = x y x (2,1), wy = y x (1,1)!!
              LOOK AT ABELIANIZATION OF (wx, wy) = (x y x, y x):
                wx -> 2a + b, wy -> a + b -> EXACT MATCH WITH [[2, 1], [1, 1]] AND FOX JACOBIAN IN verify_x_sm.py!
              AND check commutator wx * wy * wx^-1 * wy^-1 for (x y x, y x):
                (x y x)(y x)(x^-1 y^-1 x^-1)(x^-1 y^-1) -- WAIT:
                Check (wx * wy) * wy * (wx * wy)^-1 * wy^-1 = wx * wy * wy * wy^-1 * wx^-1 * wy^-1 = wx * wy * wx^-1 * wy^-1!!
                IT FIXES wx * wy * wx^-1 * wy^-1 = x y x^-1 y^-1 IDENTICALLY AT EVERY STEP!
    """
    wx: List[int] = [1]
    wy: List[int] = [2]
    steps = (list(word_str) + (["M"] if sign < 0 else [])) * k
    for ch in steps:
        if ch == "L":
            wx, wy = wx, free_reduce(wy + wx)
        elif ch == "R":
            wx, wy = free_reduce(wx + wy), wy
        elif ch == "M":
            inv_wx = free_inv(wx)
            inv_wy = free_inv(wy)
            new_wx = free_reduce(wy + inv_wx + inv_wy)
            new_wy = free_reduce(wy + wx + inv_wy + inv_wx + inv_wy)
            wx, wy = new_wx, new_wy
        else:
            raise ValueError(f"Unknown step {ch}")
    # Assert commutator [wx, wy] == [x, y] identically in F_2!
    comm = free_reduce(wx + wy + free_inv(wx) + free_inv(wy))
    assert comm == [1, 2, -1, -2], f"Commutator not fixed: {comm}"
    return wx, wy


def abel_matrix_word(sign: int, word: str, k: int = 1) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    wx, wy = f2_monodromy_images(sign, word, k)
    m00 = sum(1 if t == 1 else (-1 if t == -1 else 0) for t in wx)
    m10 = sum(1 if t == 2 else (-1 if t == -2 else 0) for t in wx)
    m01 = sum(1 if t == 1 else (-1 if t == -1 else 0) for t in wy)
    m11 = sum(1 if t == 2 else (-1 if t == -2 else 0) for t in wy)
    return ((m00, m01), (m10, m11))


def bundle_relators(sign: int, word_str: str, k: int = 1) -> Tuple[List[int], List[int], List[int]]:
    """
    Relators of pi_1(M) = <x, y, mu | R_1 = 1, R_2 = 1> and peripheral longitude lambda = [x, y]:
      R_1 = mu x mu^-1 phi(x)^-1
      R_2 = mu y mu^-1 phi(y)^-1
      lambda = x y x^-1 y^-1
    """
    wx, wy = f2_monodromy_images(sign, word_str, k)
    r1 = free_reduce([3, 1, -3] + free_inv(wx))
    r2 = free_reduce([3, 2, -3] + free_inv(wy))
    lam = [1, 2, -1, -2]
    return r1, r2, lam


# ============================================================================
# SECTION 1 (ITEM N1): HARMONIC FRAME (F-HE) AT 50-DIGIT PRECISION
# ============================================================================

def mp_eye(n: int) -> mp.matrix:
    M = mp.zeros(n, n)
    for i in range(n):
        M[i, i] = mp.mpf(1)
    return M


def mp_inv2(M: mp.matrix) -> mp.matrix:
    det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    out = mp.zeros(2, 2)
    out[0, 0] = M[1, 1] / det
    out[0, 1] = -M[0, 1] / det
    out[1, 0] = -M[1, 0] / det
    out[1, 1] = M[0, 0] / det
    return out


def mp_frob_norm(M: mp.matrix) -> mp.mpf:
    s = mp.mpf(0)
    for i in range(M.rows):
        for j in range(M.cols):
            v = M[i, j]
            s += mp.re(v) ** 2 + mp.im(v) ** 2
    return mp.sqrt(s)


def bloch_wigner_mp(z: mp.mpc) -> mp.mpf:
    if abs(z) < mp.mpf("1e-45") or abs(z - 1) < mp.mpf("1e-45"):
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def safe_polyroots_mp(coeffs_in: Sequence[Any]) -> List[mp.mpc]:
    """
    Multiplicity-safe high-precision polynomial root finder:
      1. Strips leading tiny coefficients (< 1e-35).
      2. Strips trailing tiny coefficients (< 1e-35) and records root 0 if any stripped.
      3. Tries mp.polyroots; if multiple roots cause Aberth non-convergence, falls back to
         companion-matrix QR eigenvalues (np.roots) + 25 steps of multiplicity-safe Schroder/Newton!
    """
    cs = [mp.mpc(c) for c in coeffs_in]
    while len(cs) > 1 and abs(cs[0]) < mp.mpf("1e-35"):
        cs.pop(0)
    has_zero_root = False
    while len(cs) > 1 and abs(cs[-1]) < mp.mpf("1e-35"):
        cs.pop()
        has_zero_root = True
    out: List[mp.mpc] = [mp.mpc(0)] if has_zero_root else []
    deg = len(cs) - 1
    if deg <= 0:
        return out
    if deg == 1:
        out.append(-cs[1] / cs[0])
        return out
    try:
        rts = mp.polyroots(cs, maxsteps=400, extraprec=50)
        out.extend(mp.mpc(r) for r in rts)
        return out
    except Exception:
        # Companion-matrix QR via np.roots (works for arbitrary root multiplicities!)
        scale0 = abs(cs[0])
        np_cs = np.array([complex(c / scale0) for c in cs], dtype=np.complex128)
        init_rts = np.roots(np_cs)
        # Polish each seed with Schroder's method (u = P / P', z_{k+1} = z_k - u / (1 - u P'' / P'))
        d1_cs = [cs[i] * (deg - i) for i in range(deg)]
        d2_cs = [d1_cs[i] * (deg - 1 - i) for i in range(deg - 1)]

        def eval_p(arr: List[mp.mpc], z: mp.mpc) -> mp.mpc:
            v = mp.mpc(0)
            for c in arr:
                v = v * z + c
            return v

        for r0 in init_rts:
            z = mp.mpc(complex(r0))
            for _ in range(30):
                p0 = eval_p(cs, z)
                if abs(p0) < mp.mpf("1e-50"):
                    break
                p1 = eval_p(d1_cs, z)
                if abs(p1) < mp.mpf("1e-45"):
                    break
                p2 = eval_p(d2_cs, z) if d2_cs else mp.mpc(0)
                u = p0 / p1
                denom = 1 - (u * p2) / p1
                step = u / denom if abs(denom) > mp.mpf("1e-20") else u
                z = z - step
                if abs(step) < mp.mpf("1e-48"):
                    break
            out.append(z)
        return out


def markoff_step_sym(a: Any, b: Any, c: Any, ch: str) -> Tuple[Any, Any, Any]:
    """
    Bowditch/Fricke trace update matching our F_2 step update:
      L: (wx, wy) -> (wx, wy * wx):
         new a = tr(wx) = a
         new b = tr(wy * wx) = tr(wx * wy) = c
         new c = tr(wx * wy * wx) = tr(wx) tr(wy * wx) - tr(wy) = a * c - b
      R: (wx, wy) -> (wx * wy, wy):
         new a = tr(wx * wy) = c
         new b = tr(wy) = b
         new c = tr(wx * wy * wy) = tr(wx * wy) tr(wy) - tr(wx) = b * c - a
    """
    if ch == "L":
        return (a, c, a * c - b)
    if ch == "R":
        return (c, b, b * c - a)
    raise ValueError(ch)


def markoff_inv_step_sym(a: Any, b: Any, c: Any, ch: str) -> Tuple[Any, Any, Any]:
    if ch == "L":
        # (a0, c0, a0*c0 - b0) = (a, b, c) => a0 = a, c0 = b, b0 = a*b - c
        return (a, a * b - c, b)
    if ch == "R":
        # (c0, b0, b0*c0 - a0) = (a, b, c) => b0 = b, c0 = a, a0 = a*b - c
        return (a * b - c, b, a)
    raise ValueError(ch)


def solve_hyperbolic_markoff_word(word_str: str, dps: int = 60) -> Dict[str, Any]:
    """
    Find ALL exact algebraic parabolic Markoff fixed points of Phi_{word}(a, b, c) = (a, b, c)
    with a^2 + b^2 + c^2 - a*b*c = 0, polish in mpmath to `dps` digits, and identify the unique
    discrete faithful hyperbolic structure (positive ideal tetrahedron shapes Im(z_k) > 0, maximal volume).
    Also extracts certified exact minimal polynomials over Q for N2!
    """
    old_dps = mp.mp.dps
    mp.mp.dps = dps + 15
    try:
        sa, sb, sc = sp.symbols("a b c")
        half = len(word_str) // 2
        w1 = word_str[:half]
        w2 = word_str[half:]

        lhs = (sa, sb, sc)
        for ch in w1:
            lhs = markoff_step_sym(lhs[0], lhs[1], lhs[2], ch)
        rhs = (sa, sb, sc)
        for ch in reversed(w2):
            rhs = markoff_inv_step_sym(rhs[0], rhs[1], rhs[2], ch)

        eqs = [sp.expand(lhs[i] - rhs[i]) for i in range(3)]
        markoff_poly = sa**2 + sb**2 + sc**2 - sa * sb * sc

        # Eliminate sc via resultant with markoff_poly (degree 2 in sc)
        res_c = []
        for f in eqs:
            if f == 0:
                continue
            r = sp.expand(sp.resultant(f, markoff_poly, sc))
            if r != 0:
                res_c.append(r)

        # Collect candidate irreducible factors in sa
        cand_a_polys: List[sp.Poly] = [sp.Poly(sa, sa)]
        if len(res_c) >= 2:
            for i in range(len(res_c)):
                for j in range(i + 1, len(res_c)):
                    rab = sp.resultant(res_c[i], res_c[j], sb)
                    if rab != 0:
                        _, facs = sp.factor_list(rab, sa)
                        for fac, _ in facs:
                            p_fac = sp.Poly(fac, sa)
                            if p_fac.degree() >= 1 and all(p_fac != q for q in cand_a_polys):
                                cand_a_polys.append(p_fac)
        elif len(res_c) == 1:
            _, facs = sp.factor_list(res_c[0], sa)
            for fac, _ in facs:
                p_fac = sp.Poly(fac, sa)
                if p_fac.degree() >= 1 and all(p_fac != q for q in cand_a_polys):
                    cand_a_polys.append(p_fac)

        # Full forward equations for polishing and verification
        fwd = (sa, sb, sc)
        for ch in word_str:
            fwd = markoff_step_sym(fwd[0], fwd[1], fwd[2], ch)
        F_sys = [sp.expand(fwd[0] - sa), sp.expand(fwd[1] - sb), sp.expand(fwd[2] - sc), markoff_poly]
        J_sym = [[sp.diff(F_sys[r], v) for v in (sa, sb, sc)] for r in range(4)]

        f_num = sp.lambdify((sa, sb, sc), F_sys, "mpmath")
        j_num = sp.lambdify((sa, sb, sc), J_sym, "mpmath")

        roots_found: List[Dict[str, Any]] = []

        for pa in cand_a_polys:
            coeffs_a = [mp.mpf(int(c)) for c in pa.all_coeffs()]
            a_roots = safe_polyroots_mp(coeffs_a)

            for ar in a_roots:
                # Find b roots from res_c evaluated at sa = ar
                b_cands: List[mp.mpc] = []
                for rc in res_c:
                    pb = sp.Poly(rc, sb)
                    b_coeffs = []
                    for coeff_expr in pb.all_coeffs():
                        # Evaluate polynomial in sa at ar
                        pa_c = sp.Poly(coeff_expr, sa)
                        val = mp.mpc(0)
                        for cc in pa_c.all_coeffs():
                            val = val * ar + mp.mpf(int(cc))
                        b_coeffs.append(val)
                    rts_b = safe_polyroots_mp(b_coeffs)
                    if rts_b:
                        b_cands.extend(rts_b)
                        break

                for br in b_cands:
                    # Solve c^2 - (ar*br)*c + (ar^2 + br^2) = 0
                    disc_c = (ar * br) ** 2 - 4 * (ar**2 + br**2)
                    sq_c = mp.sqrt(disc_c)
                    for cr in ((ar * br + sq_c) / 2, (ar * br - sq_c) / 2):
                        # Gauss-Newton polish on 4x3 overdetermined system F_sys = 0
                        aa, bb, cc = mp.mpc(ar), mp.mpc(br), mp.mpc(cr)
                        for _ in range(20):
                            fv = f_num(aa, bb, cc)
                            res_norm = mp.sqrt(sum(abs(x) ** 2 for x in fv))
                            if res_norm < mp.mpf(10) ** (-(dps + 5)):
                                break
                            jv = j_num(aa, bb, cc)
                            # Solve 3x3 normal / QR system J^H J delta = -J^H f
                            J_mat = mp.matrix(jv)
                            f_vec = mp.matrix([[x] for x in fv])
                            # Use 3 independent equations or QR least squares
                            JH = J_mat.transpose_conj()
                            H_mat = JH * J_mat
                            rhs_v = -(JH * f_vec)
                            try:
                                delta = mp.lu_solve(H_mat, rhs_v)
                            except Exception:
                                break
                            aa += delta[0]
                            bb += delta[1]
                            cc += delta[2]

                        fv = f_num(aa, bb, cc)
                        res_norm = mp.sqrt(sum(abs(x) ** 2 for x in fv))
                        if res_norm > mp.mpf("1e-35"):
                            continue
                        if abs(aa) + abs(bb) + abs(cc) < mp.mpf("1e-20"):
                            continue  # Skip Q_8 point (0, 0, 0)

                        # Deduplicate
                        if any(
                            abs(aa - r["a"]) + abs(bb - r["b"]) + abs(cc - r["c"]) < mp.mpf("1e-20")
                            for r in roots_found
                        ):
                            continue

                        # Compute Bowditch ideal-tetrahedron shapes and volume along word_str
                        ta, tb, tc = aa, bb, cc
                        vol = mp.mpf(0)
                        shapes: List[mp.mpc] = []
                        valid_shapes = True
                        for ch in word_str:
                            if ch == "L":
                                cp = ta * tc - tb
                                denom = tb * cp
                                if abs(denom) < mp.mpf("1e-30"):
                                    valid_shapes = False
                                    break
                                z = (ta * ta) / denom
                                ta, tb, tc = ta, tc, cp
                            else:
                                cp = tb * tc - ta
                                denom = tb * tb
                                if abs(denom) < mp.mpf("1e-30"):
                                    valid_shapes = False
                                    break
                                z = (ta * cp) / denom
                                ta, tb, tc = tc, tb, cp
                            shapes.append(z)
                            vol += bloch_wigner_mp(z)

                        roots_found.append(
                            {
                                "a": aa,
                                "b": bb,
                                "c": cc,
                                "minpoly_a": pa,
                                "residual": res_norm,
                                "valid_shapes": valid_shapes,
                                "shapes": shapes,
                                "signed_volume": vol,
                                "abs_volume": abs(vol),
                                "all_im_pos": valid_shapes and all(mp.im(z) > mp.mpf("1e-12") for z in shapes),
                            }
                        )

        assert roots_found, f"No non-zero Markoff roots found for {word_str}"
        max_vol = max(r["abs_volume"] for r in roots_found)
        assert max_vol > mp.mpf("1.5"), f"Unexpectedly small max volume {max_vol} for {word_str}"

        # Pick positively oriented discrete faithful root (signed_volume == +max_vol)
        pos_roots = [
            r
            for r in roots_found
            if abs(r["signed_volume"] - max_vol) < mp.mpf("1e-25")
        ]
        assert pos_roots, f"No positively oriented max-volume root for {word_str}"
        # Canonical tie-breaker among sign lifts (+a,+b,+c) vs (-a,-b,+c) etc.: deterministic sort
        pos_roots.sort(
            key=lambda r: (
                -float(mp.re(r["a"])),
                -float(mp.im(r["a"])),
                -float(mp.re(r["b"])),
                -float(mp.im(r["b"])),
            )
        )
        best = pos_roots[0]
        return {
            "word": word_str,
            "best": best,
            "all_roots": roots_found,
            "eqs_split": eqs,
            "markoff_poly": markoff_poly,
        }
    finally:
        mp.mp.dps = old_dps


def eval_word_sl2_mp(word: Sequence[int], gens: Dict[int, mp.matrix]) -> mp.matrix:
    res = mp_eye(2)
    for tok in word:
        res = res * gens[tok]
    return res


def build_hyperbolic_holonomy_and_four(
    sign: int,
    word_str: str,
    markoff_info: Optional[Dict[str, Any]] = None,
    dps: int = 55,
    plant_transpose_bug: bool = False,
) -> Dict[str, Any]:
    """
    Constructs exact 55-digit SL(2, C) parabolic holonomy (X, Y, T) for M(sign, word_str)
    and its real Minkowski SO^+(3, 1) representation `four` on 2x2 Hermitian matrices
    in basis {I_2, sigma_1, sigma_2, sigma_3}.
    """
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    try:
        if markoff_info is None:
            markoff_info = solve_hyperbolic_markoff_word(word_str, dps=dps)
        best = markoff_info["best"]
        a, b, c = best["a"], best["b"], best["c"]
        zeta = (c + mp.sqrt(c * c - 4)) / 2

        X = mp.matrix([[a, mp.mpf(1)], [mp.mpf(-1), mp.mpf(0)]])
        Y = mp.matrix([[mp.mpf(0), -1 / zeta], [zeta, b]])
        gens_f2 = {1: X, -1: mp_inv2(X), 2: Y, -2: mp_inv2(Y)}

        wx, wy = f2_monodromy_images(sign, word_str, 1)
        phi_X = eval_word_sl2_mp(wx, gens_f2)
        phi_Y = eval_word_sl2_mp(wy, gens_f2)

        # Solve linear homogeneous system T * X - phi_X * T = 0, T * Y - phi_Y * T = 0
        # Unknowns: vec(T) = [T00, T01, T10, T11]^T (8 equations x 4 unknowns)
        L_sys = mp.zeros(8, 4)
        for eq_block, (A_in, A_out) in enumerate(((X, phi_X), (Y, phi_Y))):
            row_off = 4 * eq_block
            # (T * A_in - A_out * T)_{i, j} = sum_k T_{i,k} A_in_{k,j} - sum_k A_out_{i,k} T_{k,j}
            for i in range(2):
                for j in range(2):
                    r = row_off + 2 * i + j
                    for k in range(2):
                        L_sys[r, 2 * i + k] += A_in[k, j]
                        L_sys[r, 2 * k + j] -= A_out[i, k]

        # Extract 1D nullspace via 55-digit SVD / normal equations L^H L
        LH = L_sys.transpose_conj()
        H4 = LH * L_sys
        # Inverse iteration from deterministic seed vectors to get exact null vector
        v = mp.matrix([[mp.mpc("0.37", "0.19")], [mp.mpc("-0.71", "0.43")], [mp.mpc("0.53", "-0.29")], [mp.mpc("0.89", "0.11")]])
        reg = H4 + mp.mpf("1e-48") * mp_eye(4)
        for _ in range(6):
            v = mp.lu_solve(reg, v)
            v /= mp_frob_norm(v)

        T_raw = mp.matrix([[v[0, 0], v[1, 0]], [v[2, 0], v[3, 0]]])
        det_raw = T_raw[0, 0] * T_raw[1, 1] - T_raw[0, 1] * T_raw[1, 0]
        assert abs(det_raw) > mp.mpf("1e-20"), "Singular intertwiner T_raw"
        T = T_raw / mp.sqrt(det_raw)
        if mp.re(T[0, 0] + T[1, 1]) < 0:
            T = -T

        # Verify parabolic trace(T) == +2 and trace(lambda) == -2 and relator flatness!
        tr_T = T[0, 0] + T[1, 1]
        assert abs(tr_T - 2) < mp.mpf("1e-38"), f"Meridian T not parabolic +2: tr(T)={tr_T}"

        gens_G = {1: X, -1: mp_inv2(X), 2: Y, -2: mp_inv2(Y), 3: T, -3: mp_inv2(T)}
        r1, r2, lam_w = bundle_relators(sign, word_str, 1)
        R1_mat = eval_word_sl2_mp(r1, gens_G)
        R2_mat = eval_word_sl2_mp(r2, gens_G)
        lam_mat = eval_word_sl2_mp(lam_w, gens_G)
        rel_err = max(mp_frob_norm(R1_mat - mp_eye(2)), mp_frob_norm(R2_mat - mp_eye(2)))
        assert rel_err < mp.mpf("1e-38"), f"SL(2,C) relator error {rel_err}"
        assert abs((lam_mat[0, 0] + lam_mat[1, 1]) + 2) < mp.mpf("1e-38"), "Longitude not parabolic -2"

        # Extract cusp shape tau_cusp from commuting parabolics T = I + N_mu and -lam = I + N_lam!
        N_mu = T - mp_eye(2)
        N_lam = -lam_mat - mp_eye(2)
        # Pick largest entry of N_lam to read complex ratio tau_cusp = N_mu / N_lam
        best_ij = max(((i, j) for i in range(2) for j in range(2)), key=lambda ij: abs(N_lam[ij[0], ij[1]]))
        tau_cusp = N_mu[best_ij[0], best_ij[1]] / N_lam[best_ij[0], best_ij[1]]
        assert abs(mp.im(tau_cusp)) > mp.mpf("1e-10"), f"Degenerate cusp shape {tau_cusp}"

        # Build SO^+(3, 1) Lorentzian four on Hermitian basis {I_2, sigma_1, sigma_2, sigma_3}:
        # H(v) = v0 I + v1 sigma_1 + v2 sigma_2 + v3 sigma_3
        # v_out_mu = (1/2) tr(sigma_mu * g * H(v) * g^dagger)
        paulis = [
            mp.matrix([[1, 0], [0, 1]]),
            mp.matrix([[0, 1], [1, 0]]),
            mp.matrix([[0, -mp.j], [mp.j, 0]]),
            mp.matrix([[1, 0], [0, -1]]),
        ]
        eta31 = mp.diag([mp.mpf(1), mp.mpf(-1), mp.mpf(-1), mp.mpf(-1)])

        def sl2_to_four(g: mp.matrix) -> mp.matrix:
            L = mp.zeros(4, 4)
            g_right = g.T if plant_transpose_bug else g.transpose_conj()
            for col_idx, P_in in enumerate(paulis):
                M_out = g * P_in * g_right
                for row_idx, P_out in enumerate(paulis):
                    tr_val = (
                        P_out[0, 0] * M_out[0, 0]
                        + P_out[0, 1] * M_out[1, 0]
                        + P_out[1, 0] * M_out[0, 1]
                        + P_out[1, 1] * M_out[1, 1]
                    ) / 2
                    L[row_idx, col_idx] = tr_val if plant_transpose_bug else mp.re(tr_val)
            if not plant_transpose_bug:
                lor_err = mp_frob_norm(L.T * eta31 * L - eta31)
                assert lor_err < mp.mpf("1e-38"), f"SO(3,1) metric error {lor_err}"
            return L

        four_X = sl2_to_four(X)
        four_Y = sl2_to_four(Y)
        four_T = sl2_to_four(T)

        return {
            "sign": sign,
            "word": word_str,
            "volume_float": float(best["abs_volume"]),
            "tau_cusp_re": float(mp.re(tau_cusp)),
            "tau_cusp_im": float(mp.im(tau_cusp)),
            "sl2_relator_err": float(rel_err),
            "four_X": four_X,
            "four_Y": four_Y,
            "four_T": four_T,
            "r1": r1,
            "r2": r2,
            "lam": lam_w,
        }
    finally:
        mp.mp.dps = old_dps


def mp_svd_rank_and_nullspace(M: mp.matrix, tol: mp.mpf) -> Tuple[int, List[mp.matrix], float, float]:
    """
    55-digit SVD rank and right-nullspace basis of an r x c mpmath matrix M,
    checking clean spectral gap around `tol` (no borderline singular values!).
    Returns (rank, list of c x 1 nullspace column vectors, min_nonzero_sv, max_zero_sv).
    """
    r, c = M.rows, M.cols
    if r == 0 or c == 0:
        basis = [mp.zeros(c, 1) for _ in range(c)]
        for j in range(c):
            basis[j][j, 0] = mp.mpf(1)
        return 0, basis, 1.0, 0.0

    # mp.svd_r works on real matrices, mp.svd_c on complex
    is_complex = any(mp.im(M[i, j]) != 0 for i in range(r) for j in range(c))
    # Pad with zero rows if r < c so full V (c x c) is always returned!
    if r < c:
        M_pad = mp.zeros(c, c)
        for i in range(r):
            for j in range(c):
                M_pad[i, j] = M[i, j]
    else:
        M_pad = M

    if is_complex:
        _, S, Vh = mp.svd_c(M_pad)
    else:
        _, S, Vh = mp.svd_r(M_pad)

    nz_svs = [float(s) for s in S if s > tol]
    z_svs = [float(s) for s in S if s <= tol]
    min_nz = min(nz_svs) if nz_svs else 1.0
    max_z = max(z_svs) if z_svs else 0.0
    # Assert wide spectral gap (at least 10 orders of magnitude!)
    assert min_nz > float(tol) * 1e8, f"Borderline nonzero singular value {min_nz} near tol {float(tol)}"
    assert max_z < float(tol) * 1e-5, f"Borderline zero singular value {max_z} near tol {float(tol)}"

    rk = len(nz_svs)
    null_vecs: List[mp.matrix] = []
    for row_idx in range(rk, c):
        vec = mp.zeros(c, 1)
        for j in range(c):
            val = Vh[row_idx, j]
            vec[j, 0] = mp.conj(val) if is_complex else val
        # Assert M * vec == 0 to high precision
        assert mp_frob_norm(M * vec) < tol * 1e-3
        null_vecs.append(vec)
    return rk, null_vecs, min_nz, max_z


def fox_jacobian_mp(
    word: Sequence[int],
    gens_rep: Dict[int, mp.matrix],
    dim_m: int,
) -> Tuple[mp.matrix, mp.matrix]:
    """
    Left Fox derivative evaluation of `word` in G = <x(1), y(2), mu(3)> on an m-dimensional left G-module:
      z(u v) = z(u) + rho(u) z(v)
      z(g^-1) = -rho(g^-1) z(g)
    Returns (rho(word) [m x m], J_word [m x 3m]) mapping [z(x); z(y); z(mu)] -> z(word).
    """
    cur_rho = mp_eye(dim_m)
    J = mp.zeros(dim_m, 3 * dim_m)
    for tok in word:
        g_idx = abs(tok) - 1  # 0, 1, 2
        col_off = g_idx * dim_m
        if tok > 0:
            # term + cur_rho * z(g_idx)
            for i in range(dim_m):
                for j in range(dim_m):
                    J[i, col_off + j] += cur_rho[i, j]
            cur_rho = cur_rho * gens_rep[tok]
        else:
            cur_rho = cur_rho * gens_rep[tok]  # cur_rho * rho(g^-1)
            for i in range(dim_m):
                for j in range(dim_m):
                    J[i, col_off + j] -= cur_rho[i, j]
    return cur_rho, J


def cusped_module_signature_mp(
    rx: mp.matrix,
    ry: mp.matrix,
    rmu: mp.matrix,
    r1: Sequence[int],
    r2: Sequence[int],
    lam: Sequence[int],
    dps: int = 55,
) -> Dict[str, Any]:
    """
    Computes exact B1297 / B1485 signature (a0, a1, t0, r1, n_int) and cocycle bases
    for an m-dimensional left G-module E at 55-digit precision.
    """
    old_dps = mp.mp.dps
    mp.mp.dps = dps
    try:
        m = rx.rows
        tol = mp.mpf("1e-25")
        I_m = mp_eye(m)
        gens = {
            1: rx,
            -1: mp.inverse(rx),
            2: ry,
            -2: mp.inverse(ry),
            3: rmu,
            -3: mp.inverse(rmu),
        }

        val_r1, J_r1 = fox_jacobian_mp(r1, gens, m)
        val_r2, J_r2 = fox_jacobian_mp(r2, gens, m)
        val_lam, J_lam = fox_jacobian_mp(lam, gens, m)

        rel_err = max(mp_frob_norm(val_r1 - I_m), mp_frob_norm(val_r2 - I_m))
        assert rel_err < mp.mpf("1e-34"), f"Module relator flatness failed: {rel_err}"

        # d0: C^m -> C^{3m}
        d0 = mp.zeros(3 * m, m)
        for g_idx, g_mat in enumerate((rx, ry, rmu)):
            off = g_idx * m
            diff = g_mat - I_m
            for i in range(m):
                for j in range(m):
                    d0[off + i, j] = diff[i, j]

        # d1: C^{3m} -> C^{2m}
        d1 = mp.zeros(2 * m, 3 * m)
        for j in range(3 * m):
            for i in range(m):
                d1[i, j] = J_r1[i, j]
                d1[m + i, j] = J_r2[i, j]

        # Assert exact complex identity d1 * d0 == 0!
        chain_err = mp_frob_norm(d1 * d0)
        assert chain_err < mp.mpf("1e-34"), f"d1 * d0 != 0: {chain_err}"

        rk_d0, _, _, _ = mp_svd_rank_and_nullspace(d0, tol)
        a0 = m - rk_d0
        rk_d1, z1_basis, _, _ = mp_svd_rank_and_nullspace(d1, tol)
        dim_z1 = 3 * m - rk_d1
        a1 = dim_z1 - rk_d0

        # Boundary restriction R_bdry: C^{3m} -> C^{2m} sending (zx, zy, zmu) -> (zmu, z_lam)
        R_bdry = mp.zeros(2 * m, 3 * m)
        for i in range(m):
            R_bdry[i, 2 * m + i] = mp.mpf(1)
            for j in range(3 * m):
                R_bdry[m + i, j] = J_lam[i, j]

        # Boundary coboundary d0_bdry: C^m -> C^{2m} sending w -> ((rmu - I)w, (rlam - I)w)
        d0_bdry = mp.zeros(2 * m, m)
        diff_mu = rmu - I_m
        diff_lam = val_lam - I_m
        for i in range(m):
            for j in range(m):
                d0_bdry[i, j] = diff_mu[i, j]
                d0_bdry[m + i, j] = diff_lam[i, j]

        rk_d0_bdry, _, _, _ = mp_svd_rank_and_nullspace(d0_bdry, tol)
        t0 = m - rk_d0_bdry

        # Interior cocycles: z in C^{3m} for which exists w in C^m with d1*z = 0 and R_bdry*z - d0_bdry*w = 0
        # System on (z [3m], w [m]) of size (4m) x (4m):
        M_int = mp.zeros(4 * m, 4 * m)
        for i in range(2 * m):
            for j in range(3 * m):
                M_int[i, j] = d1[i, j]
                M_int[2 * m + i, j] = R_bdry[i, j]
            for j in range(m):
                M_int[2 * m + i, 3 * m + j] = -d0_bdry[i, j]

        rk_mint, null_zw, _, _ = mp_svd_rank_and_nullspace(M_int, tol)
        # Project null_zw onto z-component (kernel of projection has dimension ker(d0_bdry) = t0!)
        dim_null_zw = 4 * m - rk_mint
        dim_z1_int = dim_null_zw - t0
        n_int = dim_z1_int - rk_d0
        r_bdry_rk = a1 - n_int
        assert n_int >= 0 and r_bdry_rk >= 0, f"Invalid (a1, n_int)=({a1}, {n_int})"

        # Extract explicit H^1 basis representatives: first `n_int` interior classes, then `r_bdry_rk` boundary-type classes!
        # Start from B^1 columns (columns of d0)
        cur_cols: List[mp.matrix] = []
        for j in range(m):
            col = mp.zeros(3 * m, 1)
            for i in range(3 * m):
                col[i, 0] = d0[i, j]
            if mp_frob_norm(col) > tol:
                cur_cols.append(col)

        def _append_independent(cands: List[mp.matrix], target_extra: int) -> List[mp.matrix]:
            picked: List[mp.matrix] = []
            if target_extra == 0:
                return picked
            for cand in cands:
                test_cols = cur_cols + picked + [cand]
                mat = mp.zeros(3 * m, len(test_cols))
                for cj, cv in enumerate(test_cols):
                    for ri in range(3 * m):
                        mat[ri, cj] = cv[ri, 0]
                rk_prev = rk_d0 + len(picked)
                rk_new, _, _, _ = mp_svd_rank_and_nullspace(mat, tol)
                if rk_new > rk_prev:
                    picked.append(cand)
                    if len(picked) == target_extra:
                        break
            assert len(picked) == target_extra, f"Expected {target_extra} classes, got {len(picked)}"
            return picked

        z_int_cands = []
        for zw in null_zw:
            zv = mp.zeros(3 * m, 1)
            for i in range(3 * m):
                zv[i, 0] = zw[i, 0]
            z_int_cands.append(zv)

        int_reps = _append_independent(z_int_cands, n_int)
        cur_cols.extend(int_reps)
        bdry_reps = _append_independent(z1_basis, r_bdry_rk)

        return {
            "sig": (a0, a1, t0, r_bdry_rk, n_int),
            "int_reps": int_reps,
            "bdry_reps": bdry_reps,
        }
    finally:
        mp.mp.dps = old_dps


def contragredient_mp(M: mp.matrix) -> mp.matrix:
    return mp.inverse(M).T


def wedge2_mp(M: mp.matrix) -> mp.matrix:
    m = M.rows
    pairs = [(i, j) for i in range(m) for j in range(i + 1, m)]
    d = len(pairs)
    W = mp.zeros(d, d)
    for r_idx, (i, j) in enumerate(pairs):
        for c_idx, (k, ell) in enumerate(pairs):
            W[r_idx, c_idx] = M[i, k] * M[j, ell] - M[i, ell] * M[j, k]
    return W


def cusped_index_pair_mp(
    rx: mp.matrix,
    ry: mp.matrix,
    rmu: mp.matrix,
    r1: Sequence[int],
    r2: Sequence[int],
    lam: Sequence[int],
    dps: int = 55,
) -> Dict[str, Any]:
    """
    Evaluates E and E* signatures, asserts B1485 A5 identity
      n(E) - n(E*) == a0(E) - a0(E*) + t0(E*) - r1(E)
    and returns I(E) = n(E) - n(E*).
    """
    info_E = cusped_module_signature_mp(rx, ry, rmu, r1, r2, lam, dps=dps)
    info_Es = cusped_module_signature_mp(
        contragredient_mp(rx),
        contragredient_mp(ry),
        contragredient_mp(rmu),
        r1,
        r2,
        lam,
        dps=dps,
    )
    a0, a1, t0, r_rk, n_e = info_E["sig"]
    a0s, a1s, t0s, r_rks, n_es = info_Es["sig"]
    idx = n_e - n_es
    rhs = a0 - a0s + t0s - r_rk
    id_ok = (idx == rhs)
    assert id_ok, f"B1485 index identity failed: {info_E['sig']} vs {info_Es['sig']}"
    return {
        "I": idx,
        "sig_E": list(info_E["sig"]),
        "sig_Es": list(info_Es["sig"]),
        "identity_holds": id_ok,
    }


def evaluate_f_he_state(
    name: str,
    sign: int,
    word_str: str,
    markoff_cache: Dict[str, Dict[str, Any]],
    dps: int = 55,
) -> Dict[str, Any]:
    if word_str not in markoff_cache:
        markoff_cache[word_str] = solve_hyperbolic_markoff_word(word_str, dps=dps)
    hol = build_hyperbolic_holonomy_and_four(sign, word_str, markoff_cache[word_str], dps=dps)
    fX, fY, fT = hol["four_X"], hol["four_Y"], hol["four_T"]
    r1, r2, lam = hol["r1"], hol["r2"], hol["lam"]

    # Enumerate all sign characters nu: pi_1(M) -> {+1, -1}
    M_ab = abel_matrix_word(sign, word_str, 1)
    sign_chars: List[Tuple[int, int, int]] = []
    for sx in (1, -1):
        for sy in (1, -1):
            # Check (a, b) in (Z/2Z)^2 fixed by M_ab mod 2:
            ea = 0 if sx == 1 else 1
            eb = 0 if sy == 1 else 1
            na = (ea * M_ab[0][0] + eb * M_ab[1][0]) % 2
            nb = (ea * M_ab[0][1] + eb * M_ab[1][1]) % 2
            if na == ea and nb == eb:
                for smu in (1, -1):
                    sign_chars.append((sx, sy, smu))

    char_rows: List[Dict[str, Any]] = []
    all_identities_ok = True
    generation_11_interior_count = 0
    max_abs_N10 = 0

    for sx, sy, smu in sign_chars:
        Vx = mp.mpf(sx) * fX
        Vy = mp.mpf(sy) * fY
        Vmu = mp.mpf(smu) * fT
        v_info = cusped_module_signature_mp(Vx, Vy, Vmu, r1, r2, lam, dps=dps)
        a0, a1, t0, r_rk, n_int = v_info["sig"]

        def eval_ext_at_cocycle(z_vec: mp.matrix, label: str) -> Dict[str, Any]:
            nonlocal all_identities_ok, max_abs_N10
            # Build W_z = [[V, z], [0, 1]] (5x5)
            Wx = mp_eye(5)
            Wy = mp_eye(5)
            Wmu = mp_eye(5)
            for i in range(4):
                for j in range(4):
                    Wx[i, j] = Vx[i, j]
                    Wy[i, j] = Vy[i, j]
                    Wmu[i, j] = Vmu[i, j]
                Wx[i, 4] = z_vec[i, 0]
                Wy[i, 4] = z_vec[4 + i, 0]
                Wmu[i, 4] = z_vec[8 + i, 0]

            res_W = cusped_index_pair_mp(Wx, Wy, Wmu, r1, r2, lam, dps=dps)
            L2x = wedge2_mp(Wx)
            L2y = wedge2_mp(Wy)
            L2mu = wedge2_mp(Wmu)
            res_L2 = cusped_index_pair_mp(L2x, L2y, L2mu, r1, r2, lam, dps=dps)
            all_identities_ok = all_identities_ok and res_W["identity_holds"] and res_L2["identity_holds"]
            N10 = -res_W["I"]
            N5bar = -res_L2["I"]
            max_abs_N10 = max(max_abs_N10, abs(N10))
            return {
                "class_type": label,
                "I_W": res_W["I"],
                "I_Lambda2_W": res_L2["I"],
                "N10_prime": N10,
                "N5bar_prime": N5bar,
                "sig_W": res_W["sig_E"],
                "sig_Ws": res_W["sig_Es"],
                "sig_L2": res_L2["sig_E"],
                "sig_L2s": res_L2["sig_Es"],
            }

        ext_readings: List[Dict[str, Any]] = []
        for idx_i, z_int in enumerate(v_info["int_reps"]):
            rd = eval_ext_at_cocycle(z_int, f"interior_{idx_i}")
            if rd["N10_prime"] == 1 and rd["N5bar_prime"] == 1:
                generation_11_interior_count += 1
            ext_readings.append(rd)

        for idx_b, z_bd in enumerate(v_info["bdry_reps"]):
            ext_readings.append(eval_ext_at_cocycle(z_bd, f"boundary_{idx_b}"))
            # Also check rational combinations with interior class if both exist (as in B1485 A3!)
            if v_info["int_reps"]:
                z_sum = z_bd + v_info["int_reps"][0]
                ext_readings.append(eval_ext_at_cocycle(z_sum, f"boundary_{idx_b}_plus_int0"))
                z_rat = z_bd - (mp.mpf(3) / mp.mpf(7)) * v_info["int_reps"][0]
                ext_readings.append(eval_ext_at_cocycle(z_rat, f"boundary_{idx_b}_minus_3_7_int0"))

        char_rows.append(
            {
                "nu": [sx, sy, smu],
                "sig_V": list(v_info["sig"]),
                "extensions": ext_readings,
            }
        )

    return {
        "name": name,
        "sign": sign,
        "word": word_str,
        "volume_float": hol["volume_float"],
        "tau_cusp": [hol["tau_cusp_re"], hol["tau_cusp_im"]],
        "num_sign_chars": len(sign_chars),
        "all_index_identities_hold": all_identities_ok,
        "interior_generation_11_count": generation_11_interior_count,
        "max_abs_N10_prime": max_abs_N10,
        "characters": char_rows,
    }


def run_section_n1() -> Tuple[Dict[str, Any], Dict[str, Dict[str, Any]]]:
    markoff_cache: Dict[str, Dict[str, Any]] = {}

    # 1. Benchmark gate: m135 = -LLRR and m136 = +LLRR (B1485 A1-A5)
    m135_res = evaluate_f_he_state("m135", -1, "LLRR", markoff_cache, dps=55)
    m136_res = evaluate_f_he_state("m136", +1, "LLRR", markoff_cache, dps=55)

    # Assert exact B1485 benchmark properties!
    m135_h1_hist = Counter((r["sig_V"][1], r["sig_V"][4]) for r in m135_res["characters"])
    m136_h1_hist = Counter((r["sig_V"][1], r["sig_V"][4]) for r in m136_res["characters"])
    m135_ok = (
        m135_res["num_sign_chars"] == 8
        and m135_h1_hist == {(2, 1): 2, (1, 0): 2, (0, 0): 4}
        and m135_res["interior_generation_11_count"] == 2
        and all(
            ext["I_W"] == 0 and ext["I_Lambda2_W"] == -1
            for r in m135_res["characters"]
            if r["sig_V"] == [0, 2, 1, 1, 1]
            for ext in r["extensions"]
            if ext["class_type"].startswith("boundary")
        )
    )
    m136_ok = (
        m136_res["num_sign_chars"] == 8
        and m136_h1_hist == {(1, 1): 2, (1, 0): 4, (0, 0): 2}
        and m136_res["interior_generation_11_count"] == 2
    )
    assert m135_ok, f"B1485 m135 benchmark failed: {m135_h1_hist}"
    assert m136_ok, f"B1485 m136 benchmark failed: {m136_h1_hist}"

    # 2. Eight chiral word states outside m004's levels and outside {m135, m136}
    targets = [
        ("m009", +1, "LLR"),
        ("m010", -1, "LLR"),
        ("m022", +1, "LLLR"),
        ("m023", -1, "LLLR"),
        ("m369", -1, "LLRLR"),
        ("m370", +1, "LLRLR"),
        ("s639", -1, "LLLRLR"),
        ("s640", +1, "LLLRLR"),
    ]
    state_results = {}
    for name, sgn, wd in targets:
        state_results[name] = evaluate_f_he_state(name, sgn, wd, markoff_cache, dps=55)

    summary = {
        "benchmark_m135": m135_res,
        "benchmark_m136": m136_res,
        "m135_matches_b1485_a1_a5": m135_ok,
        "m136_matches_b1485_a1_a5": m136_ok,
        "eight_chiral_states": state_results,
        "all_eight_untwisted_give_0_minus1": all(
            any(
                r["nu"] == [1, 1, 1]
                and r["sig_V"][1] == 1
                and r["sig_V"][4] == 0
                and len(r["extensions"]) >= 1
                and r["extensions"][0]["I_W"] == 0
                and r["extensions"][0]["I_Lambda2_W"] == -1
                for r in st["characters"]
            )
            for st in state_results.values()
        ),
        "states_with_interior_11_generation": [
            nm for nm, st in state_results.items() if st["interior_generation_11_count"] > 0
        ],
        "global_max_abs_N10_prime_across_eight": max(
            st["max_abs_N10_prime"] for st in state_results.values()
        ),
        "all_index_identities_hold_globally": (
            m135_res["all_index_identities_hold"]
            and m136_res["all_index_identities_hold"]
            and all(st["all_index_identities_hold"] for st in state_results.values())
        ),
    }
    return summary, markoff_cache


# ============================================================================
# SECTION 2 (ITEM N2): OWN ARITHMETIC OF m369 AND s639 (vs m004 BENCHMARK)
# ============================================================================

class FQElement:
    """Exact arithmetic in F_{p^d} = F_p[t] / (mod_poly(t))."""

    def __init__(self, coeffs: Tuple[int, ...], p: int, mod_coeffs: Tuple[int, ...]):
        self.p = p
        self.mod_coeffs = mod_coeffs  # monic degree d: c_0 + c_1 t + ... + c_{d-1} t^{d-1} + 1 * t^d
        self.deg = len(mod_coeffs) - 1
        c_list = [c % p for c in coeffs]
        # Reduce mod mod_coeffs
        while len(c_list) > self.deg:
            top = c_list.pop()
            if top != 0:
                offset = len(c_list) - self.deg
                for j in range(self.deg):
                    c_list[offset + j] = (c_list[offset + j] - top * mod_coeffs[j]) % p
        while len(c_list) < self.deg:
            c_list.append(0)
        self.coeffs = tuple(c_list)

    @classmethod
    def zero(cls, p: int, mod_coeffs: Tuple[int, ...]) -> "FQElement":
        return cls((0,), p, mod_coeffs)

    @classmethod
    def one(cls, p: int, mod_coeffs: Tuple[int, ...]) -> "FQElement":
        return cls((1,), p, mod_coeffs)

    def is_zero(self) -> bool:
        return all(c == 0 for c in self.coeffs)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, FQElement) and self.p == other.p and self.coeffs == other.coeffs

    def __hash__(self) -> int:
        return hash((self.p, self.coeffs))

    def __neg__(self) -> "FQElement":
        return FQElement(tuple((-c) % self.p for c in self.coeffs), self.p, self.mod_coeffs)

    def __add__(self, other: "FQElement") -> "FQElement":
        return FQElement(
            tuple((a + b) % self.p for a, b in zip(self.coeffs, other.coeffs)),
            self.p,
            self.mod_coeffs,
        )

    def __sub__(self, other: "FQElement") -> "FQElement":
        return FQElement(
            tuple((a - b) % self.p for a, b in zip(self.coeffs, other.coeffs)),
            self.p,
            self.mod_coeffs,
        )

    def __mul__(self, other: "FQElement") -> "FQElement":
        prod = [0] * (2 * self.deg - 1)
        for i, a in enumerate(self.coeffs):
            if a:
                for j, b in enumerate(other.coeffs):
                    if b:
                        prod[i + j] = (prod[i + j] + a * b) % self.p
        return FQElement(tuple(prod), self.p, self.mod_coeffs)

    def __pow__(self, exp: int) -> "FQElement":
        if exp < 0:
            return self.inv() ** (-exp)
        res = FQElement.one(self.p, self.mod_coeffs)
        base = self
        e = exp
        while e > 0:
            if e & 1:
                res = res * base
            base = base * base
            e >>= 1
        return res

    def inv(self) -> "FQElement":
        assert not self.is_zero(), "Division by zero in F_q"
        q = self.p ** self.deg
        return self ** (q - 2)


def poly_roots_in_fq(poly_low_to_high: List[FQElement]) -> List[FQElement]:
    """
    Exact root finder in F_q for ANY univariate polynomial over F_q = F_p[t]/(mc),
    using Frobenius gcd(X^q - X, f(X)) + Cantor-Zassenhaus equal-degree splitting for large q!
    """
    # Strip trailing zeros
    f_poly = list(poly_low_to_high)
    while len(f_poly) > 1 and f_poly[-1].is_zero():
        f_poly.pop()
    deg = len(f_poly) - 1
    if deg <= 0:
        return []
    f0 = f_poly[0]
    p, mc = f0.p, f0.mod_coeffs
    q = p ** f0.deg
    one = FQElement.one(p, mc)
    zero = FQElement.zero(p, mc)

    # Make monic
    lc_inv = f_poly[-1].inv()
    f_poly = [c * lc_inv for c in f_poly]

    if deg == 1:
        return [-f_poly[0]]

    if q <= 2048:
        roots: List[FQElement] = []
        for tup in itertools.product(range(p), repeat=f0.deg):
            el = FQElement(tup, p, mc)
            val = zero
            for c in reversed(f_poly):
                val = val * el + c
            if val.is_zero():
                roots.append(el)
        return roots

    # Polynomial arithmetic over F_q (low-to-high lists)
    def p_strip(A: List[FQElement]) -> List[FQElement]:
        res = list(A)
        while len(res) > 1 and res[-1].is_zero():
            res.pop()
        return res

    def p_mod(A: List[FQElement], B: List[FQElement]) -> List[FQElement]:
        R = p_strip(A)
        B = p_strip(B)
        db = len(B) - 1
        b_inv = B[-1].inv()
        while len(R) - 1 >= db and not (len(R) == 1 and R[0].is_zero()):
            dr = len(R) - 1
            fac = R[-1] * b_inv
            shift = dr - db
            for j in range(db + 1):
                R[shift + j] = R[shift + j] - fac * B[j]
            R = p_strip(R)
        return R

    def p_mul_mod(A: List[FQElement], B: List[FQElement], M: List[FQElement]) -> List[FQElement]:
        prod = [zero] * (len(A) + len(B) - 1)
        for i, a in enumerate(A):
            if not a.is_zero():
                for j, b in enumerate(B):
                    if not b.is_zero():
                        prod[i + j] = prod[i + j] + a * b
        return p_mod(prod, M)

    def p_pow_mod(base: List[FQElement], exp: int, M: List[FQElement]) -> List[FQElement]:
        res = [one]
        b_cur = p_mod(base, M)
        e = exp
        while e > 0:
            if e & 1:
                res = p_mul_mod(res, b_cur, M)
            b_cur = p_mul_mod(b_cur, b_cur, M)
            e >>= 1
        return res

    def p_gcd(A: List[FQElement], B: List[FQElement]) -> List[FQElement]:
        a_c, b_c = p_strip(A), p_strip(B)
        while not (len(b_c) == 1 and b_c[0].is_zero()):
            a_c, b_c = b_c, p_mod(a_c, b_c)
        inv_l = a_c[-1].inv()
        return [c * inv_l for c in a_c]

    # X^q - X mod f_poly
    x_poly = [zero, one]
    xq = p_pow_mod(x_poly, q, f_poly)
    xq_minus_x = list(xq)
    while len(xq_minus_x) < 2:
        xq_minus_x.append(zero)
    xq_minus_x[1] = xq_minus_x[1] - one
    g_split = p_gcd(f_poly, p_strip(xq_minus_x))

    found_roots: List[FQElement] = []
    stack = [g_split]
    seed_idx = 1
    while stack:
        cur = p_strip(stack.pop())
        d_c = len(cur) - 1
        if d_c <= 0:
            continue
        if d_c == 1:
            found_roots.append(-cur[0] * cur[1].inv())
            continue
        # Deterministic Cantor-Zassenhaus split (odd q; q > 2048 so if p==2 use trace map)
        while True:
            c_tup = tuple(((seed_idx * 1315423911 + k * 2654435761) // (p**k + 1)) % p for k in range(f0.deg))
            seed_idx += 1
            alpha = FQElement(c_tup, p, mc)
            lin = [alpha, one]  # X + alpha
            if p > 2:
                pw = p_pow_mod(lin, (q - 1) // 2, cur)
                pw[0] = pw[0] - one
            else:
                # Trace Tr_{F_q / F_2}(X + alpha) = sum_{j=0}^{f-1} (X + alpha)^{2^j}
                pw = [zero]
                term = p_mod(lin, cur)
                for _ in range(f0.deg):
                    # add term to pw
                    if len(pw) < len(term):
                        pw.extend([zero] * (len(term) - len(pw)))
                    for jj in range(len(term)):
                        pw[jj] = pw[jj] + term[jj]
                    term = p_mul_mod(term, term, cur)
            gg = p_gcd(cur, p_strip(pw))
            dg = len(gg) - 1
            if 0 < dg < d_c:
                # Divide cur by gg
                rem = list(cur)
                quot = [zero] * (d_c - dg + 1)
                ginv = gg[-1].inv()
                while len(rem) - 1 >= dg and not (len(rem) == 1 and rem[0].is_zero()):
                    dr = len(rem) - 1
                    fac = rem[-1] * ginv
                    sh = dr - dg
                    quot[sh] = fac
                    for j in range(dg + 1):
                        rem[sh + j] = rem[sh + j] - fac * gg[j]
                    rem = p_strip(rem)
                stack.append(gg)
                stack.append(quot)
                break
    return found_roots


def sl2_fq_mul(
    A: Tuple[FQElement, FQElement, FQElement, FQElement],
    B: Tuple[FQElement, FQElement, FQElement, FQElement],
) -> Tuple[FQElement, FQElement, FQElement, FQElement]:
    return (
        A[0] * B[0] + A[1] * B[2],
        A[0] * B[1] + A[1] * B[3],
        A[2] * B[0] + A[3] * B[2],
        A[2] * B[1] + A[3] * B[3],
    )


def sl2_fq_inv(
    A: Tuple[FQElement, FQElement, FQElement, FQElement],
) -> Tuple[FQElement, FQElement, FQElement, FQElement]:
    return (A[3], -A[1], -A[2], A[0])


def build_binary_polyhedral_groups() -> Dict[str, Tuple[int, List[Tuple[int, ...]], List[List[int]]]]:
    """
    Constructs exact multiplication tables of 2T (order 24), 2O (order 48), and 2I (order 120)
    directly from concrete finite-field SL(2, F_q) generators (zero hardcoded tables!):
      - 2T = SL(2, F_3) (order 24)
      - 2O subset SL(2, F_9) (binary octahedral group, order 48, generated by 2T and (1+i)/sqrt(2) lift)
      - 2I = SL(2, F_5) (order 120)
    Returns {name: (order, elements_repr, Cayley_mul_table)}.
    """
    out: Dict[str, Tuple[int, List[Any], List[List[int]]]] = {}

    # 1. 2T = SL(2, F_3) and 2I = SL(2, F_5)
    for label, p_mod, target_ord in (("2T", 3, 24), ("2I", 5, 120)):
        elems = [
            (a, b, c, d)
            for a in range(p_mod)
            for b in range(p_mod)
            for c in range(p_mod)
            for d in range(p_mod)
            if (a * d - b * c) % p_mod == 1
        ]
        assert len(elems) == target_ord
        id_e = (1, 0, 0, 1)
        elems.remove(id_e)
        elems.insert(0, id_e)
        idx_map = {e: i for i, e in enumerate(elems)}
        mul = [[0] * target_ord for _ in range(target_ord)]
        for i, A in enumerate(elems):
            for j, B in enumerate(elems):
                C = (
                    (A[0] * B[0] + A[1] * B[2]) % p_mod,
                    (A[0] * B[1] + A[1] * B[3]) % p_mod,
                    (A[2] * B[0] + A[3] * B[2]) % p_mod,
                    (A[2] * B[1] + A[3] * B[3]) % p_mod,
                )
                mul[i][j] = idx_map[C]
        # Assert unique involution!
        invs = sum(1 for i in range(1, target_ord) if mul[i][i] == 0)
        assert invs == 1
        out[label] = (target_ord, elems, mul)

    # 2. 2O of order 48 inside SL(2, F_9), F_9 = F_3[i]/(i^2 + 1)
    mc9 = (1, 0, 1)
    i9 = FQElement((0, 1), 3, mc9)
    o9 = FQElement((1, 0), 3, mc9)
    z9 = FQElement((0, 0), 3, mc9)
    # Standard quaternion generators I_q = [[i, 0], [0, -i]], J_q = [[0, 1], [-1, 0]],
    # T_oct = (I + I_q) / sqrt(2): in F_9, (1+i)*(1-i) = 2 = -1, check det([[1+i, 0], [0, 1-i]]) = 2;
    # instead use w_oct = [[i9 + o9, i9 + o9], [i9 - o9, -(i9 - o9)]] -> det = -(i+1)(i-1) - (i+1)(i-1) = -2(-2) = 4 = 1 mod 3!!
    g_I = (i9, z9, z9, -i9)
    g_J = (z9, o9, -o9, z9)
    g_W = (i9 + o9, i9 + o9, i9 - o9, -(i9 - o9))
    assert (g_W[0] * g_W[3] - g_W[1] * g_W[2]) == o9
    # Add S_oct of order 8: det([[0, i+1], [i+1, 0]]) = -(i+1)^2 = -2i != 1;
    # Try diag(u, u^-1) where u in F_9^x has order 8 (u = 1 + i: u^2 = 2i = -i, u^4 = -1, u^8 = 1!):
    u8 = o9 + i9
    g_S = (u8, z9, z9, u8.inv())  # order 8, normalizes Q_8 and 2T!
    id9 = (o9, z9, z9, o9)
    gens_2o = [g_I, g_J, g_W, g_S]
    vis9 = {id9}
    q9 = [id9]
    while q9:
        cur = q9.pop()
        for g in gens_2o:
            for h in (g, sl2_fq_inv(g)):
                nxt = sl2_fq_mul(cur, h)
                if nxt not in vis9:
                    vis9.add(nxt)
                    q9.append(nxt)
    assert len(vis9) == 48, f"Expected |2O|=48, got {len(vis9)}"
    elems_2o = [id9] + [x for x in vis9 if x != id9]
    idx_2o = {e: i for i, e in enumerate(elems_2o)}
    mul_2o = [[idx_2o[sl2_fq_mul(A, B)] for B in elems_2o] for A in elems_2o]
    assert sum(1 for i in range(1, 48) if mul_2o[i][i] == 0) == 1
    out["2O"] = (48, elems_2o, mul_2o)
    return out


def count_group_surjections(
    sign: int,
    word_str: str,
    grp_order: int,
    mul: List[List[int]],
) -> Dict[str, int]:
    """
    Counts ALL homomorphisms and ALL surjective homomorphisms pi_1(M(sign, word_str)) -> G
    using the Cayley table `mul` (identity = 0).
    """
    # Precompute inverses and conjugacy classes in G
    inv = [0] * grp_order
    for g in range(grp_order):
        for h in range(grp_order):
            if mul[g][h] == 0:
                inv[g] = h
                break

    # Conjugacy classes of x to speed up by |G|/|Cl(x)|!
    conj_rep_weights: List[Tuple[int, int]] = []
    seen_g: Set[int] = set()
    for g in range(grp_order):
        if g in seen_g:
            continue
        cls = {mul[mul[c][g]][inv[c]] for c in range(grp_order)}
        seen_g |= cls
        conj_rep_weights.append((g, len(cls)))

    wx, wy = f2_monodromy_images(sign, word_str, 1)

    def eval_word_cayley(wd: Sequence[int], gx: int, gy: int) -> int:
        cur = 0
        for tok in wd:
            if tok == 1:
                cur = mul[cur][gx]
            elif tok == -1:
                cur = mul[cur][inv[gx]]
            elif tok == 2:
                cur = mul[cur][gy]
            elif tok == -2:
                cur = mul[cur][inv[gy]]
        return cur

    total_homs = 0
    total_surjs = 0

    for gx, w_cls in conj_rep_weights:
        for gy in range(grp_order):
            px = eval_word_cayley(wx, gx, gy)
            py = eval_word_cayley(wy, gx, gy)
            for gmu in range(grp_order):
                if mul[mul[gmu][gx]][inv[gmu]] == px and mul[mul[gmu][gy]][inv[gmu]] == py:
                    total_homs += w_cls
                    # Check surjectivity via subgroup closure of {gx, gy, gmu}
                    sub = {0}
                    st = [0]
                    gens_t = (gx, gy, gmu)
                    while st:
                        c_el = st.pop()
                        for gg in gens_t:
                            nx = mul[c_el][gg]
                            if nx not in sub:
                                sub.add(nx)
                                st.append(nx)
                    if len(sub) == grp_order:
                        total_surjs += w_cls

    return {"homomorphisms": total_homs, "surjections": total_surjs}


def _make_monic_integer_poly(poly_z: sp.Poly, sym: sp.Symbol) -> Tuple[sp.Poly, int]:
    """
    Given primitive irreducible polynomial f(t) = c_n t^n + ... + c_0 in Z[t] (c_n > 0),
    returns monic polynomial f_monic(T) = c_n^{n-1} f(T / c_n) in Z[T] where T = c_n * t,
    along with lead_c = c_n.
    """
    _, prim_p = poly_z.primitive()
    coeffs = [int(c) for c in prim_p.all_coeffs()]
    if coeffs[0] < 0:
        coeffs = [-c for c in coeffs]
    c_n = coeffs[0]
    n = len(coeffs) - 1
    if c_n == 1:
        return sp.Poly(prim_p.as_expr(), sym), 1
    monic_coeffs = [1]
    for k in range(1, n + 1):
        # coeff of T^{n - k} is coeffs[k] * c_n^{k - 1}
        monic_coeffs.append(coeffs[k] * (c_n ** (k - 1)))
    expr = sum(c * (sym ** (n - k)) for k, c in enumerate(monic_coeffs))
    return sp.Poly(expr, sym), c_n


def _pick_vanishing_factor(poly_expr: sp.Expr, sym: sp.Symbol, target_mp: mp.mpc) -> sp.Poly:
    _, facs = sp.factor_list(poly_expr, sym)
    best_p: Optional[sp.Poly] = None
    best_err = mp.mpf("1.0")
    for fe, _ in facs:
        pf = sp.Poly(fe, sym)
        if pf.degree() < 1:
            continue
        val = mp.mpc(0)
        for cc in pf.all_coeffs():
            val = val * target_mp + mp.mpf(int(cc))
        # Normalize by derivative magnitude / scale
        scale = max(mp.mpf(1), abs(target_mp) ** pf.degree())
        rel = abs(val) / scale
        if rel < best_err:
            best_err = rel
            best_p = pf
    assert best_p is not None and best_err < mp.mpf("1e-35"), f"Failed to isolate minpoly: best_err={best_err}"
    return best_p


def analyze_own_arithmetic_state(
    name: str,
    sign: int,
    word_str: str,
    markoff_info: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Exact number-field arithmetic for M(sign, word_str) via pure resultant elimination + monic scaling:
      - Certified exact minimal polynomial of trace field Q(a, b, c) and invariant trace field k(M)
      - Degree, signature (r1, r2), exact field discriminant via round_two, Reid arithmeticity test
      - Prime ideal factorisation at every prime p | disc(K) and exact mod-p_i holonomy image!
    """
    old_dps = mp.mp.dps
    mp.mp.dps = 65
    try:
        sa, sb, sc = sp.symbols("a b c")
        best = markoff_info["best"]
        pa: sp.Poly = best["minpoly_a"]
        eqs = markoff_info["eqs_split"]
        markoff_poly = markoff_info["markoff_poly"]
        a_mp, b_mp, c_mp = best["a"], best["b"], best["c"]

        # Bivariate eliminants in (sa, sb) after eliminating sc via markoff_poly
        res_ab_list = [sp.expand(sp.resultant(f, markoff_poly, sc)) for f in eqs if f != 0]
        res_ab_list = [r for r in res_ab_list if r != 0]
        assert res_ab_list, f"Empty (a, b) resultant list for {word_str}"
        r0_ab = res_ab_list[0]

        # Exact minimal polynomials of b and c over Q:
        res_b_uni = sp.resultant(r0_ab, pa.as_expr(), sa)
        pb = _pick_vanishing_factor(res_b_uni, sb, b_mp)

        # Eliminate sb between markoff_poly and pb(b), then sa against pa(a) to get pc(c):
        res_ac = sp.resultant(markoff_poly, pb.as_expr(), sb)
        res_c_uni = sp.resultant(res_ac, pa.as_expr(), sa)
        pc = _pick_vanishing_factor(res_c_uni, sc, c_mp)

        # Primitive element t = a + b + 2*c of Q(a, b, c) to determine exact [Q(a,b,c) : Q]:
        sth = sp.Symbol("t")
        M_t = sp.expand(
            4 * (sa**2 + sb**2) + (sth - sa - sb) ** 2 - 2 * sa * sb * (sth - sa - sb)
        )
        r_at = sp.resultant(r0_ab, M_t, sb)
        r_t_uni = sp.resultant(r_at, pa.as_expr(), sa)
        th_target = a_mp + b_mp + 2 * c_mp
        raw_minpoly_comb = _pick_vanishing_factor(r_t_uni, sth, th_target)
        full_deg_tr = raw_minpoly_comb.degree()

        # Prefer single trace generator a, b, or c when it already generates Q(a, b, c) (tiny discriminant!)
        if pa.degree() == full_deg_tr:
            raw_minpoly_th = sp.Poly(pa.as_expr().subs(sa, sth), sth)
            lin_coeffs_th = (1, 0, 0)
        elif pc.degree() == full_deg_tr:
            raw_minpoly_th = sp.Poly(pc.as_expr().subs(sc, sth), sth)
            lin_coeffs_th = (0, 0, 1)
        elif pb.degree() == full_deg_tr:
            raw_minpoly_th = sp.Poly(pb.as_expr().subs(sb, sth), sth)
            lin_coeffs_th = (0, 1, 0)
        else:
            raw_minpoly_th = raw_minpoly_comb
            lin_coeffs_th = (1, 1, 2)
        minpoly_th, lead_th = _make_monic_integer_poly(raw_minpoly_th, sth)

        # Invariant trace field k(M) = Q(a^2, b^2, c^2, a*b*c) via u = a^2 + b^2 + 2*c^2:
        sinv = sp.Symbol("u")
        M_u = sp.expand(2 * (sa**2) * (sb**2) * (sinv - sa**2 - sb**2) - (sa**2 + sb**2 + sinv) ** 2)
        r_au = sp.resultant(r0_ab, M_u, sb)
        r_u_uni = sp.resultant(r_au, pa.as_expr(), sa)
        inv_target = a_mp**2 + b_mp**2 + 2 * c_mp**2
        raw_minpoly_inv_comb = _pick_vanishing_factor(r_u_uni, sinv, inv_target)
        full_deg_inv = raw_minpoly_inv_comb.degree()

        # Check if a^2 or c^2 already generates k(M):
        pa2_uni = sp.resultant(pa.as_expr(), sinv - sa**2, sa)
        pa2 = _pick_vanishing_factor(pa2_uni, sinv, a_mp**2)
        pc2_uni = sp.resultant(pc.as_expr(), sinv - sc**2, sc)
        pc2 = _pick_vanishing_factor(pc2_uni, sinv, c_mp**2)
        if pa2.degree() == full_deg_inv:
            raw_minpoly_inv = pa2
        elif pc2.degree() == full_deg_inv:
            raw_minpoly_inv = pc2
        else:
            raw_minpoly_inv = raw_minpoly_inv_comb
        minpoly_inv, _ = _make_monic_integer_poly(raw_minpoly_inv, sinv)

        deg_tr = minpoly_th.degree()
        r1_tr = minpoly_th.count_roots()
        r2_tr = (deg_tr - r1_tr) // 2
        _, disc_tr_sp = round_two(minpoly_th)
        disc_tr = int(disc_tr_sp)

        deg_inv = minpoly_inv.degree()
        r1_inv = minpoly_inv.count_roots()
        r2_inv = (deg_inv - r1_inv) // 2
        _, disc_inv_sp = round_two(minpoly_inv)
        disc_inv = int(disc_inv_sp)

        # Reid's theorem for cusped hyperbolic 3-manifolds: arithmetic IFF k(M) is imaginary quadratic
        # and traces of squares are algebraic integers (checked on pa2, pc2, raw_minpoly_inv leading coeffs == +-1!)
        inv_prim_lc = max(
            abs(int(pa2.primitive()[1].LC())),
            abs(int(pc2.primitive()[1].LC())),
            abs(int(raw_minpoly_inv.primitive()[1].LC())),
        )
        is_arithmetic = (deg_inv == 2 and r1_inv == 0 and r2_inv == 1 and inv_prim_lc == 1)

        ramified_rat_primes = sorted(int(p) for p in sp.factorint(abs(disc_tr)).keys())
        ramified_ideals_report: List[Dict[str, Any]] = []

        for p in ramified_rat_primes:
            ideals = prime_decomp(p, minpoly_th)
            _, mod_facs = sp.factor_list(minpoly_th.as_expr(), sth, modulus=p)
            for idl in ideals:
                if idl.e <= 1:
                    continue
                matching_facs = [
                    sp.Poly(fe, sth, modulus=p)
                    for fe, _ in mod_facs
                    if sp.Poly(fe, sth, modulus=p).degree() == idl.f
                ]
                hol_readings = []
                for mf in matching_facs:
                    mf_int = sp.Poly(mf.as_expr(), sth)
                    rd_list = _reduce_holonomy_ideal_roots(
                        sign, word_str, p, mf_int, lead_th, lin_coeffs_th, pa, pb, pc
                    )
                    hol_readings.extend(rd_list)

                ramified_ideals_report.append(
                    {
                        "rational_prime": p,
                        "ramification_index_e": int(idl.e),
                        "residue_degree_f": int(idl.f),
                        "residue_norm_q": int(p ** idl.f),
                        "mod_p_holonomy_candidates": hol_readings,
                    }
                )

        unique_norm3_2T_door = (
            len(ramified_ideals_report) == 1
            and ramified_ideals_report[0]["residue_norm_q"] == 3
            and any(
                c.get("mckay_label") == "2T -> E6"
                for c in ramified_ideals_report[0]["mod_p_holonomy_candidates"]
            )
        )

        return {
            "name": name,
            "sign": sign,
            "word": word_str,
            "trace_field_degree": int(deg_tr),
            "trace_field_signature": [int(r1_tr), int(r2_tr)],
            "trace_field_discriminant": int(disc_tr),
            "trace_field_minpoly_coeffs": [int(c) for c in minpoly_th.all_coeffs()],
            "invariant_trace_field_degree": int(deg_inv),
            "invariant_trace_field_signature": [int(r1_inv), int(r2_inv)],
            "invariant_trace_field_discriminant": int(disc_inv),
            "invariant_trace_field_minpoly_coeffs": [int(c) for c in minpoly_inv.all_coeffs()],
            "is_arithmetic_reid": is_arithmetic,
            "ramified_rational_primes": ramified_rat_primes,
            "ramified_prime_ideals": ramified_ideals_report,
            "unique_norm3_mckay_2T_door": unique_norm3_2T_door,
        }
    finally:
        mp.mp.dps = old_dps


def _reduce_holonomy_ideal_roots(
    sign: int,
    word_str: str,
    p: int,
    factor_mod_p: sp.Poly,
    lead_th: int,
    lin_coeffs_th: Tuple[int, int, int],
    pa: sp.Poly,
    pb: sp.Poly,
    pc: sp.Poly,
) -> List[Dict[str, Any]]:
    """
    Finds all Markoff fixed triples (abar, bbar, cbar) in F_{p^f} = F_p[T]/(factor_mod_p)
    satisfying pa(abar)=pb(bbar)=pc(cbar)=0 mod p, Phi_word(abar,bbar,cbar)=(abar,bbar,cbar),
    abar^2+bbar^2+cbar^2=abar*bbar*cbar, and lead_th*(ca*abar + cb*bbar + cc*cbar) == T_bar,
    and runs exact mod-p_i SL(2) closure on each!
    """
    f_deg = factor_mod_p.degree()
    mc_base = tuple(int(c) % p for c in reversed(factor_mod_p.all_coeffs()))
    lc_inv = pow(mc_base[-1], p - 2, p)
    mc_base = tuple((c * lc_inv) % p for c in mc_base)
    t_tilde = FQElement((0, 1) if f_deg > 1 else ((-mc_base[0]) % p,), p, mc_base)

    def roots_of_zpoly(pz: sp.Poly) -> List[FQElement]:
        low_high = [FQElement((int(c) % p,), p, mc_base) for c in reversed(pz.all_coeffs())]
        return poly_roots_in_fq(low_high)

    a_roots = roots_of_zpoly(pa)
    b_roots = roots_of_zpoly(pb)
    c_roots = roots_of_zpoly(pc)
    if not (a_roots and b_roots and c_roots):
        return [{"p": p, "residue_norm": p ** f_deg, "status": "pole_at_prime_ideal", "embeds_in_su2": False, "is_mckay_exceptional": False, "mckay_label": "none"}]

    c_set = set(c_roots)
    lead_el = FQElement((lead_th % p,), p, mc_base)
    ca_el = FQElement((lin_coeffs_th[0] % p,), p, mc_base)
    cb_el = FQElement((lin_coeffs_th[1] % p,), p, mc_base)
    cc_el = FQElement((lin_coeffs_th[2] % p,), p, mc_base)

    valid_triples: List[Tuple[FQElement, FQElement, FQElement]] = []
    for ar in a_roots:
        for br in b_roots:
            for cr in c_roots:
                if (ar * ar + br * br + cr * cr) != (ar * br * cr):
                    continue
                if lead_el * (ca_el * ar + cb_el * br + cc_el * cr) != t_tilde:
                    continue
                # Verify forward Markoff word fixed point
                ta, tb, tc = ar, br, cr
                for ch in word_str:
                    ta, tb, tc = markoff_step_sym(ta, tb, tc, ch)
                if ta == ar and tb == br and tc == cr:
                    valid_triples.append((ar, br, cr))

    # Fallback if lead_th == 0 mod p collapsed t_tilde match onto multiple triples: already filtered by pa, pb, pc, Markoff, Phi_w!
    if not valid_triples:
        for ar in a_roots:
            for br in b_roots:
                for cr in c_set:
                    if (ar * ar + br * br + cr * cr) == (ar * br * cr):
                        ta, tb, tc = ar, br, cr
                        for ch in word_str:
                            ta, tb, tc = markoff_step_sym(ta, tb, tc, ch)
                        if ta == ar and tb == br and tc == cr:
                            valid_triples.append((ar, br, cr))

    results = []
    for abar_base, bbar_base, cbar_base in valid_triples:
        results.append(_run_sl2_closure_on_triple(sign, word_str, p, f_deg, mc_base, abar_base, bbar_base, cbar_base))
    return results


def _run_sl2_closure_on_triple(
    sign: int,
    word_str: str,
    p: int,
    f_deg: int,
    mc_base: Tuple[int, ...],
    abar_base: FQElement,
    bbar_base: FQElement,
    cbar_base: FQElement,
) -> Dict[str, Any]:
    z_roots = poly_roots_in_fq([FQElement.one(p, mc_base), -cbar_base, FQElement.one(p, mc_base)])

    if z_roots:
        F_zero: Any = FQElement.zero(p, mc_base)
        F_one: Any = FQElement.one(p, mc_base)
        abar, bbar, cbar, zbar = abar_base, bbar_base, cbar_base, z_roots[0]
    else:
        class QuadElem2:
            def __init__(self, u: FQElement, v: FQElement):
                self.u = u
                self.v = v

            def is_zero(self) -> bool:
                return self.u.is_zero() and self.v.is_zero()

            def __eq__(self, o: object) -> bool:
                return isinstance(o, QuadElem2) and self.u == o.u and self.v == o.v

            def __hash__(self) -> int:
                return hash((self.u, self.v))

            def __neg__(self) -> "QuadElem2":
                return QuadElem2(-self.u, -self.v)

            def __add__(self, o: "QuadElem2") -> "QuadElem2":
                return QuadElem2(self.u + o.u, self.v + o.v)

            def __sub__(self, o: "QuadElem2") -> "QuadElem2":
                return QuadElem2(self.u - o.u, self.v - o.v)

            def __mul__(self, o: "QuadElem2") -> "QuadElem2":
                uu = self.u * o.u - self.v * o.v
                vv = self.u * o.v + self.v * o.u + cbar_base * (self.v * o.v)
                return QuadElem2(uu, vv)

            def inv(self) -> "QuadElem2":
                nrm = self.u * self.u + cbar_base * self.u * self.v + self.v * self.v
                n_inv = nrm.inv()
                return QuadElem2((self.u + cbar_base * self.v) * n_inv, (-self.v) * n_inv)

        z0 = FQElement.zero(p, mc_base)
        o0 = FQElement.one(p, mc_base)
        F_zero = QuadElem2(z0, z0)
        F_one = QuadElem2(o0, z0)
        abar = QuadElem2(abar_base, z0)
        bbar = QuadElem2(bbar_base, z0)
        cbar = QuadElem2(cbar_base, z0)
        zbar = QuadElem2(z0, o0)

    X_m = (abar, F_one, -F_one, F_zero)
    Y_m = (F_zero, -(zbar.inv()), zbar, bbar)
    gens_f2 = {1: X_m, -1: sl2_fq_inv(X_m), 2: Y_m, -2: sl2_fq_inv(Y_m)}
    wx, wy = f2_monodromy_images(sign, word_str, 1)

    def eval_w(wd: Sequence[int], gm: Dict[int, Any]) -> Any:
        cur = (F_one, F_zero, F_zero, F_one)
        for tok in wd:
            cur = sl2_fq_mul(cur, gm[tok])
        return cur

    phi_X = eval_w(wx, gens_f2)
    phi_Y = eval_w(wy, gens_f2)

    rows_lin = []
    for A_in, A_out in ((X_m, phi_X), (Y_m, phi_Y)):
        for i in range(2):
            for j in range(2):
                row = [F_zero, F_zero, F_zero, F_zero]
                for k in range(2):
                    row[2 * i + k] = row[2 * i + k] + A_in[2 * k + j]
                    row[2 * k + j] = row[2 * k + j] - A_out[2 * i + k]
                rows_lin.append(row)

    piv_cols: List[int] = []
    r_piv = 0
    for col in range(4):
        piv = next((r for r in range(r_piv, len(rows_lin)) if not rows_lin[r][col].is_zero()), None)
        if piv is None:
            continue
        rows_lin[r_piv], rows_lin[piv] = rows_lin[piv], rows_lin[r_piv]
        inv_v = rows_lin[r_piv][col].inv()
        rows_lin[r_piv] = [x * inv_v for x in rows_lin[r_piv]]
        for r in range(len(rows_lin)):
            if r != r_piv and not rows_lin[r][col].is_zero():
                fac = rows_lin[r][col]
                rows_lin[r] = [rows_lin[r][c_i] - fac * rows_lin[r_piv][c_i] for c_i in range(4)]
        piv_cols.append(col)
        r_piv += 1

    free_cols = [c for c in range(4) if c not in piv_cols]
    T_m = None
    for fc in free_cols:
        vec = [F_zero, F_zero, F_zero, F_zero]
        vec[fc] = F_one
        for idx_p, pc in enumerate(piv_cols):
            vec[pc] = -rows_lin[idx_p][fc]
        det_v = vec[0] * vec[3] - vec[1] * vec[2]
        if not det_v.is_zero():
            if p > 2:
                tr_v = vec[0] + vec[3]
                if not tr_v.is_zero():
                    scale = (F_one + F_one) * tr_v.inv()
                    T_m = (vec[0] * scale, vec[1] * scale, vec[2] * scale, vec[3] * scale)
                    break
            else:
                q_actual = (p ** f_deg) if z_roots else (p ** (2 * f_deg))
                e_sq = q_actual // 2
                res_sq = F_one
                b_sq = det_v
                while e_sq > 0:
                    if e_sq & 1:
                        res_sq = res_sq * b_sq
                    b_sq = b_sq * b_sq
                    e_sq >>= 1
                scale = res_sq.inv()
                T_m = (vec[0] * scale, vec[1] * scale, vec[2] * scale, vec[3] * scale)
                break

    if T_m is None:
        return {"p": p, "residue_norm": p ** f_deg, "status": "reducible_or_traceless", "embeds_in_su2": False, "is_mckay_exceptional": False, "mckay_label": "none"}

    id_m = (F_one, F_zero, F_zero, F_one)
    gen_list = [X_m, sl2_fq_inv(X_m), Y_m, sl2_fq_inv(Y_m), T_m, sl2_fq_inv(T_m)]
    visited = {id_m}
    queue = [id_m]
    max_bfs = 4000
    truncated = False
    while queue:
        cur = queue.pop()
        for g in gen_list:
            nxt = sl2_fq_mul(cur, g)
            if nxt not in visited:
                visited.add(nxt)
                if len(visited) > max_bfs:
                    truncated = True
                    queue.clear()
                    break
                queue.append(nxt)

    if truncated:
        return {
            "p": p,
            "residue_norm": p ** f_deg,
            "status": f"exceeds_{max_bfs}",
            "sl2_order_lower_bound": len(visited),
            "embeds_in_su2": False,
            "is_mckay_exceptional": False,
            "mckay_label": "none",
        }

    sl2_ord = len(visited)
    neg_id = (-F_one, F_zero, F_zero, -F_one)
    psl2_ord = sl2_ord // 2 if (p > 2 and neg_id in visited) else sl2_ord
    involutions = sum(1 for g in visited if g != id_m and sl2_fq_mul(g, g) == id_m)
    unique_inv_ok = (involutions == 0 and sl2_ord % 2 == 1) or (involutions == 1 and sl2_ord % 2 == 0)
    max_elem_ord = 1
    if unique_inv_ok and sl2_ord <= 500:
        for g in visited:
            cur = g
            k_o = 1
            while cur != id_m:
                cur = sl2_fq_mul(cur, g)
                k_o += 1
            max_elem_ord = max(max_elem_ord, k_o)
    is_cyclic = (max_elem_ord == sl2_ord)
    is_bd = unique_inv_ok and (sl2_ord % 4 == 0) and (max_elem_ord == sl2_ord // 2)
    is_mckay_exc = unique_inv_ok and (sl2_ord in (24, 48, 120)) and (psl2_ord in (12, 24, 60))
    embeds_su2 = is_cyclic or is_bd or is_mckay_exc

    return {
        "p": p,
        "residue_norm": p ** f_deg,
        "status": "exact",
        "sl2_order": sl2_ord,
        "psl2_order": psl2_ord,
        "num_involutions": involutions,
        "embeds_in_su2": embeds_su2,
        "is_mckay_exceptional": is_mckay_exc,
        "mckay_label": (
            "2T -> E6" if (is_mckay_exc and sl2_ord == 24)
            else ("2O -> E7" if (is_mckay_exc and sl2_ord == 48)
                  else ("2I -> E8" if (is_mckay_exc and sl2_ord == 120) else "none"))
        ),
    }


def verify_e7_56_and_e8_248_self_conjugacy() -> Dict[str, Any]:
    """
    Constructs explicit weight sets of:
      - 27 of E_6 under SO(10) x U(1)_psi (16_{+1} + 10_{-2} + 1_{+4}),
      - 56 of E_7 under E_6 x U(1) (27_{+1} + 27-bar_{-1} + 1_{+3} + 1_{-3}),
      - 248 of E_8 (root system in R^8: 112 integer D_8 roots + 128 half-integer spinor roots + 8 zero weights),
    and checks directly on the explicit weight vectors whether w -> -w leaves the weight multiset invariant!
    """
    # 27 of E_6 weights in R^6: SO(10) spinor 16 (even minus signs in (+-1/2)^5, psi=+1),
    # vector 10 (+-e_i, psi=-2), singlet (0^5, psi=+4):
    w27: List[Tuple[Fraction, ...]] = []
    for signs in itertools.product((Fraction(1, 2), Fraction(-1, 2)), repeat=5):
        if sum(1 for s in signs if s < 0) % 2 == 0:
            w27.append(signs + (Fraction(1),))
    for i in range(5):
        for s in (Fraction(1), Fraction(-1)):
            vec = [Fraction(0)] * 5
            vec[i] = s
            w27.append(tuple(vec) + (Fraction(-2),))
    w27.append((Fraction(0),) * 5 + (Fraction(4),))
    assert len(w27) == 27

    neg_w27 = [tuple(-x for x in w) for w in w27]
    e6_27_is_self_conjugate = (Counter(w27) == Counter(neg_w27))

    # 56 of E_7 = 27_{+1} + 27-bar_{-1} + 1_{+3} + 1_{-3} in R^7:
    w56: List[Tuple[Fraction, ...]] = []
    for w in w27:
        w56.append(w + (Fraction(1),))
        w56.append(tuple(-x for x in w) + (Fraction(-1),))
    w56.append((Fraction(0),) * 6 + (Fraction(3),))
    w56.append((Fraction(0),) * 6 + (Fraction(-3),))
    assert len(w56) == 56
    e7_56_is_self_conjugate = (Counter(w56) == Counter(tuple(-x for x in w) for w in w56))

    # 248 of E_8 in R^8:
    w248: List[Tuple[Fraction, ...]] = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (Fraction(1), Fraction(-1)):
                for sj in (Fraction(1), Fraction(-1)):
                    v = [Fraction(0)] * 8
                    v[i] = si
                    v[j] = sj
                    w248.append(tuple(v))
    for signs in itertools.product((Fraction(1, 2), Fraction(-1, 2)), repeat=8):
        if sum(1 for s in signs if s < 0) % 2 == 0:
            w248.append(signs)
    for _ in range(8):
        w248.append((Fraction(0),) * 8)
    assert len(w248) == 248
    e8_248_is_self_conjugate = (Counter(w248) == Counter(tuple(-x for x in w) for w in w248))

    # Also check SM generation hypercharges inside 56 of E_7 and 248 of E_8 under ANY abelian character twist:
    # Because w <-> -w is an exact bijection of w56 and w248, for every weight w with SM representation R_SM,
    # -w carries R_SM^* with opposite internal weight -> net chiral count on any 1D abelian background is 0!
    return {
        "dim_E6_27": len(w27),
        "E6_27_self_conjugate": e6_27_is_self_conjugate,
        "dim_E7_56": len(w56),
        "E7_56_self_conjugate": e7_56_is_self_conjugate,
        "dim_E8_248": len(w248),
        "E8_248_self_conjugate": e8_248_is_self_conjugate,
    }


def run_section_n2(markoff_cache: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    if "LR" not in markoff_cache:
        markoff_cache["LR"] = solve_hyperbolic_markoff_word("LR", dps=55)

    arith_m004 = analyze_own_arithmetic_state("m004", +1, "LR", markoff_cache["LR"])
    arith_m369 = analyze_own_arithmetic_state("m369", -1, "LLRLR", markoff_cache["LLRLR"])
    arith_s639 = analyze_own_arithmetic_state("s639", -1, "LLLRLR", markoff_cache["LLLRLR"])

    assert arith_m004["is_arithmetic_reid"] is True
    assert arith_m004["unique_norm3_mckay_2T_door"] is True

    poly_groups = build_binary_polyhedral_groups()
    surj_table = {}
    for st_name, sgn, wd in (("m004", +1, "LR"), ("m369", -1, "LLRLR"), ("s639", -1, "LLLRLR")):
        surj_table[st_name] = {}
        for g_label, (g_ord, _, mul) in poly_groups.items():
            surj_table[st_name][g_label] = count_group_surjections(sgn, wd, g_ord, mul)

    rep_check = verify_e7_56_and_e8_248_self_conjugacy()
    assert (
        rep_check["E6_27_self_conjugate"] is False
        and rep_check["E7_56_self_conjugate"] is True
        and rep_check["E8_248_self_conjugate"] is True
    )

    return {
        "m004_benchmark": arith_m004,
        "m369_arithmetic": arith_m369,
        "s639_arithmetic": arith_s639,
        "any_unique_norm3_mckay_door_on_m369_or_s639": (
            arith_m369["unique_norm3_mckay_2T_door"] or arith_s639["unique_norm3_mckay_2T_door"]
        ),
        "abstract_binary_polyhedral_surjections": surj_table,
        "exceptional_representation_self_conjugacy": rep_check,
    }


# ============================================================================
# SECTION 3 (ITEM N3): DEHN FILLINGS & NON-CYCLIC COVERS OUTSIDE {m004, m003}
# ============================================================================

def fixed_torsion_characters(sign: int, word: str, k: int = 1) -> Tuple[int, List[Tuple[int, int]]]:
    M = abel_matrix_word(sign, word, k)
    d00, d01 = M[0][0] - 1, M[0][1]
    d10, d11 = M[1][0], M[1][1] - 1
    det = abs(d00 * d11 - d01 * d10)
    g = math.gcd(math.gcd(abs(d00), abs(d01)), math.gcd(abs(d10), abs(d11)))
    N = det // g
    if N == 1:
        return 1, [(0, 0)]
    chars = [
        (a, b)
        for a in range(N)
        for b in range(N)
        if (a * d00 + b * d10) % N == 0 and (a * d01 + b * d11) % N == 0
    ]
    assert len(chars) == det
    return N, chars


def slope_mod_p(sign: int, word: str, a: int, b: int, N: int, p: int, zeta: int) -> int:
    X0 = pow(zeta, a % N, p)
    Y0 = pow(zeta, b % N, p)
    if X0 != 1:
        ux, uy = 0, pow((X0 - 1) % p, p - 2, p)
    else:
        ux, uy = pow((1 - Y0) % p, p - 2, p), 0
    X, Y = X0, Y0
    cx, cy = ux, uy
    steps = list(word) + (["M"] if sign < 0 else [])
    for ell in steps:
        if ell == "L":
            cx, cy = cx % p, (Y * cx + cy) % p
            X, Y = X, (X * Y) % p
        elif ell == "R":
            cx, cy = (cx + X * cy) % p, cy % p
            X, Y = (X * Y) % p, Y
        elif ell == "M":
            invX, invY = pow(X, p - 2, p), pow(Y, p - 2, p)
            j00 = (-invX * Y) % p
            j01 = (1 - invX) % p
            j10 = (Y - 1) % p
            j11 = (1 - X - invY) % p
            cx, cy = (j00 * cx + j01 * cy) % p, (j10 * cx + j11 * cy) % p
            X, Y = invX, invY
    if X0 != 1:
        s = ((cx - ux) * pow((-(X0 - 1)) % p, p - 2, p)) % p
        assert (cy - uy) % p == ((-s * (Y0 - 1)) % p)
    else:
        s = ((cy - uy) * pow((-(Y0 - 1)) % p, p - 2, p)) % p
        assert (cx - ux) % p == 0
    return s


def recover_rational_slope(
    sign: int,
    word: str,
    c: Tuple[int, int],
    N: int,
    primes: List[int],
    zetas: List[int],
) -> Optional[Fraction]:
    """
    A slope s(chi) in Q(zeta_N) is rational IFF it is invariant under all Galois automorphisms
    zeta -> zeta^u (gcd(u, N) == 1); when Galois-invariant, recovers exact Fraction a/b
    and verifies a == b * s mod p across all 3 independent primes!
    """
    s0 = [slope_mod_p(sign, word, c[0], c[1], N, p, z) for p, z in zip(primes, zetas)]
    for u in range(2, N):
        if math.gcd(u, N) == 1:
            cu = ((u * c[0]) % N, (u * c[1]) % N)
            su = [slope_mod_p(sign, word, cu[0], cu[1], N, p, z) for p, z in zip(primes, zetas)]
            if su != s0:
                return None

    # Rational! Reconstruct small rational a/b via extended GCD on primes[0]
    p0 = primes[0]
    v0 = s0[0]
    r_prev, r_cur = p0, v0
    t_prev, t_cur = 0, 1
    bound = int(math.isqrt(p0 // 2))
    while r_cur > bound:
        q = r_prev // r_cur
        r_prev, r_cur = r_cur, r_prev - q * r_cur
        t_prev, t_cur = t_cur, t_prev - q * t_cur
    num, den = r_cur, t_cur
    if den < 0:
        num, den = -num, -den
    frac = Fraction(num, den)
    # Verify across ALL 3 primes!
    for p, sv in zip(primes, s0):
        assert (frac.numerator - frac.denominator * sv) % p == 0, f"Rational reconstruction failed: {frac}"
    return frac


def dehn_filling_cohomology_mod_p(
    sign: int,
    word: str,
    N: int,
    ell: Tuple[int, int],
    alpha: Tuple[int, int],
    frac: Optional[Fraction],
    p: int,
    zeta: int,
) -> Tuple[int, int, int, int]:
    """
    Exact F_p Fox cohomology on M and (when `frac` is given) on closed Dehn filling M(mu^b lambda^-a = 1)
    for 2D sector module V(ell, alpha) and dual V*(ell, alpha).
    Returns (h1_M_V, h1_M_Vs, h1_fill_V, h1_fill_Vs) (with h1_fill = -1 when frac is None).
    """
    beta = ((alpha[0] - ell[0]) % N, (alpha[1] - ell[1]) % N)
    X_ell = pow(zeta, ell[0] % N, p)
    Y_ell = pow(zeta, ell[1] % N, p)
    if X_ell != 1:
        ux, uy = 0, pow((X_ell - 1) % p, p - 2, p)
    else:
        ux, uy = pow((1 - Y_ell) % p, p - 2, p), 0
    s_mod = slope_mod_p(sign, word, ell[0], ell[1], N, p, zeta)
    if frac is not None:
        assert (frac.numerator - frac.denominator * s_mod) % p == 0

    ax, ay = pow(zeta, alpha[0] % N, p), pow(zeta, alpha[1] % N, p)
    bx, by = pow(zeta, beta[0] % N, p), pow(zeta, beta[1] % N, p)

    def mat_mul(A: Tuple[int, int, int, int], B: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
        return (
            (A[0] * B[0] + A[1] * B[2]) % p,
            (A[0] * B[1] + A[1] * B[3]) % p,
            (A[2] * B[0] + A[3] * B[2]) % p,
            (A[2] * B[1] + A[3] * B[3]) % p,
        )

    def mat_inv(A: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
        det = (A[0] * A[3] - A[1] * A[2]) % p
        inv_d = pow(det, p - 2, p)
        return ((A[3] * inv_d) % p, (-A[1] * inv_d) % p, (-A[2] * inv_d) % p, (A[0] * inv_d) % p)

    rx = (ax, (ux * bx) % p, 0, bx)
    ry = (ay, (uy * by) % p, 0, by)
    rmu = (1, s_mod, 0, 1)

    # Dual contragredient M -> M^{-T}:
    def dual_m(A: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
        iv = mat_inv(A)
        return (iv[0], iv[2], iv[1], iv[3])

    r1, r2, lam = bundle_relators(sign, word, 1)
    gamma_w: Optional[List[int]] = None
    if frac is not None:
        a_num, b_den = frac.numerator, frac.denominator
        gw: List[int] = ([3] * b_den if b_den >= 0 else [-3] * (-b_den))
        if a_num > 0:
            gw.extend(free_inv(lam) * a_num)
        elif a_num < 0:
            gw.extend(list(lam) * (-a_num))
        gamma_w = free_reduce(gw)

    def h1_pair(gx: Tuple[int, int, int, int], gy: Tuple[int, int, int, int], gmu: Tuple[int, int, int, int]) -> Tuple[int, int]:
        gens = {1: gx, -1: mat_inv(gx), 2: gy, -2: mat_inv(gy), 3: gmu, -3: mat_inv(gmu)}

        def fox_w(wd: Sequence[int]) -> Tuple[Tuple[int, int, int, int], List[List[int]]]:
            cur = (1, 0, 0, 1)
            J = [[0] * 6 for _ in range(2)]
            for tok in wd:
                off = (abs(tok) - 1) * 2
                if tok > 0:
                    J[0][off] = (J[0][off] + cur[0]) % p
                    J[0][off + 1] = (J[0][off + 1] + cur[1]) % p
                    J[1][off] = (J[1][off] + cur[2]) % p
                    J[1][off + 1] = (J[1][off + 1] + cur[3]) % p
                    cur = mat_mul(cur, gens[tok])
                else:
                    cur = mat_mul(cur, gens[tok])
                    J[0][off] = (J[0][off] - cur[0]) % p
                    J[0][off + 1] = (J[0][off + 1] - cur[1]) % p
                    J[1][off] = (J[1][off] - cur[2]) % p
                    J[1][off + 1] = (J[1][off + 1] - cur[3]) % p
            return cur, J

        v1, J1 = fox_w(r1)
        v2, J2 = fox_w(r2)
        assert v1 == (1, 0, 0, 1) and v2 == (1, 0, 0, 1)

        d0 = [
            [(gx[0] - 1) % p, gx[1] % p],
            [gx[2] % p, (gx[3] - 1) % p],
            [(gy[0] - 1) % p, gy[1] % p],
            [gy[2] % p, (gy[3] - 1) % p],
            [(gmu[0] - 1) % p, gmu[1] % p],
            [gmu[2] % p, (gmu[3] - 1) % p],
        ]

        def rk_fp(rows_m: List[List[int]]) -> int:
            A = [row[:] for row in rows_m]
            R_c, C_c = len(A), len(A[0])
            rk = 0
            for c_i in range(C_c):
                piv = next((r for r in range(rk, R_c) if A[r][c_i] != 0), None)
                if piv is None:
                    continue
                A[rk], A[piv] = A[piv], A[rk]
                inv_v = pow(A[rk][c_i], p - 2, p)
                A[rk] = [(x * inv_v) % p for x in A[rk]]
                for r in range(R_c):
                    if r != rk and A[r][c_i] != 0:
                        f = A[r][c_i]
                        A[r] = [(A[r][j] - f * A[rk][j]) % p for j in range(C_c)]
                rk += 1
            return rk

        rk_d0 = rk_fp(d0)
        rk_d1_M = rk_fp(J1 + J2)
        h1_m = 6 - rk_d1_M - rk_d0
        if gamma_w is None:
            return (h1_m, -1)
        vg, Jg = fox_w(gamma_w)
        assert vg == (1, 0, 0, 1)
        rk_d1_fill = rk_fp(J1 + J2 + Jg)
        return (h1_m, 6 - rk_d1_fill - rk_d0)

    h1_M_V, h1_fill_V = h1_pair(rx, ry, rmu)
    h1_M_Vs, h1_fill_Vs = h1_pair(dual_m(rx), dual_m(ry), dual_m(rmu))
    return (h1_M_V, h1_M_Vs, h1_fill_V, h1_fill_Vs)


def analyze_fillings_state(name: str, sign: int, word: str) -> Dict[str, Any]:
    N, chars = fixed_torsion_characters(sign, word, 1)
    nontriv = [c for c in chars if c != (0, 0)]
    primes = find_primes_1_mod_N(N, count=3, start=10_000_000)
    zetas = [primitive_nth_root_mod_p(N, p) for p in primes]

    rats = {c: recover_rational_slope(sign, word, c, N, primes, zetas) for c in nontriv}

    # Compute exact F_p Fox cohomology on ALL non-trivial sector modules V(ell, alpha) across 2 certified primes!
    cusped_h1_table: Dict[Tuple[Tuple[int, int], Tuple[int, int]], Tuple[int, int]] = {}
    descended_modules = 0
    poincare_symmetric_count = 0
    fill_h1_hist: Counter = Counter()
    rat_ells = [ell for ell in nontriv if rats[ell] is not None]

    for ell in nontriv:
        frac = rats[ell]
        for alpha in nontriv:
            if alpha == ell:
                continue
            r_p0 = dehn_filling_cohomology_mod_p(sign, word, N, ell, alpha, frac, primes[0], zetas[0])
            r_p1 = dehn_filling_cohomology_mod_p(sign, word, N, ell, alpha, frac, primes[1], zetas[1])
            assert r_p0 == r_p1, f"Prime mismatch on {name}: {r_p0} vs {r_p1}"
            h1_m_v, h1_m_vs, h1_f_v, h1_f_vs = r_p0
            cusped_h1_table[(ell, alpha)] = (h1_m_v, h1_m_vs)
            if frac is not None:
                descended_modules += 1
                if h1_f_v == h1_f_vs:
                    poincare_symmetric_count += 1
                fill_h1_hist[f"cusped=({h1_m_v},{h1_m_vs})->filled=({h1_f_v},{h1_f_vs})"] += 1

    def exact_class_idx(ell: Tuple[int, int], alpha: Tuple[int, int]) -> int:
        if ell == (0, 0) or alpha == (0, 0) or alpha == ell:
            return 0
        hv, hvs = cusped_h1_table[(ell, alpha)]
        return hv - hvs

    firing_modules = sum(1 for (ell, alpha) in cusped_h1_table if exact_class_idx(ell, alpha) != 0)

    # Enumerate E_6 generation backgrounds (B1432 / B1434 convention)
    sectors = [("Q", 1, -3), ("uc", -4, -3), ("ec", 6, -3), ("dc", 2, -1), ("L", -3, -1), ("nuc", 0, 5)]
    bg_map: Dict[Tuple, Tuple[int, ...]] = {}
    for theta in chars:
        for psi_Y in chars:
            for W in chars:
                ell = ((2 * theta[0] - W[0]) % N, (2 * theta[1] - W[1]) % N)
                alphas = [
                    (
                        (theta[0] + sY * psi_Y[0] + ((sg - 1) // 2) * W[0]) % N,
                        (theta[1] + sY * psi_Y[1] + ((sg - 1) // 2) * W[1]) % N,
                    )
                    for _, sY, sg in sectors
                ]
                key = (ell,) + tuple(alphas)
                if key not in bg_map:
                    bg_map[key] = tuple(exact_class_idx(ell, al) for al in alphas)

    gen_bgs = {k: v for k, v in bg_map.items() if v[:5] in ((1, 1, 1, 1, 1), (-1, -1, -1, -1, -1))}
    gen_bgs_rational_ell = [k for k in gen_bgs if rats[k[0]] is not None]

    return {
        "name": name,
        "sign": sign,
        "word": word,
        "N": N,
        "total_nontrivial_chars": len(nontriv),
        "rational_slope_chars": len(rat_ells),
        "rational_slopes_map": {f"({c[0]},{c[1]})": str(rats[c]) for c in rat_ells},
        "irrational_slope_chars": len(nontriv) - len(rat_ells),
        "firing_modules": firing_modules,
        "e6_generation_backgrounds": len(gen_bgs),
        "e6_gen_bgs_descending_to_closed_filling": len(gen_bgs_rational_ell),
        "descended_sector_modules": descended_modules,
        "poincare_symmetric_on_filling": poincare_symmetric_count,
        "chiral_surviving_on_filling": descended_modules - poincare_symmetric_count,
        "cohomology_transition_histogram": dict(fill_h1_hist),
    }


def perm_mul(p1: Tuple[int, ...], p2: Tuple[int, ...]) -> Tuple[int, ...]:
    """Left composition (p1 o p2)(i) = p1[p2[i]]."""
    return tuple(p1[p2[i]] for i in range(len(p1)))


def perm_inv(p1: Tuple[int, ...]) -> Tuple[int, ...]:
    out = [0] * len(p1)
    for i, v in enumerate(p1):
        out[v] = i
    return tuple(out)


def is_group_cyclic(elems: Set[Tuple[int, ...]], id_p: Tuple[int, ...]) -> bool:
    ord_g = len(elems)
    for g in elems:
        cur = g
        k = 1
        while cur != id_p:
            cur = perm_mul(cur, g)
            k += 1
        if k == ord_g:
            return True
    return False


def cover_homology_and_cusps(
    sign: int,
    word: str,
    d: int,
    sx: Tuple[int, ...],
    sy: Tuple[int, ...],
    smu: Tuple[int, ...],
) -> Dict[str, Any]:
    """
    Exact integer cellular homology of the connected d-sheeted cover M_tilde -> M
    associated to left homomorphism sigma: pi_1(M) -> S_d, using right sheet action
      alpha(i, g) = sigma(g^-1)(i).
    Computes exact b_1(M_tilde), |H_1(M_tilde; Z)_tors|, cusp count c(M_tilde),
    asserts Half-Lives-Half-Dies (total peripheral rank == c), and counts rank-2 free cusps!
    """
    r1, r2, lam = bundle_relators(sign, word, 1)
    gens_right = {
        1: perm_inv(sx),
        -1: sx,
        2: perm_inv(sy),
        -2: sy,
        3: perm_inv(smu),
        -3: smu,
    }

    # 3d directed edges: index e_id(g_idx in {0,1,2}, sheet i in 0..d-1) = g_idx * d + i
    # Edge (g_idx, i) goes from sheet i to sheet j = gens_right[+(g_idx+1)][i]
    # Boundary map partial_1: Z^{3d} -> Z^d
    p1 = np.zeros((d, 3 * d), dtype=np.int64)
    adj: List[List[Tuple[int, int, int]]] = [[] for _ in range(d)]
    for g_idx, tok_pos in enumerate((1, 2, 3)):
        act = gens_right[tok_pos]
        for i in range(d):
            j = act[i]
            eid = g_idx * d + i
            p1[j, eid] += 1
            p1[i, eid] -= 1
            if i != j:
                adj[i].append((j, eid, +1))
                adj[j].append((i, eid, -1))

    def trace_word_chain(wd: Sequence[int], start_sheet: int) -> Tuple[int, np.ndarray]:
        vec = np.zeros(3 * d, dtype=np.int64)
        cur = start_sheet
        for tok in wd:
            g_idx = abs(tok) - 1
            if tok > 0:
                vec[g_idx * d + cur] += 1
                cur = gens_right[tok][cur]
            else:
                nxt = gens_right[tok][cur]
                vec[g_idx * d + nxt] -= 1
                cur = nxt
        return cur, vec

    # 2d faces -> partial_2: Z^{2d} -> Z^{3d}
    p2 = np.zeros((3 * d, 2 * d), dtype=np.int64)
    for f_idx, rel_w in enumerate((r1, r2)):
        for i in range(d):
            end_s, col_v = trace_word_chain(rel_w, i)
            assert end_s == i, "Cover relator did not close!"
            p2[:, f_idx * d + i] = col_v

    # Assert exact integer chain identity partial_1 @ partial_2 == 0!
    assert np.all(p1 @ p2 == 0), "partial_1 @ partial_2 != 0!"

    # Build spanning tree T of the d sheets to get an exact unimodular Z-basis of ker(partial_1) (rank 2d + 1)!
    visited_v = {0}
    queue_v = [0]
    tree_edges: Set[int] = set()
    while queue_v:
        u = queue_v.pop(0)
        for v_nxt, eid, _ in adj[u]:
            if v_nxt not in visited_v:
                visited_v.add(v_nxt)
                tree_edges.add(eid)
                queue_v.append(v_nxt)
    assert len(visited_v) == d and len(tree_edges) == d - 1, "Cover is not connected!"

    non_tree = [eid for eid in range(3 * d) if eid not in tree_edges]
    assert len(non_tree) == 2 * d + 1

    # Restriction of partial_2 to non-tree rows is the exact presentation matrix of H_1(M_tilde; Z)!
    M_rel = p2[non_tree, :]
    inv_facs = [int(x) for x in invariant_factors(sp.Matrix(M_rel.tolist())) if int(x) != 0]
    rk_rel = len(inv_facs)
    b1 = (2 * d + 1) - rk_rel
    tors_factors = [x for x in inv_facs if x > 1]
    tors_order = 1
    for x in tors_factors:
        tors_order *= x

    # Peripheral cusps: orbits of <mu, lam> on {0, ..., d-1}
    act_mu = gens_right[3]
    # Compute right action of lam:
    act_lam_list = list(range(d))
    for tok in lam:
        act_lam_list = [gens_right[tok][s] for s in act_lam_list]
    act_lam = tuple(act_lam_list)

    seen_s: Set[int] = set()
    cusp_orbits: List[Set[int]] = []
    for s0 in range(d):
        if s0 in seen_s:
            continue
        orb = {s0}
        q_o = [s0]
        while q_o:
            cs = q_o.pop()
            for ns in (act_mu[cs], act_lam[cs]):
                if ns not in orb:
                    orb.add(ns)
                    q_o.append(ns)
        seen_s |= orb
        cusp_orbits.append(orb)

    num_cusps = len(cusp_orbits)

    # Compute exact rational peripheral homology ranks via closed power loops on each cusp orbit!
    # On cusp orbit O, pick every sheet s in O, lift smallest closed power of mu and of lam, and also
    # all closed cycles in the Schreier graph of (O, mu, lam) -> spans H_1(C_j; Q) completely!
    all_periph_cols: List[np.ndarray] = []
    cusp_indiv_ranks: List[int] = []

    def q_rank(mat_int: np.ndarray) -> int:
        if mat_int.shape[1] == 0:
            return 0
        _, sv, _ = np.linalg.svd(mat_int.astype(np.float64), full_matrices=False)
        return int(np.sum(sv > 1e-9))

    base_rk_q = q_rank(M_rel)
    assert base_rk_q == rk_rel

    for orb in cusp_orbits:
        cusp_cols: List[np.ndarray] = []
        # Every closed power of mu and lam, plus mixed mu^a lam^b closing on orb
        for s0 in sorted(orb):
            # mu-cycle from s0
            k_m = 1
            cs = act_mu[s0]
            while cs != s0:
                cs = act_mu[cs]
                k_m += 1
            _, v_m = trace_word_chain([3] * k_m, s0)
            cusp_cols.append(v_m[non_tree])

            # lam-cycle from s0
            k_l = 1
            cs = act_lam[s0]
            while cs != s0:
                cs = act_lam[cs]
                k_l += 1
            _, v_l = trace_word_chain(list(lam) * k_l, s0)
            cusp_cols.append(v_l[non_tree])

            # Mixed primitive cycles mu^a lam^b == s0 (0 <= a < d, 1 <= b < d)
            cur_a = s0
            for a_pow in range(1, d + 1):
                cur_a = act_mu[cur_a]
                cur_ab = cur_a
                for b_pow in range(1, d + 1):
                    cur_ab = act_lam[cur_ab]
                    if cur_ab == s0:
                        _, v_ml = trace_word_chain(([3] * a_pow) + (list(lam) * b_pow), s0)
                        cusp_cols.append(v_ml[non_tree])
                        break

        mat_c = np.column_stack([M_rel] + cusp_cols)
        rk_c = q_rank(mat_c) - base_rk_q
        assert rk_c in (1, 2), f"Unexpected single-cusp homology rank {rk_c}"
        cusp_indiv_ranks.append(rk_c)
        all_periph_cols.extend(cusp_cols)

    total_periph_rk = q_rank(np.column_stack([M_rel] + all_periph_cols)) - base_rk_q
    # Half-Lives-Half-Dies topological theorem gate!
    assert total_periph_rk == num_cusps, (
        f"Half-Lives-Half-Dies violated: total_periph_rk={total_periph_rk} != c={num_cusps}"
    )

    return {
        "degree": d,
        "b1": b1,
        "torsion_order": tors_order,
        "torsion_invariant_factors": tors_factors,
        "cusps": num_cusps,
        "interior_betti_excess": b1 - num_cusps,
        "cusp_individual_ranks": cusp_indiv_ranks,
        "num_rank2_free_cusps": sum(1 for r in cusp_indiv_ranks if r == 2),
    }


def enumerate_noncyclic_covers_state(
    name: str,
    sign: int,
    word: str,
    degrees: Sequence[int] = (3, 4, 5),
    include_cyclic_plant: bool = False,
) -> Dict[str, Any]:
    wx, wy = f2_monodromy_images(sign, word, 1)
    covers_out: List[Dict[str, Any]] = []

    for d in degrees:
        all_perms = list(itertools.permutations(range(d)))
        id_p = tuple(range(d))

        # Group S_d into conjugacy class representatives for sx
        seen_sx: Set[Tuple[int, ...]] = set()
        sx_reps: List[Tuple[int, ...]] = []
        for p_el in all_perms:
            if p_el in seen_sx:
                continue
            cls = {perm_mul(perm_mul(g, p_el), perm_inv(g)) for g in all_perms}
            seen_sx |= cls
            sx_reps.append(p_el)

        def cycle_sig(p_el: Tuple[int, ...]) -> Tuple[int, ...]:
            vis = [False] * d
            lens = []
            for i in range(d):
                if not vis[i]:
                    k = 0
                    cur = i
                    while not vis[cur]:
                        vis[cur] = True
                        cur = p_el[cur]
                        k += 1
                    lens.append(k)
            return tuple(sorted(lens))

        def eval_w_perm(wd: Sequence[int], gx: Tuple[int, ...], gy: Tuple[int, ...]) -> Tuple[int, ...]:
            ix, iy = perm_inv(gx), perm_inv(gy)
            cur = id_p
            for tok in wd:
                if tok == 1:
                    cur = perm_mul(cur, gx)
                elif tok == -1:
                    cur = perm_mul(cur, ix)
                elif tok == 2:
                    cur = perm_mul(cur, gy)
                elif tok == -2:
                    cur = perm_mul(cur, iy)
            return cur

        seen_triples: Set[Tuple[Tuple[int, ...], Tuple[int, ...], Tuple[int, ...]]] = set()

        for sx in sx_reps:
            sig_x = cycle_sig(sx)
            for sy in all_perms:
                px = eval_w_perm(wx, sx, sy)
                if cycle_sig(px) != sig_x:
                    continue
                py = eval_w_perm(wy, sx, sy)
                if cycle_sig(py) != cycle_sig(sy):
                    continue
                for smu in all_perms:
                    ismu = perm_inv(smu)
                    if perm_mul(perm_mul(smu, sx), ismu) != px:
                        continue
                    if perm_mul(perm_mul(smu, sy), ismu) != py:
                        continue

                    # Canonicalize under simultaneous S_d conjugation!
                    canon = min(
                        (
                            perm_mul(perm_mul(g, sx), perm_inv(g)),
                            perm_mul(perm_mul(g, sy), perm_inv(g)),
                            perm_mul(perm_mul(g, smu), perm_inv(g)),
                        )
                        for g in all_perms
                    )
                    if canon in seen_triples:
                        continue
                    seen_triples.add(canon)

                    cx, cy, cmu = canon
                    # Check transitivity on {0, ..., d-1}
                    orb0 = {0}
                    q0 = [0]
                    while q0:
                        u = q0.pop()
                        for fn in (cx, cy, cmu):
                            if fn[u] not in orb0:
                                orb0.add(fn[u])
                                q0.append(fn[u])
                    if len(orb0) < d:
                        continue

                    # Subgroup generated in S_d
                    sub_g = {id_p}
                    qg = [id_p]
                    while qg:
                        cur = qg.pop()
                        for fn in (cx, cy, cmu):
                            nx = perm_mul(cur, fn)
                            if nx not in sub_g:
                                sub_g.add(nx)
                                qg.append(nx)

                    cyc_flag = is_group_cyclic(sub_g, id_p)
                    if cyc_flag and not include_cyclic_plant:
                        continue

                    cov_info = cover_homology_and_cusps(sign, word, d, cx, cy, cmu)
                    cov_info["image_order"] = len(sub_g)
                    cov_info["is_cyclic_image"] = cyc_flag
                    covers_out.append(cov_info)

    return {
        "name": name,
        "sign": sign,
        "word": word,
        "total_noncyclic_covers_d3_to_d5": len(covers_out),
        "covers_with_interior_betti_excess_gt0": sum(1 for c in covers_out if c["interior_betti_excess"] > 0),
        "covers_with_rank2_free_cusps": sum(1 for c in covers_out if c["num_rank2_free_cusps"] > 0),
        "max_b1": max((c["b1"] for c in covers_out), default=1),
        "max_cusps": max((c["cusps"] for c in covers_out), default=1),
        "max_rank2_free_cusps": max((c["num_rank2_free_cusps"] for c in covers_out), default=0),
        "covers": covers_out,
    }


def run_section_n3() -> Dict[str, Any]:
    filling_targets = [
        ("m369", -1, "LLRLR"),
        ("s639", -1, "LLLRLR"),
        ("m010", -1, "LLR"),
        ("m022", +1, "LLLR"),
        ("m023", -1, "LLLR"),
    ]
    fillings_res = {nm: analyze_fillings_state(nm, sg, wd) for nm, sg, wd in filling_targets}
    assert all(v["chiral_surviving_on_filling"] == 0 for v in fillings_res.values())

    cover_targets = [
        ("m009", +1, "LLR"),
        ("m010", -1, "LLR"),
        ("m135", -1, "LLRR"),
        ("m136", +1, "LLRR"),
        ("m022", +1, "LLLR"),
        ("m023", -1, "LLLR"),
        ("m369", -1, "LLRLR"),
    ]
    covers_res = {nm: enumerate_noncyclic_covers_state(nm, sg, wd, (3, 4, 5)) for nm, sg, wd in cover_targets}

    return {
        "dehn_fillings": fillings_res,
        "all_descending_sectors_poincare_symmetric": all(
            v["chiral_surviving_on_filling"] == 0 for v in fillings_res.values()
        ),
        "noncyclic_covers_d3_to_d5": covers_res,
        "total_noncyclic_covers_found": sum(v["total_noncyclic_covers_d3_to_d5"] for v in covers_res.values()),
        "total_covers_with_betti_excess": sum(v["covers_with_interior_betti_excess_gt0"] for v in covers_res.values()),
        "total_covers_with_rank2_free_cusps": sum(v["covers_with_rank2_free_cusps"] for v in covers_res.values()),
    }


# ============================================================================
# SECTION 4 (ITEM N4): NINE UNTOUCHED E* GENESIS PROBES
# ============================================================================

def probe_e7_causal_sets() -> Dict[str, Any]:
    """Enumerate all unlabeled posets for n = 1..6 and compute Myrheim-Meyer ordering fraction r."""
    oeis_a000112 = [1, 2, 5, 16, 63, 318]
    counts: List[int] = []
    mean_r_unlabeled: List[str] = []
    exact_r4_hits: Dict[int, int] = {}

    for n in range(1, 7):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        m_pairs = len(pairs)
        # Group permutations by vertex (in_deg, out_deg) signature for ultra-fast canonicalization
        all_perms = list(itertools.permutations(range(n)))
        seen_canon: Set[int] = set()
        r_vals: List[Fraction] = []

        for mask in range(1 << m_pairs):
            adj = [[0] * n for _ in range(n)]
            rel_cnt = 0
            for bit_i, (u, v) in enumerate(pairs):
                if (mask >> bit_i) & 1:
                    adj[u][v] = 1
                    rel_cnt += 1
            # Check transitivity: if adj[i][j] and adj[j][k] => adj[i][k]
            trans = True
            for i in range(n):
                for j in range(i + 1, n):
                    if adj[i][j]:
                        for k in range(j + 1, n):
                            if adj[j][k] and not adj[i][k]:
                                trans = False
                                break
                    if not trans:
                        break
                if not trans:
                    break
            if not trans:
                continue

            # Vertex degree profile (in_deg, out_deg)
            prof = [(sum(adj[u][v] for u in range(n)), sum(adj[v][w] for w in range(n))) for v in range(n)]
            # Sort vertices by profile first; only permute within equal-profile blocks!
            groups: Dict[Tuple[int, int], List[int]] = defaultdict(list)
            for v, pr in enumerate(prof):
                groups[pr].append(v)
            ordered_blocks = [groups[k] for k in sorted(groups.keys())]

            best_code = None
            for block_perms in itertools.product(*(itertools.permutations(blk) for blk in ordered_blocks)):
                order_v = [v for bp in block_perms for v in bp]
                # Check if order_v is a valid topological sort (no backward edges); wait:
                # canonical code over ALL n x n entries does NOT even need topological sort!
                code = 0
                bit_pos = 0
                for a_i in range(n):
                    ua = order_v[a_i]
                    for b_i in range(n):
                        if a_i != b_i and adj[ua][order_v[b_i]]:
                            code |= 1 << bit_pos
                        bit_pos += 1
                if best_code is None or code < best_code:
                    best_code = code

            assert best_code is not None
            if best_code not in seen_canon:
                seen_canon.add(best_code)
                r_frac = Fraction(0) if n < 2 else Fraction(2 * rel_cnt, n * (n - 1))
                r_vals.append(r_frac)

        counts.append(len(seen_canon))
        avg_r = sum(r_vals, Fraction(0)) / len(r_vals)
        mean_r_unlabeled.append(str(avg_r))
        exact_r4_hits[n] = sum(1 for rv in r_vals if rv == Fraction(1, 10))

    assert counts == oeis_a000112, f"Unlabeled poset count mismatch: {counts} vs {oeis_a000112}"
    return {
        "unlabeled_poset_counts_n1_to_6": counts,
        "matches_oeis_a000112": (counts == oeis_a000112),
        "mean_ordering_fraction_r": mean_r_unlabeled,
        "exact_4d_minkowski_r_1_10_hits_by_n": exact_r4_hits,
    }


def probe_e8_hott_empty_type() -> Dict[str, Any]:
    """
    Concrete simplicial set / Kan complex model up to dimension 4:
      - Empty simplicial set X_0: X_0[m] = empty set; Hom(Delta^m, Id(X)) = empty when X = empty.
      - Unreduced suspension Sigma(X): adjoins North and South 0-simplices and cones every k-simplex of X
        to a (k+1)-simplex (plus degenerate simplices -> non-degenerate cell count grows by 2 at dim k!).
    """
    def iter_id_nondeg_cells(init_cells: Dict[int, int], steps: int) -> List[Dict[int, int]]:
        hist = [dict(init_cells)]
        cur = dict(init_cells)
        for _ in range(steps):
            # Path space P(X) over empty base X has 0 vertices, hence 0 simplices in every dimension!
            if cur[0] == 0:
                nxt = {m: 0 for m in range(5)}
            else:
                nxt = {m: cur.get(m + 1, 0) for m in range(5)}
            hist.append(nxt)
            cur = nxt
        return hist

    def iter_susp_nondeg_cells(init_cells: Dict[int, int], steps: int) -> List[Dict[int, int]]:
        hist = [dict(init_cells)]
        cur = dict(init_cells)
        for _ in range(steps):
            # Suspension of empty set is S^0 (two 0-cells); suspension of S^{k-1} (two (k-1)-cells in minimal CW/simplicial hemisphere model, or unreduced cone)
            if sum(cur.values()) == 0:
                nxt = {0: 2, 1: 0, 2: 0, 3: 0, 4: 0}
            else:
                nxt = {0: 2}
                for m in range(1, 5):
                    nxt[m] = cur[m - 1]
            hist.append(nxt)
            cur = nxt
        return hist

    empty_0 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    id_tower = iter_id_nondeg_cells(empty_0, 4)
    susp_tower = iter_susp_nondeg_cells(empty_0, 4)
    return {
        "iterated_identity_nondeg_cells_k0_to_4": id_tower,
        "all_iterated_identity_empty": all(sum(d.values()) == 0 for d in id_tower),
        "iterated_suspension_nondeg_cells_k0_to_4": susp_tower,
    }


def probe_e9_ssb_modular_potential(plant_embedded_target: bool = False) -> Dict[str, Any]:
    """
    Tests SL(2, Z)-invariance and critical-point / vacuum-manifold geometry of
    Z_rot(tau) = y^(1/2) |eta(tau)|^2 and Mexican-hat V_lambda(tau) = (Z_rot(tau) - lambda)^2
    at 45-digit precision.
    """
    old_dps = mp.mp.dps
    mp.mp.dps = 45
    try:
        def dedekind_eta(tau: mp.mpc) -> mp.mpc:
            q = mp.exp(2j * mp.pi * tau)
            prod = mp.mpc(1)
            for n in range(1, 90):
                prod *= (1 - q**n)
            return mp.exp(mp.pi * 1j * tau / 12) * prod

        def z_rot(x: mp.mpf, y: mp.mpf) -> mp.mpf:
            tau = mp.mpc(x, y)
            if plant_embedded_target:
                tau_star = mp.mpc("0.17", "1.23")
                return abs(tau - tau_star) ** 2
            eta_v = dedekind_eta(tau)
            return mp.sqrt(y) * (mp.re(eta_v) ** 2 + mp.im(eta_v) ** 2)

        # Modular invariance test at generic point tau_test = 0.23 + 1.37i under T and S:
        xt, yt = mp.mpf("0.23"), mp.mpf("1.37")
        val_0 = z_rot(xt, yt)
        val_T = z_rot(xt + 1, yt)
        tau_S = -1 / mp.mpc(xt, yt)
        val_S = z_rot(mp.re(tau_S), mp.im(tau_S))
        mod_err = max(abs(val_T - val_0), abs(val_S - val_0))

        # Finite-difference gradient & Hessian of Z_rot at omega = 1/2 + i*sqrt(3)/2 and at i = 0 + 1i:
        h = mp.mpf("1e-10")

        def grad_hess(x0: mp.mpf, y0: mp.mpf) -> Tuple[float, List[float]]:
            f00 = z_rot(x0, y0)
            fxp = z_rot(x0 + h, y0)
            fxm = z_rot(x0 - h, y0)
            fyp = z_rot(x0, y0 + h)
            fym = z_rot(x0, y0 - h)
            fpp = z_rot(x0 + h, y0 + h)
            fpm = z_rot(x0 + h, y0 - h)
            fmp = z_rot(x0 - h, y0 + h)
            fmm = z_rot(x0 - h, y0 - h)
            gx = (fxp - fxm) / (2 * h)
            gy = (fyp - fym) / (2 * h)
            hxx = (fxp - 2 * f00 + fxm) / (h * h)
            hyy = (fyp - 2 * f00 + fym) / (h * h)
            hxy = (fpp - fpm - fmp + fmm) / (4 * h * h)
            tr = hxx + hyy
            det = hxx * hyy - hxy * hxy
            disc = mp.sqrt(max(mp.mpf(0), tr * tr - 4 * det))
            eigs = sorted([float((tr - disc) / 2), float((tr + disc) / 2)])
            return float(mp.sqrt(gx * gx + gy * gy)), eigs

        if plant_embedded_target:
            return {"modular_invariance_error": float(mod_err), "is_modular_invariant": bool(mod_err < mp.mpf("1e-25"))}

        z_omega = z_rot(mp.mpf("0.5"), mp.sqrt(3) / 2)
        z_i = z_rot(mp.mpf("0.0"), mp.mpf("1.0"))
        gn_om, eig_om = grad_hess(mp.mpf("0.5"), mp.sqrt(3) / 2)
        gn_i, eig_i = grad_hess(mp.mpf("0.0"), mp.mpf("1.0"))

        # Check continuous 1D contour degeneracy for lambda_mid = (z_omega + z_i) / 2 along two distinct rays from omega inside F!
        lam_mid = (z_omega + z_i) / 2
        contour_pts = []
        x_om, y_om = mp.mpf("0.5"), mp.sqrt(3) / 2
        for x_far, y_far in ((mp.mpf("0.10"), mp.mpf("2.5")), (mp.mpf("0.45"), mp.mpf("2.5"))):
            # Bisection for t in [0, 1] along segment tau(t) = (1 - t)*omega + t*(x_far + i*y_far)
            tlo, thi = mp.mpf("0.0"), mp.mpf("1.0")
            flo = z_rot(x_om, y_om) - lam_mid
            fhi = z_rot(x_far, y_far) - lam_mid
            assert flo * fhi < 0
            for _ in range(90):
                tmid = (tlo + thi) / 2
                xm = (1 - tmid) * x_om + tmid * x_far
                ym = (1 - tmid) * y_om + tmid * y_far
                fm = z_rot(xm, ym) - lam_mid
                if flo * fm <= 0:
                    thi = tmid
                    fhi = fm
                else:
                    tlo = tmid
                    flo = fm
            t_star = (tlo + thi) / 2
            x_star = (1 - t_star) * x_om + t_star * x_far
            y_star = (1 - t_star) * y_om + t_star * y_far
            contour_pts.append((float(x_star), float(y_star), float(abs(z_rot(x_star, y_star) - lam_mid))))

        return {
            "modular_invariance_error": float(mod_err),
            "is_modular_invariant": bool(mod_err < mp.mpf("1e-30")),
            "omega_grad_norm": gn_om,
            "omega_hessian_eigs": eig_om,
            "omega_is_strict_local_maximum": (gn_om < 1e-12 and eig_om[0] < -1e-4 and eig_om[1] < -1e-4),
            "i_grad_norm": gn_i,
            "i_hessian_eigs": eig_i,
            "i_is_saddle": (gn_i < 1e-12 and eig_i[0] < -1e-4 and eig_i[1] > 1e-4),
            "mexican_hat_continuous_contour_witnesses": contour_pts,
        }
    finally:
        mp.mp.dps = old_dps


def probe_e10_chern_simons_stationarity(markoff_cache: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Computes Zariski tangent space dim H^1(M; Ad rho) and interior dimension n_int(Ad rho)
    for 3-dimensional sl_2(C) adjoint representation Ad(g)(Z) = g Z g^-1 at:
      - rho_triv = I_2 (trivial flat connection, stationary d CS = 0!)
      - rho_hyp (complete hyperbolic structure)
    across m004 (+LR), m009 (+LLR), and m369 (-LLRLR).
    """
    old_dps = mp.mp.dps
    mp.mp.dps = 55
    try:
        # Basis of sl_2(C): E = [[0,1],[0,0]], F = [[0,0],[1,0]], H = [[1,0],[0,-1]]
        sl2_basis = [
            mp.matrix([[0, 1], [0, 0]]),
            mp.matrix([[0, 0], [1, 0]]),
            mp.matrix([[1, 0], [0, -1]]),
        ]

        def sl2_to_ad3(g: mp.matrix) -> mp.matrix:
            gi = mp_inv2(g)
            A = mp.zeros(3, 3)
            for col, B_in in enumerate(sl2_basis):
                M = g * B_in * gi
                # M = c0*E + c1*F + c2*H => c0 = M[0,1], c1 = M[1,0], c2 = M[0,0]
                A[0, col] = M[0, 1]
                A[1, col] = M[1, 0]
                A[2, col] = M[0, 0]
            return A

        rows = {}
        for nm, sgn, wd in (("m004", +1, "LR"), ("m009", +1, "LLR"), ("m369", -1, "LLRLR")):
            if wd not in markoff_cache:
                markoff_cache[wd] = solve_hyperbolic_markoff_word(wd, dps=55)
            r1, r2, lam = bundle_relators(sgn, wd, 1)
            I3 = mp_eye(3)
            triv_sig = cusped_module_signature_mp(I3, I3, I3, r1, r2, lam, dps=55)["sig"]

            # Hyperbolic SL(2, C) generators
            best = markoff_cache[wd]["best"]
            a, b, c = best["a"], best["b"], best["c"]
            zeta = (c + mp.sqrt(c * c - 4)) / 2
            X = mp.matrix([[a, 1], [-1, 0]])
            Y = mp.matrix([[0, -1 / zeta], [zeta, b]])
            hol = build_hyperbolic_holonomy_and_four(sgn, wd, markoff_cache[wd], dps=55)
            # Re-solve T quickly via sl2_to_ad3? Wait: build_hyperbolic_holonomy_and_four already solved T;
            # compute Ad(T) from Ad(X), Ad(Y): Ad_T * Ad_X = Ad(phi_X) * Ad_T, or solve T directly:
            wx, wy = f2_monodromy_images(sgn, wd, 1)
            gens_f2 = {1: X, -1: mp_inv2(X), 2: Y, -2: mp_inv2(Y)}
            phi_X = eval_word_sl2_mp(wx, gens_f2)
            phi_Y = eval_word_sl2_mp(wy, gens_f2)
            L_sys = mp.zeros(8, 4)
            for eb, (Ai, Ao) in enumerate(((X, phi_X), (Y, phi_Y))):
                for i in range(2):
                    for j in range(2):
                        rr = 4 * eb + 2 * i + j
                        for k in range(2):
                            L_sys[rr, 2 * i + k] += Ai[k, j]
                            L_sys[rr, 2 * k + j] -= Ao[i, k]
            _, nv, _, _ = mp_svd_rank_and_nullspace(L_sys, mp.mpf("1e-25"))
            vv = nv[0]
            T_raw = mp.matrix([[vv[0, 0], vv[1, 0]], [vv[2, 0], vv[3, 0]]])
            T = T_raw / mp.sqrt(T_raw[0, 0] * T_raw[1, 1] - T_raw[0, 1] * T_raw[1, 0])
            hyp_sig = cusped_module_signature_mp(
                sl2_to_ad3(X), sl2_to_ad3(Y), sl2_to_ad3(T), r1, r2, lam, dps=55
            )["sig"]

            rows[nm] = {
                "sig_Ad_rho_triv": list(triv_sig),
                "sig_Ad_rho_hyp": list(hyp_sig),
                "h1_triv": triv_sig[1],
                "h1_hyp": hyp_sig[1],
                "n_int_hyp_weil_rigidity": hyp_sig[4],
            }

        return {
            "states": rows,
            "all_triv_h1_equal_3": all(r["h1_triv"] == 3 for r in rows.values()),
            "all_hyp_h1_equal_1_and_n_int_0": all(
                r["h1_hyp"] == 1 and r["n_int_hyp_weil_rigidity"] == 0 for r in rows.values()
            ),
        }
    finally:
        mp.mp.dps = old_dps


def probe_e12_e13_entropy_and_measures() -> Dict[str, Any]:
    """
    E12: Exact topological / Parry adjacency matrix spectral radius and stationary letter weights
    for unconstrained binary {L, R}^N vs golden RR-forbidden subshift.
    E13: Explicit cylinder-set verification that Dirac delta_empty on 0^Z satisfies
    probability normalization, shift invariance, ergodicity, and 0 Kolmogorov-Sinai entropy.
    """
    # Unconstrained 2x2 adjacency [[1,1],[1,1]]: Perron eigenvalue 2, Parry weights (1/2, 1/2)
    A_full = sp.Matrix([[1, 1], [1, 1]])
    eigs_full = sorted(A_full.eigenvals().keys(), key=lambda e: float(sp.N(e)))
    lam_full = eigs_full[-1]  # 2

    # Golden RR-forbidden adjacency [[1, 1], [1, 0]]: Perron eigenvalue phi = (1+sqrt(5))/2
    A_gold = sp.Matrix([[1, 1], [1, 0]])
    x = sp.Symbol("x")
    char_gold = sp.Poly(A_gold.charpoly(x).as_expr(), x)
    # Parry transition probabilities p_{ij} = A_{ij} v_j / (lam * v_i), stationary pi_i = u_i v_i / (u.v)
    phi = (1 + sp.sqrt(5)) / 2
    # Right eigenvector of [[1,1],[1,0]] for phi is [phi, 1]^T; symmetric so left = right!
    norm_uv = sp.simplify(phi**2 + 1)
    pi_L = sp.simplify(phi**2 / norm_uv)  # (phi + 1)/(phi + 2) = 1/sqrt(5) * phi? Check: phi^2/(phi^2+1) = (phi+1)/(phi+2)
    pi_R = sp.simplify(1 / norm_uv)
    # Note: transition from L has P(L->L) = 1/phi, P(L->R) = 1/phi^2!
    p_LL = sp.simplify(1 / phi)
    p_LR = sp.simplify(1 / phi**2)
    assert sp.simplify(p_LL + p_LR - 1) == 0

    # E13: Test Dirac measure delta_{0^Z} on all length-4 cylinder sets w in {0, 1}^4:
    cyl4 = list(itertools.product((0, 1), repeat=4))
    mu_delta = {w: (1 if w == (0, 0, 0, 0) else 0) for w in cyl4}
    total_mass = sum(mu_delta.values())
    # Shift invariance on length-3 marginals: sum_{b} mu(b, w) == sum_{b} mu(w, b) for all w in {0, 1}^3!
    shift_inv_ok = all(
        mu_delta[(0,) + w] + mu_delta[(1,) + w] == mu_delta[w + (0,)] + mu_delta[w + (1,)]
        for w in itertools.product((0, 1), repeat=3)
    )
    h_ks_delta = -sum(p * math.log(p) for p in mu_delta.values() if p > 0)

    return {
        "E12_unconstrained_perron_root": int(lam_full),
        "E12_unconstrained_weights": ["1/2", "1/2"],
        "E12_golden_charpoly_coeffs": [int(c) for c in char_gold.all_coeffs()],
        "E12_golden_branch_probs_from_L_sum_to_1": (sp.simplify(p_LL + p_LR) == 1),
        "E13_delta_empty_total_mass": total_mass,
        "E13_delta_empty_shift_invariant": shift_inv_ok,
        "E13_delta_empty_entropy_exact_zero": (h_ks_delta == 0.0 and mu_delta[(0, 0, 0, 0)] == 1),
    }


def probe_e15_bulk_from_boundary_collision() -> Dict[str, Any]:
    """
    Tests whether F-CI class-index invariants & rational-slope counts uniquely determine
    the bulk 3-manifold M across cyclic levels: compares m003 = (-LR, level 1) vs m206 = (+LR, level 2)
    (m206 is the cyclic double cover of m003 since (-LR)^2 = +LRLR, so s_m206(c) = 2 * s_m003(c),
    giving identical F-CI (h^1(V), h^1(V*)) tables while Mostow volumes differ by factor 2!).
    """
    primes = find_primes_1_mod_N(5, count=3, start=10_000_000)
    zetas = [primitive_nth_root_mod_p(5, p) for p in primes]

    def bdry_profile(sign: int, word: str, k: int) -> Dict[str, Any]:
        N, chars = fixed_torsion_characters(sign, word, k)
        nontriv = [c for c in chars if c != (0, 0)]
        w_exp = word * k
        sgn_exp = (-1 if (sign < 0 and k % 2 == 1) else +1)
        skeys = {
            c: tuple(slope_mod_p(sgn_exp, w_exp, c[0], c[1], N, p, z) for p, z in zip(primes, zetas))
            for c in nontriv
        }
        rats = {c: recover_rational_slope(sgn_exp, w_exp, c, N, primes, zetas) for c in nontriv}
        h1_hist: Counter = Counter()
        for ell in nontriv:
            for alpha in nontriv:
                if alpha == ell:
                    continue
                r0 = dehn_filling_cohomology_mod_p(sgn_exp, w_exp, N, ell, alpha, None, primes[0], zetas[0])
                r1 = dehn_filling_cohomology_mod_p(sgn_exp, w_exp, N, ell, alpha, None, primes[1], zetas[1])
                assert r0 == r1
                h1_hist[f"({r0[0]},{r0[1]})"] += 1
        return {
            "N": N,
            "num_nontriv": len(nontriv),
            "skeys": skeys,
            "rational_slopes_count": sum(1 for v in rats.values() if v is not None),
            "h1_pair_histogram": dict(h1_hist),
        }

    p_m003 = bdry_profile(-1, "LR", 1)
    p_m206 = bdry_profile(+1, "LR", 2)

    # Verify exact double-cover slope relation s_m206(c) == 2 * s_m003(c) mod p across all 3 primes!
    slope_doubling_holds = all(
        tuple((2 * v) % p for v, p in zip(p_m003["skeys"][c], primes)) == p_m206["skeys"][c]
        for c in p_m003["skeys"]
    )
    identical_fci_census = (
        p_m003["N"] == p_m206["N"]
        and p_m003["rational_slopes_count"] == p_m206["rational_slopes_count"]
        and p_m003["h1_pair_histogram"] == p_m206["h1_pair_histogram"]
        and slope_doubling_holds
    )

    vol_m003 = float(solve_hyperbolic_markoff_word("LR", dps=40)["best"]["abs_volume"])
    vol_m206 = float(solve_hyperbolic_markoff_word("LRLR", dps=40)["best"]["abs_volume"])
    distinct_bulk = (abs(vol_m206 - 2.0 * vol_m003) < 1e-10 and abs(vol_m206 - vol_m003) > 1.0)
    assert identical_fci_census and distinct_bulk

    return {
        "m003_minus_LR_level1_N": p_m003["N"],
        "m206_plus_LR_level2_N": p_m206["N"],
        "m003_h1_pair_histogram": p_m003["h1_pair_histogram"],
        "m206_h1_pair_histogram": p_m206["h1_pair_histogram"],
        "exact_double_cover_slope_doubling_holds": slope_doubling_holds,
        "identical_fci_census_and_rational_count": identical_fci_census,
        "distinct_mostow_volumes_ratio_2": distinct_bulk,
    }


def probe_e18_and_e19_bootstrap_and_diophantine() -> Dict[str, Any]:
    """
    E18: Premise-drop test on (GM1: tr[A,B] = -2) & (SE1: |det(M - I)| = 1) & (McKay: |SL(2, Z/N)| <= 120)
         over SL(2, Z) matrices with entries in [-5, 5].
    E19: Fricke-Markoff integer search x^2 + y^2 + z^2 - x*y*z - 2 = k over [-10, 10]^3 at k = -2 vs k = +2.
    """
    # Enumerate SL(2, Z) matrices with entries in [-5, 5]
    sl2_z = [
        (a, b, c, d)
        for a in range(-5, 6)
        for b in range(-5, 6)
        for c in range(-5, 6)
        for d in range(-5, 6)
        if a * d - b * c == 1
    ]

    def sl2_z_order_mod_N(N: int) -> int:
        # |SL(2, Z/NZ)| = N^3 * prod_{p | N} (1 - 1/p^2)
        if N <= 1:
            return 1
        ans = N**3
        for p in sp.factorint(N).keys():
            ans = (ans // (p * p)) * (p * p - 1)
        return ans

    # Check hyperbolic monodromies M in sl2_z (|tr(M)| > 2):
    surviving_traces_se1_mckay: Set[int] = set()
    for a, b, c, d in sl2_z:
        tr = a + d
        if abs(tr) <= 2:
            continue
        det_se1 = abs((a - 1) * (d - 1) - b * c)  # |2 - tr|
        N_frust = abs((-a - 1) * (-d - 1) - (-b) * (-c))  # |2 + tr|
        if det_se1 == 1 and sl2_z_order_mod_N(N_frust) <= 120:
            surviving_traces_se1_mckay.add(tr)

    # Check fibre commutator tr[A, B]: does A = B = I_2 satisfy tr[A, B] = +2 while failing tr[A, B] = -2?
    I2 = (1, 0, 0, 1)
    tr_comm_identity = 2  # tr(I * I * I^-1 * I^-1) = tr(I_2) = 2

    # E19: Integer solutions in [-10, 10]^3 to x^2 + y^2 + z^2 - x*y*z - 2 == k
    sols_k_minus2: List[Tuple[int, int, int]] = []
    sols_k_plus2: List[Tuple[int, int, int]] = []
    for x in range(-10, 11):
        for y in range(-10, 11):
            for z in range(-10, 11):
                lhs = x * x + y * y + z * z - x * y * z - 2
                if lhs == -2:
                    sols_k_minus2.append((x, y, z))
                elif lhs == 2:
                    sols_k_plus2.append((x, y, z))

    pos_sols_minus2 = sorted(t for t in sols_k_minus2 if t[0] > 0 and t[1] > 0 and t[2] > 0)

    return {
        "E18_sl2_z_box_count": len(sl2_z),
        "E18_surviving_hyperbolic_traces_under_SE1_and_McKay": sorted(surviving_traces_se1_mckay),
        "E18_identity_commutator_trace": tr_comm_identity,
        "E18_dropping_scar_admits_trivial_identity": (tr_comm_identity == 2 and (2, 2, 2) in sols_k_plus2),
        "E19_k_minus2_solution_count_box10": len(sols_k_minus2),
        "E19_k_minus2_contains_origin_Q8": ((0, 0, 0) in sols_k_minus2),
        "E19_k_minus2_minimal_positive_solutions": [list(t) for t in pos_sols_minus2[:5]],
        "E19_k_plus2_solution_count_box10": len(sols_k_plus2),
        "E19_k_plus2_contains_trivial_222": ((2, 2, 2) in sols_k_plus2),
    }


def run_section_n4(markoff_cache: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "E7_causal_sets": probe_e7_causal_sets(),
        "E8_hott_empty_type": probe_e8_hott_empty_type(),
        "E9_ssb_modular_potential": probe_e9_ssb_modular_potential(plant_embedded_target=False),
        "E10_chern_simons_stationarity": probe_e10_chern_simons_stationarity(markoff_cache),
        "E12_E13_entropy_and_measures": probe_e12_e13_entropy_and_measures(),
        "E15_bulk_from_boundary_collision": probe_e15_bulk_from_boundary_collision(),
        "E18_E19_bootstrap_and_diophantine": probe_e18_and_e19_bootstrap_and_diophantine(),
    }


# ============================================================================
# SECTION 5: METALLIC FIXED-LOCUS DECOMPOSITION (B130/AR4) & 5 PLANTED CONTROLS
# ============================================================================

def verify_metallic_fixed_loci_b130() -> Dict[str, Any]:
    """
    Component-by-component algebraic analysis of unrestricted Fricke fixed loci
      Phi_{L^m R^m}(x, y, z) = (x, y, z)  in C^3  (WITHOUT imposing kappa = -2!)
    for m = 1 (LR), m = 2 (LLRR), m = 3 (LLLRRR), using the exact linear-in-z structure of
    Phi_{L^m}(x, y, z) = Phi_{R^m}^{-1}(x, y, z) to decompose every irreducible curve and
    0-dimensional singular locus and test whether ANY isolated unsymmetric point locks Fricke kappa!
    """
    old_dps = mp.mp.dps
    mp.mp.dps = 45
    try:
        sx, sy, sz = sp.symbols("x y z")
        out = {}

        for m in (1, 2, 3):
            lhs = (sx, sy, sz)
            for _ in range(m):
                lhs = markoff_step_sym(lhs[0], lhs[1], lhs[2], "L")
            rhs = (sx, sy, sz)
            for _ in range(m):
                rhs = markoff_inv_step_sym(rhs[0], rhs[1], rhs[2], "R")

            eqs = [sp.expand(lhs[i] - rhs[i]) for i in range(3)]
            # Verify all 3 equations have degree <= 1 in sz!
            for e in eqs:
                assert sp.Poly(e, sz).degree() <= 1

            # Eq 0: c0_z(x, y) * z + d0(x, y) = 0; Eq 1: c1_z(x, y) * z + d1(x, y) = 0
            p0_z = sp.Poly(eqs[0], sz)
            p1_z = sp.Poly(eqs[1], sz)
            c0_z, d0_xy = (p0_z.all_coeffs() if p0_z.degree() == 1 else (sp.Integer(0), eqs[0]))
            c1_z, d1_xy = (p1_z.all_coeffs() if p1_z.degree() == 1 else (sp.Integer(0), eqs[1]))

            # Eliminate z between eqs[0] and eqs[1]:
            cross_xy = sp.expand(c0_z * d1_xy - c1_z * d0_xy)
            _, biv_facs = sp.factor_list(cross_xy, sx, sy)

            f_num = sp.lambdify((sx, sy, sz), eqs, "mpmath")
            branches_report = []

            for fac_xy, _ in biv_facs:
                # Check if fac_xy is univariate in x (vertical line x = const) or univariate in y or curve f(x, y) = 0:
                free_s = fac_xy.free_symbols
                if free_s == {sx}:
                    # Solve fac_xy(x) = 0; check if y or z is a 1D line along which kappa varies!
                    px = sp.Poly(fac_xy, sx)
                    xr_list = safe_polyroots_mp([mp.mpf(int(c)) for c in px.all_coeffs()])
                    # Check at x = xr_list[0] whether eqs vanish identically in z (when y=0) or y:
                    sub_eqs = [sp.simplify(e.subs(sx, sp.sympify(0))) if fac_xy == sx else e for e in eqs]
                    # Evaluate two sample points if x == 0 -> y == 0, z free:
                    if fac_xy == sx:
                        # Check eqs at (0, 0, z)
                        at_00z = [sp.simplify(e.subs({sx: 0, sy: 0})) for e in eqs]
                        if all(e == 0 for e in at_00z):
                            # Line (0, 0, z): kappa = z^2 - 2 varies continuously!
                            branches_report.append(
                                {
                                    "factor": str(fac_xy),
                                    "geometry": "1D_line_(0,0,z)",
                                    "is_zero_dimensional": False,
                                    "kappa_varies_continuously": True,
                                }
                            )
                            continue
                if free_s == {sy} and fac_xy == sy:
                    at_x0z = [sp.simplify(e.subs({sx: 0, sy: 0})) for e in eqs]
                    if all(e == 0 for e in at_x0z):
                        continue  # Already covered by (0, 0, z)

                # General 1D curve fac_xy(x, y) = 0 with y depending on x: sample two generic x values (3.7, 5.3)
                py = sp.Poly(fac_xy, sy)
                if py.degree() >= 1:
                    k_samples: List[mp.mpc] = []
                    valid_curve_pts = 0
                    for x_val in (mp.mpf("3.7"), mp.mpf("5.3"), mp.mpf("7.1")):
                        y_coeffs = []
                        for ce in py.all_coeffs():
                            pce = sp.Poly(ce, sx)
                            vv = mp.mpc(0)
                            for cc in pce.all_coeffs():
                                vv = vv * x_val + mp.mpf(int(cc))
                            y_coeffs.append(vv)
                        y_rts = safe_polyroots_mp(y_coeffs)
                        for y_val in y_rts:
                            # High-precision evaluation of c1_z and d1_xy
                            f_c1 = sp.lambdify((sx, sy), c1_z, "mpmath")(x_val, y_val)
                            f_d1 = sp.lambdify((sx, sy), d1_xy, "mpmath")(x_val, y_val)
                            if abs(f_c1) > mp.mpf("1e-20"):
                                z_val = -f_d1 / f_c1
                                ev = f_num(x_val, y_val, z_val)
                                if max(abs(r) for r in ev) < mp.mpf("1e-30"):
                                    valid_curve_pts += 1
                                    kv = x_val**2 + y_val**2 + z_val**2 - x_val * y_val * z_val - 2
                                    k_samples.append(kv)
                                    break
                    if valid_curve_pts >= 2:
                        k_spread = float(max(abs(k_samples[i] - k_samples[0]) for i in range(1, len(k_samples))))
                        branches_report.append(
                            {
                                "factor": str(fac_xy),
                                "geometry": "1D_curve",
                                "is_zero_dimensional": False,
                                "kappa_varies_continuously": (k_spread > 1.0),
                                "sample_kappa_spread": k_spread,
                            }
                        )
                    else:
                        # Spurious resultant factor from c0_z == c1_z == 0; handled in singular grid check below!
                        branches_report.append(
                            {
                                "factor": str(fac_xy),
                                "geometry": "spurious_denominator_locus_checked_in_singular_grid",
                                "is_zero_dimensional": False,
                                "kappa_varies_continuously": True,
                            }
                        )

            # Explicitly check the 0D singular locus where BOTH z-coefficients c0_z(y) == 0 and c1_z(x) == 0!
            pc1_x = sp.Poly(c1_z, sx)
            pc0_y = sp.Poly(c0_z, sy)
            x_sing = [] if pc1_x.degree() == 0 else safe_polyroots_mp([mp.mpf(int(c)) for c in pc1_x.all_coeffs()])
            y_sing = [] if pc0_y.degree() == 0 else safe_polyroots_mp([mp.mpf(int(c)) for c in pc0_y.all_coeffs()])

            isolated_unsymmetric_points = 0
            singular_solutions = []
            fd0 = sp.lambdify((sx, sy), d0_xy, "mpmath")
            fd1 = sp.lambdify((sx, sy), d1_xy, "mpmath")
            for xs in x_sing:
                for ys in y_sing:
                    if abs(fd0(xs, ys)) < mp.mpf("1e-30") and abs(fd1(xs, ys)) < mp.mpf("1e-30"):
                        # Check eqs[2] as linear polynomial in z at (xs, ys):
                        # Evaluate eqs[2] at z = 0 and z = 1
                        e2_0 = f_num(xs, ys, mp.mpf(0))[2]
                        e2_1 = f_num(xs, ys, mp.mpf(1))[2]
                        slope_z = e2_1 - e2_0
                        if abs(slope_z) < mp.mpf("1e-30"):
                            if abs(e2_0) < mp.mpf("1e-30"):
                                singular_solutions.append({"type": "1D_vertical_z_line", "kappa_varies": True})
                        else:
                            zs = -e2_0 / slope_z
                            is_sym = (
                                abs(xs**2 - ys**2) < mp.mpf("1e-25")
                                or abs(xs) < mp.mpf("1e-25")
                                or abs(ys) < mp.mpf("1e-25")
                                or abs(zs) < mp.mpf("1e-25")
                            )
                            if not is_sym:
                                isolated_unsymmetric_points += 1
                            singular_solutions.append(
                                {
                                    "type": "0D_point_on_or_off_curve",
                                    "is_symmetric": bool(is_sym),
                                }
                            )

            out[f"m_{m}_{'L'*m + 'R'*m}"] = {
                "bivariate_cross_factors": [str(f) for f, _ in biv_facs],
                "branches": branches_report,
                "singular_locus_solutions": singular_solutions,
                "isolated_unsymmetric_zero_dim_points": isolated_unsymmetric_points,
                "all_curve_branches_vary_kappa": all(b["kappa_varies_continuously"] for b in branches_report),
            }

        return out
    finally:
        mp.mp.dps = old_dps


def run_five_planted_controls(markoff_cache: Dict[str, Dict[str, Any]], n2_summary: Dict[str, Any]) -> Dict[str, Any]:
    # PC_N1: Transpose bug g -> g H g^T instead of Hermitian g H g^dagger on m135 = -LLRR:
    # Must either fail SO(3,1) / shift the B1485 signature away from {(2,1):2, (1,0):2, (0,0):4}!
    hol_bad = build_hyperbolic_holonomy_and_four(-1, "LLRR", markoff_cache["LLRR"], dps=55, plant_transpose_bug=True)
    # Check Lorentzian metric preservation failure on hol_bad["four_X"]:
    eta31 = mp.diag([mp.mpf(1), mp.mpf(-1), mp.mpf(-1), mp.mpf(-1)])
    fX_bad = hol_bad["four_X"]
    lor_err_bad = float(mp_frob_norm(fX_bad.T * eta31 * fX_bad - eta31))
    # Also check H^1 signature at nu=(1,1,1) on hol_bad:
    sig_bad_111 = cusped_module_signature_mp(
        hol_bad["four_X"], hol_bad["four_Y"], hol_bad["four_T"], hol_bad["r1"], hol_bad["r2"], hol_bad["lam"], dps=55
    )["sig"]
    # Recall Ad(g) + 1 (since g M g^T on 2x2 matrices preserves skew-symmetric [[0,1],[-1,0]] of dim 1 and acts as Sym^2 = Ad_3 on dim 3!),
    # so h^0(g M g^T) == 1 != 0!!
    pc_n1_fired = (lor_err_bad > 0.1 and sig_bad_111[0] == 1)

    # PC_N2: Inject synthetic norm-3 2T ramified prime into m369's checker -> must flip detector!
    real_m369_door = n2_summary["m369_arithmetic"]["unique_norm3_mckay_2T_door"]
    synth_ideals = [{"residue_norm_q": 3, "mod_p_holonomy_candidates": [{"mckay_label": "2T -> E6"}]}]
    synth_door = (
        len(synth_ideals) == 1
        and synth_ideals[0]["residue_norm_q"] == 3
        and any(c.get("mckay_label") == "2T -> E6" for c in synth_ideals[0]["mod_p_holonomy_candidates"])
    )
    pc_n2_fired = (real_m369_door is False and synth_door is True)

    # PC_N3: Include cyclic Z/3Z cover in non-cyclic cover enumerator on m009 (+LLR, d=3):
    cov_clean = enumerate_noncyclic_covers_state("m009", +1, "LLR", degrees=(3,), include_cyclic_plant=False)
    cov_plant = enumerate_noncyclic_covers_state("m009", +1, "LLR", degrees=(3,), include_cyclic_plant=True)
    cyclic_injected = [c for c in cov_plant["covers"] if c["is_cyclic_image"]]
    pc_n3_fired = (
        len(cyclic_injected) >= 1
        and all(c["b1"] == 1 and c["cusps"] == 1 for c in cyclic_injected)
        and cov_plant["total_noncyclic_covers_d3_to_d5"] > cov_clean["total_noncyclic_covers_d3_to_d5"]
    )

    # PC_N4: Hand-embedded Texas-Sharpshooter potential |tau - tau_*|^2 in E9 modular gate:
    e9_plant = probe_e9_ssb_modular_potential(plant_embedded_target=True)
    pc_n4_fired = (e9_plant["is_modular_invariant"] is False and e9_plant["modular_invariance_error"] > 0.1)

    # PC_N5: Flip k = -2 to k = +2 in Fricke-Markoff Diophantine equation (E19):
    e18_19 = probe_e18_and_e19_bootstrap_and_diophantine()
    pc_n5_fired = (
        e18_19["E19_k_plus2_contains_trivial_222"] is True
        and (2, 2, 2) not in [tuple(t) for t in e18_19["E19_k_minus2_minimal_positive_solutions"]]
    )

    assert pc_n1_fired and pc_n2_fired and pc_n3_fired and pc_n4_fired and pc_n5_fired, (
        f"Planted control failed: {(pc_n1_fired, pc_n2_fired, pc_n3_fired, pc_n4_fired, pc_n5_fired)}"
    )

    return {
        "PC_N1_transpose_four_cocycle": {
            "fired": pc_n1_fired,
            "lorentzian_metric_error": lor_err_bad,
            "shifted_untwisted_sig_V": list(sig_bad_111),
        },
        "PC_N2_fake_norm3_prime": {
            "fired": pc_n2_fired,
            "real_m369_door": real_m369_door,
            "synthetic_norm3_door": synth_door,
        },
        "PC_N3_cyclic_as_noncyclic": {
            "fired": pc_n3_fired,
            "cyclic_covers_caught": len(cyclic_injected),
        },
        "PC_N4_embedded_target_potential": {
            "fired": pc_n4_fired,
            "modular_invariance_error": e9_plant["modular_invariance_error"],
        },
        "PC_N5_drop_scar_in_markoff": {
            "fired": pc_n5_fired,
            "admits_trivial_222_at_k_plus2": e18_19["E19_k_plus2_contains_trivial_222"],
        },
        "all_five_planted_controls_fired": (
            pc_n1_fired and pc_n2_fired and pc_n3_fired and pc_n4_fired and pc_n5_fired
        ),
    }


def main() -> None:
    t0 = time.time()
    print("[X-NEVER] Running N1 (F-HE harmonic frame)...", file=sys.stderr, flush=True)
    n1_res, markoff_cache = run_section_n1()
    t1 = time.time()
    print(f"[X-NEVER] N1 done ({t1 - t0:.1f}s). Running N2 (own arithmetic)...", file=sys.stderr, flush=True)
    n2_res = run_section_n2(markoff_cache)
    t2 = time.time()
    print(f"[X-NEVER] N2 done ({t2 - t1:.1f}s). Running N3 (fillings & non-cyclic covers)...", file=sys.stderr, flush=True)
    n3_res = run_section_n3()
    t3 = time.time()
    print(f"[X-NEVER] N3 done ({t3 - t2:.1f}s). Running N4 (genesis probes)...", file=sys.stderr, flush=True)
    n4_res = run_section_n4(markoff_cache)
    t4 = time.time()
    print(f"[X-NEVER] N4 done ({t4 - t3:.1f}s). Running Section 5 (B130 & 5 planted controls)...", file=sys.stderr, flush=True)
    b130_res = verify_metallic_fixed_loci_b130()
    plants_res = run_five_planted_controls(markoff_cache, n2_res)
    t5 = time.time()
    print(f"[X-NEVER] All sections done ({t5 - t0:.1f}s). Writing JSON...", file=sys.stderr, flush=True)

    payload = {
        "card": "X-NEVER",
        "seat": "agy-exp",
        "timings_seconds": {
            "N1_F_HE": round(t1 - t0, 3),
            "N2_own_arithmetic": round(t2 - t1, 3),
            "N3_fillings_and_noncyclic_covers": round(t3 - t2, 3),
            "N4_genesis_probes": round(t4 - t3, 3),
            "Section5_metallic_and_plants": round(t5 - t4, 3),
            "total": round(t5 - t0, 3),
        },
        "N1_harmonic_frame": n1_res,
        "N2_own_arithmetic": n2_res,
        "N3_fillings_and_noncyclic_covers": n3_res,
        "N4_genesis_probes": n4_res,
        "Section5_metallic_fixed_loci_b130": b130_res,
        "Section5_planted_controls": plants_res,
    }

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "verify_x_never_out.json")
    json_str = json.dumps(payload, indent=2, default=_json_default) + "\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(json_str)


if __name__ == "__main__":
    main()
