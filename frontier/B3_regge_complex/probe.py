"""
Frontier probe B3 — the figure-eight triangulation and the 4D Regge question.

  SPECULATIVE FRONTIER WORK. Outputs are *logged observations*, not claims.
  See ../../GOVERNANCE.md sec. 5 and ./README.md.

Question (ROADMAP.md, probe B3; handoff "Step 5A"):
  Build a 4D Regge complex by stacking figure-eight slices by the monodromy A,
  count its simplices, and move toward Regge calculus -> Einstein.

This probe does the part that is rigorous -- the figure-eight's 3D ideal
triangulation and its Regge edge/gluing check -- then states honestly why the
"4D stacking" step is not yet a well-defined construction.

Run:  python frontier/B3_regge_complex/probe.py
"""

import sympy as sp

# --- Figure-eight (4_1) standard ideal triangulation -----------------------
# Standard fact (Thurston, "The Geometry and Topology of 3-Manifolds"): the
# figure-eight knot complement admits an ideal triangulation by 2 regular ideal
# tetrahedra. These counts are verifiable in SnapPy (Manifold("4_1")).
NUM_TETRAHEDRA = 2
NUM_EDGE_CLASSES = 2          # 12 tetrahedron-edges glued into 2 classes
NUM_FACE_CLASSES = 4          # 8 tetrahedron-faces glued in pairs
NUM_CUSPS = 1

# A regular ideal tetrahedron (shape z = exp(i*pi/3)) has all six dihedral
# angles equal to pi/3.
DIHEDRAL = sp.pi / 3


def regge_edge_check():
    """3D Regge / gluing-equation check at the complete hyperbolic structure.

    In 3D Regge calculus curvature concentrates on edges (1D hinges). The
    deficit angle at an edge is 2*pi minus the sum of dihedral angles meeting
    there. The complete hyperbolic structure is the zero-deficit solution.
    """
    total_dihedral = NUM_TETRAHEDRA * 6 * DIHEDRAL   # 6 edges per tetrahedron
    angle_sum_per_edge = total_dihedral / NUM_EDGE_CLASSES
    deficit = sp.simplify(2 * sp.pi - angle_sum_per_edge)
    return {
        "total_dihedral_angle": total_dihedral,
        "dihedral_angles_per_edge": total_dihedral / NUM_EDGE_CLASSES / DIHEDRAL,
        "angle_sum_per_edge": angle_sum_per_edge,
        "deficit_per_edge": deficit,
        "gluing_equations_satisfied": deficit == 0,
    }


def four_d_requirements():
    """What a genuine 4D Regge complex needs -- and what the handoff omits."""
    return [
        "a 4-MANIFOLD -- the handoff names none; the figure-eight is a 3-manifold",
        "a triangulation by 4-simplices (the handoff gives no 4-cell)",
        "2-face (triangle) hinges -- in 4D, curvature concentrates on triangles",
        "a deficit rule  delta(triangle) = 2*pi - sum of dihedral angles around it",
        "the Regge action  S = sum over triangles of (area * deficit)",
    ]


def main():
    print("=" * 72)
    print("Frontier probe B3 -- figure-eight triangulation & the 4D Regge question")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md sec. 5)")
    print("=" * 72)

    print("\n[1] Figure-eight (4_1) ideal triangulation -- exact, standard")
    print(f"    tetrahedra      = {NUM_TETRAHEDRA}  (both regular ideal, z = exp(i*pi/3))")
    print(f"    edge classes    = {NUM_EDGE_CLASSES}")
    print(f"    face classes    = {NUM_FACE_CLASSES}")
    print(f"    cusps           = {NUM_CUSPS}")

    c = regge_edge_check()
    print("\n[2] 3D Regge / gluing-equation check at the complete structure")
    print(f"    dihedral angle (regular ideal tet)   = pi/3")
    print(f"    dihedral angles meeting per edge     = {c['dihedral_angles_per_edge']}")
    print(f"    angle sum per edge                   = {c['angle_sum_per_edge']}")
    print(f"    Regge deficit per edge               = {c['deficit_per_edge']}")
    print(f"    gluing equations satisfied (flat)    = {c['gluing_equations_satisfied']}")

    print("\n[3] What a 4D Regge complex would require")
    for i, req in enumerate(four_d_requirements(), 1):
        print(f"    ({i}) {req}")

    print("\n[verdict]  See README.md. In brief: the 3D triangulation and its")
    print("Regge edge-equation are exact and satisfied (zero deficit at the")
    print("complete hyperbolic structure). The handoff's '4D complex by stacking")
    print("figure-eight slices' is NOT a defined construction -- it supplies no")
    print("4-manifold and no 4-simplices. B3 identifies that undefined step as")
    print("the real gap on the path toward Regge -> Einstein.")


if __name__ == "__main__":
    main()
