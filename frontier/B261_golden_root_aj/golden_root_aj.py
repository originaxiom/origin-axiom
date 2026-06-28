"""B261 -- the golden-root AJ operator: the two ends are the two REGIMES of one q-difference recursion.
FIREWALLED (quantum topology / arithmetic, not physics). Nothing to CLAIMS.md.

The B260 next stone: the Coulomb branch (A-polynomial) quantizes to the colored-Jones recursion (AJ conjecture,
proved for 4_1 by Garoufalidis -- the quantized A-polynomial annihilates J_N and its classical limit q->1 IS the
A-polynomial). So the Coulomb branch is the classical shadow of the colored-Jones recursion. This probe evaluates
that recursion at the golden / E8 root q = e^{2pi i/5} and finds the two-ended structure inside ONE operator.

THE TWO REGIMES OF THE AJ OPERATOR (same q-difference recursion, two limits):
  * HYPERBOLIC / E6 end -- q = e^{2pi i/N} with N->infinity together (the Kashaev / volume-conjecture limit):
    the recursion is q-HOLONOMIC and J_N grows EXPONENTIALLY, (2pi/N) log|J_N| -> Vol = 2.0299 (B258).
  * SPHERICAL / E8 end -- q = zeta_5 = e^{2pi i/5} FIXED (a primitive 5th root): the operator coefficients
    Q = q^N are PERIODIC in N (period 5), so the recursion DEGENERATES to a finite one and J_N is PERIODIC.
    Computed: [N] J_N(4_1; zeta_5) = {1,-2,-2,1,0 | -1,2,2,-1,0} -- ANTIPERIOD 5 (f(N+5)=-f(N)), period 10.
    Bounded, integral (extends B240's {1,-2,-2,1}). The exponential (Vol) growth is GONE. The period = 5 = k+2 =
    det(4_1) = the E8 "5".

THE COULOMB BRANCH AT THE GOLDEN MERIDIAN (classical side, same point):
    A-poly balanced form (B260): L + 1/L = u^2 - u - 4, u = M^2 + M^-2. At the golden meridian M^2 = zeta_5,
    u = 2cos(2pi/5) = 1/phi = (sqrt5-1)/2, so
        L + 1/L = -(2 + sqrt5) = -phi^3   in Q(sqrt5)   [the E8 / golden field].
    The golden meridian root forces the longitude into Q(sqrt5).

SYNTHESIS: the golden root is special because 5 = k+2 = det -- it makes the quantum recursion's period exactly 5
and lands the classical longitude in Q(sqrt5). One AJ operator carries BOTH ends of the transition: exponential
(hyperbolic/E6/Vol) at the Kashaev limit, periodic (spherical/E8/Q(sqrt5)) at the golden root. This is the quantum
realization of the two-ended unification (B258), now from the Coulomb-branch/AJ side (B260).

Run: python golden_root_aj.py (pyenv; mpmath + sympy).
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 50


def colored_jones(N, q):
    """Habiro: J_N(4_1;q) = sum_{k=0}^{N-1} q^{-kN} prod_{j=1}^k (1-q^{N-j})(1-q^{N+j}). Normalized, unknot=1."""
    tot = mp.mpc(0)
    for k in range(N):
        term = q ** (-k * N)
        for j in range(1, k + 1):
            term *= (1 - q ** (N - j)) * (1 - q ** (N + j))
        tot += term
    return tot


def golden_root_sequence(n_terms=15):
    """[N] J_N at q=zeta_5, N=1..n_terms (rounded to integers). Antiperiod-5 / period-10."""
    q5 = mp.e ** (2j * mp.pi / 5)
    t = mp.e ** (1j * mp.pi / 5)  # t = q^{1/2}
    out = []
    for N in range(1, n_terms + 1):
        qint = (t ** N - t ** (-N)) / (t - t ** (-1))
        out.append(int(mp.nint((qint * colored_jones(N, q5)).real)))
    return out


def golden_meridian_longitude():
    """L + 1/L at the golden meridian M^2 = zeta_5: = -(2+sqrt5) = -phi^3, in Q(sqrt5). Returns the sympy value."""
    u = sp.nsimplify(2 * sp.cos(2 * sp.pi / 5), [sp.sqrt(5)])      # = (sqrt5 - 1)/2 = 1/phi
    return sp.nsimplify(sp.simplify(u**2 - u - 4), [sp.sqrt(5)])    # = -(2+sqrt5)


if __name__ == "__main__":
    print("=== B261: the golden-root AJ operator ===\n")
    seq = golden_root_sequence()
    print(f"[N] J_N(4_1; zeta_5), N=1..15 = {seq}")
    antiperiod = all(seq[N + 5] == -seq[N] for N in range(10))
    period10 = all(seq[N + 10] == seq[N] for N in range(5))
    print(f"  antiperiod-5 (f(N+5)=-f(N)): {antiperiod};  period-10: {period10}")
    print("  => recursion DEGENERATES q-holonomic -> finite/periodic at q=zeta_5; period 5 = k+2 = det = the E8 '5'.")
    assert antiperiod and period10 and seq[:4] == [1, -2, -2, 1]   # extends B240

    LpL = golden_meridian_longitude()
    phi = (1 + sp.sqrt(5)) / 2
    print(f"\ngolden meridian M^2=zeta_5:  L + 1/L = {LpL} = -phi^3 ({sp.simplify(LpL + phi**3) == 0}), in Q(sqrt5).")
    assert sp.simplify(LpL + phi**3) == 0

    print("\nONE AJ operator, two ends: exponential (Kashaev->Vol, hyperbolic/E6) and periodic (zeta_5,")
    print("spherical/E8/Q(sqrt5)). The quantum realization of the two-ended unification (B258). ALL CHECKS PASS")
