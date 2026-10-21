"""P-229 (GENESIS §5's frames-by-object table, the F-FC cells): main's own check of the SM seat's free-cusp results.

sm:B1385 T1 / sm:B1368: every word state (and every cyclic level of m004) has one cusp, b1 = 1 and peripheral rank 1, so no
free cusp.  sm:B1369: the free-cusp census of B1186's 112 (83 free cusps on 35 members) and the region-swap parity (79 of the
83 closed by an isometry fixing the cusp and acting by -1 on its free classes).  sm:B1370: the four residual cusps' moduli.

Main's route, written from the seat's read-outs, not its scripts:
  - H1(M; Q) from the dual spine of the canonical triangulation (dual vertices = tetrahedra, dual edges = faces, dual
    2-cells = edges); a cusp's peripheral image = the span of its vertex-link cycles (paths through tetrahedra around
    the ideal vertex, crossing faces that contain it);
  - the isometries = the combinatorial automorphisms of the canonical triangulation (checked: |Aut| = |Isom| from
    SnapPy's symmetry group, and the cusp permutations against SnapPy's isometries);
  - g acts by -1 on ann(P_c) in H^1 iff (g_* + I) H1 lies in P_c's image (dualise: g^* = -1 on W^perp iff g_* = -1 on V/W);
  - an independent control of b1 and the peripheral ranks from SnapPy's fundamental group (exponent sums).
"""
import sys, json, itertools, pathlib
from fractions import Fraction
import snappy

HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
P_ID = [0, 1, 2, 3]
SIGN = -1        # the parity: g acts by SIGN on the free classes; +1 makes the identity close every cusp (the lock's bite)


# ---------- exact linear algebra over Q ----------
def rank(rows):
    M = [[Fraction(x) for x in r] for r in rows if any(r)]
    if not M: return 0
    m = len(M[0]); r = 0
    for c in range(m):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M): break
    return r

