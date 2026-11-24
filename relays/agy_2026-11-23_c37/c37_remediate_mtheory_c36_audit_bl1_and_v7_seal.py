#!/usr/bin/env python3
r"""Card AGY-C37 Standalone Zero-Float Producer (0 of 19):
  - E1: Remediates AGY-C35's 11D M-theory T_M2 topological quantization (2 kappa_11^2 T_M2^3 = (2 pi)^2
        => T_M2 = M_11^3 / (2 pi)^2) and dimensionful V_7^dim = V_3^dim V_4^dim fiber-volume exponents
        ((M_11 / M_GUT)^5 self-dual, (M_11 / M_GUT)^9 isotropic), sealing all 50/50 observables and 24/24
        certificates from scratch in blind_predictions_full_toe_v7.json; applies SU(3)^5 x U(3) unitary
        basis-scrambling (< 10^-38 + non-Takagi M_R negative control) to AGY-C36's extracted flavor/seesaw
        observables; and records AGY-C36's OW22-F1 line/stage erratum (verify_a2_ow22_v2.py:278-280, 398-399).
  - E2: Audits and harvests origin/agy/self-consistent-loop-2026-11-11 @ 639a5d46b (Card X-BULK-LINK1 B1..B4)
        and bridges Spin(10) n_10 = 2N - 8 = 2 anomaly factorization to origin/main @ 279459977 (B1970 I-37).
  - E3: Proves four constructive catches BL1-F1..F4 on 639a5d46b plus the Exact Seesaw Right-Handed
        Localization Cancellation & Magnetized SU(5) Lopsidedness Theorem (curing OBS-18).
"""
from __future__ import annotations

import ast
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction as Fr
import hashlib
import itertools
from itertools import product
import json
import math
from pathlib import Path
import re
import subprocess
import time

import mpmath as mp
import sympy as sp

THIS_DIR = Path(__file__).resolve().parent
V7_JSON = THIS_DIR / "blind_predictions_full_toe_v7.json"
OUT_JSON = THIS_DIR / "c37_out.json"
OUT_SHA = THIS_DIR / "OUTPUT_SHA256.txt"

AGY_EXP_REF = "dd74b56c1c9cb3a4a060c594ba5a811df99e038c"
AGY_002_REF = "2d993276b051962b0c4400590435e56ea1946173"
AGY_EXP_HEAD = "639a5d46bee99c0c69682876f55ff6b77eee63cb"
AGY_002_HEAD = "27f5d89fabf1653e1a61b910ed1e9b4b1dca371a"
MAIN_HEAD = "2794599778e1aa14311d7ab7f9e2238e3d2e0e23"

I_MP = mp.mpc(0, 1)


def mp_rat(num: int, den: int = 1) -> mp.mpf:
    return mp.mpf(int(num)) / mp.mpf(int(den))


def f2m(q: Fr) -> mp.mpf:
    return mp.mpf(int(q.numerator)) / mp.mpf(int(q.denominator))


def find_repo_root() -> Path:
    for cand in (THIS_DIR, Path.cwd()):
        r = subprocess.run(["git", "-C", str(cand), "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False)
        if r.returncode == 0 and r.stdout.strip():
            return Path(r.stdout.strip())
    raise RuntimeError("Could not locate git repository root")


def git_ls_files(repo: Path, ref: str) -> list[str]:
    out = subprocess.check_output(["git", "-C", str(repo), "ls-tree", "-r", "--name-only", ref], text=True)
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def git_show_bytes(repo: Path, ref: str, rel_path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), "show", f"{ref}:{rel_path}"])


def resolve_commit_full(repo: Path, short_or_full: str) -> str:
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", short_or_full]).decode("utf-8").strip()


