"""How many free coefficients does the ruled-branch modular-flavour ansatz have?
Yukawa forms: L^T Y R H with L, R in T (or R in Tbar), H a singlet.
 Y in M_k(rhobar (x) rhobar) [both in T], k odd;   Y in M_k(rhobar (x) rho) [R in Tbar], k even.
rhobar = chi_eta^3 (x) rhobar_u, so rhobar(x)rhobar = chi_eta^6 (x) (rhobar_u (x) rhobar_u):
  f in M_k  <=>  F = eta^18 f in M_{k+9}(Rbar) with ord_q F >= 3/4 in every component.
rhobar(x)rho = rhobar_u (x) rho_u: F = f, polynomial components of degree k.
Components are polynomials in X=theta2^2, Y=theta3^2, Z=theta4^2 modulo Y^2 = X^2 + Z^2."""
import numpy as np, itertools, cmath
from numpy.linalg import svd

I3 = np.eye(3, dtype=complex)
P24 = np.array([[0,0,1],[0,1,0],[1,0,0]], dtype=complex)
P34 = np.array([[1,0,0],[0,0,1],[0,1,0]], dtype=complex)
rho_u_t = np.diag([1j, 1, 1]) @ P34
rho_u_s = -1j * P24

def monomials(K):
    return [(a, b, K - a - b) for b in (0, 1) for a in range(K - b + 1)]

def mono_index(K):
    return {m: i for i, m in enumerate(monomials(K))}

def reduce_mono(a, b, c):
    """X^a Y^b Z^c with b>=2 -> expand (X^2+Z^2)^(b//2) Y^(b%2); returns dict mono->coeff"""
    out = {}
    m, r = divmod(b, 2)
    for j in range(m + 1):
        coeff = cmath.comb(m, j) if hasattr(cmath, 'comb') else None
    from math import comb
    for j in range(m + 1):
        out[(a + 2*j, r, c + 2*(m - j))] = out.get((a + 2*j, r, c + 2*(m - j)), 0) + comb(m, j)
    return out

def act_T_mono(a, b, c):
    # X -> iX, Y -> Z, Z -> Y:  X^a Y^b Z^c -> i^a X^a Z^b Y^c = i^a X^a Y^c Z^b
    return {m: (1j)**a * v for m, v in reduce_mono(a, c, b).items()}

def act_S_mono(a, b, c, K):
    # X -> Z, Z -> X, with factor (-i)^K:  X^a Y^b Z^c -> (-i)^K X^c Y^b Z^a
    return {m: (-1j)**K * v for m, v in reduce_mono(c, b, a).items()}

def form_space(R_t, R_s, K):
    """Return a basis (as coefficient vectors) of {F=(F_1..F_d): F(tau+1)=R_t F, F(-1/tau)=R_s tau^K F}."""
    d = R_t.shape[0]
    monos = monomials(K); idx = mono_index(K); n = len(monos)
    N = d * n
    rows = []
    # T-condition: for each component i:  T(F_i) - sum_j (R_t)_{ij} F_j = 0
    for i in range(d):
        eq = {}
        for mi, (a, b, c) in enumerate(monos):
            for m, v in act_T_mono(a, b, c).items():
                key = (m, i * n + mi); eq[key] = eq.get(key, 0) + v
        for j in range(d):
            if abs(R_t[i, j]) > 0:
                for mi, m in enumerate(monos):
                    key = (m, j * n + mi); eq[key] = eq.get(key, 0) - R_t[i, j]
        # one row per monomial
        bym = {}
        for (m, col), v in eq.items(): bym.setdefault(m, {})[col] = bym.get(m, {}).get(col, 0) + v
        for m, cols in bym.items():
            row = np.zeros(N, dtype=complex)
            for col, v in cols.items(): row[col] += v
            rows.append(row)
    # S-condition
    for i in range(d):
        eq = {}
        for mi, (a, b, c) in enumerate(monos):
            for m, v in act_S_mono(a, b, c, K).items():
                key = (m, i * n + mi); eq[key] = eq.get(key, 0) + v
        for j in range(d):
            if abs(R_s[i, j]) > 0:
                for mi, m in enumerate(monos):
                    key = (m, j * n + mi); eq[key] = eq.get(key, 0) - R_s[i, j]
        bym = {}
        for (m, col), v in eq.items(): bym.setdefault(m, {})[col] = bym.get(m, {}).get(col, 0) + v
        for m, cols in bym.items():
            row = np.zeros(N, dtype=complex)
            for col, v in cols.items(): row[col] += v
            rows.append(row)
    A = np.array(rows)
    u, s, vh = svd(A)
    tol = 1e-9 * max(1, s[0])
    rank = int(np.sum(s > tol))
    null = vh[rank:].conj().T   # columns span the nullspace
    return null, monos

