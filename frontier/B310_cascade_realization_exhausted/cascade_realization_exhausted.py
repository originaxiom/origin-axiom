"""B310 -- the cascade realization question, EXHAUSTED in-sandbox. The decisive multi-seat cross-check: is the
E6 cascade the figure-eight's character-variety realizing a breaking at pi i/3-spaced deformation values, or is it
the standard E6 GUT chain (Slansky 1981) in geometric language? Run: python (pyenv).

Both web-Opus seats independently flagged the load-bearing distinction (the parallel-derivation catch):
  * the SUBGROUP CHAIN E6 -> SU(6)xSU(2) -> SU(3)^3 -> SU(2)^3 is verified (B305/B306) -- but it is STANDARD;
  * the DEFORMATION REALIZATION (the chain appears at specific u-values on the fig-8's E6 character variety, with
    pi i/3 spacing = the cusp shape, the SM between n=2 and n=3) is the genuinely-new claim -- and it was NOT verified.
This settles it computationally (the user's "exhaust the math before the specialist"):

(1) GENERIC. The cascade = centralizer of exp((2pi i/N) h) in E6 (h = principal element), pure Borel-de Siebenthal /
    Slansky Lie theory -- NO figure-eight input. The chain is the standard E6 GUT chain. (B305/B306 already tiered it
    generic; the seats' "verified three ways" verified the CHAIN, not a fig-8 realization.)

(2) THE pi i/3 EQUAL-SPACING CLAIM IS REFUTED. The cascade u-values u_N = 2pi i/N (N=2,3,4,5,6) have gaps (in units
    of pi i) 1/3, 1/6, 1/10, 1/15 -- NOT equal. Only the single N=3 -> N=6 gap is pi i/3. "Equally-spaced pi i/3" is
    false arithmetic.

(3) THE "SPACING = CUSP SHAPE pi/3" CONFLATION IS REFUTED. m004's cusp shape is 2 sqrt(3) i ~ 3.46 i (B290); pi i/3 ~
    1.047 i; the tetrahedral SADDLE is z = e^{i pi/3} (a shape, not a u-spacing). The claim conflates the saddle
    u-value (i pi/3, where N=6 breaks) with the cusp modulus (2 sqrt3 i). Different objects.

(4) THE ONE GENUINE OBJECT CONNECTION (already banked, B305): the N=3 trinification grading EIGENVALUE is
    omega = e^{2pi i/3} = the figure-eight's Eisenstein Riley root (B285) in Q(sqrt-3). So the trinification STEP sits
    at the genuine geometric Eisenstein value -- but that is the eigenvalue omega, not a "deformation spacing", and it
    is one step, already in B305.

VERDICT: the cascade = the standard E6 GUT chain (generic) + the Eisenstein-omega connection at trinification (banked,
B305). The pi i/3 spacing / cusp-shape realization is REFUTED. Whether the chain is realized as PHYSICAL gauge
dynamics on T[4_1;E6] (the DGG 3d-3d correspondence for type E6) is the CRUX -- specialist-gated, no exceptional state
integral in-sandbox. THE CASCADE MATH IS EXHAUSTED: no new object-specific content beyond the banked omega; the
remaining question is the CRUX. FIREWALLED; nothing to CLAIMS.
"""
import sympy as sp


def cascade_u_values():
    """u_N = 2 pi i / N for the cascade steps, in units of pi i (N -> 2/N)."""
    return {N: sp.Rational(2, N) for N in (2, 3, 4, 5, 6)}


def spacing_gaps():
    """gaps between consecutive cascade u-values (units of pi i). Equal pi i/3 <=> all == 1/3."""
    Ns = [2, 3, 4, 5, 6]
    vals = [sp.Rational(2, N) for N in Ns]
    return [vals[i] - vals[i + 1] for i in range(len(vals) - 1)]


def equal_pi3_spacing():
    return all(g == sp.Rational(1, 3) for g in spacing_gaps())


# --- the verdict facts ---
CASCADE_IS_GENERIC_E6 = True                             # centralizers of exp(2pi i/N h); no fig-8 input; Slansky
EQUAL_PI3_SPACING_REFUTED = True                         # gaps 1/3,1/6,1/10,1/15 -- not equal
CUSP_SHAPE = "2*sqrt(3)*i"                               # B290; NOT pi i/3
SPACING_EQUALS_CUSP_SHAPE_REFUTED = True                 # conflates saddle u-value (i pi/3) with cusp modulus
TRINIFICATION_EIGENVALUE_IS_OMEGA = True                 # N=3 grading eigenvalue = omega in Q(sqrt-3) (B305, banked)
DEFORMATION_REALIZATION_VERIFIED = False                 # the genuinely-new claim is NOT verified (and pi/3 refuted)
REALIZATION_IS_THE_CRUX = True                           # T[4_1;E6] DGG -- specialist
CASCADE_MATH_EXHAUSTED = True                            # no new object-specific content beyond the banked omega
DERIVES_SM_VALUES = False


def verdict():
    gaps = spacing_gaps()
    return bool(not equal_pi3_spacing() and gaps == [sp.Rational(1, 3), sp.Rational(1, 6),
                                                     sp.Rational(1, 10), sp.Rational(1, 15)]
                and CASCADE_IS_GENERIC_E6 and EQUAL_PI3_SPACING_REFUTED and SPACING_EQUALS_CUSP_SHAPE_REFUTED
                and TRINIFICATION_EIGENVALUE_IS_OMEGA and not DEFORMATION_REALIZATION_VERIFIED
                and REALIZATION_IS_THE_CRUX and CASCADE_MATH_EXHAUSTED and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("cascade u-values (units of pi i):", {N: str(v) for N, v in cascade_u_values().items()})
    print("gaps (units of pi i):", [str(g) for g in spacing_gaps()], "-> equal pi/3:", equal_pi3_spacing())
    print("cascade generic E6 (Slansky):", CASCADE_IS_GENERIC_E6)
    print("trinification eigenvalue = omega (B305, the one object connection):", TRINIFICATION_EIGENVALUE_IS_OMEGA)
    print("deformation realization (pi/3 spacing) verified:", DEFORMATION_REALIZATION_VERIFIED, "(REFUTED)")
    print("realization = the CRUX (specialist):", REALIZATION_IS_THE_CRUX, "| cascade math exhausted:",
          CASCADE_MATH_EXHAUSTED)
    print("verdict:", verdict())
