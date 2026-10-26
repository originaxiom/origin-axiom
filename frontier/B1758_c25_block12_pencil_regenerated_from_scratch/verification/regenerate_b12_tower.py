"""B1758 (P-301 / R70-1): Regenerate the block-12 pencil (R8, R14, R16, mu, C2, C0, e_, det14) from scratch in exact
rational arithmetic from B854 (without the missing session scratchpad pickle b12_tower.pkl), cross-check modulo splitting
primes (q = 40123, 40493, 40583, 40693), and certify det14(rho) > 0 and e(rho) > 0 at all three real roots of mu(rho)
for THEOREM_LEDGER C25 by three independent exact algebraic methods:
  1. Completing the square over Q: det14(rho) = (9084997258444800000/28561)*(rho + 13/3072)^2 + 2727198720 >= 2727198720 > 0 for ALL real rho.
  2. Exact resultant / minimal polynomial over Q: Res_rho(mu(rho), u - det14(rho)) = -f6(sqrt(-u)) has strictly alternating signs (+, -, +, -), and similarly for e(rho).
  3. Exact rational root-isolation interval arithmetic (Sturm / Collins-Akritas): strictly positive rational lower bounds at all three real roots, matching B893/signature_results.json.
"""
import io, json, pathlib, time
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import GF

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B854 = ROOT / "frontier" / "B854_centralizer_exact" / "e6_centralizer.py"
B893_JSON = ROOT / "frontier" / "B893_omega_vs_measurement" / "signature_results.json"


def build_exact_tower():
    t0 = time.time()
    src = B854.read_text(encoding="utf-8")
    src = src.replace("for _ in range(4000):", "for _ in range(0):")
    old_loop = """for n in [8, 14, 16, 22]:
    P = sp.zeros(n+1, n+1)
    for M in G:
        P += symn(M, n)
    P = sp.simplify(P / 24)
    col = [P.col(j) for j in range(n+1) if any(P.col(j))][0]
    d = sp.lcm([sp.Rational(c).q for c in col]); g = sp.gcd([sp.Rational(c*d).p for c in col])
    Ipoly[n] = [sp.Rational(c*d/g) for c in col]"""
    new_loop = """for n in [8, 14, 16]:
    for k_col in range(n+1):
        col = [sp.Integer(0)] * (n+1)
        for M in G:
            X = M[0,0]*x + M[1,0]*y; Y = M[0,1]*x + M[1,1]*y
            p = sp.Poly(sp.expand(X**(n-k_col)*Y**k_col), x, y)
            for j in range(n+1):
                col[j] += p.coeff_monomial(x**(n-j)*y**j)
        col = [sp.simplify(c / 24) for c in col]
        if any(col):
            break
    d = sp.lcm([sp.Rational(c).q for c in col]); g = sp.gcd([sp.Rational(c*d).p for c in col])
    Ipoly[n] = [sp.Rational(c*d/g) for c in col]"""
    assert old_loop in src
    src = src.replace(old_loop, new_loop)
    src = src.replace("for n in [8, 14, 16, 22]:", "for n in [8, 14, 16]:")
    src = src.split("# ---------------------------------------------------------------- VERIFY closure")[0]

    import contextlib
    env = {}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, "b854_exact", "exec"), env)
    br, hvec, evec, ROOTS, DIM, N, INV = env["br"], env["hvec"], env["evec"], env["ROOTS"], env["DIM"], env["N"], env["INV"]

    def admat_rat(v):
        cols = [br(v, hvec(j) if j < N else evec(ROOTS[j - N])) for j in range(DIM)]
        return sp.Matrix([[sp.Rational(cols[j][i].numerator, cols[j][i].denominator)
                           for j in range(DIM)] for i in range(DIM)])

    G_mat = {n: admat_rat(INV[n]) for n in (8, 14, 16)}

    t_sym = sp.Symbol("t")
    D14 = DomainMatrix.from_Matrix(G_mat[14]).convert_to(sp.QQ)
    p = D14.charpoly()
    P = sp.Poly([sp.Rational(c) for c in p], t_sym)
    r = sp.div(P, sp.gcd(P, P.diff(t_sym)))[0]
    facs = [f for f, _ in sp.factor_list(r)[1] if f.degree() == 6]
    pows = [DomainMatrix.eye(78, sp.QQ)]
    for _ in range(6):
        pows.append(pows[-1] * D14)

    f6 = None
    K_dm = None
    for f in facs:
        cs = f.all_coeffs()[::-1]
        Pf = DomainMatrix.zeros((78, 78), sp.QQ)
        for k, c in enumerate(cs):
            if c:
                Pf = Pf + pows[k].scalarmul(sp.QQ.from_sympy(sp.Rational(c)))
        cand = Pf.nullspace()
        if cand.shape[0] == 12:
            f6 = f
            K_dm = cand
            break
    assert f6 is not None and K_dm is not None

    Nb_dm = K_dm.transpose()
    Nb12 = Nb_dm.to_Matrix()
    pivs = []
    for row_i in range(12):
        for col_j in range(78):
            if Nb12[col_j, row_i] != 0 and all(Nb12[col_j, r2] == 0 for r2 in range(12) if r2 != row_i):
                pivs.append(col_j)
                break
    assert len(pivs) == 12

    def restrict_fast(M_sp):
        M_dm = DomainMatrix.from_Matrix(M_sp).convert_to(sp.QQ)
        MN_dm = M_dm * Nb_dm
        MN = MN_dm.to_Matrix()
        R = sp.Matrix(12, 12, lambda i, j: MN[pivs[i], j] / Nb12[pivs[i], i])
        R_dm = DomainMatrix.from_Matrix(R).convert_to(sp.QQ)
        assert MN_dm == Nb_dm * R_dm, "Exact subspace invariance failed"
        return R

    R8 = restrict_fast(G_mat[8])
    R14 = restrict_fast(G_mat[14])
    R16 = restrict_fast(G_mat[16])
    assert R8 * R14 == R14 * R8 and R8 * R16 == R16 * R8 and R14 * R16 == R16 * R14
    elapsed = time.time() - t0
    return R8, R14, R16, f6, pivs, elapsed


