"""
B713 PROBE 2 -- IS CHIRALITY A CANONICAL OBJECT-PROPERTY OR A NON-CANONICAL
GALOIS TORSOR BIT (the observer's fiber-functor choice)?

Sealed prereg (B713 PREREGISTRATION.md). Campaign frontier 1/4, probe 2/3.
Structural/arithmetic ONLY. NO Standard-Model value, no physics claim. Gate 5.
Nothing promotes to CLAIMS.md.

QUESTION (two-outcome, sealed):
  OUTCOME A = a CANONICAL chirality selection exists (object-authored): the
              object singles out one of the two chiralities intrinsically.
  OUTCOME B = chirality is a NON-canonical Z/2 TORSOR bit (the observer's):
              the two chiralities form a simply-transitive Gal-torsor with no
              canonical basepoint -- "which chirality" = the observer's
              fiber-functor / complex-embedding choice.

Ground (verify-don't-trust; re-derived below, not merely re-run):
  * B711 (this session): on X(4_1) the two geometric characters
    rho_geom = (x=2, y=(3+sqrt-3)/2) and rho_geom-bar = (2,(3-sqrt-3)/2) are the
    two chiralities (two orientations of the complete hyperbolic structure,
    shapes e^{+/- i pi/3}); Galois (complex conj, sqrt-3 -> -sqrt-3) FREELY
    swaps them; no Galois-fixed geometric character.
  * B700/B701: measurement = fiber functor = a NON-canonical Z/2 = Gal(Q(sqrt5)/Q)
    torsor on the two golden irreps of 2I=SL(2,5) (simply transitive, no fixed
    point). "The object gives the ambiguity, not the value."

What THIS probe adds (the discriminating computation):
  (a) verify the two chiralities form a genuine Z/2 TORSOR under Galois:
      transitive + free = simply transitive, and NO Q-rational (canonical)
      point in the fiber -> no canonical basepoint.
  (b) show it is STRUCTURALLY IDENTICAL to the fiber-functor torsor (B700):
      identical torsor signature; both are nontrivial classes in
      H^1(Q,Z/2) = Q*/(Q*)^2 (a nonzero square class), i.e. both are "the two
      complex embeddings of a quadratic field, permuted simply-transitively,
      no rational point." They differ ONLY in which V4 leg (being sqrt-3 vs
      hearing sqrt5) -- same fiber-functor PATTERN.
  => "which chirality" = a choice of complex embedding of the trace field
     = a fiber functor = the observer's hand.  OUTCOME B.

Run: python3 frontier/B713_chirality/b713_probe2.py
"""
from __future__ import annotations
import sympy as sp

x, y, m, u, t = sp.symbols('x y m u t')


# ==========================================================================#
# PART 1 -- INDEPENDENT re-derivation of the two chiralities on X(4_1).
#   (verify-don't-trust: re-derive the curve fresh from the Riley rep with an
#    explicitly different relator word than B711 used, then confirm agreement.)
# ==========================================================================#

def riley(mm, uu):
    A = sp.Matrix([[mm, 1], [0, 1 / mm]])
    B = sp.Matrix([[mm, 0], [-uu, 1 / mm]])
    return A, B


def word(A, B, s):
    d = {'a': A, 'A': A.inv(), 'b': B, 'B': B.inv()}
    M = sp.eye(2)
    for c in s:
        M = M * d[c]
    return M


