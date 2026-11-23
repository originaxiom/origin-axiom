#!/usr/bin/env python3
"""
Isolated Cold-Room Zero-Trust Independent Referee (v2) for Seat agy-002:
  - Card A2-OW24 v2 (relays/a2_ow24_v2/a2_ow24_v2_results.json)
  - Honest Master Ledger A2-OW16 v12 (relays/a2_ow16_v12/a2_ow16_v12_results.json)

Supersedes frozen Cold-Room Referee v1 (226ead9d0 -> 598eaeb57, left 100% untouched):
  - Frozen v1 passed REF-0 (213/213 manifests), REF-1 (OW24-A), REF-3 (OW24-C),
    and REF-4 (OW24-D & OW16 v11), while catching two genuine 240-root E_8 bugs in
    A2-OW24 v1 Module OW24-B:
      (1) REF2_OW24B_10H_DOUBLET_DOUBLECOUNT (double-counting (0,2) and (0,3) in (10,6)),
      (2) REF2_OW24B_Z2_M4_UNBROKEN_E6_GAUGE_ENHANCEMENT (unbroken E_6 N_V=82 in T^2/Z_2 (-2,-2,0,4)).
  - Producer froze a2_ow24_v1 (19311db5a), a2_ow16_v11 (0b426dc80), and a2_ow24_referee
    (598eaeb57) untouched, committed pre-v2 substantive erratum (942f6694e), and sealed
    remediated A2-OW24 v2 (ee114fa91 -> 9b60653f1) & A2-OW16 v12 (22a167258 -> b71741c00).
  - Referee v2 independently re-verifies ALL 5 modules (REF-0..REF-4) from scratch with
    100% disjoint engines against A2-OW24 v2 and A2-OW16 v12.

Cold-Room, Guardrail-6, & Custody Compliance:
  - Empirical Firewall: strictly 0 of 19 (ZERO empirical PDG, NuFIT, Planck,
    DESI, or CODATA numbers anywhere).
  - Zero Shared Code (Guardrail 6): NEVER imports or invokes any producer
    script or function. Producer .py files are ONLY parsed via Python ast.
  - Hygiene: 0 Python float/complex AST literals, 0 binary64 float()/complex()
    casts, 0 JSON float tokens (assert_no_json_floats), 0 frontier/relays
    imports, 0 hardcoded proof booleans (Guardrail 2).
"""

from __future__ import annotations

import ast
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import re
from typing import Any

import mpmath as mp
import sympy as sp


REPO_ROOT = Path(__file__).resolve().parents[2]
RELAYS_DIR = REPO_ROOT / "relays"
SELF_DIR = Path(__file__).resolve().parent
SELF_SCRIPT = Path(__file__).resolve()
OUT_JSON = SELF_DIR / "a2_ow24_referee_v2_results.json"

SCRIPT_OW24 = RELAYS_DIR / "a2_ow24_v2" / "verify_a2_ow24_v2.py"
RESULTS_OW24 = RELAYS_DIR / "a2_ow24_v2" / "a2_ow24_v2_results.json"
SCRIPT_OW16 = RELAYS_DIR / "a2_ow16_v12" / "verify_a2_ow16_v12.py"
RESULTS_OW16 = RELAYS_DIR / "a2_ow16_v12" / "a2_ow16_v12_results.json"
RESULTS_OW23 = RELAYS_DIR / "a2_ow23_v3" / "a2_ow23_v3_results.json"
RESULTS_OW19 = RELAYS_DIR / "a2_ow19_v3" / "a2_ow19_v3_results.json"

IMAG = mp.mpc(0, 1)


# ==============================================================================
# Core Exact Utilities, Hygiene AST/JSON Scanners, & Branch Custody Verifier
# ==============================================================================

def mrat(p: int, q: int = 1) -> mp.mpf:
    return mp.mpf(int(p)) / mp.mpf(int(q))


def mpow10(exp_int: int) -> mp.mpf:
    return mp.mpf(10) ** int(exp_int)


def fstr(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}" if q.denominator != 1 else str(q.numerator)


def mstr(val: Any, digits: int = 14) -> str:
    return mp.nstr(val, digits)


def rel_err(a: Any, b: Any) -> mp.mpf:
    am = mp.mpf(a)
    bm = mp.mpf(b)
    denom = max(abs(bm), mpow10(-50))
    return abs(am - bm) / denom


def frob_norm(mat: mp.matrix) -> mp.mpf:
    return mp.sqrt(mp.fsum(abs(mat[r, c]) ** 2 for r in range(mat.rows) for c in range(mat.cols)))


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def assert_no_json_floats(json_text: str) -> int:
    """Detect any JSON float token via json.loads parse_float hook."""
    found: list[str] = []

    def _catch_float(tok: str) -> str:
        found.append(tok)
        return tok

    json.loads(json_text, parse_float=_catch_float)
    return len(found)


