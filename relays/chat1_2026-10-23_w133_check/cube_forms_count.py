#!/usr/bin/env python3
"""chat1's count for relay 223's ask to the web seat (a VERIFICATION-type count; no data): which weights carry modular
forms in the cube group's 1', rho' and rho' (x) sgn, with rho' = rho_T (x) chi_eta^21 (W135's k = 21: image the cube's
rotation group, order 24, real, det 1).
The reductions (each checked below):
  - sgn, the sign character of the cube group pulled back to SL(2, Z), is chi_eta^12 (T -> -1, S -> -1).
  - So 1' = chi_eta^12, and rho' (x) sgn = rho_T (x) chi_eta^33 = rho_T (x) chi_eta^9.
  - A holomorphic form of weight w with multiplier rho_T (x) chi_eta^k is F = eta^k G, with G of multiplier rho_T and
    weight w - k/2, and F's line exponents >= 0, i.e. each G line's exponents >= the least exponent >= -k/24 in that
    line's class mod 1.  G = A R + B DR + C D^2R as in w133_check.py (the Wronskian makes this complete).
  - A scalar form of weight w with character chi_eta^12 is eta^12 times a level-one form of weight w - 6.
Checks: rho'(T), rho'(S) real with det 1 and generating a group of order 24 (the cube's rotations); the sign character
on T and S; each vector count at two values of the pole truncation M.
    python3 -B cube_forms_count.py      # writes cube_forms_count.json and cube_forms_count_run.txt"""
import contextlib, importlib.util, io, json, pathlib
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent
_src = (HERE / "w133_check.py").read_text()
_cut = _src.index('OUT["C4"] = {}')
NS = {"__file__": str(HERE / "w133_check.py"), "__name__": "w133_defs"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src[:_cut], "w133_check.py", "exec"), NS)          # w133_check's definitions (series, R, DR, D2R, wh_basis)
R, DR, D2R, wh_basis = NS["R"], NS["DR"], NS["D2R"], NS["wh_basis"]
LOG, OUT = [], {}


def say(s):
    LOG.append(s); print(s, flush=True)


# the group checks
z8 = sp.exp(sp.I * sp.pi / 4)
Pm = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]); Li = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
chiT = lambda m: sp.exp(2 * sp.pi * sp.I * m / 24); chiS = lambda m: sp.exp(-sp.I * sp.pi * m / 4)
rT = sp.simplify(z8 * Li * chiT(21)); rS = sp.simplify(z8 * Pm * chiS(21))
real = all(sp.simplify(sp.im(x)) == 0 for x in list(rT) + list(rS))
grp, frontier = {sp.ImmutableMatrix(sp.eye(3))}, [sp.eye(3)]
while frontier:
    nxt = []
    for g in frontier:
        for h in (rT, rS):
            k = sp.ImmutableMatrix(sp.simplify(g * h))
            if k not in grp:
                grp.add(k); nxt.append(k)
    frontier = nxt
OUT["group"] = {"rho'(T)": str(rT), "rho'(S)": str(rS), "real": bool(real), "det": [str(sp.simplify(rT.det())), str(sp.simplify(rS.det()))],
                "order of the image": len(grp), "sign character = chi_eta^12 on T and S": [str(sp.simplify(chiT(12))), str(sp.simplify(chiS(12)))]}
say(f"group: {OUT['group']}")


def dim_vector(k, w, mmax):
    """holomorphic forms of weight w and multiplier rho_T (x) chi_eta^k"""
    kG = Fr(w) - Fr(k, 2)
    bounds = {}
    for l, e in (("i", Fr(1, 8)), ("+", Fr(7, 8)), ("-", Fr(3, 8))):
        lo = -Fr(k, 24)                                          # least exponent >= -k/24 in e + Z
        x = e + ((lo - e) // 1) * 1
        while x < lo:
            x += 1
        bounds[l] = int(8 * x)
    cols = []
    for gen, kk in ((R, kG + Fr(1, 2)), (DR, kG - Fr(3, 2)), (D2R, kG - Fr(7, 2))):
        if kk != int(kk):
            return None, bounds                                   # no level-one form of non-integral weight
        for name, f in wh_basis(int(kk), mmax):
            cols.append({l: f * gen[l] for l in "i+-"})
    if not cols:
        return 0, bounds
    rows = []
    for l in "i+-":
        lo = min(c[l].v for c in cols)
        for kx in range(lo, bounds[l]):
            rows.append([c[l].co(kx) for c in cols])
    if not rows:
        return len(cols), bounds
    return len(sp.Matrix(rows).nullspace()), bounds


def dim_scalar_level1(w):
    if w < 0 or w % 2:
        return 0
    return (w // 12 + (0 if w % 12 == 2 else 1))


OUT["counts"] = {}
say("weight w: dim M_w(rho'), dim M_w(rho' (x) sgn), dim M_w(1')   [rho' at two pole truncations M]")
for w in range(0, 25):
    a1, b1 = dim_vector(21, w, 4); a2, _ = dim_vector(21, w, 6)
    s1, c1 = dim_vector(9, w, 4); s2, _ = dim_vector(9, w, 6)
    one = dim_scalar_level1(w - 6)
    OUT["counts"][w] = {"rho'": [a1, a2], "rho' x sgn": [s1, s2], "1'": one, "G bounds rho'": b1, "G bounds rho' x sgn": c1}
    say(f"w = {w:2d}: rho' {a1} ({a2}); rho' x sgn {s1} ({s2}); 1' {one}")
(HERE / "cube_forms_count.json").write_text(json.dumps(OUT, indent=1, default=str) + "\n")
(HERE / "cube_forms_count_run.txt").write_text("\n".join(LOG) + "\n")
