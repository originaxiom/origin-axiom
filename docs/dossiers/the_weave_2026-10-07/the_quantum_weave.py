#!/usr/bin/env python3
"""W125 — the quantum weave of closed universes (the script; `W125_RULE.md` was committed and pushed before it).

W122's 42 threads (b++w and b+-w over the primitive cyclic words w in L and R with both letters, of length 2 to 6),
each Dehn filled at every primitive slope (p, q) up to sign with Q = |p + q tau|^2 / Im tau <= 16 000, tau the cusp's
shape lambda/mu in SnapPy's own basis. A filling is certified when its solution type is "all tetrahedra positively
oriented" and its volume is below its bundle's; for Q <= 200 its volume must also agree at high precision within 1e-9.

    K0  the instrument          K1  Neumann-Zagier's volume      K2  the core's length
    K3  the lattice (each cusp shape): Epstein's E(tau, 0) = 1, the 3/pi log coefficient, Stanford-Yan's (3.30)
    K4  the remainder after the universal divergence converges     K5  read-outs (the towers' finite parts)

    python3 -B the_quantum_weave.py      # writes the_quantum_weave.json and the_quantum_weave_run.txt beside itself
"""
import json
import math
import multiprocessing as mp
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
XMAX = 16000.0                       # the fillings' bound on Q
XLAT = 20000.0                       # the lattice sums' bound on Q
EPS = (0.016, 0.008, 0.004, 0.002)
SS = (0.5, 1.0, 2.0, 4.0)
POS = "all tetrahedra positively oriented"
EULER = 0.5772156649015329
log = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    log.append(s)


def lyndon(n):
    res = []
    for k in range(2 ** n):
        w = "".join("R" if (k >> i) & 1 else "L" for i in range(n))
        rots = [w[i:] + w[:i] for i in range(n)]
        if "L" in w and "R" in w and w == min(rots) and len(set(rots)) == n:
            res.append(w)
    return res


WORDS = [w for n in range(2, 7) for w in lyndon(n)]
BUNDLES = [p + w for w in WORDS for p in ("b++", "b+-")]


def slopes(tau, X, primitive=True):
    """every (p, q) with Q <= X: primitive up to sign (q > 0, or q = 0 and p = 1), or the full lattice minus 0"""
    x, y = tau.real, tau.imag
    qmax = int(math.floor(math.sqrt(X / y))) + 1
    P, Qs = [], []
    for q in range((0 if primitive else -qmax), qmax + 1):
        r2 = X * y - (q * y) ** 2
        if r2 < 0:
            continue
        r = math.sqrt(r2)
        lo, hi = int(math.floor(-q * x - r)) - 1, int(math.ceil(-q * x + r)) + 1
        p = np.arange(lo, hi + 1)
        if primitive:
            if q == 0:
                p = np.array([1])
            else:
                p = p[np.gcd(np.abs(p), q) == 1]
        elif q == 0:
            p = p[p != 0]
        Q = ((p + q * x) ** 2 + (q * y) ** 2) / y
        keep = Q <= X
        P.extend((int(a), q) for a in p[keep])
        Qs.extend(Q[keep].tolist())
    return P, np.array(Qs)


def log_abs_eta(tau):
    """log|eta(tau)|, by the q-series after reducing tau to the fundamental domain (sqrt(y)|eta|^2 is invariant;
    the caller uses that combination only)"""
    z = complex(tau)
    for _ in range(200):
        z = complex(z.real - round(z.real), z.imag)
        if abs(z) < 1 - 1e-15:
            z = -1 / z
        else:
            break
    q = np.exp(2j * np.pi * z)
    n = np.arange(1, 400)
    return -np.pi * z.imag / 12 + float(np.sum(np.log(np.abs(1 - q ** n)))), z


