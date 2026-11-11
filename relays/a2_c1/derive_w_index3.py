#!/usr/bin/env python3
"""Blind second derivation of W:INDEX3 from GENESIS.md statements alone.

Pure exact cyclotomic arithmetic over Q(zeta_24) (stdlib only, ZERO floats, zero repo imports).
Verifies from first principles:
1. Exact Mp_2(Z) representation rho_T of F_23 = eta^21 * (theta_2^2, theta_3^2, theta_4^2)^T:
   - proves rho_T(S_mp)^2 = Z = +i * I_3 (compatible with weight k = 3/2, whereas conjugate rho_T_bar
     has rho_T_bar(Z) = -i * I_3, incompatible with weight 3/2!)
   - proves (rho_T(S_mp) * rho_T(T_mp))^3 = rho_T(S_mp)^2 = +i * I_3 with zero projective defect
   - diagonalises rho_T(T_mp) exactly over Q(zeta_8), finding cusp exponents (1/8, 3/8, 7/8).
2. Constructs the exact graded ring of Gamma(4) half-integral modular forms
   R = Q(zeta_24)[theta_2, theta_3, theta_4] / (theta_2^4 + theta_4^4 - theta_3^4)
   with exact Mp_2(Z) action at every degree d = 2k, and computes by exact rational/cyclotomic
   linear algebra:
   - at weight k = 3/2 (n = 0 cusp units): dim M_{3/2}(rho_T) = 0 AND Serre dual dim S_{1/2}(rho_T_bar) = 0,
     proving h^0 = 0, h^1 = 0, chi_{3/2}(rho_T, n = 0) = 0, and W_0 = (pi_coarse)_* V_{3/2}(rho_T, 0) = O_{P^1}(-1)^3!
   - hence for EVERY integer n, W_n = W_0 (x) O_{P^1}(n) = O_{P^1}(n - 1)^3 has exact Euler characteristic
     chi(X(1), V_{3/2}(rho_T, n)) = 3 * n (and +-3 at n = 1 uniform cusp unit, depending on 4d orientation/grading).
3. Independently verifies n = 1 WITHOUT invoking Birkhoff-Grothendieck by using multiplication by
   Delta(tau) = eta(tau)^24 = 2^(-8) * (theta_2 * theta_3 * theta_4)^8 (degree 24, weight 12, q^1 at cusp),
   computing dim Hom_{Mp_2(Z)}(rho_T, R_27) directly in degree-27 polynomials modulo Jacobi's quadric:
   confirms dim M_{27/2}(rho_T) == 3 EXACTLY!
4. Controls CTL-INDEX3:
   - Checks all 6 SL(2, Z) character twists rho_T (x) chi_eta^(4r) (r = 0..5) at weight 3/2 by exact
     Kawasaki orbifold Riemann-Roch over Q(zeta_24): shows r = 0, 2, 3, 4, 5 give chi = 0 while r = 1
     (i.e. chi_eta^(+4) twist) gives chi = 1 != 0 at n = 0!
   - Checks conjugate rho_T_bar at weight 3/2: fails central Z-action (+i vs -i) => 0 sections for ALL n!
   - Checks non-uniform cusp pole triples m = (m_1, m_2, m_3) inside M_{27/2}(rho_T) by exact q^(1/4)-series
     expansion of the 3 basis vectors: proves m = (0, 0, 1) (single-eigenline least remainder) gives dim = 1,
     m = (0, 1, 1) gives dim = 2, and ONLY uniform m = (1, 1, 1) (or sum m_j = 3) gives dim = 3!
"""
from fractions import Fraction


# Exact arithmetic in Q(zeta_24), where zeta_24^8 - zeta_24^4 + 1 = 0 (degree phi(24) = 8!).
# Basis: 1, z, z^2, ..., z^7 with reduction rule z^8 = z^4 - 1.
# Useful roots inside Q(zeta_24):
#   zeta_24 = z
#   zeta_12 = z^2
#   zeta_8  = z^3   (check: (z^3)^4 = z^12: z^8 = z^4 - 1 => z^12 = z^8 - z^4 = -1! Exact!)
#   zeta_6  = z^4
#   i       = z^6   (check: (z^6)^2 = z^12 = -1, and (z^3)^2 = z^6 => zeta_8 = e^{pi i / 4}, i = zeta_8^2! Exact!)
ZERO = (Fraction(0),) * 8
ONE = (Fraction(1),) + (Fraction(0),) * 7


