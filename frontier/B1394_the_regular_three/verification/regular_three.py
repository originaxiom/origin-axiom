#!/usr/bin/env python3
"""B1394 -- the regular three: sources on the fixed arcs of an order-3 isometry, across m004's class.

For a member M, every cyclic subgroup <g> of order 3 whose generator is an orientation-preserving rotation (non-empty fixed arcs),
and every g-invariant character chi: H_1(M) -> mu_3 (torsion included): the twisted cohomology of M with coefficients chi (on the dual
spine of SnapPy's canonical retriangulation, B1369's complex, over F_7 and F_13), the lift phi of g to the flat line
(delta phi = z - g*z mod 3), and the weight omega^{phi} of the lift on the fibre over each fixed arc.  The theorem sealed in
PREREGISTRATION.md: if H*(M; chi) = 0 the k = 3m weights are balanced (m of each cube root of unity).

The instrument reuses B1369's FamilyMember (dual complex, automorphisms, action on C_1) through B1385's StateMember for covers.
Usage: python3 regular_three.py [control|census]   (control = m202 only, the lane's R32 case)."""
import importlib.util
import json
import sys
import time
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore")
import snappy
from flint import nmod_mat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


FI = _load("b1369_family_isometries", "frontier/B1369_the_siblings_in_the_sm_frame/verification/family_isometries.py")
EC = _load("b1385_eisenstein_cusps", "frontier/B1385_the_states_together/verification/eisenstein_cusps.py")
VB = [1, 2, 4, 8]
FACES = [14, 13, 11, 7]
PRIMES = ((7, 2), (13, 3))              # (p, a primitive cube root of unity in F_p)


# ------------------------------------------------------------------ linear algebra over F_p
def mat(rows, ncols, p):
    return nmod_mat(len(rows), ncols, [x % p for r in rows for x in r], p) if rows else nmod_mat(0, ncols, [], p)


def rank(A):
    return A.rank() if A.nrows() and A.ncols() else 0


def nullspace_cols(A, p):
    """a basis of {x : A x = 0} as a list of vectors (lists)"""
    X, nul = A.nullspace()
    return [[int(X[i, j]) % p for i in range(A.ncols())] for j in range(nul)]