def fill_bundle(b):
    import snappy
    M = snappy.Manifold(b)
    Vb = float(M.volume())
    tau = complex(M.cusp_info()[0]["shape"])
    if tau.imag < 0:                 # Q is unchanged under conjugation; the slope list is the same
        tau = tau.conjugate()
    sl, Q = slopes(tau, XMAX)
    st, V, ell, hp = [], [], [], []
    for (p, q), Qv in zip(sl, Q):
        try:
            N = snappy.Manifold(b)
            N.dehn_fill((p, q))
            s = N.solution_type()
            v = float(N.volume()) if s == POS else float("nan")
            c = float(complex(N.cusp_info()[0]["core_length"]).real) if s == POS else float("nan")
            ok = True
            if s == POS and Qv <= 200:
                ok = abs(float(N.high_precision().volume()) - v) < 1e-9
            st.append(s if ok else s + " (high precision disagrees)")
            V.append(v)
            ell.append(c)
            hp.append(ok)
        except Exception as e:  # recorded, not hidden
            st.append("error: " + repr(e)[:80])
            V.append(float("nan"))
            ell.append(float("nan"))
            hp.append(False)
    return {"bundle": b, "volume": Vb, "shape": [tau.real, tau.imag], "slopes": sl, "Q": Q.tolist(),
            "solution": st, "V": V, "core": ell, "hp": hp}


def analyse(r, w122):
    b, Vb = r["bundle"], r["volume"]
    tau = complex(*r["shape"])
    Q, V, ell = np.array(r["Q"]), np.array(r["V"]), np.array(r["core"])
    cert = np.array([s == POS for s in r["solution"]]) & np.isfinite(V) & (V < Vb)
    out = {"bundle": b, "volume": Vb, "shape": r["shape"], "slopes": len(Q), "certified": int(cert.sum())}
    # K0
    out["K0 volume vs W122"] = abs(Vb - w122[b]["volume"])
    out["K0 count / (3/pi) XMAX"] = len(Q) / (3 / math.pi * XMAX)
    unc = [[r["slopes"][i][0], r["slopes"][i][1], round(float(Q[i]), 3), r["solution"][i]]
           for i in np.nonzero(~cert)[0]]
    out["uncertified"] = unc
    out["uncertified with Q > 60"] = [u for u in unc if u[2] > 60]
    i0 = int(np.nanargmin(np.where(cert, V, np.inf)))
    out["least certified"] = [r["slopes"][i0], float(V[i0])]
    # K1, K2
    big = cert & (Q >= 400)
    k1 = np.abs(Q[big] * (Vb - V[big]) / math.pi ** 2 - 1)
    k2 = np.abs(Q[big] * ell[big] / (2 * math.pi) - 1)
    out["K1 worst |Q dV/pi^2 - 1| at Q >= 400"] = float(k1.max())
    out["K1 worst slope"] = r["slopes"][int(np.nonzero(big)[0][int(k1.argmax())])]
    out["K2 worst |Q l/2pi - 1| at Q >= 400"] = float(k2.max())
    out["K2 worst slope"] = r["slopes"][int(np.nonzero(big)[0][int(k2.argmax())])]
    mid = cert & (Q >= 100) & (Q <= 1000)
    out["second-order coefficient (median of Q(Q dV/pi^2 - 1), Q in [100, 1000])"] = float(
        np.median(Q[mid] * (Q[mid] * (Vb - V[mid]) / math.pi ** 2 - 1)))
    # K3: the lattice, from the cusp shape alone
    _, Qp = slopes(tau, XLAT)
    _, Qf = slopes(tau, XLAT, primitive=False)
    F = {e: float(np.sum(np.exp(-e * Qp))) - 3 / (math.pi * e) for e in EPS}
    G = {e: float(np.sum(np.exp(-e * Qp) / Qp)) for e in EPS}
    H = {e: float(np.sum(np.exp(-e * Qf) / Qf)) / (2 * math.pi) - 0.5 * math.log(1 / e) for e in EPS}
    le, zf = log_abs_eta(tau)
    kron = EULER / 2 - math.log(2) - (0.5 * math.log(zf.imag) + 2 * le)
    out["K3 F"] = F
    out["K3a 2F(0.002) - F(0.004)"] = 2 * F[0.002] - F[0.004]
    out["K3 G"] = G
    out["K3b (G(0.002) - G(0.004)) / ((3/pi) log 2)"] = (G[0.002] - G[0.004]) / (3 / math.pi * math.log(2))
    out["K3 H"] = H
    out["K3c 2H(0.002) - H(0.004)"] = 2 * H[0.002] - H[0.004]
    out["K3c Stanford-Yan (3.30) value"] = kron
    out["lattice counts (primitive, full)"] = [len(Qp), len(Qf)]
    # K4, K5: the towers
    Qc, dV = Q[cert], Vb - V[cert]
    Delta, fin, rich = {}, {}, {}
    for s in SS:
        for e in EPS:
            w = np.exp(-e * Qc)
            Delta[f"{s} {e}"] = float(np.sum(w * (np.exp(s * dV) - np.exp(s * math.pi ** 2 / Qc))))
            fin[f"{s} {e}"] = float(np.sum(w * np.exp(s * dV))) - 3 / (math.pi * e) - 3 * math.pi * s * math.log(1 / e)
        rich[str(s)] = 2 * fin[f"{s} 0.002"] - fin[f"{s} 0.004"]
    out["K4 Delta(s, eps)"] = Delta
    out["K4 |Delta(s, 0.002) - Delta(s, 0.004)| for s = 1/2, 1, 2"] = [
        abs(Delta[f"{s} 0.002"] - Delta[f"{s} 0.004"]) for s in (0.5, 1.0, 2.0)]
    out["K4 bare change e^{sV}Z(0.002) - e^{sV}Z(0.004) for s = 1/2, 1, 2"] = [
        fin[f"{s} 0.002"] - fin[f"{s} 0.004"] + 3 / (math.pi * 0.002) - 3 / (math.pi * 0.004)
        + 3 * math.pi * s * math.log(2) for s in (0.5, 1.0, 2.0)]
    out["fin(s, eps)"] = fin
    out["fin Richardson"] = rich
    fin_or_none = lambda x: float(x) if math.isfinite(x) else None
    out["rows with Q <= 100"] = [[r["slopes"][i], round(float(Q[i]), 4), r["solution"][i], fin_or_none(V[i]),
                                  fin_or_none(ell[i])]
                                 for i in np.nonzero(Q <= 100)[0]]
    return out


