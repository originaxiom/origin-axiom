"""R71 (part 1) -- the seats on the cusp, reconciled on one bench.

(a) The eight isometries of m004 on the cusp torus, built from R62's exact data (iota = translation by tau/2,
    sigma = -z, mirror = conj(z) + 1/2 + tau/4), written in the SM seat's coordinates (x along lambda, y along mu)
    and compared with the B1277-addendum table and with B1279's (mu, lambda) table.
(b) B1291's parity check on the same maps: |Fix| = |det(A - I)|, only the two inversions have fixed points, 4 each.
(c) The SM seat's Fourier-orbit table for a theta-odd (b_1-class) field on the cusp: allowed dimension per orbit,
    recomputed from the eight maps and their parities epsilon(sigma) = the mu-sign.
(d) The region-swap theorem: for ANY field g with g o sigma = -g and a transverse zero set, chi({g>0}) = chi({g<0}) = 0.
    Checked on a grid for random allowed fields; the SM seat's caveat (the (+-2,0) coefficient vanishing) is shown to
    have an ill-defined chi only for the exact product mode (non-transverse zero set with 8 crossings: +4 for the open
    rectangles, -4 for their closures) and chi = 0 again as soon as any allowed subleading mode is present.  So chi(d+M) = 0 for a theta-odd field needs no assumption about which mode leads.
(e) The corners: every theta-odd allowed field vanishes at the eight fixed points of the two inversions.

Coordinates: R62's (u, v) with u along the meridian (real direction, length 1) and v along tau (length 2 sqrt 3);
the SM seat's (x, y) = (v, u).  All maps are z -> +-z + t or +-conj(z) + t on C / (Z + Z tau).
"""
import itertools, random
from fractions import Fraction as Fr
import numpy as np

# ---------- (a) the eight maps in (u, v): (u, v) -> (su*u + a, sv*v + b)
H = Fr(1, 2); Q = Fr(1, 4)
IOTA = (1, 1, Fr(0), H)          # translation by tau/2                     (R62: beta = 2 = tau/2 -> (0, 1/2))
SIGMA = (-1, -1, Fr(0), Fr(0))   # z -> -z
MIRROR = (1, -1, H, Q)           # z -> conj(z) + 1/2 + tau/4               (R62: E = [[1, 1/2 + sqrt3 i/2],[0,1]])
def compose(f, g):               # f o g
    su, sv, a, b = f; tu, tv, c, d = g
    return (su*tu, sv*tv, (su*c + a) % 1, (sv*d + b) % 1)
ID = (1, 1, Fr(0), Fr(0))
G = {ID}
frontier = [ID]
while frontier:
    new = []
    for f in frontier:
        for gen in (IOTA, SIGMA, MIRROR):
            h = compose(gen, f)
            if h not in G: G.add(h); new.append(h)
    frontier = new
G = sorted(G)
assert len(G) == 8, len(G)
def name(f):
    su, sv, a, b = f
    return {(1,1,Fr(0),Fr(0)):'id', IOTA:'iota (=T)', SIGMA:'sigma (=theta)', compose(SIGMA, IOTA):'sigma.iota (=theta T)',
            MIRROR:'mirror m', compose(MIRROR, IOTA):'m.iota', compose(MIRROR, SIGMA):'m.sigma', compose(MIRROR, compose(SIGMA, IOTA)):'m.sigma.iota'}[f]
def order(f):
    g, n = f, 1
    while g != ID: g = compose(f, g); n += 1
    return n
def fixed_points(f):
    su, sv, a, b = f
    # solve su*u + a = u, sv*v + b = v mod 1
    def sols(s, t):
        if s == 1: return [Fr(0)] if t == 0 else []          # translation: whole circle (count as 'inf') or none
        return sorted({((t/2) + Fr(i, 2)) % 1 for i in range(2)})  # -w + t = w  ->  2w = t
    if su == 1 and a != 0 or sv == 1 and b != 0: return []
    if su == 1 or sv == 1: return 'circles'
    return [(p, q) for p in sols(su, a) for q in sols(sv, b)]
