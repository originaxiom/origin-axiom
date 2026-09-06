"""R13, see HARMONIC_CUSP_DESIGN.md. No file writes or old-module execution.

The height-ascent, Riley model and Bessel expansion adapt the READ
primitives of B1007_arb_maass/_reference_double.py. Crucial extension:
track the meridional cocycle for a harmonic primitive, not an automorphic
scalar cusp eigenfunction. This is a conditional numerical model.
"""
from __future__ import annotations

import collections
import itertools
import json
import math
import time
from dataclasses import dataclass

import numpy as np
import sympy as sp
from scipy import integrate, special

LENGTH = 2 * math.sqrt(3)
A = np.array([[1, 1], [0, 1]], dtype=complex)
B = np.array([[1, 0], [0.5 - 0.5j * math.sqrt(3), 1]], dtype=complex)
GENERATORS = {"a": A, "b": B, "A": np.linalg.inv(A), "B": np.linalg.inv(B)}


def inverse_word(word):
    return word[::-1].swapcase()


def period(word):
    return sum(1 if letter.islower() else -1 for letter in word)


def word_matrix(word):
    out = np.eye(2, dtype=complex)
    for letter in word:
        out = out @ GENERATORS[letter]
    return out


def reduced_words(max_length):
    frontier = [""]
    for _ in range(max_length):
        frontier = [w + a for w in frontier for a in "abAB"
                    if not w or a != w[-1].swapcase()]
        yield from frontier


def moves(max_length=5, cmax=2.2):
    out, seen = [], set()
    for word in reduced_words(max_length):
        mat = word_matrix(word)
        c = mat[1, 0]
        if not 1e-12 < abs(c) <= cmax:
            continue
        if c.real < 0 or (abs(c.real) < 1e-12 and c.imag < 0):
            mat = -mat
        key = tuple(np.round([mat[1, 0].real, mat[1, 0].imag,
                              mat[1, 1].real, mat[1, 1].imag], 9))
        if key not in seen:
            seen.add(key)
            out.append((mat, word, period(word)))
    return out


def action(mat, w, z):
    a, b = mat[0]
    c, d = mat[1]
    v = c * w + d
    den = abs(v)**2 + abs(c)**2 * z*z
    return ((a*w+b)*v.conjugate()+a*c.conjugate()*z*z)/den, z/den


def reduce_lattice(w):
    mu = int(round(w.real))
    lam = int(round(w.imag / LENGTH))
    return w-mu-1j*LENGTH*lam, -mu, (mu, lam)


def pullback(move_list, w, z, max_steps=100, keep_trace=False):
    w, cocycle, shifts = reduce_lattice(w)
    trace = [("lattice", shifts)] if keep_trace else []
    mats = np.array([m[0] for m in move_list])
    c, d = mats[:, 1, 0], mats[:, 1, 1]
    for step in range(max_steps):
        den = abs(c*w+d)**2+abs(c)**2*z*z
        idx = int(np.argmin(den))
        if den[idx] >= 1-1e-12:
            return w, z, cocycle, trace
        mat, word, ab = move_list[idx]
        w, z = action(mat, w, z)
        w, ab_lattice, shifts = reduce_lattice(w)
        cocycle += ab + ab_lattice
        if keep_trace:
            trace.extend([("word", word), ("lattice", shifts)])
    raise RuntimeError("height ascent did not terminate within declared limit")


@dataclass(frozen=True)
class Mode:
    k: int
    l: int
    kind: str

    @property
    def norm2(self):
        return sp.Rational(self.k*self.k, 12) + self.l*self.l

    @property
    def kappa(self):
        return 2*math.pi*math.sqrt(float(self.norm2))

    def trig(self, w):
        xx = 2*math.pi*self.k*np.asarray(w).imag/LENGTH
        yy = 2*math.pi*self.l*np.asarray(w).real
        if self.kind == "SC":
            return np.sin(xx)*np.cos(yy)
        if self.kind == "CS":
            return np.cos(xx)*np.sin(yy)
        return np.sin(xx+yy)

    def exact_trig(self, x, y):
        xx, yy = 2*sp.pi*self.k*x, 2*sp.pi*self.l*y
        if self.kind == "SC":
            return sp.sin(xx)*sp.cos(yy)
        if self.kind == "CS":
            return sp.cos(xx)*sp.sin(yy)
        return sp.sin(xx+yy)


