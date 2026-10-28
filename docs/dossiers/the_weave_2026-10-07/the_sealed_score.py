#!/usr/bin/env python3
"""W170 — the plan's stage 5, the score, sealed (the rule: W170_RULE.md, committed and pushed before this script).
The state stages 2 and 4 select: the line (2/5, 1/2) at Re tau = 0 (W169's X = 1), L_max, Im tau on 2.10..3.20 (111
heights; the height the one fitted number).  The Higgs pair on W166's code: H_u = K_up^-1 DR (S~), H_d = conj(K_d^-1 DR)
(S; K_d = 3 K_down + K_lep), raw couplings, c = 3.  Read-out: the same pair at W158's 38 strip rows.

  V  the pairs, blind (no target file read; every git read logged), frozen by sha256
  S  the frozen blob and hash checked and recomputed; then
     Z0  the instrument;  Z1  |J| < 1e-12 at every height;  Z2  chi2_six above 16.75 at every height;
     Z3  the least chi2_nine above 20.09 (decisive);  R  read-outs, the nulls on seeds 1949-1968

    python3 -B docs/dossiers/the_weave_2026-10-07/the_sealed_score.py V
    python3 -B docs/dossiers/the_weave_2026-10-07/the_sealed_score.py S
"""
import contextlib
import io
import json
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
    import the_higgs_from_the_action as W66   # noqa: E402  (W166: forms, the nine, the frame, the rows, encodings)
W58, W61, T8, T42 = W66.W58, W66.W61, W66.T8, W66.T42

DOS = W66.DOS
OUT_V = HERE / "the_sealed_score_vectors.json"
OUT_S = HERE / "the_sealed_score.json"
VREL = DOS + "the_sealed_score_vectors.json"
LINE = (Fr(2, 5), Fr(1, 2))
X0 = 0.0
HOR = "L_max"
HEIGHTS = [round(2.10 + 0.01 * i, 2) for i in range(111)]
RD = {"up": "St", "down": "S", "lep": "S"}
C = 3
SEEDS = tuple(range(1949, 1969))
BAR = 20.09
_ROOT = {}


def sanitize(text):
    for k, v in _ROOT.items():
        text = text.replace(v, k)
    return text


def sealed_pair(B, tau, rd):
    """W166's forms: H_u = K_up^-1 DR; H_d = conj((3 K_down + K_lep)^-1 DR)"""
    DR = np.array(T8.higgs_DR(tau))
    Ku = W66.form(B, "up", rd["up"])
    Kd = 3 * W66.form(B, "down", rd["down"]) + W66.form(B, "lep", rd["lep"])
    hu = W61.gauge_h1(np.linalg.solve(Ku, DR))
    hd = W61.gauge_h1(np.conj(np.linalg.solve(Kd, DR)))
    conds = [float(np.linalg.cond(Ku)), float(np.linalg.cond(Kd))]
    pd = bool(np.linalg.eigvalsh(Ku)[0] > 0 and np.linalg.eigvalsh(Kd)[0] > 0)
    return hu, hd, conds, pd


def produce(root):
    col, col_sha, W93, W89, L = W66.frame(root)
    k = L.index(LINE)
    block = {"state": {}, "rows": {}}
    Bs, conds, pds = {}, [], []
    for y in HEIGHTS:
        B = W58.basis(W93, W89, col, L[k], X0, y, HOR)
        hu, hd, c, pd = sealed_pair(B, complex(X0, y), RD)
        block["state"][f"{y:.2f}"] = [W66.enc(hu), W66.enc(hd)]
        Bs[("state", f"{y:.2f}")] = B
        conds += c
        pds.append(pd)
    rows = W66.rows_from_outputs(root, L)
    for r in rows:
        B = W58.basis(W93, W89, col, L[r["k"]], r["x"], r["y"], r["hor"])
        hu, hd, c, pd = sealed_pair(B, complex(r["x"], r["y"]), W66.rd_of(r))
        rid = W66.row_id(r)
        block["rows"][rid] = [W66.enc(hu), W66.enc(hd)]
        Bs[("rows", rid)] = B
    return {"block": block, "B": Bs, "rows": rows, "column sha256": col_sha, "largest condition": max(conds),
            "all positive definite": all(pds), "line index": k}


def part_V(root, out):
    P = produce(root)
    out["line"] = [str(q) for q in LINE]
    out["heights"] = len(HEIGHTS)
    out["rows"] = len(P["rows"])
    out["row list"] = P["rows"]
    out["column sha256"] = P["column sha256"]
    out["files read"] = sorted(set(W66.READS))
    out["target files read"] = sorted(set(W66.READS) & set(W66.TARGET_FILES))
    out["Z0 (part V)"] = {"no target file read": not out["target files read"],
                          "every form positive definite at the state": P["all positive definite"],
                          "largest condition number at the state": P["largest condition"]}
    out["vectors"] = P["block"]
    out["vectors sha256"] = W66.block_hash(P["block"])


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
            "(b) random nines: fraction_mean": float(np.mean(fb))}


