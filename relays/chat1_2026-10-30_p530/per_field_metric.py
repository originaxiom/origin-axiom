# Referee 2 check (read-only on the record): on the zero line, one reading (S) for every sector, c = 1, one shared
# section, does a per-field generation metric H (B1822: "8 real parameters per field ... 40 across Q, u, d, L, e";
# "H = diag(1, 1, kappa) is admitted") split the sectors? Canonical coupling = H_L^{-1/2 T} Y H_R^{-1/2}.
# Built from B1726's committed census modules exactly as compute() builds Y.
import sys, math, importlib.util, pathlib
import numpy as np
ROOT = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("census", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
import mpmath as mp
M = c._modules(); B, te, col = M["B"], M["te"], M["col"]
re_t, im_t = 0.35, 2.75
t = complex(re_t, im_t); w = 0.0
av = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in te.B[1]]
S = av[0] * B.QI + av[1] * B.QJ + av[2] * B.QK
L = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col]))
def Y_sector(lf, rf):
    x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); cc = B.cA(x, yy, t, R)
    u = {s: (math.sqrt(2 * math.pi * L + cc[s]) * R[s] if cc[s] is not None and 2 * math.pi * L + cc[s] > 0 else 0) for s in B.UNITS}
    return B.coupling(S, B.weighted_M(u))
def isqrt(H):
    e, V = np.linalg.eigh(H); return V @ np.diag(e ** -0.5) @ V.conj().T
def ratios(Y):
    sv = np.linalg.svd(Y, compute_uv=False); return (sv[1] / sv[0], sv[2] / sv[0])
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
Ys = {s: Y_sector(*f) for s, f in SECT.items()}
print("H = I for every field:", {s: tuple(round(v, 8) for v in ratios(Y)) for s, Y in Ys.items()})
H = {"Q": np.eye(3), "u": np.diag([1, 1, 1.1]), "d": np.eye(3), "L": np.eye(3), "e": np.diag([1.1, 1, 1])}
out = {}
for s, (lf, rf) in SECT.items():
    out[s] = ratios(isqrt(H[lf]).T @ Ys[s] @ isqrt(H[rf]))
print("per-field H (u: diag(1,1,1.1), e: diag(1.1,1,1), others I):", {s: tuple(round(v, 8) for v in r) for s, r in out.items()})
