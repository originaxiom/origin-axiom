#!/usr/bin/env python3
"""W138 (P-304): the third opinion on main's B1726, THE TWO INGREDIENTS, REPLICATED (the rule: W138_RULE.md, committed
and pushed before this script runs). Drafted and compiled in the read-only preparation, before the rule; not run before
its commit. It runs once, from the repository root.

  A   main's compare.py re-run on the committed census.jsonl in a temporary tree (main's files fetched from git at a
      pinned commit, every sha256 checked); its comparison.json and stdout diffed against the committed ones
  A2  the calibration re-implemented here (own code; the same priors, generator and seeds): the 120 per-seed fractions
      again, and one menu main did not compute, every covariant reading with the lepton factor free (labelled)
  B   census points recomputed on this seat's own code, with no import of main's census.py, b1656_funcs.py,
      the_exponents.py or qseries.py: the two best points named in B1726 FINDINGS, 30 points by seed 304, 6 order-5
      points by seed 3045, and B1725's control point when the web seat's census is reachable; the largest deviation per
      key family
  B0  the own instrument's controls (no census): its residues against main's bilinear re-implemented here from its
      definition; the joint law J1 (W96) on every coupling built; every kernel norm finite
  C   R7's mechanism on the committed census: D_frame = (m_mu m_d)/(m_s m_e) at c = 1 on every order-5 row in both
      readings; orders 1, 2, 4 (B1728's other d = e orders) and the spread on order 10 as read-outs

The own instrument (this seat's code, docs/dossiers/the_weave_2026-10-07/):
  W93 the_twisted_half_bound_checked.py  units, eps, blocks, the dual basis, coupling_np, and the closed-form residues
      R_s = c_s theta_s(ub) theta_s(delta) at any tau (its line convention is w = p1 tau - p2, so main's (a, b) with
      w = a tau + b enters as (a, -b))
  W89 the_electrons_zero_checked.py  the z-form kernels' regularised norms (polar Gauss-Legendre, ub reduced to the cell);
      called with a term count of 12 (UNSURE-1 below)
  W96 the_joint_law_checked.py  the identity det Y = 4 det S det M tr(eps S M^T), used here as a per-coupling check
  fresh here  the Higgs DR = q dR/dq + E2 R/24 from direct theta sums; the scale kappa between W93's residues and
      main's (UNSURE-2); the line list; L read from B1667's committed column (an input, sha256-pinned, not recomputed)

Marked as unsure (to be settled in the rule, not by running):
  UNSURE-1  W89.np_theta's default 40 terms overflow (cos of an argument with |Im| > ~2.9) and give nan for kernels at
            Im tau >~ 2.9; read off the code, not seen in a run. Here the term count is 12 and every norm is asserted
            finite.
  UNSURE-2  kappa = F_A F_D / theta_1'(0): derived by hand (the P-304 preparation report, section 5) from main's bilinear
            (b1656_funcs.py:34-38: Res M at u = 0, then (P, Q) -> (P + Q, P - Q)); checked in B0 against the
            circle residues of a fresh re-implementation of that bilinear. It matters only for main's absolute 1e-12 cut
            on |R_s| (b1656_funcs.py:66-67); every ratio and |V| is scale-free.
  UNSURE-3  the tolerances in TOL are proposals for the rule.

    python3 -B <path>/third_opinion_draft.py [--workers 8] [--rev <commit>] [--out <file>] [--parts A,A2,B,C]
"""
import argparse
import hashlib
import json
import math
import multiprocessing as mpr
import platform
import random
import subprocess
import sys
import tempfile
import time
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
REV_DEFAULT = "1059939ccf470250665441622af4ddae85c11780"   # origin/main as read for this draft (2026-10-23)
ARC = "frontier/B1726_the_two_ingredients_replicated"
VER = ARC + "/verification"
LOCK = "tests/test_b1726_the_two_ingredients_replicated.py"
DOSSIER = "docs/dossiers/the_weave_2026-10-07"
WEB_REV = "origin/chat1/web-seat"
WEB_CENSUS = "relays/chat1_2026-10-22_selection_map/two_ingredients_census.jsonl"
HZ = "frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json"
CKM = "frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json"
COLUMN = "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json"

# sha256 pins. census.jsonl's is the lock test's CENSUS_SHA (tests/test_b1726...:8); ARTIFACT_HASHES.txt has no line for it.
PINNED = {
    VER + "/census.py": "185cf17d8b51c11559bf14650d5ad1dd12745eaa228fc40da0a8b9181d1986bf",
    VER + "/compare.py": "4cd90052f73d12f40daedb95b46d79b0ec5222e551cca58c9e395672f8016692",
    VER + "/census.jsonl": "d67432f0dc252e911514f211eb29844fd0bfcc5a270c00188312607435b0478d",
    COLUMN: "688152749777970f21a85b3278a39ae33884b9ae99623d5eec541f41de34a774",
    HZ: "63450365401c149c726e928f842bc7810086ad4d897a62f51217e3c12189880f",
    CKM: "61ea1565a2a8b4e053c33cc3b29e37484f6c9c2aeca54f9b6a83c89137e0d606",
}
SHA_B1725_CENSUS = "f379a4b8cfe2966d9d067abff323f6f654560d589c1d55f55320d816d59c5c4b"
UNPINNED = (VER + "/control.json", VER + "/comparison.json", VER + "/compare_run.txt", ARC + "/ARTIFACT_HASHES.txt", LOCK)

