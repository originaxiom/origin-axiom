"""The referee read's checks: the referee lane's load-bearing numbers, recomputed on this seat's code (POST HOC).

Not a sealed arc: no rule and no prediction. Every number here was first computed in scratch on 2026-10-17 while
reading the referee lane's branch (referee/B1668_the_price_of_the_nineteen @ 0c781663f), and was seen before this
file existed. This file repeats those checks in one run; its output is committed as written. The relay to the referee
lane cites it (docs/handoffs/SM_TO_REFEREE_LANE_2026-10-17_THE_REFEREE_READ.md).

Run from the repository root: python3 docs/dossiers/the_weave_2026-10-07/the_referee_read_checks.py
"""
import itertools
import json
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 30
HERE = Path(__file__).resolve().parent
OUT = {"what": "the referee read's checks (post hoc; every number seen in scratch first)",
       "branch read": "referee/B1668_the_price_of_the_nineteen @ 0c781663f"}
PHI = (1 + 5 ** 0.5) / 2


def th(tau):
    q = mp.exp(1j * mp.pi * tau)
    return mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)


def eta(tau):
    return mp.exp(2j * mp.pi * tau / 24) * mp.qp(mp.exp(2j * mp.pi * tau))


def eis(tau, k, c):
    q = mp.exp(2j * mp.pi * tau)
    return 1 + c * mp.nsum(lambda n: n ** (k - 1) * q ** n / (1 - q ** n), [1, mp.inf])


def E4(tau):
    return eis(tau, 4, 240)


def E6(tau):
    return eis(tau, 6, -504)


def jinv(tau):
    a, b = E4(tau) ** 3, E6(tau) ** 2
    return 1728 * a / (a - b)


def Y1(tau):
    t2, t3, t4 = [x ** 2 for x in th(tau)]
    return mp.matrix([[0, t4, t3], [t4, 0, t2], [t3, t2, 0]])


def svals(M):
    return np.sort(np.linalg.svd(np.array(M.tolist() if hasattr(M, "tolist") else M, dtype=complex),
                                 compute_uv=False))[::-1]


def wrap(a):
    return float((a + mp.pi) % (2 * mp.pi) - mp.pi)


# ------------------------------------------------------------ R1. N8a: the sum rule and the half floor
rng = np.random.default_rng(1)
dev, floor = 0.0, 1.0
for _ in range(20000):
    a, b, c = rng.normal(size=3) + 1j * rng.normal(size=3)
    s = svals(np.array([[0, a, b], [a, 0, c], [b, c, 0]]))
    dev = max(dev, abs(s[0] - s[1] - s[2]) / s[0])
    floor = min(floor, s[1] / s[0])
OUT["R1 zero-diagonal complex symmetric 3x3 (20000 draws)"] = {
    "max |s1 - s2 - s3| / s1": dev, "min s2 / s1": round(floor, 6)}

# ------------------------------------------------------------ R2. the weight-1 coupling
r2 = {}
for tau in [mp.mpc(0.137, 1.291), mp.mpc(-0.284, 2.173), mp.mpc(0.4, 0.9)]:
    r2[f"det Y1 / (8 eta^6) at {mp.nstr(tau, 4)}"] = mp.nstr(mp.det(Y1(tau)) / (8 * eta(tau) ** 6), 15)
for name, tau in [("omega", mp.exp(2j * mp.pi / 3)), ("i", mp.mpc(0, 1))]:
    s = svals(Y1(tau))
    r2[f"spectrum / s1 at {name}"] = [round(float(x), 10) for x in s / s[0]]
r2["phi^-1, phi^-2"] = [round(1 / PHI, 10), round(PHI ** -2, 10)]
OUT["R2 Y1 = theta constants off the diagonal"] = r2

# ------------------------------------------------------------ R3. the Dedekind phase law
OUT["R3 12 arg eta(x+iy) - pi x"] = {
    f"({x}, {y})": mp.nstr(12 * mp.arg(eta(mp.mpc(x, y))) - mp.pi * x, 6)
    for x, y in [(0.3, 2.5), (-0.45, 2.5), (0.3, 1.0), (0.45, 0.9)]}

