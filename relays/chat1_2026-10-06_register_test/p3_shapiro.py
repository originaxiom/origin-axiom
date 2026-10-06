"""P3 of the sealed register test: dim H1(ker w; V|) = dim H1(m000; V) + dim H1(m000; V(x)w),
V the natural 2-dim rep of SL(2,F3) over F3, for every surjection rho of pi1(m000).  Fox calculus mod 3."""
import sys, importlib.util
spec = importlib.util.spec_from_file_location("door", __import__("os").path.join(__import__("os").path.dirname(__file__), "p2_door.py"))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    D = importlib.util.module_from_spec(spec); spec.loader.exec_module(D)
p = 3
def M(g): return [[g[0], g[1]], [g[2], g[3]]]
def madd(A, B): return [[(A[i][j]+B[i][j]) % p for j in range(2)] for i in range(2)]
def mmul(A, B): return [[sum(A[i][k]*B[k][j] for k in range(2)) % p for j in range(2)] for i in range(2)]
def neg(A): return [[(-A[i][j]) % p for j in range(2)] for i in range(2)]
Z = [[0, 0], [0, 0]]; ID = [[1, 0], [0, 1]]
def rank(rows):
    rows = [r[:] for r in rows]; rk = 0; ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        piv = next((i for i in range(rk, len(rows)) if rows[i][c] % p), None)
        if piv is None: continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        iv = pow(rows[rk][c], -1, p); rows[rk] = [(v*iv) % p for v in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][c] % p:
                f = rows[i][c]; rows[i] = [(a - f*b) % p for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk
def fox(word, gens, val):        # Fox derivatives of a word (list of (sym,e)), images under val (2x2 mats)
    D_ = {g: Z for g in gens}; pref = ID
    for s, e in word:
        if e == 1:
            D_[s] = madd(D_[s], pref); pref = mmul(pref, val[s])
        else:
            vinv = M(D.inv(tuple(sum(val[s], []))))
            pref = mmul(pref, vinv); D_[s] = madd(D_[s], neg(pref))
    return D_
def h1(gens, rels, val):
    n = len(gens)
    J = []
    for r in rels:
        F = fox(r, gens, val)
        for i in range(2): J.append([F[g][i][j] for g in gens for j in range(2)])
    dimZ = 2*n - rank(J)
    B = [[(val[g][i][j] - (1 if i == j else 0)) % p for g in gens for i in range(2)] for j in range(2)]
    return dimZ - rank(B)
Xg = D.X; Rg = [D.letters(D.R[0])]
res = []; ok = True
for rho in D.SG:
    V = {x: M(rho[x]) for x in Xg}
    Vw = {x: (neg(V[x]) if D.w[x] else V[x]) for x in Xg}
    a = h1(Xg, Rg, V); b = h1(Xg, Rg, Vw)
    psi = {s: M(D.ev(D.SYMS[s], rho)) for s in D.NONTRIV}
    c = h1(D.NONTRIV, D.HREL, psi)
    res.append((a, b, c)); ok &= (c == a + b)
from collections import Counter
print("(dim H1(m000;V), dim H1(m000;V(x)w), dim H1(m004;V|)) over all 48 surjections:", dict(Counter(res)))
print(f"P3 Shapiro: {'PASS' if ok else 'KILL'}")

# ---------- controls: the code must be able to return NON-zero ----------
triv = {x: ID for x in Xg}; trivw = {x: (neg(ID) if D.w[x] else ID) for x in Xg}
psi_t = {s: ID for s in D.NONTRIV}
a, b, c = h1(Xg, Rg, triv), h1(Xg, Rg, trivw), h1(D.NONTRIV, D.HREL, psi_t)
print(f"control, trivial V=F3^2: m000 {a}, m000(x)w {b}, m004 {c}   expected 2, 0, 2 (H1 = Z each): "
      f"{'PASS' if (a, b, c) == (2, 0, 2) else 'FAIL'}")
# a reducible non-trivial rep: G -> Z (the H1 map) -> unipotent [[1,1],[0,1]] mod 3
U = [[1, 1], [0, 1]]
def upow(k): k %= 3; R_ = ID
def unip(k):
    k %= 3; return [[1, k], [0, 1]]
uni = {x: unip(D.phiZ[x]) for x in Xg}; uniw = {x: (neg(uni[x]) if D.w[x] else uni[x]) for x in Xg}
psi_u = {s: unip(sum(D.phiZ[x]*e for x, e in D.SYMS[s])) for s in D.NONTRIV}
a, b, c = h1(Xg, Rg, uni), h1(Xg, Rg, uniw), h1(D.NONTRIV, D.HREL, psi_u)
print(f"control, unipotent V: m000 {a}, m000(x)w {b}, m004 {c}   Shapiro c = a + b: {'PASS' if c == a + b else 'FAIL'}  (non-vacuous: {c > 0})")
