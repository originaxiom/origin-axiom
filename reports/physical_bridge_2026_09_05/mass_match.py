"""Conditional singlet-mass bridge; see EXTENSION_1.md for its limited scope.

This imports ordinary 4d one-loop gauge mass renormalization, neglecting exotic
Yukawa interactions and finite matching. It does not derive a physical action
or mass spectrum from the repository's algebra.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
import sympy as sp

from .gauge_running import SM_B, evolve, inverse_couplings
from .spectrum import D_PAIR, L_PAIR, matter_beta


def casimirs(field, k=F(5, 3)):
    """Quadratic Casimirs, not indices (spectator multiplicities cancel)."""
    return (field.y**2/F(k), 3*field.weak_index/field.weak,
            8*field.color_index/field.color_dim)


def commutant_basis(generators):
    n = generators[0].rows
    entries = sp.symbols(f"m0:{n*n}")
    matrix = sp.Matrix(n, n, entries)
    equations = [entry for gen in generators for entry in gen*matrix-matrix*gen]
    constraints, rhs = sp.linear_eq_to_matrix(equations, entries)
    assert rhs == sp.zeros(rhs.rows, 1)
    return [sp.Matrix(n, n, v) for v in constraints.nullspace()]


def mass_block_check():
    """All endomorphisms of the 5 commuting with SU5 or its SM subalgebra."""
    def elementary(i, j):
        result = sp.zeros(5)
        result[i, j] = 1
        return result

    su5 = [elementary(i,j) for i in range(5) for j in range(5) if i != j]
    su5 += [elementary(i,i)-elementary(i+1,i+1) for i in range(4)]
    sm = [elementary(i,j) for block in (range(3), range(3,5))
          for i in block for j in block if i != j]
    sm += [elementary(i,i)-elementary(i+1,i+1) for i in (0,1,3)]
    sm += [sp.diag(-sp.Rational(1,3), -sp.Rational(1,3), -sp.Rational(1,3),
                   sp.Rational(1,2), sp.Rational(1,2))]
    full, broken = commutant_basis(su5), commutant_basis(sm)
    pd, pl = sp.diag(1,1,1,0,0), sp.diag(0,0,0,1,1)
    assert len(su5) == 24 and len(sm) == 12
    assert all(gen*m == m*gen for m in full for gen in su5)
    assert all(gen*m == m*gen for m in broken for gen in sm)
    assert len(full) == 1 and full[0].is_diagonal()
    assert full[0] == full[0][0,0]*sp.eye(5)
    assert len(broken) == 2
    assert all(gen*m == m*gen for m in (pd,pl) for gen in sm)
    # A nonzero doublet/triplet split is allowed by the SM, not by full SU5.
    split = 2*pd+3*pl
    assert any(gen*split != split*gen for gen in su5)
    return {"SU5_commutant_dimension": len(full), "SM_commutant_dimension": len(broken),
            "SU5_basis": [str(m) for m in full], "SM_basis": [str(m) for m in broken],
            "split_mass_control_rejected_by_SU5": True}


def alpha_integrals(x_ir, t_end, thresholds, *, start=0., baseline=SM_B):
    """Integral of each alpha from start to t_end on a piecewise one-loop path.

Returns an analytic integral and an independent quadrature of the local
running coupling. Thresholds activate delta_b at log(M/MZ).
"""
    if not (math.isfinite(start) and math.isfinite(t_end) and 0 <= start <= t_end):
        raise ValueError("require 0 <= start <= t_end")
    events = sorted([(float(t), np.asarray(db, float)) for t, db in thresholds],
                    key=lambda item: item[0])
    if any(not math.isfinite(t) or not 0 <= t <= t_end or db.shape != (3,)
           or not np.isfinite(db).all() for t, db in events):
        raise ValueError("invalid threshold")
    events.append((t_end, np.zeros(3)))
    x, b = np.asarray(x_ir, float), np.array(baseline, float)
    analytic, numerical = np.zeros(3), np.zeros(3)
    previous = 0.
    for end, db in events:
        x_end = evolve(x, previous, end, loops=1, b=b)
        left = max(start, previous)
        if left < end:
            x_left = evolve(x, previous, left, loops=1, b=b)
            for i in range(3):
                width = end-left
                if b[i] == 0:
                    analytic[i] += width/x_left[i]
                else:
                    analytic[i] += -2*math.pi/b[i]*math.log1p(
                        -b[i]*width/(2*math.pi*x_left[i]))
                value, error = quad(lambda t: 1/(x_left[i]-b[i]*(t-left)/(2*math.pi)),
                                    left, end, epsabs=2e-12, epsrel=2e-12)
                if error > 1e-8:
                    raise RuntimeError("quadrature control did not converge")
                numerical[i] += value
        x, b, previous = x_end, b+db, end
    return analytic, numerical


def log_mass_enhancement(integrals, field):
    """log[m(IR)/m(UV)], with only the one-loop gauge term active."""
    return float(6*np.dot(np.array(casimirs(field), float), integrals)/(4*math.pi))


def common_uv_upper_bound(x_ir, t_u, copies):
    """Uniform bound over ALL thresholds in [MZ,MU], for this spectrum only.

