#!/usr/bin/env python3
"""chat1's check of the SM seat's W133 (relay 219's asks to the web seat), on chat1's own code. A VERIFICATION, not a
test against data: nothing here reads a mass, a mixing or any measured number.

The objects (as W133 states them; nothing here imports the SM seat's code):
  R = (-th2^2, -th4^2, i th3^2) / (th2 th3 th4), weight -1/2, components in the parity basis (i, j, k); rho_T is its
  multiplier.  Lines (the T-eigenbasis): l_i = R_i, l_+ = R_j + i R_k, l_- = R_j - i R_k.  x = q^(1/8).
  h(r, n): weight-3/2 sections F with multiplier rho_T (x) chi_eta^r and n uniform units at the cusp, i.e. each line's
  q-exponents >= its least positive class minus n.  Writing F = eta^r G, G has multiplier rho_T and weight 3/2 - r/2.
  N(F) = F_i F_j F_k; PF1-W asks N(F) to have no zero on the upper half plane.

  C1  rho_T from R's own transformation, numerically at random tau: R(tau + 1) = z8 Li R(tau) and
      R(-1/tau) = tau^(-1/2) z8 Pm R(tau) (principal branch), z8 = e^(i pi/4); W133's matrices.
  C2  P1's character: the product of rho's non-zero entries equals det rho . sgn and equals chi_eta^21 on S and T
      (chi_eta(T) = e^(2 pi i/24), chi_eta(S) = e^(-i pi/4) with automorphy tau^(1/2)); chi_eta^(21+3r) = chi_eta^9
      exactly for r = 4 mod 8.
  C3  The Wronskian det(R, DR, D^2R) (Serre derivatives, line basis) is a constant times eta^9 to the series'
      precision, so R, DR, D^2R are a free basis over level-one weakly holomorphic forms (Cramer).
  C4  dim h(r, n) on chi_eta-twists r = 0, 4, 12, 20 and n = 0, 1, 2, from G = A R + B DR + C D^2R, A, B, C spanned by
      E4^a E6^b Delta^(-m) (m <= MMAX), with the line bounds; computed at two MMAX to show it is stable.
  C5  The family F_a = eta^(3-a) (e th2^a, e th4^a, i th3^a), a = 2 mod 4, e = i^((a+2)/2) (so e = -1 for a = 2 mod 8,
      W133's family, and e = +1 for a = 6 mod 8): numerically at random tau, F_a(tau + 1) = rho(T) chi_eta^r(T) F_a and
      F_a(-1/tau) = tau^(3/2) rho(S) chi_eta^r(S) F_a with r = 2a mod 24; N(F_a) = i 2^a eta^9.
  C6  Which F_a lie in each h(r, n) (exact line orders against the bounds), and whether their number equals dim h(r, n).
  C7  Each F_a in a window, written in C4's basis (exact linear algebra), to confirm membership independently of C6.
    python3 -B w133_check.py      # writes w133_check.json and w133_check_run.txt

First launch (f86b337c6, log kept as w133_check_run_launch1_wrong.txt): C1 and C5 failed numerically because mpmath's
jtheta takes the nome q^(1/2) and its principal q^(1/4) branch is wrong at Re tau outside (-1, 1); C4 counted
coefficient vectors over a dependent set (E4^a E6^b Delta^-m for every m <= MMAX, which E4^3 - E6^2 = 1728 Delta
relates).  Fixed here: thetas and eta summed directly in tau; the weakly holomorphic basis is Delta^-MMAX M_(k+12 MMAX)."""
import json, math, cmath, pathlib, random
from fractions import Fraction as Fr
import mpmath as mp
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 40
LOG, OUT = [], {}
XMAX = 120                                                   # series are carried to absolute x-order < XMAX (tracked)


def say(s):
    LOG.append(s); print(s, flush=True)


