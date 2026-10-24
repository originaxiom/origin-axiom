# Post hoc (2026-10-24, after main's B1750 note): W145's census frame against its T-law image and its
# mirror image, on this seat's own code. Not a sealed run. Run from the repository root.
import sys, io, contextlib
from fractions import Fraction as Fr
sys.path.insert(0, "docs/dossiers/the_weave_2026-10-07")
with contextlib.redirect_stdout(io.StringIO()):
    import the_third_opinion_b1741 as W
T8 = W.T8
root = T8.repo_root()
files = {p: T8.git_bytes(root, W.REV, p) for p in W.FILES}
W93, W89 = T8.own_modules(root)
col = T8.L_column(files)
y = 2.993325909
pts = {"frame (2/5,1/10) at 0.4": ((Fr(2,5), Fr(1,10)), 0.4),
       "T-law image: line 153 (2/5,9/10) at 3.4": ((Fr(2,5), Fr(9,10)), 3.4),
       "mirror image: line 150 (2/5,3/10) at 3.6": ((Fr(2,5), Fr(3,10)), 3.6)}
own = {k: T8.own_point(W93, W89, col, l, x, y)[0] for k, (l, x) in pts.items()}
f = own["frame (2/5,1/10) at 0.4"]
for k in list(pts)[1:]:
    print(k, T8.compare_point(f, own[k]))