def main():
    w122 = json.loads((HERE / "the_closed_universes.json").read_text(encoding="utf-8"))["census"]["bundles"]
    say("W125: census", len(WORDS), "words,", len(BUNDLES), "bundles; fillings to Q <=", XMAX, "; lattice to", XLAT)
    with mp.Pool(4) as pool:
        raw = pool.map(fill_bundle, BUNDLES, chunksize=1)
    res = []
    for r in raw:
        a = analyse(r, w122)
        res.append(a)
        say(a["bundle"], "vol %.6f" % a["volume"], "slopes", a["slopes"], "cert", a["certified"],
            "K1 %.4f" % a["K1 worst |Q dV/pi^2 - 1| at Q >= 400"], "K2 %.4f" % a["K2 worst |Q l/2pi - 1| at Q >= 400"],
            "K3a %.4f" % a["K3a 2F(0.002) - F(0.004)"], "K3b %.4f" % a["K3b (G(0.002) - G(0.004)) / ((3/pi) log 2)"],
            "K3c %.4f vs %.4f" % (a["K3c 2H(0.002) - H(0.004)"], a["K3c Stanford-Yan (3.30) value"]),
            "K4", [round(x, 4) for x in a["K4 |Delta(s, 0.002) - Delta(s, 0.004)| for s = 1/2, 1, 2"]])
    by = {a["bundle"]: a for a in res}
    least = min(res, key=lambda a: a["least certified"][1])
    K0 = {"(a) max |V_b - W122|": max(a["K0 volume vs W122"] for a in res),
          "(b) count ratios (min, max)": [min(a["K0 count / (3/pi) XMAX"] for a in res),
                                          max(a["K0 count / (3/pi) XMAX"] for a in res)],
          "(c) uncertified with Q > 60": {a["bundle"]: a["uncertified with Q > 60"] for a in res
                                          if a["uncertified with Q > 60"]},
          "(d) least certified": [least["bundle"], least["least certified"]]}
    K0["holds"] = (K0["(a) max |V_b - W122|"] < 1e-9 and 0.99 <= K0["(b) count ratios (min, max)"][0]
                   and K0["(b) count ratios (min, max)"][1] <= 1.01 and not K0["(c) uncertified with Q > 60"]
                   and least["bundle"] == "b+-LR" and abs(least["least certified"][1] - 0.9427073628) < 1e-8)
    K1 = {"worst": max(a["K1 worst |Q dV/pi^2 - 1| at Q >= 400"] for a in res)}
    K1["holds"] = K1["worst"] <= 0.02
    K2 = {"worst": max(a["K2 worst |Q l/2pi - 1| at Q >= 400"] for a in res)}
    K2["holds"] = K2["worst"] <= 0.02
    K3 = {"(a) worst |2F(0.002) - F(0.004) - 1|": max(abs(a["K3a 2F(0.002) - F(0.004)"] - 1) for a in res),
          "(b) worst |ratio - 1|": max(abs(a["K3b (G(0.002) - G(0.004)) / ((3/pi) log 2)"] - 1) for a in res),
          "(c) worst |2H(0.002) - H(0.004) - SY|": max(abs(a["K3c 2H(0.002) - H(0.004)"]
                                                           - a["K3c Stanford-Yan (3.30) value"]) for a in res)}
    K3["holds"] = (K3["(a) worst |2F(0.002) - F(0.004) - 1|"] <= 0.01 and K3["(b) worst |ratio - 1|"] <= 0.01
                   and K3["(c) worst |2H(0.002) - H(0.004) - SY|"] <= 0.01)
    K4 = {"worst |Delta(0.002) - Delta(0.004)|": max(max(a["K4 |Delta(s, 0.002) - Delta(s, 0.004)| for s = 1/2, 1, 2"])
                                                       for a in res),
          "bare change (min, max)": [min(min(a["K4 bare change e^{sV}Z(0.002) - e^{sV}Z(0.004) for s = 1/2, 1, 2"])
                                         for a in res),
                                     max(max(a["K4 bare change e^{sV}Z(0.002) - e^{sV}Z(0.004) for s = 1/2, 1, 2"])
                                         for a in res)]}
    K4["holds"] = K4["worst |Delta(0.002) - Delta(0.004)|"] < 0.5
    # K5: the renormalized ensemble (this scheme: e^{-eps Q}, the universal terms subtracted at eps = 0.002)
    weeks = by["b+-LR"]["least certified"][1]
    K5 = {}
    for s in SS:
        terms = {a["bundle"]: math.exp(-s * a["volume"]) * a["fin(s, eps)"][f"{s} 0.002"] for a in res}
        terms_r = {a["bundle"]: math.exp(-s * a["volume"]) * a["fin Richardson"][str(s)] for a in res}
        Z = sum(terms.values())
        Zr = sum(terms_r.values())
        rank = sorted(terms, key=lambda k: -abs(terms[k]))
        K5[str(s)] = {"Z_ren (eps = 0.002)": Z, "Z_ren (Richardson)": Zr,
                      "leading threads (by |term|), with shares": [[k, terms[k] / Z] for k in rank[:6]],
                      "the Weeks term's share e^{-s V_Weeks} / Z_ren": math.exp(-s * weeks) / Z,
                      "the cusped ensemble sum_b e^{-s V_b}": sum(math.exp(-s * a["volume"]) for a in res)}
        lead = K5[str(s)]["leading threads (by |term|), with shares"][:3]
        say("K5 s =", s, "Z_ren %.6g" % Z, "(Richardson %.6g)" % Zr, "leading", [[k, round(v, 4)] for k, v in lead],
            "Weeks share %.4g" % K5[str(s)]["the Weeks term's share e^{-s V_Weeks} / Z_ren"])
    verdict = {"K0": K0["holds"], "K1": K1["holds"], "K2": K2["holds"], "K3": K3["holds"], "K4": K4["holds"]}
    say("K0", K0)
    say("K1", K1, "| K2", K2)
    say("K3", K3)
    say("K4", K4)
    say("verdict", verdict)
    out = {"arc": "W125", "rule": "W125_RULE.md", "census": {"words": WORDS, "bundles": BUNDLES, "XMAX": XMAX,
                                                             "XLAT": XLAT, "eps": EPS, "s": SS},
           "K0": K0, "K1": K1, "K2": K2, "K3": K3, "K4": K4, "K5": K5, "per bundle": res, "verdict": verdict}
    (HERE / "the_quantum_weave.json").write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    (HERE / "the_quantum_weave_run.txt").write_text("\n".join(log) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
