"""R14 explicit sourced hyperbolic cusp-end Higgs field, not a global m202 solution.

Prescribed constant line densities; see SINGULAR_CUSP_DESIGN.md.
No files are written. theta_1 is evaluated by its DLMF 20.2.1 series.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass

import mpmath as mp
import numpy as np
import sympy as sp

TAU = .5+.5j*math.sqrt(3)


def theta_series(w, tau=TAU, terms=12):
    w = np.asarray(w, dtype=complex)
    value = np.zeros_like(w)
    first = np.zeros_like(w)
    second = np.zeros_like(w)
    for n in range(terms):
        freq = (2*n+1)*math.pi
        coefficient = 2*(-1)**n*np.exp(1j*math.pi*tau*(n+.5)**2)
        value += coefficient*np.sin(freq*w)
        first += coefficient*freq*np.cos(freq*w)
        second -= coefficient*freq*freq*np.sin(freq*w)
    return value, first, second


def green(w, tau=TAU, terms=12):
    """Potential, Euclidean gradient and Hessian on the flat torus."""
    if tau.imag <= 0:
        raise ValueError("upper-half-plane torus parameter required")
    w = np.asarray(w, dtype=complex)
    theta, first, second = theta_series(w, tau, terms)
    if np.any(abs(theta) < 1e-14):
        raise ValueError("point lies on an excluded source")
    ratio = first/theta
    curvature = second/theta-ratio*ratio
    value = np.log(abs(theta))-math.pi*w.imag*w.imag/tau.imag
    grad = np.stack([ratio.real, -ratio.imag-2*math.pi*w.imag/tau.imag], axis=-1)
    hessian = np.stack([curvature.real, -curvature.imag,
                        -curvature.imag, -curvature.real-2*math.pi/tau.imag], axis=-1)
    return value, grad, hessian.reshape(w.shape+(2, 2))


@dataclass
class CuspField:
    beta: tuple = (1., 1., 1.)
    tau: complex = TAU
    c: float = 0.
    z0: float = 1.

    @property
    def points(self):
        return np.array([0, (1+self.tau)/3, 2*(1+self.tau)/3])

    @property
    def total(self):
        return sum(self.beta)

    def radial(self, z):
        z = np.asarray(z, dtype=float)
        coefficient = math.pi*self.total/self.tau.imag
        return (coefficient*z*z*np.log(z/self.z0)+self.c*z*z,
                coefficient*z*(2*np.log(z/self.z0)+1)+2*self.c*z,
                coefficient*(2*np.log(z/self.z0)+3)+2*self.c)

    def evaluate(self, w, z):
        w = np.asarray(w, dtype=complex)
        z = np.broadcast_to(np.asarray(z, dtype=float), w.shape)
        value, dz, dzz = self.radial(z)
        grad = np.zeros(w.shape+(3,))
        grad[..., 2] = dz
        hessian = np.zeros(w.shape+(3, 3))
        hessian[..., 2, 2] = dzz
        for beta, point in zip(self.beta, self.points):
            g, dg, ddg = green(w-point, self.tau)
            value += beta*g
            grad[..., :2] += beta*dg
            hessian[..., :2, :2] += beta*ddg
        return value, grad, hessian


def symbolic_checks():
    z, z0, density, c = sp.symbols("z z0 density c", positive=True)
    radial = sp.pi*density*z*z*sp.log(z/z0)+c*z*z
    residual = sp.simplify(sp.diff(radial, z, 2)-sp.diff(radial, z)/z-2*sp.pi*density)
    r = sp.symbols("r", positive=True)
    line = sp.log(sp.tanh(r))
    line_residual = sp.simplify(sp.diff(line, r, 2)+(sp.coth(r)+sp.tanh(r))*sp.diff(line, r))
    return {"zero_mode_ode_residual": str(residual), "local_geodesic_residual": str(line_residual),
            "missing_zero_mode_off_source_residual": str(-2*sp.pi*density*z*z),
            "radial_flux_density": str(sp.simplify(sp.diff(radial, z)/z)),
            "flux_log_derivative": str(sp.simplify(z*sp.diff(sp.diff(radial, z)/z, z)))}


def torus_controls():
    points = np.array([.137+.193j, .311+.219j, -.173+.291j])
    g, dg, _ = green(points)
    periodic = []
    for shift in (1, TAU, 1+TAU):
        shifted, shifted_grad, _ = green(points+shift)
        periodic.append({"shift": str(shift), "value_error": float(np.max(abs(shifted-g))),
                         "gradient_error": float(np.max(abs(shifted_grad-dg)))})
    value12 = theta_series(points, terms=12)[0]
    value18 = theta_series(points, terms=18)[0]
    with mp.workdps(50):
        nome = mp.exp(mp.j*mp.pi*mp.mpc(TAU.real, TAU.imag))
        reference = np.array([complex(mp.jtheta(1, mp.pi*mp.mpc(p.real, p.imag), nome)) for p in points])
    return {"periodicity": periodic, "cutoff_error": float(np.max(abs(value12-value18))),
            "mpmath_error": float(np.max(abs(value18-reference)))}


def fixed_point_controls():
    r = sp.Matrix([[0, -1], [1, 1]])
    rotation = r*r
    points = [sp.Matrix([sp.Rational(i, 3), sp.Rational(j, 3)]) for i in range(3) for j in range(3)]
    fixed = [p for p in points if all(v.q == 1 for v in (rotation-sp.eye(2))*p)]
    action = [next(i for i, q in enumerate(fixed) if all(v.q == 1 for v in r*p-q)) for p in fixed]
    test_points = np.array([.137+.193j, .311+.219j, -.173+.291j])
    symmetry = []
    for beta in ((1., 1., 1.), (2., 1., 1.), (1., 2., 1.)):
        field = CuspField(beta)
        values = field.evaluate(test_points, 1.2)[0]
        moved = field.evaluate(TAU*test_points, 1.2)[0]
        symmetry.append({"beta": beta, "potential_rotation_error": float(np.max(abs(values-moved)))})
    return {"order3_matrix": [list(map(int, row)) for row in rotation.tolist()],
            "fixed_points": [[str(x) for x in p] for p in fixed],
            "order6_permutation": action, "symmetry": symmetry}


def pde_controls():
    rows = []
    for beta in ((1., 1., 1.), (-1., -1., -1.), (-2., 1., 1.)):
        field = CuspField(beta)
        for point in (np.array([.137, .193, 1.]), np.array([.311, .219, 1.7]), np.array([-.173, .291, 2.4])):
            w, z = complex(point[0], point[1]), point[2]
            value, gradient, hessian = field.evaluate(w, z)
            analytic = z*z*(np.trace(hessian)-gradient[2]/z)
            finite = []
            for step in (3e-4, 1e-4):
                def f(p):
                    return float(field.evaluate(complex(p[0], p[1]), p[2])[0])
                lap = sum(f(point+axis)-2*float(value)+f(point-axis) for axis in step*np.eye(3))/step**2
                dz = (f(point+np.array([0, 0, step]))-f(point-np.array([0, 0, step])))/(2*step)
                finite.append({"step": step, "residual": float(z*z*(lap-dz/z))})
            rows.append({"beta": beta, "point": point.tolist(), "analytic": float(analytic), "finite": finite})
    return rows


def flux_controls(beta=(1., 1., 1.), radius=.01, lower=1., upper=3., c=0.):
    field = CuspField(beta, c=c)
    angles = 2*math.pi*np.arange(2048)/2048
    directions = np.column_stack([np.cos(angles), np.sin(angles)])
    tubes = []
    for point, charge in zip(field.points, beta):
        w = point+radius*np.exp(1j*angles)
        _, gradient, _ = field.evaluate(w, 1.)
        # Integral along the excised-domain OUTWARD normal: -z partial_R.
        integral = -2*math.pi*radius*np.mean(np.sum(gradient[:, :2]*directions, axis=1))*math.log(upper/lower)
        expected = -(2*math.pi*charge-2*math.pi*field.total/field.tau.imag*math.pi*radius**2)*math.log(upper/lower)
        tubes.append({"beta": charge, "flux": float(integral), "expected": expected,
                      "normal_component_at_z1_max": float(np.max(-np.sum(gradient[:, :2]*directions, axis=1)))})
    area = field.tau.imag-3*math.pi*radius*radius
    upper_flux = area*field.radial(upper)[1]/upper
    lower_flux = -area*field.radial(lower)[1]/lower
    return {"beta": beta, "radius": radius, "c": c, "lower": lower, "upper": upper,
            "tubes": tubes, "upper_flux": float(upper_flux), "lower_flux": float(lower_flux),
            "total_flux": float(upper_flux+lower_flux+sum(t["flux"] for t in tubes)),
            "without_tubes": float(upper_flux+lower_flux)}


def run():
    radial = []
    for c in (-20., 0., 20.):
        field = CuspField(c=c)
        radial.append({"c": c, "normal_at_z1": float(field.radial(1.)[1]),
                       "normal_at_z10": float(10*field.radial(10.)[1])})
    return {"scope": "Explicit cusp-end solution, NOT global m202 matching or a chiral spectrum",
            "symbolic": symbolic_checks(), "torus": torus_controls(),
            "fixed": fixed_point_controls(), "pde": pde_controls(),
            "flux": [flux_controls(b) for b in ((1., 1., 1.), (-1., -1., -1.), (-2., 1., 1.))],
            "free_radial_flux_data": radial}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
