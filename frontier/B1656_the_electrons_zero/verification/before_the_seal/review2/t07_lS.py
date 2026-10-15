# Review 2, check 4a: the l_S machinery.  (i) det Y(S,M) = det(M) * l_S(M), l_S linear (additivity/homogeneity) for the instrument's l_S;
# (ii) cancellation/conditioning of the shift trick at the residue matrices M_R of all 18 lines x 3 sectors (S-independent), vs an independent
#      evaluation l_S(M) = sum_ij M_ij l_S(E_ij) (unit-matrix basis, each shifted by I -> det(E+I) in {1,2}); (iii) is M_R rank one?
import numpy as np, math, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("residues","sector_twists","line_w","OM","GEN","SECTORS","SIXY","UNITS","nR2","np","coupling","weighted_M","EPS"): globals()[k] = ns[k]
# the instrument's l_S, copied verbatim from the file text
import pathlib, re
SRC = pathlib.Path(__file__).resolve().parents[2].joinpath("the_electrons_zero.py").read_text()
a = SRC.index("def l_S(S, M):"); b = SRC.index("e6 = {")
exec(SRC[a:b], globals())
rng = np.random.default_rng(777)
def rc(): return rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
# (i)
worst_add = worst_ratio = worst_hom = 0.0
for _ in range(20):
    S = rc(); M1, M2 = rc(), rc(); al = complex(*rng.normal(size=2))
    l1, l2, l12 = l_S(S, M1), l_S(S, M2), l_S(S, M1 + M2); la = l_S(S, al*M1)
    worst_add = max(worst_add, abs(l12 - l1 - l2)/(abs(l1) + abs(l2)))
    worst_hom = max(worst_hom, abs(la - al*l1)/abs(al*l1))
    worst_ratio = max(worst_ratio, abs(np.linalg.det(coupling(S, M1)) - np.linalg.det(M1)*l1)/abs(np.linalg.det(M1)*l1))
print("(i) random S, M: additivity rel err %.2e, homogeneity rel err %.2e, det Y = det M * l_S(M) rel err %.2e" % (worst_add, worst_hom, worst_ratio))
# (ii) M_R conditioning
E = [np.array([[1 if (i == r and j == c) else 0 for j in range(2)] for i in range(2)], dtype=complex) for r in range(2) for c in range(2)]
LINES18 = [(b_ + i/3, b_ + j/3) for b_ in (1/9, 2/9) for i in range(3) for j in range(3)]
S = rc()
f = lambda N: np.linalg.det(coupling(S, N))/np.linalg.det(N)
lE = [f(Ek + np.eye(2)) - f(np.eye(2)) for Ek in E]        # l_S on the unit-matrix basis (well conditioned shifts)
worst_rel = 0.0; mindet = 1e9; maxcond = 0.0; rank1 = 0.0; minratio = 1e9
for (p1, p2) in LINES18:
    w = line_w(p1, p2, OM)
    for sec, (fl, fr) in SECTORS.items():
        x, y = sector_twists(w, OM, SIXY[fl], SIXY[fr]); R = residues(x, y, OM); MR = weighted_M(R)
        c0 = float(np.abs(MR).max()); dshift = abs(np.linalg.det(MR + c0*np.eye(2)))/c0**2
        mindet = min(mindet, dshift); maxcond = max(maxcond, np.linalg.cond(MR + c0*np.eye(2)))
        rank1 = max(rank1, abs(np.linalg.det(MR))/c0**2)
        l_inst = l_S(S, MR); l_ref = sum(MR[r, c]*lE[2*r + c] for r in range(2) for c in range(2))
        if abs(l_ref) > 1e-12:
            worst_rel = max(worst_rel, abs(l_inst - l_ref)/abs(l_ref)); minratio = min(minratio, abs(l_ref))
print("(ii) 18 lines x 3 sectors at omega (S fixed random): min |det(M_R + c0 I)|/c0^2 = %.3f ; max cond(M_R + c0 I) = %.2f ; max |det M_R|/c0^2 = %.1e (rank one) ; rel diff l_S(instrument) vs unit-basis = %.2e ; min |l_S| = %.3e" % (mindet, maxcond, rank1, worst_rel, minratio))
# generic-tau and other-tau residue matrices too
for t in (GEN, -0.17+0.95j, 0.31+0.7j, 0.2+0.55j):
    md = 1e9
    for (p1, p2) in [(0.137, 0.291), (0.613, 0.287), (2/9, 5/9)]:
        w = line_w(p1, p2, t)
        for sec, (fl, fr) in SECTORS.items():
            x, y = sector_twists(w, t, SIXY[fl], SIXY[fr]); R = residues(x, y, t); MR = weighted_M(R); c0 = float(np.abs(MR).max())
            md = min(md, abs(np.linalg.det(MR + c0*np.eye(2)))/c0**2)
    print("   tau", np.round(t, 3), ": min |det(M_R + c0 I)|/c0^2 = %.3f" % md)
# how close to singular can M + c0*I get for a RANK-ONE M with max-entry c0?  scan: M = v w^T random rank-one, trace = w.v
mins = []
for _ in range(200000):
    v = rng.normal(size=2) + 1j*rng.normal(size=2); ww = rng.normal(size=2) + 1j*rng.normal(size=2); M = np.outer(v, ww); c0 = np.abs(M).max()
    mins.append(abs(np.linalg.det(M + c0*np.eye(2)))/c0**2)
mins = np.array(mins); print("   random rank-one M: min det(M+c0 I)/c0^2 = %.2e ; fraction < 1e-2: %.4f ; < 1e-3: %.5f" % (mins.min(), np.mean(mins < 1e-2), np.mean(mins < 1e-3)))
