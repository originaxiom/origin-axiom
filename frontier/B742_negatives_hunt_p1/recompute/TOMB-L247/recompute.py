#!/usr/bin/env python3
"""B739 Stage-B recompute -- TOMB-L247 (tombstone K-J, speculations/TOMBSTONES.md:L247).

Banked claim killed (K-J): "phi^2 is the degenerate-block (phi_{2,1}) torus-block
monodromy multiplier of the seed", with a '3 = 3' numerical confirmation.

Banked discriminating fact (fact_basis: asserted -- never computed in the arc):
  "The degenerate (phi_{2,1}) torus block is reducible (kappa = 2); the seed is
   irreducible (kappa > 2). They are different points of the character variety.
   The apparent '3 = 3' confirmation was an artifact -- an eigenvalue-trace
   compared against a commutator-trace (different quantities)."

This script RE-DERIVES that fact as an actual computation (E19: compute-not-cite).

DECLARED CONVENTIONS (E1 -- the arc left these implicit):
  C1. Once-punctured torus: pi_1 = F_2 = <a,b>, puncture/boundary class = [a,b].
      SL(2,C) character variety in full-trace Fricke coordinates
      (X,Y,Z) = (tr A, tr B, tr AB); the commutator/puncture trace is the
      regular function  kappa = tr[A,B] = X^2 + Y^2 + Z^2 - XYZ - 2.
      "kappa" is the tombstone's commutator parameter (K-N: kappa_m = m^2+2,
      golden kappa_1 = 3, silver kappa_2 = 6 -- reproduced below).
  C2. The seed = the golden (m=1) member of the repo's metallic family:
      rho(a) = L = [[1,0],[1,1]], rho(b) = R^m = [[1,m],[0,1]] with m=1;
      seed word rho(ab) = L*R (trace 3, eigenvalues phi^{+-2}; conjugate to the
      B13 seed matrix [[2,1],[1,1]]).
  C3. "Degenerate (phi_{2,1}) torus-block monodromy" = the SL(2,C) monodromy of
      the rank-2 local system defined by the level-2 null-vector (BPZ) ODE of a
      phi_{2,1} insertion on the torus, taken at fixed modulus tau in the
      classical/oper normal form: the n=1 Lame oper
          psi''(z) = (2 P(z|tau) + E) psi(z),   P = Weierstrass p-function,
      accessory parameter E arbitrary (the block family sweeps it). The word
      "multiplier" in the killed claim is the Floquet-Hermite multiplier of
      exactly this equation. The character variety in C1 is the classical
      monodromy space the tombstone's kill sentence refers to.
  C4. Fixed generic numerical parameters (deterministic, declared):
      tau = 0.31 + 1.27i (generic lattice), a = 0.29 + 0.41*tau (Hermite
      parameter, E = P(a)), base point z0 = 0.171 + 0.213*tau for the direct
      path-integrated monodromy. The kappa_block = 2 conclusion is
      parameter-uniform: the symbolic parts [S1a]/[S1b] cover every reducible
      (incl. Jordan-triangular) case, so genericity of (tau, a) is not
      load-bearing for the verdict.

Deterministic: no wall-clock, no randomness, no network. sympy + mpmath only.
"""

import sympy as sp
import mpmath as mp

BAR = "=" * 78


def check(label, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"    [{status}] {label}" + (f"  {detail}" if detail else ""))
    if not ok:
        raise AssertionError(f"{label}: FAILED {detail}")


def ns(x, n=20):
    return mp.nstr(x, n)


