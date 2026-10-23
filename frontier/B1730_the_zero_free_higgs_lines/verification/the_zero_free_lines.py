"""B1730 (P-300, its W133 part, and the web seat's extension): the zero-free weight-3/2 Higgs lines, verified on main.
No data.  Main's own code; the only shared piece is B1691's exact q-series module (x = q^(1/8), Gaussian rationals).
  A  the multiplier rho_R from R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4) itself (theta functions summed in tau), against
     W64's rho(T) = e^{i pi/4} L^-1, rho(S) = e^{i pi/4} P; the character identity: the product of the non-zero entries of
     rho(T), rho(S) is chi_eta^21 exactly, so N(F) = F_i F_j F_k of a weight-3/2 section of rho (x) chi_eta^r carries
     chi_eta^(21+3r), and N/eta^9 can be a zero-free constant only if r = 4 mod 8
  B  the family F_a = eta^(3-a) (eps th2^a, eps th4^a, i th3^a), a = 2 mod 4, eps = i^((a+2)/2): its multiplier is
     rho (x) chi_eta^r with r = 2a mod 24 (under T and S, at random tau, a = -30 ... 50), and N(F_a) = i 2^a eta^9
  C  the spaces h(r, n) (weight 3/2, rho (x) chi_eta^r, n units at the cusp) for r in {0, 4, 12, 20}, n in {0, 1, 2},
     exactly: F = eta^r G, G = A R + B DR + C D2R with A, B, C level-one weakly holomorphic (R, DR, D2R a free basis:
     B1691's Wronskian = const eta^9); the dimension at two pole allowances; which F_a lie in each, by line orders and
     by exact membership in the span; whether they span it
    python3 -B the_zero_free_lines.py      # writes the_zero_free_lines.json beside itself
Importing computes nothing."""
import sys, json, math, random, pathlib
from fractions import Fraction as F
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
Q1691 = ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification"
RS = (0, 4, 12, 20)
NS = (0, 1, 2)
AS = tuple(range(-30, 51, 4))                      # a = 2 mod 4


# ---------------------------------------------------------------- A, B: numerics (theta functions summed in tau)
def _num():
    import mpmath as mp
    mp.mp.dps = 30
    def th2(t): return mp.fsum(mp.exp(1j * mp.pi * t * (n + mp.mpf(1) / 2) ** 2) for n in range(-40, 40))
    def th3(t): return mp.fsum(mp.exp(1j * mp.pi * t * n * n) for n in range(-40, 41))
    def th4(t): return mp.fsum((-1) ** n * mp.exp(1j * mp.pi * t * n * n) for n in range(-40, 41))
    def eta(t):
        q = mp.exp(2j * mp.pi * t); p = mp.mpf(1)
        for n in range(1, 400): p *= 1 - q ** n
        return mp.exp(1j * mp.pi * t / 12) * p
    return mp, th2, th3, th4, eta


def part_a():
    import sympy as sp
    mp, th2, th3, th4, eta = _num()
    def R(t):
        a, b, c = th2(t), th3(t), th4(t); d = a * b * c
        return mp.matrix([-a * a / d, -c * c / d, 1j * b * b / d])
    rng = random.Random(1730)
    ts = [mp.mpc(rng.uniform(-0.4, 0.4), rng.uniform(0.9, 1.6)) for _ in range(3)]
    X = mp.matrix(3, 3); XT = mp.matrix(3, 3); XS = mp.matrix(3, 3)
    for j, t in enumerate(ts):
        r0, r1, r2 = R(t), R(t + 1), R(-1 / t) * mp.power(t, mp.mpf(1) / 2)      # R(-1/tau) = tau^(-1/2) M_S R(tau)
        for i in range(3): X[i, j], XT[i, j], XS[i, j] = r0[i], r1[i], r2[i]
    MT, MS = XT * mp.inverse(X), XS * mp.inverse(X)
    w = mp.exp(1j * mp.pi / 4)
    Linv = mp.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]]); Pm = mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    dT = max(abs(MT[i, j] - w * Linv[i, j]) for i in range(3) for j in range(3))
    dS = max(abs(MS[i, j] - w * Pm[i, j]) for i in range(3) for j in range(3))
    # the character identity, exactly
    z = sp.exp(sp.I * sp.pi / 4)
    rT = z * sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]]); rS = z * sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    def mono(M): return sp.prod([e for e in M if e != 0])
    chiT, chiS = sp.exp(2 * sp.pi * sp.I / 24), sp.exp(-sp.I * sp.pi / 4)
    idT = sp.simplify(mono(rT) - chiT ** 21) == 0; idS = sp.simplify(mono(rS) - chiS ** 21) == 0
    # N/eta^9 at weight 0 carries chi_eta^(12 + 3r): trivial exactly when 24 | 12 + 3r
    allowed = [r for r in range(24) if (12 + 3 * r) % 24 == 0]
    return {"rho_T_from_R_vs_W64": float(dT), "rho_S_from_R_vs_W64": float(dS),
            "monomial_product_T_is_chi_eta^21": bool(idT), "monomial_product_S_is_chi_eta^21": bool(idS),
            "r_mod_24_with_trivial_character_of_N_over_eta9": allowed}


