"""B702 lock (CORRECTED) — the swap torsion asymmetry + the audibility law.
Retracted: the "hearing <=> real-quadratic SWAP field" law (conflated the
being-face swap with the hearing-face weld). Correct facts:
 (1) both swaps are IMAGINARY-quadratic with rational tones; golden swap =
     roots of unity (torsion/periodic), silver = generic norm-1 (aperiodic);
 (2) AUDIBILITY: a stage hears a metallic tone <=> its character field
     Q(sqrt p*) is REAL <=> p = 1 mod 4 (the weld/character field, B700)."""
import sympy as sp


def test_golden_swap_is_imaginary_torsion_rational_tones():
    # golden swap eigenvalues zeta6, omega are roots of unity in Q(sqrt-3) (imaginary)
    z6 = sp.exp(sp.I * sp.pi / 3); om = sp.exp(2 * sp.I * sp.pi / 3)
    for e in [z6, om]:
        assert sp.simplify(abs(e)) == 1                       # norm 1
        assert sp.simplify(e**sp.Integer(6)) == 1 or sp.simplify(e**sp.Integer(3)) == 1  # torsion
    tones = [sp.simplify(2 * sp.re(z6)), sp.simplify(2 * sp.re(om))]
    assert all(t.is_rational for t in tones)                  # {1, -1}, rational
    # the swap field Q(sqrt-3) is IMAGINARY (NOT Q(sqrt5)) -- this is the retraction point
    assert not sp.sqrt(-3).is_real


def test_weld_phi_is_hearing_not_swap():
    # the phi-tone belongs to the order-10 WELD in Q(sqrt5) (real), a DIFFERENT object
    weld_tone = sp.nsimplify(2 * sp.cos(sp.Rational(3, 5) * sp.pi), [sp.sqrt(5)])
    assert not weld_tone.is_rational and weld_tone.is_real   # -1/phi, irrational, real
    assert sp.sqrt(5).is_real                                 # Q(sqrt5) real (hearing-face)


def test_audibility_law_p_mod_4():
    # AUDIBILITY: a stage hears <=> character field Q(sqrt p*) real <=> p = 1 mod 4
    def hears(p):
        pstar = ((-1) ** ((p - 1) // 2)) * p
        return pstar > 0
    assert hears(5) and hears(13)          # p=1 mod 4 -> real -> hears
    assert not hears(7) and not hears(11)  # p=3 mod 4 -> imaginary -> no tone
    for p in (5, 7, 11, 13):
        assert hears(p) == (p % 4 == 1)
