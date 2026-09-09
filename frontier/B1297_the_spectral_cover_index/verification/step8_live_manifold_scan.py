"""PREREG §5(e), the live half: is the index EVER nonzero on a real one-cusped hyperbolic manifold?
Scan the orientable cusped census for one-cusped M with torsion of order >= 3 in H1; V = Sym^2(rho_geo) (x) chi,
chi a torsion character trivial on the cusp with chi^2 != 1 (so V is not self-dual, t0 > 0); numeric ranks (SVD)
from SnapPy's holonomy.  Reports r1 vs t0 and the identities; lists every nonzero index found."""
import os, sys, json, itertools, warnings
warnings.filterwarnings("ignore")
import numpy as np, snappy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
TOL = 1e-7
def nrank(M):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False)
    if s.size == 0: return 0
    return int(np.sum(s > TOL * max(1.0, s[0])))
def nnull(M):
    u, s, vh = np.linalg.svd(M)
    r = int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0
    return vh[r:].conj().T          # columns span the nullspace
def sym2(g):
    p, q = g[0, 0], g[0, 1]; r, s = g[1, 0], g[1, 1]
    # basis X^2, XY, Y^2 with g.X = pX + rY, g.Y = qX + sY  (same convention as d2lib.sym_power)
    return np.array([[p*p, p*q, q*q], [2*p*r, p*s + q*r, 2*q*s], [r*r, r*s, s*s]], dtype=complex)
class NRep:
    def __init__(self, ims): self.im = {(g, 1): M for g, M in ims.items()}; self.dim = next(iter(ims.values())).shape[0]
    def letter(self, g, e):
        if e == -1 and (g, -1) not in self.im: self.im[(g, -1)] = np.linalg.inv(self.im[(g, 1)])
        return self.im[(g, e)]
    def __call__(self, w):
        M = np.eye(self.dim, dtype=complex)
        for g, e in w: M = M @ self.letter(g, e)
        return M
def nfox(rep, word, gens):
    n = rep.dim; D = {g: np.zeros((n, n), dtype=complex) for g in gens}; P = np.eye(n, dtype=complex)
    for g, e in word:
        if e == 1: D[g] += P; P = P @ rep.letter(g, 1)
        else: P = P @ rep.letter(g, -1); D[g] -= P
    return D
def blocks(rows_of_blocks): return np.block(rows_of_blocks)
def data(gens, rels, rep, cusp_words):
    n = rep.dim
    d0 = blocks([[rep.letter(g, 1) - np.eye(n)] for g in gens])
    d1 = blocks([[nfox(rep, R, gens)[g] for g in gens] for R in rels])
    r0, r1 = nrank(d0), nrank(d1)
    a0, a1, a2 = n - r0, n * len(gens) - r1 - r0, n * len(rels) - r1
    Z1 = nnull(d1)
    Res = blocks([[nfox(rep, w, gens)[g] for g in gens] for w in cusp_words])
    m, l = rep(cusp_words[0]), rep(cusp_words[1])
    cd0 = np.vstack([m - np.eye(n), l - np.eye(n)])
    # torus d1 for relator m l m^-1 l^-1 : blocks (dR/dm, dR/dl)
    crep = NRep({"m": m, "l": l}); cd1 = blocks([[nfox(crep, [("m",1),("l",1),("m",-1),("l",-1)], ["m","l"])[g] for g in ["m","l"]]])
    t0 = n - nrank(cd0); t1 = 2*n - nrank(cd1) - nrank(cd0); t2 = n - nrank(cd1)
    rB = nrank(cd0); rr = nrank(np.hstack([Res @ Z1, cd0])) - rB
    return dict(a=(a0, a1, a2), t=(t0, t1, t2), r1=rr)
