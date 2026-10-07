#!/usr/bin/env python3
"""B1496 -- main's own checks of the arithmetic the research used: (1) the shape identity ch_3(Lambda^2 V) = (n - 4) ch_3(V)
for an SU(n) bundle (Chern roots x_i with sum zero), ranks 2..8; (2) the order-3 rotation of the hexagonal lattice has
|det(omega - 1)| = 3 fixed points (F-CI's three; B1291); (3) the orbifold Euler number of T^6/Z_3 is 72.  Writes checks.json."""
import json, pathlib, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
out = {}
for n in range(2, 9):
    x = sp.symbols(f"x1:{n+1}"); rel = {x[-1]: -sum(x[:-1])}
    ch3 = sum(xi**3 for xi in x) / 6
    ch3L2 = sum((x[i] + x[j])**3 for i in range(n) for j in range(i + 1, n)) / 6
    out[f"rank {n}: ch3(L2V) - (n-4) ch3(V)"] = str(sp.expand((ch3L2 - (n - 4) * ch3).subs(rel)))
omega = sp.Matrix([[0, -1], [1, -1]]); out["omega^3 = I"] = (omega**3 == sp.eye(2)); out["|det(omega - I)|"] = abs(int((omega - sp.eye(2)).det()))
out["chi_orb(T^6/Z3) = (1/3)(chi(T^6) + 8*27)"] = sp.Rational(1, 3) * (0 + 8 * 27); out["2*(36 - 0)"] = 72
json.dump({k: (str(v) if not isinstance(v, (bool, int)) else v) for k, v in out.items()}, open(HERE / "checks.json", "w"), indent=1); print(json.dumps({k: str(v) for k, v in out.items()}, indent=1))