# ---------------------------------------------------------------- exact Laurent series in x with precision tracking
class Ser:
    def __init__(self, v, c, prec):
        self.v, self.prec = v, prec
        self.c = [Fr(a) for a in c[:max(0, prec - v)]]

    def co(self, k):
        assert k < self.prec, (k, self.prec)
        i = k - self.v
        return self.c[i] if 0 <= i < len(self.c) else Fr(0)

    def __add__(self, o):
        p = min(self.prec, o.prec); v = min(self.v, o.v)
        return Ser(v, [(self.co(k) if k >= self.v else 0) + (o.co(k) if k >= o.v else 0) for k in range(v, p)], p)

    def __neg__(self):
        return Ser(self.v, [-a for a in self.c], self.prec)

    def __sub__(self, o):
        return self + (-o)

    def scale(self, a):
        return Ser(self.v, [a * b for b in self.c], self.prec)

    def __mul__(self, o):
        v = self.v + o.v; p = min(self.prec + o.v, o.prec + self.v, XMAX)
        out = [Fr(0)] * max(0, p - v)
        for i, a in enumerate(self.c):
            if a == 0:
                continue
            for j, b in enumerate(o.c):
                if i + j >= len(out):
                    break
                if b:
                    out[i + j] += a * b
        return Ser(v, out, p)

    def norm(self):                                          # drop leading zeros
        i = 0
        while i < len(self.c) and self.c[i] == 0:
            i += 1
        return Ser(self.v + i, self.c[i:], self.prec)

    def inv(self):
        s = self.norm(); a0 = s.c[0]; n = s.prec - s.v
        out = [Fr(0)] * n; out[0] = 1 / a0
        for k in range(1, n):
            out[k] = -sum(s.c[j] * out[k - j] for j in range(1, min(k, len(s.c) - 1) + 1)) / a0
        return Ser(-s.v, out, -s.v + n)

    def pw(self, m):
        if m < 0:
            return self.inv().pw(-m)
        out = Ser(0, [1], XMAX)
        for _ in range(m):
            out = out * self
        return out

    def xd(self):                                            # x d/dx
        return Ser(self.v, [(self.v + i) * a for i, a in enumerate(self.c)], self.prec)

    def order(self):
        for i, a in enumerate(self.c):
            if a != 0:
                return self.v + i
        return None


def from_dict(d, prec):
    v = min(d) if d else 0
    c = [Fr(0)] * (prec - v)
    for k, a in d.items():
        if k < prec:
            c[k - v] += a
    return Ser(v, c, prec)


P = XMAX
TH2 = from_dict({(2 * n + 1) ** 2: 2 for n in range(0, 12)}, P)
TH3 = from_dict({4 * n * n: (2 if n else 1) for n in range(0, 12)}, P)
TH4 = from_dict({4 * n * n: (2 * (-1) ** n if n else 1) for n in range(0, 12)}, P)
ETA3 = from_dict({1 + 4 * n * (n + 1): (-1) ** n * (2 * n + 1) for n in range(0, 12)}, P)


def sigma(n, k):
    return sum(d ** k for d in range(1, n + 1) if n % d == 0)


