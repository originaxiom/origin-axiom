"""Code-path check (post hoc rows of TWO_HIGGS's grid, compared with the data before): sm_search.search with n_extra = 4
against search_check.py's full-start minima on every sixth of its P2 rows (ten rows); timing per row."""
import importlib.util, sys, json, time, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[2]     # the attack folder (written as an absolute path when it ran)
sys.argv = ["x"]
s = importlib.util.spec_from_file_location("ih", A / "inverse_higgs.py"); ih = importlib.util.module_from_spec(s); s.loader.exec_module(ih)
s2 = importlib.util.spec_from_file_location("sms", A / "sm_search.py"); sms = importlib.util.module_from_spec(s2); s2.loader.exec_module(sms)
st = np.load(A / "channel_store_two_higgs.npz"); U, H = st["U"], st["H"]
d = json.load(open(A / "search_check.json")); P2 = d["P2 rows"]; HORS = ["L_max", "L_2"]
t0 = time.time(); out = []
for x in P2[0:60:6]:
    p = x["p"]; hr = HORS.index(x["hor"])
    g, (c, _) = sms.search(U[p, :, hr], H[p], ih.T9, ih.SIG, n_extra=4); out.append((round(x["new min"], 2), round(c, 2)))
print("full starts vs n_extra = 4:", out); print("s/row", (time.time() - t0) / len(out))
