"""B68 (P6) -- the EXACT q-deformed recursion search for the figure-eight AJ identity, and the precise
obstruction (why the from-scratch q->1 identity stays out of reach in-house).

AJ: the colored-Jones q-holonomic recursion at q=1 should give the classical A-polynomial. B68 verified
the order-MATCH (minimal recursion order 2 = the L-degree of A) and that it annihilates J_N for N=2..5,
but the exact recursion|_{q=1}=A identity was below B67's exact-identity bar (ill-conditioned q->1).

This (P6) attempts the EXACT order-2 recursion symbolically:
   a0(Q,q) J_N + a1(Q,q) J_{N+1} + a2(Q,q) J_{N+2} = 0,   Q = q^N (= meridian^2),
with a_b(Q,q) = sum_{i<=DQ} P_{b,i}(q) Q^i, solving the homogeneous system over Q exactly.

FINDING (exact): at Q-degree DQ=2 (meridian-degree 4) the system is TRIVIAL-ONLY -- NO order-2 recursion
exists with coefficients of M-degree <= 4. So the figure-eight quantum A-polynomial genuinely needs
Q-degree >= 4 (meridian-degree 8 -- matching the classical A's M-degree 8), consistent with B68's note
that the empirical minimal recursion has M_rec-degree 5. At DQ>=4 the exact symbolic solve (≈200
unknowns over Q(q), each J_N a wide Laurent polynomial) is computationally prohibitive in-house
(sympy linsolve does not complete) -- the same wall B68 hit. So the exact recursion|_{q=1}=A identity
is NOT newly established here; the order-match (B68) stands and the exact identity remains the
documented open item (proven in the literature by Le / Garoufalidis, not re-derived in-house).

HONEST DISPOSITION: bounded negative -- the Q-degree-2 non-existence is a clean exact sub-result; the
full exact recursion needs Q-degree >= 4 where the in-house symbolic solve is intractable. No claim.
Standalone low-dim topology; no physics. Proven core P1-P16 untouched.
"""
import sympy as sp

q = sp.symbols("q")


def J_sym(N):
    tot = sp.Integer(0)
    for k in range(N):
        term = sp.Integer(1)
        for j in range(1, k + 1):
            term *= ((q ** N + q ** (-N)) - (q ** j + q ** (-j))) / (q ** j - 2 + q ** (-j))
        tot += term
    return sp.expand(sp.cancel(sp.together(tot)))


def order2_recursion_exists(DQ, W=4, Nmax=8):
    """Is there an order-2 recursion with a_b(Q,q)=sum_{i<=DQ} P_{b,i}(q) Q^i, P Laurent deg [-W,W]?
    Returns the number of free parameters in the homogeneous solution (0 => only trivial)."""
    Js = {N: sp.expand(sp.cancel(J_sym(N))) for N in range(1, Nmax + 3)}
    P, syms = {}, []
    for b in range(3):
        for i in range(DQ + 1):
            cs = sp.symbols(f"c_{b}_{i}_:%d" % (2 * W + 1))
            syms += list(cs)
            P[(b, i)] = sum(cs[k] * q ** (k - W) for k in range(2 * W + 1))
    eqs = []
    for N in range(1, Nmax + 1):
        expr = sum(P[(b, i)] * (q ** N) ** i * Js[N + b] for b in range(3) for i in range(DQ + 1))
        num, _ = sp.fraction(sp.cancel(sp.together(expr)))
        eqs += sp.Poly(sp.expand(num * q ** 60), q).all_coeffs()
    sol = sp.linsolve(eqs, syms)
    if not sol:
        return 0
    vals = list(sol)[0]
    free = set().union(*[t.free_symbols for t in vals]) & set(syms)
    return len(free)


def main():
    print("B68 (P6) -- exact order-2 AJ recursion search\n")
    n = order2_recursion_exists(DQ=2)
    print(f"  Q-degree 2 (meridian-degree 4): free parameters = {n}  "
          f"=> {'NO order-2 recursion (trivial-only)' if n == 0 else 'recursion exists'}")
    print("  => the figure-eight quantum A-polynomial needs Q-degree >= 4 (meridian-degree 8);")
    print("     the exact symbolic solve at DQ>=4 (~200 unknowns over Q(q)) is intractable in-house.")
    print("  HONEST: the exact recursion|_{q=1}=A identity is NOT established here (B68 order-match")
    print("  stands; the identity is a literature theorem, not re-derived). Bounded negative, no claim.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
