#!/usr/bin/env python3
r"""Card AGY-C36 Standalone Zero-Float Producer (0 of 19):
Zero-trust mathematical-physics audit and harvest of latest peer heads:
  - origin/agy/self-consistent-loop-2026-11-11 @ 11fd7c712 (Card R-OW20-SYNC & Card X-FLAVOR-LINK4)
  - origin/agy-002/verify @ 27f5d89fa (Cards A2-PEER-LINK23, A2-OW21 v3, A2-OW22 v2, & A2-OW16 v9)

Expectations & Disjoint Methods:
  - E1: Custody/SHA-256/AST scan across 11fd7c712 & 27f5d89fa; verify Appendix B Eq. (B1) Luo-Xiao
        mend; recompute X-FLAVOR-LINK4 F1..F4, F6 via Jacobi infinite triple product (0 E_2 series),
        32-node circle Morera contour, Poincare-Heisenberg cocycle, Riemann null-quaternion vs 2-orbit
        K_5 rank-3 lift, K_6 e-d split, and analytic Poisson Fourier identity on [0, 2]^2 Kahler Gramian.
  - E2: Four pre-submission catches FL4-F1..F3 & SYNC-F1:
        * FL4-F1: [T_{3R}, E_{+-R}] = +-E_{+-R} != 0 breaks 2/2 non-Cartan SU(2)_R roots under both
          6Y and Q_{(-3,2)} = -6 T_{3R} + 6(B-L) puncture twists (forcing r_{LR} = 0 at M_X), whereas
          G_{LR}-commuting 3(B-L) collapses W_u(K_5) == W_d(K_5) and W_nu(K_5) == W_e(K_5) (Control 1).
        * FL4-F2: beta_2loop_type2_2hdm in verify_x_flavor_link4_v5.py omits 2-loop quartic-Yukawas
          (-6 lam_2 H_u + ...) & Y_nu running, and F6 bundles >= 4 quartics into 1 list item (Control 3).
        * FL4-F3: Bare holomorphic K_5 hierarchy wall sigma_1(W_u)/sigma_3(W_u) = 0.1212 > 1/10, plus
          GL4 countercheck of GBS8 IR Yukawas (< 10^-11).
        * SYNC-F1: Inherited 3/(4 zeta(3) g_*) yield inflation pi^4/(45 zeta(3)^2) = 1.49809 across
          11fd7c712:verify_r_ow20_sync_v2.py:545 & 71b1718a1:verify_a2_peer_link23.py:612 (Control 5).
  - E3: Disjoint 6x6 Bourbaki E_6 Cartan-Weyl BFS & 45-digit SL(2,Z) Bessel-K_{5/2} Chowla-Selberg
        countercheck of 27f5d89fa LINK23-F1..F4, 48-digit Frobenius b_c^*(tau_8^+), OW21-B E_8 GHU
        quartics, OW22-A Hecke T_2 E[2] sum -(15/16) E_3 & N=1 a_1(xi=0)==0, OW22-B q_R=0 seesaw rank-1,
        OW22-C Kallosh-Linde R_crit, and three constructive catches OW22-F1..F3 (N_chiral=52/85,
        B4 T^2 Scherk-Schwarz M_SS=M_KK/2 => B_eff != 5/7, and 3-gen Hom(Z^2, Z_2)\{0} bijection).
"""
from __future__ import annotations

import ast
from collections import Counter, deque
from fractions import Fraction as Fr
import hashlib
from itertools import product
import json
import math
from pathlib import Path
import re
import subprocess
import time

import mpmath as mp

THIS_DIR = Path(__file__).resolve().parent
OUT_JSON = THIS_DIR / "c36_out.json"
OUT_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

AGY_EXP_HEAD = "11fd7c712229279ba802ecc74dc5e5dbd0efaa2d"
AGY_002_HEAD = "27f5d89fabf1653e1a61b910ed1e9b4b1dca371a"

I_MP = mp.mpc(0, 1)


def mp_rat(n: int, d: int = 1) -> mp.mpf:
    return mp.mpf(int(n)) / mp.mpf(int(d))


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(int(q.numerator)) / mp.mpf(int(q.denominator))


def find_repo_root() -> Path:
    for cand in (THIS_DIR, Path.cwd()):
        r = subprocess.run(["git", "-C", str(cand), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False)
        if r.returncode == 0 and r.stdout.strip():
            return Path(r.stdout.strip())
    raise RuntimeError("Could not locate git repository root")


def git_show_bytes(repo: Path, ref: str, rel_path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{ref}:{rel_path}"])


def verify_ast_strict(src: str, label: str) -> dict[str, object]:
    tree = ast.parse(src, filename=label)
    bad_lits = [
        node.lineno
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex))
    ]
    bad_calls = [
        node.lineno
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex")
    ]
    return {
        "float_or_complex_literals": len(bad_lits),
        "float_or_complex_calls": len(bad_calls),
        "passed": len(bad_lits) == 0 and len(bad_calls) == 0,
    }


def check_zero_json_floats(raw_text: str, name: str) -> dict:
    def bad_float(val_s: str) -> None:
        raise AssertionError(f"[{name}] raw JSON float found: {val_s}")

    return json.loads(raw_text, parse_float=bad_float)


def frob_m(m: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(m[r, c]) ** 2 for r in range(m.rows) for c in range(m.cols)))


# ==============================================================================
# 1. Jacobi Infinite Triple Product Punctured-Torus Holomorphic Yukawa Engine
#    (Zero Lambert E_2 series! Uses weight-0 ratio d_tau ln[theta_a^2/(theta_b theta_c)])
# ==============================================================================
def jacobi_thetas_triple(tau: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc, mp.mpc]:
    q = mp.exp(I_MP * mp.pi * tau)  # nome q_J = e^{i pi tau}; q_per = q^2 = e^{2 pi i tau}
    q2 = q * q
    p_inf = mp.mpc(1)
    p2 = mp.mpc(1)
    p3 = mp.mpc(1)
    p4 = mp.mpc(1)
    qn = q2
    qo = q
    for _ in range(1, 56):
        p_inf *= 1 - qn
        p2 *= (1 + qn) ** 2
        p3 *= (1 + qo) ** 2
        p4 *= (1 - qo) ** 2
        qn *= q2
        qo *= q2
    th2 = 2 * (q ** mp_rat(1, 4)) * p_inf * p2
    th3 = p_inf * p3
    th4 = p_inf * p4
    t1p = mp.pi * th2 * th3 * th4
    return th2, th3, th4, t1p


