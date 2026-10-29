"""B1812 (P-415 / P-419; main's computation; exact, data-free): the SL(2,Z) monodromies of DeWolfe-Hauer-Iqbal-Zwiebach's E_N
7-brane configurations A^(N-1) B C C and the object's word.  DHIZ-I eq. (2.4): for branes X_1 ... X_n the monodromy is
K = K_{z_n} ... K_{z_1}, with K_[p,q] = [[1 + pq, -p^2], [q^2, 1 - pq]], A = [1,0], B = [1,-1], C = [1,1].
GENESIS's convention: L = [[1,1],[0,1]], R = [[1,0],[1,1]], so LR = [[2,1],[1,1]], RL = [[1,1],[1,2]].
Every number the FINDINGS reports is computed here.
    python3 e_n_monodromy.py      # writes e_n_monodromy.json beside itself"""
import itertools, json, math, pathlib
import sympy as sp

def K(p, q): return sp.Matrix([[1 + p * q, -p * p], [q * q, 1 - p * q]])
A, B, C = K(1, 0), K(1, -1), K(1, 1)
L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]])
LR, RL = L * R, R * L
def KE(N): return C * C * B * A ** (N - 1)                      # DHIZ-I (2.4): K_C K_C K_B K_A^(N-1)
def content(M): a, b, c, d = [int(x) for x in M]; return math.gcd(math.gcd(b, c), d - a)
def kind(M):
    t = int(M.trace()); return "elliptic" if abs(t) < 2 else ("parabolic" if abs(t) == 2 else "hyperbolic")
def conj(X, Y, rng=13):
    """an explicit g in SL(2,Z) with g X g^-1 = Y (small entries), or None"""
    for a, b, c in itertools.product(range(-rng, rng + 1), repeat=3):
        if a == 0 or (1 + b * c) % a: continue
        g = sp.Matrix([[a, b], [c, (1 + b * c) // a]])
        if g * X * g.inv() == Y: return g
    return None
def ints(M): return [[int(x) for x in r] for r in M.tolist()]

out = {"K(E_N)": {}, "LR": ints(LR), "RL": ints(RL)}
for N in range(1, 13):
    M = KE(N)
    out["K(E_N)"][N] = {"K": ints(M), "trace": int(M.trace()), "kind": kind(M), "content": content(M)}
    assert M == sp.Matrix([[-2, 2 * N - 9], [-1, N - 5]]) and int(M.trace()) == N - 7
K10 = KE(10)
g_LR, g_RL = conj(K10, LR), conj(K10, RL)
out["g with g K(E_10) g^-1 = LR (GENESIS)"] = ints(g_LR); out["g with g K(E_10) g^-1 = RL"] = ints(g_RL)
assert g_LR.det() == 1 and g_LR * K10 * g_LR.inv() == LR
# the sister's sign: -RL (trace -3) against K(E_4)
g4 = conj(KE(4), -RL)
out["g with g K(E_4) g^-1 = -RL (the sister's sign class, trace -3)"] = None if g4 is None else ints(g4)
# the metallic word states L^n R^n: traces and contents (content is a conjugacy invariant; every K(E_N) has content 1)
out["metallic L^n R^n"] = {n: {"word": ints((L ** n) * (R ** n)), "trace": int(((L ** n) * (R ** n)).trace()),
                               "content": content((L ** n) * (R ** n))} for n in (1, 2, 3, 4)}
assert all(out["K(E_N)"][N]["content"] == 1 for N in out["K(E_N)"])
out["E_3, E_4 hyperbolic of negative trace (DHIZ: not collapsible)"] = [out["K(E_N)"][3]["kind"], out["K(E_N)"][3]["trace"], out["K(E_N)"][4]["kind"], out["K(E_N)"][4]["trace"]]
(pathlib.Path(__file__).with_suffix(".json")).write_text(json.dumps(out, indent=1), encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "K(E_N)"}, indent=1))
