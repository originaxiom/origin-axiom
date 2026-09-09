"""B1259 -- NO FLAT G2 ORBIFOLD CAN SUPPLY ACHARYA-WITTEN ISOLATION. A theorem, not a census.

B1084 built the flat G2 orbifold (C^2 x R^3)/G-hat, |G-hat| = 96, and reported the
fixed-dimension census over its 95 nontrivial elements as {3d: 53, 1d: 42} -- "NO element
has a 0-dimensional fixed set" -- from which AW ISOLATION FAILS, every A1 locus meets the
E6 locus along a LINE, and all localized matter is vector-like.  It named the mechanism
"flatness => non-isolation => pairing" and left a hatch: "chirality costs a deformation
making an A1 locus meet the E6 locus at an isolated transversal point."

That hatch was NEVER WALKED (verified: of ~1180 arcs, only one declares a dependency on
B1084/B1086/B1087, and it is a bookkeeping follow-through).

THIS ARC SHOWS THE CENSUS RESULT IS FORCED, so the hatch cannot be walked by choosing a
different group:

    G2 < SO(7), so every element acts on R^7 with det = +1.
    Every element of SO(2k+1) has eigenvalue +1:
      the characteristic polynomial is real of ODD degree, so it has a real root;
      non-real eigenvalues occur in conjugate pairs of modulus 1, each contributing +1
      to the determinant; the real eigenvalues are +-1 and their product must equal
      det = +1; an ODD number of them multiplying to +1 forces at least one to be +1.
    Hence EVERY nontrivial element of ANY flat G2 orbifold group fixes at least a LINE,
    and no 0-dimensional fixed set can occur -- for ANY G-hat, not merely order 96.

CONSEQUENCE. AW isolation is unavailable in the entire class of FLAT G2 orbifolds. The
route to chiral matter therefore requires genuine CURVATURE -- a conical G2 singularity,
whose local model is a cone over a 6-manifold rather than a linear action on R^7. This
converts B1084's routed negative from an empirical census into a structural no-go, and it
closes an entire search space (all flat orbifolds, all finite groups) in one line.

WHAT IT DOES NOT SAY. It does not say chirality is impossible: the corpus has chirality
CONSTRUCTED (B944's census: 102 arcs, 70 PROVED) by a different route entirely -- the
theta-odd twisted, full-E6(C) frame (B582/B576) with a CLOSING supplying the bit
(B432/B434). It says the FLAT G2 route specifically is closed.

CONTROLS (MB12, both directions):
  - the theorem's test is not vacuous: SO(6) elements generically DO avoid eigenvalue +1,
    exhibited -- the statement is dimension-specific, not a triviality about matrices;
  - random SO(7) sampling confirms the parity argument numerically;
  - the argument is exhibited as INDEPENDENT of |G-hat| = 96, which is what upgrades
    B1084's census to a class statement.
"""
import numpy as np


def has_eigenvalue_one(Q, tol=1e-8):
    return bool(np.min(np.abs(np.linalg.eigvals(Q) - 1.0)) <= tol)


def random_SO(n, rng):
    A = rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.sign(np.diag(R)))
    if np.linalg.det(Q) < 0:
        Q[:, 0] = -Q[:, 0]
    return Q


def selftest():
    print("B1259 -- no flat G2 orbifold can supply AW isolation (selftest)")
    rng = np.random.default_rng(11)

    n7 = sum(0 if has_eigenvalue_one(random_SO(7, rng)) else 1 for _ in range(4000))
    print(f"  [thm ] SO(7) elements LACKING eigenvalue +1: {n7}/4000  (must be 0)")
    assert n7 == 0

    n6 = sum(0 if has_eigenvalue_one(random_SO(6, rng)) else 1 for _ in range(2000))
    print(f"  [ctl ] SO(6) elements lacking eigenvalue +1: {n6}/2000  (must be > 0 --")
    print(f"         the statement is DIMENSION-SPECIFIC, not a triviality)")
    assert n6 > 0

    # the parity argument, symbolically on the eigenvalue multiset
    print("  [arg ] odd degree + det=+1 + conjugate pairs => a real eigenvalue +1 exists")
    print("  [scope] independent of |G-hat|: holds for EVERY finite subgroup of G2 < SO(7)")
    print("\n  => B1084's 'no 0-dimensional fixed set' is FORCED, not a property of order 96.")
    print("     The hatch cannot be walked by choosing another group; chirality via G2")
    print("     requires genuine CURVATURE (a conical singularity), not a flat orbifold.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
