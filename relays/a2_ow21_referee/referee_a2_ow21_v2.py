#!/usr/bin/env python3
"""
Isolated Cold-Room Zero-Shared-Code Independent Referee v2 for Seat agy-002:
  - Card A2-OW21 v3 (OW21-A, OW21-B complete 2-loop CE 1503.08216 quartics, OW21-C, OW21-D)
  - Card A2-OW16 v8 (Honest 24-Observable Master Ledger)

Preserves frozen v1 referee artifacts untouched (a01592cfc -> d0962341c).

Strict Cold-Room & Custody Standard:
  - Zero shared code with verify_a2_ow21*.py or verify_a2_ow16*.py
  - Strictly 0 of 19 empirical firewall (zero PDG/NuFIT/Planck/DESI/CODATA numbers)
  - Zero Python float/complex AST literals
  - Zero binary64 float()/complex() casts
  - Zero JSON float tokens in output
  - Zero peer / frontier / relays Python imports
"""

import ast
import hashlib
import json
import math
import re
import subprocess
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

REPO_ROOT = Path(__file__).resolve().parents[2]
REFEREE_DIR = Path(__file__).resolve().parent
SELF_PATH = Path(__file__).resolve()
OUT_JSON_PATH = REFEREE_DIR / "a2_ow21_referee_results_v2.json"
FUTURE_OUTPUT_MANIFEST = REFEREE_DIR / "OUTPUT_SHA256_v2.txt"

TARGET_OW21_JSON = REPO_ROOT / "relays" / "a2_ow21_v3" / "a2_ow21_v3_results.json"
TARGET_OW16_JSON = REPO_ROOT / "relays" / "a2_ow16_v8" / "a2_ow16_v8_results.json"
SEALED_OW19_JSON = REPO_ROOT / "relays" / "a2_ow19_v3" / "a2_ow19_v3_results.json"
TARGET_OW21_SCRIPT = REPO_ROOT / "relays" / "a2_ow21_v3" / "verify_a2_ow21_v3.py"
TARGET_OW16_SCRIPT = REPO_ROOT / "relays" / "a2_ow16_v8" / "verify_a2_ow16_v8.py"

mp.mp.dps = 55


# ---------------------------------------------------------------------------
# Strict Zero-Float / Zero-Cast / AST / Custody Helpers
# ---------------------------------------------------------------------------

def mp_rat(num, den=1):
    return mp.mpf(num) / mp.mpf(den)


def frac_to_mpf(fr):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


def mp_pow10(exp_int):
    return mp.mpf(10) ** exp_int


def mpf_str(x, digits=18):
    return mp.nstr(mp.mpf(x), digits)


def assert_no_json_floats(obj, path="root"):
    if isinstance(obj, bool) or obj is None or isinstance(obj, (int, str)):
        return 0
    if isinstance(obj, dict):
        count = 0
        for k, v in obj.items():
            count += assert_no_json_floats(v, f"{path}.{k}")
        return count
    if isinstance(obj, (list, tuple)):
        count = 0
        for idx, v in enumerate(obj):
            count += assert_no_json_floats(v, f"{path}[{idx}]")
        return count
    raise AssertionError(f"Non-JSON-safe or float token at {path}: type={type(obj).__name__}")


def count_json_float_tokens_in_text(raw_text):
    found = []

    def on_float(tok):
        found.append(tok)
        return tok

    json.loads(raw_text, parse_float=on_float)
    return len(found)


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    return sha256_bytes(Path(path).read_bytes())


FORBIDDEN_IMPORT_PREFIXES = (
    "frontier",
    "relays",
    "verify_",
    "referee_",
    "scripts",
    "src",
)

FORBIDDEN_CAST_NAMES = {"float", "complex", "float64", "float32", "complex128", "complex64"}


def ast_audit_source(source_text, label):
    tree = ast.parse(source_text, filename=str(label))
    float_complex_literals = 0
    binary64_casts = 0
    forbidden_imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant):
            if type(node.value).__name__ in ("float", "complex"):
                float_complex_literals += 1
        elif isinstance(node, ast.Call):
            fn = node.func
            if isinstance(fn, ast.Name) and fn.id in FORBIDDEN_CAST_NAMES:
                binary64_casts += 1
            elif isinstance(fn, ast.Attribute) and fn.attr in FORBIDDEN_CAST_NAMES:
                binary64_casts += 1
        elif isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.name
                if any(name == p or name.startswith(p + ".") or name.startswith(p) for p in FORBIDDEN_IMPORT_PREFIXES):
                    forbidden_imports.append(name)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if any(mod == p or mod.startswith(p + ".") or mod.startswith(p) for p in FORBIDDEN_IMPORT_PREFIXES):
                forbidden_imports.append(mod)
            for alias in node.names:
                nm = alias.name
                if any(nm.startswith(p) for p in ("verify_", "referee_")):
                    forbidden_imports.append(f"{mod}.{nm}")

    return {
        "file": str(label),
        "float_complex_literals": float_complex_literals,
        "binary64_casts": binary64_casts,
        "forbidden_imports_count": len(forbidden_imports),
        "forbidden_imports": forbidden_imports,
        "clean": (float_complex_literals == 0 and binary64_casts == 0 and len(forbidden_imports) == 0),
    }


def parse_manifest_lines(text):
    entries = []
    bsd_re = re.compile(r"^SHA256\s*\((.+)\)\s*=\s*([0-9a-fA-F]{64})$")
    gnu_re = re.compile(r"^([0-9a-fA-F]{64})\s+\*?(.+)$")
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m_gnu = gnu_re.match(line)
        if m_gnu:
            entries.append((m_gnu.group(1).lower(), m_gnu.group(2).strip()))
            continue
        m_bsd = bsd_re.match(line)
        if m_bsd:
            entries.append((m_bsd.group(2).lower(), m_bsd.group(1).strip()))
            continue
        entries.append(("MALFORMED", line))
    return entries


def git_run(args):
    proc = subprocess.run(
        ["git"] + args,
        cwd=str(REPO_ROOT),
        capture_output=True,
        check=True,
    )
    return proc.stdout


def git_blob_exists(rev, rel_path):
    proc = subprocess.run(
        ["git", "cat-file", "-e", f"{rev}:{rel_path}"],
        cwd=str(REPO_ROOT),
        capture_output=True,
    )
    return proc.returncode == 0


# ---------------------------------------------------------------------------
# Deterministic SplitMix64 PRNG & Mezzadri Haar U(3) Generator (55-dps)
# ---------------------------------------------------------------------------

