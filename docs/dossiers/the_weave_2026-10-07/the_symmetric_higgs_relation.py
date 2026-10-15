"""W94: the symmetric null Higgs at omega and the down/lepton relation with no free size. The rule (W94_RULE.md, with
its pre-run correction) was committed before this script; the objects, the cells and the priors are there.

  L1  the order-3 move gamma: tau -> -1/(tau + 1) on the (i, j, k) channels: G^3 = -1; T(omega) its eigenvector with
      eigenvalue e^{-i pi/3}; the e^{+i pi/3} eigenvector isotropic; S0 and S0bar null
  L2  k_s = 2 ||S0||^2 ||M_s||^2 / ||Y(S0, M_s)||^2 in [1/2, 2] on W59's 18 lines, and the first-order law
      m2/m3 = k_s |d_S| for S = S0 + 1e-6 X
  L3  k_lep / k_down against the data's (m_mu/m_tau)/(m_s/m_b): z > 2 everywhere (W88's allowance a = 0.10)

A fibre-frame result at one tau (omega): a frozen piece. Built on W93's implementation of B1656's frame.

Run: python3 the_symmetric_higgs_relation.py  ->  the_symmetric_higgs_relation.json beside it.
"""
import json
import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_twisted_half_bound_checked as W93  # noqa: E402

OUT = HERE / "the_symmetric_higgs_relation.json"
mp.mp.dps = 40
IJK = ("i", "j", "k")


def T_of(t):
    """the untwisted triplet (c_i theta_2^2, c_j theta_4^2, c_k theta_3^2) at tau (z-form thetas at z = 0)"""
    return mp.matrix([W93.CS[s] * W93.theta(s, 0, t) ** 2 for s in IJK])


def gamma(t):
    return -1 / (t + 1)


def fit_G():
    pts = [mp.mpc("0.13", "1.07"), mp.mpc("-0.21", "0.93"), mp.mpc("0.33", "1.4"), mp.mpc("0.05", "0.8")]
    A = mp.matrix(3, 3); Bm = mp.matrix(3, 3)
    for c, t in enumerate(pts[:3]):
        a = T_of(t); b = T_of(gamma(t)) / (t + 1)
        for r in range(3):
            A[r, c] = a[r]; Bm[r, c] = b[r]
    G = Bm * A ** -1
    t4 = pts[3]
    res = mp.norm(T_of(gamma(t4)) / (t4 + 1) - G * T_of(t4)) / mp.norm(T_of(t4))
    return G, res


def S_of(vec):
    X = mp.zeros(2, 2)
    for s, x in zip(IJK, vec):
        X += x * W93.CM[s]
    return X


def k_of(S, M):
    Y = W93.coupling_mp(S, M)
    return 2 * W93.fro(S) ** 2 * W93.fro(M) ** 2 / W93.fro(Y) ** 2


def svals(Y):
    U, sv, V = mp.svd_c(Y)
    return sorted([abs(sv[i]) for i in range(3)], reverse=True)


