"""B2006, listening card 21 (main, 2026-11-25; data-free): G_k (C and sigma on the orbit of (3,3,3) mod 3^k) against G_2 = S4
on the orbit mod 9, by reduction mod 9. T1: equivariance, onto, fibre sizes, the induced map's image and kernel. T2: rho^3
(rho(C)^3 = 1, rho(sigma)^3 = -1) on the kernel. T3: the kernel's structure (abelian, exponent).
    python3 -B layer.py > layer_run.txt"""
import contextlib, io, pathlib, time
from collections import Counter, deque
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE.parent.parent / "B2004_listening_19_the_mechanism_of_the_halving_the_modular_group_and_its_order_six_character" / "verification" / "mechanism.py").read_text().split("WORDS = words(10)")[0]
ns = {"__file__": str(HERE / "layer.py")}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src, "b2004_head", "exec"), ns)
t0 = time.time()
p9, i9, c9, s9, _ = ns["orbit"](9, (3, 3, 3)); n9 = len(p9)
for k in (3, 4, 5):
    N = 3 ** k
    pts, idx, pC, pS, _ = ns["orbit"](N, (3, 3, 3)); n = len(pts)
    red = np.array([i9.get((v[0] % 9, v[1] % 9, v[2] % 9), -1) for v in pts])
    onto = red.min() >= 0 and len(set(red.tolist())) == n9
    equiv = bool(np.all(red[pC] == c9[red]) and np.all(red[pS] == s9[red]))
    fib = Counter(red.tolist())
    print("mod %d: reduction mod 9 into the 8-point orbit: defined on every point and onto: %s; C- and sigma-equivariant: %s; fibre sizes %s  [%.0f s]" % (N, onto, equiv, sorted(set(fib.values())), time.time() - t0), flush=True)
    # walk the group, recording rho and the induced permutation of the 8 points
    dt = np.int16 if n < 32000 else np.int32
    e = np.arange(n, dtype=dt); e9 = np.arange(n9)
    gens = [(pC.astype(dt), c9, 2), (pS.astype(dt), s9, 3)]
    seen = {e.tobytes(): (0, e9.tobytes())}; q = deque([(e, e9)])
    while q:
        g, g9 = q.popleft(); r = seen[g.tobytes()][0]
        for s, s_9, es in gens:
            h = s[g]; key = h.tobytes()
            if key not in seen:
                h9 = s_9[g9]; seen[key] = ((r + es) % 6, h9.tobytes()); q.append((h, h9))
    image = {v[1] for v in seen.values()}
    kernel = [np.frombuffer(key, dtype=dt) for key, v in seen.items() if v[1] == e9.tobytes()]
    rho3_on_kernel = sorted({(seen[kk.tobytes()][0] * 3) % 6 for kk in kernel})
    rho2_on_kernel = sorted({(seen[kk.tobytes()][0] * 2) % 6 for kk in kernel})
    print("    |G_k| = %d; image in G_2 has %d elements (G_2 = S4 has 24); kernel order %d (|G_k|/24 = %d); rho^3 on the kernel takes exponents %s (trivial: %s); rho^2 on the kernel takes %s  [%.0f s]" % (
        len(seen), len(image), len(kernel), len(seen) // 24, rho3_on_kernel, rho3_on_kernel == [0], rho2_on_kernel, time.time() - t0), flush=True)
    K = PermutationGroup([Permutation([int(i) for i in g]) for g in kernel[:min(len(kernel), 400)]]) if len(kernel) > 1 else None
    if K is not None:
        orders = Counter()
        for g in kernel:
            p = g.copy(); o = 1
            while not np.array_equal(p, e): p = g[p]; o += 1
            orders[o] += 1
        print("    kernel: order %d (sympy, from up to 400 of its elements as generators); abelian: %s; element orders %s; a 3-group: %s" % (
            K.order(), K.is_abelian, dict(sorted(orders.items())), all(o in (1, 3, 9, 27, 81, 243, 729) for o in orders)), flush=True)
