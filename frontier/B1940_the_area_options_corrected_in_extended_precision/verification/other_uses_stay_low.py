"""P-853's Q3 (main, 2026-11-15): does any other use of the double-precision frame reach the heights where it fails (the
identity F-bar(tau + 1) = F-bar(tau) holds to 1e-5 at 9 and fails above about 11; B1940 section 1)?
- the grid read-outs (B1928's fiber_grid, B1932's fiber_grid_t90, used by B1928, B1932's move-count options and B1938):
  their heights, read from the committed grid files;
- B1924's thread averages, which evaluate the frame along closed geodesics: every word of length 12 and 16 with both
  letters (exhaustive), and the words of its n = 22 and 28 runs regenerated from their fixed seeds with B1924's own
  keeps_mark; the height of a closed geodesic is the largest radius sqrt(tr^2 - 4) / (2 |c|) over the word's rotations;
- the point evaluations of B1935 (heights 1.07 to 1.62) and B1942 (1.5 to 3.6) are read from their scripts.
Prints the largest height of each."""
import sys, json, math, random, itertools, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
B24 = next((ROOT / "frontier").glob("B1924_*")) / "verification"
sys.path.insert(0, str(B24)); _a = sys.argv; sys.argv = ["x"]
import thread_average as T
sys.argv = _a
for name in ("B1928_*/verification/fiber_grid.json", "B1928_*/verification/fiber_grid_fine.json", "B1932_*/verification/fiber_grid_t90.json"):
    for f in (ROOT / "frontier").glob(name):
        d = json.loads(f.read_text()); g = d["grid"] if isinstance(d, dict) and "grid" in d else d
        print("%s: the grid's top height %.3f" % (f.relative_to(ROOT), max(p["tau"][1] for p in g)))


def top(w):
    h = 0.0
    for r in range(len(w)):
        a, b, c, d = (int(x) for x in T.word_matrix(w[r:] + w[:r]).ravel())
        D = (a + d) ** 2 - 4
        for cc in (b, c):
            if D > 0 and cc:
                h = max(h, math.sqrt(D) / (2 * abs(cc)))
    return h


for n in (12, 16):
    m = max(top("".join(t)) for t in itertools.product("LR", repeat=n) if "L" in t and "R" in t)
    print("every word of length %d with both letters: the highest geodesic %.3f (L^(n-1) R: %.3f)" % (n, m, math.sqrt((n + 1) ** 2 - 4) / 2))
for label, n, seed in (("B1924 whole_average_3, n = 22", 22, 8453), ("B1924 whole_average_4, n = 28", 28, 8454), ("B1924 whole_average_4, n = 22b", 22, 8455)):
    rng = random.Random(seed); ws = []
    while len(ws) < 60:
        w = "".join(rng.choice("LR") for _ in range(n))
        if "L" in w and "R" in w and T.keeps_mark(w):
            ws.append(w)
    print("%s: 60 words regenerated from the seed, the highest geodesic %.3f" % (label, max(top(w) for w in ws)))
