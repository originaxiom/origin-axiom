#!/usr/bin/env python3
"""B1370 -- THE RESIDUAL'S LEADING MODE: on the four free cusps that B1369's parity left open (o10_150688 cusp 0, o10_150708 cusp 0,
o10_150716 cusp 0, o10_150725 cusp 1), which Fourier modes of the cusp torus can a Higgs form's leading cusp mode occupy, and does
the lowest allowed shell force an annular partition?

The frame (B1351 (ii), B1369 section 1): a cusp-fixed spin-0 sector on cusp c has its Higgs class in ann(P_c); the harmonic form's
expansion on the cusp is a sum over the dual lattice Lambda* of modes decaying like exp(-|k| e^t), so the partition of the torus at
infinity is the sign pattern of the lowest-|k| shell whose coefficient is non-zero.  An isometry g fixing the cusp acts on the class
by epsilon = +-1 and on the torus by an affine isometry sigma(x) = A x + b; the leading mode F obeys F o sigma = epsilon F.  When
epsilon = -1 for every class (B1369's parity) the partition is annular whatever the shell.  On the four residual cusps some fixer has
epsilon = +1, and the question is which shells survive the constraint F o sigma = epsilon F for all fixers: if the lowest surviving
shell is a single direction {+-k}, F = |a| cos(2 pi k.x + phase), whose zero set is two parallel closed geodesics -- annular, N = 0 --
unless the coefficient at that shell vanishes for a reason no symmetry supplies.

The instrument: develop the cusp cross-section from the tetrahedra shapes (the link triangles of the ideal vertex, placed in C by a
breadth-first walk; the closing-up translations generate the lattice Lambda), verify Lambda against SnapPy's cusp modulus, then read
each automorphism's affine action on the developed plane (a similarity fixing the triangle correspondence; |a| = 1 checked), its linear
part in Lambda's basis and its translation modulo Lambda.  The automorphisms and their action on the free classes come from
B1369's family_isometries.py on the manifold's own triangulation (which realises the full isometry group on all four members).
Usage: python3 residual_cusp_modes.py"""
import os, sys, cmath, math, itertools, warnings
warnings.filterwarnings("ignore")
import numpy as np
import sympy as sp
import snappy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1369_the_siblings_in_the_sm_frame", "verification"))
from family_isometries import FamilyMember, VBITS, FACES

RESIDUAL = [("o10_150688", 0), ("o10_150708", 0), ("o10_150716", 0), ("o10_150725", 1)]
CYCLIC = {0: (1, 2, 3), 1: (0, 3, 2), 2: (0, 1, 3), 3: (0, 2, 1)}    # the other vertices in the order induced by the orientation


def edge_shape(z, v, w):
    """the shape parameter of edge (v, w) of a tetrahedron with shape z on edge 01"""
    e = frozenset((v, w))
    if e in (frozenset((0, 1)), frozenset((2, 3))): return z
    if e in (frozenset((0, 2)), frozenset((1, 3))): return 1 / (1 - z)
    return 1 - 1 / z


def canonical_triangle(z, v, mirror):
    """the link triangle at vertex v: positions of its corners (at the edges (v, w)) for the three other vertices w, up to similarity;
    interior angle at corner w = arg of the shape of edge (v, w); corners in the cyclic order CYCLIC[v] (or reversed if mirror)"""
    order = CYCLIC[v] if not mirror else tuple(reversed(CYCLIC[v]))
    ang = {w: cmath.phase(edge_shape(z, v, w)) for w in order}
    a, b, c = order
    P = {a: 0j, b: 1 + 0j}
    # law of sines: |P_c - P_a| / |P_b - P_a| = sin(angle_b) / sin(angle_c); counterclockwise: P_c = |..| e^{i angle_a}
    r = math.sin(ang[b]) / math.sin(ang[c])
    P[c] = r * cmath.exp(1j * ang[a])
    return P


