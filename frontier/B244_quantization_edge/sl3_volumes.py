"""B244 (sage-python part) -- the SL(3,C) complex volumes of the figure-eight via SnapPy's Ptolemy variety
(Zickert/Garoufalidis-Thurston-Zickert), the classical saddles of the (1)<->(2) quantization edge.
Requires sage-python (SnapPy). Run: sage-python sl3_volumes.py

RESULT (recorded, reproduced here):
  N=3 boundary-unipotent reps: obstruction class c0 has 3 reps (matching B71's 3 char-variety components),
  with complex volumes { +-8.11953285, 0, 0 }; obstruction class c1 has 1 rep, volume 0.
  The GEOMETRIC component (V0 = Sym^2 of the SL(2) discrete-faithful rep, B71) has volume
     8.11953285127723 = 4 * 2.02988321281931 = 4 * Vol(SL(2)),   i.e. the (n^3-n)/6 = 4 factor at n=3.
  The W1/W2 (Dehn-filling) components are volume 0 -- geometrically distinct from V0.
"""
import snappy


def sl3_complex_volumes(name="4_1"):
    M = snappy.Manifold(name)
    vol2 = M.volume()
    V = M.ptolemy_variety(3, obstruction_class="all")
    sols = V.compute_solutions()
    cvs = sols.complex_volume_numerical()
    return vol2, cvs


if __name__ == "__main__":
    vol2, cvs = sl3_complex_volumes("4_1")
    print(f"SL(2) volume of 4_1: {vol2}")
    print("SL(3) complex volumes per obstruction class (Im = volume):")
    geo = 0.0
    for ci, cls in enumerate(cvs):
        for grp in cls:
            for cv in grp:
                v = abs(complex(cv).real)      # SnapPy complex volume = Vol + i*CS; volume is the real part
                if v > geo:
                    geo = v
        print(f"  class c{ci}: {cls}")
    print(f"\ngeometric SL(3) volume = {geo}")
    print(f"4 * SL(2) volume       = {4 * vol2}   (factor (n^3-n)/6 = (27-3)/6 = 4 at n=3)")
    print(f"match: {abs(geo - 4 * vol2) < 1e-9}")