def part_b():
    mp, th2, th3, th4, eta = _num()
    w = mp.exp(1j * mp.pi / 4)
    Linv = mp.matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]]); Pm = mp.matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    def Fa(a, t):
        eps = 1j ** ((a + 2) // 2); e = eta(t) ** (3 - a)
        return mp.matrix([e * eps * th2(t) ** a, e * eps * th4(t) ** a, e * 1j * th3(t) ** a])
    rng = random.Random(17300); ts = [mp.mpc(rng.uniform(-0.45, 0.45), rng.uniform(0.95, 1.5)) for _ in range(3)]
    worst = {"T": 0.0, "S": 0.0, "norm": 0.0}; per = {}
    for a in AS:
        r = (2 * a) % 24; dT = dS = dN = 0.0
        for t in ts:
            f0, f1, f2 = Fa(a, t), Fa(a, t + 1), Fa(a, -1 / t)
            gT = mp.exp(2j * mp.pi * r / 24) * w * (Linv * f0)
            gS = mp.power(t, mp.mpf(3) / 2) * mp.exp(-1j * mp.pi * r / 4) * w * (Pm * f0)
            sc = max(abs(f0[i]) for i in range(3))
            dT = max(dT, max(abs(f1[i] - gT[i]) for i in range(3)) / max(abs(f1[i]) for i in range(3)))
            dS = max(dS, max(abs(f2[i] - gS[i]) for i in range(3)) / max(abs(f2[i]) for i in range(3)))
            dN = max(dN, abs(f0[0] * f0[1] * f0[2] / (1j * 2 ** a * eta(t) ** 9) - 1))
        per[a] = {"r": r, "eps": int(round(float(mp.re(1j ** ((a + 2) // 2))))), "T": float(dT), "S": float(dS), "N_over_i2^a_eta9_minus_1": float(dN)}
        worst["T"], worst["S"], worst["norm"] = max(worst["T"], dT), max(worst["S"], dS), max(worst["norm"], dN)
    return {"worst_relative": {k: float(v) for k, v in worst.items()}, "per_a": per}


# ---------------------------------------------------------------- C: the spaces, exactly
_E = {}


def _exact():
    if not _E:
        sys.path.insert(0, str(Q1691))
        import qseries
        qseries.N = 160                                                          # x^160 = q^20: exact far past every order compared
        from qseries import S, theta2, theta3, E2, E4, E6, serre
        th2, th3, th4 = theta2(), theta3(1), theta3(-1)
        pi3 = th2 * th3 * th4                                                    # = 2 eta^3
        di = pi3.inv()
        R = [-(th2 * th2) * di, -(th4 * th4) * di, (th3 * th3) * S.c(0, 1) * di]
        e2, e4, e6 = E2(), E4(), E6()
        D1 = [serre(c, F(-1, 2), e2) for c in R]; D2 = [serre(c, F(3, 2), e2) for c in D1]
        Delta = (e4 * e4 * e4 - e6 * e6) * S.c(F(1, 1728))
        _E.update(S=S, th2=th2, th3=th3, th4=th4, pi3=pi3, R=R, D1=D1, D2=D2, e4=e4, e6=e6, Delta=Delta, Dinv=Delta.inv())
    return _E


def _pow(s, k):
    E = _exact(); S = E["S"]
    if k < 0: s, k = s.inv(), -k
    out = S.c(1)
    while k:                                                                    # repeated squaring
        if k & 1: out = out * s
        k >>= 1
        if k: s = s * s
    return out


def _Mbasis(w):
    E = _exact(); res = []
    if w < 0: return res
    for a in range(w // 4 + 1):
        for b in range(w // 6 + 1):
            if 4 * a + 6 * b == w: res.append(_pow(E["e4"], a) * _pow(E["e6"], b))
    return res


def _lines(v):
    E = _exact(); I = E["S"].c(0, 1)
    return [v[0], v[1] + I * v[2], v[1] - I * v[2]]


def bounds(r, n):
    """G's line bounds in x = q^(1/8): each line of F = eta^r G at least the least positive exponent of its class minus n"""
    out = []
    for e in (F(1, 8), F(7, 8), F(3, 8)):                                     # lines P, M = v+, N of rho_T
        c = (e + F(r, 24)) % 1
        if c == 0: c = F(1)
        out.append(int(8 * (c - F(r, 24) - n)))
    return out


def _coef(s, k):
    import sympy as sp
    a, b = s.d.get(k, (F(0), F(0)))
    return sp.Rational(a.numerator, a.denominator) + sp.I * sp.Rational(b.numerator, b.denominator)


def space(r, n, M):
    """a basis (as lists of three G-line series) of h(r, n) with pole allowance M at the cusp for A, B, C"""
    import sympy as sp
    E = _exact(); S = E["S"]
    k2 = 3 - r                                                                  # 2k, k = 3/2 - r/2
    gens = []
    for vec, wt in ((E["R"], (k2 + 1) // 2), (E["D1"], (k2 - 3) // 2), (E["D2"], (k2 - 7) // 2)):
        f = _pow(E["Dinv"], M)
        for b in _Mbasis(wt + 12 * M):
            gens.append(_lines([f * b * c for c in vec]))
    bd = bounds(r, n); rows = []
    for li in range(3):
        ks = sorted({k for g in gens for k in g[li].d if k < bd[li]})
        for k in ks: rows.append([_coef(g[li], k) for g in gens])
    A = sp.Matrix(rows) if rows else sp.zeros(0, len(gens))
    ker = A.nullspace() if len(gens) else []
    basis = []
    for v in ker:
        comb = [S(), S(), S()]
        for c, g in zip(v, gens):
            c = sp.nsimplify(c); re, im = sp.fraction(sp.re(c)), sp.fraction(sp.im(c))
            cc = S.c(F(int(re[0]), int(re[1])), F(int(im[0]), int(im[1])))
            comb = [comb[i] + cc * g[i] for i in range(3)]
        basis.append(comb)
    return basis, len(gens)


import functools


@functools.lru_cache(maxsize=None)
def member(a, r):
    """G_a = eta^-r F_a = (th2 th3 th4 / 2)^m (eps th2^a, eps th4^a, i th3^a), m = (3 - a - r)/3, as its three lines"""
    E = _exact(); S = E["S"]
    m = (3 - a - r) // 3; assert 3 * m == 3 - a - r
    eps = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}[((a + 2) // 2) % 4]
    pre = _pow(E["pi3"] * S.c(F(1, 2)), m)
    v = [pre * S.c(*eps) * _pow(E["th2"], a), pre * S.c(*eps) * _pow(E["th4"], a), pre * S.c(0, 1) * _pow(E["th3"], a)]
    return _lines(v)


def in_span(vec, basis, kmax=40):
    import sympy as sp
    lo = min(min(s.d) for b in basis + [vec] for s in b if s.d)
    def flat(b): return [_coef(b[li], k) for li in range(3) for k in range(lo, kmax)]
    Bm = sp.Matrix([flat(b) for b in basis]) if basis else sp.zeros(0, 3 * (kmax - lo))
    return (Bm.rank() if basis else 0) == sp.Matrix([flat(b) for b in basis] + [flat(vec)]).rank()


def part_c():
    res = {}
    for r in RS:
        for n in NS:
            b4, ng4 = space(r, n, 4); b6, ng6 = space(r, n, 6)
            bd = bounds(r, n)
            mem = []
            for a in range(-30, 71, 4):
                if (2 * a - r) % 24: continue
                L = member(a, r)
                if all(L[i].ord() is not None and L[i].ord() >= bd[i] for i in range(3)): mem.append(a)
            spans = all(in_span(member(a, r), b6) for a in mem)
            # the members are independent: their P-line orders differ (m + a = 1 + 2a/3 - r/3)
            ords = [member(a, r)[0].ord() for a in mem]
            res["h(%d,%d)" % (r, n)] = {"bounds_x": bd, "dim_M4": len(b4), "dim_M6": len(b6), "members_a": mem,
                                         "members_in_span_exactly": spans, "member_P_orders": ords,
                                         "members_distinct_orders": len(set(ords)) == len(ords),
                                         "count_formula_3n+[r=4]": 3 * n + (1 if r == 4 else 0)}
    return res


def main():
    out = {"A": part_a(), "B": part_b(), "C": part_c()}
    json.dump(out, open(HERE / "the_zero_free_lines.json", "w"), indent=1, default=str)
    print(json.dumps({"A": out["A"], "B_worst": out["B"]["worst_relative"]}, indent=1, default=str))
    for k, v in out["C"].items():
        print(k, "bounds", v["bounds_x"], "dim", v["dim_M4"], v["dim_M6"], "members", v["members_a"], "in span", v["members_in_span_exactly"], "formula", v["count_formula_3n+[r=4]"])


if __name__ == "__main__":
    main()
