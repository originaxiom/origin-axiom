"""B666 CELL A' — phase 2: the H^2 class tables for the Lambda^2(27)=351
cup and the Sym^2 / 351' cups, by Fox-map membership.

Membership systems are 1404 x 1404 (Lambda) and 1512 x 1512 (Sym); the
DISCOVERY pass runs mod p (numpy, p = 1 mod 3, both sqrt(-3) embeddings
per prime); every banked verdict then gets an EXACT certificate over
K = Q(sqrt-3), CRT-reconstructed and verified in exact arithmetic:

  ZERO : an explicit Fox primitive a with  PHI a = E(c)     (exact)
  NONZ : an explicit left functional y with y PHI = 0, y E(c) != 0 (exact)

The mod-p pass is discovery only; no verdict banks without its exact
certificate.  RHS families also include the slot-symmetry differences
E(c_ij) - E(c_ji) (Lambda: Koszul-flip symmetry) and the slot-antisym
sums E(c_ij) + E(c_ji) (351').
"""
import os
import sys
import json
import time
from fractions import Fraction as Fr

import numpy as np
import sympy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from a2_common import load, log, kser   # noqa: E402

n = load(run_g0=False, need_bar=False)
K, K0, K1 = n.K, n.K0, n.K1
kde = n.kde
mat = n.mat
LT, LE = n.LT, n.LE

log("loading checkpoint (exact E vectors)...")
with open(os.path.join(HERE, "ckpt_phase1.json")) as fh:
    ck = json.load(fh)


def devec(v):
    return [kde(t) for t in v]


E_LAM = {tuple(map(int, k.split(","))): devec(v)
         for k, v in ck["E_LAM"].items()}
E_SYM = {tuple(map(int, k.split(","))): devec(v)
         for k, v in ck["E_SYM"].items()}
E_PW = {tuple(map(int, k.split(","))): devec(v)
        for k, v in ck["E_PW"].items()}
PAIRS = [(i, j) for i in range(5) for j in range(5)]
LTP = [(i, j) for i in range(5) for j in range(5) if i < j]

# RHS families (exact)
RHS = {}
RHS["lam"] = [(("pair",) + p, E_LAM[p]) for p in PAIRS]
RHS["lam"] += [(("symdiff",) + p,
                [E_LAM[p][t] - E_LAM[(p[1], p[0])][t]
                 for t in range(1404)]) for p in LTP]
RHS["sym"] = [(("pair",) + p, E_SYM[p]) for p in PAIRS]
RHS["pw"] = [(("pair",) + p, E_PW[p]) for p in PAIRS]
RHS["pw"] += [(("asymsum",) + p,
               [E_PW[p][t] + E_PW[(p[1], p[0])][t]
                for t in range(1512)]) for p in LTP]

# ---------------------------------------------------------------------------
# mod-p machinery
# ---------------------------------------------------------------------------
NLAM, NSYM = 1404, 1512


def gen_primes(count, start=(1 << 30) - 1):
    out = []
    p = start
    while len(out) < count:
        p = sympy.prevprime(p)
        if p % 3 == 1:
            out.append(int(p))
    return out


def kred(x, p, s):
    return (x.a.numerator * pow(x.a.denominator, p - 2, p)
            + s * (x.b.numerator % p)
            * pow(x.b.denominator, p - 2, p)) % p


def vred(v, p, s):
    return np.array([kred(x, p, s) for x in v], dtype=np.int64)


# distinct Fox words
WORDS = sorted({w for r in range(4) for g in "abcd"
                for (w, _s) in n.POSLIST[r][g]})
log(f"distinct Fox prefix words: {len(WORDS)}")
for w in WORDS:
    mat(w)          # exact cache fill

I0 = np.array([p for (p, q) in LT])
I1 = np.array([q for (p, q) in LT])
A0 = np.array([p for (p, q) in LE])
A1 = np.array([q for (p, q) in LE])
DIAGCOL = np.array([1 if p == q else 0 for (p, q) in LE])


