"""B251 (sage-python cross-check) -- the figure-eight is the unique metallic knot complement; det=5, double cover
L(5,2). Run: sage-python metallic_specificity_sage.py (needs SnapPy). Cross-checks the pyenv H1 computation."""
import snappy

M = snappy.Manifold("4_1")
print("4_1 (= m=1 metallic bundle):")
print("  H1 =", M.homology(), "  (knot complement in S^3 => Z)")
A = M.alexander_polynomial()
print("  Alexander poly =", A, "  det = |Delta(-1)| =", abs(A(-1)))           # 5
print("  identifiers:", [str(x) for x in M.identify()[:3]])                   # m004 = 4_1 = b(5,2)
print("  => figure-eight = 2-bridge knot b(5,2); double branched cover = L(5,2)=S^3/Z5, |H1|=5.")
print("\n(The pyenv computation H1(M_m)=Z(+)(Z/m)^2 shows m>=2 have H1 != Z, so are NOT knot complements in S^3.)")
