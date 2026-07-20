"""B735 lock — the object's emittance: heartbeat traces = Eisenstein integers Z[w]; voice = the cusp
(open -> continuous spectrum, closed -> discrete). Structural math only (Gate 5).
"""
import mpmath as mp

def test_heartbeat_traces_are_eisenstein_integers():
    try:
        import snappy
    except ImportError:
        import pytest; pytest.skip("snappy unavailable")
    mp.mp.dps = 30
    M = snappy.Manifold("m004")
    def in_Zw(z, tol=1e-9):
        # Z[w] = Z[(1+sqrt-3)/2]: z = a + b*sqrt(-3), a,b half-integers of equal parity
        a = z.real; b = z.imag/float(mp.sqrt(3))
        return abs(2*a-round(2*a)) < tol and abs(2*b-round(2*b)) < tol and (round(2*a)-round(2*b)) % 2 == 0
    traces = []
    for g in list(M.length_spectrum(2.0))[:4]:
        L = complex(g.length)
        tr = complex(2*mp.cosh(mp.mpc(L.real, L.imag)/2))
        traces.append(in_Zw(tr))
    assert all(traces)                                     # length-spectrum traces in Z[w] = the being field

def test_voice_is_the_cusp_closing_silences_it():
    try:
        import snappy
    except ImportError:
        import pytest; pytest.skip("snappy unavailable")
    def open_cusps(M): return len([c for c in M.cusp_info() if c.is_complete])
    assert open_cusps(snappy.Manifold("m004")) == 1        # OPEN cusp -> continuous Laplacian spectrum (the voice)
    assert open_cusps(snappy.Manifold("m004(5,1)")) == 0   # CLOSED (filled) -> purely discrete -> voice silenced
    assert str(snappy.Manifold("m004(5,1)").homology()) != "Z"   # closed -> finite H1 (Z/5), not the open Z
