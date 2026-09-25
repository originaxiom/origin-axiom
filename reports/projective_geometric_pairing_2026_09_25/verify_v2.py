"""F14 implementation-only adapter repair; preserve the original producer."""
from pathlib import Path
from functools import lru_cache
import importlib.util
import sympy as s

spec=importlib.util.spec_from_file_location('f14_original_adapter',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
original_equations=v.intertwiner_equations


def mutable_equations(left,right):
    return s.Matrix(original_equations(left,right))


@lru_cache(None)
def generic_inversion():
    rho=v.f10.generators()
    source=tuple(v.clean(a.inv()) for a in rho)
    target=tuple(a.T for a in source)
    equations=mutable_equations(target,source)
    exact=equations.to_DM().convert_to(s.QQ.frac_field(v.q))
    rows=exact.nullspace(divide_last=True).to_Matrix()
    return tuple(v.clean(rows[i,:].reshape(4,4)) for i in range(rows.rows))


v.intertwiner_equations=mutable_equations
v.generic_inversion=generic_inversion


if __name__=='__main__':
    for name in v.CANDIDATES:
        print('GEOMETRY',v.geometric_certificate(name),flush=True)
    for middle in (14,34):
        for name in v.CANDIDATES:
            print('FIELD',v.candidate_certificate(middle,name),flush=True)
    for matrix in generic_inversion():
        print('GENERIC_THETA',matrix,'determinant',s.factor(matrix.det()),flush=True)
