"""B643 continuation — the inner-corrected flip (L93 refined).
Step 1: find the conjugator w with phi(LONG) ~ w LONG^{+-1} w^{-1}
(SL(2) fingerprint search over short words). Step 2: the corrected
tau* = flip . Ad-correction; gates F1-F3 rerun."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)
K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
kconj = mod["kconj"]

# SL(2) fingerprints over Q(sqrt-3)
from fractions import Fraction as Fr
lets2 = mod["lets2"]
def wmat2(w):
    M = [[K1, K0], [K0, K1]]
    for ch in w:
        g = lets2[ch]
        M = [[M[i][0]*g[0][j] + M[i][1]*g[1][j] for j in range(2)]
             for i in range(2)]
    return M
def m2key(M):
    return tuple((x.a, x.b) for row in M for x in row)
def minv2(M):
    return [[M[1][1], K0 - M[0][1]], [K0 - M[1][0], M[0][0]]]
def mm2(A, B):
    return [[A[i][0]*B[0][j] + A[i][1]*B[1][j] for j in range(2)]
            for i in range(2)]

def phi_w(wd):
    m = {'a': "a", 'b': "baB", 'A': "A", 'B': inv("baB")}
    return freduce("".join(m[ch] for ch in wd))

PHI_L = wmat2(phi_w(LONG))
Lm = wmat2(LONG)
Lmi = minv2(Lm)
# search w over BFS words: PHI_L == w * L^{+-1} * w^{-1}
targets = {"lam": Lm, "lam_inv": Lmi}
frontier = [""]
seen = {""}
found = None
for depth in range(9):
    new = []
    for wd in frontier:
        W = wmat2(wd)
        Wi = minv2(W)
        for nm, Tg in targets.items():
            C = mm2(mm2(W, Tg), Wi)
            if m2key(C) == m2key(PHI_L):
                found = (wd, nm)
                break
        if found:
            break
        for ch in "abAB":
            if wd and wd[-1] == ch.swapcase():
                continue
            nw = wd + ch
            if nw not in seen:
                seen.add(nw)
                new.append(nw)
    if found:
        break
    frontier = new
print(f"conjugator search: {found}", flush=True)
# also check the meridian: phi(a) = a  => mu fixed
print(f"phi(mu) = mu: {m2key(wmat2(phi_w('a'))) == m2key(wmat2('a'))}",
      flush=True)
print("B643-refined step 1 DONE", flush=True)
