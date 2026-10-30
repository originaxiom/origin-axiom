"""THE FINAL ATTACK, step 3 (the approved order; data-free; audit room, 2026-10-30): the rigid-direction census completed on
the menu's other 256 lines.  The menu is the 266 lines of orders 1-12 (points (j/N, k/N) of exact order N, up to sign;
B1713 Part B's enumeration; THE_FINAL_ATTACK § 4, Step B), of which the six's 2/5 family's ten were computed on
2026-10-29 by rigid_census.py (sha256 9c5116649efb372e..., unread).  The same thirteen directions (B1810's declared
DR, a0, R, t = -5/288 and B1730's zero-free F_a at n = 1), the same tau grid (B1726's: Re tau 0.05 ... 0.85, Im tau
2.05 ... 3.45), B1667's two radii, the eight readings, the same evaluator (p449/cm_zero_line.py's rows_at).
STORAGE (main's ruling for the seal's design): every float rounded to 8 significant digits (relative 5e-9, far below any
bar), one gzip file per line (-n: no timestamp), so the census can be committed beside the seal; rounding is checked
against full precision on the first lines by rigid_census_full_menu_check.py.  Nothing is compared with a measured value;
the output is read only by the sealed test.
    RC_WORKERS=12 nice -n 10 python3 -I rigid_census_full_menu.py      # resumable: finished lines are skipped"""
# B1821 (2026-10-30): committed from the audit room as the census's instrument; the only change is the import path, set to this folder.
import gzip, json, math, os, sys, pathlib
from fractions import Fraction as F
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cm_zero_line as Z
OUTDIR = HERE / "full_menu"
RE = (0.05, 0.2, 0.35, 0.55, 0.7, 0.85)
IM = tuple(round(2.05 + 0.1 * k, 2) for k in range(15))
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


MENU = menu()
assert len(MENU) == 266, len(MENU)
DONE_BY_THE_FIRST_RUN = {(F(2, 5), F(k, 10) % 1) for k in range(10)}
REST = [m for m in MENU if (m[1], m[2]) not in DONE_BY_THE_FIRST_RUN]
assert len(REST) == 256, len(REST)


def r8(x):
    if isinstance(x, float): return float("%.8g" % x) if math.isfinite(x) else x
    if isinstance(x, list): return [r8(y) for y in x]
    if isinstance(x, tuple): return [r8(y) for y in x]
    return x


def line_task(m):
    N, a, b = m
    name = "N%02d_%d-%d_%d-%d" % (N, a.numerator, a.denominator, b.numerator, b.denominator)
    path = OUTDIR / (name + ".jsonl.gz")
    if path.exists(): return name, "skipped"
    recs = []
    for re in RE:
        for im in IM:
            try:
                rows = Z.rows_at(complex(re, im), (a, b))
                comp = [[DIRS.index(r["direction"]), ("L_max", "L_2").index(r["radius"]), r["reading"],
                         r8(r["up"]), r8(r["down"]), r8(r["lepton"]), r8(r["V"]), r8(r["J"]), r["V defined"]] for r in rows]
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
    print("menu", len(MENU), "rest", len(REST), flush=True)
    with Pool(int(os.environ.get("RC_WORKERS", "8"))) as P:
        for n, (name, what) in enumerate(P.imap_unordered(line_task, REST, chunksize=1)):
            print(n, name, what, flush=True)
    print("done", flush=True)
