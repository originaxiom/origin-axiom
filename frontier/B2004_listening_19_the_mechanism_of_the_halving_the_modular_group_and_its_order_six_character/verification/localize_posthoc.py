"""B2004, POST HOC (labelled; written after mechanism_run.txt showed K2 failing as worded: on the 3-tower words outside the
commutator subgroup that are not conjugates of C also fix points, three each). The sharper question: are ALL the fixed points
of words outside the commutator subgroup (length <= 10) among the three points that C fixes? At each level: the set of such
fixed points, and whether it lies inside C's fixed set.
    python3 -B localize_posthoc.py > localize_posthoc_run.txt"""
import pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "mechanism.py").read_text()
head = src.split("WORDS = words(10)")[0]
import contextlib, io
ns = {"__file__": str(HERE / "mechanism.py")}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(head, "mech_head", "exec"), ns)
WORDS = ns["words"](10)
for N, start, lab in ((27, (3, 3, 3), "mod 27"), (81, (3, 3, 3), "mod 81"), (243, (3, 3, 3), "mod 243"), (9, (3, 3, 3), "mod 9"), (25, (3, 3, 3), "mod 25"), (5, None, "mod 5 leaf"), (7, None, "mod 7 leaf")):
    pts, idx, pC, pS, moves = ns["orbit"](N, start); n = len(pts)
    F = set(np.nonzero(pC == np.arange(n))[0].tolist())
    perm = {"s": pS, "c": pC, "C": pC[pC]}; fixedset = set(); nwords = 0
    for w in WORDS:
        if ns["rho_exp"](w) == 0: continue
        p = np.arange(n)
        for a in reversed(w): p = perm[a][p]
        fx = np.nonzero(p == np.arange(n))[0]
        if len(fx): nwords += 1; fixedset.update(fx.tolist())
    print("%s (%d points): C fixes %s; %d words outside the commutator subgroup fix points; the points they fix: %d, all among C's fixed points: %s" % (
        lab, n, sorted(pts[i] for i in F), nwords, len(fixedset), fixedset <= F))
