#!/usr/bin/env python3
"""Independent re-counter for the Ω strict-full survivor tower (verify-don't-trust).

Written from scratch (does NOT import the handoff's omega_* code) to re-derive the
strict-full counts L4..L10 = 96, 672, 3840, 20928, 105312, 521904, 2488080 under
our own governance.

Definition (reverse-engineered from the chunked pipeline + summaries, then re-stated
cleanly here):
- base L=4: all strongly-connected length-4 positive-shear histories whose 4x4 matrix
  has charpoly x^4-4x^3+5x^2-4x+1  (abc=(4,5,4), the Ω4 / golden×phase seed) AND is
  full-metric.  -> 96
- step L-1 -> L: extend each surviving endpoint by all 12 elementary row-shears
  S_ij (row_i += row_j, i!=j); keep a target iff it is full-metric; accumulate the
  path multiplicity.  A "survivor" history is one whose endpoint is full-metric at
  EVERY level from 4 to L.

Full-metric test (EXACT, stronger than the handoff's integer-combo sampling):
  M is full-metric  <=>  the space {symmetric G : M^T G M = G} contains a
  NONDEGENERATE member  <=>  det( sum_i s_i B_i ) is not the zero polynomial in the
  symbolic coordinates s_i of a basis {B_i} of that space.
We do NOT short-circuit on reciprocity in the validation run, so a match also
re-confirms TC-2 (non-reciprocal => not full-metric) empirically.

Run:
  python independent_recount.py --max-level 7              # fast validation
  python independent_recount.py --resume 7 --max-level 10  # heavy extension (background)
State is checkpointed per level to <state-dir>/counter_L{level}.json (resumable).
"""
from __future__ import annotations
import argparse, json, time, itertools, tempfile
from collections import Counter
from pathlib import Path
import sympy as sp

N = 4
EDGES = tuple((i, j) for i in range(N) for j in range(N) if i != j)
IDENTITY = tuple(tuple(1 if i == j else 0 for j in range(N)) for i in range(N))
SEED_ABC = (4, 5, 4)  # x^4 - 4x^3 + 5x^2 - 4x + 1  (golden × phase)

_SVARS = sp.symbols("s0:10")
_IDX = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]


def apply_shear(M, i, j):
    rows = [list(r) for r in M]
    rows[i] = [rows[i][k] + rows[j][k] for k in range(N)]
    return tuple(tuple(r) for r in rows)


def mat_key(M):
    return json.dumps(M, separators=(",", ":"))


def mat_from_key(k):
    return tuple(tuple(int(x) for x in row) for row in json.loads(k))


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)) for i in range(N))


def charpoly_abc(M):
    A2 = matmul(M, M); A3 = matmul(A2, M)
    t1 = sum(M[i][i] for i in range(N))
    t2 = sum(A2[i][i] for i in range(N))
    t3 = sum(A3[i][i] for i in range(N))
    e2 = (t1 * t1 - t2) // 2
    e3 = (t1 ** 3 - 3 * t1 * t2 + 2 * t3) // 6
    return (int(t1), int(e2), int(e3))  # x^4 - t1 x^3 + e2 x^2 - e3 x + 1


def strongly_connected(hist):
    adj = [set() for _ in range(N)]; radj = [set() for _ in range(N)]
    for i, j in hist:
        adj[j].add(i); radj[i].add(j)

    def reach(g):
        seen = {0}; st = [0]
        while st:
            u = st.pop()
            for v in g[u]:
                if v not in seen:
                    seen.add(v); st.append(v)
        return len(seen) == N
    return reach(adj) and reach(radj)


def invariant_basis(M):
    G = sp.zeros(N)
    for v, (i, j) in zip(_SVARS, _IDX):
        G[i, j] = v; G[j, i] = v
    A = sp.Matrix(M)
    E = A.T * G * A - G
    eqs = [E[i, j] for i in range(N) for j in range(i, N)]
    Aeq, _ = sp.linear_eq_to_matrix(eqs, _SVARS)
    out = []
    for vec in Aeq.nullspace():
        B = sp.zeros(N)
        for val, (i, j) in zip(vec, _IDX):
            B[i, j] = val; B[j, i] = val
        out.append(B)
    return out


def is_full_metric_exact(M, cache):
    k = mat_key(M)
    if k in cache:
        return cache[k]
    basis = invariant_basis(M)
    if not basis:
        cache[k] = False
        return False
    # generic member G = sum s_i B_i ; nondegenerate member exists iff det(G) != 0 as a poly
    G = sp.zeros(N)
    for c, B in zip(_SVARS, basis):
        G += c * B
    res = sp.expand(G.det()) != 0
    cache[k] = bool(res)
    return bool(res)


def initial_seed_counter(cache):
    out = Counter()
    for hist in itertools.product(EDGES, repeat=4):
        if not strongly_connected(hist):
            continue
        M = IDENTITY
        for i, j in hist:
            M = apply_shear(M, i, j)
        if charpoly_abc(M) == SEED_ABC and is_full_metric_exact(M, cache):
            out[M] += 1
    return out


def step(counter, cache, recip_shortcut):
    nxt = Counter()
    for M, mult in counter.items():
        for (i, j) in EDGES:
            T = apply_shear(M, i, j)
            if recip_shortcut:
                abc = charpoly_abc(T)
                if abc[0] != abc[2]:
                    continue  # TC-2: non-reciprocal => not full-metric
            if is_full_metric_exact(T, cache):
                nxt[T] += mult
    return nxt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-level", type=int, default=7)
    ap.add_argument("--resume", type=int, default=None, help="resume from this level's checkpoint")
    ap.add_argument("--state-dir", type=Path,
                    default=Path(tempfile.gettempdir()) / "omega_recount_state",
                    help="scratch dir for per-level checkpoints (default: system temp; keeps the repo clean)")
    ap.add_argument("--recip-shortcut", action="store_true",
                    help="skip non-reciprocal targets (faster; justified by TC-2). Off by default for an independent validation run.")
    args = ap.parse_args()
    sd = args.state_dir; sd.mkdir(parents=True, exist_ok=True)
    cache = {}
    log = sd / "progress.log"

    def emit(msg):
        line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
        print(line, flush=True)
        with open(log, "a") as f:
            f.write(line + "\n")

    if args.resume is not None:
        rows = json.loads((sd / f"counter_L{args.resume}.json").read_text())
        counter = Counter({mat_from_key(k): int(c) for k, c in rows})
        start = args.resume
        emit(f"RESUME L{start}: paths={sum(counter.values())} endpoints={len(counter)}")
    else:
        t0 = time.time()
        counter = initial_seed_counter(cache)
        start = 4
        (sd / "counter_L4.json").write_text(json.dumps([[mat_key(M), c] for M, c in counter.items()]))
        emit(f"L4 seed: paths={sum(counter.values())} endpoints={len(counter)} ({time.time()-t0:.1f}s)")

    for L in range(start + 1, args.max_level + 1):
        t0 = time.time()
        counter = step(counter, cache, args.recip_shortcut)
        (sd / f"counter_L{L}.json").write_text(json.dumps([[mat_key(M), c] for M, c in counter.items()]))
        emit(f"L{L}: paths={sum(counter.values())} endpoints={len(counter)} "
             f"distinct_solved={len(cache)} ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()
