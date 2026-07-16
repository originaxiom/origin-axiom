"""B647 cell-1 lock — the reduction is exact and re-runnable."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B647 = os.path.join(HERE, "..", "frontier", "B647_core_mechanism")


def test_cell1_verdicts():
    out = open(os.path.join(B647, "b647_output.txt")).read()
    assert "dim = 6" in out
    assert "not forced" in out
    fnd = open(os.path.join(B647, "FINDINGS.md")).read()
    assert "arg Y[134] = π/6" in fnd


def test_banked_y134_on_the_locus():
    import sympy as sp
    a, b = sp.Rational(1, 24), sp.Rational(1, 72)
    assert a == 3 * b
    assert sp.simplify(sp.arg(3 + sp.sqrt(3) * sp.I) - sp.pi / 6) == 0


def test_cell2_defect_law_exact():
    """THE DEFECT LAW: rev(lam,mu) defect = 2 conj(Y) on lawful triples;
    the dial slot's four defects satisfy the forced combination.
    (fwd-exactness + this law => Y(sigma* z) = conj Y: substituting the
    seven exact slots and the one defect into Y's definition gives
    conj(Sb)-conj(Sa) + 2conj(Y) = -conj(Y) + 2conj(Y) = conj(Y).)"""
    import sympy as sp
    r = sp.I * sp.sqrt(3)
    Y = {(1, 3, 4): sp.Rational(1, 24) + sp.Rational(1, 72) * r,
         (0, 2, 3): sp.Rational(-7983360, 13) + sp.Rational(2661120, 13) * r,
         (1, 2, 3): sp.Rational(221760, 13) * r,
         (2, 3, 4): sp.Rational(5332879641600, 13)
         + sp.Rational(8106192460800, 13) * r}
    D = {(1, 3, 4): sp.Rational(1, 12) - sp.Rational(1, 36) * r,
         (0, 2, 3): sp.Rational(-15966720, 13) - sp.Rational(5322240, 13) * r,
         (1, 2, 3): -sp.Rational(443520, 13) * r}
    for t, d in D.items():
        assert sp.simplify(d - 2 * sp.conjugate(Y[t])) == 0, t
    dA1 = sp.Rational(54751534973459448941880, 143) + sp.Rational(157785113012405615999640, 143) * r
    dA2 = sp.Rational(65097087899636757184920, 143) + sp.Rational(132218658267899124471480, 143) * r
    dR1 = sp.Rational(-33271486886548807460343360, 143) + sp.Rational(26885920774904351336356320, 143) * r
    dR2 = sp.Rational(-33261141333505306799985120, 143) + sp.Rational(2441850392725591691880960, 13) * r
    assert sp.simplify((dA1 - dA2) - (dR1 - dR2)
                       - 2 * sp.conjugate(Y[(2, 3, 4)])) == 0


def test_cell2_output_verdicts():
    out = open(os.path.join(B647, "b647_cell2_output.txt")).read()
    # 9 verdict-Trues (3 lawful triples x 3 exact slots) + 1 build-log
    # "ok: True" from the b575 prefix; 7 Falses (3 lawful rev(lam,mu)
    # + 4 dial slots)
    assert out.count("True") == 10
    assert out.count("False") == 7
    assert "defect (1/12+-1/36r)" in out


def test_cell3_gauge_adjudication():
    import sympy as sp
    r = sp.I * sp.sqrt(3)
    Y023 = sp.Rational(-7983360, 13) + sp.Rational(2661120, 13) * r
    Y123 = sp.Rational(221760, 13) * r
    Y034 = sp.Rational(2, 3) * r
    Y134 = sp.Rational(1, 24) + sp.Rational(1, 72) * r
    c0, c1, c2, c3, c4 = sp.symbols("c0:5", nonzero=True)
    ratio = (c0 * c2 * c3 * Y023) / (c1 * c2 * c3 * Y123)
    assert sp.simplify(ratio / (Y023 / Y123)) == c0 / c1   # gauge-covariant
    cr = ((c0 * c2 * c3 * Y023) * (c1 * c3 * c4 * Y134)) / \
         ((c0 * c3 * c4 * Y034) * (c1 * c2 * c3 * Y123))
    assert sp.simplify(cr) == 1                            # invariant, = 1
