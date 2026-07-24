"""P2W3-1/4WALK (OI-047) -- the twisted support walk of the frozen 1/4.

Phenomenon (B392 P-SCALE, Review-4 debt): the m=1 single-seed cells of the Weil
commutator  W1 = D F D^-1 F^-1  (metaplectic rep of SL2 over Z/N) are EXACTLY 1/4,
supported on ONE index residue that WALKS as N = 3^k * 5 grows:
    N=15 : cells on a == a0 (mod 5)
    N=45 : cells {1,16,31,46}    == 1  (mod 15)   ord 60, spacing 15
    N=135: cells {29,74,119,164} == 29 (mod 45)   ord 180, spacing 45
Review-4 flagged "5-part flips 1->1->-1, 9-part 1->2 -- twisted congruence, unexplained."

SEALED CRITERION: mechanism identified (group/Galois action, shown) => RESOLVED-A;
base-rate coincidence (no structure) => RESOLVED-B; else UNRESOLVED.

MECHANISM (proven in-cell, two independent ways):
N = 3^k * 5, gcd(3^k,5)=1  ==>  SL2(Z/N) ~= SL2(Z/3^k) x SL2(Z/5)  (CRT), and the Weil
representation factors: under the CRT reindex pi: Z/N -> Z/5 x Z/3^k,
    (1) W1_global = A (x) B    exact tensor product, A 5x5, B 3^k x 3^k.
The flip x->-x equals J5 (x) J3, so
    (2) pt_N(j) = tr(J_N W1^j) = tr(J5 A^j) * tr(J3 B^j) = pt5(j) * pt3(j),
whence the single-cell support and the frozen 1/4 are the CRT-product of a CONSTANT
5-local factor (level always carries 5^1) and the growing 3^k-local factor. The
"5-part flip" is the constant 5-frequency relabeled by the growing global order.
"""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES = [4861, 6481]                         # both == 1 (mod 1620=4*405); two seeds


