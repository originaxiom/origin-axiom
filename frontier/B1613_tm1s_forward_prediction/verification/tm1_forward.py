#!/usr/bin/env python3
"""B1613 -- TM1'S FORWARD PREDICTION: the CP phase the weave's one viable mixing relation implies.  B1612: the weave's
group allows the TM1 column (|U_e1|^2, |U_mu1|^2, |U_tau1|^2) = (2/3, 1/6, 1/6) (the root's double tick RL against RRL,
without the swap), a one-parameter relation that survives the data.  In the standard parametrisation TM1 gives
  c12^2 c13^2 = 2/3                                    (fixes theta_12 from theta_13)
  |U_mu1| = |U_tau1|  <=>  cos 2t23 (s12^2 - c12^2 s13^2) + 2 s12 c12 s13 sin 2t23 cos d = 0
                     <=>  cos d = - cos 2t23 (s12^2 - c12^2 s13^2) / (2 s12 c12 s13 sin 2t23)
so, with theta_13 and theta_23 measured, delta_CP is fixed up to d -> 360 - d.  Computed here:
 F1  the identity checked numerically: building U from (t12 by TM1, t13, t23, d by the formula) reproduces the TM1 column
     to 1e-12 at many points, both branches.
 F2  the predicted delta_CP bands (both branches) from the inputs' central values, their 1-sigma and their 3-sigma
     ranges (theta_23's range dominates); the Jarlskog invariant J on each branch.
 F3  where the TM1 relation cannot hold: the theta_23 values for which |cos d| > 1 within theta_13's range (none expected
     near maximal mixing).
Inputs, named before the run: NuFIT 6.1 normal ordering via the record's B1066 (arXiv:2604.04585 Table 1; secondary):
sin^2 t13 = 0.02248 (+0.00055 -0.00059), sin^2 t23 = 0.470 (+0.017 -0.014); the 3-sigma range of t23, 41.27 to 49.86
degrees, from the NuFIT 6.1 statement as quoted in the search record of 2026-10-08 (secondary).  No delta_CP data is read
by this instrument.  Writes tm1_forward.json."""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent


def U_of(t12, t13, t23, d):
    s12, c12, s13, c13, s23, c23 = np.sin(t12), np.cos(t12), np.sin(t13), np.cos(t13), np.sin(t23), np.cos(t23)
    e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 * np.conj(e)],
                     [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])


def tm1_t12(t13):
    return np.arccos(np.sqrt(2 / 3) / np.cos(t13))


def cos_delta(t13, t23):
    t12 = tm1_t12(t13); s12, c12, s13 = np.sin(t12), np.cos(t12), np.sin(t13)
    return -np.cos(2 * t23) * (s12 ** 2 - c12 ** 2 * s13 ** 2) / (2 * s12 * c12 * s13 * np.sin(2 * t23))


def jarlskog(t12, t13, t23, d):
    U = U_of(t12, t13, t23, d); return float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))


def main():
    out = {}
    rng = np.random.default_rng(1613); worst = 0.0
    for _ in range(2000):
        t13 = np.arcsin(np.sqrt(rng.uniform(0.018, 0.027))); t23 = np.radians(rng.uniform(40, 50))
        cd = cos_delta(t13, t23)
        if abs(cd) > 1: continue
        for d in (np.arccos(cd), 2 * np.pi - np.arccos(cd)):
            U = U_of(tm1_t12(t13), t13, t23, d); col = np.abs(U[:, 0]) ** 2
            worst = max(worst, float(np.max(np.abs(col - np.array([2 / 3, 1 / 6, 1 / 6])))))
    out["F1"] = {"max_deviation_from_TM1_column": worst, "identity_holds": worst < 1e-12}
    s13c, s13u, s13d = 0.02248, 0.00055, 0.00059; s23c, s23u, s23d = 0.470, 0.017, 0.014
    t13 = lambda s: np.arcsin(np.sqrt(s)); t23s = lambda s: np.arcsin(np.sqrt(s))
    def band(t23_lo, t23_hi, s13_lo, s13_hi):
        ds = []
        for a in np.linspace(t23_lo, t23_hi, 401):
            for b in np.linspace(s13_lo, s13_hi, 21):
                cd = cos_delta(t13(b), a)
                if abs(cd) <= 1: ds.append(np.degrees(np.arccos(cd)))
        lo, hi = min(ds), max(ds)
        return {"upper_half_plane_deg": [round(lo, 2), round(hi, 2)], "lower_half_plane_deg": [round(360 - hi, 2), round(360 - lo, 2)]}
    t23c = t23s(s23c)
    cdc = cos_delta(t13(s13c), t23c); dc = np.degrees(np.arccos(cdc))
    t12c = tm1_t12(t13(s13c))
    out["F2"] = {"central": {"sin2_theta12_TM1": round(float(np.sin(t12c) ** 2), 5), "theta23_deg": round(float(np.degrees(t23c)), 3),
                             "cos_delta": round(float(cdc), 5), "delta_deg_branches": [round(float(dc), 2), round(float(360 - dc), 2)],
                             "J_branches": [round(jarlskog(t12c, t13(s13c), t23c, np.radians(dc)), 5), round(jarlskog(t12c, t13(s13c), t23c, np.radians(360 - dc)), 5)]},
                 "one_sigma": band(t23s(s23c - s23d), t23s(s23c + s23u), s13c - s13d, s13c + s13u),
                 "three_sigma_theta23_41.27_to_49.86": band(np.radians(41.27), np.radians(49.86), s13c - 3 * s13d, s13c + 3 * s13u)}
    bad = [round(float(a), 2) for a in np.linspace(35, 55, 401) if any(abs(cos_delta(t13(b), np.radians(a))) > 1 for b in (s13c - 3 * s13d, s13c + 3 * s13u))]
    segs = []
    for a in bad:
        if segs and abs(a - segs[-1][1]) < 0.051: segs[-1][1] = a
        else: segs.append([a, a])
    out["F3"] = {"theta23_deg_segments_where_TM1_fails_within_theta13_3sigma": segs, "n_points": len(bad)}
    json.dump(out, open(HERE / "tm1_forward.json", "w"), indent=1); print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
