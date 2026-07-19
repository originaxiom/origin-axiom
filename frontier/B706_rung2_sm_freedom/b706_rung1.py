"""B706 rung-1: are dimensionless SM flavor ratios algebraic of low degree over
the object's audible field Q(sqrt5)? Falsifier = a relation must survive beyond
its discovery precision. Listening Protocol; Gate 5-SM (structure, not value)."""
import mpmath as mp
mp.mp.dps = 40
s5 = mp.sqrt(5)

# dimensionless, convention-reduced SM flavor ratios (PDG); precision ~ the data
RATIOS = {
    "m_mu/m_e":  (mp.mpf('105.6583755') / mp.mpf('0.51099895000'), 9),   # ~9 sig digits
    "m_tau/m_mu":(mp.mpf('1776.86') / mp.mpf('105.6583755'),        5),   # m_tau-limited
    "m_tau/m_e": (mp.mpf('1776.86') / mp.mpf('0.51099895000'),      5),
    "Koide_Q":   ((mp.mpf('0.51099895')+mp.mpf('105.6583755')+mp.mpf('1776.86')) /
                  (mp.sqrt('0.51099895')+mp.sqrt('105.6583755')+mp.sqrt('1776.86'))**2, 5),
    "sin2_thetaW":(mp.mpf('0.23122'), 5),
    "Cabibbo_sin":(mp.mpf('0.22500'), 4),
}

def algebraic_over_Q5(x, deg, digits, maxcoeff):
    """PSLQ for an integer relation making x algebraic of degree<=deg over Q(sqrt5).
    Basis: {x^i, x^i*sqrt5 : 0<=i<=deg}. Return (relation, holds_to_digits) or None."""
    basis = []
    for i in range(deg + 1):
        basis.append(x**i)
        basis.append(x**i * s5)
    rel = mp.pslq(basis, maxcoeff=maxcoeff, maxsteps=10**5)
    if rel is None:
        return None
    # check the relation's residual vs the data precision
    val = sum(c * b for c, b in zip(rel, basis))
    height = max(abs(c) for c in rel)
    return rel, mp.nstr(abs(val), 4), int(height)

if __name__ == "__main__":
    print("=== RUNG-1: algebraicity of SM flavor ratios over Q(sqrt5) (audible field) ===")
    print(f"{'ratio':13} {'value':>16} {'deg<=2 hit?':>40}")
    for name, (x, dig) in RATIOS.items():
        # cap the height so a spurious relation can't hide under the data precision:
        # a real low-degree relation has SMALL height; allow up to 10^3.
        r = algebraic_over_Q5(x, 2, dig, 10**3)
        verdict = "NO low-height relation (generic)" if r is None else f"CANDIDATE {r[0]} resid {r[1]} height {r[2]}"
        print(f"{name:13} {mp.nstr(x,12):>16}   {verdict}")
    print()
    print("Falsifier note: any CANDIDATE must (a) have height << 10^(data digits) and")
    print("(b) survive when the measurement precision improves. Height ~10^3 against ~5-9")
    print("data digits is NOT a survival -- it is base-rate fitting, not membership.")
