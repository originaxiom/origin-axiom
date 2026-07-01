"""B331 -- the SL(2,C) holomorphic escape is closed by the ellipticity of the generation element. sympy-only."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B331_ambivalence_closure'))
import sympy as sp
from ambivalence_closure import (g_is_elliptic_ambivalent, chi27_holomorphic,
                                 chi27_compact, chi27_central)


def test_generation_element_is_elliptic_ambivalent():
    order3, ambivalent = g_is_elliptic_ambivalent()
    assert order3 and ambivalent            # g ~ g^-1, eigenvalues {omega, omega^2}


def test_holomorphic_and_compact_characters_coincide_and_are_real():
    # the escape fails: at the elliptic g, holomorphic == compact == 0 (real) -> n1 = n2
    assert chi27_holomorphic() == 0
    assert chi27_compact() == 0


def test_central_element_is_complex_so_argument_is_sharp():
    # 'every order-3 element -> real character' is FALSE: the central z gives 27*omega (complex).
    z = chi27_central()
    assert sp.im(z) != 0
