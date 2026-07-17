"""B666 cell W3-4 (L98) -- shared library.

metallic_word / spectrum are VERBATIM copies of the banked B186 functions
as mirrored in the verified packet copy
  frontier/B646_wave2_integration/cc2_packets/next_queue/next_queue/n3_fine_grid/lib_banked.py
(which N3 diffed byte-identical against veins/v11_kappa's copy of the
banked B186 source).  A runtime provenance gate asserts the two function
bodies below appear VERBATIM in that packet file; any drift is a hard stop.

New, additive machinery (this cell): mst_edges / cut_partition -- the
Euclidean MST with edge recording, and the partition sizes obtained by
cutting one edge.  These are exact/deterministic functions of the point
set: no box grid, no placement jitter, no randomness anywhere.
"""
import os

import numpy as np

_PACKET_LIB = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..",
    "B646_wave2_integration", "cc2_packets", "next_queue", "next_queue",
    "n3_fine_grid", "lib_banked.py")

# ---------------------------------------------------------------- verbatim
_METALLIC_SRC = '''def metallic_word(n, m=1):
    sub = "a" * m + "b"; s = {-1: "b", 0: "a"}
    for k in range(1, n + 1):
        s[k] = "".join(sub if c == "a" else "a" for c in s[k - 1])
    return s[n]'''

_SPECTRUM_SRC = '''def spectrum(word, lmb, periodic=True):
    L = len(word); V = np.array([lmb if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex); np.fill_diagonal(H, V); i = np.arange(L - 1)
    H[i, i + 1] = 1; H[i + 1, i] = 1
    if periodic:
        H[0, L - 1] = 1; H[L - 1, 0] = 1
    return np.linalg.eigvals(H)'''


def provenance_gate():
    """HARD STOP unless both function bodies appear verbatim in the packet lib."""
    with open(os.path.abspath(_PACKET_LIB)) as fh:
        src = fh.read()
    assert _METALLIC_SRC in src, "metallic_word drifted from packet lib_banked.py"
    assert _SPECTRUM_SRC in src, "spectrum drifted from packet lib_banked.py"
    return True


exec(_METALLIC_SRC)
exec(_SPECTRUM_SRC)


# ---------------------------------------------------------------- new (additive)
def mst_edges(pts):
    """Euclidean MST of complex points (Prim, O(N^2)); returns the n-1 edges as
    (length, u, v) tuples.  Deterministic given the point multiset (ties broken
    by np.argmin's fixed first-minimum rule; tie configurations are measure-zero
    and none occurred in any run of this cell)."""
    P = np.c_[pts.real, pts.imag]
    n = len(P)
    in_tree = np.zeros(n, bool)
    mind = np.full(n, np.inf)
    parent = np.full(n, -1)
    mind[0] = 0.0
    edges = []
    for _ in range(n):
        u = int(np.argmin(np.where(in_tree, np.inf, mind)))
        if parent[u] >= 0:
            edges.append((float(mind[u]), u, int(parent[u])))
        in_tree[u] = True
        d = np.sqrt(((P - P[u]) ** 2).sum(1))
        upd = (~in_tree) & (d < mind)
        mind[upd] = d[upd]
        parent[upd] = u
    assert len(edges) == n - 1
    return edges


def cut_partition(edges, n, cut_idx):
    """Sizes (n_small, n_large) of the two components of the MST after removing
    edges[cut_idx].  Union-find over the remaining edges; exact integers."""
    root = list(range(n))

    def find(a):
        while root[a] != a:
            root[a] = root[root[a]]
            a = root[a]
        return a

    for i, (_, u, v) in enumerate(edges):
        if i == cut_idx:
            continue
        ru, rv = find(u), find(v)
        if ru != rv:
            root[ru] = rv
    comp = {}
    for a in range(n):
        r = find(a)
        comp[r] = comp.get(r, 0) + 1
    sizes = sorted(comp.values())
    assert len(sizes) == 2 and sum(sizes) == n
    return sizes[0], sizes[1]


def gap_labels(ev, top=5):
    """The cell's core readout.  For the top `top` MST edges (sorted by length,
    descending): (length, n_small, n_small/L).  Also returns e2/e1 (degeneracy
    ratio of the top two edges).  All deterministic; no grid, no RNG."""
    n = len(ev)
    edges = mst_edges(ev)
    order = sorted(range(len(edges)), key=lambda i: -edges[i][0])
    rows = []
    for i in order[:top]:
        ns, _ = cut_partition(edges, n, i)
        rows.append((edges[i][0], ns, ns / n))
    ratio = rows[1][0] / rows[0][0] if len(rows) > 1 else 0.0
    return rows, ratio
