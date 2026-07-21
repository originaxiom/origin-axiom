"""cc3: the record run with the RELATION-VERIFIED holonomy pair B21=+z (GL(2,O)-conjugate
to the -z pair; indices provably identical -- this run makes it concrete)."""
import sys; sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location("v", "b734_independent_verify.py")
v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

def knot_image_plus(M, with_minus=True):
    E, Z, z = (1,0), (0,0), (0,1)
    mul, add, neg = v.make_ring(M)
    A = (E, E, Z, E); B = (E, Z, z, E)          # +z (the relation-verified pair)
    gens = [A, B] + ([(neg(E), Z, Z, neg(E))] if with_minus else [])
    return v.bfs(M, gens)

for M, amb in ((2,60),(4,3840),(8,245760),(16,60*64**3)):
    img  = knot_image_plus(M, True)
    img0 = knot_image_plus(M, False)
    mul, add, neg = v.make_ring(M); Z2=(0,0)
    cen = v.central_scalars(M)
    cin = len([c for c in cen if (c,Z2,Z2,c) in img0])
    print(f"LEVEL {M} [+z pair]: |<A,B,-I>|={len(img)}, |<A,B>|={len(img0)}, central-in={cin}, "
          f"T_SL={amb//len(img)}, T_PSL={(amb//len(cen))//(len(img0)//cin)}")
    sys.stdout.flush()