def index(gens, rels, mats, cusp_words):
    V = NRep(mats); Vd = NRep({g: np.linalg.inv(M).T for g, M in mats.items()})
    A = data(gens, rels, V, cusp_words); B = data(gens, rels, Vd, cusp_words)
    I = (A["a"][0] - B["a"][0]) + B["t"][0] - A["r1"]; F = A["a"][1] - B["a"][1]
    ids = (A["r1"] + B["r1"] == A["t"][1]) and (A["t"][1] == A["t"][0] + B["t"][0]) and (F == (A["a"][0] - B["a"][0]) + A["r1"] - A["t"][0]) \
          and (A["a"][0] - A["a"][1] + A["a"][2] == 0)
    return I, F, A, B, ids

CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 60
found = []; scanned = 0; sectors = 0; log = []
census = snappy.OrientableCuspedCensus
for M in census:
    if M.num_cusps() != 1: continue
    divs = M.homology().elementary_divisors()
    tors = [d for d in divs if d not in (0, 1)]
    if not tors or max(tors) < 3: continue
    G = M.fundamental_group()
    gens = list(G.generators()); rels = [L.word_from_snappy(r) for r in G.relators()]
    mer, lon = [L.word_from_snappy(w) for w in G.peripheral_curves()[0]]
    # abelianization coordinates from the presentation (exact, integer)
    inv, cls, V, D, keep = L.h1_coordinates(gens, rels)
    if sorted(inv) != sorted(divs): continue            # sanity: presentation vs SnapPy
    tor_idx = [i for i, d in enumerate(inv) if d != 0]
    mc, lc = cls(mer), cls(lon)
    # geometric rep (PSL; sign irrelevant for Sym^2)
    try: mats2 = {g: np.array([[complex(G.SL2C(g)[i, j]) for j in range(2)] for i in range(2)]) for g in gens}
    except Exception: continue
    rho = NRep(mats2)
    if max(np.abs(rho(R) - np.sign((rho(R))[0, 0].real or 1) * np.eye(2)).max() for R in rels) > 1e-6:
        if max(min(np.abs(rho(R) - s*np.eye(2)).max() for s in (1, -1)) for R in rels) > 1e-6: continue
    scanned += 1
    # torsion characters trivial on the cusp, chi^2 != 1, one per inverse pair
    ranges = [range(inv[i]) if i in tor_idx else range(1) for i in range(len(inv))]
    seen = set(); results = []
    for expo in itertools.product(*ranges):
        if all(e == 0 for e in expo): continue
        if all((2 * e) % inv[i] == 0 for i, e in enumerate(expo) if i in tor_idx): continue      # chi^2 = 1
        # chi trivial on the cusp
        def chi_val(c): return np.exp(2j * np.pi * sum((e * c[i]) / inv[i] for i, e in enumerate(expo) if i in tor_idx))
        if abs(chi_val(mc) - 1) > 1e-9 or abs(chi_val(lc) - 1) > 1e-9: continue
        inv_expo = tuple((-e) % inv[i] if i in tor_idx else 0 for i, e in enumerate(expo))
        if inv_expo in seen: continue
        seen.add(expo)
        mats = {g: sym2(mats2[g]) * chi_val(cls([(g, 1)])) for g in gens}
        I, F, A, B, ids = index(gens, rels, mats, [mer, lon]); sectors += 1
        results.append((expo, I, F, A["a"], A["t"], A["r1"], B["r1"], ids))
        if I != 0: found.append((M.name(), divs, expo, I, F, A["a"], A["t"], A["r1"], B["r1"], ids))
    if results:
        summary = sorted(set((r[1], r[4][0], r[5], r[6], r[7]) for r in results))
        log.append((M.name(), divs, len(results), summary, M.symmetry_group().order() if True else None))
        print(f"{M.name():8s} H1={divs} sectors={len(results):2d} |Isom|={log[-1][4]:2d}  (I, t0, r1, r1*, ids) set = {summary}")
    if scanned >= CAP: break
print(f"\nscanned {scanned} one-cusped census manifolds with torsion >= 3; {sectors} non-self-dual sectors; NONZERO INDICES: {len(found)}")
for f in found: print("  NONZERO:", f)
json.dump(dict(scanned=scanned, sectors=sectors, found=[list(map(str, f)) for f in found], log=[list(map(str, l)) for l in log]), open("live_scan.json", "w"), indent=1)
