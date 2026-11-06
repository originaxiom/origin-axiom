"""Data-free: the shortest closed geodesic (the run's tube) of the excursion members L^6 R (LR)^k, from SnapPy's length
spectrum, with the volume -- the tube's length stays put while each golden period adds about m004's volume."""
import warnings; warnings.filterwarnings("ignore")
import snappy
if __name__ == "__main__":
    prev = None
    for k in range(0, 6):
        w = "LLLLLLR" + "LR" * k
        M = snappy.Manifold("b++" + w); v = float(M.volume())
        L = M.length_spectrum_alt(count=1)[0].length
        print(f"k={k} {w:18s} volume {v:.6f}  shortest geodesic {float(L.real):.6f}{float(L.imag):+.6f}i" + (f"  volume step {v - prev:.6f}" if prev is not None else ""))
        prev = v
    print("m004 volume", float(snappy.Manifold("m004").volume()))
