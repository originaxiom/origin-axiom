"""B1841 census (data-free): the exact twisted norms at B1840's four principled ends, sealed in ../PREREGISTRATION.md.

At B1753's 223 apexes (B1839's accessory geometry), every Higgs-twist class of B1713's 266 lines, the four ends
E1 L_2, E2 ln 2, E3 L_max, E4 L_2 - pi/2, through B1839's sealed census instrument imported unchanged (its split quadrature
at (40, 28) and its class cache). No data are read.
    python3 -B census.py --workers 8     -> norms.npz, norms_index.json, census_controls.json, census_run.txt
Importing computes nothing."""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, math, random, time, hashlib, pathlib, importlib.util
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B1839V = ROOT / "frontier" / "B1839_the_end_card" / "verification"
ENTRIES = ("E1_L2", "E2_ln2", "E3_Lmax", "E4_L2_minus_half_pi")
UNITS = ("1", "i", "j", "k")
CKPT = HERE / "norms_ckpt.jsonl"
_G = {}


def C39():
    """B1839's sealed census module, loaded under its own name"""
    if "c39" not in _G:
        sp = importlib.util.spec_from_file_location("b1839_census", B1839V / "census.py")
        m = importlib.util.module_from_spec(sp); sys.modules["b1839_census"] = m; sp.loader.exec_module(m); _G["c39"] = m
    return _G["c39"]


def levels(rec):
    """the four ends at one apex, from B1839's accessory geometry (B1667's L_max and L_2 there)"""
    return [rec["L_2"], math.log(2.0), rec["L_max"], rec["L_2"] - math.pi / 2]


def apex_task(rec):
    t0 = time.time(); c = C39(); M = c.mods(); ee = M["ee"]
    tau = complex(*rec["tau"]); G = ee.geometry(tau, complex(*rec["c"]))
    assert abs(G["L_max"] - rec["L_max"]) < 1e-12 and abs(G["L_2"] - rec["L_2"]) < 1e-12, rec["apex"]
    keys, idx, reps = c.classes()
    tw = [c.twists(tau, c.red_line(M["LINES"][k], rec["n"]), "down") for k in reps]
    out = np.zeros((len(reps), len(ENTRIES), 4)); margins = []
    for j, Lh in enumerate(levels(rec)):
        assert Lh >= rec["L_max"] - 1e-12, (rec["apex"], ENTRIES[j])
        nodes, margin = c.cell_nodes(tau, G["al"], G["be"], Lh); margins.append(margin)
        for q, (x, yy, R) in enumerate(tw):
            N = c.kernel_norms(nodes, x, yy, R, tau); out[q, j] = [N[s] for s in UNITS]
    return {"apex": rec["apex"], "norms": out.tolist(), "margins": margins, "seconds": time.time() - t0}


def run(workers, log):
    from multiprocessing import get_context
    acc = C39().load_acc(); done = set()
    if CKPT.exists():
        for l in CKPT.read_text(encoding="utf-8").splitlines():
            if l.strip(): done.add(json.loads(l)["apex"])
    todo = [r for r in acc if r["apex"] not in done]
    log("census: %d apexes to do (%d done), 170 classes x %d ends, %d workers" % (len(todo), len(done), len(ENTRIES), workers))
    t0 = time.time()
    with get_context("spawn").Pool(workers) as P, CKPT.open("a", encoding="utf-8") as fh:
        for k, r in enumerate(P.imap_unordered(apex_task, todo, chunksize=1)):
            fh.write(json.dumps(r) + "\n"); fh.flush()
            if (k + 1) % 20 == 0 or k + 1 == len(todo):
                log("  %d / %d apexes (%.0f s)" % (k + 1, len(todo), time.time() - t0))
    rows = {}
    for l in CKPT.read_text(encoding="utf-8").splitlines():
        if l.strip():
            r = json.loads(l); rows[r["apex"]] = r
    arr = np.array([rows[i]["norms"] for i in range(len(acc))], dtype=float)
    mg = np.array([rows[i]["margins"] for i in range(len(acc))], dtype=float)
    np.savez_compressed(HERE / "norms.npz", norms=arr, margins=mg)
    keys, idx, reps = C39().classes()
    index = {"ENTRIES": list(ENTRIES), "units": list(UNITS), "line_class": idx, "class_rep_line": reps, "shape": list(arr.shape),
             "norms_sha256": hashlib.sha256(np.ascontiguousarray(arr).tobytes()).hexdigest()}
    (HERE / "norms_index.json").write_text(json.dumps(index, indent=1), encoding="utf-8")
    log("norms: shape %s, sha256 %s; min margin %.3e; all finite %s" % (arr.shape, index["norms_sha256"], float(mg.min()), bool(np.all(np.isfinite(arr)))))
    CKPT.unlink()


def controls(log):
    c = C39(); M = c.mods(); ee = M["ee"]; acc = c.load_acc()
    arr = np.load(HERE / "norms.npz")["norms"]; ref = np.load(B1839V / "norms.npz")["norms"]
    e1 = float(np.max(np.abs(arr[:, :, 2, :] - ref[:, :, 0, :]) / np.maximum(np.abs(ref[:, :, 0, :]), 1e-300)))
    c1 = bool(e1 < 1e-13)
    log("C1 (E3 = B1839's delta = 0, every apex, class, channel): max rel %.1e -> %s" % (e1, "HOLDS" if c1 else "FAILS"))
    rng = random.Random(18411); keys, idx, reps = c.classes(); worst = 0.0
    for _ in range(16):
        i = rng.randrange(len(acc)); q = rng.randrange(len(reps)); j = rng.randrange(len(ENTRIES)); r = acc[i]
        tau = complex(*r["tau"]); G = ee.geometry(tau, complex(*r["c"]))
        x, yy, R = c.twists(tau, c.red_line(M["LINES"][reps[q]], r["n"]), "down")
        Ni, _ = ee.twisted_norms(tau, G["al"], G["be"], levels(r)[j], x, yy, R, nth=c.NTH, ns=c.NS)
        for k, s in enumerate(UNITS):
            if abs(R[s]) > 1e-12: worst = max(worst, abs(arr[i, q, j, k] / Ni[s] - 1))
    c2 = bool(worst < 1e-13)
    log("C2 (16 random (apex, class, entry) against the instrument): max rel %.1e -> %s" % (worst, "HOLDS" if c2 else "FAILS"))
    return {"C1": {"holds": c1, "max_rel": e1}, "C2": {"holds": c2, "max_rel": float(worst)}}


def main():
    t0 = time.time(); out = []

    def log(s):
        print(s, flush=True); out.append(s)
    w = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 8
    run(w, log); res = controls(log)
    (HERE / "census_controls.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    log("census exit 0 (%.0f s)" % (time.time() - t0))
    (HERE / "census_run.txt").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
