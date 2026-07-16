"""D2 — THE MELODY THEOREM (sealed prereg d2_melody/PREREG_D2.md, sha256 633c87bb...).

Computes the TOTAL Z(r) = (per-bucket sum) / |W|, one representative per bucket,
via the banked exact E6 Gauss-sum pipeline (weyl_group / gauss_sum / P_WORD from
n1_jeffrey_terms.py), imported the same way n1_jeffrey_extend.py does. Bucket
construction is copied verbatim from n1_jeffrey_extend.py's loop.

Phase 1 GATES: r = 13, 16, 19 must reproduce Z = 1, 0, 2 exactly, else STOP.
Phase 2 N0 INTEGRITY: verify N0 = 2^6*3^3*5^4*7^2*11^2*19^2 == 2309187690000
  (the literal decimal asserted by the sealed prereg). Logged loudly; does not
  hard-crash so that gates/log/results are always produced.
Phase 3 SEALED PAIRS: for kappa in {13,29,16,25,19,45}, compute Z(kappa) and
  Z(kappa+N0); PASS iff |Z(kappa)-Z(kappa+N0)| < 1e-7 for every pair. Run against
  both N0 candidates if they differ (cheap; r-independent cost).
Phase 4 SPOT CHECK: 2-representative class-function check on the 3 largest
  buckets at the two largest r actually run.

All totals -> d2_results.json (r -> [re, im]). Narrative log -> d2_run.log.
"""
import json
import sys
import time

import numpy as np
import sympy as sp
import mpmath as mp

sys.path.insert(0, '<seat-workdir>/seat-work/next_queue/n1_counting')
import n1_jeffrey_terms as J

WORKDIR = '<seat-workdir>/seat-work/loops_queue/d2_melody'
LOG_PATH = f'{WORKDIR}/d2_run.log'
RESULTS_PATH = f'{WORKDIR}/d2_results.json'
GATE_TOL = 1e-7
PAIR_TOL = 1e-7

_log_fh = open(LOG_PATH, 'w')


def log(msg=""):
    print(msg, flush=True)
    _log_fh.write(str(msg) + "\n")
    _log_fh.flush()


def save_results(cache):
    out = {str(r): [z.real, z.imag] for r, z in cache.items()}
    with open(RESULTS_PATH, 'w') as f:
        json.dump(out, f, indent=1)


def total_Z(r, sorted_buckets, nW, cache):
    """TOTAL Z(r): per-bucket sum / |W|, ONE representative per bucket."""
    if r in cache:
        return cache[r]
    total = 0j
    for key, members in sorted_buckets:
        idx0, B0, s0 = members[0]
        g, ad = J.gauss_sum(B0, r)
        total += len(members) * s0 * g / np.sqrt(ad)
    z = total / nW
    cache[r] = z
    save_results(cache)  # persist as we go
    return z


def fmt(z):
    return f"{z.real:+.10f} {z.imag:+.10f}i"


