"""POST HOC read-out (labelled; not sealed): the CP bit (L192; B1224/B1226: amphichirality forces CS in {0, 1/4}) on the
positive weave to length 18, from T-ROOT's saved output t_root_threads.json (Vol, CS mod pi^2 per Lyndon word).
CS = 1/4 in SnapPy's chern_simons units is pi^2/2 in complex_volume units (m003 = b+-LR sits there; a minus thread)."""
import json, math, pathlib
HERE = pathlib.Path(__file__).resolve().parent
d = json.loads((HERE / "t_root_threads.json").read_text())
PI2 = math.pi ** 2
def lr(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
sym = [w for w in d if lr(swap(w)) in (w, lr(w[::-1]))]
def near(x, t, tol=1e-6): return abs(x - t) < tol
sym_cs0 = [w for w in sym if near(d[w][1], 0)]
sym_quarter = [w for w in sym if near(abs(d[w][1]), PI2 / 2)]
chiral_cs0 = [w for w in d if w not in set(sym) and near(d[w][1], 0)]
chiral_quarter = [w for w in d if w not in set(sym) and near(abs(d[w][1]), PI2 / 2)]
out = {"threads": len(d), "swap_symmetric": len(sym), "swap_symmetric_CS0": len(sym_cs0),
       "swap_symmetric_CS_quarter": sym_quarter, "non_symmetric_CS0": chiral_cs0[:20], "n_non_symmetric_CS0": len(chiral_cs0),
       "non_symmetric_CS_quarter": chiral_quarter[:20],
       "max_abs_CS_on_symmetric": max(abs(d[w][1]) for w in sym)}
(HERE / "post_hoc_cp_bit.json").write_text(json.dumps(out, indent=1) + "\n")
print(json.dumps(out, indent=1))
