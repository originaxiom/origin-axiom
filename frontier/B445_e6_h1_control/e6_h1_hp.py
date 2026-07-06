#!/usr/bin/env python3
"""Correct Computation B at HIGH PRECISION (mpmath, 60 digits).

Ad_E6 = sum of Sym^{2m}, m in E6 exponents {1,4,5,7,8,11}; H^1 decouples.
dim H^1(pi_1, ad E6) = sum_m dim H^1(pi_1, Sym^{2m} rho_geo).
Menal-Ferrer-Porti: each block should give exactly 1 (one cusp) -> total 6 = rank E6.
We VERIFY this at high precision for BOTH 4_1 and 5_2 (the control).
"""
import mpmath as mp
import snappy

mp.mp.dps = 60
EXPS = [1, 4, 5, 7, 8, 11]

def get_hp(name):
    M = snappy.ManifoldHP(name)
    G = M.fundamental_group()
    gens = G.generators()
    rel = G.relators()[0]
    mats = {}
    def cl(x):  # snappy HP prints "1.234 e-64" with a stray space
        return str(x).replace(' ', '')
    for g in gens:
        A = G.SL2C(g)
        mats[g] = mp.matrix([[mp.mpc(cl(A[i,j].real()), cl(A[i,j].imag())) for j in range(2)]
                             for i in range(2)])
    return gens, rel, mats

def minv2(M):  # inverse of 2x2 (det=1)
    return mp.matrix([[M[1,1], -M[0,1]], [-M[1,0], M[0,0]]])

def sym_power(M, n):
    """Sym^n of 2x2 -> (n+1)x(n+1). Column k = (a x+c y)^{n-k}(b x+d y)^k."""
    a, b, c, d = M[0,0], M[0,1], M[1,0], M[1,1]
    def poly_pow(p, q, e):        # (p x + q y)^e as list of coeffs [x^e..y^e]
        out = [mp.mpc(0)]*(e+1)
        for i in range(e+1):
            out[i] = mp.binomial(e, i) * p**(e-i) * q**i
        return out
    def conv(u, v):
        r = [mp.mpc(0)]*(len(u)+len(v)-1)
        for i,ui in enumerate(u):
            for j,vj in enumerate(v):
                r[i+j] += ui*vj
        return r
    dim = n+1
    out = mp.zeros(dim, dim)
    for k in range(dim):
        col = conv(poly_pow(a, c, n-k), poly_pow(b, d, k))
        for i in range(dim):
            out[i,k] = col[i]
    return out

def rank_and_gap(A):
    if A.rows == 0 or A.cols == 0:
        return 0, mp.inf
    S = mp.svd_c(A, compute_uv=False)
    s = sorted([abs(x) for x in S], reverse=True)
    smax = s[0]
    thr = mp.mpf(10)**(-30) * max(smax, mp.mpf(1))
    r = sum(1 for x in s if x > thr)
    gap = (s[r-1]/s[r]) if 0 < r < len(s) else mp.inf
    return r, gap

def H1_block(gens_mats, relator, n):
    reps = {g: sym_power(gens_mats[g], n) for g in gens_mats}
    ireps = {g: None for g in gens_mats}
    for g in gens_mats:
        ireps[g] = mp.inverse(reps[g])
    dim = n+1
    I = mp.eye(dim)
    Ca = mp.zeros(dim, dim); Cb = mp.zeros(dim, dim)
    pref = mp.eye(dim)
    for letter in relator:
        g = letter.lower()
        Rg = ireps[g] if letter.isupper() else reps[g]
        coeff = (-(pref*ireps[g])) if letter.isupper() else (pref+mp.zeros(dim,dim))
        if g == 'a': Ca = Ca + coeff
        else:        Cb = Cb + coeff
        pref = pref*Rg
    # stack [Ca | Cb] as dim x 2dim
    R = mp.zeros(dim, 2*dim)
    for i in range(dim):
        for j in range(dim):
            R[i,j] = Ca[i,j]; R[i,j+dim] = Cb[i,j]
    rR, gapR = rank_and_gap(R)
    Z1 = 2*dim - rR
    # coboundary stack (rho(a)-I ; rho(b)-I) : 2dim x dim
    stk = mp.zeros(2*dim, dim)
    for i in range(dim):
        for j in range(dim):
            stk[i,j] = reps['a'][i,j] - I[i,j]
            stk[i+dim,j] = reps['b'][i,j] - I[i,j]
    rC, gapC = rank_and_gap(stk)
    B1 = rC; H0 = dim - rC
    return dict(n=n, dim=dim, H0=H0, Z1=Z1, B1=B1, H1=Z1-B1, gapR=gapR)

for name in ['4_1', '5_2']:
    gens, relator, mats = get_hp(name)
    print("="*66)
    print(f"KNOT {name}   pi_1 = <{','.join(gens)} | {relator}>   [mpmath dps=60]")
    total = 0
    for m in EXPS:
        r = H1_block(mats, relator, 2*m)
        total += r['H1']
        g = r['gapR']
        gs = "inf" if g==mp.inf else mp.nstr(g,2)
        print(f"   m={m:2d} Sym^{2*m:<2d}(dim {r['dim']:2d})  H0={r['H0']}  Z1={r['Z1']:2d} B1={r['B1']:2d}"
              f"  ->  H1={r['H1']}   (gap {gs})")
    print(f"   TOTAL adjoint H^1(pi_1, ad E6) = {total}   (rank E6 = 6)")
    print()
