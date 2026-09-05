"""R7: priced positive-square Higgs sector, full scalar and quantum checks."""
import argparse
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import time

import numpy as np
import sympy as sp
from scipy.linalg import expm

from . import vacuum as v
from . import quantum_vacuum as q
from . import quantum_shift as s


def real_vector(x):
    return np.concatenate((x.real, x.imag))


def cubic_matrix(x):
    return np.einsum("abc,c->ab", s.tensor(), x)


@lru_cache(maxsize=1)
def geometry():
    old = q.geometry()
    ks = np.zeros((294, 294))
    ks[:186, :186] = old["ks"]
    ks[186:, 186:] = 2*np.eye(108)
    si = np.zeros_like(ks)
    si[:186, :186] = old["si"]
    si[186:, 186:] = np.eye(108)/np.sqrt(2)
    z = np.concatenate((s.vacuum_coordinates(), np.zeros(108)))
    return {**old, "ks": ks, "si": si, "z": z}


def fields(z):
    z = np.asarray(z, float)
    if z.shape != (294,):
        raise ValueError("294 real coordinates required")
    p, n, a = s.fields(z[:186])
    return p, n, a, z[186:213]+1j*z[213:240], z[240:267]+1j*z[267:294]


def weights():
    out = np.full(439, .2)
    out[275:329] = .02
    out[330:438] = .02
    return out


def primitive_checks():
    geo, b = geometry(), base()
    z = geo["z"]
    np.testing.assert_allclose(constraints(z), 0, atol=1e-12)
    rng = np.random.default_rng(202609057)
    displaced = z+.02*rng.normal(size=294)
    direction = rng.normal(size=294)
    direction /= np.linalg.norm(direction)
    eps = 1e-4
    numerical = (constraints(displaced+eps*direction)-constraints(displaced-eps*direction))/(2*eps)
    np.testing.assert_allclose(numerical, jacobian(displaced)@direction, atol=2e-10)
    hplus, hminus = [full_tree_hessian(z+sign*eps*direction) for sign in [1, -1]]
    first, second = derivatives(direction)[0]
    numeric_first = geo["si"]@((hplus-hminus)/(2*eps))@geo["si"]
    numeric_second = geo["si"]@((hplus+hminus-2*b["h0"])/eps**2)@geo["si"]
    np.testing.assert_allclose(numeric_first, first, atol=2e-9)
    np.testing.assert_allclose(numeric_second, second, atol=3e-7)
    # Full compact covariance, including complex matrix entries and the cubic.
    unitary = expm(1j*(.19*geo["T"][7]+.13*geo["T"][14]))
    sv, a = unitary@geo["s"], unitary@geo["y"]@unitary.conj().T
    for sign, use_cubic in [(-1, False), (1, True)]:
        def mass(field, adj):
            operator = adj+sign*.5*np.eye(27)
            result = operator@operator
            if use_cubic:
                cc = cubic_matrix(field)
                result += cc.conj().T@cc
            return result
        np.testing.assert_allclose(mass(sv, a), unitary@mass(geo["s"], geo["y"])@unitary.conj().T,
                                   atol=2e-12)
    # Independent parameter controls, not a mode-count tolerance change.
    changed_j = jacobian(z, .4)
    changed_h = 2*changed_j.T@(weights()[:, None]*changed_j)
    detuned = np.linalg.eigvalsh(geo["si"]@changed_h@geo["si"])
    removed = weights()
    removed[384:438] = 0
    no_cubic = 2*b["j"].T@(removed[:, None]*b["j"])
    more = np.linalg.eigvalsh(geo["si"]@no_cubic@geo["si"])
    assert np.count_nonzero(detuned < 1e-9) == 77
    assert np.count_nonzero(more < 1e-9) == 89
    return {"constraint_J_error": float(np.max(np.abs(numerical-jacobian(displaced)@direction))),
            "full_H_first_error": float(np.max(np.abs(numeric_first-first))),
            "full_H_second_error": float(np.max(np.abs(numeric_second-second))),
            "complex_compact_covariance": True,
            "detuned_offset_scalar_kernel": int(np.count_nonzero(detuned < 1e-9)),
            "omitted_cubic_scalar_kernel": int(np.count_nonzero(more < 1e-9))}