RE = (0.05, 0.2, 0.35, 0.55, 0.7, 0.85)                   # census.py:15-16, written again here
IM = tuple(round(2.05 + 0.1 * k, 2) for k in range(15))
RD = ("S", "St")
HORO = ("L_max", "L_2")
SECTS = ("up", "down", "lep")
UNITS = ("1", "i", "j", "k")
SEEDS = tuple(range(1726, 1746))
NTARGET = 4000
LN3 = math.log(3)
BEST = {"best_six": (151, 0.55, 3.05), "best_nine": (149, 0.55, 2.55)}      # B1726 FINDINGS.md:27-33
SAMPLE_SEED, SAMPLE_N = 304, 30
ORDER5_SEED, ORDER5_N = 3045, 6
C1_POINT = (Fr(2, 5), Fr(1, 10), 0.4, 2.7)                                  # census.py:101-102
TOL = {"rerun_float_rel": 1e-12, "own_log": 1e-6, "own_J_rel": 1e-5, "zero": 1e-10,
       "dframe_census": 1e-8, "dframe_own": 1e-8, "residue_rel": 1e-10, "joint_law": 1e-10,
       "near_R_lo": 1e-14, "near_R_hi": 1e-10, "near_weight": 1e-6}

SEAT = ((1, 0, 0), (1, 1, 1))                   # (up, down, lepton) reading indices, S = 0, S~ = 1 (compare.py:49)
COV = tuple((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1))
MENUS = {"seat": (SEAT, (1, 3)), "cov": (COV, (1, 3)), "free": (SEAT, ("free",)), "cov_free": (COV, ("free",))}
MAIN_MENUS = ("seat", "cov", "free")


# ============================================================================================ git and files
def repo_root():
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=Path.cwd(), capture_output=True, text=True,
                         check=True)
    return Path(out.stdout.strip())


def git_bytes(root, rev, path):
    return subprocess.run(["git", "show", f"{rev}:{path}"], cwd=root, capture_output=True, check=True).stdout


def resolve(root, rev):
    return subprocess.run(["git", "rev-parse", rev], cwd=root, capture_output=True, text=True,
                          check=True).stdout.strip()


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def fetch(root, rev):
    """every file this verification reads from main, by git show at one commit; the pinned ones checked"""
    files = {p: git_bytes(root, rev, p) for p in tuple(PINNED) + UNPINNED}
    checks = {p: sha256(files[p]) == h for p, h in PINNED.items()}
    lock_has = PINNED[VER + "/census.jsonl"] in files[LOCK].decode("utf-8")
    return files, {"pinned_sha256_match": checks, "lock_test_names_the_census_sha": lock_has,
                   "unpinned_sha256": {p: sha256(files[p]) for p in UNPINNED}}


def artifact_hashes(root, rev, text):
    """ARTIFACT_HASHES.txt line by line: is each listed file in main's tree at rev, and does its sha256 match"""
    out = []
    for line in text.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        h, rel = line.split()
        path = rel if rel.startswith("frontier/") else f"{ARC}/{rel}"
        try:
            got = sha256(git_bytes(root, rev, path))
            out.append({"path": path, "in_tree": True, "match": got == h})
        except subprocess.CalledProcessError:
            out.append({"path": path, "in_tree": False, "match": None})
    return out


def census_rows(raw):
    return [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]


def nonfinite_count(rows):
    bad = 0
    for r in rows:
        for k, v in r.items():
            if "|" in k:
                bad += sum(1 for x in v if not math.isfinite(x))
    return bad


# ============================================================================================ A: compare.py re-run
def build_tree(tmp, files):
    """the smallest tree in which main's compare.py finds its ROOT (frontier/ and GENESIS.md) and its inputs"""
    (tmp / "GENESIS.md").write_text("root marker for the P-304 re-run (not main's GENESIS)\n", encoding="utf-8")
    for p in (VER + "/compare.py", VER + "/census.jsonl", VER + "/control.json", HZ, CKM):
        q = tmp / p
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_bytes(files[p])
    return tmp / VER


def run_compare(vdir, workers):
    t0 = time.time()
    p = subprocess.run([sys.executable, "-B", str(vdir / "compare.py"), "--workers", str(workers)], cwd=vdir,
                       capture_output=True, text=True)
    return {"returncode": p.returncode, "seconds": round(time.time() - t0, 1), "stdout": p.stdout,
            "stderr_tail": p.stderr[-3000:]}


def deep_diff(a, b, path="", acc=None):
    """every leaf of two JSON trees: booleans and strings exactly, numbers by relative difference"""
    acc = acc if acc is not None else {"numbers": 0, "exact": 0, "max_rel": 0.0, "mismatches": []}
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a or k not in b:
                acc["mismatches"].append([path + "/" + str(k), "missing on one side"])
            else:
                deep_diff(a[k], b[k], path + "/" + str(k), acc)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            acc["mismatches"].append([path, "length %d vs %d" % (len(a), len(b))])
        for i, (x, y) in enumerate(zip(a, b)):
            deep_diff(x, y, "%s[%d]" % (path, i), acc)
    elif isinstance(a, bool) or isinstance(b, bool) or isinstance(a, str) or a is None:
        if a != b:
            acc["mismatches"].append([path, repr(a), repr(b)])
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        acc["numbers"] += 1
        acc["exact"] += a == b
        rel = abs(a - b) / max(abs(a), abs(b), 1e-300) if a != b else 0.0
        acc["max_rel"] = max(acc["max_rel"], rel)
        if rel > TOL["rerun_float_rel"]:
            acc["mismatches"].append([path, a, b])
    else:
        acc["mismatches"].append([path, "type %s vs %s" % (type(a).__name__, type(b).__name__)])
    return acc


def fractions_exact(old, new):
    """the 120 per-seed fractions and the 6 means, exactly"""
    po, pn = old["fraction_as_good_per_seed"], new["fraction_as_good_per_seed"]
    per = all(po[s][k] == pn[s][k] for s in po for k in po[s])
    mean = all(old["fraction_as_good_mean"][k] == new["fraction_as_good_mean"][k] for k in old["fraction_as_good_mean"])
    return per and mean


