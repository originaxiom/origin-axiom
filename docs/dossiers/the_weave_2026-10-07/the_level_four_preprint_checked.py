"""W58: the level-four preprint (Barger, arXiv:2609.09262v1) checked with the record's code. The rule (W58_RULE.md) and
the transcribed claims (received/B2026_level_four_claims.json) were committed before this script.

  K1  the characters of eta that untwist rho_T to a representation of Gamma_4 = S_4, and the triplets they give
  K2  the preprint's generation lines (the T'-eigenlines) in the record's basis (the parity lines)
  K3  the selection theorem scanned over 3 <= N <= 12
  K4  every printed claim with a printed value, recomputed from its formula at tau_B (two routes for the thetas)
  K5  the double ratio and the Georgi-Jarlskog plaquette against the record's targets
  K6  the look-elsewhere: Table XIV's coverages recomputed, the anchor's own box, the product
  K7  the record's own data (Huang and Zhou 2021) at M_Z and at 10^12 GeV

The anchor's hit in K6(b) is read at t = eps^(-7/2) m_mu/m_tau from Table I (the printed 20.95 is rounded to about its
own uncertainty); its coverage does not depend on that choice.

Run: python3 the_level_four_preprint_checked.py  ->  the_level_four_preprint_checked.json beside it.
"""
import json
import math
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_higgs_and_the_generation_index as HG  # noqa: E402  (W56: rho_T in the code convention)
import the_weaves_functionals_on_tau as WF  # noqa: E402  (W51: the record's theta and eta series)

OUT = HERE / "the_level_four_preprint_checked.json"
CLAIMS = json.loads((HERE / "received" / "B2026_level_four_claims.json").read_text(encoding="utf-8"))
EPS = 14 / 75
TAU_B = 2j / math.pi * math.log(1 / EPS)
TOL = 1e-10


def thetas_two_routes(tau):
    t2, t3, t4 = (complex(x) for x in WF.thetas(tau))
    mp.mp.dps = 30
    qn = mp.exp(1j * mp.pi * tau)
    m = [complex(mp.jtheta(n, 0, qn)) for n in (2, 3, 4)]
    return (t2.real, t3.real, t4.real), max(abs(a - b) for a, b in zip((t2, t3, t4), m))


# ------------------------------------------------------------------------------------------------------------------ K1
def eta_character():
    """eta's multiplier in the code convention: eta(-1/tau) = tau^(1/2) chi(S) eta(tau), eta(tau + 1) = chi(T) eta"""
    t0 = 0.17 + 1.13j
    e0 = complex(WF.eta(t0))
    return complex(WF.eta(-1 / t0)) / (np.sqrt(t0) * e0), complex(WF.eta(t0 + 1)) / e0


def commutant_dim(*Ms):
    n = Ms[0].shape[0]
    rows = [np.kron(np.eye(n), M) - np.kron(M.T, np.eye(n)) for M in Ms]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(np.sum(s < 1e-9))


def K1():
    cS, cT = eta_character()
    found = {}
    for k in range(24):
        S, T = cS ** (-k) * HG.AS, cT ** (-k) * HG.TM
        I3 = np.eye(3)
        rel = [np.abs(S @ S - I3).max(), np.abs(np.linalg.matrix_power(S @ T, 3) - I3).max(),
               np.abs(np.linalg.matrix_power(T, 4) - I3).max()]
        if max(rel) < TOL:
            ch = sorted(int(round(4 * ((np.angle(v) / (2 * np.pi)) % 1))) % 4 for v in np.linalg.eigvals(T))
            found[k] = {"T'-charges (quarter turns)": ch,
                        "traces at S', T', S'T', T'^2": [round(float(np.trace(M).real), 9) for M in
                                                          (S, T, S @ T, T @ T)],
                        "commutant dimension": commutant_dim(S, T)}
    names = {(-1.0, 1.0, 0.0): "the cube's rotations (the preprint's 3, T-charges {0, 1, 3})",
             (1.0, -1.0, 0.0): "the standard representation (the preprint's 3', T-charges {1, 2, 3})"}
    for v in found.values():
        v["which"] = names.get(tuple(v["traces at S', T', S'T', T'^2"][:3]), "other")
    holds = (sorted(found) == [3, 15] and found[3]["T'-charges (quarter turns)"] == [0, 1, 3]
             and found[15]["T'-charges (quarter turns)"] == [1, 2, 3]
             and found[3]["which"].startswith("the cube's") and found[15]["which"].startswith("the standard")
             and all(v["commutant dimension"] == 1 for v in found.values()))
    return {"eta's multiplier (turns of chi(S), chi(T))": [float(np.angle(cS) / (2 * np.pi)),
                                                           float(np.angle(cT) / (2 * np.pi))],
            "the k with chi_eta^(-k) rho_T a representation of Gamma_4": {str(k): v for k, v in found.items()},
            "holds": bool(holds)}, cS, cT


