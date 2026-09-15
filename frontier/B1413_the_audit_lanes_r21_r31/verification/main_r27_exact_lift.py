"""Main's exact recomputation of the audit lane's R27 positive (2026-09-15): pi1(m010) = <a,b | aabaBaaBab>, mu = AbAA,
lambda = babA (SnapPy's presentation, verified below); A = [[0,1],[-1,1]], B = [[0,u^2],[u,-2]] over Q(u), u^2 - u + 1 = 0;
chi(a) = u, chi(b) = -1; V = Sym^3(rho) (x) chi (dim 4). Computes a0 = h^0, a1 = h^1, the restriction rank r1 of
H^1(Q;V) -> H^1(T;V), n = a1 - r1, for V, V*, and the semisimplification; the common eigenvector (1,u); all exact."""
import sympy as sp, snappy
u = sp.symbols('u'); MIN = u**2 - u + 1
def red(x): return sp.rem(sp.expand(x), MIN, u)
def M(m): return sp.Matrix(m).applyfunc(red)
def mul(P, Q): return (P*Q).applyfunc(red)
def inv2(P): d = red(P.det()); assert d == 1, d; return M([[P[1,1], -P[0,1]], [-P[1,0], P[0,0]]])
G = snappy.Manifold("m010").fundamental_group(); rel = G.relators()[0]; mu, lam = G.peripheral_curves()[0]
print("m010 presentation:", G.generators(), rel, "peripheral", (mu, lam), "  [lane: aabaBaaBab, AbAA, babA]")
A = M([[0,1],[-1,1]]); B = M([[0,u**2],[u,-2]])
def word(w, X, Y):
    D = {'a': X, 'b': Y, 'A': inv2(X), 'B': inv2(Y)}; R = sp.eye(2)
    for ch in w: R = mul(R, D[ch])
    return R
print("det A, det B:", red(A.det()), red(B.det()), "| relator ->", word(rel, A, B).tolist())
chi = {'a': u, 'b': -1}
def chiw(w):
    v = 1
    for ch in w: v = red(v * (chi[ch.lower()] if ch.islower() else sp.invert(chi[ch.lower()], MIN, u)))
    return red(v)
print("chi on relator, mu, lambda:", chiw(rel), chiw(mu), chiw(lam))
# Sym^3 of a 2x2 matrix on x^3, x^2 y, x y^2, y^3
def sym3(P):
    a, b, c, d = P[0,0], P[0,1], P[1,0], P[1,1]
    cols = []
    for i in range(4):   # image of x^(3-i) y^i = (a x + c y)^(3-i) (b x + d y)^i
        poly = sp.expand((a*sp.Symbol('x') + c*sp.Symbol('y'))**(3-i) * (b*sp.Symbol('x') + d*sp.Symbol('y'))**i)
        cols.append([red(poly.coeff(sp.Symbol('x'), 3-j).coeff(sp.Symbol('y'), j)) for j in range(4)])
    return sp.Matrix(cols).T
def rep_of(gen_imgs):
    return {g: gen_imgs[g] for g in gen_imgs}
def inv4(P):
    adj = P.adjugate().applyfunc(red); d = red(P.det()); di = sp.invert(d, MIN, u)
    return (adj * di).applyfunc(red)
def fox_data(Ra, Rb, wordlist):
    n = Ra.rows; I = sp.eye(n); D = {'a': Ra, 'b': Rb, 'A': inv4(Ra), 'B': inv4(Rb)}
    def w(wd):
        R = I
        for ch in wd: R = (R*D[ch]).applyfunc(red)
        return R
    def fox(wd):
        val = I; dd = {'a': sp.zeros(n), 'b': sp.zeros(n)}
        for ch in wd:
            g = ch.lower(); X = D[ch]
            if ch.islower(): dd[g] = (dd[g] + val).applyfunc(red)
            else: dd[g] = (dd[g] - val*X).applyfunc(red)
            val = (val*X).applyfunc(red)
        return val, dd
    return w, fox