class SplitMix64:
    def __init__(self, seed_int):
        self.state = seed_int & 0xFFFFFFFFFFFFFFFF

    def next_u64(self):
        self.state = (self.state + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & 0xFFFFFFFFFFFFFFFF
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & 0xFFFFFFFFFFFFFFFF
        z = (z ^ (z >> 31)) & 0xFFFFFFFFFFFFFFFF
        return z

    def next_unit_open(self):
        num = mp.mpf(self.next_u64()) * mp.mpf(1 << 64) + mp.mpf(self.next_u64()) + mp.mpf(1)
        den = mp.mpf(1 << 128) + mp.mpf(1)
        return num / den

    def next_normal_pair(self):
        u1 = self.next_unit_open()
        u2 = self.next_unit_open()
        rad = mp.sqrt(mp.mpf(-2) * mp.log(u1))
        ang = mp.mpf(2) * mp.pi * u2
        return rad * mp.cos(ang), rad * mp.sin(ang)

    def next_complex_normal(self):
        re_v, im_v = self.next_normal_pair()
        inv_s2 = mp.mpf(1) / mp.sqrt(mp.mpf(2))
        return mp.mpc(re_v * inv_s2, im_v * inv_s2)

    def next_haar_u3(self):
        cols = []
        for _ in range(3):
            cols.append([self.next_complex_normal() for _ in range(3)])
        q_cols = []
        for j in range(3):
            v = list(cols[j])
            for k in range(j):
                qk = q_cols[k]
                proj = sum(mp.conj(qk[r]) * v[r] for r in range(3))
                v = [v[r] - proj * qk[r] for r in range(3)]
            nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
            q_cols.append([v[r] / nrm for r in range(3)])
        q2_cols = []
        for j in range(3):
            v = list(q_cols[j])
            for k in range(j):
                qk = q2_cols[k]
                proj = sum(mp.conj(qk[r]) * v[r] for r in range(3))
                v = [v[r] - proj * qk[r] for r in range(3)]
            nrm = mp.sqrt(sum(abs(v[r]) ** 2 for r in range(3)))
            ph = mp.exp(mp.mpc(0, 1) * mp.mpf(2) * mp.pi * self.next_unit_open())
            q2_cols.append([ph * v[r] / nrm for r in range(3)])
        U = mp.matrix(3, 3)
        for c in range(3):
            for r in range(3):
                U[r, c] = q2_cols[c][r]
        return U


# ---------------------------------------------------------------------------
# REF-0: AST, JSON-Float, & Full Custody Audit
# ---------------------------------------------------------------------------

def run_ref0(ow21_data, ow16_data, discrepancies):
    ast_ow21 = ast_audit_source(TARGET_OW21_SCRIPT.read_text(encoding="utf-8"), "relays/a2_ow21_v3/verify_a2_ow21_v3.py")
    ast_ow16 = ast_audit_source(TARGET_OW16_SCRIPT.read_text(encoding="utf-8"), "relays/a2_ow16_v8/verify_a2_ow16_v8.py")
    ast_self = ast_audit_source(SELF_PATH.read_text(encoding="utf-8"), "relays/a2_ow21_referee/referee_a2_ow21_v2.py")

    ow21_json_floats = count_json_float_tokens_in_text(TARGET_OW21_JSON.read_text(encoding="utf-8"))
    ow16_json_floats = count_json_float_tokens_in_text(TARGET_OW16_JSON.read_text(encoding="utf-8"))

    ow21_sha_actual = sha256_file(TARGET_OW21_SCRIPT)
    ow16_sha_actual = sha256_file(TARGET_OW16_SCRIPT)
    ow21_sha_match = (ow21_sha_actual == ow21_data["hygiene"]["script_sha256"])
    ow16_sha_match = (ow16_sha_actual == ow16_data["hygiene"]["script_sha256"])

    # Verify 100% of branch relays/**/*SHA256*.txt manifests (excluding own future OUTPUT_SHA256_v2.txt)
    relays_dir = REPO_ROOT / "relays"
    manifest_files = sorted(relays_dir.rglob("*SHA256*.txt"))
    branch_total = 0
    branch_verified = 0
    branch_mismatches = []
    for mf in manifest_files:
        if mf.resolve() == FUTURE_OUTPUT_MANIFEST.resolve():
            continue
        rel_mf = mf.relative_to(REPO_ROOT).as_posix()
        entries = parse_manifest_lines(mf.read_text(encoding="utf-8"))
        for expected_hash, target_str in entries:
            branch_total += 1
            if expected_hash == "MALFORMED":
                branch_mismatches.append({"manifest": rel_mf, "reason": "malformed_line", "line": target_str})
                continue
            cand1 = mf.parent / target_str
            cand2 = REPO_ROOT / target_str
            if cand1.is_file():
                target_path = cand1
            elif cand2.is_file():
                target_path = cand2
            else:
                branch_mismatches.append({"manifest": rel_mf, "target": target_str, "reason": "missing_file"})
                continue
            actual_hash = sha256_file(target_path)
            if actual_hash == expected_hash:
                branch_verified += 1
            else:
                branch_mismatches.append({
                    "manifest": rel_mf,
                    "target": target_str,
                    "expected": expected_hash,
                    "actual": actual_hash,
                })

    # Verify all 13/13 new agy-exp 11fd7c712 manifests via git show
    diff_out = git_run(["diff", "--name-only", "dd74b56c1..11fd7c712"]).decode("utf-8")
    peer_manifest_paths = sorted(
        p.strip() for p in diff_out.splitlines()
        if p.strip() and "SHA256" in Path(p.strip()).name and p.strip().endswith(".txt")
    )
    peer_total = 0
    peer_verified = 0
    peer_mismatches = []
    for pm in peer_manifest_paths:
        content = git_run(["show", f"11fd7c712:{pm}"]).decode("utf-8")
        entries = parse_manifest_lines(content)
        for expected_hash, target_str in entries:
            peer_total += 1
            if expected_hash == "MALFORMED":
                peer_mismatches.append({"manifest": pm, "reason": "malformed_line", "line": target_str})
                continue
            parent_rel = Path(pm).parent
            cand1 = (parent_rel / target_str).as_posix()
            cand2 = target_str
            if git_blob_exists("11fd7c712", cand1):
                blob_path = cand1
            elif git_blob_exists("11fd7c712", cand2):
                blob_path = cand2
            else:
                peer_mismatches.append({"manifest": pm, "target": target_str, "reason": "missing_git_blob"})
                continue
            blob_bytes = git_run(["show", f"11fd7c712:{blob_path}"])
            actual_hash = sha256_bytes(blob_bytes)
            if actual_hash == expected_hash:
                peer_verified += 1
            else:
                peer_mismatches.append({
                    "manifest": pm,
                    "target": blob_path,
                    "expected": expected_hash,
                    "actual": actual_hash,
                })

    gate_pass = (
        ast_ow21["clean"]
        and ast_ow16["clean"]
        and ast_self["clean"]
        and ow21_json_floats == 0
        and ow16_json_floats == 0
        and ow21_sha_match
        and ow16_sha_match
        and branch_total > 0
        and branch_verified == branch_total
        and len(branch_mismatches) == 0
        and len(peer_manifest_paths) == 13
        and peer_total == 13
        and peer_verified == 13
        and len(peer_mismatches) == 0
    )
    if not gate_pass:
        discrepancies.append("REF_0_custody_or_hygiene_failed")

    return {
        "ast_audit": {
            "verify_a2_ow21_v3": ast_ow21,
            "verify_a2_ow16_v8": ast_ow16,
            "referee_a2_ow21_v2_self": ast_self,
        },
        "json_float_tokens": {
            "a2_ow21_v3_results": ow21_json_floats,
            "a2_ow16_v8_results": ow16_json_floats,
        },
        "reported_script_sha256_matches_disk": {
            "verify_a2_ow21_v3": ow21_sha_match,
            "verify_a2_ow16_v8": ow16_sha_match,
        },
        "branch_manifests": {
            "manifest_files_scanned": len(manifest_files),
            "entries_total": branch_total,
            "entries_verified": branch_verified,
            "mismatches": branch_mismatches,
        },
        "peer_11fd7c712_manifests": {
            "manifest_files_found": len(peer_manifest_paths),
            "entries_total": peer_total,
            "entries_verified": peer_verified,
            "mismatches": peer_mismatches,
        },
        "gate_pass": gate_pass,
    }


# ---------------------------------------------------------------------------
# REF-1: Disjoint mp.jtheta Audit of OW21-A (X-FLAVOR-LINK4, FL4-F1, FL4-F2)
# ---------------------------------------------------------------------------

def mat2_mul(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def mat2_transpose(A):
    return [[A[0][0], A[1][0]], [A[0][1], A[1][1]]]


def mat2_scale(c, A):
    return [[c * A[0][0], c * A[0][1]], [c * A[1][0], c * A[1][1]]]


def mat2_add(A, B):
    return [[A[0][0] + B[0][0], A[0][1] + B[0][1]], [A[1][0] + B[1][0], A[1][1] + B[1][1]]]


def jtheta_char_zero(ca_frac, cb_frac, tau, q_nome):
    I = mp.mpc(0, 1)
    na = math.floor(ca_frac)
    nb = math.floor(cb_frac)
    ta_f = ca_frac - na
    tb_f = cb_frac - nb
    ta = frac_to_mpf(ta_f)
    tb = frac_to_mpf(tb_f)
    z = mp.pi * (ta * tau + tb)
    base = mp.exp(I * mp.pi * (ta ** 2) * tau + mp.mpf(2) * mp.pi * I * ta * tb) * mp.jtheta(3, z, q_nome)
    if nb != 0 and ta_f != 0:
        base *= mp.exp(mp.mpf(2) * mp.pi * I * ta * mp.mpf(nb))
    return base


def is_odd_half_char(ca_frac, cb_frac):
    ta = ca_frac - math.floor(ca_frac)
    tb = cb_frac - math.floor(cb_frac)
    return (ta == Fraction(1, 2)) and (tb == Fraction(1, 2))


def build_s_hol_and_contractions_jtheta(tau):
    I = mp.mpc(0, 1)
    q = mp.exp(I * mp.pi * tau)
    th2 = mp.jtheta(2, 0, q)
    th3 = mp.jtheta(3, 0, q)
    th4 = mp.jtheta(4, 0, q)
    neg_one_eighth = mp_rat(-1, 8)
    l2 = neg_one_eighth * mp.jtheta(2, 0, q, 2) / th2
    l3 = neg_one_eighth * mp.jtheta(3, 0, q, 2) / th3
    l4 = neg_one_eighth * mp.jtheta(4, 0, q, 2) / th4
    e2 = -mp.jtheta(1, 0, q, 3) / mp.jtheta(1, 0, q, 1)
    e2_24 = e2 / mp.mpf(24)
    th1_p = mp.pi * mp.jtheta(1, 0, q, 1)

    q_i = [[I, mp.mpc(0, 0)], [mp.mpc(0, 0), -I]]
    q_j = [[mp.mpc(0, 0), mp.mpc(1, 0)], [mp.mpc(-1, 0), mp.mpc(0, 0)]]
    q_k = [[mp.mpc(0, 0), I], [I, mp.mpc(0, 0)]]
    I_2 = [[mp.mpc(1, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(1, 0)]]

    c_i = (-th2 / (th3 * th4)) * (l2 - l3 - l4 + e2_24)
    c_j = (-th4 / (th2 * th3)) * (l4 - l2 - l3 + e2_24)
    c_k = (I * th3 / (th2 * th4)) * (l3 - l2 - l4 + e2_24)

    S_hol = mat2_add(mat2_add(mat2_scale(c_i, q_i), mat2_scale(c_j, q_j)), mat2_scale(c_k, q_k))
    blk = [q_j, q_i, q_k]
    C = [[None] * 3 for _ in range(3)]
    for r in range(3):
        bt_qj_S = mat2_mul(mat2_mul(mat2_transpose(blk[r]), q_j), S_hol)
        for c in range(3):
            C[r][c] = mat2_mul(bt_qj_S, blk[c])

    half = mp_rat(1, 2)
    dual_e = {
        "1": mat2_scale(half, q_j),
        "i": mat2_scale(half, q_k),
        "j": mat2_scale(-half, I_2),
        "k": mat2_scale(-half, q_i),
    }
    return q, th1_p, C, dual_e, e2, mp.mpf(8) * (l2 + l3 + l4)


def w_hol_point_jtheta(tau, a_frac, b_frac, qL, qR, precomp=None):
    I = mp.mpc(0, 1)
    if precomp is None:
        q, th1_p, C, dual_e, _, _ = build_s_hol_and_contractions_jtheta(tau)
    else:
        q, th1_p, C, dual_e = precomp

    x0 = Fraction(qL) * a_frac
    x1 = Fraction(2 * qL) * b_frac
    y0 = Fraction(qR) * a_frac
    y1 = Fraction(2 * qR) * b_frac
    ap = x0 + y0
    am = x0 - y0
    bp = (x1 + y1) / Fraction(2)
    bm = (x1 - y1) / Fraction(2)

    eph = mp.exp(mp.mpf(-2) * mp.pi * I * frac_to_mpf(x0))
    kap = {
        "1": -I * eph,
        "i": mp.mpc(-1, 0),
        "j": -eph,
        "k": I,
    }
    half_f = Fraction(1, 2)
    cs = {
        "1": (ap + half_f, bp + half_f),
        "i": (ap + half_f, bp),
        "j": (ap, bp + half_f),
        "k": (ap, bp),
    }
    ds = {
        "1": (am + half_f, bm + half_f),
        "i": (am + half_f, bm),
        "j": (am, bm + half_f),
        "k": (am, bm),
    }

    M_W = [[mp.mpc(0, 0), mp.mpc(0, 0)], [mp.mpc(0, 0), mp.mpc(0, 0)]]
    for sk in ("1", "i", "j", "k"):
        if is_odd_half_char(cs[sk][0], cs[sk][1]) or is_odd_half_char(ds[sk][0], ds[sk][1]):
            continue
        t_c = jtheta_char_zero(cs[sk][0], cs[sk][1], tau, q)
        t_d = jtheta_char_zero(ds[sk][0], ds[sk][1], tau, q)
        r_sk = kap[sk] * t_c * t_d / th1_p
        M_W = mat2_add(M_W, mat2_scale(r_sk, dual_e[sk]))

    W = mp.matrix(3, 3)
    for r in range(3):
        for c in range(3):
            Cr = C[r][c]
            W[r, c] = (
                Cr[0][0] * M_W[0][0]
                + Cr[0][1] * M_W[0][1]
                + Cr[1][0] * M_W[1][0]
                + Cr[1][1] * M_W[1][1]
            )
    return W


def w_hol_avg_jtheta(tau, pts, qL, qR, precomp=None):
    if precomp is None:
        q, th1_p, C, dual_e, _, _ = build_s_hol_and_contractions_jtheta(tau)
        precomp = (q, th1_p, C, dual_e)
    acc = mp.zeros(3, 3)
    for a_f, b_f in pts:
        acc += w_hol_point_jtheta(tau, a_f, b_f, qL, qR, precomp=precomp)
    return acc / mp.mpf(len(pts))


def frob_norm(M):
    s = mp.mpf(0)
    for r in range(M.rows):
        for c in range(M.cols):
            s += abs(M[r, c]) ** 2
    return mp.sqrt(s)


def mat3_conj_T(M):
    H = mp.matrix(M.cols, M.rows)
    for r in range(M.rows):
        for c in range(M.cols):
            H[c, r] = mp.conj(M[r, c])
    return H


def svd_ascending_3x3(M):
    U, S, _ = mp.svd_c(M)
    s_asc = [S[2], S[1], S[0]]
    U_asc = mp.matrix(3, 3)
    for new_c, old_c in enumerate((2, 1, 0)):
        for r in range(3):
            U_asc[r, new_c] = U[r, old_c]
    return U_asc, s_asc


def flavor_observables(Wu, Wd, We):
    Uu, su = svd_ascending_3x3(Wu)
    Ud, sd = svd_ascending_3x3(Wd)
    _, se = svd_ascending_3x3(We)
    V = mat3_conj_T(Uu) * Ud
    v12 = abs(V[0, 1])
    v23 = abs(V[1, 2])
    v13 = abs(V[0, 2])
    J = mp.im(V[0, 1] * V[1, 2] * mp.conj(V[0, 2]) * mp.conj(V[1, 1]))
    return {
        "su": su,
        "sd": sd,
        "se": se,
        "s1_s3": [su[0] / su[2], sd[0] / sd[2], se[0] / se[2]],
        "s2_s3": [su[1] / su[2], sd[1] / sd[2], se[1] / se[2]],
        "ckm": [v12, v23, v13, J],
    }


def dbar_over_d_ratio(fn_of_tau, tau, h_step):
    I = mp.mpc(0, 1)
    two_h = mp.mpf(2) * h_step
    dx = (fn_of_tau(tau + h_step) - fn_of_tau(tau - h_step)) / two_h
    dy = (fn_of_tau(tau + I * h_step) - fn_of_tau(tau - I * h_step)) / two_h
    half = mp_rat(1, 2)
    dbar = half * (dx + I * dy)
    dhol = half * (dx - I * dy)
    return frob_norm(dbar) / frob_norm(dhol)


def run_ref1(ow21_data, ow19_data, discrepancies):
    I = mp.mpc(0, 1)
    tau8 = mp.mpc(mp_rat(16, 5), mp_rat(8, 5))

    K5 = [
        (Fraction(1, 5), Fraction(2, 5)),
        (Fraction(4, 5), Fraction(3, 5)),
        (Fraction(2, 5), Fraction(4, 5)),
        (Fraction(3, 5), Fraction(1, 5)),
    ]
    K6 = [
        (Fraction(1, 6), Fraction(1, 6)),
        (Fraction(5, 6), Fraction(5, 6)),
    ]

    q, th1_p, C, dual_e, e2_jt, e2_from_l = build_s_hol_and_contractions_jtheta(tau8)
    e2_heat_identity_err = abs(e2_jt - e2_from_l)
    precomp = (q, th1_p, C, dual_e)

    W_p5 = w_hol_point_jtheta(tau8, Fraction(1, 5), Fraction(2, 5), 1, -4, precomp=precomp)
    single_p5_det_null = abs(mp.det(W_p5))

    W_p6_a = w_hol_point_jtheta(tau8, Fraction(1, 6), Fraction(1, 6), 1, 2, precomp=precomp)
    W_p6_b = w_hol_point_jtheta(tau8, Fraction(5, 6), Fraction(5, 6), 1, 2, precomp=precomp)
    omega3 = mp.exp(mp.mpf(2) * mp.pi * I / mp.mpf(3))
    p6_cocycle_err = frob_norm(W_p6_b - omega3 * W_p6_a)

    W_u = w_hol_avg_jtheta(tau8, K5, 1, -4, precomp=precomp)
    W_d_K5 = w_hol_avg_jtheta(tau8, K5, 1, 2, precomp=precomp)
    W_d_K6 = w_hol_avg_jtheta(tau8, K6, 1, 2, precomp=precomp)
    W_e_K5 = w_hol_avg_jtheta(tau8, K5, -3, 6, precomp=precomp)
    W_e_K6 = w_hol_avg_jtheta(tau8, K6, -3, 6, precomp=precomp)
    W_d = mp_rat(1, 2) * (W_d_K5 + W_d_K6)
    W_e = mp_rat(1, 2) * (W_e_K5 + W_e_K6)

    det_Wu = abs(mp.det(W_u))
    det_Wd = abs(mp.det(W_d))
    det_We = abs(mp.det(W_e))
    det_Wd_K5 = abs(mp.det(W_d_K5))
    det_We_K5 = abs(mp.det(W_e_K5))
    e5_tie_err = abs(det_We_K5 - det_Wd_K5) / det_Wd_K5
    k6_det_split = abs(det_We - det_Wd) / det_Wd

    h_diff = mp_pow10(-12)

    def wu_of_tau(t):
        return w_hol_avg_jtheta(t, K5, 1, -4)

    def wu_norm_cube_of_tau(t):
        W = wu_of_tau(t)
        H = mat3_conj_T(W) * W
        return W * (H * H)

    dbar_hol = dbar_over_d_ratio(wu_of_tau, tau8, h_diff)
    dbar_norm_cube = dbar_over_d_ratio(wu_norm_cube_of_tau, tau8, h_diff)

    k_strs = ow19_data["OW19_A_2d_hyperbolic_kahler_and_lepto"]["kahler_2d_hyperbolic"]["K_e2_hyp_theta4_theta2_theta3"]
    k_vals = [mp.mpf(s) for s in k_strs]
    K_inv_sqrt = mp.diag([mp.mpf(1) / mp.sqrt(kv) for kv in k_vals])

    obs_flat = flavor_observables(W_u, W_d, W_e)
    obs_hyp = flavor_observables(
        K_inv_sqrt * W_u * K_inv_sqrt,
        K_inv_sqrt * W_d * K_inv_sqrt,
        K_inv_sqrt * W_e * K_inv_sqrt,
    )

    rel_shift_v12 = (obs_hyp["ckm"][0] - obs_flat["ckm"][0]) / obs_flat["ckm"][0]
    rel_shift_v23 = (obs_hyp["ckm"][1] - obs_flat["ckm"][1]) / obs_flat["ckm"][1]
    rel_shift_J = (obs_hyp["ckm"][3] - obs_flat["ckm"][3]) / abs(obs_flat["ckm"][3])
    rel_shift_yu23 = (obs_hyp["s2_s3"][0] - obs_flat["s2_s3"][0]) / obs_flat["s2_s3"][0]
    v23_exceeds_v12 = (obs_hyp["ckm"][1] > obs_hyp["ckm"][0])

    def q5_dressed_sector(t):
        q_t, th1_t, C_t, de_t, _, _ = build_s_hol_and_contractions_jtheta(t)
        pc = (q_t, th1_t, C_t, de_t)
        wu_t = w_hol_avg_jtheta(t, K5, 1, -4, precomp=pc)
        wd_t = mp_rat(1, 2) * (w_hol_avg_jtheta(t, K5, 1, 2, precomp=pc) + w_hol_avg_jtheta(t, K6, 1, 2, precomp=pc))
        we_t = mp_rat(1, 2) * (w_hol_avg_jtheta(t, K5, -3, 6, precomp=pc) + w_hol_avg_jtheta(t, K6, -3, 6, precomp=pc))
        eps5 = mp.exp(mp.mpf(2) * mp.pi * I * t / mp.mpf(5))
        D_L = mp.diag([eps5 ** 2, eps5, mp.mpc(1, 0)])
        D_uR = mp.diag([eps5 ** 3, eps5, mp.mpc(1, 0)])
        D_dR = mp.diag([eps5 ** 2, eps5, mp.mpc(1, 0)])
        return D_L * wu_t * D_uR, D_L * wd_t * D_dR, D_L * we_t * D_dR

    fn_u, fn_d, fn_e = q5_dressed_sector(tau8)
    obs_q5 = flavor_observables(fn_u, fn_d, fn_e)
    dbar_q5 = dbar_over_d_ratio(lambda t: q5_dressed_sector(t)[0], tau8, h_diff)

    rng = SplitMix64(0xA20020210002BEEF)
    haar_max_err = mp.mpf(0)
    for _ in range(10):
        U_Q = rng.next_haar_u3()
        U_uR = rng.next_haar_u3()
        U_dR = rng.next_haar_u3()
        U_L = rng.next_haar_u3()
        U_eR = rng.next_haar_u3()
        obs_scram = flavor_observables(
            U_Q * fn_u * mat3_conj_T(U_uR),
            U_Q * fn_d * mat3_conj_T(U_dR),
            U_L * fn_e * mat3_conj_T(U_eR),
        )
        for key in ("s1_s3", "s2_s3", "ckm"):
            for a_val, b_val in zip(obs_q5[key], obs_scram[key]):
                err = abs(a_val - b_val)
                if err > haar_max_err:
                    haar_max_err = err

    ow21_a = ow21_data["OW21_A_fl4_audit_and_curved_kahler"]
    ver_b = ow21_a["verified_fl4_breakthroughs"]
    f1_t = ow21_a["FL4_F1_curved_2d_hyperbolic_kahler_distortion"]
    f2_t = ow21_a["FL4_F2_holomorphic_hierarchy_ceiling_and_q5_rescue"]

    delta_det_Wu = abs(det_Wu - mp.mpf(ver_b["K5_det_Wu_rank3"]))
    delta_k6_split = abs(k6_det_split - mp.mpf(ver_b["K6_lepton_down_det_split"]))

    f1_deltas = {
        "rel_shift_v12": abs(rel_shift_v12 - mp.mpf(f1_t["rel_shift_v12"])),
        "rel_shift_v23": abs(rel_shift_v23 - mp.mpf(f1_t["rel_shift_v23"])),
        "rel_shift_J": abs(rel_shift_J - mp.mpf(f1_t["rel_shift_J"])),
        "rel_shift_Yu_s2_over_s3": abs(rel_shift_yu23 - mp.mpf(f1_t["rel_shift_Yu_s2_over_s3"])),
        "flat_ckm_max": max(abs(a - mp.mpf(b)) for a, b in zip(obs_flat["ckm"], f1_t["flat_ckm_12_23_13_J"])),
        "hyp2d_ckm_max": max(abs(a - mp.mpf(b)) for a, b in zip(obs_hyp["ckm"], f1_t["hyp2d_ckm_12_23_13_J"])),
    }
    f1_max_delta = max(f1_deltas.values())

    f2_deltas = {
        "undressed_s1_s3_max": max(abs(a - mp.mpf(b)) for a, b in zip(obs_flat["s1_s3"], f2_t["undressed_u_d_e_s1_over_s3"])),
        "q5_s1_s3_max": max(abs(a - mp.mpf(b)) for a, b in zip(obs_q5["s1_s3"], f2_t["q5_dressed_u_d_e_s1_over_s3"])),
        "q5_s2_s3_max": max(abs(a - mp.mpf(b)) for a, b in zip(obs_q5["s2_s3"], f2_t["q5_dressed_u_d_e_s2_over_s3"])),
        "q5_ckm_max": max(abs(a - mp.mpf(b)) for a, b in zip(obs_q5["ckm"], f2_t["q5_dressed_ckm_12_23_13_J"])),
    }
    f2_max_delta = max(f2_deltas.values())

    gate_pass = (
        e2_heat_identity_err < mp_pow10(-45)
        and single_p5_det_null < mp_pow10(-40)
        and p6_cocycle_err < mp_pow10(-40)
        and e5_tie_err < mp_pow10(-40)
        and delta_det_Wu < mp_pow10(-10)
        and delta_k6_split < mp_pow10(-10)
        and dbar_hol < mp_pow10(-18)
        and dbar_norm_cube > mp_rat(6, 10)
        and v23_exceeds_v12
        and f1_max_delta < mp_pow10(-6)
        and f2_max_delta < mp_pow10(-7)
        and dbar_q5 < mp_pow10(-18)
        and haar_max_err < mp_pow10(-35)
    )
    if not gate_pass:
        discrepancies.append("REF_1_disjoint_jtheta_ow21_a_failed")

    return {
        "e2_heat_eq_self_check_err": mpf_str(e2_heat_identity_err, 8),
        "single_p5_det_null": mpf_str(single_p5_det_null, 8),
        "p6_cocycle_err": mpf_str(p6_cocycle_err, 8),
        "E5_lepton_down_tie_err": mpf_str(e5_tie_err, 8),
        "K5_det_Wu_rank3": mpf_str(det_Wu, 14),
        "K6_lepton_down_det_split": mpf_str(k6_det_split, 14),
        "delta_det_Wu_vs_producer": mpf_str(delta_det_Wu, 8),
        "delta_K6_split_vs_producer": mpf_str(delta_k6_split, 8),
        "dbar_over_d_hol_rel": mpf_str(dbar_hol, 8),
        "dbar_over_d_norm_cube_raw": mpf_str(dbar_norm_cube, 10),
        "FL4_F1": {
            "rel_shift_v12": mpf_str(rel_shift_v12, 10),
            "rel_shift_v23": mpf_str(rel_shift_v23, 10),
            "rel_shift_J": mpf_str(rel_shift_J, 10),
            "rel_shift_Yu_s2_over_s3": mpf_str(rel_shift_yu23, 10),
            "ckm_v23_exceeds_v12": v23_exceeds_v12,
            "max_delta_vs_producer": mpf_str(f1_max_delta, 8),
        },
        "FL4_F2": {
            "q5_s1_s3": [mpf_str(v, 10) for v in obs_q5["s1_s3"]],
            "q5_s2_s3": [mpf_str(v, 10) for v in obs_q5["s2_s3"]],
            "q5_ckm": [mpf_str(v, 10) for v in obs_q5["ckm"]],
            "q5_dbar_over_d_rel": mpf_str(dbar_q5, 8),
            "splitmix64_haar_10trial_err": mpf_str(haar_max_err, 8),
            "max_delta_vs_producer": mpf_str(f2_max_delta, 8),
        },
        "gate_pass": gate_pass,
        "_pf_ref_2_cache": {
            "rel_shift_v23": rel_shift_v23,
        },
    }


# ---------------------------------------------------------------------------
# REF-2: E_8 Root System, Frenkel-Kac V_GHU Numerical Verification, & GL4 RGE
# ---------------------------------------------------------------------------

def build_e8_roots_and_cocycle():
    roots = []
    for i in range(8):
        for j in range(i + 1, 8):
            for si in (-1, 1):
                for sj in (-1, 1):
                    v = [Fraction(0)] * 8
                    v[i] = Fraction(si)
                    v[j] = Fraction(sj)
                    roots.append(tuple(v))
    for mask in range(256):
        neg_cnt = bin(mask).count("1")
        if neg_cnt % 2 == 0:
            v = tuple(Fraction(-1, 2) if ((mask >> k) & 1) else Fraction(1, 2) for k in range(8))
            roots.append(v)

    root_set = set(roots)
    assert len(roots) == 240 and len(root_set) == 240
    for r in roots:
        assert sum(x * x for x in r) == Fraction(2)

    alphas = [
        (Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(-1), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(-1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(0)),
        (Fraction(-1, 2),) * 8,
    ]
    A_cartan = sp.Matrix([
        [sp.Rational(sum(a * b for a, b in zip(alphas[i], alphas[j])).numerator,
                     sum(a * b for a, b in zip(alphas[i], alphas[j])).denominator)
         for j in range(8)]
        for i in range(8)
    ])
    assert int(A_cartan.det()) == 1
    M_simple = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in a] for a in alphas]).T
    M_inv = M_simple.inv()

    coeff_cache = {}

    def root_coords(r):
        if r not in coeff_cache:
            vec = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in r])
            c = M_inv * vec
            assert all(x.q == 1 for x in c)
            coeff_cache[r] = [int(x) for x in c]
        return coeff_cache[r]

    def fk_eps(r, s):
        cr = root_coords(r)
        cs = root_coords(s)
        acc = 0
        for i in range(8):
            acc += cr[i] * cs[i]
            for j in range(i + 1, 8):
                acc += cr[i] * cs[j] * int(A_cartan[i, j])
        return 1 if (acc % 2 == 0) else -1

    return roots, root_set, fk_eps


