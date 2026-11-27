#!/usr/bin/env python3
"""SM-R610 (register row P-610): W134's 17/24 of the cusp unit against C8's whole unit, located; K2 re-derived.

Sealed before any run on the real cases (the card: relays/cards/SM_R610_w134-against-c8.md). Data-free.

  R0  the instrument: chi_k(rho) = d + dk/12 - alpha(e^{pi i k/2} rho(S)) - alpha((e^{pi i k/3} rho(S) rho(T))^-1)
      - alpha(rho(T)) (B1632's Borcherds-Skoruppa form) in exact Fractions, on monomial matrices whose entries are
      roots of unity (eigenvalue turns from the cycles); calibrations; agreement with main's float chi (B1632)
  R1  the object: rho(S) = zeta8 P, rho(T) = zeta8 L^-1 (B1730, B1736); Mp2(Z) relations exactly; T-exponents;
      equivalence to main's rho_T from the weave's lifts (B1641's code, an intertwiner)
  R2  C8's requirement: dim of weight-3/2 forms of rho_T with n uniform units (O(n delta)) = chi_{3/2+12n} for n >= 1;
      a second route by main's exact q-series (B1730's space(), and the dressed variant below)
  R3  W134's admissibility from the definition: det(rho (x) chi_eta^(r+m)) as a character chi_eta^c, c computed
      (not assumed); admissible iff c = 0 mod 24
  R4  W134's count: I(r, cond, m) = -chi_{3/2+m/2}(rho (x) chi_eta^(r+m)) + sum_{p in cond} chi_{1+m/2}(p (x) ...);
      condition 0 exactly; V2, V4, L6 from B1641's pieces (float); the |I| = 3 data, the least |m|
  R5  the location: the unit's multiplier, the normalisation m = 24n, dim against index, the determinant at whole units
  R6  the joint frame: k = r + m mod 24 at each three-generation datum (B1736's rho' = rho (x) chi_eta^k)
  R7  K2: E8's roots (exact) -> E6, the 27 and the 16; Dynkin indices against every root; n_G = w_G c mod 24
  P1  plant: the unit taken as eta^-12 (n units = m = 12n); P2 plant: the dressing on the weight only (no character)
  CT  control: the conjugate hand

    python3 -B relays/sm_r610/run.py <main checkout>          # writes r610_results.json and prints a summary
    python3 -B relays/sm_r610/run.py <main checkout> --smoke  # instrument paths on inputs outside the population
"""
import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import pathlib
import sys
from fractions import Fraction as F

sys.dont_write_bytecode = True
import numpy as np  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ALLOWED = (0, 4, 8, 12, 16, 20)
MS = range(-24, 25)
CONDS = ("0", "V2", "V4", "L6")


# ---------------------------------------------------------------- exact monomial matrices (entries: roots of unity)
class Mono:
    """column j goes to row p[j] with entry exp(2 pi i t[j]); t in Fractions (turns)"""

    def __init__(self, p, t):
        self.p, self.t = tuple(p), tuple(F(x) % 1 for x in t)

    def __mul__(self, o):
        return Mono([self.p[o.p[j]] for j in range(len(o.p))], [o.t[j] + self.t[o.p[j]] for j in range(len(o.p))])

    def scale(self, s):
        return Mono(self.p, [x + s for x in self.t])

    def inv(self):
        q, u = [0] * len(self.p), [F(0)] * len(self.p)
        for j, i in enumerate(self.p):
            q[i], u[i] = j, -self.t[j]
        return Mono(q, u)

    def __eq__(self, o):
        return self.p == o.p and self.t == o.t

    def cycles(self):
        seen, out = set(), []
        for j in range(len(self.p)):
            if j in seen:
                continue
            c, k = [], j
            while k not in seen:
                seen.add(k)
                c.append(k)
                k = self.p[k]
            out.append(c)
        return out

    def eig_turns(self):
        ev = []
        for c in self.cycles():
            s, n = sum(self.t[j] for j in c), len(c)
            ev += [((s + k) / n) % 1 for k in range(n)]
        return sorted(ev)

    def det_turn(self):
        sign = sum(len(c) - 1 for c in self.cycles()) % 2
        return (sum(self.t) + F(sign, 2)) % 1

    def scalar_turn(self):
        """the turn s if the matrix is exp(2 pi i s) times the identity, else None"""
        if any(self.p[j] != j for j in range(len(self.p))) or len(set(self.t)) != 1:
            return None
        return self.t[0]

    def numeric(self):
        d = len(self.p)
        A = np.zeros((d, d), dtype=complex)
        for j in range(d):
            A[self.p[j], j] = np.exp(2j * np.pi * float(self.t[j]))
        return A