print("(a) the eight isometries on the cusp torus, R62's data, in the SM seat's coordinates x = v (along lambda), y = u (along mu)")
print(f"{'map':16} {'(mu,lambda) signs':18} {'transl (x,y)':16} {'transl (mu,lambda)':18} {'orient':7} {'order':5} {'|Fix|':5} fixed points (x,y)")
table = {}
for f in G:
    su, sv, a, b = f
    sg = ('+' if su == 1 else '-', '+' if sv == 1 else '-')
    orient = '+' if su*sv == 1 else '-'
    fp = fixed_points(f)
    nfix = len(fp) if isinstance(fp, list) else fp
    detAI = abs((su - 1)*(sv - 1))
    assert (isinstance(fp, list) and len(fp) == detAI) or detAI == 0
    table.setdefault(sg, []).append((b, a))
    print(f"{name(f):16} {str(sg):18} {str((b, a)):16} {str((a, b)):18} {orient:7} {order(f):<5} {str(nfix):5} {[(q, p) for p, q in fp] if isinstance(fp, list) else ''}")
# the SM seat's table (B1277 addendum, translations in (x, y)):
SM = {('+','+'): {(Fr(0),Fr(0)), (H,Fr(0))}, ('-','+'): {(Q,H), (Fr(3,4),H)}, ('+','-'): {(Q,H), (Fr(3,4),H)}, ('-','-'): {(Fr(0),Fr(0)), (H,Fr(0))}}
ok = all(set(table[k]) == SM[k] for k in SM)
print(f"    matches the B1277-addendum table (all four sign classes, both translation parts each): {ok}")
# B1279's table lists translations as (mu, lambda) = (y, x): T (0,1/2); thetaT (0,1/2); rotoreflections (-,+) (1/2,1/4),(1/2,3/4); glides (+,-) same
B1279 = {('+','+'): {(Fr(0),Fr(0)), (Fr(0),H)}, ('-','+'): {(H,Q), (H,Fr(3,4))}, ('+','-'): {(H,Q), (H,Fr(3,4))}, ('-','-'): {(Fr(0),Fr(0)), (Fr(0),H)}}
ok2 = all({(y, x) for x, y in table[k]} == B1279[k] for k in B1279)
print(f"    matches B1279's (mu, lambda) table: {ok2}")
assert ok and ok2
# theta's corners and theta T's corners
corners = {}
for f in G:
    fp = fixed_points(f)
    if isinstance(fp, list) and fp: corners[name(f)] = [(q, p) for p, q in fp]
print(f"    corners: {corners}")
assert corners['sigma (=theta)'] == [(Fr(0),Fr(0)), (Fr(0),H), (H,Fr(0)), (H,H)] or set(corners['sigma (=theta)']) == {(Fr(0),Fr(0)), (Fr(0),H), (H,Fr(0)), (H,H)}
assert set(corners['sigma.iota (=theta T)']) == {(Q,Fr(0)), (Q,H), (Fr(3,4),Fr(0)), (Fr(3,4),H)}
print("    theta's corners = R61's four 2-torsion points 0, 1/2, tau/2, (1+tau)/2 = the endpoints of Fix(theta)'s two arcs;")
print("    theta T's corners = R62's quarter points tau/4 (+1/2), 3tau/4 (+1/2).")

# ---------- (b) B1291 on these maps
print("\n(b) B1291's parity theorem on the same maps: |Fix on the cusp| = |det(A - I)|:")
fixcounts = sorted(abs((f[0]-1)*(f[1]-1)) for f in G)
print(f"    |Fix| over the eight = {fixcounts}   (B1291: 'only 2 of 8 have fixed points, 4 each; no orientation-reversing one has any')")
assert fixcounts == [0]*6 + [4, 4]
assert all(abs((f[0]-1)*(f[1]-1)) == 0 for f in G if f[0]*f[1] == -1)
print("    4 = 2 arcs x 2 ends: R61's two arcs are exactly what the parity theorem counts (even, one cusp).")

# ---------- (c) the theta-odd field's Fourier orbits
# b_1 class dual to the meridian: parity epsilon(f) = mu-sign = su.  g(u,v) = sum c_{l,k} e^{2 pi i (l u + k v)}, l along mu, k along lambda.
# (g o f)(u,v) = g(su u + a, sv v + b) = sum c_{l,k} e^{2 pi i (l a + k b)} e^{2 pi i (l su u + k sv v)}  -> coefficient of (l su, k sv) is c_{l,k} e^{2 pi i (l a + k b)}
print("\n(c) allowed Fourier orbits of a theta-odd field (parity = mu-sign), the SM seat's table recomputed:")
def orbit(k, l):
    return sorted({(l*f[0], k*f[1]) for f in G} | {(-l*f[0], -k*f[1]) for f in G})