def part_A(files, workers, tmp_parent):
    with tempfile.TemporaryDirectory(dir=tmp_parent) as td:
        vdir = build_tree(Path(td), files)
        run = run_compare(vdir, workers)
        new = json.loads((vdir / "comparison.json").read_text(encoding="utf-8")) if run["returncode"] == 0 else None
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    out = {"run": {k: v for k, v in run.items() if k != "stdout"},
           "stdout_equals_compare_run_txt": run["stdout"].strip() == files[VER + "/compare_run.txt"].decode().strip(),
           "stdout": run["stdout"]}
    if new is not None:
        d = deep_diff(old, new)
        d["mismatches"] = d["mismatches"][:40]
        out.update(diff=d, fractions_exact=fractions_exact(old, new), cells_equal=old["cells"] == new["cells"])
    return out


# ============================================================================================ A2: own calibration
def targets(files):
    v = json.loads(files[HZ].decode("utf-8"))["masses_GeV"]["value"]
    c = json.loads(files[CKM].decode("utf-8"))["ckm_abs"]["value"]
    t6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"],
                          v["e"] / v["tau"]]))
    return t6, np.concatenate([t6, np.log(np.array([c[0][1], c[1][2], c[0][2]]))])


def floor_log(x):
    return np.log(np.maximum(np.asarray(x, dtype=float), 1e-300))      # compare.py:36's floor, kept for comparability


def census_arrays(rows):
    """rows sorted by (line, Re tau, Im tau), two per point (the horocycles): log-ratios per reading, log |V|, J"""
    rows = sorted(rows, key=lambda r: (r["line"], r["Re_tau"], r["Im_tau"]))
    up, dn, lep, K, J, lab = [], [], [], [], [], []
    for r in rows:
        for h in HORO:
            up.append([floor_log(r[f"up|{h}|{a}"]) for a in RD])
            dn.append([floor_log(r[f"down|{h}|{a}"]) for a in RD])
            lep.append([floor_log(r[f"lep|{h}|{a}"]) for a in RD])
            K.append([[floor_log(r[f"ckm|{h}|{a}|{b}"][:3]) for b in RD] for a in RD])
            J.append([[r[f"ckm|{h}|{a}|{b}"][3] for b in RD] for a in RD])
            lab.append((r["line"], r["Re_tau"], r["Im_tau"], h))
    return {"up": np.array(up), "dn": np.array(dn), "lep": np.array(lep), "K": np.array(K), "J": np.array(J)}, lab


def own_draws(seed, n):
    """B1695's random hierarchies and B1713's random mixings, drawn in compare.py's order (75-91), written again"""
    rng = random.Random(seed)

    def masses():
        out = []
        for _sector in range(3):
            while True:
                r2 = 10 ** rng.uniform(-3, -1)
                r1 = 10 ** rng.uniform(-6, -2.5)
                if r1 < r2:
                    break
            out += [r2, r1]
        return out

    def mixing():
        while True:
            a = 10 ** rng.uniform(-1.5, -0.2)
            b = 10 ** rng.uniform(-2.5, -0.7)
            c = 10 ** rng.uniform(-3.5, -1.5)
            if c < b < a:
                return [a, b, c]

    six = [np.log(np.array(masses())) for _ in range(n)]
    nine = [np.log(np.array(masses() + mixing())) for _ in range(n)]
    return six, nine


_ARR = {}


def _init_worker(npz_path):
    d = np.load(npz_path)
    _ARR.update({k: d[k] for k in d.files})


def errors(t):
    """per row and reading: the worst |log| of each sector; the leptons at c = 1, 3 and free; the CKM per (up, down)"""
    eu = np.abs(_ARR["up"] - t[0:2]).max(axis=2)
    ed = np.abs(_ARR["dn"] - t[2:4]).max(axis=2)
    dm, de = _ARR["lep"][:, :, 0] - t[4], _ARR["lep"][:, :, 1] - t[5]
    el = {1: np.maximum(np.abs(dm), np.abs(de)), 3: np.maximum(np.abs(dm + LN3), np.abs(de - LN3)),
          "free": np.abs(dm + de) / 2}
    ek = np.abs(_ARR["K"] - t[6:9]).max(axis=3) if len(t) == 9 else None
    return eu, ed, el, ek


def menu_best(E, menu):
    """(best worst |log|, row index, ((up, down, lepton), c)) over the menu; nanargmin, so a nan row cannot hide a menu"""
    eu, ed, el, ek = E
    readings, cs = MENUS[menu]
    best = (math.inf, None, None)
    for (a, b, l) in readings:
        for c in cs:
            w = np.maximum(np.maximum(eu[:, a], ed[:, b]), el[c][:, l])
            if ek is not None:
                w = np.maximum(w, ek[:, a, b])
            i = int(np.nanargmin(w))
            if w[i] < best[0]:
                best = (float(w[i]), i, ((a, b, l), c))
    return best


def seed_job(seed):
    out = {}
    six, nine = own_draws(seed, NTARGET)
    for name, T, ds in (("six", _ARR["T6"], six), ("nine", _ARR["T9"], nine)):
        ET = errors(T)
        obs = {m: menu_best(ET, m)[0] for m in MENUS}
        hits = dict.fromkeys(MENUS, 0)
        for t in ds:
            Et = errors(t)
            for m in MENUS:
                hits[m] += menu_best(Et, m)[0] <= obs[m] + 1e-12
        for m in MENUS:
            out[f"{name}|{m}"] = hits[m] / len(ds)
    return seed, out


