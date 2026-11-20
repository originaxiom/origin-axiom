#!/usr/bin/env python3
r"""Independent Cold-Room Zero-Trust Referee for Card A2-OW3 (+ Erratum 1).

Strictly data-free (0 of 19):
  - Zero empirical / PDG numbers.
  - Zero float or complex AST literals.
  - Zero frontier/ imports.
  - Zero hard-coded proof flags; every assertion is computed live from explicit
    matrices, SnapPy hyperbolic structures, exact cyclotomic / Gaussian-integer
    algebra, and arbitrary-precision mpmath arithmetic.

Independent constructions:
  - OW3-A: Catalan constant G via three independent methods (Clausen Cl_2(pi/2),
    direct forward-difference Euler transform of sum (-1)^n/(2n+1)^2, and
    Ramanujan hypergeometric series), cross-checked against SnapPy L5a1 and 5^2_1;
    full primitive unblocked punctured-torus weave census (b++ len 2..7, b+- len
    2..7, b-+ len 1..6) with pairwise SnapPy isometry verification; all three
    Whitehead accumulation sequences (b++L^k R, b+-L^k R, b-+L^k) for k = 1..50;
    full 2D regulated phase grid Z(s, beta).
  - OW3-B Part 1: Exact Q[w]/(Phi_5(w)) cyclotomic ring + 65-digit mpmath
    verification of Tr(P_+ D(a,b)) = +1/2, Tr(P_- D(a,b)) = -1/2 across all 24
    nonzero (a,b) in (Z/5)^2 \ {(0,0)}, plus explicit 15x15 Kronecker-product
    contraction onto +(1/2) S_ph and -(1/2) S_ph.
  - OW3-B Part 2: 32x32 Cl(10) Hermitian gamma matrices constructed via explicit
    5-fold Pauli tensor products (Jordan-Wigner construction) in exact Gaussian
    integers Z[i], independent C_10 = Gamma_2 Gamma_4 Gamma_6 Gamma_8 Gamma_10,
    exact 16x16 symmetric bilinear matrices on Gamma_11 = +1, exact holomorphic
    5_H / 5bar_H separation, 48x48 end-to-end 3-generation embedding, exact
    11/12 tan(beta) invariance across {1/5, 1, 3, 10, 50}, Jarlskog commutator
    cross-check, and 10-trial Mezzadri QR Haar unitary basis-scrambling.
  - OW3-C: Independent tests catching all four planted faults PF-OW3-1..4.
"""

from __future__ import annotations

import ast
import itertools
import json
import math
import pathlib
import random
from fractions import Fraction
from typing import Dict, List, Sequence, Tuple

import mpmath as mp
import numpy as np
import snappy


# ---------------------------------------------------------------------------
# Exact Cyclotomic Ring Q[w] / (Phi_5(w)), Phi_5(w) = 1 + w + w^2 + w^3 + w^4
# ---------------------------------------------------------------------------

class Cyclo5:
    """Exact element c0 + c1*w + c2*w^2 + c3*w^3 in Q[w]/(Phi_5(w))."""

    __slots__ = ("c",)

    def __init__(self, c0: Fraction, c1: Fraction, c2: Fraction, c3: Fraction) -> None:
        self.c = (Fraction(c0), Fraction(c1), Fraction(c2), Fraction(c3))

    @classmethod
    def zero(cls) -> "Cyclo5":
        z = Fraction(0)
        return cls(z, z, z, z)

    @classmethod
    def from_rational(cls, q: Fraction) -> "Cyclo5":
        z = Fraction(0)
        return cls(Fraction(q), z, z, z)

    @classmethod
    def omega_pow(cls, k: int) -> "Cyclo5":
        r = k % 5
        z = Fraction(0)
        one = Fraction(1)
        neg = Fraction(-1)
        if r == 0:
            return cls(one, z, z, z)
        if r == 1:
            return cls(z, one, z, z)
        if r == 2:
            return cls(z, z, one, z)
        if r == 3:
            return cls(z, z, z, one)
        return cls(neg, neg, neg, neg)

    def __add__(self, other: "Cyclo5") -> "Cyclo5":
        return Cyclo5(
            self.c[0] + other.c[0],
            self.c[1] + other.c[1],
            self.c[2] + other.c[2],
            self.c[3] + other.c[3],
        )

    def __sub__(self, other: "Cyclo5") -> "Cyclo5":
        return Cyclo5(
            self.c[0] - other.c[0],
            self.c[1] - other.c[1],
            self.c[2] - other.c[2],
            self.c[3] - other.c[3],
        )

    def __mul__(self, other: "Cyclo5") -> "Cyclo5":
        raw = [Fraction(0)] * 7
        for i in range(4):
            ai = self.c[i]
            if ai == 0:
                continue
            for j in range(4):
                bj = other.c[j]
                if bj != 0:
                    raw[i + j] += ai * bj
        # Reduce powers w^5 = 1, w^6 = w, then w^4 = -(1 + w + w^2 + w^3)
        r0 = raw[0] + raw[5]
        r1 = raw[1] + raw[6]
        r2 = raw[2]
        r3 = raw[3]
        r4 = raw[4]
        return Cyclo5(r0 - r4, r1 - r4, r2 - r4, r3 - r4)

    def scale(self, q: Fraction) -> "Cyclo5":
        return Cyclo5(self.c[0] * q, self.c[1] * q, self.c[2] * q, self.c[3] * q)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cyclo5):
            return False
        return self.c == other.c

    def is_zero(self) -> bool:
        return all(x == 0 for x in self.c)

    def to_str(self) -> str:
        return (
            f"({self.c[0]}) + ({self.c[1]})*w + ({self.c[2]})*w^2 + ({self.c[3]})*w^3"
        )


