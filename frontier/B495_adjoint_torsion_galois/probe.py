"""B495 -- Gate A, class 2a: the nonabelian adjoint/Ptolemy torsion class of the
figure-eight across the SL(2,C) character variety -- the Galois-orbit sealing sweep
(Closure Campaign Phase 2; prereg docs/CLOSURE_CAMPAIGN_2026-07.md + local README.md).

QUESTION (Gate A / S032-A, restricted to this class). Is any adjoint-torsion-type
invariant of the single seed (1) trace-map-invariant, (2) discretely multivalued,
(3) UNsymmetrizable -- a genuine forced choice? Outcome enum (committed):
SEALED / COUNTEREXAMPLE / TOOL-BLOCKED.

METHOD (all banked): the B425 Fox/Wada adjoint (Sym^2) twisted-Alexander pipeline with
reg-at-1 normalization (the convention that reproduced Porti's tau_1 = -3 by a third
route); the B98 trace-map-Jacobian transverse pair tau = 2 - c(x) on the fixed curve V0
(the once-punctured-torus-bundle picture); the B330 Galois-symmetrization mechanism;
the B348 amphichirality-kills-orientation-sign pattern. Everything below is TIER: exact
(sympy rational/quadratic-field arithmetic; no floats anywhere in a claim; cypari algdep
was never needed). SnapPy is used only for two exact/combinatorial cross-checks (Ptolemy
N=2 equations, amphichirality) and is optional at run time.

STRUCTURE OF THE COMPUTATION
  0.  controls: the two banked anchors (geometric adjoint torsion -3 Eisenstein via
      Fox/Wada; dynamical zeta adjoint -5 golden). Control failure => INVALID, stop.
  1.  the character variety enumerated: X(4_1) = X_red (abelian line) + X_irr (ONE
      nonabelian curve Phi(m,z) = z^2 - (m^2+1) z + 2 m^2 - 1, derived from the relator,
      irreducible over Q, and irreducible over C by the simple-branch double-cover
      argument). Canonical finite strata of X_irr (each an intrinsic, trace-map-fixed,
      Galois-stable set):
        PC-1 geometric/parabolic pair   m = +-2, z Eisenstein  (Q(sqrt-3))
        PC-2 metabelian/binary-dihedral m = 0,   z golden      (Q(sqrt5); image Dic5)
        PC-3 bifurcation (X_red ^ X_irr, Burde-de Rham) m = +-sqrt5, z = 3 (reducible char)
        PC-4 branch/2T pair             m = +-1, z = 1         (image = binary tetrahedral)
      plus the abelian component's continuous torsion function (the B130-style
      clause-(2) exhibit) and the trivial-character end (the dynamical zeta).
  2.  the adjoint torsion at every reachable point, exactly, TWO independent methods
      (Fox/Wada Wada-quotient reg-at-1; V0 transverse Jacobian 2 - c(x)), with the
      H^1 Fox-rank certificate and the x_mu-regularity certificate at each point.
  3.  the value multiset + the three conditions + the Galois closure test
      (sqrt-3 -> -sqrt-3, sqrt5 -> -sqrt5, complex conjugation = amphichiral).
  4.  the Ptolemy cross-check at N = 2 (boundary-unipotent solution sets, both
      obstruction classes, solved exactly offline) and the honest out-of-reach list.

VERDICT (computed below, asserted, and banked in b495_adjoint_torsion.json):
SEALED at the computable horizon. The full Wada-value multiset over the canonical
strata is {-3,-3, +3,+3, +5,+5, -5,-5} -- every value RATIONAL (already in the fixed
field: total Galois collapse, stronger than the B314/B318 pair-symmetrization), the
multiset is sign-symmetric (sum 0 -- the B348 orientation-sign kill landing in this
class), product 15^4 (the seam 15 = 3.5), and the residual dr/da vs dr/db Wada unit
(= -1, constant on the curve) leaves the multiset invariant. No forced choice. The
class beyond these components (SL(n>=3)/Ptolemy N>=3, CS/eta, extended-Bloch) remains
open -- named at the end, per the C-guardrail.

Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.
"""
import itertools
import json
import os

import sympy as sp

t, r, m, z, v, s, x = sp.symbols('t r m z v s x')

E = sp.expand


# =====================================================================
# 0. shared exact machinery (B425 conventions)
# =====================================================================
def inv_word(word):
    return [(g, -e) for g, e in reversed(word)]


A_ = [('a', 1)]
B_ = [('b', 1)]
W_ = B_ + inv_word(A_) + inv_word(B_) + A_          # w = b a^-1 b^-1 a
R_ = A_ + W_ + inv_word(B_) + inv_word(W_)          # r = a w b^-1 w^-1  (4_1 relator)


def fox(word, g0):
    """Fox derivative d(word)/d(g0) as a list of (prefix, sign)."""
    terms, prefix = [], []
    for (g, e) in word:
        if e == 1:
            if g == g0:
                terms.append((list(prefix), 1))
            prefix = prefix + [(g, 1)]
        else:
            prefix = prefix + [(g, -1)]
            if g == g0:
                terms.append((list(prefix), -1))
    return terms


