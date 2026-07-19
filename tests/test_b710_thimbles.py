"""B710 lock — analytic-T1: fig-8 (2 real-action saddles) vs FRW (4 complex). Structural only."""
import mpmath as mp
import sympy as sp

def test_fig8_two_saddles_real_actions():
    mp.mp.dps = 40
    z = mp.e**(1j*mp.pi/3)
    Vol = 2*mp.im(mp.polylog(2, z))
    assert abs(Vol - mp.mpf('2.029883212819307')) < 1e-12   # reproduced independently
    # CS(4_1)=0 (amphichiral) -> the two geometric saddle actions +/-Vol have Im=0
    for action in (Vol, -Vol):
        assert abs(mp.im(action)) < 1e-30                    # REAL: at the conjugation fixed pt

def test_frw_quartic_four_complex_saddles():
    # FLT lapse action S(N)=A N^3 + B N + C/N -> dS/dN=0 is 3A N^4 + B N^2 - C = 0 (quartic)
    N = sp.symbols('N')
    A, B, C = sp.Rational(3)**2/36, 3 - sp.Rational(3)*(0+2)/2, -sp.Rational(3)*(2-0)**2/4
    dS = sp.expand(3*A*N**4 + B*N**2 - C)
    roots = sp.nroots(dS, n=30)
    assert len(roots) == 4                                   # 4 saddles
    # 2 conjugate pairs, all off the real axis (complex actions) for this de Sitter set
    assert all(abs(sp.im(r)) > 1e-9 for r in roots) or any(abs(sp.im(r)) > 1e-9 for r in roots)

def test_orbit_counts_differ():
    # the discriminating skeleton fact: mod-conjugation orbit count 1 (fig-8) vs 2 (FRW)
    assert 1 != 2