def cyc_from_power(k):
    """Return z^k in Q(zeta_24) for any integer k."""
    k %= 24
    # Reduce powers >= 8 using z^8 = z^4 - 1:
    coeffs = [Fraction(0)] * 24
    coeffs[k] = Fraction(1)
    for p in range(23, 7, -1):
        if coeffs[p] != 0:
            c = coeffs[p]
            coeffs[p] = Fraction(0)
            coeffs[p - 4] += c
            coeffs[p - 8] -= c
    return tuple(coeffs[:8])


Z24_POW = [cyc_from_power(k) for k in range(24)]
I_CYC = Z24_POW[6]       # +i
Z8_CYC = Z24_POW[3]      # e^{2 pi i / 8} = e^{pi i / 4}


def c_add(a, b):
    return tuple(a[j] + b[j] for j in range(8))


def c_sub(a, b):
    return tuple(a[j] - b[j] for j in range(8))


def c_neg(a):
    return tuple(-a[j] for j in range(8))


def c_scale(a, q):
    q = Fraction(q)
    return tuple(a[j] * q for j in range(8))


def c_mul(a, b):
    res = [Fraction(0)] * 15
    for i in range(8):
        if a[i] != 0:
            ai = a[i]
            for j in range(8):
                if b[j] != 0:
                    res[i + j] += ai * b[j]
    for p in range(14, 7, -1):
        if res[p] != 0:
            c = res[p]
            res[p] = Fraction(0)
            res[p - 4] += c
            res[p - 8] -= c
    return tuple(res[:8])


def c_conj(a):
    """Complex conjugation z -> z^(-1) = z^23 in Q(zeta_24)."""
    out = ZERO
    for j in range(8):
        if a[j] != 0:
            out = c_add(out, c_scale(Z24_POW[(24 - j) % 24], a[j]))
    return out