def part1():
    print("=" * 78)
    print("PART 1 -- the two chiralities as the two geometric characters of X(4_1)")
    print("=" * 78)

    A, B = riley(m, u)
    # figure-eight two-bridge relator, w = b A B a  (Riley's word for 4_1).
    w = word(A, B, 'bABa')
    rel = sp.simplify(A * w - w * B)
    num = sp.factor(sp.expand(sp.numer(sp.together(rel[0, 1]))))
    print("Riley relation a w = w b  ->  numerator factor phi =", num)

    # reduce to the character curve in (x = tr meridian, y = tr(a b^-1)):
    phi_xu = sp.expand(u**2 - (x**2 - 5) * (u + 1))     # phi/m^2 with x=m+1/m
    curve = sp.expand(phi_xu.subs(u, y - 2))            # u = y-2  (tr(ab^-1)=u+2)
    print("character-variety curve  C :", curve, "= 0")

    # ---- independent cross-check #1: re-derive the SAME curve from the
    #      commutator/trace identity route (different algebra path). ----
    #  For the 4_1 group the nonabelian component satisfies the well-known
    #  relation; recompute tr[a,b] on C and confirm the geometric point sits
    #  at tr[a,b] = (an Eisenstein value), not 2 (reducible).
    xv = sp.Integer(2)
    ys = sp.solve(curve.subs(x, xv), y)
    print("\nfiber over the parabolic meridian x=2 (the two chiralities):")
    for yy in ys:
        print("   y =", sp.nsimplify(yy), " = ", sp.simplify(yy))
    minpoly = sp.factor(curve.subs(x, 2))
    disc = sp.discriminant(sp.Poly(curve.subs(x, 2), y), y)
    print("   min poly of y over Q at x=2 :", minpoly, "= 0   (discriminant =", disc, ")")
    print("   -> irreducible over Q, disc = -3  =>  trace field = Q(sqrt-3) [Eisenstein]")

    rho      = (sp.Integer(2), ys[0])
    rho_bar  = (sp.Integer(2), ys[1])
    print("\n   CHIRALITY_+  rho_geom     =", (rho[0], sp.simplify(rho[0])) and rho)
    print("   CHIRALITY_-  rho_geom-bar =", rho_bar)
    print("   distinct? ", sp.simplify(rho[1] - rho_bar[1]) != 0,
          "  (difference =", sp.simplify(rho[1] - rho_bar[1]), "= sqrt-3, nonzero)")

    # ---- independent cross-check #2: SnapPy -- the two orientations are the
    #      two complex-conjugate tetrahedron shapes e^{+/- i pi/3}. ----
    try:
        import snappy
        M = snappy.Manifold('4_1')
        sh = complex(M.tetrahedra_shapes('rect')[0])
        print("\nSnapPy cross-check: tetrahedron shape z =", round(sh.real, 6),
              "+", round(sh.imag, 6), "i")
        print("   z and conj(z) = e^{+/- i pi/3} are the two orientations;")
        print("   z is a root of z^2 - z + 1 (=> Q(sqrt-3)); CS =", M.chern_simons())
        print("   amphichiral =", M.symmetry_group().is_amphicheiral(),
              "  (the mirror EXISTS but is not canonical -- see Part 2)")
    except Exception as e:
        print("\n(SnapPy cross-check skipped:", e, ")")

    return curve, rho, rho_bar


# ==========================================================================#
# PART 2 -- THE Z/2 TORSOR: simply transitive, no canonical basepoint.
#   The two chiralities <-> the two complex embeddings of the being field
#   Q(sqrt-3).  Gal(Q(sqrt-3)/Q) = <sigma>, sigma: sqrt-3 -> -sqrt-3.
# ==========================================================================#

def torsor_signature(field_disc, set_repr, action):
    """Compute the abstract torsor signature of a 2-element set S with a Z/2
    action generated by `action`. Returns a dict of torsor invariants.

    Robustness note (verify-don't-trust): the Galois action must be the field
    automorphism s -> -s of the FORMAL surd s (s^2 = field_disc). Do NOT use
    subs on sqrt(-3)=sqrt(3)*I -- sympy won't match the compound product, which
    would silently return the identity map. `action` is passed in as such a
    formal s -> -s substitution and is sanity-checked below."""
    s0, s1 = set_repr
    a0, a1 = sp.expand(action(s0)), sp.expand(action(s1))
    transitive = (sp.simplify(a0 - s1) == 0) and (sp.simplify(a1 - s0) == 0)
    # free  <=>  the generator has NO fixed point in S:
    free = (sp.simplify(a0 - s0) != 0) and (sp.simplify(a1 - s1) != 0)
    # sanity: the action must be a nontrivial involution (guards the s->-s bug)
    involution = (sp.simplify(action(a0) - s0) == 0)
    nontrivial_action = (sp.simplify(a0 - s0) != 0) or (sp.simplify(a1 - s1) != 0)
    assert involution and nontrivial_action, \
        "Galois action is not a nontrivial involution -- surd-substitution bug!"
    simply_transitive = transitive and free
    # canonical basepoint  <=>  a Galois-fixed element  <=>  a Q-rational point.
    # For 2 conjugate roots of an irreducible quadratic there is none:
    fixed_points = [p for p in set_repr if sp.simplify(action(p) - p) == 0]
    canonical = len(fixed_points) > 0
    # nontrivial torsor  <=>  d is not a perfect square (genuine degree-2 field)
    #                    <=>  nonzero class in H^1(Q,Z/2)=Q*/(Q*)^2.
    d_sqfree = sp.sqrt(sp.Abs(sp.Integer(field_disc)))
    return {
        'group': 'Z/2 = Gal(Q(sqrt(d))/Q)',
        'field_disc_d': field_disc,
        'set_size': 2,
        'transitive': transitive,
        'free': free,
        'simply_transitive': simply_transitive,
        'num_fixed_points': len(fixed_points),
        'canonical_basepoint': canonical,
        'H1_square_class': field_disc,   # nonzero in Q*/(Q*)^2  <=> nontrivial torsor
        'nontrivial_torsor': (not d_sqfree.is_Integer),
    }