def build_phis(p, s):
    """PHI_lam (1404^2) and PHI_sym (1512^2) mod p."""
    MW = {w: np.array([[kred(x, p, s) for x in row] for row in mat(w)],
                      dtype=np.int64) for w in WORDS}
    inv2 = pow(2, p - 2, p)
    PhiL = np.zeros((NLAM, NLAM), dtype=np.int64)
    PhiS = np.zeros((NSYM, NSYM), dtype=np.int64)
    for r in range(4):
        for gi, g in enumerate("abcd"):
            for (w, sgn) in n.POSLIST[r][g]:
                M = MW[w]
                CL = (M[np.ix_(I0, I0)] * M[np.ix_(I1, I1)]
                      - M[np.ix_(I0, I1)] * M[np.ix_(I1, I0)]) % p
                CS = (M[np.ix_(A0, A0)] * M[np.ix_(A1, A1)]
                      + M[np.ix_(A0, A1)] * M[np.ix_(A1, A0)]) % p
                CS[:, DIAGCOL == 1] = (CS[:, DIAGCOL == 1] * inv2) % p
                if sgn > 0:
                    PhiL[r * 351:(r + 1) * 351, gi * 351:(gi + 1) * 351] \
                        = (PhiL[r * 351:(r + 1) * 351,
                                gi * 351:(gi + 1) * 351] + CL) % p
                    PhiS[r * 378:(r + 1) * 378, gi * 378:(gi + 1) * 378] \
                        = (PhiS[r * 378:(r + 1) * 378,
                                gi * 378:(gi + 1) * 378] + CS) % p
                else:
                    PhiL[r * 351:(r + 1) * 351, gi * 351:(gi + 1) * 351] \
                        = (PhiL[r * 351:(r + 1) * 351,
                                gi * 351:(gi + 1) * 351] - CL) % p
                    PhiS[r * 378:(r + 1) * 378, gi * 378:(gi + 1) * 378] \
                        = (PhiS[r * 378:(r + 1) * 378,
                                gi * 378:(gi + 1) * 378] - CS) % p
    return PhiL % p, PhiS % p


def rref_aug(Phi, RHSm, p):
    """full rref of [Phi | RHS | I] with pivots restricted to Phi cols.
    Returns (R, piv)."""
    N = Phi.shape[0]
    A = np.concatenate([Phi % p, RHSm % p, np.eye(N, dtype=np.int64)],
                       axis=1)
    piv = []
    r = 0
    for c in range(N):
        nz = np.nonzero(A[r:, c])[0]
        if nz.size == 0:
            continue
        pr = r + int(nz[0])
        if pr != r:
            A[[r, pr]] = A[[pr, r]]
        iv = pow(int(A[r, c]), p - 2, p)
        A[r] = (A[r] * iv) % p
        rows = np.nonzero(A[:, c])[0]
        rows = rows[rows != r]
        if rows.size:
            A[rows] = (A[rows]
                       - np.outer(A[rows, c], A[r])) % p
        piv.append(c)
        r += 1
        if r == N:
            break
    return A, piv


def run_module(kind, Phi, rhs_keys, rhs_red, p):
    """one modular elimination for one module; returns the digest."""
    N = Phi.shape[0]
    nrhs = rhs_red.shape[1]
    R, piv = rref_aug(Phi, rhs_red, p)
    rank = len(piv)
    bottom = R[rank:, :]
    resid = bottom[:, N:N + nrhs]           # y_t . E_j  for all null rows
    consist = [bool(np.all(resid[:, j] == 0)) for j in range(nrhs)]
    sols = {}
    for j, key in enumerate(rhs_keys):
        if consist[j]:
            x = np.zeros(N, dtype=np.int64)
            for r_i, pc in enumerate(piv):
                x[pc] = R[r_i, N + j]
            sols[key] = x
    return {"rank": rank, "piv": tuple(piv), "consist": consist,
            "resid": resid, "nullrows": bottom[:, N + nrhs:],
            "sols": sols}


# ---------------------------------------------------------------------------
# CRT + rational reconstruction
# ---------------------------------------------------------------------------
def crt_pair(res_list, mod_list):
    x, m = 0, 1
    for r, p in zip(res_list, mod_list):
        # combine x mod m with r mod p (Python ints only: np.int64
        # residues silently overflow / raise once m exceeds 2^63)
        r, p = int(r), int(p)
        t = ((r - x) * pow(m % p, p - 2, p)) % p
        x = x + m * t
        m *= p
    return x % m, m


