"""P-476's check (R76-1; data-free): vol(L^a R) against the Whitehead link's volume, with SnapPy (b++w = the orientable
punctured-torus bundle with monodromy +w). The volumes rise to 3.66386 from below, the gap falling like a^-2, so the
action weight e^(-Vol/pi) does not decay along the family: a measure built from it concentrates on short threads only
through a length cutoff. The table stops at a = 55: at a = 89 SnapPy's default triangulation is not all positively
oriented (a numerical limit of the solver, not used)."""
import warnings
warnings.filterwarnings("ignore")
import snappy
W = float(snappy.Manifold("L5a1").volume())
print(f"the Whitehead link L5a1: volume {W:.10f}")
prev = 0.0
for a in (1, 2, 3, 5, 8, 13, 21, 34, 55):
    M = snappy.Manifold("b++" + "L" * a + "R")
    assert M.solution_type() == "all tetrahedra positively oriented"
    v = float(M.volume()); assert prev < v < W; prev = v
    print(f"a = {a:3d}: vol(L^a R) = {v:.10f}, gap {W - v:.3e}, gap * a^2 = {(W - v) * a * a:.2f}")
