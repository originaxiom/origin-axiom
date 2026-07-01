"""B347 / gate A (S032-A) -- the cyclic-cover torsion class is a Galois orbit: no forced choice.

Extends B330's mechanism to the first of its named untested classes: REIDEMEISTER/ABELIAN
TORSION OF THE CYCLIC COVERS. The n-fold cyclic cover of the figure-eight complement is the
mapping torus of A^n (fibered knot, monodromy A = [[2,1],[1,1]]), so its torsion module is
coker(A^n - I) -- the P8 object. The scalar torsion factors are the Alexander-polynomial
values {Delta(zeta_n^j)}, Delta(t) = t^2 - 3t + 1 = charpoly(A) (the A-sector polynomial).

Verified here, all exact:
  (i)   the torsion ORDERS are the P8/Lucas ladder: |det(A^n - I)| = L_{2n} - 2
        (= the C5 Lucas-hierarchy values) -- the canonical, fixed-field data;
  (ii)  the factor multiset {Delta(zeta_n^j) : j=1..n-1} is CLOSED under the full
        Galois group Gal(Q(zeta_n)/Q) (index permutation j -> jk), and its elementary
        symmetric functions are INTEGERS (fixed field) -- a symmetrizable Galois orbit,
        the B330 lemma verbatim: the object hands you the orbit, never a member;
  (iii) the torsion GROUPS via Smith normal form -- n=3 gives (Z/4)^2, independently
        re-deriving B326's cover-torsion module;
  (iv)  the deck Z/n action on coker(A^n - I) is fixed-point-free for EVERY n, with a
        one-line uniform cause: det(A - I) = Delta(1) = -1 is a unit, so
        im(A^n - I) = (I + A + ... + A^{n-1}) Z^2 exactly, and the fixed submodule is 0
        -- generalizing B330's n=3 stress test to all n at once.

HONEST TIER NOTE (MB8, generic vs discriminating): Delta(1) = +-1 holds for EVERY knot in
S^3, so (iv)'s no-distinguished-sub-object mechanism is GENERIC-KNOT, not object-specific.
The object-specific content is (i)-(ii): WHICH orbit (the trace-3 / Lucas ladder, the P8 =
C5 tie). Do not read (iv) as figure-eight forcing.

CONDITIONAL (C-guardrail): seals the cyclic-cover ABELIAN torsion class; the nonabelian
(Ptolemy / adjoint) torsion of character-variety components is NOT covered here (B98/B99
record the geometric adjoint torsion tau_1 = -3, a single rational -- canonical -- but the
class as a whole stays untested). Firewalled; nothing to CLAIMS.md. Needs only sympy.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

t = sp.symbols("t")
A = sp.Matrix([[2, 1], [1, 1]])
DELTA = t**2 - 3 * t + 1                     # Alexander polynomial of 4_1 = charpoly(A)


def torsion_orders(nmax=8):
    """(i) |det(A^n - I)| = L_{2n} - 2: the cyclic-cover torsion orders ARE the P8/C5 ladder."""
    F = sp.Matrix([[1, 1], [1, 0]])
    out = {}
    for n in range(2, nmax + 1):
        Tn = abs((A**n - sp.eye(2)).det())
        Ln = sp.trace(F ** (2 * n))          # Lucas number L_{2n}, computed from F itself
        out[n] = (int(Tn), int(Ln - 2))
    return out


def resultant_identity(nmax=6):
    """prod_{j=0}^{n-1} Delta(zeta_n^j) = det(A^n - I) exactly (resultant of Delta and t^n - 1)."""
    out = {}
    for n in range(2, nmax + 1):
        zeta = sp.exp(2 * sp.pi * sp.I / n)
        prod = sp.nsimplify(sp.expand_complex(sp.prod(
            [DELTA.subs(t, zeta**j) for j in range(n)])))
        out[n] = (prod, (A**n - sp.eye(2)).det())
    return out


def factor_orbit_is_galois_closed(n):
    """(ii) the factor multiset {Delta(zeta^j) : j=1..n-1} is a symmetrizable Galois orbit:
    (a) sigma_k: zeta -> zeta^k permutes it (index map j -> jk mod n is a bijection on 1..n-1
        for gcd(k,n)=1 -- structural), and
    (b) its elementary symmetric functions are INTEGERS (they lie in the fixed field Q and
        are algebraic integers) -- the canonical data the object actually determines."""
    perm_ok = all(
        sorted(j * k % n for j in range(1, n)) == list(range(1, n))
        for k in range(1, n) if sp.gcd(k, n) == 1)
    zeta = sp.exp(2 * sp.pi * sp.I / n)
    vals = [DELTA.subs(t, zeta**j) for j in range(1, n)]
    x = sp.symbols("x")
    # extract coefficients FIRST, then simplify each one -- expand_complex on the
    # whole x-polynomial would split x itself into re/im and mangle extraction
    coeffs = sp.Poly(sp.prod([x - v for v in vals]), x).all_coeffs()
    esf = [sp.nsimplify(sp.expand_complex(sp.expand(c))) for c in coeffs[1:]]
    esf_int = all(e.is_integer for e in esf)
    # cross-check: the constant coefficient is (-1)^(n-1) * prod = det(A^n-I)/Delta(1)
    prod_check = sp.Integer((-1) ** (n - 1)) * esf[-1] == (A**n - sp.eye(2)).det() / DELTA.subs(t, 1)
    return perm_ok, esf, esf_int and bool(prod_check)


def torsion_groups(nmax=6):
    """(iii) the torsion groups coker(A^n - I) by Smith normal form. n=3 -> (Z/4)^2 = B326."""
    out = {}
    for n in range(2, nmax + 1):
        S = smith_normal_form(A**n - sp.eye(2))
        out[n] = tuple(abs(int(S[i, i])) for i in range(2))
    return out


def deck_action_fixed_point_free(nmax=6):
    """(iv) the deck generator (induced by A) on coker(A^n - I) fixes only 0, for every n.
    Uniform cause: A^n - I = (A - I) N with N = I + A + ... + A^{n-1}, and det(A - I) =
    Delta(1) = -1 is a UNIT, so [v] fixed <=> (A-I)v in im(A^n - I) <=> v in N Z^2, and
    N Z^2 = (A-I)^{-1} im(A^n - I) = im(A^n - I) exactly. Verified both structurally
    (det(A-I) = -1, N Z^2 = im as lattices) and by brute force on coker representatives."""
    unit = (A - sp.eye(2)).det() == -1
    results = {}
    for n in range(2, nmax + 1):
        M = A**n - sp.eye(2)
        N = sum((A**i for i in range(n)), sp.zeros(2, 2))
        # lattice equality N Z^2 == im(A^n - I): each generates the other over Z
        eq1 = all(x.is_integer for x in (M.inv() * N))     # N Z^2 <= im  requires M^{-1}N integral
        eq2 = all(x.is_integer for x in (N.inv() * M))     # im <= N Z^2
        # brute force: count fixed classes of [v] -> [A v] on Z^2 / M Z^2
        d = abs(int(M.det()))
        fixed = 0
        for a in range(d):
            for b in range(d):
                v = sp.Matrix([a, b])
                w = M.solve((A - sp.eye(2)) * v)           # (A-I)v = M w
                if all(x.is_integer for x in w):
                    fixed += 1
        # each residue class mod M Z^2 is hit d times by the (a,b) grid of size d^2
        results[n] = (eq1 and eq2, fixed // d)             # expect (True, 1): only the zero class
    return unit, results


def generic_tier_note():
    """MB8 honesty: Delta(1) = -1 (knot determinant condition) -- the fixed-point-freeness
    mechanism is generic to all knots in S^3, NOT figure-eight-specific."""
    return int(DELTA.subs(t, 1))


if __name__ == "__main__":
    print("B347 -- the cyclic-cover torsion class as a Galois orbit (gate A extension)\n")
    print("(i) torsion orders |det(A^n-I)| vs Lucas L_2n - 2 (the P8/C5 ladder):")
    print("   ", torsion_orders())
    print("(ii) factor multisets Galois-closed with integer symmetric functions:")
    for n in (3, 4, 5, 6):
        perm, esf, ok = factor_orbit_is_galois_closed(n)
        print(f"    n={n}: perm={perm}, esf={esf}, all integers={ok}")
    print("(iii) torsion groups (SNF):", torsion_groups(), " [n=3 = (4,4) = B326]")
    unit, res = deck_action_fixed_point_free()
    print(f"(iv) det(A-I) = -1 (unit): {unit}; per-n (lattice N Z^2 = im, #fixed classes): {res}")
    print(f"\nMB8 note: Delta(1) = {generic_tier_note()} -- generic-knot mechanism, not object-specific.")
    print("CONDITIONAL: the cyclic-cover abelian-torsion class is a symmetrizable Galois orbit +")
    print("canonical integers; no forced choice in this class. Nonabelian/Ptolemy torsion stays open.")
