"""Independent check of the period-2 automorphism P: a->A, b->aaab.
(1) exact: rho(P(r)) = I in Q(zeta_12), triple identical;  (2) its action on H1(C) = H1(M; Z[Z/3]) by Fox calculus in the
regular representation of Z/3 (Shapiro) with Smith normal form over Z -- no Reidemeister-Schreier anywhere."""
import os, sys, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
from d2lib import OMEGA
from fractions import Fraction as Fr

REL = L.word_from_snappy("aaabABBAb")
A = L.mat([[1 - OMEGA, 1], [-1, 0]]); B = L.mat([[0, -1], [1, OMEGA * (-2)]])
rho = L.Rep({"a": A, "b": B})
def subst(word, images):
    out = []
    for g, e in word: out += images[g] if e == 1 else L.inv_word(images[g])
    return L.free_reduce(out)
P = {"a": L.word_from_snappy("A"), "b": L.word_from_snappy("aaab")}
S = {"a": L.word_from_snappy("A"), "b": L.word_from_snappy("B")}
DK = {"a": L.word_from_snappy("Bab"), "b": L.word_from_snappy("b")}
ID = {"a": L.word_from_snappy("a"), "b": L.word_from_snappy("b")}
Pr = subst(REL, P)
print("P(r) =", L.word_to_snappy(Pr), " rho(P(r)) =", rho(Pr), " == I:", L.meq(rho(Pr), L.eye(2)))
print("exact triple of P: ", L.tr(rho(P['a'])), L.tr(rho(P['b'])), L.tr(rho(P['a'] + P['b'])))
print("exact triple of id:", L.tr(A), L.tr(B), L.tr(rho(L.word_from_snappy('ab'))))
assert L.meq(rho(Pr), L.eye(2)) and L.tr(rho(P['a'])) == L.tr(A) and L.tr(rho(P['b'])) == L.tr(B)

phi = {"a": 0, "b": 1}; gens = ["a", "b"]
def perm(k):
    M = [[0] * 3 for _ in range(3)]
    for j in range(3): M[(j + k) % 3][j] = 1
    return M
def imul(X, Y): return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
def iadd(X, Y): return [[a + b for a, b in zip(r, s)] for r, s in zip(X, Y)]
def isub(X, Y): return [[a - b for a, b in zip(r, s)] for r, s in zip(X, Y)]
I3 = [[int(i == j) for j in range(3)] for i in range(3)]
class IntRep:
    def letter(self, g, e): return perm(phi[g] * e)
rep = IntRep()
def ifox(word):
    D = {g: [[0] * 3 for _ in range(3)] for g in gens}; Pm = I3
    for g, e in word:
        if e == 1: D[g] = iadd(D[g], Pm); Pm = imul(Pm, rep.letter(g, 1))
        else: Pm = imul(Pm, rep.letter(g, -1)); D[g] = isub(D[g], Pm)
    return D
def iblock(blocks):
    rows = []
    for br in blocks:
        for i in range(3): rows.append([x for blk in br for x in blk[i]])
    return rows
d1 = iblock([[isub(perm(phi[g]), I3) for g in gens]])
Dfox = ifox(REL); d2 = iblock([[Dfox[g]] for g in gens])
print("d1*d2 == 0:", all(x == 0 for r in imul(d1, d2) for x in r))
Dg, U, V = L.smith([r[:] for r in d1], 6)
rk = sum(1 for i in range(3) if Dg[i][i] != 0)
kerbasis = [[V[i][j] for i in range(6)] for j in range(rk, 6)]
def inv_int(M):
    n = len(M); A_ = [[Fr(x) for x in r] + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(M)]
    for c in range(n):
        p = next(i for i in range(c, n) if A_[i][c] != 0); A_[c], A_[p] = A_[p], A_[c]
        pv = A_[c][c]; A_[c] = [x / pv for x in A_[c]]
        for i in range(n):
            if i != c and A_[i][c] != 0:
                f = A_[i][c]; A_[i] = [x - f * y for x, y in zip(A_[i], A_[c])]
    R = [r[n:] for r in A_]; assert all(x.denominator == 1 for r in R for x in r); return [[int(x) for x in r] for r in R]
