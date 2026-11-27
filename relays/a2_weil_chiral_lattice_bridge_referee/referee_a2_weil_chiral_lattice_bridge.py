"""
Blind Cold-Room Zero-Trust Referee for Card A2-WEIL-CHIRAL-LATTICE-BRIDGE
Seat code: fam3-v1-high-03 | Strictly 0 of 19 (pure mathematics, zero empirical data)

Disjoint verification methods across all four modules:
  W1: Exact SymPy cyclotomic quotient rings Q[x]/(Phi_N(x)) for N in {3,5,7,9,15}
      paired with 50-digit mpmath Fourier-dual (momentum) Weil basis sweep over
      all 220 (N, r) pairs and all 17 odd N in 3..35, plus exact CRT N=15.
  W2: Leg(5) via 12-ray involution projection on Rays(5) = (F_5^2 minus {0})/{+-1};
      K_5 via explicit PSL(2, F_5) conjugation; intertwiner U via simultaneous
      (W_6, W_ch, C_3) diagonalization; Phi^Siegel via jtheta(1) + Euler-pentagonal
      Dedekind eta; Phi^wp via -d^2/dz^2 ln jtheta(1, pi*z, q); O_27^(3,3,3) via
      <C_tr, Sig_tr>-orbit and Q_6 via direct partition refinement; G_3 order-216
      homomorphism and character-defect exhaustion; O_27 - Q_6 chiral moments
      m=0..4 via G_3 group-algebra DP; Q_6 x Weil_N moments m=0..6 via direct
      matrix powers and non-Hermitian eigen-decomposition.
  W3: Branch-free completed-square 1D Jacobi-theta realization of Theta^even (wt 1)
      and Theta^odd (wt 2) for L_N (N in {3,7,11,15,19}) and L'_15; SL(2, Z)
      equivariance; omega_+ chiral-sector locking; zero-parameter 2D modulus
      stabilization via coarse fundamental-domain scan, golden-section search,
      secant root-finding on 4-point central dV/dy, and 5-point Richardson 2D
      Hessians.
  W4: Exact Q[[q^{1/15}]] identities through t^60 via SymPy Poly; L'_15 swap
      isometry j -> -4j == (-1,+1) = P_flip^(3); CRT 3x5 singular values and
      left-singular mixing |V_{3x3}| via non-squaring 8x8 Hermitian Jordan-Wielandt
      block [[0, M], [M^H, 0]] at tau0, tau0+1, -1/tau0, and dynamically located
      L_15 tau_* = i y_*; 10-trial independent LCG128-seeded Householder-reflection
      Haar U(3) x U(5) basis-scrambling invariance (Guardrail 3).
  Controls: Five independent Referee Planted Fault Controls (RPF1..RPF5),
      in-script AST float-literal & T7b Part 1 static guard, and JSON float guard.
"""

from __future__ import annotations

import ast
from collections import deque
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
from typing import Any, Dict, List, Sequence, Tuple

import mpmath as mp
import sympy as sp

# ---------------------------------------------------------------------------
# Global 50-digit precision & exact constants (zero Python float literals)
# ---------------------------------------------------------------------------
mp.mp.dps = 50

ZERO = mp.mpf(0)
ONE = mp.mpf(1)
TWO = mp.mpf(2)
THREE = mp.mpf(3)
FOUR = mp.mpf(4)
FIVE = mp.mpf(5)
SIX = mp.mpf(6)

TOL_STRICT = mp.mpf("1e-35")
TOL_GATE_30 = mp.mpf("1e-30")
TOL_GATE_28 = mp.mpf("1e-28")
TOL_GATE_25 = mp.mpf("1e-25")
TOL_GRAD = mp.mpf("1e-28")

OUT_DIR = Path(__file__).resolve().parent
OUT_JSON = OUT_DIR / "referee_a2_weil_chiral_lattice_bridge_out.json"


# ---------------------------------------------------------------------------
# Hygiene, Formatting & Number-Theoretic Helpers
# ---------------------------------------------------------------------------
def fstr(x: Any, digits: int = 38) -> str:
    if isinstance(x, mp.mpc):
        return f"({mp.nstr(mp.re(x), digits)})+({mp.nstr(mp.im(x), digits)})j"
    return mp.nstr(mp.mpf(x), digits)


def sci(x: Any, digits: int = 12) -> str:
    return mp.nstr(mp.mpf(x), digits)


def jacobi_symbol(a: int, n: int) -> int:
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    a %= n
    res = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def odd_prime_factors(n: int) -> List[int]:
    factors: List[int] = []
    d = 3
    m = n
    while d * d <= m:
        if m % d == 0:
            factors.append(d)
            while m % d == 0:
                m //= d
        d += 2
    if m > 1:
        factors.append(m)
    return factors


def has_sqrt_minus_one_mod(n: int) -> bool:
    return all(p % 4 == 1 for p in odd_prime_factors(n))


def find_sqrt_minus_one_mod(n: int) -> int:
    for a in range(1, n):
        if (a * a + 1) % n == 0:
            return a
    raise ValueError(f"No square root of -1 mod {n}")


def mat_frob(M: mp.matrix) -> mp.mpf:
    s = ZERO
    for i in range(M.rows):
        for j in range(M.cols):
            v = M[i, j]
            s += mp.re(v) * mp.re(v) + mp.im(v) * mp.im(v)
    return mp.sqrt(s)


def mat_trace(M: mp.matrix) -> mp.mpc:
    s = mp.mpc(0)
    for i in range(M.rows):
        s += M[i, i]
    return s


def mat_conj_entries(M: mp.matrix) -> mp.matrix:
    R = mp.matrix(M.rows, M.cols)
    for i in range(M.rows):
        for j in range(M.cols):
            R[i, j] = mp.conj(M[i, j])
    return R


def kron_mp(A: mp.matrix, B: mp.matrix) -> mp.matrix:
    ra, ca = A.rows, A.cols
    rb, cb = B.rows, B.cols
    K = mp.matrix(ra * rb, ca * cb)
    for ia in range(ra):
        for ja in range(ca):
            a = A[ia, ja]
            if a == 0:
                continue
            for ib in range(rb):
                for jb in range(cb):
                    K[ia * rb + ib, ja * cb + jb] = a * B[ib, jb]
    return K


def perm_matrix_mp(perm: Sequence[int]) -> mp.matrix:
    n = len(perm)
    P = mp.zeros(n, n)
    for j, i in enumerate(perm):
        P[i, j] = ONE
    return P


def orthonormal_basis_from_projector(P: mp.matrix, tol: mp.mpf = mp.mpf("1e-20")) -> mp.matrix:
    """Modified Gram-Schmidt orthonormal basis for column space of Hermitian projector P."""
    n = P.rows
    cols: List[mp.matrix] = []
    for j in range(n):
        v = mp.matrix(n, 1)
        for i in range(n):
            v[i, 0] = P[i, j]
        # Two passes of Gram-Schmidt for full 50-digit orthogonality
        for _ in range(2):
            for u in cols:
                ip = mp.mpc(0)
                for i in range(n):
                    ip += mp.conj(u[i, 0]) * v[i, 0]
                for i in range(n):
                    v[i, 0] -= ip * u[i, 0]
        nv = mat_frob(v)
        if nv > tol:
            for i in range(n):
                v[i, 0] /= nv
            cols.append(v)
    k = len(cols)
    B = mp.matrix(n, k)
    for j, u in enumerate(cols):
        for i in range(n):
            B[i, j] = u[i, 0]
    return B


def spectrum_real_hermitian(H: mp.matrix) -> List[mp.mpf]:
    if H.rows == 0:
        return []
    Hs = (H + H.H) / TWO
    eigs, _ = mp.eigh(Hs)
    return sorted([mp.re(eigs[i]) for i in range(len(eigs))])


def max_spec_diff(s1: Sequence[mp.mpf], s2: Sequence[mp.mpf]) -> mp.mpf:
    if len(s1) != len(s2):
        return mp.mpf("1e9")
    if not s1:
        return ZERO
    return max(abs(a - b) for a, b in zip(s1, s2))


# ---------------------------------------------------------------------------
# Static AST & T7b Part 1 Guard + JSON Float Guard
# ---------------------------------------------------------------------------
REFUSED_MODULES = {
    "ctypes", "_ctypes", "multiprocessing", "_multiprocessing", "importlib",
    "subprocess", "socket", "ssl", "http", "urllib", "urllib3", "requests",
    "ftplib", "smtplib", "poplib", "imaplib", "telnetlib", "xmlrpc",
    "asyncio", "aiohttp", "websockets", "paramiko", "pty", "popen2",
}
REFUSED_DOTTED = {"logging.handlers"}
REFUSED_CALLS = {"exec", "eval", "compile", "__import__", "import_module"}


def run_static_hygiene_audit(script_path: Path) -> Dict[str, Any]:
    src = script_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(script_path))
    float_literals: List[int] = []
    refused_imports: List[str] = []
    refused_calls: List[str] = []
    sys_path_mutations: List[int] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            float_literals.append(node.lineno)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in REFUSED_MODULES or alias.name in REFUSED_DOTTED:
                    refused_imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            root = mod.split(".")[0]
            if root in REFUSED_MODULES or mod in REFUSED_DOTTED:
                refused_imports.append(mod)
        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id in REFUSED_CALLS:
                refused_calls.append(f"{fn.id}@{node.lineno}")
            elif isinstance(fn, ast.Attribute) and fn.attr in REFUSED_CALLS:
                refused_calls.append(f".{fn.attr}@{node.lineno}")
            elif isinstance(fn, ast.Attribute) and isinstance(fn.value, ast.Attribute):
                if (
                    isinstance(fn.value.value, ast.Name)
                    and fn.value.value.id == "sys"
                    and fn.value.attr == "path"
                ):
                    sys_path_mutations.append(node.lineno)
        elif isinstance(node, ast.Assign):
            for tgt in node.targets:
                if (
                    isinstance(tgt, ast.Attribute)
                    and isinstance(tgt.value, ast.Name)
                    and tgt.value.id == "sys"
                    and tgt.attr == "path"
                ):
                    sys_path_mutations.append(node.lineno)

    return {
        "ast_float_literal_count": len(float_literals),
        "ast_float_lines": float_literals,
        "refused_import_count": len(refused_imports),
        "refused_imports": refused_imports,
        "refused_call_count": len(refused_calls),
        "refused_calls": refused_calls,
        "sys_path_mutation_count": len(sys_path_mutations),
        "t7b_part1_clean": (
            len(refused_imports) == 0
            and len(refused_calls) == 0
            and len(sys_path_mutations) == 0
        ),
        "passed": (
            len(float_literals) == 0
            and len(refused_imports) == 0
            and len(refused_calls) == 0
            and len(sys_path_mutations) == 0
        ),
    }


