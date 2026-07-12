#!/usr/bin/env python3
"""B540: the observer flow — induction dynamics on the 7 canonical systems.

Each canonical system (B535 census) is itself a substitution. Apply the
object's verb to it: grow its fixed point, induce on the length-1 prefix
window, canonicalize. Iterate to closure. Output: the flow graph, fixed
points, cycles, basins.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    factor_position_map, standard_return_words_from_positions,
    canonical_induced_system, canonical_codes,
)

# The 7 canonical systems (B535 C1), keyed by first-appearance factor
SYSTEMS = {
    'S_A':   ((0, 1, 2, 3), (3, 2, 0, 3), (3,), (0, 1, 2, 0, 3)),
    'S_B':   ((0, 1, 2), (0, 1, 0, 3, 2, 0), (0, 1), (0, 1, 2, 0)),
    'S_a':   ((0, 1, 2, 2, 3), (0, 2, 3), (0, 1, 2, 3), (0, 2)),   # = sigma
    'S_b':   ((0, 1, 2, 3), (2, 0, 3), (0, 3), (2, 0, 1, 0, 3)),
    'S_aA':  ((0, 1, 2, 3, 2, 1), (4, 2, 3, 2, 3), (0, 1), (4, 2, 3),
              (0, 1, 2, 3)),
    'S_Bab': ((0, 1, 2, 1, 3), (3,), (1, 0, 3), (0, 1, 2, 1, 0, 3)),
    'S_bABab': ((0, 1, 0, 1, 2, 3, 1, 0, 1, 2, 3, 1, 4, 1, 0, 1, 2, 3, 1),
                (0, 1, 3, 1, 4, 1),
                (0, 1, 0, 1, 2, 3, 1, 4, 1, 0, 1, 2, 3, 1, 4, 1),
                (0, 1, 0, 1, 2, 3, 1, 0, 1, 2, 3, 1, 4, 1, 0, 1, 2, 3, 1,
                 4, 1, 0, 1, 2, 3, 1),
                (0, 1, 0, 1, 2, 3, 1, 4, 1, 0, 1, 2, 3, 1)),
}
ALPHA = 'abcde'


def grow_codes(codes, target=200000):
    """Fixed/periodic point of the coded substitution, as a string."""
    sub = {ALPHA[i]: ''.join(ALPHA[j] for j in codes[i])
           for i in range(len(codes))}
    # find a prolongable seed: letter g with sub[g][0] == g, else iterate from 'a'
    seed = next((g for g in sub if sub[g][0] == g), ALPHA[0])
    w = seed
    while len(w) < target:
        w2 = ''.join(sub[c] for c in w)
        if w2 == w:
            break
        w = w2
    return w[:target]


def derive_prefix(codes):
    """The derived substitution of the coded system w.r.t. its prefix letter
    (standard Durand construction, self-contained: the engine's version is
    sigma-specific). tau(R_i) parses uniquely into return words of u since
    each return word starts with u and contains no other u."""
    sub = {ALPHA[i]: ''.join(ALPHA[j] for j in codes[i])
           for i in range(len(codes))}
    seed = next((g for g in sub if sub[g][0] == g), None)
    if seed is None:
        # use a periodic point: find g with sub^k(g) starting with g (k<=3)
        for g in sub:
            w2 = g
            for _ in range(3):
                w2 = ''.join(sub[c] for c in w2)
                if w2[0] == g:
                    seed = g
                    break
            if seed:
                break
    w = seed
    while len(w) < 100000:
        w = ''.join(sub[c] for c in w)
    u = w[0]
    # return words to u, in order of first appearance
    pos = [i for i, c in enumerate(w[:50000]) if c == u]
    rws, order = {}, []
    for a, b in zip(pos, pos[1:]):
        r = w[a:b]
        if r not in rws:
            rws[r] = len(order)
            order.append(r)
    # derived substitution: parse tau(R) into return words
    def parse(word):
        out, start = [], 0
        idx = [i for i, c in enumerate(word) if c == u] + [len(word)]
        for a, b in zip(idx, idx[1:]):
            out.append(rws[word[a:b]])
        return tuple(out)
    codes_out = tuple(parse(''.join(sub[c] for c in R)) for R in order)
    return canonical_codes(codes_out)


def main():
    canon = {canonical_codes(v): k for k, v in SYSTEMS.items()}
    flow = {}
    frontier_new = []
    for name, codes in SYSTEMS.items():
        out = derive_prefix(canonical_codes(codes))
        if out in canon:
            flow[name] = canon[out]
        else:
            label = f"NEW_{len(frontier_new)}"
            frontier_new.append((label, out))
            canon[out] = label
            flow[name] = label
    # iterate closure on any new nodes
    while frontier_new:
        label, codes = frontier_new.pop()
        out = derive_prefix(codes)
        if out not in canon:
            nl = f"NEW_{len(canon)}"
            canon[out] = nl
            frontier_new.append((nl, out))
        flow[label] = canon[out]

    print("THE OBSERVER FLOW (derive w.r.t. length-1 prefix):")
    for k in sorted(flow):
        arrow = " (FIXED POINT)" if flow[k] == k else ""
        print(f"  {k:9s} -> {flow[k]}{arrow}")

    # cycles and basins
    print("\nOrbit structure:")
    for start in sorted(SYSTEMS):
        path = [start]
        cur = start
        seen = {start}
        while flow[cur] not in seen:
            cur = flow[cur]
            path.append(cur)
            seen.add(cur)
        cyc_entry = flow[cur]
        i = path.index(cyc_entry)
        cycle = path[i:] if cyc_entry in path else [cyc_entry]
        print(f"  {start}: transient {path[:i]} -> cycle {path[i:] + [cyc_entry]}"
              if i > 0 else
              f"  {start}: enters cycle immediately: {path + [cyc_entry]}")

    # summary
    fixed = [k for k in flow if flow[k] == k]
    print(f"\nfixed points: {fixed}")
    new_nodes = [k for k in flow if k.startswith('NEW')]
    print(f"new systems beyond the census: {len(new_nodes)}"
          + (f" {new_nodes}" if new_nodes else " (census closed under the flow)"))


if __name__ == '__main__':
    main()
