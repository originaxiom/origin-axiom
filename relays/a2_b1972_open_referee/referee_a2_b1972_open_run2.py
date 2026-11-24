#!/usr/bin/env python3
"""
Disjoint Cold-Room Zero-Trust Referee (run2) for Card A2-B1972-OPEN (branch agy-002/verify).

Frozen v1 (referee_a2_b1972_open.py @ 14242bc56 -> a2c393de3) is preserved untouched.
Fixes in run2 (strictly referee-side bookkeeping/convention defects uncovered by v1):
  1. Include stdlib compiler directive '__future__' in ALLOWED_SANDBOX_MODULES.
  2. Compute both W-D2 decoupled 1st-gen split lnD1_r12 = |ln((m1/m2)_lp / (m1/m2)_dn)|
     and lnD1_r13 = |ln((m1/m3)_lp / (m1/m3)_dn)|; break exact s <-> -s symmetry ties
     (|lnD1(+s) - lnD1(-s)| <= 1e-12) canonically by larger min_diag_V, and cross-check
     Producer v3 both on scan optima and directly at Producer v3's exact (k_label, phi).
  3. Cache mp.psi(0, a_mp) by (dps, a_r) for fast exact evaluation (identical math).

Strict rules:
- Empirical firewall: 0 of 19 (zero empirical SM / PDG / NuFIT / Planck / DESI / CODATA numbers).
- Zero shared code with Producer v3, agy C13, chat1 W-D2, or main B1971.
- Depends ONLY on Python stdlib, sympy, and mpmath (zero subprocesses, zero network).
- Zero Python float/complex AST literals, zero float()/complex() casts, zero JSON float tokens.
- Zero literal-flag proofs: every boolean verdict is computed directly from algebraic or numerical checks.
"""

import ast
import hashlib
import json
import math
import pathlib
import re
from collections import deque
from fractions import Fraction

import mpmath as mp
import sympy as sp


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
RELAYS_DIR = REPO_ROOT / "relays"
REFEREE_DIR = pathlib.Path(__file__).resolve().parent
PROD_V3_DIR = RELAYS_DIR / "a2_b1972_open_v3"
OUT_JSON_PATH = REFEREE_DIR / "referee_a2_b1972_open_run2_results.json"


# ---------------------------------------------------------------------------
# Pure zero-float / zero-complex helpers
# ---------------------------------------------------------------------------

def im_unit():
    return mp.mpc(0, 1)


def mp_frac(fr):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def nearest_int(fr):
    """Exact nearest integer for Fraction fr (when 2*fr is not an odd integer)."""
    return (2 * fr.numerator + fr.denominator) // (2 * fr.denominator)


def frac_mod1(fr):
    """Exact reduction of Fraction fr to [0, 1)."""
    return Fraction(fr.numerator % fr.denominator, fr.denominator)


def dist_to_Z(fr):
    r = frac_mod1(fr)
    c = Fraction(1, 1) - r
    return r if r <= c else c


def is_integer_frac(fr):
    return (fr.numerator % fr.denominator) == 0


def nstr_mp(val, digits=14):
    return mp.nstr(val, digits)


def parse_mp_str(s):
    return mp.mpf(str(s))


def rel_or_abs_diff(a_mp, b_mp):
    denom = max(abs(a_mp), abs(b_mp), mp.mpf(1))
    return abs(a_mp - b_mp) / denom


def rel_diff(a_mp, b_mp):
    denom = max(abs(a_mp), abs(b_mp), mp.power(10, -80))
    return abs(a_mp - b_mp) / denom


# ---------------------------------------------------------------------------
# AST & JSON Hygiene Auditor
# ---------------------------------------------------------------------------

ALLOWED_SANDBOX_MODULES = {
    "__future__", "ast", "collections", "copy", "datetime", "decimal", "fractions",
    "functools", "hashlib", "itertools", "json", "math", "mpmath",
    "operator", "pathlib", "re", "statistics", "string", "sympy", "sys",
    "time", "typing",
}

BANNED_CALL_MODULES = {
    "subprocess", "urllib", "http", "socket", "requests", "shutil", "ctypes",
}


def audit_python_ast(py_path):
    src = py_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(py_path))
    float_lines = []
    complex_lines = []
    banned_casts = []
    imports = set()
    banned_calls = []
    io_calls = []

    self_file_vars = {"__file__"}
    for _ in range(3):
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                rhs_src = ast.unparse(node.value) if hasattr(ast, "unparse") else ""
                mentions_self = any(v in rhs_src for v in self_file_vars)
                modifies_path = any(tok in rhs_src for tok in (".parent", "with_name", "dirname", "/"))
                if mentions_self and not modifies_path:
                    for tgt in node.targets:
                        if isinstance(tgt, ast.Name):
                            self_file_vars.add(tgt.id)

    func_param_call_args = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_param_call_args[node.name] = {
                "params": [a.arg for a in node.args.args],
                "calls": [],
            }
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            fname = node.func.id
            if fname in func_param_call_args:
                arg_srcs = [ast.unparse(a) if hasattr(ast, "unparse") else "" for a in node.args]
                func_param_call_args[fname]["calls"].append(arg_srcs)

    parent_func = {}

    def _walk_func(node, cur_fn):
        parent_func[id(node)] = cur_fn
        next_fn = node.name if isinstance(node, ast.FunctionDef) else cur_fn
        for child in ast.iter_child_nodes(node):
            _walk_func(child, next_fn)

    _walk_func(tree, None)

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            val = node.value
            if isinstance(val, float):
                float_lines.append(node.lineno)
            elif isinstance(val, complex):
                complex_lines.append(node.lineno)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            fn = node.func
            fn_name = None
            full_name = None
            if isinstance(fn, ast.Name):
                fn_name = fn.id
                full_name = fn.id
            elif isinstance(fn, ast.Attribute):
                fn_name = fn.attr
                if isinstance(fn.value, ast.Name):
                    full_name = fn.value.id + "." + fn.attr
                else:
                    full_name = fn.attr
            if fn_name in ("float", "complex"):
                banned_casts.append({"line": node.lineno, "call": full_name})
            if full_name in ("os.system", "os.popen", "eval", "exec", "__import__"):
                banned_calls.append({"line": node.lineno, "call": full_name})
            if fn_name in ("open", "read_text", "read_bytes", "write_text", "write_bytes"):
                arg_repr = [ast.unparse(a) for a in node.args[:2]] if hasattr(ast, "unparse") else []
                kw_repr = {kw.arg: ast.unparse(kw.value) for kw in node.keywords} if hasattr(ast, "unparse") else {}
                target_repr = ast.unparse(fn.value) if (isinstance(fn, ast.Attribute) and hasattr(ast, "unparse")) else ""
                is_write = fn_name in ("write_text", "write_bytes")
                if fn_name == "open":
                    mode_str = kw_repr.get("mode", arg_repr[1] if len(arg_repr) >= 2 else "'r'")
                    is_write = any(ch in mode_str for ch in ("w", "a", "x"))
                is_self_read = False
                if not is_write:
                    path_expr = arg_repr[0] if fn_name == "open" and len(arg_repr) >= 1 else target_repr
                    if any(v in path_expr for v in self_file_vars):
                        is_self_read = True
                    else:
                        enc = parent_func.get(id(node))
                        if enc and enc in func_param_call_args:
                            params = func_param_call_args[enc]["params"]
                            calls = func_param_call_args[enc]["calls"]
                            if path_expr in params and len(calls) > 0:
                                p_idx = params.index(path_expr)
                                if all(
                                    len(c_args) > p_idx and any(v in c_args[p_idx] for v in self_file_vars)
                                    for c_args in calls
                                ):
                                    is_self_read = True
                io_calls.append({
                    "line": node.lineno,
                    "call": fn_name,
                    "kind": "write" if is_write else "read",
                    "is_self_read": is_self_read,
                    "target": target_repr,
                    "args": arg_repr,
                })

    external_read_calls = [c for c in io_calls if c["kind"] == "read" and not c["is_self_read"]]
    disallowed_imports = sorted(imports - ALLOWED_SANDBOX_MODULES)
    banned_mod_imports = sorted(imports & BANNED_CALL_MODULES)
    return {
        "path": str(py_path.relative_to(REPO_ROOT)),
        "float_literal_lines": sorted(set(float_lines)),
        "complex_literal_lines": sorted(set(complex_lines)),
        "banned_cast_calls": banned_casts,
        "imports": sorted(imports),
        "disallowed_imports": disallowed_imports,
        "banned_module_imports": banned_mod_imports,
        "banned_calls": banned_calls,
        "io_calls": io_calls,
        "external_read_calls": external_read_calls,
        "ast_zero_float_clean": (
            len(float_lines) == 0
            and len(complex_lines) == 0
            and len(banned_casts) == 0
        ),
        "sandbox_no_subprocess_or_net": (
            len(banned_mod_imports) == 0
            and len(banned_calls) == 0
        ),
    }


def check_json_zero_floats(json_path):
    raw = json_path.read_text(encoding="utf-8")
    float_tokens = []

    def _catch_float(tok):
        float_tokens.append(tok)
        return tok

    data = json.loads(raw, parse_float=_catch_float)
    return data, float_tokens


def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Disjoint Theta / Eta / Kronecker / Frame C Primitives (via mp.jtheta)
# ---------------------------------------------------------------------------

_PSI_CACHE = {}


def cached_digamma_frac(a_fr):
    key = (mp.mp.dps, a_fr.numerator, a_fr.denominator)
    val = _PSI_CACHE.get(key)
    if val is None:
        val = mp.psi(0, mp_frac(a_fr))
        _PSI_CACHE[key] = val
    return val


def q_nome(tau):
    return mp.exp(im_unit() * mp.pi * tau)


def dedekind_eta(tau):
    q2 = mp.exp(2 * im_unit() * mp.pi * tau)
    return mp.exp(im_unit() * mp.pi * tau / 12) * mp.qp(q2)


def theta2_jtheta(tau):
    q = q_nome(tau)
    return mp.exp(im_unit() * mp.pi * tau / 4) * mp.jtheta(3, mp.pi * tau / 2, q)


def theta3_jtheta(tau):
    return mp.jtheta(3, 0, q_nome(tau))


def theta4_jtheta(tau):
    return mp.jtheta(4, 0, q_nome(tau))


def thc_jtheta(a_fr, b_fr, tau):
    half = Fraction(1, 2)
    if is_integer_frac(a_fr - half) and is_integer_frac(b_fr - half):
        return mp.mpc(0, 0)
    k = nearest_int(a_fr)
    a_r = a_fr - k
    l = nearest_int(b_fr)
    b_r = b_fr - l
    a_mp = mp_frac(a_r)
    b_mp = mp_frac(b_r)
    q = q_nome(tau)
    phase_arg = im_unit() * mp.pi * (a_mp * a_mp * tau + 2 * a_mp * b_mp + 2 * a_mp * mp.mpf(l))
    z = mp.pi * (a_mp * tau + b_mp)
    return mp.exp(phase_arg) * mp.jtheta(3, z, q)


def shifted_kronecker_Fu(alpha_fr, beta_fr, tau):
    a_r = frac_mod1(alpha_fr)
    b_r = frac_mod1(beta_fr)
    if a_r == 0 and b_r == 0:
        raise ValueError("Shifted Kronecker limit singular at (0, 0)")
    x = mp.re(tau)
    y = mp.im(tau)
    a_mp = mp_frac(a_r)
    b_mp = mp_frac(b_r)

    if a_r == 0:
        zero_mode = (
            y * (mp.pi ** 2) / (mp.sin(mp.pi * b_mp) ** 2)
            + mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(y))
        )
    else:
        zero_mode = mp.pi * (
            -cached_digamma_frac(a_r) - cached_digamma_frac(Fraction(1, 1) - a_r) - 2 * mp.log(2) - mp.log(y)
        )

    m_bound = int(mp.ceil((mp.mp.dps + 15) * mp.log(10) / (2 * mp.pi * y))) + 4
    fourier_sum = mp.mpf(0)
    two_pi = 2 * mp.pi
    for m in range(-m_bound, m_bound + 1):
        if a_r == 0 and m == 0:
            continue
        v = mp.mpf(m) + a_mp
        av = abs(v)
        w = mp.exp(two_pi * im_unit() * (b_mp + v * x) - two_pi * av * y)
        fourier_sum += (two_pi / av) * mp.re(w / (1 - w))
    return zero_mode + fourier_sum


def kronecker_a0(alpha_fr, beta_fr, tau):
    a_r = frac_mod1(alpha_fr)
    b_r = frac_mod1(beta_fr)
    if a_r > Fraction(1, 2):
        a_r = a_r - 1
    a_mp = mp_frac(a_r)
    b_mp = mp_frac(b_r)
    q = q_nome(tau)
    z = mp.pi * (a_mp * tau + b_mp)
    return 2 * im_unit() * mp.pi * a_mp + mp.pi * mp.jtheta(1, z, q, 1) / mp.jtheta(1, z, q)


def L2_cusp_limit():
    return mp.pi + mp.log(mp.pi) - 3 * mp.log(2)


def channel_norm_T90(c0_fr, c1_fr, tau, L2_val=None):
    if L2_val is None:
        L2_val = L2_cusp_limit()
    half = Fraction(1, 2)
    alpha_fr = frac_mod1(c0_fr - half)
    beta_fr = frac_mod1(c1_fr - half)
    y = mp.im(tau)
    Fu = shifted_kronecker_Fu(alpha_fr, beta_fr, tau)
    c_s = Fu + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    a0 = kronecker_a0(alpha_fr, beta_fr, tau)
    return 2 * mp.pi * L2_val + c_s - mp.pi * (abs(a0) ** 2) * mp.exp(-2 * L2_val)


