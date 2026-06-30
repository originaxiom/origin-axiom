"""B302 -- the multiplicity thread: the generation ℤ/3 is the figure-eight's HIDDEN SYMMETRY (relational, not internal).
Run with sage-python (SnapPy + Sage NF) for the reproducer; verdict.py re-checks the algebra in pyenv.

The root-insight thread (continuing B298/B300): a VALUE is relational; the object is a monad; the two open walls map to
the owner's two relational sources -- Wall A (couplings) <-> the seam, Wall B (generations) <-> MULTIPLICITY. This
pursues Wall B. The degree-2 obstruction (B298) said one object can't make a multiplicity of 3. The fresh reframe:
the "3" is not IN the object, it is in the object's RELATION to its arithmetic siblings -- the commensurability class.

THE RESULT (the ℤ/3 is a hidden symmetry):
  (A) the OBJECT has no order-3: Sym(m004)=D4 (order 8=2^3), and the knot group is TORSION-FREE. [SnapPy]
  (B) the COMMENSURATOR does: m004 is THE arithmetic ℚ(√−3) knot (B282), so by Neumann-Reid its commensurator is the
      Bianchi group PGL(2,O_-3) -- which has order-3 elements (ℚ(√−3) has the Eisenstein units ω, the only imaginary-
      quadratic field besides ℚ(i) with extra units). Exhibited: [[0,-1],[1,-1]] (order 3 already in SL(2,ℤ)) and the
      Eisenstein diag(ω,1) (order 3, ω the cube-root unit). These are HIDDEN symmetries -- in Comm, not in Sym.
  (C) the figure-eight is a finite cover (index 12, Riley; covolume check) of the minimal orbifold ℍ^3/PGL(2,O_-3),
      which carries that order-3 torsion. m003 (the sister, B282) is in the SAME class (same vol 2.0299, same field).

CONSEQUENCE: the generation ℤ/3 is RELATIONAL -- present in the arithmetic commensurability class (the relation to
siblings/covers), absent from the single torsion-free object. This EXPLAINS B298 (the degree-2 obstruction = the knot
group is torsion-free) and is tied to B282 (the figure-eight is the unique arithmetic ℚ(√−3) knot with hidden
symmetries -- Neumann-Reid). It LOCATES the multiplicity where the root insight predicted (the relation), it does NOT
derive three generations (the physics dictionary is firewalled, [LEAP] in S045). Nothing to CLAIMS.
"""
import snappy
from sage.all import Matrix, NumberField, PolynomialRing, QQ


def object_has_no_order3():
    S = snappy.Manifold('m004').symmetry_group()
    return str(S), S.order()                              # D4, 8 (=2^3, no order-3); knot group torsion-free


def eisenstein_order3_elements():
    R = PolynomialRing(QQ, 'x'); x = R.gen()
    K = NumberField(x**2 + x + 1, 'w'); w = K.gen()       # O_-3 = Z[w], w a primitive cube root
    g = Matrix(K, [[0, -1], [1, -1]])                     # order 3 already in SL(2,Z) < SL(2,O_-3)
    h = Matrix(K, [[w, 0], [0, 1]])                       # Eisenstein order-3 in PGL(2,O_-3)
    return (g**3 == Matrix.identity(K, 2)), (w**3 == 1)


def cover_index_of_minimal_orbifold():
    # covol(PSL(2,O_-3)) by Humbert: |d|^{3/2} zeta_K(2)/(4 pi^2); index = vol(m004)/covol
    import mpmath as mp
    mp.mp.dps = 25
    d = 3
    # zeta_{Q(sqrt-3)}(2) = zeta(2) * L(2, chi_-3)
    L2 = mp.mpf(0)
    for n in range(1, 200000):
        chi = 1 if n % 3 == 1 else (-1 if n % 3 == 2 else 0)
        L2 += chi / mp.mpf(n)**2
    zetaK2 = mp.zeta(2) * L2
    covol = mp.mpf(d)**mp.mpf('1.5') * zetaK2 / (4 * mp.pi**2)
    vol_m004 = mp.mpf('2.029883212819307')
    return float(vol_m004 / covol)                        # ~12 (Riley)


if __name__ == "__main__":
    sym, order = object_has_no_order3()
    print(f"(A) m004 Sym = {sym} (order {order} = 2^3) -> NO order-3; knot group torsion-free")
    g3, w3 = eisenstein_order3_elements()
    print(f"(B) commensurator PGL(2,O_-3) has order-3: [[0,-1],[1,-1]]^3=I: {g3}; Eisenstein w^3=1: {w3}  (HIDDEN)")
    idx = cover_index_of_minimal_orbifold()
    print(f"(C) figure-eight covers minimal orbifold H^3/PGL(2,O_-3): index = {idx:.1f} (~12, Riley); carries order-3")
    print("\nVERDICT: the generation ℤ/3 is the figure-eight's HIDDEN SYMMETRY -- relational (in the commensurability")
    print("class), absent in the single torsion-free object. Explains B298; tied to B282. Generation-reading firewalled.")
    assert order == 8 and g3 and w3 and abs(idx - 12) < 0.5
