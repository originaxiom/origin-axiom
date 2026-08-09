#!/usr/bin/env python3
"""B973 / L135 -- WHICH CHARGES HAVE IRRATIONAL WEIGHTS ON M12?

weightlines.py found that the simultaneous weight-line decomposition of M12 is
visible only at SOME primes: 4 of 10 kappa-split primes in the window, and every
failure was the same shape -- charge g14, one 2-dim piece, residual degree
exactly 2. That pattern is a measurement, not an accident, so measure it
directly: for EACH of the four charges independently, does the characteristic
polynomial of ad(g_i)|M12 split over F_p?

The frame is split (2,2) into a NONCOMPACT pair {g8,g16} and a COMPACT pair
{g14,g22} (CMT_DRAFT.md:23-25). The question this file answers is whether the
weight-field behaviour respects that split.

REPRESENTATION: adjoint sector throughout; g_i in e6, M12 subset e6. No 27 VEV.
TIER: mod p, many primes. Splitting DENSITY is Chebotarev evidence about the
weight field; it does NOT identify the field. Nothing banked.
"""
import sys, json, time
sys.path.insert(0, str(_REPO / "frontier/B961_frame_instrument"))
import sympy as sp
import frame
import pathlib as _pl
_REPO = _pl.Path(__file__).resolve().parents[2]

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)

DIM = frame.DIM; BB = frame.BB
INV = frame._G["INV"]; NS = [8, 14, 16, 22]; CH = {n: INV[n] for n in NS}
R = {}

AD = {n: frame.ad(CH[n]) for n in NS}
core = AD[8].nullspace(); Bc = sp.Matrix.hstack(*core); cdim = Bc.shape[1]
P = (Bc.T * Bc).inv() * Bc.T
C14 = P * AD[14] * Bc; fl = C14.nullspace()
Bf = Bc * sp.Matrix.hstack(*fl); fdim = Bf.shape[1]
piv = list(sp.Matrix(sp.Matrix.hstack(*fl).T).rref()[1])
comp = [i for i in range(cdim) if i not in piv][: cdim - fdim]
Tm = sp.Matrix.hstack(sp.Matrix.hstack(*fl), sp.eye(cdim)[:, comp]); Ti = Tm.inv()
C22 = P * AD[22] * Bc
Q14 = (Ti * C14 * Tm)[fdim:, fdim:]; Q22 = (Ti * C22 * Tm)[fdim:, fdim:]
s = sp.symbols('s'); qd = Q14.shape[0]
nu = sp.expand(sp.interpolate(
    list(zip(range(qd + 1), [(Q14 + sp.Rational(x) * Q22).det() for x in range(qd + 1)])), s))
kap = [sp.Poly(sp.primitive(f_)[1], s) for f_, m_ in sp.factor_list(sp.Poly(nu, s))[1]
       if m_ == 6 and sp.degree(f_, s) == 3][0]
kco = [int(kap.as_expr().coeff(s, i)) for i in range(4)]
assert kco == [-6859, -56402640, 3033676800, 2771822592000]
K = [[0] * DIM for _ in range(DIM)]
SP = [[(q, kk, BB[i][q][kk]) for q in range(DIM) for kk in range(DIM) if BB[i][q][kk]]
      for i in range(DIM)]
for i in range(DIM):
    for j in range(i, DIM):
        t = 0
        for (q, kk, c) in SP[i]:
            d = BB[j][kk][q]
            if d: t += c * d
        K[i][j] = int(t); K[j][i] = int(t)
log("build ready (floor 12, kappa reproduced)")


