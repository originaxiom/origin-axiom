"""Independent post-R5 derivative and exact polynomial checks, no finite differences."""
import argparse
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import sympy as sp

from . import vacuum as v
from . import quantum_vacuum as q


def exact_fourth_trace_identity():
    h = sp.symbols("h3:7", real=True)
    j0, g0 = v.fluctuation_matrices()
    j, orbit = sp.MutableSparseMatrix(j0), sp.MutableSparseMatrix(g0)
    _, rep, _, positive, _ = v.representation()
    a = sum((h[i]*rep[i+2] for i in range(4)), sp.zeros(27))
    # Exact Gram, independently checked against the concrete Hermitian matrices.
    compact = v.representation()[4]
    flat = sp.SparseMatrix([list(t) for t in compact])
    gram = flat.conjugate()*flat.T
    assert gram == sp.diag(6*v.CARTAN, 12*sp.eye(72))
    norm = sp.expand(sp.trace(a*a))
    for i in range(78):
        j[166, 108+i] = 2*sp.trace(a*compact[i])
    for i in range(27):
        for offset in [0, 27]:
            j[167+i+offset, i+offset] = a[i, i]
            j[221+i+offset, 54+i+offset] = a[i, i]
    for r, (_, label, _) in enumerate(positive):
        charge = sum(h[i]*label[i+2] for i in range(4))
        p, t = 6+2*r, 7+2*r
        orbit[108+t, p] = -charge
        orbit[108+p, t] = charge
    ks = sp.SparseMatrix(sp.diag(2*sp.eye(108), gram))
    ki = sp.SparseMatrix(sp.diag(sp.eye(108)/2, gram.inv()))
    scalar = 2*ki*j.T*j
    vector = 3*sp.SparseMatrix(gram.inv())*orbit.T*ks*orbit
    result = {}
    for name, mass in [("scalar", scalar), ("vector", vector)]:
        fourth = sp.expand(sum(value*mass[c, r] for (r, c), value in mass.todok().items()))
        c0 = fourth.subs(dict.fromkeys(h, 0))
        line = sp.Poly(fourth.subs(dict.fromkeys(h[1:], 0)), h[0])
        ncoef = sp.Poly(norm.subs(dict.fromkeys(h[1:], 0)), h[0]).coeff_monomial(h[0]**2)
        c2 = line.coeff_monomial(h[0]**2)/ncoef
        c4 = line.coeff_monomial(h[0]**4)/ncoef**2
        remainder = sp.expand(fourth-c0-c2*norm-c4*norm**2)
        result[name] = {"constant": str(c0), "N_coefficient": str(c2),
                        "N_squared_coefficient": str(c4), "remainder": str(remainder),
                        "at_N_5": str(c0+5*c2+25*c4)}
        assert remainder == 0, (name, remainder)
    result["N"] = str(norm)
    result["scope"] = "all four real Cartan coordinates; physical mass trace on N=5"
    return result


def trace_function_derivatives(m, first, second, constant, mu=1):
    """First and second derivative of Tr[x^2(log(x/mu^2)-constant)]."""
    m, first, second = [np.asarray(x, float) for x in [m, first, second]]
    eig, u = np.linalg.eigh((m+m.T)/2)
    tol = 2e-9*max(1, np.max(np.abs(eig)))
    if eig.min() < -tol:
        raise ValueError("not a positive-semidefinite expansion point")
    eig[np.abs(eig) < tol] = 0
    b, c = u.T@first@u, u.T@second@u
    zero = eig == 0
    if np.any(zero) and np.max(np.abs(b[np.ix_(zero, zero)])) > 1e-8:
        raise ValueError("kernel has nonzero linear mass: not a two-sided PSD path")
    fp = np.zeros_like(eig)
    positive = ~zero
    fp[positive] = eig[positive]*(2*np.log(eig[positive]/mu**2)-2*constant+1)
    dd = np.zeros((len(eig), len(eig)))
    for i, x in enumerate(eig):
        for j, y in enumerate(eig):
            if not x and not y:
                continue
            if x and y and abs(x-y) < 1e-8*max(x, y):
                dd[i, j] = 2*np.log((x+y)/(2*mu**2))-2*constant+3
            else:
                dd[i, j] = (fp[i]-fp[j])/(x-y)
    return float(fp@np.diag(b)), float(fp@np.diag(c)+np.sum(dd*b*b))


