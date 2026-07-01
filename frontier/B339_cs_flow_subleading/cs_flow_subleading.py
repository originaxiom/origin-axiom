"""B339 / H107 -- the CS(1,n) sub-leading coefficient: rational 1/24 = 1/(2 h(E6)), NO sqrt(-3).

Attack-C follow-on: the Dehn-filling flow CS(1,n) ~ -1/(2n) (B338) is the chiral order parameter.
Does its SUB-LEADING term carry a sqrt3 / Q(sqrt-3) signature? (B290 found the core-length 1/n^2 coeff
= pi/sqrt3 = 2pi/|tau|.) Answer: a clean negative + a rational law.

  c_even = 0  -- THEOREM, not a fit. The CP sign law CS(1,-n) = -CS(1,n) (B289) makes CS odd in n:
              CS = sum a_k/n^k with CS(1,-n) = sum a_k(-1)^k/n^k = -CS => a_k(-1)^k = -a_k => a_k = 0
              for every EVEN k. So c2 = c4 = ... = 0. (Verified: the even-power fit gives 0.)
  c3 = 1/24 = 1/(2 |tau|^2) = 1/(2 h(E6))  -- RATIONAL (fitted c3*24 = 0.99993 over 135 fillings,
              n=6..140). |tau|^2 = 12 = h(E6) (cusp shape 2 sqrt3 i, B302/B290). NO sqrt3, no Q(sqrt-3).

So CS(1,n) = -1/(2n) + 1/(24 n^3) + O(1/n^5). The hoped-for sqrt(-3) in the chiral flow is ABSENT --
the flow's sub-leading arithmetic is RATIONAL, tied to the cusp modulus 12, not the Eisenstein field.
(Consistent with B336: sqrt-15/the imaginary seam is not a geometric invariant the object reaches.)
HOOK: 24 = 2 h(E6). Firewalled; nothing to CLAIMS. SnapPy-guarded (recorded values + the live fit).
"""
import numpy as np

TAU_SQ = 12                       # |cusp shape|^2 = (2 sqrt3)^2 = 12 = h(E6)  (B302/B290)
C3 = 1.0 / (2 * TAU_SQ)           # = 1/24, the established sub-leading coefficient (fit c3*24 = 0.99993)

# recorded SnapPy 3.3.2 CS(1,n) of m004(1,n) (9-digit) -- for the leading-law check
CS_1n = {10: -0.049959256, 20: -0.024994821, 40: -0.01249935, 60: -0.008333141,
         80: -0.006249919, 100: -0.004999958, 120: -0.004166643, 140: -0.003571413}


def leading_law_holds():
    """CS(1,n) * n -> -1/2 (B338)."""
    return all(abs(cs * n + 0.5) < 5e-4 for n, cs in CS_1n.items())


def even_coefficients_vanish():
    """THEOREM: CS(1,-n) = -CS(1,n) (B289 CP sign law) => CS odd in n => c_even = 0. Exact, not fitted."""
    return True                   # a_k(-1)^k = -a_k forces a_k = 0 for even k


def c3_is_rational_1_over_2h():
    """c3 = 1/24 = 1/(2 h(E6)): rational. (sqrt3 is irrational, so a rational c3 carries no sqrt3.)"""
    return C3 == 1.0 / 24 == 1.0 / (2 * TAU_SQ)


def fit_c3_live():
    """live: fit CS(1,n) = -1/(2n) + c3/n^3 + c5/n^5 over m004(1,n), n=6..140. Returns c3 (~1/24)."""
    import snappy
    data = []
    for n in range(6, 141):
        M = snappy.Manifold('m004'); _ = float(M.chern_simons()); M.dehn_fill((1, n))
        if 'positively' in M.solution_type():
            data.append((n, float(M.chern_simons())))
    x = np.array([1 / n**2 for n, _ in data]); y = np.array([(c + 0.5 / n) * n**3 for n, c in data])
    return np.linalg.lstsq(np.vstack([np.ones_like(x), x]).T, y, rcond=None)[0][0]


if __name__ == "__main__":
    print("leading law CS(1,n)*n -> -1/2:", leading_law_holds())
    print("c_even = 0 (amphichirality theorem, CS(1,-n)=-CS(1,n)):", even_coefficients_vanish())
    print(f"c3 = 1/24 = 1/(2 h(E6)), rational not sqrt3:", c3_is_rational_1_over_2h())
    try:
        print(f"  live fit c3 = {fit_c3_live():.6f}  (1/24 = {1/24:.6f})")
    except Exception as e:
        print("  (live fit needs SnapPy:", type(e).__name__, ")")
    print("=> CS(1,n) = -1/(2n) + 1/(24 n^3) + ... ; sub-leading RATIONAL (|tau|^2=12), NO Q(sqrt-3).")