def higgs_triplet_c_and_h(tau):
    t2 = theta2_jtheta(tau)
    t3 = theta3_jtheta(tau)
    t4 = theta4_jtheta(tau)
    eta = dedekind_eta(tau)
    denom = 24 * (eta ** 3)
    c0 = -(t2 ** 2) * (t3 ** 4 + t4 ** 4) / denom
    c1 = (t4 ** 2) * (t2 ** 4 + t3 ** 4) / denom
    minus_i_c2 = (t3 ** 2) * (t2 ** 4 - t4 ** 4) / denom
    c2 = im_unit() * minus_i_c2
    h = [c1, c0, c2]
    return [c0, c1, c2], h, eta


def spinor_matrices_mp():
    I_u = im_unit()
    I2 = mp.matrix([[1, 0], [0, 1]])
    QI = mp.matrix([[I_u, 0], [0, -I_u]])
    QJ = mp.matrix([[0, 1], [-1, 0]])
    QK = mp.matrix([[0, I_u], [I_u, 0]])
    eps = QJ
    C_blocks = [QJ, QI, QK]
    half = mp.mpf(1) / 2
    E_dual = {
        "1": half * mp.matrix([[0, 1], [-1, 0]]),
        "i": half * mp.matrix([[0, I_u], [I_u, 0]]),
        "j": half * mp.matrix([[-1, 0], [0, -1]]),
        "k": half * mp.matrix([[-I_u, 0], [0, I_u]]),
    }
    return I2, QI, QJ, QK, eps, C_blocks, E_dual


SECTOR_CHARGES = {
    "up": (1, -4),
    "down": (1, 2),
    "lep": (-3, 6),
}


def frame_c_channel_data(sector, a_fr, b_fr, tau, L2_val=None):
    qL, qR = SECTOR_CHARGES[sector]
    x0 = qL * a_fr
    y0 = qR * a_fr
    a_plus = x0 + y0
    a_minus = x0 - y0
    b_plus = (qL + qR) * b_fr
    b_minus = (qL - qR) * b_fr
    half = Fraction(1, 2)

    e_fac = mp.exp(-2 * im_unit() * mp.pi * mp_frac(x0))
    kappa_map = {
        "1": -im_unit() * e_fac,
        "i": mp.mpc(-1, 0),
        "j": -e_fac,
        "k": im_unit(),
    }
    chars = {
        "1": ((a_plus + half, b_plus + half), (a_minus + half, b_minus + half)),
        "i": ((a_plus + half, b_plus), (a_minus + half, b_minus)),
        "j": ((a_plus, b_plus + half), (a_minus, b_minus + half)),
        "k": ((a_plus, b_plus), (a_minus, b_minus)),
    }

    eta = dedekind_eta(tau)
    denom = 2 * mp.pi * (eta ** 3)
    R_s = {}
    N_s = {}
    u_s = {}
    for ch in ("1", "i", "j", "k"):
        (c0, c1), (d0, d1) = chars[ch]
        is_odd_c = is_integer_frac(c0 - half) and is_integer_frac(c1 - half)
        is_odd_d = is_integer_frac(d0 - half) and is_integer_frac(d1 - half)
        if is_odd_c or is_odd_d:
            R_s[ch] = mp.mpc(0, 0)
            N_s[ch] = mp.mpf(0)
            u_s[ch] = mp.mpc(0, 0)
        else:
            tc = thc_jtheta(c0, c1, tau)
            td = thc_jtheta(d0, d1, tau)
            rv = kappa_map[ch] * tc * td / denom
            nv = channel_norm_T90(c0, c1, tau, L2_val=L2_val)
            R_s[ch] = rv
            N_s[ch] = nv
            u_s[ch] = mp.sqrt(nv) * rv

    _, _, _, _, _, _, E_dual = spinor_matrices_mp()
    M_mat = mp.zeros(2, 2)
    for ch in ("1", "i", "j", "k"):
        M_mat += u_s[ch] * E_dual[ch]

    u_vec = [u_s["j"], u_s["i"], u_s["k"]]
    w_val = -u_s["1"]
    return {
        "R_s": R_s,
        "N_s": N_s,
        "u_s": u_s,
        "M": M_mat,
        "u": u_vec,
        "w": w_val,
    }


def direct_spinor_yukawa_mp(h_vec, s_val, M_mat):
    I2, QI, QJ, QK, eps, C_blocks, _ = spinor_matrices_mp()
    H_mat = h_vec[0] * QJ + h_vec[1] * QI + h_vec[2] * QK + s_val * I2
    Y = mp.zeros(3, 3)
    for a in range(3):
        CaT_eps_H = C_blocks[a].T * eps * H_mat
        for b in range(3):
            K_ab = CaT_eps_H * C_blocks[b]
            acc = mp.mpc(0, 0)
            for m in range(2):
                for n in range(2):
                    acc += K_ab[m, n] * M_mat[m, n]
            Y[a, b] = acc
    return Y


def svd_ascending(Y):
    U, S, V = mp.svd_c(Y)
    order = sorted([0, 1, 2], key=lambda idx: S[idx])
    s_sorted = [S[i] for i in order]
    U_sorted = mp.zeros(3, 3)
    for new_col, old_col in enumerate(order):
        for row in range(3):
            U_sorted[row, new_col] = U[row, old_col]
    return U_sorted, s_sorted


def null_basis_mp():
    inv_rt2 = mp.mpf(1) / mp.sqrt(2)
    I_u = im_unit()
    return mp.matrix([
        [inv_rt2, inv_rt2, 0],
        [0, 0, 1],
        [I_u * inv_rt2, -I_u * inv_rt2, 0],
    ])


def vec_null_coords(v):
    U_null = null_basis_mp()
    vm = mp.matrix([[v[0]], [v[1]], [v[2]]])
    c = U_null.H * vm
    return [c[0, 0], c[1, 0], c[2, 0]]


def ckm_and_observables(U_up, s_up, U_dn, s_dn, s_lp=None):
    V = U_up.H * U_dn
    absV = [[abs(V[i, j]) for j in range(3)] for i in range(3)]
    min_diag = min(absV[0][0], absV[1][1], absV[2][2])
    J_val = abs(mp.im(V[0, 0] * V[1, 1] * mp.conj(V[0, 1]) * mp.conj(V[1, 0])))
    r23_up = s_up[1] / s_up[2]
    r13_up = s_up[0] / s_up[2]
    r12_up = s_up[0] / s_up[1]
    r23_dn = s_dn[1] / s_dn[2]
    r13_dn = s_dn[0] / s_dn[2]
    r12_dn = s_dn[0] / s_dn[1]
    out = {
        "V": V,
        "absV": absV,
        "min_diag": min_diag,
        "J": J_val,
        "r23_up": r23_up,
        "r13_up": r13_up,
        "r12_up": r12_up,
        "r23_dn": r23_dn,
        "r13_dn": r13_dn,
        "r12_dn": r12_dn,
    }
    if s_lp is not None:
        r23_lp = s_lp[1] / s_lp[2]
        r13_lp = s_lp[0] / s_lp[2]
        r12_lp = s_lp[0] / s_lp[1]
        out["r23_lp"] = r23_lp
        out["r13_lp"] = r13_lp
        out["r12_lp"] = r12_lp
        # W-D2 §3-4 decoupled 1st-gen split D1 = (m1/m2)_lp / (m1/m2)_dn and 2nd-gen split D2 = (m2/m3)_lp / (m2/m3)_dn
        out["lnD1_r12"] = abs(mp.log(r12_lp / r12_dn))
        out["lnD1_r13"] = abs(mp.log(r13_lp / r13_dn))
        out["lnD2"] = abs(mp.log(r23_lp / r23_dn))
    return out


# ---------------------------------------------------------------------------
# MODULE R_OPEN_1
# ---------------------------------------------------------------------------

