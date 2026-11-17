"""Main's own recomputation of the web seat's W-A2 (2026-11-17; harvest row 1852), parts A to E, and one addition, F.
No data.  The web seat's script is not run or imported.
A  the lines of F_p^2 fixed by the act LR = [[2, 1], [1, 1]], every prime below 2000.
B  level 5's Weyl operators W(a, b) = X^a Z^b on C^5; conjugation by the Weil representation (B1951's rho) moves them by a
   linear map of F_5^2; compared with the record's transport T: (a, b) -> (a, b - a), S: (a, b) -> (-b, a) (B1724).
C  the five theta functions of degree 5 on the fibre: u -> u + 1/5 acts as Z, u -> u + tau/5 as X up to a common factor,
   u -> -u sends psi_j to psi_(-j); the parity split.
D  the frame's quaternion units as the level-2 Weyl operators; the T-eigenphases of the Higgs direction's triplet (from
   the frame's own q-series) against the Weil triplet's.
E  the rivals p = 3, 7, 11, 13: the anomalies of the even exterior powers under S(U(m) x U(n)).
F  (main's addition) how the generation blocks move under tau -> tau + 1, computed on frame C itself: the left unitary
   U_L with Y(tau + 1, w) Y(tau + 1, w)^dagger = U_L Y(tau, w') Y(tau, w')^dagger U_L^dagger at every point."""
import itertools, json, math, pathlib, sys
from fractions import Fraction as Fr
from math import comb
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
OUT = {}

