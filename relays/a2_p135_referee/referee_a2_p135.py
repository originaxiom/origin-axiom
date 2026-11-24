"""Disjoint Cold-Room Zero-Trust Referee for Card A2-P135 (0 of 19).

Audit Target:
  - Scope Card: relays/cards/AGY-002_A2-P135_simpson-tame-table-e8-condensate-embedding-and-agy-exp-9b34bfc03-check.md
  - Producer v3: relays/a2_p135_v3/a2_p135_v3_results.json (commit 096499514)

Disjoint Algorithms (Zero Shared Code with Producer v3, W70, or chat1):
  - R_P135_A: 4th-order Kutta-3/8 numerical ODE integration (grids N=64, 128, 256
    with Richardson extrapolation at mp.dps=40) for both diagonal Simpson (1990)
    flat connection holonomy/radial norms and the rank-2 nilpotent Jordan connection,
    plus coordinate-free polynomial trace/Cayley-Hamilton proof of XY=-YX => Q_8
    and symbolic Atiyah deg(-1) parabolic stability.
  - R_P135_B: Coordinate-free Bourbaki 8x8 Cartan E_8 Weyl-reflection BFS (240 roots,
    ZERO R^8 coordinates) + 9-node affine E_8^(1) unique deletion A_5 + A_2 + A_1,
    all-C^3 symbolic + 469-grid hypercharge uniqueness, k_Y = 14/3, su(2)_Q singlet,
    and neutral colour-singlet Higgs doublet root counts purely from Cartan pairings.
  - R_P135_C: Independent Fuchsian Liouville ODE solved via Kutta-3/8 + exact SL(2,R)-
    invariant Hermitian form H + Gauss-Legendre radial-log quadrature for G^(s=1/2)(tau_8^+),
    exact mp.jtheta (zero hand-summed q-series) W_hol cross-checked against direct
    X_0/X_1 theta sums, mp.svd_c Takagi with explicit V^H transposition cross-checked
    against 6x6 real eigsy, 10-trial Xorshift64*+Box-Muller Haar U(3)^3 scrambling
    (true U_e^H U_T vs buggy U_e^H conj(U_T)), all 6 cases vs Producer v3, and LOCK_V3
    A2-OW26-F1 m_0/v_EW check.
  - R_P135_D: 6/6 independent Referee Planted Fault Controls (RPF-1..6), Producer v3
    SHA-256 & sandbox-runnability AST audit, full branch *SHA256*.txt manifest audit,
    and merge-base non-relay edit check.

Firewall: Strictly 0 of 19 (zero empirical SM/PDG/NuFIT/Planck/DESI/CODATA inputs).
Hygiene:  0 Python float/complex AST literals, 0 float()/complex() casts, 0 JSON floats.
"""

from __future__ import annotations

import ast
import collections
import fractions
import glob
import hashlib
import json
import pathlib
import subprocess

import mpmath as mp
import sympy as sp

Frac = fractions.Fraction
I_MP = mp.mpc(0, 1)


def q_mp(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(num) / mp.mpf(den)


def p10(exp: int) -> mp.mpf:
    return mp.mpf(10) ** exp


def mstr(val: mp.mpf | mp.mpc, sig: int = 14) -> str:
    if isinstance(val, mp.mpc):
        return f"({mp.nstr(mp.re(val), sig)}, {mp.nstr(mp.im(val), sig)})"
    return mp.nstr(val, sig)


def assert_no_json_floats(obj: object, path: str = "$") -> list[str]:
    bad: list[str] = []
    if isinstance(obj, float):
        bad.append(path)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            bad.extend(assert_no_json_floats(v, f"{path}.{k}"))
    elif isinstance(obj, list):
        for idx, v in enumerate(obj):
            bad.extend(assert_no_json_floats(v, f"{path}[{idx}]"))
    return bad


def audit_python_ast(py_path: pathlib.Path, check_sandbox: bool = False) -> dict:
    src = py_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(py_path))
    float_lines: list[int] = []
    complex_lines: list[int] = []
    cast_calls: list[list[object]] = []
    imports: set[str] = set()
    io_calls: list[list[object]] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, float):
                float_lines.append(node.lineno)
            elif isinstance(node.value, complex):
                complex_lines.append(node.lineno)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            fname = ""
            if isinstance(node.func, ast.Name):
                fname = node.func.id
                if fname in ("float", "complex"):
                    cast_calls.append([node.lineno, fname])
            elif isinstance(node.func, ast.Attribute):
                fname = node.func.attr
            if check_sandbox and fname in (
                "open",
                "read_text",
                "read_bytes",
                "write_text",
                "write_bytes",
                "Popen",
                "run",
                "system",
                "check_output",
                "check_call",
            ):
                recv = ast.unparse(node.func) if hasattr(ast, "unparse") else fname
                io_calls.append([node.lineno, fname, recv])

    res: dict[str, object] = {
        "float_literal_lines": sorted(set(float_lines)),
        "complex_literal_lines": sorted(set(complex_lines)),
        "banned_cast_calls": cast_calls,
        "imports": sorted(imports),
        "clean": (len(float_lines) == 0 and len(complex_lines) == 0 and len(cast_calls) == 0),
    }
    if check_sandbox:
        forbidden_mods = {
            "subprocess",
            "os",
            "sys",
            "shutil",
            "urllib",
            "http",
            "socket",
            "requests",
            "numpy",
            "scipy",
            "math",
            "cmath",
            "frontier",
            "relays",
        }
        bad_mods = sorted(imports & forbidden_mods)
        # Verify any read_text/read_bytes in Producer only touches self script path (no external reads)
        # by checking that no open()/subprocess calls exist and all read_* receivers come from Path(__file__).
        self_file_vars: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                rhs_str = ast.unparse(node.value) if hasattr(ast, "unparse") else ""
                if "__file__" in rhs_str and "parent" not in rhs_str:
                    for tgt in node.targets:
                        if isinstance(tgt, ast.Name):
                            self_file_vars.add(tgt.id)
            elif isinstance(node, ast.AnnAssign) and node.value is not None:
                rhs_str = ast.unparse(node.value) if hasattr(ast, "unparse") else ""
                if "__file__" in rhs_str and "parent" not in rhs_str:
                    if isinstance(node.target, ast.Name):
                        self_file_vars.add(node.target.id)
        external_reads: list[list[object]] = []
        for lineno, fname, recv in io_calls:
            if fname in ("open", "Popen", "run", "system", "check_output", "check_call"):
                external_reads.append([lineno, fname, recv])
            elif fname in ("read_text", "read_bytes"):
                base_var = str(recv).split(".")[0]
                if base_var not in self_file_vars and "__file__" not in str(recv):
                    external_reads.append([lineno, fname, recv])
        res["forbidden_sandbox_imports"] = bad_mods
        res["io_calls_observed"] = io_calls
        res["external_file_reads_or_subproc"] = external_reads
        res["sandbox_runnable"] = (
            bool(res["clean"]) and len(bad_mods) == 0 and len(external_reads) == 0
        )
    return res


# =============================================================================
# Generic 4th-order Kutta-3/8 Integrator (Scalar & 2x2 Matrix, mpmath)
# =============================================================================

def kutta38_scalar(rhs_fn, t0: mp.mpf, t1: mp.mpf, y0: mp.mpc, n_steps: int) -> mp.mpc:
    h = (t1 - t0) / mp.mpf(n_steps)
    h3 = h / mp.mpf(3)
    h23 = (mp.mpf(2) * h) / mp.mpf(3)
    h8 = h / mp.mpf(8)
    t = t0
    y = y0
    for _ in range(n_steps):
        k1 = rhs_fn(t, y)
        k2 = rhs_fn(t + h3, y + h3 * k1)
        k3 = rhs_fn(t + h23, y - h3 * k1 + h * k2)
        k4 = rhs_fn(t + h, y + h * k1 - h * k2 + h * k3)
        y = y + h8 * (k1 + mp.mpf(3) * k2 + mp.mpf(3) * k3 + k4)
        t = t + h
    return y


