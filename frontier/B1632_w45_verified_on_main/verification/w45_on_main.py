#!/usr/bin/env python3
"""B1632 -- THE SM SEAT'S W45 VERIFIED ON MAIN (made load-bearing by the owner's tagging of the cusp's unit, GENESIS v1.39).
W45: the triplet T, as a representation rho_T of the metaplectic group Mp2(Z) built from the weave's own lifts, has
Riemann-Roch number chi_{3/2}(rho_T) = dim M_{3/2}(rho_T) - dim S_{1/2}(rho_T^dual) = 0 at the weight the geometry forces;
one unit of end data on every component adds dim T = 3.  Main's own route: the Borcherds-Skoruppa formula, used as an
Euler characteristic for every half-integral weight,
    chi_k(rho) = d + d k / 12 - alpha(e^{pi i k/2} rho(S)) - alpha((e^{pi i k/3} rho(S) rho(T))^{-1}) - alpha(rho(T)),
alpha(A) = sum of beta_j over A's eigenvalues e^{2 pi i beta_j}, 0 <= beta_j < 1.  Exact up to floating point; no data.
 C0  calibration on known spaces: the trivial representation (chi_0 = 1, chi_2 = 0, chi_4 = 1, chi_6 = 1, chi_12 = 2) and
     the eta multiplier (rho(T) = e^{2 pi i/24}, rho(S) = e^{-pi i/4}: chi_{1/2} = 1, the form eta).
 C1  the weave's lifts on T: the S-lift (H_1 matrix [[0,-1],[1,0]], B1630's R L^-1 R) and the lifts of L, R; for every
     identification (S, T) in {S~, S~^-1} x {L, L^-1, R, R^-1}, whether the Mp2(Z) relations hold: S^2 central,
     S^2 = (S T)^3, S^8 = I.
 C2  for each valid identification and its dual (complex conjugate): the weights k in 1/2 Z (from -1/2 to 27/2) at which
     the weight is allowed (rho(S)^2 = e^{-pi i k} I, the centre's consistency, for this convention), and chi_k there.
 C3  the unit: allowing a pole of order n at the cusp on every component adds n d to chi (Riemann-Roch); chi_{3/2} + 3n
     for n = 0, 1, 2.
Writes w45_on_main.json."""
import json, pathlib, os, importlib.util, itertools, cmath, math
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("om", FRONTIER / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
om = importlib.util.module_from_spec(spec); spec.loader.exec_module(om)
cp = om.cp; TB = cp.TB


def alpha(A):
    s = 0.0
    for e in np.linalg.eigvals(A):
        b = (cmath.phase(e) / (2 * math.pi)) % 1.0
        if abs(b - 1.0) < 1e-9: b = 0.0
        s += b
    return s


def chi(k, rS, rT):
    d = rS.shape[0]
    return d + d * k / 12 - alpha(cmath.exp(1j * math.pi * k / 2) * rS) - alpha(np.linalg.inv(cmath.exp(1j * math.pi * k / 3) * (rS @ rT))) - alpha(rT)


def allowed(k, rS):
    return bool(np.allclose(rS @ rS, cmath.exp(-1j * math.pi * k) * np.eye(rS.shape[0]), atol=1e-9))


def main():
    out = {}
    one = np.eye(1, dtype=complex)
    triv = {k: round(chi(k, one, one), 9) for k in (0, 2, 4, 6, 12)}
    etaS = np.array([[cmath.exp(-1j * math.pi / 4)]]); etaT = np.array([[cmath.exp(2j * math.pi / 24)]])
    out["C0"] = {"trivial_chi": triv, "trivial_ok": triv == {0: 1.0, 2: 0.0, 4: 1.0, 6: 1.0, 12: 2.0},
                 "eta_chi_half": round(chi(0.5, etaS, etaT), 9), "eta_allowed_half": allowed(0.5, etaS)}
    L = {"a": "a", "b": "ab"}; R = {"a": "ab", "b": "b"}; Linv = {"a": "a", "b": "Ab"}; Rinv = {"a": "aB", "b": "b"}
    Sa = om.compose(om.compose(R, Linv), R)
    assert np.array_equal(om.h1(Sa), np.array([[0, -1], [1, 0]]))
    TS = cp.restrict(om.M_of(Sa), TB); TL = cp.restrict(om.M_of(L), TB); TR = cp.restrict(om.M_of(R), TB)
    Sopts = {"S~": TS, "S~^-1": np.linalg.inv(TS)}
    Topts = {"L": TL, "L^-1": np.linalg.inv(TL), "R": TR, "R^-1": np.linalg.inv(TR)}
    rels = []
    for (sn, S), (tn, T) in itertools.product(Sopts.items(), Topts.items()):
        S2 = S @ S
        central = bool(np.allclose(S2 @ T, T @ S2, atol=1e-9) and np.allclose(S2, S2[0, 0] * np.eye(3), atol=1e-9))
        braid = bool(np.allclose(S2, np.linalg.matrix_power(S @ T, 3), atol=1e-9))
        s8 = bool(np.allclose(np.linalg.matrix_power(S, 8), np.eye(3), atol=1e-9))
        rels.append({"S": sn, "T": tn, "S2_central_scalar": central, "S2_eq_ST_cubed": braid, "S8_eq_I": s8, "valid": central and braid and s8})
    out["C1"] = {"identifications": rels, "valid": [(r["S"], r["T"]) for r in rels if r["valid"]]}
    c2 = {}
    for r in rels:
        if not r["valid"]: continue
        S, T = Sopts[r["S"]], Topts[r["T"]]
        for name, (rS, rT) in (("rho", (S, T)), ("rho_dual", (S.conj(), T.conj()))):
            row = {}
            for twok in range(-1, 28):
                k = twok / 2
                if allowed(k, rS): row[str(k)] = round(chi(k, rS, rT), 9)
            c2[f"{r['S']},{r['T']}:{name}"] = {"allowed_weights_chi": row, "T_eigen_turns": sorted(round((cmath.phase(e) / (2 * math.pi)) % 1, 6) for e in np.linalg.eigvals(rT))}
    out["C2"] = c2
    out["C3"] = {key: {str(n): (v["allowed_weights_chi"].get("1.5") + 3 * n if v["allowed_weights_chi"].get("1.5") is not None else None) for n in (0, 1, 2)} for key, v in c2.items()}
    json.dump(out, open(HERE / "w45_on_main.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