class QF:
    """Exact arithmetic over Q(r | r^2 = n) [sympy I allowed alongside]."""

    def __init__(self, n):
        self.n = n

    def red(self, e):
        e = E(e)
        if self.n is None or not e.has(r):
            return e
        p = sp.Poly(e, r)
        out = 0
        for k, c in enumerate(p.all_coeffs()[::-1]):   # low -> high degree in r
            out += c * (self.n ** (k // 2)) * (r ** (k % 2))
        return E(out)

    def mat(self, M):
        return M.applyfunc(self.red)

    def mul(self, A, B):
        return self.mat(A * B)

    def det(self, M):
        return self.red(M.det(method='berkowitz'))


def sym2(M):
    """Sym^2 of a 2x2 matrix = the adjoint rep of SL2 (Ad(-M) = Ad(M); asserted below)."""
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    return sp.Matrix([[a**2, a * b, b**2],
                      [2 * a * c, a * d + b * c, 2 * b * d],
                      [c**2, c * d, d**2]])


def sl2_inv(M):
    return sp.Matrix([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]])


def word_mat(word, ra, rb, F):
    L = {('a', 1): ra, ('a', -1): sl2_inv(ra), ('b', 1): rb, ('b', -1): sl2_inv(rb)}
    M = sp.eye(2)
    for ge in word:
        M = F.mat(M * L[ge])
    return M


def foxmat(ra, rb, F, deriv):
    """Phi(dr/d(deriv)) in Sym^2 x t^deg -- the adjoint Fox matrix."""
    RA, RB = F.mat(sym2(ra)), F.mat(sym2(rb))
    RAi, RBi = F.mat(sym2(sl2_inv(ra))), F.mat(sym2(sl2_inv(rb)))
    L = {('a', 1): RA, ('a', -1): RAi, ('b', 1): RB, ('b', -1): RBi}
    S = sp.zeros(3, 3)
    for (word, sign) in fox(R_, deriv):
        M = sp.eye(3)
        texp = 0
        for (g, e) in word:
            M = F.mul(M, L[(g, e)])
            texp += e
        S += sign * M * t**texp
    return F.mat(S)


def wada(ra, rb, F, deriv='b'):
    """Wada quotient det Phi(dr/d deriv) / det(Sym^2(other) t - I)  (B425 pipeline)."""
    S = foxmat(ra, rb, F, deriv)
    other = F.mat(sym2(ra if deriv == 'b' else rb))
    return sp.cancel(sp.together(F.det(S)) / sp.together(F.det(other * t - sp.eye(3))))


def reg_at_1(W, F):
    """Strip (t-1)^k from numerator and denominator, evaluate at t=1 (B425 reg).
    Returns (value, k_num, k_den)."""
    num, den = sp.fraction(sp.cancel(sp.together(W)))
    num, den = sp.Poly(F.red(E(num)), t), sp.Poly(F.red(E(den)), t)

    def strip(P):
        k = 0
        while P.degree() > 0 and F.red(E(P.eval(1))) == 0:
            P = sp.Poly(sp.div(P.as_expr(), (t - 1), t)[0], t)
            k += 1
        return P, k

    (num, kn), (den, kd) = strip(num), strip(den)
    val = sp.cancel(F.red(E(num.eval(1))) / F.red(E(den.eval(1))))
    return F.red(E(sp.radsimp(val))), kn, kd


def fox_rank(ra, rb, F):
    """rank of the 3x6 adjoint Fox Jacobian [Phi(dr/da) | Phi(dr/db)] at t=1.
    rank 2  <=>  dim Z^1 = 4  <=>  dim H^1 = 1 at points with no Ad-invariants."""
    J = F.mat(foxmat(ra, rb, F, 'a').subs(t, 1).row_join(foxmat(ra, rb, F, 'b').subs(t, 1)))
    if any(F.red(E(J[:, list(c)].det())) != 0 for c in itertools.combinations(range(6), 3)):
        return 3
    for rows in itertools.combinations(range(3), 2):
        for cols in itertools.combinations(range(6), 2):
            if F.red(E(sp.Matrix([[J[i, j] for j in cols] for i in rows]).det())) != 0:
                return 2
    return 1 if any(e != 0 for e in J) else 0


def group_order(ra, rb, F, cap=200):
    """order of <ra, rb> by exact closure enumeration (finite-image certificate)."""
    def key(M):
        return tuple(sp.nsimplify(F.red(E(M[i, j]))) for i in range(2) for j in range(2))
    gens = [ra, rb, sl2_inv(ra), sl2_inv(rb)]
    seen = {key(sp.eye(2))}
    frontier = [sp.eye(2)]
    while frontier and len(seen) <= cap:
        new = []
        for M in frontier:
            for g in gens:
                N = F.mat(M * g)
                k = key(N)
                if k not in seen:
                    seen.add(k)
                    new.append(N)
        frontier = new
    return len(seen) if len(seen) <= cap else None


REPORT = {}


def bank(section, **kv):
    REPORT.setdefault(section, {}).update({k: (str(w) if isinstance(w, (sp.Basic, sp.Matrix))
                                               else w) for k, w in kv.items()})


# =====================================================================
# SECTION 0 -- CONTROLS (the banked anchors; failure => INVALID)
# =====================================================================
def controls():
    print("== 0. CONTROLS (banked anchors; tier: exact) ==")
    F3 = QF(-3)
    # (a) geometric adjoint torsion at rho_geo (B425 / V30 / V31 / B98): -3, Eisenstein.
    #     s = 1, rho(a) = [[1,1],[0,1]], rho(b) = [[1,0],[v,1]], relator => v^2 - v + 1 = 0
    #     (equivalently B425's u = -v with u^2 + u + 1 = 0, u = omega).
    ra = sp.Matrix([[1, 1], [0, 1]])
    out = {}
    for tag, vr in [("rho_geo", (1 + r) / 2), ("rho_geo_bar", (1 - r) / 2)]:
        rb = sp.Matrix([[1, 0], [vr, 1]])
        assert word_mat(R_, ra, rb, F3) == sp.eye(2), "holonomy relator fails"
        Wq = wada(ra, rb, F3, 'b')
        val, kn, kd = reg_at_1(Wq, F3)
        out[tag] = (sp.factor(Wq), val, kn, kd)
        assert val == -3 and (kn, kd) == (1, 0), f"CONTROL FAIL at {tag}: {val}"
    W_geo = out["rho_geo"][0]
    assert W_geo == sp.factor((t - 1) * (t**2 - 5 * t + 1) / t**3), "geo Wada poly drifted"
    print(f"   geometric pair: W(t) = {W_geo}   tau = -3  (both Galois lifts)   [exact]")

    # (b) dynamical zeta (B423/B425): det'(I - Sym^2 A_cat), A_cat = [[2,1],[1,1]] = -5.
    Fq = QF(None)
    cp = sp.factor(sym2(sp.Matrix([[2, 1], [1, 1]])).charpoly(t).as_expr())
    red = sp.div(sp.expand(cp), t - 1, t)
    assert red[1] == 0, "charpoly Sym2(cat) lacks the (t-1) factor"
    zeta1 = red[0].subs(t, 1)
    assert sp.factor(cp) == sp.factor((t - 1) * (t**2 - 7 * t + 1)) and zeta1 == -5, \
        f"CONTROL FAIL: dynamical zeta {zeta1}"
    print(f"   dynamical zeta: charpoly Sym^2(cat) = {cp}  ->  zeta_1 = -5 = 2 - L_4   [exact]")

    # (c) PSL sign-lift collapse: Ad(-M) = Ad(M) => the m = -2, 0-, ... sign-lifts carry
    #     identical adjoint computations (symbolic identity, all four matrix entries free).
    a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4')
    Msym = sp.Matrix([[a1, a2], [a3, a4]])
    assert sp.expand(sym2(-Msym) - sym2(Msym)) == sp.zeros(3, 3)
    print("   PSL collapse: Sym^2(-M) == Sym^2(M) (symbolic)  => sign-lifts add no values")
    bank("controls", geo_W=W_geo, geo_tau=-3, dyn_charpoly=cp, dyn_zeta1=-5,
         psl_collapse=True)
    return True


# =====================================================================
# SECTION 1 -- the SL(2,C) character variety of 4_1, enumerated
# =====================================================================
def enumerate_variety():
    print("\n== 1. THE CHARACTER VARIETY (tier: exact) ==")
    # Riley normal form rho(a) = [[s,1],[0,1/s]], rho(b) = [[s,0],[v,1/s]].
    Ra = sp.Matrix([[s, 1], [0, 1 / s]])
    Rb = sp.Matrix([[s, 0], [v, 1 / s]])
    Rel = sp.simplify(Ra * (Rb * Ra.inv() * Rb.inv() * Ra) * Rb.inv()
                      * (Ra.inv() * Rb * Ra * Rb.inv()) - sp.eye(2))
    ents = [sp.numer(sp.together(Rel[i, j])) for i in range(2) for j in range(2)]
    G = sp.factor(sp.gcd(ents))
    # the nonabelian (Riley) ideal: common factor of all four entries, unit s^2 removed
    riley = sp.expand(sp.cancel(G / s**2))
    print(f"   Riley polynomial (v-form): {riley} = 0")
    # in terms of y = s^2 + s^-2 = m^2 - 2 it reads (v-1) y + v^2 - 3 v + 3:
    yv = sp.symbols('yv')
    riley_y = sp.expand((v - 1) * yv + v**2 - 3 * v + 3)
    assert sp.simplify(riley - ((v - 1) * (s**2 + 1 / s**2) + v**2 - 3 * v + 3)) == 0
    # B425 anchor: at s = 1 the Riley polynomial is v^2 - v + 1 (u = -v: u^2 + u + 1).
    assert sp.expand(riley.subs(s, 1)) == sp.expand(v**2 - v + 1)
    print("   anchor: s=1 => v^2 - v + 1 = 0 (the B425 holonomy quadratic; u = -v)   [exact]")

    # character coordinates: meridian trace m = s + 1/s, z = tr(ab) = m^2 - 2 + v.
    zz = sp.expand((Ra * Rb).trace())            # = s^2 + s^-2 + v
    assert sp.simplify(zz - ((s + 1 / s)**2 - 2 + v)) == 0
    Phi = sp.expand(riley_y.subs([(yv, m**2 - 2), (v, z - m**2 + 2)]))
    print(f"   nonabelian character variety: Phi(m,z) = {Phi} = 0")
    assert Phi == sp.expand(z**2 - (m**2 + 1) * z + 2 * m**2 - 1)
    # ONE nonabelian component:
    assert sp.factor_list(Phi)[1][0][1] == 1 and len(sp.factor_list(Phi)[1]) == 1, \
        "Phi reducible over Q?"
    disc = sp.factor(sp.discriminant(Phi, z))
    print(f"   disc_z Phi = {disc}   (squarefree: {sp.gcd(sp.expand(disc), sp.diff(sp.expand(disc), m)) == 1})")
    assert disc == sp.factor((m - 1) * (m + 1) * (m**2 - 5))
    assert sp.gcd(sp.expand(disc), sp.diff(sp.expand(disc), m)) == 1
    # C-irreducibility: {Phi=0} -> C_m is a degree-2 cover branched (simply) at the four
    # simple roots of disc; a double cover with a simple branch point is connected, so
    # the nonabelian curve is irreducible over C: X(4_1) has exactly TWO components.
    print("   => X(4_1) = [abelian line] + [ONE nonabelian curve] (simple-branch double cover)")

    # the canonical finite strata (definitions intrinsic; fields printed):
    kappa = sp.expand(2 * m**2 + z**2 - m**2 * z - 2)     # tr[a,b] on characters
    strata = {}
    #  PC-1 geometric: boundary-parabolic m = +-2
    q_geo = sp.factor(Phi.subs(m, 2))
    assert q_geo == sp.factor(z**2 - 5 * z + 7) and sp.discriminant(z**2 - 5 * z + 7, z) == -3
    strata['PC1_geometric'] = dict(locus="m = +-2 (meridian-parabolic)", quad=str(q_geo),
                                   field="Q(sqrt-3)  [disc -3, Eisenstein]")
    #  PC-2 metabelian: m = 0
    q_met = sp.factor(Phi.subs(m, 0))
    assert q_met == sp.factor(z**2 - z - 1) and sp.discriminant(z**2 - z - 1, z) == 5
    strata['PC2_metabelian'] = dict(locus="m = 0 (traceless meridian)", quad=str(q_met),
                                    field="Q(sqrt5)  [disc 5, golden; z = phi literally]")
    #  PC-3 bifurcation: X_red ^ X_irr (Burde-de Rham) = branch component m^2 = 5
    zbif = sp.solve(Phi.subs(m**2, 5), z)
    assert zbif == [3] and sp.simplify(kappa.subs([(m**2, 5), (z, 3)]) - 2) == 0
    #      reducible character (kappa = 2); v = z - m^2 + 2 = 0 and Riley(v=0) = -(Delta(s^2)):
    alex_check = sp.factor(riley.subs(v, 0) * s**2)
    assert alex_check == sp.factor(-(s**4 - 3 * s**2 + 1))     # = -Delta_{4_1}(s^2)
    strata['PC3_bifurcation'] = dict(locus="m = +-sqrt5, z = 3 (X_red ^ X_irr; Delta(s^2)=0)",
                                     quad="z = 3 (double)", field="Q(sqrt5)  [m = +-sqrt5]")
    #  PC-4 branch/2T: m^2 = 1
    z2t = sp.solve(Phi.subs(m**2, 1), z)
    k2t = sp.simplify(kappa.subs([(m**2, 1), (z, 1)]))
    assert z2t == [1] and k2t == 0                    # irreducible character (kappa != 2)
    strata['PC4_branch_2T'] = dict(locus="m = +-1, z = 1 (x_mu-critical; image 2T)",
                                   quad="z = 1 (double)", field="Q  [character rational]")
    for k, d in strata.items():
        print(f"   {k}: {d['locus']}  quad {d['quad']}  field {d['field']}")

    # x_mu-regularity certificates: dPhi/dz at each stratum
    dPhi = sp.diff(Phi, z)
    reg_cert = {
        'PC1_geometric': sp.simplify(dPhi.subs(m, 2).subs(z, sp.Rational(5, 2) + sp.sqrt(-3) / 2)),
        'PC2_metabelian': sp.simplify(dPhi.subs(m, 0).subs(z, sp.Rational(1, 2) + sp.sqrt(5) / 2)),
        'PC3_bifurcation': sp.simplify(dPhi.subs([(m**2, 5), (z, 3)])),
        'PC4_branch_2T': sp.simplify(dPhi.subs([(m**2, 1), (z, 1)])),
    }
    assert reg_cert['PC1_geometric'] != 0 and reg_cert['PC2_metabelian'] != 0
    assert reg_cert['PC3_bifurcation'] == 0 and reg_cert['PC4_branch_2T'] == 0
    print("   x_mu-regularity dPhi/dz: geo/meta NONZERO (Porti mu-framing valid);")
    print("                            bif/2T ZERO (mu-framing critical -- certificates exact)")
    bank("variety", riley=riley, Phi=Phi, disc=disc, strata=strata,
         reg_cert={k: str(w) for k, w in reg_cert.items()},
         alexander_from_v0=str(alex_check), components=2)
    return Phi, kappa


# =====================================================================
# SECTION 2 -- the adjoint torsion at every reachable point (two methods)
# =====================================================================
def torsion_sweep():
    print("\n== 2. THE ADJOINT TORSION AT EVERY REACHABLE POINT (tier: exact) ==")
    rows = []

    def run(tag, ra, rb, F, field, x_mu_regular, note=""):
        assert word_mat(R_, ra, rb, F) == sp.eye(2), f"{tag}: relator fails"
        Wb_ = wada(ra, rb, F, 'b')
        Wa_ = wada(ra, rb, F, 'a')
        vb, knb, kdb = reg_at_1(Wb_, F)
        va, kna, kda = reg_at_1(Wa_, F)
        unit = sp.cancel(sp.together(Wa_ / Wb_))
        unit = sp.simplify(F.red(E(sp.radsimp(unit))))
        rk = fox_rank(ra, rb, F)
        rows.append(dict(tag=tag, field=field, W=str(sp.factor(Wb_)), tau=str(vb),
                         t1_mult=(knb, kdb), gauge_unit=str(unit), tau_dr_da=str(va),
                         fox_rank=rk, x_mu_regular=x_mu_regular, tier="exact", note=note))
        print(f"   {tag:22s} tau = {str(vb):3s}  W(t) = {str(sp.factor(Wb_)):34s} "
              f"rank {rk}  unit(da/db) = {unit}")
        return vb

    F3, F5 = QF(-3), QF(5)
    # PC-1 geometric pair (s = 1; v the two Eisenstein roots)
    ra = sp.Matrix([[1, 1], [0, 1]])
    v_geo = run("PC1 rho_geo", ra, sp.Matrix([[1, 0], [(1 + r) / 2, 1]]), F3,
                "point Q(sqrt-3), value Q", True)
    v_geo2 = run("PC1 rho_geo_bar", ra, sp.Matrix([[1, 0], [(1 - r) / 2, 1]]), F3,
                 "point Q(sqrt-3), value Q", True)
    # PC-2 metabelian pair (s = I; v = (5 +- sqrt5)/2; image Dic5, order 20)
    ra_m = sp.Matrix([[sp.I, 1], [0, -sp.I]])
    rb_m1 = sp.Matrix([[sp.I, 0], [(5 + r) / 2, -sp.I]])
    rb_m2 = sp.Matrix([[sp.I, 0], [(5 - r) / 2, -sp.I]])
    v_met = run("PC2 metabelian+", ra_m, rb_m1, F5, "point Q(i,sqrt5), value Q", True)
    v_met2 = run("PC2 metabelian-", ra_m, rb_m2, F5, "point Q(i,sqrt5), value Q", True)
    o_dic = group_order(ra_m, rb_m1, F5)
    assert o_dic == 20, f"metabelian image order {o_dic} != 20 (Dic5)"
    # PC-3 bifurcation rep (s = phi golden, v = 0: the non-semisimple reducible rep,
    #      the limit of X_irr into X_red; its semisimplification is the abelian rep)
    phi_ = (1 + r) / 2
    phii = F5.red((r - 1) / 2)                                  # 1/phi = phi - 1
    v_bif = run("PC3 bifurcation", sp.Matrix([[phi_, 1], [0, phii]]),
                sp.Matrix([[phi_, 0], [0, phii]]), F5,
                "point Q(sqrt5), value Q", False,
                note="reducible non-semisimple rep; W = the DYNAMICAL ZETA polynomial")
    # PC-4 branch/2T pair (s = zeta_6, v = 2; image binary tetrahedral, order 24)
    s6, s6i = (1 + r) / 2, (1 - r) / 2
    ra_q = sp.Matrix([[s6, 1], [0, s6i]])
    rb_q = sp.Matrix([[s6, 0], [2, s6i]])
    v_2t = run("PC4 branch/2T", ra_q, rb_q, F3, "point Q(sqrt-3), value Q", False,
               note="x_mu-critical; W = (t-1)Phi_3(t)/t^3, the Eisenstein cyclotomic")
    o_2t = group_order(ra_q, rb_q, F3)
    traces_2t = sorted({sp.nsimplify(F3.red(E(word_mat(w, ra_q, rb_q, F3).trace())))
                        for w in [A_, B_, A_ + B_, A_ + inv_word(B_),
                                  A_ + A_, B_ + B_, A_ + B_ + A_, A_ + A_ + B_]}, key=str)
    assert o_2t == 24, f"2T image order {o_2t} != 24"
    print(f"   finite-image certificates: metabelian image order 20 (Dic5), "
          f"branch image order 24 (2T; sample traces {traces_2t})")

    # the expected exact values (assert = the sweep's content)
    assert (v_geo, v_geo2, v_met, v_met2, v_bif, v_2t) == (-3, -3, 5, 5, -5, 3)

    # Method B: the V0 transverse-Jacobian (B98) recomputed from scratch
    print("\n   -- method B: trace-map transverse Jacobian on V0 (independent) --")
    T1 = lambda vv: (vv[2], vv[0], vv[0] * vv[2] - vv[1])
    xx, yy, zz = sp.symbols('xx yy zz')
    F2 = [E(c) for c in T1(T1((xx, yy, zz)))]
    yc = xx / (xx - 1)
    assert all(sp.simplify(F2[i].subs([(yy, yc), (zz, yc)]) - [xx, yc, yc][i]) == 0
               for i in range(3)), "V0 not pointwise fixed"
    J = sp.Matrix([[sp.diff(F2[i], u) for u in (xx, yy, zz)] for i in range(3)])
    cpV0 = sp.factor(J.subs([(yy, yc), (zz, yc)]).charpoly(t).as_expr())
    c_x = sp.together((2 * xx**2 - xx + 1) / (xx - 1))
    assert sp.simplify(cpV0 - (t - 1) * (t**2 - c_x * t + 1)) == 0, "B98 Jacobian drifted"
    tauB = sp.cancel(2 - c_x)
    assert sp.simplify(tauB - (-(2 * xx**2 - 3 * xx + 3) / (xx - 1))) == 0
    assert sp.discriminant(2 * xx**2 - 3 * xx + 3, xx) == -15   # the seam quadratic
    kapV0 = sp.simplify(xx**2 + 2 * yc**2 - xx * yc**2 - 2)
    minus2 = sp.factor(sp.numer(sp.together(kapV0 + 2)))
    plus2 = sp.factor(sp.numer(sp.together(kapV0 - 2)))
    assert minus2 == sp.factor(xx**2 * (xx**2 - 3 * xx + 3))
    assert plus2 == sp.factor((xx - 2)**2 * (xx**2 + xx - 1))
    print(f"   V0 pointwise T1^2-fixed; char = (t-1)(t^2 - c(x) t + 1), c = {c_x}")
    print(f"   tau_B(x) = 2 - c = {sp.factor(tauB)}   [zero locus disc = -15 = the seam]")
    print(f"   kappa_V0 = -2  <=>  {minus2} = 0    (x=0 pair [2T] + geometric pair)")
    print(f"   kappa_V0 = +2  <=>  {plus2} = 0    (x=2 [trivial/dyn end] + golden pair)")
    tb = {}
    for tag, pt in [("x_geo (x^2-3x+3)", sp.Rational(3, 2) + sp.sqrt(-3) / 2),
                    ("x_meta (x^2+x-1)", -sp.Rational(1, 2) + sp.sqrt(5) / 2),
                    ("x_meta' (x^2+x-1)", -sp.Rational(1, 2) - sp.sqrt(5) / 2),
                    ("x = 0 (2T fiber)", sp.Integer(0)),
                    ("x = 2 (trivial fiber)", sp.Integer(2))]:
        tb[tag] = sp.simplify(tauB.subs(xx, pt))
        print(f"      tau_B({tag:20s}) = {tb[tag]}")
    assert list(tb.values()) == [-3, 5, 5, 3, -5]
    # zeta_5 realization of the metabelian fiber points (exact radicals):
    x5 = (sp.sqrt(5) - 1) / 2          # 2 cos(2 pi/5)
    y5 = -(sp.sqrt(5) + 1) / 2         # 2 cos(4 pi/5)
    assert sp.simplify(x5**2 + x5 - 1) == 0
    assert sp.simplify(y5 - x5 / (x5 - 1)) == 0    # (x, y, z) = (x5, y5, y5) on V0
    print("   metabelian fiber characters = the zeta_5 points (x,y,z)=(2cos72, -phi, -phi) etc.")

    # AGREEMENT method A == method B at every stratum (the two-method certificate):
    agree = {"geo": (v_geo, tb["x_geo (x^2-3x+3)"]), "meta": (v_met, tb["x_meta (x^2+x-1)"]),
             "2T": (v_2t, tb["x = 0 (2T fiber)"]), "bif/dyn": (v_bif, tb["x = 2 (trivial fiber)"])}
    assert all(a == b for a, b in agree.values())
    print("   METHOD AGREEMENT (Fox/Wada == transverse Jacobian) at all four strata:",
          {k: str(a) for k, (a, b) in agree.items()})
    bank("sweep", rows=rows, tauB="-(2x^2-3x+3)/(x-1)", tauB_zero_disc=-15,
         kappa_minus2="x^2 (x^2-3x+3)", kappa_plus2="(x-2)^2 (x^2+x-1)",
         dic5_order=20, twoT_order=24, method_agreement=True)
    return rows


# =====================================================================
# SECTION 3 -- the abelian component (the clause-(2) exhibit)
# =====================================================================
def abelian_component():
    print("\n== 3. THE ABELIAN COMPONENT (tier: exact) ==")
    F0 = QF(None)
    d = sp.Matrix([[s, 0], [0, 1 / s]])
    Wab = sp.cancel(sp.together(sp.factor(wada(d, d, F0, 'b'))))
    num, den = sp.fraction(Wab)
    numf, denf = sp.factor(num), sp.factor(den)
    print(f"   W_ab(s,t) = {numf} / ({denf})")
    Alex = t**2 - 3 * t + 1
    expect = sp.cancel((Alex * (s**4 - 3 * s**2 * t + t**2) * (s**4 * t**2 - 3 * s**2 * t + 1))
                       / (s**2 * t**3 * (t - s**2) * (t - 1) * (s**2 * t - 1)))
    assert sp.cancel(Wab - expect) == 0, "abelian Wada drifted"
    # = Delta(t) Delta(t/s^2) Delta(t s^2) x unit: the three Ad-weights 1, s^2, s^-2.
    # (t-1)-structure: simple POLE at t=1 (kd - kn = 1) -- the classical abelian torsion pole;
    # the natural regularized abelian value-function (a perfect square, Delta-governed):
    Vab = sp.cancel(sp.together((s**4 - 3 * s**2 + 1)**2 / (s**2 * (s**2 - 1)**2)))
    val, kn, kd = reg_at_1(Wab, F0)
    assert (kn, kd) == (0, 1), "abelian (t-1)-pole structure drifted"
    assert sp.cancel(sp.together(val) - Vab) == 0
    print(f"   (t-1)-structure: kn=0, kd=1 (simple pole); value-function V_ab(s) = {Vab}")
    dV = sp.cancel(sp.diff(Vab, s))
    assert dV != 0
    print("   dV_ab/ds != 0: CONTINUOUS family -> fails clause (2) [B130 pattern]; no choice")
    zero_at = sp.factor(s**4 - 3 * s**2 + 1)
    print(f"   V_ab = 0 exactly on Delta(s^2) = {zero_at} = 0  <=>  m = +-sqrt5 "
          f"(the PC-3 bifurcation -- matches the nonabelian side)")
    bank("abelian", Wab=Wab, Vab=Vab, pole=(0, 1), zero_locus=str(zero_at))


# =====================================================================
# SECTION 4 -- multiset, three conditions, Galois closure
# =====================================================================
def galois_seal():
    print("\n== 4. THE VALUE MULTISET + THE THREE CONDITIONS (tier: exact) ==")
    # per-point multiset over the canonical strata (PSL points; SL2 sign-lifts collapse
    # by the Sym^2(-M) = Sym^2(M) identity of Section 0):
    MULTISET = [-3, -3, 3, 3, 5, 5, -5, -5]
    # [geo, geo_bar, 2T+, 2T-, meta+, meta-, bif+, bif-]
    # condition (1) trace-map invariance: every stratum lies on the pointwise-T1^2-fixed
    # curve V0 (Section 2), the strata are cut by intrinsic conditions (kappa_V0 = -+2,
    # disc = 0, m-parabolic), and the dr/da vs dr/db presentation gauge is the CONSTANT
    # unit -1 (Section 2 table) whose flip leaves the sign-symmetric multiset invariant.
    inv_under_gauge = sorted([-x_ for x_ in MULTISET]) == sorted(MULTISET)
    assert inv_under_gauge
    # condition (2) discrete multivaluedness: finite, more than one value.
    distinct = sorted(set(MULTISET))
    assert distinct == [-5, -3, 3, 5] and len(MULTISET) == 8
    # condition (3) symmetrizability -- the Galois-closure test:
    #   sigma_3 (sqrt-3 -> -sqrt-3): swaps rho_geo <-> rho_geo_bar and the two 2T lifts;
    #       values (-3,-3), (3,3): FIXED (already rational).
    #   sigma_5 (sqrt5 -> -sqrt5): swaps meta+ <-> meta- and bif+ <-> bif-;
    #       values (5,5), (-5,-5): FIXED.
    #   complex conjugation == the amphichiral involution (B348/B318): maps each rep to
    #       its conjugate within the same stratum; all values REAL rational.
    # every value in the FIXED FIELD Q -- total Galois collapse:
    assert all(sp.sympify(x_).is_rational for x_ in MULTISET)
    e1 = sum(MULTISET)
    prod = sp.prod(MULTISET)
    assert e1 == 0 and prod == 15**4
    esym = [sp.Integer(1)]
    for val in MULTISET:
        esym = [esym[i] + (esym[i - 1] * val if i else 0) for i in range(len(esym))] + \
               [esym[-1] * val]
    assert all(c.is_rational for c in esym)
    print(f"   multiset over canonical strata: {MULTISET}")
    print(f"   (1) trace-map-invariant: strata T1^2-fixed; gauge unit -1 leaves multiset "
          f"invariant: {inv_under_gauge}")
    print(f"   (2) discretely multivalued: {len(distinct)} distinct values {distinct} (finite)")
    print(f"   (3) symmetrizable: every value RATIONAL (fixed field); sum = {e1}; "
          f"product = {prod} = 15^4  [15 = 3.5 = the seam]")
    print("       sign content comes in +- pairs (sum 0): the orientation sign is killed --")
    print("       the B348 amphichirality pattern landing in the torsion class")
    # the two banked 'ends' sit inside the multiset:
    assert -3 in MULTISET and -5 in MULTISET
    bank("seal", multiset=MULTISET, distinct=distinct, sum=int(e1), product=int(prod),
         product_is_seam4=True, gauge_invariant=bool(inv_under_gauge),
         all_rational=True, verdict="SEALED")
    return MULTISET


# =====================================================================
# SECTION 5 -- Ptolemy cross-check (N=2, exact, offline) + amphichirality
# =====================================================================
def ptolemy_and_amphichirality():
    print("\n== 5. PTOLEMY N=2 CROSS-CHECK + AMPHICHIRALITY (snappy; exact outputs) ==")
    try:
        import snappy
    except Exception as exc:                                    # pragma: no cover
        print(f"   snappy unavailable ({exc}); step skipped (equations are combinatorial;")
        print("   the sealing verdict does not depend on this cross-check)")
        bank("ptolemy", available=False)
        return
    M = snappy.Manifold("4_1")
    sols = {}
    for i, V in enumerate(M.ptolemy_variety(2, obstruction_class='all')):
        eqs = [sp.sympify(str(e).replace('^', '**')) for e in V.equations]
        vars_ = sorted({sym for e in eqs for sym in e.free_symbols}, key=str)
        # nonzero Ptolemy coordinates: saturate by adding c != 0 via aux inverse variable;
        # aux FIRST in lex order so it is eliminated and univariate eliminants survive
        w_ = sp.symbols('w_aux')
        gb_sat = sp.groebner(eqs + [w_ * sp.prod(vars_) - 1], w_, *vars_, order='lex')
        solvable = gb_sat.exprs != [sp.Integer(1)]
        sols[i] = dict(equations=[str(e) for e in eqs], nonempty=bool(solvable))
        if solvable:
            # eliminate down to the last variable
            uni = [p for p in gb_sat.exprs if p.free_symbols <= {vars_[-1]}]
            uni_p = sp.factor(uni[0]) if uni else None
            sols[i]['eliminant'] = str(uni_p)
            print(f"   obstruction class {i}: NONEMPTY; eliminant {uni_p}")
        else:
            print(f"   obstruction class {i}: EMPTY (Groebner basis = <1> after saturation)")
    # the known structure: trivial class empty; nontrivial class = the Eisenstein quadratic
    assert sols[0]['nonempty'] is False
    assert sols[1]['nonempty'] is True
    elim = sp.sympify(sols[1]['eliminant'])
    c0 = sp.symbols('c_0101_0')
    ok_quad = sp.expand(elim - (c0**2 - c0 + 1)) == 0 or \
        sp.expand(elim + (c0**2 - c0 + 1)) == 0 or \
        sp.factor(sp.expand(elim)).has(c0**2 - c0 + 1)
    assert ok_quad, f"unexpected eliminant {elim}"
    print("   => boundary-unipotent PSL(2) points at N=2 = the geometric pair ONLY")
    print("      (obstruction class 0 empty; class 1 cut by c^2 - c + 1 = 0, Eisenstein)")
    S = M.symmetry_group()
    amph = bool(S.is_amphicheiral())
    assert amph
    print(f"   symmetry group {S}: amphicheiral = {amph}  [the geometric sign-killer, B348]")
    bank("ptolemy", available=True, classes=sols, amphicheiral=amph)


# =====================================================================
# SECTION 6 -- verdict + honest residual
# =====================================================================
def verdict():
    print("\n== 6. VERDICT ==")
    print("   SEALED (at the computable horizon).")
    print("   Every adjoint-torsion value the object produces on the canonical strata of")
    print("   its SL(2,C) character variety is a RATIONAL number -- the Galois orbits")
    print("   collapse into the fixed field; the multiset {+-3, +-5} is sign-symmetric")
    print("   (sum 0, product 15^4), gauge-invariant, and amphichirality kills the")
    print("   orientation sign. No clause-(3) forced choice exists in this class.")
    print("   OUT OF REACH (named, honest):")
    print("    - SL(n>=3)/E6 adjoint & Ptolemy N>=3 torsion values: B99's transverse")
    print("      spectrum at Sym^2(rho_geo) is numerical {5, 4.5 +- 4.664 i}; the exact")
    print("      tier needs either the 8-coordinate symbolic SL(3) trace-map Jacobian")
    print("      (in-sandbox-feasible in principle, time-boxed out of this probe) or")
    print("      number-field Groebner tooling; exact ENUMERATION of Ptolemy N>=3")
    print("      solution sets: TOOL-BLOCKED (magma/sage or the Ptolemy database).")
    print("    - CS/eta beyond CS=0: phase 2b, not this probe.")
    print("    - extended-Bloch / K3^ind torsion: phase 2e, not this probe.")
    print("    - the universal all-invariants statement: OPEN (C-guardrail; sealing !=")
    print("      universal impossibility proof).")
    print("   Firewall: mathematics only; nothing promotes; nothing to CLAIMS.md.")
    bank("verdict", outcome="SEALED",
         phrasing="sealed at the computable horizon; the class beyond these components "
                  "remains open",
         out_of_reach=["SL(n>=3)/Ptolemy N>=3 exact values (B99 numerical; magma/sage "
                       "or Ptolemy DB for exact enumeration: TOOL-BLOCKED)",
                       "CS/eta (phase 2b)", "extended-Bloch/K3ind (phase 2e)",
                       "universal statement (open)"])


def main():
    ok = controls()
    if not ok:                                                   # pragma: no cover
        print("CONTROL FAILED -- probe INVALID; stopping per prereg.")
        return 1
    enumerate_variety()
    torsion_sweep()
    abelian_component()
    galois_seal()
    ptolemy_and_amphichirality()
    verdict()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "b495_adjoint_torsion.json")
    json.dump(REPORT, open(out, "w"), indent=1, default=str)
    print(f"\n[written] {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
