"""Dump B1737's population (data-free, main's own code): level, N, M, nI, each fixed character (i,j), the exact slope
s as a complex number, and B1737's Z(0, chi). Run from main's worktree."""
import sys, json, cmath, math, pathlib, importlib.util
WT = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("b1737", WT / "frontier/B1737_the_slope_is_a_zeta_value/verification/the_slope_is_a_zeta_value.py")
B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
SL = B._sl(); out = []
for st, k in B.LEVELS:
    eps = 1 if st[0] == "+" else -1; word = st[1:]
    N, F, S = SL.exact_slopes(eps, word, k); M = B.abel_M(SL, eps, word, k); nI = k if eps < 0 else 0
    zz = cmath.exp(2j * math.pi / N)
    for (i, j, _), s in S.items():
        if (i, j) == (0, 0): continue
        sv = sum(float(c) * zz ** e for e, c in enumerate(s.c))
        z = B.Z0(M, i, j, N)
        out.append({"level": [st, k], "N": N, "M": [[int(x) for x in r] for r in M], "nI": nI, "i": i, "j": j,
                    "s": [sv.real, sv.imag], "Z0": [z.real, z.imag]})
json.dump(out, open(sys.argv[2], "w"))
print(len(out), "characters;", len({(tuple(o['level'])) for o in out}), "levels")
print("max |Im s|:", max(abs(o["s"][1]) for o in out), " max |Im Z0|:", max(abs(o["Z0"][1]) for o in out))
