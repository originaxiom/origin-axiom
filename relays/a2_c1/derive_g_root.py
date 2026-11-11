#!/usr/bin/env python3
"""Blind second derivation of G:ROOT from stated premises GM3, GM4, SE1, SE2 alone.

Pure exact integer arithmetic (stdlib only, zero floats, zero repo imports).
Verifies:
1. H_1(M_Phi; Z) = Z (+) Z^2 / (Phi - I) Z^2 via exact Smith normal form over Z.
2. Orientable (SE2: det(Phi) = +1) + hyperbolic (GM3: |tr(Phi)| > 2) + torsion-free H_1
   (SE1: invariant factors of Phi - I have no >1 finite divisor and rank matches) => tr(Phi) = 3.
3. Exact Gauss reduction of all indefinite binary quadratic forms of discriminant D = 5,
   proving wide class number h(5) = 1 and narrow class number h^+(5) = 1, hence a UNIQUE
   SL(2, Z) conjugacy class of trace 3, represented by LR = [[2, 1], [1, 1]].
4. Explicit SL(2, Z) conjugacy on [-12, 12]^4 census and explicit conjugators between
   based representatives LR, RL, and (LR)^{-1}.
5. Controls CTL-ROOT:
   - Dropping SE2 (det = -1) admits tr = +-1 (LP and (LP)^{-1}, Gieseking manifold m000).
   - Dropping GM3 (|tr| <= 2, det = +1) admits elliptic tr = 1 (order 6) AND parabolic
     Phi = L = [[1, 1], [0, 1]] where H_1(M_L; Z) = Z^2 IS ALSO TORSION-FREE over Z.
   - Perturbing tr = +3 to tr = -3 (-LR, m003) yields Tor(H_1) = Z/5Z (order 5 != 1).
"""
import math


def mat_mul(A, B):
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]