# ------------------------------------------------------------------ the member
class Member:
    def __init__(self, FM, label):
        self.FM, self.label = FM, label
        self.nt, self.nf, self.ne = FM.n, FM.nf, FM.ne
        self.finite = sum(1 for t in FM.tets for j in range(4) if FM.cusp_idx[t.Index][j] < 0)  # corners at finite vertices
        vfin = set()
        for t in FM.tets:
            for j in range(4):
                if FM.cusp_idx[t.Index][j] < 0:
                    vfin.add(t.Class[VB[j]].Index)
        self.nfinite = len(vfin)
        # faces: start (Corners[0]) and end (Corners[1]) tets
        self.fstart = {f.Index: f.Corners[0].Tetrahedron.Index for f in FM.faces}
        self.fend = {f.Index: f.Corners[1].Tetrahedron.Index for f in FM.faces}
        # the ordered walk around every edge: (tet, edge bits, face index, sign)
        self.walks = {e.Index: self._walk(e) for e in FM.edges}
        self.D = [[int(FM.D[i, j]) for j in range(self.nf)] for i in range(self.nt)]
        self.E = [[int(FM.E[i, j]) for j in range(self.ne)] for i in range(self.nf)]

    def _walk(self, e):
        c = e.Corners[0]
        t, ed = c.Tetrahedron, c.Subsimplex
        F = [Fx for Fx in FACES if (Fx & ed) == ed][0]
        start = (t.Index, ed, F)
        cur_t, cur_ed, cur_F = t, ed, F
        out = []
        for _ in range(10000):
            fi, sgn = self.FM.face_index[(cur_t.Index, cur_F)]
            out.append((cur_t.Index, cur_ed, fi, sgn))
            g = cur_t.Gluing[cur_F]
            nt = cur_t.Neighbor[cur_F]
            n_ed, n_Fin = g.image(cur_ed), g.image(cur_F)
            cur_F = [Fx for Fx in FACES if (Fx & n_ed) == n_ed and Fx != n_Fin][0]
            cur_t, cur_ed = nt, n_ed
            if (cur_t.Index, cur_ed, cur_F) == start:
                return out
        raise RuntimeError("edge walk did not close")

    # ---- automorphisms
    def aut_tuple(self, a):
        return tuple((a[i][0].Index, tuple(a[i][1].tuple())) for i in range(self.nt))

    def compose(self, a2, a1):
        return tuple((a2[s][0], tuple(a2[s][1][p[j]] for j in range(4))) for (s, p) in a1)

    def order(self, a):
        ident = tuple((i, (0, 1, 2, 3)) for i in range(self.nt))
        k, x = 1, a
        while x != ident:
            x = self.compose(a, x)
            k += 1
            assert k <= 1000
        return k

    @staticmethod
    def img_bits(p, bits):
        out = 0
        for j in range(4):
            if bits & VB[j]:
                out |= VB[p[j]]
        return out

    def G1T(self, a_obj):
        """g* on 1-cochains: (g*z)(f) = sum_f' G1[f', f] z(f') -- the transpose of B1369's chain action"""
        G1 = self.FM.action_on_C1(a_obj)
        return [[int(G1[fp, f]) for fp in range(self.nf)] for f in range(self.nf)]

    # ---- the fixed arcs of an order-3 element (B1390's pieces, returned as components)
    def fixed_components(self, a):
        FM = self.FM
        adj = {}
        counter = [0]

        def link(x, y):
            adj.setdefault(x, []).append(y)
            adj.setdefault(y, []).append(x)

        def vnode(t, bit):
            k = FM.cusp_idx[t.Index][VB.index(bit)]
            if k >= 0:
                counter[0] += 1
                return ("end", k, counter[0])
            return ("V", t.Class[bit].Index)

        anomalies = []
        for i, (s, p) in enumerate(a):
            if s != i:
                continue
            fixed_v = [j for j in range(4) if p[j] == j]
            if len(fixed_v) != 1:
                anomalies.append(("invariant tet with %d fixed vertices" % len(fixed_v), i))
                continue
            j0 = fixed_v[0]
            t = FM.tets[i]
            link(("T", i), vnode(t, VB[j0]))
            link(("T", i), ("F", t.Class[15 ^ VB[j0]].Index))
        for e in FM.edges:
            c = e.Corners[0]
            t, eb = c.Tetrahedron, c.Subsimplex
            s, p = a[t.Index]
            eb2 = self.img_bits(p, eb)
            if FM.tets[s].Class[eb2] is not e:
                continue
            # which end goes where: compare the images of the two vertex classes
            v0, v1 = [VB[j] for j in range(4) if eb & VB[j]]
            w0 = FM.tets[s].Class[self.img_bits(p, v0)]
            if w0 is t.Class[v0]:
                link(("E", e.Index), vnode(t, v0))
                link(("E", e.Index), vnode(t, v1))
        comps, seen = [], set()
        for x in adj:
            if x in seen:
                continue
            comp, stack = [], [x]
            seen.add(x)
            while stack:
                y = stack.pop()
                comp.append(y)
                for z in adj[y]:
                    if z not in seen:
                        seen.add(z)
                        stack.append(z)
            ends = [y for y in comp if y[0] == "end"]
            bad = [y for y in comp if (y[0] == "end" and len(adj[y]) != 1) or (y[0] != "end" and len(adj[y]) != 2)]
            if bad or len(ends) != 2:
                anomalies.append(("component", len(ends), bad[:2]))
            comps.append(comp)
        return comps, anomalies

    # ---- characters mod 3
    def invariant_characters(self, G1T):
        """representatives z of the g-invariant classes of H^1(spine; F_3), enumerated in full (the trivial one first)"""
        p = 3
        nf, nt, ne = self.nf, self.nt, self.ne
        # rows: E^T z = 0 (ne rows);  (G1T - I) z - D^T b = 0 (nf rows);  unknowns (z, b)
        rows = []
        for e in range(ne):
            rows.append([self.E[f][e] for f in range(nf)] + [0] * nt)
        for f in range(nf):
            rows.append([(G1T[f][fp] - (1 if fp == f else 0)) for fp in range(nf)] + [-self.D[t][f] for t in range(nt)])
        A = mat(rows, nf + nt, p)
        W = [v[:nf] for v in nullspace_cols(A, p)]
        B = [[self.D[t][f] % 3 for f in range(nf)] for t in range(nt)]             # coboundaries D^T e_t
        basis, cur = [], B[:]
        r0 = rank(mat(cur, nf, p)) if cur else 0
        for w in W:
            trial = cur + [w]
            r = rank(mat(trial, nf, p))
            if r > r0:
                cur, r0 = trial, r
                basis.append(w)
        d = len(basis)
        reps = []
        for idx in range(3 ** d):
            cs, x = [], idx
            for _ in range(d):
                cs.append(x % 3)
                x //= 3
            z = [sum(c * b[f] for c, b in zip(cs, basis)) % 3 for f in range(nf)]
            reps.append(z)
        return reps, d

    # ---- the twisted complex over F_p
    def twisted(self, z, p, w):
        nt, nf, ne = self.nt, self.nf, self.ne
        pw = [1, w % p, (w * w) % p]
        d0 = [[0] * nt for _ in range(nf)]
        for f in range(nf):
            d0[f][self.fend[f]] = (d0[f][self.fend[f]] + 1) % p
            d0[f][self.fstart[f]] = (d0[f][self.fstart[f]] - pw[z[f] % 3]) % p
        d1 = [[0] * nf for _ in range(ne)]
        for e, walk in self.walks.items():
            S = 0
            for (t, ed, fi, sgn) in walk:
                Snext = (S + sgn * z[fi]) % 3
                if sgn == +1:
                    d1[e][fi] = (d1[e][fi] + pw[(-Snext) % 3]) % p
                else:
                    d1[e][fi] = (d1[e][fi] - pw[(-S) % 3]) % p
                S = Snext
            assert S % 3 == 0, "z is not a cocycle around edge %d" % e
        M0, M1 = mat(d0, nt, p), mat(d1, nf, p)
        prod = M1 * M0
        assert all(int(prod[i, j]) == 0 for i in range(prod.nrows()) for j in range(prod.ncols())), "d1 d0 != 0"
        r0, r1 = rank(M0), rank(M1)
        h0 = nt - r0
        h1 = (nf - r1) - r0
        h2s = ne - r1
        assert h0 - h1 + h2s == nt - nf + ne
        return h0, h1, h2s - self.nfinite

    # ---- the lift and the arc weights
    def weights(self, a, comps, z, G1T):
        nt, nf = self.nt, self.nf
        rhs = [(z[f] - sum(G1T[f][fp] * z[fp] for fp in range(nf))) % 3 for f in range(nf)]
        # solve D^T phi = rhs over F_3: rows f: phi(end) - phi(start) = rhs(f)
        rows = [[self.D[t][f] for t in range(nt)] + [-rhs[f]] for f in range(nf)]
        A = mat(rows, nt + 1, 3)
        sols = [v for v in nullspace_cols(A, 3) if v[-1] % 3 != 0]
        assert sols, "no lift: the character is not invariant"
        v = sols[0]
        inv = pow(v[-1], -1, 3)
        phi = [(x * inv) % 3 for x in v[:nt]]
        # check
        for f in range(nf):
            assert (phi[self.fend[f]] - phi[self.fstart[f]] - rhs[f]) % 3 == 0
        lam = []
        for comp in comps:
            ts = [y[1] for y in comp if y[0] == "T"]
            if ts:
                vals = {phi[t] for t in ts}
                assert len(vals) == 1, "weight not constant along an arc"
                lam.append(vals.pop())
                continue
            es = [y[1] for y in comp if y[0] == "E"]
            e = es[0]
            walk = self.walks[e]
            t0, ed0 = walk[0][0], walk[0][1]
            s, pp = a[t0]
            target = (s, self.img_bits(pp, ed0))
            pos = [j for j, (t, ed, fi, sg) in enumerate(walk) if (t, ed) == target]
            assert len(pos) == 1, "the rotated corner is not on the walk once"
            S = 0
            for j in range(pos[0]):
                t, ed, fi, sg = walk[j]
                S = (S + sg * z[fi]) % 3
            lam.append((phi[t0] + S) % 3)
        return Counter(lam), phi