# ---------------------------------------------------------------- A
def primes(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\0\0"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def fixed_lines(p):
    n = 0
    for v in [(1, y) for y in range(p)] + [(0, 1)]:
        w = ((2 * v[0] + v[1]) % p, (v[0] + v[1]) % p)
        if (w[0] * v[1] - w[1] * v[0]) % p == 0: n += 1
    return n


cnt = {p: fixed_lines(p) for p in primes(2000)}
one = [p for p, c in cnt.items() if c == 1]
rule = all(c == (1 if p == 5 else 2 if p % 5 in (1, 4) else 0) for p, c in cnt.items())
OUT["A_primes_with_one_fixed_line"] = one; OUT["A_rule_holds_below_2000"] = rule
print("A: primes below 2000 at which the act fixes exactly one line: %s; two lines exactly when p = +-1 mod 5, none otherwise: %s" % (one, rule))

# ---------------------------------------------------------------- B
z5 = np.exp(2j * np.pi / 5)
X = np.roll(np.eye(5), 1, axis=0).astype(complex)                       # X|x> = |x + 1>
Z = np.diag([z5 ** x for x in range(5)])
Wop = lambda a, b: np.linalg.matrix_power(X, a % 5) @ np.linalg.matrix_power(Z, b % 5)
hs = lambda A, B: abs(np.trace(A.conj().T @ B)) / 5
gram = max(hs(Wop(a, b), Wop(c, d)) for (a, b), (c, d) in itertools.combinations(itertools.product(range(5), repeat=2), 2))
T5 = np.diag([z5 ** ((2 * x * x) % 5) for x in range(5)]); F5 = np.array([[z5 ** ((x * y) % 5) for y in range(5)] for x in range(5)]) / np.sqrt(5); S5 = -F5
def image(g, a, b):
    M = g @ Wop(a, b) @ np.linalg.inv(g)
    best = max(itertools.product(range(5), repeat=2), key=lambda v: hs(Wop(*v), M))
    return best, hs(Wop(*best), M)
def linmap(g):
    e1, o1 = image(g, 1, 0); e2, o2 = image(g, 0, 1)
    ok = all(image(g, a, b)[0] == ((a * e1[0] + b * e2[0]) % 5, (a * e1[1] + b * e2[1]) % 5) and image(g, a, b)[1] > 1 - 1e-12 for a in range(5) for b in range(5))
    return (e1, e2), ok
(MT, okT), (MS, okS) = linmap(T5), linmap(S5)
recT = ((1, 4), (0, 1)); recS = ((0, 1), (4, 0))                        # images of (1, 0) and (0, 1) under the record's rule
OUT["B"] = {"offdiag_HS": gram, "XZ=zeta^-1 ZX": float(abs(X @ Z - z5 ** -1 * Z @ X).max()), "M_T": MT, "M_S": MS, "linear": okT and okS,
            "equals_record": (MT == recT and MS == recS)}
print("B: the 25 Weyl operators are orthogonal (largest overlap %.1e); XZ = zeta^-1 ZX (%.1e); rho(T) sends (1,0),(0,1) to %s, rho(S) to %s, linearly on all 25: %s; the record's transport is %s and %s: equal %s"
      % (gram, OUT["B"]["XZ=zeta^-1 ZX"], MT, MS, okT and okS, recT, recS, OUT["B"]["equals_record"]))

# ---------------------------------------------------------------- C
import mpmath as mp
mp.mp.dps = 30
def psi(j, u, tau, N=5, K=40):
    return mp.fsum(mp.exp(mp.pi * 1j * N * tau * (n + mp.mpf(j) / N) ** 2 + 2j * mp.pi * N * u * (n + mp.mpf(j) / N)) for n in range(-K, K + 1))
tau = mp.mpc("0.13", "1.1"); u = mp.mpc("0.217", "0.094")
cZ = max(abs(psi(j, u + mp.mpf(1) / 5, tau) - mp.exp(2j * mp.pi * j / 5) * psi(j, u, tau)) / abs(psi(j, u, tau)) for j in range(5))
fac = [psi(j, u + tau / 5, tau) / psi((j + 1) % 5, u, tau) for j in range(5)]
cX = max(abs(f / fac[0] - 1) for f in fac)
cP = max(abs(psi(j, -u, tau) - psi((-j) % 5, u, tau)) / abs(psi(j, u, tau)) for j in range(5))
us = [mp.mpc(0.1 * k + 0.03, 0.07 * k - 0.11) for k in range(5)]
rk = int(np.linalg.matrix_rank(np.array([[complex(psi(j, uu, tau)) for j in range(5)] for uu in us]), tol=1e-9))
Par = np.array([[1.0 if (x + y) % 5 == 0 else 0.0 for y in range(5)] for x in range(5)]); ev = np.round(np.linalg.eigvalsh(Par)).astype(int)
OUT["C"] = {"Z": float(cZ), "X_common_factor": float(cX), "parity": float(cP), "rank": rk, "split": [int((ev == 1).sum()), int((ev == -1).sum())]}
print("C: u -> u + 1/5 is Z (%.1e); u -> u + tau/5 is X up to one common factor (%.1e); u -> -u sends psi_j to psi_(-j) (%.1e); rank %d; parity split %d + %d"
      % (cZ, cX, cP, rk, OUT["C"]["split"][0], OUT["C"]["split"][1]))

# ---------------------------------------------------------------- D
sys.path.insert(0, str(HERE.parents[1] / "B1945_the_frames_cusp_exponents" / "verification"))
import determinant_law as DL
I_, QI, QJ, QK, EPS, U_, ED, BLOCKS = DL.FM.setup()
qn = lambda M: np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)])
Q = [qn(QI), qn(QJ), qn(QK)]
sq = max(np.abs(q @ q + np.eye(2)).max() for q in Q); ac = max(np.abs(a @ b + b @ a).max() for a, b in itertools.combinations(Q, 2))
hsq = max(abs(np.trace(a.conj().T @ b)) for a, b in itertools.combinations(Q + [np.eye(2, dtype=complex)], 2))
DL.mp.mp.dps = 40
def trip(t): return DL.mp.matrix([DL.te.ev(cc, t) for cc in DL.te.B[1]])
ts = [DL.mp.mpc("0.11", "1.3"), DL.mp.mpc("-0.23", "1.7"), DL.mp.mpc("0.37", "1.1")]
A = DL.mp.matrix(3, 3); Bm = DL.mp.matrix(3, 3)
for k, t in enumerate(ts):
    a, b = trip(t), trip(t + 1)
    for r in range(3): A[r, k] = a[r]; Bm[r, k] = b[r]
TH = Bm * A ** -1                                                        # c(tau + 1) = TH c(tau)
chk = trip(DL.mp.mpc("0.05", "2.1") + 1) - TH * trip(DL.mp.mpc("0.05", "2.1"))
evs = np.linalg.eigvals(qn(TH)); ph = sorted(round(float(np.angle(v) / (2 * np.pi)) % 1, 6) for v in evs)
weil3 = sorted({Fr((2 * x * x) % 5, 5) for x in range(5)})
OUT["D"] = {"units_square_to_minus_one": float(sq), "anticommute": float(ac), "HS_orthogonal": float(hsq), "T_matrix_check": float(max(abs(x) for x in chk)),
            "higgs_T_phases": ph, "moduli": sorted(round(float(abs(v)), 9) for v in evs), "weil_T_phases": [str(x) for x in weil3]}
print("D: the frame's units square to -1 (%.1e), anticommute (%.1e) and are orthogonal (%.1e): the level-2 Weyl operators up to phases" % (sq, ac, hsq))
print("D: the Higgs direction's triplet under tau -> tau + 1: a constant matrix (%.1e at a fourth point), eigenvalue moduli %s, phases %s (eighths: %s); the Weil representation's T-phases: %s"
      % (OUT["D"]["T_matrix_check"], OUT["D"]["moduli"], ph, [round(x * 8, 4) for x in ph], [str(x) for x in weil3]))

