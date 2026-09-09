#!/usr/bin/env python3
"""B1295 / D4(b) -- the census check of T-CLOSED-CLOSING-COUNTS-TWO-OR-NOTHING (B1294).

THE CLAIM UNDER TEST.  On a closed rational homology sphere every finite-order
orientation-reversing isometry has  chi(Fix) = 2 ; every orientation-preserving one has 0.
B1294 proved it by Lefschetz + Poincare duality.  This file checks it by COUNTING FIXED
CELLS, not by evaluating a Lefschetz number, on the closings the programme actually uses:

    Y_n  = n-fold cyclic branched cover of S^3 over the figure-eight knot   (n = 1..9)
         = the filling of the n-fold cyclic cover N_n of m004 along the lift mu~ of the meridian ; Y_1 = S^3, Y_9 = the
           SM seat's manifold.  All are QHS (Delta_{4_1} has no cyclotomic factor).
    Y_0  = the longitude (0,1) filling of m004, b_1 = 1  -- NOT a QHS: the CONTROL.

HOW THE COUNT IS MADE (independent of the theorem).
  * The isometries of N_n are the combinatorial automorphisms of its canonical ideal
    triangulation (the lift of m004's two regular ideal tetrahedra).  They are enumerated
    here from SnapPy's gluing data by propagation; SnapPy's own `isomorphisms_to` list is
    used only as a cross-check (order 8n, cusp matrices diagonal in (mu~, lambda~)).
  * Fix(g) on the open manifold N_n is a union of totally geodesic pieces, one per cell the
    automorphism maps to itself, determined by the induced permutation of that cell's ideal
    corners (the isometries of a regular ideal tetrahedron / triangle / geodesic).  Its
    compactly supported Euler characteristic is summed over OPEN cells:
        open tet : id -1 | transposition (reflection: open 2-disc) +1 | double transposition
                   (pi-rotation: open segment) -1 | 3-cycle (open ray) -1 | 4-cycle (rotatory
                   reflection: one point) +1
        open face: id +1 | transposition (open ray to the cusp) -1 | 3-cycle (centre) +1
        open edge: direction kept -1 | reversed (midpoint) +1
    Sanity: the identity gives chi_c(N_n) = -T + F - E = 0.
  * The filling solid torus V is an equidistant tube round the branch circle C; Fix(g|V)
    fibres over Fix(g|C) with contractible fibres, so chi(Fix V) = chi(Fix C), and
    chi(Fix C) = 2 iff g reverses C, else 0.  g reverses C iff it acts by -1 on
    H_1(dT)/<filling curve>.  With the cusp action diagonal in (mu~, lambda~):
        Y_n (fill mu~)     : sign on lambda~ = eps * a      (eps = orientation of g, a = its
                                                            sign on H_1(N_n;Q) = Q, spanned by mu~)
        Y_0 (fill lambda~) : sign on mu~     = a
    (lambda~ spans the kernel of H_1(dT;Q) -> H_1(N_n;Q); det A = eps.)
  * Excision over the cusp end (chi_c of a closed ray is 0) gives
        chi(Fix Y) = chi_c(Fix N_n) + chi(Fix C).
  * a is computed from the automorphism's action on H_1 of the dual spine (tets -> vertices,
    face classes -> edges, edge classes -> 2-cells), exact rational linear algebra.
  * Internal consistency, per automorphism: Hopf trace on the dual spine
        L_Hopf = #fixed tets - sum_{fixed faces} dir + sum_{fixed edges} eps*dir
    must equal the geometric chi(Fix of the compact core) = chi_c(Fix N_n) + chi(Fix cusp torus),
    the latter counted on the cusp triangulation the same way.  Neither side uses the theorem.

PASS = every orientation-reversing automorphism of every N_n (n = 1..9) gives chi(Fix Y_n) = 2,
every orientation-preserving one gives 0, all consistency checks hold, and the control Y_0
shows an orientation-reversing count != 2.
"""
import itertools, json, sys, warnings
from fractions import Fraction
warnings.filterwarnings("ignore")
import snappy
import sympy as sp

S4 = list(itertools.permutations(range(4)))

def compose(p, q):            # (p o q)(i) = p[q[i]]
    return tuple(p[q[i]] for i in range(len(q)))

def inverse(p):
    inv = [0]*len(p)
    for i, pi in enumerate(p): inv[pi] = i
    return tuple(inv)

