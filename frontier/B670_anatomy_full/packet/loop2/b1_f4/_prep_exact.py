"""Dev-only helper: exec B575 prefix once, build v0 + N exactly, pickle the
results to _exact_cache.pkl so the mod-p linear-algebra logic (the expensive,
iterative part of b1_f4.py) can be developed/re-run without repaying the
~110s exact e6-build cost each time. Not one of the deliverables; the final
b1_f4.py re-derives everything from scratch per the task's SETUP clause."""
import os, sys, time, json, pickle
from fractions import Fraction as Fr

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}", flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = "<repo>/frontier/B575_bridge_obstruction/l51_obstruction.py"
W0A_JSON = "<seat-workdir>/invariant_line/w0a_singlet/w0a_v0.json"
A1_JSON = "<seat-workdir>/anatomy/loop1/a1_jordan/a1_results.json"
d = 27
gates = {}

log("STEP 0: exec B575 prefix (stages 0-3; exact e6 + 27 build)...")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
exec(compile(src[:cut], B575, "exec"), ns)
log(f"  B575 prefix done ({time.time()-t0:.0f}s)")

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27 = ns["A27"], ns["B27"]
mmul, meye, rref, nullspace = ns["mmul"], ns["meye"], ns["rref"], ns["nullspace"]
W27, E6_e, E6_f = ns["W27"], ns["E6_e"], ns["E6_f"]


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(d) if not v[k].is_zero()), K0)
            for i in range(d)]


def msub2(X, Y):
    return [[X[i][j] - Y[i][j] for j in range(d)] for i in range(d)]


log("STEP 1: v0 = joint nullspace of (A27-I, B27-I)  [W0a result]...")
I = meye(d)
AmI = msub2(A27, I)
BmI = msub2(B27, I)
ns_basis = nullspace(AmI + BmI)
gates["v0_dim1"] = (len(ns_basis) == 1)
log(f"  joint nullspace dim = {len(ns_basis)}  [HARD GATE dim=1]: "
    f"{'PASS' if gates['v0_dim1'] else 'FAIL'}")
assert gates["v0_dim1"]

v0_raw = ns_basis[0]
idx0 = next(i for i, x in enumerate(v0_raw) if not x.is_zero())
scale = v0_raw[idx0].inv()
v0 = [scale * x for x in v0_raw]
assert (v0[idx0] - K1).is_zero()
assert all(x.is_zero() for x in apply(AmI, v0))
assert all(x.is_zero() for x in apply(BmI, v0))
log(f"  v0 verified exactly; normalized idx0={idx0}")

w0a = json.load(open(W0A_JSON))
gates["v0_idx0_matches_w0a"] = (w0a["v0_normalized_idx0"] == idx0)
w0a_v0 = [K(Fr(a_s), Fr(b_s)) for a_s, b_s in w0a["v0_coordinates_full"]]
gates["v0_matches_w0a"] = all((v0[i] - w0a_v0[i]).is_zero() for i in range(d))
log(f"  cross-check vs w0a_v0.json: idx0 match={gates['v0_idx0_matches_w0a']}, "
    f"coordinates match={gates['v0_matches_w0a']}")
assert gates["v0_idx0_matches_w0a"] and gates["v0_matches_w0a"]

a1 = json.load(open(A1_JSON))
gates["v0_idx0_matches_a1_jordan"] = (a1["v0_normalized_idx0"] == idx0)
log(f"  cross-check vs loop1/a1_jordan/a1_results.json: idx0 match="
    f"{gates['v0_idx0_matches_a1_jordan']}")
assert gates["v0_idx0_matches_a1_jordan"]

log("STEP 2: the Jordan cubic invariant N (B632 cell2_texture.py method, "
    "verbatim per w1_portal.py STEP 3)...")
support, SUPIDX = [], {}
for p in range(d):
    for q in range(p, d):
        for r in range(q, d):
            if all(W27[p][k] + W27[q][k] + W27[r][k] == 0 for k in range(6)):
                SUPIDX[(p, q, r)] = len(support)
                support.append((p, q, r))
nsup = len(support)
log(f"  zero-weight-sum sorted triples: {nsup}")

eqs = {}
for gi, X in enumerate(list(E6_e) + list(E6_f)):
    xent = [(s, t) for s in range(d) for t in range(d) if not X[s][t].is_zero()]
    for (a, b, c) in support:
        k = SUPIDX[(a, b, c)]
        for (u, v, w) in ((a, b, c), (b, a, c), (c, a, b)):
            for s, t in xent:
                if s == u:
                    key = (gi,) + tuple(sorted((t, v, w)))
                    row = eqs.setdefault(key, {})
                    row[k] = row.get(k, K0) + X[u][t]
rows = [[row.get(k, K0) for k in range(nsup)] for row in eqs.values()
        if any(not cv.is_zero() for cv in row.values())]
log(f"  invariance equations: {len(rows)}")
sol = nullspace(rows)
gates["N_dim1"] = (len(sol) == 1)
log(f"  cubic invariant space dim = {len(sol)}  [GATE: must equal 1]: "
    f"{'PASS' if gates['N_dim1'] else 'FAIL'}")
assert gates["N_dim1"]
Cvals = sol[0]
CFULL = {}
for (p, q, r), k in SUPIDX.items():
    if not Cvals[k].is_zero():
        for perm in {(p, q, r), (p, r, q), (q, p, r), (q, r, p), (r, p, q), (r, q, p)}:
            CFULL[perm] = Cvals[k]
log(f"  nonzero sorted coefficients: {sum(1 for k in range(nsup) if not Cvals[k].is_zero())}/{nsup}")
log(f"  CFULL (full, all orderings) size: {len(CFULL)}")


def dot(f, v):
    return sum((f[t] * v[t] for t in range(d) if not v[t].is_zero()), K0)


def C3(u, v):
    cov = [K0] * d
    for (p, q, r), cval in CFULL.items():
        if not u[p].is_zero() and not v[q].is_zero():
            cov[r] = cov[r] + cval * u[p] * v[q]
    return cov


u1 = [K(i % 5 - 2) for i in range(d)]
v1 = [K((2 * i) % 7 - 3) for i in range(d)]
w1 = [K((3 * i) % 4 - 1) for i in range(d)]
ninv = {}
for nm, M in (("A27", A27), ("B27", B27)):
    lhs = dot(C3(apply(M, u1), apply(M, v1)), apply(M, w1))
    rhs = dot(C3(u1, v1), w1)
    ninv[nm] = (lhs - rhs).is_zero()
    log(f"  N-invariance under {nm}: {'PASS' if ninv[nm] else 'FAIL'}")
gates["N_invariant_all"] = all(ninv.values())
assert gates["N_invariant_all"]

# serialize: K-elements -> (str(a.numerator),str(a.denominator),str(b.numerator),str(b.denominator))
def kser(x):
    return [str(x.a.numerator), str(x.a.denominator), str(x.b.numerator), str(x.b.denominator)]


cache = {
    "gates": gates,
    "idx0": idx0,
    "v0": [kser(x) for x in v0],
    "A27": [[kser(A27[i][j]) for j in range(d)] for i in range(d)],
    "B27": [[kser(B27[i][j]) for j in range(d)] for i in range(d)],
    "CFULL": {f"{p},{q},{r}": kser(cval) for (p, q, r), cval in CFULL.items()},
    "nsup": nsup,
}
with open(os.path.join(HERE, "_exact_cache.pkl"), "wb") as f:
    pickle.dump(cache, f)
log(f"cached exact A27,B27,v0,CFULL -> {os.path.join(HERE, '_exact_cache.pkl')}")
log("DONE.")