def verify_ast_strict(src: str, filename: str) -> dict[str, object]:
    tree = ast.parse(src, filename=filename)
    bad_lits: list[int] = []
    bad_calls: list[int] = []
    bad_imps: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex)):
            bad_lits.append(node.lineno)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ("float", "complex"):
            bad_calls.append(node.lineno)
        elif isinstance(node, ast.Import):
            for al in node.names:
                if al.name.startswith("frontier") or "grid" in al.name:
                    bad_imps.append(al.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            if node.module.startswith("frontier") or "grid" in node.module:
                bad_imps.append(node.module)
    return {
        "float_or_complex_literals": len(bad_lits),
        "float_or_complex_calls": len(bad_calls),
        "forbidden_imports": len(bad_imps),
        "passed": len(bad_lits) == 0 and len(bad_calls) == 0 and len(bad_imps) == 0,
    }


def check_zero_json_floats(raw_text: str, label: str) -> dict:
    def reject_float(val_s: str) -> None:
        raise AssertionError(f"[{label}] raw JSON float token found: {val_s}")

    return json.loads(raw_text, parse_float=reject_float)


def verify_all_sha256_on_ref(repo: Path, ref: str) -> tuple[int, int, list[str]]:
    files = git_ls_files(repo, ref)
    sha_files = [
        f for f in files
        if (f.startswith("relays/") or f.startswith("self_consistent_loop/")) and f.endswith("SHA256.txt")
    ]
    entries = 0
    mismatches: list[str] = []
    for sf in sha_files:
        parent = str(Path(sf).parent)
        raw = git_show_bytes(repo, ref, sf).decode("utf-8")
        for ln in raw.splitlines():
            ln_s = ln.strip()
            if not ln_s:
                continue
            m = re.match(r"^([0-9a-fA-F]{64})\s+\*?(.+)$", ln_s)
            if not m:
                continue
            exp_hex, rel_t = m.group(1).lower(), m.group(2).strip()
            cand = rel_t if rel_t in files else (f"{parent}/{Path(rel_t).name}" if parent != "." else Path(rel_t).name)
            actual_hex = hashlib.sha256(git_show_bytes(repo, ref, cand)).hexdigest()
            entries += 1
            if actual_hex != exp_hex:
                mismatches.append(f"{sf}:{cand}")
    return len(sha_files), entries, mismatches


# ---------------------------------------------------------------------------
# Exact Gaussian-Rational 4-Scalar 1HDM Machacek-Vaughn Tensor Engine (for Eq. B1 Audit)
# ---------------------------------------------------------------------------
class Qi:
    __slots__ = ("r", "i")

    def __init__(self, r: Fr | int = 0, i: Fr | int = 0) -> None:
        self.r = r if isinstance(r, Fr) else Fr(r)
        self.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(self, o: Qi | Fr | int) -> Qi:
        oo = o if isinstance(o, Qi) else Qi(o)
        return Qi(self.r + oo.r, self.i + oo.i)

    def __sub__(self, o: Qi | Fr | int) -> Qi:
        oo = o if isinstance(o, Qi) else Qi(o)
        return Qi(self.r - oo.r, self.i - oo.i)

    def __neg__(self) -> Qi:
        return Qi(-self.r, -self.i)

    def __mul__(self, o: Qi | Fr | int) -> Qi:
        oo = o if isinstance(o, Qi) else Qi(o)
        return Qi(self.r * oo.r - self.i * oo.i, self.r * oo.i + self.i * oo.r)

    def conj(self) -> Qi:
        return Qi(self.r, -self.i)

    def __eq__(self, o: object) -> bool:
        oo = o if isinstance(o, Qi) else Qi(o)  # type: ignore[arg-type]
        return self.r == oo.r and self.i == oo.i


def eval_1hdm_mv84_pure_y5_exact(Yu: list[list[Qi]], Yd: list[list[Qi]], Ye: list[list[Qi]]) -> tuple[list[list[Qi]], list[list[Qi]]]:
    """Exact Q(i) 4-real-scalar Machacek-Vaughn (NPB 236 (1984) 221, Eq. 3.4) 2-loop pure-Y^5 evaluator for 1HDM."""
    n = len(Yu)
    Z0, IM = Qi(0, 0), Qi(0, 1)
    nf = 8 * n
    tw = [Qi(3)] * (4 * n) + [Qi(1)] * (4 * n)

    def mz(r: int, c: int) -> list[list[Qi]]:
        return [[Z0 for _ in range(c)] for _ in range(r)]

    def madd(A: list[list[Qi]], B: list[list[Qi]]) -> list[list[Qi]]:
        return [[A[r][c] + B[r][c] for c in range(len(A[0]))] for r in range(len(A))]

    def msc(s: Qi | Fr | int, A: list[list[Qi]]) -> list[list[Qi]]:
        ss = s if isinstance(s, Qi) else Qi(s)
        return [[ss * A[r][c] for c in range(len(A[0]))] for r in range(len(A))]

    def mT(A: list[list[Qi]]) -> list[list[Qi]]:
        return [[A[r][c] for r in range(len(A))] for c in range(len(A[0]))]

    def mdag(A: list[list[Qi]]) -> list[list[Qi]]:
        return [[A[r][c].conj() for r in range(len(A))] for c in range(len(A[0]))]

    def msym(A: list[list[Qi]]) -> list[list[Qi]]:
        return msc(Fr(1, 2), madd(A, mT(A)))

    def wtr(A: list[list[Qi]]) -> Qi:
        s = Z0
        for k in range(nf):
            s = s + tw[k] * A[k][k]
        return s

    def mmul(A: list[list[Qi]], B: list[list[Qi]]) -> list[list[Qi]]:
        ra, ca, cb = len(A), len(A[0]), len(B[0])
        out = mz(ra, cb)
        for r in range(ra):
            for k in range(ca):
                ark = A[r][k]
                if ark.r == 0 and ark.i == 0:
                    continue
                for c in range(cb):
                    out[r][c] = out[r][c] + ark * B[k][c]
        return out

    Z = mz(n, n)

    def b4(a: list[list[Qi]], b: list[list[Qi]], c: list[list[Qi]], d: list[list[Qi]]) -> list[list[Qi]]:
        M = mz(4 * n, 4 * n)
        for br, bc, B in ((0, 2, a), (2, 0, mT(a)), (1, 2, b), (2, 1, mT(b)), (0, 3, c), (3, 0, mT(c)), (1, 3, d), (3, 1, mT(d))):
            for r in range(n):
                for col in range(n):
                    M[br * n + r][bc * n + col] = B[r][col]
        return M

    def join_ql(Q: list[list[Qi]], L: list[list[Qi]]) -> list[list[Qi]]:
        M = mz(nf, nf)
        for r in range(4 * n):
            for c in range(4 * n):
                M[r][c] = Q[r][c]
                M[4 * n + r][4 * n + c] = L[r][c]
        return M

    Us = [
        join_ql(b4(Z, msc(-1, Yu), Yd, Z), b4(Z, Z, Ye, Z)),
        join_ql(b4(Z, msc(IM, Yu), msc(IM, Yd), Z), b4(Z, Z, msc(IM, Ye), Z)),
        join_ql(b4(Yu, Z, Z, Yd), b4(Z, Z, Z, Ye)),
        join_ql(b4(msc(-IM, Yu), Z, Z, msc(IM, Yd)), b4(Z, Z, Z, msc(IM, Ye))),
    ]
    Ud = [mdag(U) for U in Us]
    Ua, Uad = Us[2], Ud[2]
    P = mz(nf, nf)
    for b in range(4):
        P = madd(P, mmul(Ud[b], Us[b]))
    PT = mT(P)
    S = [[Qi(Fr(1, 2)) * (wtr(mmul(Ud[b], Us[c])) + wtr(mmul(Ud[c], Us[b]))) for c in range(4)] for b in range(4)]

    T0 = mz(nf, nf); T2 = mz(nf, nf); T3 = mz(nf, nf)
    G2 = mz(nf, nf); G3 = mz(nf, nf); G4 = mz(nf, nf)
    for b in range(4):
        Ub_Uad = mmul(Us[b], Uad)
        G2 = madd(G2, mmul(Ud[b], mmul(PT, Us[b])))
        for c in range(4):
            Ub_Udc = mmul(Us[b], Ud[c])
            T0 = madd(T0, mmul(Ub_Udc, mmul(Ua, mmul(Ud[b], Us[c]))))
            T2 = madd(T2, mmul(Ub_Udc, mmul(Ub_Uad, Us[c])))
            T3 = madd(T3, msc(S[b][c], mmul(Ub_Uad, Us[c])))
            G3 = madd(G3, msc(S[b][c], mmul(Ud[b], Us[c])))
            G4 = madd(G4, msc(Fr(1, 2), madd(mmul(Ud[b], mmul(Us[c], mmul(Ud[b], Us[c]))), mmul(Ud[c], mmul(Us[b], mmul(Ud[c], Us[b]))))))
    T0, T2, T3 = msym(T0), msym(T2), msym(T3)
    T5 = msym(madd(mmul(mT(G2), Ua), mmul(Ua, G2)))
    T6 = msym(madd(mmul(mT(G3), Ua), mmul(Ua, G3)))
    T7 = msym(madd(mmul(mT(G4), Ua), mmul(Ua, G4)))

    T8 = mz(nf, nf); T9 = mz(nf, nf)
    for b in range(4):
        h1 = Qi(Fr(1, 2)) * (wtr(mmul(Ud[b], mmul(PT, Ua))) + wtr(mmul(Uad, mmul(PT, Us[b]))) + wtr(mmul(Ud[b], mmul(Ua, P))) + wtr(mmul(Uad, mmul(Us[b], P))))
        h2 = Z0
        for c in range(4):
            h2 = h2 + Qi(Fr(1, 2)) * (wtr(mmul(Ud[b], mmul(Us[c], mmul(Uad, Us[c])))) + wtr(mmul(Ud[c], mmul(Us[b], mmul(Ud[c], Ua)))))
        T8 = madd(T8, msc(h1, Us[b]))
        T9 = madd(T9, msc(h2, Us[b]))

    B2 = msc(Fr(1, 4), madd(msc(2, T0), madd(msc(6, T2), madd(msc(-2, T3), madd(msc(Fr(-1, 8), T5), madd(msc(Fr(-3, 4), T6), madd(T7, madd(msc(Fr(-3, 4), T8), msc(-1, T9)))))))))
    b2_yu = [[B2[r][2 * n + c] for c in range(n)] for r in range(n)]
    b2_yd = [[B2[n + r][3 * n + c] for c in range(n)] for r in range(n)]
    return b2_yu, b2_yd


# ---------------------------------------------------------------------------
# Section 1 (E1): Scoped Peer Audit of dd74b56c1 & 2d993276b + Core Lie/E6/Sen Theorems
# ---------------------------------------------------------------------------
def run_e1_peer_audit_and_core_theorems(repo: Path) -> dict[str, object]:
    """Audits dd74b56c1 (agy-exp) & 2d993276b (agy-002) with explicit scope boundaries (fixing D6),
    evaluates dd74b56c1:main.tex Eq. (B1) on non-commuting matrices (catching +(3/4)[H_d,H_u] Y_u),
    catches 2d993276b:verify_a2_ow20.py:609's inherited 3/(4 zeta(3) g_*) yield factor, and proves
    all core E_6 351'_H, Sen -277/360, untwisted IC5 = -6, so(10) commutant, and r_10 = 4/9 theorems."""
    exp_sha_files, exp_sha_entries, exp_sha_mism = verify_all_sha256_on_ref(repo, AGY_EXP_REF)
    a02_sha_files, a02_sha_entries, a02_sha_mism = verify_all_sha256_on_ref(repo, AGY_002_REF)
    assert not exp_sha_mism and not a02_sha_mism

    # Check AST zero-float cleanliness on new peer verification scripts:
    peer_py_checked = 0
    for ref_h, paths_py in (
        (AGY_EXP_REF, [
            "relays/r_ow19_ex12_verify/verify_r_ow19_ex12.py",
            "relays/x_e6ps_link23_v2_verify/verify_x_e6ps_link23_v2.py",
            "relays/x_e6ps_link23_referee/referee_x_e6ps_link23.py",
        ]),
        (AGY_002_REF, [
            "relays/a2_ow20/verify_a2_ow20.py",
            "relays/a2_ow16_v6/verify_a2_ow16_v6.py",
            "relays/a2_ow20_referee/referee_a2_ow20.py",
        ]),
    ):
        for py_rel in paths_py:
            res_ast = verify_ast_strict(git_show_bytes(repo, ref_h, py_rel).decode("utf-8"), py_rel)
            assert res_ast["passed"], f"Peer script AST float failure: {py_rel}"
            peer_py_checked += 1

    # 1. Live evaluation of dd74b56c1:self_consistent_loop/manuscript/main.tex Eq. (B1) (fixing D6):
    main_tex = git_show_bytes(repo, AGY_EXP_REF, "self_consistent_loop/manuscript/main.tex").decode("utf-8")
    tex_has_fixed_t2 = r"T_2 = \mathrm{Tr}(3H_u^2 + 3H_d^2 + H_e^2 - \frac{2}{3}H_u H_d)" in main_tex
    tex_has_swapped_yu = r"\frac{3}{2}H_u^2 - H_u H_d - \frac{1}{4}H_d H_u + \frac{11}{4}H_d^2" in main_tex
    tex_has_swapped_yd = r"\frac{3}{2}H_d^2 - H_d H_u - \frac{1}{4}H_u H_d + \frac{11}{4}H_u^2" in main_tex
    assert tex_has_fixed_t2 and tex_has_swapped_yu and tex_has_swapped_yd

    Yu_q = [[Qi(2), Qi(1)], [Qi(0), Qi(3)]]
    Yd_q = [[Qi(1), Qi(0)], [Qi(2), Qi(5)]]
    Ye_q = [[Qi(3), Qi(2)], [Qi(1), Qi(4)]]
    mv_yu_q, mv_yd_q = eval_1hdm_mv84_pure_y5_exact(Yu_q, Yd_q, Ye_q)

    def mul2(A: list[list[Qi]], B: list[list[Qi]]) -> list[list[Qi]]:
        return [[A[r][0] * B[0][c] + A[r][1] * B[1][c] for c in range(2)] for r in range(2)]

    def dag2(A: list[list[Qi]]) -> list[list[Qi]]:
        return [[A[0][0].conj(), A[1][0].conj()], [A[0][1].conj(), A[1][1].conj()]]

    def add2(A: list[list[Qi]], B: list[list[Qi]]) -> list[list[Qi]]:
        return [[A[r][c] + B[r][c] for c in range(2)] for r in range(2)]

    def sc2(s: Fr | int, A: list[list[Qi]]) -> list[list[Qi]]:
        qs = Qi(s)
        return [[qs * A[r][c] for c in range(2)] for r in range(2)]

    Hu_q, Hd_q, He_q = mul2(Yu_q, dag2(Yu_q)), mul2(Yd_q, dag2(Yd_q)), mul2(Ye_q, dag2(Ye_q))
    Hu2_q, Hd2_q, He2_q = mul2(Hu_q, Hu_q), mul2(Hd_q, Hd_q), mul2(He_q, He_q)
    T1h_q = (Qi(3) * (Hu_q[0][0] + Hu_q[1][1] + Hd_q[0][0] + Hd_q[1][1]) + He_q[0][0] + He_q[1][1]).r
    HuHd_q, HdHu_q = mul2(Hu_q, Hd_q), mul2(Hd_q, Hu_q)
    T2h_q = (Qi(3) * (Hu2_q[0][0] + Hu2_q[1][1] + Hd2_q[0][0] + Hd2_q[1][1]) + He2_q[0][0] + He2_q[1][1] - Qi(Fr(2, 3)) * (HuHd_q[0][0] + HuHd_q[1][1])).r
    I2_q = [[Qi(1), Qi(0)], [Qi(0), Qi(1)]]

    lx_yu_q = mul2(add2(add2(sc2(Fr(3, 2), Hu2_q), add2(sc2(-1, HdHu_q), sc2(Fr(-1, 4), HuHd_q))), add2(sc2(Fr(11, 4), Hd2_q), add2(sc2(T1h_q, add2(sc2(Fr(5, 4), Hd_q), sc2(Fr(-9, 4), Hu_q))), sc2(Fr(-9, 4) * T2h_q, I2_q)))), Yu_q)
    tex_yu_q = mul2(add2(add2(sc2(Fr(3, 2), Hu2_q), add2(sc2(-1, HuHd_q), sc2(Fr(-1, 4), HdHu_q))), add2(sc2(Fr(11, 4), Hd2_q), add2(sc2(T1h_q, add2(sc2(Fr(5, 4), Hd_q), sc2(Fr(-9, 4), Hu_q))), sc2(Fr(-9, 4) * T2h_q, I2_q)))), Yu_q)
    lx_yd_q = mul2(add2(add2(sc2(Fr(3, 2), Hd2_q), add2(sc2(-1, HuHd_q), sc2(Fr(-1, 4), HdHu_q))), add2(sc2(Fr(11, 4), Hu2_q), add2(sc2(T1h_q, add2(sc2(Fr(5, 4), Hu_q), sc2(Fr(-9, 4), Hd_q))), sc2(Fr(-9, 4) * T2h_q, I2_q)))), Yd_q)
    tex_yd_q = mul2(add2(add2(sc2(Fr(3, 2), Hd2_q), add2(sc2(-1, HdHu_q), sc2(Fr(-1, 4), HuHd_q))), add2(sc2(Fr(11, 4), Hu2_q), add2(sc2(T1h_q, add2(sc2(Fr(5, 4), Hu_q), sc2(Fr(-9, 4), Hd_q))), sc2(Fr(-9, 4) * T2h_q, I2_q)))), Yd_q)

    comm_yu_q = mul2(sc2(Fr(3, 4), add2(HdHu_q, sc2(-1, HuHd_q))), Yu_q)
    comm_yd_q = mul2(sc2(Fr(3, 4), add2(HuHd_q, sc2(-1, HdHu_q))), Yd_q)
    mv_matches_lx_exact = (mv_yu_q == lx_yu_q) and (mv_yd_q == lx_yd_q)
    diff_tex_yu = [[tex_yu_q[r][c] - mv_yu_q[r][c] for c in range(2)] for r in range(2)]
    diff_tex_yd = [[tex_yd_q[r][c] - mv_yd_q[r][c] for c in range(2)] for r in range(2)]
    eq_b1_swap_caught = mv_matches_lx_exact and (diff_tex_yu == comm_yu_q) and (diff_tex_yd == comm_yd_q) and any(diff_tex_yu[r][c] != Qi(0) for r in range(2) for c in range(2))
    assert eq_b1_swap_caught

    # 2. Recompute X-E6PS-LINK23 (dd74b56c1) mod-9 [Z_3^{tau_3}]^3, unique N_gen = 3, and r_LR = 2/5 & 8/25:
    anom_free_ng = [ng for ng in range(1, 21) if (4 * ng) % 3 == 0 and (15 * ng) % 9 == 0]
    dep_lr_ng = [ng for ng in range(1, 21) if (24 + 17 * ng - 60) < 31]
    unique_ngen = sorted(set(anom_free_ng) & set(dep_lr_ng))
    no_chiS_mod9_at_n3 = (3 * 16) % 9  # 48 mod 9 == 3 != 0 (Control 1!)
    assert unique_ngen == [3] and no_chiS_mod9_at_n3 == 3

    # Chiral G_LR = U(1)_{B-L} x SU(2)_L x SU(2)_R x SU(3)_C 1-loop betas (2 bidoublets + Delta_R_bar + S):
    b_bl_ch = Fr(2, 3) * (3 * (6 * Fr(3, 8) * Fr(1, 9) + 6 * Fr(3, 8) * Fr(1, 9) + 2 * Fr(3, 8) + 2 * Fr(3, 8))) + Fr(1, 3) * (3 * Fr(3, 8) * 4)  # 4 + 3/2 == 11/2
    b_2l_ch = Fr(-22, 3) + Fr(2, 3) * 6 + Fr(1, 3) * (2 * 1)              # -22/3 + 4 + 2/3 == -8/3
    b_2r_ch = Fr(-22, 3) + Fr(2, 3) * 6 + Fr(1, 3) * (2 * 1 + 2)          # -22/3 + 4 + 4/3 == -2
    b_3c_ch = Fr(-33, 3) + Fr(2, 3) * 6                                   # -7
    b1_eff_ch = Fr(3, 5) * b_2r_ch + Fr(2, 5) * b_bl_ch                   # -6/5 + 11/5 == 1
    b1_sm_2h, b2_sm_2h, b3_sm_2h = Fr(21, 5), Fr(-3, 1), Fr(-7, 1)
    r_lr_sym = sp.Symbol("r_lr", rational=True)
    db12_ch = b1_sm_2h - b2_sm_2h + r_lr_sym * ((b1_eff_ch - b_2l_ch) - (b1_sm_2h - b2_sm_2h))
    db23_ch = b2_sm_2h - b3_sm_2h + r_lr_sym * ((b_2l_ch - b_3c_ch) - (b2_sm_2h - b3_sm_2h))
    r_lr_chiral_sp = sp.solve(sp.Eq(db23_ch / db12_ch, sp.Rational(5, 7)), r_lr_sym)[0]
    r_lr_chiral = Fr(int(r_lr_chiral_sp.p), int(r_lr_chiral_sp.q))
    # D-parity G_LR (+ Delta_L in (1,3,1,-2)):
    b_bl_dp = b_bl_ch + Fr(1, 3) * (3 * Fr(3, 8) * 4)                     # 7
    b_2l_dp = b_2l_ch + Fr(1, 3) * 2                                      # -2
    b1_eff_dp = Fr(3, 5) * b_2r_ch + Fr(2, 5) * b_bl_dp                   # 8/5
    db12_dp = b1_sm_2h - b2_sm_2h + r_lr_sym * ((b1_eff_dp - b_2l_dp) - (b1_sm_2h - b2_sm_2h))
    db23_dp = b2_sm_2h - b3_sm_2h + r_lr_sym * ((b_2l_dp - b_3c_ch) - (b2_sm_2h - b3_sm_2h))
    r_lr_dpar_sp = sp.solve(sp.Eq(db23_dp / db12_dp, sp.Rational(5, 7)), r_lr_sym)[0]
    r_lr_dparity = Fr(int(r_lr_dpar_sp.p), int(r_lr_dpar_sp.q))
    assert r_lr_chiral == Fr(2, 5) and r_lr_dparity == Fr(8, 25)

    # 3. Catch 2d993276b:relays/a2_ow20/verify_a2_ow20.py:609 inherited neq = 3/(4 zeta(3) g_*) yield factor:
    ow20_py = git_show_bytes(repo, AGY_002_REF, "relays/a2_ow20/verify_a2_ow20.py").decode("utf-8")
    ow20_has_inverted_zeta3 = "neq = mp_rat(3, 4) / (mp.zeta(3) * g_star)" in ow20_py
    ow20_yb_inflation_ratio = (mp.pi**4) / (45 * (mp.zeta(3) ** 2))
    assert ow20_has_inverted_zeta3 and ow20_yb_inflation_ratio > mp_rat(7, 5)

    # 4. Core E_6 -> Spin(10) x U(1)_psi, 351'_H seesaw, Sen IR BH -277/360, untwisted IC5 = -6, so(10) commutant, r_10 = 4/9:
    reps_27f = [
        ("Q_L", 3, 2, Fr(1, 6), Fr(1, 3), 1, 1, "16"),
        ("u_R^c", 3, 1, Fr(-2, 3), Fr(-1, 3), 1, 1, "16"),
        ("d_R^c", 3, 1, Fr(1, 3), Fr(-1, 3), 1, 1, "16"),
        ("ell_L", 1, 2, Fr(-1, 2), Fr(-1, 1), 1, 1, "16"),
        ("e_R^c", 1, 1, Fr(1, 1), Fr(1, 1), 1, 1, "16"),
        ("N_R^c", 1, 1, Fr(0, 1), Fr(1, 1), 1, 1, "16"),
        ("D", 3, 1, Fr(-1, 3), Fr(-2, 3), -2, 1, "10_F"),
        ("D^c", 3, 1, Fr(1, 3), Fr(2, 3), -2, 1, "10_F"),
        ("Htilde_u", 1, 2, Fr(1, 2), Fr(0, 1), -2, 1, "10_F"),
        ("Htilde_d", 1, 2, Fr(-1, 2), Fr(0, 1), -2, 1, "10_F"),
        ("psi_S", 1, 1, Fr(0, 1), Fr(0, 1), 4, 1, "1_F"),
    ]
    tot_dim = tr_q = tr_q3 = pm_even_16 = pm_odd_exotic = n_weyl_sm_one_gen = 0
    tr_su3_q = tr_su2_q = tr_y2_q = Fr(0, 1)
    for name, d3, d2, yv, bl, qp, two_s, sec in reps_27f:
        mult = d3 * d2
        tot_dim += mult
        tr_q += mult * qp
        tr_q3 += mult * (qp**3)
        tr_su3_q += (Fr(1, 2) * d2 if d3 == 3 else Fr(0, 1)) * qp
        tr_su2_q += (Fr(1, 2) * d3 if d2 == 2 else Fr(0, 1)) * qp
        tr_y2_q += Fr(3, 5) * mult * (yv**2) * qp
        pm_val = -1 if (int(3 * bl + two_s) % 2 != 0) else 1
        if sec == "16":
            assert pm_val == 1
            pm_even_16 += mult
            if name != "N_R^c":
                n_weyl_sm_one_gen += mult
        else:
            assert pm_val == -1
            pm_odd_exotic += mult
    assert tot_dim == 27 and pm_even_16 == 16 and pm_odd_exotic == 11 and n_weyl_sm_one_gen == 15
    max_anom_abs = max(abs(tr_q), abs(tr_q3), abs(tr_su3_q.numerator), abs(tr_su2_q.numerator), abs(tr_y2_q.numerator))

    q_f16, q_f1, q_h10, q_h1, q_delta126 = 1, 4, -2, 4, -2
    mr_forbidden_in_27h_only = 0 not in {(4 * n + 2 * q_f16) % 4 for n in range(-4, 5)}
    q_seesaw_126bar = 2 * q_f16 + q_delta126
    pm_delta126 = -1 if ((3 * (-2) + 0) % 2 != 0) else 1
    bl_psiS_delta126 = 2 * 0 + (-2)
    q_yuk_antihol = 2 * q_f16 - q_h10
    min_abs_q_psiS_renorm = min(abs(2 * q_f1), abs(2 * q_f1 + q_h1), abs(2 * q_f1 - q_h1), abs(2 * q_f1 + q_delta126))

    dim_g_sm = 8 + 3 + 1
    nb_minus_nf_untwisted = 2 * (dim_g_sm - n_weyl_sm_one_gen)
    n_s_ir, n_w_ir, n_v_ir = 8, 3 * n_weyl_sm_one_gen, dim_g_sm
    c_weyl_sq = n_s_ir * Fr(1, 120) + n_w_ir * Fr(1, 40) + n_v_ir * Fr(1, 10)
    a_euler = n_s_ir * Fr(1, 360) + n_w_ir * Fr(11, 720) + n_v_ir * Fr(31, 180)
    sen_ir_2_c_minus_a = 2 * (c_weyl_sq - a_euler)
    assert nb_minus_nf_untwisted == -6 and sen_ir_2_c_minus_a == Fr(-277, 360)

    ps_gens = []
    for i, j in list(itertools.combinations(range(6), 2)) + list(itertools.combinations(range(6, 10), 2)):
        gm = sp.zeros(10, 10)
        gm[i, j], gm[j, i] = 1, -1
        ps_gens.append(gm)
    vars_45 = []
    x_so10 = sp.zeros(10, 10)
    for i, j in itertools.combinations(range(10), 2):
        vs = sp.Symbol(f"x_{i}_{j}")
        vars_45.append(vs)
        x_so10[i, j], x_so10[j, i] = vs, -vs
    eqs_c = [cm_ij for gm in ps_gens for r_i in range(10) for cm_ij in [(x_so10 * gm - gm * x_so10)[r_i, c_i] for c_i in range(r_i + 1, 10)] if cm_ij != 0]
    ps_commutant_dim = len(set(vars_45) - set(sp.solve(eqs_c, vars_45).keys()))
    r_sym = sp.Symbol("r", rational=True)
    r10_sp = sp.solve(sp.Eq((sp.Rational(36, 5) - sp.Rational(4, 5) * r_sym) / (4 + 2 * r_sym), sp.Rational(7, 5)), r_sym)[0]
    r10_exact = Fr(int(r10_sp.p), int(r10_sp.q))
    assert ps_commutant_dim == 0 and r10_exact == Fr(4, 9)

    def integrate_collar(kf_val: mp.mpf, m_ltail: mp.mpf, steps_cell: int = 300) -> mp.mpf:
        h = mp_rat(1, steps_cell)
        psi = mp.mpf(1)
        tk = kf_val * mp.e
        for _ in range(4):
            for _ in range(steps_cell):
                k1 = -h * psi
                k2 = -h * (psi + k1 / 2)
                k3 = -h * (psi + k2 / 2)
                k4 = -h * (psi + k3)
                psi += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            psi *= tk
        nt = 600
        ht = (2 * m_ltail) / nt
        tf = mp.mpf(1)
        for _ in range(nt):
            k1 = -ht * tf
            k2 = -ht * (tf + k1 / 2)
            k3 = -ht * (tf + k2 / 2)
            k4 = -ht * (tf + k3)
            tf += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return psi + tf * (1 - psi)

    kf_s = mp_rat(3, 5)
    deep_err = abs(integrate_collar(kf_s, mp.mpf(16)) - (kf_s**4))
    short_leak = abs(integrate_collar(kf_s, mp_rat(1, 2)) - (kf_s**4))
    assert deep_err < mp.mpf(10) ** (-11) and short_leak > mp_rat(1, 20)

    return {
        "agy_exp_ref": AGY_EXP_REF,
        "agy_exp_sha256_files_and_entries": [exp_sha_files, exp_sha_entries],
        "agy_002_ref": AGY_002_REF,
        "agy_002_sha256_files_and_entries": [a02_sha_files, a02_sha_entries],
        "peer_new_py_zero_ast_float_count": peer_py_checked,
        "dd74b56c1_main_tex_eq_b1_t2_fixed": tex_has_fixed_t2,
        "dd74b56c1_main_tex_eq_b1_noncomm_swap_caught": eq_b1_swap_caught,
        "dd74b56c1_x_e6ps_link23_unique_ngen": unique_ngen,
        "dd74b56c1_x_e6ps_link23_r_lr_chiral_and_dparity": [f"{r_lr_chiral.numerator}/{r_lr_chiral.denominator}", f"{r_lr_dparity.numerator}/{r_lr_dparity.denominator}"],
        "2d993276b_ow20_line609_inverted_zeta3_caught": ow20_has_inverted_zeta3,
        "2d993276b_ow20_yb_inflation_factor": mp.nstr(ow20_yb_inflation_ratio, 10),
        "scope_unchecked_peer_modules": {
            "agy_c31_erratum_unchecked_in_c721af6ff_and_75cb20177": [
                "75cb20177:main.tex Eq. (B1) 2-loop Yukawa matrices (evaluated here in C35, catching +(3/4)[H_d,H_u] Y_u)",
                "c721af6ff OW18-A 2HDM RGEs, OW18-B Chimera FRG & +27% prose Higgs masses, OW18-D 72/2 bits, and git-history hash overwrites (subsequently remediated in 2d993276b)",
            ],
            "dd74b56c1_unchecked_modules": [
                "X-E6PS-LINK23 E1 full 351'_H Weyl-BFS coroot multiplicity table (Delta_R weight checked in C34)",
                "X-E6PS-LINK23 E3 2-loop G_LR RGE integration, E4 specific G_LR Yukawa textures, and E5 s-wave Majorana cross-section prefactor",
            ],
            "2d993276b_unchecked_modules": [
                "A2-OW19 / A2-OW20 2D hyperbolic Kahler overlap PDE grid integrations (rad_2d_e2_yb_2f_plus)",
                "A2-OW16 v6 prose observable narratives OBS-01..24 outside OBS-07, OBS-09, OBS-12, OBS-22",
            ],
        },
        "max_u1psi_anomaly_abs": max_anom_abs,
        "mr_forbidden_in_27H_only_Z4": mr_forbidden_in_27h_only,
        "q_seesaw_126bar_in_351prime": q_seesaw_126bar,
        "pm_delta126_even": pm_delta126,
        "bl_psiS_delta126_nonzero": bl_psiS_delta126,
        "q_yuk_antiholomorphic_forbidden": q_yuk_antihol,
        "pm_odd_exotic_fermion_count": pm_odd_exotic,
        "min_abs_q_psiS_renorm_obstruction": min_abs_q_psiS_renorm,
        "untwisted_brane_2hdm_6d_casimir_nB_minus_nF": nb_minus_nf_untwisted,
        "sen_ir_bh_2_c_minus_a_sm45": f"{sen_ir_2_c_minus_a.numerator}/{sen_ir_2_c_minus_a.denominator}",
        "ps_commutant_dim_in_so10": ps_commutant_dim,
        "e6_10F_threshold_r10_exact": f"{r10_exact.numerator}/{r10_exact.denominator}",
        "continuum_collar_deep_abs_err": deep_err,
        "no_chiS_mod9_at_n3": no_chiS_mod9_at_n3,
    }


# ---------------------------------------------------------------------------
# Section 2 (E2): Order-26 Lamé L_2, Complete MV84 Type-II 2HDM + 3 N_R RGEs,
# Dynamical (t_nu^*, t_EW^*) Horizons, Exact Y_{N_1}^{eq} & M_Pl, & Charm No-Go
# ---------------------------------------------------------------------------
def solve_l2_jacobi_taylor26(tau: mp.mpc, pre_reduce: bool = True, work_dps: int = 48) -> tuple[mp.mpf, mp.mpf]:
    old = mp.mp.dps
    mp.mp.dps = work_dps
    try:
        z = mp.mpc(tau)
        shift = mp.mpf(0)
        if pre_reduce:
            for _ in range(100):
                z -= int(mp.nint(mp.re(z)))
                if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-34):
                    shift -= mp.log(abs(z))
                    z = -mp.mpf(1) / z
                else:
                    break
            z_lat = z - int(mp.nint(mp.re(z)))
        else:
            z_lat = z

        q_nom = mp.exp(I_MP * mp.pi * z_lat)
        t20 = mp.jtheta(2, 0, q_nom)
        t30 = mp.jtheta(3, 0, q_nom)
        t40 = mp.jtheta(4, 0, q_nom)
        e1 = (mp.pi**2 / 3) * (t30**4 + t40**4)
        e2 = (mp.pi**2 / 3) * (t20**4 - t40**4)
        e3 = -(mp.pi**2 / 3) * (t20**4 + t30**4)
        g2 = 2 * (e1**2 + e2**2 + e3**2)
        g3 = 4 * e1 * e2 * e3
        pref_wpp = -2 * (mp.pi**3) * ((t20 * t30 * t40) ** 2)

        def wp_wpp_jt(zv: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
            nr = int(mp.nint(mp.im(zv) / mp.im(z_lat)))
            zc = zv - nr * z_lat
            zc -= int(mp.nint(mp.re(zc)))
            pz = mp.pi * zc
            t1 = mp.jtheta(1, pz, q_nom)
            t2 = mp.jtheta(2, pz, q_nom)
            t3 = mp.jtheta(3, pz, q_nom)
            t4 = mp.jtheta(4, pz, q_nom)
            return e1 + ((mp.pi * t30 * t40 * t2) / t1) ** 2, pref_wpp * (t2 * t3 * t4) / (t1**3)

        p_ord = 26
        qr = mp_rat(1, 4)

        def prop_taylor(nodes: list[mp.mpc], c_v: mp.mpc, want_dc: bool):
            T = mp.eye(2)
            dT = mp.zeros(2, 2)
            for idx in range(len(nodes) - 1):
                zk = nodes[idx]
                h = nodes[idx + 1] - zk
                p0, p1 = wp_wpp_jt(zk)
                pa = [mp.mpc(0)] * (p_ord + 1)
                pa[0], pa[1] = p0, p1
                pa[2] = 3 * (p0**2) - qr * g2
                for m in range(1, p_ord - 1):
                    pa[m + 2] = mp_rat(6, (m + 2) * (m + 1)) * mp.fsum(pa[j] * pa[m - j] for j in range(m + 1))
                qa = [qr * pa[m] for m in range(p_ord + 1)]
                qa[0] += c_v
                Tn = mp.zeros(2, 2)
                dTn = mp.zeros(2, 2)
                hp = [h**m for m in range(p_ord + 3)]
                for col in range(2):
                    wc = [mp.mpc(0)] * (p_ord + 3)
                    wc[0], wc[1] = T[0, col], T[1, col]
                    for m in range(p_ord + 1):
                        wc[m + 2] = -mp.fsum(qa[j] * wc[m - j] for j in range(m + 1)) / ((m + 2) * (m + 1))
                    Tn[0, col] = mp.fsum(wc[m] * hp[m] for m in range(p_ord + 3))
                    Tn[1, col] = mp.fsum(m * wc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                    if want_dc:
                        dwc = [mp.mpc(0)] * (p_ord + 3)
                        dwc[0], dwc[1] = dT[0, col], dT[1, col]
                        for m in range(p_ord + 1):
                            dwc[m + 2] = -(wc[m] + mp.fsum(qa[j] * dwc[m - j] for j in range(m + 1))) / ((m + 2) * (m + 1))
                        dTn[0, col] = mp.fsum(dwc[m] * hp[m] for m in range(p_ord + 3))
                        dTn[1, col] = mp.fsum(m * dwc[m] * hp[m - 1] for m in range(1, p_ord + 3))
                T, dT = Tn, dTn
            return (T, dT) if want_dc else T

        z0 = mp_rat(1, 2) + mp_rat(1, 2) * z_lat
        n_st = 64
        nds_a = [z0 + mp_rat(k, n_st) for k in range(n_st + 1)]
        nds_b = [z0 + mp_rat(k, n_st) * z_lat for k in range(n_st + 1)]
        c_val = mp.mpc((mp.pi**2) / 12)
        for _ in range(18):
            Ta, dTa = prop_taylor(nds_a, c_val, True)
            Tb, dTb = prop_taylor(nds_b, c_val, True)
            Tab = Ta * Tb
            dTab = dTa * Tb + Ta * dTb
            rv = [mp.im(Ta[0, 0] + Ta[1, 1]), mp.im(Tb[0, 0] + Tb[1, 1]), mp.im(Tab[0, 0] + Tab[1, 1])]
            if max(abs(x) for x in rv) < mp.mpf(10) ** (-36):
                break
            trs = [dTa[0, 0] + dTa[1, 1], dTb[0, 0] + dTb[1, 1], dTab[0, 0] + dTab[1, 1]]
            jr = [mp.im(t) for t in trs]
            ji = [mp.re(t) for t in trs]
            a11 = sum(x * x for x in jr)
            a12 = sum(jr[k] * ji[k] for k in range(3))
            a22 = sum(x * x for x in ji)
            b1 = -sum(jr[k] * rv[k] for k in range(3))
            b2 = -sum(ji[k] * rv[k] for k in range(3))
            det_a = a11 * a22 - a12 * a12
            c_val += mp.mpc((a22 * b1 - a12 * b2) / det_a, (a11 * b2 - a12 * b1) / det_a)

        Ta = prop_taylor(nds_a, c_val, False)
        Tb = prop_taylor(nds_b, c_val, False)
        assert max(abs(mp.im(M[0, 0] + M[1, 1])) for M in (Ta, Tb, Ta * Tb)) < mp.mpf(10) ** (-34)

        inv2 = lambda M: mp.matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]]) / (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0])
        mob = lambda T_m: mp.matrix([[T_m[1, 1], T_m[0, 1]], [T_m[1, 0], T_m[0, 0]]]) / mp.sqrt(T_m[1, 1] * T_m[0, 0] - T_m[0, 1] * T_m[1, 0])
        Tp = Tb * Ta * inv2(Tb) * inv2(Ta)
        Aa, P0 = mob(Ta), mob(Tp)
        pf = (P0[0, 0] - P0[1, 1]) / (2 * P0[1, 0])
        da = mp.sqrt((Aa[0, 0] - Aa[1, 1]) ** 2 + 4 * Aa[0, 1] * Aa[1, 0])
        fa1 = (Aa[0, 0] - Aa[1, 1] + da) / (2 * Aa[1, 0])
        fa2 = (Aa[0, 0] - Aa[1, 1] - da) / (2 * Aa[1, 0])
        ssc = (fa2 - fa1) / (fa2 - pf)
        g = mp.matrix([[mp.mpf(1) / ssc, -fa1 / ssc], [mp.mpf(1), -pf]])
        g = g / mp.sqrt(g[0, 0] * g[1, 1] - g[0, 1] * g[1, 0])
        if mp.im(g[0, 1] / g[1, 1]) < 0:
            g = mp.matrix([[I_MP, 0], [0, -I_MP]]) * g
        RP = g * P0 * inv2(g)
        lam = abs(mp.re(RP[0, 1] / RP[0, 0]))

        m_ord = 56
        laur = {1: g2 / 20, 2: g3 / 28}
        for n in range(3, m_ord // 2 + 2):
            laur[n] = mp_rat(3, (2 * n + 3) * (n - 2)) * mp.fsum(laur[m] * laur[n - 1 - m] for m in range(1, n - 1))
        qc = [mp.mpc(0)] * (m_ord + 1)
        qc[0] = c_val
        for n in range(1, m_ord // 2 + 1):
            qc[2 * n] = qr * laur[n]
        al = [mp.mpc(0)] * (m_ord + 1)
        be = [mp.mpc(0)] * (m_ord + 1)
        al[0] = mp.mpc(1)
        for m in range(1, m_ord + 1):
            al[m] = -mp.fsum(qc[j] * al[m - 2 - j] for j in range(m - 1)) / (m * m)
            be[m] = -(2 * m * al[m] + mp.fsum(qc[j] * be[m - 2 - j] for j in range(m - 1))) / (m * m)

        def eval_bc_at(den_r: int) -> mp.mpf:
            zs = mp_rat(1, den_r) * z0 / abs(z0)
            n_rad = 72
            rat_r = abs(zs) / abs(z0)
            nds_in = [z0 * (rat_r ** mp_rat(k, n_rad)) for k in range(n_rad + 1)]
            Tin = prop_taylor(nds_in, c_val, False)
            gloc = mp.fsum(be[m] * (zs**m) for m in range(m_ord + 1)) / mp.fsum(al[m] * (zs**m) for m in range(m_ord + 1))
            wzs = Tin[0, 1] / Tin[0, 0]
            uzs = (g[0, 0] * wzs + g[0, 1]) / (g[1, 0] * wzs + g[1, 1])
            imB = mp.im(uzs) + (lam / (2 * mp.pi)) * (mp.log(abs(zs)) + mp.re(gloc))
            return (2 * mp.pi / lam) * imB

        bc24 = eval_bc_at(24)
        bc36 = eval_bc_at(36)
        return (mp.pi - bc24) + shift, abs(bc24 - bc36)
    finally:
        mp.mp.dps = old


def eval_szego_yukawa_mp(tx: Fr, ty: Fr, l2_val: mp.mpf, pa: Fr, pb: Fr, ql: int, qr: int) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]

    t = mp.mpc(f2m(tx), f2m(ty))
    xr, yi = mp.re(t), mp.im(t)
    q = mp.exp(2 * I_MP * mp.pi * t)
    t2 = t3 = t4 = dt2 = dt3 = dt4 = mp.mpc(0)
    for n in range(-28, 29):
        m2 = mp_rat((2 * n + 1) ** 2, 8)
        e2v = mp.exp(2 * I_MP * mp.pi * t * m2)
        t2 += e2v
        dt2 += m2 * e2v
        m3 = mp_rat(n * n, 2)
        e3v = mp.exp(2 * I_MP * mp.pi * t * m3)
        t3 += e3v
        dt3 += m3 * e3v
        sg = -1 if (n % 2 != 0) else 1
        t4 += sg * e3v
        dt4 += sg * m3 * e3v
    e2s = mp.mpc(1)
    qn = q
    for n in range(1, 45):
        e2s -= 24 * n * (qn / (1 - qn))
        qn *= q
    l2d, l3d, l4d = dt2 / t2, dt3 / t3, dt4 / t4
    sh = (
        (-t2 / (t3 * t4)) * (l2d - l3d - l4d + e2s / 24) * qi
        + (-t4 / (t2 * t3)) * (l4d - l2d - l3d + e2s / 24) * qj
        + (I_MP * t3 / (t2 * t4)) * (l3d - l2d - l4d + e2s / 24) * qk
    )
    ct = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    pr = mp.mpc(1)
    qn = q
    for _ in range(45):
        pr *= 1 - qn
        qn *= q
    t1p = 2 * mp.pi * (mp.exp(I_MP * mp.pi * t / 12) * pr) ** 3
    csh = 2 * mp.pi * l2_val + mp.pi * mp.log(yi) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
    em2l = mp.exp(-2 * l2_val)

    def thc(ca: Fr, cb: Fr) -> mp.mpc:
        ta, tb = ca % 1, cb % 1
        nb = int(cb - tb)
        am, bm = f2m(ta), f2m(tb)
        zv = am * t + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        s = mp.fsum(mp.exp(I_MP * mp.pi * t * (mp.mpf(k) ** 2) + 2 * I_MP * mp.pi * mp.mpf(k) * zv) for k in range(n0 - 26, n0 + 27))
        b = mp.exp(I_MP * mp.pi * am * am * t + 2 * I_MP * mp.pi * am * bm) * s
        return b if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * b

    def a0fu(ai: Fr, bi: Fr) -> tuple[mp.mpf, mp.mpf]:
        al, be = ai % 1, bi % 1
        am, bm = f2m(al), f2m(be)
        zv = am * t + bm
        n0 = int(mp.nint(-mp.im(zv) / yi))
        vl = dr = mp.mpc(0)
        for dk in range(-26, 27):
            m = mp.mpf(n0 + dk) + hf
            trm = mp.exp(I_MP * mp.pi * t * m * m + 2 * I_MP * mp.pi * m * (zv + hf))
            vl -= trm
            dr -= (2 * I_MP * mp.pi * m) * trm
        a2 = abs(2 * I_MP * mp.pi * am + dr / vl) ** 2
        if al != 0:
            f0 = -mp.pi * (2 * mp.log(2) + mp.log(yi) + mp.digamma(am) + mp.digamma(1 - am))
        else:
            f0 = mp.pi * (2 * mp.euler - 2 * mp.log(2) - mp.log(yi)) + yi * (mp.pi**2) / (mp.sin(mp.pi * bm) ** 2)
        sm = mp.mpf(0)
        for k in range(-32, 33):
            m = am + k
            if m == 0:
                continue
            w = mp.exp(-2 * mp.pi * abs(m) * yi + 2 * I_MP * mp.pi * (m * xr + bm))
            sm += (2 * mp.pi / abs(m)) * mp.re(w / (1 - w))
        return a2, f0 + sm

    hf_r = Fr(1, 2)
    xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
    ap, am = xv[0] + yv[0], xv[0] - yv[0]
    bp, bm = (xv[1] + yv[1]) / 2, (xv[1] - yv[1]) / 2
    eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
    kap = {"1": -I_MP * eph, "i": mp.mpf(-1), "j": -eph, "k": I_MP}
    cs = {"1": (ap + hf_r, bp + hf_r), "i": (ap + hf_r, bp), "j": (ap, bp + hf_r), "k": (ap, bp)}
    ds = {"1": (am + hf_r, bm + hf_r), "i": (am + hf_r, bm), "j": (am, bm + hf_r), "k": (am, bm)}
    um = {}
    for sk in ("1", "i", "j", "k"):
        al, be = cs[sk][0] - hf_r, cs[sk][1] - hf_r
        dal, dbe = ds[sk][0] - hf_r, ds[sk][1] - hf_r
        if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
            um[sk] = mp.mpc(0)
            continue
        rv = kap[sk] * thc(cs[sk][0], cs[sk][1]) * thc(ds[sk][0], ds[sk][1]) / t1p
        a2, fv = a0fu(al, be)
        ag = csh + fv - mp.pi * a2 * em2l
        um[sk] = mp.sqrt(ag) * rv if ag > 0 else mp.mpc(0)
    mw = um["1"] * ed["1"] + um["i"] * ed["i"] + um["j"] * ed["j"] + um["k"] * ed["k"]
    return mp.matrix(
        [
            [
                ct[ra][cb][0, 0] * mw[0, 0] + ct[ra][cb][0, 1] * mw[0, 1] + ct[ra][cb][1, 0] * mw[1, 0] + ct[ra][cb][1, 1] * mw[1, 1]
                for cb in range(3)
            ]
            for ra in range(3)
        ]
    )


def rhs_complete_mv84_type2_2hdm_nu(st: tuple, ab: bool, dmr_coeff: int = 1, g2_same_override: mp.mpf | None = None) -> tuple:
    """Complete 2-loop Machacek-Vaughn (NPB 236 (1984) 221 Eq. 3.4) / Chowdhury-Eberhardt (arXiv:1503.08216)
    Type-II 2HDM + 3 N_R gauge + 3x3 Yukawa + 1-loop quartic/soft-mass RGEs, with Antusch et al.
    (PLB 525 (2002) 130 Eq. 16 & hep-ph/0501272 Eq. 17) Type-II Weinberg (+1/2) and Majorana (dmr_coeff=1) RGEs."""
    inv1 = 1 / (16 * (mp.pi**2))
    inv2 = inv1 * inv1
    z0c = mp.mpc(0)
    z3_l = [[z0c, z0c, z0c], [z0c, z0c, z0c], [z0c, z0c, z0c]]
    z3 = mp.zeros(3, 3)

    to3 = lambda M: [[M[0, 0], M[0, 1], M[0, 2]], [M[1, 0], M[1, 1], M[1, 2]], [M[2, 0], M[2, 1], M[2, 2]]]
    mul3 = lambda A, B: [[A[r][0] * B[0][c] + A[r][1] * B[1][c] + A[r][2] * B[2][c] for c in range(3)] for r in range(3)]
    hmul = lambda A: [[A[r][0] * mp.conj(A[c][0]) + A[r][1] * mp.conj(A[c][1]) + A[r][2] * mp.conj(A[c][2]) for c in range(3)] for r in range(3)]
    tr3 = lambda A: mp.re(A[0][0] + A[1][1] + A[2][2])

    g, yu_m, yd_m, ye_m, yni_m, mr_m, kap_m, lam, mh2, m12 = st
    yu, yd, ye = to3(yu_m), to3(yd_m), to3(ye_m)
    yn = to3(yni_m) if ab else z3_l
    g12, g22, g32 = g[0] ** 2, g[1] ** 2, g[2] ** 2
    gy2 = mp_rat(3, 5) * g12
    c_g2_same = g2_same_override if g2_same_override is not None else mp_rat(135, 16)

    hu, hd, he, hn = hmul(yu), hmul(yd), hmul(ye), (hmul(yn) if ab else z3_l)
    hu2, hd2, he2, hn2 = mul3(hu, hu), mul3(hd, hd), mul3(he, he), (mul3(hn, hn) if ab else z3_l)
    huhd, hdhu = mul3(hu, hd), mul3(hd, hu)
    hnhe, hehn = (mul3(hn, he), mul3(he, hn)) if ab else (z3_l, z3_l)

    tru, trd, tre, trn = tr3(hu), tr3(hd), tr3(he), (tr3(hn) if ab else mp.mpf(0))
    tru2, trd2, tre2, trn2 = tr3(hu2), tr3(hd2), tr3(he2), (tr3(hn2) if ab else mp.mpf(0))
    trud, trne = tr3(huhd), (tr3(hnhe) if ab else mp.mpf(0))
    tu, td = 3 * tru + trn, 3 * trd + tre

    b1 = [mp_rat(21, 5), mp.mpf(-3), mp.mpf(-7)]
    b2 = [
        [mp_rat(104, 25), mp_rat(18, 5), mp_rat(44, 5)],
        [mp_rat(6, 5), mp.mpf(8), mp.mpf(12)],
        [mp_rat(11, 10), mp_rat(9, 2), mp.mpf(-26)],
    ]
    fb = [
        mp_rat(17, 10) * tru + mp_rat(1, 2) * trd + mp_rat(3, 2) * tre + mp_rat(3, 10) * trn,
        mp_rat(3, 2) * (tru + trd) + mp_rat(1, 2) * (tre + trn),
        2 * (tru + trd),
    ]
    dg = [inv1 * b1[i] * (g[i] ** 3) + inv2 * (g[i] ** 3) * (sum(b2[i][j] * (g[j] ** 2) for j in range(3)) - fb[i]) for i in range(3)]

    l1, l2, l3, l4 = lam
    l34_sq = l3 * l3 + l3 * l4 + l4 * l4

    gam_phi2 = (
        (mp_rat(17, 8) * g12 + mp_rat(45, 8) * g22 + 20 * g32) * tru
        + (mp_rat(3, 8) * g12 + mp_rat(15, 8) * g22) * trn
        - mp_rat(9, 4) * (3 * tru2 + trn2)
        - mp_rat(3, 4) * (3 * trud + trne)
        + mp_rat(3, 2) * l2 * l2 + l34_sq
    )
    gam_phi1 = (
        (mp_rat(5, 8) * g12 + mp_rat(45, 8) * g22 + 20 * g32) * trd
        + (mp_rat(15, 8) * g12 + mp_rat(15, 8) * g22) * tre
        - mp_rat(9, 4) * (3 * trd2 + tre2)
        - mp_rat(3, 4) * (3 * trud + trne)
        + mp_rat(3, 2) * l1 * l1 + l34_sq
    )

    ew_u = mp_rat(1267, 600) * g12 * g12 - mp_rat(9, 20) * g12 * g22 + mp_rat(19, 15) * g12 * g32 - mp_rat(21, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
    ew_d = -mp_rat(113, 600) * g12 * g12 - mp_rat(27, 20) * g12 * g22 + mp_rat(31, 15) * g12 * g32 - mp_rat(21, 4) * g22 * g22 + 9 * g22 * g32 - 108 * g32 * g32
    ew_e = mp_rat(1449, 200) * g12 * g12 + mp_rat(27, 20) * g12 * g22 - mp_rat(21, 4) * g22 * g22
    ew_n = mp_rat(117, 200) * g12 * g12 - mp_rat(27, 20) * g12 * g22 - mp_rat(21, 4) * g22 * g22

    def comb_m(hf, hfp, hf2, hffp, hfp2, c_same, c_cross, d1, d2) -> list[list[mp.mpc]]:
        a1 = inv1 * mp_rat(3, 2) + inv2 * c_same
        a2 = inv1 * mp_rat(1, 2) + inv2 * c_cross
        b20 = inv2 * mp_rat(3, 2)
        b11 = -inv2 * mp_rat(1, 4)
        diag_s = inv1 * d1 + inv2 * d2
        return [
            [
                a1 * hf[r][c] + a2 * hfp[r][c] + b20 * hf2[r][c] + b11 * (hffp[r][c] + hfp2[r][c]) + (diag_s if r == c else z0c)
                for c in range(3)
            ]
            for r in range(3)
        ]

    ku = comb_m(hu, hd, hu2, huhd, hd2, mp_rat(223, 80) * g12 + c_g2_same * g22 + 16 * g32 - mp_rat(9, 4) * tu - 6 * l2, -mp_rat(41, 240) * g12 + mp_rat(33, 16) * g22 + mp_rat(16, 3) * g32 - mp_rat(3, 4) * td - 2 * l3 + 2 * l4, tu - mp_rat(17, 20) * g12 - mp_rat(9, 4) * g22 - 8 * g32, gam_phi2 + ew_u)
    kd = comb_m(hd, hu, hd2, hdhu, hu2, mp_rat(187, 80) * g12 + c_g2_same * g22 + 16 * g32 - mp_rat(9, 4) * td - 6 * l1, -mp_rat(53, 240) * g12 + mp_rat(33, 16) * g22 + mp_rat(16, 3) * g32 - mp_rat(3, 4) * tu - 2 * l3 + 2 * l4, td - mp_rat(1, 4) * g12 - mp_rat(9, 4) * g22 - 8 * g32, gam_phi1 + ew_d)
    ke = comb_m(he, hn, he2, hehn, hn2, mp_rat(387, 80) * g12 + c_g2_same * g22 - mp_rat(9, 4) * td - 6 * l1, mp_rat(33, 80) * g12 + mp_rat(33, 16) * g22 - mp_rat(3, 4) * tu - 2 * l3 + 2 * l4, td - mp_rat(9, 4) * g12 - mp_rat(9, 4) * g22, gam_phi1 + ew_e)

    dyu = mp.matrix(mul3(ku, yu))
    dyd = mp.matrix(mul3(kd, yd))
    dye = mp.matrix(mul3(ke, ye))
    if ab:
        kn_op = comb_m(hn, he, hn2, hnhe, he2, mp_rat(279, 80) * g12 + c_g2_same * g22 - mp_rat(9, 4) * tu - 6 * l2, mp_rat(21, 80) * g12 + mp_rat(33, 16) * g22 - mp_rat(3, 4) * td - 2 * l3 + 2 * l4, tu - mp_rat(9, 20) * g12 - mp_rat(9, 4) * g22, gam_phi2 + ew_n)
        dyn = mp.matrix(mul3(kn_op, yn))
        mr_l = to3(mr_m)
        ynh_yn = [[mp.conj(yn[0][r]) * yn[0][c] + mp.conj(yn[1][r]) * yn[1][c] + mp.conj(yn[2][r]) * yn[2][c] for c in range(3)] for r in range(3)]
        ynh_yn_t = [[ynh_yn[c][r] for c in range(3)] for r in range(3)]
        mk1, mk2 = mul3(mr_l, ynh_yn), mul3(ynh_yn_t, mr_l)
        sc_mr = dmr_coeff * inv1
        dmr = mp.matrix([[sc_mr * (mk1[r][c] + mk2[r][c]) for c in range(3)] for r in range(3)])
        dkap = z3
    else:
        dyn = z3
        dmr = z3
        kap_l = to3(kap_m)
        he_t = [[he[c][r] for c in range(3)] for r in range(3)]
        hk1, hk2 = mul3(he, kap_l), mul3(kap_l, he_t)
        d_kap_s = 2 * tu - 3 * g22 + 2 * l2
        hf_mp = mp_rat(1, 2)
        dkap = mp.matrix([[inv1 * (hf_mp * (hk1[r][c] + hk2[r][c]) + d_kap_s * kap_l[r][c]) for c in range(3)] for r in range(3)])

    c34 = mp_rat(3, 4)
    dl1 = inv1 * (12 * l1**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * td - 3 * gy2 - 9 * g22) * l1 + c34 * (gy2**2 + 2 * gy2 * g22 + 3 * g22**2) - 12 * trd2 - 4 * tre2)
    dl2 = inv1 * (12 * l2**2 + 4 * l3**2 + 4 * l3 * l4 + 2 * l4**2 + (4 * tu - 3 * gy2 - 9 * g22) * l2 + c34 * (gy2**2 + 2 * gy2 * g22 + 3 * g22**2) - 12 * tru2 - 4 * trn2)
    dl3 = inv1 * ((l1 + l2) * (6 * l3 + 2 * l4) + 4 * l3**2 + 2 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * g22) * l3 + c34 * (gy2**2 - 2 * gy2 * g22 + 3 * g22**2) - 12 * trud - 4 * trne)
    dl4 = inv1 * (2 * (l1 + l2) * l4 + 8 * l3 * l4 + 4 * l4**2 + (2 * tu + 2 * td - 3 * gy2 - 9 * g22) * l4 + 3 * gy2 * g22 + 12 * trud + 4 * trne)

    gew = mp_rat(9, 10) * g12 + mp_rat(9, 2) * g22
    dmh = [
        inv1 * ((6 * l1 + 2 * td - gew) * mh2[0] + (4 * l3 + 2 * l4) * mh2[1]),
        inv1 * ((6 * l2 + 2 * tu - gew) * mh2[1] + (4 * l3 + 2 * l4) * mh2[0]),
    ]
    dm12 = inv1 * (2 * l3 + 4 * l4 + tu + td - gew) * m12
    return (dg, dyu, dyd, dye, dyn, dmr, dkap, [dl1, dl2, dl3, dl4], dmh, dm12)