def parity(p):
    s = 0
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] > p[j]: s += 1
    return -1 if s % 2 else 1

def cycle_type(p):            # p a permutation of an index set given as dict or tuple
    keys = list(range(len(p)))
    seen, ct = set(), []
    for k in keys:
        if k in seen: continue
        n, j = 0, k
        while j not in seen:
            seen.add(j); j = p[j]; n += 1
        ct.append(n)
    return tuple(sorted(ct, reverse=True))

# ---------------------------------------------------------------------------------------
class Tri:
    """An oriented ideal triangulation from SnapPy gluing data, with its cell classes."""
    def __init__(self, M):
        data = M._get_tetrahedra_gluing_data()
        self.T = len(data)
        self.nb = [list(d[0]) for d in data]
        self.pm = [[tuple(p) for p in d[1]] for d in data]
        # consistency of the gluing data and orientability (all gluing perms odd)
        for t in range(self.T):
            for f in range(4):
                t2, p = self.nb[t][f], self.pm[t][f]
                assert self.nb[t2][p[f]] == t and self.pm[t2][p[f]] == inverse(p), "gluing data inconsistent"
                assert parity(p) == -1, "triangulation not consistently oriented"
        self._faces(); self._edges(); self._cusp_cells()

    # face classes: {(t,f), (nb, p[f])}
    def _faces(self):
        self.face_id, self.faces = {}, []
        for t in range(self.T):
            for f in range(4):
                if (t, f) in self.face_id: continue
                t2, p = self.nb[t][f], self.pm[t][f]
                k = len(self.faces)
                self.faces.append(((t, f), (t2, p[f])))
                self.face_id[(t, f)] = k; self.face_id[(t2, p[f])] = k
        self.F = len(self.faces)

    # oriented edge classes: union-find on (t,(u,v))
    def _edges(self):
        parent = {}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry: parent[rx] = ry
        for t in range(self.T):
            for u in range(4):
                for v in range(4):
                    if u != v: parent[(t, (u, v))] = (t, (u, v))
        for t in range(self.T):
            for f in range(4):
                t2, p = self.nb[t][f], self.pm[t][f]
                for u in range(4):
                    for v in range(4):
                        if u != v and u != f and v != f:
                            union((t, (u, v)), (t2, (p[u], p[v])))
        roots = sorted({find(x) for x in parent}, key=lambda r: (r[0], r[1]))
        self.oedge_id = {x: roots.index(find(x)) for x in parent}   # oriented class index
        # unoriented classes = pairs {class of (u,v), class of (v,u)}; assert no self-reversal
        self.edge_of_oclass, self.edge_dir = {}, {}
        self.E = 0
        for x in parent:
            c = self.oedge_id[x]
            if c in self.edge_of_oclass: continue
            crev = self.oedge_id[(x[0], (x[1][1], x[1][0]))]
            assert crev != c, "edge identified to itself reversed (non-orientable)"
            self.edge_of_oclass[c] = self.E; self.edge_dir[c] = +1
            self.edge_of_oclass[crev] = self.E; self.edge_dir[crev] = -1
            self.E += 1
        self.oedge_rep = {}
        for x in parent:
            c = self.oedge_id[x]
            self.oedge_rep.setdefault(c, x)

    # cusp triangulation: triangles (t,v); edges (t,v,f) oriented by (w1,w2); vertices (t,v,w)
    def _cusp_cells(self):
        parent = {}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]; x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry: parent[rx] = ry
        # cusp vertices (t,v,w) identified across faces f not in {v,w}
        for t in range(self.T):
            for v in range(4):
                for w in range(4):
                    if v != w: parent[(t, v, w)] = (t, v, w)
        for t in range(self.T):
            for f in range(4):
                t2, p = self.nb[t][f], self.pm[t][f]
                for v in range(4):
                    for w in range(4):
                        if v != w and f not in (v, w):
                            union((t, v, w), (t2, p[v], p[w]))
        self.cv_id = {x: find(x) for x in parent}
        self.CV = len(set(self.cv_id.values()))
        # oriented cusp edges (t,v,f,(w1,w2)) identified across face f
        parent2 = {}
        def find2(x):
            while parent2[x] != x:
                parent2[x] = parent2[parent2[x]]; x = parent2[x]
            return x
        for t in range(self.T):
            for v in range(4):
                for f in range(4):
                    if f == v: continue
                    w1, w2 = [w for w in range(4) if w not in (v, f)]
                    parent2[(t, v, f, (w1, w2))] = (t, v, f, (w1, w2))
                    parent2[(t, v, f, (w2, w1))] = (t, v, f, (w2, w1))
        for t in range(self.T):
            for v in range(4):
                for f in range(4):
                    if f == v: continue
                    t2, p = self.nb[t][f], self.pm[t][f]
                    w1, w2 = [w for w in range(4) if w not in (v, f)]
                    for (a, b) in ((w1, w2), (w2, w1)):
                        x, y = (t, v, f, (a, b)), (t2, p[v], p[f], (p[a], p[b]))
                        rx, ry = find2(x), find2(y)
                        if rx != ry: parent2[rx] = ry
        self.ce_id = {x: find2(x) for x in parent2}
        self.CE = len(set(self.ce_id.values())) // 2
        self.CT = 4 * self.T
        # cusp Euler characteristic must vanish (tori)
        assert self.CV - self.CE + self.CT == 0, (self.CV, self.CE, self.CT)

    # ---- automorphisms by propagation -------------------------------------------------
    def automorphisms(self):
        out = []
        for t0 in range(self.T):
            for pi0 in S4:
                img = {0: (t0, pi0)}
                stack, ok = [0], True
                while stack and ok:
                    t = stack.pop()
                    gt, pt = img[t]
                    for f in range(4):
                        nb, p = self.nb[t][f], self.pm[t][f]
                        gnb = self.nb[gt][pt[f]]
                        pnb = compose(compose(self.pm[gt][pt[f]], pt), inverse(p))
                        if nb in img:
                            if img[nb] != (gnb, pnb): ok = False; break
                        else:
                            img[nb] = (gnb, pnb); stack.append(nb)
                if ok and len(img) == self.T:
                    # bijectivity on tets
                    if len({img[t][0] for t in img}) == self.T:
                        out.append([img[t] for t in range(self.T)])
        return out

    # ---- the per-automorphism data ------------------------------------------------------
    def analyse(self, g):
        eps = parity(g[0][1])
        assert all(parity(g[t][1]) == eps for t in range(self.T))
        chi_c = 0; fixed = {"tet": [], "face": [], "edge": []}
        # tets
        for t in range(self.T):
            gt, pt = g[t]
            if gt == t:
                ct = cycle_type(pt)
                w = {(1,1,1,1): -1, (2,1,1): +1, (2,2): -1, (3,1): -1, (4,): +1}[ct]
                chi_c += w; fixed["tet"].append((t, ct))
        # faces
        face_dir = {}
        for k, ((t, f), (t2, f2)) in enumerate(self.faces):
            gt, pt = g[t]
            gk = self.face_id[(gt, pt[f])]
            if gk != k: continue
            # induced permutation of the class's corners (corners of the canonical incidence)
            corners = [c for c in range(4) if c != f]
            if (gt, pt[f]) == (t, f):
                ind = {c: pt[c] for c in corners}; face_dir[k] = +1
            else:
                q = self.pm[gt][pt[f]]          # maps vertices of gt(=t2) back to t
                ind = {c: q[pt[c]] for c in corners}; face_dir[k] = -1
            perm = tuple(corners.index(ind[c]) for c in corners)
            ct = cycle_type(perm)
            w = {(1,1,1): +1, (2,1): -1, (3,): +1}[ct]
            chi_c += w; fixed["face"].append((k, ct, face_dir[k]))
        # edges
        edge_dir = {}
        for c, x in self.oedge_rep.items():
            e = self.edge_of_oclass[c]
            if self.edge_dir[c] != +1: continue    # one oriented representative per edge
            t, (u, v) = x
            gt, pt = g[t]
            gc = self.oedge_id[(gt, (pt[u], pt[v]))]
            if self.edge_of_oclass[gc] != e: continue
            d = self.edge_dir[gc]                 # +1 kept, -1 reversed
            edge_dir[e] = d
            chi_c += (-1 if d == +1 else +1); fixed["edge"].append((e, d))
        # cusp torus count
        chi_cusp = 0
        for t in range(self.T):
            gt, pt = g[t]
            for v in range(4):
                if gt == t and pt[v] == v:
                    corners = [w for w in range(4) if w != v]
                    perm = tuple(corners.index(pt[w]) for w in corners)
                    chi_cusp += {(1,1,1): +1, (2,1): -1, (3,): +1}[cycle_type(perm)]
        seen_e = set()
        for x, cls in self.ce_id.items():
            if cls in seen_e: continue
            t, v, f, (a, b) = x
            rev = self.ce_id[(t, v, f, (b, a))]
            seen_e.add(cls); seen_e.add(rev)
            gt, pt = g[t]
            gcls = self.ce_id[(gt, pt[v], pt[f], (pt[a], pt[b]))]
            if gcls == cls: chi_cusp -= 1
            elif gcls == rev: chi_cusp += 1
        seen_v = set()
        for x, cls in self.cv_id.items():
            if cls in seen_v: continue
            seen_v.add(cls)
            t, v, w = x
            gt, pt = g[t]
            if self.cv_id[(gt, pt[v], pt[w])] == cls: chi_cusp += 1
        # Hopf trace on the dual spine
        L_hopf = sum(1 for t in range(self.T) if g[t][0] == t) - sum(face_dir.values()) \
                 + sum(eps * d for d in edge_dir.values())
        return dict(eps=eps, chi_c=chi_c, chi_cusp=chi_cusp, L_hopf=L_hopf, fixed=fixed)

    # ---- dual spine homology and the action on H_1(;Q) ------------------------------------
    def dual_spine(self):
        """C_0 = tets, C_1 = face classes (oriented first->second incidence), C_2 = edge classes."""
        d1 = sp.zeros(self.T, self.F)
        for k, ((t, f), (t2, f2)) in enumerate(self.faces):
            d1[t2, k] += 1; d1[t, k] -= 1
        d2 = sp.zeros(self.F, self.E)
        for c, x in self.oedge_rep.items():
            if self.edge_dir[c] != +1: continue
            e = self.edge_of_oclass[c]
            t, (u, v) = x
            # walk around the edge crossing faces; start by crossing a face containing the edge
            start = (t, u, v)
            f = [w for w in range(4) if w not in (u, v)][0]
            cur_t, cur_u, cur_v, cur_f = t, u, v, f
            while True:
                k = self.face_id[(cur_t, cur_f)]
                sign = +1 if self.faces[k][0] == (cur_t, cur_f) else -1
                d2[k, e] += sign
                t2, p = self.nb[cur_t][cur_f], self.pm[cur_t][cur_f]
                nu, nv, nf_in = p[cur_u], p[cur_v], p[cur_f]
                nf = [w for w in range(4) if w not in (nu, nv, nf_in)][0]
                cur_t, cur_u, cur_v, cur_f = t2, nu, nv, nf
                if (cur_t, cur_u, cur_v) == start and cur_f == f: break
        assert (d1 * d2).is_zero_matrix
        return d1, d2

    def h1_action(self, g, d1, d2):
        """Matrix of g_* on H_1(dual spine; Q) = ker d1 / im d2, and the Betti number."""
        gC1 = sp.zeros(self.F, self.F)
        for k, ((t, f), (t2, f2)) in enumerate(self.faces):
            gt, pt = g[t]
            gk = self.face_id[(gt, pt[f])]
            sign = +1 if self.faces[gk][0] == (gt, pt[f]) else -1
            gC1[gk, k] += sign
        Z = d1.nullspace(); B = d2.columnspace()
        # quotient basis: extend B to a basis of Z
        Bm = sp.Matrix.hstack(*B) if B else sp.zeros(self.F, 0)
        rankB = Bm.rank()
        reps = []
        cur = Bm
        for z in Z:
            test = sp.Matrix.hstack(cur, z)
            if test.rank() > cur.rank():
                reps.append(z); cur = test
        b1 = len(reps)
        A = sp.zeros(b1, b1)
        for j, z in enumerate(reps):
            gz = gC1 * z
            # solve gz = sum_i A[i,j] reps[i] + Bm * y
            Mx = sp.Matrix.hstack(*reps, Bm) if B else sp.Matrix.hstack(*reps)
            sol = Mx.gauss_jordan_solve(gz)[0]
            sol = sol.subs({s: 0 for s in sol.free_symbols})
            for i in range(b1): A[i, j] = sol[i]
        return A, b1

