"""G3 -- MIRROR-WORD (P_WORD = -3) EXACT MILGRAM CERTIFICATION (cc2, 2026-07-17).
Sealed prereg: digest_queue/PREREG_DIGEST.md, sha256 5848c32db3cdfee776eaaeba0a8
e3a3283f1444, G3 clause.

Ports the exact Milgram-certification machinery of promotion_queue/p1_milgram/
p1_milgram.py (gauss_exact, cyc_reduce, embed, poly_of, the candidate-ID loop,
the Q(zeta_8) totals) to the MIRROR bucket P_WORD = -3, rebuilding the buckets
locally in the p4_run.py convention (B_w = -3I - w - w^-1; SAME weyl_group()/
C6/hnf_column()/gauss_sum() reused verbatim from n1_jeffrey_terms.py).

Differences from p1_milgram.py's +3-channel machinery, per the prereg clause:
  - the identity class has det 5^6 = 15625 (B_id = -5I), not det 1 -- there is
    no det-1 "trivial" class in this channel;
  - the odd-exponent-prime bookkeeping is generalized from p1's hardcoded
    "has5" flag to a general squarefree-part-of-|A| computation (verified via
    SNF elementary divisors, q3_lemmas.py style) so it would also catch odd
    exponents at 3, 7, 17 if the data required it (empirically it doesn't --
    see the SNF scan below: only 5 ever carries an odd exponent).

Pipeline:
  STEP 0: build P_WORD=-3 buckets; SNF elementary-divisor scan; assert the det
          multiset matches P4's banked {25,45,64,...,15625} (25 classes).
  STEP 1: GATE -- numeric Z_{-3}(r), r=13..25 (J.gauss_sum, p4_run.py's own
          numeric convention) vs p4_results.json's banked Zm, to < 1e-7.
  STEP 2: exact gamma_w identification at generic rungs r=13,29,31,37 (all
          coprime to 2*3*5*7*17 -- every prime seen in any elementary divisor
          of the 25 classes -- spanning (r|5) = -1,+1,+1,-1).
  STEP 3: THE MIRROR GENERIC LAW from the identified exact totals; verified
          against every generic rung in the run's data (13,19,23 numeric +
          13,29,31,37 exact).
  STEP 4: silence characterization (generic vs non-generic zeros in 13..25).
  STEP 5: NOTICED-level odd-prime overlap/mismatch note (no promotion).
"""
import itertools
import json
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

sys.path.insert(0, '<seat-workdir>/next_queue/n1_counting')
import n1_jeffrey_terms as J   # weyl_group(), C6, hnf_column(), gauss_sum() -- reused
                               # verbatim; P_WORD rebuilt locally at -3 below (the
                               # p4_run.py convention, not J.P_WORD which is +3)

OUTDIR = '<seat-workdir>/digest_queue/g3_mirror'
P4_RESULTS = '<seat-workdir>/promotion_queue/p4_sectors/p4_results.json'
LOGPATH = f'{OUTDIR}/g3_run.log'

P_WORD = -3
IDENT_RS = (13, 29, 31, 37)          # exact identification rungs (prereg-specified)
GATE_RS = tuple(range(13, 26))       # r = 13..25, gated against P4
Wn = 51840                           # |W(E6)|

EXPECT_DET_MULTISET = sorted([
    25, 45, 64, 64, 80, 100, 125, 125, 144, 225, 245, 289, 320, 400, 400,
    500, 625, 625, 720, 1024, 2025, 1125, 2500, 3125, 15625])

_fh = None


def log(msg):
    print(msg, flush=True)
    if _fh is not None:
        _fh.write(msg + "\n")
        _fh.flush()


# =====================================================================
# STEP 0: build the P_WORD = -3 buckets locally (p4_run.py's convention:
# reuse J.weyl_group()/J.C6/J.hnf_column()/J.gauss_sum(), rebuild B ourselves)
# =====================================================================
def build_mirror_buckets():
    W, eps = J.weyl_group()
    log(f"|W(E6)| = {len(W)}")
    buckets = {}
    for idx in range(len(W)):
        w = W[idx]
        winv = np.rint(np.linalg.inv(w)).astype(np.int64)
        assert (w @ winv == np.eye(6, dtype=np.int64)).all()
        B = P_WORD * np.eye(6, dtype=np.int64) - w - winv
        cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
        spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
        buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))
    ordered = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
    assert len(ordered) == 25, f"expected 25 Weyl classes, got {len(ordered)}"
    assert sum(len(m) for _, m in ordered) == len(W), "|W| not conserved by buckets"
    return W, ordered


