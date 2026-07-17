"""CELL G — L100: THE RESONANT-PHASE LAW => the exact minimal period of the melody.

The banked ladder (B646 n1 / B651 d2 pipeline, replicated verbatim below):
    Z(r) = (1/|W|) * sum over the 25 Weyl classes of  size * sign * G_w(r) / sqrt|det B_w|,
    B_w  = 3*I - w - w^{-1},   G_w(r) = sum over the HNF box of exp(-i*pi*((r*q(mu)) mod 2)),
    q(mu) = mu^T (C6 B_w^{-1}) mu   (exact rationals).

METHOD (the certificate structure): each class's Gauss sum is a finite character sum
    G_w(r) = sum over q in Q/2Z of n^w_q * chi_q(r),      chi_q(r) = exp(-i*pi*r*q),
with EXACT rational q and EXACT integer counts n^w_q (the full phase data of every
jumped term at every resonant rung, all unit classes at once).  Aggregating,
    Z(r) = sum_q N_q chi_q(r),   N_q = sum_s A_{q,s} sqrt(s)  (s squarefree, A exact in Q).
Distinct chi_q are distinct homomorphisms Z -> C*, hence linearly independent (Artin).
Therefore d is a period of Z  <=>  chi_q(d) = 1 for every SUPPORTED q (N_q != 0)
<=> d*q in 2Z for every supported q.  The set of periods is ord*Z, so
    MINIMAL PERIOD  =  lcm over supported q = a/b (lowest terms) of ord(q),
    ord(q) = 1 if q = 0;  b if a even;  2b if a odd.
N_q = 0 is decided EXACTLY: sqrt(s) for distinct squarefree s are linearly
independent over Q, so N_q = 0 iff every A_{q,s} = 0 (exact Fraction arithmetic).

GATES (all must pass before the verdict):
  A0  |W| = 51840, 25 buckets, the (size, sign, |detB|) table == the banked
      jeffrey_terms.json table exactly.
  B   2-representative EXACT q-multiset equality per bucket (class-function, exact).
  A1  per-class G at r = 13, 19: verbatim banked gauss_sum (float path) vs the
      multiset evaluation — dev < 1e-9.
  P1  per-class G(13), G(29) == zeta_8^j * sqrt|detB| with j from cc2's banked
      p1_certificates.json (exact-cyclotomic seat), dps 50, quantized at 1e-30.
  F1  the uniform jump law |G(r)|^2 = prod p^(a + min(v_p(r), a)) over the SNF
      elementary divisors, r in {13, 16, 19, 20, 45, 57}, integer-quantized at 1e-30.
  A2  totals Z(13) = 1, Z(16) = 0, Z(19) = 2 at dps 50 (quantized at 1e-30);
      the generic law Z = (1 - (kappa|5))/2 at 17, 23, 29.
  C   P_min | N0 = 2^6*3^3*5^4*7^2*11^2*19^2 (the melody theorem) and 5 | P_min
      (B656/G2: the generic subsequence has minimal period 5).
  D   melody spot pairs: Z(kappa) vs Z(kappa + P_min) on the D2 sealed rung set,
      evaluated per-class (includes any aggregate-cancelled q), dps 30.
  E   minimality witnesses: for every prime p | P_min a rung kappa with
      Z(kappa) != Z(kappa + P_min/p), certified at dps 50 (plus the algebraic
      certificate: a supported q with (P_min/p)*q not in 2Z).

Provenance of replicated code: weyl_group/C6 verbatim from
frontier/B600_level_ladder/packet/scripts/engine.py (banked); bucket construction
and gauss_sum verbatim from frontier/B646_wave2_integration/cc2_packets/
next_queue/next_queue/n1_counting/n1_jeffrey_terms.py (banked pipeline, P_WORD = 3).
House pattern: dps 50, quantize at 1e-30. Exact arithmetic in every decisive step.
"""
import itertools
import json
import math
import time
from collections import Counter
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