# ---------------------------------------------------------------------------------------
def snappy_side(N):
    """SnapPy's own isometry list: order and cusp matrices (the cross-check)."""
    isos = N.isomorphisms_to(N)
    mats = []
    for i in isos:
        A = i.cusp_maps()[0]
        mats.append([[int(A[0,0]), int(A[0,1])], [int(A[1,0]), int(A[1,1])]])
    return len(isos), mats

def run_manifold(name, N, fill_index, expect_qhs=True, mu_index=0):
    """fill_index 0: fill mu~ (Y_n); 1: fill lambda~ (Y_0 control).  mu_index: which SnapPy basis curve is mu~."""
    tri = Tri(N)
    auts = tri.automorphisms()
    d1, d2 = tri.dual_spine()
    n_sn, mats = snappy_side(N)
    rows, ok = [], True
    diag = all(m[0][1] == 0 and m[1][0] == 0 for m in mats)
    for g in auts:
        r = tri.analyse(g)
        A, b1 = tri.h1_action(g, d1, d2)
        assert b1 == 1, b1
        a = int(A[0, 0]); assert a in (-1, 1)
        eps = r["eps"]
        # sign of g on the class generating H_1(dT)/<filling curve>
        s_core = eps * a if fill_index == 0 else a
        chi_C = 2 if s_core == -1 else 0
        chi_closed = r["chi_c"] + chi_C
        L_core = r["chi_c"] + r["chi_cusp"]          # chi(Fix of the compact core)
        cons = (L_core == r["L_hopf"] == 1 - a)
        rows.append(dict(eps=eps, a=a, chi_c=r["chi_c"], chi_cusp=r["chi_cusp"], L_hopf=r["L_hopf"],
                         s_core=s_core, chi_closed=chi_closed, consistent=cons,
                         fixed_tets=len(r["fixed"]["tet"]), fixed_faces=len(r["fixed"]["face"]),
                         fixed_edges=len(r["fixed"]["edge"])))
        ok &= cons
    n_rev = sum(1 for r in rows if r["eps"] == -1)
    counts_rev = sorted({r["chi_closed"] for r in rows if r["eps"] == -1})
    counts_pres = sorted({r["chi_closed"] for r in rows if r["eps"] == +1})
    from collections import Counter
    sig = Counter((r["eps"], r["a"], r["chi_c"], r["chi_closed"], r["fixed_tets"], r["fixed_faces"], r["fixed_edges"]) for r in rows)
    snappy_sig = Counter((m[0][0]*m[1][1], m[mu_index][mu_index]) for m in mats)   # (det, sign on mu~)
    mine_sig = Counter((r["eps"], r["a"]) for r in rows)
    out = dict(name=name, tets=tri.T, faces=tri.F, edges=tri.E, n_aut=len(auts), n_snappy=n_sn,
               snappy_cusp_maps_diagonal=diag, snappy_vs_mine_signs=(snappy_sig == mine_sig),
               n_rev=n_rev, counts_rev=counts_rev, counts_pres=counts_pres, consistent=ok,
               signature={str(k): v for k, v in sorted(sig.items())}, rows=rows)
    return out