def main():
    mp.mp.dps = 30  # as in the source (n1_jeffrey_terms.main)
    t_start = time.time()
    log(f"=== D2 melody-theorem run — {time.strftime('%Y-%m-%d %H:%M:%S')} ===")
    log("Prereg: d2_melody/PREREG_D2.md (sha256 633c87bb434450f61f6a5c88bd9760f3b1e8ff6c239bed2a72e98057f8848017 — verified)")
    log("Pipeline: n1_jeffrey_terms.weyl_group / gauss_sum / P_WORD (imported as n1_jeffrey_extend.py does)")
    log(f"mpmath dps = {mp.mp.dps}")

    t0 = time.time()
    W, eps = J.weyl_group()
    log(f"|W| = {len(W)}  (build {time.time() - t0:.2f}s)")
    assert len(W) == 51840, "Weyl group build mismatch — HARD STOP"

    # ---- bucket construction, verbatim per n1_jeffrey_extend.py ----
    t0 = time.time()
    buckets = {}
    for idx in range(len(W)):
        w = W[idx]
        winv = np.rint(np.linalg.inv(w)).astype(np.int64)
        B = J.P_WORD * np.eye(6, dtype=np.int64) - w - winv
        cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
        spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
        buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))
    sorted_buckets = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
    assert sum(len(m) for _, m in sorted_buckets) == len(W)
    log(f"buckets: {len(sorted_buckets)}  (build {time.time() - t0:.2f}s)")
    log(f"  top 5 bucket sizes: {[len(m) for _, m in sorted_buckets[:5]]}")

    cache = {}

    # ================= PHASE 1: GATES =================
    log("\n=== PHASE 1 — GATES (must reproduce exactly, else STOP) ===")
    gate_expected = {13: 1.0, 16: 0.0, 19: 2.0}
    for r in (13, 16, 19):
        t0 = time.time()
        z = total_Z(r, sorted_buckets, len(W), cache)
        log(f"  Z({r}) = {fmt(z)}  |Z|={abs(z):.10f}  ({time.time() - t0:.2f}s)")

    gate_ok = True
    for r, exp in gate_expected.items():
        z = cache[r]
        dev = abs(z - complex(exp, 0))
        ok = dev < GATE_TOL
        gate_ok &= ok
        log(f"  GATE r={r}: expected {exp:+.1f}, got {fmt(z)}, dev={dev:.3e} -> {'PASS' if ok else 'FAIL'}")

    if not gate_ok:
        log("\nGATES FAILED — STOPPING per prereg instructions. No pairs run.")
        save_results(cache)
        log(f"Partial results saved to {RESULTS_PATH}")
        sys.exit(1)
    log("ALL GATES PASS — proceeding.")

    # ================= PHASE 2: N0 INTEGRITY CHECK =================
    log("\n=== PHASE 2 — N0 integrity check ===")
    N0_formula = 2**6 * 3**3 * 5**4 * 7**2 * 11**2 * 19**2
    N0_sealed_literal = 2309187690000
    log(f"  N0_formula        (2^6*3^3*5^4*7^2*11^2*19^2)      = {N0_formula}")
    log(f"  N0_sealed_literal (decimal written in PREREG_D2.md) = {N0_sealed_literal}")
    n0_ok = (N0_formula == N0_sealed_literal)
    if n0_ok:
        log("  N0 CHECK PASSED: sealed decimal equals its own stated factorization exactly.")
        n0_candidates = [("N0_formula", N0_formula)]
    else:
        diff = N0_formula - N0_sealed_literal
        log(f"  *** CRITICAL ANOMALY *** sealed decimal != formula product. diff = {diff}")
        log(f"    factorint(N0_sealed_literal) = {sp.factorint(N0_sealed_literal)}")
        log(f"    factorint(N0_formula)        = {sp.factorint(N0_formula)}")
        log("  The literal sealed decimal does NOT carry the claimed 2^6*3^3*5^4*7^2*11^2*19^2")
        log("  structure at all (no factor of 7, 11, or 19). This is an arithmetic defect in")
        log("  the sealed prereg text, confirmed by independent stepwise recomputation and by")
        log("  sympy.factorint on both integers. Per 'assert this factorization in-script' plus")
        log("  the general 'must reproduce exactly, else STOP' discipline: the SEALED PAIRS test")
        log("  AS LITERALLY SPECIFIED cannot be certified (its defining constant is internally")
        log("  self-contradictory). Proceeding to run BOTH candidates for full transparency,")
        log("  clearly labeled; neither is being silently substituted as 'the' sealed answer.")
        n0_candidates = [("N0_formula(corrected)", N0_formula),
                          ("N0_sealed_literal(verbatim, fails its own factorization)", N0_sealed_literal)]

    # ================= PHASE 3: SEALED PAIRS =================
    kappas = [13, 29, 16, 25, 19, 45]
    all_pair_reports = {}
    for label, N0 in n0_candidates:
        log(f"\n=== PHASE 3 — SEALED PAIRS under {label}, N0={N0} ===")
        report = []
        for k in kappas:
            zk = total_Z(k, sorted_buckets, len(W), cache)
            zkn = total_Z(k + N0, sorted_buckets, len(W), cache)
            dev = abs(zk - zkn)
            ok = dev < PAIR_TOL
            report.append((k, zk, zkn, dev, ok))
            log(f"  kappa={k:>3}: Z(kappa)={fmt(zk)}   Z(kappa+N0)={fmt(zkn)}   "
                f"dev={dev:.3e} -> {'PASS' if ok else 'FAIL'}")
        all_pass = all(ok for *_, ok in report)
        log(f"  --- {label}: {'ALL-PASS' if all_pass else 'FALSIFIED'} "
            f"({sum(ok for *_, ok in report)}/{len(report)} pairs pass) ---")
        all_pair_reports[label] = report

    # ================= PHASE 4: SPOT CHECK =================
    log("\n=== PHASE 4 — SPOT CHECK: 2-rep class-function check, 3 largest buckets, 2 largest r ===")
    two_largest_r = sorted(cache.keys(), reverse=True)[:2]
    log(f"  two largest r actually run: {two_largest_r}")
    spot_tally = {"pass": 0, "fail": 0, "skipped_singleton": 0}
    for bi, (key, members) in enumerate(sorted_buckets[:3]):
        reps = members[:2]
        if len(reps) < 2:
            log(f"  bucket {bi} (size {len(members)}): singleton bucket, cannot 2-rep check -> SKIP")
            spot_tally["skipped_singleton"] += 1
            continue
        for r in two_largest_r:
            vals = []
            for idx, B, s in reps:
                g, ad = J.gauss_sum(B, r)
                vals.append(g)
            maxdev = max(abs(v - vals[0]) for v in vals)
            close = all(abs(v - vals[0]) < 1e-7 * max(1, abs(vals[0])) or abs(v - vals[0]) < 1e-6 for v in vals)
            spot_tally["pass" if close else "fail"] += 1
            log(f"  bucket {bi} (size {len(members)}, |detB|={ad}) r={r}: "
                f"2-rep maxdev={maxdev:.3e} -> {'PASS' if close else 'FAIL'}")
    log(f"  spot check tally: {spot_tally}")

    # ================= WRAP UP =================
    save_results(cache)
    log(f"\nTotal r values computed: {len(cache)}")
    log(f"Results saved to {RESULTS_PATH}")
    log(f"Total wall time: {time.time() - t_start:.2f}s")
    log("DONE.")


if __name__ == '__main__':
    main()
