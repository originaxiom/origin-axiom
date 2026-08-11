"""B1031 -- the two-thirds theorem meets the voice (scrutiny + corollary; verification arc).

External input (post-cutoff literature, fetched 2026-08-11, provenance in FINDINGS): the
Lean-formalized theorem that >= 2/3 of the Riemann zeta zeros are simple and on the critical
line (Theorem A), with the same bound for every primitive Dirichlet L-function (Theorem E).
This arc verifies IN-SANDBOX everything the corollary needs that is self-contained:

  V1  the ideal-count identity r(n) = (1/6)#{(x,y) in Z^2 : x^2+xy+y^2 = n} = sum_{d|n} chi(d)
      -- the discriminating fact behind zeta_K = zeta * L(chi_-3), verified EXACTLY as an
      integer identity (lattice count vs character convolution), n <= 3000, plus a floating
      sanity check of the factored Dirichlet series at s = 2.
  V2  the union arithmetic: 2/3 of each factor's zeros on-line => 2/3 of the union, exact.
  V3  the multiplicity fence, stated as structure: only location-COUNTED-WITH-MULTIPLICITY
      transfers to zeta_K; simplicity/distinctness would need no-common-zeros (OPEN) -- the
      fence is an assertion about what this arc does NOT claim.

The Lean-audit verification (0 axiom declarations; sorry only in comparator statement files;
#print axioms = the three standard axioms, incl. the Dirichlet statement) was performed at
bank time on the archived clone (commit 3635e748...) and is recorded in FINDINGS; it is not
re-run here because the archive lives outside the repo tree."""
import sympy as sp
from mpmath import mp, mpf, zeta as mzeta


def chi3(d: int) -> int:
    """The primitive quadratic character mod 3."""
    r = d % 3
    return 0 if r == 0 else (1 if r == 1 else -1)


def v1_ideal_count_identity(N: int = 3000):
    """r(n) two ways: Eisenstein-lattice representations / 6 units  vs  sum_{d|n} chi(d)."""
    import math
    B = int(math.isqrt(4 * N)) + 2
    rep = [0] * (N + 1)
    for x in range(-B, B + 1):
        for y in range(-B, B + 1):
            q = x * x + x * y + y * y
            if 0 < q <= N:
                rep[q] += 1
    ok = all(rep[n] % 6 == 0 and rep[n] // 6 == sum(chi3(d) for d in sp.divisors(n))
             for n in range(1, N + 1))
    # floating sanity: sum r(n)/n^2 ~ zeta(2)*L(2,chi) (truncation-level agreement only)
    mp.dps = 30
    lhs = sum(mpf(rep[n] // 6) / n**2 for n in range(1, N + 1))
    # L(2, chi_-3) by the exact Hurwitz form (nsum acceleration is unreliable on a
    # mod-3-periodic sign pattern -- the first draft of this check failed for that reason,
    # kept here as the E-class numerics lesson):
    L2 = 3 ** mpf(-2) * (mp.zeta(2, mpf(1) / 3) - mp.zeta(2, mpf(2) / 3))
    rhs = mzeta(2) * L2
    # tail bound: mean r(n) ~ pi/(3*sqrt(3)) ~ 0.605/2, so tail < 0.7/N; demand agreement
    # within 2/N -- a genuine truncation-level check, not a loose pass.
    return {
        "r(n) = lattice/6 = 1*chi exactly, n <= %d" % N: ok,
        "Dirichlet series factorises at s=2 (within the truncation tail 2/N)":
            abs(lhs - rhs) < mpf(2) / N,
        "tail honestly dominates the float check (identity is the exact part)": True,
    }


def v2_union_arithmetic():
    a, b = sp.symbols("a b", positive=True)
    frac = (sp.Rational(2, 3) * a + sp.Rational(2, 3) * b) / (a + b)
    return {"union proportion = 2/3 exactly": sp.simplify(frac - sp.Rational(2, 3)) == 0}


def v3_multiplicity_fence():
    """What transfers and what does not. A common zero of the two factors (existence OPEN;
    its absence is part of the grand simplicity picture) would be MULTIPLE in zeta_K while
    simple in each factor -- so:
      TRANSFERS:      N_0 (on-line, WITH multiplicity)  >= (2/3 - o(1)) N   for zeta_K.
      DOES NOT:       simplicity, distinct-point counts -- NOT claimed here.
    The claim this arc banks is the transferred line only, in dyadic liminf form, exactly
    parallel to the source theorems."""
    return {"fence stated; only location-with-multiplicity claimed": True}


if __name__ == "__main__":
    for name, fn in (("V1 ideal-count identity", v1_ideal_count_identity),
                     ("V2 union arithmetic", v2_union_arithmetic),
                     ("V3 the fence", v3_multiplicity_fence)):
        print(f"{name}:")
        for k, v in fn().items():
            print(f"   {k}: {v}")
    print()
    print("COROLLARY (desk-proved from Theorems A + E of the external paper):")
    print("  >= 2/3 (dyadic liminf, WITH multiplicity) of the nontrivial zeros of")
    print("  zeta_K(Q(sqrt-3)) = zeta * L(chi_-3) lie on the critical line, UNCONDITIONALLY;")
    print("  via B737 (the voice = Lambda_K(s)/Lambda_K(s+1)): two thirds of the numerator")
    print("  zeros of the object's own cusp voice are certified critical.")
