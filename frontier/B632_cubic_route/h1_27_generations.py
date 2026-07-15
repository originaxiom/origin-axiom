"""B632 cell 1 — the principal decomposition of the 27 as a local system
and h^1(M; 27_rho), exact over Q(omega).

Reuses B575's build verbatim (exec of stages 0-3: the e6-in-gl(27)
basis, the principal sl2, the exact holonomy A27/B27, the relator gate
G3), then computes on the NEW module: the 27 itself.

Prereg: PREREGISTRATION.md (verdict table locked before running).
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
B575 = os.path.join(HERE, "..", "B575_bridge_obstruction", "l51_obstruction.py")

src = open(B575).read()
cut = src.index("# ---------------------------------------------------------------- stage 4")
prefix = src[:cut]
ns = {"__name__": "b575_prefix", "__file__": B575}
t0 = time.time()
print("executing B575 stages 0-3 (exact e6 build + holonomy)...", flush=True)
exec(compile(prefix, B575, "exec"), ns)
print(f"B575 prefix done in {time.time()-t0:.1f}s", flush=True)

K0, K1 = ns["K0"], ns["K1"]
K = ns["K"]
h_pr = ns["h_pr"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
REL = ns["REL"]
meye, mzero, madd, mmul, mscale, msub = (ns[k] for k in
    ("meye", "mzero", "madd", "mmul", "mscale", "msub"))
nullspace, rref = ns["nullspace"], ns["rref"]

# ---- (1) the principal decomposition of the 27 ------------------------------
# h_pr eigenvalues: exact kernel ranks of (h_pr - t I) over the weight range
print("\n(1) principal-sl2 decomposition of the 27:", flush=True)
eigmult = {}
for t in range(-30, 31):
    rows = [[h_pr[i][j] - (K(t) if i == j else K0) for j in range(27)]
            for i in range(27)]
    ker = nullspace(rows)
    if ker:
        eigmult[t] = len(ker)
assert sum(eigmult.values()) == 27, f"h_pr not diagonalizable over Z? {eigmult}"
print(f"  h-eigenvalue multiplicities: {eigmult}", flush=True)
# peel off strings: repeatedly take the top weight T -> one V(T), decrement
mult = dict(eigmult)
spins = []
while any(v > 0 for v in mult.values()):
    T = max(t for t, v in mult.items() if v > 0)
    spins.append(T // 2)
    for t in range(-T, T + 1, 2):
        mult[t] = mult.get(t, 0) - 1
        assert mult[t] >= 0, f"string peel failed at {t} (top {T})"
spins.sort(reverse=True)
dims = [2 * s + 1 for s in spins]
print(f"  27 = " + " + ".join(f"V({2*s})" for s in spins) +
      f"   (dims {dims}, sum {sum(dims)})", flush=True)
assert sum(dims) == 27

# ---- (2) Fox calculus on the 27 ----------------------------------------------
print("\n(2) H^*(M; 27_rho) by Fox calculus (exact):", flush=True)
acts = {'a': A27, 'b': B27, 'A': A27i, 'B': B27i}
La = [[K0] * 27 for _ in range(27)]
Lb = [[K0] * 27 for _ in range(27)]
Pi = meye(27)
for ch in REL:
    if ch == 'a':   contrib, tgt, sgn = meye(27), 'a', 1
    elif ch == 'A': contrib, tgt, sgn = acts['A'], 'a', -1
    elif ch == 'b': contrib, tgt, sgn = meye(27), 'b', 1
    else:           contrib, tgt, sgn = acts['B'], 'b', -1
    term = mmul(Pi, contrib)
    if sgn < 0:
        term = mscale(K(-1), term)
    if tgt == 'a':
        La = madd(La, term)
    else:
        Lb = madd(Lb, term)
    Pi = mmul(Pi, acts[ch])

# rank of [La | Lb] (27 x 54)
big = [[La[i][j] for j in range(27)] + [Lb[i][j] for j in range(27)]
       for i in range(27)]
_, piv = rref([row[:] for row in big])
rank_d1 = len(piv)

# h^0: common fixed vectors of A27, B27
rows0 = ([[A27[i][j] - (K1 if i == j else K0) for j in range(27)]
          for i in range(27)] +
         [[B27[i][j] - (K1 if i == j else K0) for j in range(27)]
          for i in range(27)])
h0 = len(nullspace(rows0))

h1 = (54 - rank_d1) - (27 - h0)
h2 = 27 - rank_d1
print(f"  rank(delta^1) = {rank_d1};  h^0 = {h0},  h^1 = {h1},  h^2 = {h2}",
      flush=True)
assert h0 - h1 + h2 == 0, "Euler gate FAILED"
print("  Euler gate PASS (h0 - h1 + h2 = 0)", flush=True)

# ---- (3) the block cross-check -----------------------------------------------
print("\n(3) block cross-check:", flush=True)
pred_h0 = sum(1 for s in spins if s == 0)          # trivial blocks
pred_h1 = sum(1 for s in spins)                    # 1 per block (MFP / banked)
print(f"  predicted from blocks: h^0 = {pred_h0} (trivial blocks), "
      f"h^1 = {pred_h1} (= #blocks; banked h^1=1 per Sym block, b1=1 trivial)",
      flush=True)
match = "AGREE" if (h0 == pred_h0 and h1 == pred_h1) else "DISAGREE"
print(f"  direct vs blocks: {match}", flush=True)

print(f"\n==== VERDICT (locked table): h^1(M; 27_rho) = {h1} ====", flush=True)
if h1 == 3:
    print("THREE-slot cohomological multiplicity EXISTS — B308's gate opens; "
          "cell 2 (the cup-product cubic texture) is the queued computation.",
          flush=True)
elif h1 < 3:
    print("The cubic/Yukawa route DIES here (fewer than three slots) — "
          "banked as the honest kill.", flush=True)
else:
    print("More slots than generations — data; any generation reading needs "
          "a selection principle stated before use.", flush=True)
print("B632 cell 1 DONE", flush=True)
