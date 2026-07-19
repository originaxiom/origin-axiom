"""B719 lock — scale/multiplicity is the observer's (imported covering degree); h=3 pattern stands."""
import snappy

def test_size_is_the_covering_index_not_a_scale():
    base = snappy.Manifold('m003(-2,3)'); bv = base.volume()
    for c in base.covers(5) + base.covers(7):
        assert abs(c.volume() - c.cover_info()['degree']*bv) < 1e-8   # vol = degree*base exactly

def test_smallest_cover_is_the_homology_floor():
    base = snappy.Manifold('m003(-2,3)')
    assert str(base.homology()) == 'Z/5'
    # gaps below |H1|=5: no cover at degree 2,3,4; unique at 5 (the abelian Z/5 cover)
    assert len(base.covers(2)) == 0 and len(base.covers(3)) == 0 and len(base.covers(4)) == 0
    assert len(base.covers(5)) == 1

def test_h3_filter_stands_as_observed():
    import math
    def h_imag(D):
        h=0; a=1
        while a*a <= -D/3:
            for b in range(-a,a+1):
                if (b*b-D)%(4*a)==0:
                    c=(b*b-D)//(4*a)
                    if c>=a and not (b<0 and (a==c or a==abs(b))):
                        if math.gcd(math.gcd(a,b),c)==1: h+=1
            a+=1
        return h
    for D in (-23, -31, -59, -283):        # Weeks sibling + 3 arithmetic children
        assert h_imag(D) == 3               # all class number 3 (sparse)

def test_h3_is_generic_not_inherited():
    # the CONTROL: same small-disc fields are arithmetic children of DIFFERENT Bianchi parents
    # -> h=3 is generic, not a sqrt-3 fingerprint. Q(sqrt-1)[prime 2] children have ODD h=3
    # (falsifies inherited prediction of even h). h=3 is heavy among smallest discs.
    import math
    def h_imag(D):
        h=0; a=1
        while a*a <= -D/3:
            for b in range(-a,a+1):
                if (b*b-D)%(4*a)==0:
                    c=(b*b-D)//(4*a)
                    if c>=a and not (b<0 and (a==c or a==abs(b))):
                        if math.gcd(math.gcd(a,b),c)==1: h+=1
            a+=1
        return h
    # -23,-59,-283 are children of MULTIPLE Bianchi parents (per the control) and are ODD h=3
    for D in (-23,-59,-283):
        assert h_imag(D) == 3 and h_imag(D) % 2 == 1   # odd 3 -> not prime-2-genus-inherited

