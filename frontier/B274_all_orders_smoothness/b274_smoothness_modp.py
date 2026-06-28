"""B274 -- all-orders smoothness of rho_prin in the E6 character variety of the figure-eight.
FIREWALLED (deformation theory of flat connections, not physics). Nothing to CLAIMS.md.

B273 showed the quadratic cup-product obstruction H^1 x H^1 -> H^2(e6) vanishes identically (integration TO SECOND
ORDER). This upgrades that to ALL ORDERS, two independent ways:

ROUTE (b) -- the boundary/cusp closer (the actual all-orders argument). Heusener-Porti / Menal-Ferrer-Porti: for a
one-cusped hyperbolic M, if the restriction H^1(M,Ad rho) -> H^1(dM,Ad rho) is injective and the boundary character
variety is smooth at rho|_dM, then rho is a SMOOTH point of X(M) of dim = 1/2 dim H^1(dM). All hypotheses are finite
integer certificates, computed here exactly mod p:
  - dim H^1(M, e6) = 6, dim H^2(M, e6) = 6                              [matches B264]
  - meridian holonomy REGULAR: ker(ad e) = 6 = rank(E6)                [principal nilpotent is regular unipotent]
    => the boundary T^2-variety is smooth at rho|_dM (commuting pairs near a regular element), and
       H^0(dM,e6) = ker(Ad(mu)-I) = ker(ad e) = 6  =>  dim H^1(dM,e6) = 2*6 = 12 = 2*rank
  - restriction injective: half-lives-half-dies makes the image a Lagrangian of dim 6 = dim H^1(M)  [B270 per-block]
  => rho_prin is a smooth point, dim 1/2 * 12 = 6 = rank(E6). ALL ORDERS. The implication is the cited MFP criterion
     (not re-derived in-sandbox) -- the same footing as the SL(2)/Thurston statement already in the program.

ROUTE (a) -- the cubic (third-order) obstruction, as independent in-sandbox corroboration + a real falsification
gate. Extend B273's relator eps-expansion to eps^3 with the deformation exp(eps ad xi + eps^2 ad eta) Ad(rho(g)):
construct the ACTUAL bounding cochain eta with d^1(eta) = -q (B273 only proved it exists), check eps^2 vanishes
(o2), then the eps^3 coefficient is ad(q3); test [q3]=0 in H^2. Done for all 6 exponent directions + a generic
combination, two primes, and verified invariant under the eta-indeterminacy (eta -> eta + ker d^1).

RESULT (both primes 99991, 100003): all route-(b) certificates = {6,6,6,12}; the cubic obstruction VANISHES for all
six directions and the generic combination (q3 a nonzero cochain but a coboundary; eta-shift invariant). So:
rho_prin is a smooth point of the E6 character variety; the {4,8} E6-irreducible flat connections (B265) exist
UNCONDITIONALLY (not merely to finite order).

Run: sage-python b274_smoothness_modp.py  (exact mod p; ~1-2 min/prime).
"""
from sage.all import LieAlgebra, QQ, GF, matrix, vector, identity_matrix, zero_vector, set_random_seed

EXPONENTS = [1, 4, 5, 7, 8, 11]
REL = "abABaBAbaB"