def develop_cusp(FM, c, mirror):
    """place every link triangle of cusp c in C; return positions per corner and the closing-up translations"""
    shapes = [complex(z) for z in FM.M.tetrahedra_shapes('rect')]
    nodes = FM.cusp[c]['nodes']
    pos = {}
    root = nodes[0]
    ti, vbit = root; v = VBITS.index(vbit)
    pos[root] = canonical_triangle(shapes[ti], v, mirror)
    queue = [root]; translations = []
    while queue:
        (ti, vbit) = queue.pop(0); v = VBITS.index(vbit); t = FM.tets[ti]
        P = pos[(ti, vbit)]
        for u in range(4):
            if u == v: continue
            F = 15 ^ VBITS[u]                       # the face opposite u, containing v
            g = t.Gluing[F]; nt = t.Neighbor[F]
            v2 = VBITS.index(g.image(vbit))
            w1, w2 = [w for w in range(4) if w not in (u, v)]
            w1b, w2b = VBITS.index(g.image(VBITS[w1])), VBITS.index(g.image(VBITS[w2]))
            u2 = [w for w in range(4) if w not in (v2, w1b, w2b)][0]
            Q = canonical_triangle(shapes[nt.Index], v2, mirror)
            # similarity taking Q[w1b] -> P[w1], Q[w2b] -> P[w2]
            a = (P[w2] - P[w1]) / (Q[w2b] - Q[w1b]); b = P[w1] - a * Q[w1b]
            placed = {w: a * Q[w] + b for w in Q}
            key = (nt.Index, VBITS[v2])
            if key not in pos:
                pos[key] = placed; queue.append(key)
            else:
                old = pos[key]
                d = [placed[w] - old[w] for w in placed]
                if max(abs(x - d[0]) for x in d) > 1e-7:
                    return None, None                 # not a pure translation: wrong convention
                if abs(d[0]) > 1e-9: translations.append(d[0])
    return pos, translations


def lattice_basis(translations):
    """a reduced basis of the rank-2 lattice generated by the translations (Gauss reduction on a generating set)"""
    vecs = [t for t in translations if abs(t) > 1e-9]
    # find two independent generators, then reduce the rest into them by integer combinations
    basis = []
    for t in vecs:
        if not basis: basis = [t]; continue
        if len(basis) == 1:
            if abs((t / basis[0]).imag) > 1e-7: basis.append(t)
            continue
        break
    b1, b2 = basis
    def reduce(b1, b2):
        for _ in range(100):
            if abs(b1) > abs(b2): b1, b2 = b2, b1
            m = round(((b2 * b1.conjugate()).real) / abs(b1) ** 2)
            if m == 0: break
            b2 = b2 - m * b1
        return b1, b2
    b1, b2 = reduce(b1, b2)
    # every translation must be an integer combination
    def coords(t):
        M = np.array([[b1.real, b2.real], [b1.imag, b2.imag]]); x = np.linalg.solve(M, [t.real, t.imag]); return x
    for t in vecs:
        x = coords(t)
        if max(abs(x - np.round(x))) > 1e-6:
            # refine: the lattice generated might be finer -- add t and re-reduce
            b1, b2 = reduce(b1, t) if abs(t) < abs(b2) else reduce(b1, b2)
    for t in vecs:
        x = coords(t); assert max(abs(x - np.round(x))) < 1e-6, "translations do not generate a lattice"
    return b1, b2


def reduce_tau(t):
    t = complex(t)
    if t.imag < 0: t = -t                      # the lattice Z + tau Z equals Z + (-tau) Z
    for _ in range(500):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12: t = -1 / t
        else: break
    return t


