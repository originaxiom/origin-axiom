"""CELL R3 (part 2) — the E6-ladder per-class Landsberg-Schaar closed form.

TARGET: each of the 25 Weyl-class terms of the banked E6 Z-ladder
    G_w(r) = sum_{mu in Z^6/B_w Z^6} e^{-i pi r q(mu)},  q = mu^T C6 B_w^{-1} mu mod 2,
    B_w = 3I - w - w^{-1}   (P_WORD = 3 = tr of the golden monodromy)
gets its per-term closed form
    G_w(r) = prod_{p | det B_w}  zeta_8^{j_{w,p}(r)} * p^{k_{w,p}(r)/2}
with k = the F1 exponent  sum_blocks (a + min(v_p(r), a))  and j given by explicit
residue tables + the unit-scaling Jacobi law.  PROOF METHOD (fully exact):
  (1) primary splitting  (A_w, q) = orthosum_p (A_p, q_p):  CRT idempotents,
      orthogonality  q(x) = sum_p q(x_p) mod 2  verified exactly on EVERY box
      element  =>  G_w(r) = prod_p G_{w,p}(r)   (finite proof per class);
  (2) each G_{w,p} is periodic in r with period L_p = lcm ord(q_p)  (Artin
      character independence — the banked cellG argument);
  (3) exact cyclotomic evaluation of G_{w,p}(r) on EVERY residue r mod L_p as an
      integer vector in Z[zeta_M] reduced mod Phi_M, matched EXACTLY against the
      candidates zeta_8^j p^{k/2} (sqrt p realized by its quadratic Gauss sum,
      internally re-proved: g_p^2 = (-1)^{(p-1)/2} p).
  Periodic + equal on a full period  =>  the closed form holds for ALL r in Z.

GATES (banked cross-anchors):
  A0  class table == jeffrey_terms.json (B646);  SNF divisors + exact q-multisets
      == l100_results.json (B662/cellG).
  P1  closed form at r = 13, 29  ==  zeta_8^j sqrt|det B| with j from
      p1_certificates.json (B651) — exact match (the dev-2e-48 certificates).
  F1  the jump law |G|^2 = prod p^(a+min(v,a))  now PER-TERM on ALL residues.
  P   per-class period == cellG's;  lcm over classes == 175560  (B663/A2 / L100).
  G5  THE GENERIC LAW PER-TERM: Z(u) = (1 - (u|5))/2 for EVERY unit u mod 175560,
      assembled from the closed forms in exact Z[zeta_8] arithmetic (the B656/G2
      generic-5 subsequence, now a theorem of the 25 closed forms).
  SC  resonant showcase rungs vs the exact multiset route (dps 50, quantize 1e-30).

Provenance of replicated machinery: weyl_group/C6/bucket construction and the
HNF-box q-multiset verbatim from frontier/B662_successor_campaign/cellG/
l100_period.py (banked), itself verbatim from B600 engine.py + B646
n1_jeffrey_terms.py.  New files only; no tracked file modified.
Run: python3 r3_e6_perterm.py   (~10-20 min).
"""
import itertools
import json
import math
import os
import time
from collections import Counter
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))
CELLG = os.path.normpath(os.path.join(
    HERE, '..', '..', 'B662_successor_campaign', 'cellG', 'l100_results.json'))
BANKED_TERMS = os.path.normpath(os.path.join(
    HERE, '..', '..', 'B646_wave2_integration', 'cc2_packets', 'next_queue',
    'next_queue', 'n1_counting', 'jeffrey_terms.json'))
BANKED_P1 = os.path.normpath(os.path.join(
    HERE, '..', '..', 'B651_wave3_integration', 'cc2_packets', 'promotion_queue',
    'promotion_queue', 'p1_milgram', 'p1_certificates.json'))
P_WORD = 3
P_MIN_BANKED = 175560

C6 = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
               [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]],
              dtype=np.int64)
GATES = {}
OUT = {}
T0 = time.time()


def log(msg=""):
    print(msg, flush=True)


def weyl_group():
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