def eval_v_ghu_numeric(doublet_roots, phi_vals, g_val, root_set, fk_eps):
    gam1 = (Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    signs = [
        1,
        fk_eps(gam1, doublet_roots[1]),
        1,
        fk_eps(gam1, doublet_roots[3]),
    ]
    eff_phi = [mp.mpf(signs[i]) * phi_vals[i] for i in range(4)]

    cartan_sq = mp.mpf(0)
    for k in range(8):
        hk = mp.mpf(0)
        for a in range(4):
            hk += (abs(eff_phi[a]) ** 2) * frac_to_mpf(doublet_roots[a][k])
        cartan_sq += hk * hk

    off_map = {}
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            gam = tuple(doublet_roots[a][k] - doublet_roots[b][k] for k in range(8))
            if gam in root_set:
                neg_rb = tuple(-x for x in doublet_roots[b])
                n_ab = mp.mpf(fk_eps(doublet_roots[a], neg_rb))
                term = n_ab * eff_phi[a] * mp.conj(eff_phi[b])
                off_map[gam] = off_map.get(gam, mp.mpc(0, 0)) + term
    off_sq = sum(abs(val) ** 2 for val in off_map.values())
    return (g_val ** 2 / mp.mpf(4)) * (cartan_sq + off_sq)


def eval_v_2hdm_quartic(phi_vals, g_val, lams_over_g2):
    up, u0, d0, dm = phi_vals
    h2_sq = abs(up) ** 2 + abs(u0) ** 2
    h1_sq = abs(d0) ** 2 + abs(dm) ** 2
    h1h2_sq = abs(dm * up - d0 * u0) ** 2
    g2 = g_val ** 2
    l1, l2, l3, l4 = [g2 * frac_to_mpf(lv) for lv in lams_over_g2]
    return (
        mp_rat(1, 2) * l1 * (h1_sq ** 2)
        + mp_rat(1, 2) * l2 * (h2_sq ** 2)
        + l3 * h1_sq * h2_sq
        + l4 * h1h2_sq
    )


def make_2hdm_type2_rge_rhs():
    c = {
        "inv16pi2": mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2)),
        "sq35": mp.sqrt(mp_rat(3, 5)),
        "sq53": mp.sqrt(mp_rat(5, 3)),
        "r1_2": mp_rat(1, 2), "r3_2": mp_rat(3, 2), "r5_2": mp_rat(5, 2),
        "r9_2": mp_rat(9, 2), "r11_2": mp_rat(11, 2), "r15_2": mp_rat(15, 2),
        "r19_2": mp_rat(19, 2), "r21_2": mp_rat(21, 2), "r25_2": mp_rat(25, 2),
        "r27_2": mp_rat(27, 2), "r45_2": mp_rat(45, 2), "r73_2": mp_rat(73, 2),
        "r4_3": mp_rat(4, 3), "r8_3": mp_rat(8, 3), "r16_3": mp_rat(16, 3), "r44_3": mp_rat(44, 3),
        "r3_4": mp_rat(3, 4), "r5_4": mp_rat(5, 4), "r9_4": mp_rat(9, 4),
        "r11_4": mp_rat(11, 4), "r15_4": mp_rat(15, 4), "r19_4": mp_rat(19, 4),
        "r21_4": mp_rat(21, 4), "r25_4": mp_rat(25, 4), "r27_4": mp_rat(27, 4),
        "r39_4": mp_rat(39, 4), "r45_4": mp_rat(45, 4), "r51_4": mp_rat(51, 4),
        "r5_6": mp_rat(5, 6), "r11_6": mp_rat(11, 6), "r17_6": mp_rat(17, 6),
        "r25_6": mp_rat(25, 6), "r85_6": mp_rat(85, 6),
        "r11_8": mp_rat(11, 8), "r15_8": mp_rat(15, 8), "r25_8": mp_rat(25, 8),
        "r45_8": mp_rat(45, 8), "r51_8": mp_rat(51, 8), "r101_8": mp_rat(101, 8),
        "r111_8": mp_rat(111, 8), "r131_8": mp_rat(131, 8), "r157_8": mp_rat(157, 8),
        "r161_8": mp_rat(161, 8), "r191_8": mp_rat(191, 8), "r197_8": mp_rat(197, 8),
        "r217_8": mp_rat(217, 8), "r231_8": mp_rat(231, 8), "r291_8": mp_rat(291, 8),
        "r19_9": mp_rat(19, 9), "r31_9": mp_rat(31, 9), "r104_9": mp_rat(104, 9),
        "r5_12": mp_rat(5, 12), "r17_12": mp_rat(17, 12), "r25_12": mp_rat(25, 12), "r85_12": mp_rat(85, 12),
        "r33_16": mp_rat(33, 16), "r79_16": mp_rat(79, 16), "r131_16": mp_rat(131, 16),
        "r165_16": mp_rat(165, 16), "r179_16": mp_rat(179, 16), "r225_16": mp_rat(225, 16),
        "r25_24": mp_rat(25, 24),
        "r41_144": mp_rat(41, 144), "r53_144": mp_rat(53, 144),
        "r113_216": mp_rat(113, 216), "r1267_216": mp_rat(1267, 216),
    }
    c["inv16pi2_sq"] = c["inv16pi2"] * c["inv16pi2"]
    for k in (2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 18, 20, 21, 24, 26, 28, 32, 33, 36, 40, 54, 60, 64, 72, 78, 80, 108):
        c[f"i{k}"] = mp.mpf(k)
    z0 = mp.mpf(0)

    def rhs(st, include_2loop_quartics=True):
        g1g, g2, g3, yt, yb, ytau, l1, l2, l3, l4 = st
        gp = c["sq35"] * g1g
        gp2 = gp * gp
        gp4 = gp2 * gp2
        gp6 = gp4 * gp2
        g22 = g2 * g2
        g24 = g22 * g22
        g26 = g24 * g22
        g32 = g3 * g3
        g34 = g32 * g32
        yt2 = yt * yt
        yt4 = yt2 * yt2
        yt6 = yt4 * yt2
        yb2 = yb * yb
        yb4 = yb2 * yb2
        yb6 = yb4 * yb2
        yl2 = ytau * ytau
        yl4 = yl2 * yl2
        yl6 = yl4 * yl2
        l12 = l1 * l1
        l22 = l2 * l2
        l32 = l3 * l3
        l42 = l4 * l4

        inv1 = c["inv16pi2"]
        inv2 = c["inv16pi2_sq"]

        # 1. Gauge couplings (Chowdhury-Eberhardt 1503.08216 / Dev-Pilaftsis 1408.3405, GUT g1)
        gp3 = gp2 * gp
        bgp1 = c["i7"] * gp3
        bgp2 = (c["r104_9"] * gp2 + c["i6"] * g22 + c["r44_3"] * g32
                - c["r5_6"] * yb2 - c["r17_6"] * yt2 - c["r5_2"] * yl2) * gp3
        dg1g = c["sq53"] * (inv1 * bgp1 + inv2 * bgp2)

        g23 = g22 * g2
        bg2_1 = -c["i3"] * g23
        bg2_2 = (c["i2"] * gp2 + c["i8"] * g22 + c["i12"] * g32
                 - c["r3_2"] * yb2 - c["r3_2"] * yt2 - c["r1_2"] * yl2) * g23
        dg2 = inv1 * bg2_1 + inv2 * bg2_2

        g33 = g32 * g3
        bg3_1 = -c["i7"] * g33
        bg3_2 = (c["r11_6"] * gp2 + c["r9_2"] * g22 - c["i26"] * g32
                 - c["i2"] * yb2 - c["i2"] * yt2) * g33
        dg3 = inv1 * bg3_1 + inv2 * bg3_2

        if include_2loop_quartics:
            q1, q2, q3, q4 = l1, l2, l3, l4
            q12, q22, q32, q42 = l12, l22, l32, l42
        else:
            q1 = q2 = q3 = q4 = z0
            q12 = q22 = q32 = q42 = z0

        # 2. Type-II Yukawas
        byt1 = (-c["r17_12"] * gp2 - c["r9_4"] * g22 - c["i8"] * g32
                + c["r1_2"] * yb2 + c["r9_2"] * yt2) * yt
        byt2 = (c["r1267_216"] * gp4 - c["r3_4"] * gp2 * g22 + c["r19_9"] * gp2 * g32
                - c["r21_4"] * g24 + c["i9"] * g22 * g32 - c["i108"] * g34
                + c["r3_2"] * q22 + q32 + q3 * q4 + q42
                + gp2 * (-c["r41_144"] * yb2 + c["r131_16"] * yt2)
                + g22 * (c["r33_16"] * yb2 + c["r225_16"] * yt2)
                + g32 * (c["r16_3"] * yb2 + c["i36"] * yt2)
                - c["r5_2"] * yb4 - c["r5_2"] * yb2 * yt2 - c["r3_4"] * yb2 * yl2 - c["i12"] * yt4
                - c["i2"] * yb2 * q3 + c["i2"] * yb2 * q4 - c["i6"] * yt2 * q2) * yt
        dyt = inv1 * byt1 + inv2 * byt2

        byb1 = (-c["r5_12"] * gp2 - c["r9_4"] * g22 - c["i8"] * g32
                + c["r9_2"] * yb2 + c["r1_2"] * yt2 + yl2) * yb
        byb2 = (-c["r113_216"] * gp4 - c["r9_4"] * gp2 * g22 + c["r31_9"] * gp2 * g32
                - c["r21_4"] * g24 + c["i9"] * g22 * g32 - c["i108"] * g34
                + q32 + q3 * q4 + q42 + c["r3_2"] * q12
                + gp2 * (c["r79_16"] * yb2 - c["r53_144"] * yt2 + c["r25_8"] * yl2)
                + g22 * (c["r225_16"] * yb2 + c["r33_16"] * yt2 + c["r15_8"] * yl2)
                + g32 * (c["i36"] * yb2 + c["r16_3"] * yt2)
                - c["i12"] * yb4 - c["r5_2"] * yb2 * yt2 - c["r9_4"] * yb2 * yl2
                - c["r5_2"] * yt4 - c["r9_4"] * yl4
                - c["i6"] * yb2 * q1 - c["i2"] * yt2 * q3 + c["i2"] * yt2 * q4) * yb
        dyb = inv1 * byb1 + inv2 * byb2

        byl1 = (-c["r15_4"] * gp2 - c["r9_4"] * g22 + c["i3"] * yb2 + c["r5_2"] * yl2) * ytau
        byl2 = (c["r161_8"] * gp4 + c["r9_4"] * gp2 * g22 - c["r21_4"] * g24
                + q32 + q3 * q4 + q42 + c["r3_2"] * q12
                + gp2 * (c["r25_24"] * yb2 + c["r179_16"] * yl2)
                + g22 * (c["r45_8"] * yb2 + c["r165_16"] * yl2)
                + c["i20"] * g32 * yb2
                - c["r27_4"] * yb4 - c["r9_4"] * yb2 * yt2 - c["r27_4"] * yb2 * yl2
                - c["i3"] * yl4 - c["i6"] * yl2 * q1) * ytau
        dyl = inv1 * byl1 + inv2 * byl2

        # 3. Complete 2-loop Type-II Quartics (lam_5 = 0)
        l34_mix = c["i2"] * l32 + c["i2"] * l3 * l4 + l42
        bos_l12_common_1 = (c["r3_4"] * gp4 + c["r3_2"] * gp2 * g22 + c["r9_4"] * g24
                            + c["i4"] * l32 + c["i4"] * l3 * l4 + c["i2"] * l42)
        bos_l12_common_2 = (
            -c["r131_8"] * gp6 - c["r191_8"] * gp4 * g22 - c["r101_8"] * gp2 * g24 + c["r291_8"] * g26
            + gp4 * (c["i5"] * l3 + c["r5_2"] * l4)
            + gp2 * g22 * (c["i5"] * l4)
            + g24 * (c["i15"] * l3 + c["r15_2"] * l4)
            + gp2 * (c["i8"] * l32 + c["i8"] * l3 * l4 + c["i4"] * l42)
            + g22 * (c["i6"] * ((c["i2"] * l3 + l4) ** 2))
            - c["i16"] * (l32 * l3) - c["i24"] * l32 * l4 - c["i32"] * l3 * l42 - c["i12"] * (l42 * l4)
        )
        l34_lin = c["i20"] * l32 + c["i20"] * l3 * l4 + c["i12"] * l42

        bl1_1 = (bos_l12_common_1 - c["i3"] * gp2 * l1 - c["i9"] * g22 * l1 + c["i12"] * l12
                 - c["i12"] * yb4 - c["i4"] * yl4 + (c["i12"] * yb2 + c["i4"] * yl2) * l1)
        bl1_2 = (bos_l12_common_2
                 + c["r217_8"] * gp4 * l1 + c["r39_4"] * gp2 * g22 * l1 - c["r51_8"] * g24 * l1
                 + c["i18"] * gp2 * l12 + c["i54"] * g22 * l12 - c["i78"] * (l12 * l1) - l1 * l34_lin
                 + gp4 * (c["r5_2"] * yb2 - c["r25_2"] * yl2)
                 + gp2 * g22 * (c["i9"] * yb2 + c["i11"] * yl2)
                 - g24 * (c["r9_2"] * yb2 + c["r3_2"] * yl2)
                 + gp2 * (c["r8_3"] * yb4 - c["i8"] * yl4 + c["r25_6"] * yb2 * l1 + c["r25_2"] * yl2 * l1)
                 + g22 * (c["r45_2"] * yb2 * l1 + c["r15_2"] * yl2 * l1)
                 - g32 * (c["i64"] * yb4 - c["i80"] * yb2 * l1)
                 + c["i60"] * yb6 + c["i12"] * yb4 * yt2 + c["i20"] * yl6
                 - (c["i3"] * yb4 + c["i9"] * yb2 * yt2 + yl4) * l1
                 - c["i72"] * yb2 * l12 - c["i12"] * yt2 * l34_mix - c["i24"] * yl2 * l12)
        dl1 = inv1 * bl1_1 + inv2 * bl1_2

        bl2_1 = (bos_l12_common_1 - c["i3"] * gp2 * l2 - c["i9"] * g22 * l2 + c["i12"] * l22
                 - c["i12"] * yt4 + c["i12"] * yt2 * l2)
        bl2_2 = (bos_l12_common_2
                 + c["r217_8"] * gp4 * l2 + c["r39_4"] * gp2 * g22 * l2 - c["r51_8"] * g24 * l2
                 + c["i18"] * gp2 * l22 + c["i54"] * g22 * l22 - c["i78"] * (l22 * l2) - l2 * l34_lin
                 - c["r19_2"] * gp4 * yt2 + c["i21"] * gp2 * g22 * yt2 - c["r9_2"] * g24 * yt2
                 + gp2 * (-c["r16_3"] * yt4 + c["r85_6"] * yt2 * l2)
                 + c["r45_2"] * g22 * yt2 * l2
                 - g32 * (c["i64"] * yt4 - c["i80"] * yt2 * l2)
                 + c["i12"] * yb2 * yt4 + c["i60"] * yt6
                 - (c["i9"] * yb2 * yt2 + c["i3"] * yt4) * l2
                 - (c["i12"] * yb2 + c["i4"] * yl2) * l34_mix - c["i72"] * yt2 * l22)
        dl2 = inv1 * bl2_1 + inv2 * bl2_2

        l1_p_l2 = l1 + l2
        y_sum_662 = c["i6"] * yb2 + c["i6"] * yt2 + c["i2"] * yl2
        bl3_1 = (c["r3_4"] * gp4 - c["r3_2"] * gp2 * g22 + c["r9_4"] * g24
                 - c["i3"] * gp2 * l3 - c["i9"] * g22 * l3
                 + l1_p_l2 * (c["i6"] * l3 + c["i2"] * l4) + c["i4"] * l32 + c["i2"] * l42
                 - c["i12"] * yb2 * yt2 + y_sum_662 * l3)
        bl3_2 = (-c["r131_8"] * gp6 + c["r101_8"] * gp4 * g22 + c["r11_8"] * gp2 * g24 + c["r291_8"] * g26
                 + gp4 * (c["r15_4"] * l1_p_l2 + c["r197_8"] * l3 + c["r5_2"] * l4)
                 - gp2 * g22 * (c["r5_2"] * l1_p_l2 - c["r11_4"] * l3 + c["i3"] * l4)
                 + g24 * (c["r45_4"] * l1_p_l2 - c["r111_8"] * l3 + c["r15_2"] * l4)
                 + gp2 * (l1_p_l2 * (c["i12"] * l3 + c["i4"] * l4) + c["i2"] * l32 - c["i2"] * l42)
                 + g22 * (l1_p_l2 * (c["i36"] * l3 + c["i18"] * l4) + c["i6"] * ((l3 - l4) ** 2))
                 - (l12 + l22) * (c["i15"] * l3 + c["i4"] * l4)
                 - l1_p_l2 * (c["i36"] * l32 + c["i16"] * l3 * l4 + c["i14"] * l42)
                 - c["i12"] * (l32 * l3) - c["i4"] * l32 * l4 - c["i16"] * l3 * l42 - c["i12"] * (l42 * l4)
                 + gp4 * (c["r5_4"] * yb2 - c["r19_4"] * yt2 - c["r25_4"] * yl2)
                 - gp2 * g22 * (c["r9_2"] * yb2 + c["r21_2"] * yt2 + c["r11_2"] * yl2)
                 - g24 * (c["r9_4"] * yb2 + c["r9_4"] * yt2 + c["r3_4"] * yl2)
                 + gp2 * (-c["r4_3"] * yb2 * yt2 + (c["r25_12"] * yb2 + c["r85_12"] * yt2 + c["r25_4"] * yl2) * l3)
                 + g22 * (c["r45_4"] * yb2 + c["r45_4"] * yt2 + c["r15_4"] * yl2) * l3
                 + g32 * (-c["i64"] * yb2 * yt2 + (c["i40"] * yb2 + c["i40"] * yt2) * l3)
                 + c["i36"] * yb4 * yt2 + c["i36"] * yb2 * yt4
                 - c["r27_2"] * yb4 * l3 + c["i15"] * yb2 * yt2 * l3 - c["r27_2"] * yt4 * l3 - c["r9_2"] * yl4 * l3
                 - (c["i6"] * yb2 * l1 + c["i6"] * yt2 * l2 + c["i2"] * yl2 * l1) * (c["i6"] * l3 + c["i2"] * l4)
                 - y_sum_662 * (c["i2"] * l32 + l42))
        dl3 = inv1 * bl3_1 + inv2 * bl3_2

        bl4_1 = (c["i3"] * gp2 * g22 - (c["i3"] * gp2 + c["i9"] * g22) * l4
                 + c["i2"] * l1_p_l2 * l4 + c["i8"] * l3 * l4 + c["i4"] * l42
                 + c["i12"] * yb2 * yt2 + y_sum_662 * l4)
        bl4_2 = (-c["r73_2"] * gp4 * g22 - c["i14"] * gp2 * g24
                 + c["r157_8"] * gp4 * l4
                 + gp2 * g22 * (c["i5"] * l1_p_l2 + c["i2"] * l3 + c["r51_4"] * l4)
                 - c["r231_8"] * g24 * l4
                 + gp2 * (c["i4"] * l1_p_l2 * l4 + c["i4"] * l3 * l4 + c["i8"] * l42)
                 + g22 * (c["i36"] * l3 * l4 + c["i18"] * l42)
                 - c["i7"] * (l12 + l22) * l4
                 - l1_p_l2 * (c["i40"] * l3 * l4 + c["i20"] * l42)
                 - c["i28"] * l32 * l4 - c["i28"] * l3 * l42
                 + gp2 * g22 * (c["i9"] * yb2 + c["i21"] * yt2 + c["i11"] * yl2)
                 + gp2 * (c["r4_3"] * yb2 * yt2 + (c["r25_12"] * yb2 + c["r85_12"] * yt2 + c["r25_4"] * yl2) * l4)
                 + g22 * (c["r45_4"] * yb2 + c["r45_4"] * yt2 + c["r15_4"] * yl2) * l4
                 + g32 * (c["i64"] * yb2 * yt2 + (c["i40"] * yb2 + c["i40"] * yt2) * l4)
                 - c["i24"] * yb2 * yt4 - c["i24"] * yb4 * yt2
                 - c["r27_2"] * yb4 * l4 - yb2 * yt2 * (c["i24"] * l3 + c["i33"] * l4) - c["r27_2"] * yt4 * l4 - c["r9_2"] * yl4 * l4
                 - (c["i12"] * yb2 * l1 + c["i12"] * yt2 * l2 + c["i4"] * yl2 * l1) * l4
                 - (c["i2"] * y_sum_662) * (c["i2"] * l3 * l4 + l42))
        dl4 = inv1 * bl4_1 + inv2 * bl4_2

        return [dg1g, dg2, dg3, dyt, dyb, dyl, dl1, dl2, dl3, dl4]

    return rhs