def run_R_OPEN_1():
    edges_e8 = [(0, 2), (2, 3), (1, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
    A = [[2 if i == j else 0 for j in range(8)] for i in range(8)]
    for u, v in edges_e8:
        A[u][v] = -1
        A[v][u] = -1

    det_A = int(sp.Matrix(A).det())

    def bil(v1, v2):
        total = 0
        for i in range(8):
            vi = v1[i]
            if vi == 0:
                continue
            row = A[i]
            for j in range(8):
                if v2[j] != 0 and row[j] != 0:
                    total += vi * row[j] * v2[j]
        return total

    def reflect(v, idx):
        ip = sum(A[idx][j] * v[j] for j in range(8))
        if ip == 0:
            return v
        lst = list(v)
        lst[idx] -= ip
        return tuple(lst)

    simple_roots = [tuple(1 if j == i else 0 for j in range(8)) for i in range(8)]
    roots_set = set(simple_roots)
    q = deque(simple_roots)
    while q:
        r = q.popleft()
        for i in range(8):
            nr = reflect(r, i)
            if nr not in roots_set:
                roots_set.add(nr)
                q.append(nr)

    all_norms_2 = all(bil(r, r) == 2 for r in roots_set)
    pos_roots = [r for r in roots_set if sum(r) > 0]
    neg_roots = [r for r in roots_set if sum(r) < 0]
    highest_root = max(pos_roots, key=lambda r: sum(r))
    alpha0 = tuple(-c for c in highest_root)

    aff_roots = [alpha0] + simple_roots
    A_aff = [[bil(aff_roots[i], aff_roots[j]) for j in range(9)] for i in range(9)]
    null_basis = sp.Matrix(A_aff).nullspace()
    kac_vec_raw = null_basis[0]
    lcm_den = 1
    for entry in kac_vec_raw:
        lcm_den = math.lcm(lcm_den, int(sp.fraction(entry)[1]))
    kac_marks = [int(entry * lcm_den) for entry in kac_vec_raw]
    if kac_marks[0] < 0:
        kac_marks = [-x for x in kac_marks]

    deletion_catalog = {}
    e6_a2_nodes = []
    for d in range(9):
        kept = [i for i in range(9) if i != d]
        adj = {i: [] for i in kept}
        for i in kept:
            for j in kept:
                if i != j and A_aff[i][j] == -1:
                    adj[i].append(j)
        visited = set()
        comps = []
        for node in kept:
            if node in visited:
                continue
            comp = []
            dq = deque([node])
            visited.add(node)
            while dq:
                cur = dq.popleft()
                comp.append(cur)
                for nb in adj[cur]:
                    if nb not in visited:
                        visited.add(nb)
                        dq.append(nb)
            comp.sort()
            sub_mat = sp.Matrix([[A_aff[i][j] for j in comp] for i in comp])
            deg_seq = sorted([len(adj[i]) for i in comp])
            comps.append({
                "nodes": comp,
                "size": len(comp),
                "det": int(sub_mat.det()),
                "deg_seq": deg_seq,
            })
        comps.sort(key=lambda c: (-c["size"], c["det"]))
        deletion_catalog[str(d)] = comps
        if (
            len(comps) == 2
            and comps[0]["size"] == 6 and comps[0]["det"] == 3 and comps[0]["deg_seq"] == [1, 1, 1, 2, 2, 3]
            and comps[1]["size"] == 2 and comps[1]["det"] == 3 and comps[1]["deg_seq"] == [1, 1]
        ):
            e6_a2_nodes.append(d)

    unique_del_node = e6_a2_nodes[0] if len(e6_a2_nodes) == 1 else -1
    del_simple_idx = unique_del_node - 1
    e6_nodes = deletion_catalog[str(unique_del_node)][0]["nodes"]
    a2_nodes = deletion_catalog[str(unique_del_node)][1]["nodes"]
    e6_roots_basis = [aff_roots[i] for i in e6_nodes]
    a2_roots_basis = [aff_roots[i] for i in a2_nodes]

    g0 = [r for r in roots_set if (r[del_simple_idx] % 3) == 0]
    g1 = [r for r in roots_set if (r[del_simple_idx] % 3) == 1]
    g2 = [r for r in roots_set if (r[del_simple_idx] % 3) == 2]

    e6_sub_roots = [r for r in g0 if all(bil(r, b) == 0 for b in a2_roots_basis)]
    a2_sub_roots = [r for r in g0 if all(bil(r, b) == 0 for b in e6_roots_basis)]
    dim_78 = len(e6_sub_roots) + len(e6_nodes)
    dim_8 = len(a2_sub_roots) + len(a2_nodes)
    dim_81_a = len(g1)
    dim_81_b = len(g2)

    d5_nodes = [1, 2, 3, 4, 5]
    A_sp = sp.Matrix(A)
    eq_rows = []
    rhs = []
    for n_idx in d5_nodes + a2_nodes:
        rv = sp.Matrix(aff_roots[n_idx])
        eq_rows.append(list((rv.T * A_sp)))
        rhs.append(0)
    rv6 = sp.Matrix(aff_roots[6])
    eq_rows.append(list((rv6.T * A_sp)))
    rhs.append(1)
    q_psi = sp.Matrix(eq_rows).LUsolve(sp.Matrix(rhs))
    q_psi_A = list(q_psi.T * A_sp)

    def dot_q(qA_vec, r):
        acc = sp.Rational(0)
        for i in range(8):
            if r[i] != 0:
                acc += qA_vec[i] * r[i]
        return acc

    psi_buckets = {}
    for r in g1:
        val = dot_q(q_psi_A, r)
        psi_buckets.setdefault(val, []).append(r)
    spin10_split_sizes = sorted([len(v) for v in psi_buckets.values()], reverse=True)

    psi_16 = [k for k, v in psi_buckets.items() if len(v) == 48][0]
    psi_10 = [k for k, v in psi_buckets.items() if len(v) == 30][0]

    def a2_weight(r):
        return tuple(bil(r, b) for b in a2_roots_basis)

    def e6_weight(r):
        return tuple(bil(r, b) for b in e6_roots_basis)

    a2_weights_list = sorted(set(a2_weight(r) for r in g1))
    fam_index = {w: idx for idx, w in enumerate(a2_weights_list)}

    g1_set = set(g1)
    same_family_couplings = 0
    ordered_10_16_16 = []
    for r1 in g1:
        f1 = fam_index[a2_weight(r1)]
        for r2 in g1:
            r3 = tuple(-(r1[i] + r2[i]) for i in range(8))
            if r3 in g1_set:
                f2 = fam_index[a2_weight(r2)]
                f3 = fam_index[a2_weight(r3)]
                if len({f1, f2, f3}) < 3:
                    same_family_couplings += 1
                if (
                    f1 == 0 and f2 == 1 and f3 == 2
                    and dot_q(q_psi_A, r1) == psi_10
                    and dot_q(q_psi_A, r2) == psi_16
                    and dot_q(q_psi_A, r3) == psi_16
                ):
                    ordered_10_16_16.append((r1, r2, r3))

    su5_idx = [0, 2, 3, 4]
    A_su5 = sp.Matrix([[A[i][j] for j in su5_idx] for i in su5_idx])
    y_su5 = A_su5.LUsolve(sp.Matrix([0, 0, 1, 0]))
    q_Y_raw = [sp.Rational(0)] * 8
    for pos, idx in enumerate(su5_idx):
        q_Y_raw[idx] = y_su5[pos]
    q_Y_A_raw = list(sp.Matrix(q_Y_raw).T * A_sp)

    sm_step_roots = [simple_roots[0], simple_roots[2], simple_roots[4]]
    g1_f0 = [r for r in g1 if fam_index[a2_weight(r)] == 0]

    def sm_multiplets(root_subset):
        sub_set = set(root_subset)
        seen = set()
        comps = []
        for r in root_subset:
            if r in seen:
                continue
            comp = []
            dq = deque([r])
            seen.add(r)
            while dq:
                cur = dq.popleft()
                comp.append(cur)
                for sr in sm_step_roots:
                    for sgn in (1, -1):
                        nxt = tuple(cur[i] + sgn * sr[i] for i in range(8))
                        if nxt in sub_set and nxt not in seen:
                            seen.add(nxt)
                            dq.append(nxt)
            comps.append(comp)
        return comps

    mults_16 = sm_multiplets([r for r in g1_f0 if dot_q(q_psi_A, r) == psi_16])
    mults_10 = sm_multiplets([r for r in g1_f0 if dot_q(q_psi_A, r) == psi_10])

    Q_mult = [m for m in mults_16 if len(m) == 6][0]
    raw_Y_Q = dot_q(q_Y_A_raw, Q_mult[0])
    scale_6Y = sp.Rational(1) / raw_Y_Q
    q_6Y_A = [v * scale_6Y for v in q_Y_A_raw]

    label_by_e6w = {}
    sm_16_inventory = {}
    for comp in mults_16:
        sz = len(comp)
        y6_vals = set(dot_q(q_6Y_A, r) for r in comp)
        assert len(y6_vals) == 1
        y6 = int(next(iter(y6_vals)))
        lbl = {
            (6, 1): "Q", (3, -4): "u_c", (3, 2): "d_c",
            (2, -3): "L", (1, 6): "e_c", (1, 0): "nu_c",
        }.get((sz, y6), "UNK_16_%d_%d" % (sz, y6))
        sm_16_inventory[lbl] = {"dim": sz, "6Y": y6}
        for r in comp:
            label_by_e6w[e6_weight(r)] = lbl

    sm_10_inventory = {}
    for comp in mults_10:
        sz = len(comp)
        y6_vals = set(dot_q(q_6Y_A, r) for r in comp)
        assert len(y6_vals) == 1
        y6 = int(next(iter(y6_vals)))
        lbl = {
            (2, 3): "H_u", (2, -3): "H_d", (3, -2): "T", (3, 2): "Tbar",
        }.get((sz, y6), "UNK_10_%d_%d" % (sz, y6))
        sm_10_inventory[lbl] = {"dim": sz, "6Y": y6}
        for r in comp:
            label_by_e6w[e6_weight(r)] = lbl

    unordered_couplings = set()
    for rH, ra, rb in ordered_10_16_16:
        wH = e6_weight(rH)
        wa = e6_weight(ra)
        wb = e6_weight(rb)
        pair = (wa, wb) if wa <= wb else (wb, wa)
        unordered_couplings.add((wH, pair))

    ew_counts = {"Q_uc_Hu": 0, "Q_dc_Hd": 0, "L_ec_Hd": 0, "L_nuc_Hu": 0}
    triplet_counts = {}
    kawamura_killed = 0
    ew_kept_total = 0
    for wH, (wa, wb) in unordered_couplings:
        lH = label_by_e6w[wH]
        la = label_by_e6w[wa]
        lb = label_by_e6w[wb]
        pair_set = tuple(sorted([la, lb]))
        if lH in ("T", "Tbar"):
            kawamura_killed += 1
            key = "%s_%s_%s" % (pair_set[0], pair_set[1], lH)
            triplet_counts[key] = triplet_counts.get(key, 0) + 1
        elif lH in ("H_u", "H_d"):
            ew_kept_total += 1
            if pair_set == ("Q", "u_c") and lH == "H_u":
                ew_counts["Q_uc_Hu"] += 1
            elif pair_set == ("Q", "d_c") and lH == "H_d":
                ew_counts["Q_dc_Hd"] += 1
            elif pair_set == ("L", "e_c") and lH == "H_d":
                ew_counts["L_ec_Hd"] += 1
            elif pair_set == ("L", "nu_c") and lH == "H_u":
                ew_counts["L_nuc_Hu"] += 1

    e8_ok = (
        det_A == 1
        and len(roots_set) == 240
        and all_norms_2
        and len(pos_roots) == 120
        and len(neg_roots) == 120
        and list(highest_root) == [2, 3, 4, 6, 5, 4, 3, 2]
        and kac_marks == [1, 2, 3, 4, 6, 5, 4, 3, 2]
        and e6_a2_nodes == [7]
        and dim_78 == 78 and dim_8 == 8 and dim_81_a == 81 and dim_81_b == 81
        and (dim_78 + dim_8 + dim_81_a + dim_81_b) == 248
        and spin10_split_sizes == [48, 30, 3]
        and same_family_couplings == 0
        and len(ordered_10_16_16) == 80
        and len(unordered_couplings) == 40
        and kawamura_killed == 24
        and ew_kept_total == 16
        and ew_counts == {"Q_uc_Hu": 6, "Q_dc_Hd": 6, "L_ec_Hd": 2, "L_nuc_Hu": 2}
    )

    with mp.workdps(75):
        I_u = im_unit()
        test_taus = [
            mp.mpc(mp.mpf(13) / 100, mp.mpf(7) / 5),
            mp.mpc(mp.mpf(-3) / 10, mp.mpf(11) / 5),
            mp.mpc(mp.mpf(3) / 7, mp.mpf(11) / 10),
        ]

        def eta_times_r(z):
            t2 = theta2_jtheta(z)
            t3 = theta3_jtheta(z)
            t4 = theta4_jtheta(z)
            et = dedekind_eta(z)
            fac = 2 * (et ** 2)
            return [-(t2 ** 2) / fac, -(t4 ** 2) / fac, I_u * (t3 ** 2) / fac]

        R_rad = mp.mpf(1) / 20
        N_pts = 64
        max_hs_err = mp.mpf(0)
        max_jacobi_abstruse_err = mp.mpf(0)
        max_jacobi_prod_err = mp.mpf(0)
        max_R_dot_c_err = mp.mpf(0)
        max_hh_eta6_err = mp.mpf(0)

        for tau in test_taus:
            deriv_eta_r = [mp.mpc(0, 0), mp.mpc(0, 0), mp.mpc(0, 0)]
            for m in range(N_pts):
                ang = 2 * mp.pi * mp.mpf(m) / mp.mpf(N_pts)
                exp_p = mp.exp(I_u * ang)
                exp_m = mp.exp(-I_u * ang)
                vals = eta_times_r(tau + R_rad * exp_p)
                for k in range(3):
                    deriv_eta_r[k] += vals[k] * exp_m
            scale_d = mp.mpf(1) / (mp.mpf(N_pts) * R_rad * 2 * mp.pi * I_u)
            eta = dedekind_eta(tau)
            c_cauchy = [deriv_eta_r[k] * scale_d / eta for k in range(3)]
            c_closed, h_vec, _ = higgs_triplet_c_and_h(tau)
            for k in range(3):
                err_k = abs(c_cauchy[k] - c_closed[k]) / max(abs(c_closed[k]), mp.mpf(1))
                if err_k > max_hs_err:
                    max_hs_err = err_k

            t2 = theta2_jtheta(tau)
            t3 = theta3_jtheta(tau)
            t4 = theta4_jtheta(tau)
            max_jacobi_abstruse_err = max(max_jacobi_abstruse_err, abs(t3 ** 4 - t2 ** 4 - t4 ** 4))
            max_jacobi_prod_err = max(max_jacobi_prod_err, abs(t2 * t3 * t4 - 2 * (eta ** 3)))

            r_vec = [-(t2 ** 2) / (2 * (eta ** 3)), -(t4 ** 2) / (2 * (eta ** 3)), I_u * (t3 ** 2) / (2 * (eta ** 3))]
            r_dot_c = r_vec[0] * c_closed[0] + r_vec[1] * c_closed[1] + r_vec[2] * c_closed[2]
            max_R_dot_c_err = max(max_R_dot_c_err, abs(r_dot_c))

            hh = h_vec[0] ** 2 + h_vec[1] ** 2 + h_vec[2] ** 2
            max_hh_eta6_err = max(max_hh_eta6_err, abs(hh / ((eta ** 6) / 4) - 1))

        M_T = mp.matrix([[0, 1], [1, 0]])
        M_S = mp.matrix([[-1, -1], [0, 1]])

        def doublet_wt2(z):
            x = theta3_jtheta(z) ** 4
            y = theta4_jtheta(z) ** 4
            return mp.matrix([[x, y]])

        def doublet_wt4(z):
            x = theta3_jtheta(z) ** 4
            y = theta4_jtheta(z) ** 4
            return mp.matrix([[x * (x - 2 * y), y * (y - 2 * x)]])

        max_wt2_T_err = mp.mpf(0)
        max_wt2_S_err = mp.mpf(0)
        max_wt4_T_err = mp.mpf(0)
        max_wt4_S_err = mp.mpf(0)
        ratio_wt4_wt2 = []
        for tau in test_taus:
            v2 = doublet_wt2(tau)
            v2_T = doublet_wt2(tau + 1)
            v2_S = (tau ** (-2)) * doublet_wt2(-mp.mpf(1) / tau)
            max_wt2_T_err = max(max_wt2_T_err, mp.norm(v2_T - v2 * M_T) / mp.norm(v2))
            max_wt2_S_err = max(max_wt2_S_err, mp.norm(v2_S - v2 * M_S) / mp.norm(v2))

            v4 = doublet_wt4(tau)
            v4_T = doublet_wt4(tau + 1)
            v4_S = (tau ** (-4)) * doublet_wt4(-mp.mpf(1) / tau)
            max_wt4_T_err = max(max_wt4_T_err, mp.norm(v4_T - v4 * M_T) / mp.norm(v4))
            max_wt4_S_err = max(max_wt4_S_err, mp.norm(v4_S - v4 * M_S) / mp.norm(v4))
            ratio_wt4_wt2.append(v4[0, 0] / v2[0, 0])

        wt4_non_proportional_gap = abs(ratio_wt4_wt2[0] - ratio_wt4_wt2[1])

    MT_sp = sp.Matrix([[0, 1], [1, 0]])
    MS_sp = sp.Matrix([[-1, -1], [0, 1]])
    MST_sp = MS_sp * MT_sp
    x_s, y_s = sp.symbols("x_s y_s")

    def sym_k_rep(M_mat, k):
        xp = M_mat[0, 0] * x_s + M_mat[1, 0] * y_s
        yp = M_mat[0, 1] * x_s + M_mat[1, 1] * y_s
        cols = []
        for j in range(k + 1):
            poly = sp.Poly(sp.expand((xp ** (k - j)) * (yp ** j)), x_s, y_s)
            col = [poly.coeff_monomial((k - i, i)) for i in range(k + 1)]
            cols.append(col)
        return sp.Matrix(cols).T

    mult_2std_by_k = {}
    for k in (1, 2, 3, 4):
        tr_I = k + 1
        tr_ST = int(sym_k_rep(MST_sp, k).trace())
        m_2std = sp.Rational(2 * tr_I - 2 * tr_ST, 6)
        assert m_2std.q == 1
        mult_2std_by_k["k_%d_wt_%d" % (k, 2 * k)] = int(m_2std)

    C_wt4 = sp.Matrix([[1, 0], [-2, -2], [0, 1]])
    wt4_intertwiner_exact = (
        (sym_k_rep(MT_sp, 2) * C_wt4 - C_wt4 * MT_sp) == sp.zeros(3, 2)
        and (sym_k_rep(MS_sp, 2) * C_wt4 - C_wt4 * MS_sp) == sp.zeros(3, 2)
    )

    hs_and_mod_ok = (
        max_hs_err < mp.power(10, -58)
        and max_jacobi_abstruse_err < mp.power(10, -65)
        and max_jacobi_prod_err < mp.power(10, -65)
        and max_R_dot_c_err < mp.power(10, -65)
        and max_hh_eta6_err < mp.power(10, -65)
        and max_wt2_T_err < mp.power(10, -55)
        and max_wt2_S_err < mp.power(10, -55)
        and max_wt4_T_err < mp.power(10, -55)
        and max_wt4_S_err < mp.power(10, -55)
        and wt4_non_proportional_gap > mp.mpf(1) / 100
        and mult_2std_by_k == {"k_1_wt_2": 1, "k_2_wt_4": 1, "k_3_wt_6": 1, "k_4_wt_8": 2}
        and wt4_intertwiner_exact
    )

    t2, t4, z_sym = sp.symbols("t2 t4 z_sym")
    p1 = -sp.Rational(1, 2) * t2
    p2 = sp.Rational(1, 8) * (t2 ** 2) - sp.Rational(1, 4) * t4

    a_ser = sp.series(z_sym / (2 * sp.sinh(z_sym / 2)), z_sym, 0, 6).removeO()
    a2 = a_ser.coeff(z_sym, 2)
    a4 = a_ser.coeff(z_sym, 4)
    I_half_p = sp.expand(a4 * (p1 ** 2 - 2 * p2) + (a2 ** 2) * p2)

    l_ser = sp.series(z_sym / sp.tanh(z_sym), z_sym, 0, 6).removeO()
    l2 = l_ser.coeff(z_sym, 2)
    l4 = l_ser.coeff(z_sym, 4)
    L_deg8_p = sp.expand(l4 * (p1 ** 2 - 2 * p2) + (l2 ** 2) * p2)
    I_B2_p = sp.expand(-sp.Rational(1, 8) * L_deg8_p)

    A_deg0 = sp.Integer(1)
    A_deg4 = a2 * p1
    A_deg8 = I_half_p
    ch0 = sp.Integer(5)
    ch4 = p1
    ch8 = sp.Rational(1, 12) * (p1 ** 2 - 2 * p2)
    I_3half_p = sp.expand(A_deg8 * ch0 + A_deg4 * ch4 + A_deg0 * ch8)

    b_half_trR4 = sp.Rational(sp.Poly(I_half_p, t2, t4).coeff_monomial((0, 1)))
    b_3half_trR4 = sp.Rational(sp.Poly(I_3half_p, t2, t4).coeff_monomial((0, 1)))
    b_B2_trR4 = sp.Rational(sp.Poly(I_B2_p, t2, t4).coeff_monomial((0, 1)))

    n_3half = int(b_3half_trR4 / b_half_trR4)
    n_B2 = int(b_B2_trR4 / b_half_trR4)
    total_273 = n_3half + n_B2
    tensor_29 = 1 + n_B2

    nT_sym, NV_sym = sp.symbols("nT_sym NV_sym")
    NH_cancel = NV_sym + total_273 - tensor_29 * nT_sym
    I_tot_6d = sp.expand(
        I_3half_p + I_B2_p - nT_sym * (I_B2_p + I_half_p) + NV_sym * I_half_p - NH_cancel * I_half_p
    )
    I_tot_t4_coeff = sp.simplify(sp.Poly(I_tot_6d, t2, t4).coeff_monomial((0, 1)))
    I_tot_t2sq_coeff = sp.simplify(sp.Poly(I_tot_6d, t2, t4).coeff_monomial((2, 0)))
    gs_factorization_ok = (
        I_tot_t4_coeff == 0
        and sp.simplify(I_tot_t2sq_coeff + sp.Rational(1, 128) * (9 - nT_sym)) == 0
    )

    delta_nv12 = (total_273 - tensor_29 * 1) - (81 - 12)
    delta_nv14 = (total_273 - tensor_29 * 1) - (81 - 14)

    grav_ok = (
        b_half_trR4 == sp.Rational(1, 5760)
        and (2 * b_half_trR4) == sp.Rational(1, 2880)
        and n_3half == 245
        and n_B2 == 28
        and total_273 == 273
        and tensor_29 == 29
        and delta_nv12 == 175
        and delta_nv14 == 177
        and gs_factorization_ok
    )

    return {
        "e8_bourbaki_coordinate_free": {
            "cartan_det": det_A,
            "num_roots": len(roots_set),
            "all_norms_2": all_norms_2,
            "highest_root": list(highest_root),
            "kac_marks": kac_marks,
            "unique_e6_a2_deleted_nodes": e6_a2_nodes,
            "dims": {"78_1": dim_78, "1_8": dim_8, "27_3": dim_81_a, "27bar_3bar": dim_81_b},
            "sum_dims": dim_78 + dim_8 + dim_81_a + dim_81_b,
            "27_3_spin10_split": spin10_split_sizes,
            "sm_16_inventory": sm_16_inventory,
            "sm_10_inventory": sm_10_inventory,
            "same_family_couplings": same_family_couplings,
            "so10_10_16_16_ordered": len(ordered_10_16_16),
            "so10_10_16_16_total": len(unordered_couplings),
            "kawamura_triplets_killed": kawamura_killed,
            "triplet_channel_breakdown": triplet_counts,
            "ew_channels_kept": ew_counts,
            "passed": e8_ok,
        },
        "halphen_serre_cauchy_and_s3_modular": {
            "cauchy_N_pts": N_pts,
            "max_halphen_serre_rel_err": nstr_mp(max_hs_err, 8),
            "max_jacobi_abstruse_err": nstr_mp(max_jacobi_abstruse_err, 8),
            "max_jacobi_prod_err": nstr_mp(max_jacobi_prod_err, 8),
            "max_R_dot_c_err": nstr_mp(max_R_dot_c_err, 8),
            "max_hh_over_eta6_div4_err": nstr_mp(max_hh_eta6_err, 8),
            "wt2_doublet_T_err": nstr_mp(max_wt2_T_err, 8),
            "wt2_doublet_S_err": nstr_mp(max_wt2_S_err, 8),
            "wt4_doublet_T_err": nstr_mp(max_wt4_T_err, 8),
            "wt4_doublet_S_err": nstr_mp(max_wt4_S_err, 8),
            "wt4_non_proportional_gap": nstr_mp(wt4_non_proportional_gap, 8),
            "mult_2std_by_weight": mult_2std_by_k,
            "wt4_intertwiner_exact": wt4_intertwiner_exact,
            "i37_verdict": "UNEARNED_WT3HALF_AND_HOLOMORPHY_ASSUMED",
            "passed": hs_and_mod_ok,
        },
        "pontryagin_6d_trR4": {
            "b_half_trR4": str(b_half_trR4),
            "b_half_sum_x4": str(2 * b_half_trR4),
            "n_gravitino_3half": n_3half,
            "n_selfdual_B2": n_B2,
            "total_273": total_273,
            "tensor_multiplet_29": tensor_29,
            "delta_244_nv12_and_nv14": [delta_nv12, delta_nv14],
            "gs_t2sq_coeff_at_cancel": str(I_tot_t2sq_coeff),
            "gs_factorization_exact": gs_factorization_ok,
            "passed": grav_ok,
        },
        "passed": e8_ok and hs_and_mod_ok and grav_ok,
    }


# ---------------------------------------------------------------------------
# MODULE R_OPEN_2
# ---------------------------------------------------------------------------

def run_R_OPEN_2():
    h0, h1, h2, s_sym, u0, u1, u2, w_sym = sp.symbols("h0 h1 h2 s u0 u1 u2 w")
    I2_s = sp.eye(2)
    QI_s = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    QJ_s = sp.Matrix([[0, 1], [-1, 0]])
    QK_s = sp.Matrix([[0, sp.I], [sp.I, 0]])
    eps_s = QJ_s
    C_s = [QJ_s, QI_s, QK_s]
    half_s = sp.Rational(1, 2)
    E1_s = half_s * sp.Matrix([[0, 1], [-1, 0]])
    Ei_s = half_s * sp.Matrix([[0, sp.I], [sp.I, 0]])
    Ej_s = half_s * sp.Matrix([[-1, 0], [0, -1]])
    Ek_s = half_s * sp.Matrix([[-sp.I, 0], [0, sp.I]])

    def Y_direct_sym(hv, sv, M_sym):
        H_sym = hv[0] * QJ_s + hv[1] * QI_s + hv[2] * QK_s + sv * I2_s
        Y = sp.zeros(3, 3)
        for a in range(3):
            for b in range(3):
                K_ab = C_s[a].T * eps_s * H_sym * C_s[b]
                acc = sp.Integer(0)
                for m in range(2):
                    for n in range(2):
                        acc += K_ab[m, n] * M_sym[m, n]
                Y[a, b] = sp.expand(acc)
        return Y

    def cross_mat_sym(v):
        return sp.Matrix([
            [0, -v[2], v[1]],
            [v[2], 0, -v[0]],
            [-v[1], v[0], 0],
        ])

    hv = sp.Matrix([h0, h1, h2])
    uv = sp.Matrix([u0, u1, u2])
    M_s = (-w_sym) * E1_s + u1 * Ei_s + u0 * Ej_s + u2 * Ek_s
    Y_dir = Y_direct_sym(hv, s_sym, M_s)
    uh = u0 * h0 + u1 * h1 + u2 * h2
    uu = u0 ** 2 + u1 ** 2 + u2 ** 2
    hh = h0 ** 2 + h1 ** 2 + h2 ** 2

    Y_closed = uv * hv.T + hv * uv.T - uh * sp.eye(3) + w_sym * cross_mat_sym(hv) - s_sym * (w_sym * sp.eye(3) + cross_mat_sym(uv))
    closed_form_exact = (sp.simplify(Y_dir - Y_closed) == sp.zeros(3, 3))

    Y_MT = Y_direct_sym(hv, s_sym, M_s.T)
    Y_neg_s_T = Y_direct_sym(hv, -s_sym, M_s).T
    wd2_transpose_exact = (sp.simplify(Y_MT - Y_neg_s_T) == sp.zeros(3, 3))

    det_Y_dir = sp.expand(Y_dir.det())
    det_3factor = sp.expand((uu + w_sym ** 2) * (hh + s_sym ** 2) * (uh - w_sym * s_sym))
    det_3factor_exact = (sp.expand(det_Y_dir - det_3factor) == 0)

    poly_s = sp.Poly(det_Y_dir, s_sym)
    D0 = sp.expand(poly_s.nth(0))
    D1 = sp.expand(poly_s.nth(1))
    D2 = sp.expand(poly_s.nth(2))
    D3 = sp.expand(poly_s.nth(3))
    cubic_coeffs_exact = (
        sp.expand(D0 - (uu + w_sym ** 2) * hh * uh) == 0
        and sp.expand(D1 + w_sym * hh * (uu + w_sym ** 2)) == 0
        and sp.expand(D2 - uh * (uu + w_sym ** 2)) == 0
        and sp.expand(D3 + w_sym * (uu + w_sym ** 2)) == 0
    )

    rt2 = sp.sqrt(2)
    U_null_s = sp.Matrix([
        [1 / rt2, 1 / rt2, 0],
        [0, 0, 1],
        [sp.I / rt2, -sp.I / rt2, 0],
    ])
    e_s = sp.Matrix([0, 1, 0])
    mark_op = sp.simplify(U_null_s.H * (sp.I * sp.eye(3) + cross_mat_sym(e_s)) * U_null_s)
    twin_op = sp.simplify(U_null_s.H * (-sp.I * sp.eye(3) + cross_mat_sym(e_s)) * U_null_s)
    null_eigs_exact = (
        sp.simplify(U_null_s.H * U_null_s - sp.eye(3)) == sp.zeros(3, 3)
        and mark_op == sp.diag(2 * sp.I, 0, sp.I)
        and twin_op == sp.diag(0, -2 * sp.I, -sp.I)
    )

    with mp.workdps(95):
        tau_chk = mp.mpc(mp.mpf(13) / 100, mp.mpf(7) / 5)
        a_chk, b_chk = Fraction(1, 5), Fraction(2, 5)
        Fu_base = shifted_kronecker_Fu(a_chk, b_chk, tau_chk)
        Fu_T = shifted_kronecker_Fu(a_chk, b_chk - a_chk, tau_chk + 1)
        Fu_S = shifted_kronecker_Fu(b_chk, -a_chk, -mp.mpf(1) / tau_chk)
        Fu_T_err = abs(Fu_T - Fu_base)
        Fu_S_err = abs(Fu_S - Fu_base)
        a0_base = kronecker_a0(a_chk, b_chk, tau_chk)
        a0_S = kronecker_a0(b_chk, -a_chk, -mp.mpf(1) / tau_chk)
        a0_S_err = abs(abs(a0_S) - abs(tau_chk) * abs(a0_base)) / abs(a0_S)

    pts_mt = {
        "mark": (Fraction(2, 5), Fraction(4, 5)),
        "twin": (Fraction(1, 5), Fraction(2, 5)),
    }
    x_col = Fraction(13, 100)

    with mp.workdps(105):
        I_u = im_unit()
        tau20 = mp.mpc(mp_frac(x_col), mp.mpf(20))
        _, h20, _ = higgs_triplet_c_and_h(tau20)
        cmax20 = max(abs(h20[0]), abs(h20[1]), abs(h20[2]))
        s_test = (mp.mpf(1) / 10 + I_u * (mp.mpf(3) / 20)) * cmax20
        max_det3_num_err = mp.mpf(0)
        max_det_ratio_err = mp.mpf(0)
        max_wd2_num_err = mp.mpf(0)
        max_scrambling_err = mp.mpf(0)

        def det_unitary(seed):
            A_r = mp.zeros(3, 3)
            for i in range(3):
                for j in range(3):
                    re_i = ((seed * 37 + i * 19 + j * 13 + 7) % 29) - 14
                    im_i = ((seed * 53 + i * 23 + j * 11 + 5) % 31) - 15
                    A_r[i, j] = mp.mpc(re_i, im_i)
            Q, _ = mp.qr(A_r)
            return Q

        U_Q = det_unitary(11)
        U_uR = det_unitary(23)
        U_dR = det_unitary(37)
        U_eL = det_unitary(53)
        U_eR = det_unitary(71)
        haar_unitarity_err = max(
            mp.norm(U.H * U - mp.eye(3)) for U in (U_Q, U_uR, U_dR, U_eL, U_eR)
        )

        for pname, (a_fr, b_fr) in pts_mt.items():
            ch_up = frame_c_channel_data("up", a_fr, b_fr, tau20)
            ch_dn = frame_c_channel_data("down", a_fr, b_fr, tau20)
            ch_lp = frame_c_channel_data("lep", a_fr, b_fr, tau20)

            Y_up = direct_spinor_yukawa_mp(h20, mp.mpc(0, 0), ch_up["M"])
            Y_dn = direct_spinor_yukawa_mp(h20, s_test, ch_dn["M"])
            Y_lp = direct_spinor_yukawa_mp(h20, s_test, ch_lp["M"])
            Y_dn_negs = direct_spinor_yukawa_mp(h20, -s_test, ch_dn["M"])

            lam = ch_lp["u"][1] / ch_dn["u"][1]
            wd2_err = mp.norm(Y_lp - lam * Y_dn_negs.T) / mp.norm(Y_lp)
            max_wd2_num_err = max(max_wd2_num_err, wd2_err)

            u = ch_dn["u"]
            w = ch_dn["w"]
            uu_v = u[0] ** 2 + u[1] ** 2 + u[2] ** 2
            hh_v = h20[0] ** 2 + h20[1] ** 2 + h20[2] ** 2
            uh_v = u[0] * h20[0] + u[1] * h20[1] + u[2] * h20[2]
            det_dn = mp.det(Y_dn)
            det_dn_pred = (uu_v + w ** 2) * (hh_v + s_test ** 2) * (uh_v - w * s_test)
            max_det3_num_err = max(max_det3_num_err, abs(det_dn / det_dn_pred - 1))

            det_lp = mp.det(Y_lp)
            ratio_pred = (lam ** 3) * (uh_v + w * s_test) / (uh_v - w * s_test)
            max_det_ratio_err = max(max_det_ratio_err, abs((det_lp / det_dn) / ratio_pred - 1))

            Uu1, su1 = svd_ascending(Y_up)
            Ud1, sd1 = svd_ascending(Y_dn)
            _, sl1 = svd_ascending(Y_lp)
            obs1 = ckm_and_observables(Uu1, su1, Ud1, sd1, sl1)

            Uu2, su2 = svd_ascending(U_Q * Y_up * U_uR.H)
            Ud2, sd2 = svd_ascending(U_Q * Y_dn * U_dR.H)
            _, sl2 = svd_ascending(U_eL * Y_lp * U_eR.H)
            obs2 = ckm_and_observables(Uu2, su2, Ud2, sd2, sl2)

            for key in ("r23_up", "r13_up", "r23_dn", "r13_dn", "r23_lp", "r13_lp", "min_diag", "J", "lnD1_r12", "lnD1_r13", "lnD2"):
                max_scrambling_err = max(max_scrambling_err, rel_diff(obs1[key], obs2[key]))
            for i in range(3):
                for j in range(3):
                    max_scrambling_err = max(max_scrambling_err, abs(obs1["absV"][i][j] - obs2["absV"][i][j]))

    # Scan Mark and Twin across y = 10, 20, 30; keep exact lookup table by (k_label, phi_over_pi)
    scan_results = {"mark": {}, "twin": {}}
    scan_lookup = {"mark": {}, "twin": {}}
    analytic_rates = {}
    for pname, (a_fr, b_fr) in pts_mt.items():
        kstar_S_by_y = {}
        kstar_St_by_y = {}
        for y_int in (10, 20, 30):
            dps_y = 45 + 3 * y_int
            y_lbl = "y_%d" % y_int
            scan_lookup[pname][y_lbl] = {}
            with mp.workdps(dps_y):
                I_u = im_unit()
                tau = mp.mpc(mp_frac(x_col), mp.mpf(y_int))
                _, h_vec, _ = higgs_triplet_c_and_h(tau)
                h_conj = [mp.conj(v) for v in h_vec]
                c_max = max(abs(h_vec[0]), abs(h_vec[1]), abs(h_vec[2]))

                ch_up = frame_c_channel_data("up", a_fr, b_fr, tau)
                ch_dn = frame_c_channel_data("down", a_fr, b_fr, tau)
                ch_lp = frame_c_channel_data("lep", a_fr, b_fr, tau)

                u_dn = ch_dn["u"]
                w_dn = ch_dn["w"]
                uh_S = u_dn[0] * h_vec[0] + u_dn[1] * h_vec[1] + u_dn[2] * h_vec[2]
                uh_St = u_dn[0] * h_conj[0] + u_dn[1] * h_conj[1] + u_dn[2] * h_conj[2]
                kstar_S = abs(uh_S) / (abs(w_dn) * c_max)
                kstar_St = abs(uh_St) / (abs(w_dn) * c_max)
                kstar_S_by_y[y_int] = kstar_S
                kstar_St_by_y[y_int] = kstar_St

                Y_up_s0 = direct_spinor_yukawa_mp(h_vec, mp.mpc(0, 0), ch_up["M"])
                U_up, s_up = svd_ascending(Y_up_s0)
                up_r23_s0 = s_up[1] / s_up[2]

                kappa_grid = [("k_%d" % k, mp.power(10, mp.mpf(k) / 2)) for k in range(-30, 5)]
                kappa_grid.append(("k_analytic", kstar_S))

                thresh_align = mp.mpf(99) / 100
                thresh_hier = mp.mpf(1) / 100
                tie_tol = mp.power(10, -12)
                best_aligned = None
                max_lnD2_hier = mp.mpf(0)

                for k_lbl, kap in kappa_grid:
                    for m_phi in range(8):
                        phi_str = str(Fraction(m_phi, 4))
                        phi = mp.pi * mp.mpf(m_phi) / 4
                        s_val = kap * mp.exp(I_u * phi) * c_max
                        Y_dn = direct_spinor_yukawa_mp(h_vec, s_val, ch_dn["M"])
                        Y_lp = direct_spinor_yukawa_mp(h_vec, s_val, ch_lp["M"])
                        U_dn, s_dn = svd_ascending(Y_dn)
                        _, s_lp = svd_ascending(Y_lp)
                        obs = ckm_and_observables(U_up, s_up, U_dn, s_dn, s_lp)
                        rec = {
                            "k_label": k_lbl,
                            "phi_over_pi": phi_str,
                            "lnD1_r12_mp": obs["lnD1_r12"],
                            "lnD1_r13_mp": obs["lnD1_r13"],
                            "lnD2_mp": obs["lnD2"],
                            "min_diag_mp": obs["min_diag"],
                            "r23_dn_mp": obs["r23_dn"],
                            "r23_lp_mp": obs["r23_lp"],
                        }
                        scan_lookup[pname][y_lbl][(k_lbl, phi_str)] = rec
                        hier_ok = (obs["r23_dn"] <= thresh_hier) and (obs["r23_lp"] <= thresh_hier)
                        if hier_ok:
                            if obs["lnD2"] > max_lnD2_hier:
                                max_lnD2_hier = obs["lnD2"]
                            if obs["min_diag"] >= thresh_align:
                                if best_aligned is None:
                                    best_aligned = rec
                                else:
                                    d_ln1 = obs["lnD1_r12"] - best_aligned["lnD1_r12_mp"]
                                    if d_ln1 > tie_tol:
                                        best_aligned = rec
                                    elif abs(d_ln1) <= tie_tol and obs["min_diag"] > best_aligned["min_diag_mp"]:
                                        best_aligned = rec

                # Also record the exact s <-> -s twin (phi + pi mod 2 pi) of best_aligned
                best_m = int(Fraction(best_aligned["phi_over_pi"]) * 4)
                opp_phi_str = str(Fraction((best_m + 4) % 8, 4))
                opp_rec = scan_lookup[pname][y_lbl][(best_aligned["k_label"], opp_phi_str)]
                s_neg_s_lnD1_diff = abs(best_aligned["lnD1_r12_mp"] - opp_rec["lnD1_r12_mp"])

                scan_results[pname][y_lbl] = {
                    "analytic_kappa_star_S_Wminus": nstr_mp(kstar_S, 12),
                    "analytic_kappa_star_Stilde_Wplus": nstr_mp(kstar_St, 12),
                    "up_r23_s0": nstr_mp(up_r23_s0, 12),
                    "best_aligned_lnD1": {
                        "k_label": best_aligned["k_label"],
                        "phi_over_pi": best_aligned["phi_over_pi"],
                        "lnD1": nstr_mp(best_aligned["lnD1_r12_mp"], 12),
                        "lnD1_r13": nstr_mp(best_aligned["lnD1_r13_mp"], 12),
                        "lnD2": nstr_mp(best_aligned["lnD2_mp"], 12),
                        "min_diag_V": nstr_mp(best_aligned["min_diag_mp"], 12),
                        "r23_dn": nstr_mp(best_aligned["r23_dn_mp"], 12),
                        "r23_lp": nstr_mp(best_aligned["r23_lp_mp"], 12),
                        "s_vs_minus_s_lnD1_symmetry_diff": nstr_mp(s_neg_s_lnD1_diff, 8),
                    },
                    "max_lnD2_with_hierarchy": nstr_mp(max_lnD2_hier, 12),
                }

        with mp.workdps(75):
            rS = -mp.log(kstar_S_by_y[30] / kstar_S_by_y[20]) / (10 * mp.pi)
            rSt = -mp.log(kstar_St_by_y[30] / kstar_St_by_y[20]) / (10 * mp.pi)
            analytic_rates[pname] = {
                "rate_S_Wminus": nstr_mp(rS, 10),
                "rate_Stilde_Wplus": nstr_mp(rSt, 10),
                "err_S_vs_0p10": nstr_mp(abs(rS - mp.mpf(1) / 10), 8),
                "err_Stilde_vs_0p30": nstr_mp(abs(rSt - mp.mpf(3) / 10), 8),
            }

    with mp.workdps(60):
        rates_ok = all(
            parse_mp_str(analytic_rates[p]["err_S_vs_0p10"]) < mp.power(10, -4)
            and parse_mp_str(analytic_rates[p]["err_Stilde_vs_0p30"]) < mp.power(10, -4)
            for p in ("mark", "twin")
        )
        twin_survives_ok = (
            parse_mp_str(scan_results["twin"]["y_10"]["best_aligned_lnD1"]["lnD1"]) > mp.mpf(22) / 10
            and parse_mp_str(scan_results["twin"]["y_20"]["best_aligned_lnD1"]["lnD1"]) > mp.mpf(22) / 10
            and parse_mp_str(scan_results["twin"]["y_30"]["best_aligned_lnD1"]["lnD1"]) > mp.mpf(22) / 10
            and parse_mp_str(scan_results["twin"]["y_10"]["best_aligned_lnD1"]["min_diag_V"]) >= mp.mpf(994) / 1000
            and parse_mp_str(scan_results["twin"]["y_20"]["best_aligned_lnD1"]["min_diag_V"]) >= mp.mpf(99998) / 100000
            and parse_mp_str(scan_results["twin"]["y_30"]["best_aligned_lnD1"]["min_diag_V"]) >= mp.mpf(99999998) / 100000000
        )
        mark_collapses_ok = (
            parse_mp_str(scan_results["mark"]["y_10"]["best_aligned_lnD1"]["lnD1"]) < mp.mpf(5) / 100
            and parse_mp_str(scan_results["mark"]["y_20"]["best_aligned_lnD1"]["lnD1"]) < mp.power(10, -3)
            and parse_mp_str(scan_results["mark"]["y_30"]["best_aligned_lnD1"]["lnD1"]) < mp.power(10, -4)
        )
        lnD2_vanishes_ok = all(
            parse_mp_str(scan_results[p]["y_10"]["max_lnD2_with_hierarchy"]) < mp.mpf(2) / 100
            and parse_mp_str(scan_results[p]["y_20"]["max_lnD2_with_hierarchy"]) < mp.power(10, -3)
            and parse_mp_str(scan_results[p]["y_30"]["max_lnD2_with_hierarchy"]) < mp.power(10, -4)
            for p in ("mark", "twin")
        )

    sym_and_num_ok = (
        closed_form_exact
        and wd2_transpose_exact
        and det_3factor_exact
        and cubic_coeffs_exact
        and null_eigs_exact
        and Fu_T_err < mp.power(10, -60)
        and Fu_S_err < mp.power(10, -60)
        and a0_S_err < mp.power(10, -60)
        and max_det3_num_err < mp.power(10, -50)
        and max_det_ratio_err < mp.power(10, -50)
        and max_wd2_num_err < mp.power(10, -50)
        and haar_unitarity_err < mp.power(10, -60)
        and max_scrambling_err < mp.power(10, -50)
    )

    out_dict = {
        "symbolic_direct_2x2_proofs": {
            "closed_form_exact": closed_form_exact,
            "wd2_transpose_negation_exact": wd2_transpose_exact,
            "exact_3factor_det_Y": det_3factor_exact,
            "cubic_s_coefficients_exact": cubic_coeffs_exact,
            "null_basis_singlet_eigs_exact": null_eigs_exact,
        },
        "modular_and_numerical_identities": {
            "Fu_T_invariance_err": nstr_mp(Fu_T_err, 8),
            "Fu_S_invariance_err": nstr_mp(Fu_S_err, 8),
            "a0_S_covariance_err": nstr_mp(a0_S_err, 8),
            "frame_c_3factor_det_Y_max_err": nstr_mp(max_det3_num_err, 8),
            "frame_c_det_ratio_max_err": nstr_mp(max_det_ratio_err, 8),
            "frame_c_wd2_transpose_max_err": nstr_mp(max_wd2_num_err, 8),
            "guardrail3_haar_unitarity_err": nstr_mp(haar_unitarity_err, 8),
            "guardrail3_basis_scrambling_max_err": nstr_mp(max_scrambling_err, 8),
        },
        "analytic_window_rates_eps_units": analytic_rates,
        "mark_twin_dichotomy_scan": scan_results,
        "rates_0p10_and_0p30_ok": rates_ok,
        "twin_survives_aligned_O1_split": twin_survives_ok,
        "mark_collapses_exponentially": mark_collapses_ok,
        "lnD2_vanishes_exponentially": lnD2_vanishes_ok,
        "passed": sym_and_num_ok and rates_ok and twin_survives_ok and mark_collapses_ok and lnD2_vanishes_ok,
    }
    return out_dict, scan_lookup


# ---------------------------------------------------------------------------
# MODULE R_OPEN_3
# ---------------------------------------------------------------------------

def classify_dir_label(coords):
    labels = ["n", "nb", "e"]
    mags = [abs(c) for c in coords]
    best_i = max([0, 1, 2], key=lambda idx: mags[idx])
    return labels[best_i], mags[best_i]


def classify_point_at_tau(a_fr, b_fr, tau, h_vec):
    ch_up = frame_c_channel_data("up", a_fr, b_fr, tau)
    ch_dn = frame_c_channel_data("down", a_fr, b_fr, tau)
    Y_up = direct_spinor_yukawa_mp(h_vec, mp.mpc(0, 0), ch_up["M"])
    Y_dn = direct_spinor_yukawa_mp(h_vec, mp.mpc(0, 0), ch_dn["M"])
    U_up, s_up = svd_ascending(Y_up)
    U_dn, s_dn = svd_ascending(Y_dn)
    obs = ckm_and_observables(U_up, s_up, U_dn, s_dn)

    U_null = null_basis_mp()
    W_up = U_null.H * U_up
    W_dn = U_null.H * U_dn
    labels = ["n", "nb", "e"]
    assign_up = []
    assign_dn = []
    min_dom_coord = mp.mpf(1)
    for col in range(3):
        m_u = [abs(W_up[row, col]) for row in range(3)]
        i_u = max([0, 1, 2], key=lambda idx: m_u[idx])
        assign_up.append(labels[i_u])
        if m_u[i_u] < min_dom_coord:
            min_dom_coord = m_u[i_u]

        m_d = [abs(W_dn[row, col]) for row in range(3)]
        i_d = max([0, 1, 2], key=lambda idx: m_d[idx])
        assign_dn.append(labels[i_d])
        if m_d[i_d] < min_dom_coord:
            min_dom_coord = m_d[i_d]

    u_up_dir, _ = classify_dir_label(vec_null_coords(ch_up["u"]))
    u_dn_dir, _ = classify_dir_label(vec_null_coords(ch_dn["u"]))

    if u_dn_dir == "e" and abs(ch_dn["u"][1]) > mp.power(10, -80):
        ratio_we = ch_dn["w"] / ch_dn["u"][1]
        if abs(ratio_we - im_unit()) < mp.mpf(1) / 10:
            we_sgn = "+i"
        elif abs(ratio_we + im_unit()) < mp.mpf(1) / 10:
            we_sgn = "-i"
        else:
            we_sgn = "other"
    else:
        we_sgn = "none"

    return {
        "min_diag": obs["min_diag"],
        "absV": obs["absV"],
        "J": obs["J"],
        "assign_up": tuple(assign_up),
        "assign_dn": tuple(assign_dn),
        "min_dom_coord": min_dom_coord,
        "clean_99": min_dom_coord >= mp.mpf(99) / 100,
        "aligned_0p9": obs["min_diag"] >= mp.mpf(9) / 10,
        "u_up_dir": u_up_dir,
        "u_dn_dir": u_dn_dir,
        "we_sgn": we_sgn,
        "s_up": s_up,
        "s_dn": s_dn,
    }


def run_R_OPEN_3():
    x_col = Fraction(13, 100)
    pts_mt = {
        "mark": (Fraction(2, 5), Fraction(4, 5)),
        "twin": (Fraction(1, 5), Fraction(2, 5)),
    }

    expected_rates = {
        "mark": {
            "V12": Fraction(3, 5),
            "V23": Fraction(3, 10),
            "V13": Fraction(11, 10),
            "V31": Fraction(9, 10),
            "J": Fraction(2, 1),
        },
        "twin": {
            "V12": Fraction(9, 10),
            "V23": Fraction(1, 10),
            "V13": Fraction(1, 1),
            "V31": Fraction(6, 5),
            "J": Fraction(11, 5),
        },
    }
    n1_n4_out = {}
    n1_n4_ok = True
    for pname, (a_fr, b_fr) in pts_mt.items():
        vals_by_y = {}
        hh_err_y30 = None
        for y_int in (20, 30):
            with mp.workdps(45 + 3 * y_int):
                tau = mp.mpc(mp_frac(x_col), mp.mpf(y_int))
                _, h_vec, eta = higgs_triplet_c_and_h(tau)
                hh = h_vec[0] ** 2 + h_vec[1] ** 2 + h_vec[2] ** 2
                hh_err = abs(hh / ((eta ** 6) / 4) - 1)
                if y_int == 30:
                    hh_err_y30 = hh_err
                res = classify_point_at_tau(a_fr, b_fr, tau, h_vec)
                vals_by_y[y_int] = {
                    "V12": res["absV"][0][1],
                    "V23": res["absV"][1][2],
                    "V13": res["absV"][0][2],
                    "V31": res["absV"][2][0],
                    "J": res["J"],
                }
        with mp.workdps(75):
            rates_map = {}
            max_rate_err = mp.mpf(0)
            for key, exp_fr in expected_rates[pname].items():
                rt = -mp.log(vals_by_y[30][key] / vals_by_y[20][key]) / (10 * mp.pi)
                rates_map[key] = nstr_mp(rt, 10)
                err_r = abs(rt - mp_frac(exp_fr))
                if err_r > max_rate_err:
                    max_rate_err = err_r
            if max_rate_err >= mp.power(10, -4) or hh_err_y30 >= mp.power(10, -60):
                n1_n4_ok = False
            n1_n4_out[pname] = {
                "rates_20_to_30": rates_map,
                "max_rate_err": nstr_mp(max_rate_err, 8),
                "hh_over_eta6_div4_err_y30": nstr_mp(hh_err_y30, 8),
            }

    ord5_pts = [
        (Fraction(k, 5), Fraction(l, 5))
        for k in range(5) for l in range(5)
        if not (k == 0 and l == 0)
    ]
    half = Fraction(1, 2)
    ord5_buckets = {}
    ord5_matches = 0
    ord5_aligned = 0
    ord5_clean = 0
    p_sum_all_odd = True
    with mp.workdps(135):
        tau30 = mp.mpc(mp_frac(x_col), mp.mpf(30))
        _, h30, _ = higgs_triplet_c_and_h(tau30)
        for a_fr, b_fr in ord5_pts:
            a_tilde = dist_to_Z(a_fr)
            n_plus_up = nearest_int(-(-3 * a_fr))
            n_minus_up = nearest_int(-(5 * a_fr))
            p_up = (n_plus_up + n_minus_up) % 2

            if a_fr == 0:
                pred_up_dir = "nb"
                pred_dn_dir = "nb"
                pred_we = "none"
                pred_assign = ("n", "e", "nb")
            else:
                m_plus_dn = nearest_int(-(3 * a_fr + half))
                m_minus_dn = nearest_int(-(-a_fr + half))
                p_dn = (m_plus_dn + m_minus_dn) % 2
                if ((p_up + p_dn) % 2) != 1:
                    p_sum_all_odd = False
                pred_up_dir = "n" if p_up == 1 else "nb"
                pred_dn_dir = "e"
                pred_we = "+i" if p_dn == 0 else "-i"
                pred_assign = ("n", "nb", "e") if a_tilde == Fraction(2, 5) else ("n", "e", "nb")

            res = classify_point_at_tau(a_fr, b_fr, tau30, h30)
            if res["aligned_0p9"]:
                ord5_aligned += 1
            if res["clean_99"]:
                ord5_clean += 1
            if (
                res["u_up_dir"] == pred_up_dir
                and res["u_dn_dir"] == pred_dn_dir
                and res["we_sgn"] == pred_we
                and res["assign_up"] == pred_assign
                and res["assign_dn"] == pred_assign
            ):
                ord5_matches += 1
            b_key = "%s|%s|%s|%s" % (res["u_up_dir"], res["u_dn_dir"], res["we_sgn"], "".join(res["assign_up"]))
            ord5_buckets[b_key] = ord5_buckets.get(b_key, 0) + 1

    ord5_ok = (
        len(ord5_pts) == 24
        and ord5_aligned == 24
        and ord5_clean == 24
        and ord5_matches == 24
        and p_sum_all_odd
        and sorted(ord5_buckets.values()) == [4, 10, 10]
    )

    pts_b1963 = []
    pts_b1971 = []
    for n_ord in (8, 10):
        for i in range(n_ord):
            for j in range(n_ord):
                a_fr = Fraction(i, n_ord)
                b_fr = Fraction(j, n_ord)
                if math.lcm(a_fr.denominator, b_fr.denominator) == n_ord:
                    pts_b1963.append((n_ord, a_fr, b_fr))
                if max(a_fr.denominator, b_fr.denominator) == n_ord:
                    pts_b1971.append((n_ord, a_fr, b_fr))
    pts_b1963 = sorted(set(pts_b1963), key=lambda t: (t[0], t[1], t[2]))
    pts_b1971 = sorted(set(pts_b1971), key=lambda t: (t[0], t[1], t[2]))
    extra_8_pts = sorted(set(pts_b1963) - set(pts_b1971))
    extra_on_a_half = sum(1 for _, a, _ in extra_8_pts if a == half)
    extra_on_b_half = sum(1 for _, _, b in extra_8_pts if b == half)

    def run_census(pt_list, x_fr, y_int):
        aligned_c = 0
        unaligned_c = 0
        clean_c = 0
        unaligned_by_a = {}
        non_clean_by_a = {}
        with mp.workdps(45 + 3 * y_int):
            tau = mp.mpc(mp_frac(x_fr), mp.mpf(y_int))
            _, h_vec, _ = higgs_triplet_c_and_h(tau)
            for n_ord, a_fr, b_fr in pt_list:
                res = classify_point_at_tau(a_fr, b_fr, tau, h_vec)
                if res["aligned_0p9"]:
                    aligned_c += 1
                else:
                    unaligned_c += 1
                    k = "a=%s_ord%d" % (str(a_fr), n_ord)
                    unaligned_by_a[k] = unaligned_by_a.get(k, 0) + 1
                if res["clean_99"]:
                    clean_c += 1
                else:
                    k = "a=%s_ord%d" % (str(a_fr), n_ord)
                    non_clean_by_a[k] = non_clean_by_a.get(k, 0) + 1
        return {
            "total": len(pt_list),
            "aligned_ge_0p9": aligned_c,
            "unaligned_lt_0p9": unaligned_c,
            "clean_99_count": clean_c,
            "unaligned_by_a": unaligned_by_a,
            "non_clean_by_a": non_clean_by_a,
        }

    b1971_set = set(pts_b1971)
    c120 = {"total": 0, "aligned_ge_0p9": 0, "unaligned_lt_0p9": 0, "clean_99_count": 0, "unaligned_by_a": {}}
    c112 = {"total": 0, "aligned_ge_0p9": 0, "unaligned_lt_0p9": 0, "clean_99_count": 0, "unaligned_by_a": {}}
    with mp.workdps(135):
        tau30 = mp.mpc(mp_frac(x_col), mp.mpf(30))
        _, h30, _ = higgs_triplet_c_and_h(tau30)
        for item in pts_b1963:
            n_ord, a_fr, b_fr = item
            res = classify_point_at_tau(a_fr, b_fr, tau30, h30)
            targets = [c120, c112] if item in b1971_set else [c120]
            for d in targets:
                d["total"] += 1
                if res["aligned_0p9"]:
                    d["aligned_ge_0p9"] += 1
                else:
                    d["unaligned_lt_0p9"] += 1
                    k = "a=%s_ord%d" % (str(a_fr), n_ord)
                    d["unaligned_by_a"][k] = d["unaligned_by_a"].get(k, 0) + 1
                if res["clean_99"]:
                    d["clean_99_count"] += 1

    multi_col_y20 = {}
    for x_lbl, x_fr in (("x_0", Fraction(0, 1)), ("x_0p13", Fraction(13, 100)), ("x_0p25", Fraction(1, 4)), ("x_0p5", Fraction(1, 2))):
        multi_col_y20[x_lbl] = run_census(pts_b1971, x_fr, 20)

    a_half_rate_match = True
    for sec in ("up", "down"):
        qL, qR = SECTOR_CHARGES[sec]
        ap = (qL + qR) * half
        am = (qL - qR) * half
        r_1i = dist_to_Z(ap + half) ** 2 + dist_to_Z(am + half) ** 2
        r_jk = dist_to_Z(ap) ** 2 + dist_to_Z(am) ** 2
        if not (r_1i == 0 and r_jk == half):
            a_half_rate_match = False

    census_ok = (
        len(pts_b1971) == 112
        and len(pts_b1963) == 120
        and len(extra_8_pts) == 8
        and extra_on_a_half == 4
        and extra_on_b_half == 4
        and c112["total"] == 112 and c112["aligned_ge_0p9"] == 104 and c112["unaligned_lt_0p9"] == 8 and c112["clean_99_count"] == 96
        and c112["unaligned_by_a"] == {"a=1/2_ord8": 4, "a=1/2_ord10": 4}
        and c120["total"] == 120 and c120["aligned_ge_0p9"] == 108 and c120["unaligned_lt_0p9"] == 12 and c120["clean_99_count"] == 100
        and c120["unaligned_by_a"] == {"a=1/2_ord8": 4, "a=1/2_ord10": 8}
        and all(
            multi_col_y20[k]["total"] == 112
            and multi_col_y20[k]["aligned_ge_0p9"] == 104
            and multi_col_y20[k]["unaligned_lt_0p9"] == 8
            and multi_col_y20[k]["clean_99_count"] == 96
            and multi_col_y20[k]["unaligned_by_a"] == {"a=1/2_ord8": 4, "a=1/2_ord10": 4}
            for k in ("x_0", "x_0p13", "x_0p25", "x_0p5")
        )
        and a_half_rate_match
    )

    return {
        "b1971_N1_N4": n1_n4_out,
        "b1971_N1_N4_ok": n1_n4_ok,
        "order5_congruence": {
            "total_points": len(ord5_pts),
            "aligned_count": ord5_aligned,
            "clean_count": ord5_clean,
            "congruence_matches": ord5_matches,
            "p_up_plus_p_dn_always_odd": p_sum_all_odd,
            "buckets": ord5_buckets,
            "passed": ord5_ok,
        },
        "orders_8_10_reconciliation": {
            "b1971_112_x0p13_y30": c112,
            "b1963_120_x0p13_y30": c120,
            "extra_lcm10_points_count": len(extra_8_pts),
            "extra_on_a_half": extra_on_a_half,
            "extra_on_b_half": extra_on_b_half,
            "multi_column_y20_b1971": multi_col_y20,
            "a_half_rate_match_exact": a_half_rate_match,
            "passed": census_ok,
        },
        "passed": n1_n4_ok and ord5_ok and census_ok,
    }


# ---------------------------------------------------------------------------
# MODULE R_OPEN_4
# ---------------------------------------------------------------------------

def run_R_OPEN_4(r1_res, r2_res, r2_lookup, r3_res):
    rpf = {}

    # RPF-1: Non-modular F_6 fails S_3 weight-2 equivariance
    with mp.workdps(75):
        I_u = im_unit()
        tau = mp.mpc(mp.mpf(13) / 100, mp.mpf(7) / 5)

        def f6_ratio_vec(z):
            t2 = theta2_jtheta(z)
            t3 = theta3_jtheta(z)
            t4 = theta4_jtheta(z)
            et = dedekind_eta(z)
            f6 = [(t2 ** 6) / (et ** 3), (t4 ** 6) / (et ** 3), I_u * (t3 ** 6) / (et ** 3)]
            r_v = [-(t2 ** 2) / (2 * (et ** 3)), -(t4 ** 2) / (2 * (et ** 3)), I_u * (t3 ** 2) / (2 * (et ** 3))]
            return [f6[k] / r_v[k] for k in range(3)], f6, et

        q_base, f6_base, eta_base = f6_ratio_vec(tau)
        q_T, _, _ = f6_ratio_vec(tau + 1)
        q_T_expected = [q_base[0], q_base[2], q_base[1]]
        f6_T_equiv_err = mp.sqrt(sum(abs(q_T[k] - q_T_expected[k]) ** 2 for k in range(3)))
        f6_dot = f6_base[0] ** 2 + f6_base[1] ** 2 + f6_base[2] ** 2
        f6_norm_err = abs(f6_dot / (-48 * (eta_base ** 6)) - 1)
        rpf1_caught = (f6_T_equiv_err > mp.mpf(1)) and (f6_norm_err < mp.power(10, -65))
        rpf["RPF_1_f6_fails_s3_wt2"] = {
            "f6_T_equiv_err": nstr_mp(f6_T_equiv_err, 8),
            "f6_dot_over_minus48eta6_err": nstr_mp(f6_norm_err, 8),
            "caught": rpf1_caught,
        }

    # RPF-2: Opposite-sign singlet (down: +s, lep: -s) collapses |ln D1| and |ln D2| to 0
    with mp.workdps(105):
        I_u = im_unit()
        tau20 = mp.mpc(mp.mpf(13) / 100, mp.mpf(20))
        _, h20, _ = higgs_triplet_c_and_h(tau20)
        cmax20 = max(abs(h20[0]), abs(h20[1]), abs(h20[2]))
        a_tw, b_tw = Fraction(1, 5), Fraction(2, 5)
        ch_up_tw = frame_c_channel_data("up", a_tw, b_tw, tau20)
        ch_dn_tw = frame_c_channel_data("down", a_tw, b_tw, tau20)
        ch_lp_tw = frame_c_channel_data("lep", a_tw, b_tw, tau20)
        uh_tw = ch_dn_tw["u"][0] * h20[0] + ch_dn_tw["u"][1] * h20[1] + ch_dn_tw["u"][2] * h20[2]
        kstar_tw = abs(uh_tw) / (abs(ch_dn_tw["w"]) * cmax20)
        s_tw = kstar_tw * mp.exp(I_u * 7 * mp.pi / 4) * cmax20

        U_u_tw, s_u_tw = svd_ascending(direct_spinor_yukawa_mp(h20, mp.mpc(0, 0), ch_up_tw["M"]))
        U_d_tw, s_d_tw = svd_ascending(direct_spinor_yukawa_mp(h20, s_tw, ch_dn_tw["M"]))
        _, s_l_opp = svd_ascending(direct_spinor_yukawa_mp(h20, -s_tw, ch_lp_tw["M"]))
        obs_opp = ckm_and_observables(U_u_tw, s_u_tw, U_d_tw, s_d_tw, s_l_opp)
        rpf2_caught = (
            obs_opp["lnD1_r12"] < mp.power(10, -45)
            and obs_opp["lnD1_r13"] < mp.power(10, -45)
            and obs_opp["lnD2"] < mp.power(10, -45)
        )
        rpf["RPF_2_opposite_sign_singlet_collapses_lnD1"] = {
            "lnD1_r12_opposite_sign": nstr_mp(obs_opp["lnD1_r12"], 8),
            "lnD1_r13_opposite_sign": nstr_mp(obs_opp["lnD1_r13"], 8),
            "lnD2_opposite_sign": nstr_mp(obs_opp["lnD2"], 8),
            "caught": rpf2_caught,
        }

    # RPF-3: Corrupting 6D N_H - N_V + 29 n_T = 273 by +1 breaks Pontryagin tr R^4 cancellation
    t2_s, t4_s = sp.symbols("t2_s t4_s")
    p1_s = -sp.Rational(1, 2) * t2_s
    p2_s = sp.Rational(1, 8) * (t2_s ** 2) - sp.Rational(1, 4) * t4_s
    I_half_s = sp.expand((7 * p1_s ** 2 - 4 * p2_s) / 5760)
    I_3half_s = sp.expand((275 * p1_s ** 2 - 980 * p2_s) / 5760)
    I_B2_s = sp.expand(-(7 * p2_s - p1_s ** 2) / 360)
    I_corrupt = sp.expand(I_3half_s + I_B2_s - (I_B2_s + I_half_s) + 12 * I_half_s - 257 * I_half_s)
    t4_corrupt_coeff = sp.Rational(sp.Poly(I_corrupt, t2_s, t4_s).coeff_monomial((0, 1)))
    rpf3_caught = (t4_corrupt_coeff != 0) and (t4_corrupt_coeff == -sp.Rational(1, 5760))
    rpf["RPF_3_6d_trR4_perturbation"] = {
        "corrupted_t4_coeff": str(t4_corrupt_coeff),
        "caught": rpf3_caught,
    }

    # RPF-4: Wrong sign of s in W-D2 §3 identity Y_lep(h, s) vs lam Y_down(h, +s)^T
    with mp.workdps(105):
        I_u = im_unit()
        tau20 = mp.mpc(mp.mpf(13) / 100, mp.mpf(20))
        _, h20, _ = higgs_triplet_c_and_h(tau20)
        cmax20 = max(abs(h20[0]), abs(h20[1]), abs(h20[2]))
        s_bad = (mp.mpf(1) / 10 + I_u * (mp.mpf(3) / 20)) * cmax20
        a_mk, b_mk = Fraction(2, 5), Fraction(4, 5)
        ch_dn_mk = frame_c_channel_data("down", a_mk, b_mk, tau20)
        ch_lp_mk = frame_c_channel_data("lep", a_mk, b_mk, tau20)
        lam_mk = ch_lp_mk["u"][1] / ch_dn_mk["u"][1]
        Y_lp_s = direct_spinor_yukawa_mp(h20, s_bad, ch_lp_mk["M"])
        Y_dn_plus_s = direct_spinor_yukawa_mp(h20, s_bad, ch_dn_mk["M"])
        wrong_sign_err = mp.norm(Y_lp_s - lam_mk * Y_dn_plus_s.T) / mp.norm(Y_lp_s)
        rpf4_caught = wrong_sign_err > mp.mpf(1) / 10
        rpf["RPF_4_wrong_sign_s_breaks_wd2_identity"] = {
            "wrong_sign_rel_err": nstr_mp(wrong_sign_err, 8),
            "caught": rpf4_caught,
        }

    # RPF-5: Conjugating up Higgs (S_tilde, S, S) destroys CKM alignment
    with mp.workdps(105):
        tau20 = mp.mpc(mp.mpf(13) / 100, mp.mpf(20))
        _, h20, _ = higgs_triplet_c_and_h(tau20)
        h20_conj = [mp.conj(v) for v in h20]
        worst_min_diag = mp.mpf(1)
        for a_fr, b_fr in ((Fraction(2, 5), Fraction(4, 5)), (Fraction(1, 5), Fraction(2, 5))):
            ch_up = frame_c_channel_data("up", a_fr, b_fr, tau20)
            ch_dn = frame_c_channel_data("down", a_fr, b_fr, tau20)
            U_up_st, s_up_st = svd_ascending(direct_spinor_yukawa_mp(h20_conj, mp.mpc(0, 0), ch_up["M"]))
            U_dn_s, s_dn_s = svd_ascending(direct_spinor_yukawa_mp(h20, mp.mpc(0, 0), ch_dn["M"]))
            obs_st = ckm_and_observables(U_up_st, s_up_st, U_dn_s, s_dn_s)
            if obs_st["min_diag"] < worst_min_diag:
                worst_min_diag = obs_st["min_diag"]
        rpf5_caught = worst_min_diag < mp.mpf(1) / 5
        rpf["RPF_5_Stilde_up_deranges_CKM"] = {
            "min_diag_V_Stilde_S": nstr_mp(worst_min_diag, 8),
            "caught": rpf5_caught,
        }

    # RPF-6: Perturbing h off h.h = eta^6/4 lifts B1971 N3 nullity & N4 V13 cancellation
    with mp.workdps(105):
        tau20 = mp.mpc(mp.mpf(13) / 100, mp.mpf(20))
        _, h20, eta20 = higgs_triplet_c_and_h(tau20)
        cmax20 = max(abs(h20[0]), abs(h20[1]), abs(h20[2]))
        a_mk, b_mk = Fraction(2, 5), Fraction(4, 5)
        ch_up_mk = frame_c_channel_data("up", a_mk, b_mk, tau20)
        ch_dn_mk = frame_c_channel_data("down", a_mk, b_mk, tau20)

        U_u0, s_u0 = svd_ascending(direct_spinor_yukawa_mp(h20, mp.mpc(0, 0), ch_up_mk["M"]))
        U_d0, s_d0 = svd_ascending(direct_spinor_yukawa_mp(h20, mp.mpc(0, 0), ch_dn_mk["M"]))
        v13_unpert = ckm_and_observables(U_u0, s_u0, U_d0, s_d0)["absV"][0][2]

        inv_rt2 = mp.mpf(1) / mp.sqrt(2)
        delta_h = (mp.mpf(1) / 10) * cmax20
        h20_pert = [h20[0] + delta_h * inv_rt2, h20[1] + delta_h, h20[2] + delta_h * im_unit() * inv_rt2]
        hh_pert = h20_pert[0] ** 2 + h20_pert[1] ** 2 + h20_pert[2] ** 2
        hh_pert_err = abs(hh_pert / ((eta20 ** 6) / 4) - 1)

        U_up_p, s_up_p = svd_ascending(direct_spinor_yukawa_mp(h20_pert, mp.mpc(0, 0), ch_up_mk["M"]))
        U_dn_p, s_dn_p = svd_ascending(direct_spinor_yukawa_mp(h20_pert, mp.mpc(0, 0), ch_dn_mk["M"]))
        v13_pert = ckm_and_observables(U_up_p, s_up_p, U_dn_p, s_dn_p)["absV"][0][2]
        v13_lift_factor = v13_pert / v13_unpert
        rpf6_caught = (hh_pert_err > mp.power(10, 5)) and (v13_lift_factor > mp.power(10, 5))
        rpf["RPF_6_higgs_perturbation_breaks_N3_N4"] = {
            "hh_over_eta6_div4_pert_err": nstr_mp(hh_pert_err, 8),
            "v13_unperturbed": nstr_mp(v13_unpert, 8),
            "v13_perturbed": nstr_mp(v13_pert, 8),
            "v13_lift_factor": nstr_mp(v13_lift_factor, 8),
            "caught": rpf6_caught,
        }

    rpf_caught_count = sum(1 for v in rpf.values() if v["caught"])
    rpf_ok = (rpf_caught_count == 6)

    # --- Producer v3 SHA-256, AST, Sandbox, JSON, and Direct Point-by-Point Cross-Check ---
    prod_script_path = PROD_V3_DIR / "verify_a2_b1972_open_v3.py"
    prod_json_path = PROD_V3_DIR / "a2_b1972_open_v3_results.json"
    prod_script_sha_file = PROD_V3_DIR / "SCRIPT_SHA256.txt"
    prod_out_sha_file = PROD_V3_DIR / "OUTPUT_SHA256.txt"

    prod_script_sha_actual = sha256_file(prod_script_path)
    prod_json_sha_actual = sha256_file(prod_json_path)
    prod_script_sha_recorded = prod_script_sha_file.read_text(encoding="utf-8").strip().split()[0]
    prod_out_sha_recorded = prod_out_sha_file.read_text(encoding="utf-8").strip().split()[0]

    prod_ast = audit_python_ast(prod_script_path)
    prod_external_reads = prod_ast["external_read_calls"]
    prod_data, prod_json_floats = check_json_zero_floats(prod_json_path)

    discrepancies = []
    non_blocking_diagnostics = []

    p_o1 = prod_data["OPEN_1_c13_vs_i37_and_6d_trR4"]
    r_e8 = r1_res["e8_bourbaki_coordinate_free"]
    if p_o1["e8_e6_su3_branching_verified"]["dims"] != r_e8["dims"]:
        discrepancies.append("OPEN_1 E8 branching dims mismatch")
    if p_o1["e8_e6_su3_branching_verified"]["27_3_spin10_split"] != r_e8["27_3_spin10_split"]:
        discrepancies.append("OPEN_1 (27,3) Spin(10) split mismatch")
    if p_o1["e8_e6_su3_branching_verified"]["so10_10_16_16_total"] != r_e8["so10_10_16_16_total"]:
        discrepancies.append("OPEN_1 SO(10) 10*16*16 count mismatch")
    if p_o1["e8_e6_su3_branching_verified"]["kawamura_triplets_killed"] != r_e8["kawamura_triplets_killed"]:
        discrepancies.append("OPEN_1 Kawamura triplet count mismatch")
    if p_o1["e8_e6_su3_branching_verified"]["ew_channels_kept"] != r_e8["ew_channels_kept"]:
        discrepancies.append("OPEN_1 EW channels kept mismatch")
    if p_o1["s3_schur_analysis_M2k_Gamma2"]["mult_2std_by_weight"] != r1_res["halphen_serre_cauchy_and_s3_modular"]["mult_2std_by_weight"]:
        discrepancies.append("OPEN_1 S_3 multiplicities mismatch")

    p_g = p_o1["grav_6d_trR4_anomaly"]
    r_g = r1_res["pontryagin_6d_trR4"]
    for k in ("n_gravitino_3half", "n_selfdual_B2", "tensor_multiplet_29", "total_273", "delta_244_nv12_and_nv14"):
        if p_g[k] != r_g[k]:
            discrepancies.append("OPEN_1 6D gravity %s mismatch" % k)
    if p_g["b_half"] != r_g["b_half_trR4"]:
        if p_g["b_half"] == r_g["b_half_sum_x4"]:
            non_blocking_diagnostics.append(
                "OPEN_1 6D b_half convention note: Producer reports b_half=1/2880 (coeff of S_4 = sum x_i^4 = (1/2) tr R^4), "
                "whereas Pontryagin substitution p_2 = (1/8) t2^2 - (1/4) t4 gives coeff(tr R^4) = 1/5760; "
                "all physical anomaly ratios (245, 28, 29, 273, Delta_244=[175, 177]) match identically."
            )
        else:
            discrepancies.append("OPEN_1 6D b_half mismatch")

    p_o2 = prod_data["OPEN_2_wd2_singlet_theorem_and_SSS_plus_s"]
    max_o2_crosscheck_err = mp.mpf(0)
    with mp.workdps(50):
        tol_1e6 = mp.power(10, -6)
        for pname in ("mark", "twin"):
            for rkey in ("rate_S_Wminus", "rate_Stilde_Wplus"):
                pv = parse_mp_str(p_o2["analytic_window_rates_eps_units"][pname][rkey])
                rv = parse_mp_str(r2_res["analytic_window_rates_eps_units"][pname][rkey])
                err = rel_or_abs_diff(pv, rv)
                max_o2_crosscheck_err = max(max_o2_crosscheck_err, err)
                if err >= tol_1e6:
                    discrepancies.append("OPEN_2 %s %s diff=%s" % (pname, rkey, nstr_mp(err, 6)))
            for y_lbl in ("y_10", "y_20", "y_30"):
                p_cell = p_o2["uncomputed_wd2_sec4_SSS_plus_singlet"][pname][y_lbl]
                r_cell = r2_res["mark_twin_dichotomy_scan"][pname][y_lbl]
                for fkey in ("analytic_kappa_star_S_Wminus", "analytic_kappa_star_Stilde_Wplus", "up_r23_s0", "SSS_plus_singlet_max_lnD2_with_hierarchy"):
                    r_fkey = "max_lnD2_with_hierarchy" if fkey.startswith("SSS_") else fkey
                    pv = parse_mp_str(p_cell[fkey])
                    rv = parse_mp_str(r_cell[r_fkey])
                    err = rel_diff(pv, rv)
                    max_o2_crosscheck_err = max(max_o2_crosscheck_err, err)
                    if err >= tol_1e6:
                        discrepancies.append("OPEN_2 %s %s %s diff=%s" % (pname, y_lbl, fkey, nstr_mp(err, 6)))
                # Compare optimal lnD1 and lnD2 (s <-> -s invariant), AND direct point-by-point match at Producer's exact (k_label, phi)
                p_b = p_cell["SSS_plus_singlet_best_aligned_lnD1"]
                r_b = r_cell["best_aligned_lnD1"]
                for bkey in ("lnD1", "lnD2"):
                    err = rel_diff(parse_mp_str(p_b[bkey]), parse_mp_str(r_b[bkey]))
                    max_o2_crosscheck_err = max(max_o2_crosscheck_err, err)
                    if err >= tol_1e6:
                        discrepancies.append("OPEN_2 %s %s opt.%s diff=%s" % (pname, y_lbl, bkey, nstr_mp(err, 6)))
                # Exact point-by-point verification at Producer's (k_label, phi_over_pi)
                p_key = (p_b["k_label"], p_b["phi_over_pi"])
                r_exact = r2_lookup[pname][y_lbl].get(p_key)
                if r_exact is None:
                    discrepancies.append("OPEN_2 %s %s missing exact key %s" % (pname, y_lbl, str(p_key)))
                else:
                    pt_map = {
                        "lnD1": r_exact["lnD1_r12_mp"],
                        "lnD2": r_exact["lnD2_mp"],
                        "min_diag_V": r_exact["min_diag_mp"],
                        "r23_dn": r_exact["r23_dn_mp"],
                        "r23_lp": r_exact["r23_lp_mp"],
                    }
                    for bkey, rval in pt_map.items():
                        err = rel_diff(parse_mp_str(p_b[bkey]), rval)
                        max_o2_crosscheck_err = max(max_o2_crosscheck_err, err)
                        if err >= tol_1e6:
                            discrepancies.append("OPEN_2 %s %s exact_pt.%s diff=%s" % (pname, y_lbl, bkey, nstr_mp(err, 6)))
                    if r_b["phi_over_pi"] != p_b["phi_over_pi"]:
                        non_blocking_diagnostics.append(
                            "OPEN_2 %s %s s <-> -s tie note: exact |lnD1| tie between phi=%s*pi (Producer min_diag=%s) "
                            "and phi=%s*pi (Referee canonical max-min_diag=%s); all 5 observables at Producer's exact point match to <1e-7."
                            % (pname, y_lbl, p_b["phi_over_pi"], p_b["min_diag_V"], r_b["phi_over_pi"], r_b["min_diag_V"])
                        )

    p_o3 = prod_data["OPEN_3_b1971_and_closed_form_census_congruence"]
    max_o3_rate_crosscheck_err = mp.mpf(0)
    with mp.workdps(50):
        for pname in ("mark", "twin"):
            for rkey in ("V12", "V23", "V13", "V31"):
                pv = parse_mp_str(p_o3["b1971_N1_N3_N4_verified"][pname]["rates_20_to_30"][rkey])
                rv = parse_mp_str(r3_res["b1971_N1_N4"][pname]["rates_20_to_30"][rkey])
                err = rel_or_abs_diff(pv, rv)
                max_o3_rate_crosscheck_err = max(max_o3_rate_crosscheck_err, err)
                if err >= mp.power(10, -5):
                    discrepancies.append("OPEN_3 %s rate %s diff=%s" % (pname, rkey, nstr_mp(err, 6)))

    if p_o3["order5_closed_form_congruence"]["buckets"] != r3_res["order5_congruence"]["buckets"]:
        discrepancies.append("OPEN_3 order-5 buckets mismatch")
    for key in ("total", "aligned_ge_0p9", "unaligned_lt_0p9", "clean_99_count", "unaligned_by_a"):
        if p_o3["orders_8_10_census_b1971_x0p13_y30"][key] != r3_res["orders_8_10_reconciliation"]["b1971_112_x0p13_y30"][key]:
            discrepancies.append("OPEN_3 B1971 112-pt %s mismatch" % key)
        if p_o3["orders_8_10_census_b1963_lcm120_x0p13_y30"][key] != r3_res["orders_8_10_reconciliation"]["b1963_120_x0p13_y30"][key]:
            discrepancies.append("OPEN_3 B1963 120-pt %s mismatch" % key)
        for x_lbl in ("x_0", "x_0p13", "x_0p25", "x_0p5"):
            if p_o3["orders_8_10_multi_column_height_reconciliation"][x_lbl]["y_20"][key] != r3_res["orders_8_10_reconciliation"]["multi_column_y20_b1971"][x_lbl][key]:
                discrepancies.append("OPEN_3 multi-col %s y_20 %s mismatch" % (x_lbl, key))

    producer_v3_audit_ok = (
        prod_script_sha_actual == prod_script_sha_recorded
        and prod_json_sha_actual == prod_out_sha_recorded
        and prod_data.get("script_sha256") == prod_script_sha_actual
        and prod_ast["ast_zero_float_clean"]
        and prod_ast["sandbox_no_subprocess_or_net"]
        and len(prod_ast["disallowed_imports"]) == 0
        and len(prod_external_reads) == 0
        and len(prod_json_floats) == 0
        and len(discrepancies) == 0
    )

    manifest_files = sorted(RELAYS_DIR.rglob("*SHA256*.txt"))
    entries_checked = 0
    manifest_mismatches = []
    line_re = re.compile(r"^([0-9a-fA-F]{64})\s+\*?(.+)$")
    for mf in manifest_files:
        for lineno, raw_line in enumerate(mf.read_text(encoding="utf-8").splitlines(), start=1):
            line = raw_line.strip()
            if not line:
                continue
            m = line_re.match(line)
            if not m:
                manifest_mismatches.append({"manifest": str(mf.relative_to(REPO_ROOT)), "line": lineno, "error": "unparseable"})
                continue
            expected_hex = m.group(1).lower()
            rel_target = m.group(2).strip()
            cand1 = mf.parent / rel_target
            cand2 = REPO_ROOT / rel_target
            target_path = cand1 if cand1.is_file() else (cand2 if cand2.is_file() else None)
            entries_checked += 1
            if target_path is None:
                manifest_mismatches.append({"manifest": str(mf.relative_to(REPO_ROOT)), "target": rel_target, "error": "missing"})
            else:
                got_hex = sha256_file(target_path)
                if got_hex != expected_hex:
                    manifest_mismatches.append({
                        "manifest": str(mf.relative_to(REPO_ROOT)),
                        "target": rel_target,
                        "expected": expected_hex,
                        "actual": got_hex,
                    })

    manifests_ok = (len(manifest_mismatches) == 0) and (len(manifest_files) >= 321)

    return {
        "referee_planted_faults": rpf,
        "rpf_caught_count": rpf_caught_count,
        "rpf_total": 6,
        "producer_v3_audit": {
            "script_sha256_match": prod_script_sha_actual == prod_script_sha_recorded,
            "output_sha256_match": prod_json_sha_actual == prod_out_sha_recorded,
            "json_internal_script_sha_match": prod_data.get("script_sha256") == prod_script_sha_actual,
            "script_sha256": prod_script_sha_actual,
            "output_sha256": prod_json_sha_actual,
            "ast_zero_float_clean": prod_ast["ast_zero_float_clean"],
            "sandbox_no_subprocess_or_net": prod_ast["sandbox_no_subprocess_or_net"],
            "disallowed_imports": prod_ast["disallowed_imports"],
            "external_read_calls": prod_external_reads,
            "json_float_tokens_count": len(prod_json_floats),
            "open2_max_crosscheck_rel_err": nstr_mp(max_o2_crosscheck_err, 8),
            "open3_max_rate_crosscheck_err": nstr_mp(max_o3_rate_crosscheck_err, 8),
            "discrepancies": discrepancies,
            "discrepancies_count": len(discrepancies),
            "non_blocking_diagnostics": non_blocking_diagnostics,
            "passed": producer_v3_audit_ok,
        },
        "branch_manifest_audit": {
            "manifest_files_checked": len(manifest_files),
            "manifest_entries_checked": entries_checked,
            "mismatches_count": len(manifest_mismatches),
            "mismatches": manifest_mismatches,
            "passed": manifests_ok,
        },
        "passed": rpf_ok and producer_v3_audit_ok and manifests_ok,
    }


def main():
    self_path = pathlib.Path(__file__).resolve()
    self_ast = audit_python_ast(self_path)
    self_sha = sha256_file(self_path)

    r1 = run_R_OPEN_1()
    r2, r2_lookup = run_R_OPEN_2()
    r3 = run_R_OPEN_3()
    r4 = run_R_OPEN_4(r1, r2, r2_lookup, r3)

    all_passed = (
        self_ast["ast_zero_float_clean"]
        and self_ast["sandbox_no_subprocess_or_net"]
        and r1["passed"]
        and r2["passed"]
        and r3["passed"]
        and r4["passed"]
    )

    payload = {
        "card_id": "A2-B1972-OPEN",
        "role": "disjoint_cold_room_zero_trust_referee",
        "run": "run2",
        "prior_frozen_v1": {
            "script": "referee_a2_b1972_open.py",
            "script_commit": "14242bc56",
            "output_commit": "a2c393de3",
            "disposition": "frozen_untouched_referee_side_bookkeeping_fixes_in_run2",
        },
        "seat": "agy-002",
        "empirical_firewall": "0 of 19",
        "script": self_path.name,
        "script_sha256": self_sha,
        "self_hygiene": {
            "ast_zero_float_clean": self_ast["ast_zero_float_clean"],
            "sandbox_no_subprocess_or_net": self_ast["sandbox_no_subprocess_or_net"],
            "float_literal_lines": self_ast["float_literal_lines"],
            "complex_literal_lines": self_ast["complex_literal_lines"],
            "banned_cast_calls": self_ast["banned_cast_calls"],
            "disallowed_imports": self_ast["disallowed_imports"],
        },
        "R_OPEN_1": r1,
        "R_OPEN_2": r2,
        "R_OPEN_3": r3,
        "R_OPEN_4": r4,
        "discrepancies_count": r4["producer_v3_audit"]["discrepancies_count"],
        "non_blocking_diagnostics": r4["producer_v3_audit"]["non_blocking_diagnostics"],
        "all_referee_gates_passed": all_passed,
    }

    OUT_JSON_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