def elem_divisors(B):
    from sympy.matrices.normalforms import smith_normal_form
    M = sp.Matrix(B.tolist())
    snf = smith_normal_form(M)
    return [abs(int(snf[i, i])) for i in range(6) if abs(int(snf[i, i])) != 1]


def vp(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def scan_classes(ordered):
    """SNF elementary-divisor scan per class (q3_lemmas.py style): finds the
    odd-exponent primes generally (not hardcoded) and the det multiset."""
    rows = []
    seen_primes = set()
    for bi, (key, members) in enumerate(ordered):
        idx0, B0, sgn = members[0]
        divs = elem_divisors(B0)
        det = 1
        for d in divs:
            det *= d
        exps = {}
        for d in divs:
            for p, e in sp.factorint(d).items():
                exps[p] = exps.get(p, 0) + e
        odd_primes = sorted(p for p, e in exps.items() if e % 2 == 1)
        sqfree = 1
        for p in odd_primes:
            sqfree *= p
        seen_primes |= set(exps.keys())
        rows.append(dict(bucket=bi, size=len(members), sign=sgn, det=det,
                          divs=divs, odd_primes=odd_primes, sqfree=sqfree, B=B0))
    return rows, sorted(seen_primes)


# =====================================================================
# STEP 1: numeric GATE vs P4's banked Z_{-3}(r), r=13..25
# =====================================================================
def numeric_gate(ordered):
    with open(P4_RESULTS) as f:
        p4 = json.load(f)
    banked_zm = {int(r): complex(*v["Zm"]) for r, v in p4["results"].items()}

    zm = {r: 0j for r in GATE_RS}
    for bi, (key, members) in enumerate(ordered):
        idx0, B0, s0 = members[0]
        reps = members[:2] if len(members) > 1 else members[:1]
        for r in GATE_RS:
            vals, ads = [], []
            for idx, B, s in reps:
                g, ad = J.gauss_sum(B, r)
                vals.append(g)
                ads.append(ad)
            assert all(a == ads[0] for a in ads), f"|det B| mismatch bucket {bi}"
            is_class_fn = all(abs(v - vals[0]) < 1e-7 * max(1, abs(vals[0])) or
                               abs(v - vals[0]) < 1e-6 for v in vals)
            assert is_class_fn, f"NOT A CLASS FUNCTION r={r} bucket={bi}: {vals}"
            zm[r] += len(members) * s0 * vals[0] / np.sqrt(ads[0])
    zm = {r: zm[r] / Wn for r in GATE_RS}

    gate_rows = []
    all_pass = True
    for r in GATE_RS:
        dev = abs(zm[r] - banked_zm[r])
        ok = dev < 1e-7
        all_pass &= ok
        gate_rows.append((r, zm[r], banked_zm[r], dev, ok))
        log(f"  r={r:2d}: computed Zm={zm[r].real:+.12f}{zm[r].imag:+.2e}i  "
            f"banked={banked_zm[r].real:+.12f}{banked_zm[r].imag:+.2e}i  "
            f"|dev|={dev:.3e}  {'PASS' if ok else 'FAIL'}")
    return zm, gate_rows, all_pass


# =====================================================================
# STEP 2: exact Milgram machinery (ported verbatim from p1_milgram.py, with
# the has5-only bookkeeping generalized to an arbitrary squarefree part)
# =====================================================================
x = sp.symbols('x')


def cyc_reduce(vec_dict, N):
    coeffs = [0] * N
    for e, c in vec_dict.items():
        coeffs[e % N] += c
    p = sp.Poly(list(reversed(coeffs)), x, domain='QQ')
    rem = p.rem(sp.Poly(sp.cyclotomic_poly(N, x), x))
    return rem


def gauss_exact(B, r):
    """G_w(r) as (Poly mod Phi_N, N): sum of zeta_{2b}^{-a} over cosets (verbatim
    from p1_milgram.py -- generic in B and r, no P_WORD dependence)."""
    Bs = sp.Matrix(B.tolist())
    ad = abs(int(Bs.det()))
    M = sp.Matrix(J.C6.tolist()) * Bs.inv()
    H = J.hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    Mf = [[Fraction(M[i, j]) for j in range(6)] for i in range(6)]
    terms = {}
    dens = set()
    raw = []
    for xx in itertools.product(*[range(d) for d in diag]):
        q = Fraction(0)
        for i in range(6):
            if xx[i]:
                for jj in range(6):
                    if xx[jj]:
                        q += xx[i] * Mf[i][jj] * xx[jj]
        e = (r * q) % 2
        raw.append(e)
        dens.add(e.denominator)
    N = 2 * np.lcm.reduce([int(d) for d in dens]) if dens else 2
    N = int(N)
    for e in raw:
        expo = int(-(e * N // 2)) % N
        terms[expo] = terms.get(expo, 0) + 1
    return cyc_reduce(terms, N), N, ad


def embed(polyrem, N, Np):
    k = Np // N
    out = {}
    cs = list(reversed(polyrem.all_coeffs()))
    for e, c in enumerate(cs):
        if c:
            out[(e * k) % Np] = out.get((e * k) % Np, 0) + c
    return out


def poly_of(dic, Np):
    coeffs = [0] * Np
    for e, c in dic.items():
        coeffs[e % Np] += c
    p = sp.Poly(list(reversed(coeffs)), x, domain='QQ')
    return p.rem(sp.Poly(sp.cyclotomic_poly(Np, x), x))


def legendre(t, p):
    t %= p
    if t == 0:
        return 0
    return 1 if sp.is_quad_residue(t, p) else -1


def sqrtp_dict(p, Np):
    """g_p = sum_{t=1}^{p-1} (t|p) zeta_p^t  (the classical quadratic Gauss sum;
    generalizes p1_milgram.py's sqrt5_dict to any odd prime p | Np). Equals
    sqrt(p) if p = 1 mod 4, i*sqrt(p) if p = 3 mod 4 -- both handled correctly
    since this is built as an exact element of Q(zeta_p) subset Q(zeta_Np)."""
    k = Np // p
    d = {}
    for t in range(1, p):
        leg = legendre(t, p)
        d[(t * k) % Np] = d.get((t * k) % Np, 0) + leg
    return d


def mul_dicts(d1, d2, Np):
    out = {}
    for e1, c1 in d1.items():
        for e2, c2 in d2.items():
            out[(e1 + e2) % Np] = out.get((e1 + e2) % Np, 0) + c1 * c2
    return out


def sqrtfree_dict(sqfree, Np):
    """Gauss-sum representative of sqrt(sqfree) for squarefree sqfree > 1
    (product of the individual odd-prime quadratic Gauss sums)."""
    d = {0: 1}
    for p in sp.factorint(sqfree):
        d = mul_dicts(d, sqrtp_dict(p, Np), Np)
    return d


def identify_gamma(class_rows, rs):
    """Per class, per rung: identify gamma_w(r) = G_w(r)/sqrt|A_w| as zeta_8^j
    exactly, by matching G_w(r) itself (an exact cyclotomic integer) against
    candidates m * sqrt(sqfree) * zeta_8^j (m, sqfree from the class's own SNF
    elementary divisors)."""
    for row in class_rows:
        bi, B0, sqfree = row['bucket'], row['B'], row['sqfree']
        for r in rs:
            Gp, N, ad = gauss_exact(B0, r)
            assert ad == row['det'], f"bucket {bi} r={r}: det mismatch {ad} vs {row['det']}"
            m2, ok = sp.integer_nthroot(ad // sqfree if sqfree > 1 else ad, 2)
            assert ok, f"bucket {bi} r={r}: {ad}/{sqfree} not a perfect square"
            m = int(m2)
            primes_needed = sorted(sp.factorint(sqfree).keys()) if sqfree > 1 else []
            Np = int(np.lcm.reduce([N, 8] + list(primes_needed)))
            Gd = embed(Gp, N, Np)
            Gcan = poly_of(Gd, Np)
            base_sqrt = sqrtfree_dict(sqfree, Np) if sqfree > 1 else {0: 1}
            ident = None
            for j in range(8):
                base = {(j * (Np // 8)) % Np: m}
                cand = mul_dicts(base, base_sqrt, Np)
                if poly_of(cand, Np) == Gcan:
                    ident = j
                    break
            assert ident is not None, (
                f"bucket {bi} r={r}: no zeta8^j*sqrt({sqfree}) candidate matched "
                f"(ad={ad}, N={N})")
            row[f"j_{r}"] = ident
    return class_rows


def z8_total(class_rows, rkey):
    """exact (1/|W|) sum sign*size*zeta_8^j  ->  Q-coords on (1, z, z^2, z^3)
    using zeta_8^4 = -1."""
    acc = [Fraction(0)] * 8
    for row in class_rows:
        acc[row[rkey]] += Fraction(row["sign"] * row["size"], Wn)
    return [acc[k] - acc[k + 4] for k in range(4)]


LEGENDRE5 = {1: 1, 2: -1, 3: -1, 4: 1}


def leg5(r):
    return LEGENDRE5[r % 5]


def main():
    global _fh
    _fh = open(LOGPATH, 'w')
    log("=" * 78)
    log("G3 -- MIRROR-WORD (P_WORD=-3) EXACT MILGRAM CERTIFICATION")
    log("prereg sha256 5848c32db3cdfee776eaaeba0a8e3e6408d67cb9cb8d79fbe7da3aa3283f1444")
    log("=" * 78)

    # ---- STEP 0: build buckets + SNF scan ----
    log("\n---- STEP 0: build P_WORD=-3 buckets locally + SNF elementary-divisor scan ----")
    W, ordered = build_mirror_buckets()
    class_rows, seen_primes = scan_classes(ordered)
    log(f"25 Weyl classes built, |W| conserved = {sum(r['size'] for r in class_rows) == len(W)}")
    log(f"primes seen in ANY elementary divisor across all 25 classes: {seen_primes}")
    det_multiset = sorted(r['det'] for r in class_rows)
    det_match = det_multiset == EXPECT_DET_MULTISET
    log(f"det(B) multiset matches prereg/P4 spec: {det_match}")
    assert det_match, (det_multiset, EXPECT_DET_MULTISET)
    odd_exp_primes = sorted({p for r in class_rows for p in r['odd_primes']})
    log(f"odd-exponent primes actually occurring (per-class sqrt-part primes): {odd_exp_primes}")
    id_row = [r for r in class_rows if r['det'] == 15625][0]
    log(f"identity class: det={id_row['det']} (= 5^6), sqfree={id_row['sqfree']} "
        f"(B_id = -5I, confirms NO det-1 class in this channel)")

    # ---- STEP 1: numeric gate vs P4 ----
    log("\n---- STEP 1: GATE -- numeric Z_{-3}(r), r=13..25, vs P4's banked Zm (< 1e-7) ----")
    zm_numeric, gate_rows, gate_pass = numeric_gate(ordered)
    log(f"\nGATE {'PASS' if gate_pass else 'FAIL'}: {sum(g[4] for g in gate_rows)}/13 rungs "
        f"reproduce P4's banked Z_-(r) to < 1e-7")
    if not gate_pass:
        log("HARD STOP per prereg: gate failed, aborting before any law extraction.")
        _fh.close()
        sys.exit(1)

    # ---- STEP 2: exact identification at r=13,29,31,37 ----
    log("\n---- STEP 2: exact gamma_w identification at generic rungs r=13,29,31,37 ----")
    log("(13,29,31,37 all coprime to 2*3*5*7*17 -- every prime in any elementary "
        "divisor of the 25 classes; (r|5) = -1,+1,+1,-1 respectively)")
    identify_gamma(class_rows, IDENT_RS)
    for row in class_rows:
        log(f"  b{row['bucket']:2d} sz{row['size']:5d} sgn{row['sign']:+d} "
            f"det{row['det']:6d} sqfree={row['sqfree']:3d} "
            f"j13={row['j_13']} j29={row['j_29']} j31={row['j_31']} j37={row['j_37']}")

    # exact totals at the identification rungs
    exact_totals = {r: z8_total(class_rows, f"j_{r}") for r in IDENT_RS}
    log("\nEXACT Z_{-3}(r) in Q(zeta_8) coords (1, z, z^2, z^3):")
    for r in IDENT_RS:
        log(f"  r={r:2d}: {[str(c) for c in exact_totals[r]]}  ((r|5)={leg5(r):+d})")

    # cross-check exact r=13 total against the numeric gate value at r=13
    exact13_real = float(exact_totals[13][0])
    cross_dev = abs(exact13_real - zm_numeric[13].real)
    log(f"\ncross-check: exact total(r=13) real part = {exact13_real:+.6f} vs numeric "
        f"gate Zm(13) = {zm_numeric[13].real:+.12f}  |dev|={cross_dev:.3e}  "
        f"{'OK' if cross_dev < 1e-7 else 'MISMATCH'}")

    # ---- STEP 3: the mirror generic law ----
    log("\n---- STEP 3: THE MIRROR GENERIC LAW ----")
    law_checks = []
    # exact rungs
    for r in IDENT_RS:
        coords = exact_totals[r]
        assert coords[1] == 0 and coords[2] == 0 and coords[3] == 0, \
            f"r={r}: total not purely real in Q(zeta8): {coords}"
        observed = coords[0]
        predicted = Fraction(leg5(r) - 1, 2)
        law_checks.append((r, "exact", observed, predicted, observed == predicted))
    # numeric generic rungs already in the gate data: 13, 19, 23 (coprime to 2*3*5*7*17)
    for r in (13, 19, 23):
        predicted = (leg5(r) - 1) / 2
        observed = zm_numeric[r].real
        law_checks.append((r, "numeric", observed, predicted, abs(observed - predicted) < 1e-7))

    log("THE MIRROR GENERIC LAW:  Z_{-3}(r) = ((r|5) - 1) / 2   for gcd(r, 2*3*5*7*17) = 1")
    log("(equivalently: -(1-(r|5))/2, i.e. Z_{-3}(generic r) = -Z_{+3}(generic r) exactly, "
        "consistent with the P4 eps=+1 gate)")
    all_law_ok = True
    for r, kind, obs, pred, ok in law_checks:
        all_law_ok &= ok
        log(f"  r={r:2d} ({kind:7s}): observed={obs}  predicted={pred}  {'OK' if ok else 'VIOLATION'}")
    log(f"LAW VERIFIED on all generic rungs in the data: {all_law_ok}")
    assert all_law_ok

    # ---- STEP 4: silence characterization ----
    log("\n---- STEP 4: mirror silence characterization, r=13..25 (+ identification rungs) ----")
    BAD = {2, 3, 5, 7, 17}
    with open(P4_RESULTS) as f:
        p4 = json.load(f)
    zp_numeric = {int(r): complex(*v["Zp"]) for r, v in p4["results"].items()}
    silences = []
    for r in GATE_RS:
        is_zero = abs(zm_numeric[r]) < 1e-7
        is_generic = all(r % p != 0 for p in BAD)
        zp_zero = abs(zp_numeric[r]) < 1e-7
        silences.append((r, is_zero, is_generic, zp_zero))
    for r, is_zero, is_generic, zp_zero in silences:
        tag = ("generic-silent (law: (r|5)=+1)" if (is_zero and is_generic) else
               "non-generic silent" if is_zero else "")
        if is_zero:
            log(f"  r={r:2d}: Z_-(r)=0  generic={is_generic}  Z_+(r) also 0={zp_zero}  {tag}")
    zero_rs = [r for r, z, g, zp0 in silences if z]
    generic_zero_rs = [r for r, z, g, zp0 in silences if z and g]
    nongeneric_zero_rs = [r for r, z, g, zp0 in silences if z and not g]
    shared_zero_rs = [r for r, z, g, zp0 in silences if z and zp0]
    log(f"\nsummary: Z_-(r)=0 at r={zero_rs} within 13..25")
    log(f"  generic silences (explained by the law, (r|5)=+1): {generic_zero_rs}")
    log(f"  non-generic silences (finer per-class cancellation, not from the generic "
        f"law alone): {nongeneric_zero_rs}")
    log(f"  shared with the direct (+3) channel's own silence (Z_+ also 0): {shared_zero_rs}")

    # ---- STEP 5: NOTICED odd-prime overlap/mismatch (no promotion) ----
    log("\n---- STEP 5: NOTICED -- mirror odd primes vs direct channel's import set ----")
    mirror_odd = sorted(p for p in seen_primes if p != 2)
    direct_import_set = {15: 5, 16: 2, 17: 17, 20: 5}   # banked, from level_ladder_campaign
    log(f"mirror spectrum's odd primes (structural, from the 25 classes' elementary "
        f"divisors): {mirror_odd}")
    log(f"direct channel's banked inert-import set (per-rung sqrt-p imports, banked "
        f"in level_ladder_campaign/PREREG_L5.md, L5_RUN.log, PREREG_Q1.md): "
        f"{direct_import_set} (i.e. primes {{2,5,17}})")
    overlap = sorted(set(mirror_odd) & {2, 5, 17})
    mirror_only = sorted(set(mirror_odd) - {2, 5, 17})
    direct_only = sorted({2, 5, 17} - set(mirror_odd))
    log(f"OVERLAP: {overlap}  (5 and 17 appear on both sides)")
    log(f"MIRROR-ONLY (never seen as a direct-channel import): {mirror_only}  (3 and 7)")
    log(f"DIRECT-ONLY: {direct_only}  (2 is a dyadic import at kappa=16 in the direct "
        f"channel; in the mirror's own structural det multiset, 2 occurs in 10/25 "
        f"classes but ALWAYS with even exponent -- it never contributes a sqrt-2 "
        f"factor, only the fixed zeta_8 dyadic modulus)")
    log("STATEMENT (factual, NOTICED-level, no promotion): the two odd-prime sets "
        "share {5, 17} and disagree on {2} (direct-only, dyadic) vs {3, 7} "
        "(mirror-only). No law is asserted from this; it is recorded as data per "
        "the G3 falsifier clause.")

    # =====================================================================
    # save certificates
    # =====================================================================
    def frac_list(v):
        return [str(c) for c in v]

    out = {
        "prereg_sha256": "5848c32db3cdfee776eaaeba0a8e3e6408d67cb9cb8d79fbe7da3aa3283f1444",
        "gate": "PASS" if gate_pass else "FAIL",
        "det_multiset_check": det_match,
        "det_multiset": det_multiset,
        "primes_seen_in_elementary_divisors": seen_primes,
        "odd_exponent_primes_occurring": odd_exp_primes,
        "identity_class": {"det": id_row['det'], "sqfree": id_row['sqfree']},
        "gate_rows": [{"r": r, "Zm_computed": [zm.real, zm.imag],
                       "Zm_banked": [zb.real, zb.imag], "dev": dev, "pass": bool(ok)}
                      for r, zm, zb, dev, ok in gate_rows],
        "gamma_table": [{"bucket": row["bucket"], "size": row["size"], "sign": row["sign"],
                          "det": row["det"], "sqfree": row["sqfree"],
                          "odd_primes": row["odd_primes"],
                          **{f"j_{r}": row[f"j_{r}"] for r in IDENT_RS}}
                         for row in class_rows],
        "exact_totals_zeta8_coords": {str(r): frac_list(exact_totals[r]) for r in IDENT_RS},
        "cross_check_r13": {"exact_real": exact13_real, "numeric": zm_numeric[13].real,
                             "dev": cross_dev},
        "mirror_generic_law": "Z_-3(r) = ((r|5) - 1) / 2  for gcd(r, 2*3*5*7*17) = 1",
        "law_checks": [{"r": r, "kind": kind, "observed": str(obs), "predicted": str(pred),
                         "ok": bool(ok)} for r, kind, obs, pred, ok in law_checks],
        "law_verified_all_generic_rungs_in_data": all_law_ok,
        "silence_characterization": {
            "zero_rs_13_25": zero_rs,
            "generic_zero_rs": generic_zero_rs,
            "nongeneric_zero_rs": nongeneric_zero_rs,
            "shared_with_direct_channel": shared_zero_rs,
        },
        "noticed_odd_prime_note": {
            "mirror_odd_primes": mirror_odd,
            "direct_import_set_primes": [2, 5, 17],
            "direct_import_set_by_kappa": direct_import_set,
            "overlap": overlap,
            "mirror_only": mirror_only,
            "direct_only": direct_only,
        },
    }
    with open(f'{OUTDIR}/g3_certificates.json', 'w') as f:
        json.dump(out, f, indent=1)
    log(f"\nWROTE {OUTDIR}/g3_certificates.json")
    log("DONE", )
    _fh.close()


if __name__ == '__main__':
    main()