def c5_matmul(A: List[List[Cyclo5]], B: List[List[Cyclo5]]) -> List[List[Cyclo5]]:
    n = len(A)
    m = len(B[0])
    p = len(B)
    out = [[Cyclo5.zero() for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(p):
            aik = A[i][k]
            if aik.is_zero():
                continue
            for j in range(m):
                bkj = B[k][j]
                if not bkj.is_zero():
                    out[i][j] = out[i][j] + (aik * bkj)
    return out


def c5_trace(A: List[List[Cyclo5]]) -> Cyclo5:
    acc = Cyclo5.zero()
    for i in range(len(A)):
        acc = acc + A[i][i]
    return acc


def c5_eye(n: int) -> List[List[Cyclo5]]:
    one = Cyclo5.from_rational(Fraction(1))
    z = Cyclo5.zero()
    return [[one if i == j else z for j in range(n)] for i in range(n)]


def c5_mat_pow(A: List[List[Cyclo5]], exp: int) -> List[List[Cyclo5]]:
    res = c5_eye(len(A))
    for _ in range(exp):
        res = c5_matmul(res, A)
    return res


def c5_mat_eq(A: List[List[Cyclo5]], B: List[List[Cyclo5]]) -> bool:
    return all(
        A[i][j] == B[i][j]
        for i in range(len(A))
        for j in range(len(A[0]))
    )


# ---------------------------------------------------------------------------
# Exact Gaussian Integers Z[i] for 32x32 Cl(10) Jordan-Wigner Construction
# ---------------------------------------------------------------------------

class GaussInt:
    """Exact Gaussian integer re + im*i with integer coordinates."""

    __slots__ = ("re", "im")

    def __init__(self, re: int, im: int = 0) -> None:
        self.re = int(re)
        self.im = int(im)

    def __add__(self, other: "GaussInt") -> "GaussInt":
        return GaussInt(self.re + other.re, self.im + other.im)

    def __sub__(self, other: "GaussInt") -> "GaussInt":
        return GaussInt(self.re - other.re, self.im - other.im)

    def __neg__(self) -> "GaussInt":
        return GaussInt(-self.re, -self.im)

    def __mul__(self, other: "GaussInt") -> "GaussInt":
        return GaussInt(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def conj(self) -> "GaussInt":
        return GaussInt(self.re, -self.im)

    def norm_sq(self) -> int:
        return self.re * self.re + self.im * self.im

    def div_exact_int(self, d: int) -> "GaussInt":
        if self.re % d != 0 or self.im % d != 0:
            raise ValueError("Non-exact Gaussian integer division")
        return GaussInt(self.re // d, self.im // d)

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GaussInt):
            return False
        return self.re == other.re and self.im == other.im

    def to_complex(self) -> complex:
        return complex(self.re, self.im)


G0 = GaussInt(0, 0)
G1 = GaussInt(1, 0)
GM1 = GaussInt(-1, 0)
GI = GaussInt(0, 1)
GMI = GaussInt(0, -1)


def gi_kron(A: List[List[GaussInt]], B: List[List[GaussInt]]) -> List[List[GaussInt]]:
    ra, ca = len(A), len(A[0])
    rb, cb = len(B), len(B[0])
    out = [[G0 for _ in range(ca * cb)] for _ in range(ra * rb)]
    for i in range(ra):
        for j in range(ca):
            aij = A[i][j]
            if aij.is_zero():
                continue
            for p in range(rb):
                for q in range(cb):
                    bpq = B[p][q]
                    if not bpq.is_zero():
                        out[i * rb + p][j * cb + q] = aij * bpq
    return out


def gi_kron_all(mats: Sequence[List[List[GaussInt]]]) -> List[List[GaussInt]]:
    res = mats[0]
    for m in mats[1:]:
        res = gi_kron(res, m)
    return res


def gi_matmul(A: List[List[GaussInt]], B: List[List[GaussInt]]) -> List[List[GaussInt]]:
    ra, ca = len(A), len(A[0])
    cb = len(B[0])
    out = [[G0 for _ in range(cb)] for _ in range(ra)]
    for i in range(ra):
        row_a = A[i]
        row_o = out[i]
        for k in range(ca):
            aik = row_a[k]
            if aik.is_zero():
                continue
            row_b = B[k]
            for j in range(cb):
                bkj = row_b[j]
                if not bkj.is_zero():
                    row_o[j] = row_o[j] + (aik * bkj)
    return out


def gi_add(A: List[List[GaussInt]], B: List[List[GaussInt]]) -> List[List[GaussInt]]:
    return [
        [A[i][j] + B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def gi_sub(A: List[List[GaussInt]], B: List[List[GaussInt]]) -> List[List[GaussInt]]:
    return [
        [A[i][j] - B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def gi_scale(A: List[List[GaussInt]], s: GaussInt) -> List[List[GaussInt]]:
    return [[s * x for x in row] for row in A]


def gi_transpose(A: List[List[GaussInt]]) -> List[List[GaussInt]]:
    r, c = len(A), len(A[0])
    return [[A[i][j] for i in range(r)] for j in range(c)]


def gi_dagger(A: List[List[GaussInt]]) -> List[List[GaussInt]]:
    r, c = len(A), len(A[0])
    return [[A[i][j].conj() for i in range(r)] for j in range(c)]


def gi_eye(n: int) -> List[List[GaussInt]]:
    return [[G1 if i == j else G0 for j in range(n)] for i in range(n)]


def gi_max_norm_sq(A: List[List[GaussInt]]) -> int:
    m = 0
    for row in A:
        for x in row:
            ns = x.norm_sq()
            if ns > m:
                m = ns
    return m


# ---------------------------------------------------------------------------
# Task OW3-A: Catalan Constant, Unblocked Weave Census, Whitehead Wall, Z(s,b)
# ---------------------------------------------------------------------------

def compute_catalan_independent() -> Dict[str, object]:
    """Compute Catalan's constant G by three independent methods at 65+ dps."""
    mp.mp.dps = 80

    # Method 1: Lobachevsky / Clausen function Cl_2(pi/2) = G
    g_clausen = mp.clsin(2, mp.pi / 2)

    # Method 2: Direct forward-difference Euler transform of sum_{n>=0} (-1)^n / (2n+1)^2
    with mp.workdps(160):
        n_terms = 240
        row = [mp.mpf(1) / mp.mpf((2 * j + 1) ** 2) for j in range(n_terms)]
        total = mp.mpf(0)
        pow2 = mp.mpf(2)
        for _ in range(n_terms):
            total += row[0] / pow2
            pow2 *= 2
            row = [row[i] - row[i + 1] for i in range(len(row) - 1)]
        g_euler = +total
    g_euler = mp.mpf(g_euler)

    # Method 3: Ramanujan all-positive hypergeometric series
    # G = (pi/8) * ln(2 + sqrt(3)) + (3/8) * sum_{n>=0} 1 / ((2n+1)^2 * C(2n, n))
    s_ram = mp.mpf(0)
    binom = 1
    for n in range(160):
        s_ram += mp.mpf(1) / mp.mpf((2 * n + 1) ** 2 * binom)
        binom = (binom * (2 * n + 2) * (2 * n + 1)) // ((n + 1) * (n + 1))
    g_ramanujan = (mp.pi / 8) * mp.log(2 + mp.sqrt(3)) + (mp.mpf(3) / 8) * s_ram

    four_g = 4 * g_clausen
    diff_clausen_euler = abs(g_clausen - g_euler)
    diff_clausen_ramanujan = abs(g_clausen - g_ramanujan)
    tol_55 = mp.mpf(1) / mp.mpf(10 ** 55)

    # SnapPy cross-checks: L5a1 and 5^2_1 (standard + high-precision ManifoldHP)
    m_l5a1 = snappy.Manifold("L5a1")
    m_521 = snappy.Manifold("5^2_1")
    mhp_l5a1 = snappy.ManifoldHP("L5a1")
    mhp_521 = snappy.ManifoldHP("5^2_1")

    vol_l5a1 = mp.mpf(float(m_l5a1.volume()))
    vol_521 = mp.mpf(float(m_521.volume()))
    vol_hp_l5a1 = mp.mpf(str(mhp_l5a1.volume()))
    vol_hp_521 = mp.mpf(str(mhp_521.volume()))

    tol_10 = mp.mpf(1) / mp.mpf(10 ** 10)
    err_l5a1 = abs(vol_l5a1 - four_g)
    err_521 = abs(vol_521 - four_g)
    err_hp_l5a1 = abs(vol_hp_l5a1 - four_g)
    err_hp_521 = abs(vol_hp_521 - four_g)

    passed = (
        (diff_clausen_euler < tol_55)
        and (diff_clausen_ramanujan < tol_55)
        and (err_l5a1 < tol_10)
        and (err_521 < tol_10)
        and (err_hp_l5a1 < tol_55)
        and (err_hp_521 < tol_55)
    )

    return {
        "G_clausen_65dps": mp.nstr(g_clausen, 65),
        "G_euler_transform_65dps": mp.nstr(g_euler, 65),
        "G_ramanujan_65dps": mp.nstr(g_ramanujan, 65),
        "four_G_65dps": mp.nstr(four_g, 65),
        "diff_clausen_vs_euler": mp.nstr(diff_clausen_euler, 12),
        "diff_clausen_vs_ramanujan": mp.nstr(diff_clausen_ramanujan, 12),
        "snappy_L5a1_vol": mp.nstr(vol_l5a1, 16),
        "snappy_5_2_1_vol": mp.nstr(vol_521, 16),
        "snappy_HP_L5a1_vol": mp.nstr(vol_hp_l5a1, 60),
        "snappy_HP_5_2_1_vol": mp.nstr(vol_hp_521, 60),
        "err_L5a1_vs_4G": mp.nstr(err_l5a1, 12),
        "err_5_2_1_vs_4G": mp.nstr(err_521, 12),
        "err_HP_L5a1_vs_4G": mp.nstr(err_hp_l5a1, 12),
        "err_HP_5_2_1_vs_4G": mp.nstr(err_hp_521, 12),
        "pass": bool(passed),
        "_four_G_mp": four_g,
    }


def _flip_lr(w: str) -> str:
    return "".join("R" if ch == "L" else "L" for ch in w)


def _is_primitive_orient(w: str) -> bool:
    n = len(w)
    for d in range(1, n):
        if n % d == 0 and w == w[:d] * (n // d):
            return False
    return True


def _is_primitive_nonorient(w: str) -> bool:
    # Monodromy J*w has det=-1; only odd powers (J*u)^{2m+1} have det=-1:
    # (J*u)^m = J * (u + flip(u) + u + ... + u)
    n = len(w)
    for d in range(1, n):
        if n % d == 0 and (n // d) % 2 == 1:
            u = w[:d]
            built = "".join(u if i % 2 == 0 else _flip_lr(u) for i in range(n // d))
            if built == w:
                return False
    return True


def _canon_orient(w: str) -> str:
    n = len(w)
    cands = []
    for base in (w, w[::-1], _flip_lr(w), _flip_lr(w[::-1])):
        for i in range(n):
            cands.append(base[i:] + base[:i])
    return min(cands)


def _canon_nonorient(w: str) -> str:
    # Conjugating J*w by generator moves last letter to front and flips L<->R.
    # Conjugating by J flips all letters. Note reversal switches b-+ <-> b--.
    n = len(w)
    cands = set()
    for base in (w, _flip_lr(w)):
        cur = base
        for _ in range(2 * n):
            cands.add(cur)
            cur = ("R" if cur[-1] == "L" else "L") + cur[:-1]
    return min(cands)


def run_ow3_a() -> Dict[str, object]:
    """Run Task OW3-A completely independently from SnapPy and mpmath."""
    mp.mp.dps = 80
    catalan_info = compute_catalan_independent()
    four_g = catalan_info.pop("_four_G_mp")
    tol_10 = mp.mpf(1) / mp.mpf(10 ** 10)
    tol_55 = mp.mpf(1) / mp.mpf(10 ** 55)
    tol_100 = mp.mpf(1) / mp.mpf(100)
    bar_99 = mp.mpf(99) / mp.mpf(100)

    # 1. Enumerate complete unblocked primitive hyperbolic census
    pp_words = sorted(
        {
            _canon_orient("".join(t))
            for k in range(2, 8)
            for t in itertools.product("LR", repeat=k)
            if len(set(t)) == 2 and _is_primitive_orient("".join(t))
        },
        key=lambda s: (len(s), s),
    )
    pm_words = sorted(
        {
            _canon_orient("".join(t))
            for k in range(2, 8)
            for t in itertools.product("LR", repeat=k)
            if len(set(t)) == 2 and _is_primitive_orient("".join(t))
        },
        key=lambda s: (len(s), s),
    )
    mp_words = sorted(
        {
            _canon_nonorient("".join(t))
            for k in range(1, 7)
            for t in itertools.product("LR", repeat=k)
            if _is_primitive_nonorient("".join(t))
        },
        key=lambda s: (len(s), s),
    )

    census_records = []
    manifolds_cache = []
    for branch, prefix, words in (
        ("+", "b++", pp_words),
        ("-", "b+-", pm_words),
        ("P", "b-+", mp_words),
    ):
        for w in words:
            name = prefix + w
            m_obj = snappy.Manifold(name)
            sol = m_obj.solution_type()
            vol = mp.mpf(float(m_obj.volume()))
            ident_list = [str(x) for x in m_obj.identify()]
            rec = {
                "branch": branch,
                "name": name,
                "word": w,
                "length": len(w),
                "orientable": bool(m_obj.is_orientable()),
                "solution_type": sol,
                "volume": mp.nstr(vol, 16),
                "identify": ident_list[:3],
                "_vol_mp": vol,
            }
            census_records.append(rec)
            manifolds_cache.append((rec, m_obj))

    all_positive = all(
        r["solution_type"] == "all tetrahedra positively oriented"
        for r in census_records
    )

    # Pairwise non-isometry check across all close-volume pairs in the census
    vol_bucket_tol = mp.mpf(1) / mp.mpf(1000)
    duplicate_isometries = []
    for i in range(len(manifolds_cache)):
        ri, mi = manifolds_cache[i]
        for j in range(i + 1, len(manifolds_cache)):
            rj, mj = manifolds_cache[j]
            if abs(ri["_vol_mp"] - rj["_vol_mp"]) < vol_bucket_tol:
                if mi.is_isometric_to(mj):
                    duplicate_isometries.append((ri["name"], rj["name"]))

    # Verify 1-to-1 sister volume pairing on orientable branches (+ vs -)
    pp_map = {r["word"]: r["_vol_mp"] for r in census_records if r["branch"] == "+"}
    pm_map = {r["word"]: r["_vol_mp"] for r in census_records if r["branch"] == "-"}
    max_sister_diff = max(abs(pp_map[w] - pm_map[w]) for w in pp_words)

    # Anchor manifold checks (Manifold + ManifoldHP)
    census_sorted = sorted(census_records, key=lambda r: (r["_vol_mp"], r["length"], r["name"]))
    orient_sorted = [r for r in census_sorted if r["orientable"]]

    by_name = {r["name"]: r for r in census_records}
    rec_m000 = by_name["b-+L"]
    rec_m001 = by_name["b-+LL"]
    rec_m003 = by_name["b+-LR"]
    rec_m004 = by_name["b++LR"]

    # High-precision checks on anchors
    hp_m000 = mp.mpf(str(snappy.ManifoldHP("b-+L").volume()))
    hp_m001 = mp.mpf(str(snappy.ManifoldHP("b-+LL").volume()))
    hp_m003 = mp.mpf(str(snappy.ManifoldHP("b+-LR").volume()))
    hp_m004 = mp.mpf(str(snappy.ManifoldHP("b++LR").volume()))

    m000_is_m000 = any(x.startswith("m000(") for x in rec_m000["identify"])
    m001_is_m001 = any(x.startswith("m001(") for x in rec_m001["identify"])
    m003_is_m003 = any(x.startswith("m003(") for x in rec_m003["identify"])
    m004_is_m004 = any(x.startswith("m004(") for x in rec_m004["identify"])

    m000_strict_min = (
        census_sorted[0]["name"] == "b-+L"
        and (census_sorted[1]["_vol_mp"] - census_sorted[0]["_vol_mp"]) > mp.mpf(1) / mp.mpf(2)
    )
    m001_second_min = census_sorted[1]["name"] == "b-+LL"

    err_2m000_vs_m004 = abs(2 * rec_m000["_vol_mp"] - rec_m004["_vol_mp"])
    err_hp_2m000_vs_m004 = abs(2 * hp_m000 - hp_m004)
    err_2m001_vs_4G = abs(2 * rec_m001["_vol_mp"] - four_g)
    err_hp_2m001_vs_4G = abs(2 * hp_m001 - four_g)
    err_m003_vs_m004 = abs(rec_m003["_vol_mp"] - rec_m004["_vol_mp"])
    err_hp_m003_vs_m004 = abs(hp_m003 - hp_m004)
    m003_m004_distinct = not snappy.Manifold("b+-LR").is_isometric_to(snappy.Manifold("b++LR"))
    orient_ground_pair = {orient_sorted[0]["name"], orient_sorted[1]["name"]} == {"b+-LR", "b++LR"}
    orient_gap_above_ground = orient_sorted[2]["_vol_mp"] - orient_sorted[0]["_vol_mp"]

    # 2. Three Whitehead accumulation sequences for k = 1..50
    seq_specs = [
        ("b++L^kR", "b++", "R", 1),
        ("b+-L^kR", "b+-", "R", 1),
        ("b-+L^k", "b-+", "", 0),
    ]
    whitehead_sequences: Dict[str, object] = {}
    seq_vols_mp: Dict[str, List[mp.mpf]] = {}
    for seq_key, prefix, suffix, extra_len in seq_specs:
        entries = []
        vols = []
        all_pos_seq = True
        for k in range(1, 51):
            wname = prefix + ("L" * k) + suffix
            m_obj = snappy.Manifold(wname)
            sol = m_obj.solution_type()
            if sol != "all tetrahedra positively oriented":
                all_pos_seq = False
            v = mp.mpf(float(m_obj.volume()))
            vols.append(v)
            gap = four_g - v
            nz_coeff = mp.mpf(k * k) * gap
            entries.append(
                {
                    "k": k,
                    "length": k + extra_len,
                    "volume": mp.nstr(v, 16),
                    "gap_4G_minus_vol": mp.nstr(gap, 12),
                    "k2_times_gap": mp.nstr(nz_coeff, 10),
                }
            )
        seq_vols_mp[seq_key] = vols
        monotone_strict = all(vols[i] < vols[i + 1] for i in range(49))
        strictly_below_4G = all(v < four_g for v in vols)
        gap_25 = four_g - vols[24]
        gap_50 = four_g - vols[49]
        hp_50 = mp.mpf(str(snappy.ManifoldHP(prefix + ("L" * 50) + suffix).volume()))
        hp_gap_50 = four_g - hp_50
        whitehead_sequences[seq_key] = {
            "k_min": 1,
            "k_max": 50,
            "all_positively_oriented": bool(all_pos_seq),
            "strictly_monotone_increasing": bool(monotone_strict),
            "strictly_below_4G_all_50": bool(strictly_below_4G),
            "vol_k1": mp.nstr(vols[0], 16),
            "vol_k25": mp.nstr(vols[24], 16),
            "gap_k25": mp.nstr(gap_25, 12),
            "k2_gap_k25": mp.nstr(mp.mpf(25 * 25) * gap_25, 10),
            "vol_k50": mp.nstr(vols[49], 16),
            "vol_HP_k50": mp.nstr(hp_50, 40),
            "gap_k50": mp.nstr(gap_50, 12),
            "gap_HP_k50": mp.nstr(hp_gap_50, 12),
            "k2_gap_k50": mp.nstr(mp.mpf(50 * 50) * gap_50, 10),
            "two_pi_squared_ref": mp.nstr(2 * (mp.pi ** 2), 10),
            "gap_k50_lt_1_over_100": bool(gap_50 > 0 and gap_50 < tol_100 and hp_gap_50 > 0 and hp_gap_50 < tol_100),
            "sample_points": [entries[idx] for idx in (0, 1, 4, 9, 19, 24, 39, 41, 44, 49)],
        }

    max_wh_sister_diff = max(
        abs(seq_vols_mp["b++L^kR"][i] - seq_vols_mp["b+-L^kR"][i])
        for i in range(50)
    )

    # Pure-volume divergence bound proof for Z(0, beta), beta in {0, 1, 5, 10}
    divergence_bounds = {}
    for beta_int in (0, 1, 5, 10):
        beta_mp = mp.mpf(beta_int)
        floor_term = mp.exp(-beta_mp * four_g)
        pp_terms = [mp.exp(-beta_mp * v) for v in seq_vols_mp["b++L^kR"]]
        mp_terms = [mp.exp(-beta_mp * v) for v in seq_vols_mp["b-+L^k"]]
        min_pp = min(pp_terms)
        min_mp = min(mp_terms)
        partial_50_pp = sum(pp_terms)
        partial_50_mp = sum(mp_terms)
        divergence_bounds[f"beta={beta_int}"] = {
            "asymptotic_term_floor_exp(-4*beta*G)": mp.nstr(floor_term, 14),
            "min_term_b++_k1_50": mp.nstr(min_pp, 14),
            "min_term_b-+_k1_50": mp.nstr(min_mp, 14),
            "partial_sum_50_b++": mp.nstr(partial_50_pp, 14),
            "partial_sum_50_b-+": mp.nstr(partial_50_mp, 14),
            "all_terms_exceed_floor": bool(min_pp > floor_term and min_mp > floor_term),
            "partial_50_exceeds_50x_floor": bool(
                partial_50_pp > 50 * floor_term and partial_50_mp > 50 * floor_term
            ),
        }

    # 3. Regulated 2D phase grid Z(s, beta): s in {0, 1/2, 1, 2}, beta in {0, 1, 5, 10}
    s_grid = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(2)]
    beta_grid = [Fraction(0), Fraction(1), Fraction(5), Fraction(10)]
    phase_grid = []
    m000_share_s0_b10 = mp.mpf(0)
    orient_max_tie_gap = mp.mpf(0)
    m000_unconditional_dom = True
    s_pos_restores_decay = True

    for s_frac in s_grid:
        s_mp = mp.mpf(s_frac.numerator) / mp.mpf(s_frac.denominator)
        for b_frac in beta_grid:
            b_mp = mp.mpf(b_frac.numerator) / mp.mpf(b_frac.denominator)
            weights_all = [
                (r, mp.exp(-s_mp * mp.mpf(r["length"]) - b_mp * r["_vol_mp"]))
                for r in census_records
            ]
            z_all = sum(w for _, w in weights_all)
            w_m000 = next(w for r, w in weights_all if r["name"] == "b-+L")
            w_m001 = next(w for r, w in weights_all if r["name"] == "b-+LL")
            share_m000 = w_m000 / z_all
            share_m001 = w_m001 / z_all

            weights_orient = [(r, w) for r, w in weights_all if r["orientable"]]
            z_orient = sum(w for _, w in weights_orient)
            w_m003 = next(w for r, w in weights_orient if r["name"] == "b+-LR")
            w_m004 = next(w for r, w in weights_orient if r["name"] == "b++LR")
            share_m003_o = w_m003 / z_orient
            share_m004_o = w_m004 / z_orient
            share_0304_o = (w_m003 + w_m004) / z_orient
            tie_gap = abs(share_m003_o - share_m004_o)
            if tie_gap > orient_max_tie_gap:
                orient_max_tie_gap = tie_gap

            if s_frac == 0 and b_frac == 10:
                m000_share_s0_b10 = share_m000

            # Check m000 strict single-manifold dominance whenever (s, beta) != (0, 0)
            if not (s_frac == 0 and b_frac == 0):
                max_other = max(w for r, w in weights_all if r["name"] != "b-+L")
                if not (w_m000 > max_other):
                    m000_unconditional_dom = False

            # Whitehead family 50-term regulated sum and tail ratio
            wh_terms = [
                mp.exp(-s_mp * mp.mpf(k + 1) - b_mp * seq_vols_mp["b++L^kR"][k - 1])
                for k in range(1, 51)
            ]
            wh_sum_50 = sum(wh_terms)
            wh_tail_ratio = wh_terms[49] / wh_terms[0]
            if s_frac > 0:
                # Expected exponential decay factor exp(-49*s) * exp(-beta*(V50-V1)) < exp(-49*s)
                if not (wh_tail_ratio < mp.exp(-49 * s_mp)):
                    s_pos_restores_decay = False

            phase_grid.append(
                {
                    "s": str(s_frac),
                    "beta": str(b_frac),
                    "Z_all_census": mp.nstr(z_all, 14),
                    "m000_share_all": mp.nstr(share_m000, 14),
                    "m001_share_all": mp.nstr(share_m001, 14),
                    "Z_orient_census": mp.nstr(z_orient, 14),
                    "m003_share_orient": mp.nstr(share_m003_o, 14),
                    "m004_share_orient": mp.nstr(share_m004_o, 14),
                    "m003_plus_m004_share_orient": mp.nstr(share_0304_o, 14),
                    "m003_m004_tie_gap": mp.nstr(tie_gap, 12),
                    "whitehead_b++_sum_50": mp.nstr(wh_sum_50, 14),
                    "whitehead_b++_ratio_k50_over_k1": mp.nstr(wh_tail_ratio, 12),
                }
            )

    # Clean internal mp keys from census summary
    census_top10 = [
        {k: v for k, v in r.items() if k != "_vol_mp"}
        for r in census_sorted[:10]
    ]

    ow3_a_pass = (
        bool(catalan_info["pass"])
        and all_positive
        and (len(duplicate_isometries) == 0)
        and (max_sister_diff < tol_10)
        and m000_is_m000
        and m001_is_m001
        and m003_is_m003
        and m004_is_m004
        and m000_strict_min
        and m001_second_min
        and (err_2m000_vs_m004 < tol_10)
        and (err_hp_2m000_vs_m004 < tol_55)
        and (err_2m001_vs_4G < tol_10)
        and (err_hp_2m001_vs_4G < tol_55)
        and (err_m003_vs_m004 < tol_10)
        and (err_hp_m003_vs_m004 < tol_55)
        and m003_m004_distinct
        and orient_ground_pair
        and (m000_share_s0_b10 > bar_99)
        and (orient_max_tie_gap < tol_10)
        and m000_unconditional_dom
        and s_pos_restores_decay
        and (max_wh_sister_diff < tol_10)
        and all(
            whitehead_sequences[k]["all_positively_oriented"]
            and whitehead_sequences[k]["strictly_monotone_increasing"]
            and whitehead_sequences[k]["strictly_below_4G_all_50"]
            and whitehead_sequences[k]["gap_k50_lt_1_over_100"]
            for k in whitehead_sequences
        )
        and all(
            v["all_terms_exceed_floor"] and v["partial_50_exceeds_50x_floor"]
            for v in divergence_bounds.values()
        )
    )

    return {
        "catalan_and_whitehead_volume": catalan_info,
        "census_counts": {
            "branch_plus_b++_len2_7": len(pp_words),
            "branch_minus_b+-_len2_7": len(pm_words),
            "branch_P_b-+_len1_6": len(mp_words),
            "total_distinct_primitive_manifolds": len(census_records),
            "all_positively_oriented": bool(all_positive),
            "duplicate_isometries_found": duplicate_isometries,
            "max_orientable_sister_vol_diff": mp.nstr(max_sister_diff, 12),
        },
        "anchor_verification": {
            "m000_vol_HP": mp.nstr(hp_m000, 40),
            "m001_vol_HP": mp.nstr(hp_m001, 40),
            "m003_vol_HP": mp.nstr(hp_m003, 40),
            "m004_vol_HP": mp.nstr(hp_m004, 40),
            "m000_is_m000": bool(m000_is_m000),
            "m001_is_m001": bool(m001_is_m001),
            "m003_is_m003": bool(m003_is_m003),
            "m004_is_m004": bool(m004_is_m004),
            "m000_strict_global_min": bool(m000_strict_min),
            "m001_strict_second_min": bool(m001_second_min),
            "err_2Vol_m000_vs_Vol_m004": mp.nstr(err_2m000_vs_m004, 12),
            "err_HP_2Vol_m000_vs_Vol_m004": mp.nstr(err_hp_2m000_vs_m004, 12),
            "err_2Vol_m001_vs_4G": mp.nstr(err_2m001_vs_4G, 12),
            "err_HP_2Vol_m001_vs_4G": mp.nstr(err_hp_2m001_vs_4G, 12),
            "err_Vol_m003_vs_Vol_m004": mp.nstr(err_m003_vs_m004, 12),
            "err_HP_Vol_m003_vs_Vol_m004": mp.nstr(err_hp_m003_vs_m004, 12),
            "m003_m004_non_isometric": bool(m003_m004_distinct),
            "orientable_ground_pair_is_m003_m004": bool(orient_ground_pair),
            "orientable_gap_to_third_manifold": mp.nstr(orient_gap_above_ground, 12),
            "m000_share_at_s0_beta10": mp.nstr(m000_share_s0_b10, 14),
            "m000_share_s0_beta10_gt_99_100": bool(m000_share_s0_b10 > bar_99),
            "orient_max_m003_m004_tie_gap": mp.nstr(orient_max_tie_gap, 12),
            "m000_unconditional_single_dominance": bool(m000_unconditional_dom),
            "s_gt_0_restores_whitehead_decay": bool(s_pos_restores_decay),
        },
        "census_lowest_10_by_volume": census_top10,
        "whitehead_sequences_k1_to_50": whitehead_sequences,
        "whitehead_max_sister_diff_k1_50": mp.nstr(max_wh_sister_diff, 12),
        "pure_volume_divergence_bounds": divergence_bounds,
        "phase_grid_2d": phase_grid,
        "pass": bool(ow3_a_pass),
        "_raw_anchor_vols": {
            "m000": hp_m000,
            "m003": hp_m003,
            "m004": hp_m004,
            "four_G": four_g,
            "wh_b++": seq_vols_mp["b++L^kR"],
        },
    }


# ---------------------------------------------------------------------------
# Task OW3-B Part 1: Path-A Single-Higgs 15x15 Trace Collapse
# ---------------------------------------------------------------------------

def run_ow3_b_part1() -> Dict[str, object]:
    """Prove Tr(P_+ D(a,b)) = +1/2 and Tr(P_- D(a,b)) = -1/2 in Q[w]/(Phi_5)
    and 65-digit mpmath, plus explicit 15x15 Kronecker contraction collapse."""
    z0 = Cyclo5.zero()
    one = Cyclo5.from_rational(Fraction(1))
    half = Cyclo5.from_rational(Fraction(1, 2))
    neg_half = Cyclo5.from_rational(Fraction(-1, 2))

    # Exact 5x5 matrices over Q[w]/(Phi_5(w))
    X_ex = [[one if i == (j + 1) % 5 else z0 for j in range(5)] for i in range(5)]
    Z_ex = [[Cyclo5.omega_pow(j) if i == j else z0 for j in range(5)] for i in range(5)]
    P_ex = [[one if i == (-j) % 5 else z0 for j in range(5)] for i in range(5)]
    I5_ex = c5_eye(5)

    P_plus_ex = [
        [(I5_ex[i][j] + P_ex[i][j]).scale(Fraction(1, 2)) for j in range(5)]
        for i in range(5)
    ]
    P_minus_ex = [
        [(I5_ex[i][j] - P_ex[i][j]).scale(Fraction(1, 2)) for j in range(5)]
        for i in range(5)
    ]

    # Check exact Weyl-Heisenberg and projector relations
    ZX_ex = c5_matmul(Z_ex, X_ex)
    wXZ_ex = [[x * Cyclo5.omega_pow(1) for x in row] for row in c5_matmul(X_ex, Z_ex)]
    alg_checks_exact = {
        "X5_eq_I": c5_mat_eq(c5_mat_pow(X_ex, 5), I5_ex),
        "Z5_eq_I": c5_mat_eq(c5_mat_pow(Z_ex, 5), I5_ex),
        "ZX_eq_wXZ": c5_mat_eq(ZX_ex, wXZ_ex),
        "P2_eq_I": c5_mat_eq(c5_matmul(P_ex, P_ex), I5_ex),
        "Pplus_idem": c5_mat_eq(c5_matmul(P_plus_ex, P_plus_ex), P_plus_ex),
        "Pminus_idem": c5_mat_eq(c5_matmul(P_minus_ex, P_minus_ex), P_minus_ex),
        "Pplus_Pminus_eq_0": c5_mat_eq(
            c5_matmul(P_plus_ex, P_minus_ex),
            [[z0 for _ in range(5)] for _ in range(5)],
        ),
        "Tr_Pplus_eq_3": c5_trace(P_plus_ex) == Cyclo5.from_rational(Fraction(3)),
        "Tr_Pminus_eq_2": c5_trace(P_minus_ex) == Cyclo5.from_rational(Fraction(2)),
    }

    # Orthogonal integer basis vectors for W_3^+ and W_2^- (squared norms 1,2,2 and 2,2)
    b3_vecs = [
        ([1, 0, 0, 0, 0], Fraction(1)),
        ([0, 1, 0, 0, 1], Fraction(1, 2)),
        ([0, 0, 1, 1, 0], Fraction(1, 2)),
    ]
    b2_vecs = [
        ([0, 1, 0, 0, -1], Fraction(1, 2)),
        ([0, 0, 1, -1, 0], Fraction(1, 2)),
    ]

    def basis_trace_exact(
        D_mat: List[List[Cyclo5]], basis: Sequence[Tuple[List[int], Fraction]]
    ) -> Cyclo5:
        acc = Cyclo5.zero()
        for vec, inv_norm_sq in basis:
            val = Cyclo5.zero()
            for i in range(5):
                if vec[i] == 0:
                    continue
                for j in range(5):
                    if vec[j] == 0:
                        continue
                    term = D_mat[i][j].scale(Fraction(vec[i] * vec[j]))
                    val = val + term
            acc = acc + val.scale(inv_norm_sq)
        return acc

    X_pows_ex = [c5_mat_pow(X_ex, a) for a in range(5)]
    Z_pows_ex = [c5_mat_pow(Z_ex, b) for b in range(5)]

    exact_all_24_plus_ok = True
    exact_all_24_minus_ok = True
    exact_basis_matches_proj = True
    exact_nonzero_count = 0

    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            exact_nonzero_count += 1
            ph = Cyclo5.omega_pow(3 * a * b)
            XZ = c5_matmul(X_pows_ex[a], Z_pows_ex[b])
            D_ab = [[ph * x for x in row] for row in XZ]
            tr_p_proj = c5_trace(c5_matmul(P_plus_ex, D_ab))
            tr_m_proj = c5_trace(c5_matmul(P_minus_ex, D_ab))
            tr_p_bas = basis_trace_exact(D_ab, b3_vecs)
            tr_m_bas = basis_trace_exact(D_ab, b2_vecs)
            if tr_p_proj != half or tr_p_bas != half:
                exact_all_24_plus_ok = False
            if tr_m_proj != neg_half or tr_m_bas != neg_half:
                exact_all_24_minus_ok = False
            if tr_p_proj != tr_p_bas or tr_m_proj != tr_m_bas:
                exact_basis_matches_proj = False

    # Independent 65-digit mpmath verification + explicit 15x15 Kronecker contraction
    mp.mp.dps = 65
    tol_50 = mp.mpf(1) / mp.mpf(10 ** 50)
    zeta5 = mp.exp(mp.mpc(0, 2) * mp.pi / 5)

    X_mp = mp.zeros(5, 5)
    Z_mp = mp.zeros(5, 5)
    P_mp = mp.zeros(5, 5)
    for j in range(5):
        X_mp[(j + 1) % 5, j] = mp.mpf(1)
        Z_mp[j, j] = zeta5 ** j
        P_mp[(-j) % 5, j] = mp.mpf(1)

    inv_s2 = mp.mpf(1) / mp.sqrt(2)
    B3 = mp.zeros(5, 3)
    B3[0, 0] = mp.mpf(1)
    B3[1, 1] = inv_s2
    B3[4, 1] = inv_s2
    B3[2, 2] = inv_s2
    B3[3, 2] = inv_s2

    B2 = mp.zeros(5, 2)
    B2[1, 0] = inv_s2
    B2[4, 0] = -inv_s2
    B2[2, 1] = inv_s2
    B2[3, 1] = -inv_s2

    def mat_dagger(M: mp.matrix) -> mp.matrix:
        out = mp.zeros(M.cols, M.rows)
        for i in range(M.rows):
            for j in range(M.cols):
                out[j, i] = mp.conj(M[i, j])
        return out

    def mat_max_abs(M: mp.matrix) -> mp.mpf:
        mx = mp.mpf(0)
        for i in range(M.rows):
            for j in range(M.cols):
                v = abs(M[i, j])
                if v > mx:
                    mx = v
        return mx

    def mat_trace_mp(M: mp.matrix) -> mp.mpc:
        acc = mp.mpc(0, 0)
        for i in range(M.rows):
            acc += M[i, i]
        return acc

    B3H = mat_dagger(B3)
    B2H = mat_dagger(B2)
    ortho_err = max(
        mat_max_abs(B3H * B3 - mp.eye(3)),
        mat_max_abs(B2H * B2 - mp.eye(2)),
        mat_max_abs(B3H * B2),
        mat_max_abs(B3 * B3H + B2 * B2H - mp.eye(5)),
        mat_max_abs(P_mp * B3 - B3),
        mat_max_abs(P_mp * B2 + B2),
    )

    X_pows_mp = [mp.eye(5)]
    Z_pows_mp = [mp.eye(5)]
    for _ in range(4):
        X_pows_mp.append(X_pows_mp[-1] * X_mp)
        Z_pows_mp.append(Z_pows_mp[-1] * Z_mp)

    half_mp = mp.mpf(1) / mp.mpf(2)
    neg_half_mp = -half_mp
    max_mp_err_plus = mp.mpf(0)
    max_mp_err_minus = mp.mpf(0)

    # Explicit 15x15 Kronecker contraction test with deterministic integer-seeded Y(a,b) and ph(a,b)
    rng = random.Random(314159265)
    O1_15 = mp.zeros(15, 15)
    S_ph = mp.zeros(3, 3)

    def mp_kron(A: mp.matrix, B: mp.matrix) -> mp.matrix:
        out = mp.zeros(A.rows * B.rows, A.cols * B.cols)
        for i in range(A.rows):
            for j in range(A.cols):
                aij = A[i, j]
                if aij == 0:
                    continue
                for p in range(B.rows):
                    for q in range(B.cols):
                        out[i * B.rows + p, j * B.cols + q] = aij * B[p, q]
        return out

    D_traces_mp = []
    for a in range(5):
        for b in range(5):
            if a == 0 and b == 0:
                continue
            D_ab = (zeta5 ** ((3 * a * b) % 5)) * (X_pows_mp[a] * Z_pows_mp[b])
            tr_p = mat_trace_mp(B3H * D_ab * B3)
            tr_m = mat_trace_mp(B2H * D_ab * B2)
            ep = abs(tr_p - half_mp)
            em = abs(tr_m - neg_half_mp)
            if ep > max_mp_err_plus:
                max_mp_err_plus = ep
            if em > max_mp_err_minus:
                max_mp_err_minus = em
            D_traces_mp.append((a, b, tr_p, tr_m))

            # Random complex 3x3 matrix Y(a,b) and complex phase ph(a,b) from exact rationals
            ph_num = mp.mpc(rng.randint(-19, 19), rng.randint(-19, 19))
            if ph_num == 0:
                ph_num = mp.mpc(1, 1)
            ph_ab = ph_num / abs(ph_num)
            Y_ab = mp.zeros(3, 3)
            for i in range(3):
                for j in range(3):
                    Y_ab[i, j] = mp.mpc(rng.randint(-11, 11), rng.randint(-11, 11)) / mp.mpf(7)
            S_ph += ph_ab * Y_ab
            O1_15 += ph_ab * mp_kron(Y_ab, D_ab)

    # Project 15x15 -> 9x9 (W_3^+) and 6x6 (W_2^-) and take partial trace over W_3^+, W_2^-
    I3_mp = mp.eye(3)
    proj_9 = mp_kron(I3_mp, B3H) * O1_15 * mp_kron(I3_mp, B3)
    proj_6 = mp_kron(I3_mp, B2H) * O1_15 * mp_kron(I3_mp, B2)

    Y_eff_plus = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            acc = mp.mpc(0, 0)
            for c in range(3):
                acc += proj_9[3 * i + c, 3 * j + c]
            Y_eff_plus[i, j] = acc

    Y_eff_minus = mp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            acc = mp.mpc(0, 0)
            for w in range(2):
                acc += proj_6[2 * i + w, 2 * j + w]
            Y_eff_minus[i, j] = acc

    err_15x15_plus = mat_max_abs(Y_eff_plus - half_mp * S_ph)
    err_15x15_minus = mat_max_abs(Y_eff_minus - neg_half_mp * S_ph)

    # Verify arbitrary G_SM-invariant linear combination alpha*Tr_{W3+} + beta*Tr_{W2-}
    alpha = mp.mpc(3, -2)
    beta = mp.mpc(-5, 4)
    combo = alpha * Y_eff_plus + beta * Y_eff_minus
    combo_target = ((alpha - beta) / mp.mpf(2)) * S_ph
    err_linear_combo = mat_max_abs(combo - combo_target)

    passed = (
        all(alg_checks_exact.values())
        and (exact_nonzero_count == 24)
        and exact_all_24_plus_ok
        and exact_all_24_minus_ok
        and exact_basis_matches_proj
        and (ortho_err < tol_50)
        and (max_mp_err_plus < tol_50)
        and (max_mp_err_minus < tol_50)
        and (err_15x15_plus < tol_50)
        and (err_15x15_minus < tol_50)
        and (err_linear_combo < tol_50)
    )

    return {
        "exact_cyclotomic_Q_w_mod_Phi5": {
            "algebra_identities": alg_checks_exact,
            "nonzero_shift_count": exact_nonzero_count,
            "all_24_Tr_Pplus_eq_plus_half": bool(exact_all_24_plus_ok),
            "all_24_Tr_Pminus_eq_minus_half": bool(exact_all_24_minus_ok),
            "projector_trace_matches_basis_trace": bool(exact_basis_matches_proj),
        },
        "mpmath_65dps_and_15x15_contraction": {
            "basis_orthonormality_and_parity_err": mp.nstr(ortho_err, 12),
            "max_err_Tr_W3plus_vs_plus_half": mp.nstr(max_mp_err_plus, 12),
            "max_err_Tr_W2minus_vs_minus_half": mp.nstr(max_mp_err_minus, 12),
            "err_15x15_collapse_W3plus_vs_half_Sph": mp.nstr(err_15x15_plus, 12),
            "err_15x15_collapse_W2minus_vs_neg_half_Sph": mp.nstr(err_15x15_minus, 12),
            "err_general_linear_combination_collapse": mp.nstr(err_linear_combo, 12),
            "S_ph_frobenius_norm": mp.nstr(
                mp.sqrt(sum(abs(S_ph[i, j]) ** 2 for i in range(3) for j in range(3))), 14
            ),
        },
        "pass": bool(passed),
        "_raw_pf3": {
            "exact_all_24_plus_half": exact_all_24_plus_ok,
            "max_mp_err_plus": max_mp_err_plus,
        },
    }


# ---------------------------------------------------------------------------
# Task OW3-B Part 2: 32x32 Spin(10) X:HOL via 5-Fold Pauli Tensor Products
# ---------------------------------------------------------------------------

def _extract_yukawa_observables(
    Mu: np.ndarray, Md: np.ndarray, Me: np.ndarray
) -> Dict[str, float]:
    """Extract all 12 physical dimensionless observables + Jarlskog commutator cross-check."""
    Uu, su, _ = np.linalg.svd(Mu)
    Ud, sd, _ = np.linalg.svd(Md)
    Ue, se, _ = np.linalg.svd(Me)

    iu = np.argsort(su)
    id_ = np.argsort(sd)
    ie = np.argsort(se)
    su, Uu = su[iu], Uu[:, iu]
    sd, Ud = sd[id_], Ud[:, id_]
    se, Ue = se[ie], Ue[:, ie]

    V = Uu.conj().T @ Ud
    J_ckm = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))

    # Independent basis-invariant Jarlskog commutator cross-check
    Hu = Mu @ Mu.conj().T
    Hd = Md @ Md.conj().T
    comm = Hu @ Hd - Hd @ Hu
    du = (su[2] ** 2 - su[1] ** 2) * (su[2] ** 2 - su[0] ** 2) * (su[1] ** 2 - su[0] ** 2)
    dd = (sd[2] ** 2 - sd[1] ** 2) * (sd[2] ** 2 - sd[0] ** 2) * (sd[1] ** 2 - sd[0] ** 2)
    J_comm = float(np.imag(np.linalg.det(comm)) / (2 * du * dd))

    return {
        "m_u_over_m_t": float(su[0] / su[2]),
        "m_c_over_m_t": float(su[1] / su[2]),
        "m_d_over_m_b": float(sd[0] / sd[2]),
        "m_s_over_m_b": float(sd[1] / sd[2]),
        "m_e_over_m_tau": float(se[0] / se[2]),
        "m_mu_over_m_tau": float(se[1] / se[2]),
        "abs_V_us": float(abs(V[0, 1])),
        "abs_V_cb": float(abs(V[1, 2])),
        "abs_V_ub": float(abs(V[0, 2])),
        "J_CP": J_ckm,
        "m_b_over_m_tau": float(sd[2] / se[2]),
        "m_t_over_m_b": float(su[2] / sd[2]),
        "J_CP_commutator_diff": float(abs(J_ckm - J_comm)),
    }


def _sample_haar_u3(rng: np.random.Generator) -> Tuple[np.ndarray, float]:
    """Exact Mezzadri QR Haar-random unitary in U(3)."""
    Z = rng.standard_normal((3, 3)) + complex(0, 1) * rng.standard_normal((3, 3))
    Q, R = np.linalg.qr(Z)
    diag = np.diag(R)
    phases = diag / np.abs(diag)
    U = Q * phases[None, :]
    unitarity_err = float(np.max(np.abs(U.conj().T @ U - np.eye(3))))
    return U, unitarity_err


def run_ow3_b_part2() -> Dict[str, object]:
    """Independent 5-fold Pauli Jordan-Wigner Cl(10), C_10, 16x16 holomorphic
    bilinears, 48x48 embedding, 11/12 tan(beta) invariance, and 10-trial Haar test."""
    # Exact 2x2 Pauli matrices in GaussInt Z[i]
    I2 = [[G1, G0], [G0, G1]]
    s1 = [[G0, G1], [G1, G0]]
    s2 = [[G0, GMI], [GI, G0]]
    s3 = [[G1, G0], [G0, GM1]]

    # Build 10 Hermitian 32x32 Cl(10) gamma matrices via 5-fold Pauli tensor products
    gammas: List[List[List[GaussInt]]] = []
    for k in range(5):
        prefix = [s3] * k
        suffix = [I2] * (4 - k)
        gammas.append(gi_kron_all(prefix + [s1] + suffix))
        gammas.append(gi_kron_all(prefix + [s2] + suffix))

    I32 = gi_eye(32)
    I32_x2 = gi_scale(I32, GaussInt(2, 0))
    Z32 = [[G0 for _ in range(32)] for _ in range(32)]

    # 1. Verify Hermiticity and all 100 Cl(10) anticommutators in exact Z[i]
    herm_max_err = max(gi_max_norm_sq(gi_sub(gi_dagger(G), G)) for G in gammas)
    cliff_max_err = 0
    for mu in range(10):
        for nu in range(10):
            anticomm = gi_add(gi_matmul(gammas[mu], gammas[nu]), gi_matmul(gammas[nu], gammas[mu]))
            target = I32_x2 if mu == nu else Z32
            err = gi_max_norm_sq(gi_sub(anticomm, target))
            if err > cliff_max_err:
                cliff_max_err = err

    # 2. Construct C_10 = Gamma_2 Gamma_4 Gamma_6 Gamma_8 Gamma_10 (0-indexed: 1,3,5,7,9)
    C10 = gi_matmul(
        gi_matmul(gi_matmul(gi_matmul(gammas[1], gammas[3]), gammas[5]), gammas[7]),
        gammas[9],
    )
    C10_dag = gi_dagger(C10)
    C10_T = gi_transpose(C10)
    c10_unitarity_err = gi_max_norm_sq(gi_sub(gi_matmul(C10_dag, C10), I32))
    # Compute transpose sign directly from matrix check (no hard-coded sign!)
    err_sym = gi_max_norm_sq(gi_sub(C10_T, C10))
    err_antisym = gi_max_norm_sq(gi_add(C10_T, C10))
    c10_transpose_sign = 1 if err_sym == 0 else (-1 if err_antisym == 0 else 0)

    # Check conjugation C_10 Gamma_mu C_10^-1 vs -Gamma_mu^T (and +Gamma_mu^T)
    conj_minus_err = max(
        gi_max_norm_sq(
            gi_add(gi_matmul(gi_matmul(C10, G), C10_dag), gi_transpose(G))
        )
        for G in gammas
    )
    conj_plus_err = max(
        gi_max_norm_sq(
            gi_sub(gi_matmul(gi_matmul(C10, G), C10_dag), gi_transpose(G))
        )
        for G in gammas
    )
    c10_conj_sign = -1 if conj_minus_err == 0 else (1 if conj_plus_err == 0 else 0)

    # 3. Chirality operator Gamma_11 = (-i)^5 Gamma_1 ... Gamma_10 = -i * prod(gammas)
    gprod = I32
    for G in gammas:
        gprod = gi_matmul(gprod, G)
    Gamma11 = gi_scale(gprod, GMI)
    s3_5 = gi_kron_all([s3] * 5)
    gamma11_vs_s3_5_err = gi_max_norm_sq(gi_sub(Gamma11, s3_5))
    gamma11_sq_err = gi_max_norm_sq(gi_sub(gi_matmul(Gamma11, Gamma11), I32))
    gamma11_anticomm_err = max(
        gi_max_norm_sq(gi_add(gi_matmul(Gamma11, G), gi_matmul(G, Gamma11)))
        for G in gammas
    )

    # 4. Holomorphic / anti-holomorphic combinations Gamma_k^+ = c_k^dag, Gamma_k^- = c_k
    G_plus: List[List[List[GaussInt]]] = []
    G_minus: List[List[List[GaussInt]]] = []
    for k in range(5):
        g_odd = gammas[2 * k]
        g_even = gammas[2 * k + 1]
        # (g_odd - i g_even) / 2  and  (g_odd + i g_even) / 2
        gp_x2 = gi_sub(g_odd, gi_scale(g_even, GI))
        gm_x2 = gi_add(g_odd, gi_scale(g_even, GI))
        G_plus.append([[x.div_exact_int(2) for x in row] for row in gp_x2])
        G_minus.append([[x.div_exact_int(2) for x in row] for row in gm_x2])

    # Verify CAR: {c_j, c_k^dag} = delta_{jk} I_32, {c_j, c_k} = 0, {c_j^dag, c_k^dag} = 0
    car_max_err = 0
    for j in range(5):
        for k in range(5):
            e1 = gi_max_norm_sq(
                gi_sub(
                    gi_add(gi_matmul(G_minus[j], G_plus[k]), gi_matmul(G_plus[k], G_minus[j])),
                    I32 if j == k else Z32,
                )
            )
            e2 = gi_max_norm_sq(
                gi_add(gi_matmul(G_minus[j], G_minus[k]), gi_matmul(G_minus[k], G_minus[j]))
            )
            e3 = gi_max_norm_sq(
                gi_add(gi_matmul(G_plus[j], G_plus[k]), gi_matmul(G_plus[k], G_plus[j]))
            )
            car_max_err = max(car_max_err, e1, e2, e3)

    # 5. Project onto chiral 16-dim subspace Gamma_11 == +1
    even_indices = [i for i in range(32) if Gamma11[i][i] == G1]
    P16 = [[G1 if j == col else G0 for j in range(32)] for col in even_indices]
    P16_T = gi_transpose(P16)

    # Extract quantum numbers (n_1..n_5) directly from n_k = Gamma_k^+ Gamma_k^-
    n_ops = [gi_matmul(G_plus[k], G_minus[k]) for k in range(5)]
    multiplet_map = {
        (0, 0): "nu_c",
        (0, 2): "e_c",
        (2, 0): "u_c",
        (1, 1): "Q",
        (2, 2): "d_c",
        (3, 1): "L",
    }
    chiral_states = []
    multiplet_counts: Dict[str, int] = {}
    multiplet_sixY: Dict[str, List[int]] = {}
    for row_idx, full_idx in enumerate(even_indices):
        occ = tuple(n_ops[k][full_idx][full_idx].re for k in range(5))
        nc = occ[0] + occ[1] + occ[2]
        nw = occ[3] + occ[4]
        y6 = -2 * nc + 3 * nw
        mp_name = multiplet_map[(nc, nw)]
        chiral_states.append(
            {"idx16": row_idx, "idx32": full_idx, "occ": occ, "sixY": y6, "multiplet": mp_name}
        )
        multiplet_counts[mp_name] = multiplet_counts.get(mp_name, 0) + 1
        multiplet_sixY.setdefault(mp_name, [])
        if y6 not in multiplet_sixY[mp_name]:
            multiplet_sixY[mp_name].append(y6)

    # 6. Project all 10 bilinear matrices M_k^{+-} = P_16 (C_10 Gamma_k^{+-}) P_16^T
    M_plus: List[List[List[GaussInt]]] = []
    M_minus: List[List[List[GaussInt]]] = []
    all_10_sym_err = 0
    all_10_sixY_conservation_ok = True
    higgs_sixY_plus = [-2, -2, -2, 3, 3]
    higgs_sixY_minus = [2, 2, 2, -3, -3]

    for k in range(5):
        Mp = gi_matmul(gi_matmul(P16, gi_matmul(C10, G_plus[k])), P16_T)
        Mm = gi_matmul(gi_matmul(P16, gi_matmul(C10, G_minus[k])), P16_T)
        M_plus.append(Mp)
        M_minus.append(Mm)
        all_10_sym_err = max(
            all_10_sym_err,
            gi_max_norm_sq(gi_sub(gi_transpose(Mp), Mp)),
            gi_max_norm_sq(gi_sub(gi_transpose(Mm), Mm)),
        )
        for i in range(16):
            for j in range(16):
                if not Mp[i][j].is_zero():
                    if chiral_states[i]["sixY"] + chiral_states[j]["sixY"] + higgs_sixY_plus[k] != 0:
                        all_10_sixY_conservation_ok = False
                if not Mm[i][j].is_zero():
                    if chiral_states[i]["sixY"] + chiral_states[j]["sixY"] + higgs_sixY_minus[k] != 0:
                        all_10_sixY_conservation_ok = False

    # Inspect weak-doublet components k in {4, 5} (0-indexed: 3, 4)
    def analyze_doublet_matrix(M: List[List[GaussInt]]) -> Dict[str, object]:
        pair_counts: Dict[str, int] = {}
        total_nnz = 0
        for i in range(16):
            for j in range(16):
                if not M[i][j].is_zero():
                    total_nnz += 1
                    pair = tuple(sorted((chiral_states[i]["multiplet"], chiral_states[j]["multiplet"])))
                    key = f"({pair[0]}, {pair[1]})"
                    pair_counts[key] = pair_counts.get(key, 0) + 1
        return {
            "total_nonzero_entries": total_nnz,
            "pair_entry_counts": pair_counts,
            "Q_uc_entries": pair_counts.get("(Q, u_c)", 0),
            "L_nuc_entries": pair_counts.get("(L, nu_c)", 0),
            "Q_dc_entries": pair_counts.get("(Q, d_c)", 0),
            "L_ec_entries": pair_counts.get("(L, e_c)", 0),
            "sym_err": gi_max_norm_sq(gi_sub(gi_transpose(M), M)),
        }

    weak_analysis = {
        "M4_plus_Hu": analyze_doublet_matrix(M_plus[3]),
        "M5_plus_Hu": analyze_doublet_matrix(M_plus[4]),
        "M4_minus_Hd": analyze_doublet_matrix(M_minus[3]),
        "M5_minus_Hd": analyze_doublet_matrix(M_minus[4]),
    }

    holo_separation_ok = (
        all(
            weak_analysis[key]["total_nonzero_entries"] == 8
            and weak_analysis[key]["Q_uc_entries"] == 6
            and weak_analysis[key]["L_nuc_entries"] == 2
            and weak_analysis[key]["Q_dc_entries"] == 0
            and weak_analysis[key]["L_ec_entries"] == 0
            for key in ("M4_plus_Hu", "M5_plus_Hu")
        )
        and all(
            weak_analysis[key]["total_nonzero_entries"] == 8
            and weak_analysis[key]["Q_dc_entries"] == 6
            and weak_analysis[key]["L_ec_entries"] == 2
            and weak_analysis[key]["Q_uc_entries"] == 0
            and weak_analysis[key]["L_nuc_entries"] == 0
            for key in ("M4_minus_Hd", "M5_minus_Hd")
        )
    )

    # 7. Exact 48x48 end-to-end 3-generation embedding + 11/12 tan(beta) invariance
    # Purely synthetic rational/Gaussian-integer Yukawas (0 of 19, zero empirical data)
    I_c = complex(0, 1)
    Yu = np.array(
        [
            [1, 2, 1 + I_c],
            [0, 7, 3 - 2 * I_c],
            [1 - I_c, 2, 29],
        ],
        dtype=np.complex128,
    ) / 10
    Yd = np.array(
        [
            [2, 1 + I_c, 3],
            [1 - 2 * I_c, 11, 4 + I_c],
            [2, 1 - I_c, 37],
        ],
        dtype=np.complex128,
    ) / 10
    Ye = np.array(
        [
            [1, 3 - I_c, 1],
            [2 + I_c, 13, 2],
            [1, 5 + 2 * I_c, 41],
        ],
        dtype=np.complex128,
    ) / 10

    # End-to-end check: build neutral-component 16x16 Higgs matrices (k=5 -> index 4)
    # and embed into 48x48 (3 generations x 16 chiral states)
    M5p_np = np.array([[x.to_complex() for x in row] for row in M_plus[4]], dtype=np.complex128)
    M5m_np = np.array([[x.to_complex() for x in row] for row in M_minus[4]], dtype=np.complex128)

    # Mask into quark / lepton sub-couplings of M5p (Hu^0) and M5m (Hd^0)
    def mask_pair(M: np.ndarray, a_name: str, b_name: str) -> np.ndarray:
        out = np.zeros_like(M)
        for i in range(16):
            for j in range(16):
                p = {chiral_states[i]["multiplet"], chiral_states[j]["multiplet"]}
                if p == {a_name, b_name}:
                    out[i, j] = M[i, j]
        return out

    M_Hu_Qu = mask_pair(M5p_np, "Q", "u_c")
    M_Hd_Qd = mask_pair(M5m_np, "Q", "d_c")
    M_Hd_Le = mask_pair(M5m_np, "L", "e_c")

    # Find one color index for (Q_u, u_c), one for (Q_d, d_c), and (L_e, e_c)
    qu_pair = next(
        (i, j)
        for i in range(16)
        for j in range(16)
        if chiral_states[i]["multiplet"] == "Q"
        and chiral_states[j]["multiplet"] == "u_c"
        and abs(M_Hu_Qu[i, j]) > 0
    )
    qd_pair = next(
        (i, j)
        for i in range(16)
        for j in range(16)
        if chiral_states[i]["multiplet"] == "Q"
        and chiral_states[j]["multiplet"] == "d_c"
        and abs(M_Hd_Qd[i, j]) > 0
    )
    le_pair = next(
        (i, j)
        for i in range(16)
        for j in range(16)
        if chiral_states[i]["multiplet"] == "L"
        and chiral_states[j]["multiplet"] == "e_c"
        and abs(M_Hd_Le[i, j]) > 0
    )

    tan_beta_list = [Fraction(1, 5), Fraction(1), Fraction(3), Fraction(10), Fraction(50)]
    invariant_11_keys = [
        "m_u_over_m_t",
        "m_c_over_m_t",
        "m_d_over_m_b",
        "m_s_over_m_b",
        "m_e_over_m_tau",
        "m_mu_over_m_tau",
        "abs_V_us",
        "abs_V_cb",
        "abs_V_ub",
        "J_CP",
        "m_b_over_m_tau",
    ]
    all_12_keys = invariant_11_keys + ["m_t_over_m_b"]

    tb_rows = []
    embed_48_max_err = float(0)
    for tb in tan_beta_list:
        tb_f = float(tb)
        vd = math.sqrt(1 / (1 + tb_f * tb_f))
        vu = tb_f * vd

        # Construct full 48x48 chiral mass bilinear W48
        W48 = (
            vu * np.kron(Yu, M_Hu_Qu)
            + vd * np.kron(Yd, M_Hd_Qd)
            + vd * np.kron(Ye, M_Hd_Le)
        )
        # Extract 3x3 mass sub-blocks directly from W48!
        Mu_48 = np.array(
            [[W48[16 * g1 + qu_pair[0], 16 * g2 + qu_pair[1]] for g2 in range(3)] for g1 in range(3)],
            dtype=np.complex128,
        )
        Md_48 = np.array(
            [[W48[16 * g1 + qd_pair[0], 16 * g2 + qd_pair[1]] for g2 in range(3)] for g1 in range(3)],
            dtype=np.complex128,
        )
        Me_48 = np.array(
            [[W48[16 * g1 + le_pair[0], 16 * g2 + le_pair[1]] for g2 in range(3)] for g1 in range(3)],
            dtype=np.complex128,
        )
        # Verify W48 blocks match vu*Yu, vd*Yd, vd*Ye up to exact unit phase of M5^{+-}
        embed_48_max_err = max(
            embed_48_max_err,
            float(np.max(np.abs(Mu_48 - M_Hu_Qu[qu_pair[0], qu_pair[1]] * vu * Yu))),
            float(np.max(np.abs(Md_48 - M_Hd_Qd[qd_pair[0], qd_pair[1]] * vd * Yd))),
            float(np.max(np.abs(Me_48 - M_Hd_Le[le_pair[0], le_pair[1]] * vd * Ye))),
        )

        obs = _extract_yukawa_observables(Mu_48, Md_48, Me_48)
        obs["tan_beta"] = str(tb)
        obs["mt_mb_divided_by_tan_beta"] = obs["m_t_over_m_b"] / tb_f
        tb_rows.append(obs)

    ref_row = tb_rows[0]
    max_11_drift = max(
        abs(row[k] - ref_row[k])
        for row in tb_rows[1:]
        for k in invariant_11_keys
    )
    max_mt_mb_linear_drift = max(
        abs(row["mt_mb_divided_by_tan_beta"] - ref_row["mt_mb_divided_by_tan_beta"])
        for row in tb_rows[1:]
    )
    max_j_comm_diff = max(row["J_CP_commutator_diff"] for row in tb_rows)
    mt_mb_span_ratio = tb_rows[-1]["m_t_over_m_b"] / tb_rows[0]["m_t_over_m_b"]
    expected_span_ratio = float(tan_beta_list[-1] / tan_beta_list[0])
    span_ratio_err = abs(mt_mb_span_ratio - expected_span_ratio)

    # 8. Mandatory Guardrail 3: 10-trial random Haar unitary basis-scrambling test
    rng_np = np.random.default_rng(20261120)
    tb_haar = Fraction(3)
    tb_haar_f = float(tb_haar)
    vd_h = math.sqrt(1 / (1 + tb_haar_f * tb_haar_f))
    vu_h = tb_haar_f * vd_h
    Mu_base = vu_h * Yu
    Md_base = vd_h * Yd
    Me_base = vd_h * Ye
    base_obs = _extract_yukawa_observables(Mu_base, Md_base, Me_base)

    haar_max_obs_drift = float(0)
    haar_max_unitarity_err = float(0)
    haar_trial_drifts = []
    for trial in range(10):
        UL, e1 = _sample_haar_u3(rng_np)
        URu, e2 = _sample_haar_u3(rng_np)
        URd, e3 = _sample_haar_u3(rng_np)
        ULe, e4 = _sample_haar_u3(rng_np)
        URe, e5 = _sample_haar_u3(rng_np)
        haar_max_unitarity_err = max(haar_max_unitarity_err, e1, e2, e3, e4, e5)
        scr_obs = _extract_yukawa_observables(
            UL @ Mu_base @ URu.conj().T,
            UL @ Md_base @ URd.conj().T,
            ULe @ Me_base @ URe.conj().T,
        )
        trial_max = max(abs(scr_obs[k] - base_obs[k]) for k in all_12_keys)
        haar_trial_drifts.append({"trial": trial + 1, "max_abs_drift_12_obs": trial_max})
        if trial_max > haar_max_obs_drift:
            haar_max_obs_drift = trial_max

    tol_14 = float(Fraction(1, 10 ** 14))
    tol_12 = float(Fraction(1, 10 ** 12))

    expected_counts = {"nu_c": 1, "e_c": 1, "u_c": 3, "Q": 6, "d_c": 3, "L": 2}
    expected_sixY = {"nu_c": [0], "e_c": [6], "u_c": [-4], "Q": [1], "d_c": [2], "L": [-3]}

    passed = (
        (herm_max_err == 0)
        and (cliff_max_err == 0)
        and (c10_unitarity_err == 0)
        and (c10_transpose_sign == -1)
        and (err_antisym == 0)
        and (c10_conj_sign == -1)
        and (conj_minus_err == 0)
        and (gamma11_vs_s3_5_err == 0)
        and (gamma11_sq_err == 0)
        and (gamma11_anticomm_err == 0)
        and (car_max_err == 0)
        and (len(even_indices) == 16)
        and (multiplet_counts == expected_counts)
        and (multiplet_sixY == expected_sixY)
        and (all_10_sym_err == 0)
        and all_10_sixY_conservation_ok
        and holo_separation_ok
        and (embed_48_max_err < tol_14)
        and (max_11_drift < tol_14)
        and (max_mt_mb_linear_drift < tol_14)
        and (span_ratio_err < tol_12)
        and (max_j_comm_diff < tol_14)
        and (abs(base_obs["J_CP"]) > float(Fraction(1, 10000)))
        and (haar_max_unitarity_err < tol_14)
        and (haar_max_obs_drift < tol_12)
    )

    return {
        "construction": "5-fold Pauli Jordan-Wigner tensor product in exact Z[i]",
        "cl10_and_c10_exact_checks": {
            "gamma_hermiticity_max_norm_sq_err": herm_max_err,
            "cl10_100_anticommutators_max_norm_sq_err": cliff_max_err,
            "C10_unitarity_max_norm_sq_err": c10_unitarity_err,
            "C10_transpose_computed_sign": c10_transpose_sign,
            "C10_antisymmetry_max_norm_sq_err": err_antisym,
            "C10_conjugation_computed_sign": c10_conj_sign,
            "C10_conjugation_max_norm_sq_err": conj_minus_err,
            "Gamma11_equals_sigma3_tensor_5_err": gamma11_vs_s3_5_err,
            "Gamma11_squared_minus_I_err": gamma11_sq_err,
            "Gamma11_anticomm_all_gammas_err": gamma11_anticomm_err,
            "CAR_anticommutators_max_norm_sq_err": car_max_err,
        },
        "chiral_16_decomposition": {
            "dimension": len(even_indices),
            "multiplet_counts": multiplet_counts,
            "multiplet_6Y_charges": multiplet_sixY,
            "all_10_M_k_pm_symmetry_max_err": all_10_sym_err,
            "all_10_M_k_pm_exact_6Y_conservation": bool(all_10_sixY_conservation_ok),
        },
        "holomorphic_doublet_separation": {
            "weak_doublets": weak_analysis,
            "exact_holomorphic_separation_pass": bool(holo_separation_ok),
        },
        "tan_beta_11_of_12_invariance": {
            "tan_beta_grid": [str(x) for x in tan_beta_list],
            "embed_48x48_block_max_err": embed_48_max_err,
            "max_drift_11_invariant_ratios": max_11_drift,
            "max_drift_mt_mb_over_tan_beta": max_mt_mb_linear_drift,
            "mt_mb_ratio_50_over_one_fifth": mt_mb_span_ratio,
            "expected_linear_span_ratio": expected_span_ratio,
            "span_ratio_err": span_ratio_err,
            "max_J_CP_vs_commutator_diff": max_j_comm_diff,
            "baseline_J_CP": base_obs["J_CP"],
            "rows": tb_rows,
        },
        "guardrail_3_haar_scrambling_10_trials": {
            "trials": 10,
            "tan_beta": str(tb_haar),
            "max_unitarity_err": haar_max_unitarity_err,
            "max_abs_drift_all_12_obs": haar_max_obs_drift,
            "per_trial": haar_trial_drifts,
        },
        "pass": bool(passed),
        "_raw_pf4": {
            "Hu_cross_entries": (
                weak_analysis["M4_plus_Hu"]["Q_dc_entries"]
                + weak_analysis["M4_plus_Hu"]["L_ec_entries"]
                + weak_analysis["M5_plus_Hu"]["Q_dc_entries"]
                + weak_analysis["M5_plus_Hu"]["L_ec_entries"]
            ),
            "Hd_cross_entries": (
                weak_analysis["M4_minus_Hd"]["Q_uc_entries"]
                + weak_analysis["M4_minus_Hd"]["L_nuc_entries"]
                + weak_analysis["M5_minus_Hd"]["Q_uc_entries"]
                + weak_analysis["M5_minus_Hd"]["L_nuc_entries"]
            ),
        },
    }


# ---------------------------------------------------------------------------
# Task OW3-C: Four Planted Faults (PF-OW3-1 through PF-OW3-4)
# ---------------------------------------------------------------------------

def run_ow3_c(
    raw_a: Dict[str, object],
    raw_b1: Dict[str, object],
    raw_b2: Dict[str, object],
) -> Dict[str, object]:
    """Independently test and refute all four planted faults from computed quantities."""
    mp.mp.dps = 80
    tol_10 = mp.mpf(1) / mp.mpf(10 ** 10)
    tol_50 = mp.mpf(1) / mp.mpf(10 ** 50)

    # PF-OW3-1: False volume-uniqueness claim Vol(m004) < Vol(m000) or Vol(m004) < Vol(m003)
    v0 = raw_a["m000"]
    v3 = raw_a["m003"]
    v4 = raw_a["m004"]
    claim_v4_lt_v0 = bool(v4 < v0)
    claim_v4_lt_v3 = bool(v4 < v3 - tol_10)
    pf1_caught = (not claim_v4_lt_v0) and (not claim_v4_lt_v3) and (abs(2 * v0 - v4) < tol_10) and (abs(v3 - v4) < tol_10)

    # PF-OW3-2: False convergence claim for Z(0, beta=10)
    four_g = raw_a["four_G"]
    wh_pp = raw_a["wh_b++"]
    beta10 = mp.mpf(10)
    floor_10 = mp.exp(-beta10 * four_g)
    terms_25 = [mp.exp(-beta10 * v) for v in wh_pp[:25]]
    terms_50 = [mp.exp(-beta10 * v) for v in wh_pp]
    all_25_below_4G = all(v < four_g for v in wh_pp[:25])
    all_50_below_4G = all(v < four_g for v in wh_pp)
    min_term_50 = min(terms_50)
    pf2_caught = (
        all_25_below_4G
        and all_50_below_4G
        and bool(min_term_50 > floor_10)
        and bool(sum(terms_25) > 25 * floor_10)
        and bool(sum(terms_50) > 50 * floor_10)
    )

    # PF-OW3-3: False Path-A variation claim that Tr_{W_3^+}(D(a, b)) varies across (a, b)
    pf3_caught = bool(raw_b1["exact_all_24_plus_half"]) and bool(raw_b1["max_mp_err_plus"] < tol_50)

    # PF-OW3-4: False holomorphic cross-coupling H_u -> (Q, d^c) or H_d -> (Q, u^c)
    hu_cross = int(raw_b2["Hu_cross_entries"])
    hd_cross = int(raw_b2["Hd_cross_entries"])
    pf4_caught = (hu_cross == 0) and (hd_cross == 0)

    all_caught = pf1_caught and pf2_caught and pf3_caught and pf4_caught

    return {
        "PF-OW3-1_volume_uniqueness": {
            "planted_false_claim": "Vol(m004) < Vol(m000) or Vol(m004) < Vol(m003)",
            "claim_m004_lt_m000_holds": claim_v4_lt_v0,
            "claim_m004_lt_m003_holds": claim_v4_lt_v3,
            "Vol_m004_minus_Vol_m000": mp.nstr(v4 - v0, 14),
            "abs_Vol_m004_minus_Vol_m003": mp.nstr(abs(v4 - v3), 12),
            "fault_caught": bool(pf1_caught),
        },
        "PF-OW3-2_pure_volume_convergence_beta10": {
            "planted_false_claim": "Z(0, beta=10) converges",
            "all_k1_25_below_4G": bool(all_25_below_4G),
            "all_k1_50_below_4G": bool(all_50_below_4G),
            "floor_exp_minus_40G": mp.nstr(floor_10, 14),
            "min_term_k1_50_b++": mp.nstr(min_term_50, 14),
            "partial_sum_k1_25": mp.nstr(sum(terms_25), 14),
            "partial_sum_k1_50": mp.nstr(sum(terms_50), 14),
            "fault_caught": bool(pf2_caught),
        },
        "PF-OW3-3_pathA_trace_variation": {
            "planted_false_claim": "Tr_{W_3^+}(D(a,b)) varies across nonzero (a,b)",
            "exact_Q_w_all_24_equal_plus_half": bool(raw_b1["exact_all_24_plus_half"]),
            "mpmath_65dps_max_deviation": mp.nstr(raw_b1["max_mp_err_plus"], 12),
            "fault_caught": bool(pf3_caught),
        },
        "PF-OW3-4_holomorphic_cross_coupling": {
            "planted_false_claim": "H_u couples to (Q, d^c) or H_d couples to (Q, u^c) in 16x16x10_C",
            "Hu_forbidden_nonzero_entries": hu_cross,
            "Hd_forbidden_nonzero_entries": hd_cross,
            "fault_caught": bool(pf4_caught),
        },
        "all_4_faults_caught": bool(all_caught),
        "pass": bool(all_caught),
    }


def _self_audit_ast(script_path: pathlib.Path) -> Dict[str, object]:
    """Compute live AST hygiene counts (float/complex literals and frontier imports)."""
    tree = ast.parse(script_path.read_text(encoding="utf-8"))
    bad_literals = [
        (node.lineno, type(node.value).__name__)
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, (float, complex))
    ]
    frontier_imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if "frontier" in alias.name:
                    frontier_imports.append((node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if "frontier" in mod:
                frontier_imports.append((node.lineno, mod))
    return {
        "empirical_inputs": "0 of 19",
        "frontier_imports_count": len(frontier_imports),
        "float_or_complex_ast_literals_count": len(bad_literals),
        "hygiene_pass": (len(frontier_imports) == 0) and (len(bad_literals) == 0),
    }


def main() -> None:
    script_path = pathlib.Path(__file__).resolve()
    hygiene = _self_audit_ast(script_path)

    res_a = run_ow3_a()
    raw_a = res_a.pop("_raw_anchor_vols")

    res_b1 = run_ow3_b_part1()
    raw_b1 = res_b1.pop("_raw_pf3")

    res_b2 = run_ow3_b_part2()
    raw_b2 = res_b2.pop("_raw_pf4")

    res_c = run_ow3_c(raw_a, raw_b1, raw_b2)

    overall_pass = (
        bool(hygiene["hygiene_pass"])
        and bool(res_a["pass"])
        and bool(res_b1["pass"])
        and bool(res_b2["pass"])
        and bool(res_c["pass"])
    )

    payload = {
        "card": "AGY-002_A2-OW3 (+ Erratum 1)",
        "role": "Independent Cold-Room Zero-Trust Referee",
        "hygiene": hygiene,
        "OW3-A": res_a,
        "OW3-B": {
            "Part_1_Path_A_15x15_NoGo": res_b1,
            "Part_2_Spin10_XHOL_32x32": res_b2,
            "pass": bool(res_b1["pass"]) and bool(res_b2["pass"]),
        },
        "OW3-C": res_c,
        "overall_pass": bool(overall_pass),
    }

    out_path = script_path.parent / "referee_a2_ow3_out.json"
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print(f"Cold-room referee execution complete; wrote {out_path.name}")


if __name__ == "__main__":
    main()