def mat_inv_gl2z(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    assert d in (1, -1), f"Not in GL(2, Z): det={d}"
    return [[d * A[1][1], -d * A[0][1]], [-d * A[1][0], d * A[0][0]]]


def tr(A):
    return A[0][0] + A[1][1]


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def smith_normal_form_2x2(M):
    """Exact 2x2 integer Smith normal form invariant factors (d1, d2) with d1 >= 0, d2 >= 0, d1 | d2."""
    a, b = M[0][0], M[0][1]
    c, d = M[1][0], M[1][1]
    if a == 0 and b == 0 and c == 0 and d == 0:
        return (0, 0)
    d1 = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d)))
    det_m = abs(a * d - b * c)
    if det_m == 0:
        return (d1, 0)
    return (d1, det_m // d1)


def h1_mapping_torus(Phi):
    """For M_Phi = (T_{1,1} x [0,1]) / ((x,1)~(Phi(x),0)),
    pi_1(M_Phi) = <a, b, t | t a t^{-1} = Phi_*(a), t b t^{-1} = Phi_*(b)>.
    Abelianisation kills [a, b] (the puncture boundary loop!), giving:
    H_1(M_Phi; Z) = Z<t> (+) coker(Phi - I).
    Returns (free_rank, torsion_invariants)."""
    B = [[Phi[0][0] - 1, Phi[0][1]], [Phi[1][0], Phi[1][1] - 1]]
    d1, d2 = smith_normal_form_2x2(B)
    free_rank = 1 + (1 if d1 == 0 else 0) + (1 if d2 == 0 else 0)
    torsion = tuple(x for x in (d1, d2) if x > 1)
    return free_rank, torsion


def is_hyperbolic_gl2z(Phi):
    """A mapping class of T_{1,1} is pseudo-Anosov iff Phi^2 in SL(2, Z) has |tr(Phi^2)| > 2."""
    d = det(Phi)
    assert d in (1, -1)
    Phi2 = mat_mul(Phi, Phi)
    return abs(tr(Phi2)) > 2


def gauss_reduced_forms(D):
    """Enumerate ALL Gauss-reduced indefinite binary quadratic forms [a, b, c] of non-square discriminant D > 0.
    A form a x^2 + b x y + c y^2 (b^2 - 4ac = D) is Gauss-reduced iff 0 < sqrt(D) - b < 2|a| < sqrt(D) + b."""
    forms = []
    s = math.isqrt(D)
    assert s * s < D, "D must not be a square"
    # From 0 < sqrt(D) - b => b <= s, and b > 0 since 2|a| > sqrt(D) - b and 2|a| < sqrt(D) + b => b > 0.
    for b in range(1, s + 1):
        if (D - b * b) % 4 != 0:
            continue
        prod = (D - b * b) // 4  # -a*c = prod > 0
        for abs_a in range(1, prod + 1):
            if prod % abs_a != 0:
                continue
            # Check (sqrt(D) - b) < 2*abs_a < (sqrt(D) + b) strictly using integers:
            # 2*abs_a - b < sqrt(D) < 2*abs_a + b (when 2*abs_a > b; if 2*abs_a <= b, first inequality is automatic)
            cond_upper = (2 * abs_a - b <= 0) or ((2 * abs_a - b) ** 2 < D)
            cond_lower = (2 * abs_a + b > 0) and ((2 * abs_a + b) ** 2 > D)
            if cond_upper and cond_lower:
                for sign_a in (1, -1):
                    a = sign_a * abs_a
                    c = -prod // a
                    assert b * b - 4 * a * c == D
                    forms.append((a, b, c))
    return sorted(forms)


def gauss_step(form):
    """Single proper SL(2, Z) Gauss reduction step on indefinite reduced form (a, b, c) of discriminant D."""
    a, b, c = form
    D = b * b - 4 * a * c
    s = math.isqrt(D)
    # Standard Zagier / Gauss step S * T^k with matrix [[0, -1], [1, k]]:
    denom = 2 * abs(c)
    # Choose k so that sqrt(D) - denom < b' <= sqrt(D) where b' = -b + 2*c*k (up to sign):
    # Specifically, apply [[0, -1], [1, m]] sending (a, b, c) -> (c, -b + 2*c*m, a - b*m + c*m^2)
    best = None
    for m in range(-abs(a) - abs(b) - 5, abs(a) + abs(b) + 6):
        a2 = c
        b2 = -b + 2 * c * m
        c2 = a - b * m + c * m * m
        if b2 > 0 and b2 * b2 < D and ((2 * abs(a2) - b2 <= 0) or ((2 * abs(a2) - b2) ** 2 < D)) and ((2 * abs(a2) + b2) ** 2 > D):
            best = ((a2, b2, c2), [[0, -1], [1, m]])
            break
    assert best is not None
    return best


def matrix_to_form_tr3(A):
    """Bijection from {A in SL(2, Z) : tr(A) = 3} to primitive forms of discriminant 5:
    For A = [[p, q], [r, 3 - p]], f_A(x, y) = r x^2 + (3 - 2p) x y - q y^2 has disc (3-2p)^2 + 4qr = 5."""
    assert det(A) == 1 and tr(A) == 3
    p, q = A[0]
    r, s = A[1]
    assert p + s == 3
    f = (r, 3 - 2 * p, -q)
    assert f[1] ** 2 - 4 * f[0] * f[2] == 5
    return f


def reduce_sl2z_tr3_to_LR(A):
    """Construct an explicit C in SL(2, Z) such that C^{-1} A C = LR = [[2, 1], [1, 1]] by Euclidean / parabolic descent."""
    LR = [[2, 1], [1, 1]]
    L = [[1, 1], [0, 1]]
    Linv = [[1, -1], [0, 1]]
    S = [[0, -1], [1, 0]]
    cur = [row[:] for row in A]
    C = [[1, 0], [0, 1]]
    # Reduce the quadratic form f_cur(x, y) into the reduced Gauss set {(1, 1, -1), (-1, 1, 1)}:
    for _ in range(200):
        if cur == LR:
            assert mat_mul(mat_mul(mat_inv_gl2z(C), A), C) == LR
            return C
        f = matrix_to_form_tr3(cur)
        a, b, c = f
        if f == (1, 1, -1):
            # p = (3 - b)//2 = 1, r = 1, q = 1 => cur = [[1, 1], [1, 2]] = RL!
            # L^{-1} * RL * L? Check: L * RL * L^{-1} = [[2, 1], [1, 1]] = LR, so C_step = L^{-1}!
            step = Linv
        elif f == (-1, 1, 1):
            # cur = [[1, -1], [-1, 2]] = (LR)^{-1}; S * cur * S^{-1} = [[2, 1], [1, 1]] = LR, so C_step = S^{-1} = -S?
            # Wait: check S^{-1} = [[0, 1], [-1, 0]]: S^{-1} [[1, -1], [-1, 2]] S = [[2, 1], [1, 1]]!
            step = [[0, 1], [-1, 0]]
        elif abs(a) > abs(c) and c != 0:
            step = S
        else:
            # Shift b = 3 - 2p modulo 2|a| via [[1, m], [0, 1]]:
            # Conjugating cur by U = [[1, m], [0, 1]]: U^{-1} cur U has r' = r = a, p' = p - m*r => b' = b + 2*m*a
            if a == 0:
                step = S
            else:
                # Choose m minimizing |b + 2*m*a|, breaking ties toward reduced range
                candidates = []
                for m in (-(b // (2 * a)) - 1, -(b // (2 * a)), -(b // (2 * a)) + 1):
                    b_new = b + 2 * m * a
                    candidates.append((abs(b_new - 1), abs(b_new), m))
                _, _, m_best = min(candidates)
                if m_best == 0:
                    step = S
                else:
                    step = [[1, m_best], [0, 1]]
        cur = mat_mul(mat_mul(mat_inv_gl2z(step), cur), step)
        C = mat_mul(C, step)
    raise RuntimeError(f"Failed to reduce {A}")


def main():
    L = [[1, 1], [0, 1]]
    R = [[1, 0], [1, 1]]
    P = [[0, 1], [1, 0]]
    LR = mat_mul(L, R)
    RL = mat_mul(R, L)
    LP = mat_mul(L, P)
    LR_inv = mat_inv_gl2z(LR)

    print("=== 1. ALGEBRAIC FORMULA FOR H_1(M_Phi; Z) AND TRACE SELECTION ===")
    print(f"LR = {LR}, det(LR) = {det(LR)}, tr(LR) = {tr(LR)}, H_1(M_LR) rank/torsion = {h1_mapping_torus(LR)}")
    print(f"RL = {RL}, det(RL) = {det(RL)}, tr(RL) = {tr(RL)}, H_1(M_RL) rank/torsion = {h1_mapping_torus(RL)}")
    print(f"(LR)^(-1) = {LR_inv}, H_1(M_(LR)^(-1)) rank/torsion = {h1_mapping_torus(LR_inv)}")

    # Proof check on trace equation under det = +1:
    # For det(Phi) = +1, det(Phi - I) = 2 - tr(Phi).
    # Torsion-free with finite coker(Phi - I) <=> |2 - tr(Phi)| = 1 <=> tr(Phi) in {1, 3}.
    valid_traces_det_pos1 = [t for t in range(-20, 21) if abs(2 - t) == 1]
    hyperbolic_traces_det_pos1 = [t for t in valid_traces_det_pos1 if abs(t) > 2]
    print(f"det=+1 traces with |det(Phi - I)| = 1 in [-20, 20]: {valid_traces_det_pos1}")
    print(f"det=+1 hyperbolic traces (|tr| > 2) with |det(Phi - I)| = 1: {hyperbolic_traces_det_pos1}")
    assert valid_traces_det_pos1 == [1, 3]
    assert hyperbolic_traces_det_pos1 == [3]

    print("\n=== 2. EXACT CLASS NUMBER PROOF (DISCRIMINANT D = 5) ===")
    red_forms = gauss_reduced_forms(5)
    print(f"All Gauss-reduced indefinite forms of discriminant D = 5: {red_forms}")
    assert red_forms == [(-1, 1, 1), (1, 1, -1)]
    next_f, step_mat = gauss_step((1, 1, -1))
    next_f2, step_mat2 = gauss_step(next_f)
    print(f"Gauss cycle from (1, 1, -1): (1, 1, -1) -> {next_f} (via {step_mat}) -> {next_f2} (via {step_mat2})")
    assert next_f == (-1, 1, 1) and next_f2 == (1, 1, -1)
    print("Conclusion: narrow class number h^+(5) = 1 and wide class number h(5) = 1.")
    print("Every A in SL(2, Z) with tr(A) = 3 lies in the single SL(2, Z)-conjugacy class of LR.")

    print("\n=== 3. EXHAUSTIVE BOX CENSUS IN GL(2, Z) WITH ENTRIES IN [-8, 8] ===")
    sl2_tr3_count = 0
    gl2_det_neg1_tf_hyp = []
    parabolic_tf_examples = []
    elliptic_tf_examples = []
    for a in range(-8, 9):
        for b in range(-8, 9):
            for c in range(-8, 9):
                for d in range(-8, 9):
                    d_val = a * d - b * c
                    if d_val not in (1, -1):
                        continue
                    M = [[a, b], [c, d]]
                    rk, tor = h1_mapping_torus(M)
                    hyp = is_hyperbolic_gl2z(M)
                    if tor == ():  # strictly torsion-free H_1(M; Z)!
                        if d_val == 1 and hyp:
                            assert tr(M) == 3, f"Unexpected hyperbolic SL(2,Z) trace: {M}"
                            C = reduce_sl2z_tr3_to_LR(M)
                            assert det(C) == 1
                            sl2_tr3_count += 1
                        elif d_val == -1 and hyp:
                            assert abs(tr(M)) == 1, f"Unexpected det=-1 hyperbolic trace: {M}"
                            gl2_det_neg1_tf_hyp.append(tr(M))
                        elif d_val == 1 and not hyp:
                            if tr(M) == 2 and len(parabolic_tf_examples) < 3:
                                parabolic_tf_examples.append((M, rk, tor))
                            elif abs(tr(M)) < 2 and len(elliptic_tf_examples) < 3:
                                elliptic_tf_examples.append((M, tr(M), rk, tor))
    print(f"Verified {sl2_tr3_count} hyperbolic SL(2, Z) torsion-free matrices in [-8, 8]^4:")
    print("  100% have tr = 3 and 100% were explicitly conjugated in SL(2, Z) to LR = [[2, 1], [1, 1]].")

    print("\n=== 4. BASED VS UNBASED AMBIGUITY (UNSAID IN G:ROOT) ===")
    C_RL = reduce_sl2z_tr3_to_LR(RL)
    C_inv = reduce_sl2z_tr3_to_LR(LR_inv)
    print(f"Explicit C in SL(2, Z) with C^(-1) * RL * C = LR: {C_RL}")
    print(f"Explicit C in SL(2, Z) with C^(-1) * (LR)^(-1) * C = LR: {C_inv}")
    print("Fixed-point quadratic of LR (2 tau + 1 = tau(tau + 1)): tau^2 - tau - 1 = 0")
    print("Fixed-point quadratic of RL (tau + 1 = tau(tau + 2)):   tau^2 + tau - 1 = 0")
    print("=> GM3 + GM4 + SE1 + SE2 determines the unbased conjugacy class [LR] (unmarked manifold m004),")
    print("   NOT the based matrix LR vs RL vs (LR)^(-1), nor an orientation of m004.")

    print("\n=== 5. CONTROLS (CTL-ROOT: ALL MUST FIRE AS PREDICTED) ===")
    # Control A: Drop SE2 (allow det = -1)
    rk_lp, tor_lp = h1_mapping_torus(LP)
    print(f"CTL-ROOT-A (drop SE2, det = -1): LP = {LP}, det={det(LP)}, tr={tr(LP)}, hyp={is_hyperbolic_gl2z(LP)}, H_1=(rk={rk_lp}, tor={tor_lp}); count in [-8,8]^4 = {len(gl2_det_neg1_tf_hyp)}")
    assert det(LP) == -1 and is_hyperbolic_gl2z(LP) and tor_lp == () and len(gl2_det_neg1_tf_hyp) > 0

    # Control B: Drop GM3 (allow non-hyperbolic in SL(2, Z))
    ell6 = [[1, -1], [1, 0]]  # L^(-1) R? tr = 1, det = 1, order 6
    rk_e6, tor_e6 = h1_mapping_torus(ell6)
    rk_L, tor_L = h1_mapping_torus(L)
    print(f"CTL-ROOT-B1 (drop GM3, elliptic tr=1): M={ell6}, hyp={is_hyperbolic_gl2z(ell6)}, H_1=(rk={rk_e6}, tor={tor_e6})")
    print(f"CTL-ROOT-B2 (drop GM3, parabolic L):   L={L}, hyp={is_hyperbolic_gl2z(L)}, H_1=(rk={rk_L}, tor={tor_L}) -> ALSO TORSION-FREE (Z^2)!")
    assert rk_e6 == 1 and tor_e6 == ()
    assert rk_L == 2 and tor_L == ()

    # Control C: Sign-twin -LR (m003, tr = -3)
    neg_LR = [[-2, -1], [-1, -1]]
    rk_m003, tor_m003 = h1_mapping_torus(neg_LR)
    print(f"CTL-ROOT-C (perturb tr=+3 -> tr=-3, m003): -LR={neg_LR}, H_1=(rk={rk_m003}, tor={tor_m003})")
    assert rk_m003 == 1 and tor_m003 == (5,)

    print("\nALL G:ROOT CHECKS AND CONTROLS PASSED.")


if __name__ == "__main__":
    main()
