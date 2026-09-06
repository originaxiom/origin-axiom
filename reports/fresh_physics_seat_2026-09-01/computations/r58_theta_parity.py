"""R58 -- theta-parity of the three h^1 classes of m004, EXACT modulo primes p = 1 (mod 3).
27 = Sym16 + Sym8 + Sym0 under the principal sl2.  iota: a->a^-1, b->b^-1, t->t a^-1 realizes theta (T-thetaTANGENT).
rho(iota u) = G^-1 rho(u) G.  Action on cocycles: f -> Sym^n(G) . (f o iota).  Each H^1 is 1-dim; the action is +-1."""
from math import comb
import sys

def run(p):
    om = next(z for z in range(2, p) if (z*z + z + 1) % p == 0)
    inv_ = lambda a: pow(a, p-2, p)
    def mm(X, Y):
        n, m, k = len(X), len(Y[0]), len(Y)
        return [[sum(X[i][l]*Y[l][j] for l in range(k)) % p for j in range(m)] for i in range(n)]
    def minv2(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        di = inv_((a*d - b*c) % p)
        return [[d*di % p, -b*di % p], [-c*di % p, a*di % p]]
    def eye(n): return [[int(i == j) for j in range(n)] for i in range(n)]
    x = [[1, 1], [0, 1]]; y = [[1, 0], [(-om) % p, 1]]
    def ev(word, D):
        M = eye(len(D['a']))
        for ch in word: M = mm(M, D[ch])
        return M
    D2 = {'a': mm(x, minv2(y)), 'b': mm(mm(mm(mm(mm(y, x), minv2(y)), minv2(x)), y), minv2(x)), 't': x}
    for k in 'abt': D2[k.upper()] = minv2(D2[k])
    A, B, T = D2['a'], D2['b'], D2['t']
    assert mm(mm(T, A), minv2(T)) == mm(mm(A, B), A) and mm(mm(T, B), minv2(T)) == mm(A, B)
    iota = {'a': 'A', 'b': 'B', 't': 'tA'}
    def iw(word):
        out = ''
        for ch in word:
            out += iota[ch] if ch.islower() else ''.join(c.swapcase() for c in reversed(iota[ch.lower()]))
        return out
    R1, R2 = 'taTABA', 'tbTBA'
    assert ev(R1, D2) == eye(2) and ev(R2, D2) == eye(2) and ev(iw(R1), D2) == eye(2) and ev(iw(R2), D2) == eye(2)
    # conjugator G (unnormalized): E rho(iota u) = rho(u) E for u in a,b,t  -> nullspace over F_p
    def nullspace(M):   # rows x cols matrix over F_p -> list of null vectors
        M = [row[:] for row in M]; rows, cols = len(M), len(M[0]); piv = []; r = 0
        for c in range(cols):
            pr = next((i for i in range(r, rows) if M[i][c] % p), None)
            if pr is None: continue
            M[r], M[pr] = M[pr], M[r]; iv = inv_(M[r][c]); M[r] = [v*iv % p for v in M[r]]
            for i in range(rows):
                if i != r and M[i][c] % p:
                    f = M[i][c]; M[i] = [(vi - f*vr) % p for vi, vr in zip(M[i], M[r])]
            piv.append(c); r += 1
            if r == rows: break
        free = [c for c in range(cols) if c not in piv]; basis = []
        for fc in free:
            v = [0]*cols; v[fc] = 1
            for i, pc in enumerate(piv): v[pc] = (-M[i][fc]) % p
            basis.append(v)
        return basis, len(piv)
    cols = []
    for k in range(4):
        E = [[0, 0], [0, 0]]; E[k // 2][k % 2] = 1
        col = []
        for u in 'abt':
            P = mm(E, ev(iw(u), D2)); Q = mm(D2[u], E)
            col += [(P[i][j] - Q[i][j]) % p for i in range(2) for j in range(2)]
        cols.append(col)
    Mmat = [[cols[k][i] for k in range(4)] for i in range(12)]
    ns, rk = nullspace(Mmat); assert len(ns) == 1, (len(ns), rk)
    G = [[ns[0][0], ns[0][1]], [ns[0][2], ns[0][3]]]
    detG = (G[0][0]*G[1][1] - G[0][1]*G[1][0]) % p
    for u in 'abt': assert mm(G, ev(iw(u), D2)) == mm(D2[u], G)
    trG = (G[0][0] + G[1][1]) % p
    def symn(M, n):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
        S = [[0]*(n+1) for _ in range(n+1)]
        for k in range(n+1):
            p1 = [comb(n-k, i) * pow(a, n-k-i, p) * pow(c, i, p) % p for i in range(n-k+1)]
            p2 = [comb(k, j) * pow(b, k-j, p) * pow(d, j, p) % p for j in range(k+1)]
            prod = [0]*(n+1)
            for i, u in enumerate(p1):
                for j, v in enumerate(p2): prod[i+j] = (prod[i+j] + u*v) % p
            for m in range(n+1): S[m][k] = prod[m]
        return S
    out = {}
    for n in (0, 8, 16):
        Dn = {k: symn(v, n) for k, v in D2.items()}; dim = n + 1
        assert symn(mm(A, B), n) == mm(symn(A, n), symn(B, n))          # homomorphism control (the B1267 bug)
        def fox(word):
            C = {g: [[0]*dim for _ in range(dim)] for g in 'abt'}; prefix = eye(dim)
            for ch in word:
                g = ch.lower()
                if ch.islower():
                    C[g] = [[(C[g][i][j] + prefix[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = mm(prefix, Dn[g])
                else:
                    Pm = mm(prefix, Dn[g.upper()])
                    C[g] = [[(C[g][i][j] - Pm[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = Pm
            return [C['a'][i] + C['b'][i] + C['t'][i] for i in range(dim)]
        d1 = fox(R1) + fox(R2)                                          # 2dim x 3dim
        I_ = eye(dim)
        d0 = [[(Dn[g][i][j] - I_[i][j]) % p for j in range(dim)] for g in 'abt' for i in range(dim)]   # 3dim x dim
        Z1, _ = nullspace(d1)
        _, rankB = nullspace([[d0[i][j] for i in range(3*dim)] for j in range(dim)])   # rank of d0 = rank of its transpose
        h1 = len(Z1) - rankB
        SG = symn(G, n)
        Iact = []
        for g in 'abt':
            Fg = mm(SG, fox(iw(g))); Iact += Fg
        # find f0 in Z1 \ B1, compute F0 = Iact f0, solve F0 = lam f0 + d0 v
        def matvec(M, v): return [sum(M[i][j]*v[j] for j in range(len(v))) % p for i in range(len(M))]
        d0T = [[d0[i][j] for i in range(3*dim)] for j in range(dim)]
        lam_found = None
        for f0 in Z1:
            # is f0 in B1?  check rank([d0 | f0]) > rank(d0)
            aug = [[d0[i][j] for j in range(dim)] + [f0[i]] for i in range(3*dim)]
            _, r_aug = nullspace([[aug[i][j] for i in range(3*dim)] for j in range(dim+1)])
            if r_aug == rankB: continue
            F0 = matvec(Iact, f0)
            # solve [d0 | f0] (v, lam) = F0  -> nullspace of [d0 | f0 | -F0]
            sys_ = [[d0[i][j] for j in range(dim)] + [f0[i], (-F0[i]) % p] for i in range(3*dim)]
            sol, _ = nullspace(sys_)
            sol = [s for s in sol if s[-1] % p]
            assert sol, "no solution: iota does not preserve H1?!"
            s = sol[0]; lam = s[dim] * inv_(s[dim+1]) % p
            lam_found = lam * pow(inv_(detG), n // 2, p) % p      # normalize det G = 1 (even n: no square root needed)
            break
        out[n] = (h1, lam_found)
    return om, trG, out
for p in (10009, 100003, 1000003):
    om, trG, out = run(p)
    rd = lambda v: ('+1' if v == 1 else '-1' if v == p-1 else str(v))
    print(f"p = {p:7d} (omega = {om}, tr G = {trG} -> order 2 in PSL2):  " + "   ".join(f"Sym^{n}: h1 = {h1}, theta = {rd(lam)}" for n, (h1, lam) in out.items()))

# ---------------- the FIBER: H^1(F_2; Sym^n) before closing, its theta split, and where the M^2-invariant line sits
def fiber(p):
    om = next(z for z in range(2, p) if (z*z + z + 1) % p == 0)
    inv_ = lambda a: pow(a, p-2, p)
    def mm(X, Y):
        n, m, k = len(X), len(Y[0]), len(Y)
        return [[sum(X[i][l]*Y[l][j] for l in range(k)) % p for j in range(m)] for i in range(n)]
    def minv2(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; di = inv_((a*d - b*c) % p)
        return [[d*di % p, -b*di % p], [-c*di % p, a*di % p]]
    def eye(n): return [[int(i == j) for j in range(n)] for i in range(n)]
    x = [[1, 1], [0, 1]]; y = [[1, 0], [(-om) % p, 1]]
    A = mm(x, minv2(y)); B = mm(mm(mm(mm(mm(y, x), minv2(y)), minv2(x)), y), minv2(x)); T = x
    Ai, Bi = minv2(A), minv2(B)
    # G: G A^-1 = A G, G B^-1 = B G  (fiber-only conjugator; same G as before)
    def nullspace(M):
        M = [row[:] for row in M]; rows, cols = len(M), len(M[0]); piv = []; r = 0
        for c in range(cols):
            pr = next((i for i in range(r, rows) if M[i][c] % p), None)
            if pr is None: continue
            M[r], M[pr] = M[pr], M[r]; iv = inv_(M[r][c]); M[r] = [v*iv % p for v in M[r]]
            for i in range(rows):
                if i != r and M[i][c] % p:
                    f = M[i][c]; M[i] = [(vi - f*vr) % p for vi, vr in zip(M[i], M[r])]
            piv.append(c); r += 1
            if r == rows: break
        free = [c for c in range(cols) if c not in piv]; basis = []
        for fc in free:
            v = [0]*cols; v[fc] = 1
            for i, pc in enumerate(piv): v[pc] = (-M[i][fc]) % p
            basis.append(v)
        return basis, len(piv)
    cols = []
    for k in range(4):
        E = [[0, 0], [0, 0]]; E[k // 2][k % 2] = 1; col = []
        for R_, Ri in ((A, Ai), (B, Bi)):
            P = mm(E, Ri); Q = mm(R_, E); col += [(P[i][j] - Q[i][j]) % p for i in range(2) for j in range(2)]
        cols.append(col)
    ns, _ = nullspace([[cols[k][i] for k in range(4)] for i in range(8)]); assert len(ns) == 1
    G = [[ns[0][0], ns[0][1]], [ns[0][2], ns[0][3]]]; detG = (G[0][0]*G[1][1] - G[0][1]*G[1][0]) % p
    def symn(M, n):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; S = [[0]*(n+1) for _ in range(n+1)]
        for k in range(n+1):
            p1 = [comb(n-k, i) * pow(a, n-k-i, p) * pow(c, i, p) % p for i in range(n-k+1)]
            p2 = [comb(k, j) * pow(b, k-j, p) * pow(d, j, p) % p for j in range(k+1)]
            prod = [0]*(n+1)
            for i, u in enumerate(p1):
                for j, v in enumerate(p2): prod[i+j] = (prod[i+j] + u*v) % p
            for m in range(n+1): S[m][k] = prod[m]
        return S
    res = {}
    for n in (0, 8, 16):
        dim = n + 1; SA, SB, ST = symn(A, n), symn(B, n), symn(T, n); SAi, SBi = symn(Ai, n), symn(Bi, n)
        SG = [[v * pow(inv_(detG), n // 2, p) % p if False else v for v in row] for row in symn(G, n)]  # scale fixed below
        scale = pow(inv_(detG), n // 2, p)
        I_ = eye(dim)
        # cocycles on F_2 = (f(a), f(b)) in V^2, no relations. B^1 = {(SA v - v, SB v - v)}.
        # iota: F(a) = SG f(a^-1) = -SG SAi f(a);  F(b) = -SG SBi f(b)
        def blk(M11, M12, M21, M22):
            return [[(M11[i][j]) for j in range(dim)] + [M12[i][j] for j in range(dim)] for i in range(dim)] + \
                   [[(M21[i][j]) for j in range(dim)] + [M22[i][j] for j in range(dim)] for i in range(dim)]
        Z = [[0]*dim for _ in range(dim)]
        NA = [[(-scale * v) % p for v in row] for row in mm(SG, SAi)]; NB = [[(-scale * v) % p for v in row] for row in mm(SG, SBi)]
        Iact = blk(NA, Z, Z, NB)
        # monodromy on cocycles: (phi f)(g) = ST^-1 f(t g t^-1)?  Use the mapping-torus relation: t g t^-1 = phi(g).
        # A cocycle f on F_2 pulled back by phi and conjugated by ST^-1: F(g) = ST^-1 f(phi(g)); phi(a) = aba, phi(b) = ab
        STi = symn(minv2(T), n)
        def foxF(word):   # Fox on the free group with generators a, b
            C = {'a': [[0]*dim for _ in range(dim)], 'b': [[0]*dim for _ in range(dim)]}; prefix = I_
            D = {'a': SA, 'b': SB, 'A': SAi, 'B': SBi}
            for ch in word:
                g = ch.lower()
                if ch.islower():
                    C[g] = [[(C[g][i][j] + prefix[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = mm(prefix, D[g])
                else:
                    Pm = mm(prefix, D[ch]); C[g] = [[(C[g][i][j] - Pm[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = Pm
            return [C['a'][i] + C['b'][i] for i in range(dim)]
        Phi = mm(STi, foxF('aba')) + mm(STi, foxF('ab'))       # 2dim x 2dim
        # H^1 = V^2 / B^1;  work in the quotient: pick complement via nullspace of B^T ... simpler: compute action matrices on V^2,
        # then the induced eigen-structure on the quotient via traces: tr(Iact on H^1) = tr(Iact on V^2) - tr(Iact on B^1).
        # Iact on B^1: coboundary of v maps to coboundary of SG.Sym(iota-action on v)... compute directly: Iact d0 = d0 K  -> K = action on V (dim x dim)
        d0 = [[(SA[i][j] - I_[i][j]) % p for j in range(dim)] for i in range(dim)] + [[(SB[i][j] - I_[i][j]) % p for j in range(dim)] for i in range(dim)]
        # K solves d0 K = Iact d0 (columns): least squares exact via nullspace on the augmented system per column
        def solve(Mat, rhs):   # Mat (r x c), rhs (r) -> one solution
            aug = [Mat[i] + [(-rhs[i]) % p] for i in range(len(Mat))]
            sol, _ = nullspace(aug); sol = [s for s in sol if s[-1] % p]
            s = sol[0]; f = inv_(s[-1]); return [v * f % p for v in s[:-1]]
        rhs_all = mm(Iact, d0)
        K = [[0]*dim for _ in range(dim)]
        for j in range(dim):
            col = solve(d0, [rhs_all[i][j] for i in range(2*dim)])
            for i in range(dim): K[i][j] = col[i]
        assert mm(d0, K) == rhs_all
        trI = (sum(Iact[i][i] for i in range(2*dim)) - sum(K[i][i] for i in range(dim))) % p
        trI = trI if trI <= p // 2 else trI - p
        h0 = 1 if n == 0 else 0
        hdim = 2*dim - dim + h0   # H^1(F_2; V) = 2 dim V - dim V + h^0
        even = (hdim + trI) // 2; odd = (hdim - trI) // 2
        # Lefschetz prediction: tr(iota|H^1) = h0-term - 3*tr(Sym^n G_normalized)   (three fixed points, index +1 each)
        res[n] = (hdim, even, odd, trI)
    return res
for p in (10009, 100003):
    r = fiber(p)
    print(f"p = {p}: fiber H^1(F; Sym^n): " + "   ".join(f"n={n}: dim {h}, theta-even {e}, theta-odd {o} (tr {t})" for n, (h, e, o, t) in r.items()))