Each pair starts with equal UV singular values. At the self-consistent
decoupling points, log(MD/ML)=integral(gamma_D)-integral(gamma_L).
Discard the positive second term and bound the first over the whole interval.
None means the chosen bound is inconclusive, not that the model is impossible.
"""
    x = np.asarray(x_ir, float)
    if (copies not in (1,2,3) or x.shape != (3,) or not np.isfinite(x).all()
            or (x <= 0).any() or not math.isfinite(t_u) or t_u < 0):
        raise ValueError("require 1..3 copies, positive couplings, finite t_U >= 0")
    b1_max = float(F(41,10)+F(2,3)*copies)
    x1_lower = x[0]-b1_max*t_u/(2*math.pi)
    if x1_lower <= 0:
        return None
    a1_max, a3_max = float(1/x1_lower), float(1/x[2])
    single = t_u*((2/5)*a1_max+8*a3_max)/(4*math.pi)
    return {"alpha1_uniform_upper_bound": a1_max,
            "alpha3_uniform_upper_bound": a3_max,
            "per_pair_log_MD_over_ML_upper_bound": single,
            "sum_log_MD_over_ML_upper_bound": copies*single}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error("output exists; choose a new path to preserve the run")
    raw = args.input.read_bytes()
    source = json.loads(raw)
    r2 = source["R2_spectrum"]
    # The archive is the same historical numerical fixture as R1/R2, not new data.
    from .run_audit import BANK, RESULT_HASH, legacy_functions
    archived = (BANK / "results.json").read_bytes()
    if hashlib.sha256(archived).hexdigest() != RESULT_HASH:
        raise RuntimeError("historical fixture changed")
    fixture = json.loads(archived)
    old, _ = legacy_functions()
    mz = old["MZ"]
    x = inverse_couplings(fixture["input"]["inv_alpha_em_MZ"],
                         fixture["test_pair"]["sw2"][0], fixture["test_pair"]["alpha_s"][0])
    t = r2["required_t_U"]
    required = -r2["required_sum_log_M_L_over_M_D"]
    bounds = []
    for n in (1,2,3):
        bound = common_uv_upper_bound(x, t, n)
        bounds.append({"copies": n, "bound": bound,
                       "sufficient_to_exclude_common_UV_mass_in_this_model":
                           bound is not None and bound["sum_log_MD_over_ML_upper_bound"] < required})
    examples = []
    d, l = np.array(matter_beta(D_PAIR), float), np.array(matter_beta(L_PAIR), float)
    for row in r2["examples"]:
        if not row["feasible_with_all_masses_between_MZ_and_MU"]:
            continue
        n = row["copies"]
        td, tl = (math.log(row[f"illustrative_M_{name}_GeV"]/mz) for name in ("D","L"))
        thresholds = [(td,n*d), (tl,n*l)]
        ad, qd = alpha_integrals(x, t, thresholds, start=td)
        al, ql = alpha_integrals(x, t, thresholds, start=tl)
        hd = log_mass_enhancement(ad, D_PAIR[0])
        hl = log_mass_enhancement(al, L_PAIR[0])
        examples.append({"copies": n, "log_D_mass_enhancement": hd,
                         "log_L_mass_enhancement": hl,
                         "required_log_UV_mass_D_over_L_per_equal_copy": td-tl-hd+hl,
                         "analytic_quadrature_difference": float(max(max(abs(ad-qd)),
                                                                      max(abs(al-ql))))})
    result = {"status": "POST-R1/R2 CONDITIONAL MODEL CHECK; no new empirical test",
              "input_sha256": hashlib.sha256(raw).hexdigest(),
              "mass_blocks": mass_block_check(),
              "D_Casimirs_exact": [str(c) for c in casimirs(D_PAIR[0])],
              "L_Casimirs_exact": [str(c) for c in casimirs(L_PAIR[0])],
              "required_sum_log_MD_over_ML": required,
              "uniform_bounds": bounds, "illustrative_models": examples}
    # Validate the complete serialization BEFORE creating a result artifact.
    payload = json.dumps(result, indent=2, allow_nan=False)
    with args.output.open("x") as handle:
        handle.write(payload+"\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
