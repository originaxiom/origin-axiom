"""B645 — C3: the dial law via normalization-free invariants.

Y[ijk] scales as c_i c_j c_k under rep rescaling; only exponent vectors
n with sum_{slots containing i} n_slot = 0 for every i are basis-free.
Parse the nine banked Y tables (B637 stage 3 + part 2b), compute the
invariant lattice per double, evaluate exactly over Q(sqrt(-3)), and
compare across the dial. Also re-verify the core law 24 zeta6 on all
nine from the parsed tables (an independent transcription lock)."""
import itertools as it
import os
import re
from fractions import Fraction as Fr

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "B637_corrected_cell3")
r = sp.sqrt(-3)

VAL = re.compile(r"Y\[\((\d), (\d), (\d)\)\] = (.+)$")


def parse_val(s):
    s = s.strip()
    if s == "0":
        return sp.Integer(0)
    m = re.match(r"\((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r\)", s)
    a, b = sp.Rational(m.group(1)), sp.Rational(m.group(2))
    return a + b * r


def parse_tables(path, headers):
    txt = open(path).read().splitlines()
    tabs = {}
    cur = None
    for ln in txt:
        for h, name in headers:
            if h in ln:
                cur = name
                tabs[cur] = {}
        m = VAL.search(ln)
        if m and cur is not None:
            tabs[cur][(int(m.group(1)), int(m.group(2)),
                       int(m.group(3)))] = parse_val(m.group(4))
    return tabs

T = {}
T.update(parse_tables(
    os.path.join(B637, "stage3_output.txt"),
    [("phi(a)=a:", "Dphi_a"), ("phi(a)=A:", "Dphi_Ainv"),
     ("phi(a)=b:", "Dphi_b"), ("phi(a)=B:", "Dphi_Binv"),
     ("unbent weld table", "weld_none")]))
T.update(parse_tables(
    os.path.join(B637, "part2b_stage2_fixed_output.txt"),
    [("D_bent(M; m=1):", "bent_m1"), ("D_bent(M; m=5):", "bent_m5"),
     ("D_bent(M; m=7):", "bent_m7"), ("D_bent(M; m=11):", "bent_m11")]))

print(f"parsed doubles: {sorted(T)} (expect 9)", flush=True)
for k, tab in T.items():
    assert len(tab) == 10, (k, len(tab))

print("\n== lock: the core law on all nine (from parsed tables) ==")
z6 = (1 + r) / 2
for k in sorted(T):
    lhs = T[k][(0, 2, 3)]
    rhs = 24 * z6 * T[k][(1, 2, 3)]
    print(f"  {k}: Y[023] = 24 z6 Y[123]: {sp.simplify(lhs - rhs) == 0}")

print("\n== the normalization-free invariant lattice per double ==")
for k in sorted(T):
    nz = [s for s in sorted(T[k]) if T[k][s] != 0]
    # incidence: rows = rep indices 0..4, cols = nonzero slots
    M = sp.Matrix([[1 if i in s else 0 for s in nz] for i in range(5)])
    null = M.nullspace()
    print(f"  {k}: nonzero {len(nz)}; invariant rank {len(null)}")
    for v in null:
        v = (v * sp.lcm([sp.denom(x) for x in v])).applyfunc(sp.nsimplify)
        num, den, desc_n, desc_d = sp.Integer(1), sp.Integer(1), [], []
        for s, e in zip(nz, list(v)):
            e = int(e)
            if e > 0:
                num *= T[k][s] ** e
                desc_n.append(f"Y{list(s)}^{e}" if e > 1 else f"Y{list(s)}")
            elif e < 0:
                den *= T[k][s] ** (-e)
                desc_d.append(f"Y{list(s)}^{-e}" if e < -1
                              else f"Y{list(s)}")
        val = sp.simplify(num / den)
        a, b = val.as_real_imag()
        print(f"    ({' '.join(desc_n)})/({' '.join(desc_d)}) = "
              f"{sp.nsimplify(val)}")