# ---------------------------------------------------------------------------
# [S1] SYMBOLIC (sympy, exact)
# ---------------------------------------------------------------------------
def s1_symbolic():
    print(BAR)
    print("[S1] SYMBOLIC (sympy, exact arithmetic)")
    print(BAR)

    # --- [S1a] Reducible => kappa = 2, identically. -----------------------
    # A reducible pair fixes a common line; conjugating that line to e_1 makes
    # both matrices upper triangular (trace is conjugation invariant), so the
    # generic upper-triangular SL(2) pair covers ALL reducible pairs,
    # including Jordan/parabolic ones.
    al, be, ga, de = sp.symbols("alpha beta gamma delta", nonzero=True)
    A = sp.Matrix([[al, be], [0, 1 / al]])
    B = sp.Matrix([[ga, de], [0, 1 / ga]])
    kappa_red = sp.simplify((A * B * A.inv() * B.inv()).trace())
    print(f"\n[S1a] generic upper-triangular SL(2) pair: tr[A,B] = {kappa_red}")
    check("reducible pair => kappa = tr[A,B] = 2 identically", kappa_red == 2)

    # --- [S1b] Same fact in Fricke coordinates for diagonal pairs. --------
    p, s = sp.symbols("p s", nonzero=True)
    X = p + 1 / p
    Y = s + 1 / s
    Z = p * s + 1 / (p * s)
    kappa_diag = sp.simplify(X**2 + Y**2 + Z**2 - X * Y * Z - 2)
    print(f"[S1b] diagonal pair diag(p,1/p), diag(s,1/s): "
          f"X^2+Y^2+Z^2-XYZ-2 = {kappa_diag}")
    check("diagonal pair => Fricke kappa = 2 identically", kappa_diag == 2)

    # --- [S1c] The '3 = 3' artifact, block side, exact. -------------------
    # Even if the block multiplier is TUNED to phi^2 exactly, the cycle
    # monodromy diag(phi^2, phi^-2) has eigenvalue-trace 3 while the
    # commutator-trace (the character-variety discriminant kappa) stays 2.
    phi = (1 + sp.sqrt(5)) / 2
    MA = sp.diag(phi**2, phi**-2)
    trMA = sp.simplify(MA.trace())
    MB = sp.diag(s, 1 / s)
    comm = sp.simplify(MA * MB * MA.inv() * MB.inv())
    print(f"[S1c] block cycle monodromy diag(phi^2, phi^-2): "
          f"eigenvalue-trace = phi^2 + phi^-2 = {trMA}")
    check("phi^2 + phi^-2 = 3 (exact)", sp.simplify(trMA - 3) == 0)
    check("[diag(phi^2,phi^-2), any diag] = identity => kappa = 2, never 3",
          comm == sp.eye(2))

    # --- [S1d] The seed, exact. ------------------------------------------
    L = sp.Matrix([[1, 0], [1, 1]])
    R = sp.Matrix([[1, 1], [0, 1]])
    W = L * R                                   # seed word rho(ab)
    K = L * R * L.inv() * R.inv()               # puncture holonomy rho([a,b])
    trW = W.trace()
    trK = K.trace()
    lam = sp.symbols("lam")
    eigs = sp.solve(sp.Eq(W.charpoly(lam).as_expr(), 0), lam)
    print(f"\n[S1d] seed: L={L.tolist()}, R={R.tolist()}")
    print(f"      word LR = {W.tolist()},  tr(LR) = {trW}")
    print(f"      commutator [L,R] = {K.tolist()},  tr[L,R] = {trK}")
    print(f"      eigenvalues of LR: {eigs}")
    check("word-trace tr(LR) = 3", trW == 3)
    check("commutator-trace kappa_seed = tr[L,R] = 3", trK == 3)
    check("largest eigenvalue of the seed word = phi^2 (exact)",
          any(sp.simplify(e - phi**2) == 0 for e in eigs))
    Xs, Ys, Zs = L.trace(), R.trace(), trW
    fricke = Xs**2 + Ys**2 + Zs**2 - Xs * Ys * Zs - 2
    print(f"      Fricke check: ({Xs})^2+({Ys})^2+({Zs})^2"
          f"-({Xs})({Ys})({Zs})-2 = {fricke}")
    check("Fricke polynomial reproduces kappa_seed = 3", fricke == trK)
    check("kappa_seed = 3 != 2  => seed character is NOT on the reducible locus",
          trK != 2)
    # Irreducibility, directly: invariant lines of L are its eigenlines, ditto R.
    evL = L.eigenvects()
    evR = R.eigenvects()
    vL = evL[0][2][0]
    vR = evR[0][2][0]
    print(f"      eigenlines: L -> span{vL.T.tolist()} (geom mult "
          f"{len(evL[0][2])}), R -> span{vR.T.tolist()} (geom mult {len(evR[0][2])})")
    check("L has a single eigenline", len(evL) == 1 and len(evL[0][2]) == 1)
    check("R has a single eigenline", len(evR) == 1 and len(evR[0][2]) == 1)
    check("no common eigenline => the seed pair is IRREDUCIBLE",
          sp.Matrix.hstack(vL, vR).det() != 0)
    # Why '3 = 3' looked like a confirmation: at m=1 the commutator is
    # conjugate to the seed word itself (same char poly t^2 - 3t + 1).
    cpW = W.charpoly(lam).as_expr()
    cpK = K.charpoly(lam).as_expr()
    print(f"      charpoly(LR) = {cpW},  charpoly([L,R]) = {cpK}")
    check("m=1 accident: charpoly(word) == charpoly(commutator)",
          sp.expand(cpW - cpK) == 0)

    # --- [S1e] Metallic control (the MB6 control the session skipped). ----
    m = sp.symbols("m")
    Rm = sp.Matrix([[1, m], [0, 1]])
    tr_word = sp.expand((L * Rm).trace())
    tr_comm = sp.expand((L * Rm * L.inv() * Rm.inv()).trace())
    sols = sp.solve(sp.Eq(tr_word, tr_comm), m)
    print(f"\n[S1e] metallic family: eigenvalue-trace tr(L R^m) = {tr_word}, "
          f"commutator-trace tr[L,R^m] = {tr_comm}")
    print("      m : (word-trace, commutator-trace)")
    for mv in range(1, 6):
        print(f"      {mv} : ({tr_word.subs(m, mv)}, {tr_comm.subs(m, mv)})")
    check("tr(L R^m) = m + 2 (eigenvalue-trace)",
          sp.expand(tr_word - (m + 2)) == 0)
    check("tr[L,R^m] = m^2 + 2 (commutator-trace; K-N's kappa_m)",
          sp.expand(tr_comm - (m**2 + 2)) == 0)
    check("the two traces coincide ONLY at m in {0,1}", sorted(sols) == [0, 1],
          f"solutions: {sols}")
    return trK  # kappa_seed = 3, exact