def ident(d):
    return Mono(range(d), [0] * d)


def alpha(A):
    return sum(A.eig_turns(), F(0))


def allowed(k, S):
    s = (S * S).scalar_turn()
    return s is not None and s == (-F(k) / 2) % 1


def chi(k, S, T):
    k, d = F(k), len(S.p)
    return d + d * k / 12 - alpha(S.scale(k / 4)) - alpha((S * T).scale(k / 6).inv()) - alpha(T)


def chi_or_zero(k, S, T):
    return chi(k, S, T) if allowed(k, S) else None


def eta_char(a, d=3):
    """chi_eta^a on (S, T) as d x d scalars: S -> e^{-pi i a/4}, T -> e^{2 pi i a/24}"""
    return ident(d).scale(F(-a, 8)), ident(d).scale(F(a, 24))


def twist(S, T, a):
    cS, cT = eta_char(a, len(S.p))
    return S * cS, T * cT


# the object (B1730, B1736): rho(S) = zeta8 P, rho(T) = zeta8 L^-1, L^-1 = [[1,0,0],[0,0,1],[0,-1,0]]
RHO_S = Mono([1, 0, 2], [F(1, 8)] * 3)
RHO_T = Mono([0, 2, 1], [F(1, 8), F(1, 8) + F(1, 2), F(1, 8)])


def conj(A):
    return Mono(A.p, [-x for x in A.t])


# ---------------------------------------------------------------- loading main's modules (read-only)
def load(main, rel, name, strip_from=None):
    path = main / rel
    if strip_from is None:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod
    src = path.read_text(encoding="utf-8")
    cut = src.index(strip_from)
    ns = {"__file__": str(path), "__name__": name}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src[:cut], str(path), "exec"), ns)  # main's code up to strip_from; nothing is written
    return ns


# ---------------------------------------------------------------- R0
def R0(w45):
    one = ident(1)
    triv = {k: chi(k, one, one) for k in (0, 2, 4, 6, 12)}
    eS, eT = eta_char(1, 1)
    eta_half = chi(F(1, 2), eS, eT)
    e2S, e2T = eta_char(2, 1)
    agree = []
    for twok in range(-1, 52):
        k = F(twok, 2)
        for a in range(24):
            S, T = twist(RHO_S, RHO_T, a)
            if allowed(k, S):
                agree.append(abs(float(chi(k, S, T)) - w45.chi(float(k), S.numeric(), T.numeric())))
    c = {"trivial: chi_0, 2, 4, 6, 12 = 1, 0, 1, 1, 2": [triv[k] for k in (0, 2, 4, 6, 12)] == [1, 0, 1, 1, 2],
         "eta: chi_1/2 = 1, allowed": eta_half == 1 and allowed(F(1, 2), eS),
         "eta^2: chi_1 = 1 (B1641's calibration)": chi(1, e2S, e2T) == 1,
         "main's float chi agrees on every allowed (k, twist), k = -1/2 .. 51/2": max(agree) < 1e-9}
    return {"checks": c, "comparisons": len(agree), "max |exact - float|": max(agree)}, all(c.values())


