"""B287 verdict (pyenv; SnapPy/Regina/Twister-derived constants from distinguished_closing.py) -- THE DISTINGUISHED
CLOSING (the selection spine).

The load-bearing question B286 left open: are the closings SELECTIVE or a CATALOGUE? Answer for the object's OWN
structure: SELECTIVE. The figure-eight is a once-punctured-torus bundle; the fiber/0-slope filling caps the puncture
to the closed Sol torus bundle with monodromy EXACTLY A = [[2,1],[1,1]] (P1, A=LR), the UNIQUE torus bundle among the
10 exceptional fillings. Three independent methods agree (Alexander poly = charpoly A; Twister 'aB'=A isometric to
m004; Regina recognises m004(0,1) = T x I / [[2,1],[1,1]]). The P8 torsion ladder |det(A^n - I)| lives in its covers.

FIREWALL: this is pure topology. It shows the object re-instantiates its OWN proven-core monodromy at a canonical
closing. It does NOT select a Standard-Model world (the "distinguished closing = our universe" reading is a [HOOK]).
"""

# --- the proven-core matrix (P1) the distinguished closing re-instantiates ---
A = [[2, 1], [1, 1]]                                     # A = LR, trace 3, det 1, eigenvalues phi^2, phi^-2

# --- the 10 exceptional fillings, classified (SnapPy H1 + Regina recognition) ---
#   integer slopes (n,1) for n in -4..4, plus the meridian slope = S^3 (10 total, Thurston).
EXCEPTIONAL_INTEGER_SLOPES = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
EXCEPTIONAL_COUNT = len(EXCEPTIONAL_INTEGER_SLOPES) + 1     # + meridian(S^3) = 10

H1 = {-4: "Z/4", -3: "Z/3", -2: "Z/2", -1: "0", 0: "Z", 1: "0", 2: "Z/2", 3: "Z/3", 4: "Z/4"}
REGINA = {                                                 # positive Regina recognitions (None = recognizer incomplete)
    -4: "SFS [D:(2,1)(2,1)] U/m SFS [D:(2,1)(3,1)]",        # toroidal graph manifold
    -2: "SFS [S2:(2,1)(4,1)(5,-4)]",                        # Seifert fibered
     0: "T x I / [ 2,1 | 1,1 ]",                            # <-- Sol torus bundle, monodromy EXACTLY A
     2: "SFS [S2:(2,1)(4,1)(5,-4)]",                        # Seifert fibered (= the (-2) one; amphichirality)
     4: "SFS [D:(2,1)(2,1)] U/m SFS [D:(2,1)(3,1)]",        # toroidal graph manifold
}
# (-1)(+1) are the Brieskorn homology sphere Sigma(2,3,7) (Seifert, H1=0); (-3)(+3) Seifert with H1=Z/3.
# Regina's StandardTriangulation.recognise returns None on their simplified triangulations (recognizer incomplete);
# their Seifert types are classical (Thurston). NOT load-bearing: the headline is the UNIQUE torus bundle.
GEOMETRY_TYPE = {-4: "toroidal", -3: "Seifert", -2: "Seifert", -1: "Seifert", 0: "Sol (torus bundle)",
                 1: "Seifert", 2: "Seifert", 3: "Seifert", 4: "toroidal"}

# --- the three independent confirmations of the headline ---
ALEXANDER_POLYNOMIAL = "t^2 - 3*t + 1"                      # = charpoly(A); m004 fibration monodromy is A
TWISTER_WORD = "aB"                                         # t_alpha t_beta^-1 = [[2,1],[1,1]] = A
TWISTER_BUNDLE_ISOMETRIC_TO_M004 = True
REGINA_0SURGERY = "T x I / [ 2,1 | 1,1 ]"                   # monodromy matrix EXACTLY A
DISTINGUISHED_SLOPE = 0                                     # the fiber/0-slope (caps the puncture)
DISTINGUISHED_IS_UNIQUE_TORUS_BUNDLE = True                # only (0,1) is Sol/torus-bundle among the 10

# --- selection verdict (this axis) ---
SELECTIVE_FOR_OWN_STRUCTURE = True                         # a canonical closing re-sees A=LR (P1) + P8 ladder
DERIVES_SM_VALUES = False                                  # firewall: math selection, not a physical world


def charpoly_A():
    """charpoly of A, computed (pyenv sympy) -- must equal ALEXANDER_POLYNOMIAL."""
    import sympy as sp
    t = sp.symbols('t')
    M = sp.Matrix(A)
    return sp.expand((t * sp.eye(2) - M).det())            # t^2 - 3t + 1


def p8_torsion_ladder(nmax=6):
    """|det(A^n - I)| = the H1-torsion of the closed A^n torus bundles (P8). n=1 -> 1 -> H1(0-surgery)=Z."""
    import sympy as sp
    M = sp.Matrix(A); I = sp.eye(2)
    return [abs((M**n - I).det()) for n in range(1, nmax + 1)]


def verdict():
    import sympy as sp
    t = sp.symbols('t')
    charpoly_ok = sp.expand(charpoly_A() - (t**2 - 3*t + 1)) == 0
    ladder = p8_torsion_ladder()
    ladder_ok = ladder[:4] == [1, 5, 16, 45] and ladder[0] == 1     # n=1 torsion 1 <-> H1(0-surgery)=Z
    regina_ok = REGINA[0] == "T x I / [ 2,1 | 1,1 ]" and \
        [n for n in REGINA if REGINA[n].startswith("T x I")] == [0]
    return bool(charpoly_ok and ladder_ok and regina_ok
                and TWISTER_BUNDLE_ISOMETRIC_TO_M004 and DISTINGUISHED_IS_UNIQUE_TORUS_BUNDLE
                and SELECTIVE_FOR_OWN_STRUCTURE and not DERIVES_SM_VALUES)


if __name__ == "__main__":
    print("charpoly(A) =", charpoly_A(), " == Alexander poly m004")
    print("P8 torsion ladder |det(A^n-I)| =", p8_torsion_ladder())
    print("distinguished closing: m004(0,1) =", REGINA_0SURGERY, "(monodromy = A, P1)")
    print("unique torus bundle among the 10 exceptionals:", DISTINGUISHED_IS_UNIQUE_TORUS_BUNDLE)
    print("selective for own structure:", SELECTIVE_FOR_OWN_STRUCTURE, "| derives SM values:", DERIVES_SM_VALUES)
    print("verdict:", verdict())
