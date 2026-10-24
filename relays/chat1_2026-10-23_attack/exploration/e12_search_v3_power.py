"""Data-free power test (labelled; committed before its run) of search_v3 against the sealed search (v1) and e11's v2b,
with the unification-scale sigma (targets_unification.json, tan beta 10: the relative errors with the 10% floor), on THE
READING TEST's store (planted targets only, no data).  48 planted rows (seed 2028): 16 near the null conic (|s|
log-uniform 1e-4..1e-1), 16 near n or n-bar, 16 uniform; targets the A1 model's nine at the planted direction plus
Gaussian noise of sigma ("met" = the search's minimum at or below the planted direction's chi2) and without noise
(recovery to 0.1).  The grid stage is computed once per row; the seconds per search exclude it."""
import contextlib, importlib.util, io, json, math, sys, time, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parents[1]
sys.argv = ["x"]


def load(name, f):
    spec = importlib.util.spec_from_file_location(name, HERE / f); m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


oh = load("oh", "one_higgs_search.py"); s3 = load("s3", "search_v3.py")
tu = json.loads((HERE / "targets_unification.json").read_text())["GUT"]["tan beta 10"]
SIG = np.sqrt(np.array(tu["relative errors"]) ** 2 + 0.10 ** 2)
st = np.load(HERE / "reading_test_store.npz"); U, H = st["U"], st["H"]


def v2b(Uh, extra, T, L, seed):
    chis = np.sum(((L - T) / SIG) ** 2, axis=1)
    order = np.argsort(chis); keep = []
    for idx in order:
        if all(abs(np.vdot(oh.HS[j], oh.HS[idx])) < math.cos(0.05) for j in keep):
            keep.append(int(idx))
        if len(keep) == 16:
            break
    starts = [oh.HS[j] for j in keep] + list(extra) + [np.conj(q) for q in extra]
    best = (float(chis[order[0]]), np.concatenate([oh.HS[order[0]].real, oh.HS[order[0]].imag]))
    for h in starts:
        o = oh.refine(Uh, np.concatenate([h.real, h.imag]), T, SIG, False)
        if o is not None and o[0] < best[0]:
            best = o
    rng = np.random.default_rng(seed)
    for k in range(12):
        hb = oh.vec(best[1]); sc = 0.02 if k < 6 else 0.06
        z = rng.normal(size=3) + 1j * rng.normal(size=3); z -= np.vdot(hb, z) * hb; z /= np.linalg.norm(z)
        hn = math.cos(sc) * hb + math.sin(sc) * z
        o = oh.refine(Uh, np.concatenate([hn.real, hn.imag]), T, SIG, False)
        if o is not None and o[0] < best[0]:
            best = o
    return best[0]


rng = np.random.default_rng(2028)
rows, tsum = [], {"v1": 0.0, "v2b": 0.0, "v3": 0.0}
for n in range(48):
    p = int(rng.integers(0, 2128)); hr = int(rng.integers(0, 2)); Uh = U[p, :, hr]
    if n < 16:
        kind = "conic"; t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
        h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0); hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
    elif n < 32:
        kind = "n/n-bar"; lead, other = (oh.F3, oh.F1) if n < 24 else (oh.F1, oh.F3)
        de = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform()); ep = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
        hp = lead + de * oh.F2 + ep * other
    else:
        kind = "uniform"; z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
    hp = hp / np.linalg.norm(hp)
    T0 = oh.nine_batch(Uh, hp[None], np.zeros(9), SIG, False)[0][0]; Tp = T0 + rng.normal(size=9) * SIG
    cp = float(oh.nine_batch(Uh, hp[None], Tp, SIG, False)[1][0])
    L = s3.grid_logs(Uh)
    r = {"n": n, "kind": kind, "|h.h|": float(abs(hp @ hp)), "planted chi2": cp}
    for tag, T in (("noisy", Tp), ("exact", T0)):
        chis = np.sum(((L - T) / SIG) ** 2, axis=1)
        a = time.time(); r[f"v1 {tag}"] = oh.search(Uh, H[p], T, SIG, False, n_extra=4, chis=chis)[1][0]; tsum["v1"] += time.time() - a
        a = time.time(); r[f"v2b {tag}"] = v2b(Uh, H[p], T, L, 1000 + n); tsum["v2b"] += time.time() - a
        a = time.time(); r[f"v3 {tag}"] = s3.search3(Uh, H[p], T, SIG, L=L, seed=1000 + n)[1][0]; tsum["v3"] += time.time() - a
    rows.append(r)
    print(json.dumps(r), flush=True)
summ = {k: sum(r[f"{k} noisy"] <= r["planted chi2"] + 1e-9 for r in rows) for k in ("v1", "v2b", "v3")}
for k in ("v1", "v2b", "v3"):
    summ[f"{k} exact <= 0.1"] = sum(r[f"{k} exact"] <= 0.1 for r in rows)
    summ[f"{k} seconds per search"] = tsum[k] / 96
print("SUMMARY", json.dumps(summ))
