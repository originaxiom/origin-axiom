"""Audit check: h^1 of chi1/chi2 for every ordered pair of characters used by nonor_index.py (its own library, unchanged),
and a cusp sanity check (m, x parabolic, m x m^-1 = x^-1) on the holonomy."""
import sys, itertools, snappy, numpy as np
from collections import Counter
SRC = open(sys.argv[1]).read()
NS = {}; exec(SRC.split("M0 = snappy.Manifold('m000')")[0], NS)
p = NS['p']
M0 = snappy.Manifold('m000')
for name, N, m in (('m000', M0, 'a'), ('N3', M0.covers(3, cover_type='cyclic')[0], 'bAcb')):
    S = NS['setup'](N, m); gens, rels = S['gens'], S['rels']
    chars = NS['characters'](S)
    h1s = Counter(); nonsplit = 0
    for c1, c2 in itertools.product(chars, repeat=2):
        lam = {g: [[c1[g] * pow(c2[g], p - 2, p) % p]] for g in gens}
        h1 = NS['coh'](lam, gens, rels, 1)['a1']
        exts = NS['extensions'](S, c1, c2)
        h1s[h1] += 1; nonsplit += len(exts)
        assert len(exts) == h1, (h1, len(exts))
    print(f"{name}: {len(chars)} characters; h1(chi1/chi2) over ordered pairs: {dict(sorted(h1s.items()))}; extensions built {nonsplit}")
    # cusp sanity on the holonomy (PSL(2,C) via SnapPy's O(3,1) -> use SL2 of the orientation cover is awkward; use O31 matrices)
    G = N.fundamental_group(); x, y = G.peripheral_curves()[0]
    def O(w): 
        M = np.eye(4)
        for ch in w: M = M @ np.array(G.O31(ch), dtype=float) if False else M @ np.array([[float(v) for v in row] for row in G.O31(ch)])
        return M
    mm, xx = O(m), O(x); mi = np.linalg.inv(mm)
    rel = mm @ xx @ mi @ xx
    def parab(A): return abs(np.trace(A) - 4) < 1e-6   # parabolic in O(3,1): trace 4 for orientation-preserving parabolic
    print(f"   m = {m}, x = {x}, y = {y}: |m x m^-1 x - I| = {np.abs(rel - np.eye(4)).max():.2e}; trace(x) = {np.trace(xx):.6f}; "
          f"trace(m^2) = {np.trace(mm @ mm):.6f}; det m = {np.linalg.det(mm):+.3f}")
    # is y in <m, x>?  test y == m^2 or y == m^2 x^k for small k, or y == x^k m^2
    yy = O(y); found = []
    for k in range(-4, 5):
        for e in (2, -2):
            Mk = np.linalg.matrix_power(mm, e) @ np.linalg.matrix_power(xx, k) if k >= 0 else np.linalg.matrix_power(mm, e) @ np.linalg.matrix_power(np.linalg.inv(xx), -k)
            if np.abs(Mk - yy).max() < 1e-6: found.append((e, k))
    print(f"   SnapPy longitude y as m^e x^k: {found}")
