#!/usr/bin/env python3
"""B1369's instrument -- the isometries of a family member as combinatorial automorphisms of its canonical retriangulation, with their
exact action on H_1(M; Q), on every cusp's peripheral subspace and its annihilator (the free classes of that cusp), and on the cusp
torus H_1(T_c; Q).

Why: an isometry g fixing cusp c and acting by -1 on the annihilator ann(P_c) < H^1(M; Q) pulls every harmonic 1-form whose periods
vanish on P_c back to its negative; the leading cusp mode F of such a form (the function on the torus whose sign cuts it into
partial^+ and partial^-, B1351 (ii)) then satisfies F o sigma = -F for sigma = g restricted to the torus, a homeomorphism, so sigma
maps {F > 0} onto {F < 0}: chi(partial^+) = chi(partial^-), and their sum is chi(T^2) - chi(zero set) = 0 (transverse zeros).  Both
vanish: N = 0 for every cusp-fixed spin-0 sector on cusp c.  This is fc R71's region-swap theorem (B1281 section 2D: sigma = -1 on the
torus) with the torus action allowed to be any homeomorphism -- the proof never used sigma = -1.

How: SnapPy's canonical_retriangulation() (Epstein-Penner) is an isometry invariant, so Isom(M) = its combinatorial automorphism group
(t3mlite.Mcomplex.isomorphisms_to).  The dual 2-complex of the retriangulation (0-cells: tetrahedra, 1-cells: faces, 2-cells: edges)
is a spine of M minus its finite vertices, so its H_1 is H_1(M).  A cusp's peripheral subspace is the image of the cycles of the
link graph Gamma_c (nodes: the corners of the ideal vertex, edges: its face crossings); the cusp torus is Z_1(Gamma_c) modulo the
loops around the link's vertices (the edge-ends of the triangulation at that cusp).  Every automorphism acts on all of these as a
signed permutation of cells.  Self-tests: d d = 0, the chain-map identity, |Aut| = |Isom| (SnapPy), b_1 and the peripheral ranks
against SnapPy's fundamental group, the torus actions' (trace, det) against SnapPy's cusp maps.
"""
import warnings
warnings.filterwarnings("ignore")
import sympy as sp
import snappy
from snappy.snap import t3mlite

VBITS = [1, 2, 4, 8]
FACES = [14, 13, 11, 7]           # face opposite vertex i is 15 ^ VBITS[i]


def _perm_image(p, bits):
    return p.image(bits)