CELL = '/Users/dri/origin-axiom/frontier/B662_successor_campaign/cellG'
BANKED_TERMS = ('/Users/dri/origin-axiom/frontier/B646_wave2_integration/cc2_packets/'
                'next_queue/next_queue/n1_counting/jeffrey_terms.json')
BANKED_P1 = ('/Users/dri/origin-axiom/frontier/B651_wave3_integration/cc2_packets/'
             'promotion_queue/promotion_queue/p1_milgram/p1_certificates.json')
P_WORD = 3
N0 = 2**6 * 3**3 * 5**4 * 7**2 * 11**2 * 19**2  # the melody theorem's period (formula, D2)

C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)

GATES = {}


def log(msg=""):
    print(msg, flush=True)


# ---------------------------------------------------------------- banked machinery
def weyl_group():
    """Verbatim from the banked engine (B600 packet)."""
    gens = []
    for j in range(6):
        M = np.eye(6, dtype=np.int64)
        M[j, :] -= C6[:, j]
        gens.append(M)
    I = np.eye(6, dtype=np.int64)
    seen = {I.tobytes()}
    mats, signs = [I], [1]
    frontier = [(I, 1)]
    while frontier:
        new = []
        for M, s in frontier:
            for g in gens:
                Mg = g @ M
                key = Mg.tobytes()
                if key not in seen:
                    seen.add(key)
                    new.append((Mg, -s))
                    mats.append(Mg)
                    signs.append(-s)
        frontier = new
    return np.array(mats), np.array(signs, dtype=np.int64)


def hnf_column(B):
    M = sp.Matrix(B.tolist())
    H = hermite_normal_form(M)
    return np.array(H.tolist(), dtype=np.int64)


def gauss_sum_banked(B, r):
    """Verbatim from n1_jeffrey_terms.py (the banked float path) — used as a gate."""
    Bs = sp.Matrix(B.tolist())
    det = int(Bs.det())
    ad = abs(det)
    Binv = Bs.inv()
    M = sp.Matrix(C6.tolist()) * Binv
    H = hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    assert np.prod(diag) == ad, (diag, ad)
    Mf = np.array([[Fraction(M[i, j]) for j in range(6)] for i in range(6)])
    total = 0j
    for x in itertools.product(*[range(d) for d in diag]):
        mu = np.array(x, dtype=object)
        q = Fraction(0)
        for i in range(6):
            if mu[i]:
                for j in range(6):
                    if mu[j]:
                        q += mu[i] * Mf[i, j] * mu[j]
        e = (r * q) % 2
        total += complex(mp.e ** (-1j * mp.pi * mp.mpf(e.numerator) / e.denominator))
    return total, ad


# ------------------------------------------------------- exact q-multiset per class
def q_multiset(B):
    """EXACT multiset {q(mu) mod 2 : mu in the HNF box} as Counter{Fraction: int}.
    Same box, same form as the banked gauss_sum — only the phase evaluation is
    deferred (kept exact)."""
    Bs = sp.Matrix(B.tolist())
    det = int(Bs.det())
    ad = abs(det)
    M = sp.Matrix(C6.tolist()) * Bs.inv()
    H = hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    assert np.prod(diag) == ad, (diag, ad)
    Mf = [[Fraction(M[i, j].p, M[i, j].q) for j in range(6)] for i in range(6)]
    D = 1
    for row in Mf:
        for v in row:
            D = D * v.denominator // math.gcd(D, v.denominator)
    Mi = [[int(v * D) for v in row] for row in Mf]
    twoD = 2 * D
    cnt = Counter()
    for x in itertools.product(*[range(d) for d in diag]):
        n = 0
        for i in range(6):
            xi = x[i]
            if xi:
                Mrow = Mi[i]
                for j in range(6):
                    if x[j]:
                        n += xi * Mrow[j] * x[j]
        cnt[Fraction(n % twoD, D)] += 1
    return cnt, ad