Vinv = inv_int(V)
def kcoords(x):
    y = [sum(Vinv[i][j] * x[j] for j in range(6)) for i in range(6)]
    assert all(y[i] == 0 for i in range(rk)), "not in kernel"
    return y[rk:]
rel_rows = [kcoords([d2[i][j] for i in range(6)]) for j in range(3)]
Dh, Uh, Vh = L.smith([r[:] for r in rel_rows], len(kerbasis))
invs = [Dh[i][i] if i < len(Dh) else 0 for i in range(len(kerbasis))]
print("H1(C) via Shapiro/Fox over Z[Z/3]: invariants", invs, " -> Z/4 + Z/4 + Z")
assert sorted(invs) == [0, 1, 4, 4]
def chain_map(E):
    eps = 1 if sum(e for g, e in E["b"] if g == "b") % 3 == 1 else -1
    Ebar = [[int(i == (eps * j) % 3) for j in range(3)] for i in range(3)]
    Jm = [[0] * 6 for _ in range(6)]
    for hi, h in enumerate(gens):
        DE = ifox(E[h])
        for gi, g in enumerate(gens):
            blk = imul(DE[g], Ebar)                     # semilinear: coefficient ring carried along (t -> t^eps)
            for i in range(3):
                for j in range(3): Jm[gi * 3 + i][hi * 3 + j] = blk[i][j]
    ok = imul(d1, Jm) == imul(Ebar, d1)
    return Jm, ok, eps
keep = [j for j in range(len(invs)) if invs[j] != 1]
tor = [j for j in keep if invs[j] == 4]; fre = [j for j in keep if invs[j] == 0]
def h1(c):
    y = [sum(c[i] * Vh[i][j] for i in range(len(c))) for j in range(len(c))]
    return tuple((y[j] % invs[j]) if invs[j] else y[j] for j in range(len(c)))
Bsrc = [h1([int(i == k) for i in range(len(kerbasis))]) for k in range(len(kerbasis))]
def induced(E, name):
    Jm, ok, eps = chain_map(E)
    Bimg = [h1(kcoords([sum(Jm[i][j] * v[j] for j in range(6)) for i in range(6)])) for v in kerbasis]
    sols = []
    for T in itertools.product(range(4), repeat=4):
        Tm = [[T[0], T[1]], [T[2], T[3]]]
        for c in itertools.product(range(4), repeat=2):
            for f in (1, -1):
                good = True
                for s, m in zip(Bsrc, Bimg):
                    st = [s[tor[0]], s[tor[1]]]; sf = s[fre[0]]
                    pred = [(Tm[i][0] * st[0] + Tm[i][1] * st[1] + c[i] * sf) % 4 for i in range(2)]
                    if pred != [m[tor[0]] % 4, m[tor[1]] % 4] or f * sf != m[fre[0]]: good = False; break
                if good: sols.append((Tm, c, f))
    for Tm, c, f in sols:
        trc = (Tm[0][0] + Tm[1][1]) % 4; det = (Tm[0][0] * Tm[1][1] - Tm[0][1] * Tm[1][0]) % 4
        print(f"{name:34s} chain-map ok={ok} eps(Z/3)={eps:+d}  T(torsion)={Tm} (tr {trc}, det {det} mod 4)  f={f:+d} c={c}")
    return sols
induced(ID, "identity")
induced(DK, "deck (conj by B)")
induced(S, "strong inversion a->A, b->B")
solsP = induced(P, "PERIOD-2 a->A, b->aaab")
verdict = any(Tm == [[3, 0], [0, 3]] and f == 1 for Tm, c, f in solsP)
print("\nVERDICT (independent of Reidemeister-Schreier): period-2 acts as -1 on Tors H1(C), +1 on the free part:", verdict)
assert verdict
