#!/usr/bin/env python3
"""B458 (Ethogram E5) — per-component complex volumes (Vol + i*CS) of the SL(3)
boundary-unipotent components, computed WITHOUT the (broken) database:
exact Groebner solutions fed to SnapPy's own extended-Bloch machinery.

Run: python3 component_cs.py   (fig-8 = m004 and the 5_2 control = m015, both obstruction classes)
"""
import numpy as np
import sympy as sp
import snappy
from snappy.ptolemy.coordinates import PtolemyCoordinates


def exact_solutions(V):
    """all solutions of the ptolemy variety (with normalization rows), exactly."""
    vars_ = [str(v) for v in V.variables]
    R = sp.symbols(vars_)
    gens = dict(zip(vars_, R))
    eqs = [sp.sympify(str(e), locals=gens) for e in V.equations]
    sols = sp.solve(eqs, list(R), dict=True)
    return vars_, sols


def numeric_embeddings(soldict, vars_):
    """all complex embeddings of an exact solution (conjugates via CRootOf/radicals)."""
    # collect the algebraic numbers; use sympy's nfloat on each conjugate by substituting
    # every root expression consistently: easiest robust path = polys are quadratics here,
    # sympy returns explicit radicals; each dict IS one embedding already.
    out = {}
    for k in vars_:
        v = soldict.get(sp.Symbol(k), None)
        if v is None:
            return None
        out[k] = complex(sp.N(v, 30))
    return out


def survey(name):
    print(f"===== {name} =====", flush=True)
    M = snappy.Manifold(name)
    results = []
    for obs in range(2):
        try:
            V = M.ptolemy_variety(3, obstruction_class=obs)
        except Exception as e:
            print(f"  obs={obs}: variety failed: {e}", flush=True)
            continue
        vars_, sols = exact_solutions(V)
        print(f"  obs={obs}: {len(sols)} exact solution branches", flush=True)
        section = V.py_eval_variable_dict()
        full_map = eval(section)  # the documented py_eval section (a lambda source)
        for i, s in enumerate(sols):
            num = numeric_embeddings(s, vars_)
            if num is None:
                print(f"    branch {i}: incomplete solution dict, skipped", flush=True)
                continue
            # minimal polynomial of a distinguishing coordinate for the field label
            key = sp.Symbol(vars_[1]) if len(vars_) > 1 else sp.Symbol(vars_[0])
            try:
                mp_ = sp.minimal_polynomial(s[key], sp.Symbol('t'))
                d = sp.degree(mp_)
                disc = sp.discriminant(mp_, sp.Symbol('t')) if d > 1 else None
            except Exception:
                mp_, d, disc = None, None, None
            if any(abs(v) < 1e-12 for v in num.values()):
                print(f"    branch {i}: zero ptolemy coordinate (invalid branch), skipped", flush=True)
                continue
            try:
                full = full_map(num)
                pc = PtolemyCoordinates(full, is_numerical=True,
                                        py_eval_section=None,
                                        manifold_thunk=(lambda M=M: M))
                cv = pc.complex_volume_numerical()
                cvc = complex(cv)
                vol, cs = cvc.real, cvc.imag
            except Exception as e:
                vol, cs = None, None
                print(f"    branch {i}: complex_volume failed: {type(e).__name__}: {e}", flush=True)
            results.append(dict(obs=obs, branch=i, minpoly=str(mp_), disc=str(disc),
                                vol=vol, cs=cs))
            print(f"    branch {i}: minpoly={mp_} disc={disc}  cvol={vol} + i*{cs}", flush=True)
    return results


if __name__ == '__main__':
    import json
    all_ = {}
    for nm in ['m004', 'm015']:
        all_[nm] = survey(nm)
    json.dump(all_, open('component_cs.json', 'w'), indent=1)
    print("[component_cs.json written]", flush=True)
