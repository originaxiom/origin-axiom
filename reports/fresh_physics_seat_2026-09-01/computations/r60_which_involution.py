"""Which involution grades H^1(m004; Sym^n)?  Compare on the KNOT presentation <x,y | abABaBAbaB>:
  (S) strong inversion  x->x^-1, y->y^-1
  (I) the fiber's hyperelliptic -I, transported: a=x y^-1 -> a^-1, b -> b^-1, t=x -> t a^-1  => x -> x a^-1 = x y x^-1, y -> a^-1 x = y x^-1 x ... computed from words
Exact mod p."""
from math import comb
def run(p, n_list=(2, 8, 10, 14, 16, 22)):
    om = next(z for z in range(2, p) if (z*z + z + 1) % p == 0)
    inv_ = lambda a: pow(a, p-2, p)
    def mm(X, Y):
        n, m, k = len(X), len(Y[0]), len(Y)
        return [[sum(X[i][l]*Y[l][j] for l in range(k)) % p for j in range(m)] for i in range(n)]
    def minv2(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; di = inv_((a*d - b*c) % p)
        return [[d*di % p, -b*di % p], [-c*di % p, a*di % p]]
    def eye(n): return [[int(i == j) for j in range(n)] for i in range(n)]
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
    X = [[1, 1], [0, 1]]; Y = [[1, 0], [(-om) % p, 1]]
    D = {'x': X, 'y': Y, 'X': minv2(X), 'Y': minv2(Y)}
    def ev(word, DD):
        M = eye(len(DD['x']))
        for ch in word: M = mm(M, DD[ch])
        return M
    REL = 'xyXYxYXyxY'
    assert ev(REL, D) == eye(2)
    def invw(w): return ''.join(c.swapcase() for c in reversed(w))
    # the fiber involution transported to the knot generators: a = xY, b = yxYXyX, t = x;  iota: a->A, b->B, t->tA
    # x = t -> t a^-1 = x (xY)^-1 = x y X ;  y = a^-1 x -> (a^-1)^-1 ... y = A t  => iota(y) = a . t a^-1 = (xY)(x)(yX) = xYxyX
    autos = {'strong inversion x->X, y->Y': {'x': 'X', 'y': 'Y'},
             'fiber -I transported': {'x': 'xyX', 'y': 'xYxyX'}}
    out = {}
    for name, mp in autos.items():
        def iw(word):
            o = ''
            for ch in word: o += mp[ch] if ch.islower() else invw(mp[ch.lower()])
            return o
        ok = ev(iw(REL), D) == eye(2)
        # conjugator E: E rho(iw(u)) = rho(u) E
        cols = []
        for k in range(4):
            E = [[0, 0], [0, 0]]; E[k // 2][k % 2] = 1; col = []
            for u in 'xy':
                P = mm(E, ev(iw(u), D)); Q = mm(D[u], E); col += [(P[i][j] - Q[i][j]) % p for i in range(2) for j in range(2)]
            cols.append(col)
        ns, _ = nullspace([[cols[k][i] for k in range(4)] for i in range(8)])
        if not ok or len(ns) != 1:
            out[name] = f"relator preserved: {ok}, conjugator dim {len(ns)}"; continue
        G = [[ns[0][0], ns[0][1]], [ns[0][2], ns[0][3]]]; detG = (G[0][0]*G[1][1] - G[0][1]*G[1][0]) % p
        trG = (G[0][0] + G[1][1]) % p
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
        for n in n_list:
            dim = n + 1; Dn = {k: symn(v, n) for k, v in D.items()}; I_ = eye(dim)
            def fox(word):
                C = {g: [[0]*dim for _ in range(dim)] for g in 'xy'}; prefix = I_
                for ch in word:
                    g = ch.lower()
                    if ch.islower():
                        C[g] = [[(C[g][i][j] + prefix[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = mm(prefix, Dn[g])
                    else:
                        Pm = mm(prefix, Dn[ch]); C[g] = [[(C[g][i][j] - Pm[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = Pm
                return [C['x'][i] + C['y'][i] for i in range(dim)]
            d1 = fox(REL)
            d0 = [[(Dn['x'][i][j] - I_[i][j]) % p for j in range(dim)] for i in range(dim)] + [[(Dn['y'][i][j] - I_[i][j]) % p for j in range(dim)] for i in range(dim)]
            Z1, _ = nullspace(d1)
            _, rankB = nullspace([[d0[i][j] for i in range(2*dim)] for j in range(dim)])
            h1 = len(Z1) - rankB
            SG = symn(G, n); scale = pow(inv_(detG), n // 2, p)
            Iact = []
            for g in 'xy': Iact += mm(SG, fox(iw(g)))
            lam = None
            for f0 in Z1:
                aug = [[d0[i][j] for j in range(dim)] + [f0[i]] for i in range(2*dim)]
                _, r_aug = nullspace([[aug[i][j] for i in range(2*dim)] for j in range(dim+1)])
                if r_aug == rankB: continue
                F0 = [sum(Iact[i][j]*f0[j] for j in range(2*dim)) % p for i in range(2*dim)]
                sys_ = [[d0[i][j] for j in range(dim)] + [f0[i], (-F0[i]) % p] for i in range(2*dim)]
                sol, _ = nullspace(sys_); sol = [s for s in sol if s[-1] % p]
                s = sol[0]; lam = s[dim] * inv_(s[dim+1]) % p * scale % p
                break
            res[n] = (h1, '+1' if lam == 1 else '-1' if lam == p-1 else lam)
        out[name] = (f"tr G = {trG}", res)
    return out
for p in (10009, 100003):
    for k, v in run(p).items(): print(f"p={p}  {k}: {v}")
