"""Data-free: each tetrahedron's hyperbolic volume (Bloch-Wigner D(z)) in the layered triangulation of the excursion members
b++ L^6 R (LR)^k, in SnapPy's tetrahedron order; integrity: the sum equals SnapPy's volume; the figure-eight control (two
regular tetrahedra, 1.0149416 each)."""
import warnings; warnings.filterwarnings("ignore")
import snappy, mpmath as mp
def D(z):
    z = mp.mpc(z); return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))
for word in ["LR"] + ["L"*6 + "R" + "LR"*k for k in (0, 1, 3, 5)]:
    M = snappy.Manifold("b++" + word)
    sh = [complex(z) for z in M.tetrahedra_shapes("rect")]
    vols = [float(D(z)) for z in sh]
    print("%-20s vol %.6f (sum of D %.6f)  per-tet: %s" % (word, float(M.volume()), sum(vols), " ".join("%.3f" % v for v in vols)))