def affine_action(FM, c, aut, pos, b1, b2):
    """the affine isometry sigma(x) = a x + b or a conj(x) + b of the developed plane induced by the automorphism aut (fixing cusp c);
    returns (orientation, A as a 2x2 integer matrix in the basis (b1, b2), b in Lambda-coordinates mod 1)"""
    (ti, vbit) = FM.cusp[c]['nodes'][0]; v = VBITS.index(vbit)
    s, p = aut[ti]
    P = pos[(ti, vbit)]
    key2 = (s.Index, p.image(vbit))
    Q = pos[key2]
    ws = [w for w in range(4) if w != v]
    pairs = [(P[w], Q[VBITS.index(p.image(VBITS[w]))]) for w in ws]
    best = None
    for orient in (+1, -1):
        src = [x if orient == 1 else x.conjugate() for x, y in pairs]
        a = (pairs[1][1] - pairs[0][1]) / (src[1] - src[0]); b = pairs[0][1] - a * src[0]
        err = abs(a * src[2] + b - pairs[2][1])
        if err < 1e-6:
            best = (orient, a, b); break
    assert best is not None, "no similarity matches the automorphism"
    orient, a, b = best
    assert abs(abs(a) - 1) < 1e-6, f"not an isometry: |a| = {abs(a)}"
    # linear part on Lambda: images of b1, b2
    def coords(t):
        M = np.array([[b1.real, b2.real], [b1.imag, b2.imag]]); return np.linalg.solve(M, [t.real, t.imag])
    L = lambda x: a * x if orient == 1 else a * x.conjugate()
    A = np.array([coords(L(b1)), coords(L(b2))]).T
    assert max(abs(A - np.round(A)).flatten()) < 1e-6, "linear part not integral"
    A = np.round(A).astype(int)
    bc = coords(b); bc = bc - np.floor(bc + 1e-9)
    return orient, A, bc, a, b


def dual_shells(b1, b2, nshells=6):
    """the dual lattice's shortest shells: lists of dual vectors (as (m, n) coordinates in the dual basis) grouped by |k|"""
    G = np.array([[abs(b1) ** 2, (b1 * b2.conjugate()).real], [(b1 * b2.conjugate()).real, abs(b2) ** 2]])
    Ginv = np.linalg.inv(G)          # norms of dual vectors k = m k1 + n k2 (k_i dual to b_i): |k|^2 = (m, n) Ginv (m, n)^T
    vecs = []
    for m in range(-12, 13):
        for n in range(-12, 13):
            if (m, n) == (0, 0): continue
            vecs.append((float(np.array([m, n]) @ Ginv @ np.array([m, n])), (m, n)))
    vecs.sort()
    shells = []
    for nrm, k in vecs:
        if shells and abs(shells[-1][0] - nrm) < 1e-7: shells[-1][1].append(k)
        else: shells.append([nrm, [k]])
    return shells[:nshells]


def allowed_dimension(shell, fixers, eps_of):
    """the real dimension of the space of trigonometric polynomials sum_{k in shell} a_k e^{2 pi i k.x} (a_{-k} = conj a_k) with
    F o sigma = eps(sigma) F for every fixer sigma = (A, b) (A the linear part on Lambda, b in Lambda-coordinates)"""
    ks = shell
    idx = {k: i for i, k in enumerate(ks)}
    n = len(ks)
    # unknowns: complex a_k for k in shell, as real vector (Re, Im); constraints: a_{-k} = conj(a_k), and for each sigma:
    # (F o sigma)(x) = sum_k a_k e^{2 pi i k.(A x + b)} = sum_k a_k e^{2 pi i k.b} e^{2 pi i (A^T k).x}  =>  a_{A^T k} = eps a_k e^{2 pi i k.b}
    rows = []
    def add_complex_eq(coeffs, rhs_zero=True):
        # sum_j coeffs[j] * a_{k_j} = 0 (complex): two real rows
        re = np.zeros(2 * n); im = np.zeros(2 * n)
        for j, cval in coeffs.items():
            re[2 * j] += cval.real; re[2 * j + 1] -= cval.imag
            im[2 * j] += cval.imag; im[2 * j + 1] += cval.real
        rows.append(re); rows.append(im)
    for k in ks:
        mk = (-k[0], -k[1]); i, j = idx[k], idx[mk]
        # a_{-k} - conj(a_k) = 0: real parts equal, imaginary parts opposite
        r1 = np.zeros(2 * n); r1[2 * j] = 1; r1[2 * i] = -1; rows.append(r1)
        r2 = np.zeros(2 * n); r2[2 * j + 1] = 1; r2[2 * i + 1] = 1; rows.append(r2)
    for (A, b, eps) in fixers:
        for k in ks:
            kA = tuple(int(x) for x in A.T @ np.array(k))
            assert kA in idx, "the linear part does not preserve the shell"
            phase = cmath.exp(2j * math.pi * (k[0] * b[0] + k[1] * b[1]))
            coeffs = {}
            coeffs[idx[kA]] = coeffs.get(idx[kA], 0j) + 1
            coeffs[idx[k]] = coeffs.get(idx[k], 0j) - eps * phase          # kA may equal k: accumulate
            add_complex_eq(coeffs)
    Mx = np.array(rows)
    rank = np.linalg.matrix_rank(Mx, tol=1e-8)
    return 2 * n - rank