def member_from(name_or_manifold, label):
    if isinstance(name_or_manifold, str):
        FM = FI.FamilyMember(name_or_manifold)
    else:
        FM = EC.StateMember(name_or_manifold, label)
    return Member(FM, label)


def analyse(M, verbose=True):
    FM = M.FM
    rows = []
    seen_subgroups = set()
    for a_obj in FM.auts:
        if FM.aut_sign(a_obj) != {0}:
            continue
        a = M.aut_tuple(a_obj)
        if M.order(a) != 3:
            continue
        a2 = M.compose(a, a)
        key = frozenset([a, a2])
        if key in seen_subgroups:
            continue
        seen_subgroups.add(key)
        comps, anomalies = M.fixed_components(a)
        if anomalies:
            rows.append(dict(member=M.label, anomalies=anomalies))
            continue
        if not comps:
            continue                                      # a free order-3 symmetry (no arcs): not a rotation
        k = len(comps)
        G1T = M.G1T(a_obj)
        reps, d = M.invariant_characters(G1T)
        for idx, z in enumerate(reps):
            hs = [M.twisted(z, p, w) for (p, w) in PRIMES]
            assert hs[0] == hs[1], ("primes disagree", hs)
            h0, h1, h2 = hs[0]
            lam, phi = M.weights(a, comps, z, G1T)
            counts = tuple(lam.get(j, 0) for j in range(3))
            rows.append(dict(member=M.label, k=k, dim_inv=d, trivial=(idx == 0), h=(h0, h1, h2),
                             acyclic=(h0, h1, h2) == (0, 0, 0), counts=counts,
                             balanced=(counts[0] == counts[1] == counts[2])))
    return rows


