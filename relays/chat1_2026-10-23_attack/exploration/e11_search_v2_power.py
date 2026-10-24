"""Data-free power test (labelled; committed before its run) of three one-Higgs search configurations for the
holomorphic reading (A1), on THE READING TEST's store (rows never compared with the data under A1; planted targets only,
no data):
  v1   the sealed configuration (8 grid starts, the 4 best record starts; one_higgs_search.search);
  v2a  16 grid starts and all 26 record starts;
  v2b  v2a, then basin hopping: 12 perturbations of the best solution (Fubini-Study scale 0.02 and 0.06 rad), refined.
36 planted rows (seed 2027): 12 near the null conic (|s| log-uniform 1e-4..1e-1), 12 near n or n-bar (the box), 12
uniform; targets the A1 model's nine at the planted direction plus Gaussian noise of the chi2's sigma ("met" = the
search's minimum at or below the planted direction's chi2) and without noise (recovery to 0.1)."""
import contextlib, importlib.util, io, json, math, sys, time, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parents[1]
sys.argv = ["x"]


def load(name, f):
    spec = importlib.util.spec_from_file_location(name, HERE / f); m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


ih = load("ih", "inverse_higgs.py"); oh = load("oh", "one_higgs_search.py")
T9, SIG = ih.T9, ih.SIG
st = np.load(HERE / "reading_test_store.npz"); U, H = st["U"], st["H"]


def v2(Uh, extra, T, hop):
    g, (c, x) = oh.search(Uh, extra, T, SIG, False, n_extra=None, H=None) if False else (None, (None, None))
    chis = np.concatenate([oh.nine_batch(Uh, oh.HS[a:a + 28200], T, SIG, False)[1] for a in range(0, len(oh.HS), 28200)])
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
    if hop:
        rng = np.random.default_rng(int(abs(T[0]) * 1e6) % (2 ** 32))
        for k in range(12):
            hb = oh.vec(best[1]); sc = 0.02 if k < 6 else 0.06
            z = rng.normal(size=3) + 1j * rng.normal(size=3); z -= np.vdot(hb, z) * hb; z /= np.linalg.norm(z)
            hn = math.cos(sc) * hb + math.sin(sc) * z
            o = oh.refine(Uh, np.concatenate([hn.real, hn.imag]), T, SIG, False)
            if o is not None and o[0] < best[0]:
                best = o
    return best[0]


rng = np.random.default_rng(2027)
rows = []
t0 = time.time()
for n in range(36):
    p = int(rng.integers(0, 2128)); hr = int(rng.integers(0, 2)); Uh = U[p, :, hr]
    if n < 12:
        t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
        h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0); hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
    elif n < 24:
        lead, other = (oh.F3, oh.F1) if n < 18 else (oh.F1, oh.F3)
        de = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform()); ep = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
        hp = lead + de * oh.F2 + ep * other
    else:
        z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
    hp = hp / np.linalg.norm(hp)
    T0 = oh.nine_batch(Uh, hp[None], T9, SIG, False)[0][0]; Tp = T0 + rng.normal(size=9) * SIG
    cp = float(oh.nine_batch(Uh, hp[None], Tp, SIG, False)[1][0])
    r = {"n": n, "|h.h|": float(abs(hp @ hp)), "planted chi2": cp}
    r["v1 noisy"] = oh.search(Uh, H[p], Tp, SIG, False, n_extra=4)[1][0]
    r["v2a noisy"] = v2(Uh, H[p], Tp, False)
    r["v2b noisy"] = v2(Uh, H[p], Tp, True)
    r["v1 exact"] = oh.search(Uh, H[p], T0, SIG, False, n_extra=4)[1][0]
    r["v2b exact"] = v2(Uh, H[p], T0, True)
    rows.append(r)
    print(json.dumps(r), flush=True)
summ = {k: sum(r[f"{k} noisy"] <= r["planted chi2"] + 1e-9 for r in rows) for k in ("v1", "v2a", "v2b")}
summ["v1 exact <= 0.1"] = sum(r["v1 exact"] <= 0.1 for r in rows); summ["v2b exact <= 0.1"] = sum(r["v2b exact"] <= 0.1 for r in rows)
summ["seconds"] = time.time() - t0
print("SUMMARY", json.dumps(summ))
