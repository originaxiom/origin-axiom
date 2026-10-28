"""Referee B1802, r5: the period-2 involution P (cusp map +I) on Q = m004(p,q).
(a) Claim: Q/P = L6a2 with A' filled (2,0) and K' filled (p, 2q) (derivation: P translates the cusp by lambda/2, and the lift
    of K''s Seifert longitude is K's Seifert longitude since lk(lift, K) = 2 lk(lambda', K') = 0).  For p even (p,2q) has
    gcd 2: the core of the filling is a cone-pi circle, so P fixes TWO circles (A and the filling's core); for p odd one.
    Test: the 2-fold cover with every lifted filling (1,0) is isometric to m004(p,q).
(b) The equivariant Z/2-bundles: homs rho: H1^orb(Q/P) -> Z/2 that are nontrivial on pi1(Q) = ker psi (so restrict to chi),
    and their local actions at A' (meridian m_A) and at C' (the cone generator gamma'' = mu'^(p/2) lambda'^q).
(c) The same for the strong inversion's quotient L11n132 (m004(6,1)) as a control of the arc's (e)."""
import snappy, itertools, math
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form
def abel_vec(word, gens):
    v = [0] * len(gens)
    for ch in word:
        v[gens.index(ch.lower())] += 1 if ch.islower() else -1
    return v
def H1_and_maps(M):
    """Abelianise M's (orbifold) fundamental group; return (gens, relator matrix)."""
    G = M.fundamental_group(simplify_presentation=False) if False else M.fundamental_group()
    gens = G.generators(); R = [abel_vec(r, gens) for r in G.relators()]
    return G, gens, R
def homs_to_Z2(gens, R):
    out = []
    for vals in itertools.product((0, 1), repeat=len(gens)):
        if all(sum(a * b for a, b in zip(r, vals)) % 2 == 0 for r in R): out.append(vals)
    return out
def ev(vals, vec): return sum(a * b for a, b in zip(vals, vec)) % 2
print("(a) P's quotient")
for (p, q) in [(6, 1), (8, 1), (2, 3), (4, 3), (10, 3), (6, 5), (5, 1), (3, 2), (7, 1)]:
    Qm = snappy.Manifold("m004"); Qm.dehn_fill((p, q))
    O = snappy.Manifold("L6a2"); O.dehn_fill([(2, 0), (p, 2 * q)])
    isos = []
    for C in O.covers(2):
        f = C.cusp_info("filling")
        if all(abs(x[0] - 1) < 1e-9 and abs(x[1]) < 1e-9 for x in f):
            try: isos.append(bool(C.is_isometric_to(Qm)))
            except Exception as e: isos.append("err")
    iso = "%s (all-(1,0) covers: %s)" % (any(x is True for x in isos), isos)
    g = math.gcd(p, 2 * q)
    print("  m004(%d,%d): L6a2[(2,0),(%d,%d)] vol %.6f = vol(Q)/2 %.6f; cover isometric to Q: %s; gcd(p,2q) = %d -> fixed circles of P: %d" % (
        p, q, p, 2 * q, float(O.volume()), float(Qm.volume()) / 2, iso, g, 1 + (g == 2)))
print("(b) P-equivariant Z/2 bundles: local actions (rho(m_A), rho(m_C)) of every rho restricting to chi on pi1(Q)")
for (p, q) in [(6, 1), (8, 1), (2, 3), (4, 3), (10, 3), (12, 1)]:
    O = snappy.Manifold("L6a2"); O.dehn_fill([(2, 0), (p, 2 * q)])
    G, gens, R = H1_and_maps(O)
    per = G.peripheral_curves()
    mA = abel_vec(per[0][0], gens)
    muK, laK = abel_vec(per[1][0], gens), abel_vec(per[1][1], gens)
    mC = [a * (p // 2) + b * q for a, b in zip(muK, laK)]
    H = homs_to_Z2(gens, R)
    # psi: the branched cover's class: psi(m_A) = 1, psi(m_C) = 1, psi(mu_K') = 0
    psi = [h for h in H if ev(h, mA) == 1 and ev(h, mC) == 1 and ev(h, muK) == 0]
    assert len(psi) == 1, (p, q, len(psi)); psi = psi[0]
    res = sorted(set((ev(h, mA), ev(h, mC)) for h in H if h != psi and any(h)))
    print("  m004(%d,%d): |Hom(H1^orb, Z/2)| = %d; rho nontrivial on pi1(Q): local actions %s" % (p, q, len(H), res))
print("(c) control: the strong inversion's quotient for m004(6,1), L11n132 with both components (2,0)")
O = snappy.Manifold("L11n132"); O.dehn_fill([(2, 0), (2, 0)])
G, gens, R = H1_and_maps(O); per = G.peripheral_curves()
m1, m2 = abel_vec(per[0][0], gens), abel_vec(per[1][0], gens)
H = homs_to_Z2(gens, R)
psi = [h for h in H if ev(h, m1) == 1 and ev(h, m2) == 1]; assert len(psi) == 1; psi = psi[0]
print("  |Hom(H1^orb, Z/2)| = %d; rho nontrivial on pi1(Q): local actions %s" % (len(H), sorted(set((ev(h, m1), ev(h, m2)) for h in H if h != psi and any(h)))))
print("r5 exit 0")
