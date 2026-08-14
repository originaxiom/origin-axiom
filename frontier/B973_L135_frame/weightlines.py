#!/usr/bin/env python3
"""B973 / L135 -- THE WEIGHT-LINE DECOMPOSITION OF M12.

The B973 scout named this as the one presence-side object that is
RECONSTRUCTIBLE from the rebuilt frame but had NOT been run:

    "The weight-line decomposition of M12 -- the twelve multiplicity-one charge
     weights, needed for the W_frame-orbit and orbit<->generation claims.
     Reconstructible ... but not run here."   (SCOUT.md:344-347)

rebuild.py has now validated the frame / floor / M12 chain (51/51 against banked
numbers, two fresh primes). This file runs the decomposition on top of it.

REPRESENTATION (house rule 3): all four charges are ADJOINT-sector elements of
e6; "weights" below are the eigenvalues of ad(g_i) acting on M12 subset e6. No
27 VEV appears. Nothing here reduces rank.

TIER: mod p, two primes. Bound direction: mod-p nullity >= char-0 nullity. So
every dimension below certifies char-0 <= the stated value; agreement across two
primes is evidence, not a char-0 certificate. NOT a banking.
"""
import sys, json, time, random
sys.path.insert(0, str(_REPO / "frontier/B961_frame_instrument"))
import sympy as sp
import frame
import pathlib as _pl
_REPO = _pl.Path(__file__).resolve().parents[2]

T0 = time.time()
def log(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)

DIM, N = frame.DIM, frame.N
BB = frame.BB
INV = frame._G["INV"]
NS = [8, 14, 16, 22]
CH = {n: INV[n] for n in NS}
R = {}

AD = {n: frame.ad(CH[n]) for n in NS}
core = AD[8].nullspace(); Bc = sp.Matrix.hstack(*core); cdim = Bc.shape[1]
P = (Bc.T * Bc).inv() * Bc.T
C14 = P * AD[14] * Bc
fl = C14.nullspace(); Bf = Bc * sp.Matrix.hstack(*fl); fdim = Bf.shape[1]
floor = [[Bf[i, j] for i in range(DIM)] for j in range(fdim)]
# su(3)_colour := derived(floor).  NOT the standard A2 Levi -- see SCOUT.md:325-332:
# the two agree in centralizer DIMENSION but are different subalgebras of e6, and
# any test finer than a dimension must use derived(floor).
su3 = frame.derived([[sp.Rational(x) for x in v] for v in floor])
log(f"floor dim {fdim}; su(3)_colour := derived(floor), dim {int(frame.dim_of(su3))}")

K = [[0] * DIM for _ in range(DIM)]
SP = [[(q, kk, BB[i][q][kk]) for q in range(DIM) for kk in range(DIM) if BB[i][q][kk]]
      for i in range(DIM)]
for i in range(DIM):
    for j in range(i, DIM):
        t = 0
        for (q, kk, c) in SP[i]:
            d = BB[j][kk][q]
            if d: t += c * d
        assert getattr(t, "denominator", 1) == 1
        K[i][j] = int(t); K[j][i] = int(t)

# kappa, needed for the compact walls -- recomputed here exactly (same as rebuild.py)
piv = list(sp.Matrix(sp.Matrix.hstack(*fl).T).rref()[1])
comp = [i for i in range(cdim) if i not in piv][: cdim - fdim]
Tm = sp.Matrix.hstack(sp.Matrix.hstack(*fl), sp.eye(cdim)[:, comp]); Ti = Tm.inv()
C22 = P * AD[22] * Bc
M14 = Ti * C14 * Tm; M22 = Ti * C22 * Tm
Q14 = M14[fdim:, fdim:]; Q22 = M22[fdim:, fdim:]
s = sp.symbols('s')
def detat(x): return (Q14 + sp.Rational(x) * Q22).det()
qd = Q14.shape[0]
nu = sp.expand(sp.interpolate(list(zip(range(qd + 1), [detat(x) for x in range(qd + 1)])), s))
kap = [sp.Poly(sp.primitive(f_)[1], s) for f_, m_ in sp.factor_list(sp.Poly(nu, s))[1]
       if m_ == 6 and sp.degree(f_, s) == 3][0]
