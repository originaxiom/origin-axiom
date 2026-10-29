"""STRAND A, A1 -- THE CUSP-PREFACTOR MAP (exploratory, data-free; audit room; design: DESIGN.md section 1).
On every slope alpha of order <= 30 where B1788's closed form gives the down quarks and the charged leptons the same
second-generation exponent, the frame's own lepton/down ratios R2 = (m2/m3)_e/(m2/m3)_d and R1 = (m1/m3)_d/(m1/m3)_e are
computed toward the cusp (Im tau 8, 10, 12; Re tau 1/3; two generic offsets b; L clamped beyond B1667's column as in
B1785/B1789; both readings, both horocycles), with B1726's compute unchanged.  A control replaces the charges by the
anomaly-fixed ones for N_c colours (2 N_c Y: Q 1, u -(N_c+1), d N_c-1, L -N_c, e 2 N_c, H N_c) at N_c = 2, 4, 5.
No measured number is read or set beside anything."""
import json, math, sys, pathlib, importlib.util, contextlib, io, os
from fractions import Fraction as F
from multiprocessing import Pool
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
OUT = HERE / "a1_cusp_map.jsonl"


def nn(x): x = x % 1; return min(x, 1 - x)
def e2(qL, qR, a): return F(1, 2) - (nn(2 * qL * a) + nn(2 * qR * a)) / 2
def charges(nc): return {"Q": 1, "u": -(nc + 1), "d": nc - 1, "L": -nc, "e": 2 * nc, "H": nc}


def slopes(nc):
    q = charges(nc); out = []
    for N in range(1, 31):
        for j in range(0, N // 2 + 1):
            a = F(j, N)
            if a.denominator == N and e2(q["Q"], q["d"], a) == e2(q["L"], q["e"], a): out.append(a)
    return out


_C = {}
def mod():
    if not _C:
        spec = importlib.util.spec_from_file_location("c26", ROOT / "frontier/B1726_the_two_ingredients_replicated/verification/census.py")
        C = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(C)
        C._modules(); _C["C"] = C
    return _C["C"]


def task(arg):
    nc, a, b, y = arg
    C = mod(); B = C._M["B"]
    B.SIXY.update(charges(nc))
    try:
        r = C.compute(1.0 / 3.0, y, a, b)
    except Exception as ex:
        return {"nc": nc, "alpha": str(a), "b": b, "Im": y, "error": repr(ex)[:200]}
    row = {"nc": nc, "alpha": str(a), "b": b, "Im": y}
    for h in ("L_max", "L_2"):
        for rn in ("S", "St"):
            d2, d1 = r["down|%s|%s" % (h, rn)]; e2_, e1 = r["lep|%s|%s" % (h, rn)]
            row["%s|%s" % (h, rn)] = {"R2": e2_ / d2 if d2 > 0 else None, "R1": d1 / e1 if e1 > 0 else None, "d": [d2, d1], "e": [e2_, e1]}
    return row


if __name__ == "__main__":
    jobs = []
    for nc in (3, 2, 4, 5):
        for a in slopes(nc):
            for b in (0.137, 0.311):
                for y in (8.0, 10.0, 12.0):
                    jobs.append((nc, a, b, y))
    done = set()
    if OUT.exists():
        for l in OUT.read_text().splitlines():
            r = json.loads(l); done.add((r["nc"], r["alpha"], r["b"], r["Im"]))
    jobs = [j for j in jobs if (j[0], str(j[1]), j[2], j[3]) not in done]
    print("jobs", len(jobs), flush=True)
    with Pool(int(os.environ.get("A1_WORKERS", "4"))) as P, open(OUT, "a") as fh:
        for k, row in enumerate(P.imap_unordered(task, jobs, chunksize=1)):
            fh.write(json.dumps(row) + "\n"); fh.flush()
            if k % 25 == 0: print(k, row.get("nc"), row.get("alpha"), row.get("Im"), flush=True)
    print("done", flush=True)