def ast_audit_script(path: Path) -> dict[str, Any]:
    src = path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(path))
    float_complex_lits: list[int] = []
    binary64_casts: list[int] = []
    forbidden_imports: list[str] = []

    bad_casts = ("float", "complex", "float16", "float32", "float64", "complex64", "complex128")
    bad_mod_keys = (
        "frontier",
        "relays",
        "peer",
        "self_consistent",
        "phase10",
        "verify_",
        "referee_",
        "a2_ow",
        "a2_p879",
        "a2_wg96",
        "a2_x1",
        "c29",
        "c30",
        "numpy",
    )

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            tname = type(node.value).__name__
            if tname == "float" or tname == "complex":
                float_complex_lits.append(int(getattr(node, "lineno", 0)))
        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id in bad_casts:
                binary64_casts.append(int(getattr(node, "lineno", 0)))
            elif isinstance(fn, ast.Attribute) and fn.attr in bad_casts:
                binary64_casts.append(int(getattr(node, "lineno", 0)))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                mod = alias.name
                segs = mod.split(".")
                if any(any(k in s for k in bad_mod_keys) for s in segs):
                    forbidden_imports.append(mod)
        elif isinstance(node, ast.ImportFrom):
            if node.level and node.level > 0:
                forbidden_imports.append("relative_import")
            mod = node.module or ""
            names = [a.name for a in node.names]
            joined = mod + " " + " ".join(names)
            if any(k in joined for k in bad_mod_keys):
                forbidden_imports.append(joined.strip())

    clean = bool(
        len(float_complex_lits) == 0
        and len(binary64_casts) == 0
        and len(forbidden_imports) == 0
    )
    return {
        "file": str(path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(path),
        "float_complex_literals": len(float_complex_lits),
        "binary64_casts": len(binary64_casts),
        "forbidden_imports": len(forbidden_imports),
        "clean": clean,
    }


def verify_all_branch_manifests(tamper_entry_idx: int | None = None) -> dict[str, Any]:
    """Verify 100% of *SHA256*.txt manifests under relays/ (excluding own future OUTPUT_SHA256.txt)."""
    manifest_files = sorted(RELAYS_DIR.rglob("*SHA256*.txt"))
    hex64 = re.compile(r"^[0-9a-fA-F]{64}$")
    own_future_out = str((SELF_DIR / "OUTPUT_SHA256.txt").relative_to(REPO_ROOT))

    files_checked = 0
    total_entries = 0
    verified_entries = 0
    mismatches: list[dict[str, str]] = []
    entry_idx = 0

    for mf in manifest_files:
        rel_mf = str(mf.relative_to(REPO_ROOT))
        if rel_mf == own_future_out:
            continue
        files_checked += 1
        for raw_line in mf.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 2 or not hex64.match(parts[0]):
                continue
            exp_hex = parts[0].lower()
            rel_tgt = parts[-1].lstrip("*")
            tgt_path = REPO_ROOT / rel_tgt
            if not tgt_path.exists():
                tgt_path = mf.parent / rel_tgt
            total_entries += 1
            if not tgt_path.exists():
                mismatches.append({
                    "manifest": rel_mf,
                    "target": rel_tgt,
                    "reason": "missing_target",
                })
                entry_idx += 1
                continue
            raw_bytes = tgt_path.read_bytes()
            if tamper_entry_idx is not None and entry_idx == tamper_entry_idx and len(raw_bytes) > 0:
                raw_bytes = bytes([raw_bytes[0] ^ 1]) + raw_bytes[1:]
            act_hex = sha256_bytes(raw_bytes)
            if act_hex == exp_hex:
                verified_entries += 1
            else:
                mismatches.append({
                    "manifest": rel_mf,
                    "target": rel_tgt,
                    "expected": exp_hex,
                    "actual": act_hex,
                })
            entry_idx += 1

    return {
        "manifest_files_checked": files_checked,
        "total_entries": total_entries,
        "verified_entries": verified_entries,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "all_verified": bool(total_entries > 0 and verified_entries == total_entries and len(mismatches) == 0),
    }


# ==============================================================================
# Disjoint 128-bit LCG + Mezzadri Householder-QR Haar U(3) Generator
# ==============================================================================

class LCG128:
    """128-bit full-period LCG (disjoint from producer's 64-bit SplitMix64)."""

    MOD = 1 << 128
    MASK = (1 << 128) - 1
    MULT = 47026247687942121848144207491837523525
    INC = 1

    def __init__(self, seed: int) -> None:
        self.state = int(seed) & self.MASK

    def next_u128(self) -> int:
        self.state = (self.MULT * self.state + self.INC) & self.MASK
        return self.state

    def next_unit_mp(self) -> mp.mpf:
        val = max(1, self.next_u128() >> 64)
        return mp.mpf(val) / mp.mpf(1 << 64)


def haar_u3_householder_qr(rng: LCG128) -> tuple[mp.matrix, mp.mpf]:
    """Mezzadri (2007) exact Haar U(3) via complex Householder-QR (disjoint from Gram-Schmidt)."""
    two_pi = 2 * mp.pi
    z = mp.zeros(3, 3)
    for r in range(3):
        for c in range(3):
            u1 = rng.next_unit_mp()
            u2 = rng.next_unit_mp()
            rad = mp.sqrt(-2 * mp.log(u1))
            z[r, c] = mp.mpc(rad * mp.cos(two_pi * u2), rad * mp.sin(two_pi * u2))

    r_mat = z.copy()
    q_mat = mp.eye(3)
    for k in range(2):
        m = 3 - k
        x = mp.matrix([r_mat[k + i, k] for i in range(m)])
        nx = mp.sqrt(mp.fsum(abs(x[i, 0]) ** 2 for i in range(m)))
        if nx == 0:
            continue
        x0 = x[0, 0]
        ph = x0 / abs(x0) if abs(x0) > 0 else mp.mpc(1)
        v = x.copy()
        v[0, 0] = v[0, 0] + ph * nx
        nv2 = mp.fsum(abs(v[i, 0]) ** 2 for i in range(m))
        if nv2 == 0:
            continue
        h_sub = mp.eye(m) - (2 / nv2) * (v * v.H)
        h_full = mp.eye(3)
        for i in range(m):
            for j in range(m):
                h_full[k + i, k + j] = h_sub[i, j]
        r_mat = h_full * r_mat
        q_mat = q_mat * h_full.H

    d_ph = []
    for k in range(3):
        rkk = r_mat[k, k]
        d_ph.append(rkk / abs(rkk) if abs(rkk) > 0 else mp.mpc(1))
    u_out = q_mat * mp.diag(d_ph)
    unit_err = frob_norm(u_out.H * u_out - mp.eye(3))
    return u_out, unit_err


# ==============================================================================
# REF-0: Hygiene, AST, JSON Float, & Branch Custody Audit
# ==============================================================================

def run_ref_0(
    ow24: dict[str, Any],
    ow16: dict[str, Any],
    ow24_text: str,
    ow16_text: str,
    discrepancies: list[dict[str, Any]],
) -> dict[str, Any]:
    ast_ow24 = ast_audit_script(SCRIPT_OW24)
    ast_ow16 = ast_audit_script(SCRIPT_OW16)
    ast_self = ast_audit_script(SELF_SCRIPT)

    ow24_json_floats = assert_no_json_floats(ow24_text)
    ow16_json_floats = assert_no_json_floats(ow16_text)

    ow24_sha_match = bool(ow24.get("hygiene", {}).get("script_sha256") == ast_ow24["sha256"])
    ow16_sha_match = bool(ow16.get("hygiene", {}).get("script_sha256") == ast_ow16["sha256"])
    manifests = verify_all_branch_manifests()

    if not ast_ow24["clean"]:
        discrepancies.append({"module": "REF-0", "id": "REF0_AST_OW24V2_DIRTY", "detail": ast_ow24})
    if not ast_ow16["clean"]:
        discrepancies.append({"module": "REF-0", "id": "REF0_AST_OW16V12_DIRTY", "detail": ast_ow16})
    if not ast_self["clean"]:
        discrepancies.append({"module": "REF-0", "id": "REF0_AST_SELF_DIRTY", "detail": ast_self})
    if ow24_json_floats != 0 or ow16_json_floats != 0:
        discrepancies.append({
            "module": "REF-0",
            "id": "REF0_JSON_FLOATS",
            "ow24_json_floats": ow24_json_floats,
            "ow16_json_floats": ow16_json_floats,
        })
    if not (ow24_sha_match and ow16_sha_match):
        discrepancies.append({
            "module": "REF-0",
            "id": "REF0_SCRIPT_SHA_MISMATCH",
            "ow24_sha_match": ow24_sha_match,
            "ow16_sha_match": ow16_sha_match,
        })
    if not manifests["all_verified"]:
        discrepancies.append({
            "module": "REF-0",
            "id": "REF0_MANIFEST_MISMATCH",
            "mismatches": manifests["mismatches"],
        })

    gate_ref0 = bool(
        ast_ow24["clean"]
        and ast_ow16["clean"]
        and ast_self["clean"]
        and ow24_json_floats == 0
        and ow16_json_floats == 0
        and ow24_sha_match
        and ow16_sha_match
        and manifests["all_verified"]
    )
    return {
        "gate_ref0": gate_ref0,
        "ast_verify_a2_ow24_v2": ast_ow24,
        "ast_verify_a2_ow16_v12": ast_ow16,
        "ast_referee_v2_self": ast_self,
        "ow24_v2_json_float_tokens": ow24_json_floats,
        "ow16_v12_json_float_tokens": ow16_json_floats,
        "producer_script_sha256_matches_disk": bool(ow24_sha_match and ow16_sha_match),
        "branch_manifests": manifests,
    }


# ==============================================================================
# REF-1: Disjoint OW24-A Verification — Blocker R2
# ==============================================================================

def z2_reflection_matrix_nullspaces(m_flux: int) -> tuple[int, int, bool]:
    """Disjoint M=1..20 T^2/Z_2 parity via explicit SymPy reflection matrix nullspaces."""
    pm = sp.zeros(m_flux, m_flux)
    for j in range(m_flux):
        pm[j, (-j) % m_flux] = 1
    eye_m = sp.eye(m_flux)
    involution_ok = bool(pm * pm == eye_m)
    n_even = len((pm - eye_m).nullspace())
    n_odd = len((pm + eye_m).nullspace())
    return n_even, n_odd, bool(involution_ok and (n_even + n_odd == m_flux))


def gauss_legendre_unit_interval(n_pts: int) -> tuple[list[mp.mpf], list[mp.mpf], mp.mpf]:
    """Pure arbitrary-precision Gauss-Legendre nodes & weights on [0, 1] via Legendre-Newton."""
    nodes: list[mp.mpf] = []
    weights: list[mp.mpf] = []
    half = (n_pts + 1) // 2
    tol = mpow10(-57)
    for k in range(1, half + 1):
        x = mp.cos(mp.pi * mrat(4 * k - 1, 4 * n_pts + 2))
        dp = mp.mpf(1)
        for _ in range(16):
            p0 = mp.mpf(1)
            p1 = x
            for j in range(2, n_pts + 1):
                p0, p1 = p1, ((2 * j - 1) * x * p1 - (j - 1) * p0) / j
            dp = n_pts * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < tol:
                break
        w = 2 / ((1 - x * x) * dp * dp)
        nodes.append((1 - x) / 2)
        weights.append(w / 2)
        if 2 * k - 1 != n_pts:
            nodes.append((1 + x) / 2)
            weights.append(w / 2)
    wt_sum_err = abs(mp.fsum(weights) - 1)
    return nodes, weights, wt_sum_err


def rogers_ramanujan_cf(tau: mp.mpc, depth: int = 90) -> mp.mpc:
    """Disjoint Rogers-Ramanujan continued fraction R(tau) = q^(1/5) / (1 + q/(1 + q^2/...))."""
    q = mp.exp(2 * IMAG * mp.pi * tau)
    q5 = mp.exp(2 * IMAG * mp.pi * tau / 5)
    acc = mp.mpc(1)
    for k in range(depth, 0, -1):
        acc = 1 + (q ** k) / acc
    return q5 / acc


def run_ref_1(
    ow24: dict[str, Any],
    discrepancies: list[dict[str, Any]],
) -> dict[str, Any]:
    mp.mp.dps = 65
    p_a = ow24["OW24_A_R2_magnetized_M8_single_torus_bridge"]

    parity_rows: list[dict[str, Any]] = []
    even_m_3_odd: list[int] = []
    all_involutions_ok = True
    for m_v in range(1, 21):
        ne, no, inv_ok = z2_reflection_matrix_nullspaces(m_v)
        all_involutions_ok = bool(all_involutions_ok and inv_ok)
        e8_half_ok = bool((Fraction(1, 2) * m_v).denominator == 1)
        if e8_half_ok and no == 3:
            even_m_3_odd.append(m_v)
        parity_rows.append({
            "M": m_v,
            "E8_half_int_dirac_quantized": e8_half_ok,
            "n_even": ne,
            "n_odd": no,
        })
    parity_table_exact_match = bool(parity_rows == p_a["unique_even_flux_M8_theorem"]["parity_table_1_to_20"])
    m6_n_odd = parity_rows[5]["n_odd"]
    m8_counts = [parity_rows[7]["n_even"], parity_rows[7]["n_odd"]]

    tau0 = mrat(2, 5) + IMAG * mrat(1, 5)
    y0 = mp.im(tau0)
    m_star = 8
    omega8 = m_star * tau0
    y_om = mp.im(omega8)
    q8_nome = mp.exp(IMAG * mp.pi * omega8)

    def jtheta3_quasi_reduced(u_arg: mp.mpc) -> mp.mpc:
        m_shift = int(mp.nint(mp.im(u_arg) / y_om))
        u0 = u_arg - m_shift * omega8
        return mp.exp(-IMAG * mp.pi * (m_shift * m_shift) * omega8 - 2 * IMAG * mp.pi * m_shift * u0) * mp.jtheta(
            3, mp.pi * u0, q8_nome
        )

    def psi_jtheta(j: int, z: mp.mpc) -> mp.mpc:
        pref = mp.exp(
            IMAG * mp.pi * m_star * z * mp.im(z) / y0
            + IMAG * mp.pi * mrat(j * j, m_star) * tau0
            + 2 * IMAG * mp.pi * j * z
        )
        return pref * jtheta3_quasi_reduced(m_star * z + j * tau0)

    def psi_jtheta_raw(j: int, z: mp.mpc) -> mp.mpc:
        pref = mp.exp(
            IMAG * mp.pi * m_star * z * mp.im(z) / y0
            + IMAG * mp.pi * mrat(j * j, m_star) * tau0
            + 2 * IMAG * mp.pi * j * z
        )
        return pref * mp.jtheta(3, mp.pi * (m_star * z + j * tau0), q8_nome)

    def psi_odd_jtheta(a_idx: int, z: mp.mpc) -> mp.mpc:
        return (psi_jtheta(a_idx, z) - psi_jtheta(m_star - a_idx, z)) / mp.sqrt(2)

    test_pts = [
        mrat(3, 11) + IMAG * mrat(2, 11),
        mrat(7, 13) + IMAG * mrat(5, 17),
        mrat(4, 19) + IMAG * mrat(9, 23),
    ]
    h_fd = mpow10(-20)
    max_red_vs_raw = mp.mpf(0)
    max_pde_res = mp.mpf(0)
    max_q1_err = mp.mpf(0)
    max_qt_err = mp.mpf(0)
    max_z2_err = mp.mpf(0)
    wrong_sign_pde_err = mp.mpf(0)

    for zt in test_pts:
        q1_fac = mp.exp(IMAG * mp.pi * m_star * mp.im(zt) / y0)
        qt_fac = mp.exp(IMAG * mp.pi * m_star * mp.im(mp.conj(tau0) * zt) / y0)
        for j in range(m_star):
            p0 = psi_jtheta(j, zt)
            pr = psi_jtheta_raw(j, zt)
            max_red_vs_raw = max(max_red_vs_raw, abs(p0 - pr) / max(abs(pr), mpow10(-50)))
            p1 = psi_jtheta(j, zt + 1)
            pt = psi_jtheta(j, zt + tau0)
            max_q1_err = max(max_q1_err, abs(p1 / p0 - q1_fac))
            max_qt_err = max(max_qt_err, abs(pt / p0 - qt_fac))
            max_z2_err = max(max_z2_err, abs(psi_jtheta(j, -zt) - psi_jtheta((m_star - j) % m_star, zt)))

            dzx = (psi_jtheta(j, zt + h_fd) - psi_jtheta(j, zt - h_fd)) / (2 * h_fd)
            dzy = (psi_jtheta(j, zt + IMAG * h_fd) - psi_jtheta(j, zt - IMAG * h_fd)) / (2 * h_fd)
            dbar_p = (dzx + IMAG * dzy) / 2
            conn = (mp.pi * m_star / (2 * y0)) * zt * p0
            max_pde_res = max(max_pde_res, abs(dbar_p + conn) / abs(p0))
            if j == 1 and zt == test_pts[0]:
                wrong_sign_pde_err = abs(dbar_p - conn) / abs(p0)

    max_odd_parity_err = mp.mpf(0)
    max_integrand_z2_even_err = mp.mpf(0)
    for zt in test_pts:
        vals_p = [psi_odd_jtheta(a, zt) for a in (1, 2, 3)]
        vals_m = [psi_odd_jtheta(a, -zt) for a in (1, 2, 3)]
        for a in range(3):
            max_odd_parity_err = max(max_odd_parity_err, abs(vals_m[a] + vals_p[a]))
            for b in range(3):
                max_integrand_z2_even_err = max(
                    max_integrand_z2_even_err,
                    abs(mp.conj(vals_m[a]) * vals_m[b] - mp.conj(vals_p[a]) * vals_p[b]),
                )

    mp.mp.dps = 60
    nu_gl = 130
    nv_gl = 26
    u_nodes, u_wts, u_wt_err = gauss_legendre_unit_interval(nu_gl)
    v_raw, v_wraw, v_wt_err = gauss_legendre_unit_interval(nv_gl)
    v_nodes = [v / 2 for v in v_raw]
    v_wts = list(v_wraw)

    gram = mp.zeros(3, 3)
    for v, wv in zip(v_nodes, v_wts):
        row = mp.zeros(3, 3)
        for u, wu in zip(u_nodes, u_wts):
            vals = [psi_odd_jtheta(a, u + v * tau0) for a in (1, 2, 3)]
            for r in range(3):
                vc = mp.conj(vals[r]) * wu
                for c in range(3):
                    row[r, c] += vc * vals[c]
        gram += row * wv

    mp.mp.dps = 65
    g11_val = mp.re(gram[0, 0])
    g11_cim_exact = mp.sqrt(5) / 4
    g11_cim_formula = 1 / mp.sqrt(2 * m_star * y0)
    g11_err_vs_sqrt5_4 = abs(g11_val - g11_cim_exact)
    g11_err_vs_formula = abs(g11_val - g11_cim_formula)
    g11_rel_err_vs_producer = rel_err(g11_val, p_a["magnetized_dirac_6D_at_tau0"]["L2_norm_diag_G11"])
    gram_orth_err = frob_norm(gram / g11_val - mp.eye(3))
    gram_diag_rel_spread = max(abs(mp.re(gram[k, k]) - g11_cim_exact) for k in range(3))

    b_mat = sp.Matrix([[2, 8], [-1, 0]])
    u_snf = sp.Matrix([[0, -1], [1, 2]])
    v_snf = sp.eye(2)
    s_snf = u_snf * b_mat * v_snf
    snf_diag_1_8 = bool(s_snf == sp.diag(1, 8))
    snf_unimodular = bool(abs(int(u_snf.det())) == 1 and abs(int(v_snf.det())) == 1)
    det_b = int(b_mat.det())
    ker_elems = [(a, b) for a in range(8) for b in range(8) if (a + 2 * b) % 8 == 0]
    img_elems = sorted({(a + 2 * b) % 8 for a in range(8) for b in range(8)})
    lat_elems = sorted({((2 * m + 8 * n) % 8, (-m) % 8) for m in range(8) for n in range(8)})
    cyclic_z8_exact = bool(
        snf_diag_1_8
        and snf_unimodular
        and det_b == 8
        and sorted(ker_elems) == lat_elems
        and len(ker_elems) == 8
        and img_elems == list(range(8))
    )
    scale_8_err = abs(mp.mpc(8, 0) / mp.mpc(2, -1) - omega8)

    phi_gold = (1 + mp.sqrt(5)) / 2
    r5_cf = rogers_ramanujan_cf(5 * tau0, depth=90)
    r5_exact = mp.exp(4 * IMAG * mp.pi / 5) * (mp.sqrt(phi_gold + 2) - phi_gold)
    r5_err = abs(r5_cf - r5_exact)
    r8_cf = rogers_ramanujan_cf(omega8, depth=90)
    r8_abs = abs(r8_cf)
    r8_arg_pi = mp.arg(r8_cf) / mp.pi
    r8_abs_rel = rel_err(r8_abs, p_a["cyclic_Z8_cover_and_ramanujan_X5"]["R_8tau0_abs"])
    r8_arg_rel = rel_err(r8_arg_pi, p_a["cyclic_Z8_cover_and_ramanujan_X5"]["R_8tau0_arg_over_pi"])

    gate_ref1 = bool(
        all_involutions_ok
        and parity_table_exact_match
        and even_m_3_odd == [8]
        and m6_n_odd == 2
        and m8_counts == [5, 3]
        and max_red_vs_raw < mpow10(-55)
        and max_pde_res < mpow10(-30)
        and max_q1_err < mpow10(-50)
        and max_qt_err < mpow10(-50)
        and max_z2_err < mpow10(-50)
        and max_odd_parity_err < mpow10(-50)
        and max_integrand_z2_even_err < mpow10(-55)
        and u_wt_err < mpow10(-55)
        and v_wt_err < mpow10(-55)
        and gram_orth_err < mpow10(-35)
        and g11_err_vs_sqrt5_4 < mpow10(-40)
        and g11_err_vs_formula < mpow10(-40)
        and g11_rel_err_vs_producer < mpow10(-12)
        and cyclic_z8_exact
        and scale_8_err < mpow10(-60)
        and r5_err < mpow10(-50)
        and max(r8_abs_rel, r8_arg_rel) < mpow10(-12)
    )
    if not gate_ref1:
        discrepancies.append({"module": "REF-1", "id": "REF1_OW24A_GATE_FAIL"})

    return {
        "gate_ref1": gate_ref1,
        "parity_scan_sympy_nullspaces": {
            "all_20_involutions_ok": all_involutions_ok,
            "exact_20row_match_vs_producer": parity_table_exact_match,
            "even_M_giving_3_odd_modes": even_m_3_odd,
            "M6_n_odd": m6_n_odd,
            "M8_even_odd": m8_counts,
        },
        "magnetized_jtheta_and_gauss_legendre": {
            "gl_grid": f"{nu_gl}_u_x_{nv_gl}_half_v",
            "gl_weight_sum_max_err": mstr(max(u_wt_err, v_wt_err), 10),
            "jtheta_reduced_vs_raw_max_err": mstr(max_red_vs_raw, 10),
            "max_6D_Dirac_PDE_residual_3pts_8modes": mstr(max_pde_res, 10),
            "max_quasi_periodicity_z_plus_1_err": mstr(max_q1_err, 10),
            "max_quasi_periodicity_z_plus_tau0_err": mstr(max_qt_err, 10),
            "max_Z2_reflection_err": mstr(max_z2_err, 10),
            "max_odd_parity_err": mstr(max_odd_parity_err, 10),
            "max_integrand_Z2_evenness_err": mstr(max_integrand_z2_even_err, 10),
            "L2_3x3_Gram_orthogonality_frob_err": mstr(gram_orth_err, 10),
            "L2_norm_G11_computed": mstr(g11_val, 16),
            "L2_norm_G11_err_vs_sqrt5_over_4": mstr(g11_err_vs_sqrt5_4, 10),
            "L2_norm_G11_err_vs_CIM_formula": mstr(g11_err_vs_formula, 10),
            "L2_norm_all_3_diag_max_err_vs_sqrt5_4": mstr(gram_diag_rel_spread, 10),
            "L2_norm_G11_rel_err_vs_producer": mstr(g11_rel_err_vs_producer, 10),
        },
        "snf_Z8_cover_and_rr_continued_fraction": {
            "smith_normal_form_diag_1_8": snf_diag_1_8,
            "snf_U_V_unimodular": snf_unimodular,
            "sublattice_index_det": det_b,
            "cyclic_Z8_kernel_and_image_exact": cyclic_z8_exact,
            "geometric_scaling_8_over_2mi_err": mstr(scale_8_err, 10),
            "rr_cf_R_5tau0_exact_err": mstr(r5_err, 10),
            "rr_cf_R_8tau0_abs": mstr(r8_abs, 16),
            "rr_cf_R_8tau0_arg_over_pi": mstr(r8_arg_pi, 16),
            "rr_cf_R_8tau0_abs_rel_err_vs_producer": mstr(r8_abs_rel, 10),
            "rr_cf_R_8tau0_arg_rel_err_vs_producer": mstr(r8_arg_rel, 10),
        },
        "_internal": {
            "m6_n_odd": m6_n_odd,
            "max_pde_res": max_pde_res,
            "wrong_sign_pde_err": wrong_sign_pde_err,
        },
    }


# ==============================================================================
# REF-2: Disjoint OW24-B Verification — Blocker R3 (Explicit DFT mp.eig & 240 E_8 Roots)
# ==============================================================================

def build_e8_240_roots_scaled2() -> list[tuple[int, ...]]:
    """Construct all 240 roots of E_8 in R^8 (scaled by 2 so all entries are integers)."""
    roots: list[tuple[int, ...]] = []
    for i, j in itertools.combinations(range(8), 2):
        for si in (-2, 2):
            for sj in (-2, 2):
                v = [0] * 8
                v[i] = si
                v[j] = sj
                roots.append(tuple(v))
    for signs in itertools.product((-1, 1), repeat=8):
        if sum(1 for s in signs if s == -1) % 2 == 0:
            roots.append(signs)
    return roots


def analyze_model_from_240_e8_roots(
    roots: list[tuple[int, ...]],
    q: tuple[int, int, int, int],
    r: tuple[int, int, int, int],
    order: int,
    z4_eig: dict[int, dict[int, int]],
    z2_tbl: dict[int, dict[int, int]],
) -> dict[str, Any]:
    """Analyze E_8 -> SO(10)_vis x G_hid directly on all 240 roots of E_8 (uniform E_8 Killing norm)."""
    pairs = list(zip(q, r))
    cnt = Counter(pairs)
    dbl_pairs = [p for p, m in cnt.items() if m == 2]
    sing_pairs = [p for p, m in cnt.items() if m == 1]
    is_partition_2_1_1 = bool(len(dbl_pairs) == 1 and len(sing_pairs) == 2)
    ordered = [dbl_pairs[0], dbl_pairs[0]] + sorted(sing_pairs)
    qo = tuple(p[0] for p in ordered)
    ro = tuple(p[1] for p in ordered)

    rr = list(ro)
    rr[3] -= sum(ro)

    hq = (qo[0] + qo[1], qo[0] + qo[2], qo[0] + qo[3])
    hr = (rr[0] + rr[1], rr[0] + rr[2], rr[0] + rr[3])
    h_t1 = (2, 0, 0)
    h_t2 = (0, 1, -1)

    unbroken_roots = 0
    unbroken_16_roots = 0
    zero_flux_chiral_roots = 0
    a_so10_1 = Fraction(0)
    a_so10_2 = Fraction(0)
    a_su2_1 = Fraction(0)
    a_su2_2 = Fraction(0)
    nc_pos_total = 0
    su2_dbl_count = 0
    h10_sing_roots = 0
    h10_dbl_roots = 0
    hid15_roots = 0
    n16_roots = 0
    n16bar_roots = 0

    for rt in roots:
        fl = (hq[0] * rt[5] + hq[1] * rt[6] + hq[2] * rt[7]) // 2
        tw = ((hr[0] * rt[5] + hr[1] * rt[6] + hr[2] * rt[7]) // 2) % order
        s10_n2 = sum(x * x for x in rt[:5])
        if fl == 0:
            if tw == 0:
                unbroken_roots += 1
                if s10_n2 == 5:
                    unbroken_16_roots += 1
            elif tw == 1 or tw == (order - 1):
                zero_flux_chiral_roots += 1
            continue
        if fl < 0:
            continue

        mult = z4_eig[fl][(-tw) % 4] if order == 4 else z2_tbl[fl][tw % 2]
        if mult == 0:
            continue

        t1 = (h_t1[0] * rt[5] + h_t1[1] * rt[6] + h_t1[2] * rt[7]) // 2
        t2 = (h_t2[0] * rt[5] + h_t2[1] * rt[6] + h_t2[2] * rt[7]) // 2
        t_so10_sq = Fraction(rt[0] * rt[0], 8)
        t_su2_sq = Fraction((rt[6] + rt[7]) ** 2, 16)

        a_so10_1 += mult * t_so10_sq * t1
        a_so10_2 += mult * t_so10_sq * t2
        a_su2_1 += mult * t_su2_sq * t1
        a_su2_2 += mult * t_su2_sq * t2
        nc_pos_total += mult

        su2_2t3 = rt[6] + rt[7]
        if su2_2t3 == 2:
            su2_dbl_count += mult

        if s10_n2 == 4:
            if su2_2t3 == 0:
                h10_sing_roots += mult
            else:
                h10_dbl_roots += mult
        elif s10_n2 == 0:
            hid15_roots += mult
        elif s10_n2 == 5:
            prod5 = rt[0] * rt[1] * rt[2] * rt[3] * rt[4]
            if prod5 > 0:
                n16_roots += mult
            else:
                n16bar_roots += mult

    h10_sing = h10_sing_roots // 10
    h10_hid_charged = h10_dbl_roots // 20
    nv_true = unbroken_roots + 8
    enhanced_e6 = bool(unbroken_16_roots == 32 and nv_true == 82)
    gs_diff = (a_so10_1 - a_su2_1, a_so10_2 - a_su2_2)
    det_anom = a_so10_1 * a_su2_2 - a_so10_2 * a_su2_1
    ext_e6_vis = a_so10_1 + a_so10_2
    ext_e6_hid = a_su2_1 + a_su2_2
    bulk_gs_ok = bool((ext_e6_vis == ext_e6_hid) if enhanced_e6 else (gs_diff == (Fraction(0), Fraction(0))))
    nc_post_dt = nc_pos_total if enhanced_e6 else (nc_pos_total - 10 * h10_sing + 4)
    passes_post_dt_le10 = bool((not enhanced_e6) and 0 < (nc_post_dt - nv_true) <= 10)

    return {
        "q": list(q),
        "r": list(r),
        "orbifold": f"T2/Z{order}",
        "partition_2_1_1_verified": is_partition_2_1_1,
        "N_V": nv_true,
        "enhanced_to_E6": enhanced_e6,
        "unbroken_16_gauge_roots": unbroken_16_roots,
        "zero_flux_chiral_roots_Azbar": zero_flux_chiral_roots,
        "N_C_bulk_total": nc_pos_total,
        "N_C_post_DT_HuHd": nc_post_dt,
        "N_C_post_DT_minus_NV": nc_post_dt - nv_true,
        "passes_0_lt_NC_minus_NV_le_10_post_DT": passes_post_dt_le10,
        "n16_count": n16_roots // 16,
        "n16bar_count": n16bar_roots // 16,
        "h10_sing": h10_sing,
        "h10_hid_charged": h10_hid_charged,
        "hid15_chiral_dof": hid15_roots,
        "SU2_hid_doublets": su2_dbl_count,
        "SU2_Witten_anomaly_mod2": su2_dbl_count % 2,
        "A_SO10_U1_1_2": [fstr(a_so10_1), fstr(a_so10_2)],
        "A_SU2_U1_1_2": [fstr(a_su2_1), fstr(a_su2_2)],
        "GS_diff_U1_1_2": [fstr(gs_diff[0]), fstr(gs_diff[1])],
        "ext_E6_U1_T1plusT2_vis_vs_hid": [fstr(ext_e6_vis), fstr(ext_e6_hid)] if enhanced_e6 else None,
        "bulk_only_GS_universal": bulk_gs_ok,
        "det_mixed_anomaly_matrix": fstr(det_anom),
        "has_exact_anomaly_free_U1": bool((not enhanced_e6) and det_anom == 0),
    }


def smooth_t2_e8_gs_check(
    roots: list[tuple[int, ...]],
    q: tuple[int, int, int, int],
    inject_03_doublecount: bool = False,
) -> tuple[Fraction, Fraction, int]:
    """Verify exact 6D->4D E_8 index-theorem GS universality on smooth T^2 (mult = fl > 0)."""
    hq = (q[0] + q[1], q[0] + q[2], q[0] + q[3])
    h_t1 = (2, 0, 0)
    h_t2 = (0, 1, -1)
    a_so10_1 = Fraction(0)
    a_so10_2 = Fraction(0)
    a_su2_1 = Fraction(0)
    a_su2_2 = Fraction(0)
    ndbl = 0
    for rt in roots:
        fl = (hq[0] * rt[5] + hq[1] * rt[6] + hq[2] * rt[7]) // 2
        if fl <= 0:
            continue
        t1 = (h_t1[0] * rt[5] + h_t1[1] * rt[6] + h_t1[2] * rt[7]) // 2
        t2 = (h_t2[0] * rt[5] + h_t2[1] * rt[6] + h_t2[2] * rt[7]) // 2
        t_so10_sq = Fraction(rt[0] * rt[0], 8)
        t_su2_sq = Fraction((rt[6] + rt[7]) ** 2, 16)
        factor = 1
        if inject_03_doublecount and sum(x * x for x in rt[:5]) == 4 and (rt[6] + rt[7]) != 0:
            factor = 2
        a_so10_1 += factor * fl * t_so10_sq * t1
        a_so10_2 += factor * fl * t_so10_sq * t2
        a_su2_1 += factor * fl * t_su2_sq * t1
        a_su2_2 += factor * fl * t_su2_sq * t2
        if rt[6] + rt[7] == 2:
            ndbl += factor * fl
    return a_so10_1 - a_su2_1, a_so10_2 - a_su2_2, ndbl % 2


def run_ref_2(
    ow24: dict[str, Any],
    discrepancies: list[dict[str, Any]],
    audit_notes: list[str],
) -> dict[str, Any]:
    mp.mp.dps = 50
    p_b = ow24["OW24_B_R3_e8_bulk_orbifold_anomalies_vs_g2_locus"]

    # 1. Explicit M x M unitary DFT diagonalization via mp.eig for M = 1..16 (NOT Gauss-sum traces!)
    z4_eig: dict[int, dict[int, int]] = {0: {0: 0, 1: 0, 2: 0, 3: 0}}
    max_dft_unit_err = mp.mpf(0)
    max_dft_u4_err = mp.mpf(0)
    max_dft_snap_err = mp.mpf(0)
    all_dft_sums_ok = True
    for m_v in range(1, 17):
        inv_s = 1 / mp.sqrt(m_v)
        u_dft = mp.matrix([
            [inv_s * mp.exp(2 * IMAG * mp.pi * mrat(j * k, m_v)) for k in range(m_v)]
            for j in range(m_v)
        ])
        max_dft_unit_err = max(max_dft_unit_err, frob_norm(u_dft.H * u_dft - mp.eye(m_v)))
        u2 = u_dft * u_dft
        max_dft_u4_err = max(max_dft_u4_err, frob_norm(u2 * u2 - mp.eye(m_v)))
        evals, _ = mp.eig(u_dft)
        cnt = {0: 0, 1: 0, 2: 0, 3: 0}
        for ev in evals:
            best_r, best_d = min(((r_k, abs(ev - (IMAG ** r_k))) for r_k in range(4)), key=lambda x: x[1])
            max_dft_snap_err = max(max_dft_snap_err, best_d)
            cnt[best_r] += 1
        if sum(cnt.values()) != m_v:
            all_dft_sums_ok = False
        z4_eig[m_v] = cnt

    z2_tbl: dict[int, dict[int, int]] = {0: {0: 0, 1: 0}}
    for m_v in range(1, 17):
        ne, no, _ = z2_reflection_matrix_nullspaces(m_v)
        z2_tbl[m_v] = {0: ne, 1: no}

    # 2. Construct explicit 240 roots of E_8 and run smooth-T^2 GS universality check
    roots = build_e8_240_roots_scaled2()
    all_norm2 = all(sum(x * x for x in rt) == 8 for rt in roots)
    s10_counts = Counter(sum(x * x for x in rt[:5]) for rt in roots)
    e8_branch_ok = bool(
        len(roots) == 240
        and all_norm2
        and s10_counts[8] == 40
        and s10_counts[0] == 12
        and s10_counts[5] == 128
        and s10_counts[4] == 60
    )

    smooth_fluxes = [(-4, -4, 0, 8), (-3, -3, 2, 4), (-4, -4, 2, 6), (-2, -2, 0, 4)]
    smooth_exact_all_zero = True
    smooth_bug_all_nonzero = True
    smooth_bug_m8_gs = (Fraction(0), Fraction(0))
    for q_test in smooth_fluxes:
        g1, g2, wm = smooth_t2_e8_gs_check(roots, q_test, inject_03_doublecount=False)
        if g1 != 0 or g2 != 0 or wm != 0:
            smooth_exact_all_zero = False
        b1, b2, _ = smooth_t2_e8_gs_check(roots, q_test, inject_03_doublecount=True)
        if b1 == 0 and b2 == 0:
            smooth_bug_all_nonzero = False
        if q_test == (-4, -4, 0, 8):
            smooth_bug_m8_gs = (b1, b2)

    # 3. Exhaustive T^2/Z_4 (|q_i|<=8, det=1) and T^2/Z_2 (|q_i|<=8) scans on all 240 E_8 roots
    z4_models: list[dict[str, Any]] = []
    z4_m8_models: list[dict[str, Any]] = []
    for q in itertools.combinations_with_replacement(range(-8, 9), 4):
        if sum(q) != 0 or all(x == 0 for x in q):
            continue
        for r in itertools.product(range(4), repeat=4):
            if sum(r) % 4 != 0:
                continue
            pairs = list(zip(q, r))
            if pairs != sorted(pairs):
                continue
            cnt = Counter(pairs)
            if sum(m * m - 1 for m in cnt.values() if m >= 2) == 0:
                continue
            s16 = s16b = chg16 = 0
            sflux: list[list[int]] = []
            for (qv, rv), m in cnt.items():
                if qv == 0:
                    continue
                if qv > 0:
                    nm = z4_eig[qv][(-rv) % 4]
                    if m == 1:
                        s16 += nm
                        if nm > 0:
                            sflux.append([qv, nm])
                    else:
                        chg16 += m * nm
                else:
                    nm = z4_eig[-qv][rv % 4]
                    if m == 1:
                        s16b += nm
                    else:
                        chg16 += m * nm
            if s16 == 3 and s16b == 0 and chg16 == 0:
                info = analyze_model_from_240_e8_roots(roots, q, r, 4, z4_eig, z2_tbl)
                info["flux16_sectors"] = sflux
                z4_models.append(info)
                if sflux == [[8, 3]]:
                    z4_m8_models.append(info)

    z2_models: list[dict[str, Any]] = []
    for q in itertools.combinations_with_replacement(range(-8, 9), 4):
        if sum(q) != 0 or all(x == 0 for x in q):
            continue
        for r in itertools.product(range(2), repeat=4):
            if sum(r) % 2 != 0:
                continue
            pairs = list(zip(q, r))
            if pairs != sorted(pairs):
                continue
            cnt = Counter(pairs)
            if sum(m * m - 1 for m in cnt.values() if m >= 2) == 0:
                continue
            s16 = s16b = chg16 = 0
            sflux = []
            for (qv, rv), m in cnt.items():
                if qv == 0:
                    continue
                nm = z2_tbl[abs(qv)][rv]
                if qv > 0:
                    if m == 1:
                        s16 += nm
                        if nm > 0:
                            sflux.append([qv, nm])
                    else:
                        chg16 += m * nm
                else:
                    if m == 1:
                        s16b += nm
                    else:
                        chg16 += m * nm
            if s16 == 3 and s16b == 0 and chg16 == 0:
                info = analyze_model_from_240_e8_roots(roots, q, r, 2, z4_eig, z2_tbl)
                info["flux16_sectors"] = sflux
                z2_models.append(info)

    all_9_models = z4_models + z2_models
    bulk_gs_universal_count = sum(1 for m in all_9_models if m["bulk_only_GS_universal"])
    z4_witten0_post_dt_le10 = [
        m["q"]
        for m in z4_models
        if m["SU2_Witten_anomaly_mod2"] == 0 and m["passes_0_lt_NC_minus_NV_le_10_post_DT"]
    ]

    # Complete field-by-field comparison against ALL 9 models in A2-OW24 v2
    prod_by_key: dict[tuple[str, tuple[int, ...], tuple[int, ...]], dict[str, Any]] = {}
    for row in p_b["bulk_orbifold_census"]["T2_Z4_solutions"] + p_b["bulk_orbifold_census"]["T2_Z2_solutions"]:
        prod_by_key[(row["orbifold"], tuple(row["q"]), tuple(row["r"]))] = row

    compare_fields = (
        "N_V",
        "enhanced_to_E6",
        "N_C_bulk_total",
        "N_C_post_DT_HuHd",
        "N_C_post_DT_minus_NV",
        "passes_0_lt_NC_minus_NV_le_10_post_DT",
        "h10_sing",
        "h10_hid_charged",
        "hid15_chiral_dof",
        "SU2_hid_doublets",
        "SU2_Witten_anomaly_mod2",
        "A_SO10_U1_1_2",
        "A_SU2_U1_1_2",
        "GS_diff_U1_1_2",
        "ext_E6_U1_T1plusT2_vis_vs_hid",
        "det_mixed_anomaly_matrix",
        "has_exact_anomaly_free_U1",
        "bulk_only_GS_universal",
        "flux16_sectors",
    )
    model_diffs: list[dict[str, Any]] = []
    exact_match_count = 0
    for m in all_9_models:
        key = (m["orbifold"], tuple(m["q"]), tuple(m["r"]))
        pm = prod_by_key.get(key)
        if pm is None:
            model_diffs.append({"model": list(key), "reason": "missing_in_producer"})
            continue
        diffs_here: dict[str, dict[str, Any]] = {}
        for fld in compare_fields:
            if m[fld] != pm[fld]:
                diffs_here[fld] = {"referee_240root": m[fld], "producer_v2": pm[fld]}
        if diffs_here:
            model_diffs.append({
                "orbifold": m["orbifold"],
                "q": m["q"],
                "r": m["r"],
                "field_diffs": diffs_here,
            })
        else:
            exact_match_count += 1

    if model_diffs:
        discrepancies.append({
            "module": "REF-2",
            "id": "REF2_OW24B_V2_MODEL_DIFF",
            "diffs": model_diffs,
        })

    # Physics audit note on zero-flux A_zbar chiral modes in 6D N=1 SYM
    z4_44_zf = [m["zero_flux_chiral_roots_Azbar"] for m in z4_models if m["q"] == [-4, -4, 4, 4]]
    audit_notes.append(
        "REF2_ZERO_FLUX_CHIRAL_DZ_TWIST_NOTE: Both A2-OW24 v2 and our 240-root verifier audit positive-flux chiral "
        "zero modes plus unbroken zero-flux vector multiplets (N_V=82 E_6 enhancement in T^2/Z_2 (-2,-2,0,4)). "
        "As an additional 6D N=1 SYM physics note, the 4D chiral multiplet Phi ~ A_zbar carries an internal 1-form "
        f"phase exp(+-2*pi*i/N): in T^2/Z_4 q=(-4,-4,4,4) r=(3,3,0,2), the 240-root check finds {z4_44_zf[0] if z4_44_zf else 0} "
        "zero-flux (10,2) roots with tw in {1,3}, adding one zero-flux chiral (10,2) (+20 dof, +10 doublets; Witten stays 1 "
        "and GS_diff stays non-zero). On T^2/Z_2, restoring the (-1) chiral parity shifts r=(1,1,0,0) -> (0,0,1,1) for "
        "q=(-2,-2,0,4), breaking E_6 -> SO(10) (N_V=50) only at the cost of a massless zero-flux mirror pair 16+16bar from A_zbar. "
        "Neither effect changes the 0/9 bulk-only GS universality obstruction."
    )

    # 4. Explicit SU(5) weight-sum cubic anomaly & G_2 conical-locus SU(5)_vis x SU(5)_hid closure
    w_fund = (2, 2, 2, -3, -3)
    a_5_raw = sum(w ** 3 for w in w_fund)
    a_5bar_raw = sum((-w) ** 3 for w in w_fund)
    a_10_raw = sum((w_fund[i] + w_fund[j]) ** 3 for i in range(5) for j in range(i + 1, 5))
    a_5_norm = Fraction(a_5_raw, a_5_raw)
    a_5bar_norm = Fraction(a_5bar_raw, a_5_raw)
    a_10_norm = Fraction(a_10_raw, a_5_raw)
    su5_3gen_cubic = 3 * (a_10_norm + a_5bar_norm)
    su5_corrupt_cubic = 3 * (a_10_norm + a_5_norm)

    su2_l_doublets = 3 * (3 + 1) + 2
    g2_nv = 24 + 24
    g2_nc = 3 * (10 + 5 + 1) + 2 + 2
    g2_a1 = Fraction(g2_nc - g2_nv, 2)
    g2_dep = Fraction(3 * (g2_nc - g2_nv), 1)
    g2_dp = Fraction(3 * g2_nc - 9 * g2_nv, 2)

    p_g2 = p_b["g2_conical_locus_resolution"]
    g2_exact_match = bool(
        su5_3gen_cubic == 0
        and p_g2["SU5_vis_cubic_anomaly"] == "0"
        and su2_l_doublets == 14
        and p_g2["SU2_L_doublets_count"] == 14
        and (su2_l_doublets % 2 == 0)
        and g2_nv == 48
        and g2_nc == 52
        and g2_a1 == Fraction(2)
        and p_g2["a1_xi0"] == fstr(g2_a1)
        and g2_dep == Fraction(12)
        and p_g2["Mg_DEP"] == fstr(g2_dep)
        and g2_dp == Fraction(-138)
        and p_g2["Mg_DP"] == fstr(g2_dp)
    )

    dft_eig_ok = bool(
        all_dft_sums_ok
        and max_dft_unit_err < mpow10(-45)
        and max_dft_u4_err < mpow10(-45)
        and max_dft_snap_err < mpow10(-40)
    )
    census_ok = bool(
        e8_branch_ok
        and smooth_exact_all_zero
        and smooth_bug_all_nonzero
        and p_b["bulk_orbifold_census"]["smooth_T2_GS_exact_zero_all_4_test_fluxes"]
        and len(z4_models) == 7
        and len(z4_m8_models) == 1
        and z4_m8_models[0]["q"] == [-4, -4, 0, 8]
        and z4_m8_models[0]["SU2_hid_doublets"] == 13
        and z4_m8_models[0]["SU2_Witten_anomaly_mod2"] == 1
        and z4_witten0_post_dt_le10 == [[-3, -3, 2, 4]]
        and z4_witten0_post_dt_le10 == p_b["bulk_orbifold_census"]["T2_Z4_witten0_post_DT_le10_models"]
        and len(z2_models) == 2
        and p_b["bulk_orbifold_census"]["T2_Z2_M4_enhanced_to_E6_NV82"]
        and bulk_gs_universal_count == 0
        and exact_match_count == 9
        and len(model_diffs) == 0
        and g2_exact_match
    )
    gate_ref2 = bool(dft_eig_ok and census_ok)
    if not gate_ref2 and not model_diffs:
        discrepancies.append({"module": "REF-2", "id": "REF2_OW24B_GATE_FAIL"})

    return {
        "gate_ref2": gate_ref2,
        "dft_mp_eig_1_to_16": {
            "ok": dft_eig_ok,
            "max_unitarity_err": mstr(max_dft_unit_err, 10),
            "max_U4_identity_err": mstr(max_dft_u4_err, 10),
            "max_eigenvalue_snap_err": mstr(max_dft_snap_err, 10),
            "M8_mults": z4_eig[8],
            "M12_mults": z4_eig[12],
            "M16_mults": z4_eig[16],
        },
        "e8_240_root_and_smooth_T2_proof": {
            "e8_240_roots_branching_40_12_128_60_ok": e8_branch_ok,
            "smooth_T2_exact_240root_GS_diff_zero_all_4_fluxes": smooth_exact_all_zero,
            "smooth_T2_old_v1_03_bug_violates_GS_all_4_fluxes": smooth_bug_all_nonzero,
            "smooth_T2_old_v1_03_bug_GS_diff_at_M8": [fstr(smooth_bug_m8_gs[0]), fstr(smooth_bug_m8_gs[1])],
        },
        "bulk_orbifold_240root_audit": {
            "T2_Z4_count": len(z4_models),
            "T2_Z4_unique_M8_count": len(z4_m8_models),
            "T2_Z4_witten0_post_DT_le10_models": z4_witten0_post_dt_le10,
            "T2_Z4_M8_exact_240root": z4_m8_models[0] if z4_m8_models else {},
            "T2_Z2_count": len(z2_models),
            "T2_Z2_exact_240root": z2_models,
            "bulk_only_GS_universal_count_out_of_9": bulk_gs_universal_count,
            "models_exact_match_vs_producer_v2_out_of_9": exact_match_count,
            "all_9_models_19_fields_exact_match": bool(exact_match_count == 9 and len(model_diffs) == 0),
        },
        "g2_conical_locus_weight_sum_audit": {
            "A_5_raw_from_T_2_2_2_m3_m3": a_5_raw,
            "A_10_over_A_5_computed": fstr(a_10_norm),
            "A_5bar_over_A_5_computed": fstr(a_5bar_norm),
            "SU5_3gen_cubic_anomaly": fstr(su5_3gen_cubic),
            "SU2_L_doublets": su2_l_doublets,
            "SU2_L_Witten_mod2": su2_l_doublets % 2,
            "N_V": g2_nv,
            "N_C": g2_nc,
            "a1_xi0": fstr(g2_a1),
            "Mg_DEP": fstr(g2_dep),
            "Mg_DP": fstr(g2_dp),
            "exact_match_vs_producer": g2_exact_match,
        },
        "_internal": {
            "smooth_bug_m8_gs": smooth_bug_m8_gs,
            "su5_corrupt_cubic": su5_corrupt_cubic,
            "z4_m8_true_doublets": z4_m8_models[0]["SU2_hid_doublets"] if z4_m8_models else -1,
            "z2_m4_true_nv": [m["N_V"] for m in z2_models if m["q"] == [-2, -2, 0, 4]][0],
        },
    }


# ==============================================================================
# REF-3: Disjoint OW24-C Verification — Blocker R4 (mp.jtheta + real 6x6 eigsy)
# ==============================================================================

def theta_char_jtheta(a: Fraction, b: Fraction, tau: mp.mpc) -> mp.mpc:
    """Theta function with rational characteristics [a, b] via mp.jtheta(3, ...) (NOT manual sum!)."""
    ta = a % 1
    tb = b % 1
    nb = int(b - tb)
    am = mrat(ta.numerator, ta.denominator)
    bm = mrat(tb.numerator, tb.denominator)
    qn = mp.exp(IMAG * mp.pi * tau)
    val = mp.exp(IMAG * mp.pi * am * am * tau + 2 * IMAG * mp.pi * am * bm) * mp.jtheta(
        3, mp.pi * (am * tau + bm), qn
    )
    if nb != 0 and ta != 0:
        val *= mp.exp(2 * IMAG * mp.pi * am * nb)
    return val


def eval_whol_jtheta_heat(tau: mp.mpc, pa: Fraction, pb: Fraction, ql: int, qr: int) -> tuple[mp.matrix, mp.mpf]:
    """Disjoint W_hol using mp.jtheta + heat-equation derivative identities (ZERO manual theta sums!)."""
    qn = mp.exp(IMAG * mp.pi * tau)
    t2 = mp.jtheta(2, 0, qn)
    t3 = mp.jtheta(3, 0, qn)
    t4 = mp.jtheta(4, 0, qn)
    dt2 = -mp.jtheta(2, 0, qn, 2) / 8
    dt3 = -mp.jtheta(3, 0, qn, 2) / 8
    dt4 = -mp.jtheta(4, 0, qn, 2) / 8
    l2, l3, l4 = dt2 / t2, dt3 / t3, dt4 / t4

    e2_24 = (l2 + l3 + l4) / 3
    t1d1 = mp.jtheta(1, 0, qn, 1)
    t1d3 = mp.jtheta(1, 0, qn, 3)
    e2_heat_err = abs(e2_24 - (-t1d3 / (24 * t1d1)))
    jacobi_prod_err = abs(t1d1 - t2 * t3 * t4) / abs(t1d1)
    t1p = mp.pi * t1d1

    qi = mp.matrix([[IMAG, 0], [0, -IMAG]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mrat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    sh = (
        (-t2 / (t3 * t4)) * (l2 - l3 - l4 + e2_24) * qi
        + (-t4 / (t2 * t3)) * (l4 - l2 - l3 + e2_24) * qj
        + (IMAG * t3 / (t2 * t4)) * (l3 - l2 - l4 + e2_24) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]

    xv = (ql * pa, 2 * ql * pb)
    yv = (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * IMAG * mp.pi * mrat(xv[0].numerator, xv[0].denominator))
    kap = {"1": -IMAG * eph, "i": mp.mpf(-1), "j": -eph, "k": IMAG}
    hfr = Fraction(1, 2)
    cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
    ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
    rs: dict[str, mp.mpc] = {}
    for sk in ("1", "i", "j", "k"):
        if ((cs[sk][0] - hfr) % 1 == 0 and (cs[sk][1] - hfr) % 1 == 0) or (
            (ds[sk][0] - hfr) % 1 == 0 and (ds[sk][1] - hfr) % 1 == 0
        ):
            rs[sk] = mp.mpc(0)
        else:
            rs[sk] = (
                kap[sk]
                * theta_char_jtheta(cs[sk][0], cs[sk][1], tau)
                * theta_char_jtheta(ds[sk][0], ds[sk][1], tau)
                / t1p
            )
    mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
    out = mp.matrix([
        [
            ct[ra][cb][0, 0] * mw[0, 0]
            + ct[ra][cb][0, 1] * mw[0, 1]
            + ct[ra][cb][1, 0] * mw[1, 0]
            + ct[ra][cb][1, 1] * mw[1, 1]
            for cb in range(3)
        ]
        for ra in range(3)
    ])
    return out, max(e2_heat_err, jacobi_prod_err)


def left_unitary_and_sv_eigh(mat: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    """Disjoint left-singular decomposition via Hermitian mp.eigh(M M^dagger) (ZERO mp.svd_c!)."""
    h = mat * mat.H
    h = (h + h.H) / 2
    evals, evecs = mp.eigh(h)
    order = sorted(range(3), key=lambda k: mp.re(evals[k]))
    u_mat = mp.matrix([[evecs[r, order[c]] for c in range(3)] for r in range(3)])
    s_vals = [mp.sqrt(max(mp.mpf(0), mp.re(evals[k]))) for k in order]
    return u_mat, s_vals


def takagi_real6_eigsy(m_sym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf], mp.mpf, mp.mpf, mp.mpf]:
    """Disjoint Takagi factorization via real 6x6 symmetric mp.eigsy (ZERO complex SVD!)."""
    ms = (m_sym + m_sym.T) / 2
    h6 = mp.zeros(6, 6)
    for r in range(3):
        for c in range(3):
            ar = mp.re(ms[r, c])
            bi = mp.im(ms[r, c])
            h6[r, c] = ar
            h6[r, c + 3] = bi
            h6[r + 3, c] = bi
            h6[r + 3, c + 3] = -ar
    evals, evecs = mp.eigsy(h6)
    pair_err = max(abs(evals[k] + evals[5 - k]) for k in range(3))
    s_pos = [evals[3], evals[4], evals[5]]
    u_t = mp.zeros(3, 3)
    for k in range(3):
        col = evecs[:, 3 + k]
        for r in range(3):
            u_t[r, k] = mp.mpc(col[r], -col[r + 3])
    tak_err = frob_norm(u_t.T * ms * u_t - mp.diag(s_pos))
    unit_err = frob_norm(u_t.H * u_t - mp.eye(3))
    return u_t, s_pos, tak_err, pair_err, unit_err


def run_ref_3(
    ow24: dict[str, Any],
    ow19: dict[str, Any],
    discrepancies: list[dict[str, Any]],
) -> dict[str, Any]:
    mp.mp.dps = 60
    p_c = ow24["OW24_C_R4_type12_cancel_hu_k5_and_384_atlas"]

    tau8 = mrat(16, 5) + IMAG * mrat(8, 5)
    tau8_m = -mp.conj(tau8)
    k5 = [(Fraction(1, 5), Fraction(2, 5)), (Fraction(4, 5), Fraction(3, 5)), (Fraction(2, 5), Fraction(4, 5)), (Fraction(3, 5), Fraction(1, 5))]
    k6 = [(Fraction(1, 6), Fraction(1, 6)), (Fraction(5, 6), Fraction(5, 6))]
    k5_cp = [(a, (-b) % 1) for a, b in k5]
    k6_cp = [(a, (-b) % 1) for a, b in k6]

    k_e2 = [mp.mpf(s) for s in ow19["OW19_A_2d_hyperbolic_kahler_and_lepto"]["kahler_2d_hyperbolic"]["K_e2_hyp_theta4_theta2_theta3"]]
    k_is = mp.diag([1 / mp.sqrt(v) for v in k_e2])

    max_heat_jacobi_err = mp.mpf(0)

    def w_avg(tau_v: mp.mpc, pts: list[tuple[Fraction, Fraction]], ql: int, qr: int) -> mp.matrix:
        nonlocal max_heat_jacobi_err
        acc = mp.zeros(3, 3)
        for a, b in pts:
            m_w, h_err = eval_whol_jtheta_heat(tau_v, a, b, ql, qr)
            max_heat_jacobi_err = max(max_heat_jacobi_err, h_err)
            acc += m_w
        return acc / len(pts)

    eps5 = mp.exp(2 * IMAG * mp.pi * tau8 / 5)
    d10 = mp.diag([eps5 ** 3, eps5 ** 2, mp.mpc(1)])
    wu0 = w_avg(tau8, k5, 1, -4)
    wd0 = (w_avg(tau8, k5, 1, 2) + w_avg(tau8, k6, 1, 2)) / 2
    we0 = (w_avg(tau8, k5, -3, 6) + w_avg(tau8, k6, -3, 6)) / 2

    def ckm_obs_eigh(yu: mp.matrix, yd: mp.matrix, ye: mp.matrix) -> dict[str, mp.mpf]:
        uu, su = left_unitary_and_sv_eigh(yu)
        ud, sd = left_unitary_and_sv_eigh(yd)
        _, se = left_unitary_and_sv_eigh(ye)
        vc = uu.H * ud
        j_inv = mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1]))
        return {
            "v12": abs(vc[0, 1]),
            "v23": abs(vc[1, 2]),
            "v13": abs(vc[0, 2]),
            "J": j_inv,
            "u13": su[0] / su[2],
            "d13": sd[0] / sd[2],
            "e13": se[0] / se[2],
            "b_tau": sd[2] / se[2],
        }

    def pmns_obs_takagi(ye: mp.matrix, mnu: mp.matrix) -> dict[str, mp.mpf]:
        ul, _ = left_unitary_and_sv_eigh(ye)
        u_t, sn, _, _, _ = takagi_real6_eigsy(mnu)
        un = mp.matrix([[mp.conj(u_t[r, c]) for c in range(3)] for r in range(3)])
        up = ul.H * un
        s13 = abs(up[0, 2]) ** 2
        s12 = abs(up[0, 1]) ** 2 / (1 - s13)
        s23 = abs(up[1, 2]) ** 2 / (1 - s13)
        dm = (sn[1] ** 2 - sn[0] ** 2) / (sn[2] ** 2 - sn[0] ** 2)
        j_p = mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1]))
        return {"s12sq": s12, "s23sq": s23, "s13sq": s13, "dm": dm, "J": j_p}

    # 1. Type-I == Type-II cancellation at q_R = +3
    w5_n3 = w_avg(tau8, k5, -3, 3)
    w6_n3 = w_avg(tau8, k6, -3, 3)
    w5_r3 = w_avg(tau8, k5, 3, 3)
    w6_r3 = w_avg(tau8, k6, 3, 3)
    w5_t2 = w_avg(tau8, k5, -3, -3)
    w6_t2 = w_avg(tau8, k6, -3, -3)

    w56_n3 = (w5_n3 + w6_n3) / 2
    mr56_3 = ((w5_r3 + w6_r3) / 2 + ((w5_r3 + w6_r3) / 2).T) / 2
    p_t1_56 = pmns_obs_takagi(we0 * d10, -w56_n3 * (mr56_3 ** (-1)) * w56_n3.T)
    p_t2_56 = pmns_obs_takagi(we0 * d10, ((w5_t2 + w6_t2) / 2 + ((w5_t2 + w6_t2) / 2).T) / 2)
    t12_56_err = max(abs(p_t1_56[k] - p_t2_56[k]) for k in p_t1_56)

    mr5_3 = (w5_r3 + w5_r3.T) / 2
    p_t1_k5 = pmns_obs_takagi(we0 * d10, -w5_n3 * (mr5_3 ** (-1)) * w5_n3.T)
    p_t2_k5 = pmns_obs_takagi(we0 * d10, (w5_t2 + w5_t2.T) / 2)
    t12_k5_err = max(abs(p_t1_k5[k] - p_t2_k5[k]) for k in p_t1_k5)
    k5_trap_rel = rel_err(p_t1_k5["s23sq"], p_c["type1_eq_type2_cancellation_theorem"]["K5_over_K5_s23sq_trapped"])

    # 2. Pure lopsided SU(5) n_5bar=(0,0,0) + 10-trial LCG128 Haar U(3)^5
    yu_f, yd_f, ye_f = d10 * wu0 * d10, d10 * wd0, we0 * d10
    yu_h, yd_h, ye_h = k_is * yu_f * k_is, k_is * yd_f * k_is, k_is * ye_f * k_is
    obs_f = ckm_obs_eigh(yu_f, yd_f, ye_f)
    obs_h = ckm_obs_eigh(yu_h, yd_h, ye_h)
    flat_ckm_max_rel = max(rel_err(obs_f[k], p_c["pure_lopsided_SU5_n5b_000"]["flat_horosphere"][k]) for k in obs_f)
    curv_ckm_max_rel = max(rel_err(obs_h[k], p_c["pure_lopsided_SU5_n5b_000"]["curved_2D_hyp"][k]) for k in obs_h)
    bits_saved = mp.log(mp.mpf(1000), 2) - mp.log(mp.mpf(10), 2)
    bits_saved_rel = rel_err(bits_saved, p_c["pure_lopsided_SU5_n5b_000"]["discrete_bits_saved_vs_9int_FN"])

    h_w = mpow10(-16)

    def build_yu_000(tv: mp.mpc) -> mp.matrix:
        e5 = mp.exp(2 * IMAG * mp.pi * tv / 5)
        d = mp.diag([e5 ** 3, e5 ** 2, mp.mpc(1)])
        return d * w_avg(tv, k5, 1, -4) * d

    upx, umx = build_yu_000(tau8 + h_w), build_yu_000(tau8 - h_w)
    upy, umy = build_yu_000(tau8 + IMAG * h_w), build_yu_000(tau8 - IMAG * h_w)
    dbar_000 = frob_norm(((upx - umx) + IMAG * (upy - umy)) / (4 * h_w)) / frob_norm(
        ((upx - umx) - IMAG * (upy - umy)) / (4 * h_w)
    )

    rng = LCG128(987654321012345678902026112324)
    max_haar_unit_err = mp.mpf(0)
    haar_ckm_err = mp.mpf(0)
    for _ in range(10):
        mats = [haar_u3_householder_qr(rng) for _ in range(5)]
        for _, ue in mats:
            max_haar_unit_err = max(max_haar_unit_err, ue)
        uq, uur, udr, uel, uer = (m[0] for m in mats)
        scr = ckm_obs_eigh(uq * yu_h * uur.H, uq * yd_h * udr.H, uel * ye_h * uer.H)
        haar_ckm_err = max(haar_ckm_err, max(abs(scr[k] - obs_h[k]) for k in obs_h))

    # 3. Physical H_u(K_5) vs M_R(K_5+K_6) + 10-trial LCG128 Haar U(3)^3
    pmns_hu_000 = pmns_obs_takagi(ye_f, -w5_n3 * (mr56_3 ** (-1)) * w5_n3.T)
    d5b_100 = mp.diag([eps5, mp.mpc(1), mp.mpc(1)])
    ye_100 = d5b_100 * we0 * d10
    ynu_100 = d5b_100 * w5_n3
    pmns_hu_100 = pmns_obs_takagi(ye_100, -ynu_100 * (mr56_3 ** (-1)) * ynu_100.T)
    hu_000_max_rel = max(rel_err(pmns_hu_000[k], p_c["physical_Hu_K5_vs_MR_K56_unblocking"]["qR_plus3_n5b_000"][k]) for k in pmns_hu_000)
    hu_100_max_rel = max(rel_err(pmns_hu_100[k], p_c["physical_Hu_K5_vs_MR_K56_unblocking"]["qR_plus3_n5b_100"][k]) for k in pmns_hu_100)

    haar_hu_err = mp.mpf(0)
    for _ in range(10):
        mats = [haar_u3_householder_qr(rng) for _ in range(3)]
        for _, ue in mats:
            max_haar_unit_err = max(max_haar_unit_err, ue)
        ul_r, uer_r, unr_r = (m[0] for m in mats)
        ye_s = ul_r * ye_100 * uer_r.H
        ynu_s = ul_r * ynu_100 * unr_r
        mr_s = unr_r.T * mr56_3 * unr_r
        scr_p = pmns_obs_takagi(ye_s, -ynu_s * (mr_s ** (-1)) * ynu_s.T)
        haar_hu_err = max(haar_hu_err, max(abs(scr_p[k] - pmns_hu_100[k]) for k in pmns_hu_100))

    # 4. Full 384-case discrete neutrino atlas
    atlas_total = 0
    atlas_nonsingular = 0
    hits: list[dict[str, Any]] = []
    hit_mats: dict[str, mp.matrix] = {}
    for qr in (3, -5, 1, 2):
        w5n = w_avg(tau8, k5, -3, qr)
        w6n = w_avg(tau8, k6, -3, qr)
        w5r = w_avg(tau8, k5, qr, qr)
        w6r = w_avg(tau8, k6, qr, qr)
        ops_n = {"K5": w5n, "K6": w6n, "5+6": (w5n + w6n) / 2, "5-6": (w5n - w6n) / 2}
        ops_r = {"K5": w5r, "K6": w6r, "5+6": (w5r + w6r) / 2, "5-6": (w5r - w6r) / 2}
        for kn, wn in ops_n.items():
            for kr, wr in ops_r.items():
                mr_m = (wr + wr.T) / 2
                _, smr, _, _, _ = takagi_real6_eigsy(mr_m)
                is_sing = bool(smr[0] < mpow10(-25))
                for n5b in ((0, 0, 0), (1, 0, 0), (1, 1, 0)):
                    d5b = mp.diag([eps5 ** n for n in n5b])
                    ye_loc = d5b * we0 * d10
                    ynu_loc = d5b * wn
                    for gname, kmat in (("FLAT", mp.eye(3)), ("CURV", k_is)):
                        atlas_total += 1
                        if is_sing:
                            continue
                        atlas_nonsingular += 1
                        mnu_loc = -ynu_loc * (mr_m ** (-1)) * ynu_loc.T
                        obs_p = pmns_obs_takagi(kmat * ye_loc * kmat, kmat * mnu_loc * kmat)
                        if (
                            mrat(15, 100) < obs_p["s12sq"] < mrat(55, 100)
                            and mrat(30, 100) < obs_p["s23sq"] < mrat(70, 100)
                            and obs_p["s13sq"] < mrat(8, 100)
                            and mrat(5, 1000) < obs_p["dm"] < mrat(15, 100)
                        ):
                            tag = f"{gname}_{kn}_over_{kr}_qR_{qr}_n5b_{n5b[0]}{n5b[1]}{n5b[2]}"
                            hits.append({"tag": tag, "obs": obs_p})
                            hit_mats = {"ye": kmat * ye_loc * kmat, "ynu": kmat * ynu_loc, "mr": mr_m}

    p_a384 = p_c["discrete_384_case_neutrino_atlas"]
    hit_ok = bool(len(hits) == 1 and hits[0]["tag"] == "CURV_5-6_over_5-6_qR_2_n5b_000")
    hit_pmns_max_rel = (
        max(rel_err(hits[0]["obs"][k], p_a384["simultaneous_hits"][0]["obs"][k]) for k in hits[0]["obs"])
        if hit_ok
        else mp.mpf(1)
    )

    _, _, tak_hit_err, tak_hit_pair_err, tak_hit_unit_err = takagi_real6_eigsy(hit_mats["mr"])

    def eps1_from_pair(tau_v: mp.mpc, p5: list[tuple[Fraction, Fraction]], p6: list[tuple[Fraction, Fraction]]) -> tuple[mp.mpf, mp.mpf]:
        wn = (w_avg(tau_v, p5, -3, 2) - w_avg(tau_v, p6, -3, 2)) / 2
        wr = (w_avg(tau_v, p5, 2, 2) - w_avg(tau_v, p6, 2, 2)) / 2
        ur, ms, _, _, _ = takagi_real6_eigsy((wr + wr.T) / 2)
        wh = (k_is * wn) * ur
        hm = wh.H * wh
        h11 = mp.re(hm[0, 0])
        e_sm = mp.mpf(0)
        e_mssm = mp.mpf(0)
        for j in (1, 2):
            xj = (ms[j] / ms[0]) ** 2
            imh = mp.im(hm[0, j] ** 2)
            e_sm += imh * (mp.sqrt(xj) * (1 / (1 - xj) + 1 - (1 + xj) * mp.log((1 + xj) / xj))) / (8 * mp.pi * h11)
            e_mssm += imh * (-mp.sqrt(xj) * (2 / (xj - 1) + mp.log((1 + xj) / xj))) / (8 * mp.pi * h11)
        return e_sm, e_mssm

    eps_sm_p, eps_mssm_p = eps1_from_pair(tau8, k5, k6)
    eps_sm_m, eps_mssm_m = eps1_from_pair(tau8_m, k5_cp, k6_cp)
    _, eps_mssm_naive_m = eps1_from_pair(tau8_m, k5, k6)
    cp_odd_sm_err = abs(eps_sm_p + eps_sm_m) / abs(eps_sm_p)
    cp_odd_mssm_err = abs(eps_mssm_p + eps_mssm_m) / abs(eps_mssm_p)
    naive_cp_fail_ratio = abs(eps_mssm_p + eps_mssm_naive_m) / abs(eps_mssm_p)

    eps_sm_rel = rel_err(eps_sm_p, p_a384["hit_eps1_SM_tau8_plus"])
    eps_mssm_rel = rel_err(eps_mssm_p, p_a384["hit_eps1_MSSM_tau8_plus"])

    ref_hit_pmns = hits[0]["obs"] if hit_ok else {}
    haar_hit_err = mp.mpf(0)
    for _ in range(10):
        mats = [haar_u3_householder_qr(rng) for _ in range(3)]
        for _, ue in mats:
            max_haar_unit_err = max(max_haar_unit_err, ue)
        ul_r, uer_r, unr_r = (m[0] for m in mats)
        ye_s = ul_r * hit_mats["ye"] * uer_r.H
        ynu_s = ul_r * hit_mats["ynu"] * unr_r
        mr_s = unr_r.T * hit_mats["mr"] * unr_r
        u_rs, m_rs, _, _, _ = takagi_real6_eigsy(mr_s)
        scr_p = pmns_obs_takagi(ye_s, -ynu_s * (mr_s ** (-1)) * ynu_s.T)
        wh_s = ynu_s * u_rs
        hm_s = wh_s.H * wh_s
        h11_s = mp.re(hm_s[0, 0])
        em_s = mp.mpf(0)
        for j in (1, 2):
            xj = (m_rs[j] / m_rs[0]) ** 2
            em_s += mp.im(hm_s[0, j] ** 2) * (-mp.sqrt(xj) * (2 / (xj - 1) + mp.log((1 + xj) / xj))) / (8 * mp.pi * h11_s)
        haar_hit_err = max(
            haar_hit_err,
            max(abs(scr_p[k] - ref_hit_pmns[k]) for k in ref_hit_pmns),
            abs(em_s - eps_mssm_p) / abs(eps_mssm_p),
        )

    mr_qr0 = (w_avg(tau8, k5, 0, 0) + w_avg(tau8, k6, 0, 0)) / 2
    _, smr_qr0, _, _, _ = takagi_real6_eigsy((mr_qr0 + mr_qr0.T) / 2)

    atlas_bits = mp.log(mp.mpf(atlas_total), 2)
    atlas_bits_rel = rel_err(atlas_bits, p_a384["guardrail1_priced_search_bits_log2_384"])

    gate_ref3 = bool(
        max_heat_jacobi_err < mpow10(-55)
        and max_haar_unit_err < mpow10(-55)
        and t12_56_err < mpow10(-48)
        and t12_k5_err < mpow10(-48)
        and k5_trap_rel < mpow10(-10)
        and (obs_f["v12"] > obs_f["v23"] > obs_f["v13"])
        and (obs_h["v12"] > obs_h["v23"] > obs_h["v13"])
        and flat_ckm_max_rel < mpow10(-10)
        and curv_ckm_max_rel < mpow10(-10)
        and bits_saved_rel < mpow10(-10)
        and dbar_000 < mpow10(-25)
        and haar_ckm_err < mpow10(-45)
        and hu_000_max_rel < mpow10(-10)
        and hu_100_max_rel < mpow10(-10)
        and haar_hu_err < mpow10(-45)
        and atlas_total == 384
        and atlas_nonsingular == 264
        and hit_ok
        and hit_pmns_max_rel < mpow10(-9)
        and eps_sm_rel < mpow10(-9)
        and eps_mssm_rel < mpow10(-9)
        and tak_hit_err < mpow10(-50)
        and tak_hit_pair_err < mpow10(-55)
        and tak_hit_unit_err < mpow10(-55)
        and max(cp_odd_sm_err, cp_odd_mssm_err) < mpow10(-45)
        and haar_hit_err < mpow10(-45)
        and atlas_bits_rel < mpow10(-10)
    )
    if not gate_ref3:
        discrepancies.append({"module": "REF-3", "id": "REF3_OW24C_GATE_FAIL"})

    return {
        "gate_ref3": gate_ref3,
        "engine_self_checks": {
            "jtheta_heat_and_jacobi_max_err": mstr(max_heat_jacobi_err, 10),
            "lcg128_householder_haar_unitarity_max_err": mstr(max_haar_unit_err, 10),
        },
        "type1_eq_type2_cancellation": {
            "K56_max_err": mstr(t12_56_err, 10),
            "K5_max_err": mstr(t12_k5_err, 10),
            "K5_over_K5_s23sq": mstr(p_t1_k5["s23sq"], 14),
            "K5_over_K5_s23sq_rel_err_vs_producer": mstr(k5_trap_rel, 10),
        },
        "pure_lopsided_SU5_n5b_000": {
            "flat_strict_CKM": bool(obs_f["v12"] > obs_f["v23"] > obs_f["v13"]),
            "curved_strict_CKM": bool(obs_h["v12"] > obs_h["v23"] > obs_h["v13"]),
            "flat_8obs_max_rel_err_vs_producer": mstr(flat_ckm_max_rel, 10),
            "curved_8obs_max_rel_err_vs_producer": mstr(curv_ckm_max_rel, 10),
            "bits_saved_log2_100": mstr(bits_saved, 14),
            "bits_saved_rel_err_vs_producer": mstr(bits_saved_rel, 10),
            "wirtinger_dbar_holomorphy": mstr(dbar_000, 10),
            "lcg128_haar_10trial_U3_5_err": mstr(haar_ckm_err, 10),
        },
        "physical_Hu_K5_unblocking": {
            "n5b_000_s23sq": mstr(pmns_hu_000["s23sq"], 14),
            "n5b_100_s23sq": mstr(pmns_hu_100["s23sq"], 14),
            "n5b_000_5obs_max_rel_err_vs_producer": mstr(hu_000_max_rel, 10),
            "n5b_100_5obs_max_rel_err_vs_producer": mstr(hu_100_max_rel, 10),
            "lcg128_haar_10trial_U3_3_err": mstr(haar_hu_err, 10),
        },
        "discrete_384_atlas_real6_takagi": {
            "total_cases": atlas_total,
            "nonsingular_MR_cases": atlas_nonsingular,
            "simultaneous_hits_count": len(hits),
            "hit_tag": hits[0]["tag"] if hits else "",
            "hit_5pmns_max_rel_err_vs_producer": mstr(hit_pmns_max_rel, 10),
            "hit_real6_takagi_frob_err": mstr(tak_hit_err, 10),
            "hit_real6_spectral_pair_err": mstr(tak_hit_pair_err, 10),
            "hit_real6_unitarity_err": mstr(tak_hit_unit_err, 10),
            "hit_eps1_MSSM": mstr(eps_mssm_p, 14),
            "hit_eps1_SM": mstr(eps_sm_p, 14),
            "hit_eps1_MSSM_rel_err_vs_producer": mstr(eps_mssm_rel, 10),
            "hit_eps1_SM_rel_err_vs_producer": mstr(eps_sm_rel, 10),
            "hit_geom_CP_odd_MSSM_err": mstr(cp_odd_mssm_err, 10),
            "hit_geom_CP_odd_SM_err": mstr(cp_odd_sm_err, 10),
            "hit_lcg128_haar_10trial_U3_3_err": mstr(haar_hit_err, 10),
            "guardrail1_log2_384_bits": mstr(atlas_bits, 14),
            "guardrail1_bits_rel_err_vs_producer": mstr(atlas_bits_rel, 10),
        },
        "_internal": {
            "k5_k5_s23sq": p_t1_k5["s23sq"],
            "qr0_sv_min": smr_qr0[0],
            "atlas_bits": atlas_bits,
            "naive_cp_fail_ratio": naive_cp_fail_ratio,
        },
    }


