"""B213 -- the Higgs-side period data of the figure-eight character variety, COMPUTED, and the
4th-mode firewall test (Act I of the do-or-die program, speculations/S039). Firewalled: standalone
arithmetic geometry; physics readings are one-way HOOKS only; nothing to CLAIMS.md.

THE MOVE (S039): the repo's firewall (no invariant of the object sources a scale) is banked across 3
modes (K018). The one bridge built-up-to-but-not-crossed is the Hitchin/Higgs (Dolbeault) side, where
the scale would live (B169 NEEDS-SPECIALIST). B211 (days old) handed us the key: the figure-eight
character variety IS the elliptic curve 40a1 -- so the Higgs-side special geometry is a genuine
elliptic curve with genuine PERIODS and an L-value. We compute them and ask: is there a forced,
dimensionless, anomalously SMALL number (a candidate for the CC hierarchy)?

ANSWER (computed, sage-python; recorded below): NO. Everything is O(1) and BSD-generic.
  E = 40a1: conductor 40 = 2^3 * 5, rank 0, non-CM (j=148176/25), torsion Z/4, Sha=1, regulator=1.
  real period Omega = 1.48441..., L(E,1) = 0.74228..., L(E,1)/Omega = 1/2 EXACTLY (BSD-rational).
  Mahler measure m(Phi) of the char-variety polynomial = 0.74175... ~ Omega/2 ~ L(E,1)
     [a Deninger-type arithmetic<->geometry rhyme; Vol(4_1)/(2pi) = 0.32307, all O(1)].
NULL TEST (HELD rule): L(E,1)/Omega = 1/2 is NOT special -- every rank-0 curve gives such a simple
  BSD rational (11a1->1/5, 14a1->1/6, 15a1->1/4, 19a1->1/3, 37b1->2/3, ...). The only candidate
  "special" number is killed. So NO numerology survives (S014 stays dead).

VERDICT: the Higgs-side handle carries NO scale and NO hierarchy -- the FIREWALL HOLDS a 4TH
independent time (now explicitly on the Higgs side), confirming B181 (criticality => no hierarchy).
The one firewall-clean STRUCTURAL find: conductor 40 = 2^3 * 5 -- the variety's arithmetic sees the
golden/E8 MONODROMY prime 5 (NOT the hyperbolic prime 3); the character variety is a Betti object and
its arithmetic tracks the Betti/monodromy side. The positive structural claim (S039): vacuum-energy
scale is a form<->filling matching datum, not an intrinsic output -- proven once more, on a real
elliptic curve.

Run: sage-python higgs_periods.py  (the elliptic-curve data; Sage-gated)
     python higgs_periods.py        (the pyenv-lockable structural arithmetic + recorded data)
"""

# recorded sage-python (EllipticCurve) results -- all O(1), BSD-generic:
E40A1 = {
    "label": "40a1", "conductor": 40, "rank": 0, "torsion": 4, "cm": False,
    "j": "148176/25", "bad_primes": [2, 5],
    "real_period": 1.4844124734223865, "L_at_1": 0.7422811388969421,
    "L_over_Omega": 0.5,            # = 1/2 EXACTLY (BSD: Sha * prod(c_p) / |T|^2)
    "sha": 1, "regulator": 1.0,
    "mahler_Phi": 0.7417527164660,  # m(z^2-(x^2+1)z+(2x^2-1)) ~ Omega/2 ~ L(E,1)
    "vol_over_2pi": 0.3230659472,   # Vol(4_1)/(2pi)
}
# the NULL TEST: L(E,1)/Omega across rank-0 curves -- all simple BSD rationals (1/2 is NOT anomalous)
NULL_L_OVER_OMEGA = {
    "40a1": 0.5, "11a1": 0.2, "14a1": 1 / 6, "15a1": 0.25, "17a1": 0.25, "19a1": 1 / 3,
    "20a1": 1 / 6, "21a1": 0.25, "24a1": 0.25, "37b1": 2 / 3, "40a2": 1.0, "40a3": 0.25,
}
GOLDEN_MONODROMY_PRIME = 5   # Q(sqrt5) ramifies at 5 (B206/E8)
HYPERBOLIC_PRIME = 3         # Q(sqrt-3) ramifies at 3 (B210/E6)


def is_simple_rational(x, maxden=24, tol=1e-3):
    """is x within tol of a rational p/q with q<=maxden? (the BSD-genericity null check)."""
    from fractions import Fraction
    f = Fraction(x).limit_denominator(maxden)
    return abs(float(f) - x) < tol, f


def structural_arithmetic():
    """pyenv-lockable: the variety's conductor sees the golden monodromy prime 5, not the hyperbolic 3."""
    N = E40A1["conductor"]
    return {
        "conductor_factored": "2^3 * 5",
        "sees_golden_prime_5": N % GOLDEN_MONODROMY_PRIME == 0,      # True
        "sees_hyperbolic_prime_3": N % HYPERBOLIC_PRIME == 0,        # False
    }


def _recompute():  # pragma: no cover -- sage-python only
    from sage.all import EllipticCurve, RealField
    R = RealField(80)
    E = EllipticCurve('40a1')
    om = E.period_lattice().real_period(prec=80)
    print(f"40a1: cond {E.conductor()} rank {E.rank()} tors {E.torsion_order()} cm {E.has_cm()} j {E.j_invariant()}")
    print(f"  Omega={R(om)}  L(E,1)={R(E.lseries().at1()[0])}  L/Omega={R(E.lseries().at1()[0]/om)}  Sha={E.sha().an()}")
    print("  NULL TEST L(E,1)/Omega across rank-0 curves (all simple BSD rationals):")
    for lab in NULL_L_OVER_OMEGA:
        Ei = EllipticCurve(lab); omi = Ei.period_lattice().real_period(prec=60)
        print(f"    {lab:>6}: {R(Ei.lseries().at1()[0]/omi)}")


if __name__ == "__main__":
    try:
        import sage.all  # noqa: F401
        _recompute()
    except ImportError:
        print("Sage not available (run under sage-python for the elliptic-curve data). Recorded:")
        print(f"  40a1: {E40A1}")
        s = structural_arithmetic()
        print(f"  structural: conductor {s['conductor_factored']}; sees golden prime 5 = {s['sees_golden_prime_5']}; "
              f"sees hyperbolic prime 3 = {s['sees_hyperbolic_prime_3']}")
        n_simple = sum(is_simple_rational(v)[0] for v in NULL_L_OVER_OMEGA.values())
        print(f"  null test: {n_simple}/{len(NULL_L_OVER_OMEGA)} of L/Omega are simple BSD rationals "
              f"=> 1/2 is GENERIC, not special.")