def mass_derivatives(direction):
    geo = q.geometry()
    d = np.asarray(direction, complex)
    d /= np.sqrt(np.trace(d@d).real)
    assert abs(np.trace(d@geo["y"])) < 1e-12
    _, _, j, orbit = q.matrices(geo["y"])
    def linear_parts(a):
        jd = np.zeros_like(j)
        jd[166, 108:] = 2*np.einsum("aij,ji->a", geo["T"], a).real
        jd[167:221, :54] = q.real_action(a)
        jd[221:275, 54:108] = q.real_action(a)
        tangent = 1j*(geo["T"]@a-a@geo["T"])
        projection = np.einsum("bij,aji->ba", geo["T"], tangent, optimize=True).real
        gd = np.zeros_like(orbit)
        gd[108:, :] = geo["gram_inv"]@projection
        return jd, gd
    j1, g1 = linear_parts(d)
    j2, g2 = linear_parts(-geo["y"]/5)
    scalar = [2*j.T@j, 2*(j1.T@j+j.T@j1),
              2*(j2.T@j+2*j1.T@j1+j.T@j2)]
    ks = geo["ks"]
    vector = [orbit.T@ks@orbit, g1.T@ks@orbit+orbit.T@ks@g1,
              g2.T@ks@orbit+2*g1.T@ks@g1+orbit.T@ks@g2]
    return ([geo["si"]@x@geo["si"] for x in scalar],
            [geo["gi"]@x@geo["gi"] for x in vector])


def analytic_curvatures():
    geo = q.geometry()
    out = {}
    for name, idx in [("color_octet", 2), ("weak_triplet", 5)]:
        matrices = mass_derivatives(geo["T"][idx].copy())
        by_scale = {}
        trace_derivs = []
        for sector in matrices:
            m, first, second = sector
            trace_derivs.append([float(2*np.trace(m@first)),
                                 float(2*np.trace(first@first+m@second))])
        assert np.max(np.abs(trace_derivs)) < 1e-8
        for mu in [.5, 1., 2.]:
            pieces = []
            slopes = []
            for mass, constant, mult in zip(matrices, [1.5, 5/6], [1, 3]):
                slope, curvature = trace_function_derivatives(*mass, constant, mu)
                slopes.append(mult*slope/(64*np.pi**2))
                pieces.append(mult*curvature/(64*np.pi**2))
            assert np.max(np.abs(slopes)) < 1e-9
            by_scale[str(mu)] = pieces
        np.testing.assert_allclose(by_scale["0.5"], by_scale["2.0"], atol=1e-10)
        finite = q.curvature_components(geo["y"], geo["T"][idx].copy(), .0025)[[0, 2]]
        assert np.max(np.abs(finite-by_scale["1.0"])) < 5e-6
        out[name] = {"scalar_vector_curvature_by_mu": by_scale,
                     "finite_difference_eps_point0025": finite.tolist(),
                     "finite_minus_analytic": (finite-by_scale["1.0"]).tolist(),
                     "mass_fourth_trace_first_second_derivatives": trace_derivs,
                     "lambda_point2_g_point5_leading_m2": float(np.dot([.2**2, .5**4], by_scale["1.0"]))}
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x", encoding="utf-8") as output:
        start = time.monotonic()
        data = {"exact_fourth_trace": exact_fourth_trace_identity(),
                "analytic_curvatures": analytic_curvatures(),
                "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "elapsed_seconds": time.monotonic()-start}
        json.dump(data, output, indent=2, allow_nan=False)
        output.write("\n")
    print(json.dumps(data, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
