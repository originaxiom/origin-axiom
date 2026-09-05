"""dim H^1(m004; Sym^n) for every n, via Fox calculus over F_p (p = 1 mod 3, so c exists).

Settles what the banked form of Menal-Ferrer-Porti leaves open: what EVEN-dimensional
reps (Sym^ODD n) contribute to h^1.  Three of B1256's four candidate sl2 embeddings
depend on the answer.

Holonomy (B598, banked): <a,b | abABaBAbaB>, a=[[1,1],[0,1]], b=[[1,0],[c,1]], c^2-c+1=0.
Rank over F_p is a LOWER bound for rank over Q(c) (hence h^1 here is an UPPER bound);
two independent primes agreeing is strong evidence, and the n<=4 cases are cross-checked
exactly by the symbolic route.
"""
import sys
from sympy import isprime

def run(p):
    c = next(x for x in range(2, p) if (x*x - x + 1) % p == 0)
    def mul(M, N):
        n = len(M)
        return [[sum(M[i][k]*N[k][j] for k in range(n)) % p for j in range(n)] for i in range(n)]
    def inv2(M):
        (a,b),(cc,d) = M
        det = (a*d - b*cc) % p; di = pow(det, p-2, p)
        return [[d*di % p, (-b)*di % p], [(-cc)*di % p, a*di % p]]
    A = [[1,1],[0,1]]; B = [[1,0],[c,1]]
    G = {"a":A, "b":B, "A":inv2(A), "B":inv2(B)}
    def sym(M, n):
        if n == 0: return [[1]]
        pq, qq, rr, ss = M[0][0], M[0][1], M[1][0], M[1][1]
        out = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):                      # image of X^(n-i) Y^i
            # (pX+qY)^(n-i) (rX+sY)^i  -> coefficients
            poly = [0]*(n+1); poly[0] = 1; deg = 0
            def mulin(poly, deg, u, v):
                new = [0]*(n+1)
                for k in range(deg+1):
                    if poly[k]:
                        new[k]   = (new[k]   + poly[k]*u) % p
                        new[k+1] = (new[k+1] + poly[k]*v) % p
                return new, deg+1
            for _ in range(n-i): poly, deg = mulin(poly, deg, pq, qq)
            for _ in range(i):   poly, deg = mulin(poly, deg, rr, ss)
            for j in range(n+1): out[j][i] = poly[j]
        return out
    def rank(M):
        M = [row[:] for row in M]; rows, cols = len(M), len(M[0]); r = 0
        for cidx in range(cols):
            piv = next((i for i in range(r, rows) if M[i][cidx]), None)
            if piv is None: continue
            M[r], M[piv] = M[piv], M[r]
            iv = pow(M[r][cidx], p-2, p)
            M[r] = [x*iv % p for x in M[r]]
            for i in range(rows):
                if i != r and M[i][cidx]:
                    f = M[i][cidx]
                    M[i] = [(M[i][j] - f*M[r][j]) % p for j in range(cols)]
            r += 1
            if r == rows: break
        return r
    REL = "abABaBAbaB"
    res = []
    for n in range(0, 17):
        N = n+1
        R = {k: sym(v, n) for k, v in G.items()}
        I = [[1 if i==j else 0 for j in range(N)] for i in range(N)]
        # d0
        d0 = [[(R["a"][i][j]-I[i][j]) % p for j in range(N)] for i in range(N)] + \
             [[(R["b"][i][j]-I[i][j]) % p for j in range(N)] for i in range(N)]
        # fox derivatives
        def fox(gen):
            tot = [[0]*N for _ in range(N)]; P = [row[:] for row in I]
            for ch in REL:
                if ch == gen:
                    for i in range(N):
                        for j in range(N): tot[i][j] = (tot[i][j] + P[i][j]) % p
                elif ch == gen.upper():
                    Q = mul(P, R[ch])
                    for i in range(N):
                        for j in range(N): tot[i][j] = (tot[i][j] - Q[i][j]) % p
                P = mul(P, R[ch])
            return tot
        Fa, Fb = fox("a"), fox("b")
        d1 = [Fa[i] + Fb[i] for i in range(N)]        # N x 2N
        h0 = N - rank(d0)
        h1 = (2*N - rank(d1)) - rank(d0)
        res.append((n, N, h0, h1))
    return res

p1 = next(q for q in range(10**6, 10**6+500) if isprime(q) and q % 3 == 1)
p2 = next(q for q in range(10**6+600, 10**6+1200) if isprime(q) and q % 3 == 1)
r1, r2 = run(p1), run(p2)
print(f"two independent primes: {p1}, {p2}\n")
print(" n   dim V   rep type              h^0   h^1   (agree?)")
for (n,N,h0,h1),(n2,N2,h02,h12) in zip(r1, r2):
    typ = "ODD-dim  (Sym^even)" if n%2==0 else "EVEN-dim (Sym^odd) "
    mark = "  <- TRIVIAL" if n==0 else ""
    print(f"{n:2}   {N:5}   {typ}   {h0:3}   {h1:3}   {'yes' if (h0,h1)==(h02,h12) else 'NO'}{mark}")