def run(p, seed):
    F = GF(p)
    t = (F["z"].gen() ** 2 - F["z"].gen() + 1).roots()[0][0]
    L = LieAlgebra(QQ, cartan_type=["E", 6]); d = L.dimension(); idx = list(L.cartan_type().index_set()); B = list(L.basis())
    adb = [matrix(F, [L.bracket(b, cc).to_vector() for cc in B]).transpose() for b in B]
    Hh = {i: L.bracket(L.e(i), L.f(i)) for i in idx}
    c = 2 * L.cartan_type().cartan_matrix().inverse() * vector(QQ, [1] * len(idx))
    e = sum(L.e(i) for i in idx); h = sum(c[k] * Hh[idx[k]] for k in range(len(idx))); f = sum(c[k] * L.f(idx[k]) for k in range(len(idx)))
    ade = matrix(F, [L.bracket(e, b).to_vector() for b in B]).transpose()
    adf = matrix(F, [L.bracket(f, b).to_vector() for b in B]).transpose()
    adh = matrix(F, [L.bracket(h, b).to_vector() for b in B]).transpose()

    def expnil(M):
        Rm = identity_matrix(F, d); term = identity_matrix(F, d); k = 1
        while term != 0 * term and k < 60:
            term = term * M / F(k); Rm = Rm + term; k += 1
        return Rm

    Ad = {"a": expnil(ade), "A": expnil(-ade), "b": expnil(t * adf), "B": expnil(-t * adf)}
    P = identity_matrix(F, d)
    for ch in REL:
        P = P * Ad[ch]
    assert P == identity_matrix(F, d), "principal rep must satisfy the relator"

    def E(i):
        return vector(F, [int(j == i) for j in range(d)])

    def adof(v):
        M = matrix(F, d, d)
        for i in range(d):
            if v[i] != 0:
                M = M + v[i] * adb[i]
        return M

    def u_r(xa, xb):
        pref = identity_matrix(F, d); ur = zero_vector(F, d)
        for ch in REL:
            g = ch.lower(); xi = xa if g == "a" else xb
            ur = ur + pref * (xi if ch.islower() else -(Ad[ch] * xi)); pref = pref * Ad[ch]
        return ur

    def block_cocycle(m):
        hw = (adh - 2 * m * identity_matrix(F, d)).stack(ade).right_kernel().basis()[0]
        W = [hw]; cur = hw
        for _ in range(2 * m):
            cur = adf * cur; W.append(cur)
        Wmat = matrix(F, W); n = 2 * m + 1
        Z = matrix(F, [u_r(w if s == "a" else zero_vector(F, d), w if s == "b" else zero_vector(F, d))
                       for s in ["a", "b"] for w in W]).transpose().right_kernel().basis()
        COB = matrix(F, [list(Wmat.solve_left((Ad["a"] - 1) * w)) + list(Wmat.solve_left((Ad["b"] - 1) * w)) for w in W]).transpose()
        xi = next(v for v in Z if COB.augment(matrix(F, v).transpose()).rank() > COB.rank())
        return sum(xi[i] * W[i] for i in range(n)), sum(xi[n + i] * W[i] for i in range(n))

    cocyc = {m: block_cocycle(m) for m in EXPONENTS}
    D1 = matrix(F, [u_r(E(i) if s == 0 else zero_vector(F, d), E(i) if s == 1 else zero_vector(F, d))
                    for s in range(2) for i in range(d)]).transpose()
    r1 = D1.rank()
    d0 = matrix(F, [list((Ad["a"] - 1) * E(i)) + list((Ad["b"] - 1) * E(i)) for i in range(d)]).transpose()
    AD = matrix(F, [adb[i].list() for i in range(d)]).transpose()

    def recover(M):
        return AD.solve_right(vector(F, M.list()))

    # ---- route (b) certificates ----
    dimH1M = 2 * d - r1 - d0.rank()
    cert = dict(H1M=dimH1M, H2M=d - r1,
                merid_regular=ade.right_kernel().dimension(),
                H0_boundary=(Ad["a"] - identity_matrix(F, d)).right_kernel().dimension())
    cert["H1_boundary"] = 2 * cert["H0_boundary"]

    # ---- route (a) cubic obstruction ----
    def cubic(xa, xb, shift_eta=False):
        adxa, adxb = adof(xa), adof(xb)

        def fac2(ch):
            axi = adxa if ch.lower() == "a" else adxb; M = Ad[ch]
            return [M, axi * M, (axi * axi) * M / F(2)] if ch.islower() else [M, -M * axi, M * (axi * axi) / F(2)]

        pr = [identity_matrix(F, d), matrix(F, d, d), matrix(F, d, d)]
        for ch in REL:
            Ff = fac2(ch); N = [matrix(F, d, d) for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    if i + j <= 2:
                        N[i + j] = N[i + j] + pr[i] * Ff[j]
            pr = N
        q = recover(pr[2])
        eta = D1.solve_right(-q)                              # d1(eta) = -q  (eta exists since [q]=0, B273)
        if shift_eta:
            ker = D1.right_kernel().basis()
            if ker:
                eta = eta + ker[0]
        eta_a = sum(eta[i] * E(i) for i in range(d)); eta_b = sum(eta[d + i] * E(i) for i in range(d))
        adya, adyb = adof(eta_a), adof(eta_b)

        def fac3(ch):
            g = ch.lower(); X = adxa if g == "a" else adxb; Y = adya if g == "a" else adyb; M = Ad[ch]
            if ch.islower():
                cc = [identity_matrix(F, d), X, Y + X * X / F(2), (X * Y + Y * X) / F(2) + X * X * X / F(6)]
                return [ci * M for ci in cc]
            cc = [identity_matrix(F, d), -X, -Y + X * X / F(2), (X * Y + Y * X) / F(2) - X * X * X / F(6)]
            return [M * ci for ci in cc]

        pr = [identity_matrix(F, d)] + [matrix(F, d, d) for _ in range(3)]
        for ch in REL:
            Ff = fac3(ch); N = [matrix(F, d, d) for _ in range(4)]
            for i in range(4):
                for j in range(4):
                    if i + j <= 3:
                        N[i + j] = N[i + j] + pr[i] * Ff[j]
            pr = N
        q3 = recover(pr[3])
        return dict(o1=bool(pr[1] == 0 * pr[1]), o2=bool(pr[2] == 0 * pr[2]),
                    vanishes=bool(D1.augment(matrix(F, q3).transpose()).rank() == r1),
                    q3_nonzero=bool(q3 != zero_vector(F, d)))

    out = dict(p=p, **cert)
    for m in EXPONENTS:
        out[f"cubic_exp{m}"] = cubic(*cocyc[m])["vanishes"]
    set_random_seed(seed)
    lam = {m: F.random_element() for m in EXPONENTS}
    xa = sum(lam[m] * cocyc[m][0] for m in EXPONENTS); xb = sum(lam[m] * cocyc[m][1] for m in EXPONENTS)
    g = cubic(xa, xb)
    out["cubic_generic"] = g["vanishes"]; out["generic_o2_zero"] = g["o2"]; out["generic_q3_nonzero"] = g["q3_nonzero"]
    out["cubic_generic_eta_shifted"] = cubic(xa, xb, shift_eta=True)["vanishes"]
    return out


if __name__ == "__main__":
    print("=== B274: all-orders smoothness of rho_prin in the E6 character variety ===\n")
    for p, seed in [(99991, 1), (100003, 2)]:
        r = run(p, seed)
        print(f"p={r['p']}  route(b) certs: dim H1(M)={r['H1M']}, dim H2(M)={r['H2M']}, "
              f"meridian regular ker(ad e)={r['merid_regular']}, dim H0(dM)={r['H0_boundary']}, dim H1(dM)={r['H1_boundary']}")
        print(f"        route(a) cubic [q3]=0: { {m: r[f'cubic_exp{m}'] for m in EXPONENTS} }  "
              f"generic={r['cubic_generic']} (o2=0:{r['generic_o2_zero']}, q3!=0:{r['generic_q3_nonzero']}, eta-shift inv:{r['cubic_generic_eta_shifted']})")
        assert r["H1M"] == 6 and r["H2M"] == 6 and r["merid_regular"] == 6 and r["H1_boundary"] == 12
        assert all(r[f"cubic_exp{m}"] for m in EXPONENTS)
        assert r["cubic_generic"] and r["generic_o2_zero"] and r["generic_q3_nonzero"] and r["cubic_generic_eta_shifted"]
    print("\n=> MFP smoothness signature {6,6,12} + regular meridian => rho_prin is a SMOOTH point, dim 6 = rank.")
    print("   Cubic (3rd-order) obstruction vanishes identically (independent corroboration).")
    print("   E6-irreducible flat connections exist UNCONDITIONALLY (all orders). ALL PASS")
