"""B273 -- the residual computation (flagged by the B272 audit): the e6 bracket-coupled cup-product obstruction
H^1 x H^1 -> H^2(e6) for the E6 deformations of the figure-eight's principal rep. It VANISHES IDENTICALLY.
FIREWALLED (deformation theory of flat connections, not physics). Nothing to CLAIMS.md.

B272 flagged: B265's "E6-irreducible flat connections EXIST" rested on integrability of the {4,8} directions, and
the e6-bracket-coupled obstruction was UNCOMPUTED (B270 did only the SL(2)/exponent-1 block). This computes it.

SETUP. rho_prin = (principal sl(2) -> e6) o rho_geo : pi_1(4_1) -> E6. On e6 it acts by Ad; built explicitly as
Ad(rho_prin(a)) = exp(ad e), Ad(rho_prin(b)) = exp(t * ad f), t = e^{i pi/3} (e,f = principal nilpotents). This
SATISFIES the figure-eight relator (verified: the 78x78 product = I). The tangent space H^1(pi_1, e6) = (+)_m
H^1(Sym^{2m}) is 6-dim (one cocycle per E6 exponent m in {1,4,5,7,8,11}). The obstruction to integrating a tangent
vector xi is the cup product [xi U xi] in H^2(e6) = coker(d^1) (dim 6), using the e6 BRACKET (which couples the
exponent blocks -- this is why it is not the per-block SL(2) computation).

METHOD. Deform rho_eps(g) = exp(eps ad xi_g) Ad(rho(g)); expand the relator to eps^2: the eps^1 term is the cocycle
condition (= 0), the eps^2 term is ad(q) with q in e6 the obstruction element; [q] = 0 in H^2 iff q in im(d^1).
Computed EXACTLY mod two large primes p = 1 mod 3 (so t^2-t+1 splits) -- no precision loss, no coefficient blowup
(double precision fails: exp of the principal nilpotent has ~1e10 entries).

RESULT (both primes p in {99991, 100003}): rank d^1 = 72, dim H^2 = 6; the obstruction q is a NONZERO 2-cochain
(non-vacuous) but [q] = 0 in H^2 for ALL six pure directions AND for a generic random combination of all six. By
Schwartz-Zippel (random point over F_p, p ~ 1e5, two primes), the FULL quadratic cup product H^1 x H^1 -> H^2 is
IDENTICALLY ZERO. The quadratic cone = H^1 (dim 6 = rank). No second-order obstruction in any direction.

CONCLUSION. The leading (quadratic) obstruction vanishes identically at rho_prin -- exactly the witness that
establishes smoothness in the proven SL(2) case (Thurston / B270), now extended to the whole E6 tangent space. So
the {4,8} E6 directions integrate to second order: the existence of E6-irreducible flat connections (B265) is
established to second order (the leading obstruction is gone), upgrading B272's "expected to exist." HONEST residual:
full all-orders smoothness rests on the higher Massey products, expected to vanish by the same cusp mechanism as
SL(2) but not separately computed here.

Run: sage-python e6_obstruction_modp.py  (exact mod p; ~1 min/prime).
"""
from sage.all import LieAlgebra, QQ, GF, matrix, vector, identity_matrix, zero_vector, set_random_seed

EXPONENTS = [1, 4, 5, 7, 8, 11]
REL = "abABaBAbaB"


def run(p, seed):
    F = GF(p)
    t = (F["z"].gen() ** 2 - F["z"].gen() + 1).roots()[0][0]   # e^{i pi/3} mod p (p = 1 mod 3)
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
    relok = identity_matrix(F, d)
    for ch in REL:
        relok = relok * Ad[ch]
    assert relok == identity_matrix(F, d), "principal rep must satisfy the relator"

    def adof(v):
        M = matrix(F, d, d)
        for i in range(d):
            if v[i] != 0:
                M = M + v[i] * adb[i]
        return M

    def u_r(xa, xb):                                  # crossed-hom cocycle map (linear part)
        pref = identity_matrix(F, d); ur = zero_vector(F, d)
        for ch in REL:
            g = ch.lower(); xi = xa if g == "a" else xb
            ur = ur + pref * (xi if ch.islower() else -(Ad[ch] * xi)); pref = pref * Ad[ch]
        return ur

    def block_cocycle(m):                             # the H^1(Sym^{2m}) generator, as an e6 vector pair
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
    D1 = matrix(F, [u_r(ei if s == 0 else zero_vector(F, d), ei if s == 1 else zero_vector(F, d))
                    for s in range(2) for ei in (vector(F, [int(j == i) for j in range(d)]) for i in range(d))]).transpose()
    r1 = D1.rank()
    AD = matrix(F, [adb[i].list() for i in range(d)]).transpose()

    def obstruction_vanishes(xa, xb):
        adxa, adxb = adof(xa), adof(xb)

        def factor(ch):
            axi = adxa if ch.lower() == "a" else adxb; M = Ad[ch]
            return [M, axi * M, (axi * axi) * M / F(2)] if ch.islower() else [M, -M * axi, M * (axi * axi) / F(2)]

        prod = [identity_matrix(F, d), matrix(F, d, d), matrix(F, d, d)]
        for ch in REL:
            Ff = factor(ch); N = [matrix(F, d, d) for _ in range(3)]
            for i in range(3):
                for j in range(3):
                    if i + j <= 2:
                        N[i + j] = N[i + j] + prod[i] * Ff[j]
            prod = N
        q = AD.solve_right(vector(F, prod[2].list()))         # ad(q) = eps^2 term
        nonvac = q != zero_vector(F, d)
        return D1.augment(matrix(F, q).transpose()).rank() == r1, nonvac

    out = {"p": p, "H2dim": d - r1}
    for m in EXPONENTS:
        out[f"exp{m}"] = obstruction_vanishes(*cocyc[m])[0]
    set_random_seed(seed)
    lam = {m: F.random_element() for m in EXPONENTS}
    xa = sum(lam[m] * cocyc[m][0] for m in EXPONENTS); xb = sum(lam[m] * cocyc[m][1] for m in EXPONENTS)
    van, nonvac = obstruction_vanishes(xa, xb)
    out["generic"] = van; out["generic_nonvacuous"] = nonvac
    return out


if __name__ == "__main__":
    print("=== B273: the e6 bracket-coupled cup-product obstruction (exact mod p) ===\n")
    for p, seed in [(99991, 1), (100003, 2)]:
        r = run(p, seed)
        print(f"p={r['p']}: H^2 dim={r['H2dim']}; per-direction [xi U xi]=0: "
              f"{ {m: r[f'exp{m}'] for m in EXPONENTS} }")
        print(f"         generic combination [xi U xi]=0: {r['generic']} (q nonzero cochain: {r['generic_nonvacuous']})")
        assert r["H2dim"] == 6
        assert all(r[f"exp{m}"] for m in EXPONENTS)
        assert r["generic"] and r["generic_nonvacuous"]
    print("\n=> the full quadratic cup product H^1 x H^1 -> H^2(e6) is IDENTICALLY ZERO (2 primes, Schwartz-Zippel).")
    print("   No 2nd-order obstruction in any direction => the {4,8} E6 deformations integrate to 2nd order.")
    print("   B265 'expected to exist' upgraded: the leading obstruction vanishes identically. ALL PASS")
