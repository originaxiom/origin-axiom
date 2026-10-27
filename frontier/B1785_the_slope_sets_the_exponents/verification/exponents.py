"""B1785 (main's plan, step 1 groundwork; DATA-FREE; no measured value is read): the frame's hierarchy exponents as functions of the line.
For every flat line on record (B1713's 266 of order <= 12 and B1755's 396 of order 13, 14, 15, 20), B1726's sealed
compute() at Re tau = 1/3 and Im tau = 4, 5, 6; for each sector and reading and horocycle, the exponent of each mass
ratio, e = -d ln(ratio) / d(2 pi Im tau), by a least-squares line through the three heights (and the residual of that
line, to see where the leading power has not set in).  Writes exponents.json."""
import sys, json, math, pathlib, importlib.util
from multiprocessing import Pool
import numpy as np
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
HEIGHTS = (4.0, 5.0, 6.0)
RE = 1.0 / 3.0


def _load(name, rel):
    if name not in sys.modules:
        sp = importlib.util.spec_from_file_location(name, ROOT / rel); m = importlib.util.module_from_spec(sp); sys.modules[name] = m; sp.loader.exec_module(m)
    return sys.modules[name]


def K(): return _load("b1726_census", "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
def L55(): return _load("b1755_census", "frontier/B1755_the_six_on_the_lines_of_order_13_to_20/verification/census.py")


def lines():
    out = [(str(a), str(b)) for a, b in K().lines()] + [(str(a), str(b)) for a, b in L55().lines()]
    seen, res = set(), []
    for l in out:
        if l not in seen: seen.add(l); res.append(l)
    return res


def one(line):
    from fractions import Fraction as Fr
    a, b = Fr(line[0]), Fr(line[1]); rows = [K().compute(RE, y, a, b) for y in HEIGHTS]
    X = np.array([2 * math.pi * y for y in HEIGHTS]); out = {"alpha": line[0], "b": line[1], "order": math.lcm(a.denominator, b.denominator)}
    for key in rows[0]:
        if not key.startswith(("up|", "down|", "lep|")): continue
        for i, name in enumerate(("m2/m3", "m1/m3")):
            Y = np.log(np.maximum([r[key][i] for r in rows], 1e-300))
            A = np.vstack([X, np.ones(3)]).T; (s, c), res, *_ = np.linalg.lstsq(A, Y, rcond=None)
            out["%s|%s" % (key, name)] = {"exponent": float(-s), "resid": float(np.max(np.abs(A @ np.array([s, c]) - Y)))}
    return out


if __name__ == "__main__":
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    L = lines(); print(len(L), "lines", flush=True)
    with Pool(nw) as P: res = P.map(one, L, chunksize=4)
    json.dump(res, open(pathlib.Path(__file__).resolve().parent / "exponents.json", "w"), indent=1)
    print("exponents exit 0")