# ---------------------------------------------------------------- R1
def R1(zf, b1641):
    S, T = RHO_S, RHO_T
    S2 = S * S
    rel = {"S^2 central scalar": S2.scalar_turn() is not None,
           "S^2 = (S T)^3": S2 == (S * T) * (S * T) * (S * T),
           "S^8 = 1": S2 * S2 * S2 * S2 == ident(3),
           "T-exponents (1/8, 3/8, 7/8)": T.eig_turns() == [F(1, 8), F(3, 8), F(7, 8)],
           "weight 3/2 allowed": allowed(F(3, 2), S)}
    A = zf.part_a()
    numerics = {k: v for k, v in A.items() if isinstance(v, float)}
    numerics_ok = all(v < 1e-12 for v in numerics.values())
    # main's rho_T from the weave's lifts (B1641/B1634): an intertwiner with the exact rho
    rTS, rTT = b1641["rTS"], b1641["rTT"]
    X, Y = S.numeric(), T.numeric()
    Mx = np.vstack([np.kron(np.eye(3), rTS) - np.kron(X.T, np.eye(3)),
                    np.kron(np.eye(3), rTT) - np.kron(Y.T, np.eye(3))])
    sv = np.linalg.svd(Mx, compute_uv=False)
    null = int(sum(sv < 1e-9))
    inter = None
    if null == 1:
        v = np.linalg.svd(Mx)[2][-1].conj()
        Q = v.reshape(3, 3, order="F")
        inter = float(min(abs(np.linalg.svd(Q, compute_uv=False))))
    rel["main's theta multiplier equals rho (B1730 part A, < 1e-12)"] = bool(numerics_ok)
    rel["main's lift rho_T is equivalent to rho (one intertwiner, invertible)"] = null == 1 and inter > 1e-6
    return {"checks": rel, "B1730 part A": numerics, "intertwiner space dim": null,
            "intertwiner least singular value": inter}, all(rel.values())


# ---------------------------------------------------------------- the q-series route (main's B1730 machinery)
def bounds_dressed(r, m):
    """G's line bounds in x = q^(1/8) for F = eta^(r+m) G holomorphic at the cusp (lines P, M = v+, N of rho)"""
    a, out = r + m, []
    for e in (F(1, 8), F(7, 8), F(3, 8)):
        c = (e + F(a, 24)) % 1
        b = 8 * (c - F(a, 24))
        assert b.denominator == 1
        out.append(int(b))
    return out


