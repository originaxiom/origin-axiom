"""EXPLORATORY: every substitution a -> u, b -> v (u, v non-empty positive words) with |u| + |v| <= N that can be undone
(the pair generates F2: Stallings folding to the two-petal rose), sorted by its matrix; which grow a word that never
repeats (primitive, hyperbolic); which thread each is (det +1: its own class; det -1: the class of its square)."""
import itertools, collections
import numpy as np

def generates_F2(words):
    # Stallings: one loop per word at vertex 0, fold, test for one vertex with one a-edge and one b-edge out
    edges = set(); n = 1
    for w in words:
        cur = 0
        for i, ch in enumerate(w):
            nxt = 0 if i == len(w) - 1 else n
            if nxt == n: n += 1
            edges.add((cur, ch, nxt)); cur = nxt
    parent = list(range(n))
    def f(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    changed = True
    while changed:
        changed = False
        E = {(f(s), c, f(t)) for s, c, t in edges}
        out, inn = {}, {}
        for s, c, t in E:
            if (s, c) in out and out[(s, c)] != t:
                parent[f(t)] = f(out[(s, c)]); changed = True; break
            out[(s, c)] = t
            if (t, c) in inn and inn[(t, c)] != s:
                parent[f(s)] = f(inn[(t, c)]); changed = True; break
            inn[(t, c)] = s
        edges = E
    E = {(f(s), c, f(t)) for s, c, t in edges}
    verts = {s for s, _, _ in E} | {t for _, _, t in E}
    return len(verts) == 1 and len(E) == 2

def thread(M):
    # positive word in L, R for a non-negative det +1 matrix (columns: images), as a canonical cyclic word
    L = np.array([[1, 1], [0, 1]]); R = np.array([[1, 0], [1, 1]]); w = []
    M = M.copy()
    while not (M == np.eye(2, dtype=int)).all():
        # M = L X if the first row dominates, M = R X if the second does
        if (M[0] >= M[1]).all(): w.append("L"); M = np.array([[1, -1], [0, 1]]) @ M
        elif (M[1] >= M[0]).all(): w.append("R"); M = np.array([[1, 0], [-1, 1]]) @ M
        else: return None
    s = "".join(w)
    return min(s[i:] + s[:i] for i in range(len(s))) if s else ""

N = 8
rows = collections.defaultdict(list)
for tot in range(2, N + 1):
    for lu in range(1, tot):
        for u in itertools.product("ab", repeat=lu):
            for v in itertools.product("ab", repeat=tot - lu):
                u_, v_ = "".join(u), "".join(v)
                if not generates_F2([u_, v_]): continue
                M = np.array([[u_.count("a"), v_.count("a")], [u_.count("b"), v_.count("b")]])
                rows[tuple(M.flatten())].append((u_, v_))
count = sum(len(v) for v in rows.values())
print(f"substitutions that can be undone, |u|+|v| <= {N}: {count}, with {len(rows)} distinct matrices")
ok = all(len(subs) == int(np.array(m).sum()) - 1 for m, subs in rows.items() if int(np.array(m).sum()) > 2)
print("every matrix carries exactly |u|+|v|-1 wordings (the conjugates; Seebold):", ok)
hyp, par = [], []
for m, subs in sorted(rows.items(), key=lambda kv: (sum(kv[0]), kv[0])):
    M = np.array(m).reshape(2, 2); d = round(np.linalg.det(M)); t = int(np.trace(M))
    primitive = (np.linalg.matrix_power(M, 2) > 0).all() or (np.linalg.matrix_power(M, 3) > 0).all()
    if primitive:
        sq = M @ M if d == -1 else M
        hyp.append((sum(m), d, t, thread(sq) if d == 1 else thread(sq) + " (square)", subs))
    else:
        par.append((sum(m), d, t, subs))
print(f"\nthey grow a word that repeats (not primitive): {sum(len(p[3]) for p in par)} wordings, {len(par)} matrices:")
for tot, d, t, subs in par:
    print(f"   |u|+|v|={tot} det {d:+d} tr {t}:", ", ".join(f"a->{u} b->{v}" for u, v in subs))
print(f"\nthey grow a word that never repeats: {sum(len(h[4]) for h in hyp)} wordings, {len(hyp)} matrices")
threads = collections.Counter()
for tot, d, t, th, subs in hyp:
    threads[th] += len(subs)
    if tot <= 5:
        print(f"   |u|+|v|={tot} det {d:+d} tr {t} thread {th}:", ", ".join(f"a->{u} b->{v}" for u, v in subs))
print("\nthreads (as cyclic words in L, R) reached, with the number of wordings that reach each:")
for th, c in sorted(threads.items(), key=lambda kv: (len(kv[0]), kv[0])):
    print(f"   {th:14s} {c}")