def nullspace(rows, m):
    """basis of {x in Q^m : row . x = 0 for every row}"""
    M = [[Fraction(x) for x in r] for r in rows]
    piv_cols = []; r = 0
    for c in range(m):
        piv = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        M[r] = [a / M[r][c] for a in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv_cols.append(c); r += 1
    free = [c for c in range(m) if c not in piv_cols]
    basis = []
    for fc in free:
        x = [Fraction(0)] * m; x[fc] = Fraction(1)
        for i, pc in enumerate(piv_cols): x[pc] = -M[i][fc]
        basis.append(x)
    return basis


# ---------- the triangulation ----------
def parse(T):
    lines = [l for l in T._to_string().splitlines()]
    i = next(k for k, l in enumerate(lines) if l.strip() and l.split()[0].isdigit() and len(l.split()) == 2)
    nor, nnon = map(int, lines[i].split()); i += 1 + nor + nnon
    while not lines[i].strip(): i += 1
    n = int(lines[i]); i += 1
    tets = []
    for _ in range(n):
        while not lines[i].strip(): i += 1
        nb = list(map(int, lines[i].split())); gl = [list(map(int, s)) for s in lines[i + 1].split()]
        cu = list(map(int, lines[i + 2].split()))
        tets.append((nb, gl, cu)); i += 7
        if i < len(lines) and '.' in lines[i]: i += 1        # the shape line, when present
    return n, tets

def inv_perm(p):
    q = [0] * 4
    for a, b in enumerate(p): q[b] = a
    return q

def spine(n, tets):
    """dual edges (faces), their orientation, the boundary map d1, the dual 2-cells' boundaries (d2), cusp cycles"""
    face_id = {}; faces = []
    for t in range(n):
        for i in range(4):
            u = tets[t][0][i]; j = tets[t][1][i][i]
            key = min((t, i), (u, j))
            if key not in face_id: face_id[key] = len(faces); faces.append(key)
    def cross(t, i):                                   # the signed dual edge crossed going out of t through face i
        u = tets[t][0][i]; j = tets[t][1][i][i]
        k = face_id[min((t, i), (u, j))]
        return k, (1 if (t, i) == faces[k] else -1)
    nf = len(faces)
    d1 = [[0] * nf for _ in range(n)]                  # rows = tetrahedra
    for k, (t, i) in enumerate(faces):
        u = tets[t][0][i]
        d1[u][k] += 1; d1[t][k] -= 1
    # dual 2-cells: walk around each edge
    seen = set(); d2 = []
    for t in range(n):
        for a, b in itertools.combinations(range(4), 2):
            if (t, a, b) in seen: continue
            c, d = [v for v in range(4) if v not in (a, b)]
            vec = [0] * nf; cur = (t, a, b, c, d)
            while True:
                tt, aa, bb, cc, dd = cur
                seen.add((tt, min(aa, bb), max(aa, bb)))
                k, s = cross(tt, cc); vec[k] += s
                p = tets[tt][1][cc]; u = tets[tt][0][cc]
                na, nb_, nc = p[aa], p[bb], p[dd]       # entered u through face p[cc]; leave through the face opposite p[dd]
                nd = p[cc]
                cur = (u, na, nb_, nc, nd)
                if u == t and {na, nb_} == {a, b} and nc == c: break
            d2.append(vec)
    # cusp cycles: the graph on (tet, vertex) with cusp index, edges across faces containing the vertex
    cusps = {}
    for t in range(n):
        for v in range(4):
            cu = tets[t][2][v]
            if cu >= 0: cusps.setdefault(cu, []).append((t, v))
    cusp_cycles = {}
    for cu, nodes in cusps.items():
        # spanning tree by BFS; each non-tree edge gives a cycle (tree path to x, the edge, tree path back)
        parent = {nodes[0]: None}; order = [nodes[0]]; vec_to = {nodes[0]: [0] * nf}; nontree = []
        q = [nodes[0]]
        while q:
            x = q.pop(0); t, v = x
            for i in range(4):
                if i == v: continue
                u = tets[t][0][i]; p = tets[t][1][i]; y = (u, p[v])
                k, s = cross(t, i)
                if y not in parent:
                    parent[y] = x; w = list(vec_to[x]); w[k] += s; vec_to[y] = w; q.append(y)
                else:
                    nontree.append((x, y, k, s))
        cyc = []
        for x, y, k, s in nontree:
            w = [a - b for a, b in zip(vec_to[x], vec_to[y])]; w[k] += s
            cyc.append(w)
        cusp_cycles[cu] = cyc
    return faces, face_id, d1, d2, cusp_cycles, cross

def automorphisms(n, tets):
    out = []
    for s in range(n):
        for sig in itertools.permutations(range(4)):
            f = {0: (s, list(sig))}; q = [0]; ok = True
            while q and ok:
                t = q.pop()
                ft, st = f[t]
                for i in range(4):
                    u = tets[t][0][i]; p = tets[t][1][i]
                    fi = st[i]; u2 = tets[ft][0][fi]; p2 = tets[ft][1][fi]
                    # sigma_u = p2 . sigma_t . p^-1
                    pin = inv_perm(p); su = [p2[st[pin[v]]] for v in range(4)]
                    if u in f:
                        if f[u] != (u2, su): ok = False; break
                    else:
                        f[u] = (u2, su); q.append(u)
            if ok and len(f) == n and len({f[t][0] for t in f}) == n:
                # cusp indices must be respected (ideal to ideal)
                if all((tets[t][2][v] < 0) == (tets[f[t][0]][2][f[t][1][v]] < 0) for t in range(n) for v in range(4)):
                    out.append(f)
    return out

def face_action(f, faces, face_id, tets, cross):
    nf = len(faces); F = [[0] * nf for _ in range(nf)]       # column k = image of dual edge k
    for k, (t, i) in enumerate(faces):
        ft, st = f[t]
        k2, s = cross(ft, st[i])
        F[k2][k] = s
    return F

def matvec(F, x): return [sum(F[i][j] * x[j] for j in range(len(x))) for i in range(len(F))]


def analyse(name, want_parity=True):
    M = snappy.Manifold(name)
    C = M.canonical_retriangulation()
    n, tets = parse(C)
    faces, face_id, d1, d2, cusp_cycles, cross = spine(n, tets)
    nf = len(faces)
    # d1 . d2^T = 0 (the chain complex)
    for r in d1:
        for v in d2: assert sum(a * b for a, b in zip(r, v)) == 0, "d1 d2 != 0"
    rB = rank(d2); Z = nullspace(d1, nf); b1 = len(Z) - rB
    ncusp = len(cusp_cycles)
    ranks = []
    for cu in sorted(cusp_cycles):
        ranks.append(rank(d2 + cusp_cycles[cu]) - rB)
    # control: SnapPy's fundamental group, exponent sums
    G = M.fundamental_group(); gens = G.generators(); g = len(gens)
    def ab(word):
        v = [0] * g
        for ch in word:
            if ch.islower(): v[gens.index(ch)] += 1
            else: v[gens.index(ch.lower())] -= 1
        return v
    R = [ab(r) for r in G.relators()]; rR = rank(R)
    b1_pi = g - rR
    ranks_pi = [rank(R + [ab(m), ab(l)]) - rR for m, l in G.peripheral_curves()]
    assert b1_pi == b1, (name, b1, b1_pi)
    assert sorted(ranks_pi) == sorted(ranks), (name, ranks, ranks_pi)
    rec = dict(name=name, cusps=ncusp, b1=b1, ranks=ranks, ranks_pi=ranks_pi,
               free=[cu for cu, r in enumerate(ranks) if r < b1])
    if not want_parity or not rec["free"]:
        return rec
    A = automorphisms(n, tets)
    iso_order = M.symmetry_group().order()
    rec["aut"] = len(A); rec["isom"] = iso_order
    assert len(A) == iso_order, (name, len(A), iso_order)
    # cusp permutations against SnapPy's isometries
    cusp_of = {}
    for t in range(n):
        for v in range(4):
            if tets[t][2][v] >= 0: cusp_of[(t, v)] = tets[t][2][v]
    perms = []
    for f in A:
        pm = {}
        for (t, v), cu in cusp_of.items():
            ft, st = f[t]; pm[cu] = tets[ft][2][st[v]]
        perms.append(tuple(pm[c] for c in range(ncusp)))
    snap = sorted(tuple(i.cusp_images()) for i in M.is_isometric_to(M, return_isometries=True))
    # SnapPy labels the cusps of M; the canonical retriangulation keeps M's cusp indices
    rec["cusp_perms_agree"] = sorted(perms) == snap
    Fs = [face_action(f, faces, face_id, tets, cross) for f in A]
    # each F is a chain map: cycles to cycles, boundaries into boundaries
    for F in Fs:
        for z in Z: assert all(x == 0 for x in matvec(d1, matvec(F, z)))
        for v in d2: assert rank(d2 + [matvec(F, v)]) == rB
    closed = {}
    for cu in rec["free"]:
        W = d2 + cusp_cycles[cu]; rW = rank(W)
        hit = []
        for idx, (f, F) in enumerate(zip(A, Fs)):
            if perms[idx][cu] != cu: continue
            # (F + I) Z  in span(W)
            good = all(rank(W + [[a - SIGN * b for a, b in zip(matvec(F, z), z)]]) == rW for z in Z)
            if good:
                det = orient_sign(f)
                hit.append(det)
        closed[cu] = dict(closing=len(hit), orientation_preserving=sum(1 for d in hit if d > 0))
    rec["parity"] = closed
    rec["open_free_cusps"] = [cu for cu in rec["free"] if closed[cu]["closing"] == 0]
    return rec

def orient_sign(f):
    s = f[0][1]
    inv = sum(1 for i in range(4) for j in range(i + 1, 4) if s[i] > s[j])
    return 1 if inv % 2 == 0 else -1


def word_states(maxlen=12):
    sys.path.insert(0, str(ROOT / "frontier/B1434_the_architecture_census/verification"))
    seen = set(); out = []
    def cyc_min(w): return min(w[i:] + w[:i] for i in range(len(w)))
    def swap(w): return w.translate(str.maketrans("LR", "RL"))
    def primitive(w): return all(w != w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)
    for n in range(2, maxlen + 1):
        for p in itertools.product("LR", repeat=n):
            w = "".join(p)
            if len(set(w)) < 2 or not primitive(w): continue
            key = min(cyc_min(w), cyc_min(swap(w)))
            if key in seen: continue
            seen.add(key); out.append(key)
    return out


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "controls":
        res = [analyse(nm) for nm in ("m004", "m003", "m129", "L6a4")]
        for r in res: print(r)
    elif mode == "words":
        ws = word_states(int(sys.argv[2]) if len(sys.argv) > 2 else 12)
        out = []
        for w in ws:
            for eps in "+-":
                M = snappy.Manifold("b+" + eps + w)
                H = M.homology()
                b1 = H.betti_number(); nc = M.num_cusps()
                G = M.fundamental_group(); gens = G.generators(); g = len(gens)
                def ab(word):
                    v = [0] * g
                    for ch in word:
                        if ch.islower(): v[gens.index(ch)] += 1
                        else: v[gens.index(ch.lower())] -= 1
                    return v
                R = [ab(r) for r in G.relators()]; rR = rank(R)
                pr = [rank(R + [ab(m), ab(l)]) - rR for m, l in G.peripheral_curves()]
                out.append(dict(state=eps + w, cusps=nc, b1=b1, ranks=pr, oriented=M.is_orientable()))
        bad = [o for o in out if not (o["cusps"] == 1 and o["b1"] == 1 and o["ranks"] == [1])]
        print(len(out), "word states;", len(bad), "with a free cusp or another shape")
        json.dump(dict(n=len(out), exceptions=bad, states=out), open(HERE / "main_ffc_words.json", "w"), indent=0)
    elif mode == "family":
        d = json.load(open(ROOT / "frontier/B1186_family_is_112/verification/family_census.json"))
        names = d["members_B"]
        res = []
        for nm in names:
            r = analyse(nm); res.append(r)
            print(nm, r["cusps"], r["b1"], r["ranks"], r.get("aut"), r.get("parity"), flush=True)
        free = [(r["name"], c) for r in res for c in r["free"]]
        open_ = [(r["name"], c) for r in res for c in r.get("open_free_cusps", [])]
        summ = dict(members=len(res), with_free=sum(1 for r in res if r["free"]), free_cusps=len(free),
                    open=open_, members_closed=len(res) - len({n for n, _ in open_}))
        print(summ)
        json.dump(dict(summary=summ, members=res), open(HERE / "main_ffc_family.json", "w"), indent=0)