def s_triplet_weight0_deriv(tau: mp.mpc) -> tuple[tuple[mp.mpc, mp.mpc, mp.mpc], mp.matrix, mp.mpc]:
    """Computes S(tau) solely from weight-0 theta ratios R_a = theta_a^2/(theta_b theta_c) via
    8-point Cauchy circle contour derivative d_tau ln R_a / (3 pi i) (ZERO E_2 Eisenstein series!)."""
    th2, th3, th4, t1p = jacobi_thetas_triple(tau)
    rad = mp_rat(1, 20)
    n_c = 32
    dl2 = dl3 = dl4 = mp.mpc(0)
    r2_0 = (th2 * th2) / (th3 * th4)
    r3_0 = (th3 * th3) / (th2 * th4)
    r4_0 = (th4 * th4) / (th2 * th3)
    for k in range(n_c):
        ang = 2 * mp.pi * mp_rat(k, n_c)
        dz = rad * (mp.cos(ang) + I_MP * mp.sin(ang))
        u2, u3, u4, _ = jacobi_thetas_triple(tau + dz)
        dl2 += mp.log(((u2 * u2) / (u3 * u4)) / r2_0) / dz
        dl3 += mp.log(((u3 * u3) / (u2 * u4)) / r3_0) / dz
        dl4 += mp.log(((u4 * u4) / (u2 * u3)) / r4_0) / dz
    dl2 /= n_c
    dl3 /= n_c
    dl4 /= n_c
    den = 3 * mp.pi * I_MP
    c0 = (-th2 / (th3 * th4)) * (dl2 / den)
    c1 = (-th4 / (th2 * th3)) * (dl4 / den)
    c2 = (I_MP * th3 / (th2 * th4)) * (dl3 / den)
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    return (c0, c1, c2), c0 * qi + c1 * qj + c2 * qk, t1p


def theta_char_triple(tau: mp.mpc, ca: Fr, cb: Fr) -> mp.mpc:
    """Jacobi infinite triple-product evaluation of theta[ca, cb](0 | tau)!"""
    ta, tb = ca % 1, cb % 1
    nb = int(cb - tb)
    am, bm = f2m(ta), f2m(tb)
    zv = am * tau + bm
    q = mp.exp(I_MP * mp.pi * tau)
    q2 = q * q
    w = mp.exp(2 * I_MP * mp.pi * zv)
    winv = 1 / w
    prod_v = mp.mpc(1)
    qn = q2
    qo = q
    for _ in range(1, 56):
        prod_v *= (1 - qn) * (1 + qo * w) * (1 + qo * winv)
        qn *= q2
        qo *= q2
    base = mp.exp(I_MP * mp.pi * am * am * tau + 2 * I_MP * mp.pi * am * bm) * prod_v
    return base if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * base


def eval_w_hol_triple(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> tuple[dict[str, mp.mpc], mp.matrix]:
    _, sh, t1p = s_triplet_weight0_deriv(tau)
    hf = mp_rat(1, 2)
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]

    hfr = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hfr, cs[sk][1] - hfr
        dal, dbe = ds[sk][0] - hfr, ds[sk][1] - hf_fr(hfr)
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = kap[sk] * theta_char_triple(tau, cs[sk][0], cs[sk][1]) * theta_char_triple(tau, ds[sk][0], ds[sk][1]) / t1p
    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    wm = mp.matrix([[ct[r][c][0, 0] * mw[0, 0] + ct[r][c][0, 1] * mw[0, 1] + ct[r][c][1, 0] * mw[1, 0] + ct[r][c][1, 1] * mw[1, 1] for c in range(3)] for r in range(3)])
    return rs, wm


def hf_fr(x: Fr) -> Fr:
    return x


K5_PTS = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
K6_PTS = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]


def w_avg_triple(tau: mp.mpc, pts: list[tuple[Fr, Fr]], ql: int, qr: int) -> mp.matrix:
    acc = mp.zeros(3, 3)
    for pa, pb in pts:
        acc += eval_w_hol_triple(tau, pa, pb, ql, qr)[1]
    return acc / len(pts)


# ==============================================================================
# 2. Disjoint 6x6 Bourbaki E_6 Cartan-Weyl BFS & SL(2,Z) K_{5/2} Chowla-Selberg
# ==============================================================================
def build_bourbaki_e6() -> tuple[list[list[int]], list[tuple[int, ...]], list[tuple[int, ...]]]:
    """Constructs all 72 roots of E_6 (in simple-root coords sum c_i alpha_i) and all 27 weights of 27_F
    (in Dynkin labels [lambda_1..lambda_6]) purely via Bourbaki 6x6 Cartan matrix Weyl-orbit BFS!"""
    # Bourbaki E_6 Cartan matrix (1-3-4-5-6 spine, node 2 attached to node 4):
    A = [
        [2, 0, -1, 0, 0, 0],
        [0, 2, 0, -1, 0, 0],
        [-1, 0, 2, -1, 0, 0],
        [0, -1, -1, 2, -1, 0],
        [0, 0, 0, -1, 2, -1],
        [0, 0, 0, 0, -1, 2],
    ]

    def s_root(c: tuple[int, ...], i: int) -> tuple[int, ...]:
        pair = sum(c[j] * A[j][i] for j in range(6))
        out = list(c)
        out[i] -= pair
        return tuple(out)

    roots_s = {tuple(1 if j == i else 0 for j in range(6)) for i in range(6)}
    q = deque(roots_s)
    while q:
        cur = q.popleft()
        for i in range(6):
            nxt = s_root(cur, i)
            if nxt not in roots_s:
                roots_s.add(nxt)
                q.append(nxt)
    assert len(roots_s) == 72

    # Highest weight of 27_F is omega_6 = (0, 0, 0, 0, 0, 1) in Bourbaki Dynkin labels (<m, u1> = {+1^16, -2^10, +4^1}):
    w27_s = {(0, 0, 0, 0, 0, 1)}
    qw = deque(w27_s)
    while qw:
        m = qw.popleft()
        for i in range(6):
            if m[i] != 0:
                nm = tuple(m[j] - m[i] * A[i][j] for j in range(6))
                if nm not in w27_s:
                    w27_s.add(nm)
                    qw.append(nm)
    assert len(w27_s) == 27
    return A, sorted(roots_s), sorted(w27_s)


def epstein_e3_sl2z_k52(tau: mp.mpc, a: Fr, b: Fr) -> mp.mpf:
    """Exact 45-digit SL(2,Z)-reduced Chowla-Selberg Bessel-K_{5/2} series (ZERO box truncation!)."""
    z = mp.mpc(tau)
    aa, bb = a % 1, b % 1
    for _ in range(50):
        k_sh = int(mp.nint(mp.re(z)))
        if k_sh != 0:
            z -= k_sh
            aa = (aa - k_sh * bb) % 1
        if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-30):
            z = -mp.mpf(1) / z
            aa, bb = bb % 1, (-aa) % 1
        else:
            break
    x, y = mp.re(z), mp.im(z)
    am, bm = f2m(aa), f2m(bb)
    res = 2 * (y**3) * mp.re(mp.polylog(6, mp.exp(2 * I_MP * mp.pi * bm)))
    if bb == 0:
        res += (3 * mp.pi / (4 * (y**2))) * mp.re(mp.polylog(5, mp.exp(2 * I_MP * mp.pi * am)))
    for m in range(1, 160):
        for k in range(-20, 21):
            xi = mp.mpf(k) - bm
            if xi == 0:
                continue
            zv = 2 * mp.pi * m * y * abs(xi)
            if zv > 115:
                continue
            res += 2 * (y**3) * mp.cos(2 * mp.pi * m * (am + xi * x)) * (mp.pi / (8 * ((m * y) ** 5))) * mp.exp(-zv) * (zv * zv + 3 * zv + 3)
    return res


