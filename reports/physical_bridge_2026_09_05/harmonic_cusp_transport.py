"""Post-result, separately sealed R13 direct Gamma and 1-form controls."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy import special

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("r13_harmonic_cusp_transport_source", HERE / "harmonic_cusp.py")
HC = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = HC
SPEC.loader.exec_module(HC)


def candidate():
    records = json.loads((HERE / "harmonic_cusp_results.json").read_text())["records"]
    fit = next(r["fit"] for r in records if r["stage"] == "fit" and r["fit"]["seed"] == 1304)
    return ([HC.Mode(m["k"], m["l"], m["kind"]) for m in fit["modes"]],
            np.array([m["coefficient"] for m in fit["modes"]]))


def potential(basis, coefficients, w, z):
    return np.asarray(w).real + HC.basis_values(basis, w, z) @ coefficients


def one_form(basis, coefficients, w, z):
    """Components in (Re w, Im w, z), not orthonormal components."""
    w, z = np.asarray(w), np.asarray(z)
    dy, du, dz = np.ones(w.shape), np.zeros(w.shape), np.zeros(w.shape)
    for mode, coefficient in zip(basis, coefficients):
        X, Y = 2*np.pi*mode.k*w.imag/HC.LENGTH, 2*np.pi*mode.l*w.real
        if mode.kind == "SC":
            tx = 2*np.pi*mode.k*np.cos(X)*np.cos(Y)
            ty = -2*np.pi*mode.l*np.sin(X)*np.sin(Y)
        elif mode.kind == "CS":
            tx = -2*np.pi*mode.k*np.sin(X)*np.sin(Y)
            ty = 2*np.pi*mode.l*np.cos(X)*np.cos(Y)
        else:
            tx = 2*np.pi*mode.k*np.cos(X+Y)
            ty = 2*np.pi*mode.l*np.cos(X+Y)
        radial = z*special.kv(1, mode.kappa*z)
        dy += coefficient*radial*ty
        du += coefficient*radial*tx/HC.LENGTH
        dz -= coefficient*mode.kappa*z*special.kv(0, mode.kappa*z)*mode.trig(w)
    return np.column_stack([dy, du, dz])


def transform(matrix, point):
    w, z = HC.action(matrix, complex(point[0], point[1]), point[2])
    return np.array([w.real, w.imag, z])


def jacobian(matrix, point, step):
    axes = step*np.eye(3)
    return np.column_stack([(transform(matrix, point+e)-transform(matrix, point-e))/(2*step) for e in axes])


def run():
    basis, coefficients = candidate()
    corrupted = coefficients.copy()
    corrupted[0] *= 1.01
    rows = []
    for idx, letter in enumerate("abAB"):
        rng = np.random.default_rng(2310+idx)
        samples = np.column_stack([rng.uniform(-2, 2, 3000), rng.uniform(-2, 2, 3000), rng.uniform(.6, .9, 3000)])
        mapped = np.array([transform(HC.GENERATORS[letter], p) for p in samples])
        keep = mapped[:, 2] >= .55
        samples, mapped = samples[keep], mapped[keep]
        w, z = samples[:, 0]+1j*samples[:, 1], samples[:, 2]
        wp, zp = mapped[:, 0]+1j*mapped[:, 1], mapped[:, 2]
        true_res = potential(basis, coefficients, wp, zp)-potential(basis, coefficients, w, z)-HC.period(letter)
        bad_res = potential(basis, corrupted, wp, zp)-potential(basis, corrupted, w, z)-HC.period(letter)
        derivatives = []
        for step in (2e-6, 1e-6):
            errors = []
            for point, target in zip(samples[:16], mapped[:16]):
                form = one_form(basis, coefficients, np.array([complex(point[0], point[1])]), np.array([point[2]]))[0]
                image_form = one_form(basis, coefficients, np.array([complex(target[0], target[1])]), np.array([target[2]]))[0]
                errors.append(float(np.max(abs(jacobian(HC.GENERATORS[letter], point, step).T@image_form-form))))
            derivatives.append({"step": step, "maximum": max(errors)})
        rows.append({"generator": letter, "samples_retained": len(samples),
                     "minimum_both_heights": float(min(z.min(), zp.min())),
                     "primitive_transport_max": float(np.max(abs(true_res))),
                     "corrupted_transport_max": float(np.max(abs(bad_res))),
                     "one_form_pullback": derivatives})
    rms = []
    for height in (1., 2.):
        x, y = np.meshgrid(np.arange(128)/128, np.arange(128)/128, indexing="ij")
        w = y.ravel()+1j*HC.LENGTH*x.ravel()
        form = one_form(basis, coefficients, w, np.full(w.shape, height))
        periods = form[:, 0].reshape(128, 128).mean(axis=1)
        rms.append({"height": height, "max_period_error": float(np.max(abs(periods-1))),
                    "tangential_orthonormal_rms": float(height*np.sqrt(np.mean(form[:, 0]**2+form[:, 1]**2))),
                    "normal_orthonormal_rms": float(height*np.sqrt(np.mean(form[:, 2]**2)))})
    return {"direct_generator_checks": rows, "period_and_components": rms}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