# q-series of X, Y, Z in p = q^{1/4}  (q = e^{2 pi i tau}): theta3 = sum p^{2n^2}, theta4 = sum (-1)^n p^{2n^2}, theta2^2 = 4p (sum p^{2n^2+2n})^2
NP = 80
def series_theta():
    t3 = np.zeros(NP); t4 = np.zeros(NP); s2 = np.zeros(NP)
    for nn in range(-20, 21):
        e = 2*nn*nn
        if e < NP: t3[e] += 1; t4[e] += (-1)**nn
    for nn in range(0, 20):
        e = 2*nn*nn + 2*nn
        if e < NP: s2[e] += 1
    def mul(a, b): return np.convolve(a, b)[:NP]
    X = np.zeros(NP); X[1:] = 4*mul(s2, s2)[:NP-1]
    Y = mul(t3, t3); Z = mul(t4, t4)
    return X, Y, Z, mul
X_s, Y_s, Z_s, mul = series_theta()
# sanity: Jacobi Y^2 = X^2 + Z^2
print("Jacobi on series:", np.abs(mul(Y_s, Y_s) - mul(X_s, X_s) - mul(Z_s, Z_s)).max())

def pow_series(base, e):
    out = np.zeros(NP); out[0] = 1
    for _ in range(e): out = mul(out, base)
    return out
pow_cache = {}
def mono_series(a, b, c):
    key = (a, b, c)
    if key not in pow_cache:
        pow_cache[key] = mul(mul(pow_series(X_s, a), pow_series(Y_s, b)), pow_series(Z_s, c))
    return pow_cache[key]

def with_cusp_condition(null, monos, d, min_p_order):
    """Impose ord_p(F_i) >= min_p_order on every component for F in the span of null."""
    if null.shape[1] == 0 or min_p_order <= 0: return null
    n = len(monos)
    rows = []
    for i in range(d):
        for pord in range(min_p_order):
            row = np.zeros(null.shape[1], dtype=complex)
            for col in range(null.shape[1]):
                v = null[:, col]
                coeff = 0
                for mi, (a, b, c) in enumerate(monos):
                    cv = v[i*n + mi]
                    if abs(cv) > 1e-12: coeff += cv * mono_series(a, b, c)[pord]
                row[col] = coeff
            rows.append(row)
    A = np.array(rows)
    if np.abs(A).max() < 1e-12: return null
    u, s, vh = svd(A)
    rank = int(np.sum(s > 1e-9*max(1, s[0])))
    sub = vh[rank:].conj().T
    return null @ sub

print("\nSanity: dim M_k(rho) via this machinery (expect 0,0,1,1 at k=-1/2,3/2,7/2,11/2):")
for K in (1, 3, 5, 7):
    null, monos = form_space(rho_u_t, rho_u_s, K)
    null2 = with_cusp_condition(null, monos, 3, 1)    # eta^3 f: ord_q F >= 1/8 -> no constant term -> ord_p >= 1
    print(f"  K={K}: dim M_K(rho_u) = {null.shape[1]}, dim M_(K-3/2)(rho) = {null2.shape[1]}")

print("\nYukawa forms with both L and R in T:  Y in M_k(rhobar x rhobar), k odd  [F = eta^18 Y of weight k+9, ord_p F >= 3]")
Rt = np.kron(rho_u_t.conj(), rho_u_t.conj()); Rs = np.kron(rho_u_s.conj(), rho_u_s.conj())
# symmetric / antisymmetric projectors on C^3 x C^3
Pperm = np.zeros((9, 9))
for i in range(3):
    for j in range(3): Pperm[3*i + j, 3*j + i] = 1
Psym = (np.eye(9) + Pperm)/2; Pasym = (np.eye(9) - Pperm)/2
results_TT = {}
for k in (1, 3, 5, 7):
    K = k + 9
    null, monos = form_space(Rt, Rs, K)
    nullc = with_cusp_condition(null, monos, 9, 3)
    # count symmetric and antisymmetric forms: project the component-vector part
    n = len(monos)
    def count_sub(P):
        if nullc.shape[1] == 0: return 0
        cols = []
        for col in range(nullc.shape[1]):
            v = nullc[:, col].reshape(9, n)
            cols.append((P @ v).reshape(-1))
        M = np.array(cols).T
        s = svd(M, compute_uv=False)
        return int(np.sum(s > 1e-9*max(1, s[0] if len(s) else 1)))
    results_TT[k] = (nullc.shape[1], count_sub(Psym), count_sub(Pasym), null.shape[1])
    print(f"  k={k}: dim M_k(rhobar x rhobar) = {nullc.shape[1]}  (symmetric part {count_sub(Psym)}, antisymmetric part {count_sub(Pasym)}; before the cusp condition {null.shape[1]})")

print("\nYukawa forms with L in T, R in Tbar:  Y in M_k(rhobar x rho), k even  [F = Y, degree k]")
Rt2 = np.kron(rho_u_t.conj(), rho_u_t); Rs2 = np.kron(rho_u_s.conj(), rho_u_s)
for k in (0, 2, 4, 6):
    null, monos = form_space(Rt2, Rs2, k)
    print(f"  k={k}: dim M_k(rhobar x rho) = {null.shape[1]}")
np.save('./yukawa_dims.npy', results_TT, allow_pickle=True)
