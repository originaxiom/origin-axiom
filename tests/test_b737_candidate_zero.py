"""B737 lock -- Candidate Zero: the object's voice is an exact zeta-quotient (Res phi = 2sqrt3/vol),
the voice carries object-specific data (disc -48 cusp CM, level palette 1/2/8), but the crux dies:
the zeta is the FIELD's (present for all h=1 fields with no manifold). Pure math (Gate 5).
"""
import mpmath as mp
import pytest

mp.mp.dps = 40

def _L_chi3(s):
    # L(s, chi_-3) via Hurwitz zeta (valid s != 1)
    return 3**(-mp.mpf(s)) * (mp.zeta(s, mp.mpf(1)/3) - mp.zeta(s, mp.mpf(2)/3))

def test_voice_residue_equals_2sqrt3_over_volume():
    snappy = pytest.importorskip("snappy")
    vol = mp.mpf(str(snappy.ManifoldHP("m004").volume()))
    zK2 = mp.zeta(2) * _L_chi3(2)
    res_phi = 2*mp.pi**2 / (9*zK2)              # Res_{s=2} phi = (h/w)/Lambda_K(2) closed form
    assert abs(res_phi - 2*mp.sqrt(3)/vol) < mp.mpf("1e-15")   # the new identity: Res phi = 2sqrt3/vol(m004)

def test_humbert_cover_index_12():
    snappy = pytest.importorskip("snappy")
    vol = mp.mpf(str(snappy.ManifoldHP("m004").volume()))
    zK2 = mp.zeta(2) * _L_chi3(2)
    vol_orb = 3**mp.mpf(1.5) * zK2 / (4*mp.pi**2)              # Humbert: |d|^{3/2} zeta_K(2)/(4 pi^2)
    assert abs(vol/vol_orb - 12) < mp.mpf("1e-12")             # m004 = degree-12 cover of the Bianchi orbifold

def test_ssb_number_is_the_zeta_residue():
    # Res_{s=1} zeta_K = L(1,chi_-3) = 2pi/(6 sqrt3) -- the exact B736-P2 SSB number.
    # (Hurwitz-difference near s=1 suffers catastrophic cancellation of the two ~1/(s-1) poles,
    #  so evaluate at a safe offset with matching tolerance: L is analytic at 1 with O(1) slope.)
    val = _L_chi3(mp.mpf(1) + mp.mpf("1e-8"))
    assert abs(val - 2*mp.pi/(6*mp.sqrt(3))) < mp.mpf("1e-6")
    # and the exact closed form (class-number formula, h=1, w=6, |d|=3) pins the 20-digit value:
    assert abs(2*mp.pi/(6*mp.sqrt(3)) - mp.mpf("0.60459978807807261686")) < mp.mpf("1e-18")

def test_cusp_shapes_object_specific_disc48_vs_hexagonal():
    # m003 cusp = hexagonal (j=0); m004 cusp = C/(Z+2sqrt(-3)Z), CM by the conductor-4 order (disc -48):
    # j(2 sqrt3 i) is the larger root of x^2 - 2835810000 x + 6549518250000 (Hilbert class poly h(-48)=2).
    j4 = mp.kleinj(2*mp.sqrt(3)*mp.j) * 1728
    b, c = -2835810000, 6549518250000
    r_big = (-b + mp.sqrt(b*b - 4*c)) / 2
    assert abs(j4 - r_big) / r_big < mp.mpf("1e-14")
    assert abs(mp.kleinj(mp.exp(mp.pi*mp.j/3))) < mp.mpf("1e-24")   # hexagonal point: j = 0 (m003 / the orbifold)

def test_level_palette_1_2_8():
    # |(O_3/2^k)^x / mu_6| = 1, 2, 8 at levels (2),(4),(8): the character palette grows with the level.
    def units(k):
        m = 2**k
        def mul(p, q):
            (x, y), (u, v) = p, q
            return ((x*u - y*v) % m, (x*v + y*u - y*v) % m)
        els = [(x, y) for x in range(m) for y in range(m)]
        U = [e for e in els if any(mul(e, f) == (1, 0) for f in els)]
        z6 = (1, 1); x = (1, 0); n = 0
        for _ in range(12):
            x = mul(x, z6); n += 1
            if x == (1, 0): break
        return len(U), n
    pal = []
    for k in (1, 2, 3):
        u, mu = units(k); pal.append(u // mu)
    assert pal == [1, 2, 8]

def test_crux_field_invariance_kills_the_bridge():
    # The P4 discriminator: the "shared substrate" (partition-pole residue 2 pi h/(w sqrt|d|)) exists for
    # EVERY h=1 imaginary-quadratic field with NO manifold present -> zero discriminating power for m004.
    # Lock the residue values for d=-3,-4: both are field facts (class-number formula), object-free.
    r3 = 2*mp.pi*1/(6*mp.sqrt(3))          # d=-3, w=6
    r4 = 2*mp.pi*1/(4*mp.sqrt(4))          # d=-4, w=4  -> pi/4
    assert abs(r3 - mp.mpf("0.60459978807807261686")) < mp.mpf("1e-18")
    assert abs(r4 - mp.pi/4) < mp.mpf("1e-25")
    # both computed with no reference to any 3-manifold => the zeta structure is the FIELD's (outcome B).