class FamilyMember:
    def __init__(self, name):
        self.name = name
        self.M = snappy.Manifold(name)
        self.T = self.M.canonical_retriangulation()
        self.mc = t3mlite.Mcomplex(self.T)
        self.cusp_idx = self.T._get_cusp_indices_and_peripheral_curve_data()[0]     # per tet, per vertex: the cusp index in T
        self.tets = self.mc.Tetrahedra
        self.n = len(self.tets)
        self.faces = self.mc.Faces
        self.edges = self.mc.Edges
        self.nf, self.ne = len(self.faces), len(self.edges)
        self.num_cusps = self.T.num_cusps()
        self._dual_complex()
        self._homology()
        self._cusps()
        self.auts = self.mc.isomorphisms_to(self.mc)
        for a in self.auts:
            self._check_aut(a)

    # ------------------------------------------------------------ the dual 2-complex
    def _dual_complex(self):
        self.face_index = {}
        for f in self.faces:
            c0, c1 = f.Corners
            self.face_index[(c0.Tetrahedron.Index, c0.Subsimplex)] = (f.Index, +1)
            self.face_index[(c1.Tetrahedron.Index, c1.Subsimplex)] = (f.Index, -1)
        D = sp.zeros(self.n, self.nf)                 # d_1: 1-cells (faces) -> 0-cells (tets); oriented from Corners[0] to Corners[1]
        for f in self.faces:
            c0, c1 = f.Corners
            D[c1.Tetrahedron.Index, f.Index] += 1
            D[c0.Tetrahedron.Index, f.Index] -= 1
        E = sp.zeros(self.nf, self.ne)                # d_2: 2-cells (edges) -> 1-cells (faces): the signed faces around the edge
        for e in self.edges:
            for (ti, F, sgn) in self._walk_edge(e):
                E[self.face_index[(ti, F)][0], e.Index] += sgn
        assert D * E == sp.zeros(self.n, self.ne), "d d != 0"
        self.D, self.E = D, E

    def _walk_edge(self, e, track_end=None):
        """the corners around edge class e as (tet index, exit face, sign of the traversal w.r.t. the face's orientation);
        with track_end = a vertex bit of the starting corner, also yields the current end's vertex bit"""
        c = e.Corners[0]
        t, ed = c.Tetrahedron, c.Subsimplex
        F = [Fx for Fx in FACES if (Fx & ed) == ed][0]
        start = (t.Index, ed, F)
        cur_t, cur_ed, cur_F, cur_end = t, ed, F, track_end
        out = []
        for _ in range(10000):
            fi, sgn = self.face_index[(cur_t.Index, cur_F)]
            out.append((cur_t.Index, cur_F, sgn) if track_end is None else (cur_t.Index, cur_F, sgn, cur_end))
            g = cur_t.Gluing[cur_F]
            nt = cur_t.Neighbor[cur_F]
            n_ed, n_Fin = g.image(cur_ed), g.image(cur_F)
            n_end = g.image(cur_end) if cur_end is not None else None
            cur_F = [Fx for Fx in FACES if (Fx & n_ed) == n_ed and Fx != n_Fin][0]
            cur_t, cur_ed, cur_end = nt, n_ed, n_end
            if (cur_t.Index, cur_ed, cur_F) == start:
                return out
        raise RuntimeError("edge walk did not close")

    # ------------------------------------------------------------ H_1(M; Q)
    def _homology(self):
        Z = self.D.nullspace()
        Bcols = self.E.columnspace()
        Bm = sp.Matrix.hstack(*Bcols) if Bcols else sp.zeros(self.nf, 0)
        H = []
        cur = Bm
        for z in Z:
            trial = sp.Matrix.hstack(cur, z) if cur.cols else z
            if trial.rank() > (cur.rank() if cur.cols else 0):
                cur = trial
                H.append(z)
        self.b1 = len(H)
        self.H = H
        HB = sp.Matrix.hstack(*(H + Bcols)) if (H or Bcols) else sp.zeros(self.nf, 0)
        self.HB = HB
        self.HB_left_inverse = (HB.T * HB).inv() * HB.T if HB.cols else None

    def coords(self, z):
        """the class of a cycle z in the basis H of H_1(M; Q)"""
        if self.b1 == 0:
            return sp.zeros(0, 1)
        x = self.HB_left_inverse * z
        assert self.HB * x == z, "not a cycle"
        return x[:self.b1, :]

    # ------------------------------------------------------------ the cusps: link graphs, peripheral subspaces, torus quotient
    def _cusps(self):
        self.cusp = {}
        for c in range(self.num_cusps):
            nodes = []
            for t in self.tets:
                for i in range(4):
                    if self.cusp_idx[t.Index][i] == c:
                        nodes.append((t.Index, VBITS[i]))
            node_id = {nd: k for k, nd in enumerate(nodes)}
            gedges = []                     # (a, b, face class, key) : a -> b across the face, traversed from the Corners[0] side
            gkey = {}
            for (ti, v) in nodes:
                t = self.tets[ti]
                for F in FACES:
                    if (F & v) != v:
                        continue
                    fi, sgn = self.face_index[(ti, F)]
                    if sgn != +1:
                        continue
                    g = t.Gluing[F]
                    nt = t.Neighbor[F]
                    b = (nt.Index, g.image(v))
                    key = (ti, F, v)
                    gkey[key] = len(gedges)
                    gedges.append((node_id[(ti, v)], node_id[b], fi, key))
            # spanning tree by BFS; pathvec[node] = the C_1 vector (faces) of the tree path root -> node; gpath[node] = the same in Gamma_c's edges
            nN, nE = len(nodes), len(gedges)
            adj = {k: [] for k in range(nN)}
            for ei, (a, b, fi, key) in enumerate(gedges):
                adj[a].append((b, ei, +1))
                adj[b].append((a, ei, -1))
            pathvec = {0: sp.zeros(self.nf, 1)}
            gpath = {0: sp.zeros(nE, 1)}
            tree = set()
            queue = [0]
            while queue:
                a = queue.pop(0)
                for (b, ei, s) in adj[a]:
                    if b in pathvec:
                        continue
                    fi = gedges[ei][2]
                    pv = pathvec[a].copy(); pv[fi, 0] += s
                    gp = gpath[a].copy(); gp[ei, 0] += s
                    pathvec[b], gpath[b] = pv, gp
                    tree.add(ei)
                    queue.append(b)
            assert len(pathvec) == nN, "link graph disconnected"
            # fundamental cycles
            cycles_C1, cycles_G = [], []
            for ei, (a, b, fi, key) in enumerate(gedges):
                if ei in tree:
                    continue
                z = pathvec[a].copy(); z[fi, 0] += 1; z -= pathvec[b]
                zg = gpath[a].copy(); zg[ei, 0] += 1; zg -= gpath[b]
                assert self.D * z == sp.zeros(self.n, 1)
                cycles_C1.append(z); cycles_G.append(zg)
            # the loops around the link's vertices: the edge-ends of the triangulation at cusp c
            K = []
            for e in self.edges:
                c0 = e.Corners[0]
                ed = c0.Subsimplex
                for endbit in VBITS:
                    if (ed & endbit) != endbit:
                        continue
                    if self.cusp_idx[c0.Tetrahedron.Index][VBITS.index(endbit)] != c:
                        continue
                    loop = sp.zeros(nE, 1)
                    for (ti, F, sgn, endv) in self._walk_edge(e, track_end=endbit):
                        if sgn == +1:
                            loop[gkey[(ti, F, endv)], 0] += 1
                        else:
                            # the Corners[0] side of this face: the neighbour reached through F, with the end mapped across
                            t = self.tets[ti]
                            g = t.Gluing[F]; nt = t.Neighbor[F]
                            loop[gkey[(nt.Index, g.image(F), g.image(endv))], 0] -= 1
                    K.append(loop)
            # the peripheral subspace in H_1(M; Q) and its annihilator
            P = [self.coords(z) for z in cycles_C1]
            Pm = sp.Matrix.hstack(*P) if P else sp.zeros(self.b1, 0)
            rankP = Pm.rank() if P else 0
            ann = Pm.T.nullspace() if P else [sp.eye(self.b1)[:, k] for k in range(self.b1)]
            # H_1(T_c; Q) = Z_1(Gamma_c) / K: a basis of the quotient
            Km = sp.Matrix.hstack(*K) if K else sp.zeros(nE, 0)
            rK = Km.rank() if K else 0
            Tbasis = []
            cur = Km
            for zg in cycles_G:
                trial = sp.Matrix.hstack(cur, zg) if cur.cols else zg
                if trial.rank() > (cur.rank() if cur.cols else 0):
                    cur = trial
                    Tbasis.append(zg)
            assert len(Tbasis) == 2, f"cusp {c}: torus quotient has dimension {len(Tbasis)}"
            TK = sp.Matrix.hstack(*(Tbasis + [Km[:, j] for j in range(Km.cols)])) if K else sp.Matrix.hstack(*Tbasis)
            # a left inverse on the span (full column rank after removing dependent K columns)
            cols = []
            for j in range(TK.cols):
                trial = cols + [j]
                if TK[:, trial].rank() == len(trial):
                    cols = trial
            TK = TK[:, cols]
            self.cusp[c] = dict(nodes=nodes, node_id=node_id, gedges=gedges, gkey=gkey, P=Pm, rankP=rankP, ann=ann,
                                free=self.b1 - rankP, Tbasis=Tbasis, TK=TK, TK_left=(TK.T * TK).inv() * TK.T)

    # ------------------------------------------------------------ automorphisms
    def _check_aut(self, aut):
        for t in self.tets:
            s, p = aut[t.Index]
            for F in FACES:
                nt, g = t.Neighbor[F], t.Gluing[F]
                s2, p2 = aut[nt.Index]
                Fimg = p.image(F)
                assert s.Neighbor[Fimg] is s2, "automorphism breaks a gluing"
                gg = s.Gluing[Fimg]
                for v in VBITS:
                    assert p2.image(g.image(v)) == gg.image(p.image(v)), "automorphism breaks a gluing permutation"

    def aut_sign(self, aut):
        signs = {aut[t.Index][1].sign() for t in self.tets}
        return signs

    def cusp_permutation(self, aut):
        perm = {}
        for c in range(self.num_cusps):
            (ti, v) = self.cusp[c]['nodes'][0]
            s, p = aut[ti]
            perm[c] = self.cusp_idx[s.Index][VBITS.index(p.image(v))]
        return perm

    def action_on_C1(self, aut):
        G1 = sp.zeros(self.nf, self.nf)
        for f in self.faces:
            c0 = f.Corners[0]
            s, p = aut[c0.Tetrahedron.Index]
            fi2, sgn2 = self.face_index[(s.Index, p.image(c0.Subsimplex))]
            G1[fi2, f.Index] = sgn2
        G0 = sp.zeros(self.n, self.n)
        for t in self.tets:
            G0[aut[t.Index][0].Index, t.Index] = 1
        assert self.D * G1 == G0 * self.D, "not a chain map"
        return G1

    def action_on_H1(self, aut):
        """the matrix of g_* on H_1(M; Q) in the basis H"""
        G1 = self.action_on_C1(aut)
        if self.b1 == 0:
            return sp.zeros(0, 0)
        A = sp.Matrix.hstack(*[self.coords(G1 * h) for h in self.H])
        assert A.det() in (1, -1), "g_* not unimodular"
        return A

    def action_on_torus(self, aut, c):
        """the 2x2 matrix of g on H_1(T_c; Q) for an automorphism fixing cusp c"""
        cd = self.cusp[c]
        nE = len(cd['gedges'])
        S = sp.zeros(nE, nE)
        for ei, (a, b, fi, key) in enumerate(cd['gedges']):
            (ti, F, v) = key
            s, p = aut[ti]
            F2, v2 = p.image(F), p.image(v)
            fi2, sgn2 = self.face_index[(s.Index, F2)]
            if sgn2 == +1:
                S[cd['gkey'][(s.Index, F2, v2)], ei] = +1
            else:
                g = s.Gluing[F2]; nt = s.Neighbor[F2]
                S[cd['gkey'][(nt.Index, g.image(F2), g.image(v2))], ei] = -1
        A = sp.zeros(2, 2)
        for j, zg in enumerate(cd['Tbasis']):
            x = cd['TK_left'] * (S * zg)
            assert cd['TK'] * x == S * zg, "torus action does not preserve the cycle space"
            A[:, j] = x[:2, :]
        return A

    @staticmethod
    def torus_type(A):
        I2 = sp.eye(2)
        if A == I2:
            return "I"
        if A == -I2:
            return "-I"
        for k in (2, 3, 4, 6):
            if A ** k == I2:
                return f"order-{k}" + (" (det -1)" if A.det() == -1 else "")
        return "?"

    def analyse_cusp(self, c):
        """for a free cusp c: every automorphism fixing it, with its torus action and its action on ann(P_c)"""
        cd = self.cusp[c]
        rows = []
        for aut in self.auts:
            if self.cusp_permutation(aut)[c] != c:
                continue
            A = self.action_on_H1(aut)
            act = [A.T * f for f in cd['ann']]
            neg = all((a + f) == sp.zeros(self.b1, 1) for a, f in zip(act, cd['ann']))
            pos = all((a - f) == sp.zeros(self.b1, 1) for a, f in zip(act, cd['ann']))
            At = self.action_on_torus(aut, c)
            tt = self.torus_type(At)
            # an isometry fixing the cusp preserves the orientation of M iff it preserves that of the cusp torus (the boundary orientation)
            rows.append(dict(torus=tt, on_free="negated" if neg else ("fixed" if pos else "mixed"), orientation=("preserving" if At.det() == 1 else "reversing"), A=A))
        closed_general = any(r['on_free'] == "negated" for r in rows)
        closed_pmI = any(r['on_free'] == "negated" and r['torus'] in ("I", "-I") for r in rows)
        return rows, closed_general, closed_pmI


if __name__ == "__main__":
    import sys
    for name in sys.argv[1:] or ["m412"]:
        FM = FamilyMember(name)
        print(name, "tets", FM.n, "b_1", FM.b1, "cusps", FM.num_cusps, "|Aut|", len(FM.auts), "|Isom| (SnapPy)", FM.M.symmetry_group().order(),
              "ranks", [FM.cusp[c]['rankP'] for c in range(FM.num_cusps)])
        for c in range(FM.num_cusps):
            if FM.cusp[c]['free'] == 0:
                continue
            rows, cg, cp = FM.analyse_cusp(c)
            print(f"  free cusp {c} (free classes {FM.cusp[c]['free']}): fixers {len(rows)}: {[(r['torus'], r['on_free'], r['orientation']) for r in rows]} -> closed (general) {cg}, closed (+-I only) {cp}")