def describe(T, menu, lab):
    E = errors(T)
    w, i, ((a, b, l), c) = menu_best(E, menu)
    six = np.concatenate([_ARR["up"][i, a], _ARR["dn"][i, b], _ARR["lep"][i, l]])
    if c == "free":
        cc = math.exp(((T[4] - six[4]) - (T[5] - six[5])) / 2)
    else:
        cc = float(c)
    six = six + np.array([0, 0, 0, 0, math.log(cc), -math.log(cc)])
    return {"best_factor": math.exp(w), "line": lab[i][0], "Re_tau": lab[i][1], "Im_tau": lab[i][2],
            "horocycle": lab[i][3], "readings": [RD[a], RD[b], RD[l]], "lepton_factor": cc,
            "D": math.exp(six[4] + six[3] - six[2] - six[5]), "J": float(_ARR["J"][i, a, b])}


def part_A2(files, rows, workers, tmp_parent):
    arr, lab = census_arrays(rows)
    t6, t9 = targets(files)
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    with tempfile.TemporaryDirectory(dir=tmp_parent) as td:
        npz = str(Path(td) / "arrays.npz")
        np.savez(npz, T6=t6, T9=t9, **arr)
        _init_worker(npz)
        best = {name: {m: describe(T, m, lab) for m in MENUS} for name, T in (("best_six", t6), ("best_nine", t9))}
        with mpr.Pool(workers, initializer=_init_worker, initargs=(npz,)) as P:
            per = dict(P.map(seed_job, SEEDS))
    keys = sorted(per[SEEDS[0]])
    mean = {k: float(np.mean([per[s][k] for s in SEEDS])) for k in keys}
    same_per_seed = all(per[s][k] == old["fraction_as_good_per_seed"][str(s)][k]
                        for s in SEEDS for k in old["fraction_as_good_per_seed"][str(s)])
    best_dev = {}
    for name in best:
        for m in MAIN_MENUS:
            o, n = old[name][m], best[name][m]
            best_dev[f"{name}|{m}"] = {
                "same_row_and_configuration": all(o[k] == n[k] for k in ("line", "Re_tau", "Im_tau", "horocycle",
                                                                          "readings")),
                "best_factor_rel": abs(o["best_factor"] - n["best_factor"]) / o["best_factor"],
                "D_rel": abs(o["D"] - n["D"]) / abs(o["D"]),
                "lepton_factor_rel": abs(o["lepton_factor"] - n["lepton_factor"]) / o["lepton_factor"]}
    return {"per_seed": {str(s): per[s] for s in SEEDS}, "mean": mean, "per_seed_equals_main": same_per_seed,
            "best": best, "best_against_main": best_dev,
            "cov_free_labelled": {"mean_six": mean["six|cov_free"], "mean_nine": mean["nine|cov_free"],
                                  "seeds_above_1pct_six": sum(per[s]["six|cov_free"] > 0.01 for s in SEEDS)}}


# ============================================================================================ B: own rows
def own_modules(root):
    """this seat's W93 and W89, imported from the dossier; W89's theta called with 12 terms (UNSURE-1)"""
    sys.path.insert(0, str(root / DOSSIER))
    import the_twisted_half_bound_checked as W93       # noqa: E402
    import the_electrons_zero_checked as W89           # noqa: E402
    base = W89.np_theta

    def np_theta_12(s, z, t, nt=12):
        return base(s, z, t, nt)

    W89.np_theta = np_theta_12
    mp.mp.dps = 40
    return W93, W89


def own_lines():
    """B1713's 266 lines of exact order 1-12 up to sign, in its order (census.py:39-52), written again"""
    out, seen = [], set()
    for n in range(1, 13):
        for j in range(n):
            for k in range(n):
                if math.gcd(math.gcd(j, k), n) != 1:
                    continue
                a, b = Fr(j, n), Fr(k, n)
                key = min((a, b), ((-a) % 1, (-b) % 1))
                if key not in seen:
                    seen.add(key)
                    out.append(key)
    return out


def order(line):
    return math.lcm(line[0].denominator, line[1].denominator)


def L_column(files):
    pts = json.loads(files[COLUMN].decode("utf-8"))["points"]
    return sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in pts if abs(p["tau"][0] - 0.25) < 1e-9)


def L_at(col, y, which):
    """linear interpolation in Im tau on B1667's Re tau = 1/4 column (census.py:63-64), written again"""
    j = 1 if which == "L_max" else 2
    for lo, hi in zip(col[:-1], col[1:]):
        if lo[0] <= y <= hi[0]:
            return lo[j] + (hi[j] - lo[j]) * (y - lo[0]) / (hi[0] - lo[0])
    raise ValueError("Im tau outside B1667's column")


def higgs_DR(tau, kmax=12, nmax=40):
    """(DR_i, DR_j, DR_k) at tau: R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4), DR = q dR/dq + E2 R / 24, q = e^{2 pi i tau};
    the thetas and their q d/dq as direct sums over n (q d/dq e^{i pi tau m} = (m/2) e^{i pi tau m})"""
    with mp.workdps(30):
        t = mp.mpc(tau.real, tau.imag)
        e = lambda m: mp.exp(1j * mp.pi * t * m)
        h = [mp.mpf(2 * n + 1) / 2 for n in range(-kmax, kmax)]
        n3 = range(-kmax, kmax + 1)
        th2, d2 = mp.fsum(e(x * x) for x in h), mp.fsum(x * x / 2 * e(x * x) for x in h)
        th3, d3 = mp.fsum(e(n * n) for n in n3), mp.fsum(mp.mpf(n * n) / 2 * e(n * n) for n in n3)
        th4, d4 = mp.fsum((-1) ** n * e(n * n) for n in n3), mp.fsum((-1) ** n * mp.mpf(n * n) / 2 * e(n * n) for n in n3)
        E2 = 1 - 24 * mp.fsum(n * e(2 * n) / (1 - e(2 * n)) for n in range(1, nmax))
        l2, l3, l4 = d2 / th2, d3 / th3, d4 / th4
        R = [-th2 / (th3 * th4), -th4 / (th2 * th3), 1j * th3 / (th2 * th4)]
        dlog = [l2 - l3 - l4, l4 - l2 - l3, l3 - l2 - l4]
        return [complex(R[i] * dlog[i] + E2 * R[i] / 24) for i in range(3)]