# ---------------------------------------------------------------------------
# Weierstrass machinery from theta functions (periods 1 and tau)
# ---------------------------------------------------------------------------
def build_weierstrass(tau):
    """sigma, zeta, P for the lattice Z + tau*Z at the CURRENT mp precision.

    sigma(z) = exp(eta1 z^2) theta1(pi z)/(pi theta1'(0)),
    zeta = sigma'/sigma, P = -zeta'  (exact identities of this construction),
    eta1 = -(pi^2/6) theta1'''(0)/theta1'(0)  (kills the z-linear term of zeta,
    i.e. enforces the Weierstrass normalization zeta = 1/z + O(z^3)).
    """
    q = mp.exp(1j * mp.pi * tau)
    th = lambda u, d=0: mp.jtheta(1, u, q, d)
    t1p0 = th(0, 1)
    eta1 = -mp.pi**2 / 6 * th(0, 3) / t1p0

    def sigma(z):
        return mp.exp(eta1 * z**2) * th(mp.pi * z) / (mp.pi * t1p0)

    def zeta(z):
        return 2 * eta1 * z + mp.pi * th(mp.pi * z, 1) / th(mp.pi * z)

    def wp(z):
        t0, t1, t2 = th(mp.pi * z), th(mp.pi * z, 1), th(mp.pi * z, 2)
        return -2 * eta1 - mp.pi**2 * (t2 * t0 - t1**2) / t0**2

    eta2 = zeta(tau / 2)
    return sigma, zeta, wp, eta1, eta2


