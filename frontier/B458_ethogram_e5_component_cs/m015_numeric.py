#!/usr/bin/env python3
"""m015 control via multi-start Newton (fields already exact from B444; the complex
volumes are the new data). Solutions polished to 1e-13, deduped, fed to PtolemyCoordinates."""
import numpy as np
import snappy
from snappy.ptolemy.coordinates import PtolemyCoordinates

rng = np.random.default_rng(7)

def solve_all(V, tries=4000):
    vars_ = [str(v) for v in V.variables]
    n = len(vars_)
    import sympy as sp
    R = sp.symbols(vars_)
    gens = dict(zip(vars_, R))
    eqs = [sp.sympify(str(e), locals=gens) for e in V.equations]
    F = sp.lambdify(R, eqs, 'numpy')
    J = sp.lambdify(R, sp.Matrix(eqs).jacobian(R), 'numpy')
    sols = []
    for _ in range(tries):
        x = rng.normal(0, 1.2, n) + 1j * rng.normal(0, 1.2, n)
        for _ in range(60):
            f = np.array(F(*x), dtype=complex)
            if np.linalg.norm(f) < 1e-13:
                break
            try:
                dx = np.linalg.lstsq(np.array(J(*x), dtype=complex), -f, rcond=None)[0]
            except Exception:
                break
            x = x + dx
        else:
            continue
        if np.linalg.norm(np.array(F(*x), dtype=complex)) < 1e-12 and np.min(np.abs(x)) > 1e-8:
            if not any(np.allclose(x, s, atol=1e-8) for s in sols):
                sols.append(x.copy())
    return vars_, sols

M = snappy.Manifold('m015')
for obs in range(2):
    V = M.ptolemy_variety(3, obstruction_class=obs)
    vars_, sols = solve_all(V)
    print(f"m015 obs={obs}: {len(sols)} numerical solutions", flush=True)
    section = V.py_eval_variable_dict()
    full_map = eval(section)
    for i, x in enumerate(sols):
        num = dict(zip(vars_, [complex(v) for v in x]))
        try:
            full = full_map(num)
            pc = PtolemyCoordinates(full, is_numerical=True, py_eval_section=None,
                                    manifold_thunk=(lambda M=M: M))
            cv = complex(pc.complex_volume_numerical())
            print(f"   sol {i}: c1={num[vars_[1]]:.6f}  cvol = {cv.real:.9f} + i*{cv.imag:.9f}", flush=True)
        except Exception as e:
            print(f"   sol {i}: cv failed {type(e).__name__}: {e}", flush=True)