def readings_at(W93, tau):
    a = higgs_DR(tau)
    S = a[0] * W93.CN["i"] + a[1] * W93.CN["j"] + a[2] * W93.CN["k"]
    return {"S": S, "St": W93.EPSN @ np.conj(S) @ W93.EPSN.T}


def charges(W93, sec):
    f, g = W93.SECTORS[sec]
    return W93.SIXY[f], W93.SIXY[g]


def theta1_prime_u(t, kmax=12):
    """d/du theta_1(u | t) at u = 0, theta_1(u) = -i sum (-1)^k e^{i pi t (k+1/2)^2 + i pi (2k+1) u} (b1656_funcs.py:31-33)"""
    return mp.pi * mp.fsum((-1) ** k * (2 * k + 1) * mp.exp(1j * mp.pi * t * (k + mp.mpf(1) / 2) ** 2)
                           for k in range(-kmax, kmax))


def kappa(qL, qR, a, b, t):
    """UNSURE-2: main's R_s = kappa x W93's R_s, kappa = F_A F_D / theta_1'(0), F_X = e^{i pi X^2 t + 2 pi i X Y_X},
    A = (qL + qR) a, Y_A = (qL + qR) b, D = (qL - qR) a, Y_D = (qL - qR) b (by hand; checked by residue_control)"""
    A, BA, D, BD = [mp.mpf(x.numerator) / x.denominator for x in ((qL + qR) * a, (qL + qR) * b, (qL - qR) * a,
                                                                  (qL - qR) * b)]
    F = mp.exp(1j * mp.pi * (A * A + D * D) * t + 2j * mp.pi * (A * BA + D * BD))
    return F / theta1_prime_u(t)


def own_residues(W93, sec, a, b, tau):
    """W93's closed form at tau on the line (a, -b) in its convention, scaled to main's normalisation"""
    with mp.workdps(40):
        t = mp.mpc(tau.real, tau.imag)
        qL, qR = charges(W93, sec)
        R = W93.residues((a, -b), sec, t)
        k = kappa(qL, qR, a, b, t)
        return {s: complex(k * R[s]) for s in UNITS}


def own_norms(W89, W93, sec, a, b, tau, R):
    """main's rule (b1656_funcs.py:66-67): a norm only where |R_s| > 1e-12; W89's kernel norm otherwise None"""
    qL, qR = charges(W93, sec)
    ub = (qL + qR) * (float(a) * tau + float(b))
    c = {}
    for s in UNITS:
        if abs(R[s]) > 1e-12:
            c[s] = float(W89.norm(W89.TH[s], tau, ub))
            if not math.isfinite(c[s]):
                raise FloatingPointError("kernel norm not finite: %s %s %s" % (sec, s, tau))
        else:
            c[s] = None
    return c


def weighted_M(W93, R, c, L):
    u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0)
         for s in UNITS}
    return sum(u[s] * W93.EN[s] for s in UNITS)


def ratios(Y):
    sv = np.linalg.svd(Y, compute_uv=False)
    return [float(sv[1] / sv[0]), float(sv[2] / sv[0])], sv


def ckm(Yu, Yd):
    Uu = np.linalg.svd(Yu)[0][:, ::-1]
    Ud = np.linalg.svd(Yd)[0][:, ::-1]
    V = np.conj(Uu.T) @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    return [float(abs(V[0, 1])), float(abs(V[1, 2])), float(abs(V[0, 2])), J]


def joint_law(W93, S, M, Y):
    """W96's J1: det Y = 4 det S det M tr(eps S M^T), relative to ||Y||^3"""
    rhs = 4 * np.linalg.det(S) * np.linalg.det(M) * np.trace(W93.EPSN @ S @ M.T)
    return float(abs(np.linalg.det(Y) - rhs) / max(np.linalg.norm(Y) ** 3, 1e-300))


def own_point(W93, W89, col, line, re_t, im_t):
    """one census point on the own instrument: the same keys as census.jsonl, and diagnostics"""
    a, b = line
    tau = complex(re_t, im_t)
    rd = readings_at(W93, tau)
    out, Y, diag = {}, {}, {"joint_law_max": 0.0, "near_R": [], "near_weight": [], "sv_gap_min": math.inf}
    for sec in SECTS:
        R = own_residues(W93, sec, a, b, tau)
        c = own_norms(W89, W93, sec, a, b, tau, R)
        for s in UNITS:
            if TOL["near_R_lo"] < abs(R[s]) < TOL["near_R_hi"]:
                diag["near_R"].append([sec, s, abs(R[s])])
        for h in HORO:
            L = L_at(col, im_t, h)
            for s in UNITS:
                if c[s] is not None and abs(2 * math.pi * L + c[s]) < TOL["near_weight"]:
                    diag["near_weight"].append([sec, h, s, 2 * math.pi * L + c[s]])
            M = weighted_M(W93, R, c, L)
            for r, S in rd.items():
                Ym = W93.coupling_np(S, M)
                Y[(sec, h, r)] = Ym
                out[f"{sec}|{h}|{r}"], sv = ratios(Ym)
                if sv[0] > 0:
                    diag["sv_gap_min"] = min(diag["sv_gap_min"], float((sv[0] - sv[1]) / sv[0]),
                                             float((sv[1] - sv[2]) / sv[0]))
                diag["joint_law_max"] = max(diag["joint_law_max"], joint_law(W93, S, M, Ym))
    for h in HORO:
        for ru in RD:
            for rdn in RD:
                out[f"ckm|{h}|{ru}|{rdn}"] = ckm(Y[("up", h, ru)], Y[("down", h, rdn)])
    return out, diag