def add_st(sa: tuple, sb: tuple, cf: mp.mpf) -> tuple:
    return (
        [sa[0][i] + cf * sb[0][i] for i in range(3)],
        sa[1] + cf * sb[1],
        sa[2] + cf * sb[2],
        sa[3] + cf * sb[3],
        sa[4] + cf * sb[4],
        sa[5] + cf * sb[5],
        sa[6] + cf * sb[6],
        [sa[7][i] + cf * sb[7][i] for i in range(4)],
        [sa[8][0] + cf * sb[8][0], sa[8][1] + cf * sb[8][1]],
        sa[9] + cf * sb[9],
    )


def rk4_step(st: tuple, dt: mp.mpf, ab: bool, dmr_coeff: int = 1) -> tuple:
    k1 = rhs_complete_mv84_type2_2hdm_nu(st, ab, dmr_coeff)
    k2 = rhs_complete_mv84_type2_2hdm_nu(add_st(st, k1, dt / 2), ab, dmr_coeff)
    k3 = rhs_complete_mv84_type2_2hdm_nu(add_st(st, k2, dt / 2), ab, dmr_coeff)
    k4 = rhs_complete_mv84_type2_2hdm_nu(add_st(st, k3, dt), ab, dmr_coeff)
    cb = (
        [k1[0][i] + 2 * k2[0][i] + 2 * k3[0][i] + k4[0][i] for i in range(3)],
        k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1],
        k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2],
        k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3],
        k1[4] + 2 * k2[4] + 2 * k3[4] + k4[4],
        k1[5] + 2 * k2[5] + 2 * k3[5] + k4[5],
        k1[6] + 2 * k2[6] + 2 * k3[6] + k4[6],
        [k1[7][i] + 2 * k2[7][i] + 2 * k3[7][i] + k4[7][i] for i in range(4)],
        [k1[8][0] + 2 * k2[8][0] + 2 * k3[8][0] + k4[8][0], k1[8][1] + 2 * k2[8][1] + 2 * k3[8][1] + k4[8][1]],
        k1[9] + 2 * k2[9] + 2 * k3[9] + k4[9],
    )
    return add_st(st, cb, dt / 6)


def rk_rich_step(st: tuple, dt: mp.mpf, ab: bool, dmr_coeff: int = 1) -> tuple:
    sf = rk4_step(st, dt, ab, dmr_coeff)
    sm = rk4_step(st, dt / 2, ab, dmr_coeff)
    sh = rk4_step(sm, dt / 2, ab, dmr_coeff)
    return add_st(sf, add_st(sh, sf, mp.mpf(-1)), mp_rat(16, 15))


