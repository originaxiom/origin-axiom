#!/usr/bin/env python3
"""(1) TOWER IDENTITY, own code. Verify m004's cyclic covers of degree 2..5 against the claimed census names,
with an orientation-aware test: SnapPy's is_isometric_to on ORIENTED manifolds returns orientation-preserving
isometries only; we corroborate by also testing against the orientation-REVERSED census manifold and by
comparing the complex volume (Vol + i CS): an orientation-reversing identification flips the sign of CS."""
import warnings, sys
warnings.filterwarnings("ignore")
import snappy

CLAIM = {2: 'm206', 3: 's961', 4: 't12839', 5: 'o10_150696'}

print("snappy", snappy.__version__)
base = snappy.Manifold('m004')
print("m004: solution_type=%s  oriented=%s  H1=%s  vol=%.12f" % (
    base.solution_type(), base.is_orientable(), base.homology(), base.volume()))
print()
for n in (2, 3, 4, 5):
    covs = base.covers(n, cover_type='cyclic')
    assert len(covs) == 1, (n, len(covs))
    Y = covs[0]
    Y.randomize()
    name = CLAIM[n]
    C = snappy.Manifold(name)
    # orientation-aware: forward and against the mirror
    fwd = Y.is_isometric_to(C, return_isometries=True)
    Cm = snappy.Manifold(name); Cm.reverse_orientation()
    rev = Y.is_isometric_to(Cm, return_isometries=True)
    dets = []
    for iso in (fwd or []):
        try:
            for m in iso.cusp_maps():
                dets.append(int(round(m[0,0]*m[1,1]-m[0,1]*m[1,0])))
        except Exception as e:
            dets.append('?%s' % e)
    try:
        cvY = Y.complex_volume(); cvC = C.complex_volume()
    except Exception as e:
        cvY = cvC = 'err %s' % e
    print("Y_%d  deg=%d  H1(Y_%d) = %s" % (n, n, n, Y.homology()))
    print("     claimed %-12s H1 = %s" % (name, C.homology()))
    print("     vol(Y)= %.12f   vol(%s)= %.12f   diff=%.2e" % (Y.volume(), name, C.volume(), abs(Y.volume()-C.volume())))
    print("     complex vol Y = %s ;  %s = %s" % (cvY, name, cvC))
    print("     is_isometric_to(%s)          -> %s   (cusp-map dets %s)" % (name, bool(fwd), dets))
    print("     is_isometric_to(mirror %s)   -> %s" % (name, bool(rev)))
    print("     num_cusps Y=%d  C=%d ;  Y.identify() = %s" % (Y.num_cusps(), C.num_cusps(), Y.identify()))
    print()