def key_family(k):
    return "ckm" if k.startswith("ckm") else k.split("|")[0]


def compare_point(own, stored):
    """largest |log(own/stored)| per family over values above TOL['zero'] in both; J relative; zero patterns"""
    dev = {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0, "zero_pattern_mismatches": 0}
    for k, sv in stored.items():
        if "|" not in k or k not in own:
            continue
        ov = own[k]
        fam = key_family(k)
        vals = list(zip(ov[:3], sv[:3])) if fam == "ckm" else list(zip(ov, sv))
        for p, q in vals:
            if (p > TOL["zero"]) != (q > TOL["zero"]):
                dev["zero_pattern_mismatches"] += 1
            elif p > TOL["zero"]:
                dev[fam] = max(dev[fam], abs(math.log(p / q)))
        if fam == "ckm" and abs(sv[3]) > TOL["zero"]:
            dev["J_rel"] = max(dev["J_rel"], abs(ov[3] - sv[3]) / abs(sv[3]))
    return dev


def sample_points(lines):
    pts = [(k, r, y) for k in range(len(lines)) for r in RE for y in IM]
    rng = random.Random(SAMPLE_SEED)
    chosen = sorted(rng.sample(range(len(pts)), SAMPLE_N))
    o5 = [p for p in pts if order(lines[p[0]]) == 5]
    rng5 = random.Random(ORDER5_SEED)
    chosen5 = sorted(rng5.sample(range(len(o5)), ORDER5_N))
    named = [("best", BEST[n]) for n in BEST]
    return named + [("seed304", pts[i]) for i in chosen] + [("order5_seed3045", o5[i]) for i in chosen5]


def best_rows_check(own_by_key, old):
    """B2: the two best rows' worst factor, D and J from the own values, against comparison.json"""
    t6 = np.array(old["_T6"])
    t9 = np.array(old["_T9"])
    out = {}
    for name, T in (("best_six", t6), ("best_nine", t9)):
        b = old[name]["seat"]
        own = own_by_key[(b["line"], b["Re_tau"], b["Im_tau"])]
        h, (ru, rdn, rl), c = b["horocycle"], b["readings"], b["lepton_factor"]
        six = np.log(own[f"up|{h}|{ru}"] + own[f"down|{h}|{rdn}"] + own[f"lep|{h}|{rl}"])
        six[4] += math.log(c)
        six[5] -= math.log(c)
        err = np.abs(six - T[:6])
        J = own[f"ckm|{h}|{ru}|{rdn}"][3]
        if name == "best_nine":
            err = np.concatenate([err, np.abs(np.log(own[f"ckm|{h}|{ru}|{rdn}"][:3]) - T[6:9])])
        D = math.exp(six[4] + six[3] - six[2] - six[5])
        out[name] = {"best_factor_own": math.exp(err.max()), "best_factor_main": b["best_factor"],
                     "best_factor_rel": abs(math.exp(err.max()) - b["best_factor"]) / b["best_factor"],
                     "D_own": D, "D_main": b["D"], "D_rel": abs(D - b["D"]) / b["D"],
                     "J_own": J, "J_main": b["J"], "J_rel": abs(J - b["J"]) / abs(b["J"])}
    return out


# ---------------------------------------------------------------- B0: main's bilinear, re-implemented from its definition
def thc_f(a, b, u, T, nk=14):
    """theta with characteristic (a, b) at T: sum over n in a + Z of e^{i pi T n^2 + 2 pi i n (u + b)} (b1656_funcs.py:28-30)"""
    n0 = -int(mp.nint(a))
    return mp.fsum(mp.exp(1j * mp.pi * T * (n + a) ** 2 + 2j * mp.pi * (n + a) * (u + b))
                   for n in range(n0 - nk, n0 + nk + 1))


def th1_f(u, t, nk=14):
    return -1j * mp.fsum((-1) ** k * mp.exp(1j * mp.pi * t * (k + mp.mpf(1) / 2) ** 2 + 1j * mp.pi * (2 * k + 1) * u)
                         for k in range(-nk, nk))


def bil_f(x, y, u, t):
    """main's bilinear (b1656_funcs.py:34-38), written again in mpmath"""
    (ax, bx), (ay, by) = x, y
    T = 2 * t
    t1 = th1_f(u, t)
    den = 1j * mp.exp(-1j * mp.pi * t / 2) * mp.exp(-1j * mp.pi * u) * t1
    X0, X1, Y0, Y1 = thc_f(ax, bx, u, T), thc_f(ax, bx, u + t, T), thc_f(ay, by, u, T), thc_f(ay, by, u + t, T)
    return [[X0 * Y0 / t1, mp.exp(1j * mp.pi * by) * X0 * Y1 / den],
            [mp.exp(1j * mp.pi * bx) * X1 * Y0 / den, mp.exp(1j * mp.pi * (bx + by)) * X1 * Y1 / th1_f(u + t, t)]]


def circle_residues(W93, sec, a, b, tau, rho=mp.mpf("0.01"), n=64):
    """R_s = the circle mean of P_s(u) u, P_s = <eps C_s, bil> (b1656_funcs.py:39-45), on the twists (q a, 2 q b)"""
    with mp.workdps(30):
        t = mp.mpc(tau.real, tau.imag)
        qL, qR = charges(W93, sec)
        x = tuple(mp.mpf(v.numerator) / v.denominator for v in (qL * a, 2 * qL * b))
        y = tuple(mp.mpf(v.numerator) / v.denominator for v in (qR * a, 2 * qR * b))
        EC = {s: W93.EPSN @ W93.CN[s] for s in UNITS}
        acc = {s: mp.mpc(0) for s in UNITS}
        for j in range(n):
            u = rho * mp.expjpi(2 * mp.mpf(j) / n)
            M = bil_f(x, y, u, t)
            for s in UNITS:
                acc[s] += u * mp.fsum(complex(EC[s][m, k]) * M[m][k] for m in range(2) for k in range(2))
        return {s: complex(acc[s] / n) for s in UNITS}


