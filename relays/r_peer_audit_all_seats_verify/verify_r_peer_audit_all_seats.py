#!/usr/bin/env python3
r"""
Standalone Pre-Hashed Producer for Card R-PEER-AUDIT-ALL-SEATS (strictly 0 of 19):
  - PA_1: Cryptographic SHA-256 Custody Audit of Active Peer Heads:
          * AGY (`origin/agy/cusp-action-2026-11-20` @ `b06c8fc1e`, Cards C35..C38 & v7.json: 12/12 manifests)
          * AGY-002 (`origin/agy-002/verify` @ `22b08aff1`, Cards A2-OW26 v8, A2-OW27 v8, A2-OW16 v18/v22,
            Cold-Room Referees v3, and canonical locks B4_UV_MZ_BLIND_LOCK_V2 & V3)
  - PA_2: Independent Zero-Shared-Code Countercheck of AGY (C37/C38 & v7.json):
          Lobachevsky Vol(m004) & M_11/M_GUT, conformal S_{+4} (n_s, r) at N=60, 2HDM quartics & Kannike
          margins at s_*, 6/6 G_SM x U(1)_chi anomalies + nu^c-omission (0,0,0,0,5,125) control, symbolic
          STr M_{Z'_chi}^2 == 0, BL1-F1 M_SS/A_*^{-1/2} & B_eff, and forensic catch AGY-C38-N1 (32-digit
          vs 45-digit |tau_* - 1/2|^2 == 1/4 semicircle precision ceiling).
  - PA_3: Independent Zero-Shared-Code Countercheck of AGY-002 (OW26 v8 & OW27 v8 @ 22b08aff1):
          Three-seat convergence on Dirac s=1/2 Gramian G^(s=1/2)(tau_8^+) & b_c^*(tau_8^+), M=8 CIM
          (8,8,16) triple overlaps, closed-form analytic gluino FCNC dilution & exact 25/58 Bino LSP,
          symbolic DISC-V7-2 1-loop top Higgs pole RG invariance + symbolic DISC-OW27-1 5-flavor QED
          top-decoupling sign, 4th-order Richardson Crank-Nicolson stiff MSSM Boltzmann Y_B, Borromean
          j((2+i)/5) = 1728, Guardrail-5 catch A2-OW26-F1 (6th continuous lever m_0/v_EW), and pure-math
          resolution A2-OW27-F2 showing Gamma_0(2)-equivariant Out(D_5) branch (3,0,2) hits all 3 blind
            OW24-C PMNS intervals simultaneously where non-equivariant (3,2,0) gave 0/192.
  - PA_4: Independent Symbolic Verification of PHYSICAL (`origin/audit/physical-bridge-2026-09-05` @ `32514763f`):
          Offset-2 double-return polynomial (z+1)^2, absence of +1 interior eigenvalue on W_2 (+) W_{-2},
          and complete-cusp collar residual scaling ||F(A_eps)||^2 = (6/5 ell) eps^5 = o(eps^4).

Guardrails enforced:
  - 0 Python float/complex AST literals, 0 binary64 float()/complex() casts, 0 JSON floats.
  - 0 imports from frontier/, peer scripts, snappy, or prior relay scripts.
  - 0 empirical PDG/NuFIT/Planck/DESI/CODATA constants (strictly 0 of 19).
"""

from __future__ import annotations

import ast
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction as Fr
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[2]
SELF_PATH = Path(__file__).resolve()
OUT_PATH = SELF_PATH.parent / "verify_r_peer_audit_all_seats_out.json"

AGY_REV = "b06c8fc1ebd74cbacebda84df3f65ad6a8e78ed3"
A2_REV_OW26 = "c00b3bb730a0f1ae0987ceec84f3c6106a526c3d"
A2_REV_OW27 = "22b08aff1b31642a1bdd91f990c4a3b95bc78805"
PHYS_REV = "32514763ff52b552a4ab6e51b7ba36c8b37017e7"

I_MP = mp.mpc(0, 1)


def q_mp(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def f_mp(fr: Fr) -> mp.mpf:
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def p10_mp(e: int) -> mp.mpf:
    return mp.mpf(10) ** int(e)


def frac_str(fr: Fr) -> str:
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)


def assert_no_json_floats(obj: Any) -> None:
    if isinstance(obj, float):
        raise AssertionError(f"Forbidden JSON float: {obj!r}")
    if isinstance(obj, dict):
        for v in obj.values():
            assert_no_json_floats(v)
    elif isinstance(obj, list):
        for v in obj.values() if isinstance(obj, dict) else obj:
            assert_no_json_floats(v)


