"""
B775 Phase-2 Wave-3  cell P2W3-L56 -- the triple-phase reality proof  tr(P_i Q_j R_k).

OI-095 residual (from B355 / the L56 quantum layer): the gauge-invariant triple-phase
class  B_{ijk} = tr(P_i Q_j R_k)  over the eigenprojector families of the three metallic
monodromies rho(A_1), rho(A_2), rho(A_3) in the level-15 Weil representation was found
605/605 numerically REAL.  This cell PROVES the reality (symbolic / structural), and
certifies it by exact modular arithmetic, or would exhibit a non-real triple.

------------------------------------------------------------------------------------------
SETUP (rebuilt independently, conventions from B355 weil_layer.py, earned family d=-2c):
    (T f)(x) = e_N(c x^2) f(x),   (S f)(x) = g(N)^{-1} sum_y e_N(-2 c x y) f(y),  N=15,c=1
    A_m = R^m L^m,  rho(A_m) = T^m S T^{-m} S^{-1};  A_m = [[1+m^2,m],[m,1]] in SL(2,Z).
Eigenprojectors are computed GAUGE-FREE by the group-algebra (spectral) formula
    P_m^{(w)} = (1/n_m) sum_{t=0}^{n_m-1} w^{-t} rho(A_m)^t ,   n_m = ord rho(A_m),
one per distinct eigenvalue w (a root of unity).  No eigenvectors (gauge) are ever used;
no ill-conditioned eig call enters the exact tier.   (orders: n_1=20, n_2=12, n_3=6.)

------------------------------------------------------------------------------------------
THE STRUCTURAL PROOF (two exact operator-level relations, then reality in one line):

 (S) S-relation.  In SL(2,Z):  S A_m S^{-1} = A_m^{-1}  (exact integer identity, all m).
     Hence  S rho(A_m) S^{-1} = rho(A_m)^{-1}, so  S P_m^{(w)} S^{-1} = P_m^{(wbar)}
     (conjugate eigenvalue).  Trace-cycling S out:
        B_{w,u,v} = tr(P_1^w P_2^u P_3^v) = B_{wbar,ubar,vbar}.                     (*)

 (J) Antiunitary relation.  Complex conjugation K satisfies conj(T)=T^{-1}, conj(S)=S^{-1}
     (B355), hence  K rho(A_m) K = rho(A_{-m})  since A_{-m}=D A_m D^{-1}, D=diag(1,-1).
     The restricted rep is self-conjugate: there is a UNITARY U with U rho(A_m) U^H
     = rho(A_{-m}) for m=1,2,3  (exhibited; existence is forced -- see lemma below).
     Then  J := U^H K  is ANTIUNITARY and  J rho(A_m) J^{-1} = rho(A_m)  for all three,
     so  J P_m^{(w)} J^{-1} = P_m^{(wbar)}, and for antiunitary J, tr(J M J^{-1}) = conj(tr M):
        conj(B_{w,u,v}) = tr(J P_1^w P_2^u P_3^v J^{-1}) = B_{wbar,ubar,vbar}.        (**)

 Combine (*) and (**):   conj(B_{w,u,v}) = B_{wbar,ubar,vbar} = B_{w,u,v}.   REAL.  QED.

 LEMMA (unitary intertwiner exists).  Hom_H(rho, conj rho) != 0 (dim 4 here), and for ANY
 invertible intertwiner W0 the positive operator P=W0^H W0 commutes with rho(A_m)
 (from W0 A_m = A_{-m} W0 and unitarity of rho(A_m)); hence U := W0 P^{-1/2} is a UNITARY
 intertwiner.  Equivalently, rho|_H is self-conjugate because its character is real on H
 (tr rho(A_1)=1, tr rho(A_2)=1, tr rho(A_3)=3 -- all real; certified on <A_1,A_2,A_3>).

------------------------------------------------------------------------------------------
CERTIFICATION TIERS
  T1  EXACT modular.  Over F_p, p = 1 mod 60 (so zeta_60 in F_p), build the whole layer with
      NO floating point; test B(zeta->w) == B(zeta->w^{-1}) for every triple (this is exactly
      "B - conj(B) = 0" reduced mod p).  Run several primes + a second convention c=2.
  T2  Numerical reproduction (2 precisions): float64 (all 605) and mpmath dps=48 (sample),
      GA projectors, worst |Im|.  Conditioning reported as projector idempotency residual.
  T3  Mechanism checks: the two exact SL2 identities; S-relation (*); the unitary intertwiner
      U; J antiunitary commuting; relation (**).
Verdict logic at the bottom can emit RESOLVED-A / RESOLVED-B / UNRESOLVED.
"""
import json, cmath, math
import numpy as np

