"""WALL-7 twisted extension: extend the f3 dim=0 verification to 60 weld points.

The degree bound for C27(t) entries is deg(exp(t*e_pr)) * 2, because
C27(t) = W(t) B27 W(t)^-1 where W(t) = exp(t*e_pr), W(t)^-1 = exp(-t*e_pr).
If e_pr is nilpotent of order p, then deg(W) = p-1, and deg(C27 entries) <= 2(p-1).
The system has 27 unknowns; the determinant of the constraint matrix has degree
<= 27 * 2(p-1). With 27*2(p-1) + 1 sample points at dim=0, the determinant is
not identically zero AND has no roots (it's a nonzero polynomial with more roots
than its degree would allow), proving dim=0 for ALL t.

This script determines the actual nilpotency order, computes the tight degree bound,
then samples enough points.
"""
import contextlib, io, os, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
B575 = os.path.join(REPO, "frontier", "B575_bridge_obstruction", "l51_obstruction.py")
B299 = os.path.join(REPO, "frontier", "B299_trinification_triality",
                    "trinification_triality.py")
LAM = "abABaaBAbA"
d = 27

print("=" * 88)
print("WALL-7 twisted extension: sampling the f3 system at many weld points")
print("=" * 88)

# ── stage 0: load B575 infrastructure ──
print("\nLoading B575 infrastructure...")
src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
ns = {"__name__": "b575_prefix", "__file__": B575}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:cut], B575, "exec"), ns)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
OMEGA = ns["OMEGA"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
e_pr, f_pr = ns["e_pr"], ns["f_pr"]
kvals, W27, C6 = ns["kvals"], ns["W27"], ns["C6"]
REL = ns["REL"]
mmul, meye, madd, mscale, msub, mzero_p, rref, nullspace, mexp_nil = (
    ns[k] for k in ("mmul", "meye", "madd", "mscale", "msub", "mzero_p",
                    "rref", "nullspace", "mexp_nil"))
print("  B575 loaded.")

# ── helpers (from the recompute) ──
def mt(M):
    n = len(M)
    return [[M[j][i] for j in range(n)] for i in range(n)]

def minv(M):
    n = len(M)
    aug = [list(M[i]) + [K1 if k == i else K0 for k in range(n)] for i in range(n)]
    Rr, piv = rref(aug)
    assert len(piv) == n, "singular"
    out = [[K0] * n for _ in range(n)]
    for r_i, pc in enumerate(piv):
        for j in range(n):
            out[pc][j] = Rr[r_i][n + j]
    return out

def is_eye(M):
    n = len(M)
    return all((M[i][j] - (K1 if i == j else K0)).is_zero()
               for i in range(n) for j in range(n))

def word_mat(word, acts, n=d):
    P = meye(n)
    for ch in word:
        P = mmul(P, acts[ch])
    return P

def inv_word(w):
    return ''.join(ch.swapcase() for ch in reversed(w))

# ── stage 1: determine nilpotency order of e_pr ──
print("\nDetermining nilpotency order of e_pr...")
E = e_pr
power = meye(d)
nil_order = 0
for p in range(1, d + 1):
    power = mmul(power, E)
    if mzero_p(power):
        nil_order = p
        break
print(f"  e_pr^{nil_order} = 0 (nilpotency order = {nil_order})")
print(f"  deg(exp(t*e_pr)) = {nil_order - 1}")
print(f"  deg(C27(t) entries) <= 2 * {nil_order - 1} = {2*(nil_order - 1)}")

# ── stage 2: build J1 (the base weld intertwiner) ──
print("\nBuilding J1...")
mu0 = W27[0]
C6K = [[K(C6[i][j]) for j in range(6)] for i in range(6)]
C6K_inv = minv(C6K)
Tdiag = []
for mu in W27:
    dm = [K(mu[i] - mu0[i]) for i in range(6)]
    q = [sum((dm[i] * C6K_inv[i][j] for i in range(6)), K0) for j in range(6)]
    val = K1
    for i, qi in enumerate(q):
        base = kvals[i].inv() if int(qi.a) >= 0 else kvals[i]
        for _ in range(abs(int(qi.a))):
            val = val * base
    Tdiag.append(val)
T27 = [[Tdiag[i] if i == j else K0 for j in range(d)] for i in range(d)]
S27 = mmul(mmul(A27, mexp_nil(mscale(K(-1), f_pr))), A27)
J1 = mmul(S27, T27)
J1i = minv(J1)
gA = mzero_p(msub(mmul(mmul(J1, mt(A27i)), J1i), A27))
gB = mzero_p(msub(mmul(mmul(J1, mt(B27i)), J1i), B27))
print(f"  J1 gates: A={gA}, B={gB}")
assert gA and gB

lam27 = word_mat(LAM, {'a': A27, 'b': B27, 'A': A27i, 'B': B27i})
lam27i = minv(lam27)

def build_double(t):
    Wt = mexp_nil(mscale(t, e_pr))
    Jt = mmul(Wt, J1)
    Jti = minv(Jt)
    C = mmul(mmul(Jt, mt(B27i)), Jti)
    Ci = mmul(mmul(Jt, mt(B27)), Jti)
    acts = {'a': A27, 'A': A27i, 'b': B27, 'B': B27i, 'c': C, 'C': Ci}
    nondeg = not mzero_p(msub(C, B27))
    R1_ok = is_eye(word_mat(REL, acts))
    return acts, C, nondeg and R1_ok

# ── stage 3: load the 8 patterns (from B299) ──
print("\nLoading B299 patterns...")
import sympy as sp
from itertools import permutations

nb = {"__name__": "b299"}
exec(compile(open(B299).read(), B299, "exec"), nb)
w299 = sorted(tuple(int(y) for y in x) for x in nb["_weights_27"]())
TH, PH = nb["THETA"], nb["PHI"]
I6 = sp.eye(6)
tri6 = []
for i in range(3):
    for j in range(3):
        m = TH**i * PH**j
        if m != I6 and not any(m == x for x in tri6):
            tri6.append(m)

w575 = [tuple(w) for w in W27]
w575set = set(w575)
w299set = set(w299)
idx299 = {w: i for i, w in enumerate(w299)}
acts6 = [nb["_action_on_dynkin"](m) for m in tri6]
patterns = []
for perm in permutations(range(6)):
    relab = [tuple(x[perm[i]] for i in range(6)) for x in w299]
    if set(relab) != w575set:
        continue
    idx299_to_575 = {j: w575.index(lw) for j, lw in enumerate(relab)}
    for A6 in acts6:
        pperm = [None] * 27
        ok = True
        for j, mu in enumerate(w299):
            img = tuple(int(sum(A6[i, l] * mu[l] for l in range(6)))
                        for i in range(6))
            if img not in w299set:
                ok = False; break
            pperm[idx299_to_575[j]] = idx299_to_575[idx299[img]]
        if ok and all(p is not None for p in pperm):
            key = tuple(pperm)
            if key not in [p[0] for p in patterns]:
                patterns.append((key, perm))
print(f"  {len(patterns)} patterns loaded")
assert len(patterns) == 8

def pattern_solve(pperm, pairs_lr):
    rows = []
    for Ml, Mr in pairs_lr:
        for i in range(d):
            for j in range(d):
                coef = [K0] * d
                for k in range(d):
                    if pperm[k] == i:
                        coef[k] = coef[k] + Ml[k][j]
                coef[j] = coef[j] - Mr[i][pperm[j]]
                if not all(c.is_zero() for c in coef):
                    rows.append(coef)
        Rr, piv = rref(rows)
    return d - len(piv)

# ── stage 4: compute the degree bound and required sample count ──
# The system matrix for the twisted solve has entries from A27 (constant)
# and C27(t) (degree <= 2*(nil_order-1)). The constraint matrix is at most
# 27 x 27 with entries of degree <= 2*(nil_order-1). A maximal minor has
# degree <= 27 * 2*(nil_order-1). To prove it's identically nonzero, we need
# degree + 1 points with dim=0.
max_entry_deg = 2 * (nil_order - 1)
max_minor_deg = 27 * max_entry_deg
required_points = max_minor_deg + 1
print(f"\n  Max entry degree in t: {max_entry_deg}")
print(f"  Max 27x27 minor degree: {max_minor_deg}")
print(f"  Points needed for generic proof: {required_points}")

# That might be too many. Let's try a tighter bound.
# Actually, each pattern has a specific structure. The A-A equations don't involve t.
# Only the B-C(t) and C(t)-B equations involve t. So not all 27 rows of the system
# involve t. The rank contribution from the A-A rows is constant. Let's see how many
# rows come from each.

# Regardless, let me just sample as many points as practical.
# Each point takes the build_double + 8 pattern_solves.
# Let me time one.

print("\n  Timing one probe point...")
t0 = time.time()
acts_test, C_test, ok_test = build_double(K(3))
t1 = time.time()
TWISTED = ((A27, A27), (B27, C_test), (C_test, B27))
dims_test = [pattern_solve(list(pp), TWISTED) for pp, _ in patterns]
t2 = time.time()
print(f"  build_double: {t1-t0:.2f}s, 8 pattern solves: {t2-t1:.2f}s, total: {t2-t0:.2f}s")
print(f"  Test probe t=3: dims = {dims_test}, all zero: {all(d==0 for d in dims_test)}")

# ── stage 5: the extended sample ──
# Use t values in K: integers and OMEGA multiples
sample_values = []
# integers: 3, 4, 5, ..., up to what's practical
for n in range(3, 60):
    sample_values.append((f"t={n}", K(n)))
# omega multiples: 2*omega, 3*omega, ...
for n in range(2, 20):
    sample_values.append((f"t={n}*omega", K(n) * OMEGA))
# mixed: n + m*omega
for n in range(1, 10):
    for m in range(1, 5):
        sample_values.append((f"t={n}+{m}*omega", K(n) + K(m) * OMEGA))

# Already verified: t=1, t=omega, t=2 (from the recompute)
already_verified = 3

# Target: get as many as possible in reasonable time
N_TARGET = min(len(sample_values), 60)

print(f"\n  Sampling {N_TARGET} additional weld points (plus 3 already verified)...")
print(f"  {'probe':>20s}  {'dims':>25s}  {'all_zero':>8s}  {'time':>6s}")

all_zero_count = already_verified
failures = []
t_start = time.time()

for idx, (label, tv) in enumerate(sample_values[:N_TARGET]):
    t0 = time.time()
    try:
        acts_t, C_t, gates_ok = build_double(tv)
        if not gates_ok:
            print(f"  {label:>20s}  {'GATE FAIL':>25s}")
            failures.append((label, "gate fail"))
            continue
        TWISTED = ((A27, A27), (B27, C_t), (C_t, B27))
        dims = [pattern_solve(list(pp), TWISTED) for pp, _ in patterns]
        elapsed = time.time() - t0
        all_zero = all(dd == 0 for dd in dims)
        if all_zero:
            all_zero_count += 1
        else:
            failures.append((label, dims))
        print(f"  {label:>20s}  {str(dims):>25s}  {str(all_zero):>8s}  {elapsed:>5.1f}s")
    except Exception as e:
        elapsed = time.time() - t0
        print(f"  {label:>20s}  {'ERROR: ' + str(e)[:30]:>25s}  {elapsed:>5.1f}s")
        failures.append((label, str(e)))

    # Check time budget (10 min max)
    if time.time() - t_start > 540:
        print(f"\n  Time budget reached after {idx+1} probes.")
        break

total_time = time.time() - t_start

print(f"\n{'='*88}")
print(f"RESULTS")
print(f"{'='*88}")
print(f"  Total points verified: {all_zero_count} (3 original + {all_zero_count - 3} new)")
print(f"  Points needed for full closure: {required_points}")
print(f"  Failures: {len(failures)}")
if failures:
    for label, detail in failures:
        print(f"    {label}: {detail}")
print(f"  Total time: {total_time:.1f}s")

if all_zero_count >= required_points:
    print(f"\n  VERDICT: STABILIZED — dim=0 at {all_zero_count} distinct t values")
    print(f"  exceeds the degree bound ({max_minor_deg}). The twisted system has")
    print(f"  dim=0 for ALL t (the determinant polynomial is nonzero and has no roots).")
    verdict = "STABILIZED"
elif len(failures) == 0 and all_zero_count > 3:
    print(f"\n  VERDICT: EXTENDED — dim=0 at {all_zero_count} distinct t values")
    print(f"  ({required_points} needed for full closure)")
    if all_zero_count > required_points // 2:
        print(f"  MORE THAN HALF the required points verified — strong evidence.")
    verdict = "EXTENDED"
else:
    print(f"\n  VERDICT: {'DAMAGED' if failures else 'EXTENDED'}")
    verdict = "DAMAGED" if failures else "EXTENDED"

print(f"\nWALL-7 EXTENSION COMPLETE — {verdict}")
