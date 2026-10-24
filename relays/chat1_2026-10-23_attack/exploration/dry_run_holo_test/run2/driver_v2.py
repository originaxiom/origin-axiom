"""Code-path dry run of holo_test.py on TWO_HIGGS's stored rows (post hoc rows, compared with the data before)."""
import importlib.util, json, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("ht", HERE / "holo_test.py"); ht = importlib.util.module_from_spec(spec); sys.modules["ht"] = ht; spec.loader.exec_module(ht)
ht.LINES = [("N=5" if k % 2 == 0 else "N=10", Fr(2, 5), Fr(k, 10)) for k in range(10)]
ht.RE = [0.0625]; ht.IM = [2.0, 2.1]; ht.RE_MIRROR = 0.9375
ht.K1, ht.K2 = 10, 20; ht.RT = ht.random_targets(10); ht.RT2 = ht.random_targets(20); ht.RT2[:, 4] = ht.RT2[:, 2] + (ht.T9[4] - ht.T9[2]); ht.RT2[:, 5] = ht.RT2[:, 3] + (ht.T9[5] - ht.T9[3]); ht.TALL = np.concatenate([ht.T9[None], ht.RT, ht.RT2])
tasks = ht.grid()
st = np.load(HERE / "channel_store_two_higgs.npz"); I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text())
idx = {(t[0], round(t[1], 6), round(t[2], 6)): i for i, t in enumerate(I["tasks"])}
sel = [idx[(k, round(r, 6), round(y, 6))] for k, r, y in tasks]
np.savez_compressed(HERE / "holo_store.npz", U=st["U"][sel], H=st["H"][sel])
(HERE / "holo_store_index.json").write_text(json.dumps({"tasks": tasks, "lines": [[t, str(a), str(b)] for t, a, b in ht.LINES],
                                                       "sectors": ht.cs.SECTORS, "hors": ht.cs.HORS, "dirs": ht.DIRS}) + "\n")
for name, fn in (("c0", ht.c0), ("scan", lambda: ht.scan(2)), ("calib", lambda: ht.calib(2)), ("cells", ht.cells)):
    t0 = time.time(); fn(); print(name, round(time.time() - t0, 1), "s", flush=True)
c = json.load(open(HERE / "holo_cells.json")); print({k: v for k, v in c.items() if k not in ("the twenty lowest rows", "every row below 21.67")})
cal = json.load(open(HERE / "holo_calib.json")); print({k: v for k, v in cal.items() if not k.startswith("statistics")})