# ---------------------------------------------------------------------------
# [S2] NUMERIC: the degenerate-block (n=1 Lame) monodromy, closed form
# ---------------------------------------------------------------------------
def s2_block_monodromy_hermite(tau_str=("0.31", "1.27")):
    mp.mp.dps = 60
    tau = mp.mpc(*tau_str)
    sigma, zeta, wp, eta1, eta2 = build_weierstrass(tau)
    print(BAR)
    print("[S2] NUMERIC: degenerate phi_{2,1} block = n=1 Lame oper "
          "psi'' = (2P(z)+E) psi")
    print(f"     lattice Z + tau Z, tau = {ns(tau)}   (mp.dps = {mp.mp.dps})")
    print(BAR)

    # --- [S2a] implementation self-checks ---------------------------------
    print("\n[S2a] Weierstrass implementation self-checks")
    z_small = mp.mpf("1e-8")
    check("sigma(z)/z -> 1 near 0", abs(sigma(z_small) / z_small - 1) < mp.mpf("1e-12"),
          f"|sigma(z)/z - 1| = {ns(abs(sigma(z_small)/z_small - 1), 5)} at z=1e-8")
    check("zeta(z) - 1/z -> 0 near 0 (no linear term: Weierstrass normalization)",
          abs(zeta(z_small) - 1 / z_small) < mp.mpf("1e-20"),
          f"residual = {ns(abs(zeta(z_small) - 1/z_small), 5)}")
    z_small2 = mp.mpf("1e-6")
    check("P(z) - 1/z^2 -> 0 near 0", abs(wp(z_small2) - 1 / z_small2**2) < mp.mpf("1e-6"),
          f"residual = {ns(abs(wp(z_small2) - 1/z_small2**2), 5)}")
    zt = mp.mpf("0.23") + mp.mpf("0.31") * tau
    check("P is elliptic: P(z+1) = P(z)", abs(wp(zt + 1) - wp(zt)) < mp.mpf("1e-45"),
          f"dev = {ns(abs(wp(zt+1)-wp(zt)), 5)}")
    check("P is elliptic: P(z+tau) = P(z)", abs(wp(zt + tau) - wp(zt)) < mp.mpf("1e-45"),
          f"dev = {ns(abs(wp(zt+tau)-wp(zt)), 5)}")
    check("quasi-period consistency: zeta(tau/2) = eta1*tau - i*pi  (Legendre)",
          abs(eta2 - (eta1 * tau - 1j * mp.pi)) < mp.mpf("1e-45"),
          f"dev = {ns(abs(eta2 - (eta1*tau - 1j*mp.pi)), 5)}")
    # derivative identities, verified by central differences (h^2 + roundoff)
    h = mp.mpf("1e-20")
    d_sig = (sigma(zt + h) - sigma(zt - h)) / (2 * h * sigma(zt))
    check("sigma'/sigma = zeta (numerical differentiation)",
          abs(d_sig - zeta(zt)) < mp.mpf("1e-30"),
          f"dev = {ns(abs(d_sig - zeta(zt)), 5)}")
    d_zeta = (zeta(zt + h) - zeta(zt - h)) / (2 * h)
    check("zeta' = -P (numerical differentiation)",
          abs(d_zeta + wp(zt)) < mp.mpf("1e-30"),
          f"dev = {ns(abs(d_zeta + wp(zt)), 5)}")

    # --- [S2b] Hermite solutions solve the Lame oper -----------------------
    a = mp.mpf("0.29") + mp.mpf("0.41") * tau
    E = wp(a)
    za = zeta(a)
    print(f"\n[S2b] Hermite solutions psi_pm(z) = exp(-+zeta(a) z) sigma(z+-a)/sigma(z)")
    print(f"      a = {ns(a)}   E = P(a) = {ns(E)}")
    psi_p = lambda z: mp.exp(-za * z) * sigma(z + a) / sigma(z)
    psi_m = lambda z: mp.exp(+za * z) * sigma(z - a) / sigma(z)
    # closed-form ODE residual: psi''/psi - (2P(z)+E)
    #   = (zeta(z+-a) - zeta(z) -+ zeta(a))^2 - (P(z) + P(a) + P(z+-a))
    res_p = lambda z: (zeta(z + a) - zeta(z) - za)**2 - (wp(z) + wp(a) + wp(z + a))
    res_m = lambda z: (zeta(z - a) - zeta(z) + za)**2 - (wp(z) + wp(a) + wp(z - a))
    zs = [mp.mpf("0.13") + mp.mpf("0.17") * tau,
          mp.mpf("0.57") + mp.mpf("0.33") * tau,
          mp.mpf("-0.22") + mp.mpf("0.41") * tau,
          mp.mpf("0.35") - mp.mpf("0.27") * tau]
    worst = max(max(abs(res_p(z)) for z in zs), max(abs(res_m(z)) for z in zs))
    print(f"      max |psi''/psi - (2P+E)| over 4 sample z, both solutions: {ns(worst, 5)}")
    check("psi_+ and psi_- solve psi'' = (2P(z)+E) psi", worst < mp.mpf("1e-40"))
    # linear independence: Wronskian (constant for a psi''=V psi equation)
    g_p = lambda z: zeta(z + a) - zeta(z) - za
    g_m = lambda z: zeta(z - a) - zeta(z) + za
    wr = lambda z: psi_p(z) * psi_m(z) * (g_m(z) - g_p(z))
    w0, w1 = wr(zs[0]), wr(zs[1])
    check("Wronskian nonzero and constant => (psi_+, psi_-) is a BASIS",
          abs(w0) > mp.mpf("1e-6") and abs(w0 - w1) < mp.mpf("1e-40"),
          f"W = {ns(w0)}")

    # --- [S2c] the monodromy is DIAGONAL in this basis => reducible --------
    print("\n[S2c] cycle monodromies measured as ratios psi(z+period)/psi(z)")
    rA_p = [psi_p(z + 1) / psi_p(z) for z in zs]
    rA_m = [psi_m(z + 1) / psi_m(z) for z in zs]
    rB_p = [psi_p(z + tau) / psi_p(z) for z in zs]
    rB_m = [psi_m(z + tau) / psi_m(z) for z in zs]
    devs = []
    for r in (rA_p, rA_m, rB_p, rB_m):
        devs.append(max(abs(r[i] - r[0]) for i in range(1, len(r))))
    print(f"      max z-dependence of the four ratios: {ns(max(devs), 5)}")
    check("each psi_pm is an EIGENVECTOR of both period translations "
          "(ratios independent of z)", max(devs) < mp.mpf("1e-40"))
    rhoA_p, rhoA_m, rhoB_p, rhoB_m = rA_p[0], rA_m[0], rB_p[0], rB_m[0]
    pred_A = mp.exp(2 * eta1 * a - za)
    pred_B = mp.exp(2 * eta2 * a - za * tau)
    print(f"      A-cycle multipliers: rho_A+ = {ns(rhoA_p)}")
    print(f"                           rho_A- = {ns(rhoA_m)}")
    print(f"      B-cycle multipliers: rho_B+ = {ns(rhoB_p)}")
    print(f"                           rho_B- = {ns(rhoB_m)}")
    check("closed form rho_A+ = exp(2 eta1 a - zeta(a))",
          abs(rhoA_p - pred_A) < mp.mpf("1e-40"), f"dev = {ns(abs(rhoA_p - pred_A), 5)}")
    check("closed form rho_B+ = exp(2 zeta(tau/2) a - zeta(a) tau)",
          abs(rhoB_p - pred_B) < mp.mpf("1e-40"), f"dev = {ns(abs(rhoB_p - pred_B), 5)}")
    check("SL(2): rho_A+ rho_A- = 1", abs(rhoA_p * rhoA_m - 1) < mp.mpf("1e-40"))
    check("SL(2): rho_B+ rho_B- = 1", abs(rhoB_p * rhoB_m - 1) < mp.mpf("1e-40"))
    check("multipliers distinct (honest 2-dim diagonalization, non-scalar)",
          abs(rhoA_p - rhoA_m) > mp.mpf("1e-3"))

    # --- [S2d] kappa of the block ------------------------------------------
    MA = mp.matrix([[rhoA_p, 0], [0, rhoA_m]])
    MB = mp.matrix([[rhoB_p, 0], [0, rhoB_m]])
    C = MA * MB * MA**-1 * MB**-1
    kappa_block = C[0, 0] + C[1, 1]
    Xn = MA[0, 0] + MA[1, 1]
    Yn = MB[0, 0] + MB[1, 1]
    Zn = rhoA_p * rhoB_p + rhoA_m * rhoB_m
    fricke_n = Xn**2 + Yn**2 + Zn**2 - Xn * Yn * Zn - 2
    print(f"\n[S2d] M_A, M_B diagonal => [M_A,M_B] = I exactly; "
          f"kappa_block = tr[M_A,M_B] = {ns(kappa_block)}")
    print(f"      Fricke check on the block character: "
          f"X^2+Y^2+Z^2-XYZ-2 = {ns(fricke_n)}")
    check("kappa_block = 2", abs(kappa_block - 2) < mp.mpf("1e-50"))
    check("block Fricke kappa = 2", abs(fricke_n - 2) < mp.mpf("1e-38"),
          f"dev = {ns(abs(fricke_n - 2), 5)}")
    return tau_str