def residue_control(W93, lines):
    worst = 0.0
    for key in BEST.values():
        a, b = lines[key[0]]
        tau = complex(key[1], key[2])
        for sec in SECTS:
            mine = own_residues(W93, sec, a, b, tau)
            ref = circle_residues(W93, sec, a, b, tau)
            scale = max(abs(v) for v in ref.values())
            worst = max(worst, max(abs(mine[s] - ref[s]) for s in UNITS) / scale)
    return worst


# ---------------------------------------------------------------- B: the sample
def part_B(root, files, rows, lines):
    W93, W89 = own_modules(root)
    col = L_column(files)
    stored = {(r["line"], r["Re_tau"], r["Im_tau"]): r for r in rows}
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    t6, t9 = targets(files)
    old["_T6"], old["_T9"] = t6.tolist(), t9.tolist()
    res, own_by_key, worst = [], {}, {"up": 0.0, "down": 0.0, "lep": 0.0, "ckm": 0.0, "J_rel": 0.0,
                                       "zero_pattern_mismatches": 0}
    diag_all = {"joint_law_max": 0.0, "near_R": [], "near_weight": [], "sv_gap_min": math.inf}
    t0 = time.time()
    for tag, (k, re_t, im_t) in sample_points(lines):
        own, diag = own_point(W93, W89, col, lines[k], re_t, im_t)
        own_by_key[(k, re_t, im_t)] = own
        dev = compare_point(own, stored[(k, re_t, im_t)])
        for f in worst:
            worst[f] = max(worst[f], dev[f]) if f != "zero_pattern_mismatches" else worst[f] + dev[f]
        diag_all["joint_law_max"] = max(diag_all["joint_law_max"], diag["joint_law_max"])
        diag_all["sv_gap_min"] = min(diag_all["sv_gap_min"], diag["sv_gap_min"])
        for f in ("near_R", "near_weight"):
            diag_all[f] += [[k, re_t, im_t] + x for x in diag[f]]
        res.append({"tag": tag, "line": k, "line_value": [str(lines[k][0]), str(lines[k][1])],
                    "order": order(lines[k]), "Re_tau": re_t, "Im_tau": im_t, "deviation": dev})
    out = {"points": res, "worst": worst, "diagnostics": diag_all, "seconds": round(time.time() - t0, 1),
           "best_rows": best_rows_check(own_by_key, old), "residue_control_rel": residue_control(W93, lines),
           "own_dframe_order5": dframe_from_rows([dict(own_by_key[(k, r, y)], line=k, Re_tau=r, Im_tau=y)
                                                  for (k, r, y) in own_by_key if order(lines[k]) == 5], lines, (5,))}
    out["b1725_control_point"] = b1725_point(root, W93, W89, col, lines)
    return out