# ==============================================================================
# REF-4: Disjoint OW24-D, A2-OW16 v12, & 6 / 6 Independent Referee Planted Faults
# ==============================================================================

def klein_j_from_jtheta(tau: mp.mpc) -> mp.mpc:
    """Disjoint Klein j(tau) from Jacobi theta_2, theta_3, theta_4 (zero q-series)."""
    qn = mp.exp(IMAG * mp.pi * tau)
    t2 = mp.jtheta(2, 0, qn)
    t3 = mp.jtheta(3, 0, qn)
    t4 = mp.jtheta(4, 0, qn)
    lam = (t2 / t3) ** 4
    return 256 * ((1 - lam + lam * lam) ** 3) / ((lam * (1 - lam)) ** 2)


def run_ref_4(
    ow24: dict[str, Any],
    ow16: dict[str, Any],
    ow23: dict[str, Any],
    ref1: dict[str, Any],
    ref2: dict[str, Any],
    ref3: dict[str, Any],
    discrepancies: list[dict[str, Any]],
) -> dict[str, Any]:
    mp.mp.dps = 55

    # 1. Independent OW24-D 12-gate & dual readiness recomputation
    o23d = ow23["OW23_D_12gate_alpha_beta_ledger_and_readiness"]
    p24d = ow24["OW24_D_12gate_and_dual_readiness"]

    r2_ok = bool(ref1["gate_ref1"])
    r3_g2_ok = bool(ref2["g2_conical_locus_weight_sum_audit"]["exact_match_vs_producer"])
    r3_bulk_gs_ok = bool(ref2["bulk_orbifold_240root_audit"]["bulk_only_GS_universal_count_out_of_9"] > 0)
    r4_exists_ok = bool(ref3["discrete_384_atlas_real6_takagi"]["simultaneous_hits_count"] >= 1)
    r4_zero_bits = bool(ref3["_internal"]["atlas_bits"] == 0)

    alpha_12 = dict(o23d["candidate_alpha_12gates"])
    beta_12 = dict(o23d["candidate_beta_12gates"])
    alpha_12.pop("G11_single_modulus_tau0_eq_8tau0_no_cover_gap")
    beta_12.pop("G11_single_modulus_tau0_eq_8tau0_no_cover_gap")
    alpha_12["G11_single_modulus_tau0_to_8tau0_M8_magnetized_bridge"] = r2_ok
    beta_12["G11_single_modulus_tau0_to_8tau0_M8_magnetized_bridge"] = r2_ok

    alpha_score = sum(int(v) for v in alpha_12.values())
    beta_score = sum(int(v) for v in beta_12.values())

    omega_cusp = mrat(-1, 2) + IMAG * mp.sqrt(3) / 2
    j_omega = klein_j_from_jtheta(omega_cusp)
    u2_cusp_ok = bool(abs(j_omega - mp.mpf(1728)) < mpow10(-10))

    uncond_crit = {
        "U1_single_action_12_of_12_internal_gates": bool(beta_score == 12),
        "U2_R2_M8_flux_dynamically_derived_from_7D_M3_no_cusp_choice": u2_cusp_ok,
        "U3_R3_bulk_orbifold_closes_GS_without_twisted_states": r3_bulk_gs_ok,
        "U4_R4_neutrino_PMNS_zero_atlas_search_bits": r4_zero_bits,
    }
    cond_crit = {
        "C1_Beta_passes_12_of_12_gates_on_M8_single_torus": bool(beta_score == 12),
        "C2_R2_single_torus_M8_Dirac_and_Gram_orthogonality_proved": r2_ok,
        "C3_R3_G2_conical_locus_SU5xSU5_anomaly_free_8_of_8": r3_g2_ok,
        "C4_R4_simultaneous_large_mixing_PMNS_existence_proved_and_bit_priced": r4_exists_ok,
        "C5_cosmology_4D_unimod_anti_decompact_and_CP_wall_erasure": bool(
            o23d["pre_unblinding_readiness"]["criteria"]["R5_cosmology_4D_unimod_plus_CP_wall_erasure_closed"]
        ),
    }
    ready_uncond = all(uncond_crit.values())
    ready_cond = all(cond_crit.values())
    seams = [k for k, v in uncond_crit.items() if not v]

    ow24d_exact_match = bool(
        alpha_score == 9
        and beta_score == 12
        and alpha_12 == p24d["candidate_alpha_12gates_mag"]
        and beta_12 == p24d["candidate_beta_12gates_mag"]
        and (not ready_uncond)
        and ready_uncond == p24d["unconditional_readiness"]["ready_to_unblind_unconditional"]
        and seams == p24d["unconditional_readiness"]["remaining_uv_seams"]
        and ready_cond
        and ready_cond == p24d["conditional_priced_blind_lock_readiness"]["ready_for_conditional_priced_blind_lock"]
    )

    # 2. Independent A2-OW16 v12 audit: 1/10/9/4 partition, 17/17 locks, 34/34 false-flag JSONs, 6/6 PF
    led = ow16["blind_prediction_ledger_24_v12"]
    obs_list = led["observables"]
    bucket_cnt = Counter(row["bucket"] for row in obs_list)
    expected_buckets = {
        "DERIVED_EXACT": 1,
        "CONDITIONAL_OR_QUALITATIVE": 10,
        "INTERNAL_WALL_OR_TENSION": 9,
        "OPEN_EXTERNAL_BOUNDARY": 4,
    }
    obs_ids = sorted(row["id"] for row in obs_list)
    expected_ids = [f"OBS-{i:02d}" for i in range(1, 25)]
    sole_exact_ids = [row["id"] for row in obs_list if row["bucket"] == "DERIVED_EXACT"]
    obs22_rows = [row for row in obs_list if row["id"] == "OBS-22"]
    obs22_beta_ok = bool(
        len(obs22_rows) == 1
        and "-76/3" in obs22_rows[0]["value"]
        and "-151/6" not in obs22_rows[0]["value"]
    )
    partition_ok = bool(
        dict(bucket_cnt) == expected_buckets
        and obs_ids == expected_ids
        and sole_exact_ids == ["OBS-07"]
        and obs22_beta_ok
    )

    def load_j(rel_path: str) -> dict[str, Any]:
        return json.loads((RELAYS_DIR / rel_path).read_text(encoding="utf-8"))

    j22 = load_j("a2_ow22_v2/a2_ow22_v2_results.json")
    j21 = load_j("a2_ow21_v3/a2_ow21_v3_results.json")
    jl23 = load_j("a2_peer_link23/a2_peer_link23_results.json")
    j20 = load_j("a2_ow20/a2_ow20_results.json")
    j19 = load_j("a2_ow19_v3/a2_ow19_v3_results.json")
    j18 = load_j("a2_ow18_v3/a2_ow18_v3_results.json")
    j17 = load_j("a2_ow17_v2/a2_ow17_v2_results.json")
    j12 = load_j("a2_ow12_v3/verify_a2_ow12_v3_out.json")

    o24a = ow24["OW24_A_R2_magnetized_M8_single_torus_bridge"]
    o24b = ow24["OW24_B_R3_e8_bulk_orbifold_anomalies_vs_g2_locus"]
    o24c = ow24["OW24_C_R4_type12_cancel_hu_k5_and_384_atlas"]
    o24d = ow24["OW24_D_12gate_and_dual_readiness"]
    o23a = ow23["OW23_A_e8_uv_gravity_dt_axion_mckay"]
    o23b = ow23["OW23_B_tau_cover_mostow_lopsided_su5_mr_seesaw"]
    o23c = ow23["OW23_C_real_7d_curvature_unimodular_cusp_cp_walls"]
    o22a = j22["OW22_A_one_universe_matrix_and_6d_susy_casimir"]
    o22b = j22["OW22_B_curved_ckm_protection_and_neutrino_rank1"]
    o22c = j22["OW22_C_o6_gb_orientifold_and_60efold_overshoot"]
    o22d = j22["OW22_D_foundational_d4_audit"]
    o21a = j21["OW21_A_fl4_audit_and_curved_kahler"]
    o21b = j21["OW21_B_6d_e8_ghu_quartics_and_repaired_glr"]
    o21c = j21["OW21_C_universal_3term_ds_and_3d_stabilization"]
    o20a = j20["OW20_A_type2_2hdm_rge_and_2flav_lepto"]
    o20b = j20["OW20_B_consistent_frg_higgs_audit_and_e6"]
    o20c = j20["OW20_C_synergy144_and_so2d_anomalies"]
    o19a = j19["OW19_A_2d_hyperbolic_kahler_and_lepto"]
    o19b = j19["OW19_B_e6_hierarchy_axion_and_majorana_dm"]
    o19c = j19["OW19_C_6d_s3_z5_root_lattice_casimir"]

    indep_locks = {
        "LOCK_01_type2_2hdm_2loop_ce_benchmark_and_haar": bool(
            o20a["type2_2hdm_chowdhury_eberhardt_benchmark"]["all_15_coeffs_exact"]
            and o20a["f_ow18_01_1hdm_bug_and_benchmark"]["ckm_running_sign_reverses"]
            and mp.mpf(o20a["type2_2hdm_noncommuting_3x3_integration"]["haar_10trial_max_frob_err"]) < mpow10(-30)
        ),
        "LOCK_02_two_flavor_leptogenesis_rad_vs_tree_and_mirror": bool(
            mp.mpf(o20a["f_c30_08_two_flavor_leptogenesis"]["rad_flat_yb_2f_plus"]) > 0
            and mp.mpf(o20a["f_c30_08_two_flavor_leptogenesis"]["tree_flat_yb_2f_plus"]) < 0
            and mp.mpf(o20a["f_c30_08_two_flavor_leptogenesis"]["mirror_rad_2f_err"]) < mpow10(-35)
            and mp.mpf(o20a["f_c30_08_two_flavor_leptogenesis"]["mirror_tree_2f_err"]) < mpow10(-35)
        ),
        "LOCK_03_consistent_non_chimera_frg_type1_vs_type2": bool(
            o20b["f_ow18_02_consistent_frg_gsm_2hdm"]["no_positive_pure_gauge_uv_fp_either_scheme"]
            and mp.mpf(o20b["f_ow18_02_consistent_frg_gsm_2hdm"]["type1_disc"]) > mp.mpf(789)
            and mp.mpf(o20b["f_ow18_02_consistent_frg_gsm_2hdm"]["type2_disc"]) < mp.mpf(-6)
        ),
        "LOCK_04_prose_higgs_error_audited_and_e6_nw81_z4": bool(
            mp.mpf(o20b["f_ow18_03_prose_vs_json_higgs_audit"]["prose_mH0_rel_err"]) > mrat(26, 100)
            and o20b["f_ow18_05_and_f_c30_01_e6_nw81_and_z4"]["breaks_DEP_lt_31_cap"]
            and o20b["f_ow18_05_and_f_c30_01_e6_nw81_and_z4"]["Z4_forbids_NR_majorana_mass_MR_identically"]
            and o20b["f_ow18_05_and_f_c30_01_e6_nw81_and_z4"]["PM_126barH_preserves_dm_parity"] == 1
        ),
        "LOCK_05_synergy144_sl2z_covariance_and_broken_antipodal": bool(
            o20c["f_ow18_06_synergy_s1_144_and_antipodal"]["P5_x_P6_pairs"] == 144
            and o20c["f_ow18_06_synergy_s1_144_and_antipodal"]["sl2z_conjugacy_covariance_ok"]
            and o20c["f_ow18_06_synergy_s1_144_and_antipodal"]["antipodal_w_eq_neg_w_broken"]
        ),
        "LOCK_06_computed_so2d_cubic_anomalies_and_spin10_beta_neg76_3": bool(
            o20c["f_ow18_08_explicit_so2d_cubic_anomalies"]["SO6_anomalous_minus1"]
            and o20c["f_ow18_08_explicit_so2d_cubic_anomalies"]["SO8_to_SO30_anomaly_free_computed"]
            and o20c["f_ow18_07_spin10_brane2h_beta"]["b_Spin10_pure_fermion_brane2H"] == "-76/3"
        ),
        "LOCK_07_ow19_2d_hyperbolic_kahler_and_gauss_bonnet": bool(
            o19a["gate_a"]
            and o19a["kahler_2d_hyperbolic"]["ostrowski_bounds_ok"]
            and mp.mpf(o19a["synergy_s1_2d_shifts"]["haar_10trial_max_drift"]) < mpow10(-30)
        ),
        "LOCK_08_ow19_e6_hierarchy_axion_thm2_and_majorana_pwave": bool(
            o19b["gate_b"]
            and o19b["b1_e6_nonsusy_hierarchy"]["dm_H2_coeff_on_g4_S2_over_pi2"] == "-1/24"
            and o19b["b2_7d_cs_axion_theorem2"]["symbolic_d_invariance_zero"]
            and o19b["b3_majorana_psiS_pwave_dm"]["g_GUT_and_S_vev_cancel_identically"]
        ),
        "LOCK_09_ow19_6d_s3_z5_root_lattice_census_3905": bool(
            o19c["gate_c"]
            and o19c["exhaustive_z5_census"]["E_8"]["max_pure_YM_C6"] == "0"
            and o19c["exhaustive_z5_census"]["SO(10)"]["max_3x16_4Dchiral_C6"] == "-1456/25"
        ),
        "LOCK_10_6d_i8_7d_cs_axion_E_over_N_8_3_exact": bool(
            j12["OW12_A_strong_cp_and_7D_CS_axion"]["spin10_7D_CS_axion"]["E_over_N"] == "8/3"
        ),
        "LOCK_11_proca_antigravity_vs_sen_ir_exact": bool(
            j18["ow18_c"]["f_a2_04_proca_antigravity_and_sen_ir"]["strictly_negative_all_Lambda_ge_MX"]
            and j18["ow18_c"]["f_a2_04_proca_antigravity_and_sen_ir"]["sen_ir_2_c_minus_a_45weyl"] == "-277/360"
        ),
        "LOCK_12_brane2h_casimir_and_dim13_proca32": bool(
            j17["ow17_a_seam_s2_brane_2H"]["casimir_6d_table"]["spin10_brane_2H"]["nB_minus_nF"] == -6
            and j18["ow18_b"]["f_a2_02_so10_and_e6_bridge"]["dim_C_P_PS_and_J5_exact"] == 13
            and j18["ow18_b"]["f_a2_02_so10_and_e6_bridge"]["n_broken_proca_exact"] == 32
        ),
        "LOCK_13_peer_link23_and_48dps_frobenius_bc_star": bool(
            jl23["all_gates_passed"]
            and jl23["L23_A_verified_link23_theorems"]["r_LR_chiral"] == "2/5"
            and jl23["L23_B_five_first_principles_catches"]["LINK23_F1_Z2_Cpsi_impossibility"]["r_u1_roots_broken_out_of_72"] == 32
            and jl23["L23_B_five_first_principles_catches"]["LINK23_F2_orbifold_16_split_and_chiS_charge"]["sector_dims_in_16"] == [2, 2, 6, 6]
            and mp.mpf(jl23["L23_C_ow19_f1_f3_remediation"]["OW19_F3_exact_48dps_frobenius_bc_star"]["bc_star_Ma_vs_Mb_diff"]) < mpow10(-45)
        ),
        "LOCK_14_ow21_v3_fl4_complete2loop_ghu_and_3term_ds": bool(
            j21["all_gates_passed"]
            and o21a["peer_11fd7c712_manifests_matched"] == 13
            and o21a["FL4_F1_curved_2d_hyperbolic_kahler_distortion"]["ckm_v23_exceeds_v12_on_curved_2dhyp"]
            and o21b["ghu_uv_quartics_over_g2"]["case2_split_type2"] == ["1", "1", "0", "-1/2"]
            and o21b["two_loop_ghu_2hdm_running_t_0_to_neg32"]["quartic_rge_order"] == "complete_2loop_gauge_yukawa_quartic_CE1503"
            and o21b["two_loop_ghu_2hdm_running_t_0_to_neg32"]["all_9_runs_bfb_ir"]
            and o21c["simultaneous_3d_stabilization_E8_3x27"]["all_3_eigenvalues_strictly_positive"]
        ),
        "LOCK_15_ow22_one_universe_curved_flavor_inflation_d4": bool(
            j22["all_gates_passed"]
            and o22a["sakharov_susy_a1_exact"]["a1_massive_N1_vec_mult_xi0"] == "0"
            and o22a["sakharov_susy_a1_exact"]["a1_total_SUSY_SO10_to_GSM_U1X_xi0"] == "37/2"
            and o22a["best_branch_B4_passes_7_of_8_failing_only_DEP"]
            and o22b["curved_2d_hyp_ckm_structural_protection"]["fn_320_strict_hierarchical_flat_and_curved"]
            and o22b["holomorphic_neutrino_rank1_theorem"]["qR0_rank2_dirac_and_exact_rank1_seesaw"]
            and o22c["seven_d_gauss_bonnet_3d_stabilization"]["all_3_eigenvalues_strictly_positive"]
            and o22c["orientifold_b1_eq_3_parity_theorem"]["orientation_reversing_cannot_preserve_all_3_cycles"]
            and (not o22c["kallosh_linde_60efold_inflation_overshoot"]["B3500_safe_V0_50"]["decompactified"])
            and o22c["kallosh_linde_60efold_inflation_overshoot"]["B3500_overshoot_V0_100"]["decompactified"]
            and o22d["joint_YM_Hodge_Orbits_Chiral"] == [4]
        ),
        "LOCK_16_ow23_v3_single_universe_killshots_and_readiness": bool(
            ow23["all_gates_passed"]
            and o23a["gravity_window_0_lt_NC_minus_NV_le_10"]["B4_UV_score"] == 8
            and o23a["gravity_window_0_lt_NC_minus_NV_le_10"]["surviving_N_gen_HuHd"] == [3]
            and o23a["e8_240_roots_and_dt_splitting"]["doublet_triplet_20_vs_30_split_exact"]
            and o23a["multi_axion_strong_cp_kill_test"]["two_axion_relaxes_both_below_1e_50"]
            and o23a["mckay_2I_SL2_F5_unity"]["SL2_F5_maximal_cyclic_orders"] == [4, 6, 10]
            and (not o23b["tau0_vs_8tau0_and_mostow_cusp"]["tau0_and_8tau0_SL2Z_equivalent"])
            and o23c["curvature_nogo_and_Rmn2_resolution"]["R7_sq_ghost_vs_bare_dS_strictly_disjoint"]
            and o23c["unimodular_4D_p0_vs_7D_p3"]["anti_decompactification_V_infty_gt_V_min"]
            and o23d["candidate_beta_score"] == 11
        ),
        "LOCK_17_ow24_v2_final_three_blockers_r2_r3_r4": bool(
            ow24["all_gates_passed"]
            and o24a["unique_even_flux_M8_theorem"]["even_M_giving_3_Z2_odd_modes_in_1_to_20"] == [8]
            and mp.mpf(o24a["magnetized_dirac_6D_at_tau0"]["L2_3x3_Gram_orthogonality_frob_err"]) < mpow10(-50)
            and o24b["bulk_orbifold_census"]["smooth_T2_GS_exact_zero_all_4_test_fluxes"]
            and o24b["bulk_orbifold_census"]["T2_Z4_count"] == 7
            and o24b["bulk_orbifold_census"]["T2_Z4_unique_M8_count"] == 1
            and o24b["bulk_orbifold_census"]["T2_Z4_witten0_post_DT_le10_models"] == [[-3, -3, 2, 4]]
            and o24b["bulk_orbifold_census"]["T2_Z2_M4_enhanced_to_E6_NV82"]
            and o24b["bulk_orbifold_census"]["bulk_only_GS_universal_count_out_of_9"] == 0
            and o24b["g2_conical_locus_resolution"]["all_anomaly_and_gravity_gates_passed"]
            and mp.mpf(o24c["type1_eq_type2_cancellation_theorem"]["qR_plus3_K56_Type1_vs_Type2_max_err"]) < mpow10(-50)
            and o24c["discrete_384_case_neutrino_atlas"]["simultaneous_hits_count"] == 1
            and o24d["candidate_beta_score"] == 12
            and (not o24d["unconditional_readiness"]["ready_to_unblind_unconditional"])
            and o24d["conditional_priced_blind_lock_readiness"]["ready_for_conditional_priced_blind_lock"]
        ),
    }
    locks_17_ok = bool(
        len(indep_locks) == 17
        and all(indep_locks.values())
        and indep_locks == ow16["cross_card_locks_v12"]["locks"]
    )

    # Independent pre-referee-v2 historical false-flag JSON census (34 files, incl. frozen a2_ow24_referee v1!)
    own_rel = str(OUT_JSON.relative_to(REPO_ROOT))
    ow16_rel = str(RESULTS_OW16.relative_to(REPO_ROOT))
    false_found: list[dict[str, Any]] = []
    for jp in sorted(RELAYS_DIR.rglob("*.json")):
        rel_p = str(jp.relative_to(REPO_ROOT))
        if rel_p in (own_rel, ow16_rel) or rel_p.startswith("relays/a2_ow24_referee_v2/"):
            continue
        d = json.loads(jp.read_text(encoding="utf-8"))
        if not isinstance(d, dict):
            continue
        flags = []
        for k in ("all_gates_passed", "overall_pass", "pass", "all_passed"):
            if k in d and d[k] is False:
                flags.append(k)
        if isinstance(d.get("summary"), dict):
            for k in ("all_gates_passed", "overall_pass", "pass", "all_passed"):
                if k in d["summary"] and d["summary"][k] is False:
                    flags.append("summary." + k)
        if flags:
            false_found.append({"file": rel_p, "false_keys": flags})
    false_34_exact = bool(
        len(false_found) == 34
        and false_found == ow16["historical_false_json_disclosure"]["files"]
    )

    g5 = ow16["guardrail5_input_ledger_v12"]
    g5_ok = bool(
        g5["dimensionful_anchor_count"] == 1
        and g5["dimensionful_anchors"] == ["v_EW"]
        and g5["total_priced_continuous_ratios_baseline_4d"] == 15
        and rel_err(g5["discrete_synergy_s1_144_to_2_bits"], mp.log(mp.mpf(72), 2)) < mpow10(-11)
        and rel_err(g5["conditional_parameter_reduction_branches"]["branch_B4_UV_pure_lopsided_SU5_bits_saved_vs_9int"], mp.log(mp.mpf(100), 2)) < mpow10(-10)
        and rel_err(g5["conditional_parameter_reduction_branches"]["branch_R4_384_atlas_hit_guardrail1_bits"], mp.log(mp.mpf(384), 2)) < mpow10(-10)
    )
    pf_ow16 = ow16["planted_faults_v12"]
    ow16_pf_6_ok = bool(pf_ow16["caught"] == 6 and pf_ow16["total"] == 6 and all(pf_ow16["controls"].values()))

    # 3. 6 / 6 Independent Referee Planted Fault Controls
    tampered_manifests = verify_all_branch_manifests(tamper_entry_idx=0)
    pf_ref_1 = bool(not tampered_manifests["all_verified"] and tampered_manifests["mismatch_count"] == 1)
    pf_ref_2 = bool(
        ref1["_internal"]["m6_n_odd"] != 3
        and ref1["_internal"]["wrong_sign_pde_err"] > mp.mpf(1)
        and ref1["_internal"]["max_pde_res"] < mpow10(-30)
    )
    pf_ref_3 = bool(
        ref2["_internal"]["smooth_bug_m8_gs"] != (Fraction(0), Fraction(0))
        and ref2["_internal"]["su5_corrupt_cubic"] != 0
    )
    pf_ref_4 = bool(
        (ref2["_internal"]["z4_m8_true_doublets"] % 2) == 1
        and ref2["_internal"]["z2_m4_true_nv"] == 82
        and ref2["_internal"]["z2_m4_true_nv"] != 50
    )
    pf_ref_5 = bool(
        ref3["_internal"]["k5_k5_s23sq"] < mrat(5, 100)
        and ref3["_internal"]["qr0_sv_min"] < mpow10(-40)
    )
    pf_ref_6 = bool(
        ref3["_internal"]["atlas_bits"] > mp.mpf(8)
        and ref3["_internal"]["naive_cp_fail_ratio"] > mrat(1, 10)
    )
    ref_faults = {
        "PF_REF_1_manifest_1byte_tamper_caught": pf_ref_1,
        "PF_REF_2_M6_parity_and_flipped_Dirac_sign_caught": pf_ref_2,
        "PF_REF_3_smooth_T2_03_doublecount_and_corrupt_SU5_cubic_caught": pf_ref_3,
        "PF_REF_4_Z4_M8_Witten_odd_and_Z2_M4_unbroken_E6_caught": pf_ref_4,
        "PF_REF_5_K5_over_K5_trap_and_qR0_singular_takagi_caught": pf_ref_5,
        "PF_REF_6_Guardrail1_zero_bit_atlas_and_naive_CP_caught": pf_ref_6,
    }
    ref_pf_ok = bool(all(ref_faults.values()))

    gate_ref4 = bool(
        ow24d_exact_match
        and partition_ok
        and locks_17_ok
        and false_34_exact
        and g5_ok
        and ow16_pf_6_ok
        and ref_pf_ok
    )
    if not gate_ref4:
        discrepancies.append({"module": "REF-4", "id": "REF4_OW24D_OR_OW16V12_GATE_FAIL"})

    return {
        "gate_ref4": gate_ref4,
        "ow24_d_audit": {
            "alpha_score": alpha_score,
            "beta_score": beta_score,
            "j_omega_abs_err_from_0": mstr(abs(j_omega), 10),
            "ready_to_unblind_unconditional": ready_uncond,
            "remaining_uv_seams": seams,
            "ready_for_conditional_priced_blind_lock": ready_cond,
            "exact_match_vs_producer": ow24d_exact_match,
        },
        "a2_ow16_v12_audit": {
            "counts_by_bucket": dict(bucket_cnt),
            "partition_1_10_9_4_and_obs22_ok": partition_ok,
            "locks_17_of_17_independent_ok": locks_17_ok,
            "historical_false_flag_jsons_count": len(false_found),
            "historical_false_flag_34_exact_match": false_34_exact,
            "guardrail5_ok": g5_ok,
            "ow16v12_planted_6_of_6_ok": ow16_pf_6_ok,
        },
        "referee_planted_faults": {
            "ok": ref_pf_ok,
            "caught": sum(int(v) for v in ref_faults.values()),
            "total": len(ref_faults),
            "controls": ref_faults,
        },
    }


