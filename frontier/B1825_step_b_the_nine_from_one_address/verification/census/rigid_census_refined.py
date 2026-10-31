"""THE FINAL ATTACK, Step B's refined census (data-free; REFINED_CENSUS_PLAN.md § 6, the second pre-seal review's grid;
P-521).  B1810's thirteen directions on all 266 lines of orders 1-12, both radii, the eight readings, the evaluator committed
in B1821 (cm_zero_line.rows_at), on:
  - Im tau = 1.0 + 0.05 k, k = 0..60 (the evaluator's radius column, Re tau = 1/4), Re tau = 0, 0.05, ..., 0.5;
  - a 0.025 x 0.025 sub-block on Im tau 1.0-1.5 x Re tau 0-0.5 (the extra points only).
Re tau in [0, 1/2] suffices by the mirror (B1821).  Every float rounded to 8 significant digits; one gzip file per line
(-n: no timestamp); resumable (a finished line is skipped); a guard refuses |Re tau| >= 1 (the F_a sections' theta_2 branch,
the second review).  Nothing is compared with a measured value; the output is read only through committed aggregate
tools before the seal, and by the sealed test.
    RC_WORKERS=8 nice -n 10 python3 -I rigid_census_refined.py      # the owner's eight-core rule"""
import gzip, json, math, os, sys, pathlib
from fractions import Fraction as F
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
EVAL = ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"
sys.path.insert(0, str(EVAL))
import cm_zero_line as Z
OUTDIR = HERE / "refined"
MAIN = [(round(0.05 * i, 4), round(1.0 + 0.05 * k, 4)) for i in range(11) for k in range(61)]
SUB = sorted({(round(0.025 * i, 4), round(1.0 + 0.025 * k, 4)) for i in range(21) for k in range(21)} - set(MAIN))
GRID = MAIN + SUB
assert len(MAIN) == 671 and len(SUB) == 320, (len(MAIN), len(SUB))
assert all(abs(re) < 1 for re, _ in GRID)
DIRS = Z.DIRS


def menu():
    seen, out = set(), []
    for N in range(1, 13):
        for j in range(N):
            for k in range(N):
                if math.gcd(math.gcd(j, k), N) != 1: continue
                a, b = F(j, N), F(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
                if key in seen: continue
                seen.add(key); out.append((N, key[0], key[1]))
    return out


MENU = menu(); assert len(MENU) == 266


def r8(x):
    if isinstance(x, float): return float("%.8g" % x) if math.isfinite(x) else x
    if isinstance(x, (list, tuple)): return [r8(y) for y in x]
    return x


def line_task(m):
    N, a, b = m
    name = "N%02d_%d-%d_%d-%d" % (N, a.numerator, a.denominator, b.numerator, b.denominator)
    path = OUTDIR / (name + ".jsonl.gz")
    if path.exists(): return name, "skipped"
    recs = []
    for re, im in GRID:
        assert abs(re) < 1
        try:
            rows = Z.rows_at(complex(re, im), (a, b))
            comp = [[DIRS.index(r["direction"]), ("L_max", "L_2").index(r["radius"]), r["reading"],
                     r8(r["up"]), r8(r["down"]), r8(r["lepton"]), r8(r["V"]), r8(r["J"]), r["V defined"]] for r in rows]
            assert len(comp) == 208, len(comp)
            recs.append({"line": [str(a), str(b)], "order": N, "tau": [re, im], "rows": comp})
        except Exception as ex:
            recs.append({"line": [str(a), str(b)], "order": N, "tau": [re, im], "error": repr(ex)[:200]})
    tmp = path.with_suffix(".tmp")
    with open(tmp, "wb") as raw, gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=9) as fh:
        for r in recs: fh.write((json.dumps(r) + "\n").encode("utf-8"))
    os.replace(tmp, path)
    return name, "%d configurations, %d errors" % (len(recs), sum(1 for r in recs if "error" in r))


if __name__ == "__main__":
    OUTDIR.mkdir(exist_ok=True)
    print("menu", len(MENU), "grid", len(GRID), "configurations", len(MENU) * len(GRID), flush=True)
    with Pool(int(os.environ.get("RC_WORKERS", "8"))) as P:
        for n, (name, what) in enumerate(P.imap_unordered(line_task, MENU, chunksize=1)):
            print(n, name, what, flush=True)
    print("done", flush=True)
