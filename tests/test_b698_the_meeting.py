"""B698 Leg A locks — the level-15 meeting is FACTORED with a Z/2 residue.
Pyenv-reproducible (mpmath + elementary NT); sage-derived elliptic L-values
are stored constants cross-checked vs LMFDB 15.a7 / Cremona 15a8."""
import importlib.util
import os
import mpmath as mp

_here = os.path.dirname(__file__)
_cell = os.path.join(_here, "..", "frontier", "B698_the_meeting_probed", "b698_legA.py")
_spec = importlib.util.spec_from_file_location("b698_legA", _cell)
b = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b)


def test_being_volume_and_mahler_exact():
    mp.mp.dps = 45
    # Vol(4_1) = (3 sqrt3/2) L(chi_-3,2) = banked hyperbolic volume
    assert mp.almosteq(b.Vol, mp.mpf("2.0298832128193072500424051085490"), 1e-28)
    # m(A_41) = Vol/pi  (Boyd, B683)
    assert mp.almosteq(b.m_A41, b.Vol / mp.pi, 1e-40)
    # the being tie is EXACT: m/L(chi_-3,2) = 3 sqrt3 / 2pi
    assert mp.almosteq(b.m_A41 / b.L_chi3_2, 3 * mp.sqrt(3) / (2 * mp.pi), 1e-40)


def test_meeting_generic_bsd():
    mp.mp.dps = 30
    # L(15a,1) = Omega/16, Sha = 1 (generic, no exotic)
    assert mp.almosteq(b.L15_1, b.Omega / 16, 1e-9)
    # L'(15a,0) = (15/4pi^2) L(15a,2)  -- functional equation, no new info
    assert mp.almosteq(b.L15_0p, (15 / (4 * mp.pi ** 2)) * b.L15_2, 1e-9)


def test_no_coupling_pslq_none():
    """K3 (being) and K2 (meeting) are arithmetically independent."""
    mp.mp.dps = 50
    for vec in ([b.m_A41, b.L15_2, b.L_chi3_2, mp.pi],
                [b.m_A41, b.L15_0p, b.L_chi3_2, mp.pi],
                [b.L15_2, b.L_chi3_2, mp.pi ** 2, mp.mpf(1)]):
        assert mp.pslq(vec, maxcoeff=10 ** 6, maxsteps=10 ** 5) is None


def test_meeting_invariant_is_Z2():
    """The genus-theory Z/2: h(Q(sqrt-15))=2 while both hands have h=1."""
    assert b.class_number_neg(-3) == 1
    assert b.class_number_neg(-15) == 2
    assert b.class_number_real_5() == 1
    # spot-check the function on known small discriminants
    assert b.class_number_neg(-4) == 1
    assert b.class_number_neg(-23) == 3
    assert b.class_number_neg(-47) == 5
