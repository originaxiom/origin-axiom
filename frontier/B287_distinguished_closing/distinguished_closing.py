"""B287 -- THE DISTINGUISHED CLOSING (the selection spine). Run with sage-python (SnapPy + Regina + Twister).

B286 located the four ingredients at the seam (the cusp / Dehn filling) but left the load-bearing question open:
are the closings SELECTIVE (one distinguished world) or a flat CATALOGUE? This answers it for the object's OWN
structure. The figure-eight is a once-punctured-torus BUNDLE, so the fiber-slope filling caps the puncture and yields
the closed Sol torus bundle whose monodromy is EXACTLY A = [[2,1],[1,1]] = the A=LR of the proven core (P1), with the
P8 torsion ladder |det(A^n - I)| in its cyclic covers. A canonical distinguished closing lives inside the proven core.

Verifies (three independent methods on the headline + the stratification):
  1. ALEXANDER POLYNOMIAL of m004 = t^2 - 3t + 1 = charpoly(A): the fibration monodromy on H1(fiber) is A.
  2. TWISTER: the once-punctured-torus bundle with monodromy word 'aB' = [[2,1],[1,1]] = A is ISOMETRIC to m004.
  3. REGINA: m004(0,1) (the fiber/0-slope filling) is recognised as  T x I / [ 2,1 | 1,1 ]  -- the closed torus
     bundle with monodromy EXACTLY A. It is the UNIQUE torus bundle (Sol) among the 10 exceptional fillings;
     the others stratify (Seifert x6, toroidal x2, S^3 x1).
  4. P8 LADDER: |det(A^n - I)| = 1,5,16,45,... = L_{2n} - 2 = the H1-torsion of the closed A^n torus bundles
     (the fiber-direction cyclic covers); the 0-surgery is the n=1 base (torsion 1, H1 = Z).
"""
import snappy
import regina


A = [[2, 1], [1, 1]]                                   # P1: A = LR, trace 3, eigenvalues phi^2, phi^-2


def alexander_check():
    return str(snappy.Manifold('m004').alexander_polynomial())   # 'a^2 - 3*a + 1' = charpoly(A)


def twister_bundle_is_m004(word='aB'):
    import snappy.twister as tw
    B = snappy.Manifold(tw.Surface('S_1_1').bundle(monodromy=word))   # 'aB' = t_alpha t_beta^-1 = [[2,1],[1,1]] = A
    return bool(B.is_isometric_to(snappy.Manifold('m004'))), float(B.volume())


def regina_recognise(p, q, tries=8):
    M = snappy.Manifold('m004'); M.dehn_fill((p, q))
    T = regina.Triangulation3(M.filled_triangulation())
    for _ in range(tries):
        T.simplify()
        std = regina.StandardTriangulation.recognise(T)
        if std and std.manifold():
            return std.manifold().name()
    return None


def classify_exceptionals():
    out = {}
    for n in range(-4, 5):
        M = snappy.Manifold('m004'); M.dehn_fill((n, 1))
        out[n] = (str(M.homology()), regina_recognise(n, 1))
    return out


def p8_ladder(nmax=6):
    # |det(A^n - I)| via integer matrix powers (no sympy needed here)
    def matmul(X, Y): return [[X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]],
                              [X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]]]
    P = [[1, 0], [0, 1]]; lad = []
    for _ in range(1, nmax + 1):
        P = matmul(P, A)
        det = (P[0][0]-1)*(P[1][1]-1) - P[0][1]*P[1][0]
        lad.append(abs(det))
    return lad


if __name__ == "__main__":
    print("1. Alexander poly m004:", alexander_check(), " (= charpoly A = t^2-3t+1)")
    iso, vol = twister_bundle_is_m004('aB')
    print(f"2. Twister bundle monodromy 'aB'=[[2,1],[1,1]]=A : vol={vol:.5f}  isometric to m004 = {iso}")
    print("\n3. Regina recognition of the 10 exceptional fillings (integer slopes; + meridian = S^3):")
    cls = classify_exceptionals()
    for n in range(-4, 5):
        tag = "   <-- DISTINGUISHED: torus bundle, monodromy = A (P1)" if n == 0 else ""
        print(f"   m004({n:+d},1): H1={cls[n][0]:<5}  {cls[n][1]}{tag}")
    torus_bundles = [n for n in cls if cls[n][1] and cls[n][1].startswith('T x I')]
    print("   => unique torus bundle (Sol) among the exceptionals:", torus_bundles)
    assert torus_bundles == [0]
    assert cls[0][1] == "T x I / [ 2,1 | 1,1 ]"          # monodromy EXACTLY A

    print("\n4. P8 torsion ladder |det(A^n - I)| =", p8_ladder(), " (= L_{2n}-2; n=1 -> 1 -> H1(0-surgery)=Z)")
    print("\nVERDICT: SELECTIVE for the object's own structure. The fiber-slope closing is the unique distinguished")
    print("closing; it re-instantiates the proven-core monodromy A=[[2,1],[1,1]] (P1) and the P8 torsion ladder.")