def allowed_dim(k, l):
    modes = orbit(k, l); idx = {m: i for i, m in enumerate(modes)}; n = len(modes)
    rows = []
    for f in G:
        su, sv, a, b = f; eps = su
        M = np.zeros((n, n), dtype=complex)
        for (ll, kk) in modes:
            ph = np.exp(2j*np.pi*(ll*float(a) + kk*float(b)))
            M[idx[(ll*su, kk*sv)], idx[(ll, kk)]] += ph
        rows.append(M - eps*np.eye(n))
    A = np.vstack(rows)
    # complex nullspace, then the real structure c_{-m} = conj(c_m): real dimension = dim of the real subspace
    u_, s, vh = np.linalg.svd(A); null = vh[np.sum(s > 1e-9):].conj().T      # n x d
    d = null.shape[1]
    if d == 0: return 0
    # reality: R c = conj(c) where R swaps m <-> -m.  Real subspace of the nullspace N: {c in N : R c = conj c}.  Its real dim = dim_R of fixed set of the antilinear map c -> R conj(c) on N (an antilinear involution) = d.
    # (the map preserves N because the constraints are real: A R conj(c) = conj(A' c) ... check numerically)
    Rm = np.zeros((n, n))
    for (ll, kk) in modes: Rm[idx[(-ll, -kk)], idx[(ll, kk)]] = 1
    test = null.conj().T @ (Rm @ null.conj())   # should be unitary-ish (map preserves N)
    assert np.allclose(np.abs(np.linalg.eigvals(test)), 1, atol=1e-8)
    return d
decay = lambda k, l: (l**2 + (k/(2*np.sqrt(3)))**2)**0.5
print(f"    {'orbit (k along lambda, l along mu)':36} {'decay':7} allowed dim")
seatdims = {}
for (k, l) in [(1,0),(2,0),(3,0),(0,1),(1,1),(2,1),(4,0),(6,0),(2,2),(4,1),(0,2)]:
    d = allowed_dim(k, l); seatdims[(k, l)] = d
    print(f"    ({k:+},{l:+}) {str(sorted(set((kk, ll) for ll, kk in orbit(k, l)))):26} {decay(k, l):.3f}   {d}")
assert [seatdims[m] for m in [(1,0),(2,0),(3,0),(0,1),(1,1),(2,1)]] == [0, 1, 0, 0, 0, 1], seatdims
print("    (SM seat: 0, 1, 0, 0, 0, 1 for these six orbits -- reproduced.)  Note (+-4,0) is killed too: the pure longitude modes are k = 2 mod 4.")

# ---------- (d) the region-swap theorem on a grid
def allowed_basis(kmax, lmax):
    """real basis functions for the allowed theta-odd space, as callables on (u, v) arrays"""
    basis = []
    seen = set()
    for k in range(0, kmax+1):
        for l in range(-lmax, lmax+1):
            key = tuple(orbit(k, l))
            if key in seen or (k, l) == (0, 0): continue
            seen.add(key)
            modes = orbit(k, l); idx = {m: i for i, m in enumerate(modes)}; n = len(modes)
            rows = []
            for f in G:
                su, sv, a, b = f; eps = su
                M = np.zeros((n, n), dtype=complex)
                for (ll, kk) in modes:
                    M[idx[(ll*su, kk*sv)], idx[(ll, kk)]] += np.exp(2j*np.pi*(ll*float(a) + kk*float(b)))
                rows.append(M - eps*np.eye(n))
            A = np.vstack(rows); u_, s, vh = np.linalg.svd(A); null = vh[np.sum(s > 1e-9):].conj().T
            for j in range(null.shape[1]):
                c = null[:, j]
                Rm = np.zeros((n, n))
                for (ll, kk) in modes: Rm[idx[(-ll, -kk)], idx[(ll, kk)]] = 1
                for cc in (c + Rm @ c.conj(), 1j*(c - Rm @ c.conj())):   # real combinations
                    if np.linalg.norm(cc) < 1e-9: continue
                    def fn(U, V, cc=cc, modes=modes):
                        out = np.zeros_like(U, dtype=complex)
                        for (ll, kk), coef in zip(modes, cc): out += coef*np.exp(2j*np.pi*(ll*U + kk*V))
                        assert np.abs(out.imag).max() < 1e-9*max(1, np.abs(out).max())
                        return out.real
                    basis.append(((k, abs(l)), fn))
    return basis
def chi_positive(gvals):
    """Euler characteristic of the closed cubical region = union of grid cells (periodic torus grid) where g > 0 at the cell centre."""
    P = gvals > 0
    F = P.sum()
    # vertices: (i, j) corners; a vertex belongs to the region if any of its 4 incident cells is positive
    Vp = P | np.roll(P, 1, 0) | np.roll(P, 1, 1) | np.roll(np.roll(P, 1, 0), 1, 1)
    # horizontal edges between vertex (i,j) and (i,j+1): belongs if cell (i,j) or cell (i-1,j) positive; vertical: cell (i,j) or cell (i,j-1)
    Eh = P | np.roll(P, 1, 0); Ev = P | np.roll(P, 1, 1)
    return int(Vp.sum()) - int(Eh.sum() + Ev.sum()) + int(F)
