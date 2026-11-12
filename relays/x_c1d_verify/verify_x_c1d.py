#!/usr/bin/env python3
"""Independent pure-mathematics verification suite for Card X-C1d
(Batch V1, last ten REGISTERED weave rows: 951, 952, 953, 954, 955, 956, 957, 958, 959, 960).

Zero imports from any SM-seat script or dossier, and zero execution of any SM-seat script.
Rebuilt from the prose at the pinned commits: the common point and the moves' lifts (solved as
intertwiners), the bundles from the common point's blocks in W23's three frames, the E_8 roots,
this seat's own Fox calculus on SnapPy's presentation of every thread (polished holonomy), exact
cohomology over the Gaussian rationals at the common point, the triplet's mixing patterns, the
lepton mixing relations, and the hypercharge arithmetic. Reused helpers are this seat's own sealed
X-C1c verifier (and through it the sealed X-C1b verifier); their digests are recorded. 0 of 19.
"""
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import multiprocessing as mpc
import pathlib
import sys
import time
from collections import Counter
from fractions import Fraction

import mpmath as mp
import numpy as np
import snappy
import sympy as sp
from snappy.snap import polished_holonomy

HERE = pathlib.Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
XC_PATH = REPO_ROOT / "relays" / "x_c1c_verify" / "verify_x_c1c.py"