def rank(Mx): return Mx.applyfunc(red).rank(iszerofunc=lambda x: red(sp.cancel(x)) == 0)
def counts(Ra, Rb, label):
    n = Ra.rows; I = sp.eye(n); w, fox = fox_data(Ra, Rb, None)
    val, dd = fox(rel); assert (val - I).applyfunc(red) == sp.zeros(n), label + " relator"
    d0 = sp.Matrix.vstack((Ra - I), (Rb - I)); r0 = rank(d0); a0 = n - r0
    d1 = sp.Matrix.hstack(dd['a'], dd['b']); r1d = rank(d1); a1 = (2*n - r1d) - r0
    # boundary: the torus T = <mu, lambda>, cochains H^1(T;V): cocycles z(mu), z(lambda) in V^2 with the torus relation;
    # restriction of a group 1-cocycle f (given by f(a), f(b)) to mu and lambda via the Fox derivatives of the peripheral words
    _, fm = fox(mu); _, fl = fox(lam)
    Rmu = sp.Matrix.hstack(fm['a'], fm['b']); Rlam = sp.Matrix.hstack(fl['a'], fl['b'])
    # H^1(T;V) = Z^1(T;V)/B^1(T;V); compute rank of the restriction on H^1(Q;V): rank of [Rmu; Rlam] on Z^1(Q) modulo (B^1(Q) mapped) and modulo B^1(T)
    Wm, Wl = w(mu), w(lam)
    BT = sp.Matrix.vstack(Wm - I, Wl - I)          # coboundaries on T: v -> ((Wmu - I) v, (Wlam - I) v)
    R = sp.Matrix.vstack(Rmu, Rlam)                # restriction of a 1-cochain (f(a), f(b)) to (f(mu), f(lambda))
    block = sp.Matrix.vstack(sp.Matrix.hstack(d1, sp.zeros(d1.rows, n)), sp.Matrix.hstack(R, BT))
    rT = rank(block) - rank(d1) - rank(BT)         # dim of the image of Z^1(Q) in H^1(T) = C^1(T)/B^1(T) (stacked-rank identity)
    t0 = n - rank(BT); t1 = 2*t0                    # torus: h^1(T) = 2 h^0(T)
    n_int = a1 - rT
    print(f"{label:24s} a0={a0} a1={a1} t0={t0} t1={t1} r1={rT} n=a1-r1={n_int}")
    return n_int
S3A, S3B = sym3(A), sym3(B)
VA, VB = (S3A*chi['a']).applyfunc(red), (S3B*chi['b']).applyfunc(red)
nV = counts(VA, VB, "V = Sym3 (x) chi")
VAd, VBd = inv4(VA).T, inv4(VB).T
nVd = counts(VAd, VBd, "V* (dual)")
print("I(V) = n(V) - n(V*) =", nV - nVd, "  [lane: +1]")
# common eigenvector and semisimplification
v = sp.Matrix([1, u]); print("A v - u v:", (A*v - u*v).applyfunc(red).T.tolist(), " B v + v:", (B*v + v).applyfunc(red).T.tolist(), "-> (1,u) common eigenvector, eigenvalues u and -1: reducible base")
P = M([[1,0],[u,1]]); Ac, Bc = mul(mul(inv2(P), A), P), mul(mul(inv2(P), B), P); print("conjugated A, B:", Ac.tolist(), Bc.tolist())
# semisimplification of V: keep the diagonal (block) parts in the flag basis: Sym3 of the diagonal parts of Ac, Bc, tensored with chi
Ad = M([[Ac[0,0],0],[0,Ac[1,1]]]); Bd = M([[Bc[0,0],0],[0,Bc[1,1]]])
SA, SB = (sym3(Ad)*chi['a']).applyfunc(red), (sym3(Bd)*chi['b']).applyfunc(red)
nS = counts(SA, SB, "V semisimplified"); nSd = counts(inv4(SA).T, inv4(SB).T, "dual of semisimplif.")
print("I(V^ss) =", nS - nSd, "  [lane: 0]")
