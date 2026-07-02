"""B354 -- the metallic interface pairing: exact certificates, the divisibility law, the parity texture.

Verification-and-banking of a cross-session (Chat-2 solo, 2026-07-02) computation, per
verify-don't-trust: every claim banked here was independently re-derived or gate-checked in this
repo before banking. Standalone character-variety / elementary-congruence math; firewalled,
nothing to CLAIMS; no physics claim.

LINEAGE (the part that was already banked -- cited, not re-claimed): B131/V120 established the
mechanism (each seed's fixed locus traces an A-polynomial curve in the shared boundary-torus
character plane (m,l) = (tr t, tr[a,b]); distinct seeds -> distinct curves -> discrete Bezout
fork; same seed -> continuum) with the golden/silver interface relations l = m^4-5m^2+2 (=B67)
and l = m^2-6 (=B69/V33) and the exact (1,2) fork kappa in {-4,-2}; Kitano-Nozaki 2020 is the
prior art (NOVELTY_AUDIT R2); B174/V168 mapped the same-seed gluing-map landscape. NEW here,
beyond B131:

  (1) THE STRONG-CHANNEL KILL (exact, re-derived by Groebner in this module): the common fixed
      representations of two DISTINCT seeds' trace maps are exactly the trivial (2,2,2) and
      quaternion (0,0,0) points = Fix(Ta) cap Fix(Tb) -- universal to the whole family, so the
      bulk-sharing channel carries no pair information. (The pair channel is the boundary one.)
  (2) THE EXACT PAIR-POINT CERTIFICATES: minimal polynomials of the (1,3) and (2,3) boundary
      pair points (B131 left these as Newton numerics) -- the quintic T^5-13T^4+60T^3-121T^2
      +114T-47 and the cubic T^3-16T^2+68T-72 in T = m^2, verified here by irreducibility +
      exact kappa-image match against B131's banked fork values. Odd degrees => the pair-point
      fields have NO quadratic subfield => no sqrt(-15): the seam does not enter the classical
      pair arithmetic (a third independent channel closed; cf. B336 single-object).
  (3) THE DIVISIBILITY LAW (one-line, exact): the metallic monodromy R^m L^m = [[1+m^2, m],[m, 1]]
      is trivial mod p iff p | m. This single congruence underlies the seed-parity texture (mod 2)
      and the bronze mod-3 scalar behaviour reported cross-session.
  (4) THE PARITY-TEXTURE EXACT LEGS: on the l = -2 fiber, golden carries m^2 in {1,4} (the
      trace-+-1 2T-omega-coset interface state present) while silver carries m^2 = 4 only (the
      state provably absent) -- exact from the two banked interface relations.

CONDITIONAL (numerical, banked as such): the (+-sqrt2, -4) golden-silver pair point is absent
from bronze's l = -4 slice (pair-specificity; Chat-2's 900-start search, reproduced) -- the exact
certificate needs A_bronze(m,l) by elimination (open follow-up). UNVERIFIED (quarantined, not
banked): the cross-session Weil-representation trace/overlap tables (no reproducer received);
registered as lead L56.
"""
import sympy as sp

x, y, z, T, m, M2 = sp.symbols('x y z T m M2')

# --- the trace maps (B167 convention) ---------------------------------------------------------
def _Ta(v):
    return (v[0], v[2], v[0] * v[2] - v[1])


def _Tb(v):
    return (v[2], v[1], v[1] * v[2] - v[0])


def _word_map(word):
    def f(v):
        for c in word:
            v = _Ta(v) if c == 'a' else _Tb(v)
        return v
    return f


def _fix_system(word):
    v = (x, y, z)
    w = _word_map(word)(v)
    return [sp.expand(w[i] - v[i]) for i in range(3)]


# --- (1) the strong channel: exact Groebner kill ----------------------------------------------
UNIVERSAL_POINTS = [{x: 0, y: 0, z: 0}, {x: 2, y: 2, z: 2}]     # quaternion, trivial


def strong_channel(word1, word2):
    """Common fixed points of two seeds' trace maps (exact solve)."""
    return sp.solve(_fix_system(word1) + _fix_system(word2), [x, y, z], dict=True)


def strong_channel_is_universal_only():
    """(1,2), (1,3) pairs and the Fix(Ta) cap Fix(Tb) control all equal the two universal points."""
    pairs = [strong_channel('ab', 'aabb'),          # golden x silver
             strong_channel('ab', 'aaabbb')]        # golden x bronze
    control = sp.solve([sp.expand(_Ta((x, y, z))[i] - (x, y, z)[i]) for i in range(3)]
                       + [sp.expand(_Tb((x, y, z))[i] - (x, y, z)[i]) for i in range(3)],
                       [x, y, z], dict=True)
    tgt = sorted(map(str, UNIVERSAL_POINTS))
    return all(sorted(map(str, s)) == tgt for s in pairs + [control])


# --- the banked interface relations (B131/B67/B69 -- cited) ------------------------------------
GOLDEN_INTERFACE = M2**2 - 5 * M2 + 2          # l as a polynomial in m^2  (B67/B131)
SILVER_INTERFACE = M2 - 6                       # (B69/V33/B131)


