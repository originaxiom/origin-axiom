#!/usr/bin/env python3
"""W166 — the plan's stage 3, the Higgs from the same action (the rule: W166_RULE.md, committed and pushed before this
script).  Each doublet is the response of the matter's induced one-loop form to the record's DR, H = K^-1 DR, type II:
H_u = K_up^-1 DR and H_d = (3 K_down + K_lep)^-1 DR, with K_s the Hermitian form of ||Y_s(h)||^2 in the row's reading
(S: G = tr(B_c^dag B_d); S~: conj of the same from the S~ basis), on W158's raw basis couplings.

Two parts, each run once, from the repository root:

  V  the vectors, blind: the 38 rows read from W156's and W157's committed outputs; no target file is read (every
     git read is logged); the rule's pair and the table's pairs at every row, B1762's recipes at B1757's four points;
     the vector block frozen by its sha256
  S  the score: the frozen block checked by its git blob and hash and recomputed; then the targets, and
     K0  the instrument (pins, rows, the form identity, the record's DR against the stored six)
     K1  the vectors frozen and blind, with the counterfactual
     K2  chi2_nine below 21.67 at some row
     K3  specificity at 1% under both nulls (decisive only if K2 holds)
     K4  B1762's boost as the inverse up form at the four points
     R   read-outs, the sensitivity table priced

    python3 -B docs/dossiers/the_weave_2026-10-07/the_higgs_from_the_action.py V
    python3 -B docs/dossiers/the_weave_2026-10-07/the_higgs_from_the_action.py S
"""
import contextlib
import hashlib
import io
import json
import math
import platform
import sys
import time
import traceback
import warnings
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with contextlib.redirect_stdout(io.StringIO()):
    import the_recipes_priced as W61         # noqa: E402  (W161: B1762's recipes; W158 and W159 under it)
W58, W59 = W61.W58, W61.W59
W57, T8, T42 = W58.W57, W58.T8, W58.T42

REV = W58.REV
DOS = "docs/dossiers/the_weave_2026-10-07/"
ROWS_FROM = {"B1749": DOS + "third_opinion_b1749.json", "B1753": DOS + "third_opinion_b1753.json"}
OUT_V = HERE / "the_higgs_from_the_action_vectors.json"
OUT_S = HERE / "the_higgs_from_the_action.json"
VREL = DOS + "the_higgs_from_the_action_vectors.json"
TARGET_FILES = (T8.HZ, T8.CKM, W61.J57, W61.J62)
SEEDS = tuple(range(1929, 1949))
BAR6, BAR9 = 16.75, 21.67
J_PDG, J_SIG = W61.J_PDG, W61.J_SIG
POINTS, LINE0 = W61.POINTS, W61.LINE0
SECTS = T8.SECTS
NC = 3
TABLE = (("T1", {"nc": 1}), ("T2", {"nc": 2}), ("T3", {"nc": 4}), ("T4", {"r": 0.0}), ("T5", {"r": 1 / 3}),
         ("T6", {"r": 3.0}), ("T7", {"norm": True}), ("T8", {"kappa": 0.0}), ("T9", {"kappa": 0.1}),
         ("T10", {"kappa": 1.0}), ("T11", {"kappa": 10.0}), ("T12", {"one": True}))
ENTRIES = ("rule",) + tuple(n for n, _ in TABLE)
_ROOT = {}
READS = []


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def git_read(root, rev, path):
    READS.append(path)
    return T8.git_bytes(root, rev, path)


# ============================================================================================ the producer
def form(B, sec, reading):
    """K with ||Y_sec(h)||_F^2 = h^dag K h in the reading: S, Y = sum h_n B_n; S~, Y = sum conj(h_n) B~_n"""
    bY = B[sec]["S"] if reading == "S" else B[sec]["St"]
    G = np.array([[np.trace(bY[c].conj().T @ bY[d]) for d in range(3)] for c in range(3)])
    return G if reading == "S" else np.conj(G)


