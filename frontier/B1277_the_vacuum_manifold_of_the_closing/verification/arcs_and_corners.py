#!/usr/bin/env python3
"""THE ARCS AND THE CORNERS (L204 re-opened on the owner's challenge): do the two fixed arcs of the object's
inversion, which end at the four corners of the cusp torus (the pillowcase corners), make chi(d+M) != 0?

Setting (Pantev-Wijnholt): for a Cartan-valued Higgs 1-form phi on the cusped object, the net number of 4d chiral
zero modes of a charge-q sector is chi(M, d-M) = -chi(d-M) (torus boundary), where d-M (d+M) is the part of the
boundary torus where the radial component g = phi(d_r) of q.phi is negative (positive).  The partition of the torus
is decided by the sign pattern of g at large cusp height r, i.e. by the slowest-decaying Fourier mode of g that the
object's symmetries allow.

(a) The eight isometries of m004 (D4) as AFFINE maps of the cusp torus.  SnapPy gives their linear parts (all
    diag(+-1, +-1) in the (meridian, longitude) basis).  The horoball pattern (centres gamma(infinity) and sizes
    1/|c|^2 of the holonomy elements gamma, enumerated as words) has SIXTEEN affine symmetries; the genuine eight are
    found by testing which candidates N normalize the holonomy group: N g N^-1 in Gamma for the generators, decided by
    the horoball dictionary (h in Gamma iff h(infinity) is a pattern centre reached by a word w with (T_m w)^-1 h a
    lattice translation).  From the eight: the corners (the four fixed points of each inversion), which mu-reversing
    isometries are reflections and which glides, and the kernel translation T.
(b) The parity eps(sigma) of the b_1 class (the theta-odd abelian Higgs field, dual to the meridian) under each
    isometry: eps = the (mu, mu) entry of the cusp map.  The radial component satisfies g o sigma = eps(sigma) g.
(c) The allowed Fourier modes: c_{Ak} = eps e^{-2 pi i (Ak).b} c_k for every isometry (A, b); the lowest-decay allowed
    orbit; its sign pattern; the Euler characteristic and components of {g > 0} on a fine grid.
    chi(d+M) = chi({g > 0}); by the inversion symmetry chi(d+M) = chi(d-M).
"""
from __future__ import annotations
import sys, math, cmath, itertools, collections
import numpy as np

try:
    import snappy
except ImportError:
    print("snappy not available"); sys.exit(2)