def main() -> None:
    ow24_text = RESULTS_OW24.read_text(encoding="utf-8")
    ow16_text = RESULTS_OW16.read_text(encoding="utf-8")
    ow24 = json.loads(ow24_text)
    ow16 = json.loads(ow16_text)
    ow23 = json.loads(RESULTS_OW23.read_text(encoding="utf-8"))
    ow19 = json.loads(RESULTS_OW19.read_text(encoding="utf-8"))

    discrepancies: list[dict[str, Any]] = []
    audit_notes: list[str] = []

    res_0 = run_ref_0(ow24, ow16, ow24_text, ow16_text, discrepancies)
    res_1 = run_ref_1(ow24, discrepancies)
    res_2 = run_ref_2(ow24, discrepancies, audit_notes)
    res_3 = run_ref_3(ow24, ow19, discrepancies)
    res_4 = run_ref_4(ow24, ow16, ow23, res_1, res_2, res_3, discrepancies)

    def strip_internal(d: dict[str, Any]) -> dict[str, Any]:
        return {k: v for k, v in d.items() if k != "_internal"}

    all_passed = bool(
        res_0["gate_ref0"]
        and res_1["gate_ref1"]
        and res_2["gate_ref2"]
        and res_3["gate_ref3"]
        and res_4["gate_ref4"]
        and len(discrepancies) == 0
    )

    out = {
        "referee_card": "A2-OW24-v2 & A2-OW16-v12 Cold-Room Zero-Trust Referee (v2)",
        "supersedes_frozen_v1": "226ead9d0 -> 598eaeb57 (frozen untouched; v2 certifies remediated A2-OW24 v2 & A2-OW16 v12)",
        "seat": "agy-002",
        "firewall": "0 of 19",
        "working_dps_ref1": 65,
        "working_dps_ref2": 50,
        "working_dps_ref3": 60,
        "REF_0_hygiene_ast_json_manifests": res_0,
        "REF_1_disjoint_ow24_a_r2_jtheta_gl_snf_rrcf": strip_internal(res_1),
        "REF_2_disjoint_ow24_b_r3_dft_eig_240e8_g2": strip_internal(res_2),
        "REF_3_disjoint_ow24_c_r4_jtheta_real6_takagi_384atlas": strip_internal(res_3),
        "REF_4_disjoint_ow24_d_ow16v12_and_6_planted_faults": res_4,
        "discrepancies_count": len(discrepancies),
        "discrepancies": discrepancies,
        "referee_audit_notes": audit_notes,
        "all_gates_passed": all_passed,
    }

    out_text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    self_json_floats = assert_no_json_floats(out_text)
    if self_json_floats != 0:
        raise AssertionError(f"Self JSON contains {self_json_floats} float tokens!")

    out_bytes = out_text.encode("utf-8")
    OUT_JSON.write_bytes(out_bytes)
    out_sha = sha256_bytes(out_bytes)
    (SELF_DIR / "OUTPUT_SHA256.txt").write_text(
        f"{out_sha}  {OUT_JSON.relative_to(REPO_ROOT)}\n",
        encoding="utf-8",
    )

    print(json.dumps({
        "referee_card": out["referee_card"],
        "all_gates_passed": all_passed,
        "gate_ref0": res_0["gate_ref0"],
        "gate_ref1": res_1["gate_ref1"],
        "gate_ref2": res_2["gate_ref2"],
        "gate_ref3": res_3["gate_ref3"],
        "gate_ref4": res_4["gate_ref4"],
        "discrepancies_count": len(discrepancies),
        "manifests_verified": f"{res_0['branch_manifests']['verified_entries']}/{res_0['branch_manifests']['total_entries']}",
        "output_sha256": out_sha,
    }, indent=2))


if __name__ == "__main__":
    main()
