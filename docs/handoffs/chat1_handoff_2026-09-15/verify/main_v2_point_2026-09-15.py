"""chat1's V_2 point (HMP section 11): K, L with x0=y0=-4, x1=-17/2+sqrt(145)/2, y1=11/2+sqrt(145)/2.
Checks: K^3 = L^3 = (KL)^4 = I; the figure-eight relator on (a,b) -> (K,L) in SnapPy's presentation (all four role assignments);
Fox h^1 for the 3, the dual 3bar, the trivial rep, and the adjoint sl_3 (via X -> K X K^-1 on 3x3 traceless matrices)."""
import mpmath as mp, itertools, snappy
mp.mp.dps = 120
s = mp.sqrt(145); x0 = y0 = mp.mpf(-4); x1 = mp.mpf(-17)/2 + s/2; y1 = mp.mpf(11)/2 + s/2
K = mp.matrix([[0,0,1],[x0,1,x1],[-1,0,-1]]); L = mp.matrix([[1,y0,y1],[0,-1,-1],[0,1,0]])
I3 = mp.eye(3)
def dev(M, N): return max(abs(M[i,j]-N[i,j]) for i in range(M.rows) for j in range(M.cols))
print("det K, det L:", mp.nstr(mp.det(K),8), mp.nstr(mp.det(L),8))
print("K^3=I:", mp.nstr(dev(K**3,I3),3), " L^3=I:", mp.nstr(dev(L**3,I3),3), " (KL)^4=I:", mp.nstr(dev((K*L)**4,I3),3))
rel = snappy.Manifold("m004").fundamental_group().relators()[0]; print("relator:", rel)
def word(w, A, B):
    Mx = mp.eye(A.rows); D = {'a': A, 'b': B, 'A': A**-1, 'B': B**-1}
    for ch in w: Mx = Mx * D[ch]
    return Mx
for name,(A,B) in {"a->K,b->L":(K,L), "a->L,b->K":(L,K), "a->K^-1,b->L":(K**-1,L), "a->K,b->L^-1":(K,L**-1)}.items():
    print(f"  relator under {name}: dev from I = {mp.nstr(dev(word(rel,A,B),I3),3)}")
def fox_h1(A, B, label):
    n = A.rows; I = mp.eye(n)
    D = {'a': A, 'b': B, 'A': A**-1, 'B': B**-1}
    val = I; d = {'a': mp.zeros(n,n), 'b': mp.zeros(n,n)}
    for ch in rel:
        g = ch.lower(); X = D[ch]
        if ch.islower(): d[g] = d[g] + val
        else: d[g] = d[g] - val*X
        val = val*X
    d0 = mp.zeros(2*n, n); d1 = mp.zeros(n, 2*n)
    for i in range(n):
        for j in range(n):
            d0[i,j] = (A-I)[i,j]; d0[n+i,j] = (B-I)[i,j]; d1[i,j] = d['a'][i,j]; d1[i,n+j] = d['b'][i,j]
    def rank(Mx):
        H = Mx.H*Mx; ev = [mp.re(e) for e in mp.eig(H)[0]]; mx = max(abs(e) for e in ev) or 1
        return sum(1 for e in ev if abs(e) > mp.mpf(10)**-60 * mx)
    r0, r1 = rank(d0), rank(d1); print(f"{label:12s} dim {n}: rho(rel) dev {mp.nstr(dev(val,I),3)}  h0={n-r0}  h1={(2*n-r1)-r0}")
    return (2*n-r1)-r0
# choose the assignment that satisfies the relator
best = min({"a->K,b->L":(K,L), "a->L,b->K":(L,K), "a->K^-1,b->L":(K**-1,L), "a->K,b->L^-1":(K,L**-1)}.items(), key=lambda kv: dev(word(rel,*kv[1]),I3))
print("using", best[0]); A, B = best[1]
fox_h1(mp.eye(1)*1, mp.eye(1)*1, "trivial")
fox_h1(A, B, "3"); fox_h1((A**-1).T, (B**-1).T, "3bar (dual)")
# adjoint on gl_3 (9-dim; contains the trivial once): X -> A X A^-1, in the basis E_ij
def ad(A):
    Ai = A**-1; M = mp.zeros(9,9)
    for c in range(9):
        E = mp.zeros(3,3); E[c//3, c%3] = 1; Y = A*E*Ai
        for r in range(9): M[r,c] = Y[r//3, r%3]
    return M
h_gl3 = fox_h1(ad(A), ad(B), "gl_3 = sl_3+1"); print("=> h1(sl_3) = h1(gl_3) - h1(trivial) =", h_gl3 - 1)
