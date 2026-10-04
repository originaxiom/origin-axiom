#!/usr/bin/env python3
"""The golden covers dossier: design-time STRUCTURE only (group theory; no homology rank, no twisted cohomology).

For each binary polyhedral group G in {Q8, 2T, 2O, 2I} (unit quaternions, built by closure): the kernels of surjections
F2 = <a, b> -> G, and how each word state's monodromy phi (sm:B1527's presentation, through sm:B1538's punct_covers) permutes
them -- the fixed kernels (fibre-direction G-covers at level 1) and the cycle type (a kernel in a k-cycle is fixed at level
M_k).  A kernel is identified by the regular action of F2 on G: the BFS-canonical labelling of the Cayley graph of G with
respect to the generating pair (x, y) determines ker(F2 -> G) and is determined by it.  This is a second, independent route
to gc_icosian.py's 2I numbers (there: generating pairs of SL(2,5) up to GL(2,5) conjugation).

Part 1: the four states of sm:B1538's population (the golden m004, m003 and the silver m136, m135), with the fixed kernels'
puncture order and whether the induced automorphism is inner or outer.  Part 2: the fixed counts at level 1 on every word
state of length 2 to 6 (cyclic words up to rotation, both signs), to scope Part 1: fixing icosian kernels at level 1 is not
special to the golden states.

    python3 gc_binary_polyhedral.py      (a few seconds)"""
import itertools
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "frontier" / "B1538_the_puncture_characters" / "verification"))
import punct_covers as F  # noqa: E402

PHI = (1 + 5 ** 0.5) / 2


def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return (a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2)


def key(q):
    return tuple(int(round(c * 10 ** 8)) for c in q)


def closure(gens):
    one = (1.0, 0.0, 0.0, 0.0)
    seen = {key(one): one}
    frontier = [one]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                k = qmul(g, h)
                kk = key(k)
                if kk not in seen:
                    seen[kk] = k
                    nxt.append(k)
        frontier = nxt
    return seen


GROUPS = {
    "Q8": [(0, 1, 0, 0), (0, 0, 1, 0)],
    "2T": [(0, 1, 0, 0), (0.5, 0.5, 0.5, 0.5)],
    "2O": [(0.5, 0.5, 0.5, 0.5), (2 ** -0.5, 2 ** -0.5, 0, 0)],
    "2I": [(0.5, 0.5, 0.5, 0.5), (PHI / 2, 1 / (2 * PHI), 0.5, 0)],
}
ORDERS = {"Q8": 8, "2T": 24, "2O": 48, "2I": 120}


class Group:
    def __init__(self, name):
        els = closure(GROUPS[name])
        assert len(els) == ORDERS[name], (name, len(els))
        self.keys = sorted(els)
        self.idx = {k: i for i, k in enumerate(self.keys)}
        self.n = len(self.keys)
        q = [els[k] for k in self.keys]
        self.table = [[self.idx[key(qmul(q[i], q[j]))] for j in range(self.n)] for i in range(self.n)]
        self.one = self.idx[key((1.0, 0.0, 0.0, 0.0))]
        self.inv = [next(j for j in range(self.n) if self.table[i][j] == self.one) for i in range(self.n)]

    def gen_size(self, x, y):
        seen, fr = {self.one}, [self.one]
        while fr:
            nxt = []
            for g in fr:
                for h in (x, y):
                    k = self.table[g][h]
                    if k not in seen:
                        seen.add(k)
                        nxt.append(k)
            fr = nxt
        return len(seen)

    def kernel_key(self, x, y):
        """BFS-canonical labelling of the right Cayley graph w.r.t. (x, y): the pair of permutations (right mult by x, y)
        on the BFS order.  Equal iff the two surjections F2 -> G have the same kernel."""
        order = {self.one: 0}
        queue = [self.one]
        for g in queue:
            for h in (x, y, self.inv[x], self.inv[y]):
                k = self.table[g][h]
                if k not in order:
                    order[k] = len(order)
                    queue.append(k)
        px = tuple(order[self.table[g][x]] for g in queue)
        py = tuple(order[self.table[g][y]] for g in queue)
        return px, py

    def order(self, g):
        k, h = 1, g
        while h != self.one:
            h, k = self.table[h][g], k + 1
        return k

    def auto_type(self, x, y, nx, ny):
        """the automorphism x -> nx, y -> ny (same kernel): inner or outer, and its order as an automorphism and modulo
        inner automorphisms (computed on the generating pair)."""
        def compose_power(k):
            ax, ay = x, y
            for _ in range(k):
                # apply the automorphism once more: x -> nx, y -> ny extended to words via the Cayley-graph labelling
                ax, ay = self.apply(x, y, nx, ny, ax), self.apply(x, y, nx, ny, ay)
            return ax, ay
        inner = lambda u, v: any(self.table[self.table[g][x]][self.inv[g]] == u and
                                 self.table[self.table[g][y]][self.inv[g]] == v for g in range(self.n))
        is_inner = inner(nx, ny)
        k_aut = next(k for k in range(1, 200) if compose_power(k) == (x, y))
        k_out = next(k for k in range(1, 200) if inner(*compose_power(k)))
        return f"is {'inner' if is_inner else 'outer'}; order {k_aut}, order {k_out} modulo inner"

    def apply(self, x, y, nx, ny, g):
        """the image of g under the automorphism determined by x -> nx, y -> ny (g written as a word in x, y by BFS)."""
        if not hasattr(self, "_words") or self._words[0] != (x, y):
            words = {self.one: ""}
            queue = [self.one]
            for h in queue:
                for ch, s in (("a", x), ("b", y), ("A", self.inv[x]), ("B", self.inv[y])):
                    k = self.table[h][s]
                    if k not in words:
                        words[k] = words[h] + ch
                        queue.append(k)
            self._words = ((x, y), words)
        return self.word(self._words[1][g], nx, ny)

    def word(self, w, x, y):
        out = self.one
        for ch in w:
            out = self.table[out][{"a": x, "b": y, "A": self.inv[x], "B": self.inv[y]}[ch]]
        return out


