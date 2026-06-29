"""B295 -- the SSB / gauge status of the CP sign (folds in Chat-2; corrects the Curie framing). Run: python (pyenv).

B289 banked: the closing forces a CP sign LAW, but WHICH sign is not object-derivable (the object is CP-symmetric).
Chat-2 argues the externality is NOT a Curie wall but (a) an SSB loophole and (b) gauge redundancy (tau gauged ->
sign pure gauge). VERIFY-DON'T-TRUST: this module tests the COMPUTABLE pieces and gates the rest.

  (1) CURIE IS NOT A HARD WALL. Spontaneous symmetry breaking under a running control parameter evades Curie's
      principle -- a logical correction to P011/B286 (which over-stated "Curie forbids the sign"). [physics, firewalled]

  (2) THE SSB INGREDIENTS -- tested:
      * degenerate +-pi/6 vacua exchanged by tau: YES. The two conjugate Riley roots omega, omega^2 (roots of the
        REAL polynomial u^2+u+1) give kappa = u^2+2 = sqrt(3) e^{-+ i pi/6} (B285); complex conjugation (= tau) swaps
        them. A symmetric (real-coefficient) structure with two degenerate vacua EXISTS.
      * a tau-symmetric DOUBLE-WELL POTENTIAL: ABSENT. The program's gradient potential V(tau)=kappa(tau^3/3-tau^2/2
        -tau) (P15/P16) is the WRONG object on three counts -- (i) its 'tau' is the MODULAR parameter on H (A acts by
        tau->(2tau+1)/(tau+1)), NOT the amphichiral involution; (ii) it is GOLDEN: critical points phi, -1/phi in
        Q(sqrt5), while the CP vacua omega, omega^2 are EISENSTEIN in Q(sqrt-3) -- disjoint; (iii) it is a SINGLE-well
        (one min phi, one max -1/phi), not a degenerate double-well. So no tau-symmetric double-well over the +-pi/6
        vacua exists in the program: SSB-availability is NOT demonstrated.
      * a control parameter k (de Sitter temperature T_dS ~ 1/sqrt(k)): exists [firewalled; S043/S044].

  (3) 'tau IS GAUGED' -- STOP-GATE. B279 banked only the topological FIX bit (tau fixes both spin structures, Mostow
      rigidity). Its own status: the gauged/parity-anomaly reading 'rests on an unverified link'. NEEDS-SPECIALIST.
      So Chat-2's 'sign is pure gauge' is CONDITIONAL on an unverified premise.

  NET: B289's conclusion stands (the sign is external), but the REASON is open -- NOT 'Curie forbids it' (refuted),
  and NOT established 'pure gauge' (tau-gauged unverified). The honest statement: the sign is not object-derivable
  because the object is CP-symmetric (B289), and NO symmetry-breaking mechanism (SSB or gauge-fixing) is established
  in-sandbox. FIREWALL: SSB/gauge/baryon physics -> speculations/ HELD/[LEAP]; nothing to CLAIMS.
"""
import sympy as sp


def cp_vacua():
    """The two degenerate +-pi/6 vacua (B285): omega, omega^2 -- roots of the REAL poly u^2+u+1, conjugate pair."""
    u = sp.symbols('u')
    riley_factor = u**2 + u + 1                         # the Eisenstein factor of the Riley polynomial
    roots = sp.roots(riley_factor, u)
    kappa = u**2 + 2
    phases = [sp.simplify(sp.arg(sp.expand_complex(kappa.subs(u, r)))) for r in roots]
    return riley_factor, list(roots), phases           # phases = [-pi/6, +pi/6]


def potential_critical_points():
    """P16's V(tau)=kappa(tau^3/3 - tau^2/2 - tau): critical points = roots of V'(tau)=kappa(tau^2-tau-1)."""
    tau = sp.symbols('tau')
    Vprime = tau**2 - tau - 1                           # up to the constant kappa
    crit = sp.roots(Vprime, tau)
    # classify each as min/max via V'' = 2*tau - 1
    kinds = {}
    for c in crit:
        kinds[sp.simplify(c)] = "min" if sp.simplify(2*c - 1) > 0 else "max"
    return list(crit), kinds                            # phi (min), -1/phi (max)  -- golden, single-well


def vacua_disjoint_from_potential():
    """The CP vacua (Q(sqrt-3)) are disjoint from V's critical points (Q(sqrt5)) -> no double-well over +-pi/6."""
    _, cp, _ = cp_vacua()
    crit, _ = potential_critical_points()
    cp_set = {sp.simplify(r) for r in cp}
    crit_set = {sp.simplify(c) for c in crit}
    return cp_set.isdisjoint(crit_set)


# --- the adjudication (firewalled flags) ---
CURIE_IS_A_HARD_WALL = False                            # SSB loophole refutes the P011/B286 over-statement
SSB_POTENTIAL_PRESENT = False                           # the program's V(tau) is the wrong-tau / golden / single-well
TAU_GAUGED_IS_VERIFIED = False                          # B279 [LEAP]; NEEDS-SPECIALIST (stop-gate)
SIGN_IS_EXTERNAL = True                                 # B289 stands
SIGN_MECHANISM_ESTABLISHED = False                      # neither SSB nor gauge-fixing shown in-sandbox
DERIVES_SM_VALUES = False                               # firewall


if __name__ == "__main__":
    rf, cp, phases = cp_vacua()
    print(f"(2a) CP vacua: roots of {rf} = {cp}; commutator phases = {phases} (+-pi/6, conjugate pair, tau-swapped)")
    crit, kinds = potential_critical_points()
    print(f"(2b) P16 V(tau) critical points = {crit} (golden, Q(sqrt5)); kinds = {kinds}  -> SINGLE-well, wrong tau")
    print(f"     CP vacua disjoint from V's critical points: {vacua_disjoint_from_potential()}  -> no SSB double-well")
    print(f"(1) Curie is a hard wall: {CURIE_IS_A_HARD_WALL} (SSB loophole)")
    print(f"(3) 'tau is gauged' verified: {TAU_GAUGED_IS_VERIFIED} (B279 [LEAP]; STOP-GATE)")
    print(f"NET: sign external = {SIGN_IS_EXTERNAL}; mechanism established = {SIGN_MECHANISM_ESTABLISHED} (open)")