def classical():
    b, geo = base(), geometry()
    scalar, fermion, vector = [SpectralTrace(m, 1.5, 1.).ev for m in b["masses"]]
    assert np.count_nonzero(scalar > 1e-9) == 209
    assert np.count_nonzero(vector > 1e-9) == 66
    np.testing.assert_allclose(b["j"]@b["go"], 0, atol=1e-12)
    light, ids = light_basis()
    assert light.shape == (294, 8)
    return {"real_scalars": 294, "positive_tree_scalar_modes": 209,
            "tree_scalar_kernel": 85, "gauge_Goldstones": 66,
            "physical_zero_modes": {"old_octet_triplet": 11, "new_Higgs_real": 8},
            "U_D_doublet_weight_indices": ids,
            "scalar_mass_squared": scalar.tolist(), "vector_mass_squared": vector.tolist(),
            "Weyl_mass_squared": fermion.tolist(),
            "new_positive_scalar_gap": float(min(x for x in np.linalg.eigvalsh(b["masses"][0][186:, 186:]) if x > 1e-9))}


@lru_cache(maxsize=1)
def quantum():
    geo, b = geometry(), base()
    mus = [.5, 1., 2.]
    instruments = [spectral(mu) for mu in mus]
    spin = np.array([1., -2., 3.])/(64*np.pi**2)
    parts = np.zeros((3, 3, 294))
    for index, direction in enumerate(np.eye(294)):
        dm = derivatives(direction)
        for mi, spec in enumerate(instruments):
            for sector in range(3):
                parts[mi, sector, index] = spin[sector]*spec[sector].first(dm[sector][0])
    ev, u = np.linalg.eigh(b["masses"][0])
    positive = ev > 1e-9
    assert np.count_nonzero(positive) == 209
    shifts, shift_changes, residuals, forces = [], [], [], []
    for mi in range(3):
        force = parts[mi].sum(axis=0)
        fc = geo["si"]@force
        kforce = u[:, ~positive].T@fc
        assert np.max(np.abs(kforce)) < 1e-8
        dc = -u[:, positive]@((u[:, positive].T@fc)/ev[positive])
        delta = geo["si"]@dc
        residual = b["h0"]@delta+force
        assert np.max(np.abs(residual)) < 1e-8
        sm = np.array(v.sm_generator_coordinates(), float)
        np.testing.assert_allclose(orbit(delta)@sm, 0, atol=1e-8)
        np.testing.assert_allclose(b["go"].T@force, 0, atol=1e-8)
        shifts.append(delta)
        shift_changes.append(derivatives(delta)[0][0])
        residuals.append([float(np.max(np.abs(kforce))), float(np.max(np.abs(residual)))])
        forces.append(force)
    light, _ = light_basis()
    light_c = np.linalg.solve(geo["si"], light)
    higgs_parts = np.zeros((3, 3, 8, 8))
    def second_all(direction, acceleration=None):
        dm = derivatives(direction, acceleration)
        return np.array([[spin[sector]*spec[sector].second(*dm[sector]) for sector in range(3)]
                         for spec in instruments])
    diagonal = [second_all(direction) for direction in light.T]
    for i in range(8):
        higgs_parts[:, :, i, i] = diagonal[i]
        for j in range(i):
            value = (second_all(light[:, i]+light[:, j])-diagonal[i]-diagonal[j])/2
            higgs_parts[:, :, i, j] = higgs_parts[:, :, j, i] = value
    angles = []
    for name, idx in [("color_octet", 2), ("weak_triplet", 5)]:
        direction, acceleration = np.zeros(294), np.zeros(294)
        direction[108+idx] = 1/np.sqrt(geo["gram"][idx, idx])
        acceleration[108:114] = -geo["yh"]/5
        canon = np.linalg.solve(geo["si"], direction)
        values = second_all(direction, acceleration)
        for mi in range(3):
            left = float(canon@shift_changes[mi]@canon)
            right = float(forces[mi]@acceleration)
            assert abs(left-right) < 1e-8
        angles.append((name, values))
    # Check covariance on the actual eight-dimensional light representation.
    sm = np.array(v.sm_generator_coordinates(), float)
    generators = [light.T@geo["ks"]@np.column_stack([orbit(r)@sm[:, k] for r in light.T])
                  for k in range(sm.shape[1])]
    runs = []
    for mi, mu in enumerate(mus):
        normal = light_c.T@shift_changes[mi]@light_c
        leading = higgs_parts[mi].sum(axis=0)+normal
        for generator in generators:
            np.testing.assert_allclose(leading@generator-generator@leading, 0, atol=1e-8)
        p, n, a, hu, hd = fields(shifts[mi])
        runs.append({"mu": mu, "gradient_parts_scalar_Weyl_vector": parts[mi].tolist(),
                     "normal_displacement": shifts[mi].tolist(),
                     "old_relative_shifts_phi1_phi2_adjoint": [float(np.linalg.norm(p)), float(np.linalg.norm(n)),
                                                               float(np.linalg.norm(a)/np.sqrt(5))],
                     "new_U_D_shift_norms_in_S_VEV_units": [float(np.linalg.norm(hu)), float(np.linalg.norm(hd))],
                     "kernel_force_and_stationarity_residual": residuals[mi],
                     "Higgs_curvature_parts_scalar_Weyl_vector": higgs_parts[mi].tolist(),
                     "Higgs_normal_shift_contribution": normal.tolist(),
                     "Higgs_leading_curvature_matrix": leading.tolist(),
                     "Higgs_leading_mass_squared": np.linalg.eigvalsh(leading).tolist(),
                     "angular_curvatures": {name: {"scalar_Weyl_vector": values[mi].tolist(),
                                                    "total": float(values[mi].sum())} for name, values in angles},
                     "SM_covariance_and_normal_shift_identity": True})
    return {"runs": runs,
            "scope": "leading effective-potential curvatures of the added model, not pole masses, RG evolution or a TOE"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    with args.output.open("x", encoding="utf-8") as handle:
        start = time.monotonic()
        result = {"primitive_checks": primitive_checks(), "classical": classical(),
                  "Yukawa_projection": exact_yukawa_projection(),
                  "exact_extra_fourth_trace": extra_fourth_trace_identity(), "quantum": quantum(),
                  "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "elapsed_seconds": time.monotonic()-start}
        json.dump(result, handle, indent=2, allow_nan=False)
        handle.write("\n")
    brief = {"primitive_checks": result["primitive_checks"], "Yukawa_projection": result["Yukawa_projection"],
             "exact_extra_fourth_trace": result["exact_extra_fourth_trace"],
             "quantum": [{key: value for key, value in row.items() if key in
                          ["mu", "old_relative_shifts_phi1_phi2_adjoint", "new_U_D_shift_norms_in_S_VEV_units",
                           "kernel_force_and_stationarity_residual", "Higgs_leading_mass_squared", "angular_curvatures"]}
                         for row in result["quantum"]["runs"]], "elapsed_seconds": result["elapsed_seconds"]}
    print(json.dumps(brief, indent=2, allow_nan=False))


def constraints(z, offset=.5):
    p, n, a, up, down = fields(z)
    return np.concatenate((v.constraints(p, n, a),
                           real_vector((a-offset*np.eye(27))@up),
                           [np.vdot(up, up).real],
                           real_vector((a+offset*np.eye(27))@down),
                           real_vector(cubic_matrix(p)@down),
                           [np.vdot(down, down).real]))


def jacobian(z, offset=.5):
    p, _, a, up, down = fields(z)
    out = np.zeros((439, 294))
    out[:275, :186] = s.constraint_data(z[:186])[1]
    ts = q.geometry()["T"]
    for start, pos, field, sign in [(275, 186, up, -1), (330, 240, down, 1)]:
        out[start:start+54, pos:pos+54] = q.real_action(a+sign*offset*np.eye(27))
        action = np.einsum("aij,j->ai", ts, field)
        out[start:start+54, 108:186] = np.hstack((action.real, action.imag)).T
    out[329, 186:240] = 2*real_vector(up)
    out[438, 240:294] = 2*real_vector(down)
    out[384:438, :54] = q.real_action(cubic_matrix(down))
    out[384:438, 240:294] = q.real_action(cubic_matrix(p))
    return out


def constraint_hessian(coefficients):
    """Weighted Hessians of all 439 explicit real constraints."""
    w = np.asarray(coefficients, float)
    if w.shape != (439,):
        raise ValueError("439 constraint coefficients required")
    out = np.zeros((294, 294))
    out[:186, :186] = s.constraint_hessian(w[:275])
    for start, pos in [(275, 186), (330, 240)]:
        z = w[start:start+27]-1j*w[start+27:start+54]
        block = np.einsum("i,aij->aj", z, q.geometry()["T"])
        block = np.hstack((block.real, -block.imag))
        out[108:186, pos:pos+54] += block
        out[pos:pos+54, 108:186] += block.T
    out[186:240, 186:240] += 2*w[329]*np.eye(54)
    out[240:294, 240:294] += 2*w[438]*np.eye(54)
    z = w[384:411]-1j*w[411:438]
    d = cubic_matrix(z)
    block = np.block([[d.real, -d.imag], [-d.imag, -d.real]])
    out[:54, 240:294] += block
    out[240:294, :54] += block.T
    return out


def full_tree_hessian(z):
    j, c, w = jacobian(z), constraints(z), weights()
    return 2*(j.T@(w[:, None]*j)+constraint_hessian(w*c))


def orbit(z):
    _, _, _, up, down = fields(z)
    out = np.zeros((294, 78))
    out[:186] = s.orbit(z[:186])
    for pos, field in [(186, up), (240, down)]:
        action = 1j*np.einsum("aij,j->ai", q.geometry()["T"], field)
        out[pos:pos+54] = np.hstack((action.real, action.imag)).T
    return out


def fermion_mass(z):
    p, n, _, up, down = fields(z)
    return .25*cubic_matrix(p+n+up+down)


@lru_cache(maxsize=1)
def base():
    geo = geometry()
    z = geo["z"]
    j, w, go, mf = jacobian(z), weights(), orbit(z), fermion_mass(z)
    h0 = 2*j.T@(w[:, None]*j)
    masses = [geo["si"]@h0@geo["si"], mf.conj().T@mf,
              .5**2*geo["gi"]@go.T@geo["ks"]@go@geo["gi"]]
    return {"j": j, "w": w, "go": go, "mf": mf, "h0": h0, "masses": masses}


def derivatives(direction, acceleration=None):
    """First/second full mass-squared derivatives, including normal constraints."""
    geo, b = geometry(), base()
    z, j, w, go, mf = geo["z"], b["j"], b["w"], b["go"], b["mf"]
    r = np.asarray(direction, float)
    acc = np.zeros(294) if acceleration is None else np.asarray(acceleration, float)
    j1, j2 = jacobian(z+r)-j, jacobian(z+acc)-j
    c1 = j@r
    c2 = 2*(constraints(z+r)-c1)+j@acc
    h1 = 2*(j1.T@(w[:, None]*j)+j.T@(w[:, None]*j1)+constraint_hessian(w*c1))
    h2 = 2*(j2.T@(w[:, None]*j)+2*j1.T@(w[:, None]*j1)
            +j.T@(w[:, None]*j2)+constraint_hessian(w*c2))
    g1, g2 = orbit(r), orbit(acc)
    k = geo["ks"]
    vm1 = g1.T@k@go+go.T@k@g1
    vm2 = g2.T@k@go+2*g1.T@k@g1+go.T@k@g2
    f1, f2 = fermion_mass(r), fermion_mass(acc)
    fm1 = f1.conj().T@mf+mf.conj().T@f1
    fm2 = f2.conj().T@mf+2*f1.conj().T@f1+mf.conj().T@f2
    return [(geo["si"]@h1@geo["si"], geo["si"]@h2@geo["si"]),
            (fm1, fm2),
            (.5**2*geo["gi"]@vm1@geo["gi"], .5**2*geo["gi"]@vm2@geo["gi"])]


class SpectralTrace:
    """Hermitian Frechet derivatives; a linear massless block is never hidden."""
    def __init__(self, mass, constant, mu):
        mass = np.asarray(mass)
        if not np.allclose(mass, mass.conj().T, atol=1e-11):
            raise ValueError("Hermitian mass required")
        ev, self.u = np.linalg.eigh(mass)
        tol = 2e-10*max(1., np.max(np.abs(ev)))
        if ev.min() < -tol:
            raise ValueError("negative mass squared at expansion point")
        ev[np.abs(ev) < tol] = 0
        self.ev, self.zero = ev, ev == 0
        self.fp = np.zeros_like(ev)
        positive = ev > 0
        self.fp[positive] = ev[positive]*(2*np.log(ev[positive]/mu**2)-2*constant+1)
        x, y = ev[:, None], ev[None, :]
        close = (x > 0)&(y > 0)&(np.abs(x-y) < 1e-8*np.maximum(x, y))
        different = (~close)&(x != y)
        self.dd = np.zeros((len(ev), len(ev)))
        self.dd[different] = ((self.fp[:, None]-self.fp[None, :])[different]
                              /(x-y)[different])
        mean = np.broadcast_to((x+y)/2, self.dd.shape)
        self.dd[close] = 2*np.log(mean[close]/mu**2)-2*constant+3
        self.fp_matrix = (self.u*self.fp)@self.u.conj().T

    def first(self, first):
        return float(np.einsum("ij,ji->", self.fp_matrix, first).real)

    def second(self, first, second):
        b = self.u.conj().T@first@self.u
        if np.any(self.zero) and np.max(np.abs(b[np.ix_(self.zero, self.zero)])) > 1e-8:
            raise ValueError("nonzero linear perturbation within massless kernel")
        return float(self.first(second)+np.sum(self.dd*np.abs(b)**2))


def spectral(mu):
    return [SpectralTrace(mass, constant, mu)
            for mass, constant in zip(base()["masses"], [1.5, 1.5, 5/6])]


@lru_cache(maxsize=1)
def light_basis():
    """Kernel enumeration first; exact generator-action identification second."""
    sv, _, ym, _, yy, psi = v.embedding()
    ds = v.contract(sv)
    upmass = (ym-sp.eye(27)/2)**2
    downmass = (ym+sp.eye(27)/2)**2+ds.H*ds
    expected_charges = [sp.Rational(1, 2), -sp.Rational(1, 2)]
    result, ids = [], []
    ts = v.representation()[4]
    weak = v.representation()[2][tuple(v.CARTAN[:, 5])]
    casimir = (weak*weak.T+weak.T*weak)/2+ts[5]**2/4
    for pos, mass, charge in zip([186, 240], [upmass, downmass], expected_charges):
        kernel = mass.nullspace()
        assert len(kernel) == 2
        indices = []
        for col in kernel:
            assert col.T*col == sp.ones(1)
            assert ym*col == charge*col
            assert casimir*col == sp.Rational(3, 4)*col
            for rootidx in [2, 3]:
                e = v.representation()[2][tuple(v.CARTAN[:, rootidx])]
                assert e*col == e.T*col == sp.zeros(27, 1)
            idx = next(i for i in range(27) if col[i])
            indices.append(idx)
            for imaginary in [False, True]:
                r = np.zeros(294)
                r[pos+idx+(27 if imaginary else 0)] = 1/np.sqrt(2)
                result.append(r)
        ids.append(indices)
    basis = np.array(result).T
    np.testing.assert_allclose(basis.T@geometry()["ks"]@basis, np.eye(8), atol=1e-12)
    np.testing.assert_allclose(base()["h0"]@basis, 0, atol=1e-12)
    return basis, ids


def exact_yukawa_projection():
    sv, nv, ym, _, yy, _ = v.embedding()
    _, ids = light_basis()
    oldmass = v.contract(sv+nv)
    raw = sp.Matrix.hstack(*oldmass.nullspace())
    gram = raw.H*raw
    assert gram.is_diagonal()
    k = raw*sp.diag(*(1/sp.sqrt(gram[i, i]) for i in range(17)))
    assert k.H*k == sp.eye(17)
    assert oldmass*k == sp.zeros(27, 17)
    em = ym+v.representation()[4][5]/2
    em_light = sp.simplify(k.H*em*k)
    assert em_light.is_diagonal()
    neutral = [next(i for i in block if em[i, i] == 0) for block in ids]
    projected = [sp.simplify(k.T*v.contract(sp.eye(27)[:, i])*k) for i in neutral]
    combined = projected[0]+projected[1]
    charge = [em_light[i, i] for i in range(17)]
    assert em_light.T*combined+combined*em_light == sp.zeros(17)
    blocks = {}
    for name, value in [("up", sp.Rational(2, 3)), ("down", sp.Rational(1, 3)),
                        ("charged_lepton", sp.Integer(1)), ("neutral", sp.Integer(0))]:
        left = [i for i, c in enumerate(charge) if c == value]
        right = [i for i, c in enumerate(charge) if c == -value]
        block = combined.extract(left, right)
        blocks[name] = {"shape": list(block.shape), "rank": block.rank(),
                        "matrix": [[str(x) for x in row] for row in block.tolist()]}
    return {"old_kernel_dimension": 17, "neutral_Higgs_indices_U_D": neutral,
            "projected_rank_U_D": [m.rank() for m in projected],
            "combined_projected_rank": combined.rank(), "blocks": blocks,
            "scope": "leading projection at small neutral Higgs VEVs, not exact finite-VEV integration"}


def extra_fourth_trace_identity():
    h = sp.symbols("h3:7", real=True)
    ts = v.representation()[1]
    a = sum((h[i]*ts[i+2] for i in range(4)), sp.zeros(27))
    sv = v.embedding()[0]
    p = v.contract(sv).H*v.contract(sv)
    assert p*p == p and sp.trace(p) == 10
    n = sp.expand(sp.trace(a*a))
    out = {}
    for name, mass in [("U", (a-sp.eye(27)/2)**2),
                       ("D", (a+sp.eye(27)/2)**2+p)]:
        fourth = sp.expand(2*sp.trace(mass*mass))
        line = sp.Poly(fourth.subs(dict.fromkeys(h[1:], 0)), h[0])
        nc = sp.Poly(n.subs(dict.fromkeys(h[1:], 0)), h[0]).coeff_monomial(h[0]**2)
        coeff = [line.coeff_monomial(h[0]**i)/nc**(i//2) for i in [0, 2, 4]]
        remainder = sp.expand(fourth-coeff[0]-coeff[1]*n-coeff[2]*n**2)
        assert remainder == 0
        out[name] = {"real_scalar_trace_coefficients_1_N_N2": list(map(str, coeff)),
                     "remainder": str(remainder),
                     "at_N_5_and_kU_kD_xi_1": str(coeff[0]+5*coeff[1]+25*coeff[2])}
    return out


if __name__ == "__main__":
    main()