def b1390_arcs(M_snappy, label):
    """B1390's instrument: the multiset of fixed-arc counts over the orientation-preserving order-3 elements"""
    EA = _load("b1390_eisenstein_axes", "frontier/B1390_the_eisenstein_axes/verification/eisenstein_axes.py")
    FS, rows, agree = EA.analyse(label, M_snappy)
    return Counter(r["arcs"] for (k, o, r) in rows if o == 1 and k == 3)


def own_arcs(M):
    out = Counter()
    for a_obj in M.FM.auts:
        if M.FM.aut_sign(a_obj) != {0}:
            continue
        a = M.aut_tuple(a_obj)
        if M.order(a) != 3:
            continue
        comps, anomalies = M.fixed_components(a)
        out[len(comps)] += 1
    return out


def census_members():
    EA = _load("b1390_eisenstein_axes", "frontier/B1390_the_eisenstein_axes/verification/eisenstein_axes.py")
    fam = json.load(open(ROOT / "frontier" / "B1186_family_is_112" / "verification" / "family_census.json"))
    members = fam["members_B"]
    assert len(members) == 112
    arith = [n for n in members if not EA.nonintegral_witness(snappy.ManifoldHP(n))]
    assert len(arith) == 99, len(arith)
    return arith


def census(out_json=None):
    t0 = time.time()
    arith = census_members()
    RP = _load("b1386_the_open_cusp", "frontier/B1386_the_open_eisenstein_cusp/verification/the_open_cusp.py")
    todo = [(n, n) for n in arith] + [("cube~3.24", RP.member())]
    all_rows, xcheck_bad = [], []
    for i, (label, src) in enumerate(todo):
        t1 = time.time()
        M = member_from(src, label)
        Ms = src if not isinstance(src, str) else snappy.Manifold(src)
        mine, theirs = own_arcs(M), b1390_arcs(Ms, label)
        if mine != theirs:
            xcheck_bad.append((label, dict(mine), dict(theirs)))
        got = analyse(M)
        all_rows += got
        print("progress %3d/%d %-12s tets %4d  rows %4d  %.1f s" % (i + 1, len(todo), label, M.nt, len(got), time.time() - t1),
              file=sys.stderr, flush=True)
    rows = [r for r in all_rows if "anomalies" not in r]
    anomalies = [r for r in all_rows if "anomalies" in r]
    members_rot = sorted({r["member"] for r in rows})
    nontriv = [r for r in rows if not r["trivial"]]
    acyc = [r for r in nontriv if r["acyclic"]]
    p1_fail = [r for r in rows if r["acyclic"] and not r["balanced"]]
    p3 = [r for r in nontriv if not r["acyclic"] and not r["balanced"]]
    summary = dict(members=len(todo), members_with_rotations=len(members_rot), pairs=len(rows), nontrivial=len(nontriv),
                   acyclic_nontrivial=len(acyc), P1_failures=len(p1_fail), P3_unbalanced_nonacyclic=len(p3),
                   arc_crosscheck_failures=xcheck_bad, anomalies=len(anomalies),
                   k_values=dict(Counter(r["k"] for r in rows)), seconds=round(time.time() - t0))
    if out_json:
        json.dump(dict(summary=summary, rows=rows, anomalies=anomalies, p3=p3, p1_fail=p1_fail), open(out_json, "w"), indent=1)
    return summary, rows, p3, p1_fail


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "control"
    t0 = time.time()
    if mode == "control":
        M = member_from("m202", "m202")
        print("m202: tets %d faces %d edges %d, finite vertices %d, b1 %d, |Aut| %d" % (M.nt, M.nf, M.ne, M.nfinite, M.FM.b1,
                                                                                     len(M.FM.auts)))
        for r in analyse(M):
            print(r)
    if mode == "census":
        summary, rows, p3, p1_fail = census(out_json=str(HERE / "census.json"))
        for k, v in summary.items():
            print("%-28s %s" % (k, v))
        print("P1 failures:", p1_fail[:5])
        print("P3 (non-acyclic, non-trivial, unbalanced):")
        for r in p3:
            print("   ", r)
    print("(%.0f s)" % (time.time() - t0))