kco = [int(kap.as_expr().coeff(s, i)) for i in range(4)]
assert kco == [-6859, -56402640, 3033676800, 2771822592000], "kappa drifted"
log(f"kappa reproduced: {kco}")

# ---------------------------------------------------------------------------
# PRIME CRITERION, STATED BEFORE ANY RESULT IS SEEN (not tuned afterwards):
#   p is admissible iff  (a) p clears the charge denominators and kappa's lead,
#                        (b) kappa splits completely mod p  (the three compact
#                            walls must be visible at all), and
#                        (c) all four ad(g_i)|M12 split over F_p (the weight
#                            lines must EXIST over F_p to be decomposed).
# (c) is a genuine requirement of the method, not a filter on the answer: an
# eigenline cannot be exhibited over a field in which its eigenvalue does not
# live. The scan below reports how many primes in the window satisfy (c) and
# how many fail it -- the failure rate is itself the datum that the M12 charge
# weights are NOT rational. First run used p=41131 (passes) and p=41201 (fails
# (c) on a 2-dim piece of ad(g14)); both are reported.
# ---------------------------------------------------------------------------
R["prime_criterion"] = ("denominators clear; kappa splits; all four ad(g_i)|M12 "
                        "split over F_p")


def run(p, probe_only=False):
    r = {}
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
    def rank(vs): return 0 if not vs else rref([list(x) for x in zip(*vs)])[2]
    def null(rows, n=None):
        n = n if n is not None else (len(rows[0]) if rows else DIM)
        rr, wh, _ = rref(rows)
        out = []
        for fc in [c for c in range(n) if c not in wh]:
            v = [0] * n; v[fc] = 1
            for c, rw in wh.items(): v[c] = (-rr[rw][fc]) % p
            out.append(v)
        return out

    ADp = {n: mp(AD[n]) for n in NS}
    Kp = [[K[i][j] % p for j in range(DIM)] for i in range(DIM)]
    su3p = [[rd(sp.Rational(x)) for x in v] for v in su3]
    corep = [[rd(Bc[i, j]) for i in range(DIM)] for j in range(cdim)]

    kr = sorted(x for x in range(p) if sum(c * pow(x, i, p) for i, c in enumerate(kco)) % p == 0)
    W = [null([[(ADp[14][i][j] + r0 * ADp[22][i][j]) % p for j in range(DIM)]
               for i in range(DIM)]) for r0 in kr]
    M12 = null([[sum(v[i] * Kp[i][j] for i in range(DIM) if v[i]) % p for j in range(DIM)]
                for v in W[0] + W[1] + W[2]])
    m = len(M12)
    r["M12_dim"] = m
    assert m == 12, f"M12 dim {m} != 12 -- rebuild invariant broken"

    # ---- restrict the four ad(g_i) to M12 --------------------------------------
    Bm = [list(x) for x in zip(*M12)]
    def restrict_full(A):
        img = [[sum(A[i][kk] * v[kk] for kk in range(DIM) if v[kk]) % p for i in range(DIM)]
               for v in M12]
        aug = [[Bm[i][j] for j in range(m)] + [img[t][i] for t in range(m)] for i in range(DIM)]
        rr2, wh2, rk2 = rref(aug)
        assert rk2 == m, "M12 not invariant"
        return [[rr2[wh2[c]][m + t] for t in range(m)] for c in range(m)]
    X = {n: restrict_full(ADp[n]) for n in NS}

    def mul(A, B, k):
        return [[sum(A[i][t] * B[t][j] for t in range(k)) % p for j in range(k)]
                for i in range(k)]
    r["ops_commute_on_M12"] = all(
        mul(X[a], X[b], m) == mul(X[b], X[a], m) for a in NS for b in NS)

    # ---- simultaneous eigen-splitting -----------------------------------------
    def sub_restrict(A, S):
        """A restricted to the invariant subspace spanned by S (list of m-vectors)."""
        k = len(S)
        Bs = [[S[j][i] for j in range(k)] for i in range(m)]
        img = [[sum(A[i][t] * v[t] for t in range(m)) % p for i in range(m)] for v in S]
        aug = [[Bs[i][j] for j in range(k)] + [img[t][i] for t in range(k)] for i in range(m)]
        rr2, wh2, rk2 = rref(aug)
        if rk2 != k: return None                      # not invariant
        return [[rr2[wh2[c]][k + t] for t in range(k)] for c in range(k)]

    def charpoly_roots(A, k):
        """det(A - x I): degree k STRUCTURALLY. k+1 nodes + 4 surplus checks."""
        def dv(x0):
            M = [[(A[i][j] - (x0 if i == j else 0)) % p for j in range(k)] for i in range(k)]
            d = 1
            for c in range(k):
                pv = next((i for i in range(c, k) if M[i][c]), None)
                if pv is None: return 0
                if pv != c: M[c], M[pv] = M[pv], M[c]; d = (-d) % p
                d = d * M[c][c] % p; iv = pow(M[c][c], p - 2, p)
                M[c] = [v * iv % p for v in M[c]]
                for i in range(c + 1, k):
                    if M[i][c]:
                        f = M[i][c]; M[i] = [(a - f * b) % p for a, b in zip(M[i], M[c])]
            return d % p
        xs = list(range(k + 1)); ys = [dv(x) for x in xs]
        co = [0] * (k + 1)
        for i in range(k + 1):
            num = [1]; den = 1
            for j in range(k + 1):
                if j == i: continue
                num = [((([0] + num)[t] if t < len(num) + 1 else 0)
                        + (-xs[j]) % p * ((num + [0])[t])) % p for t in range(len(num) + 1)]
                den = den * (xs[i] - xs[j]) % p
            di = pow(den % p, p - 2, p)
            for t in range(len(num)): co[t] = (co[t] + ys[i] * di % p * num[t]) % p
        surplus = all(sum(c * pow(x0 % p, t, p) for t, c in enumerate(co)) % p == dv(x0 % p)
                      for x0 in range(-4, 0))
        rts = [x for x in range(p) if sum(c * pow(x, t, p) for t, c in enumerate(co)) % p == 0]
        return rts, surplus

    pieces = [[[1 if i == j else 0 for i in range(m)] for j in range(m)]]   # start: all of M12
    surplus_all = True
    split_total = {}
    for n in NS:
        newp = []
        eigs = set()
        for S in pieces:
            A = sub_restrict(X[n], S)
            assert A is not None, "piece not invariant under a commuting operator"
            k = len(S)
            rts, sur = charpoly_roots(A, k)
            surplus_all = surplus_all and sur
            got = 0
            for lam in rts:
                ker = null([[(A[i][j] - (lam if i == j else 0)) % p for j in range(k)]
                            for i in range(k)], n=k)
                if not ker: continue
                lifted = [[sum(cf[t] * S[t][i] for t in range(k)) % p for i in range(m)]
                          for cf in ker]
                newp.append(lifted); got += len(ker)
                eigs.add(lam)
            if got != k:
                # criterion (c) fails: ad(g_n) has an eigenvalue outside F_p.
                r["splits_over_Fp"] = False
                r["split_failure"] = {"charge": f"g{n}", "piece_dim": k,
                                      "F_p_eigenvalues_found": got,
                                      "residual_degree": k - got}
                return r
        pieces = newp
        split_total[n] = sorted(eigs)
    r["splits_over_Fp"] = True
    if probe_only:
        return r
    r["charpoly_surplus_checks"] = surplus_all
    r["n_common_eigenspaces"] = len(pieces)
    r["all_lines_are_1_dim"] = all(len(S) == 1 for S in pieces)
    r["distinct_eigenvalues_per_charge"] = {f"g{n}": len(split_total[n]) for n in NS}
    log(f"    common eigenspaces: {len(pieces)}; all 1-dim: {r['all_lines_are_1_dim']}; "
        f"distinct eigenvalues per charge {r['distinct_eigenvalues_per_charge']}")

    # ---- the twelve weight tuples ---------------------------------------------
    def weight_of(v):
        w = []
        for n in NS:
            img = [sum(X[n][i][t] * v[t] for t in range(m)) % p for i in range(m)]
            j = next(i for i in range(m) if v[i])
            lam = img[j] * pow(v[j], p - 2, p) % p
            assert all((img[i] - lam * v[i]) % p == 0 for i in range(m)), "not an eigenvector"
            w.append(lam)
        return tuple(w)
    lines = [S[0] for S in pieces]
    Wt = [weight_of(v) for v in lines]
    r["weights"] = [list(w) for w in Wt]
    r["weights_distinct"] = len(set(Wt)) == len(Wt)
    r["multiplicity_one"] = r["weights_distinct"] and len(Wt) == 12
    log(f"    12 weights distinct (multiplicity one): {r['multiplicity_one']}")

    # ---- W_frame closure: the sign-flip Klein group on the frame coordinates ---
    # (B939 assembly.py:349-353 realizes W_frame inside Aut(e6) as
    #  {identity, compact-flip, noncompact-flip, all-flip}; here we test its
    #  induced action on the M12 weight set.)
    S_ = set(Wt)
    def act(sig, w): return tuple((sig[i] * w[i]) % p for i in range(4))
    KLEIN = {"id": (1, 1, 1, 1), "compact_flip": (1, -1, 1, -1),
             "noncompact_flip": (-1, 1, -1, 1), "all_flip": (-1, -1, -1, -1)}
    r["closed_under_W_frame"] = {k: all(act(v, w) in S_ for w in Wt) for k, v in KLEIN.items()}
    # NON-VACUITY CONTROLS: sign patterns NOT in W_frame must NOT preserve the set.
    NOTW = {"lone_g14": (1, -1, 1, 1), "lone_g8": (-1, 1, 1, 1),
            "mixed_g8_g14": (-1, -1, 1, 1), "lone_g16": (1, 1, -1, 1)}
    r["control_not_closed_under_non_W_frame"] = {
        k: all(act(v, w) in S_ for w in Wt) for k, v in NOTW.items()}
    # orbits
    seen, orbits = set(), []
    for w in Wt:
        if w in seen: continue
        o = {act(v, w) for v in KLEIN.values()}
        orbits.append(sorted(o)); seen |= o
    r["n_orbits"] = len(orbits)
    r["orbit_sizes"] = sorted(len(o) for o in orbits)
    r["orbits_are_free"] = all(len(o) == 4 for o in orbits)
    log(f"    W_frame closure {r['closed_under_W_frame']}")
    log(f"    CONTROL non-W_frame flips (must all be False) "
        f"{r['control_not_closed_under_non_W_frame']}")
    log(f"    orbits: {r['n_orbits']} of sizes {r['orbit_sizes']}; free {r['orbits_are_free']}")

    # ---- orbit <-> generation (mu-wall) correspondence ------------------------
    # a weight line sits at wall rho iff lam8 + rho*lam16 = 0, i.e. rho = -lam8/lam16.
    ratios = []
    for w in Wt:
        assert w[2] != 0, "lam16 = 0 on a weight line -- ratio undefined"
        ratios.append((-w[0]) * pow(w[2], p - 2, p) % p)
    r["distinct_ratios"] = sorted(set(ratios))
    mu_solo = [2197, -4769856, -2075673600, 500716339200]
    r["mu_roots_cited"] = sorted(x for x in range(p)
                                 if sum(c * pow(x, t, p) for t, c in enumerate(mu_solo)) % p == 0)
    r["ratios_are_the_mu_walls"] = (r["distinct_ratios"] == r["mu_roots_cited"])
    buckets = {}
    for w, rt in zip(Wt, ratios): buckets.setdefault(rt, set()).add(w)
    r["lines_per_wall"] = sorted(len(v) for v in buckets.values())
    orbset = [set(o) for o in orbits]
    r["each_wall_is_exactly_one_orbit"] = all(v in orbset for v in buckets.values())
    r["wall_orbit_bijection"] = (r["lines_per_wall"] == [4, 4, 4]
                                 and r["each_wall_is_exactly_one_orbit"]
                                 and len(buckets) == len(orbits) == 3)
    log(f"    ratios = mu-walls: {r['ratios_are_the_mu_walls']}; lines/wall "
        f"{r['lines_per_wall']}; each wall = one orbit: "
        f"{r['each_wall_is_exactly_one_orbit']}")

    # ---- colour-blindness: su(3)_colour = derived(floor) acts as 0 on M12 -----
    imgs = []
    for g in su3p:
        Ag = [[0] * DIM for _ in range(DIM)]
        for pp in range(DIM):
            if not g[pp]: continue
            for qq in range(DIM):
                for kk, cv in enumerate(BB[pp][qq]):
                    if cv:
                        Ag[kk][qq] = (Ag[kk][qq] + g[pp] * (int(cv) % p)) % p
        for v in M12:
            imgs.append([sum(Ag[i][t] * v[t] for t in range(DIM) if v[t]) % p
                         for i in range(DIM)])
    r["rank_su3_on_M12"] = rank(imgs)
    # CONTROLS: the same routine is NOT the zero map on other targets
    ctl = []
    for g in su3p:
        Ag = [[0] * DIM for _ in range(DIM)]
        for pp in range(DIM):
            if not g[pp]: continue
            for qq in range(DIM):
                for kk, cv in enumerate(BB[pp][qq]):
                    if cv: Ag[kk][qq] = (Ag[kk][qq] + g[pp] * (int(cv) % p)) % p
        for v in corep:
            ctl.append([sum(Ag[i][t] * v[t] for t in range(DIM) if v[t]) % p
                        for i in range(DIM)])
    r["control_rank_su3_on_core"] = rank(ctl)
    tor_img = []
    for n in NS:
        for v in M12:
            tor_img.append([sum(ADp[n][i][t] * v[t] for t in range(DIM) if v[t]) % p
                            for i in range(DIM)])
    r["control_rank_torus_on_M12"] = rank(tor_img)
    log(f"    su(3)_colour on M12: rank {r['rank_su3_on_M12']}  "
        f"(CONTROLS: on core {r['control_rank_su3_on_core']}, torus on M12 "
        f"{r['control_rank_torus_on_M12']})")
    return r


