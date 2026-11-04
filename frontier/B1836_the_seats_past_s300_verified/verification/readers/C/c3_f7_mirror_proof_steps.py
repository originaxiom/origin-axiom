"""C3 (Theorem 60, F7): the mirror identity Y((p1, -p2), -conj tau) = P conj(Y((p1, p2), tau)) P, checked STEP BY STEP on
MAIN's construction (B1691's b1656_funcs: thc, th1, bil, pairs, residues, cA, weighted_M, coupling; B1821's cm_zero_line
directions and radii), so that the written proof in LEDGER.md rests on main's code, not on the lane's.

Steps (each prints its worst deviation; controls must FAIL):
 S1  thc(a, -b, -conj u, -conj T) = conj thc(a, b, u, T);  th1(-conj u, -conj t) = -conj th1(u, t).
 S2  bil entrywise: bil(x', y', -conj u, -conj t) = E o conj bil(x, y, u, t),  E = [[-1, +1], [+1, -1]],  x' = (a_x, -b_x).
 S3  residues: R'_s = sgn_s conj R_s,  sgn = (1: -, i: +, j: +, k: -)   (random twists and census lines, three sectors).
 S4  channel norms: cA' = cA (real, mirror-invariant).
 S5  Higgs: direction(d, -conj t) as S' = QI conj(S) QI for the 13 directions of B1810/B1821 (a hypothesis of the theorem).
 S6  the algebra, EXACT (sympy): coupling(QI conj(S) QI, M(sgn o conj u)) = P conj(coupling(S, M(u))) P on the 16 basis pairs
     (both sides bi-antilinear, so the basis suffices); the reading S~ = EPS conj(S) EPS^T commutes with S -> QI conj(S) QI.
 S7  the full identity on census lines, two tau, three sectors, both readings, a0 = 0 and a0 = i r eta^3 (r real);
     controls: the same line at -conj tau without b -> -b (per sector); a direction times e^{0.3 i}; r = 1 + 0.5 i.
No measured number is read; nothing is compared with data.  Single-threaded."""
import os
for v in ("OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
import contextlib, io, itertools, math, pathlib, sys
import numpy as np
import mpmath as mp
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
with contextlib.redirect_stdout(io.StringIO()):
    import cm_zero_line as Z
    M = Z.mods()
B = M["B"]
OUT = []
def say(s):
    print(s, flush=True); OUT.append(s)

rng = np.random.default_rng(20261104)
mir = lambda z: -np.conj(z)

# ---- S1
w1 = w2 = 0.0
for _ in range(20):
    a, b = rng.uniform(-1, 1), rng.uniform(-1, 1)
    t = complex(rng.uniform(-.5, .5), rng.uniform(.8, 3)); u = complex(rng.normal() * .2, rng.normal() * .2)
    w1 = max(w1, abs(B.thc(a, -b, mir(u), mir(2 * t)) - np.conj(B.thc(a, b, u, 2 * t))))
    w2 = max(w2, abs(B.th1(mir(u), mir(t)) + np.conj(B.th1(u, t))))
say("S1 thc term conjugation: worst %.1e ; th1 odd-conjugation: worst %.1e" % (w1, w2))

# ---- S2
E = np.array([[-1, 1], [1, -1]])
w = 0.0; wc = 0.0
for _ in range(20):
    x = (rng.uniform(-1, 1), rng.uniform(-1, 1)); y = (rng.uniform(-1, 1), rng.uniform(-1, 1))
    t = complex(rng.uniform(-.5, .5), rng.uniform(.8, 3)); u = complex(rng.normal() * .2, rng.normal() * .2)
    A = B.bil(x, y, u, t); Am = B.bil((x[0], -x[1]), (y[0], -y[1]), mir(u), mir(t))
    w = max(w, float(np.max(np.abs(Am - E * np.conj(A)))))
    wc = max(wc, float(np.max(np.abs(Am - np.conj(A)))))           # control: no entry signs
say("S2 bil entry parities E = [[-1,+1],[+1,-1]]: worst %.1e ; control (no signs) min-over-draws of worst: %.2f" % (w, wc))

# ---- S3, S4
SG = {"1": -1, "i": 1, "j": 1, "k": -1}
def twists(p1, p2, t, ql, qr):
    return B.sector_twists(B.line_w(p1, p2, t), t, ql, qr)
w3 = w4 = 0.0; ctrl3 = 1e9; n3 = 0
lines = [(2/5, 1/10), (2/5, 3/10), (1/5, 2/5), (3/8, 1/8), (1/4, 1/4), (1/3, 1/6), (1/10, 3/10)]
for t in (complex(0.13, 1.7), complex(-0.31, 2.6)):
    for (p1, p2) in lines:
        for _, ql, qr in Z.SECTORS:
            x, y = twists(p1, p2, t, ql, qr); xm, ym = twists(p1, -p2, mir(t), ql, qr)
            R = B.residues(x, y, t); Rm = B.residues(xm, ym, mir(t))
            for s in B.UNITS:
                w3 = max(w3, abs(Rm[s] - SG[s] * np.conj(R[s])))
            Rc = B.residues(*twists(p1, p2, mir(t), ql, qr), mir(t))         # control: b not flipped
            ctrl3 = min(ctrl3, max(abs(Rc[s] - SG[s] * np.conj(R[s])) for s in B.UNITS)); n3 += 1
            if (p1, p2) in lines[:3]:
                c = B.cA(x, y, t, R); cm = B.cA(xm, ym, mir(t), Rm)
                for s in B.UNITS:
                    if c[s] is not None and cm[s] is not None:
                        w4 = max(w4, abs(c[s] - cm[s]) / max(1.0, abs(c[s])))
                    elif (c[s] is None) != (cm[s] is None):
                        w4 = max(w4, 1.0)
say("S3 residue parities (-,+,+,-) on (1,i,j,k): worst %.1e over %d sector-lines; control (b not flipped) smallest worst %.2e" % (w3, n3, ctrl3))
say("S4 channel norms mirror-invariant: worst relative %.1e (quadrature-limited)" % w4)

# ---- S5
QI, QJ, QK, EPS = B.QI, B.QJ, B.QK, B.EPS
def Smat(a, a0=0.0):
    return a0 * np.eye(2) + a[0] * QI + a[1] * QJ + a[2] * QK
w5 = 0.0; bad = []
for d in Z.DIRS:
    for t in (complex(0.13, 1.7), complex(-0.31, 2.6)):
        S = Smat(Z.direction(d, t)); Sm = Smat(Z.direction(d, mir(t)))
        dev = float(np.max(np.abs(Sm - QI @ np.conj(S) @ QI))) / float(np.max(np.abs(S)))
        w5 = max(w5, dev)
        if dev > 1e-8: bad.append(d)
say("S5 Higgs hypothesis S(-conj t) = QI conj(S(t)) QI on all %d directions: worst relative %.1e ; failing: %s" % (len(Z.DIRS), w5, sorted(set(bad))))

# ---- S6 exact algebra
I2 = sp.eye(2); sQI = sp.Matrix([[sp.I, 0], [0, -sp.I]]); sQJ = sp.Matrix([[0, 1], [-1, 0]]); sQK = sQI * sQJ; sEPS = sQJ
UN = {"1": I2, "i": sQI, "j": sQJ, "k": sQK}; keys = list(UN)
EC = {s: sEPS * C for s, C in UN.items()}
G = sp.Matrix(4, 4, lambda t_, s_: sum((EC[keys[t_]].multiply_elementwise(UN[keys[s_]])) ))
Gi = G.inv()
EDUAL = {keys[a]: sum((Gi[b, a] * UN[keys[b]] for b in range(4)), sp.zeros(2)) for a in range(4)}
BL = [sQJ, sQI, sQK]
def coup(S, Mw):
    return sp.Matrix(3, 3, lambda r, c: sum((BL[r].T * sEPS * S * BL[c]).multiply_elementwise(Mw)))
def Mw_of(u):
    return sum((u[s] * EDUAL[s] for s in UN), sp.zeros(2))
P = sp.diag(1, 1, -1)
basisS = [I2, sQI, sQJ, sQK]
nonzero = 0
for S in basisS:
    for s0 in keys:
        u = {s: (1 if s == s0 else 0) for s in keys}
        um = {s: SG[s] * sp.conjugate(u[s]) for s in keys}
        lhs = coup(sQI * S.conjugate() * sQI, Mw_of(um))
        rhs = P * coup(S, Mw_of(u)).conjugate() * P
        if sp.simplify(lhs - rhs) != sp.zeros(3): nonzero += 1
tilde = lambda S: sEPS * S.conjugate() * sEPS.T
nz2 = sum(1 for S in basisS if sp.simplify(tilde(sQI * S.conjugate() * sQI) - sQI * tilde(S).conjugate() * sQI) != sp.zeros(2))
# control: the wrong vector sign pattern (+,+,+,+) must fail on some basis pair
fail_ctrl = 0
for S in basisS:
    for s0 in keys:
        u = {s: (1 if s == s0 else 0) for s in keys}
        lhs = coup(sQI * S.conjugate() * sQI, Mw_of({s: sp.conjugate(u[s]) for s in keys}))
        if sp.simplify(lhs - P * coup(S, Mw_of(u)).conjugate() * P) != sp.zeros(3): fail_ctrl += 1
say("S6 exact algebra: basis pairs violating the identity %d of 16 ; reading S~ commutes with the mirror: violations %d of 4 ; control (no channel signs) violations %d of 16" % (nonzero, nz2, fail_ctrl))

# ---- S7 full identity (main's coupling), with and without the singlet
def eta3(t):
    q = mp.exp(2j * mp.pi * mp.mpc(t.real, t.imag))
    return complex(mp.power(q, mp.mpf(1) / 8) * mp.nprod(lambda n: (1 - q ** n) ** 3, [1, mp.inf]))
_RC = {}
def Y_of(p1, p2, t, sector, d, reading, a0fac=None, rot=1.0):
    _, ql, qr = sector
    key = (p1, p2, t, ql, qr)
    if key not in _RC:
        x, y = twists(p1, p2, t, ql, qr); R = B.residues(x, y, t); _RC[key] = (R, B.cA(x, y, t, R))
    R, c = _RC[key]
    L = Z.radii(t)[1]
    a = [rot * v for v in Z.direction(d, t)]
    a0 = 0.0 if a0fac is None else 1j * a0fac * eta3(t)
    S = Smat(a, a0)
    if reading: S = EPS @ S.conj() @ EPS.T
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(S, B.weighted_M(u))
Pn = np.diag([1, 1, -1]).astype(complex)
res = {"main": 0.0, "singlet": 0.0}; ctrl = {"per-sector (b kept)": 1e9, "direction x e^{0.3i}": 1e9, "r = 1+0.5i": 1e9}
for t in (complex(0.13, 1.7), complex(-0.31, 2.6)):
    for (p1, p2) in lines[:4]:
        for sec in Z.SECTORS:
            for d in ("DR", "F_10"):
                for rd in (0, 1):
                    Y = Y_of(p1, p2, t, sec, d, rd); nY = np.max(np.abs(Y))
                    Ym = Y_of(p1, -p2, mir(t), sec, d, rd)
                    res["main"] = max(res["main"], np.max(np.abs(Ym - Pn @ Y.conj() @ Pn)) / nY)
                    Ys = Y_of(p1, p2, t, sec, d, rd, a0fac=0.5); Ysm = Y_of(p1, -p2, mir(t), sec, d, rd, a0fac=0.5)
                    res["singlet"] = max(res["singlet"], np.max(np.abs(Ysm - Pn @ Ys.conj() @ Pn)) / np.max(np.abs(Ys)))
            Y = Y_of(p1, p2, t, sec, "F_10", 0); nY = np.max(np.abs(Y))
            ctrl["per-sector (b kept)"] = min(ctrl["per-sector (b kept)"], np.max(np.abs(Y_of(p1, p2, mir(t), sec, "F_10", 0) - Pn @ Y.conj() @ Pn)) / nY)
            Yr = Y_of(p1, p2, t, sec, "F_10", 0, rot=np.exp(0.3j)); Yrm = Y_of(p1, -p2, mir(t), sec, "F_10", 0, rot=np.exp(0.3j))
            ctrl["direction x e^{0.3i}"] = min(ctrl["direction x e^{0.3i}"], np.max(np.abs(Yrm - Pn @ Yr.conj() @ Pn)) / np.max(np.abs(Yr)))
            Yc = Y_of(p1, p2, t, sec, "F_10", 0, a0fac=1 + 0.5j); Ycm = Y_of(p1, -p2, mir(t), sec, "F_10", 0, a0fac=1 + 0.5j)
            ctrl["r = 1+0.5i"] = min(ctrl["r = 1+0.5i"], np.max(np.abs(Ycm - Pn @ Yc.conj() @ Pn)) / np.max(np.abs(Yc)))
say("S7 full identity, relative worst: a0 = 0: %.1e ; a0 = i(1/2)eta^3: %.1e  (4 lines x 2 tau x 3 sectors x DR,F_10 x 2 readings)" % (res["main"], res["singlet"]))
say("S7 controls (smallest relative failure; must be >> 0): " + "; ".join("%s %.2e" % kv for kv in ctrl.items()))
pathlib.Path(__file__).with_name("c3_run.txt").write_text("\n".join(OUT) + "\n")
