"""Referee B1798: direct (no KD) check of the R71-1 null on seeds chosen here.
For ARC in {b1753_all, b1749}: B1741's compare.py (loaded fresh, unchanged) gives chi2_features('seat', False) and
min_chi2; the census is loaded by an INDEPENDENT loader written here (b1753_all: committed 48-line census + the two
extension files, dedup by (apex, line) with equality; b1749: its committed census), and the arrays are compared with
feat_null.C_for(ARC)'s loader.  For each chosen seed: direct min chi2 of every one of 4 000 targets over all rows and the
four seat configurations; hits <= obs + 1e-9; every target with direct min <= obs + 0.5 must be a KD candidate; the KD
file's per-line minima (min over lines) must equal the direct minima for the candidates.
    python3 -B direct_null.py ARC NSEEDS SEEDSEED [--workers K]"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1"); os.environ.setdefault("OPENBLAS_NUM_THREADS", "1"); os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")
import sys, json, random, pathlib, importlib.util, hashlib
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
R71 = ROOT / "frontier/B1798_the_six_graded_under_the_class_choosing_null/verification"
B1741 = ROOT / "frontier/B1741_tau_from_the_thread_rule_the_line_free/verification/compare.py"
OBS = {"b1753_all": 2.739034460748371, "b1749": 3.573708662392164}
_G = {}


def load_mod(name, path):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp)
    sys.modules[name] = m; sp.loader.exec_module(m); return m


def my_rows(arc):
    if arc == "b1749":
        ps = [ROOT / "frontier/B1749_the_six_at_fresh_apexes/verification/census.jsonl"]
    else:
        ps = [ROOT / "frontier/B1753_the_six_on_the_five_ality_lines/verification/census.jsonl",
              R71 / "b1753_all266/census_ext.jsonl", R71 / "b1753_all266/census_ext_tail.jsonl"]
    seen = {}
    for p in ps:
        for l in p.read_text(encoding="utf-8").split("\n"):
            if not l.strip(): continue
            r = json.loads(l); k = (r["apex"], r["line"])
            if k in seen: assert seen[k] == r; continue
            seen[k] = r
    rows = list(seen.values())
    return rows


def build(arc):
    C = load_mod("ref_b1741_%s" % arc, B1741)
    assert hashlib.sha256(B1741.read_bytes()).hexdigest() == "6308ed93e53ab99522cf654a85250f1299e9fa334ce13f92a74334cd7812f3bd"
    rows = my_rows(arc)
    v = json.loads(C.DATA.read_text(encoding="utf-8"))["masses_GeV"]["value"]
    T6 = np.log(np.array([v["c"] / v["t"], v["u"] / v["t"], v["s"] / v["b"], v["d"] / v["b"], v["mu"] / v["tau"], v["e"] / v["tau"]]))
    lg = lambda x: np.log(np.maximum(np.array(x, dtype=float), 1e-300))
    U, Dn, E, lab = [], [], [], []
    # deliberately a different row order from the loaders under test (by apex, then line)
    for r in sorted(rows, key=lambda r: (r["apex"], r["line"])):
        for h in ("L_max", "L_2"):
            U.append([lg(r[f"up|{h}|{a}"]) for a in C.RD]); Dn.append([lg(r[f"down|{h}|{a}"]) for a in C.RD])
            E.append([lg(r[f"lep|{h}|{a}"]) for a in C.RD]); lab.append((r["line"], r["Re_tau"], r["Im_tau"], h))
    C._A.clear(); C._A.update(U=np.array(U), Dn=np.array(Dn), E=np.array(E), lab=lab, T6=T6)
    F = C.chi2_features("seat", False)
    return C, F, rows, lab


def _init(arc):
    if _G.get("arc") == arc: return
    C, F, rows, lab = build(arc); _G.update(arc=arc, C=C, F=F)


def run(job):
    arc, seed = job; _init(arc); C, F = _G["C"], _G["F"]
    d6, _ = C.draws(seed); T = np.array(d6)
    return seed, C.min_chi2(F, T, block=100)


def main():
    arc = sys.argv[1]; ns = int(sys.argv[2]); ss = int(sys.argv[3])
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    seeds = sorted(random.Random(ss).sample(range(5001, 7501), ns))
    print("arc", arc, "seeds", seeds, flush=True)
    C, F, rows, lab = build(arc)
    print("my loader: %d rows (%d feature rows), lines present %d" % (len(rows), len(lab), len({l[0] for l in lab})))
    obs_data = float(C.min_chi2(F, C._A["T6"][None, :])[0]); print("data min chi2 %.12f (draft obs %.12f)" % (obs_data, OBS[arc]))
    # cross-check against feat_null.C_for's loader
    sys.path.insert(0, str(R71)); fn = load_mod("feat_null_ref", R71 / "feat_null.py")
    Cf = fn.C_for(arc); Af = Cf.arrays()
    key = lambda lab_: {(l[0], l[1], l[2], l[3]): i for i, l in enumerate(lab_)}
    km, kf = key(lab), key(Af["lab"]); assert set(km) == set(kf), "label sets differ"
    idx = np.array([kf[l] for l in lab])
    print("feat_null loader: %d feature rows; max |U|,|Dn|,|E| diff %.3e %.3e %.3e" % (len(Af["lab"]),
          np.abs(Af["U"][idx] - C._A["U"]).max(), np.abs(Af["Dn"][idx] - C._A["Dn"]).max(), np.abs(Af["E"][idx] - C._A["E"]).max()))
    kd = np.load(R71 / ("kd_%s_5001_7500.npz" % arc))
    cs, ci, plm = kd["cand_seed"], kd["cand_idx"], kd["plm"]
    from multiprocessing import Pool
    with Pool(nw) as P:
        res = dict(P.imap_unordered(run, [(arc, s) for s in seeds]))
    obs = OBS[arc]; tot_direct = tot_kd = 0; worst = 0.0; miss = 0; near = 0
    for s in seeds:
        dm = res[s]; m = cs == s; cand = ci[m]; kdmin = plm[:, m].min(0)
        hd = int((dm <= obs + 1e-9).sum()); hk = int((kdmin <= obs + 1e-9).sum())
        tot_direct += hd; tot_kd += hk
        need = np.flatnonzero(dm <= obs + 0.5); near += len(need)
        miss += len(set(need.tolist()) - set(cand.tolist()))
        if len(cand): worst = max(worst, float(np.abs(dm[cand] - kdmin).max()))
        if hd != hk: print("  seed %d: direct %d, kd %d" % (s, hd, hk))
    print("%s: %d seeds, %d targets: direct hits %d, KD hits %d; targets within obs+0.5 %d, missed by KD %d; max |direct - KD| on candidates %.3e"
          % (arc, len(seeds), 4000 * len(seeds), tot_direct, tot_kd, near, miss, worst))
    print("direct_null exit 0")


if __name__ == "__main__":
    main()