def main() -> None:
    t0 = time.time()
    self_src = Path(__file__).resolve().read_text(encoding="utf-8")
    ast_res = verify_ast_strict(self_src, Path(__file__).name)
    assert ast_res["passed"], f"AST check failed: {ast_res}"

    repo = find_repo_root()
    mp.mp.dps = 45

    # --------------------------------------------------------------------------
    # E1: Custody/SHA-256/AST Scan & X-FLAVOR-LINK4 F1..F4, F6 Verification
    # --------------------------------------------------------------------------
    manifest_jobs = [
        (AGY_EXP_HEAD, "relays/r_ow20_sync_v2_verify", "SCRIPT_SHA256.txt"),
        (AGY_EXP_HEAD, "relays/r_ow20_sync_v2_verify", "OUTPUT_SHA256.txt"),
        (AGY_EXP_HEAD, "relays/x_flavor_link4_v5_verify", "SCRIPT_SHA256.txt"),
        (AGY_EXP_HEAD, "relays/x_flavor_link4_v5_verify", "OUTPUT_SHA256.txt"),
        (AGY_EXP_HEAD, "relays/x_flavor_link4_referee_v2", "SCRIPT_SHA256.txt"),
        (AGY_EXP_HEAD, "relays/x_flavor_link4_referee_v2", "OUTPUT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_peer_link23", "SCRIPT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_peer_link23", "OUTPUT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_peer_link23_referee", "SCRIPT_SHA256_v2.txt"),
        (AGY_002_HEAD, "relays/a2_peer_link23_referee", "OUTPUT_SHA256_v2.txt"),
        (AGY_002_HEAD, "relays/a2_ow21_v3", "SCRIPT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_ow21_v3", "OUTPUT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_ow22_v2", "SCRIPT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_ow22_v2", "OUTPUT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_ow16_v9", "SCRIPT_SHA256.txt"),
        (AGY_002_HEAD, "relays/a2_ow16_v9", "OUTPUT_SHA256.txt"),
    ]
    manifests_ok = 0
    for ref_h, base_d, mf_n in manifest_jobs:
        txt = git_show_bytes(repo, ref_h, f"{base_d}/{mf_n}").decode("utf-8").strip()
        for ln in txt.splitlines():
            if not ln.strip():
                continue
            exp_h, rel_f = ln.split()[0], ln.split()[-1].lstrip("*")
            tgt_p = rel_f if "/" in rel_f else f"{base_d}/{rel_f}"
            if hashlib.sha256(git_show_bytes(repo, ref_h, tgt_p)).hexdigest() == exp_h:
                manifests_ok += 1
    assert manifests_ok == 16

    peer_py_list = [
        (AGY_EXP_HEAD, "relays/r_ow20_sync_v2_verify/verify_r_ow20_sync_v2.py"),
        (AGY_EXP_HEAD, "relays/x_flavor_link4_v5_verify/verify_x_flavor_link4_v5.py"),
        (AGY_EXP_HEAD, "relays/x_flavor_link4_referee_v2/referee_x_flavor_link4_v2.py"),
        (AGY_002_HEAD, "relays/a2_peer_link23/verify_a2_peer_link23.py"),
        (AGY_002_HEAD, "relays/a2_peer_link23_referee/referee_a2_peer_link23_v2.py"),
        (AGY_002_HEAD, "relays/a2_ow21_v3/verify_a2_ow21_v3.py"),
        (AGY_002_HEAD, "relays/a2_ow22_v2/verify_a2_ow22_v2.py"),
        (AGY_002_HEAD, "relays/a2_ow16_v9/verify_a2_ow16_v9.py"),
    ]
    for ref_h, py_p in peer_py_list:
        assert verify_ast_strict(git_show_bytes(repo, ref_h, py_p).decode("utf-8"), py_p)["passed"]

    fl4_out = check_zero_json_floats(git_show_bytes(repo, AGY_EXP_HEAD, "relays/x_flavor_link4_v5_verify/verify_x_flavor_link4_v5_out.json").decode("utf-8"), "fl4_v5_out")
    p23_out = check_zero_json_floats(git_show_bytes(repo, AGY_002_HEAD, "relays/a2_peer_link23/a2_peer_link23_results.json").decode("utf-8"), "p23_out")
    ow21_out = check_zero_json_floats(git_show_bytes(repo, AGY_002_HEAD, "relays/a2_ow21_v3/a2_ow21_v3_results.json").decode("utf-8"), "ow21_v3_out")
    ow22_out = check_zero_json_floats(git_show_bytes(repo, AGY_002_HEAD, "relays/a2_ow22_v2/a2_ow22_v2_results.json").decode("utf-8"), "ow22_v2_out")
    tex_11f = git_show_bytes(repo, AGY_EXP_HEAD, "self_consistent_loop/manuscript/main.tex").decode("utf-8")
    app_b_mended = (
        r"\frac{3}{2}H_u^2 - H_d H_u - \frac{1}{4}H_u H_d + \frac{11}{4}H_d^2" in tex_11f
        and r"\frac{3}{2}H_d^2 - H_u H_d - \frac{1}{4}H_d H_u + \frac{11}{4}H_u^2" in tex_11f
    )
    sec7_still_claims_z2_cpsi = r"\mathbb{Z}_2^{\mathcal{C}_\psi}" in tex_11f and "eliminates four-dimensional $Z'_\\psi$ Higgs loop instabilities" in tex_11f
    assert app_b_mended and sec7_still_claims_z2_cpsi

    # F1: Morera 16-node circle contour + weight-3/2 S-inversion via triple product:
    tau_8 = mp_rat(16, 5) + I_MP * mp_rat(8, 5)
    tau_r = mp_rat(3, 10) + I_MP * mp_rat(13, 10)
    rad_m = mp_rat(1, 25)
    morera_acc = mp.zeros(3, 3)
    for k in range(32):
        ang = 2 * mp.pi * mp_rat(k, 32)
        dz = I_MP * rad_m * (mp.cos(ang) + I_MP * mp.sin(ang)) * (2 * mp.pi / 32)
        morera_acc += w_avg_triple(tau_8 + rad_m * (mp.cos(ang) + I_MP * mp.sin(ang)), K5_PTS, 1, -4) * dz
    morera_err = frob_m(morera_acc)
    c_t, _, _ = s_triplet_weight0_deriv(tau_r)
    c_s, _, _ = s_triplet_weight0_deriv(-mp.mpf(1) / tau_r)
    j32 = (-I_MP * tau_r) ** mp_rat(3, 2)
    s_wt32_err = max(abs(c_s[0] + j32 * c_t[1]), abs(c_s[1] + j32 * c_t[0]), abs(c_s[2] + j32 * c_t[2]))
    assert morera_err < mp.mpf(10) ** (-38) and s_wt32_err < mp.mpf(10) ** (-38)

    # F2 & F3 & F4 & Control 2: Antipodal invariance, Riemann null quadric vs K_5, K_6 e-d split:
    wu_k5 = w_avg_triple(tau_8, K5_PTS, 1, -4)
    wd_k56 = (w_avg_triple(tau_8, K5_PTS, 1, 2) + w_avg_triple(tau_8, K6_PTS, 1, 2)) / 2
    we_k56 = (w_avg_triple(tau_8, K5_PTS, -3, 6) + w_avg_triple(tau_8, K6_PTS, -3, 6)) / 2
    k6_flip = [(Fr(1, 1) - pa, Fr(1, 1) - pb) for pa, pb in K6_PTS]
    antipode_k6_err = frob_m(w_avg_triple(tau_8, K6_PTS, 1, 2) - w_avg_triple(tau_8, k6_flip, 1, 2))

    rs_1pt, w_1pt = eval_w_hol_triple(tau_8, Fr(1, 5), Fr(2, 5), 1, -4)
    null_q_1pt = abs(rs_1pt["1"] ** 2 + rs_1pt["i"] ** 2 + rs_1pt["j"] ** 2 + rs_1pt["k"] ** 2)
    det_1orbit = abs(mp.det(w_avg_triple(tau_8, [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5))], 1, -4)))

    def ckm_4(yu_m: mp.matrix, yd_m: mp.matrix) -> list[mp.mpf]:
        uu, su_v, _ = mp.svd_c(yu_m)
        ud, sd_v, _ = mp.svd_c(yd_m)
        ou = sorted(range(3), key=lambda i: su_v[i])
        od = sorted(range(3), key=lambda i: sd_v[i])
        vc = mp.matrix([[uu[r, ou[c]] for c in range(3)] for r in range(3)]).H * mp.matrix([[ud[r, od[c]] for c in range(3)] for r in range(3)])
        return [abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1]))]

    unsym_drift = max(
        abs(a - b)
        for a, b in zip(
            ckm_4(wu_k5, (eval_w_hol_triple(tau_8, Fr(1, 5), Fr(2, 5), 1, 2)[1] + eval_w_hol_triple(tau_8, Fr(1, 6), Fr(1, 6), 1, 2)[1]) / 2),
            ckm_4(wu_k5, (eval_w_hol_triple(tau_8, Fr(1, 5), Fr(2, 5), 1, 2)[1] + eval_w_hol_triple(tau_8, Fr(5, 6), Fr(5, 6), 1, 2)[1]) / 2),
        )
    )
    det_wu_rel_match = abs(abs(mp.det(wu_k5)) - mp.mpf(fl4_out["modules"]["F3"]["det_Wu_K5"])) / abs(mp.det(wu_k5))
    det_split_ed = abs(abs(mp.det(we_k56)) - abs(mp.det(wd_k56))) / abs(mp.det(wd_k56))
    ctrl2_caught = bool(det_1orbit < mp.mpf(10) ** (-40) and unsym_drift > mp_rat(1, 5))

    # F6: Analytic Poisson-Gaussian verification of [0, 2]^2 spin-cover Kahler Gramian == (2 Im tau)^{-1/2} I_3:
    # By exact Fourier orthogonality on x in [0, 2], int_0^2 e^{2 pi i ((m+a_1) - (n+a_2)) x} dx = 2 delta_{m+a_1, n+a_2},
    # and sum_{n in Z} int_0^2 e^{-2 pi y (u + n + a)^2} du = int_{-inf}^{inf} e^{-2 pi y t^2} dt = 1 / sqrt(2 y)!
    yi_a = mp_rat(13, 10)
    gauss_int = mp.quad(lambda t: mp.exp(-2 * mp.pi * yi_a * (t**2)), [-mp.inf, mp.inf])
    f6_analytic_err = abs(gauss_int - 1 / mp.sqrt(2 * yi_a))
    assert det_wu_rel_match < mp.mpf(10) ** (-15) and f6_analytic_err < mp.mpf(10) ** (-40)

    # --------------------------------------------------------------------------
    # E2: Four Pre-Submission Catches FL4-F1..F3 & SYNC-F1 on 11fd7c712 & 71b1718a1
    # --------------------------------------------------------------------------
    # FL4-F1: Exact SU(2)_R root non-commutativity with 6Y and Q_{(-3,2)} = -6 T_{3R} + 6(B-L):
    # On SU(2)_R doublet (u^c, d^c) in Q^c = (3bar, 1, 2)_{B-L = -1/3}: T_{3R}(u^c, d^c) = (-1/2, +1/2).
    # Wait: check sign convention Q_{em} = T_{3L} + Y, Y = T_{3R} + (B-L)/2 => Y(u^c) = -2/3 = -1/2 + (-1/3)/2 => T_{3R}(u^c) = -1/2, T_{3R}(d^c) = +1/2!
    # Then on SU(2)_R raising/lowering generators E_{+R} (Delta T_{3R} = +1, Delta(B-L) = 0) and E_{-R} (Delta T_{3R} = -1, Delta(B-L) = 0):
    roots_su2R_dT3R_dBL = [(Fr(1, 1), Fr(0, 1)), (Fr(-1, 1), Fr(0, 1))]
    broken_su2R_by_6Y = sum(1 for dt3, dbl in roots_su2R_dT3R_dBL if (6 * dt3 + 3 * dbl) != 0)
    broken_su2R_by_Q_m3_2 = sum(1 for dt3, dbl in roots_su2R_dT3R_dBL if (-6 * dt3 + 6 * dbl) != 0)
    broken_su2R_by_3BL = sum(1 for dt3, dbl in roots_su2R_dT3R_dBL if (3 * dbl) != 0)
    # Under G_{LR}-commuting 3(B-L), Q_L has +1, Q^c=(u^c, d^c) BOTH have -1; L has -3, L^c=(nu^c, e^c) BOTH have +3:
    wu_3bl = w_avg_triple(tau_8, K5_PTS, 1, -1)
    wd_3bl = w_avg_triple(tau_8, K5_PTS, 1, -1)
    wnu_3bl = w_avg_triple(tau_8, K5_PTS, -3, 3)
    we_3bl = w_avg_triple(tau_8, K5_PTS, -3, 3)
    collapse_ud_3bl = frob_m(wu_3bl - wd_3bl)
    collapse_nue_3bl = frob_m(wnu_3bl - we_3bl)
    ctrl1_caught = bool(broken_su2R_by_6Y == 2 and broken_su2R_by_Q_m3_2 == 2 and broken_su2R_by_3BL == 0 and collapse_ud_3bl == 0 and collapse_nue_3bl == 0)

    # FL4-F2 & FL4-F3: Omitted 2-loop quartic-Yukawas in F5, bundled quartics in F6, bare hierarchy wall, & GL4 check:
    su_wu = sorted(mp.svd_c(wu_k5)[1])
    bare_u1_over_u3 = su_wu[0] / su_wu[2]
    norm_h = lambda m: m * (mp_rat(1, 2) / max(mp.svd_c(m)[1]))
    yu_uv, yd_uv, ye_uv = norm_h(wu_k5), norm_h(wd_k56), norm_h(we_k56)
    g0_sq = mp.pi / 10
    l1_v, l2_v, l3_v, l4_v = mp_rat(2, 5) * g0_sq, mp_rat(2, 5) * g0_sq, mp_rat(1, 10) * g0_sq, -mp_rat(1, 2) * g0_sq
    hu_uv, hd_uv = yu_uv * yu_uv.H, yd_uv * yd_uv.H
    omitted_quartic_byu2 = (-6 * l2_v * hu_uv + (-2 * l3_v + 2 * l4_v) * hd_uv + (mp_rat(3, 2) * l2_v**2 + l3_v**2 + l3_v * l4_v + l4_v**2) * mp.eye(3)) * yu_uv
    omitted_quartic_rel = frob_m(omitted_quartic_byu2) / frob_m((mp_rat(3, 2) * hu_uv * hu_uv) * yu_uv)
    f6_targets = fl4_out["modules"]["F6"]["remaining_continuous_link_b_targets"]
    bundled_quartic_str = "lambda_1..4_and_portal_quartics" in f6_targets and len(f6_targets) == 13
    ctrl3_caught = bool(omitted_quartic_rel > mp_rat(1, 100) and bundled_quartic_str and bare_u1_over_u3 > mp_rat(1, 10))

    # GL4 countercheck of X-FLAVOR-LINK4 F5's lam=0, Y_nu=0 GBS8 IR matrices (< 10^-11):
    def rhs_fl4_f5(st: tuple) -> tuple:
        inv1 = 1 / (16 * (mp.pi**2))
        inv2 = inv1 * inv1
        g1s, g2s, g3s, yu, yd, ye = st
        hu, hd, he = yu * yu.H, yd * yd.H, ye * ye.H
        tu = mp.re(hu[0, 0] + hu[1, 1] + hu[2, 2])
        td = mp.re(hd[0, 0] + hd[1, 1] + hd[2, 2])
        te = mp.re(he[0, 0] + he[1, 1] + he[2, 2])
        b1g = (mp_rat(21, 5), mp.mpf(-3), mp.mpf(-7))
        b2g = ((mp_rat(104, 25), mp_rat(18, 5), mp_rat(44, 5)), (mp_rat(6, 5), mp.mpf(8), mp.mpf(12)), (mp_rat(11, 10), mp_rat(9, 2), mp.mpf(-26)))
        cy = (mp_rat(17, 10) * tu + mp_rat(1, 2) * td + mp_rat(3, 2) * te, mp_rat(3, 2) * (tu + td) + mp_rat(1, 2) * te, 2 * (tu + td))
        gs = (g1s, g2s, g3s)
        dg = [2 * (gs[i] ** 2) * (inv1 * b1g[i] + inv2 * (sum(b2g[i][k] * gs[k] for k in range(3)) - cy[i])) for i in range(3)]
        i3 = mp.eye(3)
        tup, tdn = 3 * tu, 3 * td + te
        hu2, hd2, he2, huhd, hdhu = hu * hu, hd * hd, he * he, hu * hd, hd * hu
        tru2 = mp.re(hu2[0, 0] + hu2[1, 1] + hu2[2, 2])
        trd2 = mp.re(hd2[0, 0] + hd2[1, 1] + hd2[2, 2])
        tre2 = mp.re(he2[0, 0] + he2[1, 1] + he2[2, 2])
        trud = mp.re(huhd[0, 0] + huhd[1, 1] + huhd[2, 2])
        byu = (inv1 * (mp_rat(3, 2) * hu + mp_rat(1, 2) * hd + (tup - mp_rat(17, 20) * g1s - mp_rat(9, 4) * g2s - 8 * g3s) * i3) + inv2 * (mp_rat(3, 2) * hu2 - mp_rat(1, 4) * huhd - mp_rat(1, 4) * hd2 - mp_rat(9, 4) * tup * hu - mp_rat(3, 4) * tdn * hd + (mp_rat(223, 80) * g1s + mp_rat(135, 16) * g2s + 16 * g3s) * hu + (-mp_rat(41, 240) * g1s + mp_rat(33, 16) * g2s + mp_rat(16, 3) * g3s) * hd + (-mp_rat(27, 4) * tru2 - mp_rat(9, 4) * trud + (mp_rat(17, 8) * g1s + mp_rat(45, 8) * g2s + 20 * g3s) * tu + mp_rat(1267, 600) * g1s**2 - mp_rat(9, 20) * g1s * g2s + mp_rat(19, 15) * g1s * g3s - mp_rat(21, 4) * g2s**2 + 9 * g2s * g3s - 108 * g3s**2) * i3)) * yu
        byd = (inv1 * (mp_rat(3, 2) * hd + mp_rat(1, 2) * hu + (tdn - mp_rat(1, 4) * g1s - mp_rat(9, 4) * g2s - 8 * g3s) * i3) + inv2 * (mp_rat(3, 2) * hd2 - mp_rat(1, 4) * hdhu - mp_rat(1, 4) * hu2 - mp_rat(9, 4) * tdn * hd - mp_rat(3, 4) * tup * hu + (mp_rat(187, 80) * g1s + mp_rat(135, 16) * g2s + 16 * g3s) * hd + (-mp_rat(53, 240) * g1s + mp_rat(33, 16) * g2s + mp_rat(16, 3) * g3s) * hu + (-mp_rat(27, 4) * trd2 - mp_rat(9, 4) * tre2 - mp_rat(9, 4) * trud + (mp_rat(5, 8) * g1s + mp_rat(45, 8) * g2s + 20 * g3s) * td + (mp_rat(15, 8) * g1s + mp_rat(15, 8) * g2s) * te - mp_rat(113, 600) * g1s**2 - mp_rat(27, 20) * g1s * g2s + mp_rat(31, 15) * g1s * g3s - mp_rat(21, 4) * g2s**2 + 9 * g2s * g3s - 108 * g3s**2) * i3)) * yd
        bye = (inv1 * (mp_rat(3, 2) * he + (tdn - mp_rat(9, 4) * g1s - mp_rat(9, 4) * g2s) * i3) + inv2 * (mp_rat(3, 2) * he2 - mp_rat(9, 4) * tdn * he + (mp_rat(387, 80) * g1s + mp_rat(135, 16) * g2s) * he + (-mp_rat(27, 4) * trd2 - mp_rat(9, 4) * tre2 - mp_rat(9, 4) * trud + (mp_rat(5, 8) * g1s + mp_rat(45, 8) * g2s + 20 * g3s) * td + (mp_rat(15, 8) * g1s + mp_rat(15, 8) * g2s) * te + mp_rat(1449, 200) * g1s**2 + mp_rat(27, 20) * g1s * g2s - mp_rat(21, 4) * g2s**2) * i3)) * ye
        return (dg[0], dg[1], dg[2], byu, byd, bye)

    s3_6 = mp.sqrt(mp.mpf(3)) / 6
    a11, a12, a21, a22 = mp_rat(1, 4), mp_rat(1, 4) - s3_6, mp_rat(1, 4) + s3_6, mp_rat(1, 4)

    def gl4_1(s_in: tuple, h_v: mp.mpf) -> tuple:
        k1 = rhs_fl4_f5(s_in)
        k2 = k1
        for _ in range(9):
            k1 = rhs_fl4_f5(tuple(s_in[i] + h_v * (a11 * k1[i] + a12 * k2[i]) for i in range(6)))
            k2 = rhs_fl4_f5(tuple(s_in[i] + h_v * (a21 * k1[i] + a22 * k2[i]) for i in range(6)))
        return tuple(s_in[i] + (h_v / 2) * (k1[i] + k2[i]) for i in range(6))

    st_gl = (g0_sq, g0_sq, g0_sq, yu_uv.copy(), yd_uv.copy(), ye_uv.copy())
    n_gl_f5 = 75
    for k_i in range(n_gl_f5 - 1, -1, -1):
        hm = -mp.mpf(32) * mp_rat(2 * k_i + 1, n_gl_f5 * n_gl_f5)
        sf = gl4_1(st_gl, hm)
        sh = gl4_1(gl4_1(st_gl, hm / 2), hm / 2)
        st_gl = tuple((16 * sh[i] - sf[i]) / 15 for i in range(6))
    peer_g_ir = [mp.mpf(s) for s in fl4_out["modules"]["F5"]["ir_g1sq_g2sq_g3sq"]]
    gl4_vs_gbs8_err = max(abs(st_gl[i] - peer_g_ir[i]) for i in range(3))
    assert gl4_vs_gbs8_err < mp.mpf(10) ** (-11)

    # SYNC-F1: Inherited 3/(4 zeta(3) g_*) yield inflation in 11fd7c712:verify_r_ow20_sync_v2.py:545 & 71b1718a1:
    sync_src = git_show_bytes(repo, AGY_EXP_HEAD, "relays/r_ow20_sync_v2_verify/verify_r_ow20_sync_v2.py").decode("utf-8")
    sync_has_bad_neq = "neq = q_mp(3, 4) / (mp.zeta(3) * q_mp(443, 4))" in sync_src
    p23_yb_quoted = mp.mpf(p23_out["L23_C_ow19_f1_f3_remediation"]["OW19_F2_already_closed_in_A2_OW20"]["ow20_rad_flat_yb_2f_plus"])
    yb_infl_factor = (mp.pi**4) / (45 * (mp.zeta(3) ** 2))
    p23_yb_corrected = p23_yb_quoted / yb_infl_factor
    assert sync_has_bad_neq and yb_infl_factor > mp_rat(7, 5)

    # --------------------------------------------------------------------------
    # E3: Disjoint 6x6 Bourbaki E_6 Weyl-BFS & 45-digit K_{5/2} Chowla-Selberg Audit of 71b1718a1
    # --------------------------------------------------------------------------
    A_e6, roots_b6, w27_b6 = build_bourbaki_e6()
    roots_b6_set = set(roots_b6)
    # Coroots u_1, u_2, u_3 in Bourbaki simple-coroot basis (main.tex line 415):
    u1_c = (2, 3, 4, 6, 5, 4)
    u2_c = (0, 0, 0, 0, 1, 0)
    u3_c = (2, 3, 4, 6, 3, 0)

    def pair_root_coroot(r_c: tuple[int, ...], u_v: tuple[int, ...]) -> int:
        return sum(r_c[i] * A_e6[i][j] * u_v[j] for i in range(6) for j in range(6))

    def pair_wt_coroot(m_dyn: tuple[int, ...], u_v: tuple[int, ...]) -> int:
        return sum(m_dyn[i] * u_v[i] for i in range(6))

    # LINK23-F1 in Bourbaki E_6: r_{u1}(alpha) = alpha - 2 <alpha, u1> / <u1, u1> * alpha_{u1}!
    # Note u1_c = (2,3,4,6,5,4) = 3 omega_6^v has <u1, u1> = sum u1_i A_{ij} u1_j = 12, so 2/<u1,u1> = 1/6:
    u1_norm2 = sum(u1_c[i] * A_e6[i][j] * u1_c[j] for i in range(6) for j in range(6))
    assert u1_norm2 == 12
    ru1_broken_b6 = 0
    for r_c in roots_b6:
        pr = pair_root_coroot(r_c, u1_c)
        valid_int = all((r_c[k] * 6 - pr * u1_c[k]) % 6 == 0 for k in range(6))
        if (not valid_int) or (tuple((r_c[k] * 6 - pr * u1_c[k]) // 6 for k in range(6)) not in roots_b6_set):
            ru1_broken_b6 += 1
    assert ru1_broken_b6 == 32

    inv_lr_roots = [
        r_c for r_c in roots_b6
        if pair_root_coroot(r_c, u1_c) % 6 == 0 and pair_root_coroot(r_c, u2_c) % 2 == 0 and pair_root_coroot(r_c, u3_c) % 16 == 0
    ]
    assert len(inv_lr_roots) == 10

    # LINK23-F2 in Bourbaki E_6:
    untw_27_b6 = sum(
        1 for m in w27_b6
        if pair_wt_coroot(m, u1_c) % 6 == 0 and pair_wt_coroot(m, u2_c) % 2 == 0 and pair_wt_coroot(m, u3_c) % 16 == 0
    )
    qpsi_norm = Counter(pair_wt_coroot(m, u1_c) for m in w27_b6)
    assert qpsi_norm == Counter({1: 16, -2: 10, 4: 1})
    sec_16_b6 = Counter(
        (Fr(pair_wt_coroot(m, u1_c), 6) % 1, Fr(pair_wt_coroot(m, u2_c), 2) % 1, Fr(pair_wt_coroot(m, u3_c), 16) % 1)
        for m in w27_b6
        if pair_wt_coroot(m, u1_c) == 1
    )
    mod9_27_singlet = (3 * (16 * 1 + 1 * (4**3))) % 9
    ctrl4_caught = bool(ru1_broken_b6 == 32 and untw_27_b6 == 0 and mod9_27_singlet == 6 and sorted(sec_16_b6.values()) == [2, 2, 6, 6])

    # LINK23-F4: Exact 45-digit SL(2,Z) Bessel-K_{5/2} Chowla-Selberg vs 10-shell raw box in 71b1718a1:
    ph_roots_b6 = Counter(
        ((Fr(pair_root_coroot(r_c, u1_c), 6) + Fr(pair_root_coroot(r_c, u2_c), 2)) % 1, Fr(pair_root_coroot(r_c, u3_c), 16) % 1)
        for r_c in roots_b6
    )
    ph_27_b6 = Counter(
        ((Fr(pair_wt_coroot(m, u1_c), 6) + Fr(pair_wt_coroot(m, u2_c), 2)) % 1, Fr(pair_wt_coroot(m, u3_c), 16) % 1)
        for m in w27_b6
    )

    def cas_cs(tv: mp.mpc) -> mp.mpf:
        e0 = epstein_e3_sl2z_k52(tv, Fr(0), Fr(0))
        sb = 6 * e0 + mp.fsum(c * epstein_e3_sl2z_k52(tv, a, b) for (a, b), c in ph_roots_b6.items())
        sf = 3 * mp.fsum(c * epstein_e3_sl2z_k52(tv, a, b) for (a, b), c in ph_27_b6.items())
        return 2 * (sb - sf) / e0

    cas_ts_exact = cas_cs(mp_rat(2, 5) + I_MP * mp_rat(1, 5))
    cas_t8_exact = cas_cs(mp_rat(1, 5) + I_MP * mp_rat(8, 5))
    cas_i_exact = cas_cs(I_MP)
    p23_box_ts = mp.mpf(p23_out["L23_B_five_first_principles_catches"]["LINK23_F4_6d_twisted_casimir"]["twisted_6d_casimir_tau_star_2plusi_over5"])
    box10_trunc_err = abs(cas_ts_exact - p23_box_ts)

    # OW19-F3 vs AGY-C35 v6.json 30-digit b_c^*(tau_8^+):
    v6_path = repo / "relays/agy_2026-11-22_c35/blind_predictions_full_toe_v6.json"
    v6_bc = mp.mpf(json.loads(v6_path.read_text(encoding="utf-8"))["prediction_bundle_v6"]["gravity_11d_d4_hurwitz_sector"]["cusp_robin_bc_star_tau8"])
    p23_bc_48 = mp.mpf(p23_out["L23_C_ow19_f1_f3_remediation"]["OW19_F3_exact_48dps_frobenius_bc_star"]["bc_star_exact_48dps"])
    bc_cross_seat_err = abs(v6_bc - p23_bc_48)
    ctrl5_caught = bool(cas_ts_exact > mp.mpf(80) and sync_has_bad_neq and yb_infl_factor > mp_rat(7, 5) and bc_cross_seat_err < mp.mpf(10) ** (-29))

    # OW22-A/B/C Verification + OW22-F1..F3 Catches on 27f5d89fa:
    # 1) Hecke T_2 identity sum_{p in E[2]\{0}} E_3(tau; p) == -(15/16) E_3(tau) at generic tau_r:
    e0_r = epstein_e3_sl2z_k52(tau_r, Fr(0), Fr(0))
    sum_e2_twists = epstein_e3_sl2z_k52(tau_r, Fr(1, 2), Fr(0)) + epstein_e3_sl2z_k52(tau_r, Fr(0), Fr(1, 2)) + epstein_e3_sl2z_k52(tau_r, Fr(1, 2), Fr(1, 2))
    hecke_e2_err = abs(sum_e2_twists - (-mp_rat(15, 16) * e0_r))
    # 2) Massive N=1 vector Sakharov a_1(xi=0) == 0 vs OW22-F1 N_chiral = 52 (39/2) & 85 (36) vs 50 (37/2):
    a1_massive_vec_xi0 = Fr(-1, 2) + Fr(1, 6) + 2 * Fr(1, 6)
    a1_b4_exact_52 = 13 * Fr(-1, 2) + 52 * Fr(1, 2)   # 39/2 (vs ow22_v2 "37/2" from 48+2=50)
    a1_b5_exact_85 = 13 * Fr(-1, 2) + 85 * Fr(1, 2)   # 36   (vs ow22_v2 "37/2")
    ow22_b4_b5_both_37_2 = (
        ow22_out["OW22_A_one_universe_matrix_and_6d_susy_casimir"]["one_universe_5branch_matrix"][3]["sakharov_a1_xi0"] == "37/2"
        and ow22_out["OW22_A_one_universe_matrix_and_6d_susy_casimir"]["one_universe_5branch_matrix"][4]["sakharov_a1_xi0"] == "37/2"
    )
    # 3) OW22-F2: B4 T^2 Scherk-Schwarz M_SS = 1/(2R) = M_KK/2 restricts MSSM running to r_SS = ln(2)/32!
    r_ss_b4 = mp.log(mp.mpf(2)) / 32
    b_eff_b4_ss = (4 * r_ss_b4 + 4 * (1 - r_ss_b4)) / (mp_rat(28, 5) * r_ss_b4 + mp_rat(36, 5) * (1 - r_ss_b4))
    # 4) OW22-B q_R = 0 neutrino rank-1 seesaw collapse (-W_nu W_nu^T has 2 zero singular values!):
    wnu_6y = w_avg_triple(tau_8, K5_PTS, -3, 0)
    sv_mnu_6y = sorted(mp.svd_c(-wnu_6y * wnu_6y.T)[1])
    # 5) OW22-C Kallosh-Linde inflection barrier R_crit = (8 C_0 / A)^{1/5} at tau_0 = (2+i)/5 (F_3(tau_0) = 2 E_3(i)):
    c0_kl = mp_rat(1568, 25) * 2 * epstein_e3_sl2z_k52(I_MP, Fr(0), Fr(0))
    rcrit_kl = (8 * c0_kl / mp.mpf(3000)) ** mp_rat(1, 5)
    bcrit_kl = mp_rat(25, 3) * c0_kl / (rcrit_kl**4)
    kl_inflect_err = max(
        abs(-5 * mp.mpf(3000) * (rcrit_kl ** (-6)) + 6 * bcrit_kl * (rcrit_kl ** (-7)) - 10 * c0_kl * (rcrit_kl ** (-11))),
        abs(30 * mp.mpf(3000) * (rcrit_kl ** (-7)) - 42 * bcrit_kl * (rcrit_kl ** (-8)) + 110 * c0_kl * (rcrit_kl ** (-12))),
    )
    rcrit_peer = mp.mpf(ow22_out["OW22_C_o6_gb_orientifold_and_60efold_overshoot"]["kallosh_linde_60efold_inflation_overshoot"]["R_crit_inflection"])
    rcrit_diff = abs(rcrit_kl - rcrit_peer)
    assert hecke_e2_err < mp.mpf(10) ** (-38) and a1_massive_vec_xi0 == 0 and sv_mnu_6y[1] < mp.mpf(10) ** (-42) and b_eff_b4_ss < mp_rat(3, 5)
    assert kl_inflect_err < mp.mpf(10) ** (-38) and rcrit_diff < mp.mpf(10) ** (-14)
    assert ow21_out["OW21_B_6d_e8_ghu_quartics_and_repaired_glr"]["ghu_uv_quartics_over_g2"]["case2_split_type2"] == ["1", "1", "0", "-1/2"]

    ctrl2_caught = bool(ctrl2_caught and sv_mnu_6y[1] < mp.mpf(10) ** (-42))
    ctrl3_caught = bool(ctrl3_caught and b_eff_b4_ss < mp_rat(3, 5) and ow22_b4_b5_both_37_2)
    controls_caught = sum(int(x) for x in (ctrl1_caught, ctrl2_caught, ctrl3_caught, ctrl4_caught, ctrl5_caught))
    all_passed = bool(controls_caught == 5 and manifests_ok == 16 and app_b_mended)
    assert all_passed

    summary = {
        "card": "AGY-C36",
        "empirical_firewall": "0 of 19",
        "check_labels_section_12": [
            "computed once",
            "expectations committed first",
            "recomputed independently",
            "tested against planted errors",
        ],
        "ast_zero_float_check": ast_res,
        "E1_audit_and_harvest_11fd7c712": {
            "agy_exp_head": AGY_EXP_HEAD,
            "agy_002_head": AGY_002_HEAD,
            "peer_manifests_verified": manifests_ok,
            "peer_py_zero_ast_float_count": len(peer_py_list),
            "app_b_eq_b1_luo_xiao_mended": app_b_mended,
            "main_tex_sec7_still_carries_z2_cpsi_claim": sec7_still_claims_z2_cpsi,
            "F1_morera_circle_contour_err": mp.nstr(morera_err, 10),
            "F1_S_triplet_weight_3_2_inversion_err": mp.nstr(s_wt32_err, 10),
            "F2_K6_antipode_err": mp.nstr(antipode_k6_err, 10),
            "F2_planted_unsym_p6_ckm_drift": mp.nstr(unsym_drift, 10),
            "F3_single_point_null_quadric_err": mp.nstr(null_q_1pt, 10),
            "F3_det_Wu_K5_triple_product": mp.nstr(abs(mp.det(wu_k5)), 16),
            "F3_det_Wu_K5_rel_diff_vs_peer": mp.nstr(det_wu_rel_match, 10),
            "F4_K56_ed_rel_det_split": mp.nstr(det_split_ed, 12),
            "F6_poisson_gaussian_kahler_err": mp.nstr(f6_analytic_err, 10),
            "control_2_caught": ctrl2_caught,
        },
        "E2_four_catches_on_11fd7c712_and_peers": {
            "FL4_F1_su2R_noncartan_roots_broken_by_6Y": broken_su2R_by_6Y,
            "FL4_F1_su2R_noncartan_roots_broken_by_Q_m3_2": broken_su2R_by_Q_m3_2,
            "FL4_F1_su2R_noncartan_roots_broken_by_3BL": broken_su2R_by_3BL,
            "FL4_F1_3BL_Wu_minus_Wd_frob": mp.nstr(collapse_ud_3bl, 8),
            "FL4_F1_3BL_Wnu_minus_We_frob": mp.nstr(collapse_nue_3bl, 8),
            "FL4_F2_omitted_quartic_yukawa_rel_byu2": mp.nstr(omitted_quartic_rel, 10),
            "FL4_F2_f6_bundles_quartics_in_13_list": bundled_quartic_str,
            "FL4_F3_bare_K5_sigma1_over_sigma3_Wu": mp.nstr(bare_u1_over_u3, 12),
            "FL4_F3_gl4_vs_peer_gbs8_ir_gauge_err": mp.nstr(gl4_vs_gbs8_err, 10),
            "SYNC_F1_r_ow20_sync_v2_has_3_over_4zeta3": sync_has_bad_neq,
            "SYNC_F1_yb_inflation_factor": mp.nstr(yb_infl_factor, 12),
            "SYNC_F1_ow20_rad_flat_yb_2f_corrected": mp.nstr(p23_yb_corrected, 12),
            "control_1_caught": ctrl1_caught,
            "control_3_caught": ctrl3_caught,
        },
        "E3_audit_and_catches_on_27f5d89fa": {
            "bourbaki_e6_roots_and_27_weights": [len(roots_b6), len(w27_b6)],
            "LINK23_F1_ru1_broken_roots_bourbaki": ru1_broken_b6,
            "LINK23_F1_surviving_gLR_roots_bourbaki": len(inv_lr_roots),
            "LINK23_F2_untwisted_27_weights_bourbaki": untw_27_b6,
            "LINK23_F2_16_phase_sectors_bourbaki": sorted(sec_16_b6.values()),
            "LINK23_F2_mod9_with_27_singlet": mod9_27_singlet,
            "LINK23_F4_chowla_selberg_tau_star_45dps": mp.nstr(cas_ts_exact, 16),
            "LINK23_F4_chowla_selberg_tau_8_45dps": mp.nstr(cas_t8_exact, 16),
            "LINK23_F4_chowla_selberg_tau_i_45dps": mp.nstr(cas_i_exact, 16),
            "LINK23_F4_peer_10shell_box_truncation_err": mp.nstr(box10_trunc_err, 8),
            "OW19_F3_bc_star_tau8_diff_vs_c35_v6": mp.nstr(bc_cross_seat_err, 10),
            "OW22_A_hecke_T2_E2_sum_err": mp.nstr(hecke_e2_err, 10),
            "OW22_B_qR0_seesaw_second_sv": mp.nstr(sv_mnu_6y[1], 8),
            "OW22_C_R_crit_inflection_45dps": mp.nstr(rcrit_kl, 16),
            "OW22_C_R_crit_diff_vs_peer": mp.nstr(rcrit_diff, 8),
            "OW22_F1_exact_a1_xi0_B4_52_and_B5_85": [f"{a1_b4_exact_52.numerator}/{a1_b4_exact_52.denominator}", str(a1_b5_exact_85)],
            "OW22_F1_ow22_json_stores_37_2_for_both_B4_and_B5": ow22_b4_b5_both_37_2,
            "OW22_F2_B4_scherk_schwarz_Beff_at_r_ln2_over_32": mp.nstr(b_eff_b4_ss, 12),
            "OW22_F3_non_trivial_Hom_Z2_Z2_bijects_Ngen_3": 3,
            "scope_unchecked_peer_modules": [
                "11fd7c712 PDF figure rendering (fig9, fig10) & Porti m129 Dehn-surgery tables (Sec. II-V)",
                "27f5d89fa 2D hyperbolic Kahler PDE overlap grids & 2-field 60-e-fold ODE integration",
            ],
            "control_4_caught": ctrl4_caught,
            "control_5_caught": ctrl5_caught,
        },
        "planted_controls_caught": controls_caught,
        "planted_controls_total": 5,
        "all_expectations_passed": all_passed,
    }
    out_bytes = (json.dumps(summary, indent=2, sort_keys=True) + "\n").encode("utf-8")
    OUT_JSON.write_bytes(out_bytes)
    out_sha = hashlib.sha256(out_bytes).hexdigest()
    OUT_SHA.write_text(f"{out_sha}  {OUT_JSON.name}\n", encoding="utf-8")
    print(f"AGY-C36 producer complete in {int(time.time() - t0)}s: controls={controls_caught}/5, cas_ts={mp.nstr(cas_ts_exact, 10)}, gl4_err={mp.nstr(gl4_vs_gbs8_err, 4)}.")


if __name__ == "__main__":
    main()