def b1725_point(root, W93, W89, col, lines):
    """B1725's control point (0.4 + 2.7i, (2/5, 1/10)) against the web seat's stored row, when its census is reachable"""
    try:
        raw = git_bytes(root, WEB_REV, WEB_CENSUS)
    except subprocess.CalledProcessError:
        return {"reachable": False}
    a, b, re_t, im_t = C1_POINT
    k = lines.index((a, b))
    row = None
    for x in raw.decode("utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            if r["line"] == k and r["Re_tau"] == re_t and r["Im_tau"] == im_t:
                row = r
                break
    own, _diag = own_point(W93, W89, col, (a, b), re_t, im_t)
    return {"reachable": True, "sha256_match": sha256(raw) == SHA_B1725_CENSUS, "row_found": row is not None,
            "deviation": compare_point(own, row) if row is not None else None}


# ============================================================================================ C: D_frame
def dframe_from_rows(rows, lines, orders):
    """D_frame = (lep_mu down_d)/(down_s lep_e) = (m_mu m_d)/(m_s m_e) at c = 1, per horocycle and reading; and the
    largest |log(lep/down)| per ratio. Rows with a value below TOL['zero'] are counted as masked."""
    out = {}
    for r_name in RD:
        stats = {"values": 0, "masked": 0, "max_abs_log_D": 0.0, "max_abs_log_lep_over_down": 0.0, "worst": None}
        for r in rows:
            if order(lines[r["line"]]) not in orders:
                continue
            for h in HORO:
                lep, dn = r[f"lep|{h}|{r_name}"], r[f"down|{h}|{r_name}"]
                if min(lep + dn) <= TOL["zero"]:
                    stats["masked"] += 1
                    continue
                stats["values"] += 1
                lD = abs(math.log(lep[0] * dn[1] / (dn[0] * lep[1])))
                lr = max(abs(math.log(lep[0] / dn[0])), abs(math.log(lep[1] / dn[1])))
                stats["max_abs_log_lep_over_down"] = max(stats["max_abs_log_lep_over_down"], lr)
                if lD >= stats["max_abs_log_D"]:
                    stats["max_abs_log_D"] = lD
                    stats["worst"] = [r["line"], r["Re_tau"], r["Im_tau"], h]
        out[r_name] = stats
    return out


def dframe_spread(rows, lines, n):
    """the distribution of D_frame on lines of order n (a read-out): min, median, max per reading"""
    out = {}
    for r_name in RD:
        vals = []
        for r in rows:
            if order(lines[r["line"]]) != n:
                continue
            for h in HORO:
                lep, dn = r[f"lep|{h}|{r_name}"], r[f"down|{h}|{r_name}"]
                if min(lep + dn) > TOL["zero"]:
                    vals.append(lep[0] * dn[1] / (dn[0] * lep[1]))
        out[r_name] = {"n": len(vals), "min": min(vals, default=None), "median": float(np.median(vals)) if vals else None,
                       "max": max(vals, default=None)}
    return out


def part_C(rows, lines, files):
    old = json.loads(files[VER + "/comparison.json"].decode("utf-8"))
    b = old["best_six"]["seat"]
    return {"order5": dframe_from_rows(rows, lines, (5,)),
            "orders_1_2_4_labelled": dframe_from_rows(rows, lines, (1, 2, 4)),
            "order10_spread_labelled": dframe_spread(rows, lines, 10),
            "best_six_row": {"D_main": b["D"], "c": b["lepton_factor"], "D_frame": b["D"] / b["lepton_factor"] ** 2,
                             "order": order(lines[b["line"]])},
            "order5_points": sum(1 for r in rows if order(lines[r["line"]]) == 5)}


# ============================================================================================ cells and main
def guarded(out, name, fn, *args):
    """run one part; a failure is recorded with its traceback and the other parts still run (a failed part is a
    failed launch of that part, disclosed as such)"""
    import traceback
    t0 = time.time()
    try:
        out[name] = fn(*args)
    except Exception:                                   # noqa: BLE001
        out[name + "_failed"] = traceback.format_exc()[-4000:]
    out.setdefault("part_seconds", {})[name] = round(time.time() - t0, 1)


def cells(out):
    c = {}
    if "A0" in out:
        a0 = out["A0"]
        c["A0_hashes"] = (all(a0["pinned_sha256_match"].values()) and a0["lock_test_names_the_census_sha"]
                          and a0["census_points"] == 23940 and a0["census_unique_points"] == 23940)
        c["A0_census_finite"] = a0["census_nonfinite_values"] == 0
    if "A" in out and "diff" in out["A"]:
        a = out["A"]
        c["A1_rerun"] = (a["run"]["returncode"] == 0 and a["fractions_exact"] and a["cells_equal"]
                         and not a["diff"]["mismatches"])
    if "A2" in out:
        a2 = out["A2"]
        c["A2_own_calibration"] = a2["per_seed_equals_main"] and all(
            v["same_row_and_configuration"] and v["best_factor_rel"] < 1e-12 for v in a2["best_against_main"].values())
    if "B" in out:
        b = out["B"]
        w = b["worst"]
        c["B0_own_controls"] = (b["residue_control_rel"] < TOL["residue_rel"]
                                and b["diagnostics"]["joint_law_max"] < TOL["joint_law"])
        c["B1_rows"] = (max(w["up"], w["down"], w["lep"], w["ckm"]) < TOL["own_log"] and w["J_rel"] < TOL["own_J_rel"]
                        and w["zero_pattern_mismatches"] == 0)
        c["B2_best_rows"] = all(v["best_factor_rel"] < TOL["own_log"] and v["D_rel"] < TOL["own_log"]
                                and v["J_rel"] < TOL["own_J_rel"] for v in b["best_rows"].values())
        c["C2_dframe_own"] = all(s["max_abs_log_D"] < TOL["dframe_own"] and s["values"] > 0
                                 for s in b["own_dframe_order5"].values())
    if "C" in out:
        c["C1_dframe_census"] = all(s["max_abs_log_D"] < TOL["dframe_census"] and s["values"] > 0
                                    and s["values"] + s["masked"] == 2160 for s in out["C"]["order5"].values())
        c["C3_orders_1_2_4_labelled"] = all(s["max_abs_log_D"] < TOL["dframe_census"]
                                            for s in out["C"]["orders_1_2_4_labelled"].values())
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--rev", default=REV_DEFAULT)
    ap.add_argument("--out", default=str(HERE / "third_opinion_b1726.json"))
    ap.add_argument("--parts", default="A,A2,B,C")
    ap.add_argument("--tmp", default=None, help="parent folder for the temporary trees (default: the system's)")
    args = ap.parse_args()
    parts = set(args.parts.split(","))
    root = repo_root()
    t0 = time.time()
    out = {"p304": "the third opinion on B1726 (draft script)", "rev": resolve(root, args.rev),
           "python": sys.version.split()[0], "numpy": np.__version__, "mpmath": mp.__version__,
           "machine": platform.machine(), "workers": args.workers, "tolerances": TOL}
    files, a0 = fetch(root, args.rev)
    rows = census_rows(files[VER + "/census.jsonl"])
    a0.update(census_points=len(rows), census_unique_points=len({(r["line"], r["Re_tau"], r["Im_tau"]) for r in rows}),
              census_nonfinite_values=nonfinite_count(rows),
              artifact_hashes=artifact_hashes(root, args.rev, files[ARC + "/ARTIFACT_HASHES.txt"].decode("utf-8")))
    out["A0"] = a0
    lines = own_lines()
    out["lines_check"] = {"count": len(lines), "151": [str(x) for x in lines[151]], "149": [str(x) for x in lines[149]],
                          "as_FINDINGS": lines[151] == (Fr(2, 5), Fr(1, 2)) and lines[149] == (Fr(2, 5), Fr(1, 10))}
    if "A" in parts:
        guarded(out, "A", part_A, files, args.workers, args.tmp)
    if "A2" in parts:
        guarded(out, "A2", part_A2, files, rows, args.workers, args.tmp)
    if "B" in parts:
        guarded(out, "B", part_B, root, files, rows, lines)
    if "C" in parts:
        guarded(out, "C", part_C, rows, lines, files)
    out["cells"] = cells(out)
    out["seconds"] = round(time.time() - t0, 1)
    Path(args.out).write_text(json.dumps(out, indent=1, default=float) + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