def scan_ast_self(src: str, label: str) -> dict[str, Any]:
    tree = ast.parse(src, filename=label)
    lits = [
        getattr(n, "lineno", 0)
        for n in ast.walk(tree)
        if isinstance(n, ast.Constant) and isinstance(n.value, (float, complex))
    ]
    casts = [
        getattr(n, "lineno", 0)
        for n in ast.walk(tree)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ("float", "complex")
    ]
    imps: list[str] = []
    for n in ast.walk(tree):
        if isinstance(n, (ast.Import, ast.ImportFrom)):
            mod = getattr(n, "module", "") or ""
            nms = [a.name for a in n.names]
            comb = mod + " " + " ".join(nms)
            if any(w in comb for w in ("frontier", "relays", "self_consistent", "phase10", "c29", "c30", "snappy")):
                imps.append(comb)
    return {
        "float_complex_literals": len(lits),
        "binary64_casts": len(casts),
        "forbidden_imports": len(imps),
        "clean": bool(len(lits) == 0 and len(casts) == 0 and len(imps) == 0),
    }


def git_blob(repo_dir: Path, rev_spec: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo_dir), "show", rev_spec])


def find_dict_key(obj: Any, target: str) -> Any:
    if isinstance(obj, dict):
        if target in obj:
            return obj[target]
        for v in obj.values():
            r = find_dict_key(v, target)
            if r is not None:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = find_dict_key(v, target)
            if r is not None:
                return r
    return None


# ==============================================================================
# PA_1: Cryptographic SHA-256 Custody Audit of AGY (b06c8fc1e) & AGY-002 (22b08aff1)
# ==============================================================================