# ------------------------------------------------------------ R4. the symmetric square and the flux-4 triplet
tau = mp.mpc(0.21, 1.1)
t2, t3, t4 = th(tau)
s2, s3, _ = th(2 * tau)
rho_T = [Fr(1, 8), Fr(3, 8), Fr(7, 8)]                          # rho = chi_eta^21 (x) rho_u, its t-exponents
W2 = [Fr(j * j, 4) for j in (0, 1)]                                # the flux-2 doublet: e^{i pi j^2 / 2}
sym2 = sorted({(a + b) % 1 for i, a in enumerate(W2) for b in W2[i:]})
W4e = sorted(Fr(j * j, 8) % 1 for j in (0, 1, 2))                  # the flux-4 even triplet: e^{i pi j^2 / 4}


def shifts(A, B):
    return [k for k in range(24) if sorted((x + Fr(k, 24)) % 1 for x in A) == sorted(B)]


OUT["R4 the triplet as a square"] = {
    "|th3^2 - (p^2 + q^2)|, |th2^2 - 2pq|, |th4^2 - (p^2 - q^2)|, (p, q) = (th3(2tau), th2(2tau))":
        [mp.nstr(abs(t3 ** 2 - (s3 ** 2 + s2 ** 2)), 3), mp.nstr(abs(t2 ** 2 - 2 * s2 * s3), 3),
         mp.nstr(abs(t4 ** 2 - (s3 ** 2 - s2 ** 2)), 3)],
    "t-exponents (turns): rho, Sym2(flux-2 doublet), flux-4 even triplet":
        [[str(x) for x in rho_T], [str(x) for x in sym2], [str(x) for x in W4e]],
    "characters chi_eta^k taking Sym2(flux-2) onto rho": shifts(sym2, rho_T),
    "characters chi_eta^k taking the flux-4 even triplet onto rho": shifts(W4e, rho_T)}

# ------------------------------------------------------------ R5. the eta^6 multiplier on words, both conventions
up = mp.matrix([[1, 1], [0, 1]])
lo = mp.matrix([[1, 0], [1, 1]])
tau0 = mp.mpc(0.1, 0.8)
tally = {"L = upper shear: i^(#L-#R)": 0, "L = lower shear: i^(#R-#L)": 0}
nwords = 0
for n in range(2, 9):
    for w in itertools.product("LR", repeat=n):
        w = "".join(w)
        if "L" not in w or "R" not in w:
            continue
        nwords += 1
        k = w.count("L") - w.count("R")
        for conv, (A, B, sign) in {"L = upper shear: i^(#L-#R)": (up, lo, 1),
                                   "L = lower shear: i^(#R-#L)": (lo, up, -1)}.items():
            M = mp.eye(2)
            for ch in w:
                M = M * (A if ch == "L" else B)
            a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
            e6 = eta((a * tau0 + b) / (c * tau0 + d)) ** 6 / ((c * tau0 + d) ** 3 * eta(tau0) ** 6)
            if abs(e6 - 1j ** (sign * k)) < 1e-15:
                tally[conv] += 1
OUT["R5 eta^6 multiplier against the period-phase law"] = {"words (both letters, length 2..8)": nwords, **tally}

# ------------------------------------------------------------ R6. the weave's trace triples are 3 x Markov
pairs = {"LR, RL^-1": lambda A, B: (A @ B, np.linalg.inv(B @ A)), "LR, RL": lambda A, B: (A @ B, B @ A),
         "LR, LRRL": lambda A, B: (A @ B, A @ B @ B @ A), "LRRL, LRLRRL": lambda A, B: (A @ B @ B @ A,
                                                                                      A @ B @ A @ B @ B @ A)}