def main(nmax=9, out_json="census_fixed_points.json"):
    M = snappy.Manifold("m004")
    results, checks = [], []
    def ok(c, msg):
        checks.append((bool(c), msg)); print(("  ok   " if c else "  FAIL ") + msg)

    print(f"== closings Y_n = mu~-filling of the n-fold cyclic cover N_n, n = 1..{nmax} ==")
    for n in range(1, nmax + 1):
        N = M if n == 1 else M.covers(n, cover_type="cyclic")[0]
        # SnapPy's peripheral basis on a cover is not uniformly (mu~, lambda~): every cusp matrix
        # is diagonal (checked below), so the basis curves ARE the two eigenlines, and mu~ is the
        # one whose filling kills b_1 (lambda~ bounds the lifted Seifert surface).
        Hs = []
        for slope in ((1, 0), (0, 1)):
            Yn = N.copy(); Yn.dehn_fill(slope); Hs.append(Yn.homology())
        killers = [i for i, H in enumerate(Hs) if H.betti_number() == 0]
        assert len(killers) == 1, Hs
        mu_index = killers[0]; H = Hs[mu_index]
        r = run_manifold(f"Y_{n}", N, 0, mu_index=mu_index)
        r["H1_closed"] = str(H); r["is_QHS"] = (H.betti_number() == 0); r["mu_slope"] = ((1, 0), (0, 1))[mu_index]
        r["H1_other_slope"] = str(Hs[1 - mu_index])
        results.append(r)
        print(f"Y_{n}: N_{n} has {r['tets']} tets; automorphisms {r['n_aut']} (SnapPy {r['n_snappy']}); "
              f"H1(Y_{n}) = {H}; orientation-reversing {r['n_rev']}: chi(Fix) in {r['counts_rev']}; "
              f"preserving: {r['counts_pres']}; consistent={r['consistent']} diag={r['snappy_cusp_maps_diagonal']} "
              f"signs={r['snappy_vs_mine_signs']}")
        print("      signature (eps, a, chi_c(N_n), chi(Fix Y_n), #tets, #faces, #edges kept) : count  ->", r["signature"])
        ok(r["is_QHS"], f"Y_{n} is a QHS")
        ok(r["n_aut"] == 8 * n == r["n_snappy"], f"|Isom(N_{n})| = 8n = {8*n}, matched by SnapPy")
        ok(r["snappy_cusp_maps_diagonal"], f"N_{n}: every cusp matrix is diagonal in (mu~, lambda~) (slope kept)")
        ok(r["snappy_vs_mine_signs"], f"N_{n}: (det A, A_11) multiset from SnapPy == (eps, a) from the spine")
        ok(r["consistent"], f"N_{n}: geometric chi(Fix core) == Hopf trace == 1 - a for all {r['n_aut']} automorphisms")
        ok(r["counts_rev"] == [2], f"Y_{n}: every orientation-reversing isometry has chi(Fix) = 2")
        ok(r["counts_pres"] == [0], f"Y_{n}: every orientation-preserving isometry has chi(Fix) = 0")
    # the m004 table itself (n = 1), against the known geometry
    sig1 = results[0]["signature"]
    print("      m004 rows (eps, a, chi_c, chi_closed, fixed tets, faces, edges):", sig1)
    ok(sig1.get("(-1, 1, 0, 2, 0, 0, 0)") == 2, "m004 glides: no cell mapped to itself (fixed-point free in M), 2 points on the knot in S^3")
    ok(sig1.get("(-1, -1, 2, 2, 2, 0, 0)") == 2, "m004 order-4 rotatory reflections: exactly the two tetrahedron centres, nothing on the knot")
    ok(sum(v for k, v in sig1.items() if k.startswith("(1, -1, -2, 0,")) == 2,
       "m004 pi-rotations: two open arcs cusp-to-cusp (chi_c = -2: one whole edge kept + two face-rays through a reversed edge's midpoint), closing to a circle in S^3")
    ok(sig1.get("(1, 1, 0, 0, 2, 0, 2)") == 1, "m004 r^2: a closed geodesic through both tets (pi-rotations of the tets, two edge midpoints)")
    ok(sig1.get("(1, 1, 0, 0, 2, 4, 2)") == 1, "m004 identity: everything fixed, chi_c(M) = 0")
    ok(len(sig1) == 5 and sum(sig1.values()) == 8, "m004: the eight elements of D4 are exactly these five kinds")

    print("== the control: Y_0 = the longitude filling of m004 (b_1 = 1, not a QHS) ==")
    Y0 = M.copy(); Y0.dehn_fill((0, 1)); H0 = Y0.homology()
    c = run_manifold("Y_0", M, 1, expect_qhs=False)
    c["H1_closed"] = str(H0); c["is_QHS"] = (H0.betti_number() == 0)
    results.append(c)
    print(f"Y_0: H1 = {H0}; orientation-reversing counts chi(Fix) in {c['counts_rev']}; preserving {c['counts_pres']}")
    ok(not c["is_QHS"], "Y_0 is not a QHS (b_1 = 1)")
    ok(c["counts_rev"] == [0, 4], "CONTROL FIRES: orientation-reversing counts on Y_0 are {0, 4}, never 2 "
                                  "(= 2 - 2a, the b_1 = 1 Lefschetz value; tr(g|H^1) = a odd)")

    verdict = "PASS" if all(k for k, _ in checks) else "FAIL"
    json.dump(dict(results=results, checks=checks, verdict=verdict),
              open(out_json, "w"), indent=1, default=str)
    print("SELFTEST:", verdict, f"({sum(1 for k,_ in checks if k)}/{len(checks)})")

if __name__ == "__main__":
    # --nmax N restricts the tower (the arc's lock runs n <= 3 in seconds; the banked run is n <= 9)
    nmax = int(sys.argv[sys.argv.index("--nmax") + 1]) if "--nmax" in sys.argv else 9
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "census_fixed_points.json"
    main(nmax, out)