def c_inv(a):
    """Exact multiplicative inverse in Q(zeta_24) by solving multiplication matrix over Q."""
    assert a != ZERO, "Division by zero in Q(zeta_24)"
    # Columns of multiplication by `a` on basis z^0..z^7:
    cols = [c_mul(a, Z24_POW[j]) for j in range(8)]
    M = [[cols[col][row] for col in range(8)] + [Fraction(1 if row == 0 else 0)] for row in range(8)]
    for col in range(8):
        piv = next(r for r in range(col, 8) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        fac = M[col][col]
        M[col] = [x / fac for x in M[col]]
        for r in range(8):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [M[r][c] - f * M[col][c] for c in range(9)]
    inv = tuple(M[row][8] for row in range(8))
    assert c_mul(a, inv) == ONE
    return inv


def mat_mul_c(A, B):
    m, k, n = len(A), len(B), len(B[0])
    out = [[ZERO for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for r in range(k):
            if A[i][r] != ZERO:
                air = A[i][r]
                for j in range(n):
                    if B[r][j] != ZERO:
                        out[i][j] = c_add(out[i][j], c_mul(air, B[r][j]))
    return out


def mat_eye_c(n, scalar=ONE):
    return [[scalar if i == j else ZERO for j in range(n)] for i in range(n)]


def nullspace_c(M):
    """Exact right nullspace basis of an m x n matrix M over Q(zeta_24)."""
    m = len(M)
    n = len(M[0]) if m else 0
    A = [row[:] for row in M]
    piv_cols = []
    r = 0
    for col in range(n):
        piv = next((i for i in range(r, m) if A[i][col] != ZERO), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv_p = c_inv(A[r][col])
        A[r] = [c_mul(x, inv_p) for x in A[r]]
        for i in range(m):
            if i != r and A[i][col] != ZERO:
                f = A[i][col]
                A[i] = [c_sub(A[i][c], c_mul(f, A[r][c])) for c in range(n)]
        piv_cols.append(col)
        r += 1
    free_cols = [c for c in range(n) if c not in piv_cols]
    basis = []
    for fc in free_cols:
        vec = [ZERO] * n
        vec[fc] = ONE
        for idx, pc in enumerate(piv_cols):
            vec[pc] = c_neg(A[idx][fc])
        basis.append(vec)
    return basis


def build_gamma4_space_and_mp2_action(deg):
    """Build exact basis and Mp_2(Z) action on R_deg = (C[theta_2, theta_3, theta_4] / (theta_2^4 + theta_4^4 - theta_3^4))_deg,
    corresponding to half-integral weight k = deg / 2.
    Canonical basis modulo theta_3^4 = theta_2^4 + theta_4^4: all monomials theta_2^a * theta_3^b * theta_4^c
    with a + b + c = deg and b in {0, 1, 2, 3}! (Exact dimension = 2*deg + 1 for deg >= 2, 3 for deg = 1, 1 for deg = 0!)
    Wait: check dim: #(a+c = deg - b) = deg - b + 1 summed over b=0..min(3, deg)!
      deg=1: 2 + 1 = 3
      deg=3: 4 + 3 + 2 + 1 = 10
      deg=27: 28 + 27 + 26 + 25 = 106!
    Under Mp_2(Z) (f(gamma tau) = j(gamma, tau)^deg * (gamma . f)(tau), where S_mp has factor sqrt(tau)):
    - T_mp: theta_2 -> zeta_8 * theta_2 (z^3), theta_3 -> theta_4, theta_4 -> theta_3!
      (Check: theta_2(tau+1) = e^{pi i / 4} theta_2(tau) = z^3 theta_2, theta_3(tau+1) = theta_4, theta_4(tau+1) = theta_3.)
    - S_mp: theta_2(-1/tau) = e^{-pi i / 4} sqrt(tau) theta_4(tau) = z^(-3) sqrt(tau) theta_4,
            theta_3(-1/tau) = z^(-3) sqrt(tau) theta_3,
            theta_4(-1/tau) = z^(-3) sqrt(tau) theta_2!
      (Check at deg=23 on eta^21*(th2^2, th3^2, th4^2) = 2^(-7)*(th2*th3*th4)^7*(th2^2, th3^2, th4^2):
       (z^(-3))^23 = z^(-69) = z^(3) = e^{+pi i / 4}! Exact match!)"""
    monoms = []
    for b in range(min(4, deg + 1)):
        for a in range(deg - b + 1):
            c = deg - b - a
            monoms.append((a, b, c))
    idx_of = {m: i for i, m in enumerate(monoms)}
    dim = len(monoms)

    def reduce_poly(terms):
        """Reduce dict {(a,b,c): coeff} modulo theta_3^4 -> theta_2^4 + theta_4^4."""
        work = dict(terms)
        while True:
            high = [m for m, v in work.items() if v != ZERO and m[1] >= 4]
            if not high:
                break
            for a, b, c in high:
                v = work.pop((a, b, c))
                m1 = (a + 4, b - 4, c)
                m2 = (a, b - 4, c + 4)
                work[m1] = c_add(work.get(m1, ZERO), v)
                work[m2] = c_add(work.get(m2, ZERO), v)
        vec = [ZERO] * dim
        for m, v in work.items():
            if v != ZERO:
                vec[idx_of[m]] = v
        return vec

    # Build T_mat and S_mat (column j = image of basis monomial j):
    T_cols = []
    S_cols = []
    s_phase = Z24_POW[(-3 * deg) % 24]  # (z^(-3))^deg
    for a, b, c in monoms:
        # T_mp sends theta_2^a theta_3^b theta_4^c -> z^(3a) * theta_2^a theta_4^b theta_3^c = z^(3a) * (a, c, b)!
        T_cols.append(reduce_poly({(a, c, b): Z24_POW[(3 * a) % 24]}))
        # S_mp sends theta_2^a theta_3^b theta_4^c -> s_phase * theta_4^a theta_3^b theta_2^c = s_phase * (c, b, a)!
        S_cols.append(reduce_poly({(c, b, a): s_phase}))

    T_mat = [[T_cols[col][row] for col in range(dim)] for row in range(dim)]
    S_mat = [[S_cols[col][row] for col in range(dim)] for row in range(dim)]
    return monoms, T_mat, S_mat


def hom_mp2_dimension(rho_T_mat, rho_S_mat, R_T_mat, R_S_mat):
    """Compute exact basis of intertwiners Phi: C^3 -> R_deg satisfying R_T * Phi = Phi * rho_T and R_S * Phi = Phi * rho_S.
    Each column j of Phi (j=0,1,2) is the j-th component s_j in R_deg of a vector-valued modular form s = (s_0, s_1, s_2)^T!
    Wait: check covariance convention!
    If s(tau) = [s_0, s_1, s_2]^T has components s_j = sum_i Phi_{i, j} e_i(tau),
    and (gamma . e_i)(tau) = j(gamma, tau)^(-2k) e_i(gamma tau) = sum_l R_gamma[l, i] e_l(tau):
    Wait: in `build_gamma4_space_and_mp2_action`, column `i` of `T_mat` is `e_i(gamma tau) / j(gamma, tau)^(2k)`
    expressed in the basis `e_l`, i.e., `e_i(gamma tau) = j(gamma, tau)^(2k) sum_l M_gamma[l, i] e_l(tau)`!
    Then for `s_j = sum_i Phi[i, j] e_i`:
      `s_j(gamma tau) = j^(2k) sum_{i, l} Phi[i, j] M_gamma[l, i] e_l(tau) = j^(2k) sum_l (M_gamma * Phi)[l, j] e_l(tau)`.
    On the other hand, `s(gamma tau) = j^(2k) rho(gamma) s(tau)` means:
      `s_j(gamma tau) = j^(2k) sum_r rho(gamma)[j, r] s_r(tau) = j^(2k) sum_{l, r} Phi[l, r] rho(gamma)[j, r] e_l(tau) = j^(2k) sum_l (Phi * rho(gamma)^T)[l, j] e_l(tau)`!
    SO THE EXACT INTERTWINING EQUATION IS:
      `M_gamma * Phi - Phi * rho(gamma)^T = 0` for gamma in {T_mp, S_mp}!"""
    d_space = len(R_T_mat)
    n_vars = 3 * d_space  # flatten Phi[i, j] as idx = 3*i + j
    rows = []
    for M_g, rho_g in ((R_T_mat, rho_T_mat), (R_S_mat, rho_S_mat)):
        for l in range(d_space):
            for j in range(3):
                row = [ZERO] * n_vars
                # + sum_i M_g[l][i] * Phi[i, j]
                for i in range(d_space):
                    if M_g[l][i] != ZERO:
                        row[3 * i + j] = c_add(row[3 * i + j], M_g[l][i])
                # - sum_r rho_g[j][r] * Phi[l, r]
                for r in range(3):
                    if rho_g[j][r] != ZERO:
                        row[3 * l + r] = c_sub(row[3 * l + r], rho_g[j][r])
                if any(x != ZERO for x in row):
                    rows.append(row)
    ns = nullspace_c(rows)
    # Reshape each null vector into d_space x 3 matrix Phi:
    return [[[v[3 * i + j] for j in range(3)] for i in range(d_space)] for v in ns]


def q4_series_monomial(a, b, c, max_u_pow=12):
    """Exact q_4 = q^(1/4) = e^(pi i tau / 2) series of theta_2^a * theta_3^b * theta_4^c up to u^max_u_pow,
    where u = q^(1/4) (note q_jacobi = e^(pi i tau) = u^2, and q_mod = e^(2 pi i tau) = u^4!):
      theta_2(tau) = 2 * u * (1 + u^4 + u^12 + ...)  [since q_J^(1/4) = (u^2)^(1/4)?
      HOLD ON! Check q vs u carefully!
      q_mod = e^(2 pi i tau), q_J = e^(pi i tau) = q_mod^(1/2).
      Then q_J^(1/4) = q_mod^(1/8)! Let w = q_mod^(1/8) = e^(pi i tau / 4), so q_J = w^4 and q_mod = w^8!
      - theta_2 = 2 w (1 + w^8 + w^24 + ...)
      - theta_3 = 1 + 2 w^4 + 2 w^16 + 2 w^36 + ...
      - theta_4 = 1 - 2 w^4 + 2 w^16 - 2 w^36 + ...
    Check Jacobi's identity theta_2^4 + theta_4^4 == theta_3^4 and 2 eta^3 == theta_2 theta_3 theta_4!"""
    N = max_u_pow
    th2 = [Fraction(0)] * (N + 1)
    for n in range(10):
        p = 1 + 4 * n * (n + 1)  # w * (w^4)^(n(n+1)) = w^(1 + 4n(n+1)) -> 1, 9, 25, ...
        if p <= N:
            th2[p] += 2
    th3 = [Fraction(0)] * (N + 1)
    th4 = [Fraction(0)] * (N + 1)
    th3[0] = Fraction(1)
    th4[0] = Fraction(1)
    for n in range(1, 10):
        p = 4 * n * n
        if p <= N:
            th3[p] += 2
            th4[p] += 2 * ((-1) ** n)

    def poly_mul(p1, p2):
        out = [Fraction(0)] * (N + 1)
        for i, v1 in enumerate(p1):
            if v1 != 0:
                for j in range(N + 1 - i):
                    if p2[j] != 0:
                        out[i + j] += v1 * p2[j]
        return out

    def poly_pow(p, e):
        res = [Fraction(1 if i == 0 else 0) for i in range(N + 1)]
        for _ in range(e):
            res = poly_mul(res, p)
        return res

    return poly_mul(poly_mul(poly_pow(th2, a), poly_pow(th3, b)), poly_pow(th4, c))


def main():
    print("=== 1. EXACT CYCLOTOMIC VERIFICATION OF Mp_2(Z) MULTIPLIER rho_T ===")
    # Check Q(zeta_24) identities:
    assert c_mul(I_CYC, I_CYC) == c_neg(ONE)
    assert c_mul(Z8_CYC, Z8_CYC) == I_CYC
    # Verify q-series Jacobi quadric first:
    lhs = [x + y for x, y in zip(q4_series_monomial(4, 0, 0, 40), q4_series_monomial(0, 0, 4, 40))]
    rhs = q4_series_monomial(0, 4, 0, 40)
    assert lhs == rhs, "Jacobi quadric q-series sanity check failed!"

    # In basis (v_2, v_3, v_4) = eta^21 * (theta_2^2, theta_3^2, theta_4^2):
    # T_mp: e^{2 pi i (7/8)} * diag_swap = z^(21) * [[i, 0, 0], [0, 0, 1], [0, 1, 0]]
    # Check: e^{2 pi i / 24} = z^2! WAIT A SECOND!!
    # CHECK z = zeta_24 = e^{2 pi i / 24} vs e^{pi i / 12}!!
    # Earlier we set I_CYC = z^6! If z^6 = i = e^{pi i / 2} = e^{2 pi i / 4}, then z = e^{2 pi i / 24}!
    # Let's check z^3 = e^{2 pi i (3/24)} = e^{2 pi i / 8} = e^{pi i / 4} = zeta_8!
    # THEN e^{2 pi i / 8} = z^3, and e^{2 pi i (7/8)} = (z^3)^7 = z^21!
    # AND under T_mp: eta(tau + 1) = e^{pi i / 12} eta(tau) = e^{2 pi i / 24} eta(tau) = z^1 * eta(tau)!
    # So eta(tau + 1)^21 = z^21 * eta(tau)^21!
    # AND theta_2(tau + 1)^2 = (z^3)^2 theta_2^2 = z^6 theta_2^2 = i * theta_2^2!
    # Product on v_2: z^21 * z^6 = z^27 = z^3 = e^{2 pi i (1/8)}!
    # Product on v_3 + v_4: z^21 * 1 = e^{2 pi i (7/8)}!
    # Product on v_3 - v_4: z^21 * (-1) = z^21 * z^12 = z^33 = z^9 = (z^3)^3 = e^{2 pi i (3/8)}!
    # EXACT!! Every single 24th root power matches!
    rho_T = [
        [Z24_POW[3], ZERO,        ZERO],
        [ZERO,       ZERO,        Z24_POW[21]],
        [ZERO,       Z24_POW[21], ZERO],
    ]
    rho_S = [
        [ZERO,       ZERO,       Z24_POW[3]],
        [ZERO,       Z24_POW[3], ZERO],
        [Z24_POW[3], ZERO,       ZERO],
    ]

    S2 = mat_mul_c(rho_S, rho_S)
    ST = mat_mul_c(rho_S, rho_T)
    ST3 = mat_mul_c(mat_mul_c(ST, ST), ST)
    assert S2 == mat_eye_c(3, I_CYC), f"S^2 != i I_3: {S2}"
    assert ST3 == S2, f"(ST)^3 != S^2: {ST3}"
    print("Verified over exact Q(zeta_24): rho_T(S_mp)^2 = +i * I_3 = (rho_T(S_mp) * rho_T(T_mp))^3 (ZERO projective defect).")

    # Verify F_23 = 2^(-7) * (th2*th3*th4)^7 * (th2^2, th3^2, th4^2) in R_23 transforms by rho_T!
    m23, R23_T, R23_S = build_gamma4_space_and_mp2_action(23)
    homs_23 = hom_mp2_dimension(rho_T, rho_S, R23_T, R23_S)
    print(f"Sanity check at weight 23/2 (deg 23, containing F_23): dim M_{{23/2}}(rho_T) = {len(homs_23)}")
    assert len(homs_23) >= 1

    # Check conjugate representation rho_T_bar at weight 3/2:
    rho_T_bar = [[c_conj(x) for x in row] for row in rho_T]
    rho_S_bar = [[c_conj(x) for x in row] for row in rho_S]
    S2_bar = mat_mul_c(rho_S_bar, rho_S_bar)
    assert S2_bar == mat_eye_c(3, c_neg(I_CYC))
    print("Verified: conjugate rho_T_bar has rho_T_bar(Z) = -i * I_3, incompatible with weight 3/2 (where j(Z,tau)^(-3) = +i).")

    print("\n=== 2. EXACT INDEX AT n = 0 (WEIGHT 3/2 AND SERRE DUAL WEIGHT 1/2) ===")
    _, R3_T, R3_S = build_gamma4_space_and_mp2_action(3)
    h0_n0 = hom_mp2_dimension(rho_T, rho_S, R3_T, R3_S)
    _, R1_T, R1_S = build_gamma4_space_and_mp2_action(1)
    h1_bound_n0 = hom_mp2_dimension(rho_T_bar, rho_S_bar, R1_T, R1_S)
    print(f"At n = 0 cusp units: h^0 = dim M_{{3/2}}(rho_T) = {len(h0_n0)}")
    print(f"Serre dual bound:   dim M_{{1/2}}(rho_T_bar) = {len(h1_bound_n0)}  =>  h^1 = dim S_{{1/2}}(rho_T_bar) = 0")
    assert len(h0_n0) == 0 and len(h1_bound_n0) == 0
    print("=> PROVED ALGEBRAICALLY: chi(X(1), V_{3/2}(rho_T, n = 0)) = 0 - 0 = 0,")
    print("   and W_0 = (pi_coarse)_* V_{3/2}(rho_T, 0) = O_{P^1}(-1)^3.")
    print("=> Therefore W_n = W_0 (x) O_{P^1}(n) = O_{P^1}(n - 1)^3 has chi = 3*n for EVERY n in Z (chi = +3 at n = 1, +-3 with 4d grading).")

    print("\n=== 3. DIRECT INDEPENDENT COMPUTATION AT n = 1 VIA x Delta (DEGREE 27 = WEIGHT 27/2) ===")
    # Multiplying V_{3/2}(rho_T, n=1) (allowing poles q^(alpha_j - 1)) by Delta = eta^24 = 2^(-8) (th2*th3*th4)^8
    # maps H^0(X(1), V_{3/2}(rho_T, n=1)) ISO-MORPHICALLY onto M_{27/2}(rho_T) subset R_27^3!
    m27, R27_T, R27_S = build_gamma4_space_and_mp2_action(27)
    h0_n1 = hom_mp2_dimension(rho_T, rho_S, R27_T, R27_S)
    print(f"Direct polynomial intertwiner count dim M_{{27/2}}(rho_T) [= h^0 at n = 1]: {len(h0_n1)}")
    assert len(h0_n1) == 3

    print("\n=== 4. CONTROLS (CTL-INDEX3: ALL 6 CHARACTER TWISTS & NON-UNIFORM CUSP UNITS) ===")

    def mat_trace_c(M):
        out = ZERO
        for idx in range(len(M)):
            out = c_add(out, M[idx][idx])
        return out

    def cyc_to_rational(x):
        assert all(x[j] == 0 for j in range(1, 8)), f"Expected rational in Q(zeta_24), got {x}"
        return x[0]

    def orbifold_rr_exact(deg, rho_T_mat, rho_S_mat):
        """Exact Kawasaki orbifold Riemann-Roch chi(X(1), V_{deg/2}(rho, n=0)) over Q(zeta_24).
        Twisting sections f by eta(tau)^(-deg) reduces to weight-0 PSL(2, Z)-equivariant sections with
          tilde_rho(T) = z^(-deg) rho(T_mp),  tilde_rho(S) = z^(+3*deg) rho(S_mp),
          tilde_rho(S*T) = z^(+2*deg) rho(S_mp * T_mp).
        Exact rational elliptic & parabolic divisor contributions on coarse P^1:
          sum(alpha_j)    from Fourier projector trace of rho(T_mp)^n (n = 0..23),
          sum(beta_2 / 2) = (d - tr(tilde_rho(S))) / 4,
          sum(beta_3 / 3) = d/3 + ((omega + 2*omega^2)/9)*tr(U) + ((2*omega + omega^2)/9)*tr(U^2)
                            where U = tilde_rho(S*T) and omega = z^8 = e^(2 pi i / 3).
        """
        d = len(rho_T_mat)
        # Verify central consistency i^deg * rho(Z) == I_d:
        S2_chk = mat_mul_c(rho_S_mat, rho_S_mat)
        z_fac = Z24_POW[(6 * deg) % 24]
        assert [[c_mul(z_fac, x) for x in row] for row in S2_chk] == mat_eye_c(d, ONE), "Central Z mismatch!"

        # 1. Cusp exponents alpha_j = m / 24 in [0, 1) via exact Z/24 character orthogonality:
        T_pows = [mat_eye_c(d, ONE)]
        for _ in range(23):
            T_pows.append(mat_mul_c(T_pows[-1], rho_T_mat))
        assert mat_mul_c(T_pows[-1], rho_T_mat) == mat_eye_c(d, ONE), "rho(T_mp)^24 != I"
        tr_T = [mat_trace_c(P) for P in T_pows]
        sum_alpha = Fraction(0)
        mult_total = Fraction(0)
        for m in range(24):
            acc = ZERO
            for n_pow in range(24):
                acc = c_add(acc, c_mul(Z24_POW[(-m * n_pow) % 24], tr_T[n_pow]))
            mult_m = cyc_to_rational(acc) / 24
            assert mult_m.denominator == 1 and mult_m >= 0
            mult_total += mult_m
            sum_alpha += mult_m * Fraction(m, 24)
        assert mult_total == d

        # 2. Elliptic point [i] of order 2: tilde_rho(S) = z^(3*deg) * rho_S_mat
        s_tilde_fac = Z24_POW[(3 * deg) % 24]
        tr_S_tilde = cyc_to_rational(c_mul(s_tilde_fac, mat_trace_c(rho_S_mat)))
        sum_beta2_half = (Fraction(d) - tr_S_tilde) / 4

        # 3. Elliptic point [omega] of order 3: U = tilde_rho(S*T) = z^(2*deg) * rho_S_mat * rho_T_mat
        st_mat = mat_mul_c(rho_S_mat, rho_T_mat)
        u_fac = Z24_POW[(2 * deg) % 24]
        U_mat = [[c_mul(u_fac, x) for x in row] for row in st_mat]
        U2_mat = mat_mul_c(U_mat, U_mat)
        omega = Z24_POW[8]
        omega2 = Z24_POW[16]
        c1 = c_scale(c_add(omega, c_scale(omega2, 2)), Fraction(1, 9))
        c2 = c_scale(c_add(c_scale(omega, 2), omega2), Fraction(1, 9))
        ell3_cyc = c_add(c_mul(c1, mat_trace_c(U_mat)), c_mul(c2, mat_trace_c(U2_mat)))
        sum_beta3_third = Fraction(d, 3) + cyc_to_rational(ell3_cyc)

        deg_W0 = Fraction(d * deg, 24) - sum_alpha - sum_beta2_half - sum_beta3_third
        chi_val = Fraction(d) + deg_W0
        assert chi_val.denominator == 1, f"Non-integer orbifold RR chi={chi_val}!"
        return int(chi_val)

    # Benchmark gate on classical scalar SL(2, Z) modular forms of even weight 2m = 0, 2, 4, 6, 8, 10, 12:
    scalar_rr = [orbifold_rr_exact(4 * m, [[ONE]], [[ONE]]) for m in range(7)]
    print(f"Benchmark check (scalar SL(2,Z) weights 0,2,4,6,8,10,12): chi = {scalar_rr}")
    assert scalar_rr == [1, 0, 1, 1, 1, 1, 2]
    assert orbifold_rr_exact(3, rho_T, rho_S) == 0
    assert orbifold_rr_exact(27, rho_T, rho_S) == 3

    # Control A: All 6 SL(2, Z) character twists chi_eta^(4r) (r = 0..5) at weight 3/2 (deg = 3, n = 0):
    # Note: R_3 = C[th2, th3, th4]_3 has level 4 (capturing r in {0, 3}), whereas r in {1, 2, 4, 5}
    # carry cube-root characters chi_eta^(4r) of level 12; orbifold_rr_exact evaluates all 6 twists exactly!
    twist_chi_n0 = {}
    for r in range(6):
        t_fac = Z24_POW[(4 * r) % 24]
        s_fac = Z24_POW[(12 * r) % 24]
        rho_T_tw = [[c_mul(x, t_fac) for x in row] for row in rho_T]
        rho_S_tw = [[c_mul(x, s_fac) for x in row] for row in rho_S]
        twist_chi_n0[r] = orbifold_rr_exact(3, rho_T_tw, rho_S_tw)
    print(f"CTL-INDEX3-A (all 6 SL(2,Z) character twists r=0..5 at weight 3/2, n=0): chi = {twist_chi_n0}")
    assert twist_chi_n0 == {0: 0, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0}

    # Control B: Conjugate multiplier rho_T_bar at weight 3/2 (deg 3 and deg 27):
    h_bar_n0 = hom_mp2_dimension(rho_T_bar, rho_S_bar, R3_T, R3_S)
    h_bar_n1 = hom_mp2_dimension(rho_T_bar, rho_S_bar, R27_T, R27_S)
    print(f"CTL-INDEX3-B (conjugate rho_T_bar at weight 3/2): dim at n=0 is {len(h_bar_n0)}, dim at n=1 is {len(h_bar_n1)}")
    assert len(h_bar_n0) == 0 and len(h_bar_n1) == 0

    # Control C: Non-uniform cusp pole triples m = (m_1, m_2, m_3) <= (1, 1, 1) on the 3 T_mp-eigenlines (1/8, 3/8, 7/8)!
    # In basis (v_2, v_3, v_4), the 3 T_mp-eigenlines are:
    #   e_(1/8) = v_2               (ord_w of s*Delta >= 1; if m_1 = 0, must have ord_w >= 1 + 8 = 9!)
    #   e_(3/8) = v_3 - v_4         (ord_w of s*Delta >= 3; if m_2 = 0, must have ord_w >= 3 + 8 = 11!)
    #   e_(7/8) = v_3 + v_4         (ord_w of s*Delta >= 7; if m_3 = 0, must have ord_w >= 7 + 8 = 15!)
    # Expand all monomials in m27 in w = q_mod^(1/8) up to w^16:
    monom_w = [q4_series_monomial(a, b, c, 16) for (a, b, c) in m27]

    def eval_basis_w(Phi):
        """Return w-series (length 17, entries in Q(zeta_24)) of (e_1/8, e_3/8, e_7/8) for intertwiner Phi in M_{27/2}(rho_T)."""
        s_v = [[ZERO] * 17 for _ in range(3)]
        for i, w_ser in enumerate(monom_w):
            for j in range(3):
                c_ij = Phi[i][j]
                if c_ij != ZERO:
                    for p in range(17):
                        if w_ser[p] != 0:
                            s_v[j][p] = c_add(s_v[j][p], c_scale(c_ij, w_ser[p]))
        e_1 = s_v[0]
        e_3 = [c_sub(s_v[1][p], s_v[2][p]) for p in range(17)]
        e_7 = [c_add(s_v[1][p], s_v[2][p]) for p in range(17)]
        return e_1, e_3, e_7

    series_3 = [eval_basis_w(Phi) for Phi in h0_n1]
    for k_idx, (e1, e3, e7) in enumerate(series_3):
        o1 = next((p for p, v in enumerate(e1) if v != ZERO), 99)
        o3 = next((p for p, v in enumerate(e3) if v != ZERO), 99)
        o7 = next((p for p, v in enumerate(e7) if v != ZERO), 99)
        print(f"  Basis section #{k_idx + 1} of M_{{27/2}}(rho_T): leading w = q^(1/8) powers on (1/8, 3/8, 7/8) lines = ({o1}, {o3}, {o7})")

    # Compute subspace dimensions for m = (0,0,0), (0,0,1), (0,1,1), (1,1,1):
    # A linear combination sum_{k=0..2} lambda_k Phi_k satisfies m = (m1, m2, m3) in {0,1}^3 iff:
    #   if m1 == 0: e1[p] == 0 for all p < 9
    #   if m2 == 0: e3[p] == 0 for all p < 11
    #   if m3 == 0: e7[p] == 0 for all p < 15
    for m_vec in ((0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)):
        eqs = []
        if m_vec[0] == 0:
            for p in range(9):
                eqs.append([series_3[c_idx][0][p] for c_idx in range(3)])
        if m_vec[1] == 0:
            for p in range(11):
                eqs.append([series_3[c_idx][1][p] for c_idx in range(3)])
        if m_vec[2] == 0:
            for p in range(15):
                eqs.append([series_3[c_idx][2][p] for c_idx in range(3)])
        ns = nullspace_c(eqs) if eqs else [[ONE, ZERO, ZERO], [ZERO, ONE, ZERO], [ZERO, ZERO, ONE]]
        print(f"CTL-INDEX3-C (parabolic cusp pole vector m={m_vec}, sum={sum(m_vec)}): dim H^0 = {len(ns)}")
        assert len(ns) == sum(m_vec)

    print("\nALL W:INDEX3 CHECKS AND CONTROLS PASSED.")


if __name__ == "__main__":
    main()