def main():
    log = []
    def say(*a):
        s = " ".join(str(x) for x in a)
        log.append(s)
        print(s, flush=True)

    R8, R14, R16, f6, pivs, elapsed = build_exact_tower()
    say(f"[1] Rebuilt exact 12x12 block-12 operators R8, R14, R16 from B854 in {elapsed:.2f}s")
    say(f"    f6(t) = {f6.as_expr()}")

    rho, t, u = sp.symbols("rho t u")
    MU_coeffs = [sp.Rational(500716339200), sp.Rational(-2075673600), sp.Rational(-4769856), sp.Rational(2197)]
    mu_poly = sp.Poly(sum(c * rho**(3 - k) for k, c in enumerate(MU_coeffs)), rho)
    mum = mu_poly.monic()

    # Check det(R8 + rho*R16) == c * mu(rho)^4 on block 12
    c2m, c1m, c0m = mum.all_coeffs()[1], mum.all_coeffs()[2], mum.all_coeffs()[3]
    CMP = sp.Matrix([[0, 0, -c0m], [1, 0, -c1m], [0, 1, -c2m]])
    ID3 = sp.eye(3)

    def blow36(M12, A3=ID3):
        out = sp.zeros(36, 36)
        for i in range(12):
            for j in range(12):
                if M12[i, j] != 0:
                    blk = M12[i, j] * A3
                    for a in range(3):
                        for b in range(3):
                            out[3*i + a, 3*j + b] = blk[a, b]
        return out

    Mblow = blow36(R8, ID3) + blow36(R16, CMP)
    K_dm = DomainMatrix.from_Matrix(Mblow).convert_to(sp.QQ).nullspace()
    assert K_dm.shape == (12, 36)
    W36_dm = K_dm.transpose()
    W36 = W36_dm.to_Matrix()
    pivs36 = []
    for col_i in range(12):
        for row_j in range(36):
            if W36[row_j, col_i] != 0 and all(W36[row_j, c2] == 0 for c2 in range(12) if c2 != col_i):
                pivs36.append(row_j)
                break
    assert len(pivs36) == 12

    def restrict_W36(M36):
        M_dm = DomainMatrix.from_Matrix(M36).convert_to(sp.QQ)
        MW_dm = M_dm * W36_dm
        MW = MW_dm.to_Matrix()
        R = sp.Matrix(12, 12, lambda i, j: MW[pivs36[i], j] / W36[pivs36[i], i])
        assert MW_dm == W36_dm * DomainMatrix.from_Matrix(R).convert_to(sp.QQ)
        return R

    Rho_W = restrict_W36(blow36(sp.eye(12), CMP))
    W14_Q = restrict_W36(blow36(R14, ID3))
    W16_Q = restrict_W36(blow36(R16, ID3))

    G_tr = sp.Matrix(3, 3, lambda i, j: (CMP**(i + j)).trace())
    G_tr_inv = G_tr.inv()

    def tr_F(T_Q):
        rhs = sp.Matrix(3, 1, lambda i, _: ((Rho_W**i) * T_Q).trace())
        coeffs = G_tr_inv * rhs
        return coeffs[0] + coeffs[1]*rho + coeffs[2]*rho**2

    def mul_F(p1, p2):
        return sp.rem(sp.Poly(p1 * p2, rho), mum).as_expr()

    assert tr_F(sp.eye(12)) == 4 and tr_F(Rho_W) == 4 * rho
    assert tr_F(W16_Q) == 0 and tr_F(W16_Q**3) == 0
    assert tr_F(W14_Q) == 0 and tr_F(W14_Q**3) == 0

    p2_16, p4_16 = tr_F(W16_Q**2), tr_F(W16_Q**4)
    C2_poly = -sp.Rational(1, 2) * p2_16
    C0_poly = sp.Rational(1, 4) * (2 * mul_F(C2_poly, C2_poly) - p4_16)
    disc_16 = sp.simplify(mul_F(C2_poly, C2_poly) - 4 * C0_poly)
    e_poly = -sp.Rational(1, 2) * C2_poly
    assert disc_16 == 0

    p2_14, p4_14 = tr_F(W14_Q**2), tr_F(W14_Q**4)
    C2_14 = -sp.Rational(1, 2) * p2_14
    C0_14 = sp.Rational(1, 4) * (2 * mul_F(C2_14, C2_14) - p4_14)
    disc_14 = sp.simplify(mul_F(C2_14, C2_14) - 4 * C0_14)
    det14_poly = sp.Rational(1, 2) * C2_14
    assert disc_14 == 0 and sp.simplify(mul_F(det14_poly, det14_poly) - C0_14) == 0

    # Verify W16^2 == e(rho)*I_4 identically on W_4 and tr_F(W16*W14) == tr_F(W16*W14^2) == 0 (zero gamma-part of det14)
    e_mat = (sp.Poly(e_poly, rho).coeff_monomial(1)*sp.eye(12)
             + sp.Poly(e_poly, rho).coeff_monomial(rho)*Rho_W
             + sp.Poly(e_poly, rho).coeff_monomial(rho**2)*(Rho_W**2))
    semisimple_16 = (W16_Q**2 == e_mat)
    tr_16_14 = tr_F(W16_Q * W14_Q)
    tr_16_14sq = tr_F(W16_Q * (W14_Q**2))
    assert semisimple_16 and tr_16_14 == 0 and tr_16_14sq == 0

    say(f"[2] Extracted exact F = Q[rho]/mu(rho) polynomials on W_4 = ker(R8 + rho*R16):")
    say(f"    C2(rho)    = {C2_poly}")
    say(f"    C0(rho)    = {C0_poly}")
    say(f"    e(rho)     = {e_poly}")
    say(f"    det14(rho) = {det14_poly}")
    say(f"    C2^2 - 4*C0 == 0: True | W16^2 == e(rho)*I_4: {semisimple_16} | gamma-part of det14 == 0: True")

    # Proof 1: Completing the square for det14(rho)
    p_det = sp.Poly(det14_poly, rho)
    A, B, C = p_det.coeff_monomial(rho**2), p_det.coeff_monomial(rho), p_det.coeff_monomial(1)
    vertex = -B / (2 * A)
    global_min = C - B**2 / (4 * A)
    disc_quad = B**2 - 4 * A * C
    assert A > 0 and global_min == sp.Integer(2727198720) and disc_quad < 0
    assert sp.expand(A * (rho - vertex)**2 + global_min - det14_poly) == 0
    say(f"[3] Proof 1 (Completing the square over Q):")
    say(f"    det14(rho) = ({A}) * (rho + {-vertex})^2 + {global_min}")
    say(f"    Quadratic discriminant B^2 - 4AC = {disc_quad} < 0 => det14(rho) >= {global_min} > 0 for ALL real rho!")

    # Proof 2: Exact Resultant / Minimal Polynomials over Q
    minpoly_det14 = sp.Poly(sp.resultant(mu_poly.as_expr(), u - det14_poly, rho), u).monic()
    minpoly_e = sp.Poly(sp.resultant(mu_poly.as_expr(), u - e_poly, rho), u).monic()
    f6_coeffs = f6.all_coeffs()  # [1, 0, c4, 0, c2, 0, c0]
    f6_neg_u = sp.Poly(u**3 - f6_coeffs[2]*u**2 + f6_coeffs[4]*u - f6_coeffs[6], u)
    assert minpoly_det14.all_coeffs() == [1, -f6_coeffs[2], f6_coeffs[4], -f6_coeffs[6]]
    c_det = minpoly_det14.all_coeffs()
    c_e = minpoly_e.all_coeffs()
    assert c_det[0] > 0 and c_det[1] < 0 and c_det[2] > 0 and c_det[3] < 0
    assert c_e[0] > 0 and c_e[1] < 0 and c_e[2] > 0 and c_e[3] < 0
    say(f"[4] Proof 2 (Exact Resultant / Minimal Polynomials over Q):")
    say(f"    minpoly(det14) = {minpoly_det14.as_expr()} == -f6(sqrt(-u)): True (signs +, -, +, -)")
    say(f"    minpoly(e)     = {minpoly_e.as_expr()} (signs +, -, +, -)")

    # Proof 3: Exact Rational Interval Arithmetic (Sturm / Collins-Akritas) & B893 comparison
    b893 = json.loads(B893_JSON.read_text(encoding="utf-8"))
    ivs = mu_poly.intervals(eps=sp.Rational(1, 10**25))
    assert len(ivs) == 3
    interval_certs = []
    say(f"[5] Proof 3 (Exact Rational Root-Isolation Intervals eps=10^-25 & B893 comparison):")
    for idx, ((lo, hi), _) in enumerate(ivs):
        assert lo < hi
        # Monotonicity or interval evaluation of A*rho^2 + B*rho + C and e(rho) on [lo, hi]
        # Since vertex = -13/3072 = -0.00423177... < lo for all 3 roots (lo >= -0.001938...), det14 is strictly increasing on [lo, hi]!
        assert hi < vertex or vertex < lo
        d_a, d_b = sp.Rational(det14_poly.subs(rho, lo)), sp.Rational(det14_poly.subs(rho, hi))
        det_lo, det_hi = min(d_a, d_b), max(d_a, d_b)
        assert 0 < det_lo < det_hi
        # For e(rho) = e2*rho^2 + e1*rho + e0 with e2 < 0, concave down, so min on [lo, hi] is min(e(lo), e(hi))
        e_lo = max(sp.Rational(e_poly.subs(rho, lo)), sp.Rational(0)) if False else min(sp.Rational(e_poly.subs(rho, lo)), sp.Rational(e_poly.subs(rho, hi)))
        e_hi = max(sp.Rational(e_poly.subs(rho, lo)), sp.Rational(e_poly.subs(rho, hi)))
        assert 0 < e_lo < e_hi
        b_det14 = b893["det14_at_roots"][idx]
        rel_err_det = abs(float(det_lo) - b_det14) / b_det14
        assert rel_err_det < 1e-12
        say(f"    root {idx}: rho in [{float(lo):.16e}, {float(hi):.16e}] (width {float(hi-lo):.2e})")
        say(f"      det14(rho) > {float(det_lo):.10f} > 0 (B893: {b_det14}, rel_diff={rel_err_det:.2e})")
        say(f"      e(rho)     > {float(e_lo):.10f} > 0")
        interval_certs.append({
            "root_index": idx,
            "rho_lo_float": float(lo),
            "rho_hi_float": float(hi),
            "det14_lower_bound_float": float(det_lo),
            "det14_upper_bound_float": float(det_hi),
            "det14_positive_exact": bool(det_lo > 0),
            "e_lower_bound_float": float(e_lo),
            "e_upper_bound_float": float(e_hi),
            "e_positive_exact": bool(e_lo > 0),
            "b893_det14": b_det14,
            "rel_diff_det14": rel_err_det,
        })

    # Modular cross-checks at q = 40123, 40493, 40583, 40693
    mod_checks = {}
    for q in (40123, 40493, 40583, 40693):
        rts_q = sorted(int(x) % q for x in sp.Poly(mu_poly.as_expr(), rho, modulus=q).ground_roots())
        rows_q = []
        for rq in rts_q:
            eq_rat = sp.Rational(e_poly.subs(rho, rq))
            dq_rat = sp.Rational(det14_poly.subs(rho, rq))
            eq = (eq_rat.p % q) * pow(eq_rat.q % q, -1, q) % q
            dq = (dq_rat.p % q) * pow(dq_rat.q % q, -1, q) % q
            gq = sorted(int(x) for x in sp.sqrt_mod(eq, q, all_roots=True))
            aq = sorted(int(x) for x in sp.sqrt_mod((-dq) % q, q, all_roots=True))
            rows_q.append({"rq": rq, "e_q": eq, "gamma_q": gq, "det14_q": dq, "a_q": aq})
        mod_checks[str(q)] = rows_q
    assert any(r["rq"] == 27063 and 13410 in r["gamma_q"] and 2675 in r["a_q"] for r in mod_checks["40123"])
    say(f"[6] Modular cross-check at q = 40123 reproduces B892's (rq, gamma_q, a_q) = (27063, 13410, 2675): True")

    out = {
        "arc": "B1758",
        "point_register": "P-301",
        "theorem_ledger": "C25",
        "elapsed_seconds": elapsed,
        "f6": str(f6.as_expr()),
        "mu": str(mu_poly.as_expr()),
        "C2_rho": str(C2_poly),
        "C0_rho": str(C0_poly),
        "e_rho": str(e_poly),
        "det14_rho": str(det14_poly),
        "completing_the_square": {
            "A": str(A),
            "B": str(B),
            "C": str(C),
            "vertex": str(vertex),
            "global_min": int(global_min),
            "discriminant": str(disc_quad),
            "strictly_positive_for_all_real_rho": True,
        },
        "resultants": {
            "minpoly_det14": str(minpoly_det14.as_expr()),
            "equals_neg_f6_sqrt_neg_u": True,
            "minpoly_e": str(minpoly_e.as_expr()),
            "all_signs_alternating": True,
        },
        "galois_invariance_b906": {
            "W16_sq_equals_e_I4": True,
            "tr_F_W16_W14": 0,
            "tr_F_W16_W14sq": 0,
            "gamma_part_of_det14_zero": True,
        },
        "interval_certifications": interval_certs,
        "modular_checks": mod_checks,
        "R8": [[str(R8[i, j]) for j in range(12)] for i in range(12)],
        "R14": [[str(R14[i, j]) for j in range(12)] for i in range(12)],
        "R16": [[str(R16[i, j]) for j in range(12)] for i in range(12)],
    }
    json.dump(out, open(HERE / "b12_tower_regenerated.json", "w"), indent=1)
    (HERE / "regenerate_b12_tower_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")
    say("DONE")


if __name__ == "__main__":
    main()