def main():
    out = {"rule": "W94_RULE.md", "status": "one run"}
    G, fit_res = fit_G()
    G3 = G * G * G
    om = W93.OMEGA
    Tw = T_of(om)
    lam = 1 / (om + 1)
    eig_err = mp.norm(G * Tw - lam * Tw) / mp.norm(Tw)
    E, ER = mp.eig(G)
    target = mp.exp(1j * mp.pi / 3)
    idx = min(range(3), key=lambda i: abs(E[i] - target))
    Rb = mp.matrix([ER[r, idx] for r in range(3)])
    iso_Rb = abs(sum(Rb[r] ** 2 for r in range(3))) / mp.norm(Rb) ** 2
    S0, S0b = S_of(Tw), S_of(Rb)
    l1 = {"fit residual (fourth point)": float(fit_res), "|G^3 + 1|": float(mp.mnorm(G3 + mp.eye(3), 1)),
          "T(omega) eigen error (lambda = 1/(omega + 1))": float(eig_err),
          "eigenvalues of G": [[float(mp.re(e)), float(mp.im(e))] for e in E],
          "e^{+i pi/3} eigenvector isotropy": float(iso_Rb),
          "det S0 / ||S0||^2": float(abs(W93.det2(S0)) / W93.fro(S0) ** 2),
          "det S0bar / ||S0bar||^2": float(abs(W93.det2(S0b)) / W93.fro(S0b) ** 2)}
    l1["holds"] = bool(l1["|G^3 + 1|"] < 1e-12 and eig_err < mp.mpf(10) ** -20 and abs(E[idx] - target) < 1e-20
                       and iso_Rb < mp.mpf(10) ** -25 and l1["det S0 / ||S0||^2"] < 1e-25
                       and l1["det S0bar / ||S0bar||^2"] < 1e-25)
    out["L1"] = l1
    rng = np.random.default_rng(94)
    hz = json.loads(W93.HZ.read_text(encoding="utf-8"))["masses_GeV"]
    v, sg = hz["value"], hz["sigma"]
    r_lep, r_down = v["mu"] / v["tau"], v["s"] / v["b"]
    data = r_lep / r_down
    rel = math.hypot(math.hypot(sg["mu"] / v["mu"], sg["tau"] / v["tau"]), math.hypot(sg["s"] / v["s"], sg["b"] / v["b"]))
    a = 0.10
    rows, k_ok, law_err = [], True, 0.0
    for line in W93.LINES18:
        Ms = {sec: W93.M_of(W93.residues(line, sec)) for sec in W93.SECTORS}
        for hname, S in (("S0", S0), ("S0bar", S0b)):
            k = {sec: k_of(S, Ms[sec]) for sec in Ms}
            for sec in ("down", "lep", "up"):
                if not (mp.mpf(0.5) - mp.mpf(10) ** -20 <= k[sec] <= 2 + mp.mpf(10) ** -20):
                    k_ok = False
            X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            Xm = mp.matrix([[mp.mpc(complex(X[i, j])) for j in range(2)] for i in range(2)])
            Sp = S + mp.mpf("1e-6") * W93.fro(S) * Xm / W93.fro(Xm)
            dS = abs(W93.det2(Sp)) / W93.fro(Sp) ** 2
            for sec in ("down", "lep"):
                sv = svals(W93.coupling_mp(Sp, Ms[sec]))
                law_err = max(law_err, float(abs((sv[1] / sv[0]) / (k[sec] * dS) - 1)))
            pred = float(k["lep"] / k["down"])
            z = abs(math.log(pred / data)) / math.hypot(rel, a)
            rows.append({"line": [str(line[0]), str(line[1])], "Higgs": hname,
                         "k": {s: float(k[s]) for s in k}, "k_lep/k_down": pred,
                         "k_up/k_down": float(k["up"] / k["down"]), "k_up/k_lep": float(k["up"] / k["lep"]),
                         "z": z})
    out["L2"] = {"k in [1/2, 2] for every sector, line and Higgs": k_ok, "first-order law, max relative error": law_err,
                 "holds": bool(k_ok and law_err < 1e-4)}
    zs = [r["z"] for r in rows]
    out["L3"] = {"data (m_mu/m_tau)/(m_s/m_b)": data, "data relative error": rel, "allowance a": a,
                 "cases": len(rows), "within 2 sigma": sum(z <= 2 for z in zs), "within 3 sigma": sum(z <= 3 for z in zs),
                 "smallest z": min(zs), "predicted k_lep/k_down (distinct, 6 digits)":
                     sorted({round(r["k_lep/k_down"], 6) for r in rows}),
                 "holds": bool(min(zs) > 2)}
    out["rows"] = rows
    out["all cells hold"] = all(out[c]["holds"] for c in ("L1", "L2", "L3"))
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print({c: out[c]["holds"] for c in ("L1", "L2", "L3")})


if __name__ == "__main__":
    main()