def count_json_floats(obj: Any) -> int:
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(count_json_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(count_json_floats(v) for v in obj)
    return 0


# ---------------------------------------------------------------------------
# MODULE W1 — Exact SymPy Cyclotomic Rings + 50-Digit Momentum-Basis Weil
# ---------------------------------------------------------------------------
def build_weil_position_mp(N: int, r: int) -> Dict[str, Any]:
    """Position-basis Weil operators (used for momentum-basis equivalence check & W2/W3/W4)."""
    inv2 = (N + 1) // 2
    z_tab = [mp.exp(mp.mpc(0, 2) * mp.pi * k / N) for k in range(N)]
    G = mp.mpc(0)
    for b in range(N):
        G += z_tab[(-r * inv2 * b * b) % N]
    invG = ONE / G
    L = mp.zeros(N, N)
    Sinv = mp.zeros(N, N)
    Pflip = mp.zeros(N, N)
    for j in range(N):
        L[j, j] = z_tab[(r * inv2 * j * j) % N]
        Pflip[(-j) % N, j] = ONE
        for k in range(N):
            Sinv[j, k] = invG * z_tab[(r * j * k) % N]
    S = Sinv.H
    R = Sinv * L.H * Sinv.H
    C3 = S * L.H
    Wp = L + C3 * L * C3.H + (C3 * C3) * L * (C3 * C3).H
    Wm = Wp.H
    W6 = Wp + Wm
    Wch = mp.mpc(0, -1) * (Wp - Wm)
    return {
        "G": G, "L": L, "Sinv": Sinv, "S": S, "R": R,
        "C3": C3, "Pflip": Pflip, "Wp": Wp, "Wm": Wm, "W6": W6, "Wch": Wch,
    }


def build_weil_momentum_kernels(N: int, r: int) -> Tuple[mp.mpc, mp.matrix, mp.matrix, mp.matrix]:
    """
    Fourier-dual (momentum) Weil basis: M_hat = F M F^H with F_{p,j} = N^{-1/2} zeta_N^{-p j}.
    Exact momentum-space kernels:
      (L_hat)_{p, q}    = (conj(G_{N,r}) / N) * zeta_N^{-r^{-1} * inv2 * (p - q)^2}
      (Sinv_hat)_{p, q} = G_{N,r}^{-1} * zeta_N^{r^{-1} * p * q}
      P_flip_hat        = P_flip
    """
    inv2 = (N + 1) // 2
    r_inv = pow(r, -1, N)
    z_tab = [mp.exp(mp.mpc(0, 2) * mp.pi * k / N) for k in range(N)]
    G = mp.mpc(0)
    for b in range(N):
        G += z_tab[(-r * inv2 * b * b) % N]
    invG = ONE / G
    cG_over_N = mp.conj(G) / mp.mpf(N)

    # Precompute circulant row for L_hat
    l_row = [cG_over_N * z_tab[(-r_inv * inv2 * d * d) % N] for d in range(N)]

    L_hat = mp.matrix(N, N)
    Sinv_hat = mp.matrix(N, N)
    Pflip = mp.zeros(N, N)
    for p in range(N):
        Pflip[(-p) % N, p] = ONE
        for q in range(N):
            L_hat[p, q] = l_row[(p - q) % N]
            Sinv_hat[p, q] = invG * z_tab[(r_inv * p * q) % N]
    return G, L_hat, Sinv_hat, Pflip


def expected_tr_c3_mp(N: int, r: int) -> mp.mpc:
    if N % 3 != 0:
        return mp.mpc(jacobi_symbol(-3, N), 0)
    return mp.mpc(0, jacobi_symbol(r, 3)) * mp.sqrt(THREE)


def expected_parity_dims(N: int, r: int) -> Dict[str, int]:
    # Total trace T = d0 + w d1 + w^2 d2
    # Even trace Te = (T + 1)/2, Odd trace To = (T - 1)/2
    # For any sector with dim D and trace T = ReT + i*ImT:
    # d1 - d2 = 2*ImT / sqrt(3)
    # d0 - (d1+d2)/2 = ReT  =>  3*d0 - D = 2*ReT  => d0 = (D + 2*ReT)/3
    if N % 3 != 0:
        reT = jacobi_symbol(-3, N)
        diff = 0
    else:
        reT = 0
        diff = 2 * jacobi_symbol(r, 3)

    d0 = (N + 2 * reT) // 3
    s12 = N - d0
    d1 = (s12 + diff) // 2
    d2 = (s12 - diff) // 2

    De = (N + 1) // 2
    Do = (N - 1) // 2
    # 2*ReTe = reT + 1, 2*ReTo = reT - 1
    d0e = (De + reT + 1) // 3
    d0o = (Do + reT - 1) // 3
    diff_half = diff // 2
    d1e = (De - d0e + diff_half) // 2
    d2e = (De - d0e - diff_half) // 2
    d1o = (Do - d0o + diff_half) // 2
    d2o = (Do - d0o - diff_half) // 2
    return {
        "d0": d0, "d1": d1, "d2": d2, "d1_minus_d2": d1 - d2,
        "d0_even": d0e, "d1_even": d1e, "d2_even": d2e, "even_chiral_diff": d1e - d2e,
        "d0_odd": d0o, "d1_odd": d1o, "d2_odd": d2o, "odd_chiral_diff": d1o - d2o,
    }


def sympy_cyclotomic_w1_verify() -> Dict[str, Any]:
    """
    Exact algebraic verification in Q[x]/(Phi_N(x)) for N in {3, 5, 7, 9, 15}
    plus exact algebraic CRT rho_{15,1} ~= rho_{3,2} (x) rho_{5,2} and rho_{15,4} ~= rho_{15,1}.
    """
    x = sp.Symbol("x")

    def build_cyc_ops(N: int, r: int, M_ring: int) -> Dict[str, Any]:
        # Embed zeta_N as x^{M_ring // N} in Q[x]/(Phi_{M_ring}(x))
        step = M_ring // N
        phi = sp.Poly(sp.cyclotomic_poly(M_ring, x), x, domain="QQ")
        z = [sp.rem(sp.Poly(x ** ((k * step) % M_ring), x, domain="QQ"), phi) for k in range(N)]
        inv2 = (N + 1) // 2
        G = sp.Poly(0, x, domain="QQ")
        for b in range(N):
            G = G + z[(-r * inv2 * b * b) % N]
        G = sp.rem(G, phi)
        invG = sp.invert(G, phi)
        conj_invG = sp.Poly(0, x, domain="QQ")
        for (deg,), coeff in invG.as_dict().items():
            conj_invG = conj_invG + coeff * sp.rem(
                sp.Poly(x ** ((-deg) % M_ring), x, domain="QQ"), phi
            )
        conj_invG = sp.rem(conj_invG, phi)

        L = [[sp.Poly(0, x, domain="QQ") for _ in range(N)] for _ in range(N)]
        LH = [[sp.Poly(0, x, domain="QQ") for _ in range(N)] for _ in range(N)]
        Sinv = [[sp.Poly(0, x, domain="QQ") for _ in range(N)] for _ in range(N)]
        S = [[sp.Poly(0, x, domain="QQ") for _ in range(N)] for _ in range(N)]
        Pflip = [[sp.Poly(0, x, domain="QQ") for _ in range(N)] for _ in range(N)]
        one_p = sp.Poly(1, x, domain="QQ")
        for j in range(N):
            L[j][j] = z[(r * inv2 * j * j) % N]
            LH[j][j] = z[(-r * inv2 * j * j) % N]
            Pflip[(-j) % N][j] = one_p
            for k in range(N):
                Sinv[j][k] = sp.rem(invG * z[(r * j * k) % N], phi)
                S[j][k] = sp.rem(conj_invG * z[(-r * j * k) % N], phi)

        def mm(A: List[List[sp.Poly]], B: List[List[sp.Poly]]) -> List[List[sp.Poly]]:
            n = len(A)
            out = [[sp.Poly(0, x, domain="QQ") for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    acc = sp.Poly(0, x, domain="QQ")
                    for k in range(n):
                        if not A[i][k].is_zero and not B[k][j].is_zero:
                            acc = acc + A[i][k] * B[k][j]
                    out[i][j] = sp.rem(acc, phi)
            return out

        C3 = [[sp.rem(S[i][j] * LH[j][j], phi) for j in range(N)] for i in range(N)]
        return {"phi": phi, "z": z, "G": G, "L": L, "LH": LH, "Sinv": Sinv, "S": S, "C3": C3, "Pflip": Pflip, "mm": mm}

    def mat_eq(A: List[List[sp.Poly]], B: List[List[sp.Poly]], phi: sp.Poly) -> bool:
        n = len(A)
        for i in range(n):
            for j in range(n):
                if not sp.rem(A[i][j] - B[i][j], phi).is_zero:
                    return False
        return True

    cases: Dict[str, Any] = {}
    all_exact_ok = True
    for N, r in [(3, 1), (3, 2), (5, 1), (5, 2), (7, 1), (9, 1), (15, 1), (15, 4)]:
        ops = build_cyc_ops(N, r, N)
        phi = ops["phi"]
        mm = ops["mm"]
        one_p = sp.Poly(1, x, domain="QQ")
        zero_p = sp.Poly(0, x, domain="QQ")
        Id = [[one_p if i == j else zero_p for j in range(N)] for i in range(N)]

        # Unitarity S * Sinv == I
        unit_ok = mat_eq(mm(ops["S"], ops["Sinv"]), Id, phi)
        # Spinor sign Sinv^2 == (-1/N) * Pflip
        sgn = jacobi_symbol(-1, N)
        rhs_spin = [[sp.Poly(sgn, x, domain="QQ") * ops["Pflip"][i][j] for j in range(N)] for i in range(N)]
        spin_ok = mat_eq(mm(ops["Sinv"], ops["Sinv"]), rhs_spin, phi)
        # Order 3: C3^3 == I
        C3_2 = mm(ops["C3"], ops["C3"])
        C3_3 = mm(C3_2, ops["C3"])
        c3_ord_ok = mat_eq(C3_3, Id, phi)
        # Exact tr(C3)
        tr_c3 = sp.Poly(0, x, domain="QQ")
        for i in range(N):
            tr_c3 = tr_c3 + ops["C3"][i][i]
        tr_c3 = sp.rem(tr_c3, phi)
        if N % 3 != 0:
            exp_tr = sp.Poly(jacobi_symbol(-3, N), x, domain="QQ")
        else:
            # +i*sqrt(3) = 2*omega + 1 in Q[x]/(Phi_N(x)), omega = x^{N//3}
            om_p = sp.Poly(x ** (N // 3), x, domain="QQ")
            exp_tr = sp.rem(sp.Poly(jacobi_symbol(r, 3), x, domain="QQ") * (2 * om_p + one_p), phi)
        tr_c3_ok = sp.rem(tr_c3 - exp_tr, phi).is_zero

        # Exact tr(Pflip * C3) == +1
        tr_flip = sp.Poly(0, x, domain="QQ")
        for i in range(N):
            tr_flip = tr_flip + ops["C3"][(-i) % N][i]
        tr_flip = sp.rem(tr_flip, phi)
        tr_flip_ok = sp.rem(tr_flip - one_p, phi).is_zero

        ok = unit_ok and spin_ok and c3_ord_ok and tr_c3_ok and tr_flip_ok
        all_exact_ok = all_exact_ok and ok
        cases[f"N{N}_r{r}"] = {
            "unitary_exact": unit_ok,
            "spinor_sign_exact": spin_ok,
            "c3_order3_exact": c3_ord_ok,
            "tr_c3_exact": tr_c3_ok,
            "tr_flip_c3_exact": tr_flip_ok,
            "passed": ok,
        }

    # Exact algebraic CRT in Q[x]/(Phi_15(x)): rho_{15,1} ~= rho_{3,2} (x) rho_{5,2}, rho_{15,4} ~= rho_{15,1}
    op15_1 = build_cyc_ops(15, 1, 15)
    op15_4 = build_cyc_ops(15, 4, 15)
    op3_2 = build_cyc_ops(3, 2, 15)
    op5_2 = build_cyc_ops(5, 2, 15)
    phi15 = op15_1["phi"]

    def kron_cyc(A: List[List[sp.Poly]], B: List[List[sp.Poly]]) -> List[List[sp.Poly]]:
        na, nb = len(A), len(B)
        out = [[sp.Poly(0, x, domain="QQ") for _ in range(na * nb)] for _ in range(na * nb)]
        for ia in range(na):
            for ja in range(na):
                for ib in range(nb):
                    for jb in range(nb):
                        out[ia * nb + ib][ja * nb + jb] = sp.rem(A[ia][ja] * B[ib][jb], phi15)
        return out

    # P_CRT maps j in Z/15Z -> index (j%3)*5 + (j%5)
    crt_idx = [(j % 3) * 5 + (j % 5) for j in range(15)]
    def perm_conj_cyc(M: List[List[sp.Poly]], perm: Sequence[int]) -> List[List[sp.Poly]]:
        n = len(perm)
        out = [[sp.Poly(0, x, domain="QQ") for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                out[perm[i]][perm[j]] = M[i][j]
        return out

    crt_15_1_exact: Dict[str, bool] = {}
    for gname in ("L", "Sinv", "C3", "Pflip"):
        lhs = perm_conj_cyc(op15_1[gname], crt_idx)
        rhs = kron_cyc(op3_2[gname], op5_2[gname])
        crt_15_1_exact[gname] = mat_eq(lhs, rhs, phi15)

    # U_2 maps k -> 2k mod 15: U_2 rho_{15,4} U_2^T == rho_{15,1}
    u2_perm = [(2 * k) % 15 for k in range(15)]
    crt_15_4_exact: Dict[str, bool] = {}
    for gname in ("L", "Sinv", "C3", "Pflip"):
        lhs = perm_conj_cyc(op15_4[gname], u2_perm)
        rhs = op15_1[gname]
        crt_15_4_exact[gname] = mat_eq(lhs, rhs, phi15)

    crt_ok = all(crt_15_1_exact.values()) and all(crt_15_4_exact.values())
    all_exact_ok = all_exact_ok and crt_ok
    return {
        "cases": cases,
        "crt_15_1_exact": crt_15_1_exact,
        "crt_15_4_exact": crt_15_4_exact,
        "all_exact_passed": all_exact_ok,
    }


def run_module_w1() -> Dict[str, Any]:
    sympy_res = sympy_cyclotomic_w1_verify()

    # 1. Verify exact unitary equivalence of momentum-basis kernels to F * pos * F^H for N in {3,5,7,9,15}
    momentum_equiv_max_err = ZERO
    for N, r in [(3, 1), (5, 1), (7, 1), (9, 1), (15, 1), (15, 4)]:
        pos = build_weil_position_mp(N, r)
        _, L_hat, Sinv_hat, Pflip_hat = build_weil_momentum_kernels(N, r)
        inv_sN = ONE / mp.sqrt(mp.mpf(N))
        F = mp.matrix(N, N)
        for p in range(N):
            for j in range(N):
                F[p, j] = inv_sN * mp.exp(mp.mpc(0, -2) * mp.pi * p * j / N)
        eL = mat_frob(L_hat - F * pos["L"] * F.H)
        eS = mat_frob(Sinv_hat - F * pos["Sinv"] * F.H)
        eP = mat_frob(Pflip_hat - F * pos["Pflip"] * F.H)
        momentum_equiv_max_err = max(momentum_equiv_max_err, eL, eS, eP)

    # 2. Sweep all 220 (N, r) pairs in momentum basis at 50 digits
    pairs: List[Tuple[int, int]] = []
    for N in range(3, 50, 2):
        coprimes = [r for r in range(1, N) if math.gcd(r, N) == 1]
        selected = coprimes if N <= 27 else coprimes[:6]
        for r in selected:
            pairs.append((N, r))

    max_tr_c3_err = ZERO
    max_flip_trace_err = ZERO
    max_spinor_sign_err = ZERO
    max_unitarity_err = ZERO
    parity_dim_mismatches = 0
    sample_dims: Dict[str, Dict[str, int]] = {}

    for N, r in pairs:
        _, L_hat, Sinv_hat, Pflip = build_weil_momentum_kernels(N, r)
        # tr(C3_hat) = tr(Sinv_hat^H * L_hat^H) = sum_{p,q} conj(Sinv_hat[q,p]) * conj(L_hat[p,q])
        tr_c3 = mp.mpc(0)
        tr_flip = mp.mpc(0)
        for p in range(N):
            mp_p = (-p) % N
            for q in range(N):
                l_conj = mp.conj(L_hat[p, q])
                tr_c3 += mp.conj(Sinv_hat[q, p]) * l_conj
                tr_flip += mp.conj(Sinv_hat[q, mp_p]) * l_conj

        exp_tr = expected_tr_c3_mp(N, r)
        err_tr = abs(tr_c3 - exp_tr)
        err_fl = abs(tr_flip - ONE)
        max_tr_c3_err = max(max_tr_c3_err, err_tr)
        max_flip_trace_err = max(max_flip_trace_err, err_fl)

        # Direct spinor-sign & unitarity check on Sinv_hat
        sgn = mp.mpf(jacobi_symbol(-1, N))
        if N <= 19:
            err_spin = mat_frob(Sinv_hat * Sinv_hat - sgn * Pflip)
            err_unit = mat_frob(Sinv_hat.H * Sinv_hat - mp.eye(N))
        else:
            # Deterministic probe vectors spanning both even & odd subspaces
            err_spin = ZERO
            err_unit = ZERO
            for idx_probe in (0, 1, 2, N // 2, N - 1):
                e = mp.zeros(N, 1)
                e[idx_probe, 0] = ONE
                v1 = Sinv_hat * (Sinv_hat * e) - sgn * (Pflip * e)
                v2 = Sinv_hat.H * (Sinv_hat * e) - e
                err_spin = max(err_spin, mat_frob(v1))
                err_unit = max(err_unit, mat_frob(v2))
        max_spinor_sign_err = max(max_spinor_sign_err, err_spin)
        max_unitarity_err = max(max_unitarity_err, err_unit)

        # Verify parity-split dimensions directly from traces
        om = mp.exp(mp.mpc(0, 2) * mp.pi / THREE)
        tr_e = (tr_c3 + tr_flip) / TWO
        tr_o = (tr_c3 - tr_flip) / TWO
        De = mp.mpf((N + 1) // 2)
        Do = mp.mpf((N - 1) // 2)
        exp_dims = expected_parity_dims(N, r)
        d0e_num = mp.re((De + tr_e + mp.conj(tr_e)) / THREE)
        d1e_num = mp.re((De + mp.conj(om) * tr_e + om * mp.conj(tr_e)) / THREE)
        d2e_num = mp.re((De + om * tr_e + mp.conj(om) * mp.conj(tr_e)) / THREE)
        d0o_num = mp.re((Do + tr_o + mp.conj(tr_o)) / THREE)
        d1o_num = mp.re((Do + mp.conj(om) * tr_o + om * mp.conj(tr_o)) / THREE)
        d2o_num = mp.re((Do + om * tr_o + mp.conj(om) * mp.conj(tr_o)) / THREE)
        checks_d = [
            abs(d0e_num - exp_dims["d0_even"]),
            abs(d1e_num - exp_dims["d1_even"]),
            abs(d2e_num - exp_dims["d2_even"]),
            abs(d0o_num - exp_dims["d0_odd"]),
            abs(d1o_num - exp_dims["d1_odd"]),
            abs(d2o_num - exp_dims["d2_odd"]),
        ]
        if max(checks_d) > TOL_GATE_30:
            parity_dim_mismatches += 1
        if (N, r) in ((3, 1), (5, 1), (7, 1), (9, 1), (15, 1), (15, 4), (25, 1), (35, 1)):
            sample_dims[f"N{N}_r{r}"] = exp_dims

    # 3. All 17 odd N in 3..35 (r = 1): Mod-4 mirror dichotomy in momentum basis
    mod4_records: List[Dict[str, Any]] = []
    mod4_mismatches = 0
    max_mirror_c3_err = ZERO
    max_mirror_w6_err = ZERO
    max_mirror_wch_err = ZERO
    max_c3_order3_err = ZERO
    max_full_spinor_err = ZERO
    om = mp.exp(mp.mpc(0, 2) * mp.pi / THREE)

    for N in range(3, 36, 2):
        _, L_hat, Sinv_hat, Pflip = build_weil_momentum_kernels(N, 1)
        C3_hat = Sinv_hat.H * L_hat.H
        C3_2 = C3_hat * C3_hat
        err_ord3 = mat_frob(C3_2 * C3_hat - mp.eye(N))
        max_c3_order3_err = max(max_c3_order3_err, err_ord3)

        sgn = mp.mpf(jacobi_symbol(-1, N))
        err_full_spin = mat_frob(Sinv_hat * Sinv_hat - sgn * Pflip)
        max_full_spinor_err = max(max_full_spinor_err, err_full_spin)

        Wp = L_hat + C3_hat * L_hat * C3_hat.H + C3_2 * L_hat * C3_2.H
        Wm = Wp.H
        W6 = Wp + Wm
        Wch = mp.mpc(0, -1) * (Wp - Wm)

        P_even = (mp.eye(N) + Pflip) / TWO
        P_odd = (mp.eye(N) - Pflip) / TWO
        P_q1 = (mp.eye(N) + mp.conj(om) * C3_hat + om * C3_2) / THREE
        P_q2 = (mp.eye(N) + om * C3_hat + mp.conj(om) * C3_2) / THREE

        B1e = orthonormal_basis_from_projector(P_even * P_q1)
        B2e = orthonormal_basis_from_projector(P_even * P_q2)
        B1o = orthonormal_basis_from_projector(P_odd * P_q1)
        B2o = orthonormal_basis_from_projector(P_odd * P_q2)
        B1 = orthonormal_basis_from_projector(P_q1)
        B2 = orthonormal_basis_from_projector(P_q2)

        spec1 = spectrum_real_hermitian(B1.H * W6 * B1)
        spec2 = spectrum_real_hermitian(B2.H * W6 * B2)
        spec1e = spectrum_real_hermitian(B1e.H * W6 * B1e)
        spec2e = spectrum_real_hermitian(B2e.H * W6 * B2e)
        spec1o = spectrum_real_hermitian(B1o.H * W6 * B1o)
        spec2o = spectrum_real_hermitian(B2o.H * W6 * B2o)

        diff_full = max_spec_diff(spec1, spec2)
        diff_even = max_spec_diff(spec1e, spec2e)
        diff_odd = max_spec_diff(spec1o, spec2o)

        isospectral_obs = (
            len(spec1) == len(spec2)
            and diff_full < TOL_GATE_30
            and diff_even < TOL_GATE_30
            and diff_odd < TOL_GATE_30
        )
        isospectral_pred = has_sqrt_minus_one_mod(N)

        mirror_a = None
        mirror_c3_err_str = None
        mirror_w6_err_str = None
        mirror_wch_err_str = None
        if isospectral_pred:
            a = find_sqrt_minus_one_mod(N)
            mirror_a = a
            Ua = mp.zeros(N, N)
            for k in range(N):
                Ua[(a * k) % N, k] = ONE
            e_c3 = mat_frob(Ua * mat_conj_entries(C3_hat) * Ua.T - C3_hat)
            e_w6 = mat_frob(Ua * mat_conj_entries(W6) * Ua.T - W6)
            e_wch = mat_frob(Ua * mat_conj_entries(Wch) * Ua.T + Wch)
            max_mirror_c3_err = max(max_mirror_c3_err, e_c3)
            max_mirror_w6_err = max(max_mirror_w6_err, e_w6)
            max_mirror_wch_err = max(max_mirror_wch_err, e_wch)
            mirror_c3_err_str = sci(e_c3)
            mirror_w6_err_str = sci(e_w6)
            mirror_wch_err_str = sci(e_wch)
        else:
            # Verify chiral split is genuine (either dim mismatch or spectral gap > 1e-6)
            if len(spec1) == len(spec2) and diff_full < mp.mpf("1e-6"):
                mod4_mismatches += 1

        if isospectral_obs != isospectral_pred:
            mod4_mismatches += 1

        mod4_records.append({
            "N": N,
            "prime_factors": odd_prime_factors(N),
            "all_primes_1_mod_4": isospectral_pred,
            "isospectral_observed": isospectral_obs,
            "dim_H1": len(spec1),
            "dim_H2": len(spec2),
            "dim_H1_even": len(spec1e),
            "dim_H2_even": len(spec2e),
            "dim_H1_odd": len(spec1o),
            "dim_H2_odd": len(spec2o),
            "w6_spec_diff_full": sci(diff_full) if len(spec1) == len(spec2) else "DIM_MISMATCH",
            "w6_spec_diff_even": sci(diff_even) if len(spec1e) == len(spec2e) else "DIM_MISMATCH",
            "w6_spec_diff_odd": sci(diff_odd) if len(spec1o) == len(spec2o) else "DIM_MISMATCH",
            "mirror_a": mirror_a,
            "mirror_c3_err": mirror_c3_err_str,
            "mirror_w6_err": mirror_w6_err_str,
            "mirror_wch_err": mirror_wch_err_str,
        })

    # 4. 50-digit CRT verification for N = 15 (all operators including W6, Wch)
    w15_1 = build_weil_position_mp(15, 1)
    w15_4 = build_weil_position_mp(15, 4)
    w3_2 = build_weil_position_mp(3, 2)
    w5_2 = build_weil_position_mp(5, 2)
    P_crt = perm_matrix_mp([(j % 3) * 5 + (j % 5) for j in range(15)])
    U_2 = perm_matrix_mp([(2 * k) % 15 for k in range(15)])

    crt_15_1_errs: Dict[str, str] = {}
    crt_15_4_errs: Dict[str, str] = {}
    max_crt_err = ZERO
    for op_name in ("L", "Sinv", "S", "R", "C3", "Pflip"):
        e1 = mat_frob(P_crt * w15_1[op_name] * P_crt.T - kron_mp(w3_2[op_name], w5_2[op_name]))
        e4 = mat_frob(U_2 * w15_4[op_name] * U_2.T - w15_1[op_name])
        crt_15_1_errs[op_name] = sci(e1)
        crt_15_4_errs[op_name] = sci(e4)
        max_crt_err = max(max_crt_err, e1, e4)
    # Also W6 and Wch for U_2: rho_{15,4} ~= rho_{15,1}
    for op_name in ("W6", "Wch"):
        e4 = mat_frob(U_2 * w15_4[op_name] * U_2.T - w15_1[op_name])
        crt_15_4_errs[op_name] = sci(e4)
        max_crt_err = max(max_crt_err, e4)

    passed = (
        sympy_res["all_exact_passed"]
        and len(pairs) == 220
        and momentum_equiv_max_err < TOL_GATE_30
        and max_tr_c3_err < TOL_GATE_30
        and max_flip_trace_err < TOL_GATE_30
        and max_spinor_sign_err < TOL_GATE_30
        and max_unitarity_err < TOL_GATE_30
        and max_c3_order3_err < TOL_GATE_30
        and max_full_spinor_err < TOL_GATE_30
        and parity_dim_mismatches == 0
        and mod4_mismatches == 0
        and max_mirror_c3_err < TOL_GATE_30
        and max_mirror_w6_err < TOL_GATE_30
        and max_mirror_wch_err < TOL_GATE_30
        and max_crt_err < TOL_GATE_30
    )

    return {
        "sympy_cyclotomic_exact": sympy_res,
        "momentum_basis_equiv_max_err": sci(momentum_equiv_max_err),
        "pairs_checked_count": len(pairs),
        "max_tr_c3_err": sci(max_tr_c3_err),
        "max_flip_trace_err": sci(max_flip_trace_err),
        "max_spinor_sign_err": sci(max_spinor_sign_err),
        "max_unitarity_err": sci(max_unitarity_err),
        "max_c3_order3_err": sci(max_c3_order3_err),
        "max_full_spinor_err": sci(max_full_spinor_err),
        "parity_dim_mismatches": parity_dim_mismatches,
        "sample_parity_dims": sample_dims,
        "mod4_odd_n_count": len(mod4_records),
        "mod4_isospectral_list": [r["N"] for r in mod4_records if r["isospectral_observed"]],
        "mod4_chiral_split_list": [r["N"] for r in mod4_records if not r["isospectral_observed"]],
        "mod4_mismatches": mod4_mismatches,
        "max_mirror_c3_err": sci(max_mirror_c3_err),
        "max_mirror_w6_err": sci(max_mirror_w6_err),
        "max_mirror_wch_err": sci(max_mirror_wch_err),
        "mod4_records": mod4_records,
        "crt_15_1_errs": crt_15_1_errs,
        "crt_15_4_errs": crt_15_4_errs,
        "max_crt_err": sci(max_crt_err),
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# MODULE W2 — Leg(5) 12-Ray Intertwiner, Phi^wp / Phi^Siegel, O_27 & Q_6
# ---------------------------------------------------------------------------
def norm_ray_f5(x: int, y: int) -> Tuple[int, int]:
    x %= 5
    y %= 5
    if x == 0:
        return (0, y if y in (1, 2) else (-y) % 5)
    return (x, y) if x in (1, 2) else ((-x) % 5, (-y) % 5)


def euler_pentagonal_eta(tau: mp.mpc, n_terms: int = 55) -> mp.mpc:
    """Dedekind eta(tau) via Euler pentagonal number theorem (disjoint from q-products)."""
    qt = mp.exp(mp.mpc(0, 2) * mp.pi * tau)
    s = mp.mpc(1)
    for n in range(1, n_terms + 1):
        e1 = n * (3 * n - 1) // 2
        e2 = n * (3 * n + 1) // 2
        term = qt ** e1 + qt ** e2
        if n % 2 == 1:
            s -= term
        else:
            s += term
    return mp.exp(mp.mpc(0, 1) * mp.pi * tau / mp.mpf(12)) * s


def build_leg5_via_12rays() -> Dict[str, Any]:
    """
    Build Leg(5) as the -1 eigenspace of the scalar-2 involution on the 12-ray space
    Rays(5) = (F_5^2 minus {0}) / {+-1}.
    """
    ordered_lines = [(1, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4)]
    rays: List[Tuple[int, int]] = []
    for lx, ly in ordered_lines:
        r1 = norm_ray_f5(lx, ly)
        r2 = norm_ray_f5(2 * lx, 2 * ly)
        rays.append(r1)
        rays.append(r2)
    ray_idx = {r: i for i, r in enumerate(rays)}

    inv_s2 = ONE / mp.sqrt(TWO)
    B_leg = mp.zeros(12, 6)
    for i, (lx, ly) in enumerate(ordered_lines):
        r1 = norm_ray_f5(lx, ly)
        r2 = norm_ray_f5(2 * lx, 2 * ly)
        B_leg[ray_idx[r1], i] = inv_s2
        B_leg[ray_idx[r2], i] = -inv_s2

    def rho_leg(M: Tuple[Tuple[int, int], Tuple[int, int]]) -> mp.matrix:
        P12 = mp.zeros(12, 12)
        a, b = M[0]
        c, d = M[1]
        for j, (rx, ry) in enumerate(rays):
            nx, ny = (a * rx + b * ry) % 5, (c * rx + d * ry) % 5
            P12[ray_idx[norm_ray_f5(nx, ny)], j] = ONE
        return B_leg.H * P12 * B_leg

    # Verify iota involution on 12 rays: P_iota * B_leg == -B_leg
    P_iota = mp.zeros(12, 12)
    for j, (rx, ry) in enumerate(rays):
        P_iota[ray_idx[norm_ray_f5(2 * rx, 2 * ry)], j] = ONE
    iota_err = mat_frob(P_iota * B_leg + B_leg)

    return {
        "ordered_lines": ordered_lines,
        "rays": rays,
        "B_leg": B_leg,
        "rho_leg": rho_leg,
        "iota_minus1_err": iota_err,
    }


def weil5_even_block(r: int) -> Dict[str, mp.matrix]:
    w = build_weil_position_mp(5, r)
    inv_s2 = ONE / mp.sqrt(TWO)
    Be = mp.zeros(5, 3)
    Be[0, 0] = ONE
    Be[1, 1] = inv_s2
    Be[4, 1] = inv_s2
    Be[2, 2] = inv_s2
    Be[3, 2] = inv_s2
    return {
        k: Be.H * w[k] * Be
        for k in ("L", "Sinv", "S", "R", "C3", "W6", "Wch")
    }


def build_intertwiner_simultaneous_diag(
    leg_ops: Dict[str, mp.matrix],
    Pa: mp.matrix,
    Pb: mp.matrix,
    w5_2: Dict[str, mp.matrix],
    w5_1: Dict[str, mp.matrix],
) -> mp.matrix:
    """
    Construct unitary U: H_{5,2}^even (+) H_{5,1}^even -> Leg(5) via direct
    simultaneous diagonalization of (W_6, W_ch, C_3) (disjoint from L-eigenprojectors!).
    """
    om = mp.exp(mp.mpc(0, 2) * mp.pi / THREE)
    alpha = mp.mpf(7) / mp.mpf(10)

    def match_sector(P_sec: mp.matrix, w_sec: Dict[str, mp.matrix]) -> mp.matrix:
        # Orthonormal 6x3 basis of sector
        B_sec = orthonormal_basis_from_projector(P_sec)
        assert B_sec.cols == 3
        L_s = B_sec.H * leg_ops["L"] * B_sec
        C_s = B_sec.H * leg_ops["C_om"] * B_sec
        W6_s = B_sec.H * leg_ops["W6"] * B_sec
        Wch_s = B_sec.H * leg_ops["Wch_leg"] * B_sec

        # Remember Wch_leg = -Wch_weil, so W6_s - alpha*Wch_s matches W6_w + alpha*Wch_w!
        H_leg_s = (W6_s - alpha * Wch_s + (W6_s - alpha * Wch_s).H) / TWO
        H_w = (w_sec["W6"] + alpha * w_sec["Wch"] + (w_sec["W6"] + alpha * w_sec["Wch"]).H) / TWO

        _, V_leg_raw = mp.eigh(H_leg_s)
        _, V_w_raw = mp.eigh(H_w)

        def label_by_c3(V: mp.matrix, C_mat: mp.matrix) -> Dict[int, mp.matrix]:
            labeled: Dict[int, mp.matrix] = {}
            for col in range(3):
                v = mp.matrix(3, 1)
                for row in range(3):
                    v[row, 0] = V[row, col]
                lam = (v.H * C_mat * v)[0, 0]
                best_q = min(range(3), key=lambda q: abs(lam - om ** q))
                labeled[best_q] = v
            assert len(labeled) == 3
            return labeled

        v_leg = label_by_c3(V_leg_raw, C_s)
        v_w = label_by_c3(V_w_raw, w_sec["C3"])

        # Fix relative phases of q=1 and q=2 against q=0 using off-diagonal L matrix elements
        for q in (1, 2):
            m_leg = (v_leg[0].H * L_s * v_leg[q])[0, 0]
            m_w = (v_w[0].H * w_sec["L"] * v_w[q])[0, 0]
            assert abs(m_leg) > mp.mpf("1e-10") and abs(m_w) > mp.mpf("1e-10")
            phase = (m_w / m_leg) / abs(m_w / m_leg)
            v_leg[q] = v_leg[q] * phase

        # Assemble 6 x 3 isometry U_sec = B_sec * sum_{q=0}^2 |v_leg[q]><v_w[q]|
        U_loc = mp.zeros(3, 3)
        for q in range(3):
            U_loc += v_leg[q] * v_w[q].H
        return B_sec * U_loc

    Ua = match_sector(Pa, w5_2)
    Ub = match_sector(Pb, w5_1)
    U = mp.zeros(6, 6)
    for r in range(6):
        for c in range(3):
            U[r, c] = Ua[r, c]
            U[r, 3 + c] = Ub[r, c]
    return U


def run_module_w2() -> Dict[str, Any]:
    # --- Part A: Leg(5) via 12-ray involution projection & K_5 ---
    leg = build_leg5_via_12rays()
    rho_leg = leg["rho_leg"]
    B_leg = leg["B_leg"]
    rays = leg["rays"]

    L_mat = ((1, 1), (0, 1))
    S_mat = ((0, 4), (1, 0))
    R_mat = ((1, 0), (1, 1))
    Tau_mat = ((0, 1), (1, 0))

    L_leg = rho_leg(L_mat)
    S_leg = rho_leg(S_mat)
    R_leg = rho_leg(R_mat)
    tau_mir = rho_leg(Tau_mat)
    C_om = L_leg * R_leg.H
    W_L = L_leg + C_om * L_leg * C_om.H + (C_om * C_om) * L_leg * (C_om * C_om).H
    W_R = R_leg + C_om * R_leg * C_om.H + (C_om * C_om) * R_leg * (C_om * C_om).H
    W6_leg = W_L + W_R
    Wch_leg = mp.mpc(0, 1) * (W_L - W_R)

    # Enumerate PSL(2, F_5) and build K_5 via explicit conjugation
    def mul2(A: Tuple[Tuple[int, int], Tuple[int, int]], B: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return (
            ((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5),
        )

    def inv2(A: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        return ((A[1][1] % 5, (-A[0][1]) % 5), ((-A[1][0]) % 5, A[0][0] % 5))

    def canon_psl(A: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        B = (((-A[0][0]) % 5, (-A[0][1]) % 5), ((-A[1][0]) % 5, (-A[1][1]) % 5))
        return A if A < B else B

    psl = set()
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    if (a * d - b * c) % 5 == 1:
                        psl.add(canon_psl(((a, b), (c, d))))
    conj_L = sorted(set(canon_psl(mul2(mul2(g, L_mat), inv2(g))) for g in psl))

    K5 = mp.zeros(6, 6)
    for g in conj_L:
        K5 += rho_leg(g)
    k5_eigs = spectrum_real_hermitian(K5)
    lam_a = TWO + TWO * mp.sqrt(FIVE)
    lam_b = TWO - TWO * mp.sqrt(FIVE)
    k5_eig_err = max_spec_diff(k5_eigs, [lam_b, lam_b, lam_b, lam_a, lam_a, lam_a])

    Pa = (K5 - lam_b * mp.eye(6)) / (lam_a - lam_b)
    Pb = (lam_a * mp.eye(6) - K5) / (lam_a - lam_b)
    proj_errs = {
        "Pa_idem": mat_frob(Pa * Pa - Pa),
        "Pb_idem": mat_frob(Pb * Pb - Pb),
        "orth": mat_frob(Pa * Pb),
        "complete": mat_frob(Pa + Pb - mp.eye(6)),
    }
    comm_errs = {}
    for name, op in (
        ("L", L_leg), ("S", S_leg), ("R", R_leg), ("tau_mir", tau_mir),
        ("W_L", W_L), ("W_R", W_R), ("W6", W6_leg), ("Wch_leg", Wch_leg),
    ):
        comm_errs[name] = max(mat_frob(Pa * op - op * Pa), mat_frob(Pb * op - op * Pb))

    # Build unitary intertwiner U via simultaneous (W6, Wch, C3) diagonalization
    w5_2 = weil5_even_block(2)
    w5_1 = weil5_even_block(1)
    leg_ops = {"L": L_leg, "S": S_leg, "R": R_leg, "C_om": C_om, "W6": W6_leg, "Wch_leg": Wch_leg}
    U = build_intertwiner_simultaneous_diag(leg_ops, Pa, Pb, w5_2, w5_1)

    def bdiag(A: mp.matrix, B: mp.matrix) -> mp.matrix:
        M = mp.zeros(6, 6)
        for i in range(3):
            for j in range(3):
                M[i, j] = A[i, j]
                M[3 + i, 3 + j] = B[i, j]
        return M

    intertwine_errs = {
        "unitary": mat_frob(U.H * U - mp.eye(6)),
        "L": mat_frob(U.H * L_leg * U - bdiag(w5_2["L"], w5_1["L"])),
        "S": mat_frob(U.H * S_leg * U - bdiag(w5_2["S"], w5_1["S"])),
        "R": mat_frob(U.H * R_leg * U - bdiag(w5_2["R"], w5_1["R"])),
        "C3": mat_frob(U.H * C_om * U - bdiag(w5_2["C3"], w5_1["C3"])),
        "W6": mat_frob(U.H * W6_leg * U - bdiag(w5_2["W6"], w5_1["W6"])),
        "Wch_sign": mat_frob(U.H * Wch_leg * U + bdiag(w5_2["Wch"], w5_1["Wch"])),
    }
    phi_gold = (ONE + mp.sqrt(FIVE)) / TWO
    Ba = orthonormal_basis_from_projector(Pa)
    Bb = orthonormal_basis_from_projector(Pb)
    spec_w6_a = spectrum_real_hermitian(Ba.H * W6_leg * Ba)
    spec_w6_b = spectrum_real_hermitian(Bb.H * W6_leg * Bb)
    spec_wch_a = spectrum_real_hermitian(Ba.H * Wch_leg * Ba)
    spec_wch_b = spectrum_real_hermitian(Bb.H * Wch_leg * Bb)

    exp_w6_a = sorted([TWO * mp.sqrt(FIVE), phi_gold ** 2, phi_gold ** 2])
    exp_w6_b = sorted([-TWO * mp.sqrt(FIVE), phi_gold ** (-2), phi_gold ** (-2)])
    exp_wch_a = sorted([-mp.sqrt(THREE) * phi_gold ** 2, ZERO, mp.sqrt(THREE) * phi_gold ** 2])
    exp_wch_b = sorted([-mp.sqrt(THREE) * phi_gold ** (-2), ZERO, mp.sqrt(THREE) * phi_gold ** (-2)])
    leg5_spec_err = max(
        max_spec_diff(spec_w6_a, exp_w6_a),
        max_spec_diff(spec_w6_b, exp_w6_b),
        max_spec_diff(spec_wch_a, exp_wch_a),
        max_spec_diff(spec_wch_b, exp_wch_b),
    )

    # --- Part B: Phi^wp (-d^2/dz^2 ln jtheta(1)) & Phi^Siegel (jtheta(1) + pentagonal eta) ---
    def phi_wp(tau: mp.mpc) -> mp.matrix:
        q = mp.exp(mp.mpc(0, 1) * mp.pi * tau)
        v12 = mp.matrix(12, 1)
        pi2 = mp.pi * mp.pi
        for j, (rx, ry) in enumerate(rays):
            z = (mp.mpf(rx) * tau + mp.mpf(ry)) / FIVE
            u = mp.pi * z
            t0 = mp.jtheta(1, u, q, derivative=0)
            t1 = mp.jtheta(1, u, q, derivative=1)
            t2 = mp.jtheta(1, u, q, derivative=2)
            v12[j, 0] = -pi2 * (t2 * t0 - t1 * t1) / (t0 * t0)
        return S_leg * (B_leg.H * v12)

    def phi_siegel(tau: mp.mpc) -> mp.matrix:
        q = mp.exp(mp.mpc(0, 1) * mp.pi * tau)
        et = euler_pentagonal_eta(tau)
        y_im = mp.im(tau)
        v12 = mp.matrix(12, 1)
        for j, (rx, ry) in enumerate(rays):
            a1 = mp.mpf(rx) / FIVE
            a2 = mp.mpf(ry) / FIVE
            z = a1 * tau + a2
            abs_g = mp.exp(-mp.pi * y_im * a1 * a1) * abs(mp.jtheta(1, mp.pi * z, q) / et)
            v12[j, 0] = mp.log(abs_g)
        return S_leg * (B_leg.H * v12)

    def ratio_stats(v: mp.matrix) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
        na = mat_frob(Pa * v) ** 2
        nb = mat_frob(Pb * v) ** 2
        return nb / na, na / (na + nb), nb / (na + nb)

    omega_p = ONE / TWO + mp.mpc(0, 1) * mp.sqrt(THREE) / TWO
    tau_i = mp.mpc(0, 1)
    tau0 = mp.mpf(23) / mp.mpf(100) + mp.mpc(0, 1) * mp.mpf(137) / mp.mpf(100)

    R_wp_om, fa_wp_om, fb_wp_om = ratio_stats(phi_wp(omega_p))
    R_wp_i, fa_wp_i, fb_wp_i = ratio_stats(phi_wp(tau_i))
    wp_0 = phi_wp(tau0)
    wp_T = phi_wp(tau0 + ONE)
    wp_S = phi_wp(-ONE / tau0)
    R_wp_t0, _, _ = ratio_stats(wp_0)
    R_wp_t0T, _, _ = ratio_stats(wp_T)
    R_wp_t0S, _, _ = ratio_stats(wp_S)
    wp_vec_T_err = mat_frob(wp_T - L_leg * wp_0)
    wp_vec_S_err = mat_frob(wp_S - (tau0 * tau0) * S_leg * wp_0)
    wp_inv_err = max(abs(R_wp_t0T - R_wp_t0), abs(R_wp_t0S - R_wp_t0))
    wp_om_rat_err = abs(R_wp_om - ONE / FOUR)
    wp_i_rat_err = abs(R_wp_i - mp.mpf(7) / mp.mpf(23))

    R_sg_om, fa_sg_om, fb_sg_om = ratio_stats(phi_siegel(omega_p))
    R_sg_i, fa_sg_i, fb_sg_i = ratio_stats(phi_siegel(tau_i))
    sg_0 = phi_siegel(tau0)
    sg_T = phi_siegel(tau0 + ONE)
    sg_S = phi_siegel(-ONE / tau0)
    R_sg_t0, _, _ = ratio_stats(sg_0)
    R_sg_t0T, _, _ = ratio_stats(sg_T)
    R_sg_t0S, _, _ = ratio_stats(sg_S)
    sg_vec_T_err = mat_frob(sg_T - L_leg * sg_0)
    sg_vec_S_err = mat_frob(sg_S - S_leg * sg_0)
    sg_inv_err = max(abs(R_sg_t0T - R_sg_t0), abs(R_sg_t0S - R_sg_t0))

    # --- Part C: O_27^(3,3,3) via <C_tr, Sig_tr>-orbit, Q_6 via partition refinement ---
    def L_tr(s: Tuple[int, int, int]) -> Tuple[int, int, int]:
        x, y, z = s
        return (x % 27, z % 27, (x * z - y) % 27)

    def R_tr(s: Tuple[int, int, int]) -> Tuple[int, int, int]:
        x, y, z = s
        return (z % 27, y % 27, (y * z - x) % 27)

    def C_tr(s: Tuple[int, int, int]) -> Tuple[int, int, int]:
        x, y, z = s
        return (y % 27, z % 27, x % 27)

    def Sig_tr(s: Tuple[int, int, int]) -> Tuple[int, int, int]:
        x, y, z = s
        return (y % 27, x % 27, (x * y - z) % 27)

    seed = (3, 3, 3)
    orb = {seed}
    dq = deque([seed])
    while dq:
        u = dq.popleft()
        for fn in (C_tr, Sig_tr):
            v = fn(u)
            if v not in orb:
                orb.add(v)
                dq.append(v)
    # Confirm closure under L_tr, R_tr
    closed_lr = all(L_tr(s) in orb and R_tr(s) in orb for s in orb)
    states = sorted(orb)
    nO = len(states)
    st_idx = {s: i for i, s in enumerate(states)}

    pL = tuple(st_idx[L_tr(s)] for s in states)
    pR = tuple(st_idx[R_tr(s)] for s in states)
    pC = tuple(st_idx[C_tr(s)] for s in states)
    pSig = tuple(st_idx[Sig_tr(s)] for s in states)

    def comp(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple(a[b[i]] for i in range(len(a)))

    def invp(a: Tuple[int, ...]) -> Tuple[int, ...]:
        out = [0] * len(a)
        for i, v in enumerate(a):
            out[v] = i
        return tuple(out)

    # Enumerate G_3 = <pL, pR> and verify rho: (L, R, C, Sig) -> (1, 5, 2, 3) mod 6 homomorphism
    id_p = tuple(range(nO))
    G3_rho: Dict[Tuple[int, ...], int] = {id_p: 0}
    gq = deque([id_p])
    gens_rho = [(pL, 1), (pR, 5), (invp(pL), 5), (invp(pR), 1)]
    rho_hom_mismatches = 0
    while gq:
        g = gq.popleft()
        rg = G3_rho[g]
        for h, rh in gens_rho:
            gh = comp(h, g)
            rgh = (rh + rg) % 6
            if gh not in G3_rho:
                G3_rho[gh] = rgh
                gq.append(gh)
            elif G3_rho[gh] != rgh:
                rho_hom_mismatches += 1

    # Also verify full pairwise multiplication table homomorphism check across G_3 (sample/full: 216*4 + exact C, Sig)
    c_in_g3 = pC in G3_rho
    sig_in_g3 = pSig in G3_rho
    rho_C = G3_rho.get(pC, -1)
    rho_Sig = G3_rho.get(pSig, -1)
    rho3_tuple = [(4 * v) % 6 for v in (1, 5, rho_C, rho_Sig)]

    # Direct partition refinement: find all <L, R>-invariant block systems of size 6
    def minimal_block_system(a: int, b: int) -> Tuple[Tuple[int, ...], ...]:
        parent = list(range(nO))

        def find(u: int) -> int:
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u: int, v: int) -> bool:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
                return True
            return False

        union(a, b)
        changed = True
        while changed:
            changed = False
            for i in range(nO):
                ri = find(i)
                for p in (pL, pR):
                    if union(p[i], p[ri]):
                        changed = True
        groups: Dict[int, List[int]] = {}
        for i in range(nO):
            groups.setdefault(find(i), []).append(i)
        return tuple(sorted(tuple(sorted(v)) for v in groups.values()))

    six_block_systems = set()
    for j in range(1, nO):
        bs = minimal_block_system(0, j)
        if len(bs) == 6:
            six_block_systems.add(bs)

    assert len(six_block_systems) == 1
    Q6_blocks = next(iter(six_block_systems))
    blk_of = {x: bi for bi, blk in enumerate(Q6_blocks) for x in blk}
    qL = tuple(blk_of[pL[blk[0]]] for blk in Q6_blocks)
    qR = tuple(blk_of[pR[blk[0]]] for blk in Q6_blocks)
    qC = tuple(blk_of[pC[blk[0]]] for blk in Q6_blocks)
    qSig = tuple(blk_of[pSig[blk[0]]] for blk in Q6_blocks)
    fix_qC = sum(1 for i in range(6) if qC[i] == i)

    # Exhaustive 216-element character-defect check: chi_{V_new^(3)}(g) == rho(g) * chi_{V_new^(3)}(g)
    z6 = [mp.exp(mp.mpc(0, 2) * mp.pi * k / SIX) for k in range(6)]
    chi_O27: Dict[Tuple[int, ...], int] = {}
    chi_Q6: Dict[Tuple[int, ...], int] = {}
    char_defect_mismatches = 0
    char_defect_rho3_mismatches = 0
    for g, rg in G3_rho.items():
        cO = sum(1 for i in range(nO) if g[i] == i)
        qg = tuple(blk_of[g[blk[0]]] for blk in Q6_blocks)
        cQ = sum(1 for i in range(6) if qg[i] == i)
        chi_O27[g] = cO
        chi_Q6[g] = cQ
        c_new = cO - cQ
        if abs(mp.mpc(c_new) - z6[rg] * mp.mpc(c_new)) > TOL_GATE_30:
            char_defect_mismatches += 1
        if abs(mp.mpc(c_new) - z6[(4 * rg) % 6] * mp.mpc(c_new)) > TOL_GATE_30:
            char_defect_rho3_mismatches += 1

    # O_27 - Q_6 chiral moments m=0..4 for N in {3, 5, 7, 15} via exact G_3 group-algebra DP
    pCi = invp(pC)
    p_terms = [
        pL,
        comp(pC, comp(pL, pCi)),
        comp(pCi, comp(pL, pC)),
        pR,
        comp(pC, comp(pR, pCi)),
        comp(pCi, comp(pR, pC)),
    ]

    def g3_dp_moments_o27_and_q6(N: int) -> Tuple[List[mp.mpf], List[mp.mpf], List[mp.mpf]]:
        w = build_weil_position_mp(N, 1)
        Lw, Rw, Cw = w["L"], w["R"], w["C3"]
        CwH = Cw.H
        M_terms = [
            Lw,
            Cw * Lw * CwH,
            CwH * Lw * Cw,
            Rw,
            Cw * Rw * CwH,
            CwH * Rw * Cw,
        ]
        # Build S_0, S_1, S_2: dicts mapping g in G_3 -> N x N mp.matrix
        S0: Dict[Tuple[int, ...], mp.matrix] = {id_p: mp.eye(N)}
        S1: Dict[Tuple[int, ...], mp.matrix] = {}
        for pt, Mt in zip(p_terms, M_terms):
            if pt in S1:
                S1[pt] = S1[pt] + Mt
            else:
                S1[pt] = Mt.copy()
        S2: Dict[Tuple[int, ...], mp.matrix] = {}
        for g1, M1 in S1.items():
            for pt, Mt in zip(p_terms, M_terms):
                g2 = comp(pt, g1)
                prod = Mt * M1
                if g2 in S2:
                    S2[g2] = S2[g2] + prod
                else:
                    S2[g2] = prod

        # Helper: tr((Pi_1 - Pi_2) * X) where Pi_1 - Pi_2 = (-i / sqrt(3)) * (C - C^2)
        pref = mp.mpc(0, -1) / mp.sqrt(THREE)

        def trace_prod(A: mp.matrix, B: mp.matrix) -> mp.mpc:
            acc = mp.mpc(0)
            for i in range(N):
                for j in range(N):
                    acc += A[i, j] * B[j, i]
            return acc

        def chiral_from_pair(
            Sa: Dict[Tuple[int, ...], mp.matrix],
            Sb: Dict[Tuple[int, ...], mp.matrix],
        ) -> Tuple[mp.mpf, mp.mpf]:
            val_O = mp.mpc(0)
            val_Q = mp.mpc(0)
            # Pre-multiply Cw and CwH on Sa
            Sa_C = {g: Cw * M for g, M in Sa.items()}
            Sa_CH = {g: CwH * M for g, M in Sa.items()}
            for g1 in Sa:
                M1C = Sa_C[g1]
                M1CH = Sa_CH[g1]
                for g2, M2 in Sb.items():
                    g12 = comp(g1, g2)
                    gp = comp(pC, g12)
                    gm = comp(pCi, g12)
                    cOp, cOm = chi_O27[gp], chi_O27[gm]
                    cQp, cQm = chi_Q6[gp], chi_Q6[gm]
                    if cOp != 0 or cQp != 0:
                        tp = trace_prod(M1C, M2)
                        val_O += cOp * tp
                        val_Q += cQp * tp
                    if cOm != 0 or cQm != 0:
                        tm = trace_prod(M1CH, M2)
                        val_O -= cOm * tm
                        val_Q -= cQm * tm
            return mp.re(pref * val_O), mp.re(pref * val_Q)

        m_O: List[mp.mpf] = []
        m_Q: List[mp.mpf] = []
        for Sa, Sb in ((S0, S0), (S0, S1), (S0, S2), (S1, S2), (S2, S2)):
            vO, vQ = chiral_from_pair(Sa, Sb)
            m_O.append(vO)
            m_Q.append(vQ)
        m_diff = [a - b for a, b in zip(m_O, m_Q)]
        return m_O, m_Q, m_diff

    o27_minus_q6_res: Dict[str, Any] = {}
    max_o27_q6_diff = ZERO
    dp_q6_cache: Dict[int, List[mp.mpf]] = {}
    for N in (3, 5, 7, 15):
        mO, mQ, mDiff = g3_dp_moments_o27_and_q6(N)
        dp_q6_cache[N] = mQ
        mx = max(abs(x) for x in mDiff)
        max_o27_q6_diff = max(max_o27_q6_diff, mx)
        o27_minus_q6_res[f"N{N}"] = {
            "o27_moments_0_4": [fstr(x, 30) for x in mO],
            "q6_moments_0_4_dp": [fstr(x, 30) for x in mQ],
            "max_abs_diff_0_4": sci(mx),
        }

    # Independently compute Q_6 x Weil_N chiral moments m = 0..6 via direct (6N)x(6N) matrix powers
    # AND non-Hermitian eigen-decomposition on H_1, H_2 for N in {3, 5, 7, 9}
    PL = perm_matrix_mp(qL)
    PR = perm_matrix_mp(qR)
    PC = perm_matrix_mp(qC)
    om = mp.exp(mp.mpc(0, 2) * mp.pi / THREE)

    q6_weil_direct: Dict[str, Any] = {}
    max_q6_exact_err = ZERO
    max_q6_eig_cross_err = ZERO
    max_q6_dp_cross_err = ZERO

    exact_targets_q6: Dict[int, List[mp.mpf]] = {
        3: [mp.mpf(6), ZERO, mp.mpf(36), ZERO, mp.mpf(324), ZERO, mp.mpf(2916)],
        5: [ZERO] * 7,
        7: [ZERO, ZERO, ZERO, ZERO, -mp.mpf(108) * mp.sqrt(mp.mpf(21)), ZERO, -mp.mpf(720) * mp.sqrt(mp.mpf(21))],
        9: [mp.mpf(6), ZERO, mp.mpf(36), ZERO, mp.mpf(1152), ZERO, mp.mpf(24084)],
    }

    for N in (3, 5, 7, 9, 15):
        w = build_weil_position_mp(N, 1)
        gL = kron_mp(PL, w["L"])
        gR = kron_mp(PR, w["R"])
        gC = kron_mp(PC, w["C3"])
        gCH = gC.H
        nn = 6 * N

        Wp = gL + gC * gL * gCH + gCH * gL * gC
        Wm = gR + gC * gR * gCH + gCH * gR * gC
        W6 = Wp + Wm
        Pi1 = (mp.eye(nn) + mp.conj(om) * gC + om * gCH) / THREE
        Pi2 = (mp.eye(nn) + om * gC + mp.conj(om) * gCH) / THREE
        Pdiff = Pi1 - Pi2

        # Direct matrix powers m = 0..6
        # Compute W6^0, W6^1, W6^2, W6^3 directly, then traces for m=0..6 via W6^a * W6^b!
        W0 = mp.eye(nn)
        W1 = W6
        W2 = W1 * W1
        W3 = W2 * W1
        powers_pairs = [(W0, W0), (W0, W1), (W0, W2), (W0, W3), (W2, W2), (W2, W3), (W3, W3)]
        direct_ms: List[mp.mpf] = []
        for Wa, Wb in powers_pairs:
            # tr(Pdiff * Wa * Wb) = sum_{i,j} (Pdiff * Wa)[i,j] * Wb[j,i]
            PW = Pdiff * Wa
            acc = mp.mpc(0)
            for i in range(nn):
                for j in range(nn):
                    acc += PW[i, j] * Wb[j, i]
            direct_ms.append(mp.re(acc))

        rec: Dict[str, Any] = {
            "moments_0_6_direct": [fstr(x, 34) for x in direct_ms],
        }
        if N in exact_targets_q6:
            err_ex = max(abs(a - b) for a, b in zip(direct_ms, exact_targets_q6[N]))
            max_q6_exact_err = max(max_q6_exact_err, err_ex)
            rec["max_exact_target_err"] = sci(err_ex)
        if N in dp_q6_cache:
            err_dp = max(abs(a - b) for a, b in zip(direct_ms[:5], dp_q6_cache[N]))
            max_q6_dp_cross_err = max(max_q6_dp_cross_err, err_dp)
            rec["dp_vs_direct_0_4_err"] = sci(err_dp)

        # Eigenvalue verification for N in {3, 5, 7, 9}
        if N in (3, 5, 7, 9):
            B1 = orthonormal_basis_from_projector(Pi1)
            B2 = orthonormal_basis_from_projector(Pi2)
            # W6 commutes with gC, so H1 and H2 are invariant subspaces of W6
            W6_1 = B1.H * W6 * B1
            W6_2 = B2.H * W6 * B2
            e1 = mp.eig(W6_1, left=False, right=False) if W6_1.rows > 0 else []
            e2 = mp.eig(W6_2, left=False, right=False) if W6_2.rows > 0 else []
            eig_ms: List[mp.mpf] = []
            for m in range(7):
                s1 = sum((lam ** m for lam in e1), mp.mpc(0))
                s2 = sum((lam ** m for lam in e2), mp.mpc(0))
                eig_ms.append(mp.re(s1 - s2))
            err_eig = max(abs(a - b) for a, b in zip(direct_ms, eig_ms))
            max_q6_eig_cross_err = max(max_q6_eig_cross_err, err_eig)
            rec["eig_vs_direct_0_6_err"] = sci(err_eig)
            rec["dim_H1"] = B1.cols
            rec["dim_H2"] = B2.cols
        if N == 7:
            rec["moments_0_6_div_sqrt21"] = [fstr(x / mp.sqrt(mp.mpf(21)), 30) for x in direct_ms]

        q6_weil_direct[f"N{N}"] = rec

    passed = (
        leg["iota_minus1_err"] < TOL_GATE_30
        and len(psl) == 60
        and len(conj_L) == 12
        and k5_eig_err < TOL_GATE_30
        and max(proj_errs.values()) < TOL_GATE_30
        and max(comm_errs.values()) < TOL_GATE_30
        and max(intertwine_errs.values()) < TOL_GATE_30
        and leg5_spec_err < TOL_GATE_30
        and wp_om_rat_err < TOL_GATE_30
        and wp_i_rat_err < TOL_GATE_30
        and wp_inv_err < TOL_GATE_30
        and wp_vec_T_err < TOL_GATE_30
        and wp_vec_S_err < TOL_GATE_30
        and sg_inv_err < TOL_GATE_30
        and sg_vec_T_err < TOL_GATE_30
        and sg_vec_S_err < TOL_GATE_30
        and nO == 72
        and closed_lr
        and len(G3_rho) == 216
        and c_in_g3
        and sig_in_g3
        and rho_C == 2
        and rho_Sig == 3
        and rho3_tuple == [4, 2, 2, 0]
        and rho_hom_mismatches == 0
        and fix_qC == 3
        and char_defect_mismatches == 0
        and char_defect_rho3_mismatches == 0
        and max_o27_q6_diff < TOL_GATE_25
        and max_q6_exact_err < TOL_GATE_25
        and max_q6_eig_cross_err < TOL_GATE_25
        and max_q6_dp_cross_err < TOL_GATE_25
    )

    return {
        "leg5": {
            "iota_minus1_err": sci(leg["iota_minus1_err"]),
            "psl2_f5_order": len(psl),
            "conj_class_L_size": len(conj_L),
            "k5_eigs": [fstr(x, 30) for x in k5_eigs],
            "k5_eig_err": sci(k5_eig_err),
            "projector_errs": {k: sci(v) for k, v in proj_errs.items()},
            "commutator_errs": {k: sci(v) for k, v in comm_errs.items()},
            "intertwiner_errs": {k: sci(v) for k, v in intertwine_errs.items()},
            "spec_w6_3a": [fstr(x, 30) for x in spec_w6_a],
            "spec_w6_3b": [fstr(x, 30) for x in spec_w6_b],
            "spec_wch_3a": [fstr(x, 30) for x in spec_wch_a],
            "spec_wch_3b": [fstr(x, 30) for x in spec_wch_b],
            "spec_err": sci(leg5_spec_err),
        },
        "phi_wp": {
            "R5_omega_plus": fstr(R_wp_om, 38),
            "fa_omega_plus": fstr(fa_wp_om, 38),
            "fb_omega_plus": fstr(fb_wp_om, 38),
            "err_from_1_4": sci(wp_om_rat_err),
            "R5_i": fstr(R_wp_i, 38),
            "fa_i": fstr(fa_wp_i, 38),
            "fb_i": fstr(fb_wp_i, 38),
            "err_from_7_23": sci(wp_i_rat_err),
            "R5_tau0": fstr(R_wp_t0, 38),
            "sl2z_ratio_inv_err": sci(wp_inv_err),
            "vec_T_err": sci(wp_vec_T_err),
            "vec_S_err": sci(wp_vec_S_err),
        },
        "phi_siegel": {
            "R5_omega_plus": fstr(R_sg_om, 38),
            "fa_omega_plus": fstr(fa_sg_om, 38),
            "fb_omega_plus": fstr(fb_sg_om, 38),
            "R5_i": fstr(R_sg_i, 38),
            "fa_i": fstr(fa_sg_i, 38),
            "fb_i": fstr(fb_sg_i, 38),
            "R5_tau0": fstr(R_sg_t0, 38),
            "sl2z_ratio_inv_err": sci(sg_inv_err),
            "vec_T_err": sci(sg_vec_T_err),
            "vec_S_err": sci(sg_vec_S_err),
        },
        "chiral_freezing": {
            "o27_orbit_size": nO,
            "o27_closed_under_LR": closed_lr,
            "g3_order": len(G3_rho),
            "c_in_g3": c_in_g3,
            "sig_in_g3": sig_in_g3,
            "rho_L_R_C_Sig": [1, 5, rho_C, rho_Sig],
            "rho3_L_R_C_Sig": rho3_tuple,
            "rho_hom_mismatches": rho_hom_mismatches,
            "unique_6block_systems_count": len(six_block_systems),
            "q6_block_sizes": [len(b) for b in Q6_blocks],
            "q6_fix_C": fix_qC,
            "char_defect_mismatches": char_defect_mismatches,
            "char_defect_rho3_mismatches": char_defect_rho3_mismatches,
            "o27_minus_q6_0_4": o27_minus_q6_res,
            "max_o27_q6_diff_0_4": sci(max_o27_q6_diff),
            "q6_weil_direct": q6_weil_direct,
            "max_q6_exact_err": sci(max_q6_exact_err),
            "max_q6_eig_cross_err": sci(max_q6_eig_cross_err),
            "max_q6_dp_cross_err": sci(max_q6_dp_cross_err),
        },
        "passed": passed,
    }


# ---------------------------------------------------------------------------
# MODULE W3 — Branch-Free Completed-Square 1D Jacobi-Theta & 2D Stabilization
# ---------------------------------------------------------------------------
def theta_LN_completed_square(N: int, tau: mp.mpc, Nv: int = 24) -> Tuple[mp.matrix, mp.matrix, mp.mpf]:
    """
    L_N = [[2, 1], [1, (N+1)/2]], Q(u,v) = (u + v/2)^2 + (N/4) v^2.
    Dual coset j: u = m + j*(N+1)/(2N), v = n - j/N -> u + v/2 = m + (n + j)/2.
    P_{L_N}^odd(u, v) = (u + v/2) + i*(sqrt(N)/2)*v.
    Evaluates BOTH the (u + v/2) theta-derivative term and the i*(sqrt(N)/2)*v term
    explicitly (branch-free via jtheta(3, pi*tau, q) for the half-integer shift).
    """
    q = mp.exp(mp.mpc(0, 2) * mp.pi * tau)
    th0 = mp.jtheta(3, ZERO, q)
    # sum_m m * q^{m^2} = (-i/2) d/dz jtheta(3, z, q)|_{z=0}
    dth0 = mp.mpc(0, -1) / TWO * mp.jtheta(3, ZERO, q, derivative=1)
    pref1 = mp.exp(mp.mpc(0, 1) * mp.pi * tau / TWO)
    th1 = pref1 * mp.jtheta(3, mp.pi * tau, q)
    # sum_m (m + 1/2) * exp(2*pi*i*tau*(m+1/2)^2)
    dth1 = pref1 * (
        mp.mpc(0, -1) / TWO * mp.jtheta(3, mp.pi * tau, q, derivative=1)
        + (ONE / TWO) * mp.jtheta(3, mp.pi * tau, q)
    )

    ve = mp.matrix(N, 1)
    vo = mp.matrix(N, 1)
    max_re_part = ZERO
    i_sN_2 = mp.mpc(0, 1) * mp.sqrt(mp.mpf(N)) / TWO
    N_over_4 = mp.mpf(N) / FOUR
    two_pi_i_tau = mp.mpc(0, 2) * mp.pi * tau

    for j in range(N):
        se = mp.mpc(0)
        so = mp.mpc(0)
        so_re_piece = mp.mpc(0)
        for n in range(-Nv, Nv + 1):
            v = mp.mpf(n) - mp.mpf(j) / mp.mpf(N)
            qv = mp.exp(two_pi_i_tau * N_over_4 * v * v)
            if (n + j) % 2 == 0:
                fu, dfu = th0, dth0
            else:
                fu, dfu = th1, dth1
            se += fu * qv
            so_re_piece += dfu * qv
            so += (dfu + i_sN_2 * v * fu) * qv
        ve[j, 0] = se
        vo[j, 0] = so
        max_re_part = max(max_re_part, abs(so_re_piece))
    return ve, vo, max_re_part


def theta_Lp15_completed_square(tau: mp.mpc, Nv: int = 24) -> Tuple[mp.matrix, mp.matrix]:
    """
    L'_15 = [[4, 1], [1, 4]], Q'(u,v) = 2*(u + v/4)^2 + (15/8)*v^2.
    Dual coset j: u = m + 4j/15, v = n - j/15 -> u + v/4 = m + (n + j)/4.
    P_{L'_15}^odd(u, v) = (u + v/4) + i*(sqrt(15)/4)*v.
    """
    q2 = mp.exp(mp.mpc(0, 4) * mp.pi * tau)
    f0: List[mp.mpc] = []
    f_uv4: List[mp.mpc] = []
    for s in range(4):
        pref = mp.exp(mp.mpc(0, 1) * mp.pi * tau * mp.mpf(s * s) / FOUR)
        z_arg = mp.pi * tau * mp.mpf(s)
        j0 = mp.jtheta(3, z_arg, q2)
        j1 = mp.jtheta(3, z_arg, q2, derivative=1)
        val0 = pref * j0
        val_m = pref * (mp.mpc(0, -1) / TWO) * j1
        f0.append(val0)
        f_uv4.append(val_m + (mp.mpf(s) / FOUR) * val0)

    ve = mp.matrix(15, 1)
    vo = mp.matrix(15, 1)
    i_s15_4 = mp.mpc(0, 1) * mp.sqrt(mp.mpf(15)) / FOUR
    c15_8 = mp.mpf(15) / mp.mpf(8)
    two_pi_i_tau = mp.mpc(0, 2) * mp.pi * tau

    for j in range(15):
        se = mp.mpc(0)
        so = mp.mpc(0)
        for n in range(-Nv, Nv + 1):
            v = mp.mpf(n) - mp.mpf(j) / mp.mpf(15)
            s = (n + j) % 4
            qv = mp.exp(two_pi_i_tau * c15_8 * v * v)
            se += f0[s] * qv
            so += (f_uv4[s] + i_s15_4 * v * f0[s]) * qv
        ve[j, 0] = se
        vo[j, 0] = so
    return ve, vo


def v_odd_eval(lat: str, tau: mp.mpc, Nv: int = 22) -> mp.mpf:
    if lat == "Lp15":
        _, vo = theta_Lp15_completed_square(tau, Nv=Nv)
    else:
        N = int(lat[1:])
        _, vo, _ = theta_LN_completed_square(N, tau, Nv=Nv)
    y = mp.im(tau)
    return (y * y) * (mat_frob(vo) ** 2)


def golden_section_maximize(fn, a: mp.mpf, b: mp.mpf, tol: mp.mpf = mp.mpf("1e-7")) -> mp.mpf:
    """Golden-section maximization on [a, b] (disjoint from Newton)."""
    invphi = (mp.sqrt(FIVE) - ONE) / TWO
    invphi2 = (THREE - mp.sqrt(FIVE)) / TWO
    h = b - a
    c = a + invphi2 * h
    d = a + invphi * h
    fc = fn(c)
    fd = fn(d)
    while h > tol:
        if fc < fd:
            a = c
            c = d
            fc = fd
            h = invphi * h
            d = a + invphi * h
            fd = fn(d)
        else:
            b = d
            d = c
            fd = fc
            h = invphi * h
            c = a + invphi2 * h
            fc = fn(c)
    return (a + b) / TWO


def central_deriv_4pt(fn, t: mp.mpf, h: mp.mpf) -> mp.mpf:
    return (fn(t - TWO * h) - mp.mpf(8) * fn(t - h) + mp.mpf(8) * fn(t + h) - fn(t + TWO * h)) / (mp.mpf(12) * h)


def secant_root_dV_dy(lat: str, x_fixed: mp.mpf, y_init: mp.mpf) -> mp.mpf:
    """Secant root-finder on 4-point central dV/dy = 0 (disjoint from 3-point Newton)."""
    hd = mp.mpf("1e-9")

    def g(y: mp.mpf) -> mp.mpf:
        return central_deriv_4pt(lambda yy: v_odd_eval(lat, mp.mpc(x_fixed, yy), Nv=24), y, hd)

    y0 = y_init - mp.mpf("1e-5")
    y1 = y_init + mp.mpf("1e-5")
    g0 = g(y0)
    g1 = g(y1)
    for _ in range(25):
        if abs(g1) < mp.mpf("1e-36") or abs(y1 - y0) < mp.mpf("1e-36"):
            break
        denom = g1 - g0
        if abs(denom) < mp.mpf("1e-48"):
            break
        y2 = y1 - g1 * (y1 - y0) / denom
        y0, g0 = y1, g1
        y1, g1 = y2, g(y2)
    return y1


def richardson_5pt_grad_hessian(lat: str, x0: mp.mpf, y0: mp.mpf) -> Dict[str, mp.mpf]:
    """
    5-point central finite differences with Richardson extrapolation (h and h/2)
    for 2D gradient (V_x, V_y) and Hessian (V_xx, V_yy, V_xy).
    """
    h1 = mp.mpf("1e-5")
    h2 = h1 / TWO

    def f(dx: mp.mpf, dy: mp.mpf) -> mp.mpf:
        return v_odd_eval(lat, mp.mpc(x0 + dx, y0 + dy), Nv=24)

    f0 = f(ZERO, ZERO)

    def d1_5pt(axis: str, h: mp.mpf) -> mp.mpf:
        if axis == "x":
            vals = (f(-TWO * h, ZERO), f(-h, ZERO), f(h, ZERO), f(TWO * h, ZERO))
        else:
            vals = (f(ZERO, -TWO * h), f(ZERO, -h), f(ZERO, h), f(ZERO, TWO * h))
        return (vals[0] - mp.mpf(8) * vals[1] + mp.mpf(8) * vals[2] - vals[3]) / (mp.mpf(12) * h)

    def d2_5pt(axis: str, h: mp.mpf) -> mp.mpf:
        if axis == "x":
            vals = (f(-TWO * h, ZERO), f(-h, ZERO), f(h, ZERO), f(TWO * h, ZERO))
        else:
            vals = (f(ZERO, -TWO * h), f(ZERO, -h), f(ZERO, h), f(ZERO, TWO * h))
        return (-vals[0] + mp.mpf(16) * vals[1] - mp.mpf(30) * f0 + mp.mpf(16) * vals[2] - vals[3]) / (mp.mpf(12) * h * h)

    def dxy_central(h: mp.mpf) -> mp.mpf:
        return (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h)) / (FOUR * h * h)

    # Richardson O(h^4) -> O(h^6) for 5-point rules: (16 * D(h/2) - D(h)) / 15
    Vx = (mp.mpf(16) * d1_5pt("x", h2) - d1_5pt("x", h1)) / mp.mpf(15)
    Vy = (mp.mpf(16) * d1_5pt("y", h2) - d1_5pt("y", h1)) / mp.mpf(15)
    Vxx = (mp.mpf(16) * d2_5pt("x", h2) - d2_5pt("x", h1)) / mp.mpf(15)
    Vyy = (mp.mpf(16) * d2_5pt("y", h2) - d2_5pt("y", h1)) / mp.mpf(15)
    # For O(h^2) mixed derivative: (4 * D(h/2) - D(h)) / 3
    Vxy = (FOUR * dxy_central(h2) - dxy_central(h1)) / THREE
    return {"V": f0, "Vx": Vx, "Vy": Vy, "Vxx": Vxx, "Vyy": Vyy, "Vxy": Vxy}


def run_module_w3() -> Tuple[Dict[str, Any], mp.mpf, mp.mpf]:
    tau0 = mp.mpf(23) / mp.mpf(100) + mp.mpc(0, 1) * mp.mpf(137) / mp.mpf(100)
    omega_p = ONE / TWO + mp.mpc(0, 1) * mp.sqrt(THREE) / TWO
    tau_i = mp.mpc(0, 1)
    om = mp.exp(mp.mpc(0, 2) * mp.pi / THREE)

    equiv_results: Dict[str, Any] = {}
    locking_results: Dict[str, Any] = {}
    max_equiv_err = ZERO
    max_lock_leak = ZERO
    l3_odd_norm_max = ZERO
    max_ln_re_piece = ZERO

    lattice_specs = [
        ("L3", 3, 2),
        ("L7", 7, 4),
        ("L11", 11, 6),
        ("L15", 15, 8),
        ("L19", 19, 10),
        ("Lp15", 15, 4),
    ]

    for label, N, r_eff in lattice_specs:
        w = build_weil_position_mp(N, r_eff)
        L_m, S_m, C3_m = w["L"], w["S"], w["C3"]
        Ps = [(mp.eye(N) + (om ** (-q)) * C3_m + (om ** (-2 * q)) * C3_m * C3_m) / THREE for q in range(3)]

        def eval_both(tau: mp.mpc) -> Tuple[mp.matrix, mp.matrix]:
            nonlocal max_ln_re_piece
            if label == "Lp15":
                return theta_Lp15_completed_square(tau, Nv=24)
            ve, vo, rep = theta_LN_completed_square(N, tau, Nv=24)
            max_ln_re_piece = max(max_ln_re_piece, rep)
            return ve, vo

        ve0, vo0 = eval_both(tau0)
        veT, voT = eval_both(tau0 + ONE)
        veS, voS = eval_both(-ONE / tau0)

        eT = mat_frob(veT - L_m * ve0)
        eS = mat_frob(veS - tau0 * S_m * ve0)
        oT = mat_frob(voT - L_m * vo0)
        oS = mat_frob(voS - (tau0 * tau0) * S_m * vo0)
        max_equiv_err = max(max_equiv_err, eT, eS, oT, oS)
        equiv_results[label] = {
            "N": N, "r_eff": r_eff,
            "even_T_err": sci(eT), "even_S_err": sci(eS),
            "odd_T_err": sci(oT), "odd_S_err": sci(oS),
        }

        ve_om, vo_om = eval_both(omega_p)
        ne2 = mat_frob(ve_om) ** 2
        fe = [(mat_frob(P * ve_om) ** 2) / ne2 for P in Ps]
        leak_e = fe[0] + fe[1]
        max_lock_leak = max(max_lock_leak, leak_e)

        if label == "L3":
            l3_odd_norm_max = max(mat_frob(vo0), mat_frob(vo_om))
            locking_results[label] = {
                "even_weights_omega_plus": [fstr(x, 30) for x in fe],
                "even_leak": sci(leak_e),
                "odd_identically_zero_norm": sci(l3_odd_norm_max),
            }
        else:
            no2 = mat_frob(vo_om) ** 2
            fo = [(mat_frob(P * vo_om) ** 2) / no2 for P in Ps]
            leak_o = fo[0] + fo[2]
            max_lock_leak = max(max_lock_leak, leak_o)
            locking_results[label] = {
                "even_weights_omega_plus": [fstr(x, 30) for x in fe],
                "even_leak": sci(leak_e),
                "odd_weights_omega_plus": [fstr(x, 30) for x in fo],
                "odd_leak": sci(leak_o),
            }

    # Zero-parameter 2D modulus stabilization scan + golden-section + secant + 5-pt Richardson
    stab_results: Dict[str, Any] = {}
    stab_gates_ok = True
    l15_y_star = ZERO

    # Boundary-max lattices: L7, Lp15
    for label in ("L7", "Lp15"):
        V_om = v_odd_eval(label, omega_p, Nv=22)
        V_i = v_odd_eval(label, tau_i, Nv=22)
        # Coarse scan over fundamental domain x in {0, 1/8, 1/4, 3/8, 1/2}, y from boundary to 4
        max_interior_V = ZERO
        y0_om = mp.sqrt(THREE) / TWO
        for ix in range(5):
            xv = mp.mpf(ix) / mp.mpf(8)
            y_min = mp.sqrt(ONE - xv * xv)
            for iy in range(1, 25):
                yv = y_min + mp.mpf(iy) / mp.mpf(8)
                vv = v_odd_eval(label, mp.mpc(xv, yv), Nv=16)
                if vv > max_interior_V:
                    max_interior_V = vv
        # Check dV/dy < 0 moving up from omega_+ and i
        hd = mp.mpf("1e-6")
        dV_dy_om = (v_odd_eval(label, omega_p + mp.mpc(0, hd), Nv=22) - V_om) / hd
        dV_dy_i = (v_odd_eval(label, tau_i + mp.mpc(0, hd), Nv=22) - V_i) / hd
        bdry_ok = (V_om > V_i) and (V_om > max_interior_V) and (dV_dy_om < ZERO) and (dV_dy_i < ZERO)
        stab_gates_ok = stab_gates_ok and bdry_ok
        stab_results[label] = {
            "regime": "boundary_omega_plus",
            "V_omega_plus": fstr(V_om, 36),
            "V_i": fstr(V_i, 36),
            "max_interior_grid_V": fstr(max_interior_V, 36),
            "dV_dy_at_omega_plus": fstr(dV_dy_om, 24),
            "dV_dy_at_i": fstr(dV_dy_i, 24),
            "boundary_global_max_ok": bdry_ok,
        }

    # Strict 2D interior-max lattices: L11, L15, L19
    l15_y_half = ZERO
    for label in ("L11", "L15", "L19"):
        V_om = v_odd_eval(label, omega_p, Nv=22)
        V_i = v_odd_eval(label, tau_i, Nv=22)

        # Coarse scan along x = 0 (y in [1.0, 5.0]) and x = 1/2 (y in [sqrt(3)/2, 5.0]) — zero hardcoded target!
        def bracket_max_1d(x_val: mp.mpf, y_lo: mp.mpf, y_hi: mp.mpf, steps: int = 40) -> Tuple[mp.mpf, mp.mpf]:
            ys = [y_lo + (y_hi - y_lo) * mp.mpf(k) / mp.mpf(steps) for k in range(steps + 1)]
            vs = [v_odd_eval(label, mp.mpc(x_val, y), Nv=16) for y in ys]
            best = max(range(len(vs)), key=lambda idx: vs[idx])
            lo_idx = max(0, best - 1)
            hi_idx = min(steps, best + 1)
            return ys[lo_idx], ys[hi_idx]

        # x = 0 global interior max
        a0, b0 = bracket_max_1d(ZERO, ONE, FIVE, steps=40)
        y0_gs = golden_section_maximize(lambda yy: v_odd_eval(label, mp.mpc(ZERO, yy), Nv=20), a0, b0)
        y_star = secant_root_dV_dy(label, ZERO, y0_gs)
        h_star = richardson_5pt_grad_hessian(label, ZERO, y_star)

        # x = 1/2 saddle
        a5, b5 = bracket_max_1d(ONE / TWO, mp.sqrt(THREE) / TWO, FIVE, steps=40)
        y5_gs = golden_section_maximize(lambda yy: v_odd_eval(label, mp.mpc(ONE / TWO, yy), Nv=20), a5, b5)
        y_half = secant_root_dV_dy(label, ONE / TWO, y5_gs)
        h_half = richardson_5pt_grad_hessian(label, ONE / TWO, y_half)

        if label == "L15":
            l15_y_star = y_star
            l15_y_half = y_half

        ok_max = (
            y_star > ONE
            and abs(h_star["Vx"]) < TOL_GRAD
            and abs(h_star["Vy"]) < TOL_GRAD
            and abs(h_star["Vxy"]) < TOL_GRAD
            and h_star["Vyy"] < ZERO
            and h_star["Vxx"] < ZERO
            and h_star["V"] > V_om
            and h_star["V"] > V_i
            and h_star["V"] > h_half["V"]
        )
        ok_sad = (
            y_half > mp.sqrt(THREE) / TWO
            and abs(h_half["Vx"]) < TOL_GRAD
            and abs(h_half["Vy"]) < TOL_GRAD
            and abs(h_half["Vxy"]) < TOL_GRAD
            and h_half["Vyy"] < ZERO
            and h_half["Vxx"] > ZERO
        )
        stab_gates_ok = stab_gates_ok and ok_max and ok_sad

        stab_results[label] = {
            "regime": "strict_2d_interior_max_x0",
            "V_omega_plus": fstr(V_om, 36),
            "V_i": fstr(V_i, 36),
            "x0_max": {
                "y_star": fstr(y_star, 36),
                "V_star": fstr(h_star["V"], 36),
                "Vx": sci(h_star["Vx"]),
                "Vy": sci(h_star["Vy"]),
                "Vxx": fstr(h_star["Vxx"], 30),
                "Vyy": fstr(h_star["Vyy"], 30),
                "Vxy": sci(h_star["Vxy"]),
                "strict_2d_max_ok": ok_max,
            },
            "xhalf_saddle": {
                "y_half": fstr(y_half, 36),
                "V_half": fstr(h_half["V"], 36),
                "Vx": sci(h_half["Vx"]),
                "Vy": sci(h_half["Vy"]),
                "Vxx": fstr(h_half["Vxx"], 30),
                "Vyy": fstr(h_half["Vyy"], 30),
                "Vxy": sci(h_half["Vxy"]),
                "strict_saddle_ok": ok_sad,
            },
        }

    passed = (
        max_equiv_err < TOL_GATE_30
        and max_lock_leak < TOL_GATE_30
        and l3_odd_norm_max < TOL_GATE_30
        and max_ln_re_piece < TOL_GATE_30
        and stab_gates_ok
    )

    return (
        {
            "sl2z_equivariance": equiv_results,
            "max_sl2z_equiv_err": sci(max_equiv_err),
            "max_ln_re_piece_vanishing": sci(max_ln_re_piece),
            "l3_odd_vanishing_norm": sci(l3_odd_norm_max),
            "omega_plus_locking": locking_results,
            "max_omega_plus_leak": sci(max_lock_leak),
            "stabilization": stab_results,
            "all_stabilization_gates_ok": stab_gates_ok,
            "passed": passed,
        },
        l15_y_star,
        l15_y_half,
    )


# ---------------------------------------------------------------------------
# MODULE W4 — SymPy Q[[q^{1/15}]] Identities, 8x8 Jordan-Wielandt SVD, Haar
# ---------------------------------------------------------------------------
def sympy_l15_qseries_identities(max_deg: int = 60) -> Dict[str, Any]:
    """
    Prove exact Q[[q^{1/15}]] identities through t^60 (t = q^{1/15}) using SymPy Poly:
      A*D + B*C == 0
      B*theta_{A2,0} - D*theta_{A2,1} == 0
      A*theta_{A2,0} + C*theta_{A2,1} == 0
    """
    t = sp.Symbol("t")

    def l15_odd_poly(j: int) -> sp.Poly:
        coeffs: Dict[int, sp.Rational] = {}
        # 15 * (15/4) * v^2 = V^2 / 4 <= max_deg -> |V| <= 2*sqrt(max_deg)
        v_lim = int(math.isqrt(4 * max_deg)) + 2
        n_lim = v_lim // 15 + 2
        m_lim = int(math.isqrt(max_deg)) + 4
        for n in range(-n_lim, n_lim + 1):
            V = 15 * n - j
            if V * V > 4 * max_deg:
                continue
            for m in range(-m_lim, m_lim + 1):
                U = 15 * m + 8 * j
                num = U * U + U * V + 4 * V * V
                assert num % 15 == 0
                exp = num // 15
                if exp <= max_deg:
                    coeffs[exp] = coeffs.get(exp, sp.Rational(0)) + sp.Rational(V, 15)
        expr = sum(c * (t ** e) for e, c in coeffs.items() if c != 0)
        return sp.Poly(expr, t, domain="QQ")

    def a2_even_poly(j: int) -> sp.Poly:
        coeffs: Dict[int, int] = {}
        # 15 * (3/4) * (V/3)^2 = 5 * V^2 / 4 <= max_deg
        v_lim = int(math.isqrt(4 * max_deg // 5)) + 2
        n_lim = v_lim // 3 + 2
        m_lim = int(math.isqrt(max_deg)) + 4
        for n in range(-n_lim, n_lim + 1):
            V = 3 * n - j
            if 5 * V * V > 4 * max_deg:
                continue
            for m in range(-m_lim, m_lim + 1):
                U = 3 * m + 2 * j
                num = U * U + U * V + V * V
                assert num % 3 == 0
                exp = (num // 3) * 5
                if exp <= max_deg:
                    coeffs[exp] = coeffs.get(exp, 0) + 1
        expr = sum(c * (t ** e) for e, c in coeffs.items() if c != 0)
        return sp.Poly(expr, t, domain="QQ")

    def trunc_poly(p: sp.Poly, deg: int) -> sp.Poly:
        expr = sum(c * (t ** k[0]) for k, c in p.as_dict().items() if k[0] <= deg)
        return sp.Poly(expr, t, domain="QQ")

    ser = {j: l15_odd_poly(j) for j in range(15)}
    A = ser[6]
    B = ser[3]
    C = ser[1] - ser[4]
    D = ser[7] + ser[2]
    th_a2_0 = a2_even_poly(0)
    th_a2_1 = a2_even_poly(1)

    id1 = trunc_poly(A * D + B * C, max_deg)
    id2 = trunc_poly(B * th_a2_0 - D * th_a2_1, max_deg)
    id3 = trunc_poly(A * th_a2_0 + C * th_a2_1, max_deg)

    # Also verify nontriviality (A, B, C, D, th_a2_0, th_a2_1 are all nonzero polynomials)
    nontrivial = all(not p.is_zero for p in (A, B, C, D, th_a2_0, th_a2_1))
    return {
        "max_degree_t": max_deg,
        "nontrivial_series": nontrivial,
        "AD_plus_BC_zero": id1.is_zero,
        "B_a20_minus_D_a21_zero": id2.is_zero,
        "A_a20_plus_C_a21_zero": id3.is_zero,
        "A_terms_count": len(A.as_dict()),
        "B_terms_count": len(B.as_dict()),
        "C_terms_count": len(C.as_dict()),
        "D_terms_count": len(D.as_dict()),
        "passed": nontrivial and id1.is_zero and id2.is_zero and id3.is_zero,
        "_polys": (A, B, C, D, th_a2_0, th_a2_1),
    }


def svd_via_jordan_wielandt_8x8(M: mp.matrix) -> Tuple[List[mp.mpf], mp.matrix]:
    """
    Non-squaring SVD of a 3 x 5 complex matrix M via the 8 x 8 Hermitian
    Jordan-Wielandt block H_JW = [[0, M], [M^H, 0]].
    Returns (singular_values_desc [s1, s2, s3], U_left 3x3 unitary).
    """
    assert M.rows == 3 and M.cols == 5
    H = mp.zeros(8, 8)
    for r in range(3):
        for c in range(5):
            H[r, 3 + c] = M[r, c]
            H[3 + c, r] = mp.conj(M[r, c])
    eigs, vecs = mp.eigh(H)
    # Sort eigenvalues descending; top 3 non-negative are singular values (if full rank 3)
    order = sorted(range(8), key=lambda i: mp.re(eigs[i]), reverse=True)
    # Extract top 3 eigenvalues (clamping tiny negative noise near 0 to 0 only for display, keep raw abs)
    svs: List[mp.mpf] = []
    u_cols: List[mp.matrix] = []
    rank_tol = mp.mpf("1e-25")

    for k in range(3):
        idx = order[k]
        ev = mp.re(eigs[idx])
        sv = ev if ev > ZERO else ZERO
        svs.append(sv)
        if sv > rank_tol:
            u = mp.matrix(3, 1)
            for r in range(3):
                u[r, 0] = vecs[r, idx]
            # Orthogonalize against previous u_cols for full 50-digit accuracy
            for prev in u_cols:
                ip = (prev.H * u)[0, 0]
                u = u - ip * prev
            nu = mat_frob(u)
            u = u / nu
            u_cols.append(u)

    # Complete orthonormal basis of C^3 if rank < 3 (via exact complex cross product for rank 2)
    if len(u_cols) == 2:
        a, b = u_cols[0], u_cols[1]
        # Cross product conjugated so a^H c == 0 and b^H c == 0
        c = mp.matrix(3, 1)
        c[0, 0] = mp.conj(a[1, 0] * b[2, 0] - a[2, 0] * b[1, 0])
        c[1, 0] = mp.conj(a[2, 0] * b[0, 0] - a[0, 0] * b[2, 0])
        c[2, 0] = mp.conj(a[0, 0] * b[1, 0] - a[1, 0] * b[0, 0])
        for prev in u_cols:
            c = c - (prev.H * c)[0, 0] * prev
        c = c / mat_frob(c)
        u_cols.append(c)
    else:
        for e_i in range(3):
            if len(u_cols) == 3:
                break
            v = mp.zeros(3, 1)
            v[e_i, 0] = ONE
            for prev in u_cols:
                v = v - (prev.H * v)[0, 0] * prev
            nv = mat_frob(v)
            if nv > mp.mpf("1e-10"):
                u_cols.append(v / nv)

    U = mp.zeros(3, 3)
    for j in range(3):
        for i in range(3):
            U[i, j] = u_cols[j][i, 0]
    return svs, U


def reshape_crt_3x5(vec15: mp.matrix) -> mp.matrix:
    M = mp.zeros(3, 5)
    for j in range(15):
        M[j % 3, j % 5] = vec15[j, 0]
    return M


def mixing_and_jarlskog(Ue: mp.matrix, Uo: mp.matrix) -> Tuple[mp.matrix, mp.mpf]:
    V = Ue.H * Uo
    absV = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            absV[i, j] = abs(V[i, j])
    J = mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0]))
    return absV, J


class LCG128:
    """Deterministic 128-bit LCG (pure integer, zero external RNG dependency)."""

    MOD = 1 << 128
    MULT = 47026247687942121848144207491837523525
    INC = 117397592171526113268558934119004209487

    def __init__(self, seed: int) -> None:
        self.state = seed % self.MOD

    def next_u64(self) -> int:
        self.state = (self.MULT * self.state + self.INC) % self.MOD
        return self.state >> 64

    def next_unit(self) -> mp.mpf:
        # Strict (0, 1) uniform at 50-digit resolution using two 64-bit limbs
        hi = self.next_u64()
        lo = self.next_u64()
        num = (hi << 64) | lo
        return (mp.mpf(num) + ONE) / (mp.mpf(1 << 128) + TWO)

    def next_normal(self) -> Tuple[mp.mpf, mp.mpf]:
        u1 = self.next_unit()
        u2 = self.next_unit()
        r = mp.sqrt(-TWO * mp.log(u1))
        th = TWO * mp.pi * u2
        return r * mp.cos(th), r * mp.sin(th)


def haar_unitary_householder(n: int, rng: LCG128) -> mp.matrix:
    """
    Sample exact Haar-measure U(n) via complex Ginibre matrix + Householder-reflection QR
    with diagonal phase normalization (Mezzadri 2007, disjoint from Gram-Schmidt/Cayley).
    """
    A = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            re_g, im_g = rng.next_normal()
            A[i, j] = mp.mpc(re_g, im_g)

    R = A.copy()
    Q = mp.eye(n)
    for k in range(n):
        m = n - k
        x = mp.matrix(m, 1)
        for i in range(m):
            x[i, 0] = R[k + i, k]
        nx = mat_frob(x)
        if nx == ZERO:
            continue
        x0 = x[0, 0]
        phase = ONE if abs(x0) == ZERO else x0 / abs(x0)
        v = x.copy()
        v[0, 0] += phase * nx
        nv = mat_frob(v)
        if nv == ZERO:
            continue
        v = v / nv
        # Apply Householder reflection H = I - 2 v v^H to R[k:, k:] on left and Q[:, k:] on right
        # R_sub = R[k:, k:]
        for col in range(k, n):
            ip = mp.mpc(0)
            for i in range(m):
                ip += mp.conj(v[i, 0]) * R[k + i, col]
            for i in range(m):
                R[k + i, col] -= TWO * v[i, 0] * ip
        for row in range(n):
            ip = mp.mpc(0)
            for i in range(m):
                ip += Q[row, k + i] * v[i, 0]
            for i in range(m):
                Q[row, k + i] -= TWO * ip * mp.conj(v[i, 0])

    # Normalize diagonal phases of R to positive real so Q is strictly Haar-distributed
    for k in range(n):
        rk = R[k, k]
        d = ONE if abs(rk) == ZERO else rk / abs(rk)
        for row in range(n):
            Q[row, k] *= d
    return Q


def run_module_w4(l15_y_star: mp.mpf) -> Dict[str, Any]:
    qser = sympy_l15_qseries_identities(max_deg=60)
    qser_out = {k: v for k, v in qser.items() if k != "_polys"}

    tau0 = mp.mpf(23) / mp.mpf(100) + mp.mpc(0, 1) * mp.mpf(137) / mp.mpf(100)
    tau_star = mp.mpc(ZERO, l15_y_star)
    eval_points = [
        ("tau0", tau0),
        ("tau0_plus_1", tau0 + ONE),
        ("neg_inv_tau0", -ONE / tau0),
        ("tau_star_L15", tau_star),
    ]

    # Verify L'_15 swap isometry j -> -4j == (-1, +1) = P_flip^(3)
    ve_lp0, vo_lp0 = theta_Lp15_completed_square(tau0, Nv=24)
    swap_even_err = ZERO
    for j in range(15):
        swap_even_err = max(swap_even_err, abs(ve_lp0[(-4 * j) % 15, 0] - ve_lp0[j, 0]))
    swap_mod3_ok = ((-4) % 3 == 2)
    swap_mod5_ok = ((-4) % 5 == 1)

    # Check H_3^odd (x) H_5^odd block of M_even for L'_15 vanishes identically
    M_lp_e0 = reshape_crt_3x5(ve_lp0)
    inv_s2 = ONE / mp.sqrt(TWO)
    u3_odd = mp.matrix([[ZERO], [inv_s2], [-inv_s2]])
    # H_5^odd basis columns: (|1>-|4>)/sqrt(2), (|2>-|3>)/sqrt(2)
    B5_odd = mp.zeros(5, 2)
    B5_odd[1, 0] = inv_s2
    B5_odd[4, 0] = -inv_s2
    B5_odd[2, 1] = inv_s2
    B5_odd[3, 1] = -inv_s2
    lp15_odd_odd_block_norm = mat_frob(u3_odd.H * M_lp_e0 * B5_odd)

    Pflip3 = mp.matrix([[ONE, ZERO, ZERO], [ZERO, ZERO, ONE], [ZERO, ONE, ZERO]])

    genus_out: Dict[str, Any] = {}
    all_rank_duality_ok = True
    max_sl2z_sv_ratio_err = ZERO
    max_sl2z_mix_err = ZERO
    max_pflip3_comm_err = ZERO
    max_jarlskog = ZERO
    max_block_leak = ZERO
    max_haar_sv_err = ZERO
    max_haar_mix_err = ZERO
    max_haar_unitary_err = ZERO

    rng = LCG128(202611270003)

    for lat in ("L15", "Lp15"):
        pts_rec: Dict[str, Any] = {}
        ref_ratios_e: List[mp.mpf] = []
        ref_ratios_o: List[mp.mpf] = []
        ref_absV = mp.zeros(3, 3)

        for pt_name, tau in eval_points:
            if lat == "L15":
                ve, vo, _ = theta_LN_completed_square(15, tau, Nv=24)
            else:
                ve, vo = theta_Lp15_completed_square(tau, Nv=24)
            Me = reshape_crt_3x5(ve)
            Mo = reshape_crt_3x5(vo)

            # Check P_flip^(3) commutation with Me Me^H and Mo Mo^H
            Ge = Me * Me.H
            Go = Mo * Mo.H
            c_e = mat_frob(Pflip3 * Ge - Ge * Pflip3)
            c_o = mat_frob(Pflip3 * Go - Go * Pflip3)
            max_pflip3_comm_err = max(max_pflip3_comm_err, c_e, c_o)

            sv_e, Ue = svd_via_jordan_wielandt_8x8(Me)
            sv_o, Uo = svd_via_jordan_wielandt_8x8(Mo)
            ratios_e = [sv_e[1] / sv_e[0], sv_e[2] / sv_e[0]]
            ratios_o = [sv_o[1] / sv_o[0], sv_o[2] / sv_o[0]]
            absV, J = mixing_and_jarlskog(Ue, Uo)
            max_jarlskog = max(max_jarlskog, abs(J))

            # Verify Genus Rank-2 Duality
            if lat == "L15":
                rk_ok = (ratios_e[1] > mp.mpf("1e-2")) and (ratios_o[1] < TOL_GATE_30)
            else:
                rk_ok = (ratios_o[1] > mp.mpf("1e-2")) and (ratios_e[1] < TOL_GATE_30)
            all_rank_duality_ok = all_rank_duality_ok and rk_ok

            # Verify 2 + 1 block-diagonal structure: identify the unique odd P_flip^(3) index in Ue and Uo
            e_odd_idx = max(range(3), key=lambda j: abs((u3_odd.H * Ue)[0, j]))
            o_odd_idx = max(range(3), key=lambda j: abs((u3_odd.H * Uo)[0, j]))
            leak_2p1 = abs(absV[e_odd_idx, o_odd_idx] - ONE)
            for j in range(3):
                if j != o_odd_idx:
                    leak_2p1 = max(leak_2p1, absV[e_odd_idx, j])
            for i in range(3):
                if i != e_odd_idx:
                    leak_2p1 = max(leak_2p1, absV[i, o_odd_idx])
            max_block_leak = max(max_block_leak, leak_2p1)

            if pt_name == "tau0":
                ref_ratios_e = ratios_e
                ref_ratios_o = ratios_o
                ref_absV = absV
            elif pt_name in ("tau0_plus_1", "neg_inv_tau0"):
                err_re = max(abs(a - b) for a, b in zip(ratios_e, ref_ratios_e))
                err_ro = max(abs(a - b) for a, b in zip(ratios_o, ref_ratios_o))
                err_mv = mat_frob(absV - ref_absV)
                max_sl2z_sv_ratio_err = max(max_sl2z_sv_ratio_err, err_re, err_ro)
                max_sl2z_mix_err = max(max_sl2z_mix_err, err_mv)

            pts_rec[pt_name] = {
                "sv_even": [fstr(x, 34) for x in sv_e],
                "sv_odd": [fstr(x, 34) for x in sv_o],
                "sv_ratios_even": [fstr(x, 34) for x in ratios_e],
                "sv_ratios_odd": [fstr(x, 34) for x in ratios_o],
                "abs_V_3x3": [[fstr(absV[i, j], 30) for j in range(3)] for i in range(3)],
                "jarlskog_J": sci(abs(J)),
                "pflip3_comm_even_err": sci(c_e),
                "pflip3_comm_odd_err": sci(c_o),
                "odd_mode_pair": [e_odd_idx, o_odd_idx],
                "block_2plus1_leak": sci(leak_2p1),
                "rank_duality_ok": rk_ok,
            }

        # Guardrail 3: 10-trial independent LCG128 Householder Haar U(3) x U(5) scrambling at tau0
        if lat == "L15":
            ve0, vo0, _ = theta_LN_completed_square(15, tau0, Nv=24)
        else:
            ve0, vo0 = theta_Lp15_completed_square(tau0, Nv=24)
        Me0 = reshape_crt_3x5(ve0)
        Mo0 = reshape_crt_3x5(vo0)
        sv_e0, Ue0 = svd_via_jordan_wielandt_8x8(Me0)
        sv_o0, Uo0 = svd_via_jordan_wielandt_8x8(Mo0)
        absV0, _ = mixing_and_jarlskog(Ue0, Uo0)

        lat_haar_sv_err = ZERO
        lat_haar_mix_err = ZERO
        for _trial in range(10):
            U3 = haar_unitary_householder(3, rng)
            U5e = haar_unitary_householder(5, rng)
            U5o = haar_unitary_householder(5, rng)
            max_haar_unitary_err = max(
                max_haar_unitary_err,
                mat_frob(U3.H * U3 - mp.eye(3)),
                mat_frob(U5e.H * U5e - mp.eye(5)),
                mat_frob(U5o.H * U5o - mp.eye(5)),
            )
            Me_t = U3 * Me0 * U5e.H
            Mo_t = U3 * Mo0 * U5o.H
            sve_t, Ue_t = svd_via_jordan_wielandt_8x8(Me_t)
            svo_t, Uo_t = svd_via_jordan_wielandt_8x8(Mo_t)
            absV_t, J_t = mixing_and_jarlskog(Ue_t, Uo_t)
            e_sv = max(
                max(abs(a - b) for a, b in zip(sve_t, sv_e0)),
                max(abs(a - b) for a, b in zip(svo_t, sv_o0)),
            )
            e_mx = max(mat_frob(absV_t - absV0), abs(J_t))
            lat_haar_sv_err = max(lat_haar_sv_err, e_sv)
            lat_haar_mix_err = max(lat_haar_mix_err, e_mx)

        max_haar_sv_err = max(max_haar_sv_err, lat_haar_sv_err)
        max_haar_mix_err = max(max_haar_mix_err, lat_haar_mix_err)

        genus_out[lat] = {
            "points": pts_rec,
            "haar_10trials_max_sv_err": sci(lat_haar_sv_err),
            "haar_10trials_max_mix_err": sci(lat_haar_mix_err),
        }

    passed = (
        qser["passed"]
        and swap_mod3_ok
        and swap_mod5_ok
        and swap_even_err < TOL_GATE_30
        and lp15_odd_odd_block_norm < TOL_GATE_30
        and all_rank_duality_ok
        and max_sl2z_sv_ratio_err < TOL_GATE_28
        and max_sl2z_mix_err < TOL_GATE_28
        and max_pflip3_comm_err < TOL_GATE_30
        and max_jarlskog < TOL_GATE_28
        and max_block_leak < TOL_GATE_28
        and max_haar_unitary_err < TOL_GATE_30
        and max_haar_sv_err < TOL_GATE_28
        and max_haar_mix_err < TOL_GATE_28
    )

    return {
        "l15_qseries_identities": qser_out,
        "lp15_swap_isometry": {
            "minus4_mod3_eq_minus1": swap_mod3_ok,
            "minus4_mod5_eq_plus1": swap_mod5_ok,
            "even_swap_invariance_err": sci(swap_even_err),
            "h3_odd_x_h5_odd_block_norm": sci(lp15_odd_odd_block_norm),
        },
        "genus_crt_svd": genus_out,
        "all_rank_duality_ok": all_rank_duality_ok,
        "max_sl2z_sv_ratio_err": sci(max_sl2z_sv_ratio_err),
        "max_sl2z_mix_err": sci(max_sl2z_mix_err),
        "max_pflip3_comm_err": sci(max_pflip3_comm_err),
        "max_jarlskog": sci(max_jarlskog),
        "max_block_2plus1_leak": sci(max_block_leak),
        "haar_10trials_unitary_err": sci(max_haar_unitary_err),
        "haar_10trials_max_sv_err": sci(max_haar_sv_err),
        "haar_10trials_max_mix_err": sci(max_haar_mix_err),
        "passed": passed,
        "_qser_polys": qser["_polys"],
    }


# ---------------------------------------------------------------------------
# 5 Independent Referee Planted Fault Controls (RPF1..RPF5)
# ---------------------------------------------------------------------------
def run_planted_fault_controls(l15_y_half: mp.mpf, qser_polys: Tuple[Any, ...]) -> Dict[str, Any]:
    # RPF1 (W1): wrong r=2 trace tested against r=1 formula at N=15 + false mirror claim on N=35
    _, L15_2, S15_2, _ = build_weil_momentum_kernels(15, 2)
    tr_wrong = mp.mpc(0)
    for p in range(15):
        for q in range(15):
            tr_wrong += mp.conj(S15_2[q, p]) * mp.conj(L15_2[p, q])
    rpf1_tr_err = abs(tr_wrong - expected_tr_c3_mp(15, 1))
    # Also test N=35 has NO solution to a^2 == -1 mod 35
    rpf1_n35_has_root = any((a * a + 1) % 35 == 0 for a in range(35))
    rpf1_detected = (rpf1_tr_err > ONE) and (not rpf1_n35_has_root)

    # RPF2 (W2): perturb omega_+ by 1/100 in R_5^wp AND test faulty v1 G_3 character (3,3,2,3) mod 6
    leg = build_leg5_via_12rays()
    rho_leg = leg["rho_leg"]
    B_leg = leg["B_leg"]
    rays = leg["rays"]
    S_leg = rho_leg(((0, 4), (1, 0)))
    L_mat = ((1, 1), (0, 1))
    # Quick K5 via L conjugates
    def mul2(A, B):
        return (
            ((A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 5, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 5),
            ((A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 5, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 5),
        )
    def inv2(A):
        return ((A[1][1] % 5, (-A[0][1]) % 5), ((-A[1][0]) % 5, A[0][0] % 5))
    def canon(A):
        B = (((-A[0][0]) % 5, (-A[0][1]) % 5), ((-A[1][0]) % 5, (-A[1][1]) % 5))
        return A if A < B else B
    psl = {canon(((a, b), (c, d))) for a in range(5) for b in range(5) for c in range(5) for d in range(5) if (a * d - b * c) % 5 == 1}
    K5 = mp.zeros(6, 6)
    for g in {canon(mul2(mul2(x, L_mat), inv2(x))) for x in psl}:
        K5 += rho_leg(g)
    lam_a = TWO + TWO * mp.sqrt(FIVE)
    lam_b = TWO - TWO * mp.sqrt(FIVE)
    Pa = (K5 - lam_b * mp.eye(6)) / (lam_a - lam_b)
    Pb = (lam_a * mp.eye(6) - K5) / (lam_a - lam_b)

    tau_pert = ONE / TWO + mp.mpc(0, 1) * (mp.sqrt(THREE) / TWO + ONE / mp.mpf(100))
    q_p = mp.exp(mp.mpc(0, 1) * mp.pi * tau_pert)
    v12 = mp.matrix(12, 1)
    for j, (rx, ry) in enumerate(rays):
        u = mp.pi * (mp.mpf(rx) * tau_pert + mp.mpf(ry)) / FIVE
        t0 = mp.jtheta(1, u, q_p, derivative=0)
        t1 = mp.jtheta(1, u, q_p, derivative=1)
        t2 = mp.jtheta(1, u, q_p, derivative=2)
        v12[j, 0] = -(mp.pi * mp.pi) * (t2 * t0 - t1 * t1) / (t0 * t0)
    vp = S_leg * (B_leg.H * v12)
    r_pert = (mat_frob(Pb * vp) ** 2) / (mat_frob(Pa * vp) ** 2)
    rpf2_wp_err = abs(r_pert - ONE / FOUR)

    # Faulty v1 character (L->3, R->3 mod 6) violates homomorphism on G_3 since L*R^{-1} = C^-1? Check BFS defects!
    def L_tr(s): x, y, z = s; return (x % 27, z % 27, (x * z - y) % 27)
    def R_tr(s): x, y, z = s; return (z % 27, y % 27, (y * z - x) % 27)
    def C_tr(s): x, y, z = s; return (y % 27, z % 27, x % 27)
    def Sig_tr(s): x, y, z = s; return (y % 27, x % 27, (x * y - z) % 27)
    orb = {(3, 3, 3)}
    dq = deque([(3, 3, 3)])
    while dq:
        u = dq.popleft()
        for fn in (C_tr, Sig_tr):
            v = fn(u)
            if v not in orb:
                orb.add(v)
                dq.append(v)
    sts = sorted(orb)
    idx_s = {s: i for i, s in enumerate(sts)}
    pL = tuple(idx_s[L_tr(s)] for s in sts)
    pR = tuple(idx_s[R_tr(s)] for s in sts)
    pC = tuple(idx_s[C_tr(s)] for s in sts)
    pSig = tuple(idx_s[Sig_tr(s)] for s in sts)
    def comp(a, b): return tuple(a[b[i]] for i in range(len(a)))
    id_p = tuple(range(len(sts)))
    bad_map = {id_p: 0}
    gq = deque([id_p])
    bad_defects = 0
    while gq:
        g = gq.popleft()
        rg = bad_map[g]
        for h, rh in ((pL, 3), (pR, 3), (pC, 2), (pSig, 3)):
            gh = comp(h, g)
            rgh = (rg + rh) % 6
            if gh not in bad_map:
                bad_map[gh] = rgh
                gq.append(gh)
            elif bad_map[gh] != rgh:
                bad_defects += 1
    rpf2_detected = (rpf2_wp_err > mp.mpf("1e-5")) and (bad_defects > 0)

    # RPF3 (W3): wrong equianharmonic point omega_- = -1/2 + i*sqrt(3)/2 fails q=1 locking on L_15
    omega_minus = -ONE / TWO + mp.mpc(0, 1) * mp.sqrt(THREE) / TWO
    _, vo_wrong, _ = theta_LN_completed_square(15, omega_minus, Nv=22)
    w15 = build_weil_position_mp(15, 8)
    om = mp.exp(mp.mpc(0, 2) * mp.pi / THREE)
    P1 = (mp.eye(15) + mp.conj(om) * w15["C3"] + om * w15["C3"] * w15["C3"]) / THREE
    q1_frac_wrong = (mat_frob(P1 * vo_wrong) ** 2) / (mat_frob(vo_wrong) ** 2)
    rpf3_leak = abs(ONE - q1_frac_wrong)
    # Also saddle at x = 1/2 fails concavity V_xx < 0
    h_sad_check = richardson_5pt_grad_hessian("L15", ONE / TWO, l15_y_half)
    rpf3_detected = (rpf3_leak > mp.mpf("1e-2")) and (h_sad_check["Vxx"] > ZERO)

    # RPF4 (W4): wrong sign A*D - B*C != 0 AND swap-breaking perturbation ruins rank-2 of L'_15 M_even
    A, B, C, D, _, _ = qser_polys
    t_sym = A.gen
    bad_id = sp.Poly(
        sum(c * (t_sym ** k[0]) for k, c in (A * D - B * C).as_dict().items() if k[0] <= 60),
        t_sym,
        domain="QQ",
    )
    tau0 = mp.mpf(23) / mp.mpf(100) + mp.mpc(0, 1) * mp.mpf(137) / mp.mpf(100)
    ve_lp, _ = theta_Lp15_completed_square(tau0, Nv=22)
    ve_lp_pert = ve_lp.copy()
    ve_lp_pert[1, 0] += mp.mpf("1e-5")
    sv_pert, _ = svd_via_jordan_wielandt_8x8(reshape_crt_3x5(ve_lp_pert))
    rpf4_sv3_ratio = sv_pert[2] / sv_pert[0]
    rpf4_detected = (not bad_id.is_zero) and (rpf4_sv3_ratio > mp.mpf("1e-7"))

    # RPF5 (Guardrail 3): unphysical different left unitaries U3_e != U3_o break |V_{3x3}| while keeping SVs invariant
    rng = LCG128(999888777666)
    U3_e = haar_unitary_householder(3, rng)
    U3_o = haar_unitary_householder(3, rng)
    U5 = haar_unitary_householder(5, rng)
    ve15, vo15, _ = theta_LN_completed_square(15, tau0, Nv=22)
    Me = reshape_crt_3x5(ve15)
    Mo = reshape_crt_3x5(vo15)
    sve0, Ue0 = svd_via_jordan_wielandt_8x8(Me)
    _, Uo0 = svd_via_jordan_wielandt_8x8(Mo)
    absV0, _ = mixing_and_jarlskog(Ue0, Uo0)
    sve1, Ue1 = svd_via_jordan_wielandt_8x8(U3_e * Me * U5.H)
    _, Uo1 = svd_via_jordan_wielandt_8x8(U3_o * Mo * U5.H)
    absV1, _ = mixing_and_jarlskog(Ue1, Uo1)
    rpf5_sv_err = max(abs(a - b) for a, b in zip(sve0, sve1))
    rpf5_mix_shift = mat_frob(absV1 - absV0)
    rpf5_detected = (rpf5_sv_err < TOL_GATE_30) and (rpf5_mix_shift > mp.mpf("1e-2"))

    controls = {
        "RPF1_w1_wrong_r_and_n35_mirror": {
            "tr_err": sci(rpf1_tr_err),
            "n35_has_sqrt_minus1": rpf1_n35_has_root,
            "detected": rpf1_detected,
        },
        "RPF2_w2_wp_pert_and_v1_char_defect": {
            "wp_ratio_err": sci(rpf2_wp_err),
            "v1_char_hom_defects": bad_defects,
            "detected": rpf2_detected,
        },
        "RPF3_w3_wrong_omega_and_saddle_vxx": {
            "omega_minus_q1_leak": sci(rpf3_leak),
            "xhalf_Vxx": fstr(h_sad_check["Vxx"], 20),
            "detected": rpf3_detected,
        },
        "RPF4_w4_wrong_sign_qseries_and_swap_break": {
            "AD_minus_BC_is_zero": bad_id.is_zero,
            "perturbed_lp15_sv3_ratio": sci(rpf4_sv3_ratio),
            "detected": rpf4_detected,
        },
        "RPF5_guardrail3_gauge_breaking_left_unitary": {
            "sv_invariance_err": sci(rpf5_sv_err),
            "mix_shift_detected": sci(rpf5_mix_shift),
            "detected": rpf5_detected,
        },
    }
    n_det = sum(1 for v in controls.values() if v["detected"])
    return {
        "controls": controls,
        "detected_count": n_det,
        "total_count": len(controls),
        "passed": n_det == 5,
    }


# ---------------------------------------------------------------------------
# Main Entrypoint
# ---------------------------------------------------------------------------
def main() -> int:
    script_path = Path(__file__).resolve()
    hygiene = run_static_hygiene_audit(script_path)

    w1 = run_module_w1()
    w2 = run_module_w2()
    w3, l15_y_star, l15_y_half = run_module_w3()
    w4_full = run_module_w4(l15_y_star)
    qser_polys = w4_full.pop("_qser_polys")
    rpf = run_planted_fault_controls(l15_y_half, qser_polys)

    all_passed = (
        hygiene["passed"]
        and w1["passed"]
        and w2["passed"]
        and w3["passed"]
        and w4_full["passed"]
        and rpf["passed"]
    )

    payload: Dict[str, Any] = {
        "card_id": "A2-WEIL-CHIRAL-LATTICE-BRIDGE",
        "seat_code": "fam3-v1-high-03",
        "role": "blind_cold_room_zero_trust_referee",
        "blindness": "0_of_19",
        "mpmath_dps": int(mp.mp.dps),
        "script_sha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
        "hygiene": hygiene,
        "W1": w1,
        "W2": w2,
        "W3": w3,
        "W4": w4_full,
        "planted_fault_controls": rpf,
        "json_float_literal_count": 0,
        "all_referee_gates_passed": all_passed,
    }

    n_json_floats = count_json_floats(payload)
    payload["json_float_literal_count"] = n_json_floats
    if n_json_floats != 0:
        payload["all_referee_gates_passed"] = False
        all_passed = False

    OUT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print("REFEREE CARD: A2-WEIL-CHIRAL-LATTICE-BRIDGE (seat fam3-v1-high-03, 0 of 19)")
    print(f"HYGIENE : passed={hygiene['passed']} ast_floats={hygiene['ast_float_literal_count']} json_floats={n_json_floats} t7b_clean={hygiene['t7b_part1_clean']}")
    print(f"W1      : passed={w1['passed']} pairs={w1['pairs_checked_count']} max_tr_err={w1['max_tr_c3_err']} max_flip_err={w1['max_flip_trace_err']} mod4_mismatches={w1['mod4_mismatches']} max_crt_err={w1['max_crt_err']}")
    print(f"W2      : passed={w2['passed']} leg5_spec_err={w2['leg5']['spec_err']} wp_om_err={w2['phi_wp']['err_from_1_4']} wp_i_err={w2['phi_wp']['err_from_7_23']} sg_R_om={w2['phi_siegel']['R5_omega_plus'][:14]} g3={w2['chiral_freezing']['g3_order']} defect_mm={w2['chiral_freezing']['char_defect_mismatches']} max_o27_q6={w2['chiral_freezing']['max_o27_q6_diff_0_4']}")
    print(f"W3      : passed={w3['passed']} max_equiv={w3['max_sl2z_equiv_err']} max_lock_leak={w3['max_omega_plus_leak']} L15_y_star={w3['stabilization']['L15']['x0_max']['y_star'][:14]} stab_ok={w3['all_stabilization_gates_ok']}")
    print(f"W4      : passed={w4_full['passed']} qser_ok={w4_full['l15_qseries_identities']['passed']} rank_duality={w4_full['all_rank_duality_ok']} max_J={w4_full['max_jarlskog']} haar_sv={w4_full['haar_10trials_max_sv_err']} haar_mix={w4_full['haar_10trials_max_mix_err']}")
    print(f"CONTROLS: passed={rpf['passed']} detected={rpf['detected_count']}/{rpf['total_count']}")
    print(f"OVERALL : all_referee_gates_passed={all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