# ---------------------------------------------------------------- E
def anomalies(p):
    m, n = (p + 1) // 2, (p - 1) // 2; ym, yn = Fr(p - 1, 2), -Fr(p + 1, 2)
    sY = sY3 = aM = aN = Fr(0)
    for k1 in range(m + 1):
        for k2 in range(n + 1):
            if (k1 + k2) % 2: continue
            y = k1 * ym + k2 * yn; d = comb(m, k1) * comb(n, k2)
            sY += d * y; sY3 += d * y ** 3
            if m >= 2 and 1 <= k1 <= m - 1: aM += y * Fr(comb(m - 2, k1 - 1), 2) * comb(n, k2)
            if n >= 2 and 1 <= k2 <= n - 1: aN += y * Fr(comb(n - 2, k2 - 1), 2) * comb(m, k1)
    return m, n, sY, sY3, aM, aN
OUT["E"] = {}
for p in (3, 5, 7, 11, 13):
    m, n, sY, sY3, aM, aN = anomalies(p)
    OUT["E"][str(p)] = [m, n, str(sY), str(sY3), str(aM), str(aN), cnt[p]]
    print("E: p = %2d: split %d + %d; sum Y %s, sum Y^3 %s, SU(%d)^2 Y %s, SU(%d)^2 Y %s; lines the act fixes: %d" % (p, m, n, sY, sY3, m, aM, n, aN, cnt[p]))

# ---------------------------------------------------------------- F
def gram_at(tx, a, b, sec="down", rd="S"):
    Y = DL.parts(tx, 1.7, a, b, sec)[2][rd]; return qn(Y * Y.H)
pts = [(Fr(1, 5), Fr(3, 5)), (Fr(2, 5), Fr(1, 5)), (Fr(0), Fr(3, 5)), (Fr(4, 5), Fr(4, 5)), (Fr(3, 5), Fr(0)), (Fr(1, 5), Fr(1, 5))]
res = {}
for name, tr in (("(a, b - a)", lambda a, b: (a, (b - a) % 1)), ("(a, b + a)", lambda a, b: (a, (b + a) % 1))):
    rows = []
    for a, b in pts:
        Bw = gram_at("1.13", a, b); Aw = gram_at("0.13", *tr(a, b)); s = np.abs(Bw).max()
        rows.append(np.kron(np.eye(3), Bw / s) - np.kron((Aw / s).T, np.eye(3)))
    sv = np.linalg.svd(np.vstack(rows), full_matrices=True); null = sv[1][-1] / sv[1][0]; second = sv[1][-2] / sv[1][0]
    Uv = sv[2][-1].conj().reshape(3, 3).T; Uv = Uv / np.sqrt(abs(np.linalg.det(Uv)) ** (2 / 3))
    res[name] = (null, second, Uv)
name = min(res, key=lambda k: res[k][0]); null, second, UL = res[name]
unit = float(np.abs(UL @ UL.conj().T - np.eye(3)).max()); mod = np.round(np.abs(UL), 6)
perm = bool(all(sorted(r) == [0, 0, 1] for r in mod.tolist()) and all(sorted(c) == [0, 0, 1] for c in mod.T.tolist()))
e = np.linalg.eigvals(UL); rel = sorted(round(float(np.angle(v / e[np.argmin(np.abs(np.angle(e)))]) / (2 * np.pi)) % 1, 6) for v in e)
ph_l = sorted(round(float(np.angle(v) / (2 * np.pi)) % 1, 6) for v in e)
gaps = sorted(round((ph_l[(i + 1) % 3] - ph_l[i]) % 1, 6) for i in range(3))
OUT["F"] = {"transport": name, "null_singular_value": float(null), "next_singular_value": float(second), "other_transport_null": float(res[[k for k in res if k != name][0]][0]),
            "unitary_defect": unit, "moduli": mod.tolist(), "a_permutation_up_to_phases": perm, "eigenphase_gaps": gaps}
print("F: on frame C (down, S; six points), the point transport is %s (the other fails: %.1e); U_L is determined up to a phase (singular values %.1e, then %.1e); unitary to %.1e"
      % (name, OUT["F"]["other_transport_null"], null, second, unit))
print("F: |U_L| = %s: a permutation of the blocks up to phases: %s; the gaps between its eigenphases: %s (quarters: %s)" % (mod.tolist(), perm, gaps, [round(g * 4, 4) for g in gaps]))
(HERE / "wa2_on_main.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