def run_pa_1(repo_dir: Path) -> dict[str, Any]:
    agy_dirs = [
        "relays/agy_2026-11-22_c35",
        "relays/agy_2026-11-23_c36",
        "relays/agy_2026-11-23_c37",
        "relays/agy_2026-11-24_c38",
    ]
    agy_manifest_count = 0
    agy_all_ok = True
    for folder in agy_dirs:
        for mf in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt", "COUNTERCHECK_SCRIPT_SHA256.txt"):
            txt = git_blob(repo_dir, f"{AGY_REV}:{folder}/{mf}").decode("utf-8").strip()
            for line in txt.splitlines():
                pts = line.split()
                exp_h, fn = pts[0], Path(pts[1].lstrip("*")).name
                act_h = hashlib.sha256(git_blob(repo_dir, f"{AGY_REV}:{folder}/{fn}")).hexdigest()
                if act_h != exp_h:
                    agy_all_ok = False
                agy_manifest_count += 1

    a2_dirs = [
        "relays/a2_ow26_v8",
        "relays/a2_ow16_v18",
        "relays/a2_ow26_referee_v3",
        "relays/a2_ow27_v8",
        "relays/a2_ow16_v22",
        "relays/a2_ow27_referee_v3",
    ]
    a2_manifest_count = 0
    a2_all_ok = True
    for folder in a2_dirs:
        for mf in ("SCRIPT_SHA256.txt", "OUTPUT_SHA256.txt"):
            txt = git_blob(repo_dir, f"{A2_REV_OW27}:{folder}/{mf}").decode("utf-8").strip()
            for line in txt.splitlines():
                pts = line.split()
                exp_h, fn = pts[0], Path(pts[1].lstrip("*")).name
                act_h = hashlib.sha256(git_blob(repo_dir, f"{A2_REV_OW27}:{folder}/{fn}")).hexdigest()
                if act_h != exp_h:
                    a2_all_ok = False
                a2_manifest_count += 1

    ow26_j = json.loads(git_blob(repo_dir, f"{A2_REV_OW27}:relays/a2_ow26_v8/a2_ow26_v8_results.json").decode("utf-8"))
    ow27_j = json.loads(git_blob(repo_dir, f"{A2_REV_OW27}:relays/a2_ow27_v8/a2_ow27_v8_results.json").decode("utf-8"))
    lock_v2 = find_dict_key(ow26_j, "blind_prediction_lock_v2_B4_UV")
    lock_v3 = find_dict_key(ow27_j, "blind_prediction_lock_v3_B4_UV")
    sha_v2 = hashlib.sha256(json.dumps(lock_v2, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    sha_v3 = hashlib.sha256(json.dumps(lock_v3, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    exp_v2 = "dab1f7e24f2057d54e63edd76feaab24ffc8997fc464c08e9ca31321d9639658"
    exp_v3 = "ce81cddd9d056a54fafa6b30d431073ae1af75399a1d82918f4e074f0bd98a2a"

    # Planted control PC_PA_1: mutating 1 byte of canonical lock_v3 JSON invalidates sha_v3:
    bad_sha_v3 = hashlib.sha256((json.dumps(lock_v3, sort_keys=True, separators=(",", ":")) + " ").encode("utf-8")).hexdigest()
    pc_pa_1 = bool(sha_v2 == exp_v2 and sha_v3 == exp_v3 and bad_sha_v3 != exp_v3)

    passed = bool(agy_all_ok and a2_all_ok and agy_manifest_count >= 12 and a2_manifest_count == 12 and pc_pa_1)
    return {
        "agy_c35_c38_manifest_files_verified": agy_manifest_count,
        "agy002_ow26_ow27_manifest_files_verified": a2_manifest_count,
        "lock_v2_sha256_verified": bool(sha_v2 == exp_v2),
        "lock_v3_sha256_verified": bool(sha_v3 == exp_v3),
        "pc_pa_1_planted_control_caught": pc_pa_1,
        "_ow26_j": ow26_j,
        "passed": passed,
    }


# ==============================================================================
# PA_2: Independent Countercheck of AGY (C37/C38 & v7.json @ b06c8fc1e)
# ==============================================================================

def run_pa_2(repo_dir: Path) -> dict[str, Any]:
    mp.mp.dps = 55
    v7_j = json.loads(git_blob(repo_dir, f"{AGY_REV}:relays/agy_2026-11-23_c37/blind_predictions_full_toe_v7.json").decode("utf-8"))
    c37_j = json.loads(git_blob(repo_dir, f"{AGY_REV}:relays/agy_2026-11-23_c37/c37_out.json").decode("utf-8"))
    c38_j = json.loads(git_blob(repo_dir, f"{AGY_REV}:relays/agy_2026-11-24_c38/c38_out.json").decode("utf-8"))

    # 1. Lobachevsky integral Vol(m004) = -6 int_0^{pi/3} ln(2 sin u) du -> M_11/M_GUT:
    vol_m004 = -mp.mpf(6) * mp.quad(lambda u: mp.log(mp.mpf(2) * mp.sin(u)), [mp.mpf(0), mp.pi / mp.mpf(3)])
    m11_mgut = (mp.mpf(40) * (mp.pi ** 3) / vol_m004) ** q_mp(1, 3)
    m11_v7_node = find_dict_key(v7_j, "m11_over_mgut_zero_knob")
    m11_v7_str = m11_v7_node["value"] if isinstance(m11_v7_node, dict) else str(m11_v7_node)
    err_m11 = abs(m11_mgut - mp.mpf(m11_v7_str))

    # 2. Conformal S_{+4} N=60 inflation:
    y_end = mp.mpf(1) + mp.mpf(2) / mp.sqrt(mp.mpf(3))
    y_60 = mp.findroot(lambda y: q_mp(3, 4) * ((y - y_end) - mp.log(y / y_end)) - mp.mpf(60), mp.mpf(82))
    eps_60 = mp.mpf(4) / (mp.mpf(3) * ((y_60 - mp.mpf(1)) ** 2))
    eta_60 = -mp.mpf(4) * (y_60 - mp.mpf(2)) / (mp.mpf(3) * ((y_60 - mp.mpf(1)) ** 2))
    ns_60 = mp.mpf(1) - mp.mpf(6) * eps_60 + mp.mpf(2) * eta_60
    r_60 = mp.mpf(16) * eps_60
    ns_v7 = find_dict_key(v7_j, "inflation_conformal_S4_ns_N60")
    r_v7 = find_dict_key(v7_j, "inflation_conformal_S4_r_N60")
    ns_str = ns_v7["value"] if isinstance(ns_v7, dict) else str(ns_v7)
    r_str = r_v7["value"] if isinstance(r_v7, dict) else str(r_v7)
    err_ns = abs(ns_60 - mp.mpf(ns_str))
    err_r = abs(r_60 - mp.mpf(r_str))

    # 3. C38 4-modulus semicircle residual (AGY-C38-N1 catch: 32 true digits out of 45 printed) & 2HDM quartics:
    mod4 = find_dict_key(c38_j, "four_modulus_newton_t_s_re_im_45d")
    s_c38 = mp.mpf(mod4[1])
    rx_c38, ry_c38 = mp.mpf(mod4[2]), mp.mpf(mod4[3])
    gcp_resid_c38 = abs((rx_c38 - q_mp(1, 2)) ** 2 + ry_c38 ** 2 - q_mp(1, 4))

    q_c38 = [mp.mpf(x) for x in find_dict_key(c38_j, "derived_2hdm_quartics_at_s_star_35d")]
    lam1 = mp.mpf(8) * mp.pi / (mp.mpf(5) * s_c38)
    lam3 = mp.mpf(2) * mp.pi / (mp.mpf(5) * s_c38)
    lam4 = -mp.mpf(2) * mp.pi / s_c38 + q_mp(9, 25)
    err_q = max(abs(lam1 - q_c38[0]), abs(lam1 - q_c38[1]), abs(lam3 - q_c38[2]), abs(lam4 - q_c38[3]))

    # 4. BL1-F1 M_SS / A_*^{-1/2} and B_eff:
    tau_c38 = rx_c38 + I_MP * ry_c38
    mss_min = min(
        mp.mpf(2) * mp.pi * abs((mp.mpf(m1) + q_mp(1, 2)) - tau_c38 * (mp.mpf(m2) + q_mp(1, 2))) / mp.sqrt(ry_c38)
        for m1 in range(-3, 4) for m2 in range(-3, 4)
    )
    beff_ss = mp.mpf(5) / (mp.mpf(9) - mp.mpf(2) * (mp.log(mp.mpf(2)) / mp.mpf(33)))
    mss_c37 = mp.mpf(str(find_dict_key(c37_j, "BL1_F1_M_SS_over_A_inv_sqrt")))
    err_mss = abs(mss_min - mss_c37)

    # 5. Symbolic 6/6 G_SM x U(1)_chi anomalies + nu^c omission control + symbolic STr M_{Z'_chi}^2 == 0:
    wts_16 = [s for s in itertools.product((Fr(1, 2), Fr(-1, 2)), repeat=5) if s.count(Fr(-1, 2)) % 2 == 0]

    def calc_anoms(wlist: list[tuple[Fr, ...]]) -> list[int]:
        a3 = a2 = ay2 = ax2 = ag = ax3 = Fr(0)
        for w in wlist:
            y6 = 2 * (w[0] + w[1] + w[2]) - 3 * (w[3] + w[4])
            qx = -2 * sum(w)
            ag += qx
            ax3 += qx ** 3
            ay2 += (y6 ** 2) * qx
            ax2 += y6 * (qx ** 2)
            if sum(1 for x in w[:3] if x < 0) in (1, 2):
                a3 += Fr(1, 6) * qx
            if sum(1 for x in w[3:] if x < 0) == 1:
                a2 += Fr(1, 4) * qx
        return [int(a3), int(a2), int(ay2), int(ax2), int(ag), int(ax3)]

    anoms_16 = calc_anoms(wts_16)
    anoms_15 = calc_anoms([w for w in wts_16 if w != (Fr(1, 2),) * 5])

    gs, vs = sp.symbols("gs vs", positive=True)
    x1, y1, x2, y2 = sp.symbols("x1 y1 x2 y2", real=True)
    vd = sp.Rational(1, 2) * (gs ** 2) * (10 * ((vs + x1 / sp.sqrt(2)) ** 2 + (y1 / sp.sqrt(2)) ** 2) - 10 * ((vs + x2 / sp.sqrt(2)) ** 2 + (y2 / sp.sqrt(2)) ** 2)) ** 2
    tr_scal = sp.hessian(vd, (x1, y1, x2, y2)).subs({x1: 0, y1: 0, x2: 0, y2: 0}).trace()
    mf = sp.Matrix([[0, 10 * sp.sqrt(2) * gs * vs, -10 * sp.sqrt(2) * gs * vs], [10 * sp.sqrt(2) * gs * vs, 0, 0], [-10 * sp.sqrt(2) * gs * vs, 0, 0]])
    str_u1chi = sp.simplify(3 * (400 * gs ** 2 * vs ** 2) + tr_scal - 2 * (mf.H * mf).trace())

    pc_pa_2 = bool(anoms_15 == [0, 0, 0, 0, 5, 125] and p10_mp(-34) < gcp_resid_c38 < p10_mp(-30))
    passed = bool(
        err_m11 < p10_mp(-28)
        and err_ns < p10_mp(-28) and err_r < p10_mp(-28)
        and err_q < p10_mp(-33)
        and err_mss < p10_mp(-11)
        and anoms_16 == [0, 0, 0, 0, 0, 0]
        and str_u1chi == 0
        and pc_pa_2
    )
    return {
        "m11_over_mgut_lobachevsky_diff": mp.nstr(err_m11, 8),
        "s4_inflation_ns_and_r_diffs": [mp.nstr(err_ns, 8), mp.nstr(err_r, 8)],
        "c38_gcp_semicircle_resid_32d_ceiling": mp.nstr(gcp_resid_c38, 10),
        "c38_2hdm_quartics_max_diff": mp.nstr(err_q, 8),
        "bl1_f1_mss_diff_and_beff": [mp.nstr(err_mss, 8), mp.nstr(beff_ss, 12)],
        "u1chi_6_anoms_full_and_no_nuc": [anoms_16, anoms_15],
        "u1chi_symbolic_supertrace_zero": bool(str_u1chi == 0),
        "pc_pa_2_planted_control_caught": pc_pa_2,
        "passed": passed,
    }


# ==============================================================================
# PA_3: Independent Countercheck of AGY-002 (OW26 v8 & OW27 v8 @ 22b08aff1)
# ==============================================================================

def eval_w_hol_tau_pa(tau: mp.mpc, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = q_mp(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    q = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = mp.mpc(0)
    for n in range(-24, 25):
        m2 = q_mp((2 * n + 1) ** 2, 8)
        e2v = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau * m2)
        t2 += e2v
        dt2 += m2 * e2v
        m3 = q_mp(n * n, 2)
        e3v = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau * m3)
        t3 += e3v
        dt3 += m3 * e3v
        sg = -1 if (n % 2 != 0) else 1
        t4 += sg * e3v
        dt4 += sg * m3 * e3v
    e2s = mp.mpc(1)
    qn = q
    for n in range(1, 44):
        e2s -= mp.mpf(24 * n) * (qn / (mp.mpc(1) - qn))
        qn *= q
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / mp.mpf(24)) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / mp.mpf(24)) * qj
        + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / mp.mpf(24)) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    pr = mp.mpc(1)
    qn = q
    for _ in range(44):
        pr *= mp.mpc(1) - qn
        qn *= q
    t1p = mp.mpf(2) * mp.pi * (mp.exp(I_MP * mp.pi * tau / mp.mpf(12)) * pr) ** 3
    yi = mp.im(tau)

    def thc(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = f_mp(ta), f_mp(tb)
        zv = am * tau + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        s = mp.fsum(
            mp.exp(I_MP * mp.pi * tau * (mp.mpf(k) ** 2) + mp.mpf(2) * I_MP * mp.pi * mp.mpf(k) * zv)
            for k in range(n0 - 22, n0 + 23)
        )
        b = mp.exp(I_MP * mp.pi * am * am * tau + mp.mpf(2) * I_MP * mp.pi * am * bm) * s
        return b if (nb == 0 or ta == 0) else mp.exp(mp.mpf(2) * I_MP * mp.pi * am * mp.mpf(nb)) * b

    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-mp.mpf(2) * I_MP * mp.pi * f_mp(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    hfr = Fr(1, 2)
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        if ((cs[sk][0] - hfr) % 1 == 0 and (cs[sk][1] - hfr) % 1 == 0) or (
            (ds[sk][0] - hfr) % 1 == 0 and (ds[sk][1] - hfr) % 1 == 0
        ):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = kap[sk] * thc(cs[sk][0], cs[sk][1]) * thc(ds[sk][0], ds[sk][1]) / t1p
    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    return mp.matrix([
        [
            ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1]
            + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1]
            for cb in range(3)
        ]
        for ra in range(3)
    ])


def run_pa_3(repo_dir: Path, ow26_j: dict[str, Any]) -> dict[str, Any]:
    mp.mp.dps = 50
    # 1. Three-seat G^(s=1/2)(tau_8^+) & b_c^*(tau_8^+) convergence:
    l8_j = json.loads((repo_dir / "relays/x_floor_link8_verify/verify_x_floor_link8_out.json").read_text(encoding="utf-8"))
    g_exp = [mp.mpf(x) for x in l8_j["L8_5_unified_zero_placeholder_uv_to_ir_blind_lock"]["dirac_s12_gramian_tau8"]]
    g_a2 = [mp.mpf(x) for x in find_dict_key(ow26_j, "G_s12_dirac_unit_mean_t8")]
    gram_diff = max(abs(g_exp[i] - g_a2[i]) for i in range(3))

    # 2. M=8 CIM (8, 8, 16) triple overlaps at tau_0 = (2 + i)/5:
    tau0 = q_mp(2, 5) + I_MP * q_mp(1, 5)
    pref = (mp.mpf(8) * mp.im(tau0)) ** q_mp(1, 4)
    invs2 = mp.mpf(1) / mp.sqrt(mp.mpf(2))

    def raw_cim(j1: int, j2: int, j3: int) -> mp.mpc:
        if (j1 + j2 - j3) % 8 != 0:
            return mp.mpc(0)
        rp = ((j3 - j1 - j2) // 8) % 2
        shf = q_mp((j1 - j2 + 8 * rp) % 16, 16)
        return pref * mp.fsum(mp.exp(I_MP * mp.pi * mp.mpf(16) * tau0 * ((mp.mpf(q) + shf) ** 2)) for q in range(-16, 17))

    cim_sv: dict[int, mp.mpf] = {}
    for kh in (0, 1, 2):
        ym = mp.zeros(3, 3)
        for ai, k1 in enumerate((1, 2, 3)):
            for bi, k2 in enumerate((1, 2, 3)):
                val = mp.mpc(0)
                for s1, j1 in ((invs2, k1), (-invs2, 8 - k1)):
                    for s2, j2 in ((invs2, k2), (-invs2, 8 - k2)):
                        if kh == 0:
                            val += s1 * s2 * raw_cim(j1, j2, 0)
                        else:
                            val += s1 * s2 * invs2 * (raw_cim(j1, j2, kh) + raw_cim(j1, j2, 16 - kh))
                ym[ai, bi] = val
        _, svs, _ = mp.svd_c(ym)
        cim_sv[kh] = max(svs)
    cim_kh0_a2 = mp.mpf(str(find_dict_key(ow26_j, "magnetized_M16_Higgs_kH0_yt_over_gUV")))
    cim_kh0_diff = abs(cim_sv[0] - cim_kh0_a2)

    # 3. Closed-form analytic Gluino FCNC dilution & exact 25/58 Bino LSP:
    al0 = q_mp(1, 24)
    ts_a2 = -mp.mpf(48) * mp.pi / mp.mpf(5)
    bs = (q_mp(33, 5), mp.mpf(1), mp.mpf(-3))
    c2s = (q_mp(1, 60), q_mp(3, 4), q_mp(4, 3))
    als = [al0 / (mp.mpf(1) - (b * al0 / (mp.mpf(2) * mp.pi)) * ts_a2) for b in bs]
    dmq = sum((mp.mpf(2) * c2 / b) * (mp.mpf(1) - ((al / al0) ** 2)) for c2, b, al in zip(c2s, bs, als))
    gi0, gi1 = mp.mpf(1) / g_a2[0], mp.mpf(1) / g_a2[1]
    mi = (gi0 + gi1) / mp.mpf(2)
    q1u, q2u = gi0 / mi, gi1 / mi
    ir_split_analytic = abs((q2u + dmq) - (q1u + dmq)) / ((q2u + dmq) + (q1u + dmq))
    ir_split_a2 = mp.mpf(str(find_dict_key(ow26_j, "ir_gluino_diluted_split")))
    fcnc_diff = abs(ir_split_analytic - ir_split_a2)

    # 4. Symbolic DISC-V7-2 (Sirlin-Zucchini RG invariance) & DISC-OW27-1 (5-flavor QED top decoupling sign):
    lam_s, yt_s = sp.symbols("lam yt", positive=True)
    rg_sz = sp.simplify((12 * lam_s * yt_s ** 2 - 12 * yt_s ** 4) + lam_s * 3 * yt_s ** 2 * (2 - 2 * yt_s ** 2 / lam_s) * (-2))
    b_qed_top = Fr(4, 3) * 3 * (Fr(2, 3) ** 2)

    # 5. Independent 4th-order Richardson Crank-Nicolson Stiff MSSM Boltzmann Y_B:
    boltz_s12 = ow26_j["OW26_C_sequential_seesaw_boltzmann_lsp_and_proton"]["sequential_seesaw_CURV_s12_Dirac_CP_selected"]["boltzmann_leptogenesis"]
    k_flav = [mp.mpf(x) for x in boltz_s12["K_flav"]]
    eps_flav = [mp.mpf(x) for x in boltz_s12["eps_flav"]]
    k_tot = sum(k_flav)
    u0, u1 = mp.log(q_mp(1, 10)), mp.log(mp.mpf(100))
    conv_yb = q_mp(8, 23) * (mp.mpf(135) * mp.zeta(3) / (mp.mpf(2) * (mp.pi ** 4) * q_mp(915, 4)))

    def cn_boltz(nst: int) -> mp.mpf:
        du = (u1 - u0) / mp.mpf(nst)
        rts = []
        for j in range(nst + 1):
            zv = mp.exp(u0 + mp.mpf(j) * du)
            k1, k2 = mp.besselk(1, zv), mp.besselk(2, zv)
            rts.append((k_tot * (zv ** 2) * (k1 / k2), q_mp(1, 2) * (zv ** 2) * k2, q_mp(1, 4) * (zv ** 4) * k1))
        nn = mp.mpf(0)
        ndf = [mp.mpf(0)] * 3
        for j in range(nst):
            d0, neq0, w0 = rts[j]
            d1, neq1, w1 = rts[j + 1]
            nn_new = (nn + (du / mp.mpf(2)) * (-d0 * (nn - neq0) + d1 * neq1)) / (mp.mpf(1) + (du / mp.mpf(2)) * d1)
            dn = nn_new - nn
            for a in range(3):
                ndf[a] = (ndf[a] + eps_flav[a] * dn - (du / mp.mpf(2)) * (k_flav[a] * w0) * ndf[a]) / (mp.mpf(1) + (du / mp.mpf(2)) * (k_flav[a] * w1))
            nn = nn_new
        return conv_yb * sum(ndf)

    yb_cn = (mp.mpf(4) * cn_boltz(600) - cn_boltz(300)) / mp.mpf(3)
    yb_a2 = mp.mpf(str(boltz_s12["Y_B_flavored_zero_init"]))
    yb_rel_diff = abs(yb_cn - yb_a2) / abs(yb_a2)

    # 6. Pure-Math Resolution A2-OW27-F2: exact Takagi (verified to < 1e-42 & Haar-invariant) on Gamma_0(2)-equivariant Out(D_5) branch (3, 0, 2) at tau_8^+:
    tau8 = q_mp(16, 5) + I_MP * q_mp(8, 5)
    k5 = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6 = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]
    we = (sum((eval_w_hol_tau_pa(tau8, a, b, -3, 6) for a, b in k5), mp.zeros(3, 3)) / mp.mpf(4) + sum((eval_w_hol_tau_pa(tau8, a, b, -3, 6) for a, b in k6), mp.zeros(3, 3)) / mp.mpf(2)) / mp.mpf(2)
    wnu = (sum((eval_w_hol_tau_pa(tau8, a, b, 3, -5) for a, b in k5), mp.zeros(3, 3)) / mp.mpf(4) + sum((eval_w_hol_tau_pa(tau8, a, b, 3, -5) for a, b in k6), mp.zeros(3, 3)) / mp.mpf(2)) / mp.mpf(2)
    wr = (sum((eval_w_hol_tau_pa(tau8, a, b, 3, 3) for a, b in k5), mp.zeros(3, 3)) / mp.mpf(4) + sum((eval_w_hol_tau_pa(tau8, a, b, 3, 3) for a, b in k6), mp.zeros(3, 3)) / mp.mpf(2)) / mp.mpf(2)
    wrs = (wr + wr.T) / mp.mpf(2)
    _, svr_l, _ = mp.svd_c(wrs)
    mr = mp.eye(3) + wrs / max(svr_l)
    kis = mp.diag([mp.mpf(1) / mp.sqrt(v) for v in g_exp])
    eps5 = mp.exp(mp.mpf(2) * I_MP * mp.pi * tau8 / mp.mpf(5))

    def exact_pmns_for_n10(n10: tuple[int, int, int], ul_rot: mp.matrix | None = None) -> tuple[list[mp.mpf], mp.mpf]:
        d10 = mp.diag([eps5 ** n for n in n10])
        ye = kis * we * d10 * kis
        ynu = kis * wnu
        if ul_rot is not None:
            ye = ul_rot * ye
            ynu = ul_rot * ynu
        ue_raw, se_raw, _ = mp.svd_c(ye)
        idx_e = sorted(range(3), key=lambda i: se_raw[i])
        ue = mp.matrix([[ue_raw[r, idx_e[c]] for c in range(3)] for r in range(3)])
        mnu = -ynu * (mr ** (-1)) * ynu.T
        # mp.svd_c(mnu) returns (um_r, sm_r, vhm_r) with mnu = um_r * diag(sm_r) * vhm_r = ut * diag(s_sort) * ut.T:
        um_r, sm_r, vhm_r = mp.svd_c(mnu)
        idx_n = sorted(range(3), key=lambda i: sm_r[i])
        s_sort = [sm_r[i] for i in idx_n]
        us = mp.matrix([[um_r[r, idx_n[c]] for c in range(3)] for r in range(3)])
        vt = mp.matrix([[vhm_r[idx_n[c], r] for c in range(3)] for r in range(3)])
        z_diag = us.H * vt
        ut = us * mp.diag([mp.exp(I_MP * mp.arg(z_diag[k, k]) / mp.mpf(2)) for k in range(3)])
        takagi_err = mp.norm(mnu - ut * mp.diag(s_sort) * ut.T)
        # In holomorphic Weyl superpotential W = L^T Y_e e^c H_d + L^T Y_nu nu^c H_u, L -> U_L^* L sends U_e -> U_L U_e and U_T -> U_L U_T => U_PMNS = U_e^H * U_T!
        upmns = ue.H * ut
        s13 = abs(upmns[0, 2]) ** 2
        s12 = (abs(upmns[0, 1]) ** 2) / (mp.mpf(1) - s13)
        s23 = (abs(upmns[1, 2]) ** 2) / (mp.mpf(1) - s13)
        return [s12, s23, s13], takagi_err

    # Deterministic Cayley unitary U_L(A) = (I - A)^(-1) * (I + A) with A^H = -A for Guardrail-3 U(3)_L invariance check:
    ah = mp.matrix([[I_MP * q_mp(3, 7), q_mp(2, 5) + I_MP * q_mp(1, 3), -q_mp(1, 4) + I_MP * q_mp(2, 9)],
                    [-q_mp(2, 5) + I_MP * q_mp(1, 3), -I_MP * q_mp(5, 11), q_mp(3, 8) + I_MP * q_mp(1, 6)],
                    [q_mp(1, 4) + I_MP * q_mp(2, 9), -q_mp(3, 8) + I_MP * q_mp(1, 6), I_MP * q_mp(1, 5)]])
    ul_cayley = ((mp.eye(3) - ah) ** (-1)) * (mp.eye(3) + ah)
    pmns_302, tak_err_302 = exact_pmns_for_n10((3, 0, 2))
    pmns_302_rot, _ = exact_pmns_for_n10((3, 0, 2), ul_cayley)
    haar_pmns_err = max(abs(pmns_302[i] - pmns_302_rot[i]) for i in range(3))
    pmns_320, tak_err_320 = exact_pmns_for_n10((3, 2, 0))
    ow24_hit_302 = bool(q_mp(3, 20) < pmns_302[0] < q_mp(11, 20) and q_mp(7, 20) < pmns_302[1] < q_mp(13, 20) and q_mp(1, 100) < pmns_302[2] < q_mp(1, 20))
    ow24_hit_320 = bool(q_mp(3, 20) < pmns_320[0] < q_mp(11, 20) and q_mp(7, 20) < pmns_320[1] < q_mp(13, 20) and q_mp(1, 100) < pmns_320[2] < q_mp(1, 20))

    # 7. Guardrail-5 catch A2-OW26-F1: verify m_0 = 10v vs m_0 = 3v in lock_v2 shifts alpha3_mz by > 3e-2:
    a3_10v = mp.mpf(str(find_dict_key(ow26_j, "gauge_at_MZ_m0_10v")["alpha3_mz"]))
    a3_3v = mp.mpf(str(find_dict_key(ow26_j, "gauge_at_MZ_m0_3v")["alpha3_mz"]))
    m0_lever_shift = abs(a3_10v - a3_3v)

    pc_pa_3 = bool(ow24_hit_302 and (not ow24_hit_320) and m0_lever_shift > q_mp(3, 100))
    passed = bool(
        gram_diff < p10_mp(-5)
        and cim_kh0_diff < p10_mp(-10)
        and fcnc_diff < p10_mp(-10)
        and rg_sz == 0 and b_qed_top == Fr(16, 9)
        and yb_rel_diff < q_mp(2, 100000)
        and max(tak_err_302, tak_err_320) < p10_mp(-40)
        and haar_pmns_err < p10_mp(-40)
        and pc_pa_3
    )
    return {
        "three_seat_gramian_max_diff": mp.nstr(gram_diff, 8),
        "cim_8_8_16_sigma_max_kH_0_1_2": [mp.nstr(cim_sv[0], 12), mp.nstr(cim_sv[1], 12), mp.nstr(cim_sv[2], 12)],
        "cim_kh0_diff_vs_ow26": mp.nstr(cim_kh0_diff, 8),
        "closed_form_vs_ode_fcnc_split_diff": mp.nstr(fcnc_diff, 8),
        "sirlin_zucchini_rg_zero_and_qed_top_beta": [bool(rg_sz == 0), frac_str(b_qed_top)],
        "richardson_cn_vs_radau_yb_rel_diff": mp.nstr(yb_rel_diff, 8),
        "takagi_factorization_max_err": mp.nstr(max(tak_err_302, tak_err_320), 8),
        "equivariant_302_pmns_hits_ow24_window": [mp.nstr(x, 8) for x in pmns_302],
        "nonequivariant_320_pmns_misses_ow24": [mp.nstr(x, 8) for x in pmns_320],
        "a2_ow26_f1_m0_over_v_alpha3_shift": mp.nstr(m0_lever_shift, 8),
        "pc_pa_3_planted_control_caught": pc_pa_3,
        "passed": passed,
    }


# ==============================================================================
# PA_4: Independent Symbolic Verification of PHYSICAL (32514763f)
# ==============================================================================

def run_pa_4() -> dict[str, Any]:
    omega5 = sp.exp(2 * sp.pi * sp.I / 5)
    prod_ratios = sp.simplify((omega5 ** 2) ** 5)
    no_plus1_w2 = bool(sp.simplify(omega5 ** 4 - 1) != 0 and sp.simplify(omega5 ** (-4) - 1) != 0)
    z_s = sp.Symbol("z")
    poly_k2 = sp.factor(z_s ** 2 + 2 * z_s + 1)

    r_s, l_s, eps_s, ell_s = sp.symbols("r L eps ell", positive=True)
    chi = 1 - 3 * (r_s / l_s) ** 2 + 2 * (r_s / l_s) ** 3
    res_l2 = sp.integrate(sp.diff(chi, r_s) ** 2, (r_s, 0, l_s))      # 6 / (5 L)
    kin_l2 = sp.integrate(chi ** 2, (r_s, 0, l_s))                     # 13 L / 35
    e_cusp = sp.simplify((eps_s ** 4) * res_l2.subs(l_s, ell_s / eps_s))

    # Planted control PC_PA_4: fixed-cut L = ell (unscaled by 1/eps) retains O(eps^4) quartic energy (degree 4 != 5):
    e_fixed_cut = sp.simplify((eps_s ** 4) * res_l2.subs(l_s, ell_s))
    pc_pa_4 = bool(sp.degree(e_cusp, eps_s) == 5 and sp.degree(e_fixed_cut, eps_s) == 4)

    passed = bool(prod_ratios == 1 and no_plus1_w2 and poly_k2 == (z_s + 1) ** 2 and pc_pa_4)
    return {
        "offset2_ratio_product_one": bool(prod_ratios == 1),
        "offset2_square_no_plus1_interior": no_plus1_w2,
        "double_return_polynomial_factored": str(poly_k2),
        "collar_residual_and_kinetic_integrals": [str(res_l2), str(kin_l2)],
        "complete_cusp_energy_scaling": str(e_cusp),
        "pc_pa_4_planted_control_caught": pc_pa_4,
        "passed": passed,
    }


def main() -> None:
    src = SELF_PATH.read_text(encoding="utf-8")
    ast_audit = scan_ast_self(src, str(SELF_PATH.name))
    self_sha = hashlib.sha256(SELF_PATH.read_bytes()).hexdigest()

    repo_use = REPO_ROOT if (REPO_ROOT / ".git").exists() else Path("/Users/dri/.gemini/antigravity/scratch/origin-axiom-self-consistent-loop")
    p1 = run_pa_1(repo_use)
    ow26_j = p1.pop("_ow26_j")
    p2 = run_pa_2(repo_use)
    p3 = run_pa_3(repo_use, ow26_j)
    p4 = run_pa_4()

    all_ok = bool(ast_audit["clean"] and p1["passed"] and p2["passed"] and p3["passed"] and p4["passed"])
    payload = {
        "card": "AGY-EXP_R-PEER-AUDIT-ALL-SEATS",
        "script": str(SELF_PATH.name),
        "script_sha256": self_sha,
        "firewall": "0 of 19",
        "audited_peer_revisions": {
            "agy": AGY_REV,
            "agy_002_ow26": A2_REV_OW26,
            "agy_002_ow27": A2_REV_OW27,
            "physical": PHYS_REV,
        },
        "self_ast_hygiene": ast_audit,
        "PA_1_custody_and_lock_sha256": p1,
        "PA_2_agy_c37_c38_v7_countercheck": p2,
        "PA_3_agy002_ow26_ow27_countercheck": p3,
        "PA_4_physical_3251476_countercheck": p4,
        "all_4_modules_and_4_planted_controls_passed": all_ok,
    }
    assert_no_json_floats(payload)
    if not all_ok:
        raise AssertionError("One or more Peer-Audit modules or AST checks failed!")
    OUT_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