def per_charge(p):
    def rd(x):
        x = sp.Rational(x); return x.p % p * pow(x.q % p, p - 2, p) % p
    def mp(M): return [[rd(M[i, j]) for j in range(M.shape[1])] for i in range(M.shape[0])]
    def rref(rows):
        rows = [x[:] for x in rows]; n = len(rows[0]) if rows else 0; wh = {}; rk = 0
        for c in range(n):
            pv = next((i for i in range(rk, len(rows)) if rows[i][c]), None)
            if pv is None: continue
            rows[rk], rows[pv] = rows[pv], rows[rk]
            iv = pow(rows[rk][c], p - 2, p); rows[rk] = [v * iv % p for v in rows[rk]]
            for i in range(len(rows)):
                if i != rk and rows[i][c]:
                    f = rows[i][c]
                    rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[rk])]
            wh[c] = rk; rk += 1
        return rows, wh, rk
    def null(rows, n):
        rr, wh, _ = rref(rows); out = []
        for fc in [c for c in range(n) if c not in wh]:
            v = [0] * n; v[fc] = 1
            for c, rw in wh.items(): v[c] = (-rr[rw][fc]) % p
            out.append(v)
        return out
    ADp = {n: mp(AD[n]) for n in NS}
    Kp = [[K[i][j] % p for j in range(DIM)] for i in range(DIM)]
    # Does mu split too? kappa and mu generate ONE cubic field K (CMT_DRAFT.md:78-80,
    # CITED). If that is right, every kappa-split prime is mu-split. CHECK it here
    # rather than inherit it -- the whole reading of the result depends on it.
    mu_solo = [2197, -4769856, -2075673600, 500716339200]
    mur = sorted(x for x in range(p)
                 if sum(c * pow(x, t, p) for t, c in enumerate(mu_solo)) % p == 0)
    kr = sorted(x for x in range(p) if sum(c * pow(x, i, p) for i, c in enumerate(kco)) % p == 0)
    W = [null([[(ADp[14][i][j] + r0 * ADp[22][i][j]) % p for j in range(DIM)]
               for i in range(DIM)], DIM) for r0 in kr]
    M12 = null([[sum(v[i] * Kp[i][j] for i in range(DIM) if v[i]) % p for j in range(DIM)]
                for v in W[0] + W[1] + W[2]], DIM)
    m = len(M12)
    if m != 12:
        return {"M12_dim": m, "bad": True}
    Bm = [list(x) for x in zip(*M12)]
    out = {"M12_dim": m, "n_mu_roots": len(mur), "mu_splits": len(mur) == 3,
           "n_kappa_roots": len(kr)}
    for n in NS:
        img = [[sum(ADp[n][i][kk] * v[kk] for kk in range(DIM) if v[kk]) % p
                for i in range(DIM)] for v in M12]
        aug = [[Bm[i][j] for j in range(m)] + [img[t][i] for t in range(m)] for i in range(DIM)]
        rr2, wh2, rk2 = rref(aug)
        A = [[rr2[wh2[c]][m + t] for t in range(m)] for c in range(m)]
        # char poly, degree 12 STRUCTURALLY; 13 nodes + 4 surplus checks
        def dv(x0):
            M = [[(A[i][j] - (x0 if i == j else 0)) % p for j in range(m)] for i in range(m)]
            d = 1
            for c in range(m):
                pv = next((i for i in range(c, m) if M[i][c]), None)
                if pv is None: return 0
                if pv != c: M[c], M[pv] = M[pv], M[c]; d = (-d) % p
                d = d * M[c][c] % p; iv = pow(M[c][c], p - 2, p)
                M[c] = [v * iv % p for v in M[c]]
                for i in range(c + 1, m):
                    if M[i][c]:
                        f = M[i][c]; M[i] = [(a - f * b) % p for a, b in zip(M[i], M[c])]
            return d % p
        xs = list(range(m + 1)); ys = [dv(x) for x in xs]; co = [0] * (m + 1)
        for i in range(m + 1):
            num = [1]; den = 1
            for j in range(m + 1):
                if j == i: continue
                num = [((([0] + num)[t] if t < len(num) + 1 else 0)
                        + (-xs[j]) % p * ((num + [0])[t])) % p for t in range(len(num) + 1)]
                den = den * (xs[i] - xs[j]) % p
            di = pow(den % p, p - 2, p)
            for t in range(len(num)): co[t] = (co[t] + ys[i] * di % p * num[t]) % p
        surplus = all(sum(c * pow(x0 % p, t, p) for t, c in enumerate(co)) % p == dv(x0 % p)
                      for x0 in range(-4, 0))
        rts = [x for x in range(p) if sum(c * pow(x, t, p) for t, c in enumerate(co)) % p == 0]
        # total multiplicity in F_p, via nullities of powers (semisimple => nullity is enough)
        tot = 0
        for lam in rts:
            tot += len(null([[(A[i][j] - (lam if i == j else 0)) % p for j in range(m)]
                             for i in range(m)], m))
        out[f"g{n}"] = {"distinct_Fp_roots": len(rts), "Fp_multiplicity_total": tot,
                        "splits_over_Fp": tot == m, "residual_degree": m - tot,
                        "surplus_ok": surplus}
    return out