N = 15
SEEDS = (1, 2, 3)

# ============================ EXACT MODULAR TIER (F_p, p = 1 mod 60) ======================
def modinv(a, p): return pow(a % p, -1, p)

def mat_mul(A, B, p):
    return [[sum(A[i][k]*B[k][j] for k in range(N)) % p for j in range(N)] for i in range(N)]

def mat_pow(A, e, p):
    R = [[1 if i==j else 0 for j in range(N)] for i in range(N)]
    B = [row[:] for row in A]
    while e:
        if e & 1: R = mat_mul(R, B, p)
        B = mat_mul(B, B, p); e >>= 1
    return R

def mat_inv(A, p):
    M = [row[:] + [1 if i==j else 0 for j in range(N)] for i, row in enumerate(A)]
    for col in range(N):
        piv = next(r for r in range(col, N) if M[r][col] % p)
        M[col], M[piv] = M[piv], M[col]
        inv = modinv(M[col][col], p)
        M[col] = [(x*inv) % p for x in M[col]]
        for r in range(N):
            if r != col and M[r][col] % p:
                f = M[r][col] % p
                M[r] = [(M[r][k] - f*M[col][k]) % p for k in range(2*N)]
    return [row[N:] for row in M]

def is_ident(A, p):
    return all((A[i][j] % p) == (1 if i==j else 0) for i in range(N) for j in range(N))

def order_of(A, p, mx=120):
    R = [row[:] for row in A]
    for k in range(1, mx+1):
        if is_ident(R, p): return k
        R = mat_mul(R, A, p)
    return None