N = 480
uu, vv = np.meshgrid((np.arange(N) + 0.5)/N, (np.arange(N) + 0.5)/N, indexing='ij')
basis = allowed_basis(6, 3)
print(f"\n(d) region-swap theorem on a {N}x{N} grid; allowed real basis functions up to (k,l) <= (6,3): {len(basis)} (orbits: {sorted(set(b[0] for b in basis))})")
sig = (SIGMA[0], SIGMA[1], float(SIGMA[2]), float(SIGMA[3]))
random.seed(1)
def sample(coefs):
    g = np.zeros_like(uu)
    for c, (_, fn) in zip(coefs, basis): g += c*fn(uu, vv)
    return g
results = []
for trial in range(6):
    coefs = [random.gauss(0, 1)/(1 + decay(*b[0]))**3 for b in basis]
    g = sample(coefs)
    # parity check: g o sigma = -g  (sigma: (u,v) -> (-u,-v); on the cell-centre grid: index i -> N-1-i)
    assert np.allclose(g[::-1, ::-1], -g, atol=1e-9)
    cp, cm = chi_positive(g), chi_positive(-g)
    z = int((np.sign(g) != np.sign(np.roll(g, 1, 0))).sum() + (np.sign(g) != np.sign(np.roll(g, 1, 1))).sum())
    results.append((cp, cm))
    print(f"    random allowed theta-odd field #{trial}: chi(g>0) = {cp}, chi(g<0) = {cm}, sign-change edges {z}")
assert all(r == (0, 0) for r in results)
print("    chi(d+M) = chi(d-M) = 0 for every sample: sigma swaps the two regions (g o sigma = -g), so their chi's are equal,")
print("    and they sum to chi(T^2) - chi(zero set) = 0 - 0 whenever the zero set is a closed 1-manifold.  No leading-mode assumption enters.")
# the SM seat's caveat: kill the (2,0) coefficient
i20 = [i for i, b in enumerate(basis) if b[0] == (2, 0)]; i21 = [i for i, b in enumerate(basis) if b[0] == (2, 1)]
coefs = [0.0]*len(basis)
for i in i21: coefs[i] = 1.0
g = sample(coefs); print(f"    caveat, exact product mode (the (+-2,+-1) orbit alone, c_(2,0) = 0): chi(closed g>=0 region) = {chi_positive(g)}, chi(closed g<=0) = {chi_positive(-g)}")
print("      the zero set has 8 crossings; the four open rectangles give +4 (the SM seat's +-4), their closures glued at the 8 crossings give -4:")
print("      with a non-transverse zero set d+M is not a surface and chi(d+M) is not defined -- the value is not 'nonzero', it is absent.")
assert chi_positive(g) == -4
for i, b in enumerate(basis):
    if b[0] not in ((2, 0), (2, 1)): coefs[i] = 0.05*random.gauss(0, 1)
g = sample(coefs); print(f"    caveat, same with any small allowed subleading modes (c_(2,0) still 0): chi(g>0) = {chi_positive(g)}, chi(g<0) = {chi_positive(-g)}  <- crossings resolved, back to 0")
assert chi_positive(g) == 0 and chi_positive(-g) == 0
# and the leading mode alone
coefs = [0.0]*len(basis)
for i in i20: coefs[i] = 1.0
g = sample(coefs); print(f"    the SM seat's leading mode sin(4 pi x) alone: chi(g>0) = {chi_positive(g)}, chi(g<0) = {chi_positive(-g)} (two annuli each)")
assert chi_positive(g) == 0

# ---------- (e) the corners lie on the zero set of every allowed field
print("\n(e) the eight corners on the zero set of every allowed theta-odd field:")
allc = corners['sigma (=theta)'] + corners['sigma.iota (=theta T)']
mx = 0.0
for trial in range(5):
    coefs = [random.gauss(0, 1) for b in basis]
    for (x, y) in allc:
        val = sum(c*fn(np.array([[float(y)]]), np.array([[float(x)]]))[0, 0] for c, (_, fn) in zip(coefs, basis))
        mx = max(mx, abs(val))
print(f"    max |g(corner)| over 5 random allowed fields and 8 corners: {mx:.1e}")
assert mx < 1e-9
print("\nSELFTEST: PASS")
