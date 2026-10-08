"""W34, POST HOC (after the one run of the_observer_layer_on_the_weave.py; not part of the rule's cells).

The run left 11 of the 758 states undecided in Q1, each only in the block Sym^6: one singular value of one rank fell
between 1e-40 and 1e-25 relative at 60 digits. This check recomputes exactly those 11, and the control m004, from
SnapPy's polished holonomy at 400 bits (about 120 digits; the PSL(2, C) holonomy, whose sign the even blocks do not
see), at mpmath's 120 digits, with the thresholds stated here before it ran: zero below 1e-90 relative, non-zero above
1e-50, anything between undecided. The code is the run's own (thread_block, rank_mp, kernel_mp), fed the polished
matrices.

Run: python3 the_observer_layer_posthoc.py  ->  the_observer_layer_posthoc.json beside it.
"""
import json
import sys
import time
import warnings
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_observer_layer_on_the_weave as OL  # noqa: E402

warnings.filterwarnings("ignore")
OUT = HERE / "the_observer_layer_posthoc.json"
BITS = 400


class Polished:
    """the polished group, with the interface thread_block reads (generators, relators, peripheral curves, SL2C)"""

    def __init__(self, G):
        self.G = G

    def generators(self):
        return self.G.generators()

    def relators(self):
        return self.G.relators()

    def peripheral_curves(self):
        return self.G.peripheral_curves()

    def SL2C(self, w):
        return self.G(w)


def main():
    import snappy
    OL.mp.mp.dps = 120
    OL.TOL_ZERO, OL.TOL_NONZERO = OL.mp.mpf(10) ** -90, OL.mp.mpf(10) ** -50
    run = json.loads((HERE / "the_observer_layer_on_the_weave.json").read_text(encoding="utf-8"))
    undecided = [tuple(x) for x in run["Q1 the private states on every thread (B761's quantity)"][
        "undecided (a rank between 1e-40 and 1e-25 relative)"]]
    rows = []
    t0 = time.time()
    for w, s in [("LR", "+")] + undecided:
        name = ("b++" if s == "+" else "b+-") + w
        M = snappy.Manifold(name)
        G = Polished(M.polished_holonomy(bits_prec=BITS, lift_to_SL2=False))
        blocks = [OL.thread_block(G, k) for k in OL.KS]
        nz = [x for b in blocks for x in b["nz"] if x is not None]
        zz = [x for b in blocks for x in b["z"] if x is not None]
        rows.append({"state": s + w, "blocks (H1, rank, private) or undecided": [
            "undecided" if b["undecided"] else (b["H1"], b["res"], b["private"]) for b in blocks],
            "smallest non-zero ratio": OL.short(min(nz)) if nz else None,
            "largest zero ratio": OL.short(max(zz)) if zz else None})
    res = {
        "status": "POST HOC: after W34's one run; the 11 states its rank rule left undecided, and the control m004",
        "precision": {"holonomy bits": BITS, "mpmath dps": OL.mp.mp.dps, "zero below": "1e-90",
                      "non-zero above": "1e-50"},
        "rows": rows,
        "the control m004 (1, 1, 0) in each block": rows[0]["blocks (H1, rank, private) or undecided"] == [(1, 1, 0)] * 3,
        "every undecided state now (1, 1, 0) in every block": all(
            r["blocks (H1, rank, private) or undecided"] == [(1, 1, 0)] * 3 for r in rows[1:]),
        "seconds": round(time.time() - t0, 1),
    }
    OUT.write_text(json.dumps(res, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