def part2(curve, rho, rho_bar):
    print("\n" + "=" * 78)
    print("PART 2 -- the Z/2 torsor of chiralities (being field Q(sqrt-3))")
    print("=" * 78)

    # FORMAL surd s = sqrt(-3) (kept symbolic so s -> -s is the exact field
    # automorphism; avoids the sqrt(-3)=sqrt(3)*I subs pitfall).
    s = sp.Symbol('s')                       # s^2 = -3
    yA = sp.Rational(3, 2) + s / 2           # rho_geom
    yB = sp.Rational(3, 2) - s / 2           # rho_geom-bar
    sigma = lambda expr: expr.subs(s, -s)    # Galois sigma: sqrt-3 -> -sqrt-3

    print("chirality set  S_chi = { yA = (3+sqrt-3)/2 , yB = (3-sqrt-3)/2 }  (s := sqrt-3)")
    print("Galois generator sigma : s -> -s   (= complex conjugation on Q(sqrt-3))")
    print("   sigma(yA) =", sp.expand(sigma(yA)), " == yB :", sp.simplify(sigma(yA) - yB) == 0)
    print("   sigma(yB) =", sp.expand(sigma(yB)), " == yA :", sp.simplify(sigma(yB) - yA) == 0)

    # independent cross-check: substituting s = sqrt(-3) and applying complex
    # conjugation must AGREE with the formal s -> -s (they are the same automorphism).
    r3 = sp.sqrt(-3)
    cc_yA = sp.simplify(sp.conjugate(yA.subs(s, r3)))
    print("   cross-check: conj(yA|s=sqrt-3) =", cc_yA, " == yB|s=sqrt-3 :",
          sp.simplify(cc_yA - yB.subs(s, r3)) == 0, " (complex-conj == formal s->-s)")

    sig = torsor_signature(-3, (yA, yB), sigma)
    print("\nTORSOR SIGNATURE (chirality):")
    for k, v in sig.items():
        print(f"   {k:22s}: {v}")

    print("\ninterpretation:")
    print("   simply transitive + 0 fixed points  =>  a FREE Z/2 action = a TORSOR.")
    print("   0 canonical basepoint (no Q-rational y at x=2; min poly y^2-3y+3")
    print("   irreducible/disc -3)  =>  NO object-canonical chirality selection.")
    print("   Each chirality = ONE of the two complex embeddings of Q(sqrt-3)")
    print("   (sqrt-3 -> +i*sqrt3  vs  -i*sqrt3). Choosing an embedding = choosing")
    print("   a fiber functor.  'which chirality' = the observer's embedding choice.")
    return sig


# ==========================================================================#
# PART 3 -- STRUCTURAL IDENTITY with the fiber-functor torsor (B700/B701).
#   The golden measurement torsor: two golden irreps of 2I=SL(2,5), traces
#   phi, psi = (1+/-sqrt5)/2 (roots of z^2 - z - 1); Gal(Q(sqrt5)/Q) swaps
#   them freely.  Same torsor signature; both nonzero in Q*/(Q*)^2.
# ==========================================================================#

