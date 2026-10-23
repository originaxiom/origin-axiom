import importlib.util, json, sys, math, time, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("rt", HERE / "reading_test.py"); rt = importlib.util.module_from_spec(spec); sys.modules["rt"] = rt; spec.loader.exec_module(rt)
sms = rt.sms; T9, SIG = rt.T9, rt.SIG
st = np.load(HERE / "reading_test_store.npz"); U, H = st["U"], st["H"]
rng = np.random.default_rng(1741)
ok = 0; t0 = time.time()
for n in range(24):
    p = int(rng.integers(0, 20)); hr = int(rng.integers(0, 2))
    if n < 12:
        t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
        h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
        hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
    else:
        z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
    hp = hp / np.linalg.norm(hp)
    Uh = U[p, :, hr]
    Tp = sms.nine_batch(Uh, hp[None], T9, SIG)[0][0] + rng.normal(size=9) * SIG
    cp = float(sms.nine_batch(Uh, hp[None], Tp, SIG)[1][0])
    g, (c, x) = sms.search(Uh, H[p], Tp, SIG, n_extra=4)
    good = c <= cp + 1e-9; ok += good
    print(f"n {n:2d} {'conic' if n < 12 else 'unif '} |hh| {abs(hp @ hp):.1e} planted chi2 {cp:6.2f} grid {g:7.2f} found {c:7.3f} {'ok' if good else 'MISS'}", flush=True)
print("ok", ok, "of 24;", (time.time() - t0) / 24, "s per row")
