"""B262 reproducibility -- the figure-eight gluing data from SnapPy (the ground truth Rung 1 builds on).
Run with sage-python (SnapPy env), NOT pyenv. Output is hard-coded into t41_theory.py."""
import snappy

M = snappy.Manifold('4_1')
print("manifold:", M.name(), "num_tetrahedra:", M.num_tetrahedra(), "num_cusps:", M.num_cusps())
print("complete-structure shapes:", [complex(z) for z in M.tetrahedra_shapes('rect')])
print("gluing equations (rect [a_0,a_1, b_0,b_1, c]; rows = edges then cusp meridian,longitude):")
for r in M.gluing_equations(form='rect'):
    print("   ", list(r))
# expected: 2 tetra, 1 cusp, both shapes 0.5+0.866i; edges [[2,2],[-1,-1],1] and its negative;
# meridian [[1,1],[0,-1],-1], longitude [[0,4],[0,-2],1].
