"""B662 CELL H post-analysis: invariant content of the exact matrices
printed by massey_first.py (parsed directly from cellH_output.txt —
no hand transcription). Exact over K = Q(sqrt-3) via sympy.

Computes: rank + kernel of the v0-mediated class matrix MV0 (banked
basis); rank + radical of the dual cup pairing PL (and the Koszul
re-check PL = -PR^T); the definedness/indeterminacy summary constants.
"""
import re
import sys
from fractions import Fraction as Fr

import sympy as sp

OUT = "cellH_output.txt"
lines = open(OUT).read().splitlines()

r3 = sp.sqrt(3) * sp.I          # r = sqrt(-3)

TOK = re.compile(r"\(([^()]*)\)")


def parse_k(tok):
    """parse '(a+br)' / '(a)' / '(a+-br)' exact."""
    tok = tok.strip()
    if tok.endswith("r"):
        body = tok[:-1]
        # split at the LAST '+' that separates a from b (b may start with -)
        m = re.match(r"^(-?[0-9/]+)\+(-?[0-9/]+)$", body)
        assert m, f"bad token {tok!r}"
        a, b = m.group(1), m.group(2)
    else:
        a, b = tok, "0"
    return sp.Rational(Fr(a)) + sp.Rational(Fr(b)) * r3


def grab_matrix(header, nrows):
    idx = next(i for i, l in enumerate(lines) if header in l)
    rows = []
    for l in lines[idx + 1: idx + 1 + nrows]:
        body = l.split("]  [")[-1] if "]  [" in l else l
        # strip the log prefix '[  357.4s]     [' and trailing ']'
        body = body[body.index("[", body.index("s]")) + 1:]
        body = body.rstrip().rstrip("]")
        toks = TOK.findall(body)
        assert len(toks) == 5, f"row parse fail: {l!r} -> {toks}"
        rows.append([parse_k(t) for t in toks])
    return sp.Matrix(rows)


MV0 = grab_matrix("v0-mediated class matrix", 5)
PL = grab_matrix("PL[t][s]", 5)
PR = grab_matrix("PR[s][t]", 5)

print("MV0 =")
sp.pprint(MV0)
assert sp.simplify(MV0 + MV0.T) == sp.zeros(5), "MV0 not antisymmetric?!"
print("MV0 antisymmetric: True (re-checked)")
rk = MV0.rank()
print(f"rank(MV0) = {rk}")
ker = MV0.nullspace()
print(f"kernel dim = {len(ker)}")
for v in ker:
    vv = sp.simplify(v.T)
    print(f"  kernel vector (right): {list(vv)}")

print()
assert sp.simplify(PL + PR.T) == sp.zeros(5), "PL != -PR^T ?!"
print("Koszul PL = -PR^T: True (re-checked)")
print(f"rank(PL) [the dual cup pairing H^1(27bar) x H^1(27) -> H^2(C)] "
      f"= {PL.rank()}")
lker = PL.T.nullspace()
rker = PL.nullspace()
print(f"left radical (zbar classes cupping to 0 with ALL u): dim "
      f"{len(lker)}: {[list(sp.simplify(v.T)) for v in lker]}")
print(f"right radical (u classes cupping to 0 with ALL zbar): dim "
      f"{len(rker)}: {[list(sp.simplify(v.T)) for v in rker]}")

# indeterminacy fullness: which (i,k) have indeterminacy = K?
full = [[(any(PL[t, k] != 0 for t in range(5))
          or any(PR[i, t] != 0 for t in range(5)))
         for k in range(5)] for i in range(5)]
print("\nindeterminacy of <u_i, ., u_k> is FULL (= H^2(D;C)) for (i,k):")
for i in range(5):
    print("  " + " ".join("FULL" if full[i][k] else "ZERO"
                          for k in range(5)))
print("\nPOST-ANALYSIS DONE")
