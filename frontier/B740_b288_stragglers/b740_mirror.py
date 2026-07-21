"""B740 mirror closure (sage b740_mirror.py): the 7 STILL-UNKNOWN slopes are (-p,q) mirrors of
RESOLVED (p,q) siblings; 4_1 is amphichiral so 4_1(p,q) ~ 4_1(-p,q) (orientation-reversing isometry)
=> same abstract invariant trace field => sqrt(-3)-containment inherited. Verify each isometry."""
import snappy
PAIRS = [((-7,8),(7,8)), ((-5,7),(5,7)), ((-5,8),(5,8)), ((-3,7),(3,7)), ((-3,8),(3,8)), ((-1,7),(1,7)), ((-1,8),(1,8))]
ok = 0
for (a, b) in PAIRS:
    Ma = snappy.Manifold('m004'); Ma.dehn_fill(a)
    Mb = snappy.Manifold('m004'); Mb.dehn_fill(b)
    try:
        iso = Ma.is_isometric_to(Mb)
    except Exception:
        # fall back: compare mirrored: reverse orientation of Mb
        try:
            Mbr = Mb.copy(); Mbr.reverse_orientation()
            iso = Ma.is_isometric_to(Mbr)
        except Exception as e:
            iso = f"ERR {e}"
    if iso is True: ok += 1
    print(a, "~", b, ":", iso, " vols:", round(float(Ma.volume()),10), round(float(Mb.volume()),10))
print(f"\nMIRROR CLOSURE: {ok}/{len(PAIRS)} isometries verified")
print("=> the 7 unknowns inherit their siblings' fields (conjugate = same abstract field);")
print("   sqrt(-3)-containment is conjugation-invariant => ALL CLEAN if all pairs verified.")
