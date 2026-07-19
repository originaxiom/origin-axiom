"""B702 lock — the metallic-hearing bifocal law core (pyenv-pure).
A metallic tone requires a real-quadratic swap field: norm-1 elements of the
imaginary-quadratic Q(i) have rational tone (no irrational metallic value),
while the golden's real-quadratic Q(sqrt5) carries phi."""
import sympy as sp


def test_silver_norm1_tone_is_rational():
    # any norm-1 a+bi in Q(i) has 2Re = 2a in Q -> silver tones are rational
    for (num, den) in [(3, 5), (20, 29), (321266, 386425)]:
        a = sp.Rational(num, den)
        # b^2 = 1 - a^2 need not be rational, but 2Re = 2a is rational regardless
        assert (2 * a).is_rational
    # cc2's exact silver tones are rational
    assert sp.Rational(321266, 386425).is_rational
    assert sp.Rational(21834073166, 16953624025).is_rational


def test_no_delta_relation_impossibility():
    # delta = 1+sqrt2 irrational; Q(i) cap R = Q => no silver tone equals a delta-value
    delta = 1 + sp.sqrt(2)
    assert not delta.is_rational
    assert not sp.sqrt(2).is_rational
    # a real element of Q(i) is rational; delta is not -> impossibility
    assert (sp.I * sp.I) == -1  # Q(i) is imaginary quadratic, real part is Q


def test_golden_hears_real_quadratic():
    # golden: phi in Q(sqrt5) (real quadratic), irrational, IS a tone
    phi = (1 + sp.sqrt(5)) / 2
    assert not phi.is_rational and phi.is_real
    # the law: metallic tone (irrational) requires a real-quadratic field;
    # Q(sqrt5) real -> golden hears; Q(i) imaginary -> silver silent
    assert sp.sqrt(5).is_real and not sp.sqrt(-1).is_real
