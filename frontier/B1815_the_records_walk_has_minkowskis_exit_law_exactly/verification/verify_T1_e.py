"""Main's regeneration of T1's check (e): B1666's per-thread quantity f (its _thread, unchanged, imported read-only)
averaged over threads ordered by WORD LENGTH (every Lyndon word of exactly length n with both letters), plain and
length-weighted; and, as the control, over threads ordered by trace (B1666's own enumeration) to reproduce 0.315."""
import importlib.util, glob, math, itertools, sys, io, contextlib
import pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
p = str(next(ROOT.glob("frontier/B1666_*/verification/the_layers_robust.py")))
sp = importlib.util.spec_from_file_location("lr", p); lr = importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(lr)
def mat(w):
    M = [[1, 0], [0, 1]]
    for ch in w:
        A = [[1, 1], [0, 1]] if ch == "L" else [[1, 0], [1, 1]]
        M = [[M[0][0]*A[0][0]+M[0][1]*A[1][0], M[0][0]*A[0][1]+M[0][1]*A[1][1]], [M[1][0]*A[0][0]+M[1][1]*A[1][0], M[1][0]*A[0][1]+M[1][1]*A[1][1]]]
    return M
def lyndon(n):
    for t in itertools.product("LR", repeat=n):
        w = "".join(t)
        if "L" in w and "R" in w and all(w < w[i:] + w[:i] for i in range(1, n)): yield w
for n in (10, 12, 14):
    fs, ws = [], []
    for w in lyndon(n):
        M = mat(w); t = M[0][0] + M[1][1]; f = lr._thread((w, t))["f"]; fs.append(f); ws.append(2 * math.acosh(t / 2))
    m = sum(fs) / len(fs); mw = sum(f * x for f, x in zip(fs, ws)) / sum(ws)
    sd = (sum((f - m) ** 2 for f in fs) / (len(fs) - 1)) ** 0.5 / len(fs) ** 0.5
    print("by word length n = %d: threads %d, mean f %.4f +- %.4f, length-weighted %.4f" % (n, len(fs), m, sd, mw), flush=True)
th = lr.threads_upto(200); fs = [lr._thread(x)["f"] for x in th]
print("control by trace <= 200 (B1666's own enumeration): threads %d, mean f %.4f" % (len(fs), sum(fs) / len(fs)))
