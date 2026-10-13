#!/usr/bin/env python3
"""B1635 post seal -- written after the sealed run (disclosed in FINDINGS).  Three read-backs the sealed instrument did not
settle, and one read-out:
 Q1  O+ at k = 1 (one-dimensional, so canonical up to scale) at tau = i read (1, 0.618033989, 0.381966011): is it exactly
     (1, 1/phi, 1/phi^2), and why?  Its matrix at i in the theta basis, normalized; its characteristic polynomial; the
     theta values at i (theta_2 = theta_4, theta_3^2 = sqrt2 theta_2^2) that produce it.
 Q2  the degeneracy at i by weight, basis-invariantly: for each piece (D, O+, O-, the symmetric sum) and k = 1 .. 11, is
     a generic member degenerate at i, and is every member (the minimum of the smallest relative gap over 400 random
     unit coefficient vectors).  Same at omega.
 Q3  the sealed per-basis-element readout is not invariant for pieces of dimension >= 2 (Tbar (x) T at k = 2 element #1
     read (1, 0.9999996, 2e-7)): for Tbar (x) T, k = 2, 4, 6, the generic member at the three generic tau and whether
     the space holds a degenerate member there.
 Q4  read-out, no prediction: O+ at k = 1 along the tick's axis (tau = 1/2 + (sqrt5/2) e^{i t}, through i).
Writes post_seal_couplings.json."""
import json, pathlib, importlib.util, math, cmath
import numpy as np
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("c", HERE / "couplings_on_the_ruled_branch.py")
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
inv = np.linalg.inv
PHI = (1 + 5 ** 0.5) / 2


def tt_piece(k, name):
    full, mons, _ = c.equivariant_space(k + 9, lambda A: inv(A).T, lambda A: inv(A))
    hol = c.cusp_condition(full, mons, 6)
    if name == "sym":
        return np.concatenate([c.restrict_piece(hol, "D"), c.restrict_piece(hol, "O+")]), mons
    return c.restrict_piece(hol, name), mons


def gap(Y):
    return c.svals(Y)[1]


def scan(pb, mons, tau, ep, n=400, seed=0):
    rng = np.random.default_rng(seed)
    if pb.shape[0] == 0: return None
    u, eta = c.u_eta(tau)
    vals = np.array([u[0] ** m[0] * u[1] ** m[1] * u[2] ** m[2] for m in mons])
    Ys = [(b @ vals) / (eta ** ep) for b in pb]
    gaps = []
    for _ in range(n if pb.shape[0] > 1 else 1):
        z = rng.normal(size=pb.shape[0]) + 1j * rng.normal(size=pb.shape[0]); z /= np.linalg.norm(z)
        gaps.append(gap(sum(zi * Y for zi, Y in zip(z, Ys))))
    return {"dim": int(pb.shape[0]), "generic_gap": round(float(gaps[0]), 9), "min_gap_over_members": round(float(min(gaps)), 9)}


def main():
    out = {}
    # Q1
    pb, mons = tt_piece(1, "O+")
    Y = c.evaluate(pb[0], mons, 1j, 18)
    Yn = Y / Y[np.unravel_index(np.argmax(np.abs(Y)), Y.shape)]
    s = np.linalg.svd(Y, compute_uv=False); s = s / s[0]
    ev = np.linalg.eigvals(Yn)
    cp = np.poly(Yn)
    u, eta = c.u_eta(1j)
    out["Q1"] = {"singular_values": [float(x) for x in s], "against_1_invphi_invphi2": [1.0, 1 / PHI, 1 / PHI ** 2],
                 "max_deviation": float(np.max(np.abs(s - np.array([1.0, 1 / PHI, 1 / PHI ** 2])))),
                 "normalized_matrix_abs": np.round(np.abs(Yn), 12).tolist(),
                 "normalized_matrix_phases_turns": np.round(np.angle(Yn) / (2 * math.pi) % 1, 9).tolist(),
                 "eigenvalues_of_the_normalized_matrix": sorted([complex(round(e.real, 12), round(e.imag, 12)) for e in ev], key=lambda z: z.real),
                 "characteristic_polynomial_coefficients": [complex(round(x.real, 12), round(x.imag, 12)) for x in cp],
                 "theta_at_i": {"u2_over_u4": complex(u[0] / u[2]), "u3_over_u2": complex(u[1] / u[0]), "sqrt2": 2 ** 0.5}}
    # Q2
    q2 = {}
    for k in range(1, 12, 2):
        for name in ("D", "O+", "O-", "sym"):
            pb, mons = tt_piece(k, name)
            q2[f"k={k} {name}"] = {"i": scan(pb, mons, 1j, 18), "omega": scan(pb, mons, c.OMEGA, 18)}
    out["Q2"] = q2
    # Q3
    q3 = {}
    for k in (2, 4, 6):
        full, mons, _ = c.equivariant_space(k, lambda A: A, lambda A: inv(A))
        q3[f"k={k}"] = {f"generic_{j}": scan(full, mons, t, 0) for j, t in enumerate(c.GENERIC)}
    out["Q3"] = q3
    # Q4
    pb, mons = tt_piece(1, "O+")
    q4 = []
    for t in np.linspace(0.15, math.pi - 0.15, 13):
        tau = complex(0.5 + (5 ** 0.5 / 2) * math.cos(t), (5 ** 0.5 / 2) * math.sin(t))
        q4.append({"tau": [round(tau.real, 6), round(tau.imag, 6)], "masses": c.svals(c.evaluate(pb[0], mons, tau, 18))[0]})
    out["Q4_O+_k1_along_the_ticks_axis"] = q4
    json.dump(out, open(HERE / "post_seal_couplings.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str)[:7000])


if __name__ == "__main__":
    main()