def prim_root_of_order(p, order):
    # find element of exact multiplicative order `order` in F_p^*
    for g in range(2, p):
        # g^((p-1)/order) has order dividing order; check exact
        w = pow(g, (p-1)//order, p)
        seen = w; k = 1
        while seen != 1 and k <= order:
            seen = (seen*w) % p; k += 1
        if k == order:
            return w
    raise RuntimeError("no primitive root")

def build_weil_mod(p, w, c=1):
    """T,S over F_p using zeta_60 = w (order 60). e_15(t)=w^{4t}."""
    def e15(t): return pow(w, (4*(t % 15)) % 60, p)
    T = [[0]*N for _ in range(N)]
    F = [[0]*N for _ in range(N)]
    for x in range(N):
        T[x][x] = e15(c*x*x)
        for y in range(N):
            F[x][y] = e15(-2*c*x*y)
    g = sum(e15(c*x*x) for x in range(N)) % p
    gi = modinv(g, p)
    S = [[(F[x][y]*gi) % p for y in range(N)] for x in range(N)]
    return T, S

def rho_Am_mod(m, T, S, p):
    Ti = mat_inv(T, p); Si = mat_inv(S, p)
    return mat_mul(mat_mul(mat_pow(T, m, p), S, p),
                   mat_mul(mat_pow(Ti, m, p), Si, p), p)

def ga_projectors_mod(A, n, p, w):
    """P^{(k)} for k=0..n-1 ; return only NONZERO ones keyed by k. zeta_n = w^{60/n}."""
    step = 60 // n
    ninv = modinv(n, p)
    powsA = [None]*n
    powsA[0] = [[1 if i==j else 0 for j in range(N)] for i in range(N)]
    for t in range(1, n):
        powsA[t] = mat_mul(powsA[t-1], A, p)
    out = {}
    for k in range(n):
        P = [[0]*N for _ in range(N)]
        for t in range(n):
            coef = pow(w, (-step*k*t) % 60, p)
            for i in range(N):
                Pi = P[i]; At = powsA[t][i]
                for j in range(N):
                    Pi[j] = (Pi[j] + coef*At[j]) % p
        P = [[(x*ninv) % p for x in row] for row in P]
        if any(x % p for row in P for x in row):
            out[k] = P
    return out

def tr_prod3(P, Q, R, p):
    # tr(P Q R) = sum_{i,j,k} P[i][j] Q[j][k] R[k][i]  mod p
    QR = mat_mul(Q, R, p)
    return sum(P[i][j]*QR[j][i] for i in range(N) for j in range(N)) % p

def modular_reality(p, c=1):
    w = prim_root_of_order(p, 60)
    wi = modinv(w, p)  # zeta -> zeta^{-1}
    res = {}
    for tag, root in (('w', w), ('wi', wi)):
        T, S = build_weil_mod(p, root, c)
        proj = {}
        orders = {}
        for m in SEEDS:
            A = rho_Am_mod(m, T, S, p)
            n = order_of(A, p)
            orders[m] = n
            proj[m] = ga_projectors_mod(A, n, p, root)
        res[tag] = (proj, orders)
    projw, orders = res['w']; projwi, _ = res['wi']
    keys1 = sorted(projw[1]); keys2 = sorted(projw[2]); keys3 = sorted(projw[3])
    total = 0; mism = 0
    for a in keys1:
        for b in keys2:
            for d in keys3:
                total += 1
                Bw  = tr_prod3(projw[1][a],  projw[2][b],  projw[3][d],  p)
                Bwi = tr_prod3(projwi[1][a], projwi[2][b], projwi[3][d], p)
                if Bw != Bwi:      # B(zeta) != B(zeta^{-1})  ==  B not fixed by conjugation
                    mism += 1
    return dict(p=p, c=c, orders=orders,
                nproj=[len(keys1), len(keys2), len(keys3)],
                triples=total, nonreal=mism)

# ============================ NUMERICAL TIER (float64 + mpmath) ==========================
def npweil(c=1):
    T = np.zeros((N, N), complex); F = np.zeros((N, N), complex)
    for x in range(N):
        T[x, x] = cmath.exp(2j*cmath.pi*((c*x*x) % 15)/15)
        for y in range(N):
            F[x, y] = cmath.exp(2j*cmath.pi*((-2*c*x*y) % 15)/15)
    g = sum(cmath.exp(2j*cmath.pi*((c*x*x) % 15)/15) for x in range(N))
    return T, F/g

def npAop(T, S, m):
    Ti = np.linalg.inv(T); Si = np.linalg.inv(S)
    if m >= 0:
        return np.linalg.matrix_power(T, m) @ S @ np.linalg.matrix_power(Ti, m) @ Si
    return np.linalg.matrix_power(Ti, -m) @ S @ np.linalg.matrix_power(T, -m) @ Si

def np_order(U, mx=100):
    P = np.eye(N, dtype=complex)
    for k in range(1, mx+1):
        P = P @ U
        if np.linalg.norm(P - np.eye(N)) < 1e-8: return k

def np_ga_projs(U, n):
    ev = np.linalg.eigvals(U); dist = []
    for e in ev:
        if not any(abs(e-d) < 1e-7 for d in dist): dist.append(e)
    out = {}; worstP = 0.0
    for om in dist:
        P = np.zeros((N, N), complex); Ut = np.eye(N, dtype=complex)
        for t in range(n):
            P += (om**-t)*Ut; Ut = Ut @ U
        P /= n
        worstP = max(worstP, np.linalg.norm(P@P - P))     # idempotency = conditioning proxy
        out[round(cmath.phase(om)/(2*cmath.pi)*n) % n] = P
    return out, worstP

def numerical_float(c=1):
    T, S = npweil(c)
    Us = {m: npAop(T, S, m) for m in SEEDS}
    pj = {}; worstP = 0.0
    for m in SEEDS:
        p, wp = np_ga_projs(Us[m], np_order(Us[m])); pj[m] = p; worstP = max(worstP, wp)
    worstIm = 0.0; total = 0; nonreal = 0
    vals = []
    for a in pj[1]:
        for b in pj[2]:
            for d in pj[3]:
                B = np.trace(pj[1][a] @ pj[2][b] @ pj[3][d]); total += 1
                worstIm = max(worstIm, abs(B.imag)); vals.append(B)
                if abs(B.imag) > 1e-7: nonreal += 1
    return dict(c=c, triples=total, nonreal=nonreal, worst_im=worstIm,
                worst_idempotency=worstP), pj, Us

def numerical_mpmath(sample=40, dps=48):
    import mpmath as mp
    mp.mp.dps = dps
    def e(t): return mp.e**(2j*mp.pi*(t % 15)/15)
    T = mp.zeros(N); F = mp.zeros(N)
    for x in range(N):
        T[x, x] = e(x*x)
        for y in range(N):
            F[x, y] = e(-2*x*y)
    g = sum(e(x*x) for x in range(N)); S = F/g
    Ti = T**-1; Si = S**-1
    def A(m): return (T**m)*(S*(T**-m)*Si)
    def order(U):
        R = mp.eye(N)
        for k in range(1, 100):
            R = R*U
            if mp.norm(R-mp.eye(N)) < mp.mpf(10)**-20: return k
    def projs(U, n):
        E, _ = mp.eig(U); dist = []
        for ev in E:
            if not any(abs(ev-d) < mp.mpf(10)**-15 for d in dist): dist.append(ev)
        out = []
        for om in dist:
            P = mp.zeros(N); Ut = mp.eye(N)
            for t in range(n):
                P += (om**-t)*Ut; Ut = Ut*U
            out.append(P/n)
        return out
    pj = [projs(A(m), order(A(m))) for m in SEEDS]
    import random
    rng = random.Random(20260724)
    idx = [(i, j, k) for i in range(len(pj[0])) for j in range(len(pj[1])) for k in range(len(pj[2]))]
    picks = rng.sample(idx, min(sample, len(idx)))
    worst = mp.mpf(0)
    for (i, j, k) in picks:
        v = sum((pj[0][i]*pj[1][j]*pj[2][k])[d, d] for d in range(N))
        worst = max(worst, abs(mp.im(v)))
    return dict(dps=dps, sampled=len(picks), worst_im=float(worst))

# ============================ MECHANISM TIER ============================================
def sl2_identities():
    def M(a, b, c, d): return np.array([[a, b], [c, d]], dtype=object)
    S = M(0, -1, 1, 0); Si = M(0, 1, -1, 0); D = M(1, 0, 0, -1)
    ok_S = ok_D = ok_inv = True
    for m in range(1, 6):
        Am = M(1+m*m, m, m, 1); Ami = M(1, -m, -m, 1+m*m); Amm = M(1+m*m, -m, -m, 1)
        ok_S &= np.array_equal(S@Am@Si, Ami)
        ok_D &= np.array_equal(D@Am@D, Amm)
        ok_inv &= np.array_equal(Am@Ami, np.eye(2, dtype=object))
    return dict(S_inverts_Am=bool(ok_S), D_gives_A_negm=bool(ok_D), inverse_ok=bool(ok_inv))

def mechanism(pj, Us):
    from scipy.linalg import sqrtm
    T, S = npweil(1); Ti = np.linalg.inv(T); Si = np.linalg.inv(S)
    Am = {m: Us[m] for m in SEEDS}; Amm = {m: npAop(T, S, -m) for m in SEEDS}
    # conj(T)=T^-1, conj(S)=S^-1
    conj_ok = (np.linalg.norm(np.conj(T)-np.linalg.inv(T)) < 1e-9 and
               np.linalg.norm(np.conj(S)-np.linalg.inv(S)) < 1e-9)
    # K rho(A_m) K = rho(A_-m)
    Krel = max(np.linalg.norm(np.conj(Am[m]) - Amm[m]) for m in SEEDS)
    # S rho(A_m) S^-1 = rho(A_m)^-1
    Srel = max(np.linalg.norm(S@Am[m]@Si - np.linalg.inv(Am[m])) for m in SEEDS)
    # unitary intertwiner U: solve W A_m = A_-m W, take invertible combo, polar-decompose
    I = np.eye(N)
    rows = [np.kron(Am[m].T, I) - np.kron(I, Amm[m]) for m in SEEDS]
    _, s, vh = np.linalg.svd(np.vstack(rows))
    nulldim = int(np.sum(s < 1e-8))
    nulls = [vh[-1-k].conj() for k in range(nulldim)]
    rng = np.random.default_rng(7)
    W0 = None
    for _ in range(50):
        coef = rng.standard_normal(nulldim) + 1j*rng.standard_normal(nulldim)
        cand = sum(cc*nu for cc, nu in zip(coef, nulls)).reshape(N, N)
        if abs(np.linalg.det(cand)) > 1e-2:
            W0 = cand; break
    P = W0.conj().T @ W0
    U = W0 @ np.linalg.inv(sqrtm(P))
    U_unitary = np.linalg.norm(U.conj().T @ U - I)
    U_intertw = max(np.linalg.norm(U@Am[m]@U.conj().T - Amm[m]) for m in SEEDS)
    # J = U^H K antiunitary:  J M J^-1 = U^H conj(M) U ; commutes with A_m
    J_comm = max(np.linalg.norm(U.conj().T @ np.conj(Am[m]) @ U - Am[m]) for m in SEEDS)
    # antiunitary trace identity tr(J M J^-1)=conj(tr M) on a random M
    Mr = rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N))
    JtrM = np.trace(U.conj().T @ np.conj(Mr) @ U)
    anti_trace = abs(JtrM - np.conj(np.trace(Mr)))
    # relation (*) S:  B_{w,u,v} == B_{wbar,ubar,vbar}
    def cbar(key, n): return (-key) % n
    n1, n2, n3 = 20, 12, 6
    Srel_B = 0.0; Crel_B = 0.0
    k1 = list(pj[1]); k2 = list(pj[2]); k3 = list(pj[3])
    for a in k1:
        for b in k2:
            for d in k3:
                B = np.trace(pj[1][a]@pj[2][b]@pj[3][d])
                Bbar = np.trace(pj[1][cbar(a, n1)]@pj[2][cbar(b, n2)]@pj[3][cbar(d, n3)])
                Srel_B = max(Srel_B, abs(B - Bbar))                # (*)
                Crel_B = max(Crel_B, abs(np.conj(B) - Bbar))       # (**)
    return dict(conj_TS_ok=bool(conj_ok), K_rel=float(Krel), S_rel_op=float(Srel),
                intertwiner_nulldim=nulldim, U_unitary=float(U_unitary),
                U_intertwines=float(U_intertw), J_commutes=float(J_comm),
                antiunitary_trace_id=float(anti_trace),
                S_relation_B=float(Srel_B), C_relation_B=float(Crel_B))