# ---------------------------------------------------------------------------
# [S3] NUMERIC cross-check: direct path-integrated monodromy (no closed forms)
# ---------------------------------------------------------------------------
def s3_block_monodromy_direct(tau_str, N=2000):
    mp.mp.dps = 35
    tau = mp.mpc(*tau_str)
    sigma, zeta, wp, eta1, eta2 = build_weierstrass(tau)
    a = mp.mpf("0.29") + mp.mpf("0.41") * tau
    E = wp(a)
    za = zeta(a)
    z0 = mp.mpf("0.171") + mp.mpf("0.213") * tau
    print(BAR)
    print("[S3] NUMERIC cross-check: monodromy by direct RK4 transport of "
          "psi'' = (2P+E) psi")
    print(f"     base point z0 = {ns(z0, 12)}, fixed steps N = {N} per loop "
          f"(mp.dps = {mp.mp.dps})")
    print(BAR)

    V = lambda z: 2 * wp(z) + E

    def transport(P):
        """Fundamental 2x2 transfer matrix for (psi, psi') along z0 + t*P, t:0->1."""
        hstep = mp.mpf(1) / N
        Y = mp.matrix([[1, 0], [0, 1]])

        def F(vz, Y):
            # d/dt (psi, psi') = P * [[0,1],[V,0]] (psi, psi')
            return P * mp.matrix([[Y[1, 0], Y[1, 1]],
                                  [vz * Y[0, 0], vz * Y[0, 1]]])

        v_t = V(z0)
        for k in range(N):
            t = k * hstep
            v_mid = V(z0 + (t + hstep / 2) * P)
            v_end = V(z0 + (t + hstep) * P)
            k1 = F(v_t, Y)
            k2 = F(v_mid, Y + (hstep / 2) * k1)
            k3 = F(v_mid, Y + (hstep / 2) * k2)
            k4 = F(v_end, Y + hstep * k3)
            Y = Y + (hstep / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            v_t = v_end
        return Y

    TA = transport(mp.mpc(1))
    TB = transport(tau)
    detA = TA[0, 0] * TA[1, 1] - TA[0, 1] * TA[1, 0]
    detB = TB[0, 0] * TB[1, 1] - TB[0, 1] * TB[1, 0]
    trA = TA[0, 0] + TA[1, 1]
    trB = TB[0, 0] + TB[1, 1]
    rhoA_p = mp.exp(2 * eta1 * a - za)
    rhoB_p = mp.exp(2 * eta2 * a - za * tau)
    print(f"\n      det T_A - 1 = {ns(abs(detA - 1), 5)},  "
          f"det T_B - 1 = {ns(abs(detB - 1), 5)}")
    print(f"      tr T_A = {ns(trA)}")
    print(f"      Hermite prediction rho_A+ + rho_A- = {ns(rhoA_p + 1/rhoA_p)}")
    print(f"      tr T_B = {ns(trB)}")
    print(f"      Hermite prediction rho_B+ + rho_B- = {ns(rhoB_p + 1/rhoB_p)}")
    check("det T_A = det T_B = 1 (SL(2))",
          abs(detA - 1) < mp.mpf("1e-8") and abs(detB - 1) < mp.mpf("1e-8"))
    check("tr T_A matches the Hermite multipliers",
          abs(trA - (rhoA_p + 1 / rhoA_p)) < mp.mpf("1e-8"),
          f"dev = {ns(abs(trA - (rhoA_p + 1/rhoA_p)), 5)}")
    check("tr T_B matches the Hermite multipliers",
          abs(trB - (rhoB_p + 1 / rhoB_p)) < mp.mpf("1e-8"),
          f"dev = {ns(abs(trB - (rhoB_p + 1/rhoB_p)), 5)}")

    C = TA * TB * TA**-1 * TB**-1
    kappa = C[0, 0] + C[1, 1]
    devI = max(abs(C[i, j] - (1 if i == j else 0)) for i in range(2) for j in range(2))
    print(f"\n      commutator [T_A,T_B]: max|C - I| = {ns(devI, 5)}")
    print(f"      kappa_block = tr[T_A,T_B] = {ns(kappa)}")
    check("[T_A,T_B] = I (trivial puncture monodromy: phi_{2,1} degeneracy)",
          devI < mp.mpf("1e-6"))
    check("kappa_block = tr[T_A,T_B] = 2 (independent of the Hermite ansatz)",
          abs(kappa - 2) < mp.mpf("1e-6"), f"|kappa - 2| = {ns(abs(kappa - 2), 5)}")

    # common invariant lines: eigenlines of T_A are eigenlines of T_B too
    disc = mp.sqrt(trA**2 - 4)
    lams = [(trA + disc) / 2, (trA - disc) / 2]
    max_align_dev = mp.mpf(0)
    for lam in lams:
        v = mp.matrix([TA[0, 1], lam - TA[0, 0]])
        if mp.norm(v) < mp.mpf("1e-10"):
            v = mp.matrix([lam - TA[1, 1], TA[1, 0]])
        w = mp.matrix([TB[0, 0] * v[0] + TB[0, 1] * v[1],
                       TB[1, 0] * v[0] + TB[1, 1] * v[1]])
        mu = (w[0] * mp.conj(v[0]) + w[1] * mp.conj(v[1])) / \
             (v[0] * mp.conj(v[0]) + v[1] * mp.conj(v[1]))
        dev = mp.norm(mp.matrix([w[0] - mu * v[0], w[1] - mu * v[1]])) / mp.norm(w)
        max_align_dev = max(max_align_dev, dev)
    print(f"      eigenlines of T_A are T_B-invariant: max relative dev = "
          f"{ns(max_align_dev, 5)}")
    check("common invariant lines exist => the block monodromy is REDUCIBLE "
          "(simultaneously diagonalizable)", max_align_dev < mp.mpf("1e-5"))
    return kappa


# ---------------------------------------------------------------------------
def main():
    print(BAR)
    print("B739 Stage-B recompute -- TOMB-L247 (K-J, TOMBSTONES.md:L247)")
    print("Discriminating fact: kappa(degenerate phi_{2,1} block monodromy) = 2")
    print("(reducible) vs kappa(seed) = 3 > 2 (irreducible): different points of")
    print("the SL(2,C) character variety; the '3=3' = eigenvalue-trace vs")
    print("commutator-trace artifact.")
    print(BAR + "\n")

    kappa_seed = s1_symbolic()
    print()
    tau_str = s2_block_monodromy_hermite()
    print()
    kappa_block_num = s3_block_monodromy_direct(tau_str)

    print("\n" + BAR)
    print("[VERDICT SUMMARY]")
    print(BAR)
    print(f"  kappa_seed  = tr[L,R]      = {kappa_seed}   (exact integer arithmetic)")
    print(f"  kappa_block = tr[M_A,M_B]  = 2   (exact: diagonal Hermite basis;")
    print(f"                RK4 path-integrated value {ns(kappa_block_num)})")
    print("  kappa is a regular function of the character (Fricke: X^2+Y^2+Z^2-XYZ-2),")
    print("  so kappa_block = 2 != 3 = kappa_seed proves the two monodromies are")
    print("  DIFFERENT points of the character variety: the block is reducible")
    print("  (abelian, trivial puncture monodromy), the seed is irreducible.")
    print("  The '3 = 3': phi^2 + phi^-2 = 3 is an eigenvalue-trace; tr[L,R] = 3 is a")
    print("  commutator-trace. On the block side a multiplier tuned to phi^2 still")
    print("  has commutator-trace 2. Metallic control: word-trace m+2 vs")
    print("  commutator-trace m^2+2 agree ONLY at m in {0,1} -- a golden accident,")
    print("  amplified at m=1 by charpoly(LR) = charpoly([L,R]) = t^2 - 3t + 1.")
    print("  => The banked kill (kind-mismatch) is UPHELD: RECONFIRMED.")


if __name__ == "__main__":
    main()