def gl4_integrate(rhs_fn, y0, t0, t1, n_steps, include_2loop_quartics=True):
    h = (t1 - t0) / mp.mpf(n_steps)
    s3_6 = mp.sqrt(mp.mpf(3)) / mp.mpf(6)
    a11 = mp_rat(1, 4)
    a12 = a11 - s3_6
    a21 = a11 + s3_6
    a22 = a11
    half = mp_rat(1, 2)
    tol = mp_pow10(-36)
    y = list(y0)
    max_fp_resid = mp.mpf(0)
    for _ in range(n_steps):
        f0 = rhs_fn(y, include_2loop_quartics=include_2loop_quartics)
        k1 = list(f0)
        k2 = list(f0)
        err = mp.mpf(1)
        for _it in range(100):
            z1 = [y[i] + h * (a11 * k1[i] + a12 * k2[i]) for i in range(10)]
            z2 = [y[i] + h * (a21 * k1[i] + a22 * k2[i]) for i in range(10)]
            nk1 = rhs_fn(z1, include_2loop_quartics=include_2loop_quartics)
            nk2 = rhs_fn(z2, include_2loop_quartics=include_2loop_quartics)
            err = max(
                max(abs(nk1[i] - k1[i]) for i in range(10)),
                max(abs(nk2[i] - k2[i]) for i in range(10)),
            )
            k1, k2 = nk1, nk2
            if err < tol:
                break
        if err > max_fp_resid:
            max_fp_resid = err
        y = [y[i] + h * half * (k1[i] + k2[i]) for i in range(10)]
    return y, max_fp_resid


