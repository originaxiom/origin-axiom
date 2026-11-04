"""On every one of S297's 40 half-lift points (alpha in Z/4 with beta in odd/8: order 8; alpha in Z/5 with beta in odd/10: order 10;
up to sign), and on controls, main's b1656_funcs: (i) sv(Y_lep(h)) = sv(Y_down(P h)) for random Higgs h (P = diag(-1,1,1), reading S);
(ii) the Gram identity Sigma_lep = P Sigma_down P (agy:B1761/B1762 G2); (iii) the residue relation R_lep = zeta (R_1, -R_i, R_j, R_k)_down
with one common phase zeta (c_s being sector-blind, B1826).  Data-free; two tau; L = main's L_max column (radii)."""
import sys, pathlib, json, math
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B, SECT, cm
Bf = B(); CM = cm(); QS = [Bf.QI, Bf.QJ, Bf.QK]; P = np.diag([-1.0, 1, 1]); KEYS = list(Bf.UNITS); rng = np.random.default_rng(3)
def canon(a, b): return min((a % 1, b % 1), ((-a) % 1, (-b) % 1))
pts = set()
for j in range(4):
    for k in (1, 3, 5, 7): pts.add(canon(Fr(j, 4), Fr(k, 8)))
for j in range(5):
    for k in (1, 3, 5, 7, 9): pts.add(canon(Fr(j, 5), Fr(k, 10)))
pts = sorted(pts); ctrl = [canon(Fr(2, 5), Fr(1, 5)), canon(Fr(1, 4), Fr(1, 4)), canon(Fr(1, 7), Fr(3, 7)), canon(Fr(3, 8), Fr(1, 8)), canon(Fr(1, 3), Fr(1, 6))]
def su(line, t, L, sec):
    w = float(line[0]) * t + float(line[1]); x, y = Bf.sector_twists(w, t, *SECT[sec]); R = Bf.residues(x, y, t); c = Bf.cA(x, y, t, R)
    return {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in KEYS}, R
def gram(u):
    M = Bf.weighted_M(u); Y = [Bf.coupling(Q, M) for Q in QS]; S = np.array([[np.trace(Y[c].conj().T @ Y[d]) for d in range(3)] for c in range(3)]); return S / np.trace(S).real
rows = []
for line in pts + ctrl:
    rec = {"line": [str(line[0]), str(line[1])], "order": math.lcm(line[0].denominator, line[1].denominator), "control": line in ctrl}
    sv, gr, rr = 0.0, 0.0, 0.0
    for t in (0.3 + 2.6j, -0.17 + 1.9j):
        L = CM.radii(t)[0]; ud, Rd = su(line, t, L, "down"); ue, Re = su(line, t, L, "lep")
        Md, Me = Bf.weighted_M(ud), Bf.weighted_M(ue)
        for _ in range(5):
            h = rng.normal(size=3) + 1j * rng.normal(size=3)
            a = np.linalg.svd(Bf.coupling(sum(h[k] * QS[k] for k in range(3)), Me), compute_uv=False)
            b = np.linalg.svd(Bf.coupling(sum((P @ h)[k] * QS[k] for k in range(3)), Md), compute_uv=False)
            sv = max(sv, np.abs(a - b).max() / a.max())
        gr = max(gr, np.abs(gram(ue) - P @ gram(ud) @ P).max())
        flip = np.array([Rd["1"], -Rd["i"], Rd["j"], Rd["k"]]); v = np.array([Re[s] for s in KEYS])
        zeta = np.vdot(flip, v) / np.vdot(flip, flip); rr = max(rr, np.abs(v - zeta * flip).max() / np.abs(v).max())
    rec.update({"sv_lep(h)_vs_down(Ph)": sv, "gram_G2": gr, "R_lep_vs_zeta_flipped_R_down": rr}); rows.append(rec)
for r in rows:
    print("%-8s (%-4s, %-5s) N=%2d  sv %.1e  G2 %.1e  R-relation %.1e" % ("control" if r["control"] else "", r["line"][0], r["line"][1], r["order"], r["sv_lep(h)_vs_down(Ph)"], r["gram_G2"], r["R_lep_vs_zeta_flipped_R_down"]))
hl = [r for r in rows if not r["control"]]
print("half-lift points: %d; max sv dev %.1e; max G2 dev %.1e; max R-relation dev %.1e" % (len(hl), max(r["sv_lep(h)_vs_down(Ph)"] for r in hl), max(r["gram_G2"] for r in hl), max(r["R_lep_vs_zeta_flipped_R_down"] for r in hl)))
print("controls: min sv dev %.1e" % min(r["sv_lep(h)_vs_down(Ph)"] for r in rows if r["control"]))
json.dump(rows, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1); print("exit 0")