def dim_dressed(zf, r, m, M):
    """dim of weight-(3/2 + m/2) forms of rho (x) chi_eta^(r+m), holomorphic at the cusp; B1730's space() with
    F = eta^(r+m) G (G of weight 3/2 - r/2, multiplier rho) and the holomorphic bounds above"""
    import sympy as sp
    E = zf._exact()
    k2 = 3 - r
    gens = []
    for vec, wt in ((E["R"], (k2 + 1) // 2), (E["D1"], (k2 - 3) // 2), (E["D2"], (k2 - 7) // 2)):
        f = zf._pow(E["Dinv"], M)
        for b in zf._Mbasis(wt + 12 * M):
            gens.append(zf._lines([f * b * c for c in vec]))
    bd = bounds_dressed(r, m)
    rows = []
    for li in range(3):
        ks = sorted({k for g in gens for k in g[li].d if k < bd[li]})
        for k in ks:
            rows.append([zf._coef(g[li], k) for g in gens])
    if not gens:
        return 0, 0
    A = sp.Matrix(rows) if rows else sp.zeros(0, len(gens))
    return len(gens) - A.rank(), len(gens)


def stable_dim(zf, r, m, M0):
    d0, n0 = dim_dressed(zf, r, m, M0)
    d1, n1 = dim_dressed(zf, r, m, M0 + 2)
    return {"dim": d0, "dim at M + 2": d1, "stable": d0 == d1, "generators": [n0, n1]}


# ---------------------------------------------------------------- R2: C8
def index0(r, m, S=RHO_S, T=RHO_T):
    Sx, Tx = twist(S, T, r + m)
    v = chi_or_zero(F(3, 2) + F(m, 2), Sx, Tx)
    return None if v is None else -v


def R2(zf):
    rows = {}
    for n in range(0, 5):
        k = F(3, 2) + 12 * n
        rows[str(n)] = {"chi_{3/2+12n}(rho)": int(chi(k, RHO_S, RHO_T)), "I(0, '0', 24n)": int(index0(0, 24 * n))}
    q = {}
    for n in (1, 2):
        q["B1730 space(0, %d)" % n] = len(zf.space(0, n, 4)[0])
        q["dressed route (0, %d)" % (24 * n)] = stable_dim(zf, 0, 24 * n, 2 * n + 1)
    c = {"chi_{3/2+12n}(rho) = 3n, n = 0..4": all(rows[str(n)]["chi_{3/2+12n}(rho)"] == 3 * n for n in range(5)),
         "W134's I(r=0, cond 0, m = 24n) = -3n": all(rows[str(n)]["I(0, '0', 24n)"] == -3 * n for n in range(5)),
         "B1730's space(0, n) has dim 3n, n = 1, 2": all(q["B1730 space(0, %d)" % n] == 3 * n for n in (1, 2)),
         "the dressed q-series route gives 3n, stable": all(
             q["dressed route (0, %d)" % (24 * n)]["dim"] == 3 * n and q["dressed route (0, %d)" % (24 * n)]["stable"]
             for n in (1, 2))}
    return {"checks": c, "chi route": rows, "q-series": q}, all(c.values())


# ---------------------------------------------------------------- R3: admissibility
def det_exponent(a, S=RHO_S, T=RHO_T):
    """c mod 24 with det(rho (x) chi_eta^a) = chi_eta^c, read off T and checked on S"""
    Sx, Tx = twist(S, T, a)
    cT = Tx.det_turn() * 24
    assert cT.denominator == 1
    c = int(cT) % 24
    return c, Sx.det_turn() == F(-c, 8) % 1


def R3():
    tab, consistent = {}, True
    for r in ALLOWED:
        tab[str(r)] = []
        for m in MS:
            c, ok = det_exponent(r + m)
            consistent &= ok
            if c == 0:
                tab[str(r)].append(m)
    weight_ok = all(allowed(F(3, 2) + F(m, 2), twist(RHO_S, RHO_T, r + m)[0]) for r in ALLOWED for m in MS)
    r_allowed = [r for r in range(24) if allowed(F(3, 2), twist(RHO_S, RHO_T, r)[0])]
    c = {"the det character is a power of chi_eta on S and T alike": bool(consistent),
         "c(r + m) = 9 + 3(r + m) mod 24": all(det_exponent(a)[0] == (9 + 3 * a) % 24 for a in range(-48, 49)),
         "the twists allowing weight 3/2 are r = 0 mod 4": r_allowed == list(ALLOWED),
         "every dressed datum is allowed at its weight": bool(weight_ok),
         "admissible iff m = 5 - r mod 8": all(tab[str(r)] == [m for m in MS if (m + r - 5) % 8 == 0] for r in ALLOWED),
         "m = 0 and m = +-24 never admissible": all(m not in tab[str(r)] for r in ALLOWED for m in (0, 24, -24)),
         "no twist r in 0..23 makes rho (x) chi_eta^r det-1 at a whole unit": all(
             det_exponent(r + 24 * n)[0] != 0 for r in ALLOWED for n in range(-3, 4))}
    cs = [det_exponent(a)[0] for a in range(24)]
    return {"checks": c, "admissible m by r": tab, "det exponent c(a), a = 0..23": cs}, all(c.values()), tab


# ---------------------------------------------------------------- R4: the count
def pieces_float(b1641, w45):
    """B1641's six local solutions: for each valid identification, (S, T) of the 2- and 4-dim pieces (float)"""
    out = {}
    for (s, t), (Sm, Tm, ok) in b1641["idents"].items():
        if not ok:
            continue
        by = {}
        for Q in b1641["pieces"]:
            by[Q.shape[1]] = (Q.conj().T @ Sm @ Q, Q.conj().T @ Tm @ Q)
        by["rTS"], by["rTT"] = b1641["rTS"], b1641["rTT"]
        out[f"S={s}, T={t}"] = by
    return out


def index_full(r, cond, m, by, w45):
    a = r + m
    zS, zT = np.exp(-1j * np.pi * a / 4), np.exp(2j * np.pi * a / 24)
    k = 1.5 + m / 2
    if not w45.allowed(k, zS * by["rTS"]):
        return None
    v = -w45.chi(k, zS * by["rTS"], zT * by["rTT"])
    members = {"0": [], "V2": [2], "V4": [4], "L6": [2, 4]}[cond]
    for d in members:
        Sp, Tp = by[d]
        if not w45.allowed(1 + m / 2, zS * Sp):
            return None
        v += w45.chi(1 + m / 2, zS * Sp, zT * Tp)
    return v


def R4(tab, zf, b1641, w45):
    adm = [(r, m) for r in ALLOWED for m in tab[str(r)] if abs(m) < 24]
    exact0 = {(r, m): int(index0(r, m)) for (r, m) in adm}
    least_by_r = {r: min(tab[str(r)], key=lambda m: (abs(m), m)) for r in ALLOWED}
    threes0 = sorted((r, m) for (r, m), v in exact0.items() if abs(v) == 3)
    full_tab = {"0": {f"{r},{m}": v for (r, m), v in exact0.items()}}
    pf = pieces_float(b1641, w45)
    lanes = {}
    for name, by in pf.items():
        lane = {}
        for cond in CONDS:
            for (r, m) in adm:
                v = index_full(r, cond, m, by, w45)
                lane[(r, m, cond)] = None if v is None else round(v, 9)
        lanes[name] = lane
    names = list(lanes)
    same = all(lanes[names[0]] == lanes[n] for n in names[1:])
    lane = lanes[names[0]]
    ints = all(v is not None and abs(v - round(v)) < 1e-9 for v in lane.values())
    agree0 = all(abs(lane[(r, m, "0")] - exact0[(r, m)]) < 1e-9 for (r, m) in adm)
    threes = sorted((r, m, cd) for (r, m, cd), v in lane.items() if v is not None and abs(abs(v) - 3) < 1e-9)
    w134_twelve = sorted([(4, 17, "0"), (4, -23, "L6"), (12, 17, "0"), (12, -23, "0"), (12, -23, "L6"),
                          (20, -23, "L6"), (0, 21, "0"), (0, 21, "L6"), (8, 21, "0"), (8, 21, "L6"), (8, -19, "0"),
                          (16, 21, "L6")])
    least_three = min(abs(m) for (_, m, _) in threes) if threes else None
    at_least = max(abs(lane[(r, least_by_r[r], cd)]) for r in ALLOWED for cd in CONDS)
    upto16 = max(abs(v) for (r, m, cd), v in lane.items() if abs(m) <= 16)
    # q-series second route at the positive-weight three-generation data of condition 0
    q = {f"{r},{m}": stable_dim(zf, r, m, 3) for (r, m) in threes0 if m > 0}
    q_ok = all(v["stable"] and v["dim"] == abs(exact0[tuple(int(x) for x in k.split(","))]) for k, v in q.items())
    for cd in ("V2", "V4", "L6"):
        full_tab[cd] = {f"{r},{m}": lane[(r, m, cd)] for (r, m) in adm}
    c = {"condition 0, exact: |I| = 3 at (4,17), (12,17), (12,-23), (0,21), (8,21), (8,-19) only":
             threes0 == sorted([(4, 17), (12, 17), (12, -23), (0, 21), (8, 21), (8, -19)]),
         "condition 0: the least |m| with three is 17": min(abs(m) for (_, m) in threes0) == 17 if threes0 else False,
         "the pieces' lanes agree across identifications and are integers": bool(same and ints),
         "condition 0 on main's lift rho_T (float) equals the exact route": bool(agree0),
         "all conditions: |I| = 3 at exactly W134's twelve": threes == w134_twelve,
         "all conditions: the least |m| with three is 17": least_three == 17,
         "|I| <= 1 at the least admissible datum": at_least <= 1 + 1e-9,
         "|I| <= 2 for admissible |m| <= 16": upto16 <= 2 + 1e-9,
         "the q-series dimension equals |I| at the positive-m threes of condition 0": bool(q_ok)}
    return {"checks": c, "threes": [list(x) for x in threes], "least admissible m by r": least_by_r,
            "q-series at condition 0": q, "the index at the admissible data": full_tab}, all(c.values()), threes


# ---------------------------------------------------------------- R5: the location
def R5(threes):
    unitS, unitT = eta_char(24)
    triv_unit = unitS == ident(3) and unitT == ident(3)
    same_norm = all(index0(r, 24 * n) == -(chi(F(3, 2), *twist(RHO_S, RHO_T, r)) + 3 * n) for r in ALLOWED
                    for n in range(-2, 3))
    det_whole = {f"r={r}": sorted({det_exponent(r + 24 * n)[0] for n in range(-3, 4)}) for r in ALLOWED}
    floor_ok = all(chi(F(3, 2) + F(m, 2), *twist(RHO_S, RHO_T, r + m)) - chi(F(3, 2), *twist(RHO_S, RHO_T, r))
                   == sum((lam + F(m, 24)) // 1 for lam in twist(RHO_S, RHO_T, r)[1].eig_turns())
                   for r in ALLOWED for m in MS)
    c = {"the unit's multiplier chi_eta^24 is trivial on S and T": bool(triv_unit),
         "W134's m = 24n is C8's O(n delta): I(r, 0, 24n) = -(chi_{3/2}(rho_r) + 3n), every allowed r": bool(same_norm),
         "at whole units the det exponent is 9 + 3r, never 0": all(v == [(9 + 3 * int(k[2:])) % 24] and v != [0]
                                                                   for k, v in det_whole.items()),
         "the dressing moves chi by the floors alone (W134's closed form), every r and |m| <= 24": bool(floor_ok),
         "C8's three is W134's |I(0, 0, 24)|, the same count": index0(0, 24) == -3}
    return {"checks": c, "det exponent at whole units": det_whole}, all(c.values())


# ---------------------------------------------------------------- R6: the joint frame
def R6(threes):
    ks = {f"{r},{m},{cd}": (r + m) % 24 for (r, m, cd) in threes}
    least = {f"{r},{m},{cd}": (r + m) % 24 for (r, m, cd) in threes if abs(m) == 17}
    c = {"every three-generation datum has k = r + m in {5, 13, 21} (B1736's rho')": set(ks.values()) <= {5, 13, 21},
         "the 17/24 data have k = 21 (r = 4) and k = 5 (r = 12)": least == {"4,17,0": 21, "12,17,0": 5}}
    return {"checks": c, "k by datum": ks}, all(c.values())


# ---------------------------------------------------------------- R7: K2
def e8_roots():
    """exact, as Fractions: D8's 112 and the 128 half-integer vectors with an even number of minus signs"""
    roots = []
    for i, j in itertools.combinations(range(8), 2):
        for si, sj in itertools.product((1, -1), repeat=2):
            v = [F(0)] * 8
            v[i], v[j] = F(si), F(sj)
            roots.append(tuple(v))
    for signs in itertools.product((1, -1), repeat=8):
        if signs.count(-1) % 2 == 0:
            roots.append(tuple(F(s, 2) for s in signs))
    return roots


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def project_out(v, basis):
    """v minus its orthogonal projection on span(basis) (exact, Gram solve)"""
    import sympy as sp
    G = sp.Matrix([[dot(a, b) for b in basis] for a in basis])
    rhs = sp.Matrix([dot(v, a) for a in basis])
    coef = G.LUsolve(rhs)
    return tuple(F(str(sp.nsimplify(x))) for x in (sp.Matrix(v) - sum((coef[i] * sp.Matrix(basis[i])
                                                                        for i in range(len(basis))), sp.zeros(8, 1))))


def R7():
    roots = e8_roots()
    al = (F(1), F(-1)) + (F(0),) * 6
    be = (F(0), F(1), F(-1)) + (F(0),) * 5
    e6 = [x for x in roots if dot(x, al) == 0 and dot(x, be) == 0]
    cls = [x for x in roots if (dot(x, al), dot(x, be)) == (1, 0)]
    w27 = [project_out(x, [al, be]) for x in cls]
    idx27 = sorted({sum(dot(mu, g) ** 2 for mu in w27) / 2 for g in e6})
    mu0 = w27[0]
    d5 = [g for g in e6 if dot(g, mu0) == 0]
    split = {}
    for mu in w27:
        split.setdefault(dot(mu, mu0), []).append(mu)
    sizes = sorted(len(v) for v in split.values())
    w16 = next((v for v in split.values() if len(v) == 16), [])
    w10 = next((v for v in split.values() if len(v) == 10), [])
    idx16 = sorted({sum(dot(mu, g) ** 2 for mu in w16) / 2 for g in d5})
    idx10 = sorted({sum(dot(mu, g) ** 2 for mu in w10) / 2 for g in d5})
    w = {"27": (idx27[0] if len(idx27) == 1 else None, len(w27)),
         "16": (idx16[0] if len(idx16) == 1 else None, len(w16))}
    l27, n27 = w["27"]
    l16, n16 = w["16"]

    def anomalies(r, m, l, n):
        c = det_exponent(r + m)[0]
        return (int(l * c) % 24, int(l * c) % 24, int(n * c) % 24)
    full = all((anomalies(r, m, l27, n27) == (0, 0, 0)) == (det_exponent(r + m)[0] == 0) for r in ALLOWED for m in MS)
    sm16 = all((anomalies(r, m, l16, n16) == (0, 0, 0)) == (m % 2 == 1) for r in ALLOWED for m in MS)
    form = all(anomalies(r, m, l27, n27) == ((18 * (3 + r + m)) % 24, (18 * (3 + r + m)) % 24, (81 * (3 + r + m)) % 24)
               for r in ALLOWED for m in MS)
    w134 = all((anomalies(r, m, l27, n27) == (0, 0, 0)) == ((m + r - 5) % 8 == 0) for r in ALLOWED for m in MS)
    c = {"240 roots of norm 2": len(roots) == 240 and all(dot(x, x) == 2 for x in roots),
         "E6: 72 roots orthogonal to A2; the class (1, 0) has 27": len(e6) == 72 and len(cls) == 27,
         "the 27's Dynkin index is 6 against every E6 root": idx27 == [6],
         "D5 = 40 roots orthogonal to a 27-weight; the 27 splits 1 + 10 + 16": len(d5) == 40 and sizes == [1, 10, 16],
         "the 16's index is 4 and the 10's is 2 against every D5 root": idx16 == [4] and idx10 == [2],
         "n_SU3 = n_SU2 = 18(3 + r + m), n_grav = 81(3 + r + m) mod 24 (W135's K2 formula)": bool(form),
         "the full 27 is anomaly-free iff its family part is det-1": bool(full),
         "... iff m = 5 - r mod 8 (W134's condition)": bool(w134),
         "the 16 alone needs only m odd": bool(sm16)}
    return {"checks": c, "weights (index, dim)": {k: [str(v[0]), v[1]] for k, v in w.items()}}, all(c.values())


# ---------------------------------------------------------------- plants and control
def P1():
    """the unit taken as eta^-12: n units = m = 12n; the 'least three' read in those units"""
    dims = {}
    for n in range(0, 5):
        v = chi_or_zero(F(3, 2) + 6 * n, *twist(RHO_S, RHO_T, 12 * n))
        dims[n] = None if v is None else int(v)
    reproduces_c8 = all(dims[n] == 3 * n for n in range(5))
    adm_unit = [r for r in ALLOWED if det_exponent(r + 12)[0] == 0]
    threes = sorted((r, m) for r in ALLOWED for m in MS if abs(m) < 24 and det_exponent(r + m)[0] == 0
                    and index0(r, m) is not None and abs(index0(r, m)) == 3)
    least = min(abs(m) for (_, m) in threes) if threes else None
    as_fraction = F(least, 12) if least is not None else None
    reproduces_w134 = as_fraction == F(17, 24)
    return {"dims at the plant's n units": dims, "the plant's unit admissible at": adm_unit,
            "the least three in the plant's units": str(as_fraction),
            "reproduces C8 (3n)": reproduces_c8, "reproduces W134 (17/24)": reproduces_w134,
            "fails both": (not reproduces_c8) and (not reproduces_w134)}


def P2():
    """the dressing on the weight only: weight 3/2 + m/2, character chi_eta^r unchanged"""
    def idx(r, m):
        S, T = twist(RHO_S, RHO_T, r)
        v = chi_or_zero(F(3, 2) + F(m, 2), S, T)
        return None if v is None else -v
    c8 = all(idx(0, 24 * n) == -3 * n for n in range(5))
    adm = [(r, m) for r in ALLOWED for m in MS if det_exponent(r)[0] == 0]
    threes = [(r, m) for (r, m) in adm if abs(m) < 24 and idx(r, m) is not None and abs(idx(r, m)) == 3]
    least = min((abs(m) for (_, m) in threes), default=None)
    return {"reproduces C8 (3n at whole units)": bool(c8), "admissible data": len(adm),
            "reproduces W134 (17/24)": least == 17}


def CT():
    S, T = conj(RHO_S), conj(RHO_T)
    return {"the conjugate hand allows weight 3/2 at no allowed twist and no whole unit": all(
        not allowed(F(3, 2) + 12 * n, twist(S, T, r + 24 * n)[0]) for r in ALLOWED for n in range(-2, 3))}


# ---------------------------------------------------------------- smoke (outside the population)
def smoke(main):
    w45 = load(main, "frontier/B1632_w45_verified_on_main/verification/w45_on_main.py", "w45")
    zf = load(main, "frontier/B1730_the_zero_free_higgs_lines/verification/the_zero_free_lines.py", "zf")
    b = load(main, "frontier/B1641_w46_on_main_and_the_two_objects/verification/w46_on_main.py", "b1641",
             strip_from="# ---- H ----")
    ok = {}
    one = ident(1)
    ok["exact chi runs on 1-dim characters"] = [str(chi(F(k, 2), *eta_char(k, 1))) is not None for k in range(1, 6)]
    ok["main's float chi callable"] = isinstance(w45.chi(0.5, *[x.numeric() for x in eta_char(1, 1)]), float)
    ok["Mono algebra on a 4-cycle"] = (Mono([1, 2, 3, 0], [F(1, 5)] * 4).inv() * Mono([1, 2, 3, 0], [F(1, 5)] * 4)
                                       == ident(4))
    ok["B1641 pieces loaded"] = len(b["pieces"]) == 2
    ok["dressed q-series runs (r = 2, not an allowed twist; empty by construction)"] = dim_dressed(zf, 2, 0, 1)[1] >= 0
    ok["E8 roots generated"] = len(e8_roots()) == 240
    ok["exact projection runs on a toy pair"] = len(project_out((F(1),) * 8, [(F(1), F(-1)) + (F(0),) * 6])) == 8
    ok["dressed q-series runs at (r, m) = (0, 2): not admissible, not a whole unit"] = dim_dressed(zf, 0, 2, 1)[1] > 0
    ok["det exponent runs on a 1-dim character"] = det_exponent(5, *eta_char(0, 1))[1] in (True, False)
    ok["trivial rep chi_0"] = chi(0, one, one) == 1
    print(json.dumps({k: bool(v if not isinstance(v, list) else all(v)) for k, v in ok.items()}, indent=1))


def main():
    main_dir = pathlib.Path(sys.argv[1]).resolve()
    if "--smoke" in sys.argv[2:]:
        smoke(main_dir)
        return
    w45 = load(main_dir, "frontier/B1632_w45_verified_on_main/verification/w45_on_main.py", "w45")
    zf = load(main_dir, "frontier/B1730_the_zero_free_higgs_lines/verification/the_zero_free_lines.py", "zf")
    b1641 = load(main_dir, "frontier/B1641_w46_on_main_and_the_two_objects/verification/w46_on_main.py", "b1641",
                 strip_from="# ---- H ----")
    r0, ok0 = R0(w45)
    r1, ok1 = R1(zf, b1641)
    r2, ok2 = R2(zf)
    r3, ok3, tab = R3()
    r4, ok4, threes = R4(tab, zf, b1641, w45)
    r5, ok5 = R5(threes)
    r6, ok6 = R6(threes)
    r7, ok7 = R7()
    p1, p2, ct = P1(), P2(), CT()
    cells = {"R0": ok0, "R1": ok1, "R2": ok2, "R3": ok3, "R4": ok4, "R5": ok5, "R6": ok6, "R7": ok7,
             "P1 fails both": p1["fails both"],
             "P2 reproduces C8 and fails W134": p2["reproduces C8 (3n at whole units)"]
             and not p2["reproduces W134 (17/24)"], "CT": all(ct.values())}
    out = {"row": "P-610", "script sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
           "R0": r0, "R1": r1, "R2": r2, "R3": r3, "R4": r4, "R5": r5, "R6": r6, "R7": r7, "P1": p1, "P2": p2,
           "CT": ct, "cells": {k: bool(v) for k, v in cells.items()}}
    text = json.dumps(out, indent=1, default=str) + "\n"
    (HERE / "r610_results.json").write_text(text, encoding="utf-8")
    for name in ("R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7"):
        for k, v in out[name]["checks"].items():
            print(f"{name}  {'PASS' if v else 'FAIL'}  {k}")
    for k in ("P1", "P2", "CT"):
        print(k, json.dumps(out[k], default=str))
    print("cells:", json.dumps(out["cells"]))
    print("output sha256:", hashlib.sha256(text.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
