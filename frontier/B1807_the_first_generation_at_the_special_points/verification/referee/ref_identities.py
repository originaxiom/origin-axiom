"""Attack 1: R.R = 0, R.dR = 0, R.d2R = -dR.dR, dR.dR = eta^6/4 (q-series normalisation) at several tau, by direct theta
sums with exact termwise derivatives (refkit.py); the Wronskian -(i/8) eta^9; Ramanujan's DE2 as a jet check; and
a.R + c f2 eta^6 = 0 for random sections, with c = 1/4 (R without 1/pi) and c = 1/(4 pi^2) (R/pi, B1654/B1691-FINDINGS).
    python3 ref_identities.py   -> ref_identities.json
"""
import json, pathlib, random
import mpmath as mp
from refkit import basis, dot, nrm2, E2, E4, E6, eta6_product

HERE = pathlib.Path(__file__).resolve().parent
taus = [mp.mpc(0, 1), mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.92), mp.mpc(0.5, 0.866025403784438646763723170752936183),
        mp.mpc(0.07, 2.3), mp.mpc(0.2, 1.0) + mp.mpc(0.001, 0.0007)]
out = {"identities": {}, "sections": {}}
for t in taus:
    R, dR, d2R, eta6, e2, e4, e6 = basis(t)
    sc = nrm2(R)
    W = mp.matrix([R, dR, d2R]); wr = mp.det(W)
    eta9 = eta6 ** mp.mpf(1.5)  # branch fixed below by comparing with product
    e6p = eta6_product(t)
    eta3 = mp.sqrt(e6p)  # sign ambiguity: compare |.|
    ram = E2(t).d - (e2.v ** 2 - e4) / 12
    row = {"|R.R|/|R|^2": mp.nstr(abs(dot(R, R)) / sc, 3),
           "|R.dR|/(|R||dR|)": mp.nstr(abs(dot(R, dR)) / mp.sqrt(sc * nrm2(dR)), 3),
           "|R.d2R + dR.dR|": mp.nstr(abs(dot(R, d2R) + dot(dR, dR)), 3),
           "dR.dR / eta6": mp.nstr(dot(dR, dR) / eta6, 25),
           "eta6 theta vs product rel": mp.nstr(abs(eta6 - e6p) / abs(e6p), 3),
           "|Wronskian| / |eta|^9 * 8": mp.nstr(abs(wr) / abs(eta3) ** 3 * 8, 20),
           "Wronskian / (-(i/8) eta6^(3/2)) (branch-free check of |.|: should have modulus 1)": mp.nstr(abs(wr / (-(1j / 8) * eta6 * mp.sqrt(e6p))), 20),
           "Ramanujan DE2 residual": mp.nstr(abs(ram), 3)}
    out["identities"][mp.nstr(t, 8)] = row


def Mbasis_vals(w, e4, e6):
    return [e4 ** a * e6 ** ((w - 4 * a) // 6) for a in range(w // 4 + 1) if w >= 0 and (w - 4 * a) % 6 == 0]


rng = random.Random(1807)
for n in range(0, 12):
    coefs = [[complex(rng.uniform(-3, 3), rng.uniform(-3, 3)) for _ in range(6)] for _ in range(3)]
    worst4, worstpi = 0, 0
    for t in taus:
        R, dR, d2R, eta6, e2, e4, e6 = basis(t)
        fs = []
        for j in range(3):
            b = Mbasis_vals(2 * n - 2 * j, e4, e6)
            fs.append(sum(c * g for c, g in zip(coefs[j], b)) if b else mp.mpc(0))
        a = [fs[0] * R[i] + fs[1] * dR[i] + fs[2] * d2R[i] for i in range(3)]
        aR = dot(a, R)
        scale = mp.sqrt(nrm2(a) * nrm2(R))
        worst4 = max(worst4, abs(aR + fs[2] * eta6 / 4) / scale)
        # B1654 normalisation: R' = R/pi and the section built from R' (a' = a/pi): a'.R' = a.R/pi^2
        worstpi = max(worstpi, abs(aR / mp.pi ** 2 + fs[2] * eta6 / (4 * mp.pi ** 2)) / (scale / mp.pi ** 2))
    out["sections"][str(mp.mpf(4 * n - 1) / 2)] = {"max rel |a.R + f2 eta6/4| (q-series R)": mp.nstr(worst4, 3),
                                                  "max rel |a'.R' + f2 eta6/(4 pi^2)| (R/pi)": mp.nstr(worstpi, 3)}
(HERE / "ref_identities.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