def zero_set_type(shell_vectors):
    """the directions in the allowed shell: a single +-k pair gives parallel-line zero sets (annular partitions)"""
    dirs = set()
    for (m, n) in shell_vectors:
        g = math.gcd(abs(m), abs(n)); mm, nn = m // g, n // g
        if (mm, nn) < (0, 0) or (mm < 0) or (mm == 0 and nn < 0): mm, nn = -mm, -nn
        dirs.add((mm, nn))
    return dirs


print("=== B1370: the residual free cusps' allowed leading modes ===")
summary = []
for name, c in RESIDUAL:
    FM = FamilyMember(name, canonical=False)
    S = FM.M.symmetry_group()
    assert len(FM.auts) == S.order(), f"{name}: the manifold's own triangulation does not realise every isometry"
    print(f"\n{name}, cusp {c}: b_1 {FM.b1}, ranks {[FM.cusp[k]['rankP'] for k in range(FM.num_cusps)]}, free classes on cusp {c}: {FM.cusp[c]['free']}, |Aut| = |Isom| = {len(FM.auts)}")
    pos = trans = None
    for mirror in (False, True):
        pos, trans = develop_cusp(FM, c, mirror)
        if pos is not None: break
    assert pos is not None, "no consistent development"
    b1, b2 = lattice_basis(trans)
    tau = reduce_tau(b2 / b1); tau_snappy = reduce_tau(FM.M.cusp_info()[c]['modulus'])
    print(f"  developed cusp: {len(pos)} triangles, {len(trans)} closing-up translations; lattice basis |b1| = {abs(b1):.6f}, |b2| = {abs(b2):.6f}; reduced modulus {tau.real:+.6f}{tau.imag:+.6f}i (SnapPy: {tau_snappy.real:+.6f}{tau_snappy.imag:+.6f}i) {'agree' if abs(tau - tau_snappy) < 1e-6 or abs(tau + tau_snappy.conjugate()) < 1e-6 else 'DISAGREE'}")
    # the fixers with their action on the free classes
    rows, _, _ = FM.analyse_cusp(c)
    fixers = [aut for aut in FM.auts if FM.cusp_permutation(aut)[c] == c]
    ann = FM.cusp[c]['ann']; d = len(ann)
    annM = sp.Matrix.hstack(*ann)
    acts = []
    for aut in fixers:
        Amat = FM.action_on_H1(aut)
        X = (annM.T * annM).inv() * annM.T * (Amat.T * annM)      # the action on ann in the basis ann
        orient, A, bc, a, b = affine_action(FM, c, aut, pos, b1, b2)
        acts.append((aut, X, orient, A, bc))
        print(f"    fixer: orientation {'+' if orient == 1 else '-'}, linear part on Lambda {A.tolist()} (det {int(round(np.linalg.det(A)))}), translation (Lambda-coordinates mod 1) ({bc[0]:.4f}, {bc[1]:.4f}), action on the free classes {X.tolist()}")
    # cross-checks against SnapPy: the (trace, det) multiset of the fixers' linear parts against the cusp maps of the isometries fixing
    # the cusp, and the developed lattice's modulus against cusp_translations()
    mine_td = sorted((int(np.trace(x[3])), int(round(np.linalg.det(x[3])))) for x in acts)
    def _sm2(cm): return sp.Matrix([[int(cm[i, j]) for j in range(2)] for i in range(2)])
    theirs_td = sorted((int(_sm2(iso.cusp_maps()[c]).trace()), int(_sm2(iso.cusp_maps()[c]).det())) for iso in FM.M.isomorphisms_to(FM.M) if list(iso.cusp_images())[c] == c)
    trl = FM.M.cusp_translations()[c]; tau_tr = reduce_tau(complex(trl[1]) / complex(trl[0]))
    ok_td = mine_td == theirs_td; ok_tr = abs(tau_tr - reduce_tau(b2 / b1)) < 1e-6 or abs(tau_tr + reduce_tau(b2 / b1).conjugate()) < 1e-6
    print(f"  cross-check: (trace, det) of the fixers' linear parts agree with SnapPy's cusp maps: {ok_td}; lattice modulus agrees with SnapPy's cusp_translations: {ok_tr}")
    assert ok_td and ok_tr, "cross-check against SnapPy failed"
    # the classes: for one free class, every fixer acts by +-1 on it; for two, a class v is constrained only by its stabiliser
    # (the fixers with X v = +-v), so the special lines are the eigenlines of the fixers and every other class sees the identity alone
    Xs = [x[1] for x in acts]
    if d == 1:
        classes = [("the free class", sp.Matrix([1]), [(i, int(Xs[i][0, 0])) for i in range(len(acts))])]
    else:
        lines = []
        for X in Xs:
            for ev, mult, basis in X.eigenvects():
                for vvec in basis:
                    if not all(x.is_real for x in vvec): continue            # a Higgs class is real: complex eigenvectors are not classes
                    vvec = vvec / sp.gcd(list(vvec)) if all(x.is_integer for x in vvec) else vvec
                    if not any(sp.Matrix.hstack(l, vvec).rank() == 1 for l in lines): lines.append(vvec)
        classes = []
        for vvec in lines:
            stab = []
            for i, X in enumerate(Xs):
                img = X * vvec
                if img == vvec: stab.append((i, 1))
                elif img == -vvec: stab.append((i, -1))
            classes.append((f"special line {vvec.T.tolist()[0]}", vvec, stab))
        classes.append(("a generic class (stabiliser: the identity alone)", None, [(i, 1) for i, X in enumerate(Xs) if X == sp.eye(d)]))
        print(f"  special lines in the free classes (eigenlines of fixers): {len(lines)}; stabilisers of sizes {[len(cl[2]) for cl in classes]}")
    shells = dual_shells(b1, b2, nshells=12)
    print(f"  dual shells (|k|^2, vectors): {[(round(s[0], 6), s[1]) for s in shells[:4]]}")
    for (label, vvec, stab) in classes:
        print(f"  {label}: fixers in the stabiliser {len(stab)}, their signs {[e for i, e in stab]}")
        first = None; single_before = 0
        for (nrm, ks) in shells:
            fx = [(acts[i][3], acts[i][4], e) for i, e in stab]
            dim = allowed_dimension(ks, fx, None)
            dirs = zero_set_type(ks)
            verdict = "killed by symmetry" if dim == 0 else (f"allowed (real dimension {dim}); single direction {sorted(dirs)}: cos(2 pi k.x + phase), zero set two parallel geodesics -> annular partition" if len(dirs) == 1 else f"allowed (real dimension {dim}); directions {sorted(dirs)}: a combination whose zero set can bound discs -> the partition depends on the coefficients")
            print(f"    shell |k|^2 = {nrm:.6f} {ks}: {verdict}")
            if dim > 0 and first is None:
                first = (round(nrm, 6), ks, dim, sorted(dirs))
            if dim > 0 and len(dirs) == 1 and not any(len(zero_set_type(k2)) > 1 for (n2, k2) in shells if n2 < nrm - 1e-9 and allowed_dimension(k2, fx, None) > 0):
                single_before += 1
            if dim > 0 and len(dirs) > 1:
                print(f"    -> the first allowed shell with two directions; {single_before} allowed single-direction shells precede it: the partition is annular unless the harmonic form's coefficients at all {single_before} of them vanish")
                break
        summary.append((name, c, label, first[0], first[1], first[2], first[3], single_before))
print("\n=== (D) the residual's leading allowed modes ===")
for s in summary:
    print(f"  {s[0]} cusp {s[1]}, {s[2]}: lowest allowed shell |k|^2 = {s[3]}, vectors {s[4]}, dimension {s[5]}, directions {s[6]} -> {'annular unless the coefficients of the first ' + str(s[7]) + ' allowed shells all vanish' if len(s[6]) == 1 else 'partition depends on the coefficients'}")
print("DONE")
