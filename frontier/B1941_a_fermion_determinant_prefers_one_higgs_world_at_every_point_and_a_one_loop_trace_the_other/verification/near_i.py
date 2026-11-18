"""B1941, the reversal near tau = i (Review 83's R83-17; the figure stood on the page with no committed output, which a
reader of Review 84 found): Delta at tau = 1.05 i and at 1.5 i, with the exact weight, for both colour weightings.
Data-free.  Uses s4_pointwise.py's own functions."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import s4_pointwise as S
if __name__ == "__main__":
    for x, y in ((0.0, 1.05), (0.0, 1.5)):
        d = S.deltas(S.dets(x, y, True))
        print("tau = %.2f i: %s" % (y, "; ".join("%s: %+.3f" % (k, float(v)) for k, v in sorted(d.items()) if k.startswith("ln det"))))