# ---- scan the window, report the density, then run at the first two admissible
denoms = {c.denominator for n in NS for c in CH[n] if c}
USED = {40009, 40013, 40037, 40039, 40063, 40123, 40639, 40829, 40883}
cands, q = [], 41000
while len(cands) < 10:
    q = int(sp.nextprime(q))
    if q in USED or any(d % q == 0 for d in denoms) or kco[3] % q == 0:
        continue
    if len({x for x in range(q) if sum(c * pow(x, i, q) for i, c in enumerate(kco)) % q == 0}) == 3:
        cands.append(q)
log(f"kappa-split candidate primes in the window: {cands}")
scan = []
for q in cands:
    pr = run(q, probe_only=True)
    scan.append({"p": q, "splits": pr["splits_over_Fp"],
                 "failure": pr.get("split_failure")})
    log(f"  p={q}: weights split over F_p = {pr['splits_over_Fp']}"
        + (f"  ({pr['split_failure']})" if not pr["splits_over_Fp"] else ""))
R["prime_scan"] = scan
R["n_candidates"] = len(cands)
R["n_admissible"] = sum(1 for x in scan if x["splits"])
PRIMES = [x["p"] for x in scan if x["splits"]][:2]
R["primes"] = PRIMES
log(f"admissible: {R['n_admissible']}/{R['n_candidates']}; running the suite at {PRIMES}")
assert len(PRIMES) == 2, "fewer than two admissible primes in the window"