def kernel_reps(G):
    pairs = [(x, y) for x in range(G.n) for y in range(G.n) if G.gen_size(x, y) == G.n]
    kernels = {}
    for x, y in pairs:
        kernels.setdefault(G.kernel_key(x, y), (x, y))
    return pairs, list(kernels.items())


def perm_on_kernels(G, reps, st):
    return {kk: G.kernel_key(G.word(st.img["a"], x, y), G.word(st.img["b"], x, y)) for kk, (x, y) in reps}


def trace(w):
    a, b, c, d = 1, 0, 0, 1
    for ch in w:
        a, b, c, d = (a + b, b, c + d, d) if ch == "L" else (a, a + b, c, c + d)
    return a + d


def main():
    groups = {g: Group(g) for g in ("Q8", "2T", "2O", "2I")}
    reps = {}
    print("Part 1: the four states of sm:B1538's population")
    names = {"+LR": "m004", "-LR": "m003", "+LLRR": "m136", "-LLRR": "m135"}
    for gname, G in groups.items():
        pairs, reps[gname] = kernel_reps(G)
        print(f"{gname} (order {G.n}): generating pairs {len(pairs)}, kernels F2 -> {gname}: {len(reps[gname])}, "
              f"|Aut| = {len(pairs) // len(reps[gname])}")
        for sw, nm in names.items():
            st = F.State(sw)
            perm = perm_on_kernels(G, reps[gname], st)
            seen, cyc = set(), []
            for kk, _ in reps[gname]:
                if kk in seen:
                    continue
                n, c = 0, kk
                while c not in seen:
                    seen.add(c)
                    c = perm[c]
                    n += 1
                cyc.append(n)
            fixed = [(kk, xy) for kk, xy in reps[gname] if perm[kk] == kk]
            print(f"  {nm} = {sw}: fixed {len(fixed)}; cycle lengths {dict(sorted(Counter(cyc).items()))}")
            for kk, (x, y) in fixed:
                print(f"    fixed kernel: [a,b] has order {G.order(G.word('abAB', x, y))}; the induced automorphism "
                      f"{G.auto_type(x, y, G.word(st.img['a'], x, y), G.word(st.img['b'], x, y))}")
    print("Part 2: kernels fixed at level 1 on every word state of length 2 to 6 (2T, 2O, 2I; Q8's kernel is characteristic)")
    words = set()
    for n in range(2, 7):
        for w in itertools.product("LR", repeat=n):
            w = "".join(w)
            if "L" in w and "R" in w:
                words.add(min(w[i:] + w[:i] for i in range(n)))
    for w in sorted(words, key=lambda v: (len(v), v)):
        for sign in "+-":
            st = F.State(sign + w)
            row = []
            for gname in ("2T", "2O", "2I"):
                perm = perm_on_kernels(groups[gname], reps[gname], st)
                row.append(f"{gname} {sum(1 for kk, _ in reps[gname] if perm[kk] == kk)}")
            print(f"  {sign}{w:7s} trace {trace(w):3d}: " + ", ".join(row))


if __name__ == "__main__":
    main()
