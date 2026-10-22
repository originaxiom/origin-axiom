"""B1716 (P-262, P-268): the frame's exact zeros, derived.  In B1656's four-channel coupling (Y = coupling(S, M),
M = sum_s u_s E_s*, u_s = sqrt(2 pi L + c_s) R_s):
  Z1  det(sum_s u_s E_s*) = (1/4) sum_s u_s^2                                   (random complex u; identity)
  Z2  the residue matrix has rank one, so sum_s R_s^2 = 0 for every twist pair    (random twists; by theta_1's quasi-period)
      hence det M = (1/4) sum_s c_s R_s^2, independent of L
  Z3  Y_ab = sum_s m_s [C_a^-1 S C_b]_s (m_s = M's channel weights)              (random S, m; quaternion identity)
  Z4  for S a unit C_p with m_p = 0, diag(+-1) Y is antisymmetric, so the spectrum is (|w|, |w|, 0) for any complex m
  Z5  on B1701's 27 tied lines the tied channel's residue vanishes (two tau, three sectors): B1701's 0 : 1 : 1, derived
  Z6  on every order-12 line the leptons' channels pair (D = sum c_s R_s^2 = 0) and on every order-4 line every sector's
      do (the law of P-268: left twist of exact order 4, right twist of order <= 2); and no other line of order 1-12 cancels D
No data.  python3 -B the_zeros_derived.py   # writes the_zeros_derived.json beside itself"""
import sys, json, math, pathlib, itertools
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); _argv = sys.argv; sys.argv = ['x']
import b1656_funcs as B
sys.argv = _argv
rng = np.random.default_rng(1716); OUT = {}
QU = {"1": np.eye(2, dtype=complex), "i": B.QI, "j": B.QJ, "k": B.QK}
def qcomp(q):                                   # the components of a 2x2 quaternion matrix in (1, i, j, k)
    return {s: np.trace(np.conj(U).T @ q) / 2 for s, U in QU.items()}
# Z1
z1 = 0.0
for _ in range(50):
    u = {s: complex(*rng.normal(size=2)) for s in B.UNITS}
    z1 = max(z1, abs(np.linalg.det(B.weighted_M(u)) - 0.25 * sum(v * v for v in u.values())) / sum(abs(v) ** 2 for v in u.values()))
OUT["Z1_max_rel"] = z1
# Z2
z2 = 0.0
for _ in range(40):
    t = complex(rng.uniform(-0.5, 0.5), rng.uniform(1.0, 3.0)); x = tuple(rng.uniform(-1, 1, 2)); y = tuple(rng.uniform(-1, 1, 2))
    R = B.residues(x, y, t); z2 = max(z2, abs(sum(R[s] ** 2 for s in B.UNITS)) / B.nR2(R))
OUT["Z2_max_rel_sum_R2"] = z2
# Z3
z3 = 0.0
for _ in range(50):
    S = sum(complex(*rng.normal(size=2)) * U for U in QU.values()); m = {s: complex(*rng.normal(size=2)) for s in B.UNITS}
    Y = B.coupling(S, B.weighted_M(m))
    Yq = np.array([[sum(m[s] * qcomp(np.linalg.inv(Ca) @ S @ Cb)[s] for s in B.UNITS) for Cb in B.BLOCKS] for Ca in B.BLOCKS])
    z3 = max(z3, np.max(np.abs(Y - Yq)) / np.max(np.abs(Y)))
OUT["Z3_max_rel"] = z3
# Z4
z4a, z4b = 0.0, 0.0
for p, U in (("i", B.QI), ("j", B.QJ), ("k", B.QK)):
    for _ in range(30):
        m = {s: complex(*rng.normal(size=2)) for s in B.UNITS}; m[p] = 0
        Y = B.coupling(U, B.weighted_M(m))
        z4a = max(z4a, min(np.max(np.abs(np.diag(s) @ Y + (np.diag(s) @ Y).T)) for s in itertools.product((1, -1), repeat=3)) / np.max(np.abs(Y)))
        sv = np.linalg.svd(Y, compute_uv=False); z4b = max(z4b, abs(sv[1] / sv[0] - 1) + sv[2] / sv[0])
OUT["Z4_signed_antisymmetry"] = z4a; OUT["Z4_spectrum_defect"] = z4b
# Z5: B1701's tied lines
UNIT = {(Fr(1, 2), Fr(0)): "j", (Fr(0), Fr(1, 2)): "i", (Fr(1, 2), Fr(1, 2)): "k"}
def tied(a, b): return UNIT.get(((-3 * a) % 1, (3 * b) % 1))
TIED = [(Fr(j, 6), Fr(k, 6)) for j in range(6) for k in range(6) if tied(Fr(j, 6), Fr(k, 6))]
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
z5 = 0.0
for (a, b) in TIED:
    for t in (complex(0.37, 2.2), complex(0.11, 1.7)):
        w = float(a) * t + float(b)
        for sec, (lf, rf) in SECT.items():
            x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, y, t)
            z5 = max(z5, abs(R[tied(a, b)]) / math.sqrt(B.nR2(R)))
OUT["Z5_tied_lines"] = len(TIED); OUT["Z5_max_rel_R_tied"] = z5
# Z6: the pairing law on every line of order 4, 8-12 (two tau; the matter's D relative to its scale)
def lines(N):
    seen, out = set(), []
    for j in range(N):
        for k in range(N):
            if math.gcd(math.gcd(j, k), N) != 1: continue
            a, b = Fr(j, N), Fr(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
            if key not in seen: seen.add(key); out.append(key)
    return out
def order(q, a, b):
    qa, qb = (q * a) % 1, (q * b) % 1; return math.lcm(qa.denominator, qb.denominator)
law, res = {}, {}
for N in range(1, 13):
    for (a, b) in lines(N):
        for sec, (lf, rf) in SECT.items():
            pred = order(B.SIXY[lf], a, b) == 4 and order(B.SIXY[rf], a, b) <= 2
            worst = 0.0
            for t in (complex(0.37, 2.2), complex(0.11, 1.7)):
                w = float(a) * t + float(b); x, y = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, y, t)
                c = B.cA(x, y, t, R)                          # a vanishing residue's channel contributes 0 (its c is undefined)
                D = sum(c[s] * R[s] ** 2 for s in B.UNITS if c[s] is not None)
                worst = max(worst, abs(D) / (max(abs(v) for v in c.values() if v is not None) * B.nR2(R)))
            key = "N=%d %s" % (N, sec); law.setdefault(key, [0, 0, 0]); res.setdefault(key, [])
            res[key].append(worst)
            if math.isnan(worst): law[key][2] += 1
            elif (worst < 1e-10) == pred: law[key][0] += 1
            else: law[key][1] += 1
OUT["Z6_law_agree_disagree_undefined"] = law
OUT["Z6_max_D_where_predicted"] = max((v for k, vs in res.items() for v in vs if not math.isnan(v) and v < 1e-6), default=None)
OUT["Z6_min_D_where_not"] = min((v for k, vs in res.items() for v in vs if not math.isnan(v) and v >= 1e-6), default=None)
if __name__ == "__main__":
    json.dump(OUT, open(HERE / "the_zeros_derived.json", "w"), indent=1, default=str)
    for k, v in OUT.items(): print(k, v)
