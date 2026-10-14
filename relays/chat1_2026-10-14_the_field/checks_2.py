"""Second batch of checks for THE PASSAGE TO THE FIELD (chat1, 2026-10-14). Not sealed predictions; plumbing of known
mathematics plus one unpredicted read-out (C10), reported with its controls.

  C9  The three Higgs fields at the common point, one per parity: f_s(z) = theta_s(z)/theta_1(z) (s = 2, 3, 4) is
      meromorphic with one simple pole at the puncture z = 0 (residue theta_s(0)/theta_1'(0)) and changes sign along
      the two periods by a non-trivial character, a different one for each s; and f_s^2 = (theta_s(0)/theta_1'(0))^2
      (wp(z) - e_s), where e_s = wp at the zero of theta_s. wp is computed from theta_1 alone
      (wp = -(log theta_1)'' + theta_1'''(0)/(3 theta_1'(0))), so the e_s are not taken from theta-constant formulas.
      So a Higgs at the puncture a in M_C extends to Phi_a = sum_r a_r f_r(z) e_r dz with residue a, and
      det-type invariant: Phi_a^2 = -[(a.a) wp + const_a] dz^2 with const_a = -sum_r a_r^2 e_r (the units anticommute).
  C10 READ-OUT: the record's residue triplet R (B1644/B1645, units' labels i <-> theta_2, j <-> theta_4,
      k <-> theta_3) has sum_r R_r^2 e_r = 0 when each unit is paired with the e of its own theta's zero; with the
      other five pairings it is not 0 (the control). With Jacobi (R.R = 0), this would say: the Higgs field with
      residue R is nilpotent at every point of the fibre (Phi_R^2 = 0), not only at the puncture.
"""
import json, pathlib, itertools
import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
mp.mp.dps = 30
out = {}

def theta(s, z, t, K=40):
    q = lambda e: mp.e ** (mp.pi * 1j * t * e)
    if s == 1:
        return -1j * mp.fsum((-1) ** n * q((n + mp.mpf(1) / 2) ** 2) * mp.e ** (mp.pi * 1j * (2 * n + 1) * z) for n in range(-K, K))
    if s == 2:
        return mp.fsum(q((n + mp.mpf(1) / 2) ** 2) * mp.e ** (mp.pi * 1j * (2 * n + 1) * z) for n in range(-K, K))
    if s == 3:
        return mp.fsum(q(n * n) * mp.e ** (2 * mp.pi * 1j * n * z) for n in range(-K, K + 1))
    return mp.fsum((-1) ** n * q(n * n) * mp.e ** (2 * mp.pi * 1j * n * z) for n in range(-K, K + 1))

def wp_factory(t):
    d1 = mp.diff(lambda z: theta(1, z, t), 0, 1); d3 = mp.diff(lambda z: theta(1, z, t), 0, 3)
    C = d3 / (3 * d1)
    return (lambda z: -mp.diff(lambda w: mp.log(theta(1, w, t)), z, 2) + C), d1

zero_of = {2: lambda t: mp.mpf(1) / 2, 4: lambda t: t / 2, 3: lambda t: (1 + t) / 2}   # zeros of theta_2, theta_4, theta_3
UNIT_THETA = {"i": 2, "j": 4, "k": 3}                                                   # B1644's labels

rows = []
for t in [mp.mpc(0.13, 1.07), mp.mpc(0, 1), mp.mpc(-0.31, 0.82), mp.mpc(0.2, 1.6)]:
    wp, d1 = wp_factory(t)
    e = {s: wp(zero_of[s](t)) for s in (2, 3, 4)}
    row = {"tau": [float(t.real), float(t.imag)], "sum_e": float(abs(e[2] + e[3] + e[4]))}
    # C9: characters, residues, f^2 = c^2 (wp - e_s)
    z0 = mp.mpc(0.231, 0.117)
    for s in (2, 3, 4):
        f = lambda z: theta(s, z, t) / theta(1, z, t)
        c = theta(s, 0, t) / d1
        row[f"f{s}_char_(z+1,z+tau)"] = [int(mp.nint(mp.re(f(z0 + 1) / f(z0)))), int(mp.nint(mp.re(f(z0 + t) / f(z0))))]
        row[f"f{s}_char_residual"] = float(max(abs(f(z0 + 1) / f(z0) - mp.nint(mp.re(f(z0 + 1) / f(z0)))), abs(f(z0 + t) / f(z0) - mp.nint(mp.re(f(z0 + t) / f(z0))))))
        rz = mp.mpf("1e-8"); row[f"f{s}_residue_err"] = float(abs(f(rz) * rz - c) / abs(c))
        row[f"f{s}^2_vs_c^2(wp-e)"] = float(max(abs(f(z) ** 2 - c ** 2 * (wp(z) - e[s])) / abs(f(z) ** 2) for z in (z0, mp.mpc(0.37, 0.41), mp.mpc(-0.2, 0.33))))
    # C10: sum R_r^2 e_r with the record's R and each pairing of units to e's
    den = mp.pi * theta(2, 0, t) * theta(3, 0, t) * theta(4, 0, t)
    R = {"i": -theta(2, 0, t) ** 2 / den, "j": -theta(4, 0, t) ** 2 / den, "k": 1j * theta(3, 0, t) ** 2 / den}
    scale = sum(abs(R[u]) ** 2 * abs(e[UNIT_THETA[u]]) for u in "ijk")
    pair = {}
    for perm in itertools.permutations((2, 4, 3)):
        lab = "".join(str(p) for p in perm)
        pair[lab] = float(abs(sum(R[u] ** 2 * e[p] for u, p in zip("ijk", perm))) / scale)
    row["sum_R^2_e_by_pairing_(i,j,k)->theta_zero"] = pair
    row["R.R_rel"] = float(abs(sum(R[u] ** 2 for u in "ijk")) / sum(abs(R[u]) ** 2 for u in "ijk"))
    rows.append(row)
out["rows"] = rows
out["C10_record_pairing"] = "243 (i<->theta_2's zero 1/2, j<->theta_4's zero tau/2, k<->theta_3's zero (1+tau)/2)"
print(json.dumps(out, indent=1))
json.dump(out, open(HERE / "checks_2.json", "w"), indent=1)