def _load(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


XC = _load(XC_PATH, "agy_exp_x_c1c_helpers")
XB = XC.XB
XC_SHA = hashlib.sha256(XC_PATH.read_bytes()).hexdigest()
RNG = np.random.default_rng(20261113)

Qa, Qb, I2 = XC.Qa, XC.Qb, XC.I2
AUT = XC.AUT
# The automorphisms whose lifts are the prose's explicit lifts (W28 I2: L -> e^{i pi Z/4}, R -> e^{-i pi Y/4}).
AUT_W = {"L": {"a": "a", "b": "ab"}, "R": {"a": "ab", "b": "b"}}


# ---------------------------------------------------------------------------
# 1. Bundles from the common point's blocks and the three conventions (B), (N), (S)
# ---------------------------------------------------------------------------

CHI = {"chi0": (1, 1), "chi1": (-1, 1), "chi2": (1, -1), "chi3": (-1, -1)}


def block_mats(name: str) -> tuple[np.ndarray, np.ndarray]:
    if name in CHI:
        a, b = CHI[name]
        return np.array([[a]], dtype=complex), np.array([[b]], dtype=complex)
    if name == "D":
        return Qa.copy(), Qb.copy()
    if name.startswith("D_"):  # chi_p (x) rho_Q
        a, b = CHI[name[2:]]
        return a * Qa, b * Qb
    raise ValueError(name)


def bundle(blocks: list[str]) -> tuple[np.ndarray, np.ndarray, list[tuple[str, int, int]]]:
    mats = [block_mats(b) for b in blocks]
    n = sum(m[0].shape[0] for m in mats)
    A = np.zeros((n, n), dtype=complex)
    B = np.zeros((n, n), dtype=complex)
    spans = []
    o = 0
    for nm, (a, b) in zip(blocks, mats):
        d = a.shape[0]
        A[o:o + d, o:o + d] = a
        B[o:o + d, o:o + d] = b
        spans.append((nm, o, o + d))
        o += d
    return A, B, spans


def census(rank: int) -> list[list[str]]:
    out = []
    for m0, m1, m2, m3, mD in itertools.product(range(rank + 1), range(rank + 1), range(rank + 1), range(rank + 1), range(rank // 2 + 1)):
        if m0 + m1 + m2 + m3 + 2 * mD != rank:
            continue
        blocks = ["chi0"] * m0 + ["chi1"] * m1 + ["chi2"] * m2 + ["chi3"] * m3 + ["D"] * mD
        A, B, _ = bundle(blocks)
        if abs(np.linalg.det(A) - 1) > 1e-9 or abs(np.linalg.det(B) - 1) > 1e-9:
            continue
        kept = True
        for mv in ("L", "R"):
            Ap, Bp = XC.pair_image(AUT[mv], A, B)
            Z = XC.intertwiner_basis([(A, Ap), (B, Bp)])
            if Z.shape[1] == 0:
                kept = False
                continue
            n = A.shape[0]
            X = sum((RNG.normal() + 1j * RNG.normal()) * Z[:, k].reshape(n, n) for k in range(Z.shape[1]))
            if abs(np.linalg.det(X)) < 1e-9:
                kept = False
        if kept:
            out.append(blocks)
    return out


def bundle_name(blocks: list[str]) -> str:
    c = Counter(blocks)
    parts = []
    if c["D"]:
        parts.append("D" + (f"^{c['D']}" if c["D"] > 1 else ""))
    if c["chi1"]:
        parts.append("P" + (f"^{c['chi1']}" if c["chi1"] > 1 else ""))
    if c["chi0"]:
        parts.append("chi0" + (f"^{c['chi0']}" if c["chi0"] > 1 else ""))
    return "+".join(parts)


def conventions(A: np.ndarray, B: np.ndarray, power: int) -> dict:
    """Index sets under (B), (N), (S) on S = W (power 1) or Lambda^2 W (power 2)."""
    U_L, _ = XC.lift(AUT["L"], A, B)
    U_R, _ = XC.lift(AUT["R"], A, B)
    if power == 2:
        A2, B2, UL, UR = XC.ext_power(A, 2), XC.ext_power(B, 2), XC.ext_power(U_L, 2), XC.ext_power(U_R, 2)
    else:
        A2, B2, UL, UR = A, B, U_L, U_R
    n = A2.shape[0]
    endo = XC.commutant_basis([A2, B2], n)
    cdim, types = XC.decompose(endo + [UL, UR], n)
    hol = A2 @ B2 @ np.linalg.inv(A2) @ np.linalg.inv(B2)
    ev = np.linalg.eigvals(hol)
    r_minus = int(sum(1 for e in ev if abs(e + 1) < 1e-6))
    r_plus = int(sum(1 for e in ev if abs(e - 1) < 1e-6))
    if r_minus % 2 or r_minus + r_plus != n:
        raise RuntimeError("puncture holonomy not +-1")
    Pm = (np.eye(n) - hol) / 2  # projector on the -1 eigenspace (hol is an involution here)
    minus_types, plus_types = [], []
    for t in types:
        Q = t["spaces"][0]
        w = np.linalg.norm(Pm @ Q) ** 2 / Q.shape[1]
        if abs(w - 1) < 1e-6:
            minus_types.append(t)
        elif abs(w) < 1e-6:
            plus_types.append(t)
        else:
            raise RuntimeError("type straddles the puncture eigenspaces")
    h = r_minus // 2
    return {
        "B": [h],
        "N": sorted({-h + d for d in XC.invariant_dims(types)}),
        "S": sorted({-h + d for d in XC.invariant_dims(minus_types)}),
        "r_minus": r_minus,
        "types": types,
        "irreducible_dims_N": XC.irreducible_dims_flat(types),
        "minus_types": minus_types,
    }


def type_content(t: dict, spans: list[tuple[str, int, int]]) -> str:
    Q = t["spaces"][0]
    names = []
    for nm, a, b in spans:
        if np.linalg.norm(Q[a:b, :]) > 1e-6:
            names.append("P" if nm in ("chi1", "chi2", "chi3") else nm)
    return "+".join(sorted(set(names)))


# ---------------------------------------------------------------------------
# 2. Rows 951-954
# ---------------------------------------------------------------------------

def verify_row_951() -> dict:
    """Row 951 (@ 8d659f56b, W32 read-out)."""
    c5 = census(5)
    names = sorted(bundle_name(b) for b in c5)
    exp = {
        "chi0^5": ((0, 0), [0, 5], [0, 10], [0], [0]),
        "P+chi0^2": ((0, 0), [0, 2, 3, 5], [0, 1, 9, 10], [0], [0]),
        "D+chi0^3": ((1, 3), [-1, 1, 2, 4], [-3, 1, 3, 7], [1], [1]),
        "D+P": ((1, 3), [-1, 1, 2, 4], [-3, -2, 0, 1, 3, 4, 6, 7], [1, 4], [1]),
        "D^2+chi0": ((2, 2), [-2, -1, 2, 3], [-2, 1, 2, 4, 5, 8], [-2, 2], [-2, 2]),
    }
    table = {}
    ok = sorted(exp) == names
    for blocks in c5:
        nm = bundle_name(blocks)
        A, B, _ = bundle(blocks)
        c10 = conventions(A, B, 1)
        c5b = conventions(A, B, 2)
        loc10 = sorted({-(c10["r_minus"] // 2) + d for d in (0, c10["r_minus"], A.shape[0] - c10["r_minus"], A.shape[0])})
        loc5 = sorted({-(c5b["r_minus"] // 2) + d for d in (0, c5b["r_minus"], 10 - c5b["r_minus"], 10)})
        row = {"block": [c10["B"][0], c5b["B"][0]], "n10_natural": c10["N"], "n5b_natural": c5b["N"],
               "free_natural": sorted(set(c10["N"]) & set(c5b["N"])), "free_local": sorted(set(loc10) & set(loc5))}
        table[nm] = row
        if nm in exp:
            e = exp[nm]
            ok = ok and tuple(row["block"]) == e[0] and row["n10_natural"] == e[1] and row["n5b_natural"] == e[2] and row["free_natural"] == e[3] and row["free_local"] == e[4]
    never_three = all(3 not in r["free_natural"] and 3 not in r["free_local"] for r in table.values())
    cured = table.get("D+P", {}).get("free_natural") == [1, 4] and [n - 3 for n in table["D+P"]["free_natural"]] == [-2, 1]
    # P6 on D + P: the plane x1 + x2 + x3 = 0 in the parity lines.
    A, B, spans = bundle(["chi1", "chi2", "chi3", "D"])
    Ap, Bp = XC.pair_image(AUT["L"], A, B)
    pull = {}
    for p in ("chi1", "chi2", "chi3"):
        a, b = block_mats(p)
        va = XC.eval_word(AUT["L"]["a"], a, b)[0, 0].real
        vb = XC.eval_word(AUT["L"]["b"], a, b)[0, 0].real
        pull[p] = [q for q, (x, y) in CHI.items() if (x, y) == (round(va), round(vb))][0]
    Perm = np.zeros((5, 5), dtype=complex)
    idx = {"chi1": 0, "chi2": 1, "chi3": 2}
    for p, q in pull.items():
        # U chi_p(x) = chi_q(phi(x)) ... a unit entry sending line q to line p intertwines when chi_p = chi_q o phi
        Perm[idx[p], idx[q]] = 1
    Ud, _ = XC.lift(AUT["L"], Qa, Qb)
    Perm[3:5, 3:5] = Ud
    perm_is_lift = np.allclose(Perm @ A, Ap @ Perm) and np.allclose(Perm @ B, Bp @ Perm)
    plane = np.zeros((5, 2), dtype=complex)
    plane[0, 0], plane[1, 0] = 1, -1
    plane[1, 1], plane[2, 1] = 1, -1
    Pp = plane @ np.linalg.pinv(plane)
    kept_by_perm = np.allclose((np.eye(5) - Pp) @ Perm @ plane, 0)
    Dg = np.diag([1, 2, 3, 1, 1]).astype(complex)
    in_commutant = np.allclose(Dg @ A, A @ Dg) and np.allclose(Dg @ B, B @ Dg)
    kept_by_comm = np.allclose((np.eye(5) - Pp) @ Dg @ plane, 0)
    p6_ok = perm_is_lift and kept_by_perm and in_commutant and (not kept_by_comm)
    ok = ok and never_three and cured and p6_ok
    return {"row": 951, "commits": ["8d659f56b"], "census": names, "table": table, "never_three": never_three,
            "weave_five_cured_at_one_or_four": cured,
            "p6": {"permutation_lift_intertwines": perm_is_lift, "plane_kept_by_permutation_lift": kept_by_perm,
                   "diagonal_in_bulk_commutant": in_commutant, "plane_kept_by_bulk_commutant": kept_by_comm, "ok": p6_ok},
            "readings": "the frame F-HE (a hypothesis) and the reading that three needs W in the 10-sector: not independently checked",
            "result": "the same" if ok else "differs"}


def verify_row_952() -> dict:
    """Row 952 (@ aa642bdc8): the weak centre and the puncture's -1 are one element of E_8."""
    E8 = XC.E8
    th_w = np.array([0, 0, 0, 0, 0, 0, 0.5, -0.5])
    th_6 = np.array([0.5, 0.5, 0.5, -0.5, -0.5, -0.5, 0, 0])
    a4_weak = [r for r in E8 if np.allclose(r, [0, 0, 0, 0, 0, 0, 1, -1]) or np.allclose(r, [0, 0, 0, 0, 0, 0, -1, 1])]
    a5 = [r for r in E8 if np.allclose(r[6:], 0) and sorted(r[:6].tolist()) == [-1.0, 0, 0, 0, 0, 1.0]]
    orth = [r for r in E8 if all(abs(r @ s) < 1e-12 for s in a5)]
    weak_in_orth = len(a4_weak) == 2 and all(any(np.allclose(r, s) for s in orth) for r in a4_weak)
    same_element = bool(np.allclose(np.exp(2j * np.pi * (E8 @ (th_w - th_6))), 1))
    chi = 8 + np.sum(np.exp(2j * np.pi * (E8 @ th_6)))
    chi_int = XC.as_int(chi)
    g6 = -np.eye(6, dtype=complex)
    chi_branch = XC.as_int(XC.chi248_su6_branch(g6))
    centraliser = (248 + chi_int) // 2 if chi_int is not None else None
    # which pieces carry -1: SU(6) reps 6, 15, 20, 35 and SU(2) reps 2, 3
    su6_sign = {"6": -1, "15": 1, "20": -1, "35": 1, "1": 1}
    su2_sign = {"1": 1, "2": -1, "3": 1}
    pieces = [("8", "1", "1", 8), ("1", "3", "1", 3), ("1", "1", "35", 35), ("3", "2", "6", 36), ("3b", "2", "6", 36), ("3b", "1", "15", 45), ("3", "1", "15", 45), ("1", "2", "20", 40)]
    pattern_equal = all(su6_sign[p6] == su2_sign[p2] for _, p2, p6, _ in pieces)
    minus_dim = sum(d for _, p2, _, d in pieces if su2_sign[p2] == -1)
    ok = weak_in_orth and len(orth) == 8 and same_element and chi_int == 24 and chi_branch == 24 and centraliser == 136 and pattern_equal and minus_dim == 112
    return {"row": 952, "commits": ["aa642bdc8"], "weak_A1_orthogonal_to_SU6": weak_in_orth, "orthogonal_roots": len(orth),
            "same_element_of_E8": same_element, "chi248_roots": chi_int, "chi248_branch": chi_branch, "centraliser_dim": centraliser,
            "minus_one_pieces_agree": pattern_equal, "minus_one_dimension": minus_dim,
            "readings": "the contemplation's points 1-5 and the riddle: readings (not independently checked)",
            "result": "the same" if ok else "differs"}


EXP_T2 = {
    3: {"P": ([0], [0, 3], [0]), "chi0^3": ([0], [0, 3], [0]), "D+chi0": ([1], [-1, 0, 1, 2], [-1, 1])},
    4: {"P+chi0": ([0], [0, 1, 3, 4], [0]), "chi0^4": ([0], [0, 4], [0]), "D+chi0^2": ([1], [-1, 1, 3], [-1, 1]), "D^2": ([2], [-2, 2], [-2, 2])},
}
EXP_SU5 = {
    "N": {"chi0^5": [0], "P+chi0^2": [0], "D+chi0^3": [1], "D+P": [1, 4], "D^2+chi0": [-2, 2]},
    "S": {"chi0^5": [0], "P+chi0^2": [0], "D+chi0^3": [], "D+P": [], "D^2+chi0": [-2, 2]},
}


def verify_rows_953_954() -> tuple[dict, dict]:
    """Rows 953 (@ bc4ea1303, W33) and 954 (@ 35d16dff2, W33 rule)."""
    frames = {}
    t2_ok = True
    t4_ok = True
    sources = {}
    zero_free = {}
    has_three = {"B": set(), "N": set(), "S": set()}
    for rank in (3, 4):
        cs = census(rank)
        frames[rank] = {}
        for blocks in cs:
            nm = bundle_name(blocks)
            A, B, spans = bundle(blocks)
            c = conventions(A, B, 1)
            frames[rank][nm] = {"B": c["B"], "N": c["N"], "S": c["S"]}
            e = EXP_T2[rank].get(nm)
            if e is None or (c["B"], c["N"], c["S"]) != e:
                t2_ok = False
            m = c["r_minus"] // 2
            if c["S"] != (sorted({-m, m}) if m else [0]):
                t4_ok = False
            key = f"rank{rank}:{nm}"
            zero_free[key] = not any(b in ("chi0", "D") for b in blocks)
            for conv in ("B", "N", "S"):
                if 3 in c[conv]:
                    has_three[conv].add(key)
            if 3 in c["N"]:
                h = c["r_minus"] // 2
                found = None
                for r in range(1, len(c["types"]) + 1):
                    for combo in itertools.combinations(range(len(c["types"])), r):
                        if -h + sum(c["types"][i]["d"] for i in combo) == 3:
                            found = sorted(type_content(c["types"][i], spans) + f"(dim {c['types'][i]['d']})" for i in combo)
                            break
                    if found:
                        break
                sources[key] = found
        if sorted(frames[rank]) != sorted(EXP_T2[rank]):
            t2_ok = False
    su5 = {}
    su5_ok = True
    for blocks in census(5):
        nm = bundle_name(blocks)
        A, B, _ = bundle(blocks)
        cw, c2 = conventions(A, B, 1), conventions(A, B, 2)
        for conv in ("B", "N", "S"):
            su5.setdefault(conv, {})[nm] = sorted(set(cw[conv]) & set(c2[conv]))
        for cc in (cw, c2):
            m = cc["r_minus"] // 2
            if cc["S"] != (sorted({-m, m}) if m else [0]):
                t4_ok = False
        key = f"rank5:{nm}"
        zero_free[key] = not any(b in ("chi0", "D") for b in blocks)
        for conv in ("B", "N", "S"):
            if 3 in su5[conv][nm]:
                has_three[conv].add(key)
    for conv in ("N", "S"):
        if su5.get(conv) != EXP_SU5[conv]:
            su5_ok = False
    naive_law = {conv: has_three[conv] == {k for k, v in zero_free.items() if v} for conv in ("B", "N", "S")}
    t3_ok = not any(naive_law.values())
    # T5: W = +_p chi_p (x) rho_Q and W + D.
    Aw, Bw, _ = bundle(["D_chi1", "D_chi2", "D_chi3"])
    cw = conventions(Aw, Bw, 1)
    Awd, Bwd, _ = bundle(["D_chi1", "D_chi2", "D_chi3", "D"])
    cwd = conventions(Awd, Bwd, 1)
    t5_ok = cw["N"] == [-3, 3] and cw["S"] == [-3, 3] and cwd["N"] == [-4, 4] and cwd["S"] == [-4, 4] and cwd["irreducible_dims_N"] == [8]
    exp_sources = {
        "rank3:P": ["P(dim 3)"],
        "rank3:chi0^3": ["chi0(dim 3)"],
        "rank4:P+chi0": ["P(dim 3)"],
        "rank4:D+chi0^2": ["D(dim 2)", "chi0(dim 2)"],
    }
    t6_ok = sources == exp_sources
    ok953 = t2_ok and su5_ok and t3_ok and t4_ok and t5_ok and t6_ok
    r953 = {"row": 953, "commits": ["bc4ea1303"], "frames": {str(k): v for k, v in frames.items()}, "su5_anomaly_free": su5,
            "t2_as_read_out": t2_ok, "su5_as_read_out": su5_ok, "naive_law_holds": naive_law, "t3_naive_law_fails_everywhere": t3_ok,
            "t4_spinor_rule_counts_doublets": t4_ok,
            "t5": {"W_N": cw["N"], "W_S": cw["S"], "W_plus_D_N": cwd["N"], "W_plus_D_S": cwd["S"], "W_plus_D_pieces": cwd["irreducible_dims_N"], "ok": t5_ok},
            "t6_sources": sources, "t6_ok": t6_ok,
            "readings": "the withdrawal of point 2 and the frames as hypotheses: readings (not independently checked)",
            "result": "the same" if ok953 else "differs"}
    # Row 954: the rule's hand tables against the computed ones; the rule's census T1.
    t1 = {3: sorted(EXP_T2[3]), 4: sorted(EXP_T2[4])}
    t1_ok = all(sorted(frames[r]) == t1[r] for r in (3, 4))
    vacuous_one_direction = (len(has_three["B"]) == 0 and len(has_three["S"]) == 0 and zero_free.get("rank3:P", False))
    ok954 = t1_ok and t2_ok and su5_ok and t3_ok and t4_ok and t5_ok and t6_ok and vacuous_one_direction
    r954 = {"row": 954, "commits": ["35d16dff2"], "t1_census_as_ruled": t1_ok, "tables_as_ruled": t2_ok and su5_ok,
            "no_three_under_B_and_S_while_E6_P_is_zero_free": vacuous_one_direction,
            "note": "the rule's word 'vacuous' holds in one direction only, as the read-out itself disclosed",
            "result": "the same" if ok954 else "differs"}
    return r953, r954


# ---------------------------------------------------------------------------
# 3. Rows 955, 956: Q1 (threads), Q2 (common point), Q3 (names), Q5 (register)
# ---------------------------------------------------------------------------

def _mpc(x) -> mp.mpc:
    return mp.mpc(mp.mpf(str(x.real())), mp.mpf(str(x.imag())))


def _sym_mp(M: mp.matrix, n: int) -> mp.matrix:
    def ppow(c0, c1, e):
        r = [mp.mpc(1)]
        for _ in range(e):
            nr = [mp.mpc(0)] * (len(r) + 1)
            for i, v in enumerate(r):
                nr[i] += v * c0
                nr[i + 1] += v * c1
            r = nr
        return r

    out = mp.matrix(n + 1, n + 1)
    for k in range(n + 1):
        p1 = ppow(M[0, 0], M[1, 0], n - k)
        p2 = ppow(M[0, 1], M[1, 1], k)
        for i, u in enumerate(p1):
            for j, v in enumerate(p2):
                out[i + j, k] += u * v
    return out


def _classify(M: mp.matrix, zero_thr, nonzero_thr):
    rows, cols = M.rows, M.cols
    n = max(rows, cols)
    P = mp.matrix(n, cols)
    for i in range(rows):
        for j in range(cols):
            P[i, j] = M[i, j]
    U, S, V = mp.svd_c(P)
    s = [S[i] for i in range(min(n, cols))]
    smax = max(s) if s else mp.mpf(0)
    rank = 0
    undecided = 0
    zero_idx = []
    min_nz, max_z = None, None
    for i, v in enumerate(s):
        rel = v / smax if smax > 0 else mp.mpf(0)
        if rel > nonzero_thr:
            rank += 1
            min_nz = rel if (min_nz is None or rel < min_nz) else min_nz
        elif rel < zero_thr:
            zero_idx.append(i)
            max_z = rel if (max_z is None or rel > max_z) else max_z
        else:
            undecided += 1
    null = mp.matrix(cols, len(zero_idx)) if zero_idx else None
    if zero_idx:
        for c, i in enumerate(zero_idx):
            for j in range(cols):
                null[j, c] = mp.conj(V[i, j])
    return rank, undecided, null, min_nz, max_z


def _fox(mats: dict, gens: list[str], w: str, d: int):
    idx = {g: k for k, g in enumerate(gens)}
    out = mp.matrix(d, d * len(gens))
    pre = mp.eye(d)
    for ch in w:
        if ch in idx:
            o = idx[ch] * d
            for i in range(d):
                for j in range(d):
                    out[i, o + j] += pre[i, j]
            pre = pre * mats[ch]
        else:
            g = ch.lower()
            o = idx[g] * d
            pre = pre * mats[ch]
            for i in range(d):
                for j in range(d):
                    out[i, o + j] -= pre[i, j]
    return out, pre


def _vstack(ms):
    rows = sum(m.rows for m in ms)
    out = mp.matrix(rows, ms[0].cols)
    r = 0
    for m in ms:
        for i in range(m.rows):
            for j in range(m.cols):
                out[r + i, j] = m[i, j]
        r += m.rows
    return out


def _hstack(ms):
    cols = sum(m.cols for m in ms)
    out = mp.matrix(ms[0].rows, cols)
    c = 0
    for m in ms:
        for i in range(m.rows):
            for j in range(m.cols):
                out[i, c + j] = m[i, j]
        c += m.cols
    return out


def q1_state(task):
    sign, word, bits, dps, zthr, nzthr = task
    mp.mp.dps = dps
    zthr, nzthr = mp.mpf(zthr), mp.mpf(nzthr)
    M = snappy.Manifold(("b++" if sign == "+" else "b+-") + word)
    G = polished_holonomy(M, bits_prec=bits, lift_to_SL2=False)
    gens = list(G.generators())
    rels = list(G.relators())
    mer, lon = G.peripheral_curves()[0]
    base = {}
    for g in gens:
        m = G(g)
        A = mp.matrix([[_mpc(m[0, 0]), _mpc(m[0, 1])], [_mpc(m[1, 0]), _mpc(m[1, 1])]])
        det = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
        Ai = mp.matrix([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]]) / det
        base[g], base[g.upper()] = A, Ai
    out = {}
    for k in (1, 2, 3):
        d = 2 * k + 1
        mats = {g: _sym_mp(base[g], 2 * k) for g in base}
        J = _vstack([_fox(mats, gens, r, d)[0] for r in rels])
        rJ, uJ, Z, mnJ, mzJ = _classify(J, zthr, nzthr)
        dimZ = d * len(gens) - rJ - uJ
        Bm = _vstack([mats[g] - mp.eye(d) for g in gens])
        r0, u0, _, mn0, _ = _classify(Bm, zthr, nzthr)
        h1 = dimZ - r0
        Fm, Wm = _fox(mats, gens, mer, d)
        Fl, Wl = _fox(mats, gens, lon, d)
        BP = _vstack([Wm - mp.eye(d), Wl - mp.eye(d)])
        rBP, uBP, _, mnBP, _ = _classify(BP, zthr, nzthr)
        if Z is not None:
            RZ = _vstack([Fm, Fl]) * Z
            rboth, uboth, _, mnb, _ = _classify(_hstack([BP, RZ]), zthr, nzthr)
        else:
            rboth, uboth, mnb = rBP, 0, None
        r1 = rboth - rBP
        und = uJ + u0 + uBP + uboth
        mins = [x for x in (mnJ, mn0, mnBP, mnb) if x is not None]
        out[k] = {"h1": int(h1), "r1": int(r1), "private": int(h1 - r1), "undecided": int(und),
                  "log10_min_genuine": float(mp.log10(min(mins))) if mins else None,
                  "log10_max_zero": float(mp.log10(mzJ)) if (mzJ is not None and mzJ > 0) else None}
    return sign + word, len(word), out


def run_q1(states: list[tuple[str, str]]) -> dict:
    res = {}
    for label, bits, dps, z, nz in (("sixty_digits", 212, 64, "1e-40", "1e-25"), ("one_twenty_digits", 420, 126, "1e-80", "1e-60")):
        tasks = [(s, w, bits, dps, z, nz) for s, w in states]
        try:
            with mpc.get_context("fork").Pool(8) as pool:
                outs = pool.map(q1_state, tasks, chunksize=4)
        except Exception:
            outs = [q1_state(t) for t in tasks]
        res[label] = {lab: (ln, o) for lab, ln, o in outs}
    return res


# --- exact cohomology at the common point over Q(i) ---

def sp_sym(M: sp.Matrix, n: int) -> sp.Matrix:
    y = sp.Symbol("y")
    out = sp.zeros(n + 1, n + 1)
    for k in range(n + 1):
        poly = sp.Poly(sp.expand((M[0, 0] + M[1, 0] * y) ** (n - k) * (M[0, 1] + M[1, 1] * y) ** k), y)
        for i in range(n + 1):
            out[i, k] = poly.coeff_monomial(y ** i)
    return out


SQa = sp.Matrix([[sp.I, 0], [0, -sp.I]])
SQb = sp.Matrix([[0, 1], [-1, 0]])


def sp_word(w: str, A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    rep = {"a": A, "b": B, "A": A.inv(), "B": B.inv()}
    M = sp.eye(A.shape[0])
    for ch in w:
        M = M * rep[ch]
    return sp.simplify(M)


def sp_lift(phi: dict, A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    n = A.shape[0]
    Ap, Bp = sp_word(phi["a"], A, B), sp_word(phi["b"], A, B)
    us = sp.symbols(f"u0:{n * n}")
    U = sp.Matrix(n, n, us)
    eqs = list(U * A - Ap * U) + list(U * B - Bp * U)
    sol = sp.linsolve(eqs, us)
    (vec,) = list(sol)
    free = sorted(set().union(*[sp.sympify(v).free_symbols for v in vec]), key=str)
    subs = {f: (1 if i == 0 else 0) for i, f in enumerate(free)}
    Uv = sp.Matrix(n, n, [sp.sympify(v).subs(subs) for v in vec])
    if Uv.det() == 0:
        raise RuntimeError("singular exact lift")
    return Uv


def sp_fox(mats: dict, w: str, d: int) -> tuple[sp.Matrix, sp.Matrix]:
    idx = {"a": 0, "b": 1}
    out = sp.zeros(d, 2 * d)
    pre = sp.eye(d)
    for ch in w:
        if ch in idx:
            o = idx[ch] * d
            out[:, o:o + d] = out[:, o:o + d] + pre
            pre = pre * mats[ch]
        else:
            o = idx[ch.lower()] * d
            pre = pre * mats[ch]
            out[:, o:o + d] = out[:, o:o + d] - pre
    return sp.expand(out), pre


def sp_action(phi: dict, mats: dict, g: sp.Matrix, d: int) -> sp.Matrix:
    gi = g.inv()
    Fa, _ = sp_fox(mats, phi["a"], d)
    Fb, _ = sp_fox(mats, phi["b"], d)
    return sp.simplify(sp.Matrix.vstack(gi * Fa, gi * Fb))


def common_point_block(Asys: sp.Matrix, Bsys: sp.Matrix, lifts: dict[str, sp.Matrix] | None) -> dict:
    d = Asys.shape[0]
    mats = {"a": Asys, "b": Bsys, "A": Asys.inv(), "B": Bsys.inv()}
    Bm = sp.Matrix.vstack(Asys - sp.eye(d), Bsys - sp.eye(d))
    rB = Bm.rank()
    h1 = 2 * d - rB
    Fc, Wc = sp_fox(mats, "abAB", d)
    Kc_rows = (Wc - sp.eye(d)).T.nullspace()
    Kc = sp.Matrix.hstack(*Kc_rows).T if Kc_rows else sp.zeros(0, d)
    visible = (Kc * Fc).rank() if Kc.shape[0] else 0
    out = {"dim": d, "h1": int(h1), "visible": int(visible), "private": int(h1 - visible)}
    if lifts is None:
        return out
    Krows = Bm.T.nullspace()
    K = sp.Matrix.hstack(*Krows).T
    acts = {nm: sp_action(AUT[nm], mats, g, d) for nm, g in lifts.items()}

    def fixed(names, private_only):
        stack = [K * (acts[nm] - sp.eye(2 * d)) for nm in names]
        if private_only and Kc.shape[0]:
            stack.append(Kc * Fc)
        M = sp.Matrix.vstack(*stack)
        return int(2 * d - M.rank() - rB)

    out["single_moves_h1_private"] = {nm: [fixed([nm], False), fixed([nm], True)] for nm in lifts}
    out["joint_LR"] = [fixed(["L", "R"], False), fixed(["L", "R"], True)]
    out["joint_all"] = [fixed(list(lifts), False), fixed(list(lifts), True)]
    return out


def q8_multiplicities(k: int) -> list[int]:
    q8 = XC.closure([Qa, Qb])
    chars = {"chi0": (0, 0), "chi1": (1, 0), "chi2": (0, 1), "chi3": (1, 1)}
    out = []
    for nm, (pa, pb) in chars.items():
        tot = 0
        for g in q8:
            ea = eb = None
            for xa, xb in itertools.product((0, 1), repeat=2):
                base = np.linalg.matrix_power(Qa, xa) @ np.linalg.matrix_power(Qb, xb)
                if np.allclose(g, base) or np.allclose(g, -base):
                    ea, eb = xa, xb
            tot += ((-1) ** (pa * ea + pb * eb)) * np.trace(XC.sym_power(g, 2 * k))
        out.append(XC.as_int(tot / 8))
    return out


def _primes_1mod4(lo: int, count: int) -> list[int]:
    out, q = [], lo
    while len(out) < count:
        q = int(sp.nextprime(q))
        if q % 4 == 1:
            out.append(q)
    return out


def _sqrt_m1(p: int) -> int:
    for g in range(2, p):
        r = pow(g, (p - 1) // 4, p)
        if (r * r) % p == p - 1:
            return r
    raise RuntimeError("no square root of -1")


def _gi_mod(z: sp.Expr, p: int, r: int) -> int:
    re, im = sp.nsimplify(z).as_real_imag()
    def q(x):
        x = sp.Rational(x)
        return (int(x.p) * pow(int(x.q), p - 2, p)) % p
    return (q(re) + r * q(im)) % p


def _mat_mod(M: sp.Matrix, p: int, r: int) -> np.ndarray:
    return np.array([[_gi_mod(M[i, j], p, r) for j in range(M.shape[1])] for i in range(M.shape[0])], dtype=np.int64)


def _sym_mod(U: np.ndarray, n: int, p: int) -> np.ndarray:
    def ppow(c0, c1, e):
        rr = [1]
        for _ in range(e):
            nr = [0] * (len(rr) + 1)
            for i, v in enumerate(rr):
                nr[i] = (nr[i] + v * c0) % p
                nr[i + 1] = (nr[i + 1] + v * c1) % p
            rr = nr
        return rr
    out = np.zeros((n + 1, n + 1), dtype=np.int64)
    for k in range(n + 1):
        p1 = ppow(int(U[0, 0]), int(U[1, 0]), n - k)
        p2 = ppow(int(U[0, 1]), int(U[1, 1]), k)
        for i, u in enumerate(p1):
            for j, v in enumerate(p2):
                out[i + j, k] = (out[i + j, k] + u * v) % p
    return out


def _word_mod(w: str, mats: dict, p: int, d: int) -> np.ndarray:
    M = np.eye(d, dtype=np.int64)
    for ch in w:
        M = (M @ mats[ch]) % p
    return M


def _fox_mod(w: str, mats: dict, p: int, d: int) -> np.ndarray:
    out = np.zeros((d, 2 * d), dtype=np.int64)
    pre = np.eye(d, dtype=np.int64)
    for ch in w:
        if ch in "ab":
            o = 0 if ch == "a" else d
            out[:, o:o + d] = (out[:, o:o + d] + pre) % p
            pre = (pre @ mats[ch]) % p
        else:
            o = 0 if ch == "A" else d
            pre = (pre @ mats[ch]) % p
            out[:, o:o + d] = (out[:, o:o + d] - pre) % p
    return out


def thread_kept(states: list[tuple[str, str, tuple]]) -> dict:
    """Kept dimensions of each thread's action on H^1(F_2; Sym^2k rho_Q), k = 1, 2, 3, and on the private states,
    computed exactly over Z[i] reduced modulo two primes p == 1 mod 4 (i -> a square root of -1); the two primes must agree."""
    primes = _primes_1mod4(1000000, 2)
    per_prime = []
    for p in primes:
        r = _sqrt_m1(p)
        base2 = {"a": _mat_mod(SQa, p, r), "b": _mat_mod(SQb, p, r), "A": _mat_mod(SQa.inv(), p, r), "B": _mat_mod(SQb.inv(), p, r)}
        blocks = {}
        for k in (1, 2, 3):
            d = 2 * k + 1
            mk = {nm: _mat_mod(sp_sym(M, 2 * k), p, r) for nm, M in (("a", SQa), ("b", SQb), ("A", SQa.inv()), ("B", SQb.inv()))}
            Bm = np.vstack([(mk["a"] - np.eye(d, dtype=np.int64)) % p, (mk["b"] - np.eye(d, dtype=np.int64)) % p])
            rB = XB.np_rank_gf(Bm, p)
            _, Kt = XB.np_null_gf(Bm.T % p, p)
            K = Kt.T % p
            Fc = _fox_mod("abAB", mk, p, d)
            blocks[k] = (d, mk, rB, K, Fc)
        results = {}
        for sgn, w, Mh in states:
            phi = XB.phi1_words(sgn, w)
            Ia, Ib = _word_mod(phi["a"], base2, p, 2), _word_mod(phi["b"], base2, p, 2)
            I2m = np.eye(2, dtype=np.int64)
            sys_rows = np.vstack([(np.kron(I2m, base2["a"].T) - np.kron(Ia, I2m)) % p, (np.kron(I2m, base2["b"].T) - np.kron(Ib, I2m)) % p])
            _, Zl = XB.np_null_gf(sys_rows, p)
            if Zl.shape[1] != 1:
                raise RuntimeError("lift not unique mod p")
            U2 = Zl[:, 0].reshape(2, 2) % p
            detU = int((U2[0, 0] * U2[1, 1] - U2[0, 1] * U2[1, 0]) % p)
            triple, priv_kept = [], 0
            for k in (1, 2, 3):
                d, mk, rB, K, Fc = blocks[k]
                Ug = (_sym_mod(U2, 2 * k, p) * pow(pow(detU, k, p), p - 2, p)) % p
                Ugi = XB.np_inv_gf(Ug, p)
                T = np.vstack([(Ugi @ _fox_mod(phi["a"], mk, p, d)) % p, (Ugi @ _fox_mod(phi["b"], mk, p, d)) % p])
                KT = (K @ ((T - np.eye(2 * d, dtype=np.int64)) % p)) % p
                fixed = 2 * d - XB.np_rank_gf(KT, p) - rB
                fixed_priv = 2 * d - XB.np_rank_gf(np.vstack([Fc, KT]) % p, p) - rB
                triple.append(int(fixed))
                priv_kept += int(fixed_priv)
            results[sgn + w] = (tuple(triple), priv_kept, (Mh[0][0] + Mh[1][1]) % 2)
        per_prime.append(results)
    agree = per_prime[0] == per_prime[1]
    hist_odd, hist_even = Counter(), Counter()
    private_kept_any = 0
    for lab, (tr, pk, par) in per_prime[0].items():
        (hist_odd if par else hist_even)[tr] += 1
        if pk:
            private_kept_any += 1
    return {"primes": primes, "primes_agree": agree, "odd": {str(k): v for k, v in hist_odd.items()}, "even": {str(k): v for k, v in hist_even.items()},
            "threads_keeping_a_private_state": private_kept_any}


def reduce_shape(tau: mp.mpc) -> mp.mpc:
    if mp.im(tau) < 0:
        tau = mp.conj(tau)
    for _ in range(10000):
        tau = tau - mp.nint(mp.re(tau))
        if abs(tau) < 1 - mp.mpf(10) ** (-40):
            tau = -1 / tau
        else:
            break
    re = abs(mp.re(tau))
    if re < mp.mpf(10) ** (-40):
        re = mp.mpf(0)
    return mp.mpc(re, mp.im(tau))


def q3_names(states: list[tuple[str, str]]) -> dict:
    mp.mp.dps = 60
    names = {}
    vols = {}
    for sgn, w in states:
        H = snappy.ManifoldHP(("b++" if sgn == "+" else "b+-") + w)
        v = mp.mpf(str(H.volume()))
        s = H.cusp_info("shape")[0]
        tau = reduce_shape(mp.mpc(mp.mpf(str(s.real())), mp.mpf(str(s.imag()))))
        names[sgn + w] = (mp.nstr(v, 30), mp.nstr(mp.re(tau), 30), mp.nstr(mp.im(tau), 30))
        vols[sgn + w] = mp.nstr(v, 30)
    by_name: dict[tuple, list[str]] = {}
    for lab, nm in names.items():
        by_name.setdefault(nm, []).append(lab)
    coincid = [sorted(v) for v in by_name.values() if len(v) > 1]
    rev_pairs = set()
    labels = set(names)
    for lab in labels:
        sgn, w = lab[0], lab[1:]
        rw = XB.canon_word(w[::-1])
        if rw != w and sgn + rw in labels:
            rev_pairs.add(tuple(sorted((lab, sgn + rw))))
    coincid_set = {tuple(c) for c in coincid}
    iso_ok = True
    iso_undecided = 0
    for a, b in sorted(rev_pairs):
        Ma = snappy.Manifold(("b++" if a[0] == "+" else "b+-") + a[1:])
        Mb = snappy.Manifold(("b++" if b[0] == "+" else "b+-") + b[1:])
        try:
            if not Ma.is_isometric_to(Mb):
                iso_ok = False
        except Exception:
            iso_undecided += 1
            iso_ok = False
    pm_pairs = sorted({w[1:] for w in labels})
    pm_vol = all(vols["+" + w] == vols["-" + w] for w in pm_pairs)
    pm_sep = all(names["+" + w] != names["-" + w] for w in pm_pairs)
    m004 = reduce_shape(mp.mpc(mp.mpf(str(snappy.ManifoldHP("b++LR").cusp_info("shape")[0].real())), mp.mpf(str(snappy.ManifoldHP("b++LR").cusp_info("shape")[0].imag()))))
    m003 = reduce_shape(mp.mpc(mp.mpf(str(snappy.ManifoldHP("b+-LR").cusp_info("shape")[0].real())), mp.mpf(str(snappy.ManifoldHP("b+-LR").cusp_info("shape")[0].imag()))))
    m004_ok = abs(m004 - mp.mpc(0, 2 * mp.sqrt(3))) < mp.mpf(10) ** (-40)
    m003_ok = abs(m003 - mp.mpc(mp.mpf(1) / 2, mp.sqrt(3) / 2)) < mp.mpf(10) ** (-40)
    ids = {"b++LR": [str(x) for x in snappy.Manifold("b++LR").identify()], "b+-LR": [str(x) for x in snappy.Manifold("b+-LR").identify()]}
    census_ok = any("m004" in x for x in ids["b++LR"]) and any("m003" in x for x in ids["b+-LR"]) and (not snappy.Manifold("b-+LR").is_orientable())
    return {"states": len(names), "names": len(by_name), "coincidences": len(coincid), "max_coincidence_size": max((len(c) for c in coincid), default=0),
            "reversal_pairs": len(rev_pairs), "coincidences_equal_reversal_pairs": coincid_set == rev_pairs,
            "reversal_pairs_isometric": iso_ok, "isometry_undecided": iso_undecided, "pm_pairs": len(pm_pairs), "pm_same_volume": pm_vol, "pm_separated_by_name": pm_sep,
            "m004_shape_2sqrt3_i": bool(m004_ok), "m003_shape_hexagonal": bool(m003_ok), "identify": ids, "census_identifications_ok": census_ok}


def q5_register() -> dict:
    sigma = {"a": "ab", "b": "a"}
    C_sigma = {"a": "b", "b": "ba"}
    rev = {"a": "ba", "b": "a"}
    C_rev = {"a": "b", "b": "ab"}
    iota_ainv = {"a": "a", "b": "Aba"}
    iota_binv = {"a": "Bab", "b": "b"}
    id1 = XC.compose(iota_ainv, sigma) == rev
    id2 = XC.compose(iota_binv, C_sigma) == C_rev
    id3 = XC.compose(AUT["P"], XC.compose(sigma, AUT["P"])) == C_sigma
    sigP = XC.compose(sigma, AUT["P"])
    transvection = sigP == {"a": "a", "b": "ab"}
    dets = {nm: (lambda m: m[0][0] * m[1][1] - m[0][1] * m[1][0])(XB.hom_mat(f)) for nm, f in (("sigma", sigma), ("C_sigma", C_sigma), ("rev", rev), ("C_rev", C_rev))}

    def cyc(f):
        m = XB.hom_mat(f)
        img = {}
        for v in ((1, 0), (0, 1), (1, 1)):
            img[v] = ((m[0][0] * v[0] + m[0][1] * v[1]) % 2, (m[1][0] * v[0] + m[1][1] * v[1]) % 2)
        return img

    lifts = {nm: XC.lift(f, Qa, Qb)[0] for nm, f in (("sigma", sigma), ("C_sigma", C_sigma), ("rev", rev), ("C_rev", C_rev))}
    q8 = XC.closure([Qa, Qb])

    def same_class(U, V):
        X = U @ np.linalg.inv(V)
        return any(XC.proj_eq(X, q) for q in q8)

    differ_by_a_inv = XC.proj_eq(lifts["rev"], np.linalg.inv(Qa) @ lifts["sigma"])
    actions_equal = {}
    actions_C_differ = {}
    for k in (1, 2, 3):
        A, B = XC.sym_power(Qa, 2 * k), XC.sym_power(Qb, 2 * k)
        T = {nm: XC.h1_action(f, A, B, XC.sym_power(lifts[nm], 2 * k)) for nm, f in (("sigma", sigma), ("C_sigma", C_sigma), ("rev", rev), ("C_rev", C_rev))}
        actions_equal[k] = bool(np.allclose(T["sigma"], T["rev"], atol=1e-9) and np.allclose(T["C_sigma"], T["C_rev"], atol=1e-9))
        actions_C_differ[k] = bool(not np.allclose(T["sigma"], T["C_sigma"], atol=1e-6))
    ok = (id1 and id2 and id3 and transvection and all(v == -1 for v in dets.values()) and cyc(sigma) == cyc(rev) and cyc(C_sigma) == cyc(C_rev)
          and cyc(sigma) != cyc(C_sigma) and same_class(lifts["sigma"], lifts["rev"]) and same_class(lifts["C_sigma"], lifts["C_rev"])
          and (not same_class(lifts["sigma"], lifts["C_sigma"])) and differ_by_a_inv and all(actions_equal.values()) and all(actions_C_differ.values()))
    return {"rev_is_inner_times_sigma": id1, "C_rev_is_inner_times_C_sigma": id2, "C_sigma_is_P_sigma_P": id3, "sigma_P_is_a_transvection": transvection,
            "determinants": dets, "same_cyclic_order_sigma_rev": cyc(sigma) == cyc(rev), "C_flips_cyclic_order": cyc(sigma) != cyc(C_sigma),
            "lift_class_mod_Q8_same_for_rev": same_class(lifts["sigma"], lifts["rev"]), "lift_class_flipped_by_C": not same_class(lifts["sigma"], lifts["C_sigma"]),
            "lifts_differ_by_rho_a_inverse": differ_by_a_inv, "h1_actions_equal_sigma_rev": actions_equal, "h1_actions_differ_under_C": actions_C_differ, "ok": ok}


def verify_rows_955_956() -> tuple[dict, dict]:
    states758 = XB.genesis_states(12, odd_only=False)
    st = [(s, w) for s, w, _ in states758]
    # Q2 at the common point, exact.
    lifts2 = {nm: sp_lift(AUT[nm], SQa, SQb) for nm in ("L", "R", "P", "N")}
    q2 = {}
    for k in (1, 2, 3):
        A, B = sp_sym(SQa, 2 * k), sp_sym(SQb, 2 * k)
        lk = {nm: sp_sym(g, 2 * k) / (g.det() ** k) for nm, g in lifts2.items()}
        q2[k] = common_point_block(A, B, lk)
        q2[k]["q8_multiplicities"] = q8_multiplicities(k)
    exp_tab = {1: (3, 3, 0, [0, 1, 1, 1]), 2: (7, 3, 4, [2, 1, 1, 1]), 3: (8, 6, 2, [1, 2, 2, 2])}
    tab_ok = all((q2[k]["h1"], q2[k]["visible"], q2[k]["private"], q2[k]["q8_multiplicities"]) == exp_tab[k] for k in (1, 2, 3))
    fiber = [0, sum(q2[k]["private"] for k in (1,)), sum(q2[k]["private"] for k in (1, 2)), sum(q2[k]["private"] for k in (1, 2, 3))]
    joint_ok = all(q2[k]["joint_LR"] == [0, 0] and q2[k]["joint_all"] == [0, 0] for k in (1, 2, 3))
    exp_single = {"L": [[1, 0], [1, 1], [1, 0]], "R": [[1, 0], [1, 1], [1, 0]], "P": [[2, 0], [3, 2], [4, 1]], "N": [[3, 0], [3, 0], [6, 0]]}
    single_ok = all([q2[k]["single_moves_h1_private"][nm] for k in (1, 2, 3)] == exp_single[nm] for nm in exp_single)
    threads = thread_kept(states758)
    threads_ok = threads["primes_agree"] and (threads["odd"] == {str((1, 1, 2)): 326} and threads["even"] == {str((1, 0, 1)): 136, str((1, 1, 2)): 124, str((1, 2, 3)): 132, str((3, 3, 6)): 40}
                  and threads["threads_keeping_a_private_state"] == 0)
    q2_ok = tab_ok and fiber[1:] == [0, 4, 6] and joint_ok and single_ok and threads_ok
    # Q3 and Q5.
    q3 = q3_names(st)
    q3_ok = (q3["states"] == 758 and q3["names"] == 536 and q3["coincidences"] == 222 and q3["max_coincidence_size"] == 2 and q3["reversal_pairs"] == 222
             and q3["coincidences_equal_reversal_pairs"] and q3["reversal_pairs_isometric"] and q3["pm_pairs"] == 379 and q3["pm_same_volume"]
             and q3["pm_separated_by_name"] and q3["m004_shape_2sqrt3_i"] and q3["m003_shape_hexagonal"])
    q5 = q5_register()
    # Q1 on every thread.
    q1 = run_q1(st)
    hi = q1["one_twenty_digits"]
    lo = q1["sixty_digits"]
    hi_all = all(o[k]["undecided"] == 0 and (o[k]["h1"], o[k]["r1"], o[k]["private"]) == (1, 1, 0) for _, o in hi.values() for k in (1, 2, 3))
    lo_undecided = sorted(lab for lab, (_, o) in lo.items() if any(o[k]["undecided"] for k in (1, 2, 3)))
    lo_undecided_blocks = Counter(k for lab in lo_undecided for k in (1, 2, 3) if lo[lab][1][k]["undecided"])
    lo_undecided_lengths = Counter(lo[lab][0] for lab in lo_undecided)
    lo_decided_all_110 = all((o[k]["h1"], o[k]["r1"], o[k]["private"]) == (1, 1, 0) for lab, (_, o) in lo.items() if lab not in lo_undecided for k in (1, 2, 3))
    hi_min_genuine = min(o[k]["log10_min_genuine"] for _, o in hi.values() for k in (1, 2, 3) if o[k]["log10_min_genuine"] is not None)
    hi_max_zero = max((o[k]["log10_max_zero"] for _, o in hi.values() for k in (1, 2, 3) if o[k]["log10_max_zero"] is not None), default=None)
    m004_ctrl = all((hi["+LR"][1][k]["h1"], hi["+LR"][1][k]["r1"], hi["+LR"][1][k]["private"]) == (1, 1, 0) for k in (1, 2, 3))
    q1_ok = len(hi) == 758 and hi_all and m004_ctrl
    r956_ok = q1_ok and q2_ok and q3_ok and q5["ok"]
    r956 = {"row": 956, "commits": ["47a86fa8b"],
            "q1": {"states": len(hi), "all_decided_and_1_1_0_at_120_digits": hi_all, "m004_control": m004_ctrl,
                   "log10_smallest_genuine_relative_singular_value_120": hi_min_genuine, "log10_largest_zero_relative_singular_value_120": hi_max_zero,
                   "sixty_digit_band_undecided_states_in_own_matrices": len(lo_undecided), "sixty_digit_undecided_blocks": {str(k): v for k, v in lo_undecided_blocks.items()},
                   "sixty_digit_undecided_word_lengths": {str(k): v for k, v in lo_undecided_lengths.items()}, "sixty_digit_decided_all_1_1_0": lo_decided_all_110, "ok": q1_ok},
            "q2": {"table": {str(k): {kk: vv for kk, vv in q2[k].items()} for k in (1, 2, 3)}, "fiber_dim_n_2_3_4": fiber[1:], "table_ok": tab_ok,
                   "joint_zero": joint_ok, "single_moves_ok": single_ok, "threads": threads, "threads_ok": threads_ok, "ok": q2_ok},
            "q3": q3, "q3_ok": q3_ok, "q5": q5,
            "readings": "Q4 (assembled from the record) and Q6's reading of the observer layer: not independently checked",
            "result": "the same" if r956_ok else "differs"}
    # Row 955: the rule's hand-derived structure and its predictions, against the same computations.
    blocks_by_hand = {1: [0, 1, 1, 1], 2: [2, 1, 1, 1], 3: [1, 2, 2, 2]}
    hand_ok = all(q2[k]["q8_multiplicities"] == blocks_by_hand[k] and q2[k]["h1"] == (2 * k + 1) + blocks_by_hand[k][0] and q2[k]["visible"] == (2 * k + 1) - blocks_by_hand[k][0] for k in (1, 2, 3))
    r955_ok = hand_ok and q3["census_identifications_ok"] and q5["ok"] and threads["odd"] == {str((1, 1, 2)): 326}
    r955 = {"row": 955, "commits": ["1915fe928", "ddd62c4ee"], "hand_table_from_Q8_blocks": hand_ok, "census_identifications": q3["identify"],
            "census_identifications_ok": q3["census_identifications_ok"], "founding_rule_identities": q5["ok"],
            "odd_trace_prediction_1_1_2": threads["odd"] == {str((1, 1, 2)): 326},
            "note": "the script commit ddd62c4ee is recorded as a seal only; its code was neither read nor run",
            "result": "the same" if r955_ok else "differs"}
    return r955, r956


# ---------------------------------------------------------------------------
# 4. Rows 957-960
# ---------------------------------------------------------------------------

def triplet_model(auts: dict | None = None):
    """V = H^1(F_2; I_3 (x) rho_Q) with the lifts Ad(G) (x) G, made unitary by the group average; returns the
    generators, the group on V, and the decomposition into triplets."""
    auts = auts or AUT_W
    A6 = np.kron(np.eye(3), Qa)
    B6 = np.kron(np.eye(3), Qb)
    GLw, _ = XC.lift(auts["L"], Qa, Qb)
    GRw, _ = XC.lift(auts["R"], Qa, Qb)
    TL = XC.h1_action(auts["L"], A6, B6, XC.lift6(GLw))
    TR = XC.h1_action(auts["R"], A6, B6, XC.lift6(GRw))
    n = TL.shape[0]
    GV0 = XC.closure([TL, TR, -np.eye(n, dtype=complex)])
    H = sum(g.conj().T @ g for g in GV0)
    Cc = np.linalg.cholesky(H).conj().T
    Ci = np.linalg.inv(Cc)
    TL, TR = Cc @ TL @ Ci, Cc @ TR @ Ci
    GV = [Cc @ g @ Ci for g in GV0]
    cdim, types = XC.decompose([TL, TR, -np.eye(n, dtype=complex)], n)
    return TL, TR, GV, cdim, types, (GLw, GRw)


def _unitarize(mats: list[np.ndarray]) -> tuple[list[np.ndarray], np.ndarray]:
    H = sum(g.conj().T @ g for g in mats)
    C = np.linalg.cholesky(H).conj().T
    Ci = np.linalg.inv(C)
    return [C @ g @ Ci for g in mats], C


def _eigvecs_if_distinct(g: np.ndarray):
    w, v = np.linalg.eig(g)
    if min(abs(w[i] - w[j]) for i in range(3) for j in range(i + 1, 3)) < 1e-6:
        return None
    return [v[:, i] / np.linalg.norm(v[:, i]) for i in range(3)]


def _proj(v):
    return np.outer(v, v.conj())


def _basis_key(vs):
    return frozenset(XC._key(_proj(v)) for v in vs)


def _pattern(b1, b2):
    return np.array([[abs(np.vdot(u, v)) ** 2 for v in b2] for u in b1])


def _canon(M):
    best = None
    for pr in itertools.permutations(range(3)):
        for pc in itertools.permutations(range(3)):
            t = tuple(np.round(M[np.ix_(pr, pc)], 9).ravel().tolist())
            if best is None or t < best:
                best = t
    return best


def _multiset(M):
    return tuple(sorted(np.round(np.asarray(M).ravel(), 9).tolist()))


def verify_row_957() -> dict:
    """Row 957 (@ eb4e97801, W35)."""
    TL, TR, GV, cdim, types, _lw = triplet_model()
    tri = [t for t in types if t["d"] == 3]
    split_ok = len(types) == 2 and all(t["d"] == 3 and t["m"] == 1 for t in types)
    Q = tri[0]["spaces"][0]
    restrict = lambda g: Q.conj().T @ g @ Q
    GT_raw = [restrict(g) for g in GV]
    gL, gR = restrict(TL), restrict(TR)
    irreducible = len(XC.commutant_basis([gL, gR], 3)) == 1
    GT, C = _unitarize(GT_raw)
    Ci = np.linalg.inv(C)
    uL, uR = C @ gL @ Ci, C @ gR @ Ci
    order_T = len(XC.closure([uL, uR, -np.eye(3, dtype=complex)]))
    distinct = [g for g in GT if _eigvecs_if_distinct(g) is not None]
    bases = {}
    for g in distinct:
        vs = _eigvecs_if_distinct(g)
        bases[_basis_key(vs)] = vs
    for g in GT:
        for h in GT:
            if np.allclose(g @ h, h @ g) and _eigvecs_if_distinct(g) is None and _eigvecs_if_distinct(h) is None:
                vs = _eigvecs_if_distinct(g + 0.6180339 * h + 0.123 * g @ h)
                if vs is not None:
                    bases[_basis_key(vs)] = vs
    lines = {}
    for g in GT:
        w, v = np.linalg.eig(g)
        groups = []
        for i in range(3):
            for gr in groups:
                if abs(w[gr[0]] - w[i]) < 1e-6:
                    gr.append(i)
                    break
            else:
                groups.append([i])
        if len(groups) == 2:
            simple = [gr for gr in groups if len(gr) == 1][0][0]
            vv = v[:, simple] / np.linalg.norm(v[:, simple])
            lines[XC._key(_proj(vv))] = vv
    blist = list(bases.values())
    patterns = {}
    for i in range(len(blist)):
        for j in range(i + 1, len(blist)):
            M = _pattern(blist[i], blist[j])
            patterns[_canon(M)] = _multiset(M)
    columns = set()
    for b in blist:
        for ln in lines.values():
            columns.add(tuple(sorted(np.round([abs(np.vdot(u, ln)) ** 2 for u in b], 9).tolist())))
    r3 = math.sqrt(3)
    exp_patterns = {
        "single_maximal_angle": _multiset([1, 0, 0, 0, 0.5, 0.5, 0, 0.5, 0.5]),
        "tri_bimaximal": _multiset([2 / 3, 1 / 3, 0, 1 / 6, 1 / 3, 1 / 2, 1 / 6, 1 / 3, 1 / 2]),
        "bimaximal": _multiset([0.5, 0.5, 0, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5]),
        "trimaximal": _multiset([1 / 3] * 5 + [(2 + r3) / 6] * 2 + [(2 - r3) / 6] * 2),
        "circulant": _multiset([1 / 9] * 3 + [4 / 9] * 6),
        "democratic": _multiset([1 / 3] * 9),
    }
    exp_columns = {tuple(sorted(np.round(c, 9).tolist())) for c in ([0, 0, 1], [0, 0.5, 0.5], [1 / 6, 1 / 6, 2 / 3], [0.25, 0.25, 0.5], [1 / 3, 1 / 3, 1 / 3])}
    pats_ok = len(patterns) == 6 and set(patterns.values()) == set(exp_patterns.values())
    cols_ok = columns == exp_columns

    def word(wd, gl, gr):
        M = np.eye(3, dtype=complex)
        mp_ = {"L": gl, "R": gr, "l": np.linalg.inv(gl), "r": np.linalg.inv(gr)}
        for ch in wd:
            M = M @ mp_[ch]
        return M

    def simple_line(g):
        w, v = np.linalg.eig(g)
        for i in range(3):
            if sum(1 for j in range(3) if abs(w[i] - w[j]) < 1e-6) == 1 and sum(1 for j in range(3) for k2 in range(j + 1, 3) if abs(w[j] - w[k2]) < 1e-6) == 1:
                return v[:, i] / np.linalg.norm(v[:, i])
        return None

    def raw(M):
        return np.sort(np.asarray(M, dtype=float).ravel())

    def cells(gl, gr, rev: bool):
        f = (lambda q: q[::-1]) if rev else (lambda q: q)
        out = {}
        bL, bR = _eigvecs_if_distinct(gl), _eigvecs_if_distinct(gr)
        bRL = _eigvecs_if_distinct(word(f("RL"), gl, gr))
        g1, g2 = word("RR", gl, gr), word(f("rLL"), gl, gr)
        bpair = _eigvecs_if_distinct(g1 + 0.6180339 * g2 + 0.123 * g1 @ g2) if np.allclose(g1 @ g2, g2 @ g1) else None
        out["L_vs_R"] = raw(_pattern(bL, bR)) if bL and bR else None
        out["RL_vs_RR_RinvLL"] = raw(_pattern(bRL, bpair)) if bRL and bpair else None
        out["L_vs_RL"] = raw(_pattern(bL, bRL)) if bL and bRL else None
        lRR = simple_line(word("RR", gl, gr))
        lRRL = simple_line(word(f("RRL"), gl, gr))
        out["RL_vs_RR_line"] = raw([abs(np.vdot(u, lRR)) ** 2 for u in bRL]) if (bRL and lRR is not None) else None
        out["RL_vs_RRL_line"] = raw([abs(np.vdot(u, lRRL)) ** 2 for u in bRL]) if (bRL and lRRL is not None) else None
        return out

    def close(x, ref):
        return x is not None and np.allclose(x, np.sort(np.asarray(ref, dtype=float)), atol=1e-9)

    c_fwd = cells(uL, uR, False)
    c_rev = cells(uL, uR, True)
    named_ok = (close(c_fwd["L_vs_R"], exp_patterns["bimaximal"]) and close(c_fwd["RL_vs_RR_RinvLL"], exp_patterns["tri_bimaximal"])
                and close(c_fwd["L_vs_RL"], exp_patterns["trimaximal"]) and close(c_fwd["RL_vs_RR_line"], [1 / 3] * 3)
                and close(c_fwd["RL_vs_RRL_line"], [1 / 6, 1 / 6, 2 / 3]))
    order_free = all((c_fwd[k] is None and c_rev[k] is None) or (c_fwd[k] is not None and c_rev[k] is not None and np.allclose(c_fwd[k], c_rev[k], atol=1e-9)) for k in c_fwd)
    # Haar basis scrambling on T: every named cell unchanged, compared unrounded.
    haar_max = 0.0
    for _ in range(5):
        Zr = (RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))) / np.sqrt(2)
        W, Rr = np.linalg.qr(Zr)
        W = W @ np.diag(np.diag(Rr) / abs(np.diag(Rr)))
        c_s = cells(W @ uL @ W.conj().T, W @ uR @ W.conj().T, False)
        for key in c_fwd:
            x0, x1 = c_fwd[key], c_s[key]
            haar_max = max(haar_max, 1.0 if (x0 is None or x1 is None) else float(np.max(np.abs(x0 - x1))))
    haar_ok = haar_max < 1e-12
    counts_ok = order_T == 96 and len(GT) == 96 and len(distinct) == 56 and len(bases) == 11 and len(lines) == 9
    ok = split_ok and irreducible and counts_ok and pats_ok and cols_ok and named_ok and order_free and haar_ok
    return {"row": 957, "commits": ["eb4e97801"], "V_dim": int(TL.shape[0]), "order_V": len(GV), "split_two_triplets": split_ok,
            "T_irreducible_so_form_unique_by_Schur": irreducible, "order_T": order_T, "elements_three_distinct_eigenvalues": len(distinct),
            "eigenbases": len(bases), "eigenlines": len(lines), "full_patterns": len(patterns), "patterns_as_named": pats_ok,
            "columns": sorted(columns), "columns_as_named": cols_ok, "named_cells": {k: (v.tolist() if v is not None else None) for k, v in c_fwd.items()},
            "named_cells_ok": named_ok, "product_order_free": order_free, "haar_max_change": haar_max, "haar_below_1e-12": haar_ok,
            "readings": "the comparison with data: cannot check (0 of 19); the cup-product construction itself: not independently checked (fixed up to scale by Schur)",
            "result": "the same" if ok else "differs"}


def verify_row_958() -> dict:
    """Row 958 (@ 2abff008c, W36)."""
    E8 = XC.E8
    a4g = [r for r in E8 if np.allclose(r[5:], 0) and sorted(r[:5].tolist()) == [-1.0, 0, 0, 0, 1.0]]
    orth = [r for r in E8 if all(abs(r @ s) < 1e-12 for s in a4g)]
    gen = RNG.normal(size=8)
    pos = [r for r in orth if r @ gen > 0]
    simple = [r for r in pos if not any(np.allclose(r, p + q) for p in pos for q in pos)]
    cart = np.array([[int(round(2 * (a @ b) / (b @ b))) for b in simple] for a in simple]) if simple else np.zeros((0, 0))
    a4_cartan = len(simple) == 4 and sorted(Counter(int(x) for x in cart.ravel()).items()) == [(-1, 6), (0, 6), (2, 4)]
    snf = sp.matrices.normalforms.smith_normal_form(sp.Matrix([[3, 2]]), domain=sp.ZZ)
    connected = math.gcd(3, 2) == 1 and list(snf) == [1, 0]
    w = sp.exp(2 * sp.pi * sp.I / 3)
    holds_centres = sp.simplify(w ** 3 * 1 - 1) == 0 and ((-1) ** 2 == 1)
    z5_meet = sum(1 for k in range(5) if (3 * k + 2 * k) % 5 == 0)
    xs = sp.symbols("x1:6")
    c1_l2 = sp.expand(sum(xs[i] + xs[j] for i, j in itertools.combinations(range(5), 2)))
    splitting = sp.simplify(c1_l2 - 4 * sum(xs)) == 0
    ok = len(a4g) == 20 and len(orth) == 20 and a4_cartan and connected and holds_centres and z5_meet == 5 and splitting
    return {"row": 958, "commits": ["2abff008c"], "orthogonal_roots": len(orth), "simple_roots": len(simple), "cartan_A4": a4_cartan,
            "kernel_of_character_3_2_connected": connected, "holds_both_centres": bool(holds_centres), "meets_SU5_b_in": z5_meet,
            "c1_lambda2_equals_4_c1": splitting,
            "readings": "step 4 (gapped cusp, winding, magnetic family, the common point's twist): readings, apart from the degree identity",
            "result": "the same" if ok else "differs"}


def pmns(t12, t13, t23, d):
    s12, c12, s13, c13, s23, c23 = np.sin(t12), np.cos(t12), np.sin(t13), np.cos(t13), np.sin(t23), np.cos(t23)
    e = np.exp(1j * d)
    return np.array([
        [c12 * c13, s12 * c13, s13 / e],
        [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13],
    ])


def haar(n=3):
    Z = (RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    return Q @ np.diag(np.diag(R) / abs(np.diag(R)))


def lepton_observables(Ye, Mn):
    we, Ue = np.linalg.eigh(Ye @ Ye.conj().T)
    wn, Un = np.linalg.eigh(Mn @ Mn.conj().T)
    U = Ue.conj().T @ Un
    J = (U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])).imag
    return np.abs(U) ** 2, J


def verify_row_959() -> dict:
    """Row 959 (@ 94350d689, W37)."""
    t12, t13, t23, dl = sp.symbols("t12 t13 t23 delta", real=True)
    s12, c12, s13, c13, s23, c23 = sp.sin(t12), sp.cos(t12), sp.sin(t13), sp.cos(t13), sp.sin(t23), sp.cos(t23)
    e = sp.exp(sp.I * dl)
    Ue1 = c12 * c13
    Um1 = -s12 * c23 - c12 * s23 * s13 * e
    Ut1 = s12 * s23 - c12 * c23 * s13 * e
    abs2 = lambda z: sp.expand(z * sp.conjugate(z))
    ue1_ok = sp.simplify(abs2(Ue1) - c12 ** 2 * c13 ** 2) == 0
    C12, C13 = sp.symbols("C12sq C13sq", positive=True)
    c12sol = sp.solve(sp.Eq(C12 * C13, sp.Rational(2, 3)), C12)
    sum_rule = ue1_ok and len(c12sol) == 1 and sp.simplify((1 - c12sol[0]) - (1 - sp.Rational(2, 3) / C13)) == 0
    diff = sp.expand_complex(abs2(Um1) - abs2(Ut1))
    target = (s12 ** 2 - c12 ** 2 * s13 ** 2) * sp.cos(2 * t23) + 2 * s12 * c12 * s13 * sp.sin(2 * t23) * sp.cos(dl)
    mp.mp.dps = 50
    fdiff = sp.lambdify((t12, t13, t23, dl), diff - target, "mpmath")
    worst_id = max(abs(fdiff(mp.mpf(RNG.uniform(0.1, 1.4)), mp.mpf(RNG.uniform(0.05, 0.6)), mp.mpf(RNG.uniform(0.2, 1.3)), mp.mpf(RNG.uniform(0, 6.2)))) for _ in range(25))
    cos_formula = bool(worst_id < mp.mpf(10) ** (-40))
    # cos delta then follows by solving target = 0 for cos(delta)
    cd_sym = sp.symbols("cd")
    sol_cd = sp.solve(sp.Eq(target.subs(sp.cos(dl), cd_sym), 0), cd_sym)
    cosd = -(s12 ** 2 - c12 ** 2 * s13 ** 2) * sp.cos(2 * t23) / (2 * s12 * c12 * s13 * sp.sin(2 * t23))
    cos_formula = cos_formula and len(sol_cd) == 1 and sp.simplify(sol_cd[0] - cosd) == 0
    # algebraic test points
    haar_ok = True
    col_ok = True
    worst = 0.0
    bad_overlap_moves = 0.0
    for s13sq, s23sq in ((Fraction(1, 50), Fraction(3, 7)), (Fraction(1, 45), Fraction(4, 9)), (Fraction(1, 40), Fraction(5, 9))):
        th13 = math.asin(math.sqrt(float(s13sq)))
        c13sq = 1 - float(s13sq)
        th12 = math.acos(math.sqrt(2 / (3 * c13sq)))
        th23 = math.asin(math.sqrt(float(s23sq)))
        cd = -(math.sin(th12) ** 2 - math.cos(th12) ** 2 * math.sin(th13) ** 2) * math.cos(2 * th23) / (2 * math.sin(th12) * math.cos(th12) * math.sin(th13) * math.sin(2 * th23))
        for d in (math.acos(cd), 2 * math.pi - math.acos(cd)):
            U = pmns(th12, th13, th23, d)
            col = np.abs(U[:, 0]) ** 2
            if not np.allclose(col, [2 / 3, 1 / 6, 1 / 6], atol=1e-13):
                col_ok = False
            UL, UR = haar(), haar()
            Ye = UL @ np.diag([1, 2, 3]) @ UR.conj().T
            Un = UL @ U @ np.diag(np.exp(1j * RNG.uniform(0, 2 * np.pi, 3)))
            Mn = Un @ np.diag([1, 3, 7]) @ Un.T
            P0, J0 = lepton_observables(Ye, Mn)
            for _ in range(4):
                W, VR = haar(), haar()
                P1, J1 = lepton_observables(W @ Ye @ VR.conj().T, W @ Mn @ W.T)
                worst = max(worst, float(np.max(np.abs(P1 - P0))), abs(J1 - J0))
            Jf = math.sin(th12) * math.cos(th12) * math.sin(th23) * math.cos(th23) * math.sin(th13) * math.cos(th13) ** 2 * math.sin(d)
            if abs(abs(J0) - abs(Jf)) > 1e-12 or not np.allclose(P0, np.abs(U) ** 2, atol=1e-12):
                haar_ok = False
    haar_ok = haar_ok and worst < 1e-12
    # B1614 cells.
    x, y, z = sp.symbols("x y z")
    Lm = (z, y, y * z - x)
    Rm = (x, z, x * z - y)
    sols = sp.solve([Lm[0] - x, Lm[1] - y, Lm[2] - z, Rm[0] - x, Rm[1] - y, Rm[2] - z], [x, y, z], dict=True)
    fixed = sorted(tuple(int(s[v]) for v in (x, y, z)) for s in sols)
    cells = {}
    one = sp.Matrix([[1]])
    cells["chi0"] = common_point_block(one, one, None)
    for nm, (a, b) in (("chi1", (-1, 1)), ("chi2", (1, -1)), ("chi3", (-1, -1))):
        cells[nm] = common_point_block(sp.Matrix([[a]]), sp.Matrix([[b]]), None)
    cells["adjoint"] = common_point_block(sp_sym(SQa, 2), sp_sym(SQb, 2), None)
    cells["rho_Q"] = common_point_block(SQa, SQb, None)
    for nm, (a, b) in (("chi1_rho", (-1, 1)), ("chi2_rho", (1, -1)), ("chi3_rho", (-1, -1))):
        cells[nm] = common_point_block(a * SQa, b * SQb, None)
    trip = {k: (v["h1"], v["visible"], v["private"]) for k, v in cells.items()}
    cells_ok = (trip["chi0"] == (2, 0, 2) and all(trip[p] == (1, 1, 0) for p in ("chi1", "chi2", "chi3")) and trip["adjoint"] == (3, 3, 0)
                and trip["rho_Q"] == (2, 0, 2) and all(trip[p] == (2, 0, 2) for p in ("chi1_rho", "chi2_rho", "chi3_rho")))
    TL, TR, GV, cdim, types, _lw = triplet_model()
    tri = [t["spaces"][0] for t in types if t["d"] == 3]
    chis = []
    for Q in tri:
        cl = np.trace(Q.conj().T @ TL @ Q)
        cr = np.trace(Q.conj().T @ TR @ Q)
        clr = np.trace(Q.conj().T @ TL @ TR @ Q)
        chis.append((cl, cr, clr))
    z8 = np.exp(1j * np.pi / 4)
    targets = [sg * z8 ** k for sg in (1, -1) for k in (1, -1)]
    near = lambda zz: min(abs(zz - t) for t in targets) < 1e-9
    chi_ok = len(chis) == 2 and all(abs(clr) < 1e-9 and near(cl) and near(cr) and abs(cl * cr - np.round((cl * cr).real)) < 1e-9 for cl, cr, clr in chis)
    conj_pair = len(chis) == 2 and abs(chis[0][0] - np.conj(chis[1][0])) < 1e-9
    odd = {}
    for nm in ("L", "R", "P"):
        m = XB.hom_mat(AUT[nm])
        det = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        fixedlines = sum(1 for v in ((1, 0), (0, 1), (1, 1)) if ((m[0][0] * v[0] + m[0][1] * v[1]) % 2, (m[1][0] * v[0] + m[1][1] * v[1]) % 2) == v)
        perm_sign = 1 if fixedlines == 1 else 0
        odd[nm] = (0 if det == 1 else 1, perm_sign)
    M2 = np.array([list(v) for v in odd.values()]) % 2
    rk = 0
    rows = [r.copy() for r in M2]
    for col in range(2):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] % 2), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][col] % 2:
                rows[i] = (rows[i] + rows[rk]) % 2
        rk += 1
    odd_ok = odd == {"L": (0, 1), "R": (0, 1), "P": (1, 1)} and rk == 2
    ok = sum_rule and cos_formula and col_ok and haar_ok and fixed == [(0, 0, 0), (2, 2, 2)] and cells_ok and chi_ok and conj_pair and odd_ok
    return {"row": 959, "commits": ["94350d689"], "tm1_sum_rule": bool(sum_rule), "cos_delta_formula": bool(cos_formula), "identity_worst_at_50_digits_log10": float(mp.log10(worst_id)) if worst_id > 0 else None,
            "tm1_column_on_test_points": col_ok, "haar_worst_change": worst, "haar_and_J_ok": haar_ok,
            "measured_angle_evaluation": "cannot check (0 of 19)",
            "joint_fixed_points": [list(f) for f in fixed], "cells": {k: list(v) for k, v in trip.items()}, "cells_ok": cells_ok,
            "triplet_characters_up_to_lift_sign_and_T_choice": chi_ok, "T_and_T_bar_conjugate": conj_pair, "odd_classes": {k: list(v) for k, v in odd.items()},
            "odd_rank_F2": rk, "odd_ok": odd_ok,
            "readings": "the forward prediction's numbers and its comparison with data: cannot check (0 of 19); the absolute phases of chi_T fixed by W21's lift signs: not independently checked",
            "result": "the same" if ok else "differs"}


def verify_row_960() -> dict:
    """Row 960 (@ 431c0517f, relay section 36)."""
    Y = [Fraction(-1, 3)] * 3 + [Fraction(1, 2)] * 2
    Z = [Fraction(-2)] * 3 + [Fraction(3)] * 2
    ratios = {z / y for z, y in zip(Z, Y)}
    ratio = ratios.pop() if len(ratios) == 1 else None
    stated_minus_6 = ratio == -6
    plus_6 = ratio == 6
    # Z-charges of the pieces: 10 = Lambda^2 5, 5bar = conjugate of 5.
    q_Q, q_u, q_e = Z[0] + Z[3], Z[0] + Z[1], Z[3] + Z[4]
    q_d, q_L = -Z[0], -Z[3]
    charges_ok = (q_Q, q_u, q_e, q_d, q_L) == (1, -4, 6, 2, -3)
    lepto = sorted({Z[0] - Z[3], Z[3] - Z[0]})
    n = sp.Symbol("n")
    idx10 = {"Q": n * 6 * q_Q, "u_bar": n * 3 * q_u, "e_bar": n * 1 * q_e}
    idx5 = {"d_bar": n * 3 * q_d, "L": n * 2 * q_L}
    sums_zero = sp.simplify(sum(idx10.values())) == 0 and sp.simplify(sum(idx5.values())) == 0
    idx_ok = idx10 == {"Q": 6 * n, "u_bar": -12 * n, "e_bar": 6 * n} and idx5 == {"d_bar": 6 * n, "L": -6 * n}
    hyper_of_pieces = {"Q": Y[0] + Y[3], "u_bar": Y[0] + Y[1], "e_bar": Y[3] + Y[4], "d_bar": -Y[0], "L": -Y[3]}
    charges_are_6Y = all(6 * hyper_of_pieces[k] == q for k, q in (("Q", q_Q), ("u_bar", q_u), ("e_bar", q_e), ("d_bar", q_d), ("L", q_L)))
    arithmetic_ok = charges_ok and lepto == [-5, 5] and sums_zero and idx_ok and charges_are_6Y and plus_6
    result = "the same" if (arithmetic_ok and stated_minus_6) else "differs"
    differing_clause = ("the words 'which is -6Y' (with the standard hypercharge Z = +6Y)" if (arithmetic_ok and not stated_minus_6) else None)
    return {"row": 960, "commits": ["431c0517f"], "Z_over_Y": str(ratio) if ratio is not None else None,
            "relay_sign_minus_6Y_holds": stated_minus_6, "Z_is_plus_6Y": plus_6, "Z_charges_1_m4_6_2_m3": charges_ok,
            "charges_equal_6Y_of_pieces": charges_are_6Y, "leptoquark_charges": [int(v) for v in lepto],
            "indices": {k: str(v) for k, v in {**idx10, **idx5}.items()}, "multiplet_sums_zero": bool(sums_zero), "index_arithmetic_ok": bool(idx_ok),
            "arithmetic_ok": arithmetic_ok, "differing_clause": differing_clause,
            "readings": "the saddle, its stability and the reading that hypercharge flux splits multiplets: not independently checked",
            "result": result}


# ---------------------------------------------------------------------------
# 5. Planted negative controls
# ---------------------------------------------------------------------------

def run_negative_controls() -> dict:
    # C1d-1: the naive law planted as true.
    A, B, _ = bundle(["chi0"] * 3)
    c_triv = conventions(A, B, 1)
    A, B, _ = bundle(["chi1", "chi2", "chi3"])
    c_P = conventions(A, B, 1)
    naive_rejected_N = 3 in c_triv["N"]
    naive_rejected_BS = 3 not in c_P["B"] and 3 not in c_P["S"]
    c1 = bool(naive_rejected_N and naive_rejected_BS)
    # C1d-2: the register planted as a hand (C(sigma) in place of rev(sigma)).
    q5 = q5_register()
    c2 = bool(q5["C_flips_cyclic_order"] and q5["lift_class_flipped_by_C"] and q5["h1_actions_differ_under_C"][1])
    # C1d-3: basis-dependent "mixing" and a broken triplet.
    Y = haar() @ np.diag([1, 2, 3]) @ haar().conj().T
    U, s, Vh = np.linalg.svd(Y)
    bad0 = np.abs(U.conj().T @ Vh.conj().T) ** 2
    WL, WR = haar(), haar()
    U1, s1, Vh1 = np.linalg.svd(WL @ Y @ WR.conj().T)
    bad1 = np.abs(U1.conj().T @ Vh1.conj().T) ** 2
    moves = float(np.max(np.abs(bad1 - bad0)))
    TL, TR, GV, cdim, types, _lw = triplet_model()
    T0, T1 = types[0]["spaces"][0], types[1]["spaces"][0]
    mixed, _ = np.linalg.qr(np.column_stack([T0[:, 0], T0[:, 1], T1[:, 0]]))
    gl, gr = mixed.conj().T @ TL @ mixed, mixed.conj().T @ TR @ mixed
    try:
        n_mixed = len(XC.closure([gl, gr, -np.eye(3, dtype=complex)], limit=3000))
    except RuntimeError:
        n_mixed = -1
    c3 = bool(moves > 1e-2 and n_mixed != 96)
    return {"C1d_1": {"E6_trivial_reaches_three_under_N": naive_rejected_N, "E6_P_no_three_under_B_and_S": naive_rejected_BS, "fired": c1},
            "C1d_2": {"fired": c2},
            "C1d_3": {"left_right_overlap_change": moves, "mixed_plane_closure": n_mixed, "fired": c3},
            "all_controls_fired": bool(c1 and c2 and c3)}


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items() if k not in ("types", "minus_types", "spaces")}
    if isinstance(o, (list, tuple, set, frozenset)):
        return [_clean(v) for v in (sorted(o) if isinstance(o, (set, frozenset)) else o)]
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, (Fraction, sp.Basic)):
        return str(o)
    if isinstance(o, (complex, np.complexfloating)):
        return [float(np.real(o)), float(np.imag(o))]
    if isinstance(o, np.ndarray):
        return None
    return o


def main() -> None:
    t0 = time.time()
    try:
        controls = run_negative_controls()
    except Exception as exc:
        controls = {"all_controls_fired": False, "error": repr(exc)}
    if not controls["all_controls_fired"]:
        (HERE / "verify_x_c1d_out.json").write_text(json.dumps({"card": "X-C1d", "aborted": True, "negative_controls": _clean(controls)}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        sys.exit(2)

    def safe(fn, *args):
        try:
            return fn(*args)
        except Exception as exc:  # recorded, never hidden: a verifier fault is not a result on the row
            return {"result": "verifier error", "error": repr(exc)}

    rows = {}
    rows["951"] = safe(verify_row_951)
    rows["952"] = safe(verify_row_952)
    r = safe(verify_rows_953_954)
    rows["953"], rows["954"] = (r if isinstance(r, tuple) else (r, r))
    r = safe(verify_rows_955_956)
    rows["955"], rows["956"] = (r if isinstance(r, tuple) else (r, r))
    rows["957"] = safe(verify_row_957)
    rows["958"] = safe(verify_row_958)
    rows["959"] = safe(verify_row_959)
    rows["960"] = safe(verify_row_960)
    payload = {"card": "X-C1d", "seat": "agy-exp", "own_x_c1c_helpers_sha256": XC_SHA, "own_x_c1b_helpers_sha256": XC.XB_SHA,
               "negative_controls": _clean(controls), "rows": _clean(rows), "elapsed_seconds": round(time.time() - t0, 3)}
    out_bytes = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    (HERE / "verify_x_c1d_out.json").write_bytes(out_bytes)
    (HERE / "OUTPUT_SHA256.txt").write_text(f"{hashlib.sha256(out_bytes).hexdigest()}  verify_x_c1d_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