# NOTE ON WHAT "splits over F_p" MEANS HERE (this governs the whole reading):
# every prime in the scan is chosen to split kappa. kappa and mu generate ONE
# cubic field K (CMT_DRAFT.md:78-80, CITED; re-checked per prime below via
# mu_splits). So a weight lying in F_p at EVERY kappa-split prime is evidence
# that the weight lies in K -- NOT that it is rational. A weight failing to lie
# in F_p at some kappa-split primes is evidence that it lies in a field strictly
# larger than K. That is the distinction this file measures.


denoms = {c.denominator for n in NS for c in CH[n] if c}
USED = {40009, 40013, 40037, 40039, 40063, 40123, 40639, 40829, 40883}
cands, q = [], 41000
while len(cands) < 24:
    q = int(sp.nextprime(q))
    if q in USED or any(d % q == 0 for d in denoms) or kco[3] % q == 0:
        continue
    if len({x for x in range(q)
            if sum(c * pow(x, i, q) for i, c in enumerate(kco)) % q == 0}) == 3:
        cands.append(q)
log(f"{len(cands)} kappa-split primes: {cands}")

rows = []
for p in cands:
    r = per_charge(p)
    if r.get("bad"):
        log(f"  p={p}: M12 dim {r['M12_dim']} != 12 -- skipped"); continue
    rows.append({"p": p, "mu_splits": r["mu_splits"], "n_mu_roots": r["n_mu_roots"],
                 **{f"g{n}": r[f"g{n}"] for n in NS}})
    log(f"  p={p}: mu_splits={r['mu_splits']}  " + "  ".join(
        f"g{n} split={r[f'g{n}']['splits_over_Fp']} res={r[f'g{n}']['residual_degree']}"
        for n in NS))
R["per_prime"] = rows
R["n_primes"] = len(rows)
R["mu_splits_at_every_kappa_split_prime"] = all(x["mu_splits"] for x in rows)
log(f"mu splits at every kappa-split prime: "
    f"{R['mu_splits_at_every_kappa_split_prime']}  "
    "(so 'in F_p' here means 'in the wall field K', not 'rational')")
summary = {}
for n in NS:
    ns = sum(1 for x in rows if x[f"g{n}"]["splits_over_Fp"])
    resid = sorted({x[f"g{n}"]["residual_degree"] for x in rows})
    summary[f"g{n}"] = {"split_count": ns, "of": len(rows),
                        "density": round(ns / len(rows), 3),
                        "residual_degrees_seen": resid,
                        "always_splits": ns == len(rows)}
R["summary"] = summary
R["surplus_checks_all_ok"] = all(x[f"g{n}"]["surplus_ok"] for x in rows for n in NS)
log("SUMMARY (split count / primes, residual degrees seen):")
for n in NS:
    S = summary[f"g{n}"]
    log(f"  g{n:2d}: {S['split_count']}/{S['of']} (density {S['density']}), "
        f"residual degrees {S['residual_degrees_seen']}, always splits: {S['always_splits']}")
# the frame's compact/noncompact split, as a testable statement
nc = summary["g8"]["always_splits"] and summary["g16"]["always_splits"]
cp = (not summary["g14"]["always_splits"]) and (not summary["g22"]["always_splits"])
R["noncompact_weights_in_F_p_at_every_kappa_split_prime"] = nc
R["compact_weights_NOT_in_F_p_at_some_kappa_split_primes"] = cp
R["weight_field_respects_frame_split"] = bool(nc and cp)
log(f"noncompact pair {{g8,g16}}: in F_p at every kappa-split prime = {nc} "
    "(evidence: those weights lie in the wall field K)")
log(f"compact pair {{g14,g22}}: fails at some kappa-split primes = {cp} "
    "(evidence: those weights lie in a proper extension of K)")
log(f"=> weight-field behaviour respects the frame's compact/noncompact split: "
    f"{R['weight_field_respects_frame_split']}")
log(f"surplus (degree-bound) checks all ok: {R['surplus_checks_all_ok']}")

json.dump(R, open(str(_REPO / "frontier/B973_L135_frame/weightfield_results.json"), "w"),
          indent=1, sort_keys=True, default=str)
log("DONE")
