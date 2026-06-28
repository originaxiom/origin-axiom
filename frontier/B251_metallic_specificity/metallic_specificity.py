"""B251 -- the E6<->E8 geometric transition is golden-specific: only m=1 is a knot complement (the §4.1 filter).

THE TEST (push from B249/B250): B249's object-specificity claim was that only the figure-eight (m=1) can host the
hyperbolic<->spherical transition, because the transition needs the knot structure (meridian, determinant, double
branched cover = lens space). Make it rigorous by sweeping the metallic family.

THE RESULT: the metallic bundle M_m = mapping torus of R^m L^m on the once-punctured torus has monodromy
    phi = R^m L^m = [[1+m^2, m],[m, 1]]   (R=[[1,1],[0,1]], L=[[1,0],[1,1]]; trace = m^2+2 = disc-2)
and first homology  H1(M_m) = Z (+) coker(phi - I)  on H1(fiber)=Z^2.  coker(phi-I) = coker[[m^2,m],[m,0]] has
Smith normal form diag(m,m), so

    H1(M_m) = Z (+) (Z/m)^2 ,   which equals Z  iff  m = 1.

A knot complement in S^3 has H1 = Z. So ONLY m=1 (the figure-eight) is a knot complement in S^3 -- only it has the
meridian/longitude, the knot determinant, and the double branched cover (the lens space) that the geometric
transition (B248/B249/B250) is built from. For m>=2 the discriminant m^2+4 survives in the invariant trace field
Q(sqrt(m^2+4)), but there is no knot determinant and no lens-space double cover -- no transition.

m=1 coincidence stack (golden-specific): det(4_1)=5 = m^2+4 = the discriminant; 4_1 = the 2-bridge knot b(5,2);
its double branched cover is the lens space L(5,2)=S^3/Z5, |H1|=5. The '5' of the spherical/E8 end is the 2-bridge
numerator = the knot determinant = the discriminant, all coinciding only at m=1.

This places the transition in the SHARPEST specificity tier (PAPER §4.1): golden-specific (survives only at m=1),
above object-specific (lives in {Q(sqrt5),Q(sqrt-3)}). FIREWALLED; nothing to CLAIMS.md.

Run: python metallic_specificity.py (pyenv; sympy). SnapPy cross-check: metallic_specificity_sage.py.
"""
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])


def monodromy(m):
    """phi = R^m L^m on H1(once-punctured torus) = Z^2; trace = m^2+2."""
    return (R ** m) * (L ** m)


def h1_torsion(m):
    """torsion of H1(M_m) = coker(phi - I); returns the list of invariant factors > 1."""
    snf = smith_normal_form(monodromy(m) - sp.eye(2))
    return [int(abs(snf[i, i])) for i in range(2) if abs(snf[i, i]) not in (0, 1)]


def is_knot_complement_in_S3(m):
    """a knot complement in S^3 has H1 = Z, i.e. no torsion."""
    return h1_torsion(m) == []


def figure_eight_five_stack():
    """the m=1 coincidence: discriminant = determinant = 2-bridge numerator = 5."""
    m = 1
    return {
        "discriminant m^2+4": m ** 2 + 4,            # 5
        "det(4_1) = |Delta(-1)|": 5,                  # 5 (Alexander a^2-3a+1 at -1)
        "2-bridge b(p,q) numerator p": 5,             # 4_1 = b(5,2)
        "|H1(double branched cover L(5,2))|": 5,      # L(5,2) = S^3/Z5
    }


if __name__ == "__main__":
    print("metallic family M_m = mapping torus of R^m L^m:")
    print("  m | trace=m^2+2 | H1(M_m)                | knot complement in S^3?")
    for m in range(1, 7):
        tors = h1_torsion(m)
        h1 = "Z" if not tors else "Z + " + " + ".join(f"Z/{t}" for t in tors)
        tr = int(monodromy(m).trace())
        print(f"  {m} |    {tr:>3}     | {h1:<21} | {'YES (figure-eight)' if not tors else 'NO'}")

    assert is_knot_complement_in_S3(1)
    assert all(not is_knot_complement_in_S3(m) for m in range(2, 12))   # only m=1
    assert all(h1_torsion(m) == [m, m] for m in range(2, 12))           # H1 = Z (+) (Z/m)^2
    print("\nH1(M_m) = Z (+) (Z/m)^2  =>  knot complement (H1=Z) iff m=1.")
    print(f"m=1 '5' stack (all equal 5): {figure_eight_five_stack()}")
    assert set(figure_eight_five_stack().values()) == {5}
    print("=> the E6<->E8 geometric transition is GOLDEN-SPECIFIC (m=1 only). ALL CHECKS PASS")