E2 = from_dict({0: 1, **{8 * n: -24 * sigma(n, 1) for n in range(1, P // 8 + 1)}}, P)
E4 = from_dict({0: 1, **{8 * n: 240 * sigma(n, 3) for n in range(1, P // 8 + 1)}}, P)
E6 = from_dict({0: 1, **{8 * n: -504 * sigma(n, 5) for n in range(1, P // 8 + 1)}}, P)
DELTA = (E4 * E4 * E4 - E6 * E6).scale(Fr(1, 1728))
ETA24 = ETA3.pw(8)
OUT["series checks"] = {"th2 th3 th4 = 2 eta^3": all(((TH2 * TH3 * TH4) - ETA3.scale(2)).co(k) == 0 for k in range(0, 100)),
                        "Delta = eta^24": all((DELTA - ETA24).co(k) == 0 for k in range(8, 100)),
                        "th3^4 = th2^4 + th4^4": all((TH3.pw(4) - TH2.pw(4) - TH4.pw(4)).co(k) == 0 for k in range(0, 100))}
say(f"series checks: {OUT['series checks']}")


def D(f, k):                                                 # Serre derivative on weight k: (1/8) x d/dx - (k/12) E2
    return f.xd().scale(Fr(1, 8)) - (E2 * f).scale(Fr(k) / 12)


DEN = ETA3.scale(2).inv()                                    # 1/(th2 th3 th4)
# R in the line basis: l_i = -th2^2/(2 eta^3); l_+ = R_j + i R_k = -(th4^2 + th3^2)/(2 eta^3); l_- = (th3^2 - th4^2)/(2 eta^3)
R = {"i": -(TH2 * TH2 * DEN), "+": -((TH4 * TH4 + TH3 * TH3) * DEN), "-": (TH3 * TH3 - TH4 * TH4) * DEN}
DR = {l: D(R[l], Fr(-1, 2)) for l in R}
D2R = {l: D(DR[l], Fr(3, 2)) for l in R}
OUT["line orders of R, DR, D2R"] = {n: [s[l].order() for l in "i+-"] for n, s in (("R", R), ("DR", DR), ("D2R", D2R))}
say(f"line orders (x-units) of R, DR, D2R [i, +, -]: {OUT['line orders of R, DR, D2R']}")


# ---------------------------------------------------------------- C1, C2 numerically and exactly
def th(t):                                                   # direct sums in tau (no nome branch): th2, th3, th4
    t = mp.mpc(t)
    t2 = mp.fsum(mp.exp(1j * mp.pi * t * (n + mp.mpf(1) / 2) ** 2) for n in range(-40, 40))
    t3 = mp.fsum(mp.exp(1j * mp.pi * t * n * n) for n in range(-40, 41))
    t4 = mp.fsum((-1) ** n * mp.exp(1j * mp.pi * t * n * n) for n in range(-40, 41))
    return complex(t2), complex(t3), complex(t4)


def eta(t):                                                  # e^(i pi tau/12) prod (1 - q^n), directly in tau
    t = mp.mpc(t)
    q = mp.exp(2j * mp.pi * t)
    return complex(mp.exp(1j * mp.pi * t / 12) * mp.fprod(1 - q ** n for n in range(1, 400)))


def Rnum(t):
    t2, t3, t4 = th(t)
    return [-t2 ** 2 / (t2 * t3 * t4), -t4 ** 2 / (t2 * t3 * t4), 1j * t3 ** 2 / (t2 * t3 * t4)]


z8 = cmath.exp(1j * math.pi / 4)
Pm = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
Li = [[1, 0, 0], [0, 0, 1], [0, -1, 0]]


def mv(M, v):
    return [sum(M[i][j] * v[j] for j in range(3)) for i in range(3)]


rng = random.Random(133)
taus = [complex(rng.uniform(-0.5, 0.5), rng.uniform(0.8, 1.6)) for _ in range(5)]
c1 = 0.0
for t in taus:
    r0 = Rnum(t)
    c1 = max(c1, max(abs(a - z8 * b) for a, b in zip(Rnum(t + 1), mv(Li, r0))))
    c1 = max(c1, max(abs(a - t ** -0.5 * z8 * b) for a, b in zip(Rnum(-1 / t), mv(Pm, r0))))
OUT["C1 max deviation"] = c1
say(f"C1: R(tau+1) = z8 Li R and R(-1/tau) = tau^(-1/2) z8 Pm R, max deviation {c1:.1e}")
z = sp.exp(sp.I * sp.pi / 4)
rS, rT = z * sp.Matrix(Pm), z * sp.Matrix(Li)
prod_nz = lambda M: sp.prod([M[i, j] for i in range(3) for j in range(3) if M[i, j] != 0])
perm = lambda M: sp.Matrix(3, 3, lambda i, j: 1 if M[i, j] != 0 else 0).det()
chiS = lambda m: sp.exp(-sp.I * sp.pi * m / 4)
chiT = lambda m: sp.exp(2 * sp.pi * sp.I * m / 24)
eq = lambda u, v: sp.simplify(sp.expand_complex(u - v)) == 0
c2 = {"prod of entries = det . sgn (S, T)": eq(prod_nz(rS), rS.det() * perm(rS)) and eq(prod_nz(rT), rT.det() * perm(rT)),
      "det . sgn = chi_eta^21 (S, T)": eq(rS.det() * perm(rS), chiS(21)) and eq(rT.det() * perm(rT), chiT(21)),
      "r in 0..23 with chi_eta^(21+3r) = chi_eta^9": [r for r in range(24) if eq(chiS(21 + 3 * r), chiS(9)) and eq(chiT(21 + 3 * r), chiT(9))]}
OUT["C2"] = {k: (v if isinstance(v, list) else bool(v)) for k, v in c2.items()}
say(f"C2: {OUT['C2']}")

# ---------------------------------------------------------------- C3 the Wronskian
W = (R["i"] * (DR["+"] * D2R["-"] - DR["-"] * D2R["+"]) - DR["i"] * (R["+"] * D2R["-"] - R["-"] * D2R["+"])
     + D2R["i"] * (R["+"] * DR["-"] - R["-"] * DR["+"]))
Wq = (W * ETA3.pw(-3)).norm()
OUT["C3"] = {"Wronskian / eta^9 leading": str(Wq.c[0]), "order": Wq.v, "constant to x^": Wq.prec,
             "is constant": Wq.v == 0 and all(a == 0 for a in Wq.c[1:])}
say(f"C3: det(R, DR, D2R) / eta^9 = {Wq.c[0]} (x-order {Wq.v}), constant to x^{Wq.prec}: {OUT['C3']['is constant']}")


# ---------------------------------------------------------------- C4 dim h(r, n)
def bounds(r, n):                                            # G's line bounds in x-units: 8 (frac(e + r/24) - r/24 - n)
    out = {}
    for l, e in (("i", Fr(1, 8)), ("+", Fr(7, 8)), ("-", Fr(3, 8))):
        c = (e + Fr(r, 24)) % 1
        out[l] = int(8 * (c - Fr(r, 24) - n))
    return out


_PW = {}


def cpw(name, f, m):
    if (name, m) not in _PW:
        _PW[(name, m)] = f.pw(m)
    return _PW[(name, m)]


def wh_basis(k, mmax):                                       # level-one weakly holomorphic forms of weight k, pole <= mmax:
    out = []                                                 # Delta^-mmax M_(k + 12 mmax), whose monomials are independent
    for m in (mmax,):
        w = k + 12 * m
        if w < 0:
            continue
        for a in range(0, w // 4 + 1):
            if (w - 4 * a) % 6 == 0:
                b = (w - 4 * a) // 6
                out.append((f"E4^{a} E6^{b} Delta^-{m}", cpw("E4", E4, a) * cpw("E6", E6, b) * cpw("Delta", DELTA, -m)))
    return out


def space(r, n, mmax):
    k = Fr(3, 2) - Fr(r, 2)
    cols = []
    for gen, sec, kk in ((R, "A", k + Fr(1, 2)), (DR, "B", k - Fr(3, 2)), (D2R, "C", k - Fr(7, 2))):
        for name, f in wh_basis(int(kk), mmax) if kk == int(kk) else []:
            cols.append((f"{sec}: {name}", {l: f * gen[l] for l in "i+-"}))
    bd = bounds(r, n)
    rows = []
    for l in "i+-":
        lo = min(c[1][l].v for c in cols) if cols else 0
        for kx in range(lo, bd[l]):
            rows.append([c[1][l].co(kx) for c in cols])
    M = sp.Matrix(rows) if rows else sp.zeros(0, len(cols))
    ns = M.nullspace() if cols else []
    return cols, ns, bd


OUT["C4"] = {}
SPACES = {}
for r in (0, 4, 12, 20):
    for n in (0, 1, 2):
        dims = []
        for mmax in (4, 6):
            cols, ns, bd = space(r, n, mmax)
            dims.append(len(ns))
        SPACES[(r, n)] = (cols, ns, bd)
        OUT["C4"][f"r={r} n={n}"] = {"G bounds (x-units, i + -)": bd, "dim at MMAX 4, 6": dims}
        say(f"C4: dim h({r}, {n}) = {dims} at MMAX 4, 6; G's line bounds {bd}")


# ---------------------------------------------------------------- C5 the family, numerically
def eps(a):
    return 1j ** ((a + 2) // 2)


def Fnum(a, t):
    t2, t3, t4 = th(t); e = eps(a); h = eta(t) ** (3 - a)
    return [h * e * t2 ** a, h * e * t4 ** a, h * 1j * t3 ** a]


fam = list(range(-30, 51, 4))                                # a = 2 mod 4
c5 = {}
for a in fam:
    r = (2 * a) % 24
    dT = dS = dN = 0.0
    for t in taus[:3]:
        f0 = Fnum(a, t)
        dT = max(dT, max(abs(u - z8 * cmath.exp(2j * math.pi * r / 24) * w) / (abs(u) + 1e-300) for u, w in zip(Fnum(a, t + 1), mv(Li, f0))))
        dS = max(dS, max(abs(u - t ** 1.5 * z8 * cmath.exp(-1j * math.pi * r / 4) * w) / (abs(u) + 1e-300) for u, w in zip(Fnum(a, -1 / t), mv(Pm, f0))))
        N = f0[0] * f0[1] * f0[2]
        dN = max(dN, abs(N / (1j * 2 ** a * eta(t) ** 9) - 1))
    c5[a] = {"r": r, "T": dT, "S": dS, "N/(i 2^a eta^9) - 1": dN}
OUT["C5"] = {str(a): v for a, v in c5.items()}
worst = max(max(v["T"], v["S"], v["N/(i 2^a eta^9) - 1"]) for v in c5.values())
say(f"C5: F_a for a = -30..50, a = 2 mod 4, both signs: multiplier rho (x) chi_eta^(2a) under T and S and N = i 2^a eta^9, "
    f"worst relative deviation {worst:.1e}")


# ---------------------------------------------------------------- C6 the family against the bounds, exactly
def G_lines(a, r):                                           # G_a = F_a / eta^r = (eta^3)^m (e th2^a, e th4^a, i th3^a)
    t = (r - 2 * a) // 24; m = 1 - a - 8 * t                 # 3 - a - r = 3m
    assert 3 - a - r == 3 * m
    e = 1 if ((a + 2) // 2) % 4 == 0 else -1                 # i^((a+2)/2) is real (+-1) for a = 2 mod 4
    E = ETA3.pw(m); A2, A3, A4 = TH2.pw(a), TH3.pw(a), TH4.pw(a)
    # lines: i = e th2^a; + = (e th4^a) + i (i th3^a) = e th4^a - th3^a; - = e th4^a + th3^a
    return {"i": (A2 * E).scale(e), "+": (A4.scale(e) - A3) * E, "-": (A4.scale(e) + A3) * E}, e


OUT["C6"] = {}
for (r, n), (cols, ns, bd) in SPACES.items():
    if r == 0:
        continue
    inside = []
    for a in fam:
        if (2 * a) % 24 != r:
            continue
        g, e = G_lines(a, r)
        if all(g[l].order() >= bd[l] for l in "i+-"):
            inside.append((a, e))
    OUT["C6"][f"r={r} n={n}"] = {"family members inside (a, sign)": inside, "count": len(inside), "dim": len(ns)}
    say(f"C6: h({r}, {n}): family members inside {inside}; count {len(inside)} against dim {len(ns)}")


# ---------------------------------------------------------------- C7 membership by exact linear algebra in C4's basis
OUT["C7"] = {}
for (r, n), (cols, ns, bd) in SPACES.items():
    if r == 0 or n == 0 and r != 4:
        continue
    for a, e in OUT["C6"][f"r={r} n={n}"]["family members inside (a, sign)"]:
        g, _ = G_lines(a, r)
        # solve sum_j x_j * (nullspace vector j's G) = g on coefficients x^lo .. x^30, every line
        Gs = []
        for vj in ns:
            Gs.append({l: None for l in "i+-"})
            for l in "i+-":
                acc = None
                for i in range(len(cols)):
                    if vj[i] != 0:
                        term = cols[i][1][l].scale(Fr(vj[i].p, vj[i].q))
                        acc = term if acc is None else acc + term
                Gs[-1][l] = acc
        rows, rhs = [], []
        for l in "i+-":
            lo = min(min(G[l].v for G in Gs), g[l].v)
            hi = min(min(G[l].prec for G in Gs), g[l].prec, 40)
            for kx in range(lo, hi):
                rows.append([G[l].co(kx) for G in Gs]); rhs.append(g[l].co(kx))
        A_ = sp.Matrix(rows); b_ = sp.Matrix(rhs)
        sol, params = A_.gauss_jordan_solve(b_) if A_.rank() == A_.col_insert(A_.shape[1], b_).rank() else (None, None)
        OUT["C7"][f"r={r} n={n} a={a}"] = "in the span" if sol is not None else "NOT in the span"
        say(f"C7: h({r}, {n}), a = {a} (sign {e:+d}): {'in the span of the computed basis' if sol is not None else 'NOT in the span'}")
(HERE / "w133_check.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "w133_check_run.txt").write_text("\n".join(LOG) + "\n")
