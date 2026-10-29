"""P-483: B1633's W4 comparison recounted on main.  One count per primitive thread (a primitive cyclic word in L, R, up to
rotation) of length 2..12, with B1633's own group and projectors (B1611's cp module, as B1633 imports it): does the thread's
lift have a non-zero fixed space on T?  Also by length, and the per-length fraction over ALL words (B1633's W4 quantity)."""
import importlib.util, json, pathlib, itertools
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
spec = importlib.util.spec_from_file_location("cp", ROOT / "frontier/B1611_is_cp_violation_forced_on_the_weave/verification/cp_on_the_weave.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)
G = cp.Group([cp.W.ML, cp.W.MR])
T = [cp.restrict(M, cp.TB) for M in G.els]
fixdim = [sum(1 for v in np.linalg.eigvals(M) if abs(v - 1) < 1e-9) for M in T]
iL = G.idx[cp.key(cp.W.ML)]; iR = G.idx[cp.key(cp.W.MR)]
e = next(g for g in range(G.n) if np.allclose(G.els[g], np.eye(G.els[g].shape[0]), atol=1e-9))
def lift(word):
    g = e
    for ch in word: g = G.mult[g][iL if ch == "L" else iR]
    return g
def primitive_necklaces(n):
    seen = set(); out = []
    for w in itertools.product("LR", repeat=n):
        s = "".join(w); rots = [s[k:] + s[:k] for k in range(n)]; m = min(rots)
        if m in seen: continue
        seen.add(m)
        if len(set(rots)) == n: out.append(m)
    return out
res = {}; tot = 0; zm = 0
for n in range(2, 13):
    neck = primitive_necklaces(n); z = sum(1 for w in neck if fixdim[lift(w)] > 0)
    allw = ["".join(w) for w in itertools.product("LR", repeat=n)]; za = sum(1 for w in allw if fixdim[lift(w)] > 0)
    res[n] = {"primitive threads": len(neck), "with zero modes": z, "all words": len(allw), "all words with zero modes": za, "fraction (all words)": za / len(allw)}
    tot += len(neck); zm += z
    print(n, res[n], flush=True)
res["lengths 2-12"] = {"primitive threads": tot, "with zero modes": zm, "fraction": zm / tot,
                       "even lengths": {"threads": sum(res[n]["primitive threads"] for n in range(2, 13, 2)), "with zero modes": sum(res[n]["with zero modes"] for n in range(2, 13, 2))}}
print(res["lengths 2-12"])
json.dump({str(k): v for k, v in res.items()}, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
# the seat's census (its W42 Part B): both extensions +-g of the record's lifts; a thread counts if either has a fixed vector on T,
# i.e. if T(g) has an eigenvalue +1 or -1.  Is -g in the group (z -> -z keeps z^4)?  Checked, then counted.
negs = sum(1 for g in range(G.n) if any(np.allclose(G.els[h], -G.els[g], atol=1e-9) for h in range(G.n)))
pm = [sum(1 for v in np.linalg.eigvals(M) if abs(v - 1) < 1e-9 or abs(v + 1) < 1e-9) for M in T]
either = 0; byn = {}
for n in range(2, 13):
    neck = primitive_necklaces(n); z = sum(1 for w in neck if pm[lift(w)] > 0); byn[n] = z; either += z
print("-g in G for", negs, "of", G.n, "elements; threads with zero modes in either extension (lengths 2-12):", either, byn)
d = json.load(open(pathlib.Path(__file__).with_suffix(".json"))); d["the seat's count (either extension +-g)"] = {"total": either, "by length": byn, "-g in G": negs}
json.dump(d, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