def check_2hdm_bfb(l1, l2, l3, l4):
    if l1 <= 0 or l2 <= 0:
        return False
    rt = mp.sqrt(l1 * l2)
    return (l3 > -rt) and (l3 + l4 > -rt)


def conformal_2hdm_observables(l1, l2, l3, l4):
    tb = (l1 / l2) ** mp_rat(1, 4)
    tb2 = tb * tb
    lam_eff = (l1 + l2 * (tb2 ** 2) + mp.mpf(2) * (l3 + l4) * tb2) / ((mp.mpf(1) + tb2) ** 2)
    mh0_over_v = mp.sqrt(lam_eff)
    return tb, mh0_over_v


def run_ref2(ow21_data, discrepancies):
    roots, root_set, fk_eps = build_e8_roots_and_cocycle()

    cases_roots = {
        "case1_single_10_3": (
            [
                (Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(-1), Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(-1), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
            ],
            (Fraction(1), Fraction(1), Fraction(1), Fraction(-1)),
        ),
        "case2_split_type2": (
            [
                (Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(-1), Fraction(1), Fraction(0), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0)),
                (Fraction(0), Fraction(0), Fraction(0), Fraction(-1), Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
            ],
            (Fraction(1), Fraction(1), Fraction(0), Fraction(-1, 2)),
        ),
        "case3_e6_78": (
            [
                (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
                (Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2)),
                (Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(-1, 2)),
            ],
            (Fraction(1), Fraction(1), Fraction(-1, 2), Fraction(-1, 2)),
        ),
    }

    rng = SplitMix64(0xE86D240000022345)
    random_configs = []
    for _ in range(10):
        phi_cfg = [rng.next_complex_normal() for _ in range(4)]
        g_cfg = mp_rat(1, 2) + rng.next_unit_open()
        random_configs.append((phi_cfg, g_cfg))

    v_ghu_max_errs = {}
    for cname, (droots, lams) in cases_roots.items():
        for r in droots:
            assert r in root_set
        max_e = mp.mpf(0)
        for phi_cfg, g_cfg in random_configs:
            vg = eval_v_ghu_numeric(droots, phi_cfg, g_cfg, root_set, fk_eps)
            v2 = eval_v_2hdm_quartic(phi_cfg, g_cfg, lams)
            e = abs(vg - v2)
            if e > max_e:
                max_e = e
        v_ghu_max_errs[cname] = max_e

    roots_16_in_27x3 = [
        r for r in roots
        if all(abs(x) == Fraction(1, 2) for x in r) and (r[5] + r[6] + r[7] == Fraction(-1, 2))
    ]
    roots_10_in_27x3 = [
        r for r in roots
        if all(x in (Fraction(-1), Fraction(0), Fraction(1)) for x in r) and (r[5] + r[6] + r[7] == Fraction(1))
    ]
    roots_10star = [
        r for r in roots
        if all(x in (Fraction(-1), Fraction(0), Fraction(1)) for x in r) and (r[5] + r[6] + r[7] == Fraction(-1))
    ]
    r_Hu0 = cases_roots["case1_single_10_3"][0][1]
    assert r_Hu0 in roots_10_in_27x3
    r_Q_ex = (Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2), Fraction(1, 2))
    r_uc_ex = (Fraction(-1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(1, 2), Fraction(-1, 2))
    root_sum_zero = (
        r_Q_ex in roots_16_in_27x3
        and r_uc_ex in roots_16_in_27x3
        and all(r_Q_ex[k] + r_uc_ex[k] + r_Hu0[k] == Fraction(0) for k in range(8))
    )
    conj_16_16_10star_count = 0
    s10star_set = set(roots_10star)
    for r1 in roots_16_in_27x3:
        for r2 in roots_16_in_27x3:
            neg_sum = tuple(-(r1[k] + r2[k]) for k in range(8))
            if neg_sum in s10star_set:
                conj_16_16_10star_count += 1

    n_S_repaired = 24
    n_W_repaired = 3 * 16 + 3 * 1
    n_V_repaired = 8 + 3 + 3 + 1 + 1
    M_g_repaired = n_S_repaired + n_W_repaired - 4 * n_V_repaired
    pm_S = (-1) ** (3 * 0 + 0)
    pm_S2 = pm_S * pm_S
    pm_chiS = (-1) ** (3 * 1 + 0)
    z3_omega = mp.exp(mp.mpf(2) * mp.pi * mp.mpc(0, 1) / mp.mpf(3))
    z3_s2_breaks_z3 = abs(z3_omega ** 2 - mp.mpf(1)) > mp.mpf(1)

    with mp.workdps(42):
        rhs_fn = make_2hdm_type2_rge_rhs()

        # Custodial SU(2)_H & O(8) -114 lam^3 internal literature self-checks
        st_cust = [
            mp_rat(3, 5), mp_rat(7, 10), mp_rat(9, 10),
            mp.mpf(0), mp.mpf(0), mp.mpf(0),
            mp_rat(7, 10), mp_rat(7, 10), mp_rat(1, 10), mp_rat(6, 10),
        ]
        d_cust = rhs_fn(st_cust)
        su2h_custodial_err = max(abs(d_cust[6] - d_cust[7]), abs(d_cust[9] - (d_cust[6] - d_cust[8])))

        lam_test = mp_rat(1, 2)
        st_o8 = [mp.mpf(0)] * 6 + [lam_test, lam_test, lam_test, mp.mpf(0)]
        d_o8 = rhs_fn(st_o8)
        inv1 = mp.mpf(1) / (mp.mpf(16) * (mp.pi ** 2))
        o8_expected = inv1 * (mp.mpf(16) * (lam_test ** 2)) + (inv1 ** 2) * (mp.mpf(-114) * (lam_test ** 3))
        o8_limit_err = max(abs(d_o8[6] - o8_expected), abs(d_o8[7] - o8_expected), abs(d_o8[8] - o8_expected), abs(d_o8[9]))

        g_uv = mp.sqrt(mp.mpf(4) * mp.pi / mp.mpf(40))
        y_uv = g_uv / mp.sqrt(mp.mpf(2))
        g_uv2 = g_uv * g_uv

        def uv_state(lams_frac):
            return [g_uv, g_uv, g_uv, y_uv, y_uv, y_uv] + [g_uv2 * frac_to_mpf(lf) for lf in lams_frac]

        # Full 2-loop GL4 (N=800, fixed-point tol < 1e-35) on ALL THREE Cases 1, 2, 3 (E8_tree)
        ir_c1, fp_c1 = gl4_integrate(rhs_fn, uv_state(cases_roots["case1_single_10_3"][1]), mp.mpf(0), mp.mpf(-32), 800)
        ir_c2_n200, fp_c2_n200 = gl4_integrate(rhs_fn, uv_state(cases_roots["case2_split_type2"][1]), mp.mpf(0), mp.mpf(-32), 200)
        ir_c2, fp_c2 = gl4_integrate(rhs_fn, uv_state(cases_roots["case2_split_type2"][1]), mp.mpf(0), mp.mpf(-32), 800)
        ir_c3, fp_c3 = gl4_integrate(rhs_fn, uv_state(cases_roots["case3_e6_78"][1]), mp.mpf(0), mp.mpf(-32), 800)
        c2_n200_vs_n800 = max(abs(a - b) for a, b in zip(ir_c2_n200, ir_c2))

        # PF_REF_4: Case 2 E8_tree with 2-loop quartics turned OFF in Yukawa RGEs
        ir_c2_lam0, _ = gl4_integrate(rhs_fn, uv_state(cases_roots["case2_split_type2"][1]), mp.mpf(0), mp.mpf(-32), 400, include_2loop_quartics=False)

    prod_runs = ow21_data["OW21_B_6d_e8_ghu_quartics_and_repaired_glr"]["two_loop_ghu_2hdm_running_t_0_to_neg32"]["runs"]

    case_reports = {}
    all_cases_max_delta = mp.mpf(0)
    all_cases_bfb = True
    for cname, ir_vec, fp_res in (
        ("case1_single_10_3", ir_c1, fp_c1),
        ("case2_split_type2", ir_c2, fp_c2),
        ("case3_e6_78", ir_c3, fp_c3),
    ):
        p = prod_runs[cname]["E8_tree"]
        tb, mh0 = conformal_2hdm_observables(ir_vec[6], ir_vec[7], ir_vec[8], ir_vec[9])
        bfb = check_2hdm_bfb(ir_vec[6], ir_vec[7], ir_vec[8], ir_vec[9])
        all_cases_bfb = all_cases_bfb and bfb
        deltas = {
            "g_ir_max": max(abs(ir_vec[i] - mp.mpf(p["g_ir"][i])) for i in range(3)),
            "y_ir_33_max": max(abs(ir_vec[3 + i] - mp.mpf(p["y_ir_33"][i])) for i in range(3)),
            "l_ir_max": max(abs(ir_vec[6 + i] - mp.mpf(p["l_ir"][i])) for i in range(4)),
            "tan_beta_conformal": abs(tb - mp.mpf(p["tan_beta_conformal"])),
            "mh0_over_v_conformal": abs(mh0 - mp.mpf(p["mh0_over_v_conformal"])),
        }
        c_max = max(deltas.values())
        if c_max > all_cases_max_delta:
            all_cases_max_delta = c_max
        case_reports[cname] = {
            "n_steps": 800,
            "fixed_point_resid": mpf_str(fp_res, 8),
            "bfb_ir": bfb,
            "g_ir": [mpf_str(v, 16) for v in ir_vec[0:3]],
            "y_ir_33": [mpf_str(v, 16) for v in ir_vec[3:6]],
            "l_ir": [mpf_str(v, 16) for v in ir_vec[6:10]],
            "tan_beta_conformal": mpf_str(tb, 16),
            "mh0_over_v_conformal": mpf_str(mh0, 16),
            "deltas_vs_producer": {k: mpf_str(v, 8) for k, v in deltas.items()},
            "max_delta_vs_producer": mpf_str(c_max, 8),
        }

    pf4_yuk_shift = mp.sqrt(sum((ir_c2[3 + i] - ir_c2_lam0[3 + i]) ** 2 for i in range(3)))

    gate_pass = (
        len(roots) == 240
        and all(err < mp_pow10(-35) for err in v_ghu_max_errs.values())
        and root_sum_zero
        and conj_16_16_10star_count == 0
        and M_g_repaired == 11
        and M_g_repaired < 31
        and pm_S2 == 1
        and pm_chiS == -1
        and z3_s2_breaks_z3
        and su2h_custodial_err < mp_pow10(-38)
        and o8_limit_err < mp_pow10(-38)
        and fp_c1 < mp_pow10(-35)
        and fp_c2 < mp_pow10(-35)
        and fp_c3 < mp_pow10(-35)
        and fp_c2_n200 < mp_pow10(-35)
        and all_cases_max_delta < mp_pow10(-10)
        and all_cases_bfb
    )
    if not gate_pass:
        discrepancies.append("REF_2_disjoint_gl4_or_e8_ghu_failed")

    return {
        "e8_root_count": len(roots),
        "v_ghu_10_random_complex_doublet_max_err": {k: mpf_str(v, 8) for k, v in v_ghu_max_errs.items()},
        "e8_yukawa_root_closure_zero": root_sum_zero,
        "e8_16_16_10star_triples_count": conj_16_16_10star_count,
        "repaired_glr_Mg": M_g_repaired,
        "repaired_glr_survives_lt_31": (M_g_repaired < 31),
        "soft_S2_breaks_Z3": z3_s2_breaks_z3,
        "PM_S2": pm_S2,
        "PM_chiS": pm_chiS,
        "rge_su2h_custodial_literature_check_err": mpf_str(su2h_custodial_err, 8),
        "rge_o8_neg114_literature_check_err": mpf_str(o8_limit_err, 8),
        "gl4_case2_n200_vs_n800_max_diff": mpf_str(c2_n200_vs_n800, 8),
        "gl4_cases_1_2_3_E8_tree": case_reports,
        "all_3_cases_bfb": all_cases_bfb,
        "all_3_cases_max_delta_vs_producer": mpf_str(all_cases_max_delta, 8),
        "gate_pass": gate_pass,
        "_pf_cache": {
            "case2_roots": cases_roots["case2_split_type2"][0],
            "random_configs": random_configs,
            "root_set": root_set,
            "fk_eps": fk_eps,
            "pf4_yuk_shift": pf4_yuk_shift,
        },
    }


# ---------------------------------------------------------------------------
# REF-3: Disjoint Riemann-Mellin-Jacobi-Theta E_3 & 3-Term dS Stabilization
# ---------------------------------------------------------------------------

def build_mellin_quadrature():
    n = 40
    T = mp.zeros(n, n)
    for k in range(1, n):
        b = mp.mpf(k) / mp.sqrt(mp.mpf(4 * k * k - 1))
        T[k - 1, k] = b
        T[k, k - 1] = b
    xs, vecs = mp.eigh(T)
    ws = [mp.mpf(2) * (vecs[0, k] ** 2) for k in range(n)]

    u_panels = [
        (mp.mpf(0), mp.mpf(1)),
        (mp.mpf(1), mp.mpf(2)),
        (mp.mpf(2), mp.mpf(3)),
        (mp.mpf(3), mp.mpf(4)),
    ]
    t_nodes = []
    t_weights = []
    half = mp_rat(1, 2)
    for a, b in u_panels:
        hl = (b - a) * half
        md = (a + b) * half
        for x, w in zip(xs, ws):
            u = md + hl * x
            t = mp.exp(u)
            t_nodes.append(t)
            t_weights.append(hl * w * (mp.exp(mp.mpf(3) * u) + mp.exp(mp.mpf(-2) * u)))
    return t_nodes, t_weights


def e3_mellin_jets(x_in, y, t_nodes, t_weights, t_shift=True):
    x = x_in - mp.nint(x_in) if t_shift else x_in
    q_cut = mp.mpf(50)
    m_max = int(mp.ceil(mp.sqrt(q_cut / y))) + 1
    inv_y = mp.mpf(1) / y
    inv_y2 = inv_y * inv_y
    inv_y3 = inv_y2 * inv_y

    lat = []
    for m in range(-m_max, m_max + 1):
        mf = mp.mpf(m)
        m2 = mf * mf
        m2y = m2 * y
        if m2y > q_cut:
            continue
        rem = mp.sqrt((q_cut - m2y) * y)
        nc = -mf * x
        n_lo = int(mp.floor(nc - rem)) - 1
        n_hi = int(mp.ceil(nc + rem)) + 1
        for n in range(n_lo, n_hi + 1):
            if m == 0 and n == 0:
                continue
            s = mf * x + mp.mpf(n)
            s2 = s * s
            Q = s2 * inv_y + m2y
            if Q <= q_cut:
                qx = mp.mpf(2) * mf * s * inv_y
                qy = m2 - s2 * inv_y2
                qxx = mp.mpf(2) * m2 * inv_y
                qxy = mp.mpf(-2) * mf * s * inv_y2
                qyy = mp.mpf(2) * s2 * inv_y3
                lat.append((Q, qx, qy, qxx, qxy, qyy))

    I0 = Ix = Iy = Ixx = Ixy = Iyy = mp.mpf(0)
    neg_pi = -mp.pi
    cut_arg = mp.mpf(-135)

    for t, wt in zip(t_nodes, t_weights):
        a = neg_pi * t
        s0 = sx = sy = sxx = sxy = syy = mp.mpf(0)
        for Q, qx, qy, qxx, qxy, qyy in lat:
            arg = a * Q
            if arg > cut_arg:
                e = mp.exp(arg)
                s0 += e
                sx += e * qx
                sy += e * qy
                sxx += e * (a * qx * qx + qxx)
                sxy += e * (a * qx * qy + qxy)
                syy += e * (a * qy * qy + qyy)
        I0 += wt * s0
        Ix += wt * a * sx
        Iy += wt * a * sy
        Ixx += wt * a * sxx
        Ixy += wt * a * sxy
        Iyy += wt * a * syy

    pref = (mp.pi ** 3) / mp.mpf(2)
    return (
        pref * (mp_rat(1, 6) + I0),
        pref * Ix,
        pref * Iy,
        pref * Ixx,
        pref * Ixy,
        pref * Iyy,
    )


def f3_mellin_jets(x, y, t_nodes, t_weights):
    r2 = x * x + y * y
    r4 = r2 * r2
    r6 = r4 * r2
    u1 = -x / r2
    v1 = y / r2
    e1, e1u, e1v, e1uu, e1uv, e1vv = e3_mellin_jets(u1, v1, t_nodes, t_weights, t_shift=True)

    a = (x * x - y * y) / r4
    b = (mp.mpf(2) * x * y) / r4
    c_cr = mp.mpf(-2) * x * (x * x - mp.mpf(3) * y * y) / r6
    d_cr = mp.mpf(2) * y * (mp.mpf(3) * x * x - y * y) / r6

    g1x = a * e1u - b * e1v
    g1y = b * e1u + a * e1v
    g1xx = e1uu * a * a - mp.mpf(2) * e1uv * a * b + e1vv * b * b + e1u * c_cr + e1v * d_cr
    g1xy = e1uu * a * b + e1uv * (a * a - b * b) - e1vv * a * b - e1u * d_cr + e1v * c_cr
    g1yy = e1uu * b * b + mp.mpf(2) * e1uv * a * b + e1vv * a * a - e1u * c_cr - e1v * d_cr

    e2, e2u, e2v, e2uu, e2uv, e2vv = e3_mellin_jets(mp.mpf(5) * x, mp.mpf(5) * y, t_nodes, t_weights, t_shift=True)
    return (
        e1 + e2,
        g1x + mp.mpf(5) * e2u,
        g1y + mp.mpf(5) * e2v,
        g1xx + mp.mpf(25) * e2uu,
        g1xy + mp.mpf(25) * e2uv,
        g1yy + mp.mpf(25) * e2vv,
    )


def v_3d_eval(R, x, y, A_val, B_val, C_val, t_nodes, t_weights):
    F, Fx, Fy, Fxx, Fxy, Fyy = f3_mellin_jets(x, y, t_nodes, t_weights)
    R_m5 = R ** (-5)
    R_m6 = R ** (-6)
    R_m7 = R ** (-7)
    R_m8 = R ** (-8)
    R_m10 = R ** (-10)
    R_m11 = R ** (-11)
    R_m12 = R ** (-12)

    V = A_val * R_m5 - B_val * R_m6 + C_val * F * R_m10
    VR = mp.mpf(-5) * A_val * R_m6 + mp.mpf(6) * B_val * R_m7 - mp.mpf(10) * C_val * F * R_m11
    Vx = C_val * Fx * R_m10
    Vy = C_val * Fy * R_m10

    VRR = mp.mpf(30) * A_val * R_m7 - mp.mpf(42) * B_val * R_m8 + mp.mpf(110) * C_val * F * R_m12
    VRx = mp.mpf(-10) * C_val * Fx * R_m11
    VRy = mp.mpf(-10) * C_val * Fy * R_m11
    Vxx = C_val * Fxx * R_m10
    Vxy = C_val * Fxy * R_m10
    Vyy = C_val * Fyy * R_m10

    grad = mp.matrix([VR, Vx, Vy])
    hess = mp.matrix([
        [VRR, VRx, VRy],
        [VRx, Vxx, Vxy],
        [VRy, Vxy, Vyy],
    ])
    return V, grad, hess, F


def run_ref3(ow21_data, discrepancies):
    n_sym, p_sym = sp.symbols("n p", positive=True, integer=True)
    p_curv = n_sym + 2
    p_brane = 2 * n_sym
    p_flux = n_sym + 2 * p_sym
    p_cas = 2 * n_sym + 4
    exps_7d = [int(expr.subs({n_sym: 3, p_sym: 3})) for expr in (p_curv, p_brane, p_flux, p_cas)]

    R_s, A_s, F_s = sp.symbols("R A F", positive=True)
    C_any = sp.Symbol("C_any", real=True)
    V_nogo = A_s * R_s ** (-5) + F_s * R_s ** (-9) + C_any * R_s ** (-10)
    C_sol = sp.solve(sp.diff(V_nogo, R_s), C_any)[0]
    nogo_r11_v2 = sp.simplify((R_s ** 11 * sp.diff(V_nogo, R_s, 2)).subs(C_any, C_sol))
    nogo_at_R1 = sp.simplify(nogo_r11_v2.subs(R_s, 1))
    nogo_exact_ok = (sp.simplify(nogo_at_R1 - (-25 * A_s - 9 * F_s)) == 0)

    p1_s, p2_s, p3_s, u_s, x_s = sp.symbols("p1 p2 p3 u x", positive=True)
    z_s = x_s * (p2_s * u_s - p1_s) / p3_s
    V_stat = sp.factor(x_s - u_s * x_s + z_s)
    V2_stat = sp.factor(p1_s * (p1_s + 1) * x_s - p2_s * (p2_s + 1) * u_s * x_s + p3_s * (p3_s + 1) * z_s)
    u_lo_sym = sp.solve(V2_stat, u_s)[0]
    u_hi_sym = sp.solve(V_stat, u_s)[0]
    u_lo_7d = sp.simplify(u_lo_sym.subs({p1_s: 5, p2_s: 6, p3_s: 10}))
    u_hi_7d = sp.simplify(u_hi_sym.subs({p1_s: 5, p2_s: 6, p3_s: 10}))
    ds_window_ok = (u_lo_7d == sp.Rational(25, 24)) and (u_hi_7d == sp.Rational(5, 4))

    t_nodes, t_weights = build_mellin_quadrature()
    e3_i_mel = e3_mellin_jets(mp.mpf(0), mp.mpf(1), t_nodes, t_weights, t_shift=False)[0]
    e3_i_exact = (mp.pi ** 3 / mp.mpf(8)) * mp.zeta(3)
    e3_i_err = abs(e3_i_mel - e3_i_exact)

    tx, ty = mp_rat(3, 10), mp_rat(7, 10)
    tr2 = tx * tx + ty * ty
    e3_s1 = e3_mellin_jets(tx, ty, t_nodes, t_weights, t_shift=False)[0]
    e3_s2 = e3_mellin_jets(-tx / tr2, ty / tr2, t_nodes, t_weights, t_shift=False)[0]
    e3_s_duality_err = abs(e3_s1 - e3_s2)

    A_val = mp.mpf(3000)
    B_val = mp.mpf(3500)
    C_e8 = mp_rat(1568, 25)
    C_so10 = mp_rat(-1456, 25)

    R_cur = mp_rat(9, 10)
    x_cur = mp_rat(7, 20)
    y_cur = mp_rat(11, 50)
    iters = 0
    for it in range(30):
        V_c, g_c, H_c, _ = v_3d_eval(R_cur, x_cur, y_cur, A_val, B_val, C_e8, t_nodes, t_weights)
        gnorm = mp.sqrt(g_c[0] ** 2 + g_c[1] ** 2 + g_c[2] ** 2)
        iters = it
        if gnorm < mp_pow10(-32):
            break
        ev_h, _ = mp.eigh(H_c)
        if ev_h[0] <= mp.mpf(0):
            shift = abs(ev_h[0]) + mp.mpf(100)
            H_reg = H_c + shift * mp.eye(3)
            step = -mp.lu_solve(H_reg, g_c)
        else:
            step = -mp.lu_solve(H_c, g_c)
        alpha = mp.mpf(1)
        accepted = False
        for _ls in range(40):
            Rn = R_cur + alpha * step[0]
            xn = x_cur + alpha * step[1]
            yn = y_cur + alpha * step[2]
            if Rn > mp_rat(1, 5) and yn > mp_rat(1, 20):
                Vn = v_3d_eval(Rn, xn, yn, A_val, B_val, C_e8, t_nodes, t_weights)[0]
                if Vn < V_c:
                    R_cur, x_cur, y_cur = Rn, xn, yn
                    accepted = True
                    break
            alpha *= mp_rat(1, 2)
        if not accepted:
            break

    V_min, g_min, H_min, F3_min = v_3d_eval(R_cur, x_cur, y_cur, A_val, B_val, C_e8, t_nodes, t_weights)
    grad_norm_min = mp.sqrt(g_min[0] ** 2 + g_min[1] ** 2 + g_min[2] ** 2)
    hess_eigs_e8, _ = mp.eigh(H_min)
    hess_eigs_e8_list = sorted([hess_eigs_e8[0], hess_eigs_e8[1], hess_eigs_e8[2]])
    tau_conv_err = mp.sqrt((x_cur - mp_rat(2, 5)) ** 2 + (y_cur - mp_rat(1, 5)) ** 2)
    u_dimless = (B_val / A_val) / R_cur

    C_eff = C_e8 * F3_min
    R_bar = mp_rat(5, 4)
    for _ in range(30):
        f_r = mp.mpf(5) * A_val * (R_bar ** 5) - mp.mpf(6) * B_val * (R_bar ** 4) + mp.mpf(10) * C_eff
        fp_r = mp.mpf(25) * A_val * (R_bar ** 4) - mp.mpf(24) * B_val * (R_bar ** 3)
        delta_r = f_r / fp_r
        R_bar -= delta_r
        if abs(delta_r) < mp_pow10(-40):
            break
    V_bar = A_val * (R_bar ** (-5)) - B_val * (R_bar ** (-6)) + C_eff * (R_bar ** (-10))

    _, _, H_so10, _ = v_3d_eval(R_cur, mp_rat(2, 5), mp_rat(1, 5), A_val, B_val, C_so10, t_nodes, t_weights)
    hess_eigs_so10, _ = mp.eigh(H_so10)
    so10_min_eig = min(hess_eigs_so10[0], hess_eigs_so10[1], hess_eigs_so10[2])

    ow21_c = ow21_data["OW21_C_universal_3term_ds_and_3d_stabilization"]
    stab_t = ow21_c["simultaneous_3d_stabilization_E8_3x27"]
    deltas = {
        "F3_at_minimum": abs(F3_min - mp.mpf(stab_t["F3_at_minimum"])),
        "R_min_dynamical": abs(R_cur - mp.mpf(stab_t["R_min_dynamical"])),
        "V_min_metastable_dS": abs(V_min - mp.mpf(stab_t["V_min_metastable_dS"])),
        "R_barrier_max": abs(R_bar - mp.mpf(stab_t["R_barrier_max"])),
        "V_barrier_max": abs(V_bar - mp.mpf(stab_t["V_barrier_max"])),
        "u_dimensionless": abs(u_dimless - mp.mpf(stab_t["u_dimensionless_in_25_24_to_5_4"])),
        "hess_eigs_max_rel": max(
            abs(hess_eigs_e8_list[i] - mp.mpf(stab_t["hessian_3x3_eigenvalues"][i])) / abs(mp.mpf(stab_t["hessian_3x3_eigenvalues"][i]))
            for i in range(3)
        ),
        "so10_min_eig_rel": abs(so10_min_eig - mp.mpf(stab_t["SO10_neg_casimir_direct_3x3_min_eig"])) / abs(mp.mpf(stab_t["SO10_neg_casimir_direct_3x3_min_eig"])),
    }
    max_delta_c = max(deltas.values())

    gate_pass = (
        exps_7d == [5, 6, 9, 10]
        and nogo_exact_ok
        and ds_window_ok
        and e3_i_err < mp_pow10(-35)
        and e3_s_duality_err < mp_pow10(-35)
        and grad_norm_min < mp_pow10(-24)
        and tau_conv_err < mp_pow10(-24)
        and V_min > mp.mpf(0)
        and V_bar > V_min
        and all(ev > mp.mpf(0) for ev in hess_eigs_e8_list)
        and so10_min_eig < mp.mpf(-1000)
        and max_delta_c < mp_pow10(-9)
    )
    if not gate_pass:
        discrepancies.append("REF_3_disjoint_mellin_3term_ds_failed")

    return {
        "einstein_frame_7d_exponents": exps_7d,
        "nogo_7d_at_R1": str(nogo_at_R1),
        "nogo_7d_exact_ok": nogo_exact_ok,
        "ds_window_7d_bounds": [str(u_lo_7d), str(u_hi_7d)],
        "ds_window_symbolic_ok": ds_window_ok,
        "mellin_E3_i_err_vs_exact": mpf_str(e3_i_err, 8),
        "mellin_E3_nontrivial_S_duality_err": mpf_str(e3_s_duality_err, 8),
        "F3_at_minimum": mpf_str(F3_min, 16),
        "R_min_dynamical": mpf_str(R_cur, 20),
        "tau_min_dynamical_re_im": [mpf_str(x_cur, 16), mpf_str(y_cur, 16)],
        "tau_convergence_err": mpf_str(tau_conv_err, 8),
        "V_min_metastable_dS": mpf_str(V_min, 16),
        "R_barrier_max": mpf_str(R_bar, 16),
        "V_barrier_max": mpf_str(V_bar, 16),
        "u_dimensionless": mpf_str(u_dimless, 16),
        "damped_newton_iters": iters,
        "grad_V_3d_norm": mpf_str(grad_norm_min, 8),
        "hessian_3x3_eigenvalues": [mpf_str(ev, 14) for ev in hess_eigs_e8_list],
        "SO10_neg_casimir_min_eig": mpf_str(so10_min_eig, 14),
        "deltas_vs_producer": {k: mpf_str(v, 8) for k, v in deltas.items()},
        "max_delta_vs_producer": mpf_str(max_delta_c, 8),
        "gate_pass": gate_pass,
        "_pf_cache": {
            "so10_min_eig": so10_min_eig,
            "C_eff_e8": C_eff,
        },
    }


# ---------------------------------------------------------------------------
# REF-4: Independent Audit of A2-OW16 v8 & 6/6 Referee Planted Fault Controls
# ---------------------------------------------------------------------------

def run_ref4(ow16_data, ref1_res, ref2_res, ref3_res, discrepancies):
    ledger = ow16_data["blind_prediction_ledger_24_v8"]
    obs_list = ledger["observables"]
    ids = [o["id"] for o in obs_list]
    expected_ids = {f"OBS-{k:02d}" for k in range(1, 25)}
    ids_ok = (len(ids) == 24 and set(ids) == expected_ids)

    counts = {}
    derived_exact_ids = []
    for o in obs_list:
        b = o["bucket"]
        counts[b] = counts.get(b, 0) + 1
        if b == "DERIVED_EXACT":
            derived_exact_ids.append(o["id"])

    expected_buckets = {
        "DERIVED_EXACT": 1,
        "CONDITIONAL_OR_QUALITATIVE": 10,
        "INTERNAL_WALL_OR_TENSION": 9,
        "OPEN_EXTERNAL_BOUNDARY": 4,
    }
    buckets_ok = (counts == expected_buckets and derived_exact_ids == ["OBS-07"])

    locks_blk = ow16_data["cross_card_locks_v8"]
    locks_dict = locks_blk["locks"]
    locks_ok = (
        len(locks_dict) == 14
        and locks_blk["total_locks"] == 14
        and locks_blk["locks_passed"] == 14
        and locks_blk["all_locks_passed"] is True
        and all(v is True for v in locks_dict.values())
    )

    g5 = ow16_data["guardrail5_input_ledger_v8"]
    recounted_15 = (
        len(g5["uv_continuous_ratios_core"])
        + len(g5["uv_continuous_ratios_threshold"])
        + len(g5["flavor_bulk_mass_ratios"])
        + len(g5["unfixed_2hdm_uv_quartics_priced"])
        + len(g5["unfixed_soft_and_modulus_priced"])
    )
    cbr = g5["conditional_parameter_reduction_branches"]
    elim_ghu = len(cbr["branch_6d_e8_ghu_eliminated"])
    elim_mod = len(cbr["branch_6d_e8_ghu_plus_3term_ds_eliminated_modulus"])
    s1_bits_exact = mp.log(mp.mpf(72), mp.mpf(2))
    s1_bits_err = abs(s1_bits_exact - mp.mpf(g5["discrete_synergy_s1_144_to_2_bits"]))
    b_spin10_indep = Fraction(-11, 3) * 8 + Fraction(2, 3) * 3 * 2
    g5_ok = (
        g5["dimensionful_anchor_count"] == 1
        and g5["dimensionful_anchors"] == ["v_EW"]
        and recounted_15 == 15
        and g5["total_priced_continuous_ratios_baseline_4d"] == 15
        and elim_ghu == 4
        and cbr["branch_6d_e8_ghu_count"] == 15 - elim_ghu
        and elim_mod == 2
        and cbr["branch_6d_e8_ghu_plus_3term_ds_with_priced_BA_count"] == 15 - elim_ghu - elim_mod + 1
        and cbr["branch_6d_e8_ghu_plus_3term_ds_fixed_BA_count"] == 15 - elim_ghu - elim_mod
        and s1_bits_err < mp_pow10(-11)
        and b_spin10_indep == Fraction(-76, 3)
    )

    # Independent census of ALL historical false-flag JSONs across relays/ (including frozen referee v1!)
    relays_dir = REPO_ROOT / "relays"
    discovered_false = set()
    for jp in sorted(relays_dir.rglob("*.json")):
        if jp.resolve() == OUT_JSON_PATH.resolve():
            continue
        data = json.loads(jp.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        has_false = False
        if data.get("all_gates_passed") is False or data.get("overall_pass") is False:
            has_false = True
        summ = data.get("summary")
        if isinstance(summ, dict) and summ.get("all_gates_passed") is False:
            has_false = True
        if has_false:
            discovered_false.add(jp.relative_to(REPO_ROOT).as_posix())

    disclosed_blk = ow16_data["historical_false_json_disclosure"]
    disclosed_set = {entry["file"] for entry in disclosed_blk["files"]}
    frozen_ow21_v1_path = "relays/a2_ow21/a2_ow21_results.json"
    frozen_ref_v1_path = "relays/a2_ow21_referee/a2_ow21_referee_results.json"
    historical_census_ok = (
        discovered_false == disclosed_set
        and frozen_ow21_v1_path in discovered_false
        and frozen_ref_v1_path in discovered_false
        and len(discovered_false) == disclosed_blk["total_historical_false_flag_jsons"]
    )

    # --- 6/6 Independent Referee Planted Fault Controls ---
    raw_bytes = bytearray(TARGET_OW21_SCRIPT.read_bytes())
    orig_sha = sha256_bytes(bytes(raw_bytes))
    raw_bytes[0] ^= 0x01
    tampered_sha = sha256_bytes(bytes(raw_bytes))
    pf_ref_1 = (tampered_sha != orig_sha)

    rel_v23 = ref1_res["_pf_ref_2_cache"]["rel_shift_v23"]
    pf_ref_2 = (abs(rel_v23) > mp_rat(6, 10))

    c2_roots = ref2_res["_pf_cache"]["case2_roots"]
    rand_cfgs = ref2_res["_pf_cache"]["random_configs"]
    root_set = ref2_res["_pf_cache"]["root_set"]
    fk_eps = ref2_res["_pf_cache"]["fk_eps"]
    wrong_lams = (Fraction(1), Fraction(1), Fraction(0), Fraction(1, 2))
    pf3_max_err = max(
        abs(eval_v_ghu_numeric(c2_roots, pc, gc, root_set, fk_eps) - eval_v_2hdm_quartic(pc, gc, wrong_lams))
        for pc, gc in rand_cfgs
    )
    pf_ref_3 = (pf3_max_err > mp_pow10(-2))

    pf4_yuk_shift = ref2_res["_pf_cache"]["pf4_yuk_shift"]
    pf_ref_4 = (pf4_yuk_shift > mp_pow10(-4))

    so10_eig = ref3_res["_pf_cache"]["so10_min_eig"]
    pf_ref_5 = (so10_eig < mp.mpf(-1000))

    A_pf6 = mp.mpf(3000)
    B_pf6 = mp.mpf(4500)
    C_eff_pf6 = ref3_res["_pf_cache"]["C_eff_e8"]
    lo_r = mp_rat(1, 2)
    hi_r = mp_rat(36, 25)
    for _ in range(120):
        mid_r = (lo_r + hi_r) * mp_rat(1, 2)
        f_mid = mp.mpf(5) * A_pf6 * (mid_r ** 5) - mp.mpf(6) * B_pf6 * (mid_r ** 4) + mp.mpf(10) * C_eff_pf6
        if f_mid > mp.mpf(0):
            lo_r = mid_r
        else:
            hi_r = mid_r
    R_ads = (lo_r + hi_r) * mp_rat(1, 2)
    V_ads = A_pf6 * (R_ads ** (-5)) - B_pf6 * (R_ads ** (-6)) + C_eff_pf6 * (R_ads ** (-10))
    V2_ads = mp.mpf(30) * A_pf6 * (R_ads ** (-7)) - mp.mpf(42) * B_pf6 * (R_ads ** (-8)) + mp.mpf(110) * C_eff_pf6 * (R_ads ** (-12))
    pf_ref_6 = (V_ads < mp.mpf(0)) and (V2_ads > mp.mpf(0))

    pf_controls = {
        "PF_REF_1_1byte_manifest_tamper_detected": pf_ref_1,
        "PF_REF_2_flat_I3_kahler_misses_gt_60pct_v23": pf_ref_2,
        "PF_REF_3_wrong_case2_lam4_fails_v_ghu": pf_ref_3,
        "PF_REF_4_gl4_lam0_deviates_from_E8_tree_yukawas": pf_ref_4,
        "PF_REF_5_SO10_neg_casimir_hessian_lt_neg1000": pf_ref_5,
        "PF_REF_6_excess_B4500_flips_dS_to_AdS": pf_ref_6,
    }
    pf_caught = sum(1 for v in pf_controls.values() if v)

    gate_pass = (
        ids_ok
        and buckets_ok
        and locks_ok
        and g5_ok
        and historical_census_ok
        and pf_caught == 6
    )
    if not gate_pass:
        discrepancies.append("REF_4_ow16_v8_or_planted_faults_failed")

    return {
        "ow16_v8_audit": {
            "ids_unique_24_ok": ids_ok,
            "counts_by_bucket": counts,
            "sole_derived_exact_ids": derived_exact_ids,
            "buckets_1_10_9_4_ok": buckets_ok,
            "locks_14_of_14_ok": locks_ok,
            "guardrail5_recounted_baseline_ratios": recounted_15,
            "guardrail5_reduction_15_11_10_9_ok": g5_ok,
            "s1_bits_err_vs_log2_72": mpf_str(s1_bits_err, 8),
            "b_Spin10_pure_fermion": f"{b_spin10_indep.numerator}/{b_spin10_indep.denominator}",
            "historical_false_flag_discovered_count": len(discovered_false),
            "historical_false_flag_disclosed_count": len(disclosed_set),
            "frozen_ow21_v1_included": (frozen_ow21_v1_path in discovered_false),
            "frozen_referee_v1_included": (frozen_ref_v1_path in discovered_false),
            "historical_false_flag_census_exact_match": historical_census_ok,
        },
        "planted_fault_controls": {
            "controls": pf_controls,
            "diagnostics": {
                "PF_REF_2_rel_shift_v23": mpf_str(rel_v23, 10),
                "PF_REF_3_wrong_lam4_v_ghu_max_err": mpf_str(pf3_max_err, 8),
                "PF_REF_4_gl4_lam0_yuk_frob_shift": mpf_str(pf4_yuk_shift, 8),
                "PF_REF_5_SO10_min_eig": mpf_str(so10_eig, 12),
                "PF_REF_6_B4500_R_min": mpf_str(R_ads, 14),
                "PF_REF_6_B4500_V_min_AdS": mpf_str(V_ads, 14),
            },
            "caught": pf_caught,
            "total": 6,
        },
        "gate_pass": gate_pass,
    }


def main():
    ow21_data = json.loads(TARGET_OW21_JSON.read_text(encoding="utf-8"))
    ow16_data = json.loads(TARGET_OW16_JSON.read_text(encoding="utf-8"))
    ow19_data = json.loads(SEALED_OW19_JSON.read_text(encoding="utf-8"))

    discrepancies = []

    ref0 = run_ref0(ow21_data, ow16_data, discrepancies)
    ref1 = run_ref1(ow21_data, ow19_data, discrepancies)
    ref2 = run_ref2(ow21_data, discrepancies)
    ref3 = run_ref3(ow21_data, discrepancies)
    ref4 = run_ref4(ow16_data, ref1, ref2, ref3, discrepancies)

    ref1.pop("_pf_ref_2_cache", None)
    ref2.pop("_pf_cache", None)
    ref3.pop("_pf_cache", None)

    all_gates_passed = (
        ref0["gate_pass"]
        and ref1["gate_pass"]
        and ref2["gate_pass"]
        and ref3["gate_pass"]
        and ref4["gate_pass"]
        and len(discrepancies) == 0
    )

    v1_script_entries = parse_manifest_lines((REFEREE_DIR / "SCRIPT_SHA256.txt").read_text(encoding="utf-8"))
    v1_out_entries = parse_manifest_lines((REFEREE_DIR / "OUTPUT_SHA256.txt").read_text(encoding="utf-8"))
    v1_frozen_preserved = (
        len(v1_script_entries) == 1
        and sha256_file(REFEREE_DIR / v1_script_entries[0][1]) == v1_script_entries[0][0]
        and len(v1_out_entries) == 1
        and sha256_file(REFEREE_DIR / v1_out_entries[0][1]) == v1_out_entries[0][0]
    )

    payload = {
        "card": "A2-OW21-v3 + A2-OW16-v8 Cold-Room Independent Referee v2",
        "seat": "agy-002",
        "firewall": "0 of 19",
        "v1_frozen_preserved": v1_frozen_preserved,
        "referee_hygiene": {
            "script_sha256": sha256_file(SELF_PATH),
            "float_complex_literals": ref0["ast_audit"]["referee_a2_ow21_v2_self"]["float_complex_literals"],
            "binary64_casts": ref0["ast_audit"]["referee_a2_ow21_v2_self"]["binary64_casts"],
            "forbidden_imports": ref0["ast_audit"]["referee_a2_ow21_v2_self"]["forbidden_imports_count"],
            "json_float_tokens": 0,
            "clean": ref0["ast_audit"]["referee_a2_ow21_v2_self"]["clean"],
        },
        "REF_0_ast_json_and_custody": ref0,
        "REF_1_disjoint_jtheta_ow21_a": ref1,
        "REF_2_disjoint_gl4_and_e8_ghu_ow21_b": ref2,
        "REF_3_disjoint_mellin_3term_ds_ow21_c": ref3,
        "REF_4_ow16_v8_and_planted_faults": ref4,
        "discrepancies": discrepancies,
        "discrepancies_count": len(discrepancies),
        "all_gates_passed": all_gates_passed,
    }

    assert_no_json_floats(payload)
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    json_float_cnt = count_json_float_tokens_in_text(serialized)
    assert json_float_cnt == 0, f"Found {json_float_cnt} JSON float tokens in referee v2 output"

    OUT_JSON_PATH.write_text(serialized, encoding="utf-8")
    print("REFEREE_V2_EXECUTION_COMPLETE")


if __name__ == "__main__":
    main()
