"""B1729 (P-305; data-free, no measured number is read): the frame's own lepton-to-down relation by line order.
Run once in the audit room (2026-10-23, after S192's push, with its reading criteria written first); moved here unchanged
except this docstring and the root lookup.
On a line of exact order N the leptons' twists are 3 x those of the charge pair (-1, 2), so where 3 | N the leptons
see a line of order N/3 while the quarks see N.  For every line of exact order N in {5, 10, 13, ..., 30} (up to
sign), at two tau of B1726's band (0.55 + 3.05i, 0.35 + 2.75i), both horocycles, down and leptons in one reading
(S or S~, as every menu of B1726 pairs them): the frame's R2 = (m2/m3)_lep / (m2/m3)_down and
R1 = (m1/m3)_down / (m1/m3)_lep.  Reports the quantiles of log R2 and log R1 by order, split by 3 | N.
Check: on order-5 lines R2 = R1 = 1 exactly (B1728, B1726).  (The coarser-line identity needs no check: twist_of of
the pair (-1, 2) at 3w is the leptons' twist at w by definition.)
    python3 -B frame_r2r1.py [--workers 8]      # writes frame_r2r1.json beside itself"""
import sys, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
import census as K
ORDERS = [5, 10] + list(range(13, 31))
TAUS = ((0.55, 3.05), (0.35, 2.75))


def lines_of(N):
    seen, out = set(), []
    for j in range(N):
        for k in range(N):
            if math.gcd(math.gcd(j, k), N) != 1: continue
            a, b = Fr(j, N), Fr(k, N); key = min((a, b), ((-a) % 1, (-b) % 1))
            if key in seen: continue
            seen.add(key); out.append(key)
    return out


def one(task):
    N, (re_t, im_t), a, b = task
    r = K.compute(re_t, im_t, a, b); out = []
    for h in ("L_max", "L_2"):
        for rd in ("S", "St"):
            d, e = r["down|%s|%s" % (h, rd)], r["lep|%s|%s" % (h, rd)]
            if min(d + e) < 1e-12: out.append(None); continue
            out.append([math.log(e[0] / d[0]), math.log(d[1] / e[1])])
    return N, out


def main():
    from multiprocessing import Pool
    nw = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    tasks = [(N, t, a, b) for N in ORDERS for t in TAUS for (a, b) in lines_of(N)]
    print(len(tasks), "points", flush=True)
    by = {N: [] for N in ORDERS}; masked = {N: 0 for N in ORDERS}
    with Pool(nw) as P:
        for N, out in P.imap_unordered(one, tasks, chunksize=4):
            for v in out:
                if v is None: masked[N] += 1
                else: by[N].append(v)
    res = {}
    for N in ORDERS:
        A = np.array(by[N])
        if not len(A): res[N] = {"n": 0, "masked": masked[N]}; continue
        q = lambda x: [float(np.quantile(x, p)) for p in (0.05, 0.25, 0.5, 0.75, 0.95)]
        res[N] = {"n": len(A), "masked": masked[N], "3|N": N % 3 == 0,
                  "logR2_q": q(A[:, 0]), "logR1_q": q(A[:, 1]), "max_abs_log_order5_check": float(np.max(np.abs(A))) if N == 5 else None}
    json.dump({"orders": ORDERS, "taus": TAUS, "by_order": res}, open(HERE / "frame_r2r1.json", "w"), indent=1)
    for N in ORDERS:
        r = res[N]
        if r["n"]: print(N, "3|N" if N % 3 == 0 else "   ", r["n"], "median logR2 %.3f logR1 %.3f" % (r["logR2_q"][2], r["logR1_q"][2]))


if __name__ == "__main__":
    main()