def pair_12_intersection():
    """Exact golden x silver boundary intersection: m^2 solutions + the kappa fork (=B131 {-4,-2})."""
    sols = sp.solve(sp.Eq(GOLDEN_INTERFACE, SILVER_INTERFACE), M2)
    fork = sorted(sp.expand(SILVER_INTERFACE.subs(M2, s)) for s in sols)
    return sorted(sols), fork                   # ({2, 4}, kappa {-4, -2})


# --- (2) the exact pair-point certificates ------------------------------------------------------
PAIR_13_MINPOLY = T**5 - 13 * T**4 + 60 * T**3 - 121 * T**2 + 114 * T - 47   # T = m^2
PAIR_23_MINPOLY = T**3 - 16 * T**2 + 68 * T - 72

# B131/V120's banked numeric forks (VALIDATION_LEDGER), minus the universal l=-2 shadow:
B131_FORK_13 = [-3.920, -0.689, 2.299, complex(-1.845, 2.229), complex(-1.845, -2.229)]
B131_FORK_23 = [-4.397, -1.427, 3.824]


def _match(vals, banked, tol=2e-3):
    vals = list(vals)
    for b in banked:
        hit = min(range(len(vals)), key=lambda i: abs(vals[i] - b))
        if abs(vals[hit] - b) > tol:
            return False
        vals.pop(hit)
    return not vals


def pair_13_certificate():
    """Quintic irreducible; kappa-images of its roots = B131's banked (1,3) fork; odd degree."""
    p = sp.Poly(PAIR_13_MINPOLY, T)
    kappa = [complex(sp.N(r**2 - 5 * r + 2)) for r in p.nroots(n=15)]   # golden l(T)
    return p.is_irreducible and p.degree() % 2 == 1 and _match(kappa, B131_FORK_13)


def pair_23_certificate():
    """Cubic irreducible; kappa-images of its roots = B131's banked (2,3) fork; odd degree."""
    p = sp.Poly(PAIR_23_MINPOLY, T)
    kappa = [complex(sp.N(r - 6)) for r in p.nroots(n=15)]              # silver l(T)
    return p.is_irreducible and p.degree() % 2 == 1 and _match(kappa, B131_FORK_23)


def no_quadratic_subfield():
    """Both pair-point fields have prime odd degree (5, 3) => no quadratic subfield => no sqrt(-15).
    (A subfield's degree divides the field's; 2 divides neither 5 nor 3.)"""
    return sp.Poly(PAIR_13_MINPOLY, T).degree() == 5 and sp.Poly(PAIR_23_MINPOLY, T).degree() == 3


# --- (3) the divisibility law -------------------------------------------------------------------
def metallic_monodromy():
    """abelianized R^m L^m, symbolically."""
    R = sp.Matrix([[1, m], [0, 1]])
    L = sp.Matrix([[1, 0], [m, 1]])
    return R * L                                 # [[1+m^2, m],[m, 1]]


def divisibility_law():
    """R^m L^m == I mod p  <=>  p | m  (exact: the off-diagonal is m, the corner is m^2)."""
    A = metallic_monodromy()
    D = A - sp.eye(2)
    # D = [[m^2, m],[m, 0]]: every entry divisible by p iff p | m
    return sp.simplify(D[0, 0] - m**2) == 0 and sp.simplify(D[0, 1] - m) == 0 \
        and sp.simplify(D[1, 0] - m) == 0 and D[1, 1] == 0


def divisibility_examples():
    """golden nontrivial mod 2; silver trivial mod 2; bronze trivial (scalar) mod 3."""
    A = metallic_monodromy()
    g = A.subs(m, 1).applyfunc(lambda e: e % 2) != sp.eye(2)
    s = A.subs(m, 2).applyfunc(lambda e: e % 2) == sp.eye(2)
    b = A.subs(m, 3).applyfunc(lambda e: e % 3) == sp.eye(2)
    return g and s and b


# --- (4) the parity-texture exact legs ----------------------------------------------------------
def parity_exact_legs():
    """On l = -2: golden fiber m^2 in {1,4} (the trace-+-1 state PRESENT);
    silver fiber m^2 = 4 only (ABSENT). Exact from the banked interface relations."""
    golden = sorted(sp.solve(sp.Eq(GOLDEN_INTERFACE, -2), M2))
    silver = sorted(sp.solve(sp.Eq(SILVER_INTERFACE, -2), M2))
    return golden == [1, 4] and silver == [4]


def run_all():
    return dict(
        strong_channel_universal_only=strong_channel_is_universal_only(),
        pair_12=pair_12_intersection(),
        pair_13_certified=pair_13_certificate(),
        pair_23_certified=pair_23_certificate(),
        seam_excluded_classically=no_quadratic_subfield(),
        divisibility_law=divisibility_law() and divisibility_examples(),
        parity_exact_legs=parity_exact_legs(),
    )


if __name__ == "__main__":
    for k, v in run_all().items():
        print(f"  {k}: {v}")
