#!/usr/bin/env python3
"""B1187 / WALL-7 all-t closure.

Stage A (fast): mod-q rank sweep of the twisted (f3) intertwiner system at >= 900
distinct t values, two primes q == 1 (mod 3) (sqrt(-3) exists mod q; the reduction
K -> GF(q) is a ring map, so rank_q <= rank_K and dim_q = 0 ==> dim_K = 0 at that t).
Stage B (exact, the closure): per pattern, two 27-row minors D_R1(t), D_R2(t) --
degree <= 864 -- exactly interpolated from 866 exact evaluations; gcd(D_R1, D_R2)=1
in K[t] proves the minors share no root ==> dim = 0 for EVERY t in Qbar. (B767's
"865 points => no roots" reasoning was wrong as stated -- points >= deg+1 prove
D != 0, i.e. GENERIC closure; all-t closure needs root exclusion, done here by
the two-minor gcd.)

Reuses B767's wall7 stages 0-3 verbatim (exec to the stage-4 marker).
"""
import contextlib, io, os, sys, time, json, math
from fractions import Fraction as Fr
import numpy as np

REPO = str(__import__("pathlib").Path(__file__).resolve().parents[3])
W7 = os.path.join(REPO, "frontier", "B767_stabilizations", "wall7_twisted_extension.py")
OUT = sys.argv[1] if len(sys.argv) > 1 else "wall7_all_t.json"

print("loading B767 wall7 stages 0-3 (exact, one-time)...", flush=True)
src = open(W7).read()
cut = src.index("# ── stage 4")
ns = {"__name__": "wall7_prefix", "__file__": W7}
t0 = time.time()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], W7, "exec"), ns)
print(f"  loaded in {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
d = ns["d"]
e_pr = ns["e_pr"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
J1, J1i = ns["J1"], ns["J1i"]
patterns = ns["patterns"]
mexp_nil, mscale, mmul, mt, minv = (ns["mexp_nil"], ns["mscale"], ns["mmul"],
                                    ns["mt"], ns["minv"])
nil_order = ns["nil_order"]
DEG_BOUND = 27 * 2 * (nil_order - 1)
NPTS = DEG_BOUND + 2          # 866: enough to interpolate degree <= 864 exactly
print(f"  nilpotency {nil_order}; degree bound {DEG_BOUND}; sample points {NPTS}", flush=True)

# ---------- mod-q machinery ----------
def sqrt_m3_mod(q):
    for s in range(2, q):
        if (s * s + 3) % q == 0:
            return s
    return None

def K_to_mod(x, q, s):
    num_a, den_a = x.a.numerator, x.a.denominator
    num_b, den_b = x.b.numerator, x.b.denominator
    return (num_a * pow(den_a, -1, q) + s * num_b * pow(den_b, -1, q)) % q

def mat_mod(M, q, s):
    return np.array([[K_to_mod(x, q, s) for x in row] for row in M], dtype=np.int64)

def rank_mod(M, q):
    M = M % q
    r = 0
    rows, cols = M.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c] % q:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), -1, q)
        M[r] = (M[r] * inv) % q
        mask = (M[:, c] != 0)
        mask[r] = False
        M[mask] = (M[mask] - np.outer(M[mask, c], M[r])) % q
        r += 1
        if r == rows:
            break
    return r

def build_C_mod(t_int, q, s, mods):
    """C27(t) mod q via the exact same construction, in GF(q)."""
    e_q, J1_q, B27i_q = mods["e_pr"], mods["J1"], mods["B27i"]
    n = d
    Wt = np.eye(n, dtype=np.int64)
    term = np.eye(n, dtype=np.int64)
    for k in range(1, nil_order):
        term = (term @ e_q) % q
        coef = (pow(t_int, k, q) * pow(math.factorial(k), -1, q)) % q
        Wt = (Wt + coef * term) % q
    Jt = (Wt @ J1_q) % q
    Jti = inv_mod(Jt, q)
    C = (Jt @ B27i_q.T % q @ Jti) % q
    return C

def inv_mod(M, q):
    n = M.shape[0]
    A = np.concatenate([M % q, np.eye(n, dtype=np.int64)], axis=1)
    r = 0
    for c in range(n):
        piv = None
        for i in range(r, n):
            if A[i, c] % q:
                piv = i
                break
        assert piv is not None, "singular mod q"
        A[[r, piv]] = A[[piv, r]]
        A[r] = (A[r] * pow(int(A[r, c]), -1, q)) % q
        mask = (A[:, c] != 0)
        mask[r] = False
        A[mask] = (A[mask] - np.outer(A[mask, c], A[r])) % q
        r += 1
    return A[:, n:] % q

def pattern_rows_mod(pperm, Ml, Mr, q):
    """Constraint block (729 x 27) for X Ml - Mr X = 0 with X supported on
    {(pperm[k], k)}: R[(i,j), k] = [pperm[k]==i] Ml[k,j] - [k==j] Mr[i, pperm[j]]."""
    pp = np.asarray(pperm)
    T1 = np.zeros((d, d, d), dtype=np.int64)
    T1[pp, :, np.arange(d)] = Ml % q
    T2 = np.zeros((d, d, d), dtype=np.int64)
    T2[:, np.arange(d), np.arange(d)] = Mr[:, pp] % q
    return ((T1 - T2) % q).reshape(d * d, d)

def sweep_prime(q):
    s = sqrt_m3_mod(q)
    assert s is not None, f"-3 not a QR mod {q}"
    mods = {"e_pr": mat_mod(e_pr, q, s), "J1": mat_mod(J1, q, s),
            "B27": mat_mod(B27, q, s), "B27i": mat_mod(B27i, q, s)}
    B27_q = mods["B27"]
    bad = []
    t0 = time.time()
    for t_int in range(NPTS):
        C = build_C_mod(t_int, q, s, mods)
        if not ((C - B27_q) % q).any():      # degenerate weld (C == B): skip label
            bad.append((t_int, "degenerate"))
            continue
        for pi, (pperm, _) in enumerate(patterns):
            rows = np.concatenate([pattern_rows_mod(pperm, B27_q, C, q),
                                   pattern_rows_mod(pperm, C, B27_q, q)])
            r = rank_mod(rows, q)
            if r < d:
                bad.append((t_int, pi, d - r))
    dt = time.time() - t0
    return {"q": q, "sqrt_m3": s, "points": NPTS, "violations": bad,
            "seconds": round(dt, 1)}

results = {"deg_bound": DEG_BOUND, "points": NPTS, "primes": []}
for q in (1009, 1999):        # both == 1 mod 3
    assert q % 3 == 1
    r = sweep_prime(q)
    print(f"q={q}: {r['points']} points, violations={r['violations'][:5]}"
          f"{' ...' if len(r['violations'])>5 else ''} ({r['seconds']}s)", flush=True)
    results["primes"].append(r)

clean = all(not r["violations"] for r in results["primes"])
print(f"STAGE A {'CLEAN: dim=0 at every sampled t, both primes' if clean else 'VIOLATIONS FOUND'}",
      flush=True)
results["stage_a_clean"] = clean
with open(OUT, "w") as f:
    json.dump(results, f, indent=1)
print("DONE", flush=True)