# ---------------------------------------------------------------- exact cyclotomics
class Cyc:
    """Exact integer arithmetic in Z[zeta_M] as length-M count vectors reduced
    mod Phi_M.  All coefficients stay python ints (exact)."""

    def __init__(self, M):
        self.M = M
        x = sp.symbols('x')
        phi = sp.Poly(sp.cyclotomic_poly(M, x), x)
        self.deg = phi.degree()
        self.red = []                      # x^k mod Phi_M as int tuple (len deg)
        for k in range(M):
            r = sp.Poly(x ** k, x).rem(phi)
            cs = [0] * self.deg
            for mono, c in r.terms():
                cs[mono[0]] = int(c)
            self.red.append(tuple(cs))

    def reduce(self, counts):
        """counts: dict power->int  ->  reduced coefficient tuple."""
        out = [0] * self.deg
        for k, c in counts.items():
            if c:
                rk = self.red[k % self.M]
                for i in range(self.deg):
                    out[i] += c * rk[i]
        return tuple(out)

    def zeta_pow(self, k, scale=1):
        return self.reduce({k % self.M: scale})

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def scal(self, a, s):
        return tuple(x * s for x in a)

    def is_zero(self, a):
        return all(x == 0 for x in a)


def sqrtp_vec(cyc, p):
    """sqrt(p) in Z[zeta_M] via the quadratic Gauss sum; exactness re-proved
    internally (g^2 == (-1)^((p-1)/2) p)."""
    M = cyc.M
    if p == 2:
        assert M % 8 == 0
        v = cyc.reduce({M // 8: 1, -M // 8 % M: 1})          # zeta8 + zeta8^-1
        return v
    assert M % p == 0 and M % 4 == 0
    g = {}
    for t in range(1, p):
        ls = sp.jacobi_symbol(t, p)
        k = (t * (M // p)) % M
        g[k] = g.get(k, 0) + int(ls)
    gv = cyc.reduce(g)
    # gate: g^2 = (-1)^((p-1)/2) * p  (exact polynomial square, reduced)
    x = sp.symbols('x')
    gpoly = sp.Poly(sum(c * x ** i for i, c in enumerate(gv)), x)
    sq = sp.Poly(gpoly * gpoly, x).rem(sp.Poly(sp.cyclotomic_poly(M, x), x))
    sqv = [0] * cyc.deg
    for mono, c in sq.terms():
        sqv[mono[0]] = int(c)
    target = (-1) ** ((p - 1) // 2) * p
    assert sqv[0] == target and all(c == 0 for c in sqv[1:]), f"gauss^2 fail p={p}"
    if p % 4 == 1:
        return gv
    # p = 3 mod 4: sqrt p = -i * g;  -i = zeta_M^{3M/4}
    counts = {}
    for i, c in enumerate(gv):
        if c:
            counts[(i + 3 * M // 4) % M] = counts.get((i + 3 * M // 4) % M, 0) + c
    return cyc.reduce(counts)


def ord_of_q(q):
    a, b = q.numerator, q.denominator
    if a == 0:
        return 1
    return 2 * b if a % 2 else b


def vp(n, p):
    v = 0
    while n and n % p == 0:
        v += 1
        n //= p
    return v


# ================================================================ PHASE 0 — classes
log("=== CELL R3 / E6 — the per-class Landsberg-Schaar closed form ===")
log("\n=== PHASE 0 — Weyl group, the 25 classes, banked-table gate ===")
W, eps = weyl_group()
assert len(W) == 51840
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
assert len(sorted_buckets) == 25
banked = json.load(open(BANKED_TERMS))
banked_keys = sorted((row['size'], row['sign'], row['absdetB']) for row in banked['rows'])
cellg = json.load(open(CELLG))
log(f"|W| = 51840, 25 classes  ({time.time()-T0:.1f}s)")

# ================================================================ PHASE 1+2 — split
log("\n=== PHASE 1/2 — exact q-multisets, primary splitting, orthogonality proof ===")
classes = []
for bi, (key, members) in enumerate(sorted_buckets):
    t0 = time.time()
    idx0, B0, s0 = members[0]
    Bs = sp.Matrix(B0.tolist())
    det = abs(int(Bs.det()))
    Hm = hermite_normal_form(Bs)
    H = np.array(Hm.tolist(), dtype=np.int64)
    assert all(H[i, j] == 0 for i in range(6) for j in range(6) if i > j), "HNF not upper-tri"
    diag = [int(H[i, i]) for i in range(6)]
    assert int(np.prod(diag)) == det
    Minv = Bs.inv()
    Mq = sp.Matrix(C6.tolist()) * Minv
    Mf = [[Fraction(Mq[i, j].p, Mq[i, j].q) for j in range(6)] for i in range(6)]
    D = 1
    for row in Mf:
        for v in row:
            D = D * v.denominator // math.gcd(D, v.denominator)
    Mi = [[int(v * D) for v in row] for row in Mf]
    twoD = 2 * D
    Hc = [tuple(int(H[i, j]) for i in range(6)) for j in range(6)]   # columns

    def qval(vec):
        n = 0
        for i in range(6):
            xi = vec[i]
            if xi:
                Mrow = Mi[i]
                for j in range(6):
                    if vec[j]:
                        n += xi * Mrow[j] * vec[j]
        return Fraction(n % twoD, D)

    def reduce_box(vec):
        v = list(vec)
        for i in range(5, -1, -1):
            t = v[i] // diag[i]
            if t:
                col = Hc[i]
                for r in range(6):
                    v[r] -= t * col[r]
        assert all(0 <= v[i] < diag[i] for i in range(6))
        return tuple(v)

    snf = smith_normal_form(Bs)
    divisors = [abs(int(snf[i, i])) for i in range(6) if abs(int(snf[i, i])) != 1]
    e_exp = 1
    for dv in divisors:
        e_exp = e_exp * dv // math.gcd(e_exp, dv)
    primes = sorted(sp.factorint(det)) if det > 1 else []
    # CRT idempotent coefficients
    coef = {}
    for p in primes:
        ep = p ** vp(e_exp, p)
        mpart = e_exp // ep
        cp = pow(mpart, -1, ep)
        coef[p] = (cp * mpart) % e_exp

    box = list(itertools.product(*[range(d) for d in diag]))
    mult_full = Counter()
    Ap_elems = {p: set() for p in primes}
    qcache = {}
    ortho_ok = True
    for x in box:
        qx = qval(x)
        mult_full[qx] += 1
        ssum = Fraction(0)
        for p in primes:
            xp = reduce_box(tuple(coef[p] * c for c in x))
            Ap_elems[p].add(xp)
            if xp not in qcache:
                qcache[xp] = qval(xp)
            ssum += qcache[xp]
        if primes and (ssum - qx) % 2 != 0:
            ortho_ok = False
    sizes = {p: len(Ap_elems[p]) for p in primes}
    assert ortho_ok, f"HARD STOP: orthogonality fails class {bi}"
    prod = 1
    for p in primes:
        s = sizes[p]
        assert s == p ** vp(s, p) or s == 1, (bi, p, s)
        prod *= s
    assert prod == det, f"HARD STOP: CRT sizes class {bi}: {sizes} vs det {det}"
    mult_p = {p: Counter(qcache[xp] for xp in Ap_elems[p]) for p in primes}
    # cross-gates vs cellG: exact multiset + divisors
    g_mult = {Fraction(k): v for k, v in cellg['classes'][bi]['mult'].items()}
    gate_mult = (g_mult == dict(mult_full))
    gate_div = (cellg['classes'][bi]['divisors'] == divisors)
    classes.append(dict(bucket=bi, size=len(members), sign=s0, det=det,
                        divisors=divisors, primes=primes, mult=mult_full,
                        mult_p=mult_p, period_banked=cellg['classes'][bi]['period']))
    log(f"  class {bi:>2}: size {len(members):>5} sign {s0:+d} det {det:>5} "
        f"eldiv {divisors!s:<20} |A_p| {sizes}  multiset==cellG {gate_mult} "
        f"divisors==cellG {gate_div}  ortho EXACT-ALL {ortho_ok} ({time.time()-t0:.1f}s)")
    assert gate_mult and gate_div
mine_keys = sorted((c['size'], c['sign'], c['det']) for c in classes)
GATES['A0_banked_table'] = (mine_keys == banked_keys)
log(f"GATE A0 (table == banked jeffrey_terms.json): {GATES['A0_banked_table']}")
assert GATES['A0_banked_table']
GATES['SPLIT_orthogonality_all25'] = True

# ================================================================ PHASE 3 — closed forms
log("\n=== PHASE 3 — exact per-(class, p) closed forms on every residue ===")
CYCS = {}
resisting = []
for cls in classes:
    bi = cls['bucket']
    cls['tables'] = {}
    for p in cls['primes']:
        mset = cls['mult_p'][p]
        Lp = 1
        den_max = 1
        for q in mset:
            Lp = Lp * ord_of_q(q) // math.gcd(Lp, ord_of_q(q))
            den_max = max(den_max, q.denominator)
        if p == 2:
            M = int(np.lcm(16, 2 * den_max))
        else:
            M = int(np.lcm.reduce([8, 2 * den_max, 4 * p]))
        if M not in CYCS:
            CYCS[M] = Cyc(M)
        cyc = CYCS[M]
        sp_vec = sqrtp_vec(cyc, p)
        # divisors of this p: block exponents a_d
        ads = [vp(dv, p) for dv in cls['divisors'] if dv % p == 0]
        Sa = sum(ads)
        vLp = vp(Lp, p)
        table = []
        for r in range(Lp):
            counts = {}
            for q, c in mset.items():
                e = (r * q) % 2
                idx = int(-e * M // 2) % M          # e^{-i pi e} = zeta_M^{-eM/2}
                counts[idx] = counts.get(idx, 0) + c
            gv = cyc.reduce(counts)
            v = vp(r, p) if r != 0 else 10 ** 9      # r ≡ 0 mod Lp => full jump
            kpred = sum(a + min(v, a) for a in ads)
            hit = None
            for kk in (kpred, kpred - 1, kpred + 1, kpred - 2, kpred + 2):
                if kk < 0:
                    continue
                # exact route: build each candidate zeta_8^j * p^{kk/2} directly in
                # power space (sqrt p via its quadratic Gauss sum), then reduce
                for j in range(8):
                    if kk % 2 == 0:
                        cnt = {(j * M // 8) % M: p ** (kk // 2)}
                        cvec = cyc.reduce(cnt)
                    else:
                        # sqrt(p)*zeta_8^j * p^{(kk-1)//2}: shift the GAUSS SUM in
                        # power space before reduction
                        cnt = {}
                        if p == 2:
                            base_pows = {M // 8: 1, (-M // 8) % M: 1}
                        elif p % 4 == 1:
                            base_pows = {}
                            for t in range(1, p):
                                k2 = (t * (M // p)) % M
                                base_pows[k2] = base_pows.get(k2, 0) + int(
                                    sp.jacobi_symbol(t, p))
                        else:
                            base_pows = {}
                            for t in range(1, p):
                                k2 = (t * (M // p) + 3 * M // 4) % M
                                base_pows[k2] = base_pows.get(k2, 0) + int(
                                    sp.jacobi_symbol(t, p))
                        for k2, c in base_pows.items():
                            kk2 = (k2 + j * M // 8) % M
                            cnt[kk2] = cnt.get(kk2, 0) + c * p ** ((kk - 1) // 2)
                        cvec = cyc.reduce(cnt)
                    if cyc.is_zero(cyc.sub(gv, cvec)):
                        hit = (j, kk)
                        break
                if hit:
                    break
            if hit is None and cyc.is_zero(gv):
                hit = (None, None)                   # exact zero
            if hit is None:
                resisting.append(dict(bucket=bi, p=p, r=r, Lp=Lp,
                                      vec=[int(c) for c in gv]))
                table.append(dict(r=r, j=None, k=None, zero=False, resist=True))
            else:
                j, kk = hit
                table.append(dict(r=r, j=j, k=kk,
                                  zero=(j is None), F1=(kk == kpred if kk is not None
                                                        else False)))
        cls['tables'][p] = dict(L=Lp, M=M, table=table, ads=ads)
    log(f"  class {bi:>2}: " + "  ".join(
        f"p={p}: L={cls['tables'][p]['L']} "
        f"[{'OK' if all(row.get('j') is not None or row.get('zero') for row in cls['tables'][p]['table']) else 'RESIST'}]"
        for p in cls['primes']) + ("   (det 1, trivial G=1)" if not cls['primes'] else ""))

GATES['P3_all_matched'] = (len(resisting) == 0)
log(f"\nGATE P3 (every (class,p,residue) matched zeta_8^j p^(k/2) or exact 0): "
    f"{GATES['P3_all_matched']}  (resisting: {len(resisting)})")
if resisting:
    for rr in resisting[:10]:
        log(f"  RESIST class {rr['bucket']} p={rr['p']} r={rr['r']}/{rr['Lp']}")

# F1 per-term on all residues
f1_all = all(row['F1'] or row['zero'] for cls in classes for p in cls['primes']
             for row in cls['tables'][p]['table'])
zeros = sum(1 for cls in classes for p in cls['primes']
            for row in cls['tables'][p]['table'] if row['zero'])
GATES['F1_per_term_all_residues'] = f1_all
log(f"GATE F1-per-term (k == sum(a+min(v,a)) at EVERY residue, no zeros): "
    f"{f1_all}   exact-zero cells: {zeros}")

# ================================================================ PHASE 4 — the laws
log("\n=== PHASE 4 — the unit-scaling Jacobi law ===")
law_ok = True
law_rows = []
for cls in classes:
    for p in cls['primes']:
        tab = cls['tables'][p]
        L, table = tab['L'], tab['table']
        tp = sum(tab['ads'])                       # v_p(|A_p|)
        units = [u for u in range(1, L) if math.gcd(u, L) == 1] or [1]
        j1 = table[1 % L]['j'] if L > 1 else table[0]['j']
        ok_p = True
        for u in units:
            ju = table[u]['j']
            if p == 2:
                continue                            # dyadic law fitted below
            pred_flip = (sp.jacobi_symbol(u, p) ** tp) == -1
            ok_p &= (ju == ((j1 + 4) % 8 if pred_flip else j1))
        if p != 2:
            law_ok &= ok_p
            law_rows.append((cls['bucket'], p, tp, ok_p))
log(f"  odd p: G_p(u) = (u|p)^(v_p|A_p|) * G_p(1) on ALL units, every class: "
    f"{all(r[3] for r in law_rows)}")
GATES['LAW_odd_jacobi'] = all(r[3] for r in law_rows)
# dyadic character fit
dy_rows = []
dy_ok = True
for cls in classes:
    if 2 not in cls['primes']:
        continue
    tab = cls['tables'][2]
    L, table = tab['L'], tab['table']
    units = [u for u in range(1, L, 2)]
    j1 = table[1 % L]['j']
    chi = {}
    for u in units:
        chi[u % min(L, 8) if L >= 8 else u % L] = (table[u]['j'] - j1) % 8
    mult_ok = True
    for u in units:
        for v in units:
            uv = (u * v) % L
            if ((table[u]['j'] - j1) + (table[v]['j'] - j1)) % 8 != (table[uv]['j'] - j1) % 8:
                mult_ok = False
    dy_ok &= mult_ok
    dy_rows.append((cls['bucket'], dict(sorted(chi.items())), mult_ok))
log(f"  p = 2: chi(u) = zeta_8^(j(u)-j(1)) is multiplicative on units, every class: {dy_ok}")
for bi, chi, mok in dy_rows:
    log(f"    class {bi:>2}: chi table (u mod 8 -> 8*arg/2pi): {chi}  mult {mok}")
GATES['LAW_dyadic_character'] = dy_ok

# ================================================================ PHASE 5 — gates
log("\n=== PHASE 5 — banked-certificate gates ===")


def closed_G(cls, r):
    """(j_total mod 8, half-integer exponent dict p->k) from the tables; None if a
    zero cell is hit."""
    jt, ks = 0, {}
    for p in cls['primes']:
        tab = cls['tables'][p]
        row = tab['table'][r % tab['L']]
        if row['zero']:
            return None
        jt = (jt + row['j']) % 8
        ks[p] = row['k']
    return jt, ks


log("-- GATE P1: closed form at r = 13, 29 vs cc2's banked gamma certificates --")
p1 = json.load(open(BANKED_P1))
p1_map = {(e['size'], e['sign'], e['absdet']): (e['j_13'], e['j_29']) for e in p1}
p1_ok = True
for cls in classes:
    j13b, j29b = p1_map[(cls['size'], cls['sign'], cls['det'])]
    for r, jb in ((13, j13b), (29, j29b)):
        res = closed_G(cls, r)
        assert res is not None
        jt, ks = res
        # at unit rungs v_p(r) = 0: k = sum(a) exactly, i.e. |G| = sqrt(det)
        full = all(ks[p] == sum(vp(dv, p) for dv in cls['divisors'] if dv % p == 0)
                   for p in cls['primes'])
        if not ((jt == jb) and full):
            log(f"   MISMATCH class {cls['bucket']} r={r}: closed (j={jt}, k={ks}) "
                f"vs banked j={jb}")
        p1_ok &= (jt == jb) and full
log(f"   all 25 classes, r = 13 and 29: closed form == zeta_8^j sqrt|detB| with the "
    f"BANKED j (exact): {p1_ok}")
GATES['P1_certificates_exact'] = p1_ok

log("-- GATE P: per-class periods and the minimal period --")
P_lcm = 1
per_ok = True
for cls in classes:
    Pc = 1
    for p in cls['primes']:
        L = cls['tables'][p]['L']
        Pc = Pc * L // math.gcd(Pc, L)
    per_ok &= (Pc == cls['period_banked'])
    P_lcm = P_lcm * Pc // math.gcd(P_lcm, Pc)
GATES['P_class_periods'] = per_ok
GATES['P_min_175560'] = (P_lcm == P_MIN_BANKED)
log(f"   per-class period == cellG banked P_class, all 25: {per_ok}")
log(f"   lcm over classes = {P_lcm} == 175560: {GATES['P_min_175560']}")

log("-- GATE G5: the generic law Z(u) = (1-(u|5))/2 on EVERY unit u mod 175560 --")
t0 = time.time()
g5_ok = True
bad_u = None
# precompute per-class unit lookup: j_total(u) via tables
for u in range(1, P_MIN_BANKED):
    if (u % 2 == 0 or u % 3 == 0 or u % 5 == 0 or u % 7 == 0 or u % 11 == 0
            or u % 19 == 0):
        continue
    acc = [0, 0, 0, 0]                              # Z[zeta_8] coords, Phi_8 = x^4+1
    for cls in classes:
        jt = 0
        for p in cls['primes']:
            tab = cls['tables'][p]
            jt += tab['table'][u % tab['L']]['j']
        jt %= 8
        c = cls['size'] * cls['sign']
        if jt < 4:
            acc[jt] += c
        else:
            acc[jt - 4] -= c
    expect = (1 - sp.jacobi_symbol(u, 5)) // 2
    if not (acc[0] == expect * 51840 and acc[1] == 0 and acc[2] == 0 and acc[3] == 0):
        g5_ok = False
        bad_u = (u, acc)
        break
GATES['G5_generic_law_all_units'] = g5_ok
log(f"   phi(175560) = 34560 units checked, Z(u) == (1-(u|5))/2 exactly in Z[zeta_8]: "
    f"{g5_ok}  ({time.time()-t0:.1f}s)" + (f"  FIRST FAIL {bad_u}" if bad_u else ""))

log("-- GATE SC: resonant showcase rungs — closed-form vs exact-multiset route, dps 50 --")
mp.mp.dps = 50
sc_max = mp.mpf(0)
sc_rows = []
for r in (13, 16, 19, 20, 25, 29, 35, 36, 40, 45, 48, 55, 57, 60, 63, 70, 72, 76, 95, 100):
    zc = mp.mpc(0)
    zm = mp.mpc(0)
    for cls in classes:
        # multiset route
        g = mp.mpc(0)
        for q, c in cls['mult'].items():
            e = (r * q) % 2
            g += c * mp.e ** (-1j * mp.pi * mp.mpf(e.numerator) / e.denominator)
        zm += cls['size'] * cls['sign'] * g / mp.sqrt(cls['det'])
        # closed-form route
        res = closed_G(cls, r)
        assert res is not None, (cls['bucket'], r)
        jt, ks = res
        mag = mp.mpf(1)
        for p, kk in ks.items():
            mag *= mp.sqrt(p) ** kk
        zc += cls['size'] * cls['sign'] * (mp.e ** (2j * mp.pi * jt / 8)) * mag \
            / mp.sqrt(cls['det'])
    zc, zm = zc / 51840, zm / 51840
    sc_max = max(sc_max, abs(zc - zm))
    sc_rows.append((r, mp.nstr(zc.real, 20), mp.nstr(zc.imag, 3)))
    log(f"   Z({r:>3}) = {mp.nstr(zc.real, 18):>24}  dev(closed vs multiset) = "
        f"{mp.nstr(abs(zc - zm), 3)}")
GATES['SC_showcase'] = sc_max < mp.mpf('1e-30')
log(f"   max dev over 20 rungs: {mp.nstr(sc_max, 3)}  -> {GATES['SC_showcase']}")

# named cellG resonant values
named = {35: '-sqrt5', 70: '-sqrt5', 55: '1-sqrt5', 60: '1-sqrt5', 40: '2-sqrt5',
         19: '2', 57: '2', 76: '2', 95: '2', 48: '3', 72: '3', 36: '-2', 63: '-1',
         13: '1', 16: '0'}
s5 = mp.sqrt(5)
namevals = {'-sqrt5': -s5, '1-sqrt5': 1 - s5, '2-sqrt5': 2 - s5, '2': mp.mpf(2),
            '3': mp.mpf(3), '-2': mp.mpf(-2), '-1': mp.mpf(-1), '1': mp.mpf(1),
            '0': mp.mpf(0)}
nv_ok = True
for r, s in named.items():
    zc = [row for row in sc_rows if row[0] == r]
    got = mp.mpf(zc[0][1])
    nv_ok &= abs(got - namevals[s]) < mp.mpf('1e-18')
GATES['SC_named_cellG_values'] = nv_ok
log(f"   named cellG resonant values (35:-sqrt5, 48:3, 36:-2, ...) reproduced: {nv_ok}")

# ================================================================ summary + persist
log("\n=== GATE SUMMARY ===")
for k, v in GATES.items():
    log(f"  {k}: {'PASS' if v else 'FAIL'}")
verdict = all(GATES.values())

OUT['gates'] = {k: bool(v) for k, v in GATES.items()}
OUT['P_lcm'] = P_lcm
OUT['resisting'] = resisting
OUT['zero_cells'] = zeros
OUT['classes'] = []
for cls in classes:
    OUT['classes'].append(dict(
        bucket=cls['bucket'], size=cls['size'], sign=cls['sign'], det=cls['det'],
        divisors=cls['divisors'],
        tables={str(p): dict(L=cls['tables'][p]['L'],
                             jk=[[row['r'], row['j'], row['k']] for row in
                                 cls['tables'][p]['table']])
                for p in cls['primes']}))
with open(os.path.join(HERE, 'r3_e6_results.json'), 'w') as f:
    json.dump(OUT, f, indent=1, default=str)
log(f"\nresults -> r3_e6_results.json   ({time.time()-T0:.1f}s)")
if verdict:
    log("\nVERDICT: the per-class Landsberg-Schaar closed form is PROVEN for all 25")
    log("E6-ladder class terms (exact primary splitting + exact cyclotomic")
    log("certification on every residue), reproducing the banked P1 certificates,")
    log("the F1 jump law on ALL residues, the exact period 175560, and the")
    log("generic-5 law as a THEOREM of the closed forms.")
else:
    log("\nVERDICT: incomplete — see gate summary / resisting list")