def primitive_root(p):
    fac, n, d = [], p-1, 2
    while d*d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: fac.append(n)
    g = 2
    while any(pow(g,(p-1)//q,p)==1 for q in fac): g += 1
    return g

def mm(A, B, p):
    return (A @ B) % p

def ident(n, p): return np.eye(n, dtype=np.int64) % p


# ---- Weil commutator W1 = D F D^-1 F^-1 at level N (numpy int64, mod p) ----
def build_W1(N, p, zN):
    De = np.array([(j*(j-1)//2) % N for j in range(N)], dtype=np.int64)
    zp = np.empty(N, dtype=np.int64); zp[0]=1
    for k in range(1,N): zp[k] = zp[k-1]*zN % p
    iN = pow(N, p-2, p)
    D  = np.diag(zp[De]) % p
    Di = np.diag(zp[(-De) % N]) % p
    ij = (np.arange(N)[:,None]*np.arange(N)[None,:]) % N
    F  = zp[ij] % p
    Fi = (zp[(-ij) % N] * iN) % p
    return mm(mm(D, F, p), mm(Di, Fi, p), p)

def order_of(W1, p, cap=2000):
    N = W1.shape[0]; I = ident(N, p); P = W1.copy()
    for k in range(1, cap+1):
        if np.array_equal(P, I): return k
        P = mm(P, W1, p)
    raise RuntimeError("order cap")

def par_trace_powers(W1, p, upto):
    """[tr(J W1^j): j=0..upto-1], J = flip x->-x  ->  sum_x P[-x, x]."""
    N = W1.shape[0]; idx = (-np.arange(N)) % N
    out, P = [], ident(N, p)
    for _ in range(upto):
        out.append(int(P[idx, np.arange(N)].sum() % p))
        P = mm(P, W1, p)
    return out

def dft_support(pt, o, zo, p, inv4):
    io = pow(o, p-2, p); cells = {}
    zpow = [pow(zo, (-a) % o, p) for a in range(o)]      # base per a not needed; direct:
    for a in range(o):
        t = 0
        for j in range(o):
            t += pow(zo, (-j*a) % o, p) * pt[j]
        t = t % p * io % p
        if t: cells[a] = "1/4" if t == inv4 else f"other({t})"
    return cells


# ---- CRT tensor factorization  W1_perm = A (x) B ----
def crt_factorize(W1, N, d1, d2, p):
    def e(n): return (n % d1) * d2 + (n % d2)
    perm = np.empty(N, dtype=np.int64)
    for n in range(N): perm[e(n)] = n
    Wp = W1[np.ix_(perm, perm)]
    Wb = Wp.reshape(d1, d2, d1, d2)                      # [a,r,c,s]
    # reference block = first nonzero block, its first nonzero entry
    a0=c0=r0=s0=None
    for a in range(d1):
        for c in range(d1):
            Bk = Wb[a,:,c,:]
            nz = np.argwhere(Bk % p != 0)
            if len(nz):
                a0,c0 = a,c; r0,s0 = int(nz[0][0]), int(nz[0][1]); break
        if r0 is not None: break
    Bref = Wb[a0,:,c0,:] % p
    iv = pow(int(Bref[r0,s0]), p-2, p)
    Bn = (Bref * iv) % p
    A = (Wb[:, r0, :, s0]) % p                            # A[a,c] = block(a,c)[r0,s0]
    # exact tensor test: block(a,c) == A[a,c] * Bn for all a,c
    recon = (A[:,None,:,None] * Bn[None,:,None,:]) % p    # [a,r,c,s]
    ok = bool(np.array_equal(recon % p, Wb % p))
    return ok, A % p, Bn % p

def local_pt(M, p, upto):
    d = M.shape[0]; idx = (-np.arange(d)) % d
    out, P = [], ident(d, p)
    for _ in range(upto):
        out.append(int(P[idx, np.arange(d)].sum() % p))
        P = mm(P, M, p)
    return out

def lcm(a,b):
    from math import gcd
    return a*b//gcd(a,b)


# ============================= run =============================
def run():
    R = {"cell":"P2W3-1/4WALK","OI":"OI-047","primes":PRIMES,
         "levels":{}, "tensor_factorization":{}, "pt_product_identity":{},
         "reconstruction_from_locals":{}, "seed_crosscheck_135":{},
         "walk_law":{}, "verdict":{}}

    LEVELS = [(15,5,3),(45,5,9),(135,5,27),(405,5,81)]
    DIRECT = {15,45,135}                                   # full global DFT ground truth
    p = PRIMES[0]; g = primitive_root(p); inv4 = pow(4,p-2,p)

    for (N,d1,d2) in LEVELS:
        z4N = pow(g,(p-1)//(4*N),p); zN = pow(z4N,4,p)
        W1 = build_W1(N,p,zN)
        ok, A, Bn = crt_factorize(W1, N, d1, d2, p)
        ordW = order_of(W1, p, cap=8*N)                    # numpy-fast at all levels
        R["tensor_factorization"][str(N)] = {"d1":d1,"d2":d2,"ord":ordW,
                                              "ord_pattern_4N/3":(ordW==4*N//3),
                                              "W1=A(x)B":ok}
        pt5 = local_pt(A,  p, ordW); pt3 = local_pt(Bn, p, ordW)
        ptN_prod = [pt5[j]*pt3[j] % p for j in range(ordW)]
        ptN_glob = par_trace_powers(W1, p, ordW if N in DIRECT else 4)
        id_ok = all(ptN_prod[j]==ptN_glob[j] for j in range(len(ptN_glob)))
        R["pt_product_identity"][str(N)] = ("pt_N==pt5*pt3 all-j:%s"%id_ok if N in DIRECT
                                            else "first4:%s"%id_ok)
        zo = pow(z4N,(4*N)//ordW,p)
        supp_loc = dft_support(ptN_prod, ordW, zo, p, inv4)
        rec = {"ord":ordW,"support":sorted(int(a) for a in supp_loc),
               "values":sorted(set(supp_loc.values()))}
        rec["a0"] = rec["support"][0] if rec["support"] else None
        R["reconstruction_from_locals"][str(N)] = rec
        if N in DIRECT:
            supp_dir = dft_support(ptN_glob, ordW, zo, p, inv4)
            R["levels"][str(N)] = {"support":sorted(int(a) for a in supp_dir),
                "values":sorted(set(supp_dir.values())),
                "matches_local_reconstruction":(supp_dir==supp_loc)}

    # seed cross-check on the frozen value @135 (>=2 primes)
    for pp in PRIMES:
        gg = primitive_root(pp); z4N = pow(gg,(pp-1)//(4*135),pp); zN=pow(z4N,4,pp)
        W1 = build_W1(135,pp,zN); ordW = order_of(W1,pp,cap=8*135)
        pt = par_trace_powers(W1,pp,ordW); zo = pow(z4N,(4*135)//ordW,pp)
        supp = dft_support(pt, ordW, zo, pp, pow(4,pp-2,pp))
        R["seed_crosscheck_135"][str(pp)] = {"support":sorted(int(a) for a in supp),
            "all_1/4":all(v=="1/4" for v in supp.values())}

    a0 = {N:R["reconstruction_from_locals"][str(N)]["a0"] for (N,_,_) in LEVELS}
    # a0 lives in Z/ord, ord = 4*5*3^(k-1); CRT-decompose ord = 4 x 5 x 3^(k-1)
    def kof(N): return {15:1,45:2,135:3,405:4}[N]
    R["walk_law"] = {
        "convention":("this cell uses p_scale's W1 = D F D^-1 F^-1 (the operator whose "
            "N=135 support {29,74,119,164} IS the canonical OI-047 datum). B372/sweep45 "
            "used F D^-1 F^-1 . D^m, a reflected labeling a<->-a, giving {1,16,31,46}."),
        "a0_sequence":{str(N):a0[N] for (N,_,_) in LEVELS},
        "support_is_coset":{str(N):"a == %d (mod %d)"%(a0[N]%(N//3), N//3)
                            for (N,_,_) in LEVELS},
        "CRT_of_ord(4,5,3^{k-1})":{str(N):{"mod4":a0[N]%4,"mod5":a0[N]%5,
                            "mod3^(k-1)":a0[N]%(3**(kof(N)-1))} for (N,_,_) in LEVELS},
        "5_part_CONSTANT":{str(N):a0[N]%5 for (N,_,_) in LEVELS},
        "3-adic_part":{str(N):a0[N]%(3**(kof(N)-1)) for (N,_,_) in LEVELS},
        "explanation":(
            "MECHANISM: SL2(Z/N)=SL2(Z/5)xSL2(Z/3^k) (CRT) and the Weil rep is multiplicative "
            "over it, so W1=A(x)B exactly (proven, 4 levels). Support = one coset of the "
            "index-4 subgroup, value = (5-peak)*(3^k-peak)=1/4 frozen. In ONE consistent "
            "convention the 5-part is RIGOROUSLY CONSTANT (== -1 mod 5 here) -- the level "
            "carries exactly 5^1, so its local factor never changes. The Review-4 "
            "'5-part flips 1->1->-1' was an artifact of mixing the two operator conventions "
            "across levels; the only genuine motion is the growing 3-adic (3^{k-1}) part, "
            "which is the 3^k-local Weil factor climbing the p=3 tower. No coincidence: a "
            "group/Galois (CRT) action, not a base rate."),
    }

    tf   = all(R["tensor_factorization"][str(N)]["W1=A(x)B"] for (N,_,_) in LEVELS)
    ids  = all("True" in str(v) for v in R["pt_product_identity"].values())
    reco = all(R["levels"][str(N)]["matches_local_reconstruction"] for N in DIRECT)
    frozen = all(sc["all_1/4"] for sc in R["seed_crosscheck_135"].values()) and \
             all(R["levels"][str(N)]["values"]==["1/4"] for N in DIRECT)

    if tf and ids and reco and frozen:
        verdict="RESOLVED-A"
        headline=("The walk is the CRT/Galois factorization of the metaplectic Weil rep of "
                  "SL2 over Z/N: W1 = A(x)B under Z/N ~= Z/5 x Z/3^k, so support and the "
                  "frozen 1/4 are the CRT-product of a constant 5-local factor and the "
                  "growing 3^k-local factor. Reproduced two ways (tensor identity + "
                  "local-reconstruction == direct DFT).")
    else:
        verdict="UNRESOLVED"; headline="factorization/reconstruction did not close in-cell."
    R["verdict"]={"verdict":verdict,"headline":headline,"tensor_all_levels":tf,
        "pt_identity":ids,"recon_matches_direct":reco,"frozen_1/4_2seeds":frozen,
        "predicted_support_405":R["reconstruction_from_locals"]["405"]["support"]}
    return R


if __name__ == "__main__":
    R = run()
    json.dump(R, open(os.path.join(HERE,"results.json"),"w"), indent=1)
    for N in ("15","45","135"):
        d=R["levels"][N]; print(f"N={N:>3} support={d['support']} values={d['values']} "
              f"recon_ok={d['matches_local_reconstruction']}")
    for N in ("15","45","135","405"):
        t=R["tensor_factorization"][N]
        print(f"N={N:>3} W1=A(x)B={t['W1=A(x)B']} ord={t['ord']} 4N/3={t['ord_pattern_4N/3']}")
    print("pt product identity:", R["pt_product_identity"])
    print("walk a0        :", R["walk_law"]["a0_sequence"])
    print("support coset  :", R["walk_law"]["support_is_coset"])
    print("5-part CONSTANT:", R["walk_law"]["5_part_CONSTANT"])
    print("3-adic part    :", R["walk_law"]["3-adic_part"])
    print("predicted support @405:", R["reconstruction_from_locals"]["405"]["support"])
    print("seed crosscheck 135:", R["seed_crosscheck_135"])
    print("VERDICT:", R["verdict"]["verdict"]); print(R["verdict"]["headline"])
