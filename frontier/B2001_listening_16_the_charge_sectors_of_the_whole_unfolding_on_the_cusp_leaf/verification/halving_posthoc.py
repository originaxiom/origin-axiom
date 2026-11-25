"""B2001, POST HOC (labelled; written after sectors_run.txt showed W6 and W12 agreeing and, on the 3-tower, the charged
sectors' top at half the neutral sector's slowest decay). Two checks:
(a) exact (sympy): is the set of six conjugated moves {C^k L C^-k, C^k R C^-k} closed under inversion (so W6 is symmetric
    and W12 = 2 W6)?
(b) numerically (eigvalsh, symmetric): the neutral sector's slowest decay and the charged sectors' top, and their ratio, at
    mod 27 and 81 and at mod 5, 7, 11, 13.
    python3 -B halving_posthoc.py > halving_posthoc_run.txt"""
import importlib.util, pathlib
import numpy as np, sympy as sp
x, y, z = sp.symbols("x y z")
def comp(f, g):   # f o g
    return tuple(sp.expand(e.subs({x: g[0], y: g[1], z: g[2]}, simultaneous=True)) for e in f)
L = (x, z, x*z - y); R = (z, y, y*z - x); Li = (x, x*y - z, y); Ri = (x*y - z, y, x)
C = (y, z, x); Ci = (z, x, y); I = (x, y, z)
assert comp(L, Li) == I and comp(R, Ri) == I and comp(C, Ci) == I
six = {"L": L, "R": R, "CLC^-1": comp(C, comp(L, Ci)), "CRC^-1": comp(C, comp(R, Ci)), "C^2LC^-2": comp(Ci, comp(L, C)), "C^2RC^-2": comp(Ci, comp(R, C))}
inv = {"L^-1": Li, "R^-1": Ri}
for k, v in six.items(): print("%s = %s" % (k, v))
names = {v: k for k, v in six.items()}
def inverse_in_set(g):
    for k, v in six.items():
        if comp(g, v) == I: return k
    return None
print("(a) the inverse of each of the six lies among the six: %s" % {k: inverse_in_set(v) for k, v in six.items()})
print("(a) C L C^-1 = R^-1: %s; C^2 L C^-2 equals: %s" % (six["CLC^-1"] == Ri, [k for k, v in {**six, **inv}.items() if v == six["C^2LC^-2"] and k != "C^2LC^-2"]))
spec = importlib.util.spec_from_file_location("sec", pathlib.Path(__file__).resolve().parent / "sectors.py")
src = (pathlib.Path(__file__).resolve().parent / "sectors.py").read_text().split("res = {}")[0]
ns = {}; exec(compile(src, "sectors_head", "exec"), ns)
from scipy.sparse import csr_matrix
def sector_spectra(N, start):
    pts, idx, pm = ns["leaf"](N, start); n = len(pts); P = ns["P"]
    PC = P(pm["C"]); W2 = P(pm["L"]) + P(pm["R"]); W6 = (W2 + PC @ W2 @ PC.T + PC.T @ W2 @ PC).toarray()
    sym = np.abs(W6 - W6.T).max()
    seen, cyc, fixed = set(), [], []
    for i in range(n):
        if i in seen: continue
        j, k = pm["C"][i], pm["C"][pm["C"][i]]
        if j == i: fixed.append(i); seen.add(i)
        else: cyc.append((i, j, k)); seen.update((i, j, k))
    w = np.exp(2j * np.pi / 3); out = {}
    for q in (0, 1):
        cols = []
        for (i, j, k) in cyc:
            b = np.zeros(n, complex); b[i], b[j], b[k] = 1, w ** (-q), w ** (-2 * q); cols.append(b / np.sqrt(3))
        if q == 0:
            for i in fixed:
                b = np.zeros(n, complex); b[i] = 1; cols.append(b)
        B = np.array(cols).T; M = B.conj().T @ W6 @ B
        out[q] = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2))[::-1]
    return n, sym, out
for N, start, lab in ((27, (3, 3, 3), "mod 27"), (81, (3, 3, 3), "mod 81"), (5, None, "mod 5"), (7, None, "mod 7"), (11, None, "mod 11"), (13, None, "mod 13")):
    n, sym, out = sector_spectra(N, start)
    e0 = out[0]; e1 = out[1]
    slow0 = max(abs(e) for e in e0 if abs(e) < 6 - 1e-9); top1 = max(abs(e) for e in e1)
    print("(b) %s (%d points): W6 symmetric (max |W6 - W6^T| = %s); neutral spectrum top 4 %s; charged top 4 %s; neutral slowest/6 = %.12f, charged top/6 = %.12f, ratio %.12f" % (
        lab, n, sym, np.round(e0[:4], 9).tolist(), np.round(e1[:4], 9).tolist(), slow0 / 6, top1 / 6, slow0 / top1))