# ------------------------------------------------------------------------------------------------------------------ K2
def perm_pattern(M):
    """row i -> the column of its one nonzero entry (F(gamma tau)_i is a multiple of F(tau)_j)"""
    return [int(np.argmax(np.abs(M[i, :]))) for i in range(M.shape[0])]


def K2(cS, cT):
    S, T = cS ** -3 * HG.AS, cT ** -3 * HG.TM
    w, V = np.linalg.eig(T)
    ch = [int(round(4 * ((np.angle(x) / (2 * np.pi)) % 1))) % 4 for x in w]
    order = {0: "generation 3", 1: "generation 2", 3: "generation 1"}
    lines = {}
    for c, v in zip(ch, V.T):
        v = v / np.linalg.norm(v)
        lines[order[c]] = {"T'-charge": c, "|components| on the parity lines": [round(float(x), 12) for x in np.abs(v)],
                           "a parity line": bool(np.max(np.abs(v)) > 1 - 1e-12)}
    g3, g2, g1 = lines["generation 3"], lines["generation 2"], lines["generation 1"]
    r = 1 / math.sqrt(2)
    mixed = all(np.allclose(g["|components| on the parity lines"], [r, 0, r], atol=1e-12) for g in (g1, g2))
    # the slots: the patterns of rho_T against those of (theta4^2, theta2^2, theta3^2) under tau -> tau + 1, -1/tau
    t0 = 0.17 + 1.13j

    def vec(t):
        a2, a3, a4 = (complex(x) for x in WF.thetas(t))
        return np.array([a4 ** 2, a2 ** 2, a3 ** 2])

    tpat = [int(np.argmin([abs(vec(t0 + 1)[i] - p * vec(t0)[j]) for j in range(3) for p in (1, -1, 1j, -1j)]) // 4)
            for i in range(3)]
    spat = [int(np.argmin([abs(vec(-1 / t0)[i] - p * t0 * vec(t0)[j]) for j in range(3) for p in (1, -1, 1j, -1j)])
                // 4) for i in range(3)]
    slots = {"rho_T(T) pattern": perm_pattern(HG.TM), "rho_T(S) pattern": perm_pattern(HG.AS),
             "(theta4^2, theta2^2, theta3^2) under tau + 1": tpat, "under -1/tau": spat}
    slots_agree = slots["rho_T(T) pattern"] == tpat and slots["rho_T(S) pattern"] == spat
    holds = (g3["a parity line"] and g3["|components| on the parity lines"][1] > 1 - 1e-12 and mixed
             and not g2["a parity line"] and not g1["a parity line"] and slots_agree)
    U = np.array([V[:, ch.index(c)] / np.linalg.norm(V[:, ch.index(c)]) for c in (3, 1, 0)]).T
    return {"the preprint's generation lines in the record's basis": lines,
            "the slot check (patterns)": slots, "the slots agree with W50's pairing": bool(slots_agree),
            "|S'| in the preprint's basis (generations 1, 2, 3)": np.round(np.abs(U.conj().T @ S @ U), 12).tolist(),
            "holds": bool(holds)}


# ------------------------------------------------------------------------------------------------------------------ K3
def K3():
    sols = {}
    for N in range(3, 13):
        out = []
        for a1 in range(N):
            a = (a1, a1 + 2, a1 + 3)
            if a[2] >= N:
                continue
            for c in range(N):
                b = [(x + c) % N for x in a]
                if b[1] - b[0] == -2 and b[2] - b[1] == 1:
                    out.append({"a": list(a), "c": c, "b": b})
        if out:
            sols[N] = out
    at4 = sols.get(4, [])
    char_shift = [s["c"] for s in at4 if (-s["c"]) % 4 in (0, 2)]
    holds = (sorted(sols) == [4] and sorted(s["c"] for s in at4) == [2, 3]
             and all(s["a"] == [0, 2, 3] for s in at4) and char_shift == [2])
    return {"levels with a solution": sorted(sols), "the solutions at N = 4": at4,
            "the shifts that are a character of S4 (T-charge 0 or 2)": char_shift, "holds": bool(holds)}


# ------------------------------------------------------------------------------------------------------------------ K4
def table_one():
    t = CLAIMS["Table I (MS-bar at M_Z, the preprint's Ref. [4]; masses in GeV)"]
    return t["value"], t["v_GeV"]


def closed_ckm(s12, s23, s13, d):
    c12, c23, c13 = (math.sqrt(1 - s * s) for s in (s12, s23, s13))
    e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e],
                     [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])


def predictions():
    (t2, t3, t4), route_gap = thetas_two_routes(TAU_B)
    y = TAU_B.imag
    m, v = table_one()
    eps = EPS
    mt = y ** -0.5 * v / math.sqrt(2)
    mc = 2 ** 1.5 * eps ** 4 * t3 * mt
    mu = 4 * eps ** 8 * t3 ** 3 * mt
    ms = 0.5 * m["mu"] * y ** 0.5
    md = m["e"] / eps * y ** 0.5
    mb = m["tau"] / math.sqrt(2 * eps)
    vus = math.sqrt(md / ms)
    r = 2 * math.sqrt(mu / mc)
    vub = 0.5 * t3 ** 2 * eps ** 3
    vcb = vub / r
    vtd = vcb ** 1.5
    s12, s23, s13 = vus, vcb, vub
    c12, c23, c13 = (math.sqrt(1 - s * s) for s in (s12, s23, s13))
    cosd = ((s12 * s23) ** 2 + (c12 * c23 * s13) ** 2 - vtd ** 2) / (2 * s12 * s23 * c12 * c23 * s13)
    d = math.acos(cosd)
    V = closed_ckm(s12, s23, s13, d)
    J = c12 * c23 * c13 ** 2 * s12 * s23 * s13 * math.sin(d)
    Rb = abs(V[0, 0] * np.conj(V[0, 2])) / abs(V[1, 0] * np.conj(V[1, 2]))
    Rt = abs(V[2, 0] * np.conj(V[2, 2])) / abs(V[1, 0] * np.conj(V[1, 2]))
    gam = math.acos((1 + Rb ** 2 - Rt ** 2) / (2 * Rb))
    bet = math.acos((1 + Rt ** 2 - Rb ** 2) / (2 * Rt))
    p12u, p23u = 1 / (16 * math.sqrt(2) * t3 ** 2), 1 / (4 * t3 ** 3 * y ** 0.5)
    p12d, p23d = 2 / eps, math.sqrt(eps * y / 2)
    deg = 180 / math.pi
    P = {"theta2": t2, "theta3": t3, "theta4": t4, "Im tau": y,
         "Eq. 21a": eps ** -3.5 / (2 * t3) ** 4, "Eq. 21b": eps ** -5 / (2 * t3) ** 4, "Eq. 22": eps ** 1.5,
         "Eq. 25": 1 / math.sqrt(2 * eps), "Eq. 25 exact": math.sqrt(2) / t2, "Eq. 26": 2 / eps, "P4": y ** -0.5,
         "Table VII m_t": mt, "Table VII m_b": mb, "Table VII m_c": mc, "Table VII m_s": 1e3 * ms,
         "Table VII m_d": 1e3 * md, "Table VII m_u": 1e3 * mu,
         "Eq. 28": vus, "Eq. 29": r, "Eq. 30": vub, "Eq. 31": vcb, "Eq. 32": vtd, "Eq. 33": d, "Eq. 34": t2 / 2,
         "Table VIII J": J, "Table IX A": vcb / vus ** 2, "Table IX R_b": Rb, "Table IX R_t": Rt,
         "Table IX beta": bet * deg, "Table IX gamma": gam * deg, "Table IX alpha": 180 - (bet + gam) * deg,
         "Table IX rho-bar": Rb * math.cos(gam), "Table IX eta-bar": Rb * math.sin(gam),
         "Eq. 40": vcb * vub / (vus * vtd), "Eq. 44": t2 ** 2 * m["mu"] / (2 * m["tau"]), "Eq. 46": 0.5 * t4,
         "Eq. 43": m["mu"] / (2 * m["tau"]), "Sec. III D": 2 * y ** -0.5, "Sec. III D m_u/m_d": mu / md,
         "Eq. 49 ratios": [math.log(p12u) / math.log(p23u), math.log(p12d) / math.log(p23d)],
         "Sec. III C": 1 / p23d}
    extra = {"the two theta routes' largest difference": route_gap, "P12_UD": p12u, "P23_UD": p23u,
             "P12_DL": p12d, "P23_DL": p23d, "|V_td| from the closed matrix": float(abs(V[2, 0])),
             "u = (tau - i)/(tau + i)": abs((TAU_B - 1j) / (TAU_B + 1j)),
             "Eq. 23 (Table I's leptons)": (m["e"] * m["tau"] / m["mu"] ** 2) ** (2 / 3),
             "m_c and m_u (MeV) from Table I's measured m_t instead (a read-out)":
                 [1e3 * 2 ** 1.5 * eps ** 4 * t3 * m["t"], 1e3 * 4 * eps ** 8 * t3 ** 3 * m["t"]]}
    return P, extra


def printed_numbers(s):
    out = []
    for tok in s.replace(",", " ").split():
        try:
            float(tok)
        except ValueError:
            continue
        mant = tok.lower().split("e")[0]
        dec = len(mant.split(".")[1]) if "." in mant else 0
        exp = int(tok.lower().split("e")[1]) if "e" in tok.lower() else 0
        out.append((float(tok), 10.0 ** (exp - dec)))
    return out


def K4():
    P, extra = predictions()
    printed = dict(CLAIMS["the printed claims (formula; printed value)"])
    th = CLAIMS["the constants as printed"]["theta2, theta3, theta4"]
    printed.update({"theta2": [0, str(th[0])], "theta3": [0, str(th[1])], "theta4": [0, str(th[2])],
                    "Im tau": [0, "1.0685"]})
    rows, fails = {}, []
    for key, (_, pv) in printed.items():
        nums = printed_numbers(pv)
        if not nums:
            continue
        comp = P[key] if isinstance(P[key], list) else [P[key]]
        ok = len(comp) == len(nums) and all(abs(c - n) <= u * (1 + 1e-9) + 1e-15 for c, (n, u) in zip(comp, nums))
        rows[key] = {"printed": pv, "computed": comp, "within one unit of the last printed digit": bool(ok)}
        if not ok:
            fails.append(key)
    holds = not fails and extra["the two theta routes' largest difference"] < 1e-12
    return {"claims checked": len(rows), "the claims that do not reproduce": fails, "rows": rows, "extra": extra,
            "holds": bool(holds)}, P


# ------------------------------------------------------------------------------------------------------------------ K5
def ratio_err(v, s, num, den):
    r = np.prod([v[k] for k in num]) / np.prod([v[k] for k in den])
    return r, r * math.sqrt(sum((s[k] / v[k]) ** 2 for k in num + den))


def hz(name):
    d = json.loads((HERE / "received" / name).read_text(encoding="utf-8"))["masses_GeV"]
    return d["value"], d["sigma"]


def K5(P):
    t = json.loads((HERE / "received" / "AHS2026_double_ratio.json").read_text(encoding="utf-8"))
    tv, ts = t["the double ratio"]["value"], t["the double ratio"]["sigma"]
    own = t["the record's own value (HZ2021 at M_Z, W53's data; arithmetic)"]
    dr = 2 / EPS
    v, s = hz("HZ2021_running_masses_MZ.json")
    gj, gje = ratio_err(v, s, ["b", "mu"], ["s", "tau"])
    out = {"the preprint's double ratio 2/eps": dr,
           "pull against the target (10.58 +- 0.11)": (tv - dr) / ts,
           "pull against the record's own value": (own["value"] - dr) / own["sigma"],
           "the preprint's GJ plaquette (2/(eps Im tau))^(1/2)": P["Sec. III C"],
           "the record's GJ plaquette at M_Z (value, sigma)": [gj, gje],
           "pull of the plaquette on the record's data": (gj - P["Sec. III C"]) / gje}
    out["holds"] = bool(abs(out["pull against the target (10.58 +- 0.11)"]) <= 2
                        and abs(out["pull of the plaquette on the record's data"]) <= 2)
    return out


# ------------------------------------------------------------------------------------------------------------------ K6
def prefactors(kmax, bmax, t3, t4, y):
    return [k / 2 * math.log(2) + b * math.log(t3) + c * math.log(t4) + w / 2 * math.log(y)
            for k in range(-kmax, kmax + 1) for b in range(bmax + 1) for c in (0, 1) for w in (-1, 0, 1)]


def coverage(t, sig, prefs):
    lt, step = math.log(t), 0.5 * math.log(EPS)
    lo, hi = lt - 3, lt + 3
    iv, hits = [], 0
    for p in prefs:
        n_lo = math.ceil((hi + sig - p) / step) - 1
        n_hi = math.floor((lo - sig - p) / step) + 1
        for n in range(min(n_lo, n_hi), max(n_lo, n_hi) + 1):
            f = p + n * step
            if lo - sig <= f <= hi + sig:
                iv.append((max(lo, f - sig), min(hi, f + sig)))
            if abs(f - lt) <= sig:
                hits += 1
    iv.sort()
    tot, cur = 0.0, None
    for a, b in iv:
        if b <= a:
            continue
        if cur is None or a > cur[1]:
            if cur is not None:
                tot += cur[1] - cur[0]
            cur = [a, b]
        else:
            cur[1] = max(cur[1], b)
    if cur is not None:
        tot += cur[1] - cur[0]
    return tot / (hi - lo), hits


def K6(P):
    t3, t4, y = P["theta3"], P["theta4"], P["Im tau"]
    fam = {"declared": [k / 2 * math.log(2) for k in range(-2, 3)],
           "form-value": prefactors(3, 3, t3, t4, y), "the anchor's box": prefactors(8, 4, t3, t4, y)}
    tab = CLAIMS["Table XIV as printed (target, relative uncertainty, declared-family hits and coverage, "
                 "form-value hits / coverage)"]
    rows, ok_a = {}, True
    for key, (t, sig, dh, dc, fh, fc) in tab.items():
        cd, hd = coverage(t, sig, fam["declared"])
        cf, hf = coverage(t, sig, fam["form-value"])
        good = all((c > 0 and c / p <= 1.5 and p / c <= 1.5) if p < 0.5 else abs(c - p) <= 0.1
                   for c, p in ((cd, dc), (cf, fc)))
        ok_a &= good
        rows[key] = {"declared (coverage, hits) computed": [cd, hd], "declared (coverage, hits) printed": [dc, dh],
                     "form-value (coverage, hits) computed": [cf, hf], "form-value (coverage, hits) printed": [fc, fh],
                     "reproduces": bool(good)}
    m, _ = table_one()
    t_anchor = EPS ** -3.5 * m["mu"] / m["tau"]
    ca, ha = coverage(t_anchor, 0.0002, fam["the anchor's box"])
    _, h_in_fv = coverage(t_anchor, 0.0002, fam["form-value"])
    own = math.log(2 ** 4 * t3 ** 4)
    in_box = any(abs(p - own) < 1e-12 for p in fam["the anchor's box"])
    in_fv = any(abs(p - own) < 1e-12 for p in fam["form-value"])
    prod_fv = ca * np.prod([rows[k]["form-value (coverage, hits) computed"][0]
                            for k in ("P1 m_b/m_tau", "P2 |V_us|^2 m_mu/m_e", "P4 y_t")])
    prod_decl = np.prod([r["declared (coverage, hits) computed"][0] for r in rows.values()])
    out = {"(a) Table XIV recomputed": rows, "(a) holds": bool(ok_a),
           "(b) the anchor's target eps^(-7/2) m_mu/m_tau": t_anchor,
           "(b) (2 theta3)^4 in the form-value box / in the anchor's box": [bool(in_fv), bool(in_box)],
           "(b) the anchor's box: prefactors, coverage at 0.02%, hits": [len(fam["the anchor's box"]), ca, ha],
           "(b) hits in the form-value box": h_in_fv,
           "(c) the product (the anchor's box, then the form-value family)": float(prod_fv),
           "the declared family's product (the text's 1e-6)": float(prod_decl)}
    out["holds"] = bool(ok_a and ca >= 0.10 and prod_fv >= 0.01 and in_box and not in_fv)
    return out


# ------------------------------------------------------------------------------------------------------------------ K7
def eps_tau(v):
    e = (v["e"] * v["tau"] / v["mu"] ** 2) ** (2 / 3)
    tau = 2j / math.pi * math.log(1 / e)
    (t2, t3, t4), _ = thetas_two_routes(tau)
    return e, tau.imag, t2, t3, t4


def K7():
    v, s = hz("HZ2021_running_masses_MZ.json")
    e, y, t2, t3, t4 = eps_tau(v)
    vf = 246.0
    rows = {}
    r, re_ = ratio_err(v, s, ["tau"], ["mu"])
    rows["the anchor m_tau/m_mu"] = (r - e ** -3.5 / (2 * t3) ** 4) / re_
    yt, yte = math.sqrt(2) * v["t"] / vf, math.sqrt(2) * s["t"] / vf
    rows["y_t"] = (yt - y ** -0.5) / yte
    rel_t = s["t"] / v["t"]
    pred = {"b": (v["tau"] / math.sqrt(2 * e), 0.0), "c": (2 ** 1.5 * e ** 4 * t3 * v["t"], rel_t),
            "s": (0.5 * v["mu"] * y ** 0.5, 0.0), "d": (v["e"] / e * y ** 0.5, 0.0),
            "u": (4 * e ** 8 * t3 ** 3 * v["t"], rel_t)}
    for q, (p, rel) in pred.items():
        rows["m_" + q] = (v[q] - p) / math.hypot(s[q], p * rel)
    a = {"eps, Im tau from the record's leptons": [e, y], "pulls (data - preprint) / sigma": rows,
         "holds": bool(all(abs(x) <= 2 for x in rows.values()))}
    v12, s12 = hz("HZ2021_running_masses_1e12.json")
    e12, y12, *_ = eps_tau(v12)
    bt, bte = ratio_err(v12, s12, ["b"], ["tau"])
    dr, dre = ratio_err(v12, s12, ["mu", "d"], ["s", "e"])
    b = {"eps, Im tau at 1e12 GeV": [e12, y12],
         "P1: m_b/m_tau (value, sigma) and (2 eps)^(-1/2)": [bt, bte, 1 / math.sqrt(2 * e12)],
         "P1 pull": (bt - 1 / math.sqrt(2 * e12)) / bte,
         "the double ratio (value, sigma) and 2/eps": [dr, dre, 2 / e12], "double-ratio pull": (dr - 2 / e12) / dre}
    b["holds"] = bool(abs(b["P1 pull"]) > 5 and abs(b["double-ratio pull"]) <= 2)
    return {"(a) at M_Z": a, "(b) at 1e12 GeV": b, "holds": bool(a["holds"] and b["holds"])}


def main():
    k1, cS, cT = K1()
    k4, P = K4()
    out = {"status": "W58: the level-four preprint checked (the rule W58_RULE.md and the claims file first; one run)",
           "K1": k1, "K2": K2(cS, cT), "K3": K3(), "K4": k4, "K5": K5(P), "K6": K6(P), "K7": K7()}
    out["cells"] = {k: out[k]["holds"] for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
