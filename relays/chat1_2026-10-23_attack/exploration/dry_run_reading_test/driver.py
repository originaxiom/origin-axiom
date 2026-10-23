"""Code-path test of reading_test.py on TWO_HIGGS's stored rows (post hoc rows, compared with the data before)."""
import importlib.util, json, sys, time, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("rt", HERE / "reading_test.py"); rt = importlib.util.module_from_spec(spec); sys.modules["rt"] = rt; spec.loader.exec_module(rt)
rt.LINES = [("N=5" if k % 2 == 0 else "N=10", Fr(2, 5), Fr(k, 10)) for k in range(10)]
rt.RE = [0.0625]; rt.IM = [2.0, 3.5]; rt.RE_MIRROR = 0.9375
tasks = rt.grid()
st = np.load(HERE / "channel_store_two_higgs.npz"); I = json.loads((HERE / "channel_store_two_higgs_index.json").read_text())
idx = {(t[0], round(t[1], 6), round(t[2], 6)): i for i, t in enumerate(I["tasks"])}
sel = [idx[(k, round(r, 6), round(y, 6))] for k, r, y in tasks]
np.savez_compressed(HERE / "reading_test_store.npz", U=st["U"][sel], H=st["H"][sel])
(HERE / "reading_test_store_index.json").write_text(json.dumps({"tasks": tasks, "lines": [[t, str(a), str(b)] for t, a, b in rt.LINES],
                                                               "sectors": rt.cs.SECTORS, "hors": rt.cs.HORS, "dirs": rt.DIRS}) + "\n")

t0 = time.time(); rt.c0(); print("c0", time.time() - t0)
t0 = time.time(); rt.scan(2); print("scan", time.time() - t0)
# c2 with the fake grid: n_main = len(LINES) * len(RE) * len(IM) = 20
t0 = time.time(); rt.c2(); print("c2", time.time() - t0)
rt.cells()
print(json.dumps(json.load(open(HERE / "reading_test_c0.json")), indent=1))
c = json.load(open(HERE / "reading_test_cells.json")); print({k: v for k, v in c.items() if k != "the twenty lowest rows"})
print(json.load(open(HERE / "reading_test_c2.json"))["C2 recovered (chi2 <= 0.1 against the planted targets)"])
