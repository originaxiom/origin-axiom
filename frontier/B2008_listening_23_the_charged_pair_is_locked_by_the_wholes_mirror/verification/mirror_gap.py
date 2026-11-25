"""B2008, P3 (GAP through sage: ~/.local/bin/sage -python -B mirror_gap.py > mirror_gap_run.txt): is P_tau in G_k = <C, sigma>
at mod 27, 81, 243; the order and abelian invariants of <G_k, P_tau>."""
import json, pathlib
from sage.all import libgap
HERE = pathlib.Path(__file__).resolve().parent
data = json.loads((HERE / "mirror_perms.json").read_text())
for lab in ("mod 27", "mod 81", "mod 243"):
    d = data[lab]; P = lambda l: libgap.PermList([i + 1 for i in l])
    C, S, T = P(d["C"]), P(d["S"]), P(d["T"])
    G = libgap.Group([C, S]); H = libgap.Group([C, S, T])
    print("P3 (%s): tau in G_k: %s; |G_k| = %d; |<G_k, tau>| = %d (= 2 |G_k|: %s); abelian invariants of <G_k, tau>: %s" % (
        lab, bool(libgap.IsSubset(G, libgap.Group([T]))), int(G.Size()), int(H.Size()), int(H.Size()) == 2 * int(G.Size()), [int(v) for v in H.AbelianInvariants()]), flush=True)
