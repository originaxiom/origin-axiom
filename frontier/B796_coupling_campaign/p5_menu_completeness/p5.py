r"""P5 — MENU COMPLETENESS, decided by enumeration rather than by trust.

WHY THIS IS THE WHOLE QUESTION NOW
----------------------------------
The content ledger grades three rows DERIVED-GIVEN-P5: the gauge algebra (row
1), charge quantisation (row 3, via B862), and the termination theorem (row 11).
And the confluence result retired the ranking rule, leaving P5 as the cascade's
ONLY external import. So P5 is the single most load-bearing unproved thing in
the content picture.

WHAT P5 ASSERTS: that B861's menu at each cascade step lists ALL the options.

WHAT MAKES IT DECIDABLE: the cascade's walls are CENTRALIZERS of semisimple
elements (B964: the construction IS an adjoint Higgs mechanism, and the unbroken
group is the centralizer). A centralizer of a semisimple element is always a
FULL-RANK REGULAR subalgebra -- a Levi, or a Borel-de Siebenthal subalgebra.
That is a finite, classified set, obtained from the EXTENDED Dynkin diagram:

  * remove one node of PRIME mark p from the extended diagram
        -> a maximal-rank REGULAR semisimple subalgebra   (Borel-de Siebenthal)
  * remove one node from the ORDINARY diagram, keeping a u(1)
        -> a maximal LEVI subalgebra

So "is the menu complete?" is not a survey. It is: enumerate the extended
diagram's node-deletions and compare with the banked menu.

Everything below is computed from the Cartan matrices, which are built from the
Dynkin data -- no table of subalgebras is consulted.

Gate 5-Q. Structure only.
"""
import itertools


# ---------------------------------------------------------------- the diagrams
# each entry: (name, n, edges on nodes 0..n-1, marks of the highest root,
#              which node the AFFINE node attaches to)
DIAGRAMS = {
    'E6': dict(
        n=6,
        # Bourbaki: chain 1-3-4-5-6, node 2 attached to node 4
        edges=[(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)],
        marks=[1, 2, 2, 3, 2, 1],
        affine_to=1,        # affine node attaches to the mark-2 branch node a2
    ),
    'D5': dict(
        n=5,
        # so(10): chain 1-2-3 with 4 and 5 forked off 3
        edges=[(0, 1), (1, 2), (2, 3), (2, 4)],
        marks=[1, 2, 2, 1, 1],
        affine_to=1,
    ),
    'A4': dict(
        n=4,                # su(5)
        edges=[(0, 1), (1, 2), (2, 3)],
        marks=[1, 1, 1, 1],
        affine_to=None,     # A_n affine closes the chain into a cycle
    ),
}


def components(nodes, edges):
    """Connected components of the induced subgraph."""
    nodes = set(nodes)
    adj = {v: set() for v in nodes}
    for a, b in edges:
        if a in nodes and b in nodes:
            adj[a].add(b)
            adj[b].add(a)
    seen, out = set(), []
    for v in sorted(nodes):
        if v in seen:
            continue
        comp, stack = set(), [v]
        while stack:
            u = stack.pop()
            if u in comp:
                continue
            comp.add(u)
            stack.extend(adj[u] - comp)
        seen |= comp
        out.append(comp)
    return out


def name_component(comp, edges):
    """Identify a connected simply-laced diagram by size and shape."""
    k = len(comp)
    if k == 0:
        return None
    deg = {v: 0 for v in comp}
    for a, b in edges:
        if a in comp and b in comp:
            deg[a] += 1
            deg[b] += 1
    degs = sorted(deg.values())
    if k == 1:
        return 'A1'
    if degs == [1, 1] + [2] * (k - 2):
        return f'A{k}'
    if 3 in degs:                       # a branch node
        # count arm lengths from the trivalent node
        centre = [v for v in comp if deg[v] == 3][0]
        adj = {v: set() for v in comp}
        for a, b in edges:
            if a in comp and b in comp:
                adj[a].add(b)
                adj[b].add(a)
        arms = []
        for nb in adj[centre]:
            ln, prev, cur = 1, centre, nb
            while True:
                nxt = adj[cur] - {prev}
                if not nxt:
                    break
                prev, cur = cur, nxt.pop()
                ln += 1
            arms.append(ln)
        arms.sort()
        if arms[:2] == [1, 1]:
            return f'D{k}'
        if arms == [1, 2, 2]:
            return 'E6'
        if arms == [1, 2, 3]:
            return 'E7'
        if arms == [1, 2, 4]:
            return 'E8'
        return f'D/E({k}){arms}'
    return f'?({k})'


def label(comps, edges, u1s=0):
    parts = [name_component(c, edges) for c in comps if c]
    parts = [p for p in parts if p]
    parts.sort()
    s = ' + '.join(parts) if parts else '(empty)'
    if u1s:
        s += f' + {u1s}xU(1)'
    return s


def analyse(key):
    d = DIAGRAMS[key]
    n, edges, marks = d['n'], list(d['edges']), d['marks']
    aff = n                                   # index of the affine node
    ext_edges = list(edges)
    if d['affine_to'] is not None:
        ext_edges.append((aff, d['affine_to']))
    else:                                     # A_n: affine closes the cycle
        ext_edges += [(aff, 0), (aff, n - 1)]
    ext_marks = marks + [1]

    print(f'\n{"="*70}\n{key}: extended diagram, marks {ext_marks} (affine = 1)')
    print(f'{"="*70}')

    print('\n  BOREL-de SIEBENTHAL — delete one PRIME-mark node from the extended diagram')
    print('  (these are the maximal-rank REGULAR SEMISIMPLE subalgebras)')
    bds = set()
    for v in range(n + 1):
        m = ext_marks[v]
        if m < 2 or any(m % p == 0 for p in range(2, m) if m % p == 0):
            if m not in (2, 3, 5):            # prime marks only
                continue
        if m in (2, 3, 5):
            rest = [u for u in range(n + 1) if u != v]
            lab = label(components(rest, ext_edges), ext_edges)
            bds.add(lab)
            print(f'    delete node {v} (mark {m})  ->  {lab}')

    print('\n  LEVI — delete one node from the ORDINARY diagram, keep a u(1)')
    print('  (these are the maximal-rank regular subalgebras WITH an abelian factor)')
    levi = set()
    for v in range(n):
        rest = [u for u in range(n) if u != v]
        lab = label(components(rest, edges), edges, u1s=1)
        levi.add(lab)
        print(f'    delete node {v}            ->  {lab}')

    return bds, levi


def main():
    print('P5 — MENU COMPLETENESS BY ENUMERATION')

    banked = {
        'E6': ['SO(10)xU(1) = D5+U(1)', 'SU(6)xSU(2) = A5+A1',
               'SU(3)^3 = A2+A2+A2', 'Sp(8) = C4  [an S-subalgebra, not regular]'],
        'D5': ['SU(5)xU(1) = A4+U(1)', 'Pati-Salam = A3+A1+A1 (= D3+A1+A1)'],
        'A4': ['the SM = A2+A1+U(1)', 'SU(4)xU(1) = A3+U(1)'],
    }

    for k in ('E6', 'D5', 'A4'):
        bds, levi = analyse(k)
        print(f'\n  BANKED MENU (B861) at this step:')
        for b in banked[k]:
            print(f'    - {b}')
        print(f'\n  ENUMERATED regular options: {len(bds | levi)} distinct')
        print(f'    Borel-de Siebenthal : {sorted(bds)}')
        print(f'    Levi                : {sorted(levi)}')


if __name__ == '__main__':
    main()
