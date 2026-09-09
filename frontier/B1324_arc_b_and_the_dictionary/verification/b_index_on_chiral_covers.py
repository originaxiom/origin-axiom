#!/usr/bin/env python3
"""B1324 PART B -- the one-cusped index on the chiral (and, as control, the amphichiral) one-cusped covers of m004 (DESIGN section 4).
The engine is B1297's, copied verbatim from frontier/B1297_the_spectral_cover_index/verification/step8_live_manifold_scan.py
(nrank, nnull, sym2, NRep, nfox, data, index) and d2lib imported from there; only the manifold source differs: the covers from Part A.
Sectors: V = Sym^2 rho_geo (x) chi, chi a torsion character trivial on the cusp with chi^2 != 1, one per inverse pair.
Galois-protected = character order prime to 3 (T-GALOIS-SELF-DUALITY: I = 0 on every cover); live = order divisible by 3 on a chiral cover.
Usage: python3 b_index_on_chiral_covers.py [--tol 1e-7] [--all]   (--all runs every one-cusped cover, not only the chiral ones + cyclic controls)"""
import os, sys, json, itertools, pathlib, warnings, math
warnings.filterwarnings("ignore")
import numpy as np, snappy
HERE = pathlib.Path(__file__).resolve().parent
B1297 = HERE.parents[2] / "frontier" / "B1297_the_spectral_cover_index" / "verification"
sys.path.insert(0, str(B1297))
import d2lib as L
TOL = float(sys.argv[sys.argv.index("--tol") + 1]) if "--tol" in sys.argv else 1e-7
RUN_ALL = "--all" in sys.argv

# ---- B1297 step8 engine, verbatim except TOL taken from the command line ----
def nrank(M):
    if M.size == 0: return 0
    s = np.linalg.svd(M, compute_uv=False)
    if s.size == 0: return 0
    return int(np.sum(s > TOL * max(1.0, s[0])))
def nnull(M):
    u, s, vh = np.linalg.svd(M)
    r = int(np.sum(s > TOL * max(1.0, s[0]))) if s.size else 0
    return vh[r:].conj().T
def sym2(g):
    p, q = g[0, 0], g[0, 1]; r, s = g[1, 0], g[1, 1]
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
# ---- end of the copied engine ----

def sectors_for(N):
    """all cusp-trivial torsion characters with chi^2 != 1, one per inverse pair, with their orders; the index on each (step8's loop)."""
    G = N.fundamental_group(); gens = list(G.generators()); rels = [L.word_from_snappy(r) for r in G.relators()]
    mer, lon = [L.word_from_snappy(w) for w in G.peripheral_curves()[0]]
    inv, cls, V, D, keep = L.h1_coordinates(gens, rels)
    divs = [int(x) for x in N.homology().elementary_divisors()]
    if sorted(inv) != sorted(divs): return dict(error=f"presentation H1 {inv} != SnapPy {divs}")
    tor_idx = [i for i, d in enumerate(inv) if d != 0]
    mc, lc = cls(mer), cls(lon)
    mats2 = {g: np.array([[complex(G.SL2C(g)[i, j]) for j in range(2)] for i in range(2)]) for g in gens}
    rho = NRep(mats2)
    if max(min(np.abs(rho(R) - s*np.eye(2)).max() for s in (1, -1)) for R in rels) > 1e-6: return dict(error="holonomy does not satisfy the relators to 1e-6")
    ranges = [range(inv[i]) if i in tor_idx else range(1) for i in range(len(inv))]
    seen = set(); results = []
    for expo in itertools.product(*ranges):
        if all(e == 0 for e in expo): continue
        if all((2 * e) % inv[i] == 0 for i, e in enumerate(expo) if i in tor_idx): continue
        def chi_val(c): return np.exp(2j * np.pi * sum((e * c[i]) / inv[i] for i, e in enumerate(expo) if i in tor_idx))
        if abs(chi_val(mc) - 1) > 1e-9 or abs(chi_val(lc) - 1) > 1e-9: continue
        inv_expo = tuple((-e) % inv[i] if i in tor_idx else 0 for i, e in enumerate(expo))
        if inv_expo in seen: continue
        seen.add(expo)
        order = 1
        for i, e in enumerate(expo):
            if i in tor_idx and e: order = order * (inv[i] // math.gcd(e, inv[i])) // math.gcd(order, inv[i] // math.gcd(e, inv[i]))
        mats = {g: sym2(mats2[g]) * chi_val(cls([(g, 1)])) for g in gens}
        I, F, A, B, ids = index(gens, rels, mats, [mer, lon])
        results.append(dict(expo=list(expo), order=order, galois_protected=(order % 3 != 0), I=int(I), F=int(F), a=list(A["a"]), t=list(A["t"]), r1=int(A["r1"]), r1_star=int(B["r1"]), identities=bool(ids)))
    return dict(H1=divs, sectors=results)

def main():
    census = json.loads((HERE / "a_arc_b_census.json").read_text(encoding="utf-8"))
    M = snappy.Manifold("m004"); covers = {d: M.covers(d) for d in range(2, 11)}
    picks = []
    for r in census["rows"]:
        if r["cusps"] != 1: continue
        if RUN_ALL or (not r["amphichiral"]) or r["type"] == "cyclic": picks.append(r)
    out = dict(tol=TOL, covers=[], live_nonzero=[], protected_nonzero=[], identity_failures=0, live_sectors=0, protected_sectors=0, control_sectors=0)
    for r in picks:
        N = covers[r["degree"]][r["index"]]
        res = sectors_for(N)
        rec = dict(degree=r["degree"], index=r["index"], type=r["type"], amphichiral=r["amphichiral"], **res)
        out["covers"].append(rec)
        if "error" in res: print(f"  {r['degree']}.{r['index']} {r['type']} H1={r['H1']}: {res['error']}"); continue
        summ = sorted(set((s["I"], s["order"], s["galois_protected"]) for s in res["sectors"]))
        for s in res["sectors"]:
            if not s["identities"]: out["identity_failures"] += 1
            if r["amphichiral"]: out["control_sectors"] += 1
            elif s["galois_protected"]: out["protected_sectors"] += 1
            else: out["live_sectors"] += 1
            if s["I"] != 0:
                (out["protected_nonzero"] if (s["galois_protected"] or r["amphichiral"]) else out["live_nonzero"]).append(dict(degree=r["degree"], index=r["index"], **s))
        print(f"  {r['degree']}.{r['index']:<3} {r['type']:<9} amph={r['amphichiral']!s:<5} H1={r['H1']:<18} sectors={len(res['sectors']):3d}  (I, order, protected) set = {summ}", flush=True)
    out["PASS_B"] = bool(out["live_nonzero"])
    (HERE / "b_index_on_chiral_covers.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(f"live sectors {out['live_sectors']} (nonzero {len(out['live_nonzero'])}), Galois-protected sectors {out['protected_sectors']} (nonzero {len(out['protected_nonzero'])}), control sectors on amphichiral covers {out['control_sectors']}, identity failures {out['identity_failures']}")
    print("B INDEX ON CHIRAL COVERS:", "PASS (a live nonzero index)" if out["PASS_B"] else "FAIL (every live sector vanishes)")

if __name__ == "__main__":
    main()