def mat2_add(a: list[list[mp.mpc]], b: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    return [
        [a[0][0] + b[0][0], a[0][1] + b[0][1]],
        [a[1][0] + b[1][0], a[1][1] + b[1][1]],
    ]


def mat2_scale(c: mp.mpf | mp.mpc, a: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    return [
        [c * a[0][0], c * a[0][1]],
        [c * a[1][0], c * a[1][1]],
    ]


def mat2_mul(a: list[list[mp.mpc]], b: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def mat2_frob(a: list[list[mp.mpc]]) -> mp.mpf:
    return mp.sqrt(
        abs(a[0][0]) ** 2 + abs(a[0][1]) ** 2 + abs(a[1][0]) ** 2 + abs(a[1][1]) ** 2
    )


def mat2_eye() -> list[list[mp.mpc]]:
    return [[mp.mpc(1, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(1, 0)]]


def kutta38_mat2(coeff_fn, t0: mp.mpf, t1: mp.mpf, y0: list[list[mp.mpc]], n_steps: int) -> list[list[mp.mpc]]:
    """Integrate dY/dt = coeff_fn(t) * Y via 4th-order Kutta-3/8."""
    h = (t1 - t0) / mp.mpf(n_steps)
    h3 = h / mp.mpf(3)
    h23 = (mp.mpf(2) * h) / mp.mpf(3)
    h8 = h / mp.mpf(8)
    three = mp.mpf(3)
    t = t0
    y = [[y0[0][0], y0[0][1]], [y0[1][0], y0[1][1]]]
    for _ in range(n_steps):
        k1 = mat2_mul(coeff_fn(t), y)
        y2 = mat2_add(y, mat2_scale(h3, k1))
        k2 = mat2_mul(coeff_fn(t + h3), y2)
        y3 = mat2_add(mat2_add(y, mat2_scale(-h3, k1)), mat2_scale(h, k2))
        k3 = mat2_mul(coeff_fn(t + h23), y3)
        y4 = mat2_add(
            mat2_add(mat2_add(y, mat2_scale(h, k1)), mat2_scale(-h, k2)),
            mat2_scale(h, k3),
        )
        k4 = mat2_mul(coeff_fn(t + h), y4)
        comb = mat2_add(
            mat2_add(k1, mat2_scale(three, k2)),
            mat2_add(mat2_scale(three, k3), k4),
        )
        y = mat2_add(y, mat2_scale(h8, comb))
        t = t + h
    return y


def richardson3_scalar(y64: mp.mpc, y128: mp.mpc, y256: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
    r1_a = (mp.mpf(16) * y128 - y64) / mp.mpf(15)
    r1_b = (mp.mpf(16) * y256 - y128) / mp.mpf(15)
    r2 = (mp.mpf(32) * r1_b - r1_a) / mp.mpf(31)
    return r1_a, r2


def richardson3_mat2(
    m64: list[list[mp.mpc]], m128: list[list[mp.mpc]], m256: list[list[mp.mpc]]
) -> tuple[list[list[mp.mpc]], list[list[mp.mpc]]]:
    c16 = mp.mpf(16)
    c15 = mp.mpf(15)
    c32 = mp.mpf(32)
    c31 = mp.mpf(31)
    r1_a = [[(c16 * m128[i][j] - m64[i][j]) / c15 for j in range(2)] for i in range(2)]
    r1_b = [[(c16 * m256[i][j] - m128[i][j]) / c15 for j in range(2)] for i in range(2)]
    r2 = [[(c32 * r1_b[i][j] - r1_a[i][j]) / c31 for j in range(2)] for i in range(2)]
    return r1_a, r2


# =============================================================================
# MODULE R_P135_A: Numerical Holonomy + Radial Weights (Simpson 1990 & Jordan)
# =============================================================================

def run_r_p135_a(prod_a: dict) -> tuple[dict, list[str]]:
    discrepancies: list[str] = []
    tol = p10(-12)

    with mp.workdps(40):
        two_pi = mp.mpf(2) * mp.pi
        r1 = q_mp(1, 4)
        r2 = q_mp(1, 20)
        t1 = mp.log(r1)
        t2 = mp.log(r2)

        # 1. Diagonal Simpson (1990) local model via Kutta-3/8 ODE integration
        diag_triples = [
            (Frac(1, 2), Frac(0, 1), Frac(1, 7)),
            (Frac(1, 2), Frac(1, 4), Frac(0, 1)),
            (Frac(1, 3), Frac(1, 5), Frac(1, 11)),
        ]
        diag_checks: list[dict] = []
        max_diag_mono_err = mp.mpf(0)
        max_diag_rad_err = mp.mpf(0)

        for al_f, b_f, c_f in diag_triples:
            al = q_mp(al_f.numerator, al_f.denominator)
            bv = q_mp(b_f.numerator, b_f.denominator)
            cv = q_mp(c_f.numerator, c_f.denominator)

            # A_theta = i*alpha - 2*c  =>  dS/dtheta = -A_theta * S = (-i*alpha + 2*c) * S
            a_theta = I_MP * al - mp.mpf(2) * cv
            s64 = kutta38_scalar(lambda _th, y: -a_theta * y, mp.mpf(0), two_pi, mp.mpc(1, 0), 64)
            s128 = kutta38_scalar(lambda _th, y: -a_theta * y, mp.mpf(0), two_pi, mp.mpc(1, 0), 128)
            s256 = kutta38_scalar(lambda _th, y: -a_theta * y, mp.mpf(0), two_pi, mp.mpc(1, 0), 256)
            m_r1, m_r2 = richardson3_scalar(s64, s128, s256)
            m_exact = mp.exp(-two_pi * I_MP * al + mp.mpf(4) * mp.pi * cv)
            mono_err_64_128 = abs(m_r1 - m_exact)
            mono_err = abs(m_r2 - m_exact)
            if mono_err > max_diag_mono_err:
                max_diag_mono_err = mono_err

            # Radial ODE: dS/dr = -A_r(r) S with A_r = (alpha + 2*b)/r
            # Parameterized by log-radius t = ln(r): dS/dt = -r A_r(e^t) S = -(alpha + 2*b) S
            r_coeff = al + mp.mpf(2) * bv
            rad64 = kutta38_scalar(lambda _t, y: -r_coeff * y, t1, t2, mp.mpc(1, 0), 64)
            rad128 = kutta38_scalar(lambda _t, y: -r_coeff * y, t1, t2, mp.mpc(1, 0), 128)
            rad256 = kutta38_scalar(lambda _t, y: -r_coeff * y, t1, t2, mp.mpc(1, 0), 256)
            _, rad_r2 = richardson3_scalar(rad64, rad128, rad256)
            # |s(r)|_h = |S(r)| * r^alpha
            norm_ratio_num = abs(rad_r2) * ((r2 / r1) ** al)
            norm_ratio_exact = (r2 / r1) ** (-mp.mpf(2) * bv)
            rad_err = abs(norm_ratio_num - norm_ratio_exact)
            if rad_err > max_diag_rad_err:
                max_diag_rad_err = rad_err

            # Also verify direct r-stepping dS/dr = -((alpha+2b)/r) S at N=256, 512 agrees
            dr256 = kutta38_scalar(lambda rv, y: -(r_coeff / rv) * y, r1, r2, mp.mpc(1, 0), 256)
            dr512 = kutta38_scalar(lambda rv, y: -(r_coeff / rv) * y, r1, r2, mp.mpc(1, 0), 512)
            dr_rich = (mp.mpf(16) * dr512 - dr256) / mp.mpf(15)
            direct_r_err = abs(abs(dr_rich) * ((r2 / r1) ** al) - norm_ratio_exact)

            diag_checks.append({
                "triple": [str(al_f), str(b_f), str(c_f)],
                "monodromy_richardson_64_128_err": mstr(mono_err_64_128, 8),
                "monodromy_richardson_64_128_256_err": mstr(mono_err, 8),
                "radial_norm_ratio_err": mstr(rad_err, 8),
                "direct_r_stepping_err": mstr(direct_r_err, 8),
                "passed": bool(mono_err < tol and rad_err < tol and direct_r_err < tol),
            })

        # Filtered flat-side check: alpha=1/2, b=+/-1/4, c=0 keeps tr(M) = -2 with a.a = -1/16 != 0
        b_filt = q_mp(1, 4)
        al_half = q_mp(1, 2)
        m_plus_64 = kutta38_scalar(lambda _th, y: -(I_MP * al_half) * y, mp.mpf(0), two_pi, mp.mpc(1, 0), 64)
        m_plus_128 = kutta38_scalar(lambda _th, y: -(I_MP * al_half) * y, mp.mpf(0), two_pi, mp.mpc(1, 0), 128)
        m_plus_256 = kutta38_scalar(lambda _th, y: -(I_MP * al_half) * y, mp.mpf(0), two_pi, mp.mpc(1, 0), 256)
        _, m_plus = richardson3_scalar(m_plus_64, m_plus_128, m_plus_256)
        tr_m_filtered = mp.mpf(2) * m_plus
        tr_m_filtered_err = abs(tr_m_filtered + mp.mpf(2))
        a_dot_a_filtered = -(b_filt ** 2)
        r_plus_128 = kutta38_scalar(lambda _t, y: -(al_half + mp.mpf(2) * b_filt) * y, t1, t2, mp.mpc(1, 0), 128)
        r_minus_128 = kutta38_scalar(lambda _t, y: -(al_half - mp.mpf(2) * b_filt) * y, t1, t2, mp.mpc(1, 0), 128)
        betti_ratio_plus = abs(r_plus_128) * ((r2 / r1) ** al_half)
        betti_ratio_minus = abs(r_minus_128) * ((r2 / r1) ** al_half)
        filtered_o3_confirmed = bool(
            tr_m_filtered_err < tol
            and abs(a_dot_a_filtered + q_mp(1, 16)) < tol
            and abs(betti_ratio_plus - mp.sqrt(r1 / r2)) < p10(-8)
            and abs(betti_ratio_minus - mp.sqrt(r2 / r1)) < p10(-8)
        )

        # 2. Rank-2 nilpotent Jordan model via Kutta-3/8 at r = 1/4 and r = 1/20
        c0_val = q_mp(1, 2)
        nilp_radii = [(Frac(1, 4), r1), (Frac(1, 20), r2)]
        nilp_results: dict[str, dict] = {}
        m_at_r1: list[list[mp.mpc]] | None = None

        for r_frac, rv in nilp_radii:
            uv = -mp.log(rv)

            def a_theta_nilp(_th: mp.mpf, u_cur: mp.mpf = uv, c0_cur: mp.mpf = c0_val) -> list[list[mp.mpc]]:
                return [
                    [I_MP * (al_half + mp.mpf(1) / (mp.mpf(2) * u_cur)), I_MP * c0_cur],
                    [-I_MP * c0_cur / (u_cur ** 2), I_MP * (al_half - mp.mpf(1) / (mp.mpf(2) * u_cur))],
                ]

            def neg_a_theta(_th: mp.mpf, fn=a_theta_nilp) -> list[list[mp.mpc]]:
                mat = fn(_th)
                return mat2_scale(mp.mpc(-1, 0), mat)

            m64 = kutta38_mat2(neg_a_theta, mp.mpf(0), two_pi, mat2_eye(), 64)
            m128 = kutta38_mat2(neg_a_theta, mp.mpf(0), two_pi, mat2_eye(), 128)
            m256 = kutta38_mat2(neg_a_theta, mp.mpf(0), two_pi, mat2_eye(), 256)
            m_r1_err_mat, m_num = richardson3_mat2(m64, m128, m256)
            if r_frac == Frac(1, 4):
                m_at_r1 = m_num

            tr_m = m_num[0][0] + m_num[1][1]
            det_m = m_num[0][0] * m_num[1][1] - m_num[0][1] * m_num[1][0]
            m_plus_i = mat2_add(m_num, mat2_eye())
            n_norm = mat2_frob(m_plus_i)
            n_sq_norm = mat2_frob(mat2_mul(m_plus_i, m_plus_i))
            step_diff = mat2_frob(mat2_add(m_num, mat2_scale(mp.mpc(-1, 0), m_r1_err_mat)))

            nilp_results[f"r_{r_frac.numerator}_over_{r_frac.denominator}"] = {
                "tr_M_plus_2_err": mstr(abs(tr_m + mp.mpf(2)), 8),
                "det_M_minus_1_err": mstr(abs(det_m - mp.mpf(1)), 8),
                "norm_M_plus_I": mstr(n_norm, 10),
                "norm_M_plus_I_sq": mstr(n_sq_norm, 8),
                "richardson_64_128_vs_256_diff": mstr(step_diff, 8),
                "passed": bool(
                    abs(tr_m + mp.mpf(2)) < tol
                    and abs(det_m - mp.mpf(1)) < tol
                    and n_norm > mp.mpf(1)
                    and n_sq_norm < tol
                ),
            }

        # Radial propagation of numerically extracted eigenvector v1 & h-orthogonal complement v2
        assert m_at_r1 is not None
        u1 = -mp.log(r1)
        u2 = -mp.log(r2)
        b_mat = mat2_add(m_at_r1, mat2_eye())
        row0_norm = abs(b_mat[0][0]) + abs(b_mat[0][1])
        row1_norm = abs(b_mat[1][0]) + abs(b_mat[1][1])
        if row0_norm >= row1_norm:
            b0, b1 = b_mat[0][0], b_mat[0][1]
        else:
            b0, b1 = b_mat[1][0], b_mat[1][1]
        v1_r1 = [mp.mpc(1, 0), -b0 / b1]
        # Verify v1_r1 is in ker(M(r1) + I_2)
        bv1 = [
            b_mat[0][0] * v1_r1[0] + b_mat[0][1] * v1_r1[1],
            b_mat[1][0] * v1_r1[0] + b_mat[1][1] * v1_r1[1],
        ]
        ker_v1_err = mp.sqrt(abs(bv1[0]) ** 2 + abs(bv1[1]) ** 2)

        # Build h(r1)-orthogonal complement v2_r1: v1^H h(r1) v2 = 0
        h1_00 = r1 / u1
        h1_11 = r1 * u1
        h2_00 = r2 / u2
        h2_11 = r2 * u2
        w_conj_0 = mp.conj(v1_r1[0]) * h1_00
        w_conj_1 = mp.conj(v1_r1[1]) * h1_11
        v2_raw = [-w_conj_1, w_conj_0]
        # Scale v2 so (M(r1) + I_2) v2 = -2*pi*i * v1 (canonical Jordan basis)
        bv2_raw = [
            b_mat[0][0] * v2_raw[0] + b_mat[0][1] * v2_raw[1],
            b_mat[1][0] * v2_raw[0] + b_mat[1][1] * v2_raw[1],
        ]
        scale_v2 = bv2_raw[0] / (-two_pi * I_MP * v1_r1[0])
        v2_r1 = [v2_raw[0] / scale_v2, v2_raw[1] / scale_v2]

        # Check Jordan form P^{-1} M(r1) P == [[-1, -2*pi*i], [0, -1]]
        p_mat = [[v1_r1[0], v2_r1[0]], [v1_r1[1], v2_r1[1]]]
        det_p = p_mat[0][0] * p_mat[1][1] - p_mat[0][1] * p_mat[1][0]
        p_inv = [
            [p_mat[1][1] / det_p, -p_mat[0][1] / det_p],
            [-p_mat[1][0] / det_p, p_mat[0][0] / det_p],
        ]
        m_jordan_num = mat2_mul(p_inv, mat2_mul(m_at_r1, p_mat))
        m_jordan_exact = [[mp.mpc(-1, 0), -two_pi * I_MP], [mp.mpc(0, 0), mp.mpc(-1, 0)]]
        jordan_basis_err = mat2_frob(
            mat2_add(m_jordan_num, mat2_scale(mp.mpc(-1, 0), m_jordan_exact))
        )

        # Integrate radial ODE dS/dt = -r A_r(e^t) S from t1 = ln(r1) to t2 = ln(r2)
        def neg_r_ar(t_val: mp.mpf) -> list[list[mp.mpc]]:
            u_val = -t_val
            return [
                [-(al_half + mp.mpf(1) / (mp.mpf(2) * u_val)), -c0_val],
                [-c0_val / (u_val ** 2), -(al_half - mp.mpf(1) / (mp.mpf(2) * u_val))],
            ]

        sr64 = kutta38_mat2(neg_r_ar, t1, t2, mat2_eye(), 64)
        sr128 = kutta38_mat2(neg_r_ar, t1, t2, mat2_eye(), 128)
        sr256 = kutta38_mat2(neg_r_ar, t1, t2, mat2_eye(), 256)
        _, s_rad = richardson3_mat2(sr64, sr128, sr256)

        v1_r2 = [
            s_rad[0][0] * v1_r1[0] + s_rad[0][1] * v1_r1[1],
            s_rad[1][0] * v1_r1[0] + s_rad[1][1] * v1_r1[1],
        ]
        v2_r2 = [
            s_rad[0][0] * v2_r1[0] + s_rad[0][1] * v2_r1[1],
            s_rad[1][0] * v2_r1[0] + s_rad[1][1] * v2_r1[1],
        ]

        def h_norm(vec: list[mp.mpc], h00: mp.mpf, h11: mp.mpf) -> mp.mpf:
            return mp.sqrt(h00 * (abs(vec[0]) ** 2) + h11 * (abs(vec[1]) ** 2))

        ratio_s1_num = h_norm(v1_r2, h2_00, h2_11) / h_norm(v1_r1, h1_00, h1_11)
        ratio_s2_num = h_norm(v2_r2, h2_00, h2_11) / h_norm(v2_r1, h1_00, h1_11)
        ratio_s1_exact = mp.sqrt(mp.log(r1) / mp.log(r2))
        ratio_s2_exact = mp.sqrt(mp.log(r2) / mp.log(r1))
        ratio_s1_err = abs(ratio_s1_num - ratio_s1_exact)
        ratio_s2_err = abs(ratio_s2_num - ratio_s2_exact)

        # RPF-2 data: wrong coupling c0 = 1 in numerical Kutta-3/8 monodromy at r = 1/4
        c0_bad = mp.mpf(1)

        def neg_a_theta_bad(_th: mp.mpf) -> list[list[mp.mpc]]:
            return [
                [-I_MP * (al_half + mp.mpf(1) / (mp.mpf(2) * u1)), -I_MP * c0_bad],
                [I_MP * c0_bad / (u1 ** 2), -I_MP * (al_half - mp.mpf(1) / (mp.mpf(2) * u1))],
            ]

        mb64 = kutta38_mat2(neg_a_theta_bad, mp.mpf(0), two_pi, mat2_eye(), 64)
        mb128 = kutta38_mat2(neg_a_theta_bad, mp.mpf(0), two_pi, mat2_eye(), 128)
        mb256 = kutta38_mat2(neg_a_theta_bad, mp.mpf(0), two_pi, mat2_eye(), 256)
        _, m_bad_c0 = richardson3_mat2(mb64, mb128, mb256)
        tr_bad_c0 = m_bad_c0[0][0] + m_bad_c0[1][1]
        n_bad_sq = mat2_frob(mat2_mul(mat2_add(m_bad_c0, mat2_eye()), mat2_add(m_bad_c0, mat2_eye())))

    # 3. Symbolic verification: Hitchin eq for nilpotent Jordan, XY=-YX => Q_8, Atiyah deg(-1)
    u_s, c0_s = sp.symbols("u c0", positive=True)
    h_curv_diag = sp.Matrix([[-sp.Rational(1, 4) / u_s**2, 0], [0, sp.Rational(1, 4) / u_s**2]])
    phi_m = sp.Matrix([[0, c0_s], [0, 0]])
    h_m = sp.diag(1 / u_s, u_s)
    phi_adj = h_m.inv() * phi_m.T * h_m
    hitchin_res_gen = sp.simplify(h_curv_diag + (phi_m * phi_adj - phi_adj * phi_m))
    hitchin_half_zero = bool(hitchin_res_gen.subs(c0_s, sp.Rational(1, 2)) == sp.zeros(2, 2))
    hitchin_one_nonzero = bool(hitchin_res_gen.subs(c0_s, sp.Integer(1)) != sp.zeros(2, 2))

    # Coordinate-free polynomial proof of XY = -YX => Q_8 in SL(2, C)
    a, b, c, d, p, q, r_s, s = sp.symbols("a b c d p q r s")
    X = sp.Matrix([[a, b], [c, d]])
    Y = sp.Matrix([[p, q], [r_s, s]])
    adjX = sp.Matrix([[d, -b], [-c, a]])
    adjY = sp.Matrix([[s, -q], [-r_s, p]])
    M_anti = X * Y + Y * X
    id_tr_y = sp.simplify(sp.trace(M_anti * adjX) - 2 * X.det() * sp.trace(Y))
    id_tr_x = sp.simplify(sp.trace(M_anti * adjY) - 2 * Y.det() * sp.trace(X))
    id_tr_xy = sp.simplify(sp.trace(M_anti) - 2 * sp.trace(X * Y))
    ch_x = sp.simplify(X * X - sp.trace(X) * X + X.det() * sp.eye(2))
    ch_y = sp.simplify(Y * Y - sp.trace(Y) * Y + Y.det() * sp.eye(2))
    ch_xy = sp.simplify((X * Y) ** 2 - sp.trace(X * Y) * (X * Y) + X.det() * Y.det() * sp.eye(2))

    # Concrete Q_8 group closure check
    qi = sp.Matrix([[sp.I, 0], [0, -sp.I]])
    qj = sp.Matrix([[0, 1], [-1, 0]])
    q8_elems = set()
    frontier = [sp.eye(2), qi, qj]
    for g in frontier:
        q8_elems.add(tuple(g))
    changed = True
    while changed:
        changed = False
        cur = list(q8_elems)
        for g1 in cur:
            m1 = sp.Matrix(2, 2, g1)
            for g2 in cur:
                prod = tuple(m1 * sp.Matrix(2, 2, g2))
                if prod not in q8_elems:
                    q8_elems.add(prod)
                    changed = True
    q8_comm_minus_i = bool(qi * qj * qi.inv() * qj.inv() == -sp.eye(2))
    q8_proof_ok = bool(
        id_tr_y == 0
        and id_tr_x == 0
        and id_tr_xy == 0
        and ch_x == sp.zeros(2, 2)
        and ch_y == sp.zeros(2, 2)
        and ch_xy == sp.zeros(2, 2)
        and len(q8_elems) == 8
        and q8_comm_minus_i
    )

    # Atiyah deg(-1) parabolic stability with equal weights (1/2, 1/2)
    deg_E = sp.Integer(-1)
    al1 = sp.Rational(1, 2)
    al2 = sp.Rational(1, 2)
    pardeg_E = deg_E + al1 + al2
    mu_par_E = pardeg_E / sp.Integer(2)
    # Any line subbundle L of Atiyah's indecomposable deg(-1) bundle has deg(L) <= -1
    k_nonneg = sp.Symbol("k_nonneg", integer=True, nonnegative=True)
    deg_L_general = sp.Integer(-1) - k_nonneg
    # Equal weights (1/2, 1/2) force alpha(L) = 1/2 for every 1D subspace at the puncture
    pardeg_L_general = deg_L_general + al1
    max_pardeg_L = pardeg_L_general.subs(k_nonneg, 0)
    atiyah_stable_ok = bool(
        pardeg_E == 0
        and mu_par_E == 0
        and max_pardeg_L == -sp.Rational(1, 2)
        and (pardeg_L_general - mu_par_E).is_negative is True
    )

    # Cross-check against Producer v3 P135_A results
    prod_match = bool(
        prod_a.get("passed") is True
        and prod_a["atiyah_deg_minus1_parabolic_stability"]["max_pardeg_line_subbundle"] == str(max_pardeg_L)
        and prod_a["atiyah_deg_minus1_parabolic_stability"]["pardeg_E"] == str(pardeg_E)
        and prod_a["nilpotent_rank2_jordan_model"]["monodromy_matrix"] == [["-1", "-2*pi*I"], ["0", "-1"]]
        and prod_a["o3_common_point_check"]["filtered_c0_kappa"] == "-2"
    )

    all_diag_ok = all(d["passed"] for d in diag_checks)
    all_nilp_ok = all(v["passed"] for v in nilp_results.values())
    passed = bool(
        all_diag_ok
        and filtered_o3_confirmed
        and all_nilp_ok
        and ker_v1_err < tol
        and jordan_basis_err < tol
        and ratio_s1_err < tol
        and ratio_s2_err < tol
        and hitchin_half_zero
        and hitchin_one_nonzero
        and q8_proof_ok
        and atiyah_stable_ok
        and prod_match
    )
    if not passed:
        discrepancies.append("R_P135_A_FAILED_GATE")

    out = {
        "diagonal_kutta38_checks": diag_checks,
        "max_diag_monodromy_err": mstr(max_diag_mono_err, 8),
        "max_diag_radial_norm_err": mstr(max_diag_rad_err, 8),
        "filtered_b_quarter_c0": {
            "tr_M_plus_2_err": mstr(tr_m_filtered_err, 8),
            "a_dot_a": mstr(a_dot_a_filtered, 10),
            "betti_norm_ratio_plus_b": mstr(betti_ratio_plus, 12),
            "betti_norm_ratio_minus_b": mstr(betti_ratio_minus, 12),
            "confirmed": filtered_o3_confirmed,
        },
        "nilpotent_jordan_kutta38": {
            "radii": nilp_results,
            "ker_v1_err": mstr(ker_v1_err, 8),
            "jordan_basis_err_vs_minus_1_2piI": mstr(jordan_basis_err, 8),
            "s1_norm_ratio_num": mstr(ratio_s1_num, 14),
            "s1_norm_ratio_exact": mstr(ratio_s1_exact, 14),
            "s1_norm_ratio_err": mstr(ratio_s1_err, 8),
            "s2_norm_ratio_num": mstr(ratio_s2_num, 14),
            "s2_norm_ratio_exact": mstr(ratio_s2_exact, 14),
            "s2_norm_ratio_err": mstr(ratio_s2_err, 8),
            "hitchin_symbolic_c0_half_zero": hitchin_half_zero,
            "hitchin_symbolic_c0_one_nonzero": hitchin_one_nonzero,
            "wrong_c0_one_tr_M": mstr(tr_bad_c0, 10),
            "wrong_c0_one_norm_M_plus_I_sq": mstr(n_bad_sq, 10),
        },
        "symbolic_q8_coordinate_free_proof_ok": q8_proof_ok,
        "symbolic_atiyah_deg_minus1_parabolic_stability_ok": atiyah_stable_ok,
        "matches_producer_v3_P135_A": prod_match,
        "passed": passed,
    }
    return out, discrepancies


# =============================================================================
# MODULE R_P135_B: Coordinate-Free Bourbaki Affine E_8^(1) Deletion A_5+A_2+A_1
# =============================================================================

def run_r_p135_b(prod_b: dict) -> tuple[dict, list[str]]:
    discrepancies: list[str] = []

    # 1. Standard 8x8 Bourbaki E_8 Cartan matrix (0-indexed: Bourbaki 1..8 -> 0..7)
    #    0 — 2 — 3 — 4 — 5 — 6 — 7
    #            |
    #            1
    e8_edges = [(0, 2), (2, 3), (1, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
    C = [[2 if i == j else 0 for j in range(8)] for i in range(8)]
    for u, v in e8_edges:
        C[u][v] = -1
        C[v][u] = -1

    def ip_int(r1: tuple[int, ...], r2: tuple[int, ...]) -> int:
        tot = 0
        for i in range(8):
            ci = r1[i]
            if ci == 0:
                continue
            row = C[i]
            for j in range(8):
                if r2[j] != 0 and row[j] != 0:
                    tot += ci * row[j] * r2[j]
        return tot

    def ip_frac(v1: tuple[Frac, ...], v2: tuple[Frac, ...]) -> Frac:
        tot = Frac(0, 1)
        for i in range(8):
            c1 = v1[i]
            if c1 == 0:
                continue
            row = C[i]
            for j in range(8):
                if v2[j] != 0 and row[j] != 0:
                    tot += c1 * row[j] * v2[j]
        return tot

    # 2. Generate all 240 E_8 roots purely via Weyl-reflection BFS in simple-root coordinates
    simples = [tuple(1 if j == i else 0 for j in range(8)) for i in range(8)]
    roots_set: set[tuple[int, ...]] = set(simples)
    queue = collections.deque(simples)
    while queue:
        r = queue.popleft()
        for k in range(8):
            # <r, alpha_k> = sum_i r[i] * C[i][k]
            pair_k = sum(r[i] * C[i][k] for i in range(8))
            if pair_k != 0:
                reflected = list(r)
                reflected[k] -= pair_k
                rt = tuple(reflected)
                if rt not in roots_set:
                    roots_set.add(rt)
                    queue.append(rt)

    roots = sorted(roots_set)
    all_norm2 = all(ip_int(r, r) == 2 for r in roots)

    # 3. Highest root theta_E8 and 9-node affine E_8^(1) diagram
    max_ht = max(sum(r) for r in roots)
    highest_candidates = [r for r in roots if sum(r) == max_ht]
    theta_e8 = highest_candidates[0]
    neg_theta = tuple(-x for x in theta_e8)
    aff_roots = simples + [neg_theta]  # indices 0..7 are alpha_1..alpha_8, index 8 is -theta
    C_aff = [[ip_int(aff_roots[i], aff_roots[j]) for j in range(9)] for i in range(9)]

    # 4. Programmatically find the unique node of affine E_8^(1) whose deletion leaves A_5+A_2+A_1
    def connected_components_without(deleted: int) -> list[list[int]]:
        rem = [i for i in range(9) if i != deleted]
        seen: set[int] = set()
        comps: list[list[int]] = []
        for start in rem:
            if start in seen:
                continue
            comp: list[int] = []
            dq = collections.deque([start])
            seen.add(start)
            while dq:
                u = dq.popleft()
                comp.append(u)
                for v in rem:
                    if v not in seen and C_aff[u][v] == -1:
                        seen.add(v)
                        dq.append(v)
            comps.append(comp)
        comps.sort(key=len, reverse=True)
        return comps

    def order_linear_chain(comp: list[int], adj_to: int) -> list[int]:
        if len(comp) == 1:
            return list(comp)
        # Start from the endpoint adjacent to deleted node `adj_to`
        ends = [u for u in comp if sum(1 for v in comp if v != u and C_aff[u][v] == -1) == 1]
        start = ends[0]
        for e in ends:
            if C_aff[e][adj_to] == -1:
                start = e
                break
        ordered = [start]
        while len(ordered) < len(comp):
            cur = ordered[-1]
            nxts = [v for v in comp if v not in ordered and C_aff[cur][v] == -1]
            ordered.append(nxts[0])
        return ordered

    a5_a2_a1_deletions: list[tuple[int, list[list[int]]]] = []
    for k in range(9):
        comps = connected_components_without(k)
        sizes = tuple(len(c) for c in comps)
        if sizes == (5, 2, 1):
            # Verify each component is an A_n linear chain (max degree <= 2)
            all_chains = all(
                all(sum(1 for v in comp if v != u and C_aff[u][v] == -1) <= 2 for u in comp)
                for comp in comps
            )
            if all_chains:
                a5_a2_a1_deletions.append((k, comps))

    unique_deletion_ok = (len(a5_a2_a1_deletions) == 1)
    del_node, del_comps = a5_a2_a1_deletions[0]
    a5_idx = order_linear_chain(del_comps[0], del_node)
    a2_idx = order_linear_chain(del_comps[1], del_node)
    a1_idx = order_linear_chain(del_comps[2], del_node)

    g5 = [aff_roots[i] for i in a5_idx]  # A_5 simple roots gamma_1..gamma_5
    d2 = [aff_roots[i] for i in a2_idx]  # A_2 simple roots delta_1, delta_2
    eta1 = aff_roots[a1_idx[0]]          # A_1 simple root

    # Verify exact block-diagonal Cartan matrix of A_5 + A_2 + A_1
    sub_all = g5 + d2 + [eta1]
    C_sub = sp.Matrix([[ip_int(sub_all[i], sub_all[j]) for j in range(8)] for i in range(8)])
    C_a5 = sp.Matrix([[ip_int(g5[i], g5[j]) for j in range(5)] for i in range(5)])
    C_a2 = sp.Matrix([[ip_int(d2[i], d2[j]) for j in range(2)] for i in range(2)])
    C_a1 = sp.Matrix([[ip_int(eta1, eta1)]])
    C_expected = sp.diag(C_a5, C_a2, C_a1)
    cartan_a5_a2_a1_ok = bool(
        C_sub == C_expected
        and C_a5 == sp.Matrix([
            [2, -1, 0, 0, 0],
            [-1, 2, -1, 0, 0],
            [0, -1, 2, -1, 0],
            [0, 0, -1, 2, -1],
            [0, 0, 0, -1, 2],
        ])
        and C_a2 == sp.Matrix([[2, -1], [-1, 2]])
        and C_a1 == sp.Matrix([[2]])
    )

    # 5. Fundamental weights w_0..w_5 of A_5 purely from C_{A_5}^{-1}
    C_a5_inv = C_a5.inv()
    C_a2_inv = C_a2.inv()
    omega_a5: list[tuple[Frac, ...]] = []
    for i in range(5):
        vec = [Frac(0, 1)] * 8
        for j in range(5):
            coeff = Frac(int(C_a5_inv[i, j].p), int(C_a5_inv[i, j].q))
            for coord in range(8):
                vec[coord] += coeff * g5[j][coord]
        omega_a5.append(tuple(vec))

    w_a5: list[tuple[Frac, ...]] = [omega_a5[0]]
    for k in range(5):
        prev = w_a5[-1]
        nxt = tuple(prev[coord] - Frac(g5[k][coord], 1) for coord in range(8))
        w_a5.append(nxt)

    sum_w_zero = all(sum(w_a5[k][c] for k in range(6)) == 0 for c in range(8))
    w_gram_ok = all(
        ip_frac(w_a5[i], w_a5[j]) == (Frac(5, 6) if i == j else Frac(-1, 6))
        for i in range(6)
        for j in range(6)
    )

    # 6. Branch all 240 roots under A_5 x A_2 x A_1
    def classify_root(r: tuple[int, ...]) -> tuple[str, tuple[int, ...], tuple[int, ...], int]:
        l5 = tuple(ip_int(r, g) for g in g5)
        l2 = tuple(ip_int(r, d) for d in d2)
        l1 = ip_int(r, eta1)

        # Projection norm^2 onto A_5, A_2, A_1
        v5 = sp.Matrix(l5)
        v2 = sp.Matrix(l2)
        n5_sp = (v5.T * C_a5_inv * v5)[0, 0]
        n2_sp = (v2.T * C_a2_inv * v2)[0, 0]
        n5 = Frac(int(n5_sp.p), int(n5_sp.q))
        n2 = Frac(int(n2_sp.p), int(n2_sp.q))
        n1 = Frac(l1 * l1, 2)
        assert n5 + n2 + n1 == Frac(2, 1)

        # N-ality: A_5 N_5 = sum_{i=1..5} i * l5[i-1] mod 6; A_2 N_3 = (l2[0] + 2*l2[1]) mod 3
        nal5 = sum((i + 1) * l5[i] for i in range(5)) % 6
        nal2 = (l2[0] + 2 * l2[1]) % 3

        if n5 == 2 and n2 == 0 and n1 == 0:
            rep = "(35, 1, 1)"
        elif n5 == 0 and n2 == 2 and n1 == 0:
            rep = "(1, 8, 1)"
        elif n5 == 0 and n2 == 0 and n1 == 2:
            rep = "(1, 1, 3)"
        elif n5 == Frac(3, 2) and n2 == 0 and n1 == Frac(1, 2):
            rep = "(20, 1, 2)"
        elif n5 == Frac(4, 3) and n2 == Frac(2, 3) and n1 == 0:
            if nal5 == 2 and nal2 == 2:
                rep = "(15, 3bar, 1)"
            elif nal5 == 4 and nal2 == 1:
                rep = "(15bar, 3, 1)"
            else:
                rep = f"UNKNOWN_15_{nal5}_{nal2}"
        elif n5 == Frac(5, 6) and n2 == Frac(2, 3) and n1 == Frac(1, 2):
            if nal5 == 1 and nal2 == 1:
                rep = "(6, 3, 2)"
            elif nal5 == 5 and nal2 == 2:
                rep = "(6bar, 3bar, 2)"
            else:
                rep = f"UNKNOWN_6_{nal5}_{nal2}"
        else:
            rep = f"UNKNOWN_{n5}_{n2}_{n1}"
        return rep, l5, l2, l1

    branch_counts_split: dict[str, int] = collections.Counter()
    root_info: list[tuple[tuple[int, ...], str, tuple[int, ...], tuple[int, ...], int]] = []
    for r in roots:
        rep, l5, l2, l1 = classify_root(r)
        branch_counts_split[rep] += 1
        root_info.append((r, rep, l5, l2, l1))

    branch_248_exact = {
        "(35, 1, 1)": branch_counts_split["(35, 1, 1)"] + 5,
        "(1, 8, 1)": branch_counts_split["(1, 8, 1)"] + 2,
        "(1, 1, 3)": branch_counts_split["(1, 1, 3)"] + 1,
        "(20, 1, 2)": branch_counts_split["(20, 1, 2)"],
        "(15, 3bar, 1)": branch_counts_split["(15, 3bar, 1)"],
        "(15bar, 3, 1)": branch_counts_split["(15bar, 3, 1)"],
        "(6, 3, 2)": branch_counts_split["(6, 3, 2)"],
        "(6bar, 3bar, 2)": branch_counts_split["(6bar, 3bar, 2)"],
    }
    branch_248_ok = (
        branch_248_exact
        == {
            "(35, 1, 1)": 35,
            "(1, 8, 1)": 8,
            "(1, 1, 3)": 3,
            "(20, 1, 2)": 40,
            "(15, 3bar, 1)": 45,
            "(15bar, 3, 1)": 45,
            "(6, 3, 2)": 36,
            "(6bar, 3bar, 2)": 36,
        }
        and sum(branch_248_exact.values()) == 248
    )

    # 7. h_Q = sum_{k=0..5} (-1)^k w_k == gamma_1 + gamma_3 + gamma_5, h_W = eta_1
    h_Q_from_w = tuple(
        sum((Frac(1, 1) if k % 2 == 0 else Frac(-1, 1)) * w_a5[k][c] for k in range(6))
        for c in range(8)
    )
    h_Q_int = tuple(g5[0][c] + g5[2][c] + g5[4][c] for c in range(8))
    h_Q_identity_ok = all(h_Q_from_w[c] == Frac(h_Q_int[c], 1) for c in range(8))
    h_W_int = eta1
    hq_norm_sq = ip_int(h_Q_int, h_Q_int)  # 6

    ad_diff_even_all = all((ip_int(r, h_Q_int) - ip_int(r, h_W_int)) % 2 == 0 for r in roots)
    p_odd_roots = [item for item in root_info if ip_int(item[0], h_Q_int) % 2 != 0]
    p_even_roots = [item for item in root_info if ip_int(item[0], h_Q_int) % 2 == 0]
    p_odd_count = len(p_odd_roots)
    p_even_plus_cartan = len(p_even_roots) + 8

    # Backreaction projection histogram (<r, h_Q> / <h_Q, h_Q>) on 112 p-odd roots
    backreaction_hist: dict[str, int] = collections.Counter()
    for r, _rep, _l5, _l2, _l1 in p_odd_roots:
        proj = Frac(ip_int(r, h_Q_int), hq_norm_sq)
        backreaction_hist[str(proj)] += 1

    # 8. su(2)_Q = span(h_Q, E_{g1}+E_{g3}+E_{g5}, E_{-g1}+E_{-g3}+E_{-g5}) complete SM singlet
    betas_q = [g5[0], g5[2], g5[4]]
    betas_ortho = all(
        ip_int(betas_q[i], betas_q[j]) == (2 if i == j else 0)
        for i in range(3)
        for j in range(3)
    )
    beta_diffs_no_roots = all(
        tuple(betas_q[i][c] - betas_q[j][c] for c in range(8)) not in roots_set
        for i in range(3)
        for j in range(3)
        if i != j
    )
    sl2_eigs_ok = all(ip_int(h_Q_int, b) == 2 for b in betas_q) and betas_ortho and beta_diffs_no_roots
    su2_q_color_singlet = all(ip_int(b, d) == 0 for b in betas_q for d in d2) and all(
        ip_int(h_Q_int, d) == 0 for d in d2
    )
    su2_q_weak_singlet = all(ip_int(b, h_W_int) == 0 for b in betas_q) and ip_int(h_Q_int, h_W_int) == 0
    su2_q_p_even = all(ip_int(b, h_Q_int) % 2 == 0 for b in betas_q)
    p_odd_set = {item[0] for item in p_odd_roots}
    su2_q_zero_overlap_p_odd = all(
        b not in p_odd_set and tuple(-x for x in b) not in p_odd_set for b in betas_q
    )

    # Symbolic block-scalar Y = y1(w0+w1) + y2(w2+w3) + y3(w4+w5), y1+y2+y3=0
    y1, y2, y3 = sp.symbols("y1 y2 y3")
    b_vecs = [
        tuple(w_a5[0][c] + w_a5[1][c] for c in range(8)),
        tuple(w_a5[2][c] + w_a5[3][c] for c in range(8)),
        tuple(w_a5[4][c] + w_a5[5][c] for c in range(8)),
    ]

    def y_expr_of_root(r: tuple[int, ...]) -> sp.Expr:
        rf = tuple(Frac(x, 1) for x in r)
        c1 = ip_frac(rf, b_vecs[0])
        c2 = ip_frac(rf, b_vecs[1])
        c3 = ip_frac(rf, b_vecs[2])
        return (
            sp.Rational(c1.numerator, c1.denominator) * y1
            + sp.Rational(c2.numerator, c2.denominator) * y2
            + sp.Rational(c3.numerator, c3.denominator) * y3
        )

    su2_q_y_identically_zero = all(
        sp.simplify(y_expr_of_root(b).subs(y3, -y1 - y2)) == 0 for b in betas_q
    ) and sp.simplify(y_expr_of_root(h_Q_int).subs(y3, -y1 - y2)) == 0

    # 9. Exact all-C^3 algebraic proof of the 6 admissible hypercharges (and PF-4 drop e^c -> 9)
    # Extract the distinct linear Y(y1, y2, y3) forms on each SM-hosting irrep directly from the 240 roots!
    forms_Q = sorted(
        {sp.simplify(y_expr_of_root(r).subs(y3, -y1 - y2)) for r, rep, *_ in root_info if rep == "(6, 3, 2)"},
        key=str,
    )
    forms_ac = sorted(
        {sp.simplify(y_expr_of_root(r).subs(y3, -y1 - y2)) for r, rep, *_ in root_info if rep == "(15, 3bar, 1)"},
        key=str,
    )
    forms_L = sorted(
        {sp.simplify(y_expr_of_root(r).subs(y3, -y1 - y2)) for r, rep, *_ in root_info if rep == "(20, 1, 2)"},
        key=str,
    )
    forms_ec = sorted(
        {sp.simplify(y_expr_of_root(r).subs(y3, -y1 - y2)) for r, rep, *_ in root_info if rep == "(35, 1, 1)"},
        key=str,
    )

    def solve_c3_admissible(include_ec: bool) -> list[tuple[Frac, Frac, Frac]]:
        sols: set[tuple[Frac, Frac, Frac]] = set()
        # Q_L: 1/6 in forms_Q; L: -1/2 in forms_L (2 linear equations in y1, y2 -> unique point or degenerate)
        for fq in forms_Q:
            if fq == 0:
                continue
            for fl in forms_L:
                if fl == 0:
                    continue
                eqs = [sp.Eq(fq, sp.Rational(1, 6)), sp.Eq(fl, -sp.Rational(1, 2))]
                sol = sp.solve(eqs, [y1, y2], dict=True)
                if not sol:
                    continue
                for sdict in sol:
                    if y1 not in sdict or y2 not in sdict:
                        continue
                    v1 = sp.simplify(sdict[y1])
                    v2 = sp.simplify(sdict[y2])
                    if v1.free_symbols or v2.free_symbols:
                        # 1-parameter family: pin using u^c = -2/3 or d^c = 1/3
                        for fac in forms_ac:
                            for target in (-sp.Rational(2, 3), sp.Rational(1, 3)):
                                sol2 = sp.solve(eqs + [sp.Eq(fac, target)], [y1, y2], dict=True)
                                for sd2 in sol2:
                                    if y1 in sd2 and y2 in sd2:
                                        w1, w2 = sp.simplify(sd2[y1]), sp.simplify(sd2[y2])
                                        if not w1.free_symbols and not w2.free_symbols:
                                            w3 = sp.simplify(-w1 - w2)
                                            subs_map = {y1: w1, y2: w2}
                                            vals_ac = {sp.simplify(f.subs(subs_map)) for f in forms_ac}
                                            vals_ec = {sp.simplify(f.subs(subs_map)) for f in forms_ec}
                                            if (-sp.Rational(2, 3) in vals_ac and sp.Rational(1, 3) in vals_ac):
                                                if (not include_ec) or (sp.Integer(1) in vals_ec):
                                                    sols.add((
                                                        Frac(int(w1.p), int(w1.q)),
                                                        Frac(int(w2.p), int(w2.q)),
                                                        Frac(int(w3.p), int(w3.q)),
                                                    ))
                        continue
                    v3 = sp.simplify(-v1 - v2)
                    subs_map = {y1: v1, y2: v2}
                    vals_ac = {sp.simplify(f.subs(subs_map)) for f in forms_ac}
                    vals_ec = {sp.simplify(f.subs(subs_map)) for f in forms_ec}
                    if -sp.Rational(2, 3) in vals_ac and sp.Rational(1, 3) in vals_ac:
                        if (not include_ec) or (sp.Integer(1) in vals_ec):
                            sols.add((
                                Frac(int(v1.p), int(v1.q)),
                                Frac(int(v2.p), int(v2.q)),
                                Frac(int(v3.p), int(v3.q)),
                            ))
        return sorted(sols)

    c3_admissible = solve_c3_admissible(include_ec=True)
    c3_no_ec = solve_c3_admissible(include_ec=False)

    # Exhaustive 469-point k/6 grid cross-check (|k1|, |k2|, |k3| <= 12, k1+k2+k3 = 0)
    grid_pts: list[tuple[Frac, Frac, Frac]] = []
    for k1 in range(-12, 13):
        for k2 in range(-12, 13):
            k3 = -(k1 + k2)
            if -12 <= k3 <= 12:
                grid_pts.append((Frac(k1, 6), Frac(k2, 6), Frac(k3, 6)))

    def eval_y_vec(ys: tuple[Frac, Frac, Frac]) -> tuple[Frac, ...]:
        return tuple(
            ys[0] * b_vecs[0][c] + ys[1] * b_vecs[1][c] + ys[2] * b_vecs[2][c]
            for c in range(8)
        )

    grid_admissible: list[tuple[Frac, Frac, Frac]] = []
    for ys in grid_pts:
        yv = eval_y_vec(ys)
        s_q = {ip_frac(tuple(Frac(x, 1) for x in r), yv) for r, rep, *_ in root_info if rep == "(6, 3, 2)"}
        if Frac(1, 6) not in s_q:
            continue
        s_ac = {ip_frac(tuple(Frac(x, 1) for x in r), yv) for r, rep, *_ in root_info if rep == "(15, 3bar, 1)"}
        if Frac(-2, 3) not in s_ac or Frac(1, 3) not in s_ac:
            continue
        s_l = {ip_frac(tuple(Frac(x, 1) for x in r), yv) for r, rep, *_ in root_info if rep == "(20, 1, 2)"}
        if Frac(-1, 2) not in s_l:
            continue
        s_ec = {ip_frac(tuple(Frac(x, 1) for x in r), yv) for r, rep, *_ in root_info if rep == "(35, 1, 1)"}
        if Frac(1, 1) not in s_ec:
            continue
        grid_admissible.append(ys)
    grid_admissible.sort()

    # 10. k_Y = Tr_248(Y^2) / Tr_248(T_3^2), neutral Higgs-like doublets, 24 union == 24 block roots
    tr_t3_sq = sum(Frac(ip_int(r, h_W_int), 2) ** 2 for r in roots)
    k_y_values: list[Frac] = []
    neutral_counts_per_y: list[int] = []
    neutral_union: set[tuple[int, ...]] = set()
    for ys in c3_admissible:
        yv = eval_y_vec(ys)
        tr_y_sq = sum(ip_frac(tuple(Frac(x, 1) for x in r), yv) ** 2 for r in roots)
        k_y_values.append(tr_y_sq / tr_t3_sq)

        neutrals_here: list[tuple[int, ...]] = []
        for r, rep, _l5, _l2, l1 in p_odd_roots:
            if rep != "(20, 1, 2)":
                continue
            y_val = ip_frac(tuple(Frac(x, 1) for x in r), yv)
            t3_val = Frac(l1, 2)
            if y_val in (Frac(1, 2), Frac(-1, 2)) and (t3_val + y_val == 0):
                neutrals_here.append(r)
                neutral_union.add(r)
        neutral_counts_per_y.append(len(neutrals_here))

    # Block weight partition of 112 p-odd roots:
    # A root in (20,1,2) is block-Cartan iff Y_expr(r) == 0 identically (mod y1+y2+y3=0), else block-root of SU(3)_block!
    block_cartan_roots = {
        r for r, rep, *_ in p_odd_roots
        if rep == "(20, 1, 2)" and sp.simplify(y_expr_of_root(r).subs(y3, -y1 - y2)) == 0
    }
    block_su3_roots = {
        r for r, rep, *_ in p_odd_roots
        if rep == "(20, 1, 2)" and sp.simplify(y_expr_of_root(r).subs(y3, -y1 - y2)) != 0
    }
    block_vec_roots = {r for r, rep, *_ in p_odd_roots if rep in ("(6, 3, 2)", "(6bar, 3bar, 2)")}
    union_equals_24_block_roots = (neutral_union == block_su3_roots and len(neutral_union) == 24)

    # 11. Unique neutral colour-singlet doublet root with A_5 Dynkin labels [0, 1, 0, -1, 1] and T_3 = +1/2
    target_matches = [
        item for item in p_odd_roots
        if item[1] == "(20, 1, 2)" and item[2] == (0, 1, 0, -1, 1) and item[4] == 1
    ]
    target_unique = (len(target_matches) == 1)
    r_star = target_matches[0][0]
    r_star_neutral_ys = [
        ys for ys in c3_admissible
        if ip_frac(tuple(Frac(x, 1) for x in r_star), eval_y_vec(ys)) + Frac(1, 2) == 0
    ]
    # Check stabilizer inside SU(3)_c x SU(2)_L x U(1)_Y:
    # Unbroken SU(3)_c iff <r_star, delta_1> = <r_star, delta_2> = 0;
    # Unbroken U(1)_em iff <r_star, T_3 + Y> = 0;
    # Broken SU(2)_L x U(1)_Y -> U(1)_em iff <r_star, T_3> != 0 and r_star - eta1 in roots.
    unbroken_su3_u1em = bool(
        len(r_star_neutral_ys) == 1
        and all(ip_int(r_star, d) == 0 for d in d2)
        and ip_int(r_star, h_W_int) == 1
        and tuple(r_star[c] - h_W_int[c] for c in range(8)) in roots_set
    )

    # RPF-3 data: drop one doublet from h_Q (h_Q_bad = gamma_1 + gamma_3)
    h_Q_bad = tuple(g5[0][c] + g5[2][c] for c in range(8))
    rpf3_mismatches = sum(1 for r in roots if (ip_int(r, h_Q_bad) - ip_int(r, h_W_int)) % 2 != 0)

    # Cross-check EVERY count against Producer v3 P135_B
    prod_admissible = [tuple(Frac(s) for s in row) for row in prod_b["admissible_hypercharges_list"]]
    prod_match = bool(
        prod_b.get("passed") is True
        and prod_b["e8_root_count"] == len(roots) == 240
        and prod_b["puncture_odd_root_count"] == p_odd_count == 112
        and prod_b["puncture_even_root_count_plus_8_cartans"] == p_even_plus_cartan == 136
        and prod_b["admissible_hypercharges_count_469_grid"] == len(grid_admissible) == 6
        and prod_admissible == c3_admissible
        and prod_b["k_Y_exact"] == "14/3"
        and prod_b["neutral_higgs_doublets_per_Y"] == neutral_counts_per_y == [4, 4, 4, 4, 4, 4]
        and prod_b["neutral_union_count"] == len(neutral_union) == 24
        and prod_b["backreaction_hQ_projection_histogram"] == dict(backreaction_hist)
        and prod_b["pf3_dropped_doublet_mismatches"] == rpf3_mismatches == 112
        and prod_b["pf4_drop_ec_spurious_count"] == len(c3_no_ec) == 9
        and prod_b["published_root_e3_plus_e5"]["unique_neutral_Y"] == [str(x) for x in r_star_neutral_ys[0]]
    )

    passed = bool(
        len(roots) == 240
        and all_norm2
        and theta_e8 == (2, 3, 4, 6, 5, 4, 3, 2)
        and unique_deletion_ok
        and del_node == 3
        and cartan_a5_a2_a1_ok
        and sum_w_zero
        and w_gram_ok
        and branch_248_ok
        and h_Q_identity_ok
        and ad_diff_even_all
        and p_odd_count == 112
        and p_even_plus_cartan == 136
        and sl2_eigs_ok
        and su2_q_color_singlet
        and su2_q_weak_singlet
        and su2_q_p_even
        and su2_q_zero_overlap_p_odd
        and su2_q_y_identically_zero
        and len(grid_pts) == 469
        and len(c3_admissible) == 6
        and c3_admissible == grid_admissible
        and all(ky == Frac(14, 3) for ky in k_y_values)
        and neutral_counts_per_y == [4, 4, 4, 4, 4, 4]
        and union_equals_24_block_roots
        and len(block_cartan_roots) == 16
        and len(block_su3_roots) == 24
        and len(block_vec_roots) == 72
        and dict(backreaction_hist) == {"-1/2": 2, "-1/6": 54, "1/6": 54, "1/2": 2}
        and target_unique
        and unbroken_su3_u1em
        and rpf3_mismatches == 112
        and len(c3_no_ec) == 9
        and prod_match
    )
    if not passed:
        discrepancies.append("R_P135_B_FAILED_GATE")

    out = {
        "e8_root_count_weyl_bfs": len(roots),
        "highest_root_bourbaki": list(theta_e8),
        "unique_affine_deletion_node_1indexed": del_node + 1,
        "deleted_node_kac_mark": theta_e8[del_node],
        "a5_nodes_0indexed": a5_idx,
        "a2_nodes_0indexed": a2_idx,
        "a1_nodes_0indexed": a1_idx,
        "cartan_a5_a2_a1_ok": cartan_a5_a2_a1_ok,
        "branching_248": branch_248_exact,
        "ad_hQ_equals_ad_hW_all_240": ad_diff_even_all,
        "puncture_odd_roots": p_odd_count,
        "puncture_even_plus_8_cartans": p_even_plus_cartan,
        "backreaction_histogram_112": dict(sorted(backreaction_hist.items())),
        "su2_Q_complete_sm_singlet": {
            "sl2_triple_exact": sl2_eigs_ok,
            "colour_singlet": su2_q_color_singlet,
            "weak_singlet": su2_q_weak_singlet,
            "puncture_even": su2_q_p_even,
            "zero_overlap_112_p_odd": su2_q_zero_overlap_p_odd,
            "Y_identically_zero_symbolic": su2_q_y_identically_zero,
        },
        "admissible_hypercharges_C3_count": len(c3_admissible),
        "admissible_hypercharges_469_grid_count": len(grid_admissible),
        "grid_size_checked": len(grid_pts),
        "admissible_hypercharges": [[str(x) for x in ys] for ys in c3_admissible],
        "k_Y_all_six_exact": [str(ky) for ky in k_y_values],
        "neutral_higgs_doublets_per_Y": neutral_counts_per_y,
        "neutral_union_count": len(neutral_union),
        "neutral_union_equals_24_block_roots": union_equals_24_block_roots,
        "block_partition_112": {
            "block_cartan": len(block_cartan_roots),
            "block_roots_su3": len(block_su3_roots),
            "block_vectors_6_6bar": len(block_vec_roots),
        },
        "neutral_color_singlet_doublet_root": {
            "a5_dynkin_labels": [0, 1, 0, -1, 1],
            "T3": "1/2",
            "unique_root_found": target_unique,
            "unique_neutral_Y": [str(x) for x in r_star_neutral_ys[0]],
            "unbroken_SU3c_x_U1em": unbroken_su3_u1em,
        },
        "rpf3_dropped_doublet_mismatches": rpf3_mismatches,
        "rpf4_drop_ec_solution_count": len(c3_no_ec),
        "rpf4_spurious_16_neg13_16_present": (Frac(1, 6), Frac(-1, 3), Frac(1, 6)) in c3_no_ec,
        "matches_producer_v3_P135_B": prod_match,
        "passed": passed,
    }
    return out, discrepancies


# =============================================================================
# MODULE R_P135_C: Disjoint Verification of agy-exp 9b34bfc03 (A2-OW27-F2)
# =============================================================================

def gauss_legendre_nodes_weights(n: int) -> tuple[list[mp.mpf], list[mp.mpf]]:
    """Golub-Welsch Gauss-Legendre nodes & weights on [-1, 1] via mp.eigsy (zero floats)."""
    jac = mp.zeros(n, n)
    for k in range(1, n):
        b = mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1))
        jac[k - 1, k] = b
        jac[k, k - 1] = b
    evals, evecs = mp.eigsy(jac)
    nodes = [evals[i] for i in range(n)]
    weights = [mp.mpf(2) * (evecs[0, i] ** 2) for i in range(n)]
    return nodes, weights


def compute_dirac_s12_gramian_kutta38() -> dict:
    """Compute G^(s=1/2)(tau_8^+) independently using Kutta-3/8 on Fuchsian Liouville ODE."""
    with mp.workdps(28):
        tau_r = q_mp(1, 5) + I_MP * q_mp(8, 5)
        tau_8 = q_mp(16, 5) + I_MP * q_mp(8, 5)
        im_tau = q_mp(8, 5)
        q_r = mp.exp(I_MP * mp.pi * tau_r)
        q_8 = mp.exp(I_MP * mp.pi * tau_8)

        t30 = mp.jtheta(3, mp.mpf(0), q_r)
        t40 = mp.jtheta(4, mp.mpf(0), q_r)
        e1_val = (mp.pi ** 2 / mp.mpf(3)) * (t30 ** 4 + t40 ** 4)
        pref_wp = mp.pi * t30 * t40

        def wp_r(z: mp.mpc) -> mp.mpc:
            return e1_val + (pref_wp * mp.jtheta(2, mp.pi * z, q_r) / mp.jtheta(1, mp.pi * z, q_r)) ** 2

        # Sanity check wp_r double periodicity & Laurent leading term
        z_chk = q_mp(3, 10) + I_MP * q_mp(1, 2)
        wp_per_err = max(
            abs(wp_r(z_chk + mp.mpf(1)) - wp_r(z_chk)),
            abs(wp_r(z_chk + tau_r) - wp_r(z_chk)),
        )
        z_small = q_mp(1, 1000)
        wp_laurent_err = abs((z_small ** 2) * wp_r(z_small) - mp.mpf(1))

        z0 = (mp.mpf(1) + tau_r) / mp.mpf(2)

        def monodromy_k38(c_val: mp.mpc, na: int, nb: int) -> tuple[list[list[mp.mpc]], list[list[mp.mpc]]]:
            def coeff_a(t: mp.mpf) -> list[list[mp.mpc]]:
                z = z0 + t
                qv = wp_r(z) / mp.mpf(4) + c_val
                return [[mp.mpc(0, 0), mp.mpc(1, 0)], [-qv, mp.mpc(0, 0)]]

            def coeff_b(t: mp.mpf) -> list[list[mp.mpc]]:
                z = z0 + t * tau_r
                qv = wp_r(z) / mp.mpf(4) + c_val
                return [[mp.mpc(0, 0), tau_r], [-tau_r * qv, mp.mpc(0, 0)]]

            ma = kutta38_mat2(coeff_a, mp.mpf(0), mp.mpf(1), mat2_eye(), na)
            mb = kutta38_mat2(coeff_b, mp.mpf(0), mp.mpf(1), mat2_eye(), nb)
            return ma, mb

        def monodromy_rich(c_val: mp.mpc, na: int, nb: int) -> tuple[list[list[mp.mpc]], list[list[mp.mpc]]]:
            ma1, mb1 = monodromy_k38(c_val, na, nb)
            ma2, mb2 = monodromy_k38(c_val, 2 * na, 2 * nb)
            c16, c15 = mp.mpf(16), mp.mpf(15)
            ma = [[(c16 * ma2[i][j] - ma1[i][j]) / c15 for j in range(2)] for i in range(2)]
            mb = [[(c16 * mb2[i][j] - mb1[i][j]) / c15 for j in range(2)] for i in range(2)]
            return ma, mb

        def fuchs_resid(c_val: mp.mpc, use_rich: bool, na: int, nb: int) -> tuple[list[mp.mpf], list[list[mp.mpc]], list[list[mp.mpc]]]:
            ma, mb = monodromy_rich(c_val, na, nb) if use_rich else monodromy_k38(c_val, na, nb)
            mab = mat2_mul(ma, mb)
            res = [
                mp.im(ma[0][0] + ma[1][1]),
                mp.im(mb[0][0] + mb[1][1]),
                mp.im(mab[0][0] + mab[1][1]),
            ]
            return res, ma, mb

        # Solve accessory parameter c_* via 3-trace Gauss-Newton starting from cusp seed pi^2/12
        c_cur = (mp.pi ** 2) / mp.mpf(12)
        h_fd = p10(-7)
        for it in range(9):
            use_rich = it >= 5
            na_it, nb_it = (48, 80) if not use_rich else (64, 128)
            f0, ma_cur, mb_cur = fuchs_resid(c_cur, use_rich, na_it, nb_it)
            if max(abs(x) for x in f0) < p10(-11) and use_rich:
                break
            fr, _, _ = fuchs_resid(c_cur + h_fd, use_rich, na_it, nb_it)
            fi, _, _ = fuchs_resid(c_cur + I_MP * h_fd, use_rich, na_it, nb_it)
            j00 = (fr[0] - f0[0]) / h_fd
            j10 = (fr[1] - f0[1]) / h_fd
            j20 = (fr[2] - f0[2]) / h_fd
            j01 = (fi[0] - f0[0]) / h_fd
            j11 = (fi[1] - f0[1]) / h_fd
            j21 = (fi[2] - f0[2]) / h_fd
            # Normal equations (J^T J) dx = -J^T f0
            a00 = j00 * j00 + j10 * j10 + j20 * j20
            a01 = j00 * j01 + j10 * j11 + j20 * j21
            a11 = j01 * j01 + j11 * j11 + j21 * j21
            b0 = -(j00 * f0[0] + j10 * f0[1] + j20 * f0[2])
            b1 = -(j01 * f0[0] + j11 * f0[1] + j21 * f0[2])
            det_jtj = a00 * a11 - a01 * a01
            dcr = (a11 * b0 - a01 * b1) / det_jtj
            dci = (-a01 * b0 + a00 * b1) / det_jtj
            c_cur = c_cur + dcr + I_MP * dci

        f_final, ma_fin, mb_fin = fuchs_resid(c_cur, True, 64, 128)
        tr_im_err = max(abs(x) for x in f_final)

        # Commutator check tr([M_a, M_b]) == -2
        def inv_sl2(m: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
            dt = m[0][0] * m[1][1] - m[0][1] * m[1][0]
            return [[m[1][1] / dt, -m[0][1] / dt], [-m[1][0] / dt, m[0][0] / dt]]

        comm = mat2_mul(mat2_mul(ma_fin, mb_fin), mat2_mul(inv_sl2(ma_fin), inv_sl2(mb_fin)))
        tr_comm_err = abs((comm[0][0] + comm[1][1]) + mp.mpf(2))

        # Solve unique Hermitian form H (det H = -1) satisfying M^* H M^T = H for M in {M_a, M_b}
        basis_h = [
            [[mp.mpc(1, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(0, 0)]],
            [[mp.mpc(0, 0), mp.mpc(1, 0)], [mp.mpc(1, 0), mp.mpc(0, 0)]],
            [[mp.mpc(0, 0), I_MP], [-I_MP, mp.mpc(0, 0)]],
            [[mp.mpc(0, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(1, 0)]],
        ]

        def mat2_conj(m: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
            return [[mp.conj(m[i][j]) for j in range(2)] for i in range(2)]

        def mat2_trans(m: list[list[mp.mpc]]) -> list[list[mp.mpc]]:
            return [[m[j][i] for j in range(2)] for i in range(2)]

        a_lin = mp.zeros(8, 4)
        for m_idx, m_mat in enumerate((ma_fin, mb_fin)):
            mc = mat2_conj(m_mat)
            mt = mat2_trans(m_mat)
            for j, bj in enumerate(basis_h):
                dj = mat2_add(mat2_mul(mc, mat2_mul(bj, mt)), mat2_scale(mp.mpc(-1, 0), bj))
                a_lin[4 * m_idx + 0, j] = mp.re(dj[0][0])
                a_lin[4 * m_idx + 1, j] = mp.re(dj[0][1])
                a_lin[4 * m_idx + 2, j] = mp.im(dj[0][1])
                a_lin[4 * m_idx + 3, j] = mp.re(dj[1][1])

        _, sv_h, vh_h = mp.svd_r(a_lin)
        h_coeffs = [vh_h[3, j] for j in range(4)]
        H_mat = [[mp.mpc(0, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(0, 0)]]
        for j in range(4):
            H_mat = mat2_add(H_mat, mat2_scale(h_coeffs[j], basis_h[j]))
        det_h_raw = mp.re(H_mat[0][0] * H_mat[1][1] - H_mat[0][1] * H_mat[1][0])
        H_mat = mat2_scale(mp.mpf(1) / mp.sqrt(-det_h_raw), H_mat)

        h_inv_err = max(
            mat2_frob(
                mat2_add(
                    mat2_mul(mat2_conj(ma_fin), mat2_mul(H_mat, mat2_trans(ma_fin))),
                    mat2_scale(mp.mpc(-1, 0), H_mat),
                )
            ),
            mat2_frob(
                mat2_add(
                    mat2_mul(mat2_conj(mb_fin), mat2_mul(H_mat, mat2_trans(mb_fin))),
                    mat2_scale(mp.mpc(-1, 0), H_mat),
                )
            ),
        )

        # 2D Gauss-Legendre + radial-log Kutta-3/8 quadrature over 2 half-parallelogram triangles
        n_s = 18
        n_u = 24
        t_max = mp.mpf(18)
        u_min = mp.mpf(1) / (mp.mpf(1) + t_max)
        s_raw, ws_raw = gauss_legendre_nodes_weights(n_s)
        u_raw, wu_raw = gauss_legendre_nodes_weights(n_u)

        # Map s from [-1, 1] to [-1/2, 1/2], sorted DESCENDING from +1/2 down to -1/2 (z0 is at s=+1/2!)
        s_nodes_weights = sorted(
            [(x / mp.mpf(2), w / mp.mpf(2)) for x, w in zip(s_raw, ws_raw)],
            key=lambda pair: pair[0],
            reverse=True,
        )
        # Map u from [-1, 1] to [u_min, 1], sorted DESCENDING so t = 1/u - 1 is ASCENDING
        half_span = (mp.mpf(1) - u_min) / mp.mpf(2)
        mid_u = (mp.mpf(1) + u_min) / mp.mpf(2)
        u_nodes_weights = sorted(
            [(mid_u + half_span * x, half_span * w) for x, w in zip(u_raw, wu_raw)],
            key=lambda pair: pair[0],
            reverse=True,
        )

        # Propagate Y(z) from z_a to z_b along straight segment via Kutta-3/8
        def prop_segment(z_start: mp.mpc, z_end: mp.mpc, y_start: list[list[mp.mpc]], max_dz: mp.mpf) -> list[list[mp.mpc]]:
            dz = z_end - z_start
            dist = abs(dz)
            if dist == 0:
                return y_start
            n_sub = int(mp.ceil(dist / max_dz))
            if n_sub < 2:
                n_sub = 2

            def coeff_seg(t: mp.mpf) -> list[list[mp.mpc]]:
                z = z_start + t * dz
                qv = wp_r(z) / mp.mpf(4) + c_cur
                return [[mp.mpc(0, 0), dz], [-dz * qv, mp.mpc(0, 0)]]

            return kutta38_mat2(coeff_seg, mp.mpf(0), mp.mpf(1), y_start, n_sub)

        # Spin-structure mode densities rho_k(z) at tau_8^+ for k in (4, 2, 3) matching [Q_J, Q_I, Q_K]
        sqrt_2im = mp.sqrt(mp.mpf(2) * im_tau)

        def rho_modes_tau8(z: mp.mpc) -> list[mp.mpf]:
            imz = mp.im(z)
            gfac = sqrt_2im * mp.exp(-mp.mpf(2) * mp.pi * (imz ** 2) / im_tau)
            pz = mp.pi * z
            return [
                gfac * (abs(mp.jtheta(4, pz, q_8)) ** 2),
                gfac * (abs(mp.jtheta(2, pz, q_8)) ** 2),
                gfac * (abs(mp.jtheta(3, pz, q_8)) ** 2),
            ]

        def quad_form_h(w0: mp.mpc, w1: mp.mpc) -> mp.mpf:
            return mp.re(
                mp.conj(w0) * (H_mat[0][0] * w0 + H_mat[0][1] * w1)
                + mp.conj(w1) * (H_mat[1][0] * w0 + H_mat[1][1] * w1)
            )

        area_flat = mp.mpf(0)
        area_gb = mp.mpf(0)
        flat_modes = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        dirac_s12 = [mp.mpf(0), mp.mpf(0), mp.mpf(0)]
        bc_samples: list[mp.mpf] = []
        max_dt_step = q_mp(1, 3)

        # Two boundary edges starting from z0 = 1/2 + tau_r/2:
        # Edge 1: Z(s) = 1/2 + s*tau_r, Edge 2: Z(s) = s + 1/2*tau_r
        for edge_id in (1, 2):
            z_prev = z0
            y_edge = mat2_eye()
            for s_val, w_s in s_nodes_weights:
                z_edge = (q_mp(1, 2) + s_val * tau_r) if edge_id == 1 else (s_val + q_mp(1, 2) * tau_r)
                y_edge = prop_segment(z_prev, z_edge, y_edge, q_mp(1, 20))
                z_prev = z_edge

                # Log-Frobenius scaled matrix Y_hat(0) = diag(1, Z) * Y(Z)
                y_hat = [
                    [y_edge[0][0], y_edge[0][1]],
                    [z_edge * y_edge[1][0], z_edge * y_edge[1][1]],
                ]
                t_prev = mp.mpf(0)

                def coeff_radial(t_val: mp.mpf, ze: mp.mpc = z_edge) -> list[list[mp.mpc]]:
                    z_loc = mp.exp(-t_val) * ze
                    z2q = (z_loc ** 2) * (wp_r(z_loc) / mp.mpf(4) + c_cur)
                    return [[q_mp(1, 2), mp.mpc(-1, 0)], [z2q, q_mp(-1, 2)]]

                ray_weight = im_tau * w_s  # factor 2 (z <-> -z) * (1/2 * im_tau)
                for u_val, w_u in u_nodes_weights:
                    t_cur = mp.mpf(1) / u_val - mp.mpf(1)
                    dt_seg = t_cur - t_prev
                    n_rsub = int(mp.ceil(dt_seg / max_dt_step))
                    if n_rsub < 1:
                        n_rsub = 1
                    y_hat = kutta38_mat2(coeff_radial, t_prev, t_cur, y_hat, n_rsub)
                    t_prev = t_cur

                    jac_t = w_u / (u_val ** 2)
                    wt = ray_weight * jac_t
                    z_pt = mp.exp(-t_cur) * z_edge
                    qh = abs(quad_form_h(y_hat[0][0], y_hat[0][1]))
                    em_t = mp.exp(-t_cur)
                    em_2t = em_t * em_t
                    rhos = rho_modes_tau8(z_pt)

                    area_flat += wt * em_2t
                    area_gb += wt * (mp.mpf(4) / (qh * qh))
                    for k_idx in range(3):
                        flat_modes[k_idx] += wt * em_2t * rhos[k_idx] / im_tau
                        dirac_s12[k_idx] += wt * em_t * (mp.mpf(2) / qh) * rhos[k_idx]

                # March to t_max for exact analytic Gauss-Bonnet cusp tail and b_c^* extraction
                if t_max > t_prev:
                    n_tail = int(mp.ceil((t_max - t_prev) / max_dt_step))
                    if n_tail < 1:
                        n_tail = 1
                    y_hat = kutta38_mat2(coeff_radial, t_prev, t_max, y_hat, n_tail)

                f_end = quad_form_h(y_hat[0][0], y_hat[0][1])
                w_pr0 = q_mp(1, 2) * y_hat[0][0] - y_hat[1][0]
                w_pr1 = q_mp(1, 2) * y_hat[0][1] - y_hat[1][1]
                df_end = mp.mpf(2) * mp.re(
                    mp.conj(w_pr0) * (H_mat[0][0] * y_hat[0][0] + H_mat[0][1] * y_hat[0][1])
                    + mp.conj(w_pr1) * (H_mat[1][0] * y_hat[0][0] + H_mat[1][1] * y_hat[0][1])
                )
                sgn_f = mp.mpf(1) if f_end >= 0 else mp.mpf(-1)
                slope_a = sgn_f * df_end
                area_gb += ray_weight * (mp.mpf(4) / (slope_a * abs(f_end)))
                bc_est = abs(f_end) / (mp.mpf(2) * abs(z_edge)) - t_max + mp.log(abs(z_edge))
                bc_samples.append(bc_est)

        g_mean = (dirac_s12[0] + dirac_s12[1] + dirac_s12[2]) / mp.mpf(3)
        g_um = [val / g_mean for val in dirac_s12]
        gb_rel_err = abs(area_gb / (mp.mpf(2) * mp.pi) - mp.mpf(1))
        flat_area_rel_err = abs(area_flat / im_tau - mp.mpf(1))
        flat_mode_err = max(abs(val - mp.mpf(1)) for val in flat_modes)
        bc_avg = sum(bc_samples) / mp.mpf(len(bc_samples))
        bc_spread = max(abs(x - bc_avg) for x in bc_samples)

        return {
            "g_um": g_um,
            "c_star": c_cur,
            "wp_periodicity_err": wp_per_err,
            "wp_laurent_err": wp_laurent_err,
            "tr_im_err": tr_im_err,
            "tr_comm_err": tr_comm_err,
            "h_invariance_err": h_inv_err,
            "gauss_bonnet_rel_err": gb_rel_err,
            "flat_area_rel_err": flat_area_rel_err,
            "flat_mode_norm_err": flat_mode_err,
            "bc_star_avg": bc_avg,
            "bc_star_ray_spread": bc_spread,
        }


def build_frame_c_jtheta_tools():
    """Pure mp.jtheta Frame-C holomorphic Szego Yukawa engine (zero hand-summed q-series)."""
    qi = mp.matrix([[I_MP, mp.mpf(0)], [mp.mpf(0), -I_MP]])
    qj = mp.matrix([[mp.mpf(0), mp.mpf(1)], [mp.mpf(-1), mp.mpf(0)]])
    qk = mp.matrix([[mp.mpf(0), I_MP], [I_MP, mp.mpf(0)]])
    eps = qj
    blocks = [qj, qi, qk]
    edual = {
        "1": qj / mp.mpf(2),
        "i": qk / mp.mpf(2),
        "j": -mp.eye(2) / mp.mpf(2),
        "k": -qi / mp.mpf(2),
    }

    def theta_char_jtheta(alpha: Frac, beta: Frac, tau: mp.mpc, q: mp.mpc) -> mp.mpc:
        # Exact identity: theta_c(alpha + m, beta) == theta_c(alpha, beta) for any integer m
        # Reduce alpha to [-1/2, 1/2) while keeping beta exact (unreduced!)
        m = (alpha + Frac(1, 2)).numerator // (alpha + Frac(1, 2)).denominator
        a0_f = alpha - Frac(m, 1)
        a0 = q_mp(a0_f.numerator, a0_f.denominator)
        bt = q_mp(beta.numerator, beta.denominator)
        phase = mp.exp(I_MP * mp.pi * (a0 ** 2) * tau + mp.mpf(2) * I_MP * mp.pi * a0 * bt)
        return phase * mp.jtheta(3, mp.pi * (a0 * tau + bt), q)

    def higgs_s_jtheta(tau: mp.mpc, q: mp.mpc) -> mp.matrix:
        # Exact heat equation: d/d(2*pi*i*tau) theta_a(0,q) = -(1/8) theta_a''(0,q)
        th2 = mp.jtheta(2, mp.mpf(0), q)
        th3 = mp.jtheta(3, mp.mpf(0), q)
        th4 = mp.jtheta(4, mp.mpf(0), q)
        d2 = -mp.jtheta(2, mp.mpf(0), q, derivative=2) / (mp.mpf(8) * th2)
        d3 = -mp.jtheta(3, mp.mpf(0), q, derivative=2) / (mp.mpf(8) * th3)
        d4 = -mp.jtheta(4, mp.mpf(0), q, derivative=2) / (mp.mpf(8) * th4)
        denom = mp.pi * th2 * th3 * th4  # == 2 * pi * eta(tau)^3
        r_h = [-(th2 ** 2) / denom, -(th4 ** 2) / denom, I_MP * (th3 ** 2) / denom]
        c_vec = [
            r_h[0] * (mp.mpf(2) / mp.mpf(3)) * (mp.mpf(2) * d2 - d3 - d4),
            r_h[1] * (mp.mpf(2) / mp.mpf(3)) * (mp.mpf(2) * d4 - d2 - d3),
            r_h[2] * (mp.mpf(2) / mp.mpf(3)) * (mp.mpf(2) * d3 - d2 - d4),
        ]
        return c_vec[0] * qi + c_vec[1] * qj + c_vec[2] * qk

    def is_int_frac(f: Frac) -> bool:
        return f.denominator == 1

    def eval_w_hol_point(tau: mp.mpc, p_a: Frac, p_b: Frac, ql: int, qr: int) -> tuple[mp.matrix, dict[str, mp.mpc]]:
        q = mp.exp(I_MP * mp.pi * tau)
        th2 = mp.jtheta(2, mp.mpf(0), q)
        th3 = mp.jtheta(3, mp.mpf(0), q)
        th4 = mp.jtheta(4, mp.mpf(0), q)
        denom = mp.pi * th2 * th3 * th4
        s_mat = higgs_s_jtheta(tau, q)

        x0 = Frac(ql, 1) * p_a
        a_plus = Frac(ql + qr, 1) * p_a
        a_minus = Frac(ql - qr, 1) * p_a
        b_plus = Frac(ql + qr, 1) * p_b
        b_minus = Frac(ql - qr, 1) * p_b
        hh = Frac(1, 2)
        e_fac = mp.exp(-mp.mpf(2) * I_MP * mp.pi * q_mp(x0.numerator, x0.denominator))
        kappas = {"1": -I_MP * e_fac, "i": mp.mpc(-1, 0), "j": -e_fac, "k": I_MP}
        chars = {
            "1": ((a_plus + hh, b_plus + hh), (a_minus + hh, b_minus + hh)),
            "i": ((a_plus + hh, b_plus), (a_minus + hh, b_minus)),
            "j": ((a_plus, b_plus + hh), (a_minus, b_minus + hh)),
            "k": ((a_plus, b_plus), (a_minus, b_minus)),
        }
        r_ch: dict[str, mp.mpc] = {}
        mw = mp.zeros(2, 2)
        for ch_key in ("1", "i", "j", "k"):
            (ca, cb), (da, db) = chars[ch_key]
            if (is_int_frac(ca - hh) and is_int_frac(cb - hh)) or (
                is_int_frac(da - hh) and is_int_frac(db - hh)
            ):
                val = mp.mpc(0, 0)
            else:
                val = kappas[ch_key] * theta_char_jtheta(ca, cb, tau, q) * theta_char_jtheta(da, db, tau, q) / denom
            r_ch[ch_key] = val
            mw = mw + val * edual[ch_key]

        w_mat = mp.zeros(3, 3)
        es = eps * s_mat
        for r_i in range(3):
            for c_j in range(3):
                m_blk = blocks[r_i].T * es * blocks[c_j]
                w_mat[r_i, c_j] = (
                    m_blk[0, 0] * mw[0, 0]
                    + m_blk[0, 1] * mw[0, 1]
                    + m_blk[1, 0] * mw[1, 0]
                    + m_blk[1, 1] * mw[1, 1]
                )
        return w_mat, r_ch

    def eval_w_hol_x0x1_direct(tau: mp.mpc, p_a: Frac, p_b: Frac, ql: int, qr: int) -> mp.matrix:
        """Disjoint check via direct level-2 X_0, X_1 bilinear sum (WG96 Erratum 2)."""
        q = mp.exp(I_MP * mp.pi * tau)
        th2 = mp.jtheta(2, mp.mpf(0), q)
        th3 = mp.jtheta(3, mp.mpf(0), q)
        th4 = mp.jtheta(4, mp.mpf(0), q)
        denom = mp.pi * th2 * th3 * th4
        s_mat = higgs_s_jtheta(tau, q)
        ax = q_mp((Frac(ql, 1) * p_a).numerator, (Frac(ql, 1) * p_a).denominator)
        bx = q_mp((Frac(2 * ql, 1) * p_b).numerator, (Frac(2 * ql, 1) * p_b).denominator)
        ay = q_mp((Frac(qr, 1) * p_a).numerator, (Frac(qr, 1) * p_a).denominator)
        by = q_mp((Frac(2 * qr, 1) * p_b).numerator, (Frac(2 * qr, 1) * p_b).denominator)

        def x0_sum(al: mp.mpf, bt: mp.mpf) -> mp.mpc:
            n_ctr = int(mp.floor(al + q_mp(1, 2)))
            tot = mp.mpc(0, 0)
            for k in range(-22 - n_ctr, 23 - n_ctr):
                nv = mp.mpf(k) + al
                tot += mp.exp(mp.mpf(2) * I_MP * mp.pi * tau * (nv ** 2) + mp.mpf(2) * I_MP * mp.pi * nv * bt)
            return tot

        def x1_sum(al: mp.mpf, bt: mp.mpf) -> mp.mpc:
            n_ctr = int(mp.floor(al + mp.mpf(1)))
            tot = mp.mpc(0, 0)
            for k in range(-22 - n_ctr, 23 - n_ctr):
                nv = mp.mpf(k) + al
                tot += mp.exp(
                    mp.mpf(2) * I_MP * mp.pi * tau * ((nv + q_mp(1, 2)) ** 2)
                    + mp.mpf(2) * I_MP * mp.pi * nv * bt
                )
            return tot

        x0x, x1x = x0_sum(ax, bx), x1_sum(ax, bx)
        x0y, x1y = x0_sum(ay, by), x1_sum(ay, by)
        m_m = mp.matrix([
            [x0x * x0y, -I_MP * mp.exp(I_MP * mp.pi * by) * x0x * x1y],
            [-I_MP * mp.exp(I_MP * mp.pi * bx) * x1x * x0y, -mp.exp(I_MP * mp.pi * (bx + by)) * x1x * x1y],
        ]) / denom
        ec_list = [qj, -qk, -mp.eye(2), qi]
        r_vals = [
            ec[0, 0] * m_m[0, 0] + ec[0, 1] * m_m[0, 1] + ec[1, 0] * m_m[1, 0] + ec[1, 1] * m_m[1, 1]
            for ec in ec_list
        ]
        mw = (
            r_vals[0] * edual["1"]
            + r_vals[1] * edual["i"]
            + r_vals[2] * edual["j"]
            + r_vals[3] * edual["k"]
        )
        w_mat = mp.zeros(3, 3)
        es = eps * s_mat
        for r_i in range(3):
            for c_j in range(3):
                m_blk = blocks[r_i].T * es * blocks[c_j]
                w_mat[r_i, c_j] = (
                    m_blk[0, 0] * mw[0, 0]
                    + m_blk[0, 1] * mw[0, 1]
                    + m_blk[1, 0] * mw[1, 0]
                    + m_blk[1, 1] * mw[1, 1]
                )
        return w_mat

    return eval_w_hol_point, eval_w_hol_x0x1_direct


def takagi_svd_c_asc(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf], mp.mpf]:
    """Takagi factorization M = U_T diag(s) U_T^T via mp.svd_c with explicit V^H transposition."""
    ms = (m_sym + m_sym.T) / mp.mpf(2)
    u_raw, s_raw, vh_raw = mp.svd_c(ms)
    order = sorted(range(3), key=lambda k: s_raw[k])
    s_asc = [s_raw[k] for k in order]
    u_asc = mp.zeros(3, 3)
    vh_asc = mp.zeros(3, 3)
    for col_new, col_old in enumerate(order):
        for r in range(3):
            u_asc[r, col_new] = u_raw[r, col_old]
            vh_asc[col_new, r] = vh_raw[col_old, r]
    # Explicit V^H transposition: V_h^T = V^* = U_s * D^2 => Z = U_s^H * V_h^T = D^2
    z_mat = u_asc.H * vh_asc.T
    phases = [mp.exp(I_MP * mp.arg(z_mat[k, k]) / mp.mpf(2)) for k in range(3)]
    u_t = u_asc * mp.diag(phases)
    recon_err = mp.norm(ms - u_t * mp.diag(s_asc) * u_t.T)
    return u_t, s_asc, recon_err


def takagi_real6_eigsy_asc(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf], mp.mpf]:
    """Disjoint Takagi via 6x6 real symmetric block matrix [[Re M, Im M], [Im M, -Re M]]."""
    ms = (m_sym + m_sym.T) / mp.mpf(2)
    b6 = mp.zeros(6, 6)
    for i in range(3):
        for j in range(3):
            re_v = mp.re(ms[i, j])
            im_v = mp.im(ms[i, j])
            b6[i, j] = re_v
            b6[i, j + 3] = im_v
            b6[i + 3, j] = im_v
            b6[i + 3, j + 3] = -re_v
    evals, evecs = mp.eigsy(b6)
    pos_idx = [k for k in range(6) if evals[k] > 0]
    pos_idx.sort(key=lambda k: evals[k])
    pos_idx = pos_idx[-3:]
    s_asc = [evals[k] for k in pos_idx]
    u_t = mp.zeros(3, 3)
    for col, k in enumerate(pos_idx):
        for r in range(3):
            u_t[r, col] = mp.mpc(evecs[r, k], evecs[r + 3, k])
    recon_err = mp.norm(ms - u_t * mp.diag(s_asc) * u_t.T)
    return u_t, s_asc, recon_err


def extract_pmns_obs(
    ye: mp.matrix,
    ynu: mp.matrix,
    mr: mp.matrix,
    buggy_conj: bool = False,
    takagi_fn=takagi_svd_c_asc,
) -> dict[str, mp.mpf]:
    he = ye * ye.H
    he = (he + he.H) / mp.mpf(2)
    _, ue = mp.eighe(he)
    mnu = -(ynu * (mr ** (-1)) * ynu.T)
    mnu = (mnu + mnu.T) / mp.mpf(2)
    ut, s_asc, tak_err = takagi_fn(mnu)
    if buggy_conj:
        ut_use = mp.matrix([[mp.conj(ut[r, c]) for c in range(3)] for r in range(3)])
    else:
        ut_use = ut
    up = ue.H * ut_use
    s13_sq = abs(up[0, 2]) ** 2
    s12_sq = (abs(up[0, 1]) ** 2) / (mp.mpf(1) - s13_sq)
    s23_sq = (abs(up[1, 2]) ** 2) / (mp.mpf(1) - s13_sq)
    j_pmns = mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1]))
    dm_ratio = (s_asc[1] ** 2 - s_asc[0] ** 2) / (s_asc[2] ** 2 - s_asc[0] ** 2)
    return {
        "s12_sq": s12_sq,
        "s23_sq": s23_sq,
        "s13_sq": s13_sq,
        "J_PMNS": j_pmns,
        "dm21_over_dm31": dm_ratio,
        "takagi_err": tak_err,
    }


def make_haar_unitary_3(state: list[int]) -> mp.matrix:
    """Deterministic zero-float Haar U(3) via Xorshift64* + Box-Muller + Mezzadri QR."""
    mask64 = (1 << 64) - 1
    mul_const = 2685821657736338717
    den53 = mp.mpf((1 << 53) + 2)

    def next_u01() -> mp.mpf:
        x = state[0]
        x ^= (x >> 12) & mask64
        x ^= (x << 25) & mask64
        x ^= (x >> 27) & mask64
        state[0] = x
        val = (x * mul_const) & mask64
        return mp.mpf((val >> 11) + 1) / den53

    g = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            u1 = next_u01()
            u2 = next_u01()
            rad = mp.sqrt(-mp.mpf(2) * mp.log(u1))
            ang = mp.mpf(2) * mp.pi * u2
            g[r, c] = rad * (mp.cos(ang) + I_MP * mp.sin(ang))

    # Modified Gram-Schmidt with Mezzadri diagonal phase fix
    q_cols: list[list[mp.mpc]] = []
    for c in range(3):
        v = [g[r, c] for r in range(3)]
        for prev in q_cols:
            dot = sum(mp.conj(prev[r]) * v[r] for r in range(3))
            v = [v[r] - dot * prev[r] for r in range(3)]
        nrm = mp.sqrt(sum(abs(x) ** 2 for x in v))
        v = [x / nrm for x in v]
        q_cols.append(v)

    q_mat = mp.zeros(3, 3)
    for c in range(3):
        # Diagonal R_{cc} = <q_c, g_c>
        rcc = sum(mp.conj(q_cols[c][r]) * g[r, c] for r in range(3))
        ph = rcc / abs(rcc)
        for r in range(3):
            q_mat[r, c] = q_cols[c][r] * ph
    return q_mat


def hits_ow24_window_strict(obs: dict[str, mp.mpf]) -> bool:
    return bool(
        q_mp(3, 20) < obs["s12_sq"] < q_mp(11, 20)
        and q_mp(7, 20) < obs["s23_sq"] < q_mp(13, 20)
        and q_mp(1, 100) < obs["s13_sq"] < q_mp(1, 20)
        and q_mp(1, 200) < obs["dm21_over_dm31"] < q_mp(3, 20)
    )


def hits_ow24_window_broad(obs: dict[str, mp.mpf]) -> bool:
    return bool(
        q_mp(3, 20) < obs["s12_sq"] < q_mp(11, 20)
        and q_mp(3, 10) < obs["s23_sq"] < q_mp(7, 10)
        and obs["s13_sq"] < q_mp(2, 25)
        and q_mp(1, 200) < obs["dm21_over_dm31"] < q_mp(3, 20)
    )


def run_r_p135_c(prod_c: dict, repo_root: pathlib.Path) -> tuple[dict, list[str]]:
    discrepancies: list[str] = []

    # 1. Independently compute G^(s=1/2)(tau_8^+) using Kutta-3/8 Fuchsian ODE
    fuchs_info = compute_dirac_s12_gramian_kutta38()
    g_ref_k38 = fuchs_info["g_um"]

    with mp.workdps(55):
        g_ref_55 = [mp.mpf(mp.nstr(v, 25)) for v in g_ref_k38]
        g_prod_55 = [mp.mpf(s) for s in prod_c["dirac_s12_gramian_tau8"]]
        gramian_max_diff = max(abs(g_ref_55[i] - g_prod_55[i]) for i in range(3))

        tau8 = q_mp(16, 5) + I_MP * q_mp(8, 5)
        eps5 = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau8 / mp.mpf(5))
        eval_w_pt, eval_w_x0x1 = build_frame_c_jtheta_tools()

        k5_pts = [(Frac(1, 5), Frac(2, 5)), (Frac(4, 5), Frac(3, 5)), (Frac(2, 5), Frac(4, 5)), (Frac(3, 5), Frac(1, 5))]
        k6_plus = [(Frac(1, 6), Frac(1, 6)), (Frac(5, 6), Frac(5, 6))]
        k6_minus = [(Frac(1, 6), Frac(5, 6)), (Frac(5, 6), Frac(1, 6))]

        # Cross-check single-point mp.jtheta vs disjoint level-2 X_0/X_1 sum AND Riemann null quadric sum R_s^2 == 0
        w_jth_chk, r_ch_chk = eval_w_pt(tau8, Frac(1, 5), Frac(2, 5), -3, 6)
        w_x01_chk = eval_w_x0x1(tau8, Frac(1, 5), Frac(2, 5), -3, 6)
        jtheta_vs_x0x1_err = mp.norm(w_jth_chk - w_x01_chk)
        riemann_null_err = abs(sum(r_ch_chk[k] ** 2 for k in ("1", "i", "j", "k")))

        def avg_orbit(pts: list[tuple[Frac, Frac]], ql: int, qr: int) -> mp.matrix:
            tot = mp.zeros(3, 3)
            for pa, pb in pts:
                w_m, _ = eval_w_pt(tau8, pa, pb, ql, qr)
                tot = tot + w_m
            return tot / mp.mpf(len(pts))

        def sector_mats(k6_pts: list[tuple[Frac, Frac]]) -> tuple[mp.matrix, mp.matrix, mp.matrix]:
            we = (avg_orbit(k5_pts, -3, 6) + avg_orbit(k6_pts, -3, 6)) / mp.mpf(2)
            wnu = (avg_orbit(k5_pts, 3, -5) + avg_orbit(k6_pts, 3, -5)) / mp.mpf(2)
            wr = (avg_orbit(k5_pts, 3, 3) + avg_orbit(k6_pts, 3, 3)) / mp.mpf(2)
            wrs = (wr + wr.T) / mp.mpf(2)
            _, svr, _ = mp.svd_c(wrs)
            mr = mp.eye(3) + wrs / max(svr)
            return we, wnu, mr

        we_p, wnu_p, mr_p = sector_mats(k6_plus)
        we_m, wnu_m, mr_m = sector_mats(k6_minus)

        case_specs = [
            ("K6_plus_302_asym_ynu_agyexp_claim", we_p, wnu_p, mr_p, (3, 0, 2), False),
            ("K6_plus_302_sym_ynu_LINK8_convention", we_p, wnu_p, mr_p, (3, 0, 2), True),
            ("K6_plus_320_asym_ynu_control", we_p, wnu_p, mr_p, (3, 2, 0), False),
            ("K6_plus_000_no_D10_dressing", we_p, wnu_p, mr_p, (0, 0, 0), False),
            ("K6_minus_302_asym_ynu_FL8_F3_twin", we_m, wnu_m, mr_m, (3, 0, 2), False),
            ("K6_minus_320_asym_ynu_FL8_F3_twin", we_m, wnu_m, mr_m, (3, 2, 0), False),
        ]

        kis_ref = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_ref_55])
        kis_prod = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_prod_55])

        cases_out: dict[str, dict] = {}
        max_diff_indep_vs_prod = mp.mpf(0)
        max_diff_sameG_vs_prod = mp.mpf(0)
        max_diff_svd_vs_eigsy_sameG = mp.mpf(0)
        max_takagi_err = mp.mpf(0)
        all_window_flags_match = True

        for name, we_m_loc, wnu_m_loc, mr_m_loc, n10, sym_ynu in case_specs:
            d10 = mp.diag([eps5 ** n for n in n10])
            ye_ref = kis_ref * we_m_loc * d10 * kis_ref
            ynu_ref = (kis_ref * wnu_m_loc * kis_ref) if sym_ynu else (kis_ref * wnu_m_loc)
            obs_ref = extract_pmns_obs(ye_ref, ynu_ref, mr_m_loc, buggy_conj=False, takagi_fn=takagi_svd_c_asc)

            ye_sg = kis_prod * we_m_loc * d10 * kis_prod
            ynu_sg = (kis_prod * wnu_m_loc * kis_prod) if sym_ynu else (kis_prod * wnu_m_loc)
            obs_sg_svd = extract_pmns_obs(ye_sg, ynu_sg, mr_m_loc, buggy_conj=False, takagi_fn=takagi_svd_c_asc)
            obs_sg_eig = extract_pmns_obs(ye_sg, ynu_sg, mr_m_loc, buggy_conj=False, takagi_fn=takagi_real6_eigsy_asc)

            p_case = prod_c["cases"][name]
            obs_keys = ("s12_sq", "s23_sq", "s13_sq", "dm21_over_dm31", "J_PMNS")
            d_indep = max(abs(obs_ref[k] - mp.mpf(p_case[k])) for k in obs_keys)
            d_sameg = max(abs(obs_sg_svd[k] - mp.mpf(p_case[k])) for k in obs_keys)
            d_svd_eig = max(abs(obs_sg_svd[k] - obs_sg_eig[k]) for k in obs_keys)

            if d_indep > max_diff_indep_vs_prod:
                max_diff_indep_vs_prod = d_indep
            if d_sameg > max_diff_sameG_vs_prod:
                max_diff_sameG_vs_prod = d_sameg
            if d_svd_eig > max_diff_svd_vs_eigsy_sameG:
                max_diff_svd_vs_eigsy_sameG = d_svd_eig
            if obs_ref["takagi_err"] > max_takagi_err:
                max_takagi_err = obs_ref["takagi_err"]

            hit_strict = hits_ow24_window_strict(obs_ref)
            hit_broad = hits_ow24_window_broad(obs_ref)
            if hit_strict != bool(p_case["hits_ow24_window"]) or hit_broad != bool(p_case["hits_ow24_window"]):
                all_window_flags_match = False

            cases_out[name] = {
                "s12_sq": mstr(obs_ref["s12_sq"], 12),
                "s23_sq": mstr(obs_ref["s23_sq"], 12),
                "s13_sq": mstr(obs_ref["s13_sq"], 12),
                "dm21_over_dm31": mstr(obs_ref["dm21_over_dm31"], 12),
                "J_PMNS": mstr(obs_ref["J_PMNS"], 12),
                "takagi_svd_c_err": mstr(obs_ref["takagi_err"], 8),
                "hits_ow24_window_strict": hit_strict,
                "hits_ow24_window_broad": hit_broad,
                "max_diff_indep_G_vs_producer": mstr(d_indep, 8),
                "max_diff_same_G_vs_producer_10d": mstr(d_sameg, 8),
                "max_diff_svd_c_vs_eigsy6_same_G": mstr(d_svd_eig, 8),
            }

        # 10-trial random Haar U(3)_L x U(3)_eR x U(3)_nuR scrambling test (Guardrail 3)
        d10_302 = mp.diag([eps5 ** 3, mp.mpc(1, 0), eps5 ** 2])
        ye_base = kis_ref * we_p * d10_302 * kis_ref
        ynu_base = kis_ref * wnu_p
        base_true = extract_pmns_obs(ye_base, ynu_base, mr_p, buggy_conj=False)
        base_buggy = extract_pmns_obs(ye_base, ynu_base, mr_p, buggy_conj=True)

        prng_state = [0x9E3779B97F4A7C15]
        haar_true_max_err = mp.mpf(0)
        haar_buggy_max_err = mp.mpf(0)
        max_unitarity_err = mp.mpf(0)
        for _trial in range(10):
            ul = make_haar_unitary_3(prng_state)
            uer = make_haar_unitary_3(prng_state)
            unur = make_haar_unitary_3(prng_state)
            u_err = max(
                mp.norm(ul.H * ul - mp.eye(3)),
                mp.norm(uer.H * uer - mp.eye(3)),
                mp.norm(unur.H * unur - mp.eye(3)),
            )
            if u_err > max_unitarity_err:
                max_unitarity_err = u_err

            ye_rot = ul * ye_base * uer.H
            ynu_rot = ul * ynu_base * unur.T
            mr_rot = unur * mr_p * unur.T

            rot_true = extract_pmns_obs(ye_rot, ynu_rot, mr_rot, buggy_conj=False)
            rot_buggy = extract_pmns_obs(ye_rot, ynu_rot, mr_rot, buggy_conj=True)
            obs_keys = ("s12_sq", "s23_sq", "s13_sq", "dm21_over_dm31", "J_PMNS")
            err_t = max(abs(rot_true[k] - base_true[k]) for k in obs_keys)
            err_b = max(abs(rot_buggy[k] - base_buggy[k]) for k in ("s12_sq", "s23_sq", "s13_sq"))
            if err_t > haar_true_max_err:
                haar_true_max_err = err_t
            if err_b > haar_buggy_max_err:
                haar_buggy_max_err = err_b

        # Verify A2-OW26-F1 directly from sealed LOCK_V3 on disk
        ow27_path = repo_root / "relays" / "a2_ow27_v8" / "a2_ow27_v8_results.json"
        ow27_j = json.loads(ow27_path.read_text(encoding="utf-8"))
        lock_v3 = ow27_j["OW27_E_planted_faults_and_blind_lock_v3"]["blind_prediction_lock_v3_B4_UV"]
        levers_claimed = int(lock_v3["priced_continuous_uv_levers_guardrail5"]["count_continuous_levers"])
        preds_v3 = lock_v3["dimensionless_MZ_and_mt_predictions_B4_UV_CURV_s12_Dirac"]
        a3_10v = mp.mpf(preds_v3["gauge_and_EW_at_MZ_m0_10v"]["alpha3_mz_nf5"])
        a3_3v = mp.mpf(preds_v3["gauge_and_EW_at_MZ_m0_3v"]["alpha3_mz_nf5"])
        m0_alpha3_shift = abs(a3_10v - a3_3v)
        a2_ow26_f1_confirmed = bool(levers_claimed == 5 and m0_alpha3_shift > q_mp(3, 100))

        # Check all gates
        passed = bool(
            fuchs_info["wp_periodicity_err"] < p10(-18)
            and fuchs_info["wp_laurent_err"] < p10(-8)
            and fuchs_info["tr_im_err"] < p10(-10)
            and fuchs_info["tr_comm_err"] < p10(-9)
            and fuchs_info["h_invariance_err"] < p10(-8)
            and fuchs_info["gauss_bonnet_rel_err"] < p10(-5)
            and fuchs_info["flat_area_rel_err"] < p10(-6)
            and fuchs_info["flat_mode_norm_err"] < p10(-6)
            and gramian_max_diff < p10(-5)
            and jtheta_vs_x0x1_err < p10(-40)
            and riemann_null_err < p10(-45)
            and max_takagi_err < p10(-45)
            and max_diff_indep_vs_prod < p10(-5)
            and max_diff_sameG_vs_prod < p10(-8)
            and max_diff_svd_vs_eigsy_sameG < p10(-40)
            and all_window_flags_match
            and max_unitarity_err < p10(-45)
            and haar_true_max_err < p10(-40)
            and haar_buggy_max_err > q_mp(1, 10)
            and a2_ow26_f1_confirmed
            and prod_c.get("passed") is True
        )
        if not passed:
            discrepancies.append("R_P135_C_FAILED_GATE")

        out = {
            "fuchsian_kutta38_gramian_tau8": [mstr(v, 12) for v in g_ref_55],
            "producer_gramian_tau8": prod_c["dirac_s12_gramian_tau8"],
            "gramian_max_diff_vs_producer": mstr(gramian_max_diff, 8),
            "fuchsian_diagnostics": {
                "c_star": mstr(fuchs_info["c_star"], 14),
                "bc_star_avg": mstr(fuchs_info["bc_star_avg"], 12),
                "bc_star_ray_spread": mstr(fuchs_info["bc_star_ray_spread"], 8),
                "wp_periodicity_err": mstr(fuchs_info["wp_periodicity_err"], 8),
                "wp_laurent_err": mstr(fuchs_info["wp_laurent_err"], 8),
                "tr_im_err": mstr(fuchs_info["tr_im_err"], 8),
                "tr_comm_err": mstr(fuchs_info["tr_comm_err"], 8),
                "h_invariance_err": mstr(fuchs_info["h_invariance_err"], 8),
                "gauss_bonnet_rel_err": mstr(fuchs_info["gauss_bonnet_rel_err"], 8),
                "flat_area_rel_err": mstr(fuchs_info["flat_area_rel_err"], 8),
                "flat_mode_norm_err": mstr(fuchs_info["flat_mode_norm_err"], 8),
            },
            "jtheta_vs_x0x1_direct_err": mstr(jtheta_vs_x0x1_err, 8),
            "single_point_riemann_null_quadric_err": mstr(riemann_null_err, 8),
            "max_takagi_svd_c_err": mstr(max_takagi_err, 8),
            "max_diff_indep_kutta38_vs_producer": mstr(max_diff_indep_vs_prod, 8),
            "max_diff_same_G_vs_producer_10d": mstr(max_diff_sameG_vs_prod, 8),
            "max_diff_svd_c_vs_eigsy6_same_G": mstr(max_diff_svd_vs_eigsy_sameG, 8),
            "all_6_ow24_window_flags_match": all_window_flags_match,
            "cases": cases_out,
            "haar_10trial_unitarity_err": mstr(max_unitarity_err, 8),
            "haar_10trial_true_UeH_UT_max_err": mstr(haar_true_max_err, 8),
            "haar_10trial_buggy_UeH_UTconj_max_err": mstr(haar_buggy_max_err, 8),
            "a2_ow26_f1_lock_v3_check": {
                "claimed_continuous_levers": levers_claimed,
                "alpha3_mz_nf5_m0_10v": mstr(a3_10v, 10),
                "alpha3_mz_nf5_m0_3v": mstr(a3_3v, 10),
                "alpha3_shift": mstr(m0_alpha3_shift, 10),
                "confirmed_6th_continuous_ratio": a2_ow26_f1_confirmed,
            },
            "passed": passed,
        }
        return out, discrepancies


