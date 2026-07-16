"""P4 -- THE SECTOR-SPLIT EXTENSION + THE CORRELATE STRESS TEST (cc2, 2026-07-16).
Sealed prereg: promotion_queue/p4_sectors/PREREG_P4.md, sha256 baed2eed...b130984.

Mechanism (verbatim from the prereg): at E6, Theta = charge conjugation = the image
of S^2, so Tr(Theta rho(A1)) is the -A1-bundle invariant = the Jeffrey pipeline at
P_WORD = -3 (B_w = -3I - w - w^{-1}), up to a fixed global sign eps in {+1,-1}
(W(E6) has no -1, so a det(w0)-type factor may enter). This script:

  1. Builds the SAME bucketed Jeffrey pipeline as n1_jeffrey_terms.py (import reuse,
     the n1_jeffrey_extend.py pattern) at P_WORD = -3, r = 13..25. Asserts 25 Weyl
     classes, |W| conservation, and the det(B) multiset (each gauss_sum() call
     already asserts HNF-diag-product == |det B| internally).
  2. Gates our OWN re-implementation of the P_WORD=+3 code path at r=13,19 against
     the banked totals (1.0, 2.0) -- everything else at P=+3 is taken verbatim from
     jeffrey_terms.json / jeffrey_extension.json (no recompute).
  3. Fixes the single global eps in {+1,-1} against the banked sector ladder,
     r=13..20 (k=1..8). Hard stop (CONVENTION-FAILURE) if no single eps reproduces
     all 8 rungs.
  4. Banks the fresh rungs r=21..25, evaluates the five sealed predictions, and
     renders the CORRELATE verdict.
"""
import json
import sys
import time

import numpy as np

sys.path.insert(0, '<seat-workdir>/seat-work/next_queue/n1_counting')
import n1_jeffrey_terms as J   # weyl_group(), gauss_sum(), hnf_column() -- reuse pattern
                                # (identical to n1_jeffrey_extend.py's own import of this module)

OUTDIR = '<seat-workdir>/seat-work/promotion_queue/p4_sectors'
BANKDIR = '<seat-workdir>/seat-work/next_queue/n1_counting'
LOGPATH = f'{OUTDIR}/p4_run.log'

RS_ALL = tuple(range(13, 26))          # 13..25  (E6 k = 1..13)
RS_GATE = (13, 19)                     # P=+3 code-path recompute gate / P=-3 spot-check r's
RS_LADDER = tuple(range(13, 21))       # 13..20  (k=1..8): the eps-fixing gate
RS_FRESH = tuple(range(21, 26))        # 21..25  (k=9..13): sealed predictions

# banked (tr_odd, tr_even) ladder k=1..8, r=13..20 -- verbatim from PREREG_P4.md GATE line
BANKED_LADDER = {13: (1, 0), 14: (1, 0), 15: (0, 1), 16: (0, 0),
                  17: (0, 1), 18: (1, 0), 19: (1, 1), 20: (0, 1)}

# the five sealed predictions (kappa = r), verbatim from PREREG_P4.md
SEALED = {
    21: dict(desc="3 ramified, 7 split; NO inert odd prime", even_nonzero=False, split=(1, 0)),
    22: dict(desc="11 === 2 mod 3 INERT", even_nonzero=True, split=None),
    23: dict(desc="23 === 2 mod 3 INERT, prime", even_nonzero=True, split=(0, 1)),
    24: dict(desc="2^3*3; NO inert odd prime", even_nonzero=False, split=(2, 0)),
    25: dict(desc="5 INERT but Z = 0 (silent/vacuous)", even_nonzero=None, split=None),
}

_fh = None


def log(msg):
    print(msg, flush=True)
    if _fh is not None:
        _fh.write(msg + "\n")
        _fh.flush()