# ============================ DRIVER + VERDICT ==========================================
def main():
    out = {"cell": "P2W3-L56", "observable": "B_ijk = tr(P_i Q_j R_k), level-15 Weil rep"}

    # T1 exact modular
    primes = [61, 181, 241]
    mod = [modular_reality(p, c=1) for p in primes]
    mod_c2 = modular_reality(241, c=2)   # second convention, robustness
    out["T1_exact_modular"] = {"primes_c1": mod, "convention_c2": mod_c2}
    exact_total = mod[0]["triples"]
    exact_nonreal = sum(r["nonreal"] for r in mod) + mod_c2["nonreal"]

    # T2 numerical
    nf, pj, Us = numerical_float(1)
    nf2, _, _ = numerical_float(2)
    nm = numerical_mpmath()
    out["T2_numerical"] = {"float_c1": nf, "float_c2": nf2, "mpmath": nm}

    # T3 mechanism
    out["T3_sl2_identities"] = sl2_identities()
    out["T3_mechanism"] = mechanism(pj, Us)

    # ---- verdict logic ----
    tol = 1e-6
    m = out["T3_mechanism"]; ids = out["T3_sl2_identities"]
    exact_ok   = (exact_nonreal == 0 and exact_total == 605)
    numeric_ok = (nf["nonreal"] == 0 and nf["worst_im"] < 1e-7 and
                  nf2["nonreal"] == 0 and nm["worst_im"] < 1e-30)
    mech_ok = (ids["S_inverts_Am"] and ids["D_gives_A_negm"] and m["conj_TS_ok"] and
               m["K_rel"] < tol and m["S_rel_op"] < tol and m["U_unitary"] < tol and
               m["U_intertwines"] < tol and m["J_commutes"] < tol and
               m["antiunitary_trace_id"] < tol and m["S_relation_B"] < tol and
               m["C_relation_B"] < tol)

    if exact_nonreal > 0 or nf["nonreal"] > 0 or nf2["nonreal"] > 0:
        verdict = "RESOLVED-B"      # a non-real triple exists
        headline = "A non-real triple B_ijk was found -- reality REFUTED."
    elif exact_ok and numeric_ok and mech_ok:
        verdict = "RESOLVED-A"
        headline = ("Reality THEOREM: all triple-phases tr(P_i Q_j R_k) are real. Proof = "
                    "S-relation (S inverts each metallic word) + antiunitary J=U^H K "
                    "(self-conjugacy of the restricted Weil rep); exact modular certificate "
                    "605/605 over 3 primes + convention c=2.")
    else:
        verdict = "UNRESOLVED"
        headline = "Reality holds numerically but a structural/exact leg failed to certify."

    out["verdict"] = verdict
    out["headline"] = headline
    out["exact_summary"] = {"triples": exact_total, "nonreal_total_over_primes_and_c2": exact_nonreal}
    out["gates"] = {"exact_ok": exact_ok, "numeric_ok": numeric_ok, "mechanism_ok": mech_ok}

    with open("results.json", "w") as f:
        json.dump(out, f, indent=2, default=str)

    # compact console
    print("== T1 EXACT MODULAR (F_p, p=1 mod 60; no floating point) ==")
    for r in mod:
        print(f"   p={r['p']:4d} c=1  orders={r['orders']} nproj={r['nproj']} "
              f"triples={r['triples']} nonreal={r['nonreal']}")
    print(f"   p=241 c=2  orders={mod_c2['orders']} nproj={mod_c2['nproj']} "
          f"triples={mod_c2['triples']} nonreal={mod_c2['nonreal']}")
    print(f"   EXACT total={exact_total}  nonreal_across_all={exact_nonreal}")
    print("== T2 NUMERICAL ==")
    print(f"   float c=1: triples={nf['triples']} nonreal={nf['nonreal']} "
          f"worst|Im|={nf['worst_im']:.2e} idempotency={nf['worst_idempotency']:.1e}")
    print(f"   float c=2: nonreal={nf2['nonreal']} worst|Im|={nf2['worst_im']:.2e}")
    print(f"   mpmath dps={nm['dps']} sample={nm['sampled']} worst|Im|={nm['worst_im']:.2e}")
    print("== T3 MECHANISM ==")
    print(f"   SL2:  S A_m S^-1=A_m^-1:{ids['S_inverts_Am']}  D A_m D^-1=A_-m:{ids['D_gives_A_negm']}")
    print(f"   conj(T)=T^-1,conj(S)=S^-1:{m['conj_TS_ok']}  K:rho(A_m)->rho(A_-m) res={m['K_rel']:.1e}")
    print(f"   S-rel operator res={m['S_rel_op']:.1e}  intertwiner nulldim={m['intertwiner_nulldim']}")
    print(f"   U unitary={m['U_unitary']:.1e}  U intertwines={m['U_intertwines']:.1e}  "
          f"J commutes={m['J_commutes']:.1e}  anti-trace-id={m['antiunitary_trace_id']:.1e}")
    print(f"   (*) B=B_bar res={m['S_relation_B']:.1e}   (**) conjB=B_bar res={m['C_relation_B']:.1e}")
    print("== VERDICT ==")
    print(f"   {verdict}: {headline}")

if __name__ == "__main__":
    main()
