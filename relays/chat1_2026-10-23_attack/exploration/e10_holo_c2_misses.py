"""Data-free diagnosis (labelled; committed before its run): why did the holomorphic test's search miss three of C2's
planted near-solutions (holo_c2.json)?  The planted rows are regenerated from C2's seed (1744) on the test's store; for
each miss: the planted direction's tube coordinates, its distance to the nearest grid direction, the grid's chi2 at that
nearest direction, the grid's minimum, and refinement from the planted direction itself and from its nearest grid
direction (no data: targets are the model's nine at the planted direction, with and without C2's noise)."""
import contextlib, importlib.util, io, json, math, sys, pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parents[1]
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("ht", HERE / "holo_test.py"); ht = importlib.util.module_from_spec(spec); sys.modules["ht"] = ht
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(ht)
oh, T9, SIG = ht.oh, ht.T9, ht.SIG
ht._init(); U, H = ht.G["U"], ht.G["H"]
c2 = json.loads((HERE / "holo_c2.json").read_text())["C2 rows"]
rng = np.random.default_rng(1744)
out = []
for n in range(36):
    p = int(rng.integers(0, ht.n_main())); hr = int(rng.integers(0, 2))
    if n < 12:
        t = complex(*rng.normal(size=2)); r = 10 ** rng.uniform(-4, -1); ph = rng.uniform(0, 2 * math.pi)
        h0 = np.array([2 * t, 1 - t * t, 1j * (1 + t * t)]); h0 /= np.linalg.norm(h0)
        hp = h0 + r * np.exp(1j * ph) * np.conj(h0)
    elif n < 24:
        lead, other = (oh.F3, oh.F1) if n < 18 else (oh.F1, oh.F3)
        de = 0.25 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
        ep = 0.03 * math.sqrt(rng.uniform()) * np.exp(2j * math.pi * rng.uniform())
        hp = lead + de * oh.F2 + ep * other
    else:
        z = rng.normal(size=6); hp = z[:3] + 1j * z[3:]
    hp = hp / np.linalg.norm(hp)
    Uh = U[p, :, hr]
    T0 = oh.nine_batch(Uh, hp[None], T9, SIG, False)[0][0]
    Tp = T0 + rng.normal(size=9) * SIG
    assert p == c2[n]["p"]
    if c2[n]["met"]:
        continue
    ov = np.abs(oh.HS.conj() @ hp); j = int(np.argmax(ov))
    ch = oh.nine_batch(Uh, oh.HS, T0, SIG, False)[1]
    r_pl = oh.refine(Uh, np.concatenate([hp.real, hp.imag]), T0, SIG, False)
    r_nn = oh.refine(Uh, np.concatenate([oh.HS[j].real, oh.HS[j].imag]), T0, SIG, False)
    out.append({"C2 index": n, "kind": c2[n]["kind"], "|h.h| planted": float(abs(hp @ hp)),
                "FS distance to the nearest grid direction (rad)": float(math.acos(min(1.0, ov[j]))),
                "exact targets: grid chi2 at that direction": float(ch[j]), "exact targets: grid minimum": float(ch.min()),
                "exact targets: refined from the planted direction": r_pl[0] if r_pl else None,
                "exact targets: refined from its nearest grid direction": r_nn[0] if r_nn else None,
                "exact targets: rank of the nearest grid direction among the grid": int((ch < ch[j]).sum()) + 1,
                "C2's found (noisy, exact)": [c2[n]["found (noisy)"], c2[n]["found (noiseless)"]]})
print(json.dumps(out, indent=1))
