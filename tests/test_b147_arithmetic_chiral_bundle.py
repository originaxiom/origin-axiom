"""B147 -- arithmetic chiral o-p-t bundle. Needs SnapPy + cypari (pyenv); NOT Sage (cypari clashes with Sage pari)."""
import pytest

pytest.importorskip("snappy")
pytest.importorskip("cypari")

from frontier.B147_arithmetic_chiral_bundle.probe import arithmetic_scan, arithmetic_verdict


def test_integrality_logic_discriminates():
    """Lock the poldegree fix: the integrality check must flag a non-integer (3/2 -> minpoly 2x-3, lead 2)."""
    import cypari
    pari = cypari.pari
    z = pari("3/2")
    p = pari.algdep(z, 2)                       # 2*x - 3
    ad = int(p.poldegree())
    lead = int(p.polcoef(ad))
    assert ad == 1 and abs(lead) == 2          # NOT monic -> non-integral (the bug read polcoef(2)=0)


def test_rrl_is_arithmetic_and_chiral():
    """The headline: RRL is an ARITHMETIC CHIRAL once-punctured-torus bundle (Q(sqrt-7), integral traces)."""
    r = arithmetic_verdict("RRL")
    assert r["imag_quadratic"] is True
    assert r["all_traces_integral"] is True
    assert r["ARITHMETIC"] is True
    assert r["amphichiral_self_mirror"] is False     # chiral


def test_controls():
    """RL, RRLL arithmetic (amphichiral); RRRL non-arithmetic (invariant trace field not imaginary quadratic)."""
    assert arithmetic_verdict("RL")["ARITHMETIC"] is True
    assert arithmetic_verdict("RRLL")["ARITHMETIC"] is True
    assert arithmetic_verdict("RRRL")["ARITHMETIC"] is False


def test_scan_finds_chiral_arithmetic():
    """The scan (len<=7) finds chiral arithmetic bundles -> 'no arithmetic chiral o-p-t bundle' is refuted."""
    found = arithmetic_scan(7)
    chiral = [w for w, _, c in found if c == "CHIRAL"]
    assert len(chiral) > 0
