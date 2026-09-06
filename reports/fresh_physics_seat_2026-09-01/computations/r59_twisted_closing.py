"""R59 -- the twisted closing. On the fiber H^1(F; Sym^n) compute the monodromy action Phi (from t, = M^2) and
theta = iota; the invariants of Phi (= m004's class) and of Phi.iota (= the bundle with monodromy -M^2 = the sister m003),
with theta-parities; and whether M^2 has eigenvalue -1 on the theta-odd sector. Exact mod p."""
from math import comb
def run(p):
    om = next(z for z in range(2, p) if (z*z + z + 1) % p == 0)
    inv_ = lambda a: pow(a, p-2, p)
    def mm(X, Y):
        n, m, k = len(X), len(Y[0]), len(Y)
        return [[sum(X[i][l]*Y[l][j] for l in range(k)) % p for j in range(m)] for i in range(n)]
    def minv2(M):
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]; di = inv_((a*d - b*c) % p)
        return [[d*di % p, -b*di % p], [-c*di % p, a*di % p]]
    def eye(n): return [[int(i == j) for j in range(n)] for i in range(n)]
    def rref_null(M):
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
    x = [[1, 1], [0, 1]]; y = [[1, 0], [(-om) % p, 1]]
    A = mm(x, minv2(y)); B = mm(mm(mm(mm(mm(y, x), minv2(y)), minv2(x)), y), minv2(x)); T = x
    Ai, Bi, Ti = minv2(A), minv2(B), minv2(T)
    cols = []
    for k in range(4):
        E = [[0, 0], [0, 0]]; E[k // 2][k % 2] = 1; col = []
        for R_, Ri in ((A, Ai), (B, Bi)):
            P = mm(E, Ri); Q = mm(R_, E); col += [(P[i][j] - Q[i][j]) % p for i in range(2) for j in range(2)]
        cols.append(col)
    ns, _ = rref_null([[cols[k][i] for k in range(4)] for i in range(8)]); assert len(ns) == 1
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
    out = {}
    for n in (8, 16):
        dim = n + 1; D = {'a': symn(A, n), 'b': symn(B, n), 'A': symn(Ai, n), 'B': symn(Bi, n)}
        STi = symn(Ti, n); scale = pow(inv_(detG), n // 2, p); SG = [[v*scale % p for v in row] for row in symn(G, n)]
        I_ = eye(dim)
        def fox(word):
            C = {'a': [[0]*dim for _ in range(dim)], 'b': [[0]*dim for _ in range(dim)]}; prefix = I_
            for ch in word:
                g = ch.lower()
                if ch.islower():
                    C[g] = [[(C[g][i][j] + prefix[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = mm(prefix, D[g])
                else:
                    Pm = mm(prefix, D[ch]); C[g] = [[(C[g][i][j] - Pm[i][j]) % p for j in range(dim)] for i in range(dim)]; prefix = Pm
            return [C['a'][i] + C['b'][i] for i in range(dim)]
        # monodromy on fiber cocycles: (Phi f)(g) = T^-1 . f(phi(g)),  phi(a)=aba, phi(b)=ab   [t g t^-1 = phi(g), rho(t)=T]
        Phi = mm(STi, fox('aba')) + mm(STi, fox('ab'))
        # iota on fiber cocycles: (I f)(g) = SG . f(iota g) = -SG D[g^-1] f(g)
        Z = [[0]*dim for _ in range(dim)]
        NA = [[(-v) % p for v in row] for row in mm(SG, D['A'])]; NB = [[(-v) % p for v in row] for row in mm(SG, D['B'])]
        Iact = [NA[i] + Z[i] for i in range(dim)] + [Z[i] + NB[i] for i in range(dim)]
        d0 = [[(D['a'][i][j] - I_[i][j]) % p for j in range(dim)] for i in range(dim)] + [[(D['b'][i][j] - I_[i][j]) % p for j in range(dim)] for i in range(dim)]
        # quotient V^2 / B^1: choose a complement basis: columns of d0 span B^1 (dim = dim V, h^0 = 0); pick standard vectors completing it
        Bcols = [[d0[i][j] for i in range(2*dim)] for j in range(dim)]   # rows = basis vectors of B^1
        basis = Bcols[:]; comp = []
        for e in range(2*dim):
            v = [0]*(2*dim); v[e] = 1
            _, r_before = rref_null([row[:] for row in basis] + [[0]*(2*dim)]) if False else (None, None)
            test = basis + [v]
            _, rk = rref_null([[test[i][j] for i in range(len(test))] for j in range(2*dim)])
            if rk == len(test): basis.append(v); comp.append(e)
            if len(comp) == dim: break
        assert len(comp) == dim
        # coordinates: express any vector w in the basis [B^1 | comp]; keep the comp part -> map on H^1
        Bmat = [[basis[i][j] for i in range(2*dim)] for j in range(2*dim)]   # columns = basis vectors (2dim x 2dim)
        def coords(w):
            sol, _ = rref_null([Bmat[i] + [(-w[i]) % p] for i in range(2*dim)])
            s = [s for s in sol if s[-1] % p][0]; f = inv_(s[-1]); return [v*f % p for v in s[:-1]]
        def induced(Mat):   # Mat acting on V^2 (2dim x 2dim) -> matrix on H^1 (dim x dim) in the comp coordinates
            H = [[0]*dim for _ in range(dim)]
            for j, e in enumerate(comp):
                v = [0]*(2*dim); v[e] = 1
                w = [sum(Mat[i][k]*v[k] for k in range(2*dim)) % p for i in range(2*dim)]
                c = coords(w)
                for i in range(dim): H[i][j] = c[dim + i]
            return H
        HPhi, HI = induced(Phi), induced(Iact)
        assert mm(HPhi, HI) == mm(HI, HPhi), "monodromy and theta do not commute on H^1"
        assert mm(HI, HI) == eye(dim)
        def fixed(Mat, sign=1):
            Mm = [[(Mat[i][j] - sign*I_[i][j]) % p for j in range(dim)] for i in range(dim)]
            ns, _ = rref_null(Mm); return ns
        def parity(v):
            w = [sum(HI[i][j]*v[j] for j in range(dim)) % p for i in range(dim)]
            if w == v: return '+1'
            if w == [(-c) % p for c in v]: return '-1'
            return 'mixed'
        fix_m004 = fixed(HPhi)                       # invariants of M^2
        HPhiI = mm(HPhi, HI)
        fix_m003 = fixed(HPhiI)                      # invariants of -M^2 (the theta-twisted closing = the sister)
        neg_on_odd = fixed(HPhi, -1)                 # M^2 = -1 eigenvectors
        # k-fold cyclic covers of the object: invariants of (M^2)^k, and of (-M^2)^k, on H^1(F; V), with parities
        covers = {}
        Pk = I_; PIk = I_
        for k in range(1, 13):
            Pk = mm(Pk, HPhi); PIk = mm(PIk, HPhiI)
            fk = fixed(Pk); fik = fixed(PIk)
            covers[k] = (len(fk), sorted(set(parity(v) for v in fk)), len(fik), sorted(set(parity(v) for v in fik)))
        out[n] = dict(covers=covers, h1_m004=len(fix_m004), par_m004=[parity(v) for v in fix_m004],
                      h1_m003=len(fix_m003), par_m003=[parity(v) for v in fix_m003],
                      M2_eig_minus1=len(neg_on_odd), par_minus1=[parity(v) for v in neg_on_odd],
                      same_line=(fix_m004 == fix_m003))
    return out
for p in (10009, 100003):
    o = run(p)
    for n, r in o.items():
        cv = r['covers']; print(f"p={p} n={n}: cyclic covers k=1..12 of m004: h1(F)^(M^2k) dims {[cv[k][0] for k in cv]} parities {sorted(set(sum([cv[k][1] for k in cv], [])))};  of m003: dims {[cv[k][2] for k in cv]} parities {sorted(set(sum([cv[k][3] for k in cv], [])))}")
        print(f"p={p} n={n}: m004 (M^2-fixed): h1={r['h1_m004']} theta={r['par_m004']} | sister m003 (-M^2-fixed): h1={r['h1_m003']} theta={r['par_m003']} | M^2 eigenvalue -1 on H^1(F): dim={r['M2_eig_minus1']} theta={r['par_minus1']} | same line: {r['same_line']}")
