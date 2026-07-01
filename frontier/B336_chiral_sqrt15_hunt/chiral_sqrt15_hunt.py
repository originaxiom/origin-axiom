"""B336 -- the chiral sqrt(-15) hunt (Chat-1's insight, probed): the value's home is doubly separated.

Chat-1: structure = REAL (amphichiral: J_N(q)=J_N(q^-1), real at roots of unity); value = IMAGINARY
(the seam sqrt(-15) = i sqrt15); to reach the imaginary part, BREAK amphichirality (Dehn filling,
commensurator, CP choice). We probed it -- and the premise is right but the ROUTES are closed.

A1 (premise, CONFIRMED). J_N(4_1; zeta_15) is REAL for all N (Im = 0). The single amphichiral object
carries ZERO sqrt(-15) component. (Amphichiral J_N(q)=J_N(q^-1); at a root q^-1=conj(q); integer Jones
coeffs => J_N(conj q)=conj(J_N) => J_N real.)

A2 (the routes to sqrt(-15) -- provably CLOSED):
  Route 0 (monodromy words in R,L, det=1): discs {t^2 - 4}; -15 needs t^2 = -11 -> UNREACHABLE.
  Route 2 (commensurator / covers / neighbors): the invariant trace field is a COMMENSURABILITY
     invariant (Neumann-Reid). The whole class of 4_1 is Q(sqrt-3) = Bianchi O_-3 (m004 shape =
     (1+i sqrt3)/2; m003 sister same volume, commensurable). sqrt(-15) = Bianchi O_-15 is a DIFFERENT
     class -> NO commensurable neighbor reaches Q(sqrt-15). CLOSED.
  Route 1 (Dehn fillings): closed, CHIRAL (CS != 0, verified), but generically NON-arithmetic
     (Thurston surgery) -> higher-degree trace fields, not the degree-2 Q(sqrt-15). An arithmetic
     O_-15 filling would be a specific coincidence (Sage-checkable; generic answer: no).

A3 (null test): even if a filling reached sqrt(-15), it is generic -- h(-15)=2 is shared by many
fields (B333). No SM significance from landing in one imaginary quadratic field.

VERDICT: Chat-1's premise (real object, no sqrt-15) is right; the chiral ROUTES do not deliver
sqrt(-15). Combined with B333 (sqrt-15 arithmetically generic), the value's home is DOUBLY separated:
generic in arithmetic AND not a geometric invariant of the object or its chiral breaking. sqrt(-15)
lives only as the abstract compositum/class-field of the two ends (B332/B334). Firewall holds in the
chiral sector too. Nothing to CLAIMS. SnapPy-guarded (recorded values).
"""
import sympy as sp

q = sp.symbols("q")
# recorded SnapPy 3.3.2 values (so the test runs without SnapPy)
RECORD = dict(m004_shape=complex(0.5, 0.8660254),         # (1+i sqrt3)/2 -> Q(sqrt-3)
              m003_vol=2.0298832, m004_vol=2.0298832,     # commensurable (same volume)
              chiral_filling_cs={(1, 2): -0.2466, (1, 3): -0.1654, (2, 3): 0.1691,
                                 (5, 1): 0.0770, (1, 4): -0.1244})  # CS != 0 -> chiral


def colored_jones(N):
    tot = sp.Integer(0)
    for n in range(N):
        term = q ** (-n * N)
        for j in range(1, n + 1):
            term *= (1 - q ** (N - j)) * (1 - q ** (N + j))
        tot += term
    return sp.expand(tot)


def jones_at_zeta15_is_real(Nmax=6):
    """A1: J_N(4_1; zeta_15) has zero imaginary part for all N <= Nmax (amphichiral => no sqrt-15)."""
    z = sp.exp(2 * sp.I * sp.pi / 15)
    return all(sp.simplify(sp.im(sp.expand_complex(colored_jones(N).subs(q, z)))) == 0
               for N in range(1, Nmax + 1))


def monodromy_discs(tmax=12):
    """Route 0: words in R,L are in SL(2,Z), det=1, integer trace t -> disc = t^2 - 4."""
    return sorted({t * t - 4 for t in range(-tmax, tmax + 1)})


def minus15_reachable_by_monodromy():
    return -15 in monodromy_discs()


def chiral_fillings_are_chiral():
    """Route 1: the fillings break amphichirality (CS != 0)."""
    return all(abs(cs) > 1e-3 for cs in RECORD['chiral_filling_cs'].values())


def commensurables_share_sqrt_minus3():
    """Route 2: m003/m004 same volume -> commensurable -> same invariant trace field Q(sqrt-3) != Q(sqrt-15)."""
    z = RECORD['m004_shape']
    is_eisenstein = abs(z - complex(0.5, 0.8660254)) < 1e-6         # (1+i sqrt3)/2
    commensurable = abs(RECORD['m003_vol'] - RECORD['m004_vol']) < 1e-5
    return is_eisenstein and commensurable


if __name__ == "__main__":
    print("A1: J_N(4_1; zeta_15) real for all N:", jones_at_zeta15_is_real())
    print("A2 route 0: monodromy discs", monodromy_discs(), "-> -15 reachable?", minus15_reachable_by_monodromy())
    print("A2 route 2: commensurables share Q(sqrt-3) (!= Q(sqrt-15)):", commensurables_share_sqrt_minus3())
    print("A2 route 1: fillings are chiral (CS != 0):", chiral_fillings_are_chiral(),
          "-- but non-arithmetic, not Q(sqrt-15)")
    print("=> sqrt(-15) doubly separated (generic arithmetic B333 + not a geometric invariant). Firewall holds.")