for p in PRIMES:
    log(f"--- p = {p} ---")
    R[f"p{p}"] = run(p)

# ---------------- cross-prime agreement on the PRIME-INDEPENDENT facts ---------
a, b = (R[f"p{PRIMES[0]}"], R[f"p{PRIMES[1]}"])
KEYS = ["M12_dim", "ops_commute_on_M12", "n_common_eigenspaces", "all_lines_are_1_dim",
        "multiplicity_one", "closed_under_W_frame", "control_not_closed_under_non_W_frame",
        "n_orbits", "orbit_sizes", "orbits_are_free", "ratios_are_the_mu_walls",
        "lines_per_wall", "each_wall_is_exactly_one_orbit", "wall_orbit_bijection",
        "rank_su3_on_M12", "distinct_eigenvalues_per_charge", "charpoly_surplus_checks"]
R["cross_prime_agreement"] = {k: (a[k] == b[k]) for k in KEYS}
R["cross_prime_all_agree"] = all(R["cross_prime_agreement"].values())
log(f"cross-prime agreement on prime-independent facts: {R['cross_prime_all_agree']}")

VER = []
def v(name, got, want):
    VER.append({"check": name, "got": got, "want": want, "pass": bool(got == want)})
    log(f"  [{'PASS' if got == want else 'FAIL'}] {name}: {got} (expect {want})")
