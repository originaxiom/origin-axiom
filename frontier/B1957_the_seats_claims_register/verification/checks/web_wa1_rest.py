"""B1957, check 2: the remaining checkable statements of the web seat's W-A1 (data-free, main's own code).
1 the other Weil class needs another Fourier kernel; 2 Frobenius-Schur indicators and the images on the 3 and the 2;
3 the SU(3)^3 anomaly and the doublet count; 4 the mirror covariance of frame C; 5 the act's axis against the cone
points; 6 the triplet at tau = i and its law under S; 7 the scoreboard's entries the choices audit cites."""
import itertools, json, math, pathlib, re, sys
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import web_wa1_part3 as W
DL = W.DL; mp = W.mp; CR = W.CR
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
P = np.array([[1.0 if (x + y) % 5 == 0 else 0.0 for y in range(5)] for x in range(5)])


def weil(c):
    T = np.diag([psi(c * x * x) for x in range(5)]); found = []
    for k in (1, 2, 3, 4):
        Fk = np.array([[psi(k * x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)
        for s in (1, -1, 1j, -1j):
            S = s * Fk
            if np.abs(np.linalg.matrix_power(S @ T, 3) - S @ S).max() < 1e-12 and np.abs(np.linalg.matrix_power(S, 4) - np.eye(5)).max() < 1e-12: found.append((k, s, S))
    return T, found


def group(T, S):
    key = lambda A: tuple(np.round(A.flatten(), 8)); G = {key(np.eye(5)): np.eye(5, dtype=complex)}; fr = list(G.values())
    while fr:
        nx = []
        for A in fr:
            for g in (T, S):
                N = A @ g
                if key(N) not in G: G[key(N)] = N; nx.append(N)
        fr = nx
    return list(G.values())


if __name__ == "__main__":
    for c in (1, 2):
        T, found = weil(c); print("1. T = diag psi(%d x^2): the Fourier kernels psi(k x y) that close the relations: k in %s" % (c, sorted({k for k, s, S in found})))
    T, found = weil(2); G = group(T, found[0][2]); ev, V = np.linalg.eigh(P); Ve, Vo = V[:, ev > 0], V[:, ev < 0]
    for name, Vb in (("3", Ve), ("2", Vo)):
        blocks = [Vb.conj().T @ g @ Vb for g in G]
        fs = sum(np.trace(b @ b) for b in blocks).real / len(G); norm = sum(abs(np.trace(b)) ** 2 for b in blocks) / len(G)
        img = len({tuple(np.round(b.flatten(), 7)) for b in blocks})
        print("2. on the %s: Frobenius-Schur indicator %+.3f; character norm %.3f; image of order %d" % (name, fs, norm, img))
    print("3. SU(3)^3: Q counts 2 triplets, u^c and d^c one antitriplet each: 2 - 1 - 1 = %d; weak doublets: 3 (Q) + 1 (L) = %d, even" % (2 - 1 - 1, 4))
    worst = 0.0
    for tx, ty in (("0.13", 1.7), ("0.31", 1.2), ("-0.22", 2.4)):
        L = CR.canon(complex(float(tx), ty))["L_2"]
        for w in ((Fr(2, 5), Fr(4, 5)), (Fr(1, 5), Fr(2, 5)), (Fr(0), Fr(3, 5)), (Fr(3, 5), Fr(1, 5))):
            r0, V0 = W.out(tx, ty, w, end=L); r1, V1 = W.out(repr(-float(tx)), ty, (w[0], (-w[1]) % 1), end=L)
            worst = max(worst, W.rdiff(r0, r1), W.vdiff(V0, V1))
    print("4. the mirror tau -> -conj(tau), (a, b) -> (a, -b), the end held equal: ratios and |V| agree to %.1e at three tau and four lines" % worst)
    lam = (3 + math.sqrt(5)) / 2; Lper = 2 * math.log(lam); di = dw = 9.0; ti = None
    for n in range(20001):
        s = -Lper / 2 + Lper * n / 20000; zc = complex(0.5 + (math.sqrt(5) / 2) * math.tanh(s), (math.sqrt(5) / 2) / math.cosh(s))
        for _ in range(60):                                         # reduce to the fundamental domain
            zc = complex(zc.real - math.floor(zc.real + 0.5), zc.imag)
            if abs(zc) < 1 - 1e-15: zc = -1 / zc
            else: break
        hd = lambda a, b: math.acosh(1 + abs(a - b) ** 2 / (2 * a.imag * b.imag))
        d1 = hd(zc, 1j); d2 = min(hd(zc, complex(-0.5, math.sqrt(3) / 2)), hd(zc, complex(0.5, math.sqrt(3) / 2)))
        if d1 < di: di, ti = d1, s
        dw = min(dw, d2)
    print("5. one period of the act's axis (length %.6f) on the modular surface: least distance to the cone point of order 2: %.1e; to the cone point of order 3: %.4f" % (Lper, di, dw))
    DL.mp.mp.dps = 40
    a = [DL.te.ev(cc, mp.mpc(0, 1)) for cc in DL.te.B[1]]
    print("6. the triplet at tau = i: |a3| / |a1| = %.1e; |a1 + a2| / |a1| = %.1e; imaginary parts of a1, a2: %.1e" % (float(abs(a[2]) / abs(a[0])), float(abs(a[0] + a[1]) / abs(a[0])), float(max(abs(mp.im(a[0])), abs(mp.im(a[1]))) / abs(a[0]))))
    t = mp.mpc("0.13", "1.7"); a0 = [DL.te.ev(cc, t) for cc in DL.te.B[1]]; a1 = [DL.te.ev(cc, -1 / t) for cc in DL.te.B[1]]
    fac = (-1j * t) ** (-mp.mpf(1) / 2) * t ** 2
    e = max(abs(a1[0] - fac * a0[1]), abs(a1[1] - fac * a0[0]), abs(a1[2] - fac * a0[2])) / max(abs(x) for x in a1)
    print("   under S at 0.13 + 1.7i: a(-1/tau) = (-i tau)^(-1/2) tau^2 P a(tau), P exchanging the first two components: %.1e" % float(e))
    sb = (HERE.parents[3] / "docs" / "TOTAL_INPUTS_SCOREBOARD.md").read_text()
    for code in ("S01", "S02", "S03", "C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09"):
        m = re.search(r"^\|\s*%s\s*\|(.*)$" % code, sb, re.M)
        print("7. the scoreboard's %s: %s" % (code, re.sub(r"\s+", " ", m.group(1))[:150] if m else "NOT FOUND"))