# =============================================================================
# MODULE R_P135_D: 6/6 Referee Planted Fault Controls + Full Branch Audit
# =============================================================================

def run_r_p135_d(
    repo_root: pathlib.Path,
    res_a: dict,
    res_b: dict,
    res_c: dict,
) -> tuple[dict, list[str]]:
    discrepancies: list[str] = []

    # 1. Audit Producer v3 manifests, SHA-256 byte-for-byte, AST, sandbox-runnability, JSON floats
    prod_dir = repo_root / "relays" / "a2_p135_v3"
    prod_py = prod_dir / "verify_a2_p135_v3.py"
    prod_json = prod_dir / "a2_p135_v3_results.json"
    prod_s_mf = prod_dir / "SCRIPT_SHA256.txt"
    prod_o_mf = prod_dir / "OUTPUT_SHA256.txt"

    prod_py_bytes = prod_py.read_bytes()
    prod_json_bytes = prod_json.read_bytes()
    actual_prod_script_sha = hashlib.sha256(prod_py_bytes).hexdigest()
    actual_prod_output_sha = hashlib.sha256(prod_json_bytes).hexdigest()
    claimed_prod_script_sha = prod_s_mf.read_text(encoding="utf-8").strip().split()[0]
    claimed_prod_output_sha = prod_o_mf.read_text(encoding="utf-8").strip().split()[0]

    prod_script_sha_ok = (actual_prod_script_sha == claimed_prod_script_sha)
    prod_output_sha_ok = (actual_prod_output_sha == claimed_prod_output_sha)
    prod_ast_audit = audit_python_ast(prod_py, check_sandbox=True)
    prod_json_data = json.loads(prod_json_bytes.decode("utf-8"))
    prod_json_floats = assert_no_json_floats(prod_json_data)
    prod_internal_sha_ok = (prod_json_data.get("script_sha256") == actual_prod_script_sha)

    # 2. Full branch *SHA256*.txt manifest audit across relays/
    manifest_files = sorted(glob.glob(str(repo_root / "relays" / "**" / "*SHA256*.txt"), recursive=True))
    total_manifest_files = 0
    total_manifest_entries = 0
    manifest_mismatches: list[dict] = []

    for mf_str in manifest_files:
        mf_path = pathlib.Path(mf_str)
        total_manifest_files += 1
        mf_dir = mf_path.parent
        for line in mf_path.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = s.split()
            if len(parts) < 2:
                manifest_mismatches.append({"manifest": str(mf_path.relative_to(repo_root)), "reason": "malformed_line", "line": s})
                continue
            expected_hash = parts[0]
            rel_target = parts[1].lstrip("*")
            cand1 = mf_dir / rel_target
            cand2 = repo_root / rel_target
            target_path = cand1 if cand1.exists() else (cand2 if cand2.exists() else None)
            if target_path is None:
                manifest_mismatches.append({"manifest": str(mf_path.relative_to(repo_root)), "target": rel_target, "reason": "missing_file"})
                continue
            total_manifest_entries += 1
            got_hash = hashlib.sha256(target_path.read_bytes()).hexdigest()
            if got_hash != expected_hash:
                manifest_mismatches.append({
                    "manifest": str(mf_path.relative_to(repo_root)),
                    "target": rel_target,
                    "expected": expected_hash,
                    "actual": got_hash,
                })

    # 3. Git merge-base non-relay edit audit
    mb_proc = subprocess.run(
        ["git", "merge-base", "HEAD", "origin/main"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=True,
    )
    merge_base = mb_proc.stdout.strip()
    diff_proc = subprocess.run(
        ["git", "diff", "--name-only", f"{merge_base}..HEAD"],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        check=True,
    )
    changed_files = [ln.strip() for ln in diff_proc.stdout.splitlines() if ln.strip()]
    non_relay_edits = [p for p in changed_files if not p.startswith("relays/")]

    # 4. 6/6 Independent Referee Planted Fault Controls (RPF-1..6)
    with mp.workdps(40):
        # RPF-1: Filtered flat-side b=1/4, c=0 keeps tr M = -2 while breaking nilpotency (a.a = -1/16) & Betti weight != 0
        rpf1_caught = bool(
            res_a["filtered_b_quarter_c0"]["confirmed"]
            and abs(mp.mpf(res_a["filtered_b_quarter_c0"]["a_dot_a"]) + q_mp(1, 16)) < p10(-9)
        )
        # RPF-2: Wrong nilpotent coupling c0 = 1 breaks Hitchin eq AND breaks unipotent Jordan monodromy (||(M+I)^2|| >> 1)
        rpf2_caught = bool(
            res_a["nilpotent_jordan_kutta38"]["hitchin_symbolic_c0_one_nonzero"]
            and mp.mpf(res_a["nilpotent_jordan_kutta38"]["wrong_c0_one_norm_M_plus_I_sq"]) > mp.mpf(1)
        )
        # RPF-3: Dropping one doublet from h_Q breaks Ad(h_Q) == Ad(h_W) on 112/240 roots
        rpf3_caught = (res_b["rpf3_dropped_doublet_mismatches"] == 112)
        # RPF-4: Dropping e^c condition admits spurious (1/6, -1/3, 1/6) -> 9 > 6 solutions
        rpf4_caught = bool(
            res_b["rpf4_drop_ec_solution_count"] == 9
            and res_b["rpf4_spurious_16_neg13_16_present"]
        )
        # RPF-5: Buggy U_e^H conj(U_T) breaks 10-trial SU(2)_L Haar invariance by > 0.1
        rpf5_caught = bool(
            mp.mpf(res_c["haar_10trial_buggy_UeH_UTconj_max_err"]) > q_mp(1, 10)
            and mp.mpf(res_c["haar_10trial_true_UeH_UT_max_err"]) < p10(-40)
        )
        # RPF-6: Removing D_10, using (3,2,0), or swapping K_6^+ -> K_6^- fails OW24-C window + 1-byte SHA tamper caught
        tampered = bytearray(prod_py_bytes)
        tampered[0] ^= 1
        tamper_sha = hashlib.sha256(bytes(tampered)).hexdigest()
        rpf6_caught = bool(
            (not res_c["cases"]["K6_plus_000_no_D10_dressing"]["hits_ow24_window_broad"])
            and (not res_c["cases"]["K6_plus_320_asym_ynu_control"]["hits_ow24_window_broad"])
            and (not res_c["cases"]["K6_minus_302_asym_ynu_FL8_F3_twin"]["hits_ow24_window_broad"])
            and (tamper_sha != claimed_prod_script_sha)
        )

    rpf_controls = {
        "RPF_1_filtered_betti_weight_vs_nilpotency": rpf1_caught,
        "RPF_2_wrong_nilpotent_c0_breaks_hitchin_and_jordan": rpf2_caught,
        "RPF_3_dropped_doublet_breaks_ad_hQ_eq_ad_hW": rpf3_caught,
        "RPF_4_drop_ec_admits_spurious_9_solutions": rpf4_caught,
        "RPF_5_buggy_UeH_UTconj_breaks_haar_invariance": rpf5_caught,
        "RPF_6_no_D10_320_K6minus_fail_window_and_sha_tamper": rpf6_caught,
    }
    rpf_caught_count = sum(1 for v in rpf_controls.values() if v)

    passed = bool(
        prod_script_sha_ok
        and prod_output_sha_ok
        and prod_internal_sha_ok
        and prod_ast_audit["sandbox_runnable"]
        and len(prod_json_floats) == 0
        and len(manifest_mismatches) == 0
        and len(non_relay_edits) == 0
        and rpf_caught_count == 6
    )
    if not passed:
        discrepancies.append("R_P135_D_FAILED_GATE")

    out = {
        "producer_v3_custody_and_sandbox_audit": {
            "script_sha256_actual": actual_prod_script_sha,
            "script_sha256_manifest_match": prod_script_sha_ok,
            "script_sha256_internal_json_match": prod_internal_sha_ok,
            "output_sha256_actual": actual_prod_output_sha,
            "output_sha256_manifest_match": prod_output_sha_ok,
            "ast_audit": prod_ast_audit,
            "json_float_tokens": prod_json_floats,
        },
        "branch_manifest_audit": {
            "manifest_files_checked": total_manifest_files,
            "manifest_entries_verified": total_manifest_entries,
            "mismatches_count": len(manifest_mismatches),
            "mismatches": manifest_mismatches,
        },
        "branch_git_scope_audit": {
            "merge_base_with_origin_main": merge_base,
            "total_changed_files_since_merge_base": len(changed_files),
            "non_relay_edits_count": len(non_relay_edits),
            "non_relay_edits": non_relay_edits,
        },
        "referee_planted_fault_controls": rpf_controls,
        "planted_faults_caught": rpf_caught_count,
        "planted_faults_total": 6,
        "passed": passed,
    }
    return out, discrepancies


def main() -> None:
    this_file = pathlib.Path(__file__).resolve()
    repo_root = this_file.parents[2]
    prod_json_path = repo_root / "relays" / "a2_p135_v3" / "a2_p135_v3_results.json"
    prod_data = json.loads(prod_json_path.read_text(encoding="utf-8"))

    self_hygiene = audit_python_ast(this_file, check_sandbox=False)
    self_sha256 = hashlib.sha256(this_file.read_bytes()).hexdigest()

    res_a, disc_a = run_r_p135_a(prod_data["P135_A_simpson_tame_table_and_nilpotent_jordan_model"])
    res_b, disc_b = run_r_p135_b(prod_data["P135_B_disjoint_e8_condensate_embedding_count"])
    res_c, disc_c = run_r_p135_c(prod_data["P135_C_agy_exp_9b34bfc03_A2_OW27_F2_audit"], repo_root)
    res_d, disc_d = run_r_p135_d(repo_root, res_a, res_b, res_c)

    discrepancies = disc_a + disc_b + disc_c + disc_d
    non_blocking_diagnostics: list[str] = []

    all_passed = bool(
        self_hygiene["clean"]
        and res_a["passed"]
        and res_b["passed"]
        and res_c["passed"]
        and res_d["passed"]
        and len(discrepancies) == 0
    )

    out = {
        "card_id": "A2-P135",
        "role": "disjoint_cold_room_zero_trust_referee",
        "seat": "agy-002",
        "empirical_firewall": "0 of 19",
        "script": this_file.name,
        "script_sha256": self_sha256,
        "self_ast_hygiene": self_hygiene,
        "R_P135_A_numerical_holonomy_and_radial_weights": res_a,
        "R_P135_B_coordinate_free_bourbaki_e8_affine_deletion": res_b,
        "R_P135_C_disjoint_agy_exp_9b34bfc03_A2_OW27_F2": res_c,
        "R_P135_D_planted_faults_and_branch_manifest_audit": res_d,
        "discrepancies": discrepancies,
        "discrepancies_count": len(discrepancies),
        "non_blocking_diagnostics": non_blocking_diagnostics,
        "all_referee_gates_passed": all_passed,
    }

    json_floats = assert_no_json_floats(out)
    if json_floats:
        raise RuntimeError(f"JSON float tokens detected: {json_floats}")

    out_path = this_file.parent / "referee_a2_p135_results.json"
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
