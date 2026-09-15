"""h^1(m004; 27) under the PRINCIPAL sl2 -> E6 (27 = Sym^16 + Sym^8 + 1), by Fox calculus on SnapPy's presentation,
at 60 digits (ManifoldHP). Control: h^1(Sym^2) = 1 (the cusp deformation), h^1(Sym^1) = 0 with a spin lift, h^1(trivial) = 1."""
import snappy, mpmath as mp
from math import comb
mp.mp.dps = 160
M = snappy.Manifold("m004"); import snappy.snap.polished_reps as PR; G = PR.polished_holonomy(M, bits_prec=500, lift_to_SL2=False)
gens = G.generators(); rel = G.relators()[0]; print("presentation:", gens, rel)
def mat2(X): return mp.matrix([[mp.mpc(str(X[i,j].real()).replace(" ",""), str(X[i,j].imag()).replace(" ","")) for j in range(2)] for i in range(2)])
A = mat2(G('a')); B = mat2(G('b'))
def symk(X, k):
    # action on homogeneous polynomials of degree k in (x,y): basis x^(k-i) y^i
    a,b,c,d = X[0,0],X[0,1],X[1,0],X[1,1]
    S = mp.zeros(k+1,k+1)
    for i in range(k+1):          # image of x^(k-i) y^i = (a x + c y)^(k-i) (b x + d y)^i
        for p in range(k-i+1):
            for q in range(i+1):
                coeff = comb(k-i,p)*comb(i,q) * a**p * c**(k-i-p) * b**q * d**(i-q)
                deg_y = (k-i-p) + (i-q); S[deg_y, i] += coeff   # x^(p+q) y^(k-p-q): row index = power of y
    return S
def blockdiag(*Ms):
    n = sum(m.rows for m in Ms); R = mp.zeros(n,n); o = 0
    for m in Ms:
        for i in range(m.rows):
            for j in range(m.cols): R[o+i,o+j] = m[i,j]
        o += m.rows
    return R
def rep(k_list):
    return {'a': blockdiag(*[symk(A,k) for k in k_list]), 'b': blockdiag(*[symk(B,k) for k in k_list])}
def inv(X): return X**-1
def fox(word, R):
    """returns (rho(word), {g: rho(d word / d g)}) by the product rule, over generators a,b (inverse = uppercase)."""
    n = R['a'].rows; I = mp.eye(n); val = I; D = {'a': mp.zeros(n,n), 'b': mp.zeros(n,n)}
    for ch in word:
        g = ch.lower(); X = R[g] if ch.islower() else inv(R[g])
        if ch.islower(): D[g] = D[g] + val
        else:            D[g] = D[g] - val*X
        val = val*X
    return val, D
def rank(Mx, tol=mp.mpf(10)**-60):
    s = mp.svd_r(mp.matrix([[mp.re(Mx[i,j]) for j in range(Mx.cols)] for i in range(Mx.rows)] + [[mp.im(Mx[i,j]) for j in range(Mx.cols)] for i in range(Mx.rows)]), compute_uv=False) if False else None
    # complex SVD via mpmath: use singular values of the hermitian product
    H = Mx.H * Mx; ev = mp.eigh(H, eigvals_only=True) if hasattr(mp,'eigh') else [mp.re(e) for e in mp.eig(H)[0]]
    mx = max(abs(e) for e in ev); return sum(1 for e in ev if abs(e) > tol*mx)
def h1(k_list, label):
    R = rep(k_list); n = R['a'].rows
    val, D = fox(rel, R)
    dev = max(abs(val[i,j] - (1 if i==j else 0)) for i in range(n) for j in range(n)); devm = max(abs(val[i,j] + (1 if i==j else 0)) for i in range(n) for j in range(n))
    d0 = mp.zeros(2*n, n); I = mp.eye(n)
    for i in range(n):
        for j in range(n): d0[i,j] = (R['a']-I)[i,j]; d0[n+i,j] = (R['b']-I)[i,j]
    d1 = mp.zeros(n, 2*n)
    for i in range(n):
        for j in range(n): d1[i,j] = D['a'][i,j]; d1[i,n+j] = D['b'][i,j]
    r0, r1 = rank(d0), rank(d1)
    h0 = n - r0; hh1 = (2*n - r1) - r0
    print(f"{label:22s} dim {n:2d}  rho(rel)=+I dev {mp.nstr(dev,3)} / -I dev {mp.nstr(devm,3)}  rank d0={r0} rank d1={r1}  h0={h0}  h1={hh1}")
h1([0], "trivial (control)"); h1([2], "Sym^2 (control)"); h1([1], "Sym^1 (spin lift?)"); h1([16,8,0], "27 = Sym16+Sym8+1")