def build_and_sum(p_word, rs, tag, spot_check_rs=()):
    """The SAME bucketed pipeline as n1_jeffrey_terms.main(): bucket W(E6) by
    (charpoly(w), spectrum(B)), verify each bucket is a class function (2-rep
    check when available), sum contributions len*sign*gauss_sum/sqrt(|det B|).
    Generalizes n1_jeffrey_terms.py's P_WORD=3-only, RS=(13..19)-only main() to
    arbitrary p_word / r-set so it can be reused verbatim for P_WORD=-3, r=13..25."""
    t0 = time.time()
    W, eps = J.weyl_group()
    log(f"[{tag}] |W| = {len(W)}")
    buckets = {}
    for idx in range(len(W)):
        w = W[idx]
        winv = np.rint(np.linalg.inv(w)).astype(np.int64)
        assert (w @ winv == np.eye(6, dtype=np.int64)).all()
        B = p_word * np.eye(6, dtype=np.int64) - w - winv
        cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
        spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
        key = (cp, spec)
        buckets.setdefault(key, []).append((idx, B, int(eps[idx])))
    log(f"[{tag}] buckets: {len(buckets)}")
    assert len(buckets) == 25, f"[{tag}] expected 25 Weyl conjugacy classes, got {len(buckets)}"

    results = {r: 0j for r in rs}
    rows = []
    det_multiset = []
    sorted_buckets = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
    assert sum(len(m) for _, m in sorted_buckets) == len(W), f"[{tag}] |W| not conserved by buckets"

    for bi, (key, members) in enumerate(sorted_buckets):
        idx0, B0, s0 = members[0]
        assert all(s == s0 for _, _, s in members), f"[{tag}] non-class-fn SIGN in bucket {bi}"
        reps = members[:2] if len(members) > 1 else members[:1]
        row = {"bucket": bi, "charpoly": [int(c) for c in key[0]],
               "size": len(members), "sign": s0, "absdetB": None, "contrib": {}}
        bucket_ad = None
        for r in rs:
            vals, ads = [], []
            for idx, B, s in reps:
                g, ad = J.gauss_sum(B, r)   # gauss_sum() itself asserts HNF-diag-prod == |det B|
                vals.append(g)
                ads.append(ad)
            assert all(a == ads[0] for a in ads), f"[{tag}] |det B| mismatch within bucket {bi}"
            is_class_fn = all(abs(v - vals[0]) < 1e-7 * max(1, abs(vals[0])) or
                               abs(v - vals[0]) < 1e-6 for v in vals)
            assert is_class_fn, f"[{tag}] NOT A CLASS FUNCTION at r={r} bucket={bi}: {vals}"
            if bi < 3 and r in spot_check_rs:
                tagvals = ", ".join(f"{v.real:+.10f}{v.imag:+.10f}i" for v in vals)
                log(f"    [spot-check] bucket {bi} (size {row['size']}, |detB|={ads[0]}) "
                    f"r={r}: {len(reps)} rep(s) -> [{tagvals}]  "
                    f"max|diff|={max(abs(v - vals[0]) for v in vals):.3e}  CLASS-FN OK")
            row["absdetB"] = ads[0]
            bucket_ad = ads[0]
            c = len(members) * s0 * vals[0] / np.sqrt(ads[0])
            results[r] += c
            row["contrib"][str(r)] = [c.real, c.imag]
        rows.append(row)
        det_multiset.append(bucket_ad)

    zs = {r: results[r] / len(W) for r in rs}
    log(f"[{tag}] done in {time.time() - t0:.1f}s")
    return zs, rows, sorted(det_multiset), sorted_buckets


def load_banked_zp():
    """Zp(r) = Z_{+3}(r), r=13..25, taken verbatim from the banked jsons (no recompute
    except the r=13,19 code-path gate done separately in main())."""
    with open(f'{BANKDIR}/jeffrey_terms.json') as f:
        t1 = json.load(f)['totals']
    with open(f'{BANKDIR}/jeffrey_extension.json') as f:
        t2 = json.load(f)['totals']
    zp = {}
    for r in RS_ALL:
        src = t1 if str(r) in t1 else t2
        re_, im_ = src[str(r)]
        zp[r] = complex(re_, im_)
    return zp