for p in PRIMES:
    q = R[f"p{p}"]
    v(f"four ad(g_i) commute on M12 (p={p})", q["ops_commute_on_M12"], True)
    v(f"12 common eigenlines, all 1-dim (p={p})",
      [q["n_common_eigenspaces"], q["all_lines_are_1_dim"]], [12, True])
    v(f"weights multiplicity one (p={p})", q["multiplicity_one"], True)
    v(f"closed under all four W_frame elements (p={p})",
      sorted(q["closed_under_W_frame"].values()), [True] * 4)
    v(f"CONTROL: NOT closed under any non-W_frame flip (p={p})",
      sorted(set(q["control_not_closed_under_non_W_frame"].values())), [False])
    v(f"three free W_frame orbits of size 4 (p={p})",
      [q["n_orbits"], q["orbit_sizes"]], [3, [4, 4, 4]])
    v(f"orbit<->generation bijection (p={p})", q["wall_orbit_bijection"], True)
    v(f"ratios are the cited mu-walls (p={p})", q["ratios_are_the_mu_walls"], True)
    v(f"su(3)_colour acts as 0 on M12 (p={p})", q["rank_su3_on_M12"], 0)
    v(f"CONTROL su(3)_colour NOT zero on core (p={p})", q["control_rank_su3_on_core"] > 0, True)
    v(f"CONTROL torus rank 12 on M12 (p={p})", q["control_rank_torus_on_M12"], 12)
v("cross-prime agreement", R["cross_prime_all_agree"], True)
R["VERDICT"] = VER
R["ALL_PASS"] = all(x["pass"] for x in VER)
R["FAILURES"] = [x for x in VER if not x["pass"]]
log(f"weight-line suite: {sum(1 for x in VER if x['pass'])}/{len(VER)}; "
    f"ALL PASS = {R['ALL_PASS']}")

json.dump(R, open(str(_REPO / "frontier/B973_L135_frame/weightlines_results.json"), "w"),
          indent=1, sort_keys=True, default=str)
log("DONE")
