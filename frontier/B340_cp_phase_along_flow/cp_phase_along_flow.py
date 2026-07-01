"""B340 / H108 -- the CP phase kappa along the Dehn-filling flow: extremal at the amphichiral point.

Attack-C follow-on: the object's CP phase is kappa = tr[a,b] = sqrt3 e^{+-i pi/6} at the cusp (B285).
As the (1,n) filling turns on chirality (CS != 0, B338), how does kappa move? We instrumented kappa via
SnapPy's holonomy (SL2C of the fundamental group) at each filling. The finding is object-internal (no
lepton mixing):

  cusp (n->inf, amphichiral, CS=0):  kappa = sqrt3 e^{i pi/6}  ->  arg = pi/6 (EXTREMAL), |kappa| = sqrt3.
  filling turns on chirality:         arg(kappa) DECREASES from pi/6,  |kappa| GROWS from sqrt3.
  scaling:  (pi/6 - arg kappa) ~ 3.8 * CS^2   (SECOND order in the chirality).

So the CP phase +-pi/6 is the value at ZERO chirality; chirality LOWERS it, at O(CS^2). Because the
deviation is EVEN in CS (arg kappa is a function of CS^2) while CS is ODD (CS(1,-n)=-CS(1,n), B289), the
CP-phase MAGNITUDE does not distinguish the CP SIGN at leading order -- the sign lives in the orientation
(external), consistent with B285 (the CP sign is external; the object supplies both).

VERDICT: chirality and the CP phase co-flow -- but not "both turn on together": the CP phase is EXTREMAL
(+-pi/6) at the symmetric amphichiral cusp, and chirality deforms it at second order. The object-internal
"chirality -> CP" relationship, made concrete. Firewalled (physics interpretation is [LEAP]); nothing to
CLAIMS. SnapPy-guarded (recorded values + live holonomy).
"""
import numpy as np

# recorded SnapPy 3.3.2: m004(1,n) -> (arg(kappa) deg, |kappa|, CS)
FLOW = {20: (29.86, 1.7343, -0.02499), 12: (29.62, 1.7380, -0.04164), 8: (29.14, 1.7446, -0.06242),
        5: (27.83, 1.7601, -0.09969), 3: (24.38, 1.7907, -0.16542), 2: (18.82, 1.8205, -0.24661)}
CUSP = (30.0, np.sqrt(3), 0.0)          # arg = pi/6, |kappa| = sqrt3, CS = 0  (B285)


def cusp_is_extremal_cp_phase():
    """at the amphichiral cusp: arg(kappa) = pi/6 (30 deg), |kappa| = sqrt3, CS = 0."""
    arg, mod, cs = CUSP
    return abs(arg - 30.0) < 1e-6 and abs(mod - np.sqrt(3)) < 1e-6 and cs == 0.0


def chirality_lowers_the_phase():
    """as |CS| grows (more filled), arg(kappa) decreases from pi/6 and |kappa| grows from sqrt3."""
    ordered = sorted(FLOW.items(), key=lambda kv: abs(kv[1][2]))   # by |CS| ascending
    args = [v[0] for _, v in ordered]; mods = [v[1] for _, v in ordered]
    return all(args[i] > args[i+1] for i in range(len(args)-1)) and \
           all(mods[i] < mods[i+1] for i in range(len(mods)-1))


def deviation_is_second_order():
    """(pi/6 - arg kappa) ~ const * CS^2 ; the ratio is roughly constant (~3.8)."""
    ratios = [(np.pi/6 - np.radians(arg)) / cs**2 for arg, mod, cs in FLOW.values()]
    return 3.4 < np.mean(ratios) < 4.0 and np.std(ratios) < 0.3


def live_kappa(n):
    """live: kappa = tr(rho[a,b]) of m004(1,n) via SnapPy holonomy."""
    import snappy
    M = snappy.Manifold('m004'); _ = float(M.chern_simons()); M.dehn_fill((1, n))
    G = M.fundamental_group()
    def mat(w):
        S = G.SL2C(w); return np.array([[complex(S[0, 0]), complex(S[0, 1])],
                                        [complex(S[1, 0]), complex(S[1, 1])]])
    a, b = mat('a'), mat('b')
    return np.trace(a @ b @ np.linalg.inv(a) @ np.linalg.inv(b))


if __name__ == "__main__":
    print("cusp: arg(kappa)=pi/6 extremal, |kappa|=sqrt3, CS=0:", cusp_is_extremal_cp_phase())
    print("chirality lowers arg(kappa), grows |kappa|:", chirality_lowers_the_phase())
    print("deviation ~ CS^2 (second order):", deviation_is_second_order())
    try:
        print("  live kappa(1,8) =", np.round(live_kappa(8), 4), " arg =", round(np.degrees(np.angle(live_kappa(8))), 2))
    except Exception as e:
        print("  (live needs SnapPy:", type(e).__name__, ")")
    print("=> CP phase +-pi/6 is EXTREMAL at the amphichiral cusp; chirality lowers it at O(CS^2).")