def wang(u, m):
    """rational reconstruction of u mod m; None if fails."""
    import math
    bound = math.isqrt(m // 2)
    a0, b0 = m, 0
    a1, b1 = u % m, 1
    while a1 > bound:
        q = a0 // a1
        a0, a1 = a1, a0 - q * a1
        b0, b1 = b1, b0 - q * b1
    if b1 == 0 or math.gcd(b1, m) != 1 or abs(b1) > bound:
        return None
    if b1 < 0:
        a1, b1 = -a1, -b1
    return Fr(a1, b1)


def reconstruct_K(res_plus, res_minus, primes, svals):
    """residues under both embeddings -> exact K element (or None)."""
    ra, rb = [], []
    for up, um, p, s in zip(res_plus, res_minus, primes, svals):
        up, um, p, s = int(up), int(um), int(p), int(s)
        inv2 = pow(2, p - 2, p)
        a = ((up + um) * inv2) % p
        b = ((up - um) * inv2 * pow(s, p - 2, p)) % p
        ra.append(a)
        rb.append(b)
    ua, m = crt_pair(ra, primes)
    ub, _ = crt_pair(rb, primes)
    fa = wang(ua, m)
    if fa is None:
        return None
    fb = wang(ub, m)
    if fb is None:
        return None
    return K(fa, fb)


def reconstruct_vec(vecs_plus, vecs_minus, primes, svals):
    N = len(vecs_plus[0])
    out = []
    for t in range(N):
        x = reconstruct_K([v[t] for v in vecs_plus],
                          [v[t] for v in vecs_minus], primes, svals)
        if x is None:
            return None
        out.append(x)
    return out


# ---------------------------------------------------------------------------
# the modular runs
# ---------------------------------------------------------------------------
MAXP = 24
ALLPRIMES = gen_primes(MAXP)
runs = {}          # (p, s) -> {kind: digest}
used_primes = []
svals_of = {}
YCOVER = {}        # kind -> list of (nullrow_index, [covered rhs indices])


def do_prime(p):
    s = int(sympy.ntheory.sqrt_mod(-3, p))
    for semb in (s, p - s):
        t0 = time.time()
        PhiL, PhiS = build_phis(p, semb)
        # gate: 3 exact columns vs the compound build
        rng = np.random.default_rng(p % 100000)
        for kind, Phi, npair in (("lam", PhiL, 351), ("sym", PhiS, 378)):
            for _ in range(3):
                gi = int(rng.integers(0, 4))
                m = int(rng.integers(0, npair))
                colx = n.fox_column(kind, "abcd"[gi], m)
                colr = vred(colx, p, semb)
                assert np.all(Phi[:, gi * npair + m] == colr), \
                    f"compound-vs-exact column gate FAILS ({kind})"
        dig = {}
        for kind, Phi in (("lam", PhiL), ("sym", PhiS)):
            fams = [kind] if kind == "lam" else ["sym", "pw"]
            keys, red = [], []
            for fam in fams:
                for key, vec in RHS[fam]:
                    keys.append((fam,) + key)
                    red.append(vred(vec, p, semb))
            red = np.stack(red, axis=1)
            d = run_module(kind, Phi, keys, red, p)
            if YCOVER:          # memory trim: keep only the cover rows
                d["nullrows"] = {t: d["nullrows"][t].copy()
                                 for (t, _c) in YCOVER[kind]}
                d["resid"] = None
            dig[kind] = d
        runs[(p, semb)] = dig
        log(f"  prime {p} emb {'+' if semb == s else '-'}: "
            f"rank(lam) = {dig['lam']['rank']}, "
            f"rank(sym) = {dig['sym']['rank']}  "
            f"({time.time()-t0:.0f}s)")
    used_primes.append(p)
    svals_of[p] = s


log("modular discovery (first 2 primes, both embeddings)...")
for p in ALLPRIMES[:2]:
    do_prime(p)

# agreement gates
for kind in ("lam", "sym"):
    pats = {(runs[k][kind]["piv"], tuple(runs[k][kind]["consist"]),
             runs[k][kind]["rank"]) for k in runs}
    assert len(pats) == 1, f"mod-p pattern disagreement [{kind}]"
first = runs[(used_primes[0], svals_of[used_primes[0]])]
KEYS = {}
CONS = {}
for kind in ("lam", "sym"):
    dig = first[kind]
    keys = []
    for fam in ([kind] if kind == "lam" else ["sym", "pw"]):
        for key, _ in RHS[fam]:
            keys.append((fam,) + key)
    KEYS[kind] = keys
    CONS[kind] = dict(zip(keys, dig["consist"]))
    nullity = (NLAM if kind == "lam" else NSYM) - dig["rank"]
    log(f"[{kind}] rank = {dig['rank']}, coker dim (H^2 of the "
        f"2-complex, discovery) = {nullity}")
    for fam in ([kind] if kind == "lam" else ["sym", "pw"]):
        log(f"  family [{fam}] class table "
            "(True = ZERO/coboundary, False = NONZ):")
        for i in range(5):
            row = []
            for j in range(5):
                row.append("ZERO " if CONS[kind][(fam, "pair", i, j)]
                           else "NONZ ")
            log("    " + " ".join(row))
        extra = [k for k in keys
                 if k[0] == fam and k[1] in ("symdiff", "asymsum")]
        if extra:
            log(f"  [{fam}] {extra[0][1]} verdicts: "
                + ", ".join(f"({k[2]},{k[3]})="
                            + ("ZERO" if CONS[kind][k] else "NONZ")
                            for k in extra))

# structural consistency gate: SYM zero <=> banked-27bar zero AND pw zero
BANKED27 = [[True, True, False, False, False],
            [True, True, False, False, False],
            [False, False, True, False, False],
            [False, False, False, True, False],
            [False, False, False, False, True]]
for (i, j) in PAIRS:
    lhs = CONS["sym"][("sym", "pair", i, j)]
    rhs = BANKED27[i][j] and CONS["sym"][("pw", "pair", i, j)]
    assert lhs == rhs, f"SYM = 27bar (+) 351' consistency FAILS at {(i,j)}"
log("gate PASS: [c_Sym] = 0 <=> banked 27bar ZERO and 351' ZERO "
    "(all 25 pairs)")

# ---------------------------------------------------------------------------
# choose NONZ certificates (y-cover) from the first run's null rows
# ---------------------------------------------------------------------------
for kind in ("lam", "sym"):
    dig = first[kind]
    keys = KEYS[kind]
    nonz = [j for j, k in enumerate(keys) if not dig["consist"][j]]
    resid = dig["resid"]
    chosen = []
    covered = set()
    while len(covered) < len(nonz):
        best, bestcov = None, set()
        for t in range(resid.shape[0]):
            cov = {j for j in nonz
                   if j not in covered and resid[t, j] != 0}
            if len(cov) > len(bestcov):
                best, bestcov = t, cov
        assert best is not None, \
            f"no null row detects some NONZ rhs [{kind}]"
        chosen.append((best, sorted(bestcov)))
        covered |= bestcov
    YCOVER[kind] = chosen
    log(f"[{kind}] NONZ certificate cover: "
        f"{len(chosen)} left-null functionals for {len(nonz)} NONZ rhs "
        f"(null rows {[t for t, _ in chosen]})")

# ---------------------------------------------------------------------------
# adaptive CRT reconstruction + exact verification
# ---------------------------------------------------------------------------


def gather(kind, what, idx):
    """residue vectors across runs: what in ('sol', 'null'); idx = key or
    null-row index.  Returns (plus_list, minus_list, primes, svals)."""
    vp, vm = [], []
    for p in used_primes:
        s = svals_of[p]
        dp = runs[(p, s)][kind]
        dm = runs[(p, p - s)][kind]
        if what == "sol":
            vp.append(dp["sols"][idx])
            vm.append(dm["sols"][idx])
        else:
            vp.append(dp["nullrows"][idx])
            vm.append(dm["nullrows"][idx])
    return vp, vm, used_primes[:], [svals_of[p] for p in used_primes]


def try_reconstruct(kind, what, idx):
    vp, vm, pr, sv = gather(kind, what, idx)
    return reconstruct_vec(vp, vm, pr, sv)


needed = []
for kind in ("lam", "sym"):
    for key, ok in CONS[kind].items():
        if ok:
            needed.append((kind, "sol", key))
    for (t, _cov) in YCOVER[kind]:
        needed.append((kind, "null", t))

recon = {}          # stabilized reconstructions
prev = {}
batch_targets = [3, 4, 6, 8, 12, 16, 20, MAXP]
for bt in batch_targets:
    if len(recon) == len(needed):
        break
    for p in ALLPRIMES[len(used_primes):bt]:
        do_prime(p)
    for kind in ("lam", "sym"):
        pats = {(runs[k][kind]["piv"], tuple(runs[k][kind]["consist"]))
                for k in runs}
        assert len(pats) == 1, "pattern disagreement at more primes"
    for item in needed:
        if item in recon:
            continue
        v = try_reconstruct(*item)
        if v is not None and prev.get(item) is not None \
                and len(v) == len(prev[item]) \
                and all((v[t] - prev[item][t]).is_zero()
                        for t in range(len(v))):
            recon[item] = v          # stable across two prime counts
        prev[item] = v
    log(f"reconstruction with {len(used_primes)} primes: "
        f"{len(recon)}/{len(needed)} stabilized")
still = [x for x in needed if x not in recon]
if still:
    log(f"WARNING: {len(still)} quantities not stabilized at "
        f"{MAXP} primes: {still}")

# ---------------------------------------------------------------------------
log("EXACT verification of the certificates (streaming Fox columns)...")
EX_RHS = {"lam": dict((("lam",) + k, v) for k, v in RHS["lam"]),
          "sym": dict([(("sym",) + k, v) for k, v in RHS["sym"]]
                      + [(("pw",) + k, v) for k, v in RHS["pw"]])}

verified = {}
for kind, N, npair in (("lam", NLAM, 351), ("sym", NSYM, 378)):
    ys = [(t, recon.get((kind, "null", t))) for (t, _c) in YCOVER[kind]]
    sols = [(key, recon.get((kind, "sol", key)))
            for key in CONS[kind] if CONS[kind][key]]
    ok_y = {t: [K0] * 0 for t, _ in ys}
    acc = {key: [K0] * N for key, a in sols if a is not None}
    ydots_ok = {t: True for t, y in ys if y is not None}
    t0 = time.time()
    for gi, g in enumerate("abcd"):
        for m in range(npair):
            col = n.fox_column(kind, g, m)
            cidx = gi * npair + m
            for t, y in ys:
                if y is None:
                    continue
                s = sum((y[r_] * col[r_] for r_ in range(N)
                         if not col[r_].is_zero()), K0)
                if not s.is_zero():
                    ydots_ok[t] = False
            for key, a in sols:
                if a is None:
                    continue
                c = a[cidx]
                if not c.is_zero():
                    av = acc[key]
                    for r_ in range(N):
                        if not col[r_].is_zero():
                            av[r_] = av[r_] + c * col[r_]
        log(f"  [{kind}] generator {g} columns done "
            f"({time.time()-t0:.0f}s)")
    # ZERO certificates
    for key, a in sols:
        if a is None:
            verified[(kind,) + key] = "UNCERTIFIED(reconstruction)"
            continue
        E = EX_RHS[kind][key]
        good = all((acc[key][r_] - E[r_]).is_zero() for r_ in range(N))
        verified[(kind,) + key] = ("ZERO-CERTIFIED" if good
                                   else "CERT-FAIL")
        assert good, f"ZERO certificate verification FAILS at {key}"
    # NONZ certificates
    yok = {}
    for t, y in ys:
        if y is None:
            yok[t] = False
            continue
        assert ydots_ok[t], f"y PHI != 0 for null row {t} [{kind}]"
        yok[t] = True
    for (t, cov) in YCOVER[kind]:
        for j in cov:
            key = KEYS[kind][j]
            if not yok[t]:
                verified[(kind,) + key] = "UNCERTIFIED(reconstruction)"
                continue
            y = recon[(kind, "null", t)]
            E = EX_RHS[kind][key]
            s = sum((y[r_] * E[r_] for r_ in range(N)
                     if not E[r_].is_zero()), K0)
            good = not s.is_zero()
            assert good, f"y . E = 0 exactly at {key} (mod-p lied?)"
            verified[(kind,) + key] = "NONZ-CERTIFIED"

log("verification complete; final certified tables:")
FINAL = {}
for kind in ("lam", "sym"):
    for key in KEYS[kind]:
        v = verified.get((kind,) + key, "MISSING")
        FINAL[str((kind,) + key)] = v
for fam, kind in (("lam", "lam"), ("sym", "sym"), ("pw", "sym")):
    log(f"  family [{fam}] CERTIFIED table:")
    for i in range(5):
        row = []
        for j in range(5):
            v = verified.get((kind, fam, "pair", i, j), "MISSING")
            row.append("ZERO " if v.startswith("ZERO")
                       else ("NONZ " if v.startswith("NONZ") else "???? "))
        log("    " + " ".join(row))
for kind, fam, tag in (("lam", "lam", "symdiff"), ("sym", "pw", "asymsum")):
    outs = []
    for (i, j) in LTP:
        v = verified.get((kind, fam, tag, i, j), "MISSING")
        outs.append(f"({i},{j})={v}")
    log(f"  [{fam}] {tag}: " + "; ".join(outs))

res = {
    "certified": FINAL,
    "ranks": {kind: first[kind]["rank"] for kind in ("lam", "sym")},
    "coker_dims_discovery": {"lam": NLAM - first["lam"]["rank"],
                             "sym": NSYM - first["sym"]["rank"]},
    "primes_used": used_primes,
    "ycover": {kind: [[t, [str(KEYS[kind][j]) for j in cov]]
                      for (t, cov) in YCOVER[kind]]
               for kind in ("lam", "sym")},
    "y_exact": {f"{kind}:{t}": [kser(x) for x in recon[(kind, 'null', t)]]
                for kind in ("lam", "sym")
                for (t, _c) in YCOVER[kind]
                if (kind, "null", t) in recon},
}
with open(os.path.join(HERE, "phase2_results.json"), "w") as fh:
    json.dump(res, fh)
log("phase2_results.json written")
log("PHASE 2 COMPLETE")
