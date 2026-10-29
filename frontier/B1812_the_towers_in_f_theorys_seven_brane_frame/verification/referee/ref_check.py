"""B1812 referee: independent recomputation (sympy, exact)."""
import json, math, itertools
import sympy as sp
M = sp.Matrix
def K(p, q): return M([[1 + p*q, -p*p], [q*q, 1 - p*q]])
S = M([[0, -1], [1, 0]]); T = M([[1, 1], [0, 1]])
A, B, C = K(1, 0), K(1, -1), K(1, 1)
L = M([[1, 0], [1, 1]]); R = M([[1, 1], [0, 1]])
LR = L * R
res = {}
# DHIZ (2.2) identifications
res["K_A == T^-1"] = A == T.inv(); res["K_B == S T^2"] = B == S * T**2; res["K_C == T^2 S"] = C == T**2 * S
res["LR"] = LR.tolist(); res["LR symmetric"] = LR == LR.T
def KE(N):  # DHIZ (2.4): K = K_zn ... K_z1 for X1...Xn ; X = A^(N-1) B C C
    seq = [A] * (N - 1) + [B, C, C]
    P = sp.eye(2)
    for X in seq: P = X * P
    return P
def content(Mx):  # SL2Z-conjugacy invariant gcd(b, c, d-a)
    a, b, c, d = Mx
    return math.gcd(math.gcd(int(b), int(c)), int(d - a))
def form(Mx):  # K=[[a,b],[c,d]] -> c x^2 + (d-a) x y - b y^2  (disc = tr^2-4)
    a, b, c, d = Mx
    return (int(c), int(d - a), int(-b))
tab = {}
for N in range(0 + 1, 13):
    k = KE(N)
    tab[N] = {"K": k.tolist(), "tr": int(k.trace()), "content": content(k), "branes": N + 2,
              "type": "elliptic" if abs(k.trace()) < 2 else ("parabolic" if abs(k.trace()) == 2 else "hyperbolic")}
res["E_N"] = tab
res["K(E5) == -K_C (DHIZ 2.9)"] = KE(5) == -C
# conjugator
g = M([[-3, 7], [2, -5]])
res["det g"] = int(g.det()); res["g K(E10) g^-1 == LR"] = g * KE(10) * g.inv() == LR
# metallic words
met = {}
for n in range(1, 6):
    W = R**n * L**n
    met[n] = {"RnLn": W.tolist(), "tr": int(W.trace()), "content": content(W),
              "content K(E_{tr+7})": content(KE(int(W.trace()) + 7)) if W.trace() + 7 <= 40 else None}
res["metallic RnLn"] = met
# alternative metallic: [[n,1],[1,0]]^2 and [[n,1],[1,0]]
alt = {}
for n in range(1, 6):
    Mn = M([[n, 1], [1, 0]]); W = Mn**2
    alt[n] = {"Mn^2": W.tolist(), "tr": int(W.trace()), "content": content(W)}
res["metallic Mn^2"] = alt
# abelianisation SL2Z -> Z12 : T -> 1 ; S -> ? use L=S T^-1 S^-1 relation; compute via word in S,T is messy; use brane count instead
# (L R)^-1 vs L R^-1
res["tr (LR)^-1"] = int((LR.inv()).trace()); res["tr L R^-1"] = int((L * R.inv()).trace())
res["tr -LR"] = int((-LR).trace())
print(json.dumps(res, indent=1, default=str))
json.dump(res, open(__import__("pathlib").Path(__file__).with_name("ref_check.json"), "w"), indent=1, default=str)
