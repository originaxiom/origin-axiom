"""B2007: the layer's law by GAP (run with sage's python: ~/.local/bin/sage -python -B gap_layer.py > gap_layer_run.txt).
For k = 3..6: |G_k|; the kernel of the action on the blocks of reduction to mod 3^(k-1) (the step's layer) and to mod 9 (the
whole layer K_k): orders, elementary abelian or not, abelian invariants, exponent, nilpotency class; G_k's abelian invariants."""
import json, pathlib, time
from sage.all import libgap
HERE = pathlib.Path(__file__).resolve().parent
data = json.loads((HERE / "orbits.json").read_text())
t0 = time.time()
for k in range(3, 7):
    d = data[str(k)]; n = d["n"]
    C = libgap.PermList([i + 1 for i in d["C"]]); S = libgap.PermList([i + 1 for i in d["S"]])
    G = libgap.Group([C, S]); size = int(G.Size())
    ab = [int(x) for x in G.AbelianInvariants()]
    def kernel_on(red):
        blocks = {}
        for i, b in enumerate(red): blocks.setdefault(b, []).append(i + 1)
        bl = libgap([sorted(v) for v in blocks.values()])
        hom = libgap.ActionHomomorphism(G, bl, libgap.OnSets)
        return libgap.Kernel(hom)
    Ks = kernel_on(d["red_prev"]); K = kernel_on(d["red9"])
    print("k = %d (mod %d, %d points): |G_k| = %d; G_k's abelian invariants %s  [%.0f s]" % (k, d["N"], n, size, ab, time.time() - t0), flush=True)
    print("    the step's layer (kernel to mod %d): order %d; elementary abelian: %s; abelian invariants %s" % (
        d["N"] // 3, int(Ks.Size()), bool(Ks.IsElementaryAbelian()), [int(x) for x in Ks.AbelianInvariants()]), flush=True)
    print("    the whole layer K_k (kernel to mod 9): order %d; abelian: %s; abelian invariants %s; exponent %d; nilpotency class %d  [%.0f s]" % (
        int(K.Size()), bool(K.IsAbelian()), [int(x) for x in K.AbelianInvariants()], int(K.Exponent()), int(K.NilpotencyClassOfGroup()), time.time() - t0), flush=True)
