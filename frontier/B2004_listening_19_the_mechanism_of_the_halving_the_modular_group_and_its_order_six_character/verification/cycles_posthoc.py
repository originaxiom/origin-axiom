"""B2004, POST HOC (labelled; written after localize_posthoc_run.txt): do the words outside the commutator subgroup that fix
points act on the orbit with C's cycle type (three fixed points, the rest in 3-cycles), and is their rho of order 3 (omega^+-1),
as it must be if they are conjugate to C^+-1 in the finite image group and rho factors through that group?
    python3 -B cycles_posthoc.py > cycles_posthoc_run.txt"""
import contextlib, io, pathlib
from collections import Counter
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
head = (HERE / "mechanism.py").read_text().split("WORDS = words(10)")[0]
ns = {"__file__": str(HERE / "mechanism.py")}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(head, "mech_head", "exec"), ns)
WORDS = ns["words"](10)
def cycle_type(p):
    n = len(p); seen = np.zeros(n, bool); ct = Counter()
    for i in range(n):
        if seen[i]: continue
        j, l = i, 0
        while not seen[j]: seen[j] = True; j = p[j]; l += 1
        ct[l] += 1
    return tuple(sorted(ct.items()))
for N, start, lab in ((27, (3, 3, 3), "mod 27"), (81, (3, 3, 3), "mod 81"), (243, (3, 3, 3), "mod 243"), (9, (3, 3, 3), "mod 9"), (25, (3, 3, 3), "mod 25"), (5, None, "mod 5 leaf"), (7, None, "mod 7 leaf")):
    pts, idx, pC, pS, moves = ns["orbit"](N, start); n = len(pts)
    perm = {"s": pS, "c": pC, "C": pC[pC]}; ctC = cycle_type(pC)
    types = Counter(); rhos = Counter()
    for w in WORDS:
        e = ns["rho_exp"](w)
        if e == 0: continue
        p = np.arange(n)
        for a in reversed(w): p = perm[a][p]
        if np.any(p == np.arange(n)):
            ct = cycle_type(p); same = ct == ctC; types[same] += 1; rhos[(same, e)] += 1
    print("%s: C's cycle type %s; words outside the commutator subgroup with fixed points: with C's cycle type %d, other %d; their rho exponents (in Z/6; omega^+-1 = 2, 4) by (C's type?, exponent): %s" % (
        lab, ctC, types[True], types[False], dict(sorted(rhos.items()))))