def pair(B, tau, rd, nc=NC, r=1.0, norm=False, kappa=None, one=False):
    """(H_u, H_d) = responses of the induced forms to DR; no target enters"""
    DR = np.array(T8.higgs_DR(tau))
    K = {s: form(B, s, rd[s]) for s in SECTS}
    if norm:
        K = {s: K[s] / float(np.trace(K[s]).real) for s in SECTS}
    Ku = K["up"]
    Kd = nc * K["down"] + r * K["lep"]
    if one:
        Ku = Kd = nc * K["up"] + nc * K["down"] + r * K["lep"]

    def resp(Kx):
        if kappa is None:
            return np.linalg.solve(Kx, DR)
        Kh = 3 * Kx / float(np.trace(Kx).real)
        return np.linalg.solve(np.eye(3) + kappa * Kh, DR)

    return W61.gauge_h1(resp(Ku)), W61.gauge_h1(resp(Kd))


def all_pairs(B, tau, rd):
    out = {"rule": pair(B, tau, rd)}
    for name, kw in TABLE:
        out[name] = pair(B, tau, rd, **kw)
    return out


def enc(v):
    return [[float(z.real), float(z.imag)] for z in v]


def dec(v):
    return np.array([complex(a, b) for a, b in v])


def block_hash(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def form_info(B, tau, rd):
    K = {s: form(B, s, rd[s]) for s in SECTS}
    Kd = NC * K["down"] + K["lep"]
    info = {}
    for name, M in (("K_up", K["up"]), ("3K_down + K_lep", Kd)):
        ev = np.linalg.eigvalsh(M)
        info[name] = {"least eigenvalue": float(ev[0]), "condition": float(ev[-1] / ev[0]) if ev[0] > 0 else None,
                      "hermitian defect": float(np.linalg.norm(M - M.conj().T) / np.linalg.norm(M))}
    Ku = K["up"]
    info["K_up off-block (1 + 2) over norm"] = float(np.linalg.norm([Ku[0, 1], Ku[0, 2], Ku[1, 0], Ku[2, 0]])
                                                   / np.linalg.norm(Ku))
    info["tr K_lep / tr K_down"] = float(np.trace(K["lep"]).real / np.trace(K["down"]).real)
    info["tr K_down / tr K_up"] = float(np.trace(K["down"]).real / np.trace(K["up"]).real)
    return info


def beta(hu, DR):
    return float((abs(hu[0]) / np.linalg.norm(hu[1:])) / (abs(DR[0]) / np.linalg.norm(DR[1:])))


def rows_from_outputs(root, L):
    rows = []
    for name, path in ROWS_FROM.items():
        d = json.loads(git_read(root, "HEAD", path).decode("utf-8"))
        for r in d["C1"]["rows"]:
            k = L.index((Fr(r["line"][0]), Fr(r["line"][1])))
            rows.append({"name": name, "k": k, "x": r["Re_tau"], "y": r["Im_tau"], "hor": r["horocycle"],
                         "readings": list(r["readings"]), "c": r["c"]})
    return rows


def row_id(r):
    return f"{r['name']}|{r['k']}|{r['x']!r}|{r['y']!r}|{r['hor']}"


def rd_of(r):
    return {"up": r["readings"][0], "down": r["readings"][1], "lep": r["readings"][2]}


def frame(root):
    col_bytes = git_read(root, REV, T8.COLUMN)
    col = T8.L_column({T8.COLUMN: col_bytes})
    W93, W89 = T8.own_modules(root)
    return col, T8.sha256(col_bytes), W93, W89, T8.own_lines()


def produce(root):
    """everything part V freezes; reads only the column and the two row lists"""
    col, col_sha, W93, W89, L = frame(root)
    rows = rows_from_outputs(root, L)
    block, forms, Bs = {"rows": {}, "four points": {}}, {}, {}
    for r in rows:
        B = W58.basis(W93, W89, col, L[r["k"]], r["x"], r["y"], r["hor"])
        tau = complex(r["x"], r["y"])
        P = all_pairs(B, tau, rd_of(r))
        rid = row_id(r)
        block["rows"][rid] = {e: [enc(P[e][0]), enc(P[e][1])] for e in ENTRIES}
        forms[rid] = form_info(B, tau, rd_of(r))
        Bs[rid] = (B, tau, rd_of(r))
    k0 = L.index(LINE0)
    rd4 = {"up": "St", "down": "S", "lep": "S"}
    for (x, y) in POINTS:
        B = W58.basis(W93, W89, col, L[k0], x, y, "L_max")
        tau = complex(x, y)
        P = all_pairs(B, tau, rd4)
        rec, info, _h1, _hp = W61.recipes(B, tau)
        pid = f"{x!r}|{y!r}"
        block["four points"][pid] = {"pairs": {e: [enc(P[e][0]), enc(P[e][1])] for e in ENTRIES},
                                     "B1762": {n: [enc(a), enc(b)] for n, (a, b) in zip(W61.NAMES, rec)},
                                     "B1762 boost": float(info["boost"])}
        forms[pid] = form_info(B, tau, rd4)
        Bs[pid] = (B, tau, rd4)
    return {"rows": rows, "block": block, "forms": forms, "column sha256": col_sha, "B": Bs}


def max_diff(b1, b2):
    """largest |difference| over every stored vector of two blocks of the same shape"""
    worst = 0.0

    def walk(a, b):
        nonlocal worst
        if isinstance(a, dict):
            assert set(a) == set(b)
            for kk in a:
                walk(a[kk], b[kk])
        elif isinstance(a, list):
            assert len(a) == len(b)
            for u, v in zip(a, b):
                walk(u, v)
        else:
            worst = max(worst, abs(float(a) - float(b)))

    walk(b1, b2)
    return worst


def rebuild_block(P):
    """the block from stored bases (part S): the producer again, at fixed rows"""
    block = {"rows": {}, "four points": {}}
    for rid, (B, tau, rd) in P["B"].items():
        Q = all_pairs(B, tau, rd)
        enc_pairs = {e: [enc(Q[e][0]), enc(Q[e][1])] for e in ENTRIES}
        if rid in P["block"]["rows"]:
            block["rows"][rid] = enc_pairs
        else:
            rec, info, _h1, _hp = W61.recipes(B, tau)
            block["four points"][rid] = {"pairs": enc_pairs,
                                         "B1762": {n: [enc(a), enc(b)] for n, (a, b) in zip(W61.NAMES, rec)},
                                         "B1762 boost": float(info["boost"])}
    return block


# ============================================================================================ the score
def nine(B, rd, c, hu, hd, t9, s9):
    Y = {"up": W58.Y_of(B, "up", rd["up"], hu), "down": W58.Y_of(B, "down", rd["down"], hd),
         "lep": W58.Y_of(B, "lep", rd["lep"], hd)}
    six = []
    for s in SECTS:
        sv = np.maximum(np.linalg.svd(Y[s], compute_uv=False), 1e-300)
        six += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    six = np.array(six) + np.array([0, 0, 0, 0, math.log(c), -math.log(c)])
    Uu, _ = W58.lefts(Y["up"])
    Ud, _ = W58.lefts(Y["down"])
    v = W58.ckm_from(Uu, Ud)
    f = np.concatenate([six, np.log(np.maximum(v[:3], 1e-300))])
    return f, (f - t9) / s9, v[3], Y


def mat_angle(Y1, Y2):
    c = abs(np.vdot(Y1, Y2)) / (np.linalg.norm(Y1) * np.linalg.norm(Y2))
    return float(np.degrees(np.arccos(min(1.0, c))))


def nulls(X, obs, t6, s9):
    tree = cKDTree(X)
    fa, fb = [], []
    for s in SEEDS:
        _six, nine_d = T8.own_draws(s, T8.NTARGET)
        N = np.array(nine_d)
        Ta = np.concatenate([np.tile(t6, (len(N), 1)), N[:, 6:9]], axis=1) / s9
        Tb = N / s9
        fa.append(float(np.mean(tree.query(Ta, k=1)[0] ** 2 <= obs + 1e-9)))
        fb.append(float(np.mean(tree.query(Tb, k=1)[0] ** 2 <= obs + 1e-9)))
    return {"(a) the data's six with random mixings: fraction_mean": float(np.mean(fa)),
            "(b) random nines: fraction_mean": float(np.mean(fb)), "per seed (a)": fa, "per seed (b)": fb}


# ============================================================================================ the parts
def part_V(root, out):
    P = produce(root)
    block = P["block"]
    out["rows"] = len(P["rows"])
    out["row list"] = P["rows"]
    out["column sha256"] = P["column sha256"]
    out["files read"] = sorted(set(READS))
    out["target files read"] = sorted(set(READS) & set(TARGET_FILES))
    out["forms"] = P["forms"]
    pd = [P["forms"][row_id(r)] for r in P["rows"]]
    conds = [f[n]["condition"] for f in pd for n in ("K_up", "3K_down + K_lep")]
    out["K1 (part V)"] = {"no target file read": not out["target files read"],
                          "every rule form positive definite": all(c is not None for c in conds),
                          "largest condition number": max(c for c in conds if c is not None),
                          "rows' configurations": sorted({(tuple(r["readings"]), r["c"], r["hor"])
                                                          for r in P["rows"]})}
    out["vectors"] = block
    out["vectors sha256"] = block_hash(block)


def part_S(root, out):
    # ---------------------------------------------------------------- the frozen block, before any target
    work = OUT_V.read_bytes()
    blob = T8.git_bytes(root, "HEAD", VREL)
    V = json.loads(blob.decode("utf-8"))
    out["frozen"] = {"working file equals HEAD's blob": work == blob, "blob sha256": T8.sha256(blob),
                     "stored hash": V["vectors sha256"],
                     "hash recomputed": block_hash(V["vectors"]),
                     "part V's run failed": "run_failed" in V}
    READS.clear()
    P = produce(root)
    out["recomputed before targets: max |diff|"] = max_diff(V["vectors"], P["block"])
    out["recomputed before targets: target files read"] = sorted(set(READS) & set(TARGET_FILES))
    # ---------------------------------------------------------------- the targets
    files = {p: T8.git_bytes(root, REV, p) for p in W58.FILES}
    pins = {p: T8.sha256(files[p]) == h for p, h in W58.PIN.items()}
    t6, t9 = T8.targets(files)
    sg = T42.sigma(files)
    s9 = np.concatenate([sg, T42.sigma_ckm(files)])
    after = rebuild_block(P)
    moved = []
    for j in range(3):
        _s, nd = T8.own_draws(SEEDS[j], 1)
        t9 = np.array(nd[0])                       # a moved target: no producer argument carries it
        moved.append(max_diff(V["vectors"], rebuild_block(P)))
    t6, t9 = T8.targets(files)
    out["K1 counterfactual"] = {"after the targets are loaded: max |diff|": max_diff(V["vectors"], after),
                                "under three moved targets: max |diff|": moved}
    # ---------------------------------------------------------------- K0
    rebuilt = []
    for name, path in (("B1749", W58.V49), ("B1753", W58.V53)):
        rows = T8.census_rows(files[path + "/census.jsonl"])
        _arr, lab, best, arg = W57.below_rows(rows, t6, sg)
        for i in range(len(best)):
            if best[i] < BAR6:
                k, x, y, hor = lab[i]
                a, b, l, kk = arg[i]
                rebuilt.append((name, k, x, y, hor, (T8.RD[a], T8.RD[b], T8.RD[l]), round(math.exp(kk))))
    frozen_rows = [(r["name"], r["k"], r["x"], r["y"], r["hor"], tuple(r["readings"]), r["c"])
                   for r in V["row list"]]
    rng = np.random.default_rng(166)
    ident, six_dev = 0.0, 0.0
    stored_six = {}
    for name, path in ROWS_FROM.items():
        d = json.loads(T8.git_bytes(root, "HEAD", path).decode("utf-8"))
        for r in d["C1"]["rows"]:
            stored_six[(name, r["Re_tau"], r["Im_tau"], tuple(r["line"]))] = r["chi2_six"]
    L = T8.own_lines()
    for r in V["row list"]:
        B, tau, rd = P["B"][row_id(r)]
        for _ in range(3):
            h = rng.normal(size=3) + 1j * rng.normal(size=3)
            for s in SECTS:
                for reading in T8.RD:
                    Y = W58.Y_of(B, s, reading, h)
                    lhs = float(np.linalg.norm(Y) ** 2)
                    rhs = float(np.real(np.conj(h) @ form(B, s, reading) @ h))
                    ident = max(ident, abs(lhs / rhs - 1))
        DR = np.array(T8.higgs_DR(tau))
        _f, pulls, _J, _Y = nine(B, rd, r["c"], DR, DR, t9, s9)
        line = (str(L[r["k"]][0]), str(L[r["k"]][1]))
        ref = stored_six[(r["name"], r["x"], r["y"], line)]
        six_dev = max(six_dev, abs(float((pulls[:6] ** 2).sum()) / ref - 1))
    out["K0"] = {"pins": pins, "rows rebuilt": len(rebuilt), "rebuilt equal the frozen rows":
                 sorted(rebuilt) == sorted(frozen_rows),
                 "form identity, worst relative": ident, "the record's DR against the stored six, worst relative":
                 six_dev}
    # ---------------------------------------------------------------- the score at the 38 rows
    per_row, feats = [], {e: [] for e in ENTRIES + ("T13",)}
    c2 = {e: [] for e in feats}
    for r in V["row list"]:
        rid = row_id(r)
        B, tau, rd = P["B"][rid]
        DR = np.array(T8.higgs_DR(tau))
        stored = V["vectors"]["rows"][rid]
        rec = {"row": [r["name"], [str(q) for q in L[r["k"]]], r["x"], r["y"], r["hor"]]}
        for e in ENTRIES + ("T13",):
            hu, hd = (dec(stored["rule"][0]), dec(stored["rule"][1])) if e == "T13" else \
                (dec(stored[e][0]), dec(stored[e][1]))
            c = 1 if e == "T13" else r["c"]
            f, pulls, J, _Y = nine(B, rd, c, hu, hd, t9, s9)
            x2 = float((pulls ** 2).sum())
            feats[e].append(f / s9)
            c2[e].append(x2)
            if e == "rule":
                rec.update({"chi2_nine": x2, "six part": float((pulls[:6] ** 2).sum()),
                            "CKM part": float((pulls[6:] ** 2).sum()), "J": J, "pull J": (abs(J) - J_PDG) / J_SIG,
                            "model over measured": np.exp(f - t9).tolist(),
                            "angle H_u to DR (deg)": W58.fs_angle(hu, DR), "angle H_d to DR (deg)":
                            W58.fs_angle(hd, DR), "angle H_u to H_d (deg)": W58.fs_angle(hu, hd)})
        per_row.append(rec)
    rule_c2 = np.array(c2["rule"])
    i0 = int(np.argmin(rule_c2))
    out["the rule at the 38 rows"] = per_row
    out["K2"] = {"least chi2_nine": float(rule_c2[i0]), "at": per_row[i0]["row"],
                 "rows below 21.67": [per_row[i]["row"] for i in range(len(per_row)) if rule_c2[i] < BAR9],
                 "median": float(np.median(rule_c2))}
    out["K3"] = nulls(np.array(feats["rule"]), float(rule_c2[i0]), t6, s9)
    table = {}
    for e in ENTRIES[1:] + ("T13",):
        a = np.array(c2[e])
        table[e] = {"least": float(a.min()), "median": float(np.median(a)), "rows below 21.67": int((a < BAR9).sum())}
    Xall = np.concatenate([np.array(feats[e]) for e in feats])
    obs_t = float(min(min(c2[e]) for e in feats))
    out["the sensitivity table"] = table
    out["the whole table priced (read-out)"] = {"least over the 14 entries and 38 rows": obs_t,
                                                **nulls(Xall, obs_t, t6, s9)}
    # ---------------------------------------------------------------- the four points
    b57 = T8.git_bytes(root, W61.AGY, W61.J57)
    d57 = [r for r in json.loads(b57.decode("utf-8")) if r["hor"] == "L_max"]
    out["B1757 file sha256"] = T8.sha256(b57)
    four, k4 = [], []
    for (x, y) in POINTS:
        pid = f"{x!r}|{y!r}"
        B, tau, rd = P["B"][pid]
        st = V["vectors"]["four points"][pid]
        hu, hd = dec(st["pairs"]["rule"][0]), dec(st["pairs"]["rule"][1])
        DR = np.array(T8.higgs_DR(tau))
        f, pulls, J, Y = nine(B, rd, 3, hu, hd, t9, s9)
        b_rule = beta(hu, DR)
        boost = st["B1762 boost"]
        k4.append(abs(b_rule / boost - 1))
        rec = {"tau": [x, y], "chi2_nine (rule)": float((pulls ** 2).sum()), "J": J, "beta (rule)": b_rule,
               "B1762 boost": boost, "|beta/boost - 1|": k4[-1]}
        fit = next((q for q in d57 if abs(q["tau"][0] - x) < 1e-6 and abs(q["tau"][1] - y) < 1e-6), None)
        if fit is not None:
            Hu = np.array([complex(a, b) for a, b in fit["H_u"]])
            Hd = np.array([complex(a, b) for a, b in fit["H_d"]])
            rec["B1757 chi2_nine"] = fit["chi2_nine"]
            rec["coupling angle to B1757's fit, up (deg)"] = mat_angle(Y["up"], W58.Y_of(B, "up", "S", Hu))
            rec["coupling angle to B1757's fit, down (deg)"] = mat_angle(Y["down"], W58.Y_of(B, "down", "S", Hd))
            rec["coupling angle to B1757's fit, lep (deg)"] = mat_angle(Y["lep"], W58.Y_of(B, "lep", "S", Hd))
        for n in ("L1_boost_p1", "L4p_schur_rot_pnat"):
            a, b = dec(st["B1762"][n][0]), dec(st["B1762"][n][1])
            rec[f"coupling angle to B1762's {n}, up (deg)"] = mat_angle(Y["up"], W58.Y_of(B, "up", "S", a))
            rec[f"coupling angle to B1762's {n}, down (deg)"] = mat_angle(Y["down"], W58.Y_of(B, "down", "S", b))
        four.append(rec)
    out["the four points"] = four
    out["K4"] = {"worst |beta/boost - 1|": float(max(k4))}
    fr = out["frozen"]
    k1v = V["K1 (part V)"]
    out["cells"] = {
        "K0": bool(all(pins.values()) and out["K0"]["rows rebuilt"] == 38 and out["K0"]["rebuilt equal the frozen rows"]
                   and ident < 1e-12 and six_dev < 1e-6),
        "K1": bool(k1v["no target file read"] and k1v["every rule form positive definite"]
                   and k1v["largest condition number"] < 1e10 and fr["working file equals HEAD's blob"]
                   and fr["stored hash"] == fr["hash recomputed"] and not fr["part V's run failed"]
                   and out["recomputed before targets: max |diff|"] < 1e-12
                   and not out["recomputed before targets: target files read"]
                   and out["K1 counterfactual"]["after the targets are loaded: max |diff|"] < 1e-12
                   and max(moved) < 1e-12),
        "K2": bool(rule_c2[i0] < BAR9),
        "K3": bool(out["K3"]["(a) the data's six with random mixings: fraction_mean"] <= 0.01
                   and out["K3"]["(b) random nines: fraction_mean"] <= 0.01),
        "K4": bool(max(k4) < 0.1)}
    out["K3 decisive (K2 holds)"] = out["cells"]["K2"]


def main():
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part not in ("V", "S"):
        raise SystemExit("usage: the_higgs_from_the_action.py V|S")
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W166", "part": part, "rule": "W166_RULE.md", "status": "one run", "rev": REV,
           "head": T8.resolve(root, "HEAD"), "python": sys.version.split()[0], "numpy": np.__version__,
           "machine": platform.machine()}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        try:
            (part_V if part == "V" else part_S)(root, out)
        except Exception:  # noqa: BLE001  (a failed run is a failed launch, disclosed as such)
            out["run_failed"] = sanitize(traceback.format_exc()[-4000:])
    out["warnings"] = sorted({sanitize(f"{w.category.__name__}: {w.message}") for w in caught})
    out["seconds"] = round(time.time() - t0, 1)
    target = OUT_V if part == "V" else OUT_S
    vec = out.pop("vectors", None)
    text = json.dumps(out, indent=1, default=float)
    if vec is not None:                            # the frozen block on one compact line, as hashed
        text = text[:-2] + ',\n "vectors": ' + json.dumps(vec, sort_keys=True, separators=(",", ":")) + "\n}"
    target.write_text(text + "\n", encoding="utf-8")
    if part == "V":
        print(json.dumps({"rows": out.get("rows"), "K1 (part V)": out.get("K1 (part V)"),
                          "vectors sha256": out.get("vectors sha256")}, indent=1, default=str))
    else:
        print(json.dumps(out.get("cells"), indent=1))
    if "run_failed" in out:
        print("run failed")


if __name__ == "__main__":
    main()