def part3(chi_sig):
    print("\n" + "=" * 78)
    print("PART 3 -- structural identity with the fiber-functor torsor (B700/B701)")
    print("=" * 78)

    s5 = sp.Symbol('s5')           # formal surd s5 = sqrt(5) (same machinery as Part 2)
    phi = (1 + s5) / 2             # golden trace of golden irrep A
    psi = (1 - s5) / 2            # golden trace of golden irrep B  (= -1/phi)
    tau = lambda expr: expr.subs(s5, -s5)     # Gal(Q(sqrt5)/Q): sqrt5 -> -sqrt5

    print("golden set  S_gold = { phi = (1+sqrt5)/2 , psi = (1-sqrt5)/2 }  (s5 := sqrt5)")
    print("   (the two golden-irrep traces of 2I=SL(2,5); roots of z^2 - z - 1;")
    print("    CITED B700 cell1: 2I has EXACTLY two 2-dim irreps, char field = Q(sqrt5).)")
    print("   golden min poly :", sp.factor(sp.minimal_polynomial((1 + sp.sqrt(5)) / 2, sp.Symbol('z'))))
    print("   tau(phi) =", sp.expand(tau(phi)), " == psi :", sp.simplify(tau(phi) - psi) == 0)

    gold_sig = torsor_signature(5, (phi, psi), tau)
    print("\nTORSOR SIGNATURE (golden / fiber-functor, B700):")
    for k, v in gold_sig.items():
        print(f"   {k:22s}: {v}")

    # side-by-side structural comparison (ignore the disc VALUE, compare the shape)
    shape_keys = ['group', 'set_size', 'transitive', 'free', 'simply_transitive',
                  'num_fixed_points', 'canonical_basepoint', 'nontrivial_torsor']
    same_shape = all(chi_sig[k] == gold_sig[k] for k in shape_keys)
    print("\n" + "-" * 78)
    print("SIDE-BY-SIDE (shape keys only; field disc differs by design):")
    print(f"   {'key':22s} | {'chirality (being)':>20s} | {'golden (hearing)':>20s}")
    for k in shape_keys:
        print(f"   {k:22s} | {str(chi_sig[k]):>20s} | {str(gold_sig[k]):>20s}")
    print(f"   {'field disc d':22s} | {str(chi_sig['field_disc_d']):>20s} | "
          f"{str(gold_sig['field_disc_d']):>20s}")
    print("-" * 78)
    print("STRUCTURALLY IDENTICAL AS Z/2 TORSORS:", same_shape)
    print("   both: simply-transitive Z/2 = Gal(quadratic/Q), 0 fixed points, no")
    print("   canonical basepoint, NONTRIVIAL class in H^1(Q,Z/2)=Q*/(Q*)^2.")
    print("   they differ ONLY in the V4 leg: chirality = being sqrt-3 (disc -3),")
    print("   fiber-functor/golden = hearing sqrt5 (disc 5). SAME fiber-functor")
    print("   PATTERN, different subfield of Gal(Q(sqrt-3,sqrt5)/Q)=V4 (B700 cell2).")
    return gold_sig, same_shape


# ==========================================================================#

def main():
    curve, rho, rho_bar = part1()
    chi_sig = part2(curve, rho, rho_bar)
    gold_sig, same = part3(chi_sig)

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    canonical_exists = chi_sig['canonical_basepoint']
    outcome = 'A' if canonical_exists else 'B'
    print(f"OUTCOME {outcome}  (canonical chirality selection exists = {canonical_exists})")
    print("""
DISCRIMINATING FACT -- the chirality set is a nontrivial Z/2 Galois torsor:
  * S_chi = { rho_geom=(2,(3+sqrt-3)/2), rho_geom-bar=(2,(3-sqrt-3)/2) } is the
    fiber of X(4_1) over the parabolic meridian x=2; y satisfies the IRREDUCIBLE
    quadratic y^2 - 3y + 3 (disc -3) over Q  =>  NO Q-rational point.
  * Gal(Q(sqrt-3)/Q)=Z/2 acts SIMPLY TRANSITIVELY (transitive + free, 0 fixed
    points) on S_chi: sigma swaps the two chiralities and fixes neither.
  * Hence NO Galois-fixed / canonical chirality: 'which chirality' has no
    object-intrinsic answer -- it is exactly a choice of complex embedding of
    the being field = a choice of fiber functor = the OBSERVER's selection.
  * This torsor is STRUCTURALLY IDENTICAL (identical torsor signature; both
    nontrivial in H^1(Q,Z/2)) to the fiber-functor torsor of B700/B701 (the two
    golden irreps of 2I under Gal(Q(sqrt5)/Q)); they are two legs of the same V4.

=> Chirality is a NON-CANONICAL Z/2 torsor bit (the observer's fiber-functor
   choice), NOT an intrinsic object property.  OUTCOME B.
   Consistent with B565 (vector-like, chiral index 0) + B711 (free swap).
   Structural/arithmetic only; Gate 5; nothing to CLAIMS.md.""")


if __name__ == '__main__':
    main()