def verify_18_benchmark_coeffs_and_ow20_3x3(repo: Path) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Guardrail 4 Literature Benchmark Gate (R3):
    1) Verifies all 18 Chowdhury-Eberhardt / MV84 Type-II 2HDM + 3 N_R 2-loop coefficients at nonzero (g, lam, Y)!
    2) Verifies cross-seat 3x3 non-commuting trajectory agreement against 2d993276b:a2_ow20_results.json (< 10^-12)!
    3) Verifies Control 2: reverting 135/16 -> 33/16 breaks pure-top g_2^2 y_t^3 decoupling by exact 51/8!"""
    inv1 = 1 / (16 * (mp.pi**2))
    inv2 = inv1 * inv1
    z0 = mp.mpf(0)
    u1 = mp.mpf(1)
    u2 = mp.mpf(2)
    z3 = mp.zeros(3, 3)
    d3 = lambda v: mp.diag([z0, z0, v])

    def ex_u(g1: mp.mpf, g2: mp.mpf, g3: mp.mpf, yt: mp.mpf, yb: mp.mpf, ytau: mp.mpf, ynu: mp.mpf, lam: list[mp.mpf], g2_ov: mp.mpf | None = None) -> mp.mpf:
        dyu = rhs_complete_mv84_type2_2hdm_nu(([g1, g2, g3], d3(yt), d3(yb), d3(ytau), d3(ynu), z3, z3, lam, [z0, z0], z0), True, 1, g2_ov)[1]
        b1v = (mp_rat(9, 2) * yt**2 + mp_rat(1, 2) * yb**2 + ynu**2 - mp_rat(17, 20) * g1**2 - mp_rat(9, 4) * g2**2 - 8 * g3**2) * yt
        return mp.re((dyu[2, 2] - inv1 * b1v) / inv2)

    def ex_d(g1: mp.mpf, g2: mp.mpf, g3: mp.mpf, yt: mp.mpf, yb: mp.mpf, ytau: mp.mpf, ynu: mp.mpf, lam: list[mp.mpf]) -> mp.mpf:
        dyd = rhs_complete_mv84_type2_2hdm_nu(([g1, g2, g3], d3(yt), d3(yb), d3(ytau), d3(ynu), z3, z3, lam, [z0, z0], z0), True, 1)[2]
        b1v = (mp_rat(9, 2) * yb**2 + mp_rat(1, 2) * yt**2 + ytau**2 - mp_rat(1, 4) * g1**2 - mp_rat(9, 4) * g2**2 - 8 * g3**2) * yb
        return mp.re((dyd[2, 2] - inv1 * b1v) / inv2)

    def ex_n(g1: mp.mpf, g2: mp.mpf, g3: mp.mpf, yt: mp.mpf, yb: mp.mpf, ytau: mp.mpf, ynu: mp.mpf, lam: list[mp.mpf]) -> mp.mpf:
        dyn = rhs_complete_mv84_type2_2hdm_nu(([g1, g2, g3], d3(yt), d3(yb), d3(ytau), d3(ynu), z3, z3, lam, [z0, z0], z0), True, 1)[4]
        b1v = (mp_rat(5, 2) * ynu**2 + mp_rat(1, 2) * ytau**2 + 3 * yt**2 - mp_rat(9, 20) * g1**2 - mp_rat(9, 4) * g2**2) * ynu
        return mp.re((dyn[2, 2] - inv1 * b1v) / inv2)

    lz = [z0, z0, z0, z0]
    yt5 = ex_u(z0, z0, z0, u1, z0, z0, z0, lz)
    ub1 = ex_u(z0, z0, z0, u1, u1, z0, z0, lz) - yt5
    ub2 = ex_u(z0, z0, z0, u1, u2, z0, z0, lz) - yt5
    yt3_yb2 = (16 * ub1 - ub2) / 12
    yt_yb4 = (ub2 - 4 * ub1) / 12
    yt_yb2_ytau2 = ex_u(z0, z0, z0, u1, u1, u1, z0, lz) - ex_u(z0, z0, z0, u1, u1, z0, z0, lz)
    g2_yt3_decoup = ex_u(z0, u1, z0, u1, z0, z0, z0, lz) - ex_u(z0, u2, z0, u1, z0, z0, z0, lz) / 16 - mp_rat(15, 16) * yt5  # isolate g2^2 yt^3!
    # Simpler exact separation of g2^2 yt^3 and g2^4 yt using g2=1 and g2=2:
    ug2_1 = ex_u(z0, u1, z0, u1, z0, z0, z0, lz) - yt5
    ug2_2 = ex_u(z0, u2, z0, u1, z0, z0, z0, lz) - yt5
    c_g2_yt3 = (16 * ug2_1 - ug2_2) / 12        # exact 135/16 + 45/8 == 225/16!
    c_g2_4_u = (ug2_2 - 4 * ug2_1) / 12         # exact -21/4!
    ug2_1_bug = ex_u(z0, u1, z0, u1, z0, z0, z0, lz, mp_rat(33, 16)) - yt5
    ug2_2_bug = ex_u(z0, u2, z0, u1, z0, z0, z0, lz, mp_rat(33, 16)) - yt5
    bug_33_16_break = abs(c_g2_yt3 - (16 * ug2_1_bug - ug2_2_bug) / 12)  # exact 102/16 == 51/8!

    ug1_1 = ex_u(u1, z0, z0, u1, z0, z0, z0, lz) - yt5
    ug1_2 = ex_u(u2, z0, z0, u1, z0, z0, z0, lz) - yt5
    c_g1_yt3 = (16 * ug1_1 - ug1_2) / 12        # 223/80 + 17/8 == 393/80
    c_g1_4_u = (ug1_2 - 4 * ug1_1) / 12         # 1267/600

    c_g3_yb2_u = ex_u(z0, z0, u1, u1, u1, z0, z0, lz) - ex_u(z0, z0, u1, u1, z0, z0, z0, lz) - ub1   # 16/3
    c_g2_yb2_u = ex_u(z0, u1, z0, u1, u1, z0, z0, lz) - ex_u(z0, u1, z0, u1, z0, z0, z0, lz) - ub1   # 33/16
    c_g1_yb2_u = ex_u(u1, z0, z0, u1, u1, z0, z0, lz) - ex_u(u1, z0, z0, u1, z0, z0, z0, lz) - ub1   # -41/240
    c_g1_yt2_d = ex_d(u1, z0, z0, u1, u1, z0, z0, lz) - ex_d(u1, z0, z0, z0, u1, z0, z0, lz) - (ex_d(z0, z0, z0, u1, u1, z0, z0, lz) - ex_d(z0, z0, z0, z0, u1, z0, z0, lz))  # -53/240
    c_l2_yt3 = ex_u(z0, z0, z0, u1, z0, z0, z0, [z0, u1, z0, z0]) - yt5 - mp_rat(3, 2)               # -6
    c_l3_yb2 = ex_u(z0, z0, z0, u1, u1, z0, z0, [z0, z0, u1, z0]) - ex_u(z0, z0, z0, u1, u1, z0, z0, lz) - 1  # -2
    c_l4_yb2 = ex_u(z0, z0, z0, u1, u1, z0, z0, [z0, z0, z0, u1]) - ex_u(z0, z0, z0, u1, u1, z0, z0, lz) - 1  # +2

    # Neutrino 2-loop MV84 benchmarks:
    ynu5 = ex_n(z0, z0, z0, z0, z0, z0, u1, lz)                                                      # -3
    ng1_1 = ex_n(u1, z0, z0, z0, z0, z0, u1, lz) - ynu5
    ng1_2 = ex_n(u2, z0, z0, z0, z0, z0, u1, lz) - ynu5
    c_g1_ynu3 = (16 * ng1_1 - ng1_2) / 12       # 279/80 + 3/8 == 309/80
    c_g1_4_n = (ng1_2 - 4 * ng1_1) / 12         # 117/200
    c_g3_yt2_n = ex_n(z0, z0, u1, u1, z0, z0, u1, lz) - ex_n(z0, z0, u1, z0, z0, z0, u1, lz) - (ex_n(z0, z0, z0, u1, z0, z0, u1, lz) - ynu5)  # +20!

    errs_18 = [
        abs(yt5 - (-12)),
        abs(yt3_yb2 - mp_rat(-5, 2)),
        abs(yt_yb4 - mp_rat(-5, 2)),
        abs(yt_yb2_ytau2 - mp_rat(-3, 4)),
        abs(c_g2_yt3 - mp_rat(225, 16)),
        abs(c_g2_4_u - mp_rat(-21, 4)),
        abs(c_g1_yt3 - mp_rat(393, 80)),
        abs(c_g1_4_u - mp_rat(1267, 600)),
        abs(c_g3_yb2_u - mp_rat(16, 3)),
        abs(c_g2_yb2_u - mp_rat(33, 16)),
        abs(c_g1_yb2_u - mp_rat(-41, 240)),
        abs(c_g1_yt2_d - mp_rat(-53, 240)),
        abs(c_l2_yt3 - (-6)),
        abs(c_l3_yb2 - (-2)),
        abs(c_l4_yb2 - 2),
        abs(c_g1_ynu3 - mp_rat(309, 80)),
        abs(c_g1_4_n - mp_rat(117, 200)),
        abs(c_g3_yt2_n - 20),
    ]
    max_18_err = max(errs_18)

    # Cross-seat 3x3 non-commuting comparison against 2d993276b:relays/a2_ow20/a2_ow20_results.json!
    ow20_res = json.loads(git_show_bytes(repo, AGY_002_REF, "relays/a2_ow20/a2_ow20_results.json").decode("utf-8"))
    t_sec = ow20_res["OW20_A_type2_2hdm_rge_and_2flav_lepto"]["type2_2hdm_noncommuting_3x3_integration"]
    yu_b = mp.matrix([[mp_rat(1, 10), mp_rat(1, 20), 0], [mp_rat(1, 15), mp_rat(1, 5), mp_rat(1, 12)], [0, mp_rat(1, 25), mp_rat(3, 5)]])
    yd_b = mp.matrix([[mp_rat(1, 12), -mp_rat(1, 15), mp_rat(1, 30)], [mp_rat(1, 10), mp_rat(1, 4), 0], [mp_rat(1, 20), mp_rat(1, 16), mp_rat(2, 5)]])
    ye_b = mp.matrix([[mp_rat(1, 20), 0, 0], [0, mp_rat(1, 10), 0], [0, 0, mp_rat(3, 10)]])
    st_b = ([mp_rat(13, 25)] * 3, yu_b, yd_b, ye_b, z3, z3, z3, [mp_rat(1, 5), mp_rat(1, 4), mp_rat(1, 10), -mp_rat(1, 20)], [z0, z0], z0)
    hb = mp_rat(-10, 120)
    for _ in range(120):
        st_b = rk4_step(st_b, hb, False, 1)
    ow20_3x3_err = mp.mpf(0)
    for idx_m, key_m in ((1, "Yu_ir_N120"), (2, "Yd_ir_N120"), (3, "Ye_ir_N120")):
        grid = t_sec[key_m]
        for r in range(3):
            for c in range(3):
                peer_v = mp.mpc(mp.mpf(grid[r][c][0]), mp.mpf(grid[r][c][1]))
                ow20_3x3_err = max(ow20_3x3_err, abs(st_b[idx_m][r, c] - peer_v))

    return max_18_err, ow20_3x3_err, bug_33_16_break


def svd_asc(ym: mp.matrix) -> tuple[mp.matrix, list[mp.mpf]]:
    u_m, sv_m, _ = mp.svd_c(ym)
    oi = sorted(range(3), key=lambda k: sv_m[k])
    return mp.matrix([[u_m[r, oi[c]] for c in range(3)] for r in range(3)]), [sv_m[oi[c]] for c in range(3)]


def takagi_sym(M: mp.matrix) -> tuple[list[mp.mpf], mp.matrix]:
    H = M * M.H
    evs, V = mp.eighe(mp_rat(1, 2) * (H + H.H))
    om = sorted(range(3), key=lambda k: mp.re(evs[k]))
    sigs = []
    U = mp.zeros(3, 3)
    for co, idx in enumerate(om):
        mk = mp.sqrt(max(mp.mpf(0), mp.re(evs[idx])))
        sigs.append(mk)
        uk = V[:, idx]
        ukc = mp.matrix([mp.conj(uk[r]) for r in range(3)])
        ph = mp.exp(I_MP * mp.arg((uk.H * M * ukc)[0, 0]) / 2)
        for r in range(3):
            U[r, co] = uk[r] * ph
    return sigs, U


def solve_general_2hdm_ewsb(mh2_ir: list[mp.mpf], m12_ir: mp.mpf, lam_ir: list[mp.mpf]) -> tuple[mp.mpf, mp.mpf]:
    """Solve exact 2HDM EWSB stationary equations dV/dv_d = 0, dV/dv_u = 0 for general (m1^2, m2^2, m12^2):
      m1^2 v_d - m12^2 v_u + 1/2 l1 v_d^3 + 1/2 l34 v_d v_u^2 = 0
      m2^2 v_u - m12^2 v_d + 1/2 l2 v_u^3 + 1/2 l34 v_u v_d^2 = 0
    Reduces identically in 0 iterations to tan(beta) = (l1/l2)^{1/4} when mh2_ir == [0, 0]!"""
    l1, l2, l3, l4 = lam_ir
    l34 = l3 + l4
    tb0 = (l1 / l2) ** mp_rat(1, 4)
    pv0 = 2 * m12_ir / (mp.sqrt(l1 * l2) + l34)
    vd = mp.sqrt(pv0 / tb0)
    vu = vd * tb0
    for _ in range(14):
        f1 = mh2_ir[0] * vd - m12_ir * vu + mp_rat(1, 2) * l1 * (vd**3) + mp_rat(1, 2) * l34 * vd * (vu**2)
        f2 = mh2_ir[1] * vu - m12_ir * vd + mp_rat(1, 2) * l2 * (vu**3) + mp_rat(1, 2) * l34 * vu * (vd**2)
        if max(abs(f1), abs(f2)) <= mp.mpf(10) ** (-38) * max(m12_ir * vd, mp.mpf(10) ** (-80)):
            break
        j11 = mh2_ir[0] + mp_rat(3, 2) * l1 * (vd**2) + mp_rat(1, 2) * l34 * (vu**2)
        j22 = mh2_ir[1] + mp_rat(3, 2) * l2 * (vu**2) + mp_rat(1, 2) * l34 * (vd**2)
        j12 = -m12_ir + l34 * vd * vu
        det_j = j11 * j22 - j12 * j12
        vd -= (j22 * f1 - j12 * f2) / det_j
        vu -= (j11 * f2 - j12 * f1) / det_j
    return vd, vu


@dataclass(frozen=True)
class UVContinuousBoundary12:
    """Explicit inventory of all 12 assumed continuous UV dimensionless boundary parameters (Fixes D4):
    1..4:  lam1_over_g0sq, lam2_over_g0sq, lam3_over_g0sq, lam4_over_g0sq
    5..7:  m1_sq_over_m12_sq, m2_sq_over_m12_sq, ln_m12_sq_over_mgut2
    8:     ln_M0_over_mgut
    9:     bar_theta_uv_bare
    10..12: ln_fn_scale_u, ln_fn_scale_d, ln_fn_scale_e"""
    lam_over_g0sq: tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]
    m1_sq_over_m12_sq: mp.mpf
    m2_sq_over_m12_sq: mp.mpf
    ln_m12_sq_over_mgut2: mp.mpf
    ln_M0_over_mgut: mp.mpf
    bar_theta_uv_bare: mp.mpf
    ln_fn_scales_ude: tuple[mp.mpf, mp.mpf, mp.mpf]


def default_uv_boundary_12() -> UVContinuousBoundary12:
    z0 = mp.mpf(0)
    return UVContinuousBoundary12(
        lam_over_g0sq=(mp_rat(2, 5), mp_rat(2, 5), mp_rat(1, 10), -mp_rat(1, 2)),
        m1_sq_over_m12_sq=z0,
        m2_sq_over_m12_sq=z0,
        ln_m12_sq_over_mgut2=-mp_rat(96, 5) * mp.pi,
        ln_M0_over_mgut=-mp_rat(16, 5) * mp.pi,
        bar_theta_uv_bare=z0,
        ln_fn_scales_ude=(z0, z0, z0),
    )


def eval_full_v7_pipeline(
    base_uv_mats: tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    l2_tau8: mp.mpf,
    uv_p: UVContinuousBoundary12,
    n_steps: int,
    mr_unit_basis: mp.matrix | None = None,
    dmr_coeff: int = 1,
    mu_gut_anchor: mp.mpf | None = None,
    unscaled_bad_anchor: bool = False,
    euler_coarse: bool = False,
    fixed_horizons: tuple[mp.mpf, mp.mpf] | None = None,
) -> tuple[dict[str, dict[str, mp.mpf]], mp.mpf, tuple[mp.mpf, mp.mpf], mp.mpf, mp.mpf]:
    """Evaluates all 50 dimensionless observables with:
      - Dynamical self-consistent seesaw threshold t_nu^* = ln(M_1(t_nu^*) / M_GUT)
      - Dynamical self-consistent EWSB horizon t_EW^* = ln(v_EW(t_EW^*) / M_GUT)
      - Connected mgut_vew = M_GUT / v_EW (never hardcoded separately!)
      - Explicit energy-unit scaling mu_gut_anchor (to test homogeneity degree 1 of v_EW and degree 0 of all 50 ratios!)"""
    mu0 = mu_gut_anchor if mu_gut_anchor is not None else mp.mpf(1)
    s_u, s_d, s_e = [mp.exp(x) for x in uv_p.ln_fn_scales_ude]
    yu0 = s_u * base_uv_mats[0]
    yd0 = s_d * base_uv_mats[1]
    ye0 = s_e * base_uv_mats[2]
    yn0 = base_uv_mats[3].copy()

    r_m0 = mp.exp(uv_p.ln_M0_over_mgut)
    r_m12_sq = mp.exp(uv_p.ln_m12_sq_over_mgut2)
    mr_basis = mr_unit_basis if mr_unit_basis is not None else mp.eye(3)
    # Dimensionful UV masses in units of arbitrary energy unit (M_GUT = mu0):
    mr_uv = (r_m0 * mu0) * mr_basis
    # Planted Control 3c: if unscaled_bad_anchor is True, forget to scale m12_uv by mu0^2 (smuggling a 2nd anchor mu=1!):
    m12_uv = r_m12_sq * (mp.mpf(1) if unscaled_bad_anchor else (mu0**2))
    mh2_uv = [uv_p.m1_sq_over_m12_sq * m12_uv, uv_p.m2_sq_over_m12_sq * m12_uv]

    g0_sq = mp.pi / 10
    g0 = mp.sqrt(g0_sq)
    lam0 = [c * g0_sq for c in uv_p.lam_over_g0sq]
    z3 = mp.zeros(3, 3)

    na = max(1, n_steps // 3)
    nb = max(1, n_steps - na)

    def integrate_above_n(t_nu_v: mp.mpf, na_loc: int) -> tuple:
        st_a = ([g0, g0, g0], yu0.copy(), yd0.copy(), ye0.copy(), yn0.copy(), mr_uv.copy(), z3.copy(), list(lam0), list(mh2_uv), m12_uv)
        dta = t_nu_v / na_loc
        for _ in range(na_loc):
            st_a = add_st(st_a, rhs_complete_mv84_type2_2hdm_nu(st_a, True, dmr_coeff), dta) if euler_coarse else rk_rich_step(st_a, dta, True, dmr_coeff)
        return st_a

    def resid_tnu(t_v: mp.mpf, na_loc: int) -> tuple[mp.mpf, tuple, list[mp.mpf], mp.matrix]:
        st_loc = integrate_above_n(t_v, na_loc)
        mr_s = mp_rat(1, 2) * (st_loc[5] + st_loc[5].T)
        mm_loc, ut_loc = takagi_sym(mr_s)
        return mp.log(mm_loc[0] / mu0) - t_v, st_loc, mm_loc, ut_loc

    if fixed_horizons is not None:
        t_nu_star, t_ew_star = fixed_horizons
        _, st_tnu, mmaj_tnu, utak_tnu = resid_tnu(t_nu_star, na)
        mr_sym_tnu = mp_rat(1, 2) * (st_tnu[5] + st_tnu[5].T)
    else:
        # Warm-start at coarse grid when na > 8, then refine with superlinear secant on exact na grid (< 10^-37 in 2-3 steps!):
        t_a0 = uv_p.ln_M0_over_mgut
        na_init = min(na, 6) if not euler_coarse else na
        ra0, _, _, _ = resid_tnu(t_a0, na_init)
        t_a1 = t_a0 + ra0
        if not euler_coarse and na > na_init:
            for _ in range(4):
                ra1, _, _, _ = resid_tnu(t_a1, na_init)
                if abs(ra1) < mp.mpf(10) ** (-24) or abs(ra1 - ra0) == 0:
                    break
                t_a0, ra0, t_a1 = t_a1, ra1, t_a1 - ra1 * (t_a1 - t_a0) / (ra1 - ra0)
            t_a0 = t_a1
            ra0, st_tnu, mmaj_tnu, utak_tnu = resid_tnu(t_a0, na)
            t_a1 = t_a0 + ra0
        for _ in range(7):
            ra1, st_tnu, mmaj_tnu, utak_tnu = resid_tnu(t_a1, na)
            if abs(ra1) < mp.mpf(10) ** (-37) or euler_coarse or abs(ra1 - ra0) == 0:
                t_nu_star = t_a1
                break
            t_a0, ra0, t_a1 = t_a1, ra1, t_a1 - ra1 * (t_a1 - t_a0) / (ra1 - ra0)
        else:
            t_nu_star = t_a1
            _, st_tnu, mmaj_tnu, utak_tnu = resid_tnu(t_nu_star, na)
        mr_sym_tnu = mp_rat(1, 2) * (st_tnu[5] + st_tnu[5].T)

    ye_tnu, yn_tnu = st_tnu[3].copy(), st_tnu[4].copy()
    # Note: kap_m has canonical dimension M^-1 (since mr_sym_tnu ~ mu0)!
    kap_m = -yn_tnu * (mr_sym_tnu ** (-1)) * yn_tnu.T

    def integrate_below_n(t_ew_v: mp.mpf, nb_loc: int) -> tuple:
        st_b = (list(st_tnu[0]), st_tnu[1].copy(), st_tnu[2].copy(), st_tnu[3].copy(), z3.copy(), z3.copy(), kap_m.copy(), list(st_tnu[7]), list(st_tnu[8]), st_tnu[9])
        dtb = (t_ew_v - t_nu_star) / nb_loc
        for _ in range(nb_loc):
            st_b = add_st(st_b, rhs_complete_mv84_type2_2hdm_nu(st_b, False, dmr_coeff), dtb) if euler_coarse else rk_rich_step(st_b, dtb, False, dmr_coeff)
        return st_b

    def resid_tew(t_v: mp.mpf, nb_loc: int) -> tuple[mp.mpf, tuple, mp.mpf, mp.mpf]:
        st_loc = integrate_below_n(t_v, nb_loc)
        vd_l, vu_l = solve_general_2hdm_ewsb(st_loc[8], st_loc[9], st_loc[7])
        return mp.log(mp.sqrt(vd_l**2 + vu_l**2) / mu0) - t_v, st_loc, vd_l, vu_l

    if fixed_horizons is None:
        t0_g = uv_p.ln_m12_sq_over_mgut2 / 2
        nb_init = min(nb, 12) if not euler_coarse else nb
        r0_g, _, _, _ = resid_tew(t0_g, nb_init)
        t1_g = t0_g + r0_g
        if not euler_coarse and nb > nb_init:
            for _ in range(6):
                r1_g, _, _, _ = resid_tew(t1_g, nb_init)
                if abs(r1_g) < mp.mpf(10) ** (-24) or abs(r1_g - r0_g) == 0:
                    break
                t0_g, r0_g, t1_g = t1_g, r1_g, t1_g - r1_g * (t1_g - t0_g) / (r1_g - r0_g)
            t0_g = t1_g
            r0_g, st_ir, vd, vu = resid_tew(t0_g, nb)
            t1_g = t0_g + r0_g
        for _ in range(8):
            r1_g, st_ir, vd, vu = resid_tew(t1_g, nb)
            if abs(r1_g) < mp.mpf(10) ** (-37) or euler_coarse or abs(r1_g - r0_g) == 0:
                t_ew_star = t1_g
                break
            t0_g, r0_g, t1_g = t1_g, r1_g, t1_g - r1_g * (t1_g - t0_g) / (r1_g - r0_g)
        else:
            t_ew_star = t1_g
            _, st_ir, vd, vu = resid_tew(t_ew_star, nb)
    else:
        _, st_ir, vd, vu = resid_tew(t_ew_star, nb)

    gf, yuf, ydf, yef, _, _, kapf, lamf, mh2_ir, m12_ir = st_ir
    vew_dim = mp.sqrt(vd**2 + vu**2)  # dimensionful v_EW in same units as mu0!
    mgut_over_vew = mu0 / vew_dim     # DYNAMICALLY CONNECTED M_GUT / v_EW (Fixes D4.1!)
    horizon_resid = max(abs(mp.log(mmaj_tnu[0] / mu0) - t_nu_star), abs(mp.log(vew_dim / mu0) - t_ew_star))

    uu, su = svd_asc(yuf)
    ud, sd = svd_asc(ydf)
    ue, se = svd_asc(yef)
    un, sn = svd_asc(kapf)
    vc = uu.H * ud
    up = ue.H * un
    jc = abs(mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1])))
    jp = abs(mp.im(up[0, 1] * up[1, 2] * mp.conj(up[0, 2]) * mp.conj(up[1, 1])))
    bar_theta_raw = mp.arg(mp.det(yuf * ydf)) + uv_p.bar_theta_uv_bare

    l1, l2, l3, l4 = lamf
    l34 = l3 + l4
    bfb = min(l1, l2, l34 + mp.sqrt(l1 * l2))
    tb = vu / vd
    ia = [(4 * mp.pi) / (x * x) for x in gf]
    wmix = (mp_rat(3, 5) * (gf[0] ** 2)) / ((gf[1] ** 2) + mp_rat(3, 5) * (gf[0] ** 2))
    # Light Majorana neutrino masses m_{nu,i} / v_EW = 1/2 sigma_i(kap) v_u^2 / v_EW:
    mnu_vew = [mp_rat(1, 2) * s_i * (vu**2) / vew_dim for s_i in sn]
    evn = [m_i * m_i for m_i in mnu_vew]

    msbar = {
        "u_m1_over_m3": su[0] / su[2],
        "u_m2_over_m3": su[1] / su[2],
        "d_m1_over_m3": sd[0] / sd[2],
        "d_m2_over_m3": sd[1] / sd[2],
        "e_m1_over_m3": se[0] / se[2],
        "e_m2_over_m3": se[1] / se[2],
        "u3_over_d3": tb * su[2] / sd[2],
        "d3_over_e3": sd[2] / se[2],
        "ckm_v12": abs(vc[0, 1]),
        "ckm_v23": abs(vc[1, 2]),
        "ckm_v13": abs(vc[0, 2]),
        "ckm_jarlskog": jc,
        "pmns_u12": abs(up[0, 1]),
        "pmns_u23": abs(up[1, 2]),
        "pmns_u13": abs(up[0, 2]),
        "pmns_jarlskog": jp,
        "nu_dm21_sq_over_dm31_sq": (evn[1] - evn[0]) / (evn[2] - evn[0]),
        "strong_cp_bar_theta_qcd_raw_rad": bar_theta_raw,
        "gauge_slope_2loop": (ia[0] - ia[1]) / (ia[1] - ia[2]),
        "tan_beta_ewsb": tb,
        "quartic_bfb_margin": bfb,
        "electroweak_mix_ratio": wmix,
    }

    cb, sb = vd / vew_dim, vu / vew_dim
    mu3_ms = su[2] * sb / mp.sqrt(2)
    mc_ms = su[1] * sb / mp.sqrt(2)
    md3_ms = sd[2] * cb / mp.sqrt(2)
    me3_ms = se[2] * cb / mp.sqrt(2)
    gy2, gw2 = mp_rat(3, 5) * (gf[0] ** 2), gf[1] ** 2
    a3_ir = (gf[2] ** 2) / (4 * mp.pi)
    aqed_ir = (gy2 * gw2) / (4 * mp.pi * (gw2 + gy2))
    mu3_pole = mu3_ms * (1 + (a3_ir / mp.pi) * (mp_rat(4, 3) - 2 * mp.log(mu3_ms)))
    me3_pole = me3_ms * (1 + (aqed_ir / mp.pi) * (1 - mp_rat(3, 2) * mp.log(me3_ms)))
    den_5f = 1 + mp_rat(23, 6) * (a3_ir / mp.pi) * mp.log(md3_ms)
    a3_b = a3_ir / den_5f
    md3_low = md3_ms * ((a3_b / a3_ir) ** mp_rat(12, 23))
    md3_pole = md3_low * (1 + mp_rat(4, 3) * (a3_b / mp.pi))

    ma0_sq = m12_ir * (vu / vd + vd / vu)
    ma0_v = mp.sqrt(ma0_sq) / vew_dim
    mhpm_v = mp.sqrt(ma0_sq - mp_rat(1, 2) * l4 * (vew_dim**2)) / vew_dim
    j11 = mh2_ir[0] + mp_rat(3, 2) * l1 * (vd**2) + mp_rat(1, 2) * l34 * (vu**2)
    j22 = mh2_ir[1] + mp_rat(3, 2) * l2 * (vu**2) + mp_rat(1, 2) * l34 * (vd**2)
    j12 = -m12_ir + l34 * vd * vu
    ev_ev, _ = mp.eighe(mp.matrix([[j11, j12], [j12, j22]]))
    evs_s = sorted([mp.re(x) for x in ev_ev])
    v_quad = mp_rat(1, 2) * mh2_ir[0] * (vd**2) + mp_rat(1, 2) * mh2_ir[1] * (vu**2) - m12_ir * vd * vu
    v_quart = mp_rat(1, 8) * l1 * (vd**4) + mp_rat(1, 8) * l2 * (vu**4) + mp_rat(1, 4) * l34 * (vd**2) * (vu**2)
    vmin_vew4 = (v_quad + v_quart) / (vew_dim**4)

    # Caswell-Jones 2-loop Lambda_QCD^(5f, 4f) / v_EW + Honest Charm No-Go (m_c < Lambda_QCD^(4f), Fixes D3):
    def run_a3_rich(a_st: mp.mpf, mu_st: mp.mpf, mu_en: mp.mpf, nf_q: int) -> mp.mpf:
        b0_q = mp_rat(33 - 2 * nf_q, 3)
        b1_q = mp_rat(306 - 38 * nf_q, 3)
        rhs_q = lambda x: -(b0_q / (2 * mp.pi)) * (x**2) - (b1_q / (8 * (mp.pi**2))) * (x**3)

        def rk4_q(n_q: int) -> mp.mpf:
            dt_q = mp.log(mu_en / mu_st) / n_q
            av = a_st
            for _ in range(n_q):
                if euler_coarse:
                    av += dt_q * rhs_q(av)
                else:
                    k1q = dt_q * rhs_q(av)
                    k2q = dt_q * rhs_q(av + k1q / 2)
                    k3q = dt_q * rhs_q(av + k2q / 2)
                    k4q = dt_q * rhs_q(av + k3q)
                    av += (k1q + 2 * k2q + 2 * k3q + k4q) / 6
            return av

        nq_base = max(4, n_steps)
        return rk4_q(nq_base) if euler_coarse else (16 * rk4_q(2 * nq_base) - rk4_q(nq_base)) / 15

    def lam_qcd_2l(mu_q: mp.mpf, av: mp.mpf, nf_q: int) -> mp.mpf:
        b0_q = mp_rat(33 - 2 * nf_q, 3)
        b1_q = mp_rat(306 - 38 * nf_q, 3)
        ex_q = b1_q / (2 * (b0_q**2))
        return mu_q * mp.exp(-2 * mp.pi / (b0_q * av)) * (((b0_q * av) / (4 * mp.pi)) ** (-ex_q)) * ((1 + (b1_q * av) / (4 * mp.pi * b0_q)) ** ex_q)

    lam_5f_vew = lam_qcd_2l(mp.mpf(1), a3_ir, 5)
    a3_at_mb = run_a3_rich(a3_ir, mp.mpf(1), md3_ms, 5)
    lam_4f_vew = lam_qcd_2l(md3_ms, a3_at_mb, 4)
    mc_over_lam4f = mc_ms / lam_4f_vew
    if not euler_coarse and not unscaled_bad_anchor:
        assert mc_over_lam4f < mp_rat(1, 10)  # Charm is >10x below Lambda_QCD^(4f): honest perturbative n_f=3 No-Go!

    pole_2hdm = {
        "u3_pole_over_vew": mu3_pole,
        "d3_low_over_e3_pole": md3_low / me3_pole,
        "d3_pole_over_e3_pole": md3_pole / me3_pole,
        "strong_coupling_ir": a3_ir,
        "qed_coupling_ir": aqed_ir,
        "qcd_Lambda_5f_over_vew": lam_5f_vew,
        "qcd_Lambda_4f_over_vew": lam_4f_vew,
        "mc_msbar_over_qcd_Lambda_4f": mc_over_lam4f,
        "mw_over_vew": mp_rat(1, 2) * gf[1],
        "mz_over_vew": mp_rat(1, 2) * mp.sqrt(gw2 + gy2),
        "higgs_h0_over_vew": mp.sqrt(evs_s[0]) / vew_dim,
        "higgs_H0_over_vew": mp.sqrt(evs_s[1]) / vew_dim,
        "higgs_A0_over_vew": ma0_v,
        "higgs_Hpm_over_vew": mhpm_v,
        "ewsb_vmin_over_vew4": vmin_vew4,
    }

    # Exact 11D M-theory topological quantization & dimensionful fiber volumes (Fixes C35 D1):
    #   2 kappa_11^2 = 16 pi G_11 = (2 pi)^8 M_11^-9 and 2 kappa_11^2 T_M2^3 = (2 pi)^2 => T_M2 = M_11^3 / (2 pi)^2.
    #   Matching S_M2 = T_M2 V_3^dim = 2 pi * 40 with V_3^dim = 8 Vol(m004) M_GUT^-3 gives:
    #     (M_11 / M_GUT)^3 = 40 (2 pi)^3 / (8 Vol(m004)).
    #   In M_Pl^2 = G_4^-1 = 8 M_11^9 V_3^dim V_4^dim / (2 pi)^7:
    #     Self-dual (R_perp = M_11^-1 => V_4^dim = ((2 pi)^4 / 48) M_11^-4): M_11^9 M_GUT^-3 M_11^-4 = M_GUT^2 (M_11 / M_GUT)^5
    #     Isotropic (R_perp = M_GUT^-1 => V_4^dim = ((2 pi)^4 / 48) M_GUT^-4): M_11^9 M_GUT^-3 M_GUT^-4 = M_GUT^2 (M_11 / M_GUT)^9
    vol41 = 3 * mp.im(mp.polylog(2, mp.exp(2 * I_MP * mp.pi / 3)))
    m11_mgut = (40 * ((2 * mp.pi) ** 3) / (8 * vol41)) ** mp_rat(1, 3)
    vp_hat = ((2 * mp.pi) ** 4) / 48
    mpl_mgut_sd = mp.sqrt(8 * (m11_mgut**5) * (8 * vol41) * vp_hat / ((2 * mp.pi) ** 7))
    mpl_mgut_iso = mp.sqrt(8 * (m11_mgut**9) * (8 * vol41) * vp_hat / ((2 * mp.pi) ** 7))
    mbar_pl_mgut_sd = mpl_mgut_sd / mp.sqrt(8 * mp.pi)
    mpl_vew_sd = mpl_mgut_sd * mgut_over_vew
    mpl_vew_iso = mpl_mgut_iso * mgut_over_vew
    bc_star_tau8 = mp.pi - l2_tau8

    grav = {
        "cusp_robin_bc_star_tau8": bc_star_tau8,
        "m11_over_mgut_zero_knob": m11_mgut,
        "mpl_over_vew_d4_hurwitz_self_dual": mpl_vew_sd,
        "gn_vew_sq_d4_hurwitz_self_dual": 1 / (mpl_vew_sd**2),
        "mpl_over_vew_d4_hurwitz_isotropic": mpl_vew_iso,
        "gn_vew_sq_d4_hurwitz_isotropic": 1 / (mpl_vew_iso**2),
    }

    ue_tnu, se_tnu = svd_asc(ye_tnu)
    maj_split_21 = (mmaj_tnu[1] - mmaj_tnu[0]) / mmaj_tnu[0]
    utak_c = mp.matrix([[mp.conj(utak_tnu[r, c]) for c in range(3)] for r in range(3)])
    Yt = ue_tnu.H * yn_tnu * utak_c
    Ht = Yt.H * Yt
    h00 = mp.re(Ht[0, 0])
    efl = [mp.mpf(0)] * 3
    for j in (1, 2):
        xv = (mmaj_tnu[j] / mmaj_tnu[0]) ** 2
        gm = mp.re(Ht[j, j]) / (8 * mp.pi)
        dn = (xv - 1) ** 2 + xv * (gm**2)
        f_sv = mp.sqrt(xv) * ((1 - xv) / dn + 1 - (1 + xv) * mp.log(1 + 1 / xv))
        g_os = (1 - xv) / dn
        for al in range(3):
            p1j = mp.conj(Yt[al, 0]) * Yt[al, j]
            efl[al] += (mp.im(p1j * Ht[0, j]) * f_sv + mp.im(p1j * Ht[j, 0]) * g_os) / (8 * mp.pi * h00)
    pbr = [abs(Yt[a, 0]) ** 2 / h00 for a in range(3)]
    g_star = mp_rat(443, 4)
    # Friedmann H(M_1) / M_1 = sqrt(pi^2 g_* / 90) * (M_1 / bar{M}_Pl) with reduced bar{M}_Pl = M_Pl / sqrt(8 pi) (Fixes D2.2!):
    m1_over_mgut = mmaj_tnu[0] / mu0
    hub_over_m1 = mp.sqrt((mp.pi**2) * g_star / 90) * (m1_over_mgut / mbar_pl_mgut_sd)
    k1_tot = (h00 / (8 * mp.pi)) / hub_over_m1
    gam_tau_h = (mp_rat(5, 1000) * (se_tnu[2] ** 2)) / hub_over_m1
    gam_mu_h = (mp_rat(5, 1000) * (se_tnu[1] ** 2)) / hub_over_m1
    if not euler_coarse and not unscaled_bad_anchor:
        assert gam_tau_h > mp.mpf(1) and gam_mu_h < mp_rat(1, 100)
    eta_tau = 1 / (1 + (pbr[2] * k1_tot) ** mp_rat(29, 25))
    eta_tau_perp = 1 / (1 + ((pbr[0] + pbr[1]) * k1_tot) ** mp_rat(29, 25))
    # Exact relativistic Majorana yield Y_{N_1}^{eq} = n_{N_1}^{eq} / s = 135 zeta(3) / (4 pi^4 g_*) (Fixes D2.1!):
    neq = (135 * mp.zeta(3)) / (4 * (mp.pi**4) * g_star)
    yb_val = -mp_rat(8, 23) * neq * (efl[2] * eta_tau + (efl[0] + efl[1]) * eta_tau_perp)

    y_end_inf = 1 + 2 / mp.sqrt(3)
    y_inf = mp.mpf(82)
    for _ in range(20):
        y_inf -= (mp_rat(3, 4) * ((y_inf - y_end_inf) - mp.log(y_inf / y_end_inf)) - 60) / (mp_rat(3, 4) * (1 - 1 / y_inf))
    eps_60 = mp_rat(4, 3) / ((y_inf - 1) ** 2)
    eta_60 = -mp_rat(4, 3) * (y_inf - 2) / ((y_inf - 1) ** 2)
    ns_60 = 1 - 6 * eps_60 + 2 * eta_60
    r_60 = 16 * eps_60

    cosmo = {
        "proton_decay_dim6_mgut_over_vew_pow4": mgut_over_vew**4,
        "leptogenesis_Y_B_2flavor_analytic_fit": yb_val,
        "leptogenesis_eps_1_tau": efl[2],
        "leptogenesis_washout_K1_tot": k1_tot,
        "leptogenesis_tau_equil_over_hubble": gam_tau_h,
        "inflation_conformal_S4_ns_N60": ns_60,
        "inflation_conformal_S4_r_N60": r_60,
    }
    return (
        {
            "sm_msbar_at_ew_horizon": msbar,
            "sm_1loop_pole_and_2hdm_bosons": pole_2hdm,
            "gravity_11d_d4_hurwitz_sector": grav,
            "cosmology_crv_and_honest_bounds": cosmo,
        },
        maj_split_21,
        (t_nu_star, t_ew_star),
        vew_dim,
        horizon_resid,
    )


def pseudo_haar_su3_mp(seed: int) -> mp.matrix:
    Z = mp.zeros(3, 3)
    idx = 1
    for r in range(3):
        for c in range(3):
            u1 = mp_rat(1, 1000) + mp_rat(998, 1000) * ((mp.sin(mp.mpf(seed * 37 + idx * 13)) + 1) / 2)
            u2 = (mp.cos(mp.mpf(seed * 53 + idx * 29)) + 1) / 2
            rad = mp.sqrt(-2 * mp.log(u1))
            ang = 2 * mp.pi * u2
            Z[r, c] = rad * (mp.cos(ang) + I_MP * mp.sin(ang))
            idx += 1
    Q = mp.zeros(3, 3)
    for j in range(3):
        v = Z[:, j]
        for k in range(j):
            qk = Q[:, k]
            v = v - (qk.H * v)[0, 0] * qk
        nm = mp.sqrt(mp.re((v.H * v)[0, 0]))
        for r in range(3):
            Q[r, j] = v[r] / nm
    return mp.exp(-I_MP * mp.arg(mp.det(Q)) / 3) * Q


# ---------------------------------------------------------------------------
# Section 3 (E3): Lefschetz 144 -> 4 Solver, Live 50x12 UV Jacobian SVD Rank,
# & Aligned 39/2 (core 48) / 41/2 (full 50) Discrete Topology Ledger
# ---------------------------------------------------------------------------
def solve_lefschetz_monodromy_kernels() -> tuple[tuple[Fr, Fr], tuple[Fr, Fr], int, int, int]:
    prim5_pts = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
    prim6_pts = [(a, b) for a in range(6) for b in range(6) if math.gcd(math.gcd(a, b), 6) == 1]
    assert len(prim5_pts) == 24 and len(prim6_pts) == 24
    p5_x_p6_antipodal_pairs = (len(prim5_pts) // 2) * (len(prim6_pts) // 2)
    total_rel_sign_worlds = (len(prim5_pts) * len(prim6_pts)) // 2

    ker_lr_pts = [(a, b) for (a, b) in prim5_pts if (3 * a + b) % 5 == 0 and (a + 2 * b) % 5 == 0]
    ker_t4s_pts = [(a, b) for (a, b) in prim6_pts if (5 * a + b) % 6 == 0 and (-a + b) % 6 == 0]
    assert len(ker_lr_pts) == 4 and len(ker_t4s_pts) == 2
    equiv_rel_sign_worlds = (len(ker_lr_pts) * len(ker_t4s_pts)) // 2

    ker_lr_ant = sorted({min(pt, ((-pt[0]) % 5, (-pt[1]) % 5)) for pt in ker_lr_pts})
    ker_t4s_ant = sorted({min(pt, ((-pt[0]) % 6, (-pt[1]) % 6)) for pt in ker_t4s_pts})
    return (Fr(ker_lr_ant[0][0], 5), Fr(ker_lr_ant[0][1], 5)), (Fr(ker_t4s_ant[0][0], 6), Fr(ker_t4s_ant[0][1], 6)), p5_x_p6_antipodal_pairs, total_rel_sign_worlds, equiv_rel_sign_worlds


def compute_uv_continuous_jacobian_rank(
    base_uv_mats: tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix],
    l2_tau8: mp.mpf,
) -> tuple[int, mp.mpf, int]:
    """Computes the 50 x 12 log-scaled finite-difference Jacobian matrix J_{ia} = d O_i / d theta_a
    with respect to all 12 continuous UV boundary parameters and returns:
      (numerical_svd_rank_12, smallest_singular_value_sigma12, planted_13th_redundant_col_rank)!"""
    uv0 = default_uv_boundary_12()
    eps = mp.mpf(10) ** (-6)
    base_out, _, _, _, _ = eval_full_v7_pipeline(base_uv_mats, l2_tau8, uv0, n_steps=24)
    flat_keys = [(sec, k) for sec in sorted(base_out.keys()) for k in sorted(base_out[sec].keys())]
    v0 = [base_out[sec][k] for sec, k in flat_keys]
    scales = [max(abs(x), mp.mpf(1)) for x in v0]

    def perturb(idx: int, delta: mp.mpf) -> UVContinuousBoundary12:
        lams = list(uv0.lam_over_g0sq)
        fns = list(uv0.ln_fn_scales_ude)
        if idx < 4:
            lams[idx] += delta
        elif idx == 4:
            return UVContinuousBoundary12(tuple(lams), uv0.m1_sq_over_m12_sq + delta, uv0.m2_sq_over_m12_sq, uv0.ln_m12_sq_over_mgut2, uv0.ln_M0_over_mgut, uv0.bar_theta_uv_bare, tuple(fns))  # type: ignore[arg-type]
        elif idx == 5:
            return UVContinuousBoundary12(tuple(lams), uv0.m1_sq_over_m12_sq, uv0.m2_sq_over_m12_sq + delta, uv0.ln_m12_sq_over_mgut2, uv0.ln_M0_over_mgut, uv0.bar_theta_uv_bare, tuple(fns))  # type: ignore[arg-type]
        elif idx == 6:
            return UVContinuousBoundary12(tuple(lams), uv0.m1_sq_over_m12_sq, uv0.m2_sq_over_m12_sq, uv0.ln_m12_sq_over_mgut2 + delta, uv0.ln_M0_over_mgut, uv0.bar_theta_uv_bare, tuple(fns))  # type: ignore[arg-type]
        elif idx == 7:
            return UVContinuousBoundary12(tuple(lams), uv0.m1_sq_over_m12_sq, uv0.m2_sq_over_m12_sq, uv0.ln_m12_sq_over_mgut2, uv0.ln_M0_over_mgut + delta, uv0.bar_theta_uv_bare, tuple(fns))  # type: ignore[arg-type]
        elif idx == 8:
            return UVContinuousBoundary12(tuple(lams), uv0.m1_sq_over_m12_sq, uv0.m2_sq_over_m12_sq, uv0.ln_m12_sq_over_mgut2, uv0.ln_M0_over_mgut, uv0.bar_theta_uv_bare + delta, tuple(fns))  # type: ignore[arg-type]
        else:
            fns[idx - 9] += delta
        return UVContinuousBoundary12(tuple(lams), uv0.m1_sq_over_m12_sq, uv0.m2_sq_over_m12_sq, uv0.ln_m12_sq_over_mgut2, uv0.ln_M0_over_mgut, uv0.bar_theta_uv_bare, tuple(fns))  # type: ignore[arg-type]

    J = mp.zeros(len(flat_keys), 12)
    for col in range(12):
        p_out, _, _, _, _ = eval_full_v7_pipeline(base_uv_mats, l2_tau8, perturb(col, eps), n_steps=24)
        for row, (sec, k) in enumerate(flat_keys):
            J[row, col] = (p_out[sec][k] - v0[row]) / (eps * scales[row])
        # Normalize column to unit Euclidean norm so SVD tests pure linear independence free of units:
        cnorm = mp.sqrt(sum(abs(J[r, col]) ** 2 for r in range(len(flat_keys))))
        if cnorm > 0:
            for r in range(len(flat_keys)):
                J[r, col] /= cnorm

    _, sv_12, _ = mp.svd_r(J)
    tol_svd = mp.mpf(10) ** (-5)
    rank_12 = sum(1 for s in sv_12 if s > tol_svd)
    min_sv_12 = min(sv_12)

    # Planted Control 3a: append a 13th redundant UV parameter (simultaneous shift of ln_m12_sq and m1_sq+m2_sq linear combo):
    J13 = mp.zeros(len(flat_keys), 13)
    for r in range(len(flat_keys)):
        for c in range(12):
            J13[r, c] = J[r, c]
        J13[r, 12] = mp_rat(3, 5) * J[r, 0] + mp_rat(4, 5) * J[r, 6]
    _, sv_13, _ = mp.svd_r(J13)
    rank_13_redundant = sum(1 for s in sv_13 if s > tol_svd)
    return rank_12, min_sv_12, rank_13_redundant


@dataclass(frozen=True)
class DiscreteTopologyRow:
    name: str
    category: str  # ANCHOR | CHOSEN | ADMITTED | FORCED | EMPIRICAL_FIT
    bits_num: int
    bits_den: int
    post_inspection: bool


def validate_discrete_ledger(rows: list[DiscreteTopologyRow]) -> tuple[int, int, Fr]:
    n_emp = 0
    n_anc = 0
    tot_bits = Fr(0, 1)
    for r in rows:
        b = Fr(r.bits_num, r.bits_den)
        if r.category == "EMPIRICAL_FIT":
            n_emp += 1
            raise ValueError(f"Forbidden empirical SM fit under 0 of 19 firewall: {r.name}")
        if r.category == "ANCHOR":
            n_anc += 1
            if b != 0:
                raise ValueError("Energy unit anchor must carry 0 dimensionless bits")
        if r.post_inspection and b <= 0:
            raise ValueError(f"Guardrail 1 violation: post-inspection discrete item {r.name} priced at <= 0 bits!")
        if r.category in ("CHOSEN", "ADMITTED") and b <= 0:
            raise ValueError(f"Discrete topology choice {r.name} must carry > 0 bits!")
        tot_bits += b
    if n_anc != 1:
        raise ValueError(f"Guardrail 5 violation: {n_anc} != 1 dimensionful energy unit anchors!")
    return n_emp, n_anc, tot_bits


def build_bourbaki_d5() -> tuple[list[list[int]], list[tuple[int, ...]], list[tuple[int, ...]], list[tuple[int, ...]]]:
    """Constructs all 40 roots of D_5 = Spin(10) (in simple-root coords) and weights of 10_V & 16_+ (in Dynkin labels)
    purely via the 5x5 Bourbaki D_5 Cartan matrix Weyl-orbit BFS (node 3 trivalent to 2, 4, 5)."""
    A = [
        [2, -1, 0, 0, 0],
        [-1, 2, -1, 0, 0],
        [0, -1, 2, -1, -1],
        [0, 0, -1, 2, 0],
        [0, 0, -1, 0, 2],
    ]

    def s_root(c: tuple[int, ...], i: int) -> tuple[int, ...]:
        pair = sum(c[j] * A[j][i] for j in range(5))
        out = list(c)
        out[i] -= pair
        return tuple(out)

    roots_s = {tuple(1 if j == i else 0 for j in range(5)) for i in range(5)}
    q = deque(roots_s)
    while q:
        cur = q.popleft()
        for i in range(5):
            nxt = s_root(cur, i)
            if nxt not in roots_s:
                roots_s.add(nxt)
                q.append(nxt)
    assert len(roots_s) == 40

    def weyl_weights(hw: tuple[int, ...]) -> list[tuple[int, ...]]:
        ws = {hw}
        qw = deque(ws)
        while qw:
            m = qw.popleft()
            for i in range(5):
                if m[i] != 0:
                    nm = tuple(m[j] - m[i] * A[i][j] for j in range(5))
                    if nm not in ws:
                        ws.add(nm)
                        qw.append(nm)
        return sorted(ws)

    w10 = weyl_weights((1, 0, 0, 0, 0))
    w16 = weyl_weights((0, 0, 0, 0, 1))
    assert len(w10) == 10 and len(w16) == 16
    return A, sorted(roots_s), w10, w16


def chern_root_i8_spin10(n_t: int, n_10h: int, n_1h: int) -> dict[str, Fr]:
    """Computes exact 6D N=(1,0) anomaly polynomial I_8 coefficients directly from truncated degree-4
    symmetric power series in R-eigenvalues (r1, r2) and F-eigenvalues (f1..f5), with ZERO (p1, p2) shortcuts!
    Recall: A_hat(R) = prod_{i=1}^2 ((r_i/2)/sinh(r_i/2)) = 1 - (r1^2+r2^2)/24 + (7(r1^4+r2^4) + 10 r1^2 r2^2)/5760;
            L(R)     = prod_{i=1}^2 (r_i / tanh(r_i))     = 1 + (r1^2+r2^2)/3  + (-7(r1^4+r2^4) + 10 r1^2 r2^2)/45.
    In 6D N=(1,0) SUGRA (Erler J.Math.Phys. 35 (1994) 1819):
      I_8 = (1 / 5760) [ (n_H - n_V + 29 n_T - 273) tr R^4 + (1/4)(9 - n_T ...) ] -> let's evaluate each multiplet's
      exact Atiyah-Singer chiral anomaly index density on generic rational test eigenvalues (r1, r2) & (f1..f5)!"""
    # Exact 6D N=(1,0) chiral anomaly polynomial per Erler (1994) Eqs. (2.8)-(2.15):
    #   I_grav(1_G)  : (-244 tr R^4 - 44 (tr R^2)^2) / 5760? Check with self-dual tensor:
    #   Wait: 1_G (graviton + left gravitino) + 1 self-dual B_+: together (1_G + 0_T vs 1_G + 1_T):
    #   Standard 6D N=(1,0) identities (Green-Schwarz-West / Erler 1994, where tr R^2 = -2(r1^2+r2^2), tr R^4 = 2(r1^4+r2^4)):
    #     c_{R4}    = -(273 - 29 n_T + n_V - n_H) / 5760
    #     c_{R2_sq} = -(9 - n_T) / 128 ? Let's derive directly from spin-3/2, spin-1/2, and self-dual 2-form index series!
    # In Euclidean 6D, SO(6) skew eigenvalues are (+-r1, +-r2, +-r3) (we evaluate on 3 independent skew blocks r1, r2, r3!):
    #   tr R^2 = -2(r1^2 + r2^2 + r3^2),   tr R^4 = 2(r1^4 + r2^4 + r3^4),   (tr R^2)^2 = 4(sum r_i^2)^2.
    # Chiral anomalies in 6D (normalized so 1 complex left Weyl = +A_hat(R) ch(F)|_{deg 4}; 1 hyper = 1 left Weyl, 1 vec = -1 left Weyl):
    #   A_hat(r1,r2,r3)|_4 = (7(r1^4+r2^4+r3^4) + 10(r1^2 r2^2 + r2^2 r3^2 + r3^2 r1^2)) / 5760
    #                      = (7/2 tr R^4 + (5/2)((tr R^2)^2/4 - tr R^4 / 2))? Let's solve linearly on 6 test points!
    pts = [
        (Fr(1), Fr(2), Fr(3), Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)),
        (Fr(2), Fr(1), Fr(0), Fr(1), Fr(2), Fr(0), Fr(0), Fr(0)),
        (Fr(1), Fr(1), Fr(1), Fr(1), Fr(1), Fr(1), Fr(0), Fr(0)),
        (Fr(3), Fr(2), Fr(1), Fr(2), Fr(1), Fr(3), Fr(1), Fr(0)),
        (Fr(0), Fr(1), Fr(2), Fr(1), Fr(2), Fr(3), Fr(4), Fr(5)),
    ]

    def deg4_weyl(r: tuple[Fr, Fr, Fr], weights: list[tuple[Fr, ...]], f: tuple[Fr, ...]) -> Fr:
        s2 = r[0] ** 2 + r[1] ** 2 + r[2] ** 2
        s4 = r[0] ** 4 + r[1] ** 4 + r[2] ** 4
        p2 = (r[0] ** 2) * (r[1] ** 2) + (r[1] ** 2) * (r[2] ** 2) + (r[2] ** 2) * (r[0] ** 2)
        a0 = Fr(1)
        a2 = -s2 / 24
        a4 = (7 * s4 + 10 * p2) / 5760
        ch0 = Fr(len(weights))
        # For skew-Hermitian F = i * diag, ch(i F / 2pi) has +1/2 sum (w.f)^2 and +1/24 sum (w.f)^4:
        ch2 = sum((sum(w[k] * f[k] for k in range(5)) ** 2) for w in weights) / 2
        ch4 = sum((sum(w[k] * f[k] for k in range(5)) ** 4) for w in weights) / 24
        return a4 * ch0 + a2 * ch2 + a0 * ch4

    def deg4_gravitino(r: tuple[Fr, Fr, Fr]) -> Fr:
        # Chiral gravitino A_hat(r) * (ch(T_C) - 1)|_4 where ch(T_C) - 1 = sum_{k=1}^3 (e^{r_k} + e^{-r_k}) - 1 = 5 + s2 + s4/12:
        s2 = r[0] ** 2 + r[1] ** 2 + r[2] ** 2
        s4 = r[0] ** 4 + r[1] ** 4 + r[2] ** 4
        p2 = (r[0] ** 2) * (r[1] ** 2) + (r[1] ** 2) * (r[2] ** 2) + (r[2] ** 2) * (r[0] ** 2)
        a2 = -s2 / 24
        a4 = (7 * s4 + 10 * p2) / 5760
        return 5 * a4 + a2 * s2 + s4 / 12

    def deg4_selfdual_b(r: tuple[Fr, Fr, Fr]) -> Fr:
        # Chiral self-dual 2-form -(1/8) L(r)|_4 where prod_{k=1}^3 ((r_k)/tanh(r_k)) evaluated at r_k -> r_k/2?
        # Wait: Hirzebruch L-polynomial uses x_k / tanh(x_k) -> 1 + s2/3 + (-s4 + 5 p2)/45? Check (1 + r1^2/3 - r1^4/45)(1 + r2^2/3 - r2^4/45):
        # deg-4 = -(r1^4+r2^4+r3^4)/45 + (1/9)(r1^2 r2^2 + ...) = (-s4 + 5 p2)/45!
        s4 = r[0] ** 4 + r[1] ** 4 + r[2] ** 4
        p2 = (r[0] ** 2) * (r[1] ** 2) + (r[1] ** 2) * (r[2] ** 2) + (r[2] ** 2) * (r[0] ** 2)
        return -Fr(1, 8) * (-s4 + 5 * p2) / 45

    # Build Spin(10) 45_V weights (40 roots + 5 zero) & 10_H weights in orthogonal coords e_1..e_5:
    w_adj = [(Fr(0),) * 5 for _ in range(5)]
    for a in range(5):
        for b in range(a + 1, 5):
            for sa in (-1, 1):
                for sb in (-1, 1):
                    v = [Fr(0)] * 5
                    v[a], v[b] = Fr(sa), Fr(sb)
                    w_adj.append(tuple(v))
    w_vec = []
    for a in range(5):
        for sa in (-1, 1):
            v = [Fr(0)] * 5
            v[a] = Fr(sa)
            w_vec.append(tuple(v))
    w_sing = [(Fr(0),) * 5]

    # Solve for the 5 invariant coefficients [c_R4, c_R2sq, c_F4, c_R2F2, c_F2sq] in basis:
    #   tr R^4 = 2 sum r_k^4,  (tr R^2)^2 = 4 (sum r_k^2)^2,  tr_10 F^4 = 2 sum f_a^4,
    #   tr R^2 tr_10 F^2 = (-2 sum r_k^2)(-2 sum f_a^2)? Note in standard convention tr R^2 = -2 sum r_k^2 and tr_10 F^2 = -2 sum f_a^2
    #   so (tr R^2)^2 = 4(sum r^2)^2, (tr F^2)^2 = 4(sum f^2)^2, tr R^2 tr F^2 = 4(sum r^2)(sum f^2), tr R^4 = 2 sum r^4, tr F^4 = 2 sum f^4?
    #   Wait: for anti-Hermitian R, F: (R^2) has negative eigenvalues -r_k^2 so tr(R^2) = -2 sum r_k^2, tr(R^4) = +2 sum r_k^4!
    #   In Erler / Green-Schwarz convention (tr R^2 := tr(R_E^2) with positive sum r_k^2, i.e. p_1 = (1/2) tr R^2 -> sum r_k^2 = 1/2 tr R^2,
    #   and tr R^4 = 2 sum r_k^4? Wait: for 2x2 skew [[0, r], [-r, 0]], M^2 = -r^2 I_2 (tr M^2 = -2 r^2) and M^4 = +r^4 I_2 (tr M^4 = +2 r^4);
    #   in curvature 2-form i R, (i R)^2 = +r^2 I_2 (tr = +2 r^2) and (i R)^4 = +r^4 I_2 (tr = +2 r^4)!):
    #   YES! With Hermitian curvature H_R = i R and H_F = i F:
    #     tr(H_R^2) = 2 sum r_k^2,  tr(H_R^4) = 2 sum r_k^4,  tr_10(H_F^2) = 2 sum f_a^2,  tr_10(H_F^4) = 2 sum f_a^4!
    #   And 6D N=(1,0) multiplet content:
    #     1_G = 1 left gravitino + 1 self-dual B_+;  n_T tensor = n_T anti-self-dual B_- + n_T right Weyl (-n_T left Weyl);
    #     1_V = -1 left Weyl(adj);  1_H = +1 left Weyl(rep).
    #   Wait: in 6D N=(1,0) SUGRA, a Weyl spinor in 6D is symplectic-Majorana-Weyl (HALF of a complex Dirac-Weyl spinor!),
    #   so each SMW fermion (gravitino, tensorino, gaugino, hyperino) carries an overall factor of 1/2 relative to complex Weyl!
    mat_b = []
    rhs_v = []
    for p in pts:
        r_t = p[:3]
        f_t = p[3:]
        # In 6D N=(1,0): 1_G = +gravitino(+) + B^+, n_T = n_T * (-weyl(1) - B^+), 1_V = +weyl(adj), 1_H = -weyl(rep):
        # (Note: 2 symplectic-Majorana-Weyl spinors per 6D multiplet = 1 complex Weyl spinor, while B^+ is real self-dual 2-form!)
        val = (
            deg4_gravitino(r_t)
            + (1 - n_t) * deg4_selfdual_b(r_t)
            - n_t * deg4_weyl(r_t, w_sing, f_t)
            + deg4_weyl(r_t, w_adj, f_t)
            - n_10h * deg4_weyl(r_t, w_vec, f_t)
            - n_1h * deg4_weyl(r_t, w_sing, f_t)
        )
        # Real skew-symmetric curvatures R, F have tr(R^2) = -2 sum r_k^2, tr(R^4) = +2 sum r_k^4, tr_10(F^2) = -2 sum f_a^2, tr_10(F^4) = +2 sum f_a^4:
        tr_r2 = -2 * sum(x * x for x in r_t)
        tr_r4 = 2 * sum(x ** 4 for x in r_t)
        tr_f2 = -2 * sum(x * x for x in f_t)
        tr_f4 = 2 * sum(x ** 4 for x in f_t)
        mat_b.append([tr_r4, tr_r2 * tr_r2, tr_f4, tr_r2 * tr_f2, tr_f2 * tr_f2])
        rhs_v.append(val)

    # Exact Fraction Gaussian elimination on 5x5:
    aug = [mat_b[i] + [rhs_v[i]] for i in range(5)]
    for col in range(5):
        piv = next(r for r in range(col, 5) if aug[r][col] != 0)
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        aug[col] = [x / pv for x in aug[col]]
        for r in range(5):
            if r != col and aug[r][col] != 0:
                fac = aug[r][col]
                aug[r] = [aug[r][c] - fac * aug[col][c] for c in range(6)]
    sol = [aug[i][5] for i in range(5)]
    return {"tr_R4": sol[0], "tr_R2_sq": sol[1], "tr_F4": sol[2], "tr_R2_tr_F2": sol[3], "tr_F2_sq": sol[4]}


def epstein_e3_sl2z_k52(tau: mp.mpc, a: Fr, b: Fr) -> mp.mpf:
    """Exact 56-digit SL(2,Z)-reduced Chowla-Selberg Bessel-K_{5/2} series (ZERO box truncation!)."""
    z = mp.mpc(tau)
    aa, bb = a % 1, b % 1
    for _ in range(50):
        k_sh = int(mp.nint(mp.re(z)))
        if k_sh != 0:
            z -= k_sh
            aa = (aa - k_sh * bb) % 1
        if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-34):
            z = -mp.mpf(1) / z
            aa, bb = bb % 1, (-aa) % 1
        else:
            break
    x, y = mp.re(z), mp.im(z)
    am, bm = f2m(aa), f2m(bb)
    res = 2 * (y ** 3) * mp.re(mp.polylog(6, mp.exp(2 * I_MP * mp.pi * bm)))
    if bb == 0:
        res += (3 * mp.pi / (4 * (y ** 2))) * mp.re(mp.polylog(5, mp.exp(2 * I_MP * mp.pi * am)))
    cutoff = mp.mpf(138)
    for m in range(1, 200):
        max_xi = cutoff / (2 * mp.pi * m * y)
        if max_xi < mp_rat(1, 8):
            break
        klim = int(mp.floor(max_xi)) + 1
        c_pref = 2 * (y ** 3) * (mp.pi / (8 * ((m * y) ** 5)))
        for k in range(-klim, klim + 1):
            xi = mp.mpf(k) - bm
            if xi == 0:
                continue
            zv = 2 * mp.pi * m * y * abs(xi)
            if zv <= cutoff:
                res += c_pref * mp.cos(2 * mp.pi * m * (am + xi * x)) * mp.exp(-zv) * (zv * zv + 3 * zv + 3)
    return res


def dkl_sl2z(tau: mp.mpc) -> tuple[mp.mpf, mp.mpf]:
    z = mp.mpc(tau)
    for _ in range(50):
        k_sh = int(mp.nint(mp.re(z)))
        if k_sh != 0:
            z -= k_sh
        if abs(z) < mp.mpf(1) - mp.mpf(10) ** (-30):
            z = -mp.mpf(1) / z
        else:
            break
    y = mp.im(z)
    q_h = mp.exp(I_MP * mp.pi * z / 12)
    q = mp.exp(2 * I_MP * mp.pi * z)
    pr = mp.mpc(1)
    e2 = mp.mpc(1)
    qn = q
    for n in range(1, 200):
        if abs(qn) < mp.mpf(10) ** (-56):
            break
        pr *= 1 - qn
        e2 -= 24 * n * qn / (1 - qn)
        qn *= q
    eta4 = abs(q_h * pr) ** 4
    hat_e2 = e2 - 3 / (mp.pi * y)
    inv_2y_eta4 = 1 / (2 * y * eta4)
    return inv_2y_eta4, 2 * inv_2y_eta4 * (y ** 2) * (abs(hat_e2) ** 2)


def c_cas_spin10_sl2z(tau: mp.mpc) -> mp.mpf:
    a1, a2 = Fr(1, 2), Fr(1, 2)
    tot = mp.mpf(1024) * (epstein_e3_sl2z_k52(tau, Fr(0), Fr(0)) - epstein_e3_sl2z_k52(tau, a1, a2))
    for mult, g1, g2 in [(8, Fr(0), Fr(1, 2)), (12, Fr(1, 2), Fr(0)), (12, Fr(1, 2), Fr(1, 2))]:
        tot -= mp.mpf(4 * mult) * (epstein_e3_sl2z_k52(tau, g1, g2) - epstein_e3_sl2z_k52(tau, g1 + a1, g2 + a2))
    for mult_h, g1, g2 in [(12, Fr(1, 2), Fr(1, 4)), (4, Fr(0), Fr(1, 2))]:
        tot += mp.mpf(4 * mult_h) * (epstein_e3_sl2z_k52(tau, g1, g2) - epstein_e3_sl2z_k52(tau, g1 + a1, g2 + a2))
    return tot / (2 * (mp.pi ** 7))


def v_tot_sl2z(tv: mp.mpf, sv: mp.mpf, tx: mp.mpf, ty: mp.mpf, gr2: mp.mpf) -> mp.mpf:
    tau = tx + I_MP * ty
    inv_e, ft = dkl_sl2z(tau)
    cc = c_cas_spin10_sl2z(tau)
    p1, p2 = 2 * mp.pi / 36, 2 * mp.pi / 48
    ws = 3 * mp.exp(-p1 * sv) - mp.exp(-p2 * sv)
    dws = -3 * p1 * mp.exp(-p1 * sv) + p2 * mp.exp(-p2 * sv)
    dsw = dws - ws / (2 * sv)
    v_ss = ((2 * gr2 * tv - 1) ** 2) / (2 * gr2 * sv * (tv ** 3))
    v_f = (1 / (4 * sv * tv)) * (inv_e * (4 * (sv ** 2) * (dsw ** 2) - 2 * (ws ** 2)) + (mp.pi ** 2 / 18) * ft * (ws ** 2))
    return v_ss + v_f + cc / ((sv ** 2) * (tv ** 2))


def solve_4mod_newton(seed: tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf], gr2: mp.mpf) -> tuple[list[mp.mpf], mp.mpf, list[mp.mpf]]:
    old_dps = mp.mp.dps
    mp.mp.dps = 56
    try:
        x = [mp.mpf(v) for v in seed]
        gr2_m = mp.mpf(gr2)
        for stage_hs, n_it in [
            ([mp.mpf(10) ** (-11), mp.mpf(10) ** (-12), mp.mpf(10) ** (-13), mp.mpf(10) ** (-13)], 22),
            ([mp.mpf(10) ** (-15), mp.mpf(10) ** (-16), mp.mpf(10) ** (-17), mp.mpf(10) ** (-17)], 4),
        ]:
            hs = stage_hs
            for _ in range(n_it):
                tau_cache: dict[tuple[int, int], tuple[mp.mpf, mp.mpf, mp.mpf]] = {}
                for ix in (-1, 0, 1):
                    for iy in (-1, 0, 1):
                        tau_p = (x[2] + ix * hs[2]) + I_MP * (x[3] + iy * hs[3])
                        ie, ft = dkl_sl2z(tau_p)
                        tau_cache[(ix, iy)] = (ie, ft, c_cas_spin10_sl2z(tau_p))

                def eval_c(t_a: mp.mpf, s_a: mp.mpf, ix: int, iy: int) -> mp.mpf:
                    ie, ft, cc = tau_cache[(ix, iy)]
                    p1, p2 = 2 * mp.pi / 36, 2 * mp.pi / 48
                    ws = 3 * mp.exp(-p1 * s_a) - mp.exp(-p2 * s_a)
                    dws = -3 * p1 * mp.exp(-p1 * s_a) + p2 * mp.exp(-p2 * s_a)
                    dsw = dws - ws / (2 * s_a)
                    v_ss = ((2 * gr2_m * t_a - 1) ** 2) / (2 * gr2_m * s_a * (t_a ** 3))
                    v_f = (1 / (4 * s_a * t_a)) * (ie * (4 * (s_a ** 2) * (dsw ** 2) - 2 * (ws ** 2)) + (mp.pi ** 2 / 18) * ft * (ws ** 2))
                    return v_ss + v_f + cc / ((s_a ** 2) * (t_a ** 2))

                v0 = eval_c(x[0], x[1], 0, 0)
                gr = mp.zeros(4, 1)
                hm = mp.zeros(4, 4)
                gr[0, 0] = (eval_c(x[0] + hs[0], x[1], 0, 0) - eval_c(x[0] - hs[0], x[1], 0, 0)) / (2 * hs[0])
                gr[1, 0] = (eval_c(x[0], x[1] + hs[1], 0, 0) - eval_c(x[0], x[1] - hs[1], 0, 0)) / (2 * hs[1])
                gr[2, 0] = (eval_c(x[0], x[1], 1, 0) - eval_c(x[0], x[1], -1, 0)) / (2 * hs[2])
                gr[3, 0] = (eval_c(x[0], x[1], 0, 1) - eval_c(x[0], x[1], 0, -1)) / (2 * hs[3])
                gn = mp.sqrt(mp.fsum(gr[i, 0] ** 2 for i in range(4)))
                hm[0, 0] = (eval_c(x[0] + hs[0], x[1], 0, 0) - 2 * v0 + eval_c(x[0] - hs[0], x[1], 0, 0)) / (hs[0] ** 2)
                hm[1, 1] = (eval_c(x[0], x[1] + hs[1], 0, 0) - 2 * v0 + eval_c(x[0], x[1] - hs[1], 0, 0)) / (hs[1] ** 2)
                hm[2, 2] = (eval_c(x[0], x[1], 1, 0) - 2 * v0 + eval_c(x[0], x[1], -1, 0)) / (hs[2] ** 2)
                hm[3, 3] = (eval_c(x[0], x[1], 0, 1) - 2 * v0 + eval_c(x[0], x[1], 0, -1)) / (hs[3] ** 2)
                hm[0, 1] = hm[1, 0] = (
                    eval_c(x[0] + hs[0], x[1] + hs[1], 0, 0) - eval_c(x[0] + hs[0], x[1] - hs[1], 0, 0)
                    - eval_c(x[0] - hs[0], x[1] + hs[1], 0, 0) + eval_c(x[0] - hs[0], x[1] - hs[1], 0, 0)
                ) / (4 * hs[0] * hs[1])
                for ci, idx_pair in [(2, (1, 0)), (3, (0, 1))]:
                    px, py = idx_pair
                    hm[0, ci] = hm[ci, 0] = (
                        eval_c(x[0] + hs[0], x[1], px, py) - eval_c(x[0] + hs[0], x[1], -px, -py)
                        - eval_c(x[0] - hs[0], x[1], px, py) + eval_c(x[0] - hs[0], x[1], -px, -py)
                    ) / (4 * hs[0] * hs[ci])
                    hm[1, ci] = hm[ci, 1] = (
                        eval_c(x[0], x[1] + hs[1], px, py) - eval_c(x[0], x[1] + hs[1], -px, -py)
                        - eval_c(x[0], x[1] - hs[1], px, py) + eval_c(x[0], x[1] - hs[1], -px, -py)
                    ) / (4 * hs[1] * hs[ci])
                hm[2, 3] = hm[3, 2] = (eval_c(x[0], x[1], 1, 1) - eval_c(x[0], x[1], 1, -1) - eval_c(x[0], x[1], -1, 1) + eval_c(x[0], x[1], -1, -1)) / (4 * hs[2] * hs[3])
                if gn < mp.mpf(10) ** (-44):
                    break
                evs, _ = mp.eighe((hm + hm.T) / 2)
                hs_reg = (hm + hm.T) / 2
                min_ev = min(mp.re(e) for e in evs)
                max_ev = max(abs(mp.re(e)) for e in evs)
                if min_ev <= 0:
                    hs_reg += (abs(min_ev) + max_ev * mp_rat(1, 1000)) * mp.eye(4)
                step = mp.lu_solve(hs_reg, -gr)
                al = mp.mpf(1)
                for _ in range(20):
                    nx = [x[i] + al * step[i, 0] for i in range(4)]
                    if nx[0] > 10 and nx[1] > 5 and nx[3] > mp_rat(1, 20):
                        vn = v_tot_sl2z(nx[0], nx[1], nx[2], nx[3], gr2_m)
                        if vn < v0 or gn < mp.mpf(10) ** (-15):
                            x = nx
                            break
                    al /= 2
        evs_f, _ = mp.eighe((hm + hm.T) / 2)
        return x, gn, sorted(mp.re(e) for e in evs_f)
    finally:
        mp.mp.dps = old_dps


def theta_triple(tau: mp.mpc, ca: Fr, cb: Fr) -> mp.mpc:
    ta, tb = ca % 1, cb % 1
    nb = int(cb - tb)
    am, bm = f2m(ta), f2m(tb)
    zv = am * tau + bm
    q = mp.exp(I_MP * mp.pi * tau)
    w = mp.exp(2 * I_MP * mp.pi * zv)
    pr = mp.mpc(1)
    for m in range(1, 95):
        q2m = q ** (2 * m)
        qm = q ** (2 * m - 1)
        if abs(qm) * max(abs(w), 1 / abs(w)) < mp.mpf(10) ** (-54):
            break
        pr *= (1 - q2m) * (1 + qm * w) * (1 + qm / w)
    base = mp.exp(I_MP * mp.pi * am * am * tau + 2 * I_MP * mp.pi * am * bm) * pr
    return base if (nb == 0 or ta == 0) else mp.exp(2 * I_MP * mp.pi * am * nb) * base


def s_triplet_cauchy(tau: mp.mpc) -> tuple[list[mp.mpc], mp.mpc]:
    t2_0 = theta_triple(tau, Fr(1, 2), Fr(0))
    t3_0 = theta_triple(tau, Fr(0), Fr(0))
    t4_0 = theta_triple(tau, Fr(0), Fr(1, 2))
    r2_0 = (t2_0 * t2_0) / (t3_0 * t4_0)
    r3_0 = (t3_0 * t3_0) / (t2_0 * t4_0)
    r4_0 = (t4_0 * t4_0) / (t2_0 * t3_0)
    rad = mp_rat(1, 20)
    dl2 = dl3 = dl4 = mp.mpc(0)
    for k in range(32):
        ang = 2 * mp.pi * mp_rat(k, 32)
        dz = rad * (mp.cos(ang) + I_MP * mp.sin(ang))
        u2 = theta_triple(tau + dz, Fr(1, 2), Fr(0))
        u3 = theta_triple(tau + dz, Fr(0), Fr(0))
        u4 = theta_triple(tau + dz, Fr(0), Fr(1, 2))
        dl2 += mp.log(((u2 * u2) / (u3 * u4)) / r2_0) / (32 * dz)
        dl3 += mp.log(((u3 * u3) / (u2 * u4)) / r3_0) / (32 * dz)
        dl4 += mp.log(((u4 * u4) / (u2 * u3)) / r4_0) / (32 * dz)
    den = 3 * mp.pi * I_MP
    c_hol = [
        (-t2_0 / (t3_0 * t4_0)) * (dl2 / den),
        (-t4_0 / (t2_0 * t3_0)) * (dl4 / den),
        (I_MP * t3_0 / (t2_0 * t4_0)) * (dl3 / den),
    ]
    return c_hol, mp.pi * t2_0 * t3_0 * t4_0


def eval_w_pts_triple(tau: mp.mpc, pts: list[tuple[Fr, Fr]], ql: int, qr: int, c_hol: list[mp.mpc], t1p: mp.mpc) -> mp.matrix:
    qi = mp.matrix([[I_MP, 0], [0, -I_MP]])
    qj = mp.matrix([[0, 1], [-1, 0]])
    qk = qi * qj
    hf = mp_rat(1, 2)
    ed = {"1": hf * qj, "i": hf * qk, "j": -hf * mp.eye(2), "k": -hf * qi}
    blks = [qj, qi, qk]
    sh = c_hol[0] * qi + c_hol[1] * qj + c_hol[2] * qk
    ct_s = [[ca.T * qj * sh * cb for cb in blks] for ca in blks]
    acc = mp.zeros(3, 3)
    hfr = Fr(1, 2)
    for pa, pb in pts:
        xv, yv = (ql * pa, 2 * ql * pb), (qr * pa, 2 * qr * pb)
        ap, am = xv[0] + yv[0], xv[0] - yv[0]
        bp, bm = Fr(xv[1] + yv[1], 2), Fr(xv[1] - yv[1], 2)
        eph = mp.exp(-2 * I_MP * mp.pi * f2m(xv[0]))
        kap = {"1": -I_MP * eph, "i": mp.mpc(-1), "j": -eph, "k": I_MP}
        cs = {"1": (ap + hfr, bp + hfr), "i": (ap + hfr, bp), "j": (ap, bp + hfr), "k": (ap, bp)}
        ds = {"1": (am + hfr, bm + hfr), "i": (am + hfr, bm), "j": (am, bm + hfr), "k": (am, bm)}
        rs: dict[str, mp.mpc] = {}
        for sk in ("1", "i", "j", "k"):
            al, be = cs[sk][0] - hfr, cs[sk][1] - hfr
            dal, dbe = ds[sk][0] - hfr, ds[sk][1] - hfr
            if (al % 1 == 0 and be % 1 == 0) or (dal % 1 == 0 and dbe % 1 == 0):
                rs[sk] = mp.mpc(0)
            else:
                rs[sk] = kap[sk] * theta_triple(tau, cs[sk][0], cs[sk][1]) * theta_triple(tau, ds[sk][0], ds[sk][1]) / t1p
        mw = rs["1"] * ed["1"] + rs["i"] * ed["i"] + rs["j"] * ed["j"] + rs["k"] * ed["k"]
        acc += mp.matrix([
            [sum(ct_s[ra][cb][r0, c0] * mw[r0, c0] for r0 in range(2) for c0 in range(2)) for cb in range(3)]
            for ra in range(3)
        ])
    return acc / len(pts)


def su3_cayley(seed: int) -> mp.matrix:
    hm = mp.zeros(3, 3)
    for r in range(3):
        hm[r, r] = mp_rat((seed + 2 * r + 1) % 7 - 3, 5)
        for c in range(r + 1, 3):
            zv = mp_rat((3 * seed + r + 2 * c + 1) % 9 - 4, 7) + I_MP * mp_rat((5 * seed + 2 * r + c + 2) % 11 - 5, 9)
            hm[r, c], hm[c, r] = zv, mp.conj(zv)
    i3 = mp.eye(3)
    u0 = (i3 - I_MP * hm) * ((i3 + I_MP * hm) ** (-1))
    return u0 * mp.exp(-I_MP * mp.arg(mp.det(u0)) / 3)


def ckm_pmns_obs(yu: mp.matrix, yd: mp.matrix, ye: mp.matrix, ynu: mp.matrix, mr: mp.matrix) -> list[mp.mpf]:
    uu, su, _ = mp.svd_c(yu)
    ud, sd, _ = mp.svd_c(yd)
    ue, se, _ = mp.svd_c(ye)
    ou = sorted(range(3), key=lambda k: su[k])
    od = sorted(range(3), key=lambda k: sd[k])
    oe = sorted(range(3), key=lambda k: se[k])
    uu_a = mp.matrix([[uu[r, ou[c]] for c in range(3)] for r in range(3)])
    ud_a = mp.matrix([[ud[r, od[c]] for c in range(3)] for r in range(3)])
    ue_a = mp.matrix([[ue[r, oe[c]] for c in range(3)] for r in range(3)])
    vc = uu_a.H * ud_a
    j_ckm = mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1]))
    mnu = -ynu * (mr ** (-1)) * ynu.T
    ev_nu, u_nu = mp.eighe(mnu * mnu.H)
    onu = sorted(range(3), key=lambda k: mp.re(ev_nu[k]))
    unu_a = mp.matrix([[u_nu[r, onu[c]] for c in range(3)] for r in range(3)])
    up = ue_a.H * unu_a
    return [abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), j_ckm, abs(up[0, 1]), abs(up[1, 2]), abs(up[0, 2])]




EXACT_30D_KEYS = {
    "cusp_robin_bc_star_tau8",
    "m11_over_mgut_zero_knob",
    "inflation_conformal_S4_ns_N60",
    "inflation_conformal_S4_r_N60",
}


def format_converged(key: str, val: mp.mpf) -> str:
    return mp.nstr(val, 30 if key in EXACT_30D_KEYS else 11)


def run_c36_scrambling_and_ow22_f1_erratum(repo: Path) -> dict[str, object]:
    """Closes Referee D2 & D3 on AGY-C36:
    1) Applies independent Cayley SU(3)^5 x U(3) unitary basis-scrambling (< 10^-38) + non-Takagi M_R
       negative control (> 1/50) to C36's extracted flavor/seesaw observables at tau_8 = 16/5 + 8i/5:
       unsym_drift, bare_u1_over_u3, and sv_mnu_6y (on M_nu = -W_nu M_R^{-1} W_nu^T).
    2) Verifies exact line numbers 278-280 and 398-399 (vs line 276 = -50/3) in
       27f5d89fa:relays/a2_ow22_v2/verify_a2_ow22_v2.py and computes stage-consistent STr a_1(xi=0)."""
    mp.mp.dps = 46
    tau_8 = mp_rat(16, 5) + I_MP * mp_rat(8, 5)
    k5_pts = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    c_hol_8, t1p_8 = s_triplet_cauchy(tau_8)

    wu_k5 = eval_w_pts_triple(tau_8, k5_pts, 1, -4, c_hol_8, t1p_8)
    wd_16 = (eval_w_pts_triple(tau_8, [(Fr(1, 5), Fr(2, 5))], 1, 2, c_hol_8, t1p_8) + eval_w_pts_triple(tau_8, [(Fr(1, 6), Fr(1, 6))], 1, 2, c_hol_8, t1p_8)) / 2
    wd_56 = (eval_w_pts_triple(tau_8, [(Fr(1, 5), Fr(2, 5))], 1, 2, c_hol_8, t1p_8) + eval_w_pts_triple(tau_8, [(Fr(5, 6), Fr(5, 6))], 1, 2, c_hol_8, t1p_8)) / 2
    wnu_6y = eval_w_pts_triple(tau_8, k5_pts, -3, 0, c_hol_8, t1p_8)
    mr_id = mp.eye(3)

    def ckm4(yu_m: mp.matrix, yd_m: mp.matrix) -> list[mp.mpf]:
        uu, su = svd_asc(yu_m)
        ud, sd = svd_asc(yd_m)
        vc = uu.H * ud
        return [abs(vc[0, 1]), abs(vc[1, 2]), abs(vc[0, 2]), mp.im(vc[0, 1] * vc[1, 2] * mp.conj(vc[0, 2]) * mp.conj(vc[1, 1]))]

    def eval_c36_obs(yu_m: mp.matrix, yd_a: mp.matrix, yd_b: mp.matrix, yn_m: mp.matrix, mr_m: mp.matrix) -> tuple[mp.mpf, mp.mpf, list[mp.mpf]]:
        drift = max(abs(a - b) for a, b in zip(ckm4(yu_m, yd_a), ckm4(yu_m, yd_b)))
        _, su = svd_asc(yu_m)
        u1_u3 = su[0] / su[2]
        mnu = -yn_m * (mr_m ** (-1)) * yn_m.T
        _, snu = svd_asc(mnu)
        return drift, u1_u3, snu

    drift_0, u13_0, snu_0 = eval_c36_obs(wu_k5, wd_16, wd_56, wnu_6y, mr_id)
    uq, u_uc, u_dc, ul = su3_cayley(13), su3_cayley(29), su3_cayley(47), su3_cayley(71)
    un_u3 = su3_cayley(97) * mp.exp(I_MP * mp_rat(3, 11))
    drift_s, u13_s, snu_s = eval_c36_obs(
        uq * wu_k5 * u_uc.H,
        uq * wd_16 * u_dc.H,
        uq * wd_56 * u_dc.H,
        ul * wnu_6y * un_u3.H,
        (un_u3.H).T * mr_id * un_u3.H,
    )
    # Negative control: omit Takagi Majorana basis transform M_R -> U_N^* M_R U_N^H!
    _, _, snu_bad = eval_c36_obs(
        uq * wu_k5 * u_uc.H,
        uq * wd_16 * u_dc.H,
        uq * wd_56 * u_dc.H,
        ul * wnu_6y * un_u3.H,
        mr_id,
    )
    c36_scram_err = max(abs(drift_0 - drift_s), abs(u13_0 - u13_s), max(abs(a - b) for a, b in zip(snu_0, snu_s)))
    # Note: for complex symmetric U_N^* U_N^H != I_3, test non-Takagi break on rank-3 seesaw or U(3) non-unitary/complex-orthogonal mismatch:
    # Wait: if mr_id = I_3 and un_u3 is unitary, un_u3.H * un_u3^* = (un_u3.T * un_u3)^H, whose singular values ARE 1 because un_u3.T * un_u3 IS unitary!
    # Aha! On a non-degenerate complex symmetric M_R0 = diag(1, 2, 5) (or with PMNS overlap against ye_k56), omitting M_R -> U_N^* M_R U_N^H breaks both singular values AND PMNS!
    ye_k5 = eval_w_pts_triple(tau_8, k5_pts, -3, 6, c_hol_8, t1p_8)
    mr_nontriv = mp.diag([mp.mpf(1), mp.mpf(2), mp.mpf(5)])
    _, snu_nt_0 = svd_asc(-wnu_6y * (mr_nontriv ** (-1)) * wnu_6y.T)
    _, snu_nt_ok = svd_asc(-(ul * wnu_6y * un_u3.H) * (((un_u3.H).T * mr_nontriv * un_u3.H) ** (-1)) * (ul * wnu_6y * un_u3.H).T)
    _, snu_nt_bad = svd_asc(-(ul * wnu_6y * un_u3.H) * (mr_nontriv ** (-1)) * (ul * wnu_6y * un_u3.H).T)
    c36_scram_err = max(c36_scram_err, max(abs(a - b) for a, b in zip(snu_nt_0, snu_nt_ok)))
    c36_nontakagi_break = max(abs(a - b) / max(abs(a), mp.mpf(10) ** (-20)) for a, b in zip(snu_nt_0, snu_nt_bad))
    assert c36_scram_err < mp.mpf(10) ** (-38) and c36_nontakagi_break > mp_rat(1, 50)

    # Exact line & stage-consistent STr a_1(xi=0) audit of 27f5d89fa:relays/a2_ow22_v2/verify_a2_ow22_v2.py (Fixes D3):
    ow22_lines = git_show_bytes(repo, AGY_002_HEAD, "relays/a2_ow22_v2/verify_a2_ow22_v2.py").decode("utf-8").splitlines()
    line276_is_nonsusy_xi16 = "a1_nonsusy_xi16 = 13 * a1_mvec + 32 * a1_proca + 48 * a1_weyl + 8 * a1_sc_conf" in ow22_lines[275]
    lines_278_280_are_susy_37_2 = (
        "50 chiral mults" in ow22_lines[277]
        and "a1_susy_xi0 = 13 * a1_mvec_mult + 32 * a1_massive_vec_mult_xi0 + 50 * a1_chiral_xi0" in ow22_lines[278]
        and "a1_susy_xi16 = 13 * a1_mvec_mult + 32 * a1_massive_vec_mult_xi16 + 50 * a1_chiral_xi16" in ow22_lines[279]
    )
    lines_398_399_pass_same_a1 = (
        "B4_SUSY_6D_E8_GHU_MSSM_3x16_E2SS" in ow22_lines[397] and "98, 61, 12" in ow22_lines[397] and "a1_susy_xi0" in ow22_lines[397]
        and "B5_SUSY_6D_E8_GHU_3x27_E2SS" in ow22_lines[398] and "170, 97, 12" in ow22_lines[398] and "a1_susy_xi0" in ow22_lines[398]
    )
    assert line276_is_nonsusy_xi16 and lines_278_280_are_susy_37_2 and lines_398_399_pass_same_a1

    a1_stage = lambda n_ch, n_v: Fr(n_ch - n_v, 2)
    stage_table = {
        "B4_IR_98_61_12_chiral49_vec12": f"{a1_stage(49, 12).numerator}/{a1_stage(49, 12).denominator}",
        "B4_line279_chiral50_vec13": f"{a1_stage(50, 13).numerator}/{a1_stage(50, 13).denominator}",
        "B4_UV_GSM_U1X_chiral52_vec13": f"{a1_stage(52, 13).numerator}/{a1_stage(52, 13).denominator}",
        "B5_IR_170_97_12_chiral85_vec12": f"{a1_stage(85, 12).numerator}/{a1_stage(85, 12).denominator}",
        "B5_with_13vec_chiral85_vec13": str(a1_stage(85, 13)),
        "B5_UV_rank6_E6_chiral85_vec14": f"{a1_stage(85, 14).numerator}/{a1_stage(85, 14).denominator}",
    }
    assert stage_table == {
        "B4_IR_98_61_12_chiral49_vec12": "37/2",
        "B4_line279_chiral50_vec13": "37/2",
        "B4_UV_GSM_U1X_chiral52_vec13": "39/2",
        "B5_IR_170_97_12_chiral85_vec12": "73/2",
        "B5_with_13vec_chiral85_vec13": "36",
        "B5_UV_rank6_E6_chiral85_vec14": "71/2",
    }
    _ = ye_k5
    return {
        "c36_unsym_drift": mp.nstr(drift_0, 12),
        "c36_bare_u1_over_u3": mp.nstr(u13_0, 12),
        "c36_qR0_seesaw_second_sv": mp.nstr(snu_0[1], 8),
        "c36_su3_pow5_x_u3_scrambling_max_err": mp.nstr(c36_scram_err, 10),
        "c36_nontakagi_mR_negative_ctrl_rel_break": mp.nstr(c36_nontakagi_break, 10),
        "ow22_line276_is_nonsusy_minus50_over_3": line276_is_nonsusy_xi16,
        "ow22_lines_278_280_and_398_399_verified": bool(lines_278_280_are_susy_37_2 and lines_398_399_pass_same_a1),
        "ow22_stage_consistent_a1_xi0_table": stage_table,
    }


def main() -> None:
    t0 = time.time()
    self_src = Path(__file__).resolve().read_text(encoding="utf-8")
    ast_res = verify_ast_strict(self_src, Path(__file__).name)
    assert ast_res["passed"], f"Self AST check failed: {ast_res}"

    banned_toks = ["m_" + "top", "m_" + "higgs", "alpha_" + "em", "alpha_" + "s", "sin2_" + "theta_w", "pd" + "g", "nu" + "fit", "co" + "data"]
    emp_hits = [tok for tok in banned_toks if re.search(rf"(?i)\b{tok}\b", self_src)]
    empirical_fitted_sm_count = len(emp_hits)
    assert empirical_fitted_sm_count == 0

    repo = find_repo_root()
    assert resolve_commit_full(repo, "639a5d46b") == AGY_EXP_HEAD
    assert resolve_commit_full(repo, "27f5d89fa") == AGY_002_HEAD
    assert resolve_commit_full(repo, "279459977") == MAIN_HEAD

    # ==========================================================================
    # PART 1 (E1): 11D M-Theory Remediation -> blind_predictions_full_toe_v7.json
    #              + C36 Scrambling (D2) + OW22-F1 Stage-Consistent Erratum (D3)
    # ==========================================================================
    mp.mp.dps = 48
    e1_c35 = run_e1_peer_audit_and_core_theorems(repo)
    c36_rem = run_c36_scrambling_and_ow22_f1_erratum(repo)

    tau_star_pos = mp.mpc(mp_rat(2, 5), mp_rat(1, 5))
    l2_ts_ode, _ = solve_l2_jacobi_taylor26(tau_star_pos, pre_reduce=True, work_dps=48)
    l2_ts_g14 = mp.pi - mp.log(8 * mp.sqrt(2 * mp.pi) / (mp.sqrt(5) * (mp.gamma(mp_rat(1, 4)) ** 2)))
    r13_gamma14_err = abs(l2_ts_ode - l2_ts_g14)
    assert r13_gamma14_err < mp.mpf(10) ** (-32)

    p3, p4, pairs_p5xp6, rel_worlds_all, rel_worlds_equiv = solve_lefschetz_monodromy_kernels()
    assert pairs_p5xp6 == 144 and rel_worlds_all == 288 and rel_worlds_equiv == 4

    tau8_pos = mp.mpc(mp_rat(16, 5), mp_rat(8, 5))
    l2_pos, tau8_rad_err = solve_l2_jacobi_taylor26(tau8_pos, pre_reduce=True, work_dps=48)
    assert tau8_rad_err < mp.mpf(10) ** (-34)

    tau_a_unred = mp.mpc(mp_rat(1, 5), mp_rat(8, 5))
    tau_b_unred = -mp.mpf(1) / tau_a_unred
    l2_a_unred, _ = solve_l2_jacobi_taylor26(tau_a_unred, pre_reduce=False, work_dps=48)
    l2_b_unred, _ = solve_l2_jacobi_taylor26(tau_b_unred, pre_reduce=False, work_dps=48)
    l2_mod_s_err = abs((l2_b_unred - mp.log(abs(tau_a_unred))) - l2_a_unred)
    assert l2_mod_s_err < mp.mpf(10) ** (-32)

    mp.mp.dps = 44
    max_18_bench_err, ow20_3x3_err, bug_33_16_break = verify_18_benchmark_coeffs_and_ow20_3x3(repo)
    assert max_18_bench_err < mp.mpf(10) ** (-38) and ow20_3x3_err < mp.mpf(10) ** (-12) and abs(bug_33_16_break - mp_rat(51, 8)) < mp.mpf(10) ** (-38)

    w3 = (((mp.mpf(3) + mp.sqrt(5)) / 2) ** (-4))
    w4 = 2 * (((mp.mpf(4) + mp.sqrt(12)) / 2) ** (-4))
    om3, om4 = w3 / (w3 + w4), w4 / (w3 + w4)

    def build_uv_weave(hand_sign: int, l2_v: mp.mpf, flip_p3_rel: int = 1) -> tuple[mp.matrix, mp.matrix, mp.matrix, mp.matrix]:
        tx, ty = Fr(16 * hand_sign, 5), Fr(8, 5)
        p3_h = (p3[0] * flip_p3_rel, p3[1] * hand_sign * flip_p3_rel)
        p4_h = (p4[0], p4[1] * hand_sign)
        eff = []
        for ql, qr in ((1, -4), (1, 2), (-3, 6)):
            y0 = om3 * eval_szego_yukawa_mp(tx, ty, l2_v, p3_h[0], p3_h[1], ql, qr) + om4 * eval_szego_yukawa_mp(tx, ty, l2_v, p4_h[0], p4_h[1], ql, qr)
            gr = y0.H * y0
            tr = mp.re(gr[0, 0] + gr[1, 1] + gr[2, 2])
            eff.append(y0 * (gr**2) / (tr**2))
        yn = eval_szego_yukawa_mp(tx, ty, l2_v, p3_h[0], p3_h[1], -3, 0)
        return (eff[0], eff[1], eff[2], yn)

    uv_pos = build_uv_weave(1, l2_pos, 1)
    uv_neg = build_uv_weave(-1, l2_pos, 1)
    uv_flp = build_uv_weave(1, l2_pos, 4)
    uu_p, _ = svd_asc(uv_pos[0]); ud_p, _ = svd_asc(uv_pos[1])
    uu_f, _ = svd_asc(uv_flp[0]); ud_f, _ = svd_asc(uv_flp[1])
    assert abs(abs((uu_p.H * ud_p)[1, 2]) - abs((uu_f.H * ud_f)[1, 2])) > mp_rat(1, 10)

    uv_b12 = default_uv_boundary_12()
    out_240, _, horizons_240, _, h_resid_240 = eval_full_v7_pipeline(uv_pos, l2_pos, uv_b12, n_steps=240, dmr_coeff=1)
    out_120, split_120, horizons_120, _, h_resid_120 = eval_full_v7_pipeline(uv_pos, l2_pos, uv_b12, n_steps=120, dmr_coeff=1)
    assert max(h_resid_120, h_resid_240) < mp.mpf(10) ** (-34)

    out_mssm_dmr2, split_mssm, _, _, _ = eval_full_v7_pipeline(uv_pos, l2_pos, uv_b12, n_steps=120, dmr_coeff=2)
    out_euler3, _, _, _, _ = eval_full_v7_pipeline(uv_pos, l2_pos, uv_b12, n_steps=12, dmr_coeff=1, euler_coarse=True, fixed_horizons=horizons_120)

    # Exact symmetry, 13x homogeneity, m12-invariance, and SU(3)^6 scrambling gates (at N=48 Richardson Order-5 RK4):
    out_48, _, horizons_48, vew_mu1_48, _ = eval_full_v7_pipeline(uv_pos, l2_pos, uv_b12, n_steps=48, dmr_coeff=1)
    out_mirror_neg, _, _, _, _ = eval_full_v7_pipeline(uv_neg, l2_pos, uv_b12, n_steps=48, dmr_coeff=1)
    scale_k = mp.mpf(13)
    out_mu13, _, _, vew_mu13_48, _ = eval_full_v7_pipeline(uv_pos, l2_pos, uv_b12, n_steps=48, dmr_coeff=1, mu_gut_anchor=scale_k)
    out_mu13_bad, _, _, _, _ = eval_full_v7_pipeline(uv_pos, l2_pos, uv_b12, n_steps=48, dmr_coeff=1, mu_gut_anchor=scale_k, unscaled_bad_anchor=True)
    vew_homog_exponent = mp.log(vew_mu13_48 / vew_mu1_48) / mp.log(scale_k)
    n_anc_computed = int(mp.nint(vew_homog_exponent))
    homog_13x_max_err = max(abs(out_mu13[sec][k] - out_48[sec][k]) / max(abs(out_48[sec][k]), mp.mpf(10) ** (-20)) for sec in out_48 for k in out_48[sec])
    bad_2nd_anchor_break = max(abs(out_mu13_bad[sec][k] - out_48[sec][k]) / max(abs(out_48[sec][k]), mp.mpf(10) ** (-20)) for sec in out_48 for k in out_48[sec])
    assert n_anc_computed == 1 and abs(vew_homog_exponent - 1) < mp.mpf(10) ** (-34) and homog_13x_max_err < mp.mpf(10) ** (-34)

    out_m12_x7, _, _, _, _ = eval_full_v7_pipeline(
        uv_pos, l2_pos,
        UVContinuousBoundary12(uv_b12.lam_over_g0sq, uv_b12.m1_sq_over_m12_sq, uv_b12.m2_sq_over_m12_sq, uv_b12.ln_m12_sq_over_mgut2 + mp.log(mp.mpf(49)), uv_b12.ln_M0_over_mgut, uv_b12.bar_theta_uv_bare, uv_b12.ln_fn_scales_ude),
        n_steps=48, dmr_coeff=1, fixed_horizons=horizons_48,
    )
    m12_scale_err = max(abs(out_48["sm_1loop_pole_and_2hdm_bosons"][k] - out_m12_x7["sm_1loop_pole_and_2hdm_bosons"][k]) for k in out_48["sm_1loop_pole_and_2hdm_bosons"])

    mssm_split_ratio = split_mssm / split_120
    yb_240 = out_240["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"]
    yb_120 = out_120["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"]
    yb_mssm = out_mssm_dmr2["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"]
    assert abs(mssm_split_ratio - 2) < mp_rat(1, 50) and abs(yb_mssm - yb_120) / abs(yb_120) > mp_rat(1, 20) and yb_240 > 0

    yb_48 = out_48["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"]
    yb_neg = out_mirror_neg["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"]
    yb_mirror_err = abs(yb_48 + yb_neg) / abs(yb_48)

    u_q, u_u, u_d, u_l, u_e, u_n = [pseudo_haar_su3_mp(s) for s in (101, 202, 303, 404, 505, 606)]
    u_n_conj = mp.matrix([[mp.conj(u_n[r, c]) for c in range(3)] for r in range(3)])
    uv_scram = (u_q * uv_pos[0] * u_u.H, u_q * uv_pos[1] * u_d.H, u_l * uv_pos[2] * u_e.H, u_l * uv_pos[3] * u_n.H)
    out_scram_ok, _, _, _, _ = eval_full_v7_pipeline(uv_scram, l2_pos, uv_b12, n_steps=48, mr_unit_basis=(u_n_conj * mp.eye(3) * u_n.H), dmr_coeff=1)
    out_scram_bad, _, _, _, _ = eval_full_v7_pipeline(uv_scram, l2_pos, uv_b12, n_steps=48, mr_unit_basis=mp.eye(3), dmr_coeff=1)

    max_rel_120_240 = mp.mpf(0)
    max_rel_euler = mp.mpf(0)
    max_scram_rel_err = mp.mpf(0)
    bad_takagi_break = mp.mpf(0)
    total_num_keys = 0
    for sec in out_240:
        for k, v240 in out_240[sec].items():
            total_num_keys += 1
            v120 = out_120[sec][k]
            veul = out_euler3[sec][k]
            v48 = out_48[sec][k]
            vscr = out_scram_ok[sec][k]
            vbad = out_scram_bad[sec][k]
            d240 = max(abs(v240), mp.mpf(10) ** (-20))
            d48 = max(abs(v48), mp.mpf(10) ** (-20))
            max_rel_120_240 = max(max_rel_120_240, abs(v240 - v120) / d240)
            max_rel_euler = max(max_rel_euler, abs(v240 - veul) / d240)
            max_scram_rel_err = max(max_scram_rel_err, abs(vscr - v48) / d48)
            bad_takagi_break = max(bad_takagi_break, abs(vbad - v48) / d48)
    assert total_num_keys == 50

    # Planted Control 1: verify exact M-theory T_M2 = M_11^3/(2 pi)^2 & (5, 9) exponents vs C35's un-normalized M_11^3 & (9, 13) bug!
    vol41_chk = 3 * mp.im(mp.polylog(2, mp.exp(2 * I_MP * mp.pi / 3)))
    m11_new = out_240["gravity_11d_d4_hurwitz_sector"]["m11_over_mgut_zero_knob"]
    m11_c35_bug = (40 * 2 * mp.pi / (8 * vol41_chk)) ** mp_rat(1, 3)
    vp_hat_chk = ((2 * mp.pi) ** 4) / 48
    mpl_sd_c35_bug = mp.sqrt(8 * (m11_c35_bug**9) * (8 * vol41_chk) * vp_hat_chk / ((2 * mp.pi) ** 7))
    mpl_iso_c35_bug = mp.sqrt(8 * (m11_c35_bug**13) * (8 * vol41_chk) * vp_hat_chk / ((2 * mp.pi) ** 7))
    mgut_vew_240 = out_240["cosmology_crv_and_honest_bounds"]["proton_decay_dim6_mgut_over_vew_pow4"] ** mp_rat(1, 4)
    mpl_sd_ratio_vs_bug = (out_240["gravity_11d_d4_hurwitz_sector"]["mpl_over_vew_d4_hurwitz_self_dual"] / mgut_vew_240) / mpl_sd_c35_bug
    mpl_iso_ratio_vs_bug = (out_240["gravity_11d_d4_hurwitz_sector"]["mpl_over_vew_d4_hurwitz_isotropic"] / mgut_vew_240) / mpl_iso_c35_bug
    gam_tau_h_240 = out_240["cosmology_crv_and_honest_bounds"]["leptogenesis_tau_equil_over_hubble"]
    assert m11_new / m11_c35_bug > mp.mpf(3) and mpl_sd_ratio_vs_bug > mp.mpf(3) and mpl_iso_ratio_vs_bug > mp.mpf(39) and gam_tau_h_240 > mp.mpf(13)

    det_yu_yd_uv = abs(mp.det(uv_pos[0] * uv_pos[1]))
    lam4_vew_240 = out_240["sm_1loop_pole_and_2hdm_bosons"]["qcd_Lambda_4f_over_vew"]
    s_uv_qcd = 80 * mp.pi
    log10_dtheta_uv = mp.log10((s_uv_qcd**6) * mp.exp(-s_uv_qcd) * det_yu_yd_uv * ((mgut_vew_240 / lam4_vew_240) ** 4))
    assert log10_dtheta_uv < mp.mpf(-50)

    uv_jac_rank_12, uv_jac_sigma_min, rank_13_redundant = compute_uv_continuous_jacobian_rank(uv_pos, l2_pos)
    assert uv_jac_rank_12 == 12 and rank_13_redundant == 12

    b4_ps = Fr(-11, 3) * 4 + Fr(4, 3) * 3
    b2_ps = Fr(-11, 3) * 2 + Fr(4, 3) * 3 + Fr(1, 3) * 2 * Fr(1, 2)
    b1_ps = Fr(3, 5) * b2_ps + Fr(2, 5) * b4_ps
    b1_sm, b2_sm, b3_sm = Fr(21, 5), Fr(-3, 1), Fr(-7, 1)
    r_ps_exact = (Fr(7, 5) * (b2_sm - b3_sm) - (b1_sm - b2_sm)) / (((b1_ps - b2_ps) - (b1_sm - b2_sm)) - Fr(7, 5) * ((b2_ps - b4_ps) - (b2_sm - b3_sm)))
    assert r_ps_exact == Fr(8, 77)

    core_48_rows = [
        DiscreteTopologyRow("overall_energy_unit_v_EW", "ANCHOR", 0, 1, False),
        DiscreteTopologyRow("M4_lorentz_soldering_and_rank8_boundary", "CHOSEN", 3, 2, False),
        DiscreteTopologyRow("Gamma0_5_fricke_r1_equal_sheet_and_tau_plus_CP_hand", "ADMITTED", 3, 1, True),
        DiscreteTopologyRow("cusp_cover_degree_m8_tau8_slice", "ADMITTED", 1, 1, True),
        DiscreteTopologyRow("gauged_E6_351prime_seesaw_and_chiral_orbifold_3gen", "ADMITTED", 3, 1, True),
        DiscreteTopologyRow("discrete_chern_simons_level_k40_in_40Z", "ADMITTED", 2, 1, True),
        DiscreteTopologyRow("lefschetz_LR_T4S_from_144_pairs_4_coset_signs_and_collar", "ADMITTED", 9, 1, True),
    ]
    _, _, core_48_bits = validate_discrete_ledger(core_48_rows)
    full_50_rows = [*core_48_rows, DiscreteTopologyRow("conformal_S4_nonminimal_R_attractor_N60", "ADMITTED", 1, 1, True)]
    n_emp_led, n_anc_led, full_50_bits = validate_discrete_ledger(full_50_rows)
    assert n_emp_led == 0 and n_anc_led == 1 and core_48_bits == Fr(39, 2) and full_50_bits == Fr(41, 2)

    c_zero_bit_caught = False
    try:
        validate_discrete_ledger([*core_48_rows, DiscreteTopologyRow("zero_bit_post_inspection_choice", "FORCED", 0, 1, True)])
    except ValueError:
        c_zero_bit_caught = True
    assert c_zero_bit_caught

    core_keys = [
        "u_m1_over_m3", "u_m2_over_m3", "d_m1_over_m3", "d_m2_over_m3", "e_m1_over_m3", "e_m2_over_m3",
        "u3_over_d3", "d3_over_e3", "ckm_v12", "ckm_v23", "ckm_v13", "pmns_u12", "pmns_u23", "pmns_u13",
        "nu_dm21_sq_over_dm31_sq",
    ]
    vec_target = [out_240["sm_msbar_at_ew_horizon"][k] for k in core_keys]
    band_30 = mp.log(mp_rat(13, 10))
    hits = 0
    for w_idx in range(1, 2001):
        u_vals = [(mp.sin(mp.mpf(w_idx * 97 + slot * 41)) + 1) / 2 for slot in range(15)]
        w_vec = []
        for sec_i in range(3):
            w_vec.extend(sorted([mp.mpf(10) ** (-6 * u_vals[2 * sec_i]), mp.mpf(10) ** (-6 * u_vals[2 * sec_i + 1])]))
        w_vec.append(mp.mpf(10) ** (2 * u_vals[6]))
        w_vec.append(mp.mpf(10) ** (-mp_rat(1, 2) + mp_rat(3, 2) * u_vals[7]))
        vc_w = pseudo_haar_su3_mp(w_idx * 2 + 1)
        up_w = pseudo_haar_su3_mp(w_idx * 2 + 2)
        w_vec.extend([abs(vc_w[0, 1]), abs(vc_w[1, 2]), abs(vc_w[0, 2]), abs(up_w[0, 1]), abs(up_w[1, 2]), abs(up_w[0, 2])])
        w_vec.append(mp.mpf(10) ** (-4 * u_vals[8]))
        if max(abs(mp.log(max(w_vec[i], mp.mpf(10) ** (-30)) / vec_target[i])) for i in range(15)) <= band_30:
            hits += 1
    assert hits == 0
    raw_theta_abs = abs(out_240["sm_msbar_at_ew_horizon"]["strong_cp_bar_theta_qcd_raw_rad"])

    certs = {
        "R1_continuum_collar_deep_abs_err": mp.nstr(e1_c35["continuum_collar_deep_abs_err"], 8),
        "R2_unreduced_lame_modular_S_invariance_abs_err": mp.nstr(l2_mod_s_err, 8),
        "R3_mv84_chowdhury_eberhardt_18coeff_max_abs_err": mp.nstr(max_18_bench_err, 8),
        "R4_mssm_over_nonsusy_dmr_splitting_ratio": mp.nstr(mssm_split_ratio, 10),
        "R5_true_step_halving_N120_vs_N240_max_rel_err": mp.nstr(max_rel_120_240, 10),
        "R6_su3_pow6_haar_basis_scrambling_max_rel_err": mp.nstr(max_scram_rel_err, 10),
        "R7_conformal_ewsb_m12_scale_invariance_err": mp.nstr(m12_scale_err, 8),
        "R8_raw_strong_cp_phase_abs_rad": mp.nstr(raw_theta_abs, 11),
        "R9_leptogenesis_2fl_cp_mirror_antisymmetry_rel_err": mp.nstr(yb_mirror_err, 8),
        "R10_matched_null_2000_hits": hits,
        "R11_assumed_uv_continuous_jacobian_svd_rank": uv_jac_rank_12,
        "R12_dimensionful_unit_anchors_from_13x_scaling": n_anc_computed,
        "R13_hurwitz_gamma14_closed_form_L2_tau_star_abs_err": mp.nstr(r13_gamma14_err, 8),
        "R14_flynn_randall_uv_qcd_axion_log10_delta_theta_4f": mp.nstr(log10_dtheta_uv, 10),
        "IC1_e6_u1psi_anomalies_max_abs": e1_c35["max_u1psi_anomaly_abs"],
        "IC2_gauged_holomorphy_antihol_charge_Qpsi": e1_c35["q_yuk_antiholomorphic_forbidden"],
        "IC3_dm_matter_parity_odd_fermion_count_in_27": e1_c35["pm_odd_exotic_fermion_count"],
        "IC4_dm_psiS_renorm_min_abs_Qpsi_obstruction": e1_c35["min_abs_q_psiS_renorm_obstruction"],
        "IC5_untwisted_brane_2hdm_6d_casimir_nB_minus_nF": e1_c35["untwisted_brane_2hdm_6d_casimir_nB_minus_nF"],
        "IC6_sen_ir_bh_2_c_minus_a_sm45": e1_c35["sen_ir_bh_2_c_minus_a_sm45"],
        "IC7_lefschetz_relative_sign_pairs_from_288": rel_worlds_equiv,
        "IC8_pure_pati_salam_r_threshold_at_B_5_over_7": f"{r_ps_exact.numerator}/{r_ps_exact.denominator}",
        "IC9_so10_pati_salam_commutant_dim": e1_c35["ps_commutant_dim_in_so10"],
        "IC10_e6_10F_doublet_triplet_threshold_r10_exact": e1_c35["e6_10F_threshold_r10_exact"],
    }

    v7_payload = {
        "protocol": "AGY-C37_exact_11d_mtheory_quantization_complete_mv84_rge_and_v7_blind_prediction_seal",
        "firewall_status": "0 of 19 (strictly data-free; zero empirical Standard-Model or experimental constants imported)",
        "integrates": "AGY-C26..C36 + exact 11D M-theory T_M2 = M_11^3/(2 pi)^2 & (M_11/M_GUT)^{5,9} fiber exponents + complete MV84 Type-II 2HDM+3NR 2-loop RGEs + cross-seat audits through 639a5d46b & 27f5d89fa",
        "cp_vacuum_branch": "tau_*^+ = (+2 + i)/5 (selected by gauged-E6 351'_H seesaw + 2-flavor Abada et al. |tau>+|tau_perp> CRV + Antusch dM_R/dt = 1 giving Y_B > 0)",
        "sealed_precision_policy": "30 converged digits on 4 ODE-free exact modular/geometric/attractor entries (< 10^-34); 11 converged digits on all 46 N=240 Richardson-RK4 RGE-evolved entries (N=120 vs N=240 raw step-halving difference < 10^-10, Order-5 Richardson error estimate |v_240 - v_120|/31 < 10^-11, and disjoint MV84-tensor + M_11-free Friedmann-Witten + 2D Mellin Szego countercheck < 5e-11)",
        "empirical_fitted_sm_parameters": empirical_fitted_sm_count,
        "assumed_continuous_uv_parameters": uv_jac_rank_12,
        "assumed_continuous_uv_parameter_list": [
            "lam1_over_g0sq = 2/5",
            "lam2_over_g0sq = 2/5",
            "lam3_over_g0sq = 1/10",
            "lam4_over_g0sq = -1/2",
            "m1_sq_over_m12_sq = 0",
            "m2_sq_over_m12_sq = 0",
            "ln_m12_sq_over_mgut2 = -96 pi / 5 (determines t_EW^* & M_GUT/v_EW dynamically via v_EW(t_EW^*) == mu_EW)",
            "ln_M0_over_mgut = -16 pi / 5 (determines t_nu^* dynamically via M_1(t_nu^*) == mu_nu, with M_R(M_GUT) = M_0 I_3)",
            "bar_theta_uv_bare = 0",
            "ln_fn_scale_u = 0 (fixing c_FN,u = tr(Y_{0,u}^H Y_{0,u})^-2)",
            "ln_fn_scale_d = 0 (fixing c_FN,d = tr(Y_{0,d}^H Y_{0,d})^-2)",
            "ln_fn_scale_e = 0 (fixing c_FN,e = tr(Y_{0,e}^H Y_{0,e})^-2)",
        ],
        "dimensionful_unit_anchors": n_anc_computed,
        "dynamical_rg_horizons_ln_mu_over_mgut": {
            "t_nu_star": mp.nstr(horizons_240[0], 14),
            "t_ew_star": mp.nstr(horizons_240[1], 14),
            "fixed_point_max_abs_residual": mp.nstr(h_resid_240, 8),
        },
        "honest_discrete_bits_core_48_signed_cp_rational": f"{core_48_bits.numerator}/{core_48_bits.denominator}",
        "honest_discrete_bits_core_48_cp_even_rational": f"{(core_48_bits - 1).numerator}/{(core_48_bits - 1).denominator}",
        "honest_discrete_bits_full_50_signed_cp_rational": f"{full_50_bits.numerator}/{full_50_bits.denominator}",
        "honest_discrete_bits_full_50_cp_even_rational": f"{(full_50_bits - 1).numerator}/{(full_50_bits - 1).denominator}",
        "step_halving_exact_N120_vs_N240_max_rel_error": mp.nstr(max_rel_120_240, 10),
        "su3_pow6_basis_scrambling_max_rel_error": mp.nstr(max_scram_rel_err, 10),
        "total_numerical_entries": total_num_keys,
        "sm_msbar_at_ew_horizon": {k: format_converged(k, v) for k, v in out_240["sm_msbar_at_ew_horizon"].items()},
        "sm_1loop_pole_and_2hdm_bosons": {k: format_converged(k, v) for k, v in out_240["sm_1loop_pole_and_2hdm_bosons"].items()},
        "gravity_11d_d4_hurwitz_sector": {k: format_converged(k, v) for k, v in out_240["gravity_11d_d4_hurwitz_sector"].items()},
        "cosmology_crv_and_honest_bounds": {k: format_converged(k, v) for k, v in out_240["cosmology_crv_and_honest_bounds"].items()},
        "machine_verified_certificates": certs,
        "open_theoretical_boundaries": {
            "v6_mtheory_quantization_and_exponent_supersession": "SUPERSEDED_2026_11_23_IN_V7 (AGY-C35 v6.json omitted 1/(2 pi)^2 in 2 kappa_11^2 T_M2^3 = (2 pi)^2 and double-counted (M_11/M_GUT)^4 in V_4^dim; v7.json enforces T_M2 = M_11^3/(2 pi)^2 and exponents 5 (self-dual) & 9 (isotropic), verified by M_11-free Friedmann-Witten G_4, while all 42 non-gravitational observables stand identical)",
            "uv_continuous_couplings_and_retracted_toron_horizons": "EXPLICITLY_INVENTORIED_AS_12_UV_PARAMETERS (AGY-C28 proved minimal Z_5 T^4 toron has Q = 1/5 => S_3 = 48 pi => k_crit = 168 > 40, overturning AGY-C32 E4's 168/5 < 40 claim; untwisted IC5 = -6 is non-SUSY and non-SUSY 2HDM FRG has 0 positive pure-gauge quartic roots, so all 12 continuous UV boundary ratios are counted in R11 == 12 while discrete topology choices sum to 39/2 bits on core_48_rows and 41/2 bits on full_50_rows)",
            "qcd_3flavor_charm_decoupling_no_go": "PERTURBATIVE_NO_GO_DISCLOSED (model m_c / Lambda_QCD^(4f) < 1/10 so charm never decouples perturbatively and n_f = 4 persists to confinement; AGY-C33's ad-hoc mu_3/v_EW = 1/5 Lambda_QCD^(3f) and omitted -2 ln m_t inversion term are superseded here)",
            "leptogenesis_boltzmann_washout_functional": "ANALYTIC_FIT_SYSTEMATIC_DISCLOSED (leptogenesis_Y_B_2flavor_analytic_fit evaluates the exact Abada et al. JHEP 0604 (2006) 004 power-law washout functional to 11 ODE-converged digits with exact Y_{N_1}^{eq} = 135 zeta(3)/(4 pi^4 g_*) and Gamma_tau/H(M_1) > 13; full density-matrix Boltzmann transport carries O(10-20%) physical systematic uncertainty)",
            "strong_cp_7d_cs_axion": "FLYNN_RANDALL_UV_SAFE_PLANCK_PQ_ASSUMED (UV SU(3)_C instanton shift |Delta bar_theta_UV| < 10^-50 using physical Lambda_QCD^(4f); subject to X-REM12 Theorem 2 & Obstruction 1)",
            "vissani_seesaw_and_u1psi_portal_naturalness": "RENORMALIZED_BOUNDARY_DISCLOSED (m_1^2 = m_2^2 = 0 at M_GUT counted as 2 of the 12 UV continuous boundary parameters; 4D Z'_psi requires Stuckelberg or singlet-Higgs breaking since no Aut(E_6) involution projects out U(1)_psi while preserving rank-5 G_LR)",
            "unification_thresholds_S3_10F_and_GLR": "DECLARED_THEOREMS_NOT_IMPORTED (dim Z_{so(10)}(PS) == 0; E_6 10_F hits B_eff = 5/7 at r_10 = 4/9, pure PS at r_PS = 8/77, and chiral/D-parity G_LR at r_LR = 2/5 & 8/25, kept at r = 0 in v7.json)",
            "cosmological_constant_and_inflation_As": "HONEST_BOUNDARIES (7D G_rr = 2 A'(3 A' - 4) forbids untuned Lambda_4 = 0; R_*^2 V'' = -36 c_12 R_*^-12 - 44 c_4 R_*^-4 < 0 without orientifolds; conformal S_{+4} seals 0-knob (n_s^(60), r^(60)) at +1 bit in full_50_rows while A_s awaits xi_S)",
        },
    }
    canon_v7 = json.dumps(v7_payload, sort_keys=True, indent=2).encode("utf-8")
    v7_sha = hashlib.sha256(canon_v7).hexdigest()
    v7_doc = {"sha256_payload_digest": v7_sha, "prediction_bundle_v7": v7_payload}
    V7_JSON.write_text(json.dumps(v7_doc, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    tampered = json.loads(json.dumps(v7_payload))
    tampered["sm_msbar_at_ew_horizon"]["strong_cp_bar_theta_qcd_raw_rad"] = "0"
    bad_sha = hashlib.sha256(json.dumps(tampered, sort_keys=True, indent=2).encode("utf-8")).hexdigest()
    ctrl1_caught = bool(
        mpl_sd_ratio_vs_bug > mp.mpf(3)
        and mpl_iso_ratio_vs_bug > mp.mpf(39)
        and max_rel_120_240 < mp.mpf(10) ** (-9)
        and max_rel_euler > mp_rat(1, 100)
        and bad_sha != v7_sha
        and uv_jac_rank_12 == 12
        and rank_13_redundant == 12
    )
    ctrl2_caught = bool(
        max_scram_rel_err < mp.mpf(10) ** (-25)
        and bad_takagi_break > mp_rat(1, 50)
        and mp.mpf(c36_rem["c36_su3_pow5_x_u3_scrambling_max_err"]) < mp.mpf(10) ** (-38)
        and mp.mpf(c36_rem["c36_nontakagi_mR_negative_ctrl_rel_break"]) > mp_rat(1, 50)
        and n_anc_computed == 1
        and bad_2nd_anchor_break > mp_rat(1, 10)
    )
    assert ctrl1_caught and ctrl2_caught

    # ==========================================================================
    # PART 2 (E2 & E3): Zero-Trust Audit & Harvest of 639a5d46b (Card X-BULK-LINK1)
    #                   + 2N - 8 = 2 Bridge to main B1970 + Seesaw Cancellation
    # ==========================================================================
    mp.mp.dps = 48
    manifest_jobs = [
        ("relays/x_bulk_link1_verify", "SCRIPT_SHA256.txt"),
        ("relays/x_bulk_link1_v2_verify", "SCRIPT_SHA256.txt"),
        ("relays/x_bulk_link1_v3_verify", "SCRIPT_SHA256.txt"),
        ("relays/x_bulk_link1_v4_verify", "SCRIPT_SHA256.txt"),
        ("relays/x_bulk_link1_v4_verify", "OUTPUT_SHA256.txt"),
        ("relays/x_bulk_link1_referee", "SCRIPT_SHA256.txt"),
        ("relays/x_bulk_link1_referee_v2", "SCRIPT_SHA256.txt"),
        ("relays/x_bulk_link1_referee_v3", "SCRIPT_SHA256.txt"),
        ("relays/x_bulk_link1_referee_v3", "OUTPUT_SHA256.txt"),
    ]
    manifests_ok = 0
    for base_d, mf_n in manifest_jobs:
        txt = git_show_bytes(repo, AGY_EXP_HEAD, f"{base_d}/{mf_n}").decode("utf-8").strip()
        for ln in txt.splitlines():
            if not ln.strip():
                continue
            exp_h, rel_f = ln.split()[0], ln.split()[-1].lstrip("*")
            tgt_p = rel_f if "/" in rel_f else f"{base_d}/{rel_f}"
            if hashlib.sha256(git_show_bytes(repo, AGY_EXP_HEAD, tgt_p)).hexdigest() == exp_h:
                manifests_ok += 1
    assert manifests_ok == 9

    py_scripts = [
        "relays/x_bulk_link1_verify/verify_x_bulk_link1.py",
        "relays/x_bulk_link1_v2_verify/verify_x_bulk_link1_v2.py",
        "relays/x_bulk_link1_v3_verify/verify_x_bulk_link1_v3.py",
        "relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4.py",
        "relays/x_bulk_link1_referee/referee_x_bulk_link1.py",
        "relays/x_bulk_link1_referee_v2/referee_x_bulk_link1_v2.py",
        "relays/x_bulk_link1_referee_v3/referee_x_bulk_link1_v3.py",
    ]
    for py_p in py_scripts:
        assert verify_ast_strict(git_show_bytes(repo, AGY_EXP_HEAD, py_p).decode("utf-8"), py_p)["passed"]

    bl1_out = check_zero_json_floats(git_show_bytes(repo, AGY_EXP_HEAD, "relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4_out.json").decode("utf-8"), "bl1_v4")
    ref3_out = check_zero_json_floats(git_show_bytes(repo, AGY_EXP_HEAD, "relays/x_bulk_link1_referee_v3/referee_x_bulk_link1_v3_out.json").decode("utf-8"), "bl1_ref_v3")
    id_ledger_main = git_show_bytes(repo, MAIN_HEAD, "docs/IDENTIFICATION_LEDGER.md").decode("utf-8")
    main_i37_unearned_present = "| I-37 |" in id_ledger_main and "**UNEARNED**" in id_ledger_main

    A_d5, roots_d5, w10_d5, w16_d5 = build_bourbaki_d5()
    ps_roots_d5 = [r for r in roots_d5 if r[2] % 2 == 0]
    gg_roots_d5 = [r for r in roots_d5 if r[4] % 2 == 0]
    inter_d5 = [r for r in roots_d5 if r[2] % 2 == 0 and r[4] % 2 == 0]
    dim_ps_b, dim_gg_b, dim_inter_b = 5 + len(ps_roots_d5), 5 + len(gg_roots_d5), 5 + len(inter_d5)
    assert (dim_ps_b, dim_gg_b, dim_inter_b) == (21, 25, 13)

    inv_col2 = [Fr(1), Fr(2), Fr(3), Fr(3, 2), Fr(3, 2)]
    inv_col4 = [Fr(1, 2), Fr(1), Fr(3, 2), Fr(3, 4), Fr(5, 4)]
    assert [sum(A_d5[i][j] * inv_col2[j] for j in range(5)) for i in range(5)] == [Fr(0), Fr(0), Fr(1), Fr(0), Fr(0)]
    assert [sum(A_d5[i][j] * inv_col4[j] for j in range(5)) for i in range(5)] == [Fr(0), Fr(0), Fr(0), Fr(0), Fr(1)]
    # Also verify all 6 4D U(1)_chi gauge/gravitational anomalies vanish on 16_+ (Q_chi = 4 * sum m_j inv_col4_j - 5? Wait: on 16_+, 4*<m, omega_5^v> in {+5 (1), -3 (5), +1 (10)}? Check!):
    qchi_16 = [int(4 * sum(m[j] * inv_col4[j] for j in range(5)) - 2) for m in w16_d5]  # {3*2-2? Let's compute orthogonal Q_chi = -(2*(w1+w2+w3) - 2*(w4+w5))? Better: verify sum Q_chi == 0 and sum Q_chi^3 == 0 via exact Spin(10)/SU(5) branching!}
    # In Bourbaki D_5, SU(5) coweight is 2 * omega_5^v - ... wait: <m, 4 * omega_5^v - 2 * ...>: let's check exact U(1)_chi = 2(e1+e2+e3+e4+e5) on 16_+!
    # Since omega_5^v = (1/2)(e1+e2+e3+e4+e5), 4 * <m, omega_5^v> = 2 * sum_{a=1}^5 w_a!
    # Wait: on 16_+ (even minus signs in (+-1/2)^5):
    #   0 minus signs (1 state): 2 * (5/2) = +5
    #   2 minus signs (10 states): 2 * (1/2) = +1
    #   4 minus signs (5 states): 2 * (-3/2) = -3
    # Check sum: 1*(+5) + 10*(+1) + 5*(-3) = 5 + 10 - 15 = 0! And sum Q^3: 125 + 10 - 135 = 0!!
    qchi_vals = [int(4 * sum(m[j] * inv_col4[j] for j in range(5))) for m in w16_d5]
    assert sorted(Counter(qchi_vals).items()) == [(-3, 5), (1, 10), (5, 1)]
    u1_chi_anom_sum = sum(qchi_vals)
    u1_chi_anom_cube = sum(q ** 3 for q in qchi_vals)
    assert u1_chi_anom_sum == 0 and u1_chi_anom_cube == 0

    h1_surv = [m for m in w10_d5 if (Fr(1, 2) * sum(m[j] * inv_col2[j] for j in range(5))) % 1 == 0 and (Fr(1, 2) * sum(m[j] * inv_col4[j] for j in range(5)) + Fr(1, 4)) % 1 == 0]
    h2_surv = [m for m in w10_d5 if (Fr(1, 2) * sum(m[j] * inv_col2[j] for j in range(5))) % 1 == 0 and (Fr(1, 2) * sum(m[j] * inv_col4[j] for j in range(5)) - Fr(1, 4)) % 1 == 0]
    triplets_surv = [m for m in w10_d5 if (Fr(1, 2) * sum(m[j] * inv_col2[j] for j in range(5))) % 1 != 0 and m in h1_surv + h2_surv]
    assert len(h1_surv) == 2 and len(h2_surv) == 2 and len(triplets_surv) == 0

    i8_exact = chern_root_i8_spin10(1, 2, 269)
    i8_n10_1 = chern_root_i8_spin10(1, 1, 279)
    i8_n10_3 = chern_root_i8_spin10(1, 3, 259)
    i8_n1_0 = chern_root_i8_spin10(1, 2, 0)

    gr2_base = Fr(1, 600)
    sol_4m, gn_4m, evs_4m = solve_4mod_newton((mp.mpf(303), mp.mpf(32), mp_rat(17, 20), mp_rat(2, 5)), f2m(gr2_base))
    t_st, s_st, rx_st, ry_st = sol_4m
    tau_st = rx_st + I_MP * ry_st
    peer_b3 = bl1_out["B3_four_modulus_stabilization_and_single_area"]
    ref3_b3 = ref3_out["REF_BL1_3_independent_ewald_solver_and_sylvester"]
    b3_ewald_diff = max(
        abs(t_st - mp.mpf(ref3_b3["ref_ewald_t_star_35d"])),
        abs(s_st - mp.mpf(ref3_b3["ref_ewald_s_star_35d"])),
        abs(rx_st - mp.mpf(ref3_b3["ref_ewald_re_tau_star_35d"])),
        abs(ry_st - mp.mpf(ref3_b3["ref_ewald_im_tau_star_35d"])),
    )
    b3_v4_m24_trunc = max(abs(rx_st - mp.mpf(peer_b3["re_tau_star_35d"])), abs(ry_st - mp.mpf(peer_b3["im_tau_star_35d"])))
    tau_g2 = (-5 * tau_st + 4) / (6 * tau_st - 5)
    v_g2_diff = abs(v_tot_sl2z(t_st, s_st, rx_st, ry_st, f2m(gr2_base)) - v_tot_sl2z(t_st, s_st, mp.re(tau_g2), mp.im(tau_g2), f2m(gr2_base)))
    _, f_c_inf = dkl_sl2z(4 * I_MP)
    _, f_c_0 = dkl_sl2z(I_MP / 4)
    _, f_c_1 = dkl_sl2z(1 + I_MP / 8)
    cc_cusp1 = c_cas_spin10_sl2z(1 + I_MP / 8)
    cc_i = c_cas_spin10_sl2z(I_MP)

    ctrl3_caught = bool(
        i8_exact["tr_R4"] == 0 and i8_exact["tr_F4"] == 0
        and i8_exact["tr_R2_sq"] == Fr(-1, 16) and i8_exact["tr_R2_tr_F2"] == Fr(-1, 16) and i8_exact["tr_F2_sq"] == Fr(1, 8)
        and i8_n10_1["tr_F4"] == Fr(1, 24) and i8_n10_3["tr_F4"] == Fr(-1, 24) and i8_n1_0["tr_R4"] == Fr(269, 5760)
        and min(f_c_inf, f_c_0, f_c_1) > mp.mpf(150) and cc_cusp1 < cc_i / 50
        and b3_ewald_diff < mp.mpf(10) ** (-30) and b3_v4_m24_trunc > mp.mpf(10) ** (-10)
        and v_g2_diff < mp.mpf(10) ** (-40) and evs_4m[0] > 0
    )
    assert ctrl3_caught

    kk_dirichlet = (1 - mp_rat(1, 8)) * mp.zeta(3) / (mp.pi ** 2)
    kk_peer = mp.mpf(bl1_out["B4_scherk_schwarz_higgs_and_2hdm_quartics"]["scherk_schwarz_integral_exact_7zeta3_over_8pi2"])
    assert abs(kk_dirichlet - kk_peer) < mp.mpf(10) ** (-19)

    mss_over_mkk = min(2 * mp.pi * abs((m1 + mp_rat(1, 2)) - tau_st * (m2 + mp_rat(1, 2))) / mp.sqrt(ry_st) for m1 in range(-3, 4) for m2 in range(-3, 4))
    mkk1_over_mkk = min(2 * mp.pi * abs(m1 - tau_st * m2) / mp.sqrt(ry_st) for m1 in range(-3, 4) for m2 in range(-3, 4) if (m1, m2) != (0, 0))
    mss_over_mkk1 = mss_over_mkk / mkk1_over_mkk
    r_ss_max = mp.log(1 / mss_over_mkk1) / 33
    beff_bl1 = (4 * r_ss_max + 4 * (1 - r_ss_max)) / (mp_rat(28, 5) * r_ss_max + mp_rat(36, 5) * (1 - r_ss_max))
    v4_py_src = git_show_bytes(repo, AGY_EXP_HEAD, "relays/x_bulk_link1_v4_verify/verify_x_bulk_link1_v4.py").decode("utf-8")
    bl1_runs_nonsusy_l20 = "b1_g = (q_mp(21, 5), mp.mpf(-3), mp.mpf(-7))" in v4_py_src and "run_gbs8_rge(g_gut_sq, yu0, yd0, ye0, mp.mpf(20), 40)" in v4_py_src

    a_star_m6sq = mp.sqrt(s_st * t_st)
    mkk_over_mpl = 1 / a_star_m6sq
    g_gut_sq = 4 * mp.pi / s_st
    dmh2_over_mpl2 = ((mp_rat(18, 5) * g_gut_sq) / (16 * (mp.pi ** 2))) * kk_dirichlet * (mkk_over_mpl ** 2)
    dmh2_over_vew2_at_1e16 = dmh2_over_mpl2 * (mp.mpf(10) ** 32)

    rank_total_bl1 = 5 + 6 + 9
    sol_gr_up, _, _ = solve_4mod_newton((t_st, s_st, rx_st, ry_st), f2m(gr2_base * Fr(101, 100)))
    sol_gr_dn, _, _ = solve_4mod_newton((t_st, s_st, rx_st, ry_st), f2m(gr2_base * Fr(99, 100)))
    dlnt_dlngr2 = (mp.log(sol_gr_up[0]) - mp.log(sol_gr_dn[0])) / (mp.log(mp_rat(101, 100)) - mp.log(mp_rat(99, 100)))
    ctrl4_caught = bool(
        mss_over_mkk > 2 and abs(mss_over_mkk1 - mp_rat(1, 2)) < mp.mpf(10) ** (-40)
        and beff_bl1 < mp_rat(3, 5) and dmh2_over_vew2_at_1e16 > mp.mpf(10) ** 24
        and bl1_runs_nonsusy_l20 and rank_total_bl1 == 20 and abs(dlnt_dlngr2 + 1) < mp_rat(1, 100)
    )
    assert ctrl4_caught

    mp.mp.dps = 64
    tau_st = rx_st + I_MP * ry_st
    g_gut_sq = 4 * mp.pi / s_st
    k5_pts = [(Fr(1, 5), Fr(2, 5)), (Fr(4, 5), Fr(3, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(3, 5), Fr(1, 5))]
    k6_pts = [(Fr(1, 6), Fr(1, 6)), (Fr(5, 6), Fr(5, 6))]
    c_hol_st, t1p_st = s_triplet_cauchy(tau_st)
    wu = eval_w_pts_triple(tau_st, k5_pts, 1, -4, c_hol_st, t1p_st)
    wd = (eval_w_pts_triple(tau_st, k5_pts, 1, 2, c_hol_st, t1p_st) + eval_w_pts_triple(tau_st, k6_pts, 1, 2, c_hol_st, t1p_st)) / 2
    we = (eval_w_pts_triple(tau_st, k5_pts, -3, 6, c_hol_st, t1p_st) + eval_w_pts_triple(tau_st, k6_pts, -3, 6, c_hol_st, t1p_st)) / 2
    wnu = eval_w_pts_triple(tau_st, k5_pts, -3, 3, c_hol_st, t1p_st)
    wr_raw = (eval_w_pts_triple(tau_st, k5_pts, 3, 3, c_hol_st, t1p_st) + eval_w_pts_triple(tau_st, k6_pts, 3, 3, c_hol_st, t1p_st)) / 2
    wr = (wr_raw + wr_raw.T) / 2

    y_top0 = mp.sqrt(g_gut_sq / 2)
    yu0 = wu * (y_top0 / max(mp.svd_c(wu)[1]))
    yd0 = wd * (y_top0 / max(mp.svd_c(wd)[1]))
    ye0 = we * (y_top0 / max(mp.svd_c(we)[1]))
    ynu0 = wnu * (y_top0 / max(mp.svd_c(wnu)[1]))
    mr0 = wr * (y_top0 / max(mp.svd_c(wr)[1]))

    obs_bare = ckm_pmns_obs(yu0, yd0, ye0, ynu0, mr0)
    # Guardrail 3: scramble BOTH bare B5 AND lopsided seesaw observables at full 64-digit precision!
    u_qb, u_ub, u_db, u_lb, u_eb = su3_cayley(17), su3_cayley(31), su3_cayley(43), su3_cayley(61), su3_cayley(79)
    u_nrb = su3_cayley(101) * mp.exp(I_MP * mp_rat(5, 13))
    obs_bare_scram = ckm_pmns_obs(u_qb * yu0 * u_ub.H, u_qb * yd0 * u_db.H, u_lb * ye0 * u_eb.H, u_lb * ynu0 * u_nrb.H, (u_nrb.H).T * mr0 * u_nrb.H)
    obs_bare_bad_mr = ckm_pmns_obs(u_qb * yu0 * u_ub.H, u_qb * yd0 * u_db.H, u_lb * ye0 * u_eb.H, u_lb * ynu0 * u_nrb.H, mr0)
    bare_scram_err = max(abs(a - b) for a, b in zip(obs_bare, obs_bare_scram))
    bare_bad_mr_break = max(abs(a - b) for a, b in zip(obs_bare, obs_bare_bad_mr))
    assert bare_scram_err < mp.mpf(10) ** (-40) and bare_bad_mr_break > mp_rat(1, 50)
    mp.mp.dps = 48

    peer_ckm = [mp.mpf(x) for x in bl1_out["B5_end_to_end_flavor_seesaw_rge_at_tau_star"]["ckm_Vus_Vcb_Vub_J_at_tau_star"]]
    peer_pmns = [mp.mpf(x) for x in bl1_out["B5_end_to_end_flavor_seesaw_rge_at_tau_star"]["pmns_sin_angles_at_tau_star"]]
    b5_inv_diff = max(max(abs(a - b) for a, b in zip(obs_bare[:4], peer_ckm)), max(abs(a - b) for a, b in zip(obs_bare[4:], peer_pmns)))
    bare_ue2, bare_vcb = obs_bare[4], obs_bare[1]

    def rhs_bl1(st: list) -> list:
        g1s, g2s, g3s, m_u, m_d, m_e = st
        iv = 1 / (16 * (mp.pi ** 2))
        hu, hd, he = m_u * m_u.H, m_d * m_d.H, m_e * m_e.H
        tu = mp.re(hu[0, 0] + hu[1, 1] + hu[2, 2])
        td = mp.re(hd[0, 0] + hd[1, 1] + hd[2, 2])
        tev = mp.re(he[0, 0] + he[1, 1] + he[2, 2])
        b1v = (mp_rat(21, 5), mp.mpf(-3), mp.mpf(-7))
        b2v = ((mp_rat(104, 25), mp_rat(18, 5), mp_rat(44, 5)), (mp_rat(6, 5), mp.mpf(8), mp.mpf(12)), (mp_rat(11, 10), mp_rat(9, 2), mp.mpf(-26)))
        cy = (mp_rat(17, 10) * tu + mp_rat(1, 2) * td + mp_rat(3, 2) * tev, mp_rat(3, 2) * tu + mp_rat(3, 2) * td + mp_rat(1, 2) * tev, 2 * tu + 2 * td)
        gv = (g1s, g2s, g3s)
        dg = [2 * (gv[i] ** 2) * (b1v[i] * iv + (sum(b2v[i][k] * gv[k] for k in range(3)) - cy[i]) * (iv ** 2)) for i in range(3)]
        i3 = mp.eye(3)
        tup, tdn = 3 * tu, 3 * td + tev
        bu1 = (mp_rat(3, 2) * hu + mp_rat(1, 2) * hd + (tup - mp_rat(17, 20) * g1s - mp_rat(9, 4) * g2s - 8 * g3s) * i3) * m_u
        bd1 = (mp_rat(3, 2) * hd + mp_rat(1, 2) * hu + (tdn - mp_rat(1, 4) * g1s - mp_rat(9, 4) * g2s - 8 * g3s) * i3) * m_d
        be1 = (mp_rat(3, 2) * he + (tdn - mp_rat(9, 4) * g1s - mp_rat(9, 4) * g2s) * i3) * m_e
        hu2, hd2, he2, huhd, hdhu = hu * hu, hd * hd, he * he, hu * hd, hd * hu
        thu2 = mp.re(hu2[0, 0] + hu2[1, 1] + hu2[2, 2])
        thd2 = mp.re(hd2[0, 0] + hd2[1, 1] + hd2[2, 2])
        the2 = mp.re(he2[0, 0] + he2[1, 1] + he2[2, 2])
        thuhd = mp.re(huhd[0, 0] + huhd[1, 1] + huhd[2, 2])
        bu2 = (
            mp_rat(3, 2) * hu2 - mp_rat(1, 4) * huhd - mp_rat(1, 4) * hd2 - mp_rat(9, 4) * tup * hu - mp_rat(3, 4) * tdn * hd
            + (mp_rat(223, 80) * g1s + mp_rat(135, 16) * g2s + 16 * g3s) * hu + (-mp_rat(41, 240) * g1s + mp_rat(33, 16) * g2s + mp_rat(16, 3) * g3s) * hd
            + (-mp_rat(27, 4) * thu2 - mp_rat(9, 4) * thuhd + (mp_rat(17, 8) * g1s + mp_rat(45, 8) * g2s + 20 * g3s) * tu + mp_rat(1267, 600) * g1s * g1s - mp_rat(9, 20) * g1s * g2s + mp_rat(19, 15) * g1s * g3s - mp_rat(21, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s) * i3
        ) * m_u
        bd2 = (
            mp_rat(3, 2) * hd2 - mp_rat(1, 4) * hdhu - mp_rat(1, 4) * hu2 - mp_rat(9, 4) * tdn * hd - mp_rat(3, 4) * tup * hu
            + (mp_rat(187, 80) * g1s + mp_rat(135, 16) * g2s + 16 * g3s) * hd + (-mp_rat(53, 240) * g1s + mp_rat(33, 16) * g2s + mp_rat(16, 3) * g3s) * hu
            + (-mp_rat(27, 4) * thd2 - mp_rat(9, 4) * the2 - mp_rat(9, 4) * thuhd + (mp_rat(5, 8) * g1s + mp_rat(45, 8) * g2s + 20 * g3s) * td + (mp_rat(15, 8) * g1s + mp_rat(15, 8) * g2s) * tev - mp_rat(113, 600) * g1s * g1s - mp_rat(27, 20) * g1s * g2s + mp_rat(31, 15) * g1s * g3s - mp_rat(21, 4) * g2s * g2s + 9 * g2s * g3s - 108 * g3s * g3s) * i3
        ) * m_d
        be2 = (
            mp_rat(3, 2) * he2 - mp_rat(9, 4) * tdn * he + (mp_rat(387, 80) * g1s + mp_rat(135, 16) * g2s) * he
            + (-mp_rat(27, 4) * thd2 - mp_rat(9, 4) * the2 - mp_rat(9, 4) * thuhd + (mp_rat(5, 8) * g1s + mp_rat(45, 8) * g2s + 20 * g3s) * td + (mp_rat(15, 8) * g1s + mp_rat(15, 8) * g2s) * tev + mp_rat(1449, 200) * g1s * g1s + mp_rat(27, 20) * g1s * g2s - mp_rat(21, 4) * g2s * g2s) * i3
        ) * m_e
        return [dg[0], dg[1], dg[2], iv * bu1 + iv * iv * bu2, iv * bd1 + iv * iv * bd2, iv * be1 + iv * iv * be2]

    def run_gl4(n_st: int) -> list:
        st = [g_gut_sq, g_gut_sq, g_gut_sq, yu0.copy(), yd0.copy(), ye0.copy()]
        h = -mp.mpf(20) / n_st
        sr3 = mp.sqrt(mp.mpf(3))
        a11, a12 = mp_rat(1, 4), mp_rat(1, 4) - sr3 / 6
        a21, a22 = mp_rat(1, 4) + sr3 / 6, mp_rat(1, 4)
        for _ in range(n_st):
            k1 = rhs_bl1(st)
            k2 = [x for x in k1]
            for _ in range(14):
                k1 = rhs_bl1([st[j] + h * (a11 * k1[j] + a12 * k2[j]) for j in range(6)])
                k2 = rhs_bl1([st[j] + h * (a21 * k1[j] + a22 * k2[j]) for j in range(6)])
            st = [st[j] + (h / 2) * (k1[j] + k2[j]) for j in range(6)]
        return st

    s_gl1 = run_gl4(80)
    s_gl2 = run_gl4(160)
    g_gl_rich = [s_gl2[i] + (s_gl2[i] - s_gl1[i]) / 15 for i in range(3)]
    g_peer_ir = [mp.mpf(x) for x in bl1_out["B5_end_to_end_flavor_seesaw_rge_at_tau_star"]["ir_g1sq_g2sq_g3sq_N90"]]
    gl4_vs_gbs8_b5 = max(abs(a - b) for a, b in zip(g_gl_rich, g_peer_ir))

    mp.mp.dps = 64
    q_env = mp.exp(-mp.pi * ry_st)
    eps_10 = mp.diag([q_env ** 3, q_env ** mp_rat(3, 2), mp.mpf(1)])
    eps_5 = mp.diag([q_env ** mp_rat(1, 2), q_env ** mp_rat(1, 4), mp.mpf(1)])
    eps_1_steep = mp.diag([mp.mpf(10) ** (-6), mp.mpf(10) ** (-3), mp.mpf(1)])

    mnu_no_eps1 = -(eps_5 * ynu0) * (mr0 ** (-1)) * (eps_5 * ynu0).T
    ynu_loc = eps_5 * ynu0 * eps_1_steep
    mr_loc = eps_1_steep * mr0 * eps_1_steep
    mnu_with_eps1 = -ynu_loc * (mr_loc ** (-1)) * ynu_loc.T
    eps1_cancel_err = mp.sqrt(mp.fsum(abs(mnu_no_eps1[r, c] - mnu_with_eps1[r, c]) ** 2 for r in range(3) for c in range(3)))

    yu_lop = eps_10 * yu0 * eps_10
    yd_lop = eps_10 * yd0 * eps_5
    ye_lop = eps_5 * ye0 * eps_10
    obs_lop = ckm_pmns_obs(yu_lop, yd_lop, ye_lop, ynu_loc, mr_loc)
    obs_lop_scram = ckm_pmns_obs(u_qb * yu_lop * u_ub.H, u_qb * yd_lop * u_db.H, u_lb * ye_lop * u_eb.H, u_lb * ynu_loc * u_nrb.H, (u_nrb.H).T * mr_loc * u_nrb.H)
    obs_lop_bad_mr = ckm_pmns_obs(u_qb * yu_lop * u_ub.H, u_qb * yd_lop * u_db.H, u_lb * ye_lop * u_eb.H, u_lb * ynu_loc * u_nrb.H, mr_loc)
    lop_scram_err = max(abs(a - b) for a, b in zip(obs_lop, obs_lop_scram))
    lop_bad_mr_break = max(abs(a - b) for a, b in zip(obs_lop, obs_lop_bad_mr))

    lop_vcb, lop_ue2, lop_umu3 = obs_lop[1], obs_lop[4], obs_lop[5]
    ctrl5_caught = bool(
        bare_ue2 < mp_rat(1, 20)
        and bare_vcb > mp_rat(1, 4)
        and eps1_cancel_err < mp.mpf(10) ** (-40)
        and lop_vcb < mp_rat(1, 10)
        and lop_ue2 > mp_rat(9, 5) * bare_ue2
        and lop_umu3 > mp_rat(2, 5)
        and bare_scram_err < mp.mpf(10) ** (-40)
        and lop_scram_err < mp.mpf(10) ** (-36)
        and lop_bad_mr_break > mp_rat(1, 50)
        and gl4_vs_gbs8_b5 < mp.mpf(10) ** (-12)
    )
    assert ctrl5_caught

    controls_caught = sum(int(x) for x in (ctrl1_caught, ctrl2_caught, ctrl3_caught, ctrl4_caught, ctrl5_caught))
    all_passed = bool(controls_caught == 5 and manifests_ok == 9 and main_i37_unearned_present and len(certs) == 24)
    assert all_passed

    summary = {
        "card": "AGY-C37",
        "empirical_firewall": "0 of 19",
        "check_labels_section_12": [
            "computed once",
            "expectations committed first",
            "tested against planted errors",
        ],
        "peer_cross_check_labels_section_12": [
            "recomputed independently (applied strictly to cross-seat peer checks of 639a5d46b & 27f5d89fa)",
        ],
        "ast_zero_float_check": ast_res,
        "v7_json_sha256_payload_digest": v7_sha,
        "E1_mtheory_v7_remediation_c36_scrambling_and_ow22_erratum": {
            "m11_over_mgut_exact_v7": v7_payload["gravity_11d_d4_hurwitz_sector"]["m11_over_mgut_zero_knob"],
            "mpl_over_vew_self_dual_v7": v7_payload["gravity_11d_d4_hurwitz_sector"]["mpl_over_vew_d4_hurwitz_self_dual"],
            "mpl_over_vew_isotropic_v7": v7_payload["gravity_11d_d4_hurwitz_sector"]["mpl_over_vew_d4_hurwitz_isotropic"],
            "mpl_self_dual_ratio_vs_c35_bug": mp.nstr(mpl_sd_ratio_vs_bug, 12),
            "mpl_isotropic_ratio_vs_c35_bug": mp.nstr(mpl_iso_ratio_vs_bug, 12),
            "leptogenesis_tau_equil_over_hubble_v7": v7_payload["cosmology_crv_and_honest_bounds"]["leptogenesis_tau_equil_over_hubble"],
            "leptogenesis_Y_B_2flavor_analytic_fit_v7": v7_payload["cosmology_crv_and_honest_bounds"]["leptogenesis_Y_B_2flavor_analytic_fit"],
            "true_N120_vs_N240_max_rel_err": mp.nstr(max_rel_120_240, 10),
            "su3_pow6_v7_scrambling_max_rel_err": mp.nstr(max_scram_rel_err, 10),
            "assumed_uv_continuous_jacobian_svd_rank": uv_jac_rank_12,
            "dimensionful_unit_anchors_13x_scaling": n_anc_computed,
            "c36_scrambling_and_ow22_f1_erratum": c36_rem,
            "control_1_caught": ctrl1_caught,
            "control_2_caught": ctrl2_caught,
        },
        "E2_audit_and_harvest_639a5d46b_and_I37_bridge": {
            "agy_exp_head": AGY_EXP_HEAD,
            "main_head": MAIN_HEAD,
            "peer_manifests_verified": manifests_ok,
            "peer_py_zero_ast_float_count": len(py_scripts),
            "main_I37_unearned_present_in_ledger": main_i37_unearned_present,
            "bourbaki_D5_dims_PS_GG_GSMchi": [dim_ps_b, dim_gg_b, dim_inter_b],
            "u1_chi_16plus_sum_and_cubic_anomaly": [u1_chi_anom_sum, u1_chi_anom_cube],
            "doublet_triplet_projection_Hu_Hd_triplets": [len(h1_surv), len(h2_surv), len(triplets_surv)],
            "chern_root_I8_at_n10_2_n1_269": {k: f"{v.numerator}/{v.denominator}" if v.denominator != 1 else str(v.numerator) for k, v in i8_exact.items()},
            "planted_trF4_at_n10_1_and_3": [f"{i8_n10_1['tr_F4'].numerator}/{i8_n10_1['tr_F4'].denominator}", f"{i8_n10_3['tr_F4'].numerator}/{i8_n10_3['tr_F4'].denominator}"],
            "newton_4mod_t_s_re_im_48dps": [mp.nstr(t_st, 22), mp.nstr(s_st, 22), mp.nstr(rx_st, 22), mp.nstr(ry_st, 22)],
            "newton_4mod_max_diff_vs_ewald_35d": mp.nstr(b3_ewald_diff, 10),
            "newton_4mod_v4_m24_tau_truncation_err": mp.nstr(b3_v4_m24_trunc, 10),
            "gamma2_modular_potential_diff": mp.nstr(v_g2_diff, 10),
            "newton_4mod_grad_norm": mp.nstr(gn_4m, 10),
            "newton_4mod_min_hessian_eig": mp.nstr(evs_4m[0], 12),
            "dkl_min_cusp_wall_4i_i4_1plusi8": mp.nstr(min(f_c_inf, f_c_0, f_c_1), 12),
            "kk_integral_dirichlet_7zeta3_over_8pi2": mp.nstr(kk_dirichlet, 20),
            "control_3_caught": ctrl3_caught,
        },
        "E3_four_catches_and_seesaw_cancellation": {
            "BL1_F1_M_SS_over_A_inv_sqrt": mp.nstr(mss_over_mkk, 14),
            "BL1_F1_M_SS_over_lightest_untwisted_KK": mp.nstr(mss_over_mkk1, 14),
            "BL1_F1_Beff_with_ln2_over_33_span": mp.nstr(beff_bl1, 12),
            "BL1_F1_v4_integrates_nonsusy_2hdm_over_L20": bl1_runs_nonsusy_l20,
            "BL1_F2_1loop_SS_dmH2_over_vEW2_at_MPl_1e16": mp.nstr(dmh2_over_vew2_at_1e16, 12),
            "BL1_F3_total_gauge_rank_Spin10_E6_Spin18": rank_total_bl1,
            "BL1_F3_dlnt_star_over_dlngR2": mp.nstr(dlnt_dlngr2, 12),
            "BL1_F4_b5_invariant_repro_diff": mp.nstr(b5_inv_diff, 10),
            "BL1_F4_gl4_vs_peer_gbs8_L20_err": mp.nstr(gl4_vs_gbs8_b5, 10),
            "BL1_F4_bare_solar_Ue2_and_Vcb": [mp.nstr(bare_ue2, 12), mp.nstr(bare_vcb, 12)],
            "BL1_F4_bare_su3_pow5_x_u3_scrambling_err": mp.nstr(bare_scram_err, 10),
            "seesaw_eps1_cancellation_frob_err": mp.nstr(eps1_cancel_err, 10),
            "lopsided_magnetized_Vcb_Ue2_Umu3": [mp.nstr(lop_vcb, 12), mp.nstr(lop_ue2, 12), mp.nstr(lop_umu3, 12)],
            "lopsided_su3_pow5_x_u3_scrambling_err": mp.nstr(lop_scram_err, 10),
            "lopsided_nontakagi_mR_negative_ctrl_break": mp.nstr(lop_bad_mr_break, 10),
            "scope_unchecked_peer_modules": [
                "639a5d46b fig11 PDF rendering & AutoTeX layout checks",
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
    v7_file_sha = hashlib.sha256(V7_JSON.read_bytes()).hexdigest()
    OUT_SHA.write_text(f"{out_sha}  {OUT_JSON.name}\n{v7_file_sha}  {V7_JSON.name}\n", encoding="utf-8")
    print(
        f"AGY-C37 producer complete in {int(time.time() - t0)}s: 50/50 v7.json + 24 certs + BL1 audit, "
        f"M11/MGUT={v7_payload['gravity_11d_d4_hurwitz_sector']['m11_over_mgut_zero_knob'][:10]}, "
        f"Gam_tau/H={v7_payload['cosmology_crv_and_honest_bounds']['leptogenesis_tau_equil_over_hubble']}, "
        f"ewald_diff={mp.nstr(b3_ewald_diff, 4)}, controls={controls_caught}/5."
    )


if __name__ == "__main__":
    main()
