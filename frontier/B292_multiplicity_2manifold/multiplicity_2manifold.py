"""B292 -- WHICH 2-MANIFOLD supplies the multiplicity? Run with sage-python (SnapPy). Phase IV (wall #4).

The owner's thesis names 'multiplicity of one or more items' as a third source (besides object + interaction with the
nothing). B277 fixed wall #4: a canonical N=2 lift exists (the fiber class-S theory), a chiral 4d SM is blocked by two
named inputs. B292 asks, through the multiplicity lens: which candidate '2-manifold / family' supplies the
multiplicity -- the fiber Sigma_{1,1}, the metallic tower R^m L^m, or the filling family (1,n)?

The three candidates and their CHARACTER:
  (i)  the FIBER Sigma_{1,1} -- a literal 2-(real)-MANIFOLD (once-punctured torus, chi = -1), monodromy phi = RL =
       [[2,1],[1,1]] (trace 3, pseudo-Anosov). The class-S Riemann surface (class-S(A1,Sigma_{1,1}) = N=2* SU(2)),
       SHARED by every tower member. The ONE genuine 2-manifold. Supplies the N=2 lift; NOT chirality (B277).
  (ii) the metallic TOWER R^m L^m (m=1,2,3,...) -- a DISCRETE sequence of DISTINCT 3-manifolds (volumes 2.03, 3.66,
       4.81, ... increasing), traces m^2+2; arithmetic only m=1 (Q(sqrt-3)) and m=2 (Q(i)) (B125). An arithmetic
       family, not a surface.
  (iii) the FILLING family (1,n) -- a DISCRETE sequence of closed 3-manifolds (the scale ladder 2*pi/n, B290). A scale
       family, not a surface.

VERDICT (consolidating NEGATIVE). Only the FIBER is a 2-manifold; the tower and fillings are families of 3-manifolds
(discrete integer parameters), supplying multiplicity in the ARITHMETIC and SCALE senses. NONE supplies the N=2->N=1
CHIRAL datum -> wall #4 stays blocked (B277's two named reasons). Multiplicity is realized and TRIPARTITE; the chiral
4d SM construction is a STOP-GATE (NEEDS-SPECIALIST). FIREWALLED; nothing to CLAIMS.
"""
import snappy


def fiber_euler_char(g=1, n=1):
    return 2 - 2 * g - n                                # Sigma_{1,1}: chi = -1


def tower_member(m):
    return snappy.Manifold('b++' + 'R' * m + 'L' * m)   # R^m L^m once-punctured-torus bundle; m=1 = m004


def tower_is_distinct_sequence(mmax=4):
    vols = [float(tower_member(m).volume()) for m in range(1, mmax + 1)]
    distinct = len(set(round(v, 6) for v in vols)) == len(vols)
    increasing = all(vols[i] < vols[i + 1] for i in range(len(vols) - 1))
    return vols, distinct, increasing


if __name__ == "__main__":
    print(f"(i)  fiber Sigma_(1,1): chi = {fiber_euler_char()} (a 2-manifold); monodromy phi = RL, trace 3 (pAnosov)")
    print("     m=1 tower member == m004:", tower_member(1).is_isometric_to(snappy.Manifold('m004')))
    vols, distinct, incr = tower_is_distinct_sequence()
    print(f"(ii) metallic tower R^m L^m volumes = {[round(v,4) for v in vols]}  distinct={distinct} increasing={incr}")
    print("     traces m^2+2 =", [m**2 + 2 for m in range(1, 7)], " arithmetic only m=1 (Q(sqrt-3)), m=2 (Q(i)) [B125]")
    print("(iii) filling family (1,n): scale ladder 2*pi/n [B290] -- a discrete sequence of closed 3-manifolds")
    print("\nVERDICT: only the FIBER is a 2-manifold; tower=arithmetic family, fillings=scale family (both 3-mfld")
    print("sequences). NONE supplies the N=2->N=1 chiral datum -> wall #4 blocked (B277). Chiral 4d SM = STOP-GATE.")
    assert fiber_euler_char() == -1 and distinct and incr