A, B = np.array([[1, 1], [0, 1]]), np.array([[1, 0], [1, 1]])
r6 = {}
for name, f in pairs.items():
    g, h = f(A, B)
    x, y, z = (int(round(np.trace(m))) for m in (g, h, g @ h))
    r6[name] = {"traces": [x, y, z], "x^2+y^2+z^2-xyz": x * x + y * y + z * z - x * y * z,
                "Markov triple (/3)": [x // 3, y // 3, z // 3],
                "a^2+b^2+c^2-3abc": (x // 3) ** 2 + (y // 3) ** 2 + (z // 3) ** 2 - 3 * (x // 3) * (y // 3) * (z // 3)}
OUT["R6 trace triples"] = r6

# ------------------------------------------------------------ R7. the fibre frame's floor: real and complex Higgs
rng = np.random.default_rng(7)


def iso():
    u, v = rng.normal(size=3), rng.normal(size=3)
    v -= (v @ u) / (u @ u) * u
    v *= np.linalg.norm(u) / np.linalg.norm(v)
    return u + 1j * v                                  # u.u = v.v and u.v = 0, so rho.rho = 0


def fibre(rho, a):
    Y = np.outer(rho, a) + np.outer(a, rho) - (rho @ a) * np.eye(3)
    s = svals(Y)
    return s[1] / s[0], s[2] / s[0]


mr, mc, s3max = 1.0, 1.0, 0.0
for _ in range(20000):
    rho = iso()
    mr = min(mr, fibre(rho, rng.normal(size=3))[0])
    m, z = fibre(rho, rng.normal(size=3) + 1j * rng.normal(size=3))
    mc, s3max = min(mc, m), max(s3max, z)
rho = iso()
OUT["R7 Y(a) = a rho^T + rho a^T - (a.rho) 1, rho isotropic (20000 draws each)"] = {
    "min m, real a": round(mr, 6), "min m, complex a": round(mc, 6),
    "m at a = conj(rho) (on the isotropic cone)": round(fibre(rho, rho.conj())[0], 12),
    "max s3 / s1 (the null vector)": s3max}

# ------------------------------------------------------------ R8. the determinant character
rT_u = np.array([[1j, 0, 0], [0, 0, 1], [0, 1, 0]])               # on (theta2^2, theta3^2, theta4^2)
rS_u = -1j * np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
rT = np.exp(2j * np.pi * 21 / 24) * rT_u
rS = np.exp(-1j * np.pi / 4) ** 21 * rS_u
chiT, chiS = np.exp(2j * np.pi / 24), np.exp(-1j * np.pi / 4)      # chi_eta on t and s
e_t = [k for k in range(24) if abs(np.linalg.det(rT) - chiT ** k) < 1e-12]
e_s = [k for k in range(24) if abs(np.linalg.det(rS) - chiS ** k) < 1e-12]
quark = {}
for sQ, su, sd in itertools.product((1, -1), repeat=3):
    quark[f"(sQ, su, sd) = ({sQ}, {su}, {sd})"] = (9 * (2 * sQ + su + sd)) % 24
OUT["R8 det rho as a power of chi_eta"] = {
    "k with det rho(t) = chi_eta(t)^k": e_t, "k with det rho(s) = chi_eta(s)^k (mod 8)": e_s,
    "QCD character exponent 9(2 sQ + su + sd) mod 24 (+1 = T, -1 = Tbar)": quark}

# ------------------------------------------------------------ R9. weight 3, T (x) T: where theta-bar can vanish
# det(Y_s + r Y_a) = c eta^6 E6 in each sector (the referee lane's N10a; also forced by dim M_6 = 1), c real.
r9 = {}
for y in [1.0, 1.2, 1.5, 2.0, 2.5]:
    row = {}
    for x in [0.05, 0.15, 0.25, 0.35, 0.45]:
        t = mp.mpc(x, y)
        row[str(x)] = [round(wrap(12 * mp.arg(eta(t)) + 2 * mp.arg(E6(t))), 3), round(wrap(mp.arg(jinv(t) - 1728)), 3)]
    r9[f"y = {y}"] = row
OUT["R9 phases [12 arg eta + 2 arg E6 (no counterterm), arg(j - 1728) (after the eta counterterm)]"] = r9


def phase(x, y):
    t = mp.mpc(x, y)
    return 12 * mp.arg(eta(t)) + 2 * mp.arg(E6(t))


roots = {}
for y, lo_, hi_ in [(1.0, 0.25, 0.35), (1.2, 0.15, 0.25)]:
    a, b = mp.mpf(lo_), mp.mpf(hi_)
    for _ in range(60):
        m = (a + b) / 2
        if mp.sin(phase(a, y)) * mp.sin(phase(m, y)) <= 0:
            b = m
        else:
            a = m
    x = (a + b) / 2
    roots[f"y = {y}"] = {"x": mp.nstr(x, 10), "|tau|": mp.nstr(abs(mp.mpc(x, y)), 6),
                         "phase there": mp.nstr(phase(x, y), 5)}
OUT["R9 interior zeros of the no-counterterm phase (bisection on sin)"] = roots

(HERE / "the_referee_read_checks.json").write_text(json.dumps(OUT, indent=1, ensure_ascii=False) + "\n",
                                                   encoding="utf-8")
print(json.dumps(OUT, indent=1, ensure_ascii=False))