def part_S(root, out):
    work = OUT_V.read_bytes()
    blob = T8.git_bytes(root, "HEAD", VREL)
    V = json.loads(blob.decode("utf-8"))
    out["frozen"] = {"working file equals HEAD's blob": work == blob, "stored hash": V["vectors sha256"],
                     "hash recomputed": W66.block_hash(V["vectors"]), "part V's run failed": "run_failed" in V}
    W66.READS.clear()
    P = produce(root)
    out["recomputed before targets: max |diff|"] = W66.max_diff(V["vectors"], P["block"])
    out["recomputed before targets: target files read"] = sorted(set(W66.READS) & set(W66.TARGET_FILES))
    files = {p: T8.git_bytes(root, W58.REV, p) for p in W58.FILES}
    pins = {p: T8.sha256(files[p]) == h for p, h in W58.PIN.items()}
    t6, t9 = T8.targets(files)
    sg = T42.sigma(files)
    s9 = np.concatenate([sg, T42.sigma_ckm(files)])
    # ---------------------------------------------------------------- the state
    per_y, feats = [], []
    for y in HEIGHTS:
        B = P["B"][("state", f"{y:.2f}")]
        st = V["vectors"]["state"][f"{y:.2f}"]
        hu, hd = W66.dec(st[0]), W66.dec(st[1])
        f, pulls, J, _Y = W66.nine(B, RD, C, hu, hd, t9, s9)
        feats.append(f / s9)
        per_y.append({"Im tau": y, "chi2_nine": float((pulls ** 2).sum()), "chi2_six": float((pulls[:6] ** 2).sum()),
                      "CKM part": float((pulls[6:] ** 2).sum()), "J": J,
                      "model over measured": np.exp(f - t9).tolist()})
    c9 = np.array([p["chi2_nine"] for p in per_y])
    i0 = int(np.argmin(c9))
    out["the state, per height"] = per_y
    out["Z3"] = {"least chi2_nine": float(c9[i0]), "at Im tau": HEIGHTS[i0], "its six part": per_y[i0]["chi2_six"],
                 "its CKM part": per_y[i0]["CKM part"], "bar": BAR}
    out["Z2"] = {"least chi2_six": float(min(p["chi2_six"] for p in per_y))}
    out["Z1"] = {"largest |J|": float(max(abs(p["J"]) for p in per_y))}
    out["nulls at the state"] = nulls(np.array(feats), float(c9[i0]), t6, s9)
    # ---------------------------------------------------------------- the strip read-out (data-chosen; a look)
    rows_out = []
    for r in V["row list"]:
        rid = W66.row_id(r)
        B = P["B"][("rows", rid)]
        st = V["vectors"]["rows"][rid]
        f, pulls, J, _Y = W66.nine(B, W66.rd_of(r), r["c"], W66.dec(st[0]), W66.dec(st[1]), t9, s9)
        rows_out.append({"row": [r["name"], r["k"], r["x"], r["y"]], "chi2_nine": float((pulls ** 2).sum()),
                         "chi2_six": float((pulls[:6] ** 2).sum()), "CKM part": float((pulls[6:] ** 2).sum()), "J": J})
    out["the strip rows (read-out, a look)"] = {"least chi2_nine": min(p["chi2_nine"] for p in rows_out),
                                                "least chi2_six": min(p["chi2_six"] for p in rows_out),
                                                "below 21.67": sum(1 for p in rows_out if p["chi2_nine"] < 21.67),
                                                "rows": rows_out}
    fr = out["frozen"]
    z0v = V["Z0 (part V)"]
    out["Z0"] = {"pins": pins}
    out["cells"] = {
        "Z0": bool(all(pins.values()) and z0v["no target file read"] and z0v["every form positive definite at the state"]
                   and fr["working file equals HEAD's blob"] and fr["stored hash"] == fr["hash recomputed"]
                   and not fr["part V's run failed"] and out["recomputed before targets: max |diff|"] < 1e-12
                   and not out["recomputed before targets: target files read"]),
        "Z1": bool(out["Z1"]["largest |J|"] < 1e-12),
        "Z2": bool(out["Z2"]["least chi2_six"] > 16.75),
        "Z3": bool(out["Z3"]["least chi2_nine"] > BAR)}


def main():
    part = sys.argv[1] if len(sys.argv) > 1 else ""
    if part not in ("V", "S"):
        raise SystemExit("usage: the_sealed_score.py V|S")
    root = T8.repo_root()
    _ROOT["<repo>"] = str(root)
    _ROOT["<home>"] = str(Path.home())
    t0 = time.time()
    out = {"arc": "W170", "part": part, "rule": "W170_RULE.md", "status": "one run", "rev": W58.REV,
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
    if vec is not None:
        text = text[:-2] + ',\n "vectors": ' + json.dumps(vec, sort_keys=True, separators=(",", ":")) + "\n}"
    target.write_text(text + "\n", encoding="utf-8")
    print(json.dumps(out.get("cells") if part == "S" else {"Z0 (part V)": out.get("Z0 (part V)"),
                                                           "vectors sha256": out.get("vectors sha256")}, indent=1))
    if "run_failed" in out:
        print("run failed")


if __name__ == "__main__":
    main()