def mode_basis(cutoff, symmetry=True):
    out = []
    for k in range(int(math.ceil(cutoff*LENGTH))+1):
        for l in range(-math.ceil(cutoff), math.ceil(cutoff)+1):
            if k == l == 0 or (k == 0 and l < 0):
                continue
            if float(sp.Rational(k*k, 12)+l*l) > cutoff*cutoff+1e-12:
                continue
            if not symmetry:
                out.append(Mode(k, l, "sin"))
            elif k % 2 == 0 and l >= 0:
                if k and (k//2+l) % 2:
                    out.append(Mode(k, l, "SC"))
                if l and (k//2+l) % 2 == 0:
                    out.append(Mode(k, l, "CS"))
    return sorted(out, key=lambda m: (m.norm2, m.k, m.l, m.kind))


def basis_values(basis, w, z):
    z = np.broadcast_to(np.asarray(z, dtype=float), np.shape(w))
    return np.column_stack([z*special.kv(1, m.kappa*z)*m.trig(w)
                            for m in basis])


def normal_values(basis, w, z):
    z = np.broadcast_to(np.asarray(z, dtype=float), np.shape(w))
    return np.column_stack([-m.kappa*z*z*special.kv(0, m.kappa*z)*m.trig(w)
                            for m in basis])


def sample_points(n, seed):
    rng = np.random.default_rng(seed)
    return rng.uniform(-0.5, 0.5, n) + 1j*LENGTH*rng.uniform(-0.5, 0.5, n)


def equations(basis, move_list, height, n, seed):
    w = sample_points(n, seed)
    pulled = [pullback(move_list, v, height) for v in w]
    wstar = np.array([p[0] for p in pulled])
    zstar = np.array([p[1] for p in pulled])
    ab = np.array([p[2] for p in pulled])
    matrix = basis_values(basis, wstar, zstar)-basis_values(basis, w, height)
    rhs = ab-wstar.real+w.real
    return matrix, rhs, ab, w, wstar, zstar


def least_squares(matrix, rhs):
    norms = np.linalg.norm(matrix, axis=0)
    if np.any(norms == 0):
        raise ValueError("identically zero collocation column")
    scaled = matrix/norms
    solution, _, rank, singular = np.linalg.lstsq(scaled, rhs, rcond=1e-12)
    return solution/norms, int(rank), singular


def fit(cutoff, height, seed, move_list, symmetry=True, controls=False):
    basis = mode_basis(cutoff, symmetry)
    n = max(600, 8*len(basis))
    mat, rhs, ab, *_ = equations(basis, move_list, height, n, seed)
    coefficients, rank, singular = least_squares(mat, rhs)
    hold_height = max(0.53, height-0.02)
    hold, hold_rhs, *_ = equations(basis, move_list, hold_height,
                                    max(700, 5*len(basis)), seed+10000)
    lead = next(i for i, m in enumerate(basis) if m.k == 2 and m.l == 0)
    report = {
        "cutoff": cutoff, "height": height, "seed": seed,
        "symmetry_restricted": symmetry, "samples": n, "rank": rank,
        "mode_count": len(basis), "move_count": len(move_list),
        "singular_values": singular.tolist(),
        "condition_scaled": float(singular[0]/singular[-1]),
        "train_max": float(np.max(abs(mat@coefficients-rhs))),
        "holdout_height": hold_height,
        "holdout_max": float(np.max(abs(hold@coefficients-hold_rhs))),
        "leading_coefficient": float(coefficients[lead]),
        "modes": [{"k": m.k, "l": m.l, "kind": m.kind,
                   "norm_squared": str(m.norm2), "coefficient": float(c)}
                  for m, c in zip(basis, coefficients)],
    }
    if controls:
        zero, _, _ = least_squares(mat, rhs*0)
        target = np.zeros(len(basis))
        target[lead] = 0.75
        manufactured, _, _ = least_squares(mat, mat@target)
        wrong, _, _ = least_squares(mat, rhs-ab)
        report["controls"] = {
            "zero_period_max_coefficient": float(np.max(abs(zero))),
            "manufactured_field_holdout": float(np.max(abs(hold@(manufactured-target)))),
            "manufactured_leading_error": float(abs(manufactured[lead]-0.75)),
            "wrong_cocycle_genuine_holdout": float(np.max(abs(hold@wrong-hold_rhs))),
        }
    return report


def exact_geometry():
    z, kappa = sp.symbols("z kappa", positive=True)
    F = z*sp.besselk(1, kappa*z)
    ode = sp.simplify(sp.expand_func(sp.diff(F, z, 2)-sp.diff(F, z)/z-kappa*kappa*F))
    normal = sp.simplify(sp.expand_func(z*sp.diff(F, z)+kappa*z*z*sp.besselk(0, kappa*z)))
    wrong = sp.exp(-kappa*z)
    wrong_ode = sp.simplify(sp.diff(wrong, z, 2)-sp.diff(wrong, z)/z-kappa*kappa*wrong)
    p, q, L, z0, Z = sp.symbols("p q L z0 Z", positive=True)
    norm = sp.integrate((L*p*p+q*q/L)/z, (z, z0, Z))
    volume = sp.integrate(L/z**3, (z, z0, sp.oo))
    x, y = sp.symbols("x y", real=True)
    transformations = [(x+sp.Rational(1, 2), y, 1), (-x, -y, -1),
                       (x+sp.Rational(1, 4), -y+sp.Rational(1, 2), -1),
                       (-x+sp.Rational(1, 4), y+sp.Rational(1, 2), 1)]
    residuals = []
    for mode in mode_basis(2):
        trig = mode.exact_trig(x, y)
        residuals.extend(str(sp.trigsimp(trig.subs({x: xx, y: yy}, simultaneous=True)-eps*trig))
                         for xx, yy, eps in transformations)
    a = sp.Matrix([[1, 1], [0, 1]])
    b = sp.Matrix([[1, 0], [(1-sp.sqrt(3)*sp.I)/2, 1]])
    gen = {"a": a, "b": b, "A": a.inv(), "B": b.inv()}
    w = "bABa"
    relator = "a"+w+"B"+inverse_word(w)
    product = sp.eye(2)
    for letter in relator:
        product = sp.simplify(product*gen[letter])
    return {"bessel_ode_residual": str(ode), "normal_derivative_residual": str(normal),
            "cylinder_kernel_residual": str(wrong_ode), "period_norm": str(norm),
            "constant_scalar_norm": str(volume), "symmetry_residuals": residuals,
            "relator": relator, "relator_residual": str(sp.simplify(product-sp.eye(2))),
            "relator_period": period(relator)}


def coweight_parity():
    cartan = 2*sp.eye(6)
    for i, j in [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]:
        cartan[i, j] = cartan[j, i] = -1
    permutation = [5, 1, 4, 3, 2, 0]
    theta = sp.zeros(6)
    for i, j in enumerate(permutation):
        theta[j, i] = 1
    omega1, omega6 = cartan.inv()[:, 0], cartan.inv()[:, 5]
    roots, todo = set(), [tuple(sp.eye(6)[:, i]) for i in range(6)]
    while todo:
        v = todo.pop()
        if v in roots:
            continue
        roots.add(v)
        for i in range(6):
            reflected = list(v)
            reflected[i] -= sum(cartan[i, j]*v[j] for j in range(6))
            if tuple(reflected) not in roots:
                todo.append(tuple(reflected))
    rows = {}
    for name, u in {"omega1": omega1, "omega6": omega6,
                    "sum": omega1+omega6, "difference": omega1-omega6}.items():
        zero = [r for r in roots if (sp.Matrix(r).T*cartan*u)[0] == 0]
        rows[name] = {"coordinates": [str(v) for v in u],
                      "theta_coordinates": [str(v) for v in theta*u],
                      "even": theta*u == u, "odd": theta*u == -u,
                      "centralizer_dimension": 6+len(zero),
                      "zero_root_rank": sp.Matrix(zero).rank()}
    return {"root_count": len(roots), "theta_cartan_fixed": 6-(theta-sp.eye(6)).rank(),
            "theta_isometry": theta.T*cartan*theta == cartan,
            "omega1_to_omega6": theta*omega1 == omega6,
            "directions": rows}


def normalizable_control():
    k = Mode(2, 0, "SC").kappa
    # Integral over x,y of T^2 is 1/2 for the pure sine mode.
    density = lambda z: 0.5*LENGTH*k*k*z*(special.kv(0, k*z)**2+special.kv(1, k*z)**2)
    vals = []
    for height in (1.0, 2.0, 4.0):
        value, error = integrate.quad(density, height, np.inf, epsabs=1e-13, epsrel=1e-11)
        # Integration by parts of the exact harmonic equation.
        boundary = 0.5*LENGTH*k*height*special.kv(0, k*height)*special.kv(1, k*height)
        vals.append({"z0": height, "integral": value, "quadrature_error": error,
                     "boundary_identity": float(boundary), "difference": float(value-boundary)})
    return vals


def acceptance(fits):
    high = [f for f in fits if f["symmetry_restricted"] and f["cutoff"] >= 8]
    free = next(f for f in fits if not f["symmetry_restricted"])
    center = high[-1]["leading_coefficient"]
    spread = max(abs(f["leading_coefficient"]-center) for f in high)/max(abs(center), 1e-300)
    free_delta = abs(free["leading_coefficient"]-center)/max(abs(center), 1e-300)
    passed = (all(f["rank"] == f["mode_count"] and f["holdout_max"] < 2e-5 for f in high)
              and spread < 2e-4 and abs(center) > 1e-4
              and free["rank"] == free["mode_count"] and free["holdout_max"] < 2e-4
              and free_delta < 2e-3)
    return {"status": "NUMERICAL_CANDIDATE" if passed else "UNRESOLVED",
            "high_cutoff_relative_spread": spread, "unrestricted_relative_delta": free_delta,
            "not_an_interval_or_exact_nonvanishing_proof": True}


def main():
    start = time.monotonic()
    print(json.dumps({"stage": "exact", "geometry": exact_geometry(),
                      "e6": coweight_parity(), "end_norm_positive_controls": normalizable_control()}, indent=2), flush=True)
    move5, move7 = moves(5), moves(7)
    configs = [(4, .65, 1301, move5, True), (6, .65, 1302, move5, True),
               (8, .55, 1303, move5, True), (10, .65, 1304, move5, True),
               (10, .75, 1305, move7, True), (6, .65, 1306, move7, False)]
    fitted = []
    for cutoff, height, seed, move_list, symmetry in configs:
        result = fit(cutoff, height, seed, move_list, symmetry, controls=cutoff == 6 and symmetry)
        fitted.append(result)
        print(json.dumps({"stage": "fit", "fit": result}, indent=2), flush=True)
    print(json.dumps({"stage": "verdict", **acceptance(fitted),
                      "elapsed_seconds": time.monotonic()-start}, indent=2), flush=True)


if __name__ == "__main__":
    main()