def main():
    global _fh
    _fh = open(LOGPATH, 'w')
    log("=" * 78)
    log("P4 -- SECTOR-SPLIT EXTENSION + CORRELATE STRESS TEST")
    log("prereg sha256 baed2eedc20d5c4565263dc7ae2b8d4988b23bcc1a911b9bdee51ff47b130984")
    log("=" * 78)

    # ---------- STEP 1: P=+3 code-path gate (r=13, 19 only; rest taken from bank) ----------
    log("\n---- STEP 1: P_WORD=+3 code-path gate at r=13,19 (own re-implementation) ----")
    zp_gate, _, _, _ = build_and_sum(+3, RS_GATE, tag="P+3 gate")
    gate_targets = {13: 1.0, 19: 2.0}
    gate_ok = True
    for r, target in gate_targets.items():
        dev = abs(zp_gate[r] - target)
        ok = dev < 1e-7
        gate_ok &= ok
        log(f"  r={r}: computed {zp_gate[r].real:+.12f}{zp_gate[r].imag:+.2e}i  "
            f"vs banked {target:.1f}  |dev|={dev:.3e}  {'PASS' if ok else 'FAIL'}")
    if not gate_ok:
        log("\nHARD STOP: P=+3 code-path gate FAILED -- our pipeline reimplementation does "
            "not reproduce the banked ladder. Aborting before trusting P=-3 output.")
        _fh.close()
        sys.exit(1)
    log("GATE PASS: own P_WORD=+3 code path reproduces banked r=13 (1.0) and r=19 (2.0) "
        "to < 1e-7.")

    zp = load_banked_zp()
    log("\nZ_{+3}(r), r=13..25 (banked, jeffrey_terms.json + jeffrey_extension.json):")
    for r in RS_ALL:
        log(f"  r={r:2d}: {zp[r].real:+.10f}{zp[r].imag:+.2e}i")

    # ---------- STEP 2: P=-3 full pipeline, r=13..25 ----------
    log("\n---- STEP 2: P_WORD=-3 full bucketed pipeline, r=13..25 ----")
    log("(class-function 2-rep spot check logged inline for the 3 largest buckets "
        f"at r in {RS_GATE})")
    zm, rows_m, det_multiset_m, buckets_m = build_and_sum(
        -3, RS_ALL, tag="P-3 full", spot_check_rs=RS_GATE)

    log(f"\ndet(B) multiset for P_WORD=-3 (25 Weyl classes, sorted |det B|):")
    log(f"  {det_multiset_m}")
    log(f"  distinct values: {sorted(set(det_multiset_m))}")
    assert all(isinstance(d, (int, np.integer)) and d > 0 for d in det_multiset_m), \
        "det multiset must be positive integers"

    log("\nZ_{-3}(r), r=13..25 (freshly computed):")
    for r in RS_ALL:
        log(f"  r={r:2d}: {zm[r].real:+.10f}{zm[r].imag:+.2e}i")

    # ---------- STEP 3: fix eps against the banked ladder r=13..20 ----------
    log("\n---- STEP 3: fixing the single global eps against banked ladder r=13..20 ----")
    candidate_results = {}
    for eps_try in (+1, -1):
        rows_report = []
        n_match = 0
        for r in RS_LADDER:
            tr_odd = (zp[r].real - eps_try * zm[r].real) / 2
            tr_even = (zp[r].real + eps_try * zm[r].real) / 2
            to_r, te_r = round(tr_odd), round(tr_even)
            banked = BANKED_LADDER[r]
            match = (abs(tr_odd - to_r) < 1e-6 and abs(tr_even - te_r) < 1e-6 and
                      (to_r, te_r) == banked)
            n_match += match
            rows_report.append((r, tr_odd, tr_even, (to_r, te_r), banked, match))
        candidate_results[eps_try] = (n_match, rows_report)
        log(f"  eps={eps_try:+d}: {n_match}/8 rungs match the banked ladder")
        for r, to, te, rounded, banked, match in rows_report:
            log(f"    r={r:2d} (k={r-12}): tr_odd={to:+.6f} tr_even={te:+.6f} -> "
                f"{rounded}  banked={banked}  {'OK' if match else 'MISMATCH'}")

    good_eps = [e for e, (n, _) in candidate_results.items() if n == 8]
    if len(good_eps) != 1:
        log(f"\nCONVENTION-FAILURE: {len(good_eps)} of {{+1,-1}} reproduce all 8 banked rungs "
            f"(need exactly 1). eps=+1 matched {candidate_results[1][0]}/8, "
            f"eps=-1 matched {candidate_results[-1][0]}/8. STOPPING per prereg gate.")
        result = {"gate": "CONVENTION-FAILURE",
                  "eps_plus1_matches": candidate_results[1][0],
                  "eps_minus1_matches": candidate_results[-1][0],
                  "ladder_table": {str(r): {"tr_odd": to, "tr_even": te, "rounded": list(rd),
                                              "banked": list(bk), "match": bool(mt)}
                                    for r, to, te, rd, bk, mt in candidate_results[1][1]},
                  "det_multiset_Pminus3": det_multiset_m}
        with open(f'{OUTDIR}/p4_results.json', 'w') as f:
            json.dump(result, f, indent=1)
        _fh.close()
        sys.exit(1)

    eps = good_eps[0]
    log(f"\nGATE PASS: eps = {eps:+d} is the UNIQUE global sign reproducing the entire "
        f"banked sector ladder r=13..20 (8/8).")

    # ---------- STEP 4: full ladder k=1..13 + fresh predictions ----------
    log("\n---- STEP 4: full (tr_odd, tr_even) ladder k=1..13 (r=13..25) ----")
    ladder = {}
    results_json = {}
    for r in RS_ALL:
        tr_odd = (zp[r].real - eps * zm[r].real) / 2
        tr_even = (zp[r].real + eps * zm[r].real) / 2
        assert abs(tr_odd - round(tr_odd)) < 1e-6, f"r={r}: tr_odd not near-integer: {tr_odd}"
        assert abs(tr_even - round(tr_even)) < 1e-6, f"r={r}: tr_even not near-integer: {tr_even}"
        assert abs(zp[r].imag) < 1e-6 and abs(zm[r].imag) < 1e-6, \
            f"r={r}: non-negligible imaginary part in Zp/Zm"
        ladder[r] = (tr_odd, tr_even)
        results_json[str(r)] = {
            "Zp": [zp[r].real, zp[r].imag], "Zm": [zm[r].real, zm[r].imag],
            "tr_odd": tr_odd, "tr_even": tr_even,
            "tr_odd_round": round(tr_odd), "tr_even_round": round(tr_even),
        }
        tag = "[BANKED-LADDER-GATE]" if r in RS_LADDER else "[FRESH/SEALED]"
        log(f"  k={r-12:2d} (r={r:2d}): tr_odd={tr_odd:+.6f} tr_even={tr_even:+.6f}  "
            f"~ ({round(tr_odd)},{round(tr_even)})  {tag}")

    # ---------- STEP 5: evaluate the five sealed predictions ----------
    log("\n---- STEP 5: the five sealed predictions, r=21..25 ----")
    verdicts = {}
    for r in RS_FRESH:
        to, te = ladder[r]
        to_r, te_r = round(to), round(te)
        spec = SEALED[r]
        lines = [f"  r={r} ({spec['desc']}):"]
        ok = True
        if spec['even_nonzero'] is True:
            hit = abs(te) > 1e-6
            ok &= hit
            lines.append(f"    predicted tr_even != 0 -> observed tr_even={te:+.6f} "
                          f"({'HOLDS' if hit else 'VIOLATED'})")
        elif spec['even_nonzero'] is False:
            hit = abs(te) < 1e-6
            ok &= hit
            lines.append(f"    predicted tr_even == 0 -> observed tr_even={te:+.6f} "
                          f"({'HOLDS' if hit else 'VIOLATED'})")
        else:
            lines.append(f"    Z={zp[r].real + 0:+.3f}/{zm[r].real:+.3f}-derived silent rung "
                          f"(vacuous, no falsifier) -> observed split=({to_r},{te_r}) BANKED AS DATA")
        if spec['split'] is not None:
            split_ok = (to_r, te_r) == spec['split']
            ok &= split_ok
            lines.append(f"    predicted split {spec['split']} -> observed ({to_r},{te_r}) "
                          f"({'HOLDS' if split_ok else 'VIOLATED'})")
        verdicts[r] = ok if spec['even_nonzero'] is not None else None
        for ln in lines:
            log(ln)

    falsified = [r for r, v in verdicts.items() if v is False]
    if falsified:
        correlate_verdict = f"CORRELATE-DIES-AT-({min(falsified)})"
    else:
        correlate_verdict = "CORRELATE-EXTENDS"
    log(f"\n==== CORRELATE VERDICT: {correlate_verdict} ====")

    # ---------- save p4_results.json ----------
    out = {
        "prereg_sha256": "baed2eedc20d5c4565263dc7ae2b8d4988b23bcc1a911b9bdee51ff47b130984",
        "gate": "PASS",
        "eps": eps,
        "det_multiset_Pminus3_sorted": det_multiset_m,
        "det_multiset_Pminus3_distinct": sorted(set(det_multiset_m)),
        "ladder_k1_13": {str(r - 12): {"r": r, "tr_odd": ladder[r][0], "tr_even": ladder[r][1],
                                         "rounded": [round(ladder[r][0]), round(ladder[r][1])]}
                          for r in RS_ALL},
        "sealed_predictions": {str(r): (bool(v) if v is not None else "DATA/VACUOUS")
                                for r, v in verdicts.items()},
        "correlate_verdict": correlate_verdict,
        "results": results_json,
    }
    with open(f'{OUTDIR}/p4_results.json', 'w') as f:
        json.dump(out, f, indent=1)
    log(f"\nWROTE {OUTDIR}/p4_results.json")
    _fh.close()


if __name__ == '__main__':
    main()