def sqfree_split(n):
    """n = s * f^2 with s squarefree; returns (s, f)."""
    s, f = 1, 1
    for p, e in sp.factorint(n).items():
        f *= p ** (e // 2)
        if e % 2:
            s *= p
    return s, f


def ord_of_q(q):
    """Minimal d > 0 with d*q in 2Z; q a Fraction in lowest terms."""
    a, b = q.numerator, q.denominator
    if a == 0:
        return 1
    return 2 * b if a % 2 else b


# ---------------------------------------------------------------- evaluators
def class_eval_mp(cls, r):
    """One class's G(r) from its exact multiset, at current mp.mp.dps."""
    tot = mp.mpc(0)
    for q, c in cls['mult'].items():
        e = (r * q) % 2
        tot += c * mp.e ** (-1j * mp.pi * mp.mpf(e.numerator) / e.denominator)
    return tot


def Z_mp(classes, r):
    """Z(r) per-class route (includes aggregate-cancelled q), at current dps."""
    tot = mp.mpc(0)
    for cls in classes:
        tot += cls['size'] * cls['sign'] * class_eval_mp(cls, r) / mp.sqrt(cls['det'])
    return tot / 51840


def Z_float_factory(classes):
    """Fast float evaluator (numpy) for witness searches. Safe for r < 1e15."""
    packs = []
    for cls in classes:
        a = np.array([q.numerator for q in cls['mult']], dtype=np.int64)
        b = np.array([q.denominator for q in cls['mult']], dtype=np.int64)
        c = np.array(list(cls['mult'].values()), dtype=np.float64)
        w = cls['size'] * cls['sign'] / math.sqrt(cls['det'])
        packs.append((a, b, c, w))

    def Z(r):
        assert 0 <= r < 10**15
        tot = 0j
        for a, b, c, w in packs:
            ph = ((r * a) % (2 * b)).astype(np.float64) / b.astype(np.float64)
            tot += w * np.sum(c * np.exp(-1j * np.pi * ph))
        return tot / 51840
    return Z


def main():
    t_start = time.time()
    log(f"=== CELL G / L100 — the resonant-phase law: exact minimal period — "
        f"{time.strftime('%Y-%m-%d %H:%M:%S')} ===")
    log(f"N0 (melody theorem, formula) = {N0} = 2^6*3^3*5^4*7^2*11^2*19^2")
    log(f"sanity: {N0} == {2**6*3**3*5**4*7**2*11**2*19**2}")

    # ---------------- PHASE 0: build W, buckets; gate against the banked table
    log("\n=== PHASE 0 — Weyl group + buckets (banked construction, verbatim) ===")
    t0 = time.time()
    W, eps = weyl_group()
    log(f"|W| = {len(W)}  ({time.time()-t0:.2f}s)")
    assert len(W) == 51840, "HARD STOP: Weyl group build mismatch"

    t0 = time.time()
    buckets = {}
    for idx in range(len(W)):
        w = W[idx]
        winv = np.rint(np.linalg.inv(w)).astype(np.int64)
        assert (w @ winv == np.eye(6, dtype=np.int64)).all()
        B = P_WORD * np.eye(6, dtype=np.int64) - w - winv
        cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
        spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
        buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))
    sorted_buckets = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
    log(f"buckets: {len(sorted_buckets)}  ({time.time()-t0:.2f}s)")
    assert len(sorted_buckets) == 25, "HARD STOP: expected the 25 banked classes"
    assert sum(len(m) for _, m in sorted_buckets) == 51840

    banked = json.load(open(BANKED_TERMS))
    banked_keys = sorted((row['size'], row['sign'], row['absdetB']) for row in banked['rows'])

    # ---------------- PHASE 1: exact q-multisets (2-rep exact class gate) + SNF
    log("\n=== PHASE 1 — exact q-multisets per class (2-rep EXACT equality gate) ===")
    classes = []
    gate_B_ok = True
    for bi, (key, members) in enumerate(sorted_buckets):
        idx0, B0, s0 = members[0]
        assert all(s == s0 for _, _, s in members)
        t0 = time.time()
        mult, ad = q_multiset(B0)
        if len(members) > 1:
            mult2, ad2 = q_multiset(members[1][1])
            same = (mult == mult2 and ad == ad2)
            gate_B_ok &= same
        else:
            same = None
        snf = smith_normal_form(sp.Matrix(B0.tolist()))
        divisors = [abs(int(snf[i, i])) for i in range(6) if abs(int(snf[i, i])) != 1]
        s, f = sqfree_split(ad)
        cls = dict(bucket=bi, size=len(members), sign=s0, det=ad, s=s, f=f,
                   charpoly=[int(c) for c in key[0]], divisors=divisors, mult=mult,
                   period=1)
        per = 1
        for q in mult:
            o = ord_of_q(q)
            per = per * o // math.gcd(per, o)
        cls['period'] = per
        classes.append(cls)
        log(f"  class {bi:>2}: size {len(members):>5} sign {s0:+d} |detB| {ad:>5} "
            f"= {s}*{f}^2  eldiv {divisors!s:<18} #q {len(mult):>4} "
            f"P_class {per:>6}  2-rep-exact {same}  ({time.time()-t0:.2f}s)")
    mine_keys = sorted((c['size'], c['sign'], c['det']) for c in classes)
    GATES['A0_banked_table'] = (mine_keys == banked_keys)
    GATES['B_2rep_exact'] = gate_B_ok
    log(f"GATE A0 (table == banked jeffrey_terms.json): {GATES['A0_banked_table']}")
    log(f"GATE B  (2-rep exact q-multiset equality):    {GATES['B_2rep_exact']}")
    assert GATES['A0_banked_table'] and GATES['B_2rep_exact'], "HARD STOP"

    # ---------------- PHASE 2: cross-gates against the banked evaluations
    log("\n=== PHASE 2 — cross-gates ===")
    mp.mp.dps = 30
    log("-- GATE A1: verbatim banked gauss_sum (float path) vs multiset eval, r = 13, 19 --")
    a1_max = 0.0
    for cls in classes:
        B0 = None  # recover the representative for the banked call
    # (representatives were consumed above; recompute from buckets in the same order)
    for cls, (key, members) in zip(classes, sorted_buckets):
        B0 = members[0][1]
        for r in (13, 19):
            g_banked, ad = gauss_sum_banked(B0, r)
            g_mine = complex(class_eval_mp(cls, r))
            a1_max = max(a1_max, abs(g_banked - g_mine))
    GATES['A1_banked_gauss'] = a1_max < 1e-9
    log(f"   max |banked - multiset| over 25 classes x (13, 19) = {a1_max:.3e}  "
        f"-> {GATES['A1_banked_gauss']}")

    log("-- GATE P1: G(13), G(29) == zeta_8^j * sqrt|detB| (cc2's exact certificates), dps 50 --")
    mp.mp.dps = 50
    p1 = json.load(open(BANKED_P1))
    p1_map = {(e['size'], e['sign'], e['absdet']): (e['j_13'], e['j_29']) for e in p1}
    assert len(p1_map) == 25
    p1_max = mp.mpf(0)
    for cls in classes:
        j13, j29 = p1_map[(cls['size'], cls['sign'], cls['det'])]
        assert j13 in (0, 4) and j29 in (0, 4)
        for r, j in ((13, j13), (29, j29)):
            g = class_eval_mp(cls, r)
            target = (1 if j == 0 else -1) * mp.sqrt(cls['det'])
            p1_max = max(p1_max, abs(g - target))
    GATES['P1_gamma_certs'] = p1_max < mp.mpf('1e-30')
    log(f"   max |G - zeta_8^j*sqrt(det)| over 25 classes x (13, 29) = {mp.nstr(p1_max, 3)}  "
        f"-> {GATES['P1_gamma_certs']}")

    log("-- GATE F1: the uniform jump law |G(r)|^2 = prod p^(a+min(v_p(r),a)), dps 50, "
        "quantize 1e-30 --")
    f1_rs = (13, 16, 19, 20, 45, 57)
    f1_ok, f1_n = True, 0
    for cls in classes:
        for r in f1_rs:
            g = class_eval_mp(cls, r)
            m2 = (g * mp.conj(g)).real
            pred = 1
            for d in cls['divisors']:
                for p, a in sp.factorint(d).items():
                    v = 0
                    rr = r
                    while rr % p == 0:
                        v += 1
                        rr //= p
                    pred *= p ** (a + min(v, a))
            ok = abs(m2 - pred) < mp.mpf('1e-30')
            f1_ok &= ok
            f1_n += 1
            if not ok:
                log(f"   F1 FAIL class {cls['bucket']} r={r}: |G|^2={mp.nstr(m2, 30)} "
                    f"pred={pred}")
    GATES['F1_jump_law'] = f1_ok
    log(f"   {f1_n} instances checked, all integer-quantized to the F1 prediction: {f1_ok}")

    log("-- GATE A2: totals at dps 50 (quantize 1e-30) --")
    a2 = {}
    for r, expect in ((13, 1), (16, 0), (19, 2), (17, 1), (23, 1), (29, 0)):
        z = Z_mp(classes, r)
        dev = abs(z - expect)
        a2[r] = dev < mp.mpf('1e-30')
        log(f"   Z({r}) = {mp.nstr(z.real, 20)} {mp.nstr(z.imag, 3)}i   expect {expect}  "
            f"dev {mp.nstr(dev, 3)}  -> {a2[r]}")
    GATES['A2_totals'] = all(a2.values())
    assert all(GATES.values()), f"HARD STOP: a phase-2 gate failed: {GATES}"

    # ---------------- PHASE 3: aggregation -> support -> THE MINIMAL PERIOD
    log("\n=== PHASE 3 — exact aggregation and the minimal period ===")
    agg = {}   # q -> {s: Fraction}
    for cls in classes:
        base = Fraction(cls['size'] * cls['sign'], cls['f'] * cls['s'] * 51840)
        for q, c in cls['mult'].items():
            agg.setdefault(q, {})
            agg[q][cls['s']] = agg[q].get(cls['s'], Fraction(0)) + base * c
    all_s = sorted({s for co in agg.values() for s in co})
    log(f"distinct q values across all classes: {len(agg)}")
    log(f"squarefree classes s present: {all_s}  (sqrt(s) linearly independent over Q)")

    support = {q: co for q, co in agg.items() if any(v != 0 for v in co.values())}
    cancelled = sorted(set(agg) - set(support))
    log(f"supported q (N_q != 0, exact): {len(support)};  aggregate-cancelled q: "
        f"{len(cancelled)}")
    if cancelled:
        log(f"  cancelled q values: {[str(q) for q in cancelled]}")

    P_min = 1
    for q in support:
        o = ord_of_q(q)
        P_min = P_min * o // math.gcd(P_min, o)
    L_class = 1
    for cls in classes:
        L_class = L_class * cls['period'] // math.gcd(L_class, cls['period'])

    log(f"\nTHE MINIMAL PERIOD (exact, from the aggregated character support):")
    log(f"  P_min = {P_min} = {sp.factorint(P_min)}")
    log(f"  lcm of per-class periods = {L_class} = {sp.factorint(L_class)}")
    log(f"  (equal iff no cross-class resonant cancellation affects the period)")
    GATES['C_divides_N0'] = (N0 % P_min == 0)
    GATES['C_multiple_of_5'] = (P_min % 5 == 0)
    log(f"GATE C: P_min | N0: {GATES['C_divides_N0']};  5 | P_min: "
        f"{GATES['C_multiple_of_5']}")
    log(f"  N0 / P_min = {N0 // P_min if N0 % P_min == 0 else 'NOT INTEGER'}")
    assert GATES['C_divides_N0'] and GATES['C_multiple_of_5'], "HARD STOP"

    # ---------------- PHASE 4: melody spot pairs + minimality witnesses
    log("\n=== PHASE 4 — periodicity spot pairs and minimality witnesses ===")
    mp.mp.dps = 30
    log(f"-- GATE D: Z(kappa) vs Z(kappa + P_min) on the D2 sealed rung set (per-class "
        f"route, dps 30) --")
    d_ok = True
    for k in (13, 29, 16, 25, 19, 45):
        z1, z2 = Z_mp(classes, k), Z_mp(classes, k + P_min)
        dev = abs(z1 - z2)
        ok = dev < mp.mpf('1e-25')
        d_ok &= ok
        log(f"   kappa={k:>3}: Z={mp.nstr(z1.real, 15)}{'+' if z1.imag >= 0 else ''}"
            f"{mp.nstr(z1.imag, 2)}i  Z(+P_min) dev = {mp.nstr(dev, 3)} -> {ok}")
    GATES['D_period_pairs'] = d_ok

    log(f"-- GATE E: for each prime p | P_min, a rung with Z(kappa) != Z(kappa + P_min/p) --")
    Zf = Z_float_factory(classes)
    witnesses = {}
    e_ok = True
    for p in sorted(sp.factorint(P_min)):
        d = P_min // p
        # algebraic certificate first: a supported q with d*q not in 2Z
        q_star = next(q for q in support if (d * q) % 2 != 0)
        found = None
        for k in range(13, 13 + 5000):
            if abs(Zf(k) - Zf(k + d)) > 1e-6:
                found = k
                break
        if found is None:
            e_ok = False
            log(f"   p={p}: NO float witness in [13, 5012] — algebraic certificate only: "
                f"q* = {q_star} (ord {ord_of_q(q_star)})")
            witnesses[p] = dict(d=d, q_star=str(q_star), kappa=None)
            continue
        mp.mp.dps = 50
        z1, z2 = Z_mp(classes, found), Z_mp(classes, found + d)
        dev = abs(z1 - z2)
        certified = dev > mp.mpf('1e-20')
        e_ok &= certified
        witnesses[p] = dict(d=d, q_star=str(q_star), kappa=found,
                            Z_kappa=[mp.nstr(z1.real, 30), mp.nstr(z1.imag, 30)],
                            Z_shift=[mp.nstr(z2.real, 30), mp.nstr(z2.imag, 30)],
                            dev=mp.nstr(dev, 20))
        log(f"   p={p}: d = P_min/{p} = {d};  witness kappa = {found}: "
            f"Z = {mp.nstr(z1.real, 12)}{'+' if z1.imag >= 0 else ''}{mp.nstr(z1.imag, 2)}i vs "
            f"Z(+d) = {mp.nstr(z2.real, 12)}{'+' if z2.imag >= 0 else ''}{mp.nstr(z2.imag, 2)}i, "
            f"|dev| = {mp.nstr(dev, 6)} (dps 50) -> {certified};  "
            f"algebraic q* = {q_star} (ord {ord_of_q(q_star)})")
    GATES['E_minimality_witnesses'] = e_ok

    # ---------------- PHASE 5: the resonant-rung table + persist
    log("\n=== PHASE 5 — one glance at the melody (kappa = 13..72, float) ===")
    row = []
    for k in range(13, 73):
        z = Zf(k)
        zr = round(z.real, 6)
        row.append(f"{k}:{zr:+.3f}" + (f"{z.imag:+.3f}i" if abs(z.imag) > 1e-6 else ""))
    for i in range(0, 60, 6):
        log("   " + "  ".join(row[i:i + 6]))

    # ---------------- PHASE 5b: addendum — the closed form + exact value ring
    log("\n=== PHASE 5b — addendum: the closed form and the resonant value ring ===")
    # (i) THE CLOSED FORM: P_min == lcm of ALL SNF elementary divisors across the
    #     25 classes == the exponent of the total discriminant group  +  A_w.
    lcm_div = 1
    for cls in classes:
        for dv in cls['divisors']:
            lcm_div = lcm_div * dv // math.gcd(lcm_div, dv)
    GATES['closed_form_lcm_divisors'] = (lcm_div == P_min)
    log(f"  lcm of all elementary divisors (exponent of the sum of the A_w) = {lcm_div}")
    log(f"  == P_min: {GATES['closed_form_lcm_divisors']}   (note: NO extra factor 2 — "
        f"the deepest dyadic q have even numerators, the even-type 2-adic structure of F1)")
    per_prime_cap = {}
    for cls in classes:
        for dv in cls['divisors']:
            for p, e in sp.factorint(dv).items():
                per_prime_cap[p] = max(per_prime_cap.get(p, 0), e)
    log(f"  per-prime elementary-divisor caps: {dict(sorted(per_prime_cap.items()))}")
    # (ii) resonant showcase values: exact quantization in Z[sqrt5] (fallback Z[phi])
    mp.mp.dps = 50
    s5 = mp.sqrt(5)
    log("  resonant showcase rungs, dps 50, quantized at 1e-30:")
    ring_ok = True
    for k in (16, 19, 20, 22, 24, 25, 30, 35, 36, 40, 45, 48, 55, 57, 60, 63, 70, 72,
              76, 88, 95, 100):
        z = Z_mp(classes, k)
        hit = None
        for b in range(-6, 7):
            a2 = 2 * (z.real - b * s5 / 2)
            an = mp.nint(a2)
            if abs(a2 - an) < mp.mpf('1e-30') and abs(z.imag) < mp.mpf('1e-30'):
                ia = int(an)
                if ia % 2 == 0 and b % 2 == 0:
                    hit = f"{ia//2:+d} {b//2:+d}*sqrt5   [Z[sqrt5]]"
                else:
                    hit = f"({ia:+d} {b:+d}*sqrt5)/2   [Z[phi]-level]"
                break
        ring_ok &= hit is not None
        log(f"    Z({k:>3}) = {mp.nstr(z.real, 25):>30}  ->  {hit}")
    GATES['resonant_values_quantized'] = ring_ok

    verdict_all = all(GATES.values())
    log(f"\n=== GATE SUMMARY ===")
    for k, v in GATES.items():
        log(f"  {k}: {'PASS' if v else 'FAIL'}")

    out = dict(
        P_min=P_min,
        P_min_factorization={str(p): e for p, e in sp.factorint(P_min).items()},
        N0=N0, N0_over_P_min=N0 // P_min,
        lcm_per_class_periods=L_class,
        gates={k: bool(v) for k, v in GATES.items()},
        witnesses=witnesses,
        squarefree_classes=all_s,
        n_support=len(support),
        cancelled_q=[str(q) for q in cancelled],
        support={str(q): {"ord": ord_of_q(q),
                          **{f"coeff_sqrt{s}": str(v) for s, v in co.items() if v != 0}}
                 for q, co in sorted(support.items())},
        classes=[{k: (v if k != 'mult' else {str(q): c for q, c in sorted(v.items())})
                  for k, v in cls.items()} for cls in classes],
    )
    with open(f"{CELL}/l100_results.json", "w") as fjson:
        json.dump(out, fjson, indent=1)
    log(f"\nresults -> {CELL}/l100_results.json")
    log(f"total wall time: {time.time()-t_start:.2f}s")
    if verdict_all:
        log(f"\nVERDICT: CERTIFIED — the melody's exact minimal period is {P_min} "
            f"= {sp.factorint(P_min)}")
    else:
        log("\nVERDICT: gates incomplete — see summary above")


if __name__ == '__main__':
    main()