def main():
    M = snappy.Manifold('m004')
    Gp = M.fundamental_group()
    gens = Gp.generators()
    assert gens == ['a', 'b']

    def mat(w):
        m = Gp.SL2C(w)
        return np.array([[complex(m[0, 0]), complex(m[0, 1])], [complex(m[1, 0]), complex(m[1, 1])]])
    mu_w, lam_w = Gp.peripheral_curves()[0]
    Mu0 = mat(mu_w)
    # send the parabolic fixed point of the cusp to infinity
    z0 = (Mu0[0, 0] - Mu0[1, 1]) / (2 * Mu0[1, 0])
    S = np.array([[0, -1], [1, -z0]], dtype=complex)                      # z -> -1/(z - z0), det 1
    Si = np.linalg.inv(S)
    Mu1 = S @ Mu0 @ Si
    Lam1 = S @ mat(lam_w) @ Si
    assert abs(Mu1[1, 0]) < 1e-9 and abs(Lam1[1, 0]) < 1e-9
    t_lam1 = Lam1[0, 1] / Lam1[0, 0]
    # rotate so that the longitude translation is real and positive
    delta = abs(t_lam1) / t_lam1
    D = np.array([[cmath.sqrt(delta), 0], [0, 1 / cmath.sqrt(delta)]])
    Di = np.linalg.inv(D)
    conj2 = lambda X: D @ (S @ X @ Si) @ Di
    Mu, Lam = conj2(mat(mu_w)), conj2(mat(lam_w))
    t_mu, t_lam = Mu[0, 1] / Mu[0, 0], Lam[0, 1] / Lam[0, 0]
    assert abs(t_lam.imag) < 1e-9 and abs(t_mu.real) < 1e-9, (t_mu, t_lam)
    t_lam = t_lam.real
    print(f"  cusp at infinity: meridian translation t_mu = {t_mu:.6f}, longitude t_lam = {t_lam:.6f}; |t_lam|/|t_mu| = {t_lam / abs(t_mu):.6f} = 2 sqrt 3: {abs(t_lam / abs(t_mu) - 2 * math.sqrt(3)) < 1e-6}")
    A, B = conj2(mat('a')), conj2(mat('b'))
    mats = {'a': A, 'b': B, 'A': np.linalg.inv(A), 'B': np.linalg.inv(B)}

    def reduce(z):
        return (z.real / t_lam) % 1.0, (z.imag / t_mu.imag) % 1.0
    # the horoball dictionary from words up to length L
    L = 9
    dictionary = {}
    frontier = [('', np.eye(2, dtype=complex))]
    for length in range(1, L + 1):
        nxt = []
        for w, X in frontier:
            for g in 'aAbB':
                if w and w[-1] == g.swapcase():
                    continue
                Y = X @ mats[g]
                nxt.append((w + g, Y))
                c = Y[1, 0]
                if abs(c) > 1e-9:
                    x, y = reduce(Y[0, 0] / c)
                    size = 1.0 / abs(c) ** 2
                    key = (round(x, 4) % 1.0, round(y, 4) % 1.0, round(size, 5))
                    if key not in dictionary:
                        dictionary[key] = Y
        frontier = nxt
    sizes = sorted({k[2] for k in dictionary}, reverse=True)
    pattern = collections.defaultdict(list)
    for (x, y, s) in dictionary:
        pattern[s].append((x, y))
    print(f"  horoball pattern from words up to length {L}: {len(dictionary)} balls, {len(sizes)} sizes; largest classes {[(s, len(pattern[s])) for s in sizes[:4]]}")
    lins = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    def close(p, q):
        return abs((p[0] - q[0] + 0.5) % 1.0 - 0.5) < 2e-3 and abs((p[1] - q[1] + 0.5) % 1.0 - 0.5) < 2e-3

    def preserves(Al, b):
        for s in sizes[:3]:                     # the three largest classes are complete at this word length
            pts = pattern[s]
            for (x, y) in pts:
                img = ((Al[1] * x + b[0]) % 1.0, (Al[0] * y + b[1]) % 1.0)
                if not any(close(img, q) for q in pts):
                    return False
        return True
    candidates = []
    for Al in lins:
        pts = pattern[sizes[0]]
        p0 = pts[0]
        found = set()
        for q in pts:
            b = ((q[0] - Al[1] * p0[0]) % 1.0, (q[1] - Al[0] * p0[1]) % 1.0)
            if preserves(Al, b):
                found.add((round(b[0], 3) % 1.0, round(b[1], 3) % 1.0))
        for b in sorted(found):
            candidates.append((Al, b))
    print(f"  affine symmetries of the horoball pattern: {len(candidates)} (the pattern has more symmetry than the manifold)")

    def N_matrix(Al, b):
        bz = b[0] * t_lam + b[1] * t_mu
        s = Al[1]
        anti = (Al[0] != Al[1])
        Nm = np.array([[s, bz], [0, 1]], dtype=complex)
        Nm = Nm / cmath.sqrt(np.linalg.det(Nm))
        return Nm, anti

    def in_gamma(h, depth=0):
        c = h[1, 0]
        if abs(c) < 1e-9:
            t = h[0, 1] / h[0, 0]
            m1, m2 = t.real / t_lam, t.imag / t_mu.imag
            return (abs(m1 - round(m1)) < 1e-6 and abs(m2 - round(m2)) < 1e-6
                    and abs(abs(h[0, 0]) - 1) < 1e-6 and abs(h[0, 0].imag) < 1e-6)
        z = h[0, 0] / c
        x, y = reduce(z)
        size = 1.0 / abs(c) ** 2
        key = None
        for k in dictionary:
            if abs(k[2] - size) < 1e-4 * size and close((k[0], k[1]), (x, y)):
                key = k; break
        if key is None or depth > 2:
            return None
        w = dictionary[key]
        zw = w[0, 0] / w[1, 0]
        d = z - zw
        m1, m2 = round(d.real / t_lam), round(d.imag / t_mu.imag)
        Tm = np.array([[1, m1 * t_lam + m2 * t_mu], [0, 1]], dtype=complex)
        p = np.linalg.inv(Tm @ w) @ h
        return in_gamma(p, depth + 1)
    genuine = []
    for (Al, b) in candidates:
        Nm, anti = N_matrix(Al, b)
        Ni = np.linalg.inv(Nm)
        ok = True
        for g in ('a', 'b'):
            X = mats[g]
            h = Nm @ (X.conj() if anti else X) @ Ni
            r = in_gamma(h)
            if r is None:
                ok = None; break
            ok = ok and r
        genuine.append(((Al, b), ok))
    print("  normalization test N g N^-1 in Gamma for both generators (None = undecided by the dictionary):")
    for (Al, b), ok in genuine:
        print(f"     (s_mu, s_lam) = {Al}, b = {b}: {ok}")
    isos = [(Al, b) for (Al, b), ok in genuine if ok]
    assert len(isos) == 8, len(isos)
    affine = collections.defaultdict(list)
    for Al, b in isos:
        affine[Al].append(b)
    T = [b for b in affine[(1, 1)] if b != (0.0, 0.0)]
    assert len(T) == 1
    T = T[0]
    print(f"  the eight isometries as affine maps (x along lam, y along mu, mod 1): {dict(affine)}")
    print(f"  the kernel translation T (cusp map trivial; the period-2 symmetry): {T}")
    inv = affine[(-1, -1)]
    all_corners = {}
    for cc in inv:
        corners = sorted({((cc[0] / 2 + i / 2) % 1.0, (cc[1] / 2 + j / 2) % 1.0) for i in range(2) for j in range(2)})
        all_corners[cc] = corners
        print(f"  inversion b = {cc}: its four fixed points (the corners where its two fixed arcs meet the torus): {corners}")
    for Al in ((-1, 1), (1, -1)):
        for b in affine[Al]:
            if Al == (-1, 1):
                kind = "REFLECTION (mu reversed) with fixed circles y = b_y/2, b_y/2 + 1/2 along lam" if abs(b[0]) < 1e-6 else f"GLIDE along lam by {b[0]} (no fixed points; order {2 if abs(2 * b[0] - round(2 * b[0])) < 1e-6 else 4})"
            else:
                kind = "REFLECTION (lam reversed) with fixed circles x = b_x/2, b_x/2 + 1/2 along mu" if abs(b[1]) < 1e-6 else f"GLIDE along mu by {b[1]} (no fixed points; order {2 if abs(2 * b[1] - round(2 * b[1])) < 1e-6 else 4})"
            print(f"     (s_mu, s_lam) = {Al}, b = {b}: {kind}")
    # (c) the allowed modes of g, g o sigma = eps(sigma) g, eps = s_mu (the b_1 class is dual to the meridian)
    eps = lambda Al: Al[0]
    modes = [(k, l) for k in range(-6, 7) for l in range(-3, 4) if (k, l) != (0, 0)]
    rate = lambda kl: math.sqrt((kl[0] / t_lam) ** 2 + (kl[1] / abs(t_mu)) ** 2)
    orbits, seenm = [], set()
    for kl in sorted(modes, key=rate):
        if kl in seenm:
            continue
        orb = sorted({(s2 * kl[0], s1 * kl[1]) for (s1, s2) in lins})
        seenm |= set(orb)
        orbits.append(orb)
    allowed = []
    for orb in orbits:
        idx = {kl: i for i, kl in enumerate(orb)}
        rows = []
        for (Al, b) in isos:
            for kl in orb:
                Akl = (Al[1] * kl[0], Al[0] * kl[1])
                row = np.zeros(len(orb), dtype=complex)
                phase = eps(Al) * cmath.exp(-2j * math.pi * (Akl[0] * b[0] + Akl[1] * b[1]))
                row[idx[Akl]] += 1.0
                row[idx[kl]] -= phase
                rows.append(row)
        Mc = np.array(rows)
        u, s, vh = np.linalg.svd(Mc)
        rank = int(np.sum(s > 1e-9))
        null = vh[rank:].conj().T
        allowed.append((orb, len(orb) - rank, null))
    print("  Fourier orbits of the radial component by decay rate (k along lam, l along mu), and the dimension of the symmetry-allowed coefficient space:")
    lead = None
    for orb, dim, null in allowed[:8]:
        print(f"     {orb}: decay {rate(orb[0]):.4f}, allowed dim {dim}")
        if dim > 0 and lead is None:
            lead = (orb, dim, null)
    orb, dim, null = lead
    print(f"  the leading allowed mode orbit: {orb} (decay {rate(orb[0]):.4f}), allowed dimension {dim}")
    rng = np.random.default_rng(7)
    coef = null @ (rng.normal(size=null.shape[1]) + 1j * rng.normal(size=null.shape[1]))
    c = {kl: coef[i] for i, kl in enumerate(orb)}
    cr = {kl: 0.5 * (c[kl] + np.conj(c.get((-kl[0], -kl[1]), 0))) for kl in orb}
    if max(abs(v) for v in cr.values()) < 1e-9:
        cr = {kl: 0.5j * (c[kl] - np.conj(c.get((-kl[0], -kl[1]), 0))) for kl in orb}
    N = 480
    xs = (np.arange(N) + 0.5) / N
    X, Y = np.meshgrid(xs, xs, indexing='ij')
    g = np.zeros_like(X)
    for (k, l), cv in cr.items():
        g += (cv * np.exp(2j * math.pi * (k * X + l * Y))).real

    def sample(fun, x, y):
        return fun[(np.round(x * N - 0.5).astype(int)) % N, (np.round(y * N - 0.5).astype(int)) % N]
    errs = []
    for (Al, b) in isos:
        Xs = (Al[1] * X + b[0]) % 1.0; Ys = (Al[0] * Y + b[1]) % 1.0
        errs.append(float(np.max(np.abs(sample(g, Xs, Ys) - eps(Al) * g))) / float(np.max(np.abs(g))))
    terms = ', '.join(f"({k},{l}): {v.real:+.3f}{v.imag:+.3f}i" for (k, l), v in cr.items() if abs(v) > 1e-9)
    print(f"  the leading mode g(x, y) = sum c e^(2 pi i (k x + l y)) with {terms}; symmetry residuals (relative) max {max(errs):.1e}")

    def components(mask):
        lab = -np.ones(mask.shape, dtype=int); n = 0
        for i in range(N):
            for j in range(N):
                if mask[i, j] and lab[i, j] < 0:
                    st = [(i, j)]; lab[i, j] = n
                    while st:
                        a_, b_ = st.pop()
                        for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            ii, jj = (a_ + da) % N, (b_ + db) % N
                            if mask[ii, jj] and lab[ii, jj] < 0:
                                lab[ii, jj] = n; st.append((ii, jj))
                    n += 1
        return n

    def euler(mask):
        F = int(mask.sum())
        Vc = int((mask | np.roll(mask, 1, 0) | np.roll(mask, 1, 1) | np.roll(np.roll(mask, 1, 0), 1, 1)).sum())
        Ec = int((mask | np.roll(mask, 1, 0)).sum() + (mask | np.roll(mask, 1, 1)).sum())
        return Vc - Ec + F
    pos, neg = g > 0, g < 0
    npos, nneg = components(pos), components(neg)
    chi_pos, chi_neg = euler(pos), euler(neg)
    print(f"  {{g > 0}}: {npos} component(s), Euler characteristic {chi_pos}; {{g < 0}}: {nneg} component(s), Euler characteristic {chi_neg}")
    gx = np.roll(g, -1, 0) - np.roll(g, 1, 0); gy = np.roll(g, -1, 1) - np.roll(g, 1, 1)
    gmax = float(np.max(np.hypot(gx, gy)))
    for cc, corners in all_corners.items():
        gval = [float(abs(sample(g, np.array([cx]), np.array([cy]))[0])) / float(np.max(np.abs(g))) for (cx, cy) in corners]
        gr = [float(math.hypot(sample(gx, np.array([cx]), np.array([cy]))[0], sample(gy, np.array([cx]), np.array([cy]))[0])) / gmax for (cx, cy) in corners]
        print(f"  at the corners of the inversion b = {cc}: |g| (relative) {[f'{v:.3f}' for v in gval]}, |grad g| (relative) {[f'{v:.3f}' for v in gr]}")
    verdict = ("chi(d+M) = 0: the partition of the cusp torus is annular; the arcs' corners lie on the zero set and do not make discs"
               if chi_pos == 0 else f"chi(d+M) = {chi_pos} != 0: the partition has discs")
    print(f"  => {verdict}")
    return dict(T=T, lead=orb, dim=dim, chi_pos=chi_pos, chi_neg=chi_neg, npos=npos, nneg=nneg, affine=dict(affine))


if __name__ == "__main__":
    print("=== the arcs and the corners: the object's eight isometries on its cusp torus, the b_1 Higgs field's allowed modes at the cusp, and chi(d+M) ===")
    out = main()
    ok = out['chi_pos'] == out['chi_neg'] and len(out['affine'][(-1, -1)]) == 2
    print("\nSELFTEST:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)
