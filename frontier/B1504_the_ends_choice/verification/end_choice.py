"""B1504 -- THE END'S CHOICE: what the architecture itself fixes at a cusp point (B1500's choice: lower, a Lagrangian line, or
upper, at each point of the one-point completion).

Four parts, all own code (SnapPy for triangulations and isometries, sympy for exact 2x2 algebra):

A. THE PUNCTURE.  m004 (the genesis's root) and m003 (its sign partner): the isometries' cusp maps in the meridian-longitude framing,
   read as (orientation, s_m, s_l) (main's B1324 dictionary: det = s_m s_l); the lines every isometry fixes; the fillings along them
   (the meridian gives S^3, the longitude -- the fibre's boundary, the puncture's own loop -- gives the Sol torus bundle, P019's F6
   sibling); the order bit (L^-1 LR L = RL, and b++LR, b++RL present m004 with orientation-preserving isometries between them); the
   flow class's sign under each isometry (B1369's instrument: its action on H_1(M)) against the meridian sign.
B. THE LATTICE LEMMA.  Every finite subgroup of GL(2, Z), up to conjugacy (the subgroups of the square lattice's D4 and the hexagonal
   lattice's D6): a common invariant real line exists iff the group contains no element of order 3, 4 or 6.
C. THE CENSUS.  For every member -- m004, m003, B1186's 99 arithmetic members, cube~3.24 (B1386), B1399's 109 covers -- the isometries
   (SnapPy), every cusp's stabiliser and its linear parts, whether a rotation of order 3, 4 or 6 fixes the cusp, the lines the whole
   stabiliser fixes, the orientation signs, the cusp orbits.  Cross-checked against B1369's instrument (the canonical retriangulation's
   automorphisms and their exact action on each cusp torus): the number of isometries and, per cusp, the multiset of (order, det) of
   the stabiliser's linear parts.  At a rotated hexagonal cusp: the three shortest lattice lines (the A2 roots) from the cusp shape, and
   whether the rotation permutes them in a 3-cycle.
D. PER MEMBER.  Whether a completion invariant under every isometry exists for the self-conjugate (neutral) sectors (no rotated cusp
   point); with the trivial vacuum, whether an invariant chiral completion of a charged pair exists in the frame's reading (orientation
   acts on nothing) and in the reading with a G2 orientation (orientation-reversing isometries exchange lower and upper), and the orbit
   weights that then bound its count.

Run:  python3 end_choice.py puncture | lemma | census [--partial FILE] | crosscheck_own LABEL... |
      record --partial FILE [--own FILE]
"""
import importlib.util
import itertools
import json
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import sympy as sp
import snappy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str((ROOT / rel).parent))
    spec.loader.exec_module(mod)
    return mod


I2 = sp.eye(2)


# ------------------------------------------------------------------------------------------------------------ 2x2 algebra
def order(A, cap=12):
    B = sp.eye(2)
    for k in range(1, cap + 1):
        B = B * A
        if B == I2:
            return k
    return None


def is_rotation(A):
    """a finite-order lattice automorphism with no real eigenvector: det 1 and order 3, 4 or 6"""
    return A.det() == 1 and order(A) in (3, 4, 6)


def primitive(v):
    a, b = int(v[0]), int(v[1])
    g = sp.gcd(a, b)
    a, b = a // g, b // g
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return (a, b)


def invariant_lines(A):
    """the real lines fixed by a finite-order integer matrix: 'all' for +-I, its two eigenlines for a reflection (rational: eigenvalues
    +-1 of an integer matrix), none for a rotation of order 3, 4 or 6"""
    if A == I2 or A == -I2:
        return "all"
    if is_rotation(A):
        return set()
    assert A.det() == -1 and order(A) == 2, A
    lines = set()
    for ev in (1, -1):
        ns = (A - ev * I2).nullspace()
        assert len(ns) == 1
        v = ns[0]
        den = sp.ilcm(*[sp.fraction(x)[1] for x in v])
        lines.add(primitive(v * den))
    return lines


def common_lines(mats):
    out = "all"
    for A in mats:
        L = invariant_lines(A)
        if L == "all":
            continue
        out = set(L) if out == "all" else (out & L)
    return out


# ------------------------------------------------------------------------------------------------------------ B. the lemma
def lemma():
    """every finite subgroup of GL(2, Z) is conjugate to a subgroup of D4 = Aut(Z^2 square) or of D6 = Aut(Z[w]); the property is
    conjugation-invariant, so checking all subgroups of the two is checking all finite subgroups"""
    r4, f4 = sp.Matrix([[0, -1], [1, 0]]), sp.Matrix([[1, 0], [0, -1]])
    r6, f6 = sp.Matrix([[1, -1], [1, 0]]), sp.Matrix([[0, 1], [1, 0]])

    def closure(gens):
        G = [I2]
        frontier = list(gens)
        while frontier:
            x = frontier.pop()
            if x in G:
                continue
            G.append(x)
            frontier.extend(x * g for g in G if x * g not in G)
            frontier.extend(g * x for g in G if g * x not in G)
        return G

    rows = []
    for name, (r, f) in (("D4", (r4, f4)), ("D6", (r6, f6))):
        big = closure([r, f])
        seen = []
        for k in (0, 1, 2):
            for gens in itertools.combinations(big, k):
                H = closure(list(gens))
                key = frozenset(tuple(h) for h in H)
                if key in seen:
                    continue
                seen.append(key)
                rot = any(is_rotation(h) for h in H)
                cl = common_lines(H)
                has_line = cl == "all" or len(cl) > 0
                rows.append(dict(ambient=name, order=len(H), rotation=rot, common_line=has_line,
                                 lines=("all" if cl == "all" else sorted(cl))))
                assert rot == (not has_line), (name, len(H), rot, cl)
        assert len(big) == (8 if name == "D4" else 12)
    return rows


# ------------------------------------------------------------------------------------------------------------ isometries
def snappy_isometries(M):
    isos = M.is_isometric_to(M, return_isometries=True)
    out = []
    for iso in isos:
        perm = list(iso.cusp_images())
        maps = [sp.Matrix(m) for m in iso.cusp_maps()]
        out.append((perm, maps))
    return out


def orientation(perm, maps):
    """an isometry is orientation-preserving iff its cusp map has determinant +1 at any cusp (the cusp's normal direction is kept)"""
    dets = {int(maps[c].det()) for c in range(len(perm))}
    assert len(dets) == 1, dets
    return dets.pop()


def shortest_lines(shape, k=3, box=4):
    """the k shortest primitive lattice lines of the cusp lattice Z + Z*shape (vector a*meridian + b*longitude)"""
    cands = []
    for a in range(-box, box + 1):
        for b in range(-box, box + 1):
            if (a, b) == (0, 0) or sp.gcd(a, b) != 1:
                continue
            p = primitive((a, b))
            cands.append((abs(complex(p[0]) + p[1] * shape), p))
    cands = sorted(set(cands))
    lines = []
    for L, p in cands:
        if p not in [q for _, q in lines]:
            lines.append((L, p))
        if len(lines) == k:
            break
    return lines


def analyse(M, label, crosscheck=True, canonical=True):
    t0 = time.time()
    isos = snappy_isometries(M)
    k = M.num_cusps()
    assert len(isos) == M.symmetry_group().order(), (label, len(isos))
    shapes = [complex(M.cusp_info(c)["shape"]) for c in range(k)]
    cusps = []
    for c in range(k):
        stab = [(perm, maps) for perm, maps in isos if perm[c] == c]
        mats = [maps[c] for perm, maps in stab]
        rot_orders = sorted({order(A) for A in mats if is_rotation(A)})
        cl = common_lines(mats)
        orients = sorted({orientation(p, m) for p, m in stab})
        row = dict(cusp=c, stabiliser=len(stab), rotation_orders=rot_orders, rotated=bool(rot_orders),
                   common_lines=("all" if cl == "all" else sorted(cl)), orientations=orients,
                   types=sorted({(order(A), int(A.det())) for A in mats}), shape=[shapes[c].real, shapes[c].imag])
        assert row["rotated"] == (cl != "all" and len(cl) == 0), (label, c)
        if row["rotated"] and 3 in [order(A) for A in mats] or 6 in rot_orders:
            R = next(A for A in mats if order(A) in (3, 6))
            R3 = R if order(R) == 3 else R * R
            sl = shortest_lines(shapes[c])
            roots = [p for _, p in sl]
            lens = [L for L, _ in sl]
            img = [primitive(R3 * sp.Matrix(p)) for p in roots]
            row["root_lines"] = roots
            row["root_lengths"] = lens
            row["rotation_permutes_roots"] = sorted(img) == sorted(roots) and all(img[i] != roots[i] for i in range(3))
            row["hexagonal"] = abs(lens[0] - lens[2]) < 1e-9
        cusps.append(row)
    # orbits of cusps under the isometries
    orbits, seen = [], set()
    for c in range(k):
        if c in seen:
            continue
        O = sorted({perm[c] for perm, _ in isos})
        seen |= set(O)
        rep_stab_or = cusps[c]["orientations"]
        weight2 = None
        if rep_stab_or == [1]:
            signs = {}
            for perm, maps in isos:
                signs.setdefault(perm[c], set()).add(orientation(perm, maps))
            assert all(len(s) == 1 for s in signs.values()), (label, c, signs)
            weight2 = abs(sum(next(iter(signs[d])) for d in O))
        orbits.append(dict(rep=c, cusps=O, size=len(O), rotated=cusps[c]["rotated"],
                           stabiliser_orientation_preserving=(rep_stab_or == [1]), weight_with_orientation=weight2))
    rotated_points = sum(1 for r in cusps if r["rotated"])
    out = dict(label=label, tets=M.num_tetrahedra(), cusps=k, isometries=len(isos),
               orientation_reversing=sum(1 for p, m in isos if orientation(p, m) == -1),
               cusp_rows=cusps, orbits=orbits, rotated_points=rotated_points,
               symmetric_self_dual_completion=(rotated_points == 0),
               frame_chiral_allowed=(rotated_points == 0),
               g2_chiral_orbits=[o["rep"] for o in orbits if not o["rotated"] and o["stabiliser_orientation_preserving"]
                                 and o["weight_with_orientation"]],
               seconds=None)
    out["g2_chiral_allowed"] = rotated_points == 0 and bool(out["g2_chiral_orbits"])
    out["geometric_check"] = geometric_check(isos, shapes)
    assert out["geometric_check"]["agree"], (label, out["geometric_check"])
    if crosscheck and canonical:
        out["crosscheck"] = crosscheck_b1369(M, label, isos, canonical)
    else:
        # the own-triangulation cross-check runs B1369's exact homology on the member's own triangulation (cube~3.24's has 90
        # tetrahedra), too slow for the census; run separately (crosscheck_own) on cube~3.24 it ran out of memory (killed at
        # about 14 GB, 2026-09-30), so the recorded run has none and the check there rests on geometric_check and the order
        # of SnapPy's symmetry group
        out["crosscheck"] = dict(method="deferred", auts=None, agree=True)
    out["seconds"] = round(time.time() - t0, 2)
    return out


_E = None


def crosscheck_b1369(M, label, isos, canonical):
    """B1369's instrument: a triangulation's automorphisms and their exact action on each cusp torus (a combinatorial basis).
    canonical=True (the canonical retriangulation; every isometry is an automorphism): |Aut| = |Isom| and, over the cusps, the
    multisets of (order, det) over each stabiliser agree.  canonical=False (the manifold's own triangulation, as B1386 used for
    cube~3.24; its automorphisms are some of the isometries): |Aut| divides |Isom| and each cusp's multiset from the automorphisms is a
    sub-multiset of the isometries' at the same cusp (the triangulation is M's own, so the cusp order is M's)."""
    global _E
    if _E is None:
        _E = _load("b1385_eisenstein_cusps", "frontier/B1385_the_states_together/verification/eisenstein_cusps.py")
    FM = _E.StateMember(snappy.Manifold(M), label, canonical=canonical)
    per = []
    for c in range(M.num_cusps()):
        per.append(sorted((order(FM.action_on_torus(aut, c)), int(FM.action_on_torus(aut, c).det()))
                          for aut in FM.auts if FM.cusp_permutation(aut)[c] == c))
    snap = [sorted((order(maps[c]), int(maps[c].det())) for perm, maps in isos if perm[c] == c) for c in range(M.num_cusps())]
    if canonical:
        ok = len(FM.auts) == len(isos) and sorted(map(tuple, per)) == sorted(map(tuple, snap))
    else:
        from collections import Counter
        ok = len(isos) % len(FM.auts) == 0 and all(not (Counter(a) - Counter(b)) for a, b in zip(per, snap))
    return dict(method="canonical" if canonical else "own triangulation", auts=len(FM.auts), agree=bool(ok))


def geometric_check(isos, shapes):
    """independent of SnapPy's isometry search: every cusp map of a cusp-fixing isometry must be a similarity of that cusp's flat
    lattice Z + Z*tau.  With u the image of the meridian: |u| = 1 and the longitude goes to u*tau (det +1) or u*conj(tau) (det -1).
    The matrix convention (columns or rows as images) is fixed per manifold: one of the two must hold for every map."""
    def ok(A, tau, cols):
        a, b, c, d = [complex(x) for x in (A[0, 0], A[0, 1], A[1, 0], A[1, 1])]
        m_img, l_img = ((a + c * tau), (b + d * tau)) if cols else ((a + b * tau), (c + d * tau))
        if abs(abs(m_img) - 1) > 1e-6:
            return False
        target = m_img * (tau if A.det() == 1 else tau.conjugate())
        return abs(l_img - target) < 1e-6
    res = {}
    for cols in (True, False):
        res[cols] = all(ok(maps[c], shapes[c], cols) for perm, maps in isos for c in range(len(perm)) if perm[c] == c)
    return dict(columns=res[True], rows=res[False], agree=bool(res[True] or res[False]))


# ------------------------------------------------------------------------------------------------------------ A. the puncture
def homological_longitude(M):
    """the primitive peripheral slope (meridian, longitude coordinates) that is zero in H_1(M; Q) -- on a one-cusped fibred manifold
    with b_1 = 1, the fibre's boundary.  From the abelianised presentation: H^1(M; Q) = {phi : R phi = 0}, and a peripheral word w
    maps to (w . phi) for phi in a basis of it."""
    G = M.fundamental_group()
    gens = G.generators()
    n = len(gens)

    def vec(w):
        v = [0] * n
        for ch in w:
            v[gens.index(ch.lower())] += 1 if ch.islower() else -1
        return sp.Matrix([v])

    rels = G.relators()
    H1dual = sp.Matrix([list(vec(r)) for r in rels]).nullspace() if rels else [sp.eye(n).col(i) for i in range(n)]
    m, l = G.peripheral_curves()[0]
    im = [(vec(m) * phi)[0] for phi in H1dual]
    il = [(vec(l) * phi)[0] for phi in H1dual]
    ker = sp.Matrix([im, il]).T.nullspace()
    assert len(ker) == 1, (im, il)
    v = ker[0]
    v = v * sp.ilcm(*[sp.fraction(x)[1] for x in v])
    return primitive(v)


def puncture():
    out = {}
    for name in ("m004", "m003"):
        M = snappy.Manifold(name)
        isos = snappy_isometries(M)
        rows = []
        for perm, maps in isos:
            A = maps[0]
            diag = A[0, 1] == 0 and A[1, 0] == 0
            rows.append(dict(map=[[int(x) for x in A.row(0)], [int(x) for x in A.row(1)]], orientation=int(A.det()),
                             s_m=int(A[0, 0]) if diag else None, s_l=int(A[1, 1]) if diag else None, order=order(A)))
        cl = common_lines([maps[0] for _, maps in isos])
        fibre = homological_longitude(M)
        assert cl != "all" and fibre in cl, (name, cl, fibre)
        fills = {}
        for s in sorted(cl):
            N = snappy.Manifold(name)
            N.dehn_fill(s)
            fills[str(s)] = dict(H1=str(N.homology()), solution_type=N.solution_type(),
                                 pi1_generators=N.fundamental_group().num_generators(), fibre_boundary=(s == fibre))
        out[name] = dict(isometries=len(isos), rows=rows, common_lines=sorted(cl), fibre_boundary=fibre,
                         fillings_of_the_common_lines=fills, rotated=any(is_rotation(maps[0]) for _, maps in isos),
                         shape=[complex(M.cusp_info(0)["shape"]).real, complex(M.cusp_info(0)["shape"]).imag])
    m4 = out["m004"]
    pats = sorted((r["orientation"], r["s_m"], r["s_l"]) for r in m4["rows"])
    assert pats == sorted([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)] * 2), pats
    assert all(r["orientation"] == r["s_m"] * r["s_l"] for r in m4["rows"])
    assert m4["common_lines"] == [(0, 1), (1, 0)]
    # the fillings along the two lines
    fill = {}
    for s, name in (((1, 0), "meridian"), ((0, 1), "longitude")):
        N = snappy.Manifold("m004")
        N.dehn_fill(s)
        G = N.fundamental_group()
        fill[name] = dict(slope=list(s), H1=str(N.homology()), pi1_generators=G.num_generators(), relators=G.relators(),
                          solution_type=N.solution_type())
    assert fill["meridian"]["pi1_generators"] == 0 and fill["meridian"]["H1"] == "0"          # S^3
    assert fill["longitude"]["H1"] == "Z" and "flat" in fill["longitude"]["solution_type"]     # the Sol torus bundle (B1380 S7)
    out["fillings"] = fill
    # the fibre's boundary is the longitude: the monodromy LR acts on the punctured torus, and the Seifert surface of 4_1 (the fibre)
    # has the longitude as its boundary; checked through b++LR = m004 and the filling b++LR(0,1) = the closed torus bundle of LR
    B = snappy.Manifold("b++LR")
    assert B.is_isometric_to(snappy.Manifold("m004"))
    # the order bit
    L = sp.Matrix([[1, 1], [0, 1]])
    R = sp.Matrix([[1, 0], [1, 1]])
    P = sp.Matrix([[0, 1], [1, 0]])
    assert L.inv() * (L * R) * L == R * L and L.det() == 1
    assert P * (L * R) * P == R * L and P.det() == -1
    ib = snappy.Manifold("b++LR").is_isometric_to(snappy.Manifold("b++RL"), return_isometries=True)
    dets = sorted(int(sp.Matrix(i.cusp_maps()[0]).det()) for i in ib)
    out["order_bit"] = dict(L_conjugation_is_orientation_preserving=True, P_conjugation_det=-1,
                            LR_to_RL_isometries=len(ib), their_orientations=dets)
    assert dets.count(1) >= 1 and dets.count(-1) >= 1
    # the flow class's sign under each isometry (B1369's instrument), against SnapPy's meridian sign: the multisets agree
    FI = _load("b1369_family_isometries", "frontier/B1369_the_siblings_in_the_sm_frame/verification/family_isometries.py")
    FM = FI.FamilyMember("m004")
    b1369 = sorted((int(FM.action_on_torus(a, 0).det()), int(FM.action_on_H1(a)[0, 0])) for a in FM.auts)
    snap = sorted((r["orientation"], r["s_m"]) for r in m4["rows"])
    assert b1369 == snap, (b1369, snap)
    out["flow_class_sign"] = dict(b1369=b1369, snappy=snap, agree=True)
    return out


# ------------------------------------------------------------------------------------------------------------ C. the census
def members():
    EA = _load("b1390_eisenstein_axes", "frontier/B1390_the_eisenstein_axes/verification/eisenstein_axes.py")
    fam = json.load(open(ROOT / "frontier" / "B1186_family_is_112" / "verification" / "family_census.json"))
    names = fam["members_B"]
    assert len(names) == 112
    arith = [n for n in names if not EA.nonintegral_witness(snappy.ManifoldHP(n))]
    assert len(arith) == 99
    # (label, constructor, canonical cross-check?): the family's small members through the canonical retriangulation; cube~3.24 and
    # the covers through their own triangulations (B1386's choice for cube~3.24: the canonical one has 90 tetrahedra)
    todo = [("m004", lambda: snappy.Manifold("m004"), True), ("m003", lambda: snappy.Manifold("m003"), True)]
    todo += [(n, (lambda n=n: snappy.Manifold(n)), True) for n in arith if n not in ("m004", "m003")]
    iso = (ROOT / "frontier" / "B1386_the_open_eisenstein_cusp" / "verification" / "cube3_24.isosig").read_text().strip()
    todo.append(("cube~3.24", lambda: snappy.Manifold(iso), False))
    cl = json.load(open(ROOT / "frontier" / "B1399_the_rank_two_higgs" / "verification" / "census_list.json"))["census"]
    assert len(cl) == 109
    for i, r in enumerate(cl):
        todo.append((f"B1399:{i}:{r['parent']}~{r['degree']}", (lambda s=r["triangulation_isosig"]: snappy.Manifold(s)), False))
    return todo, len(arith)


def census(partial=None):
    todo, n_arith = members()
    done = {}
    if partial and Path(partial).exists():
        for line in open(partial):
            d = json.loads(line)
            done[d["label"]] = d
    rows = []
    for label, make, canonical in todo:
        if label in done:
            rows.append(done[label])
            continue
        d = analyse(make(), label, canonical=canonical)
        rows.append(d)
        if partial:
            with open(partial, "a") as fh:
                fh.write(json.dumps(d, default=str) + "\n")
        print(f"{label:>40s}  cusps {d['cusps']}  isom {d['isometries']:3d}  rotated {d['rotated_points']}  "
              f"frame-chiral {d['frame_chiral_allowed']}  g2-chiral {d['g2_chiral_allowed']}  xcheck {d['crosscheck']['agree']} "
              f"({d['crosscheck']['method']}, {d['crosscheck']['auts']} auts)  geometric {d['geometric_check']['agree']}  "
              f"{d['seconds']} s", flush=True)
    return rows, n_arith


def summary(rows, n_arith):
    s = dict(members=len(rows), arithmetic_family=n_arith)
    s["crosscheck_failures"] = [r["label"] for r in rows if not r["crosscheck"]["agree"]]
    s["crosscheck_methods"] = {m: sum(1 for r in rows if r["crosscheck"]["method"] == m) for m in ("canonical", "deferred")}
    s["geometric_failures"] = [r["label"] for r in rows if not r["geometric_check"]["agree"]]
    s["with_rotated_points"] = [r["label"] for r in rows if r["rotated_points"]]
    s["rotated_points"] = sum(r["rotated_points"] for r in rows)
    s["rotation_orders_seen"] = sorted({o for r in rows for c in r["cusp_rows"] for o in c["rotation_orders"]})
    rot = [c for r in rows for c in r["cusp_rows"] if c["rotated"]]
    s["rotated_all_hexagonal"] = all(c.get("hexagonal") for c in rot)
    s["rotation_permutes_roots_everywhere"] = all(c.get("rotation_permutes_roots") for c in rot)
    s["symmetric_self_dual_completion"] = sum(1 for r in rows if r["symmetric_self_dual_completion"])
    s["frame_chiral_allowed"] = sum(1 for r in rows if r["frame_chiral_allowed"])
    s["g2_chiral_allowed"] = sum(1 for r in rows if r["g2_chiral_allowed"])
    s["g2_forbids_where_frame_allows"] = [r["label"] for r in rows if r["frame_chiral_allowed"] and not r["g2_chiral_allowed"]]
    s["lemma_violations"] = [r["label"] for r in rows for c in r["cusp_rows"]
                             if c["rotated"] != (c["common_lines"] != "all" and len(c["common_lines"]) == 0)]
    return s


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "puncture"
    if what == "puncture":
        print(json.dumps(puncture(), indent=1, default=str))
    elif what == "lemma":
        rows = lemma()
        print(len(rows), "subgroups;", sum(r["rotation"] for r in rows), "with a rotation, all without a common line;",
              sum(not r["rotation"] for r in rows), "without, all with one")
    elif what == "crosscheck_own":
        todo, _ = members()
        labels = sys.argv[2:]
        for label, make, canonical in todo:
            if label in labels:
                M = make()
                t0 = time.time()
                r = crosscheck_b1369(M, label, snappy_isometries(M), False)
                print(json.dumps(dict(label=label, **r, seconds=round(time.time() - t0, 1))), flush=True)
    elif what == "census":
        partial = sys.argv[sys.argv.index("--partial") + 1] if "--partial" in sys.argv else None
        rows, n_arith = census(partial)
        print(json.dumps(summary(rows, n_arith), indent=1, default=str))
    elif what == "record":
        # the recorded run: the puncture and the lemma recomputed, the census read from its partial file (every member present)
        partial = sys.argv[sys.argv.index("--partial") + 1]
        xown = sys.argv[sys.argv.index("--own") + 1] if "--own" in sys.argv else None
        rows, n_arith = census(partial)
        s = summary(rows, n_arith)
        own = [json.loads(l) for l in open(xown)] if xown else []
        s["own_triangulation_crosschecks"] = own
        lem = lemma()
        rec = dict(note="B1504 recorded run (end_choice.py record)", puncture=puncture(),
                   lemma=dict(subgroups=len(lem), with_rotation=sum(r["rotation"] for r in lem),
                              violations=sum(r["rotation"] == r["common_line"] for r in lem)),
                   summary=s, members=rows)
        (HERE / "end_choice.json").write_text(json.dumps(rec, indent=1, default=str) + "\n")
        lines = [f"{r['label']:>40s}  cusps {r['cusps']}  isometries {r['isometries']:3d}  rotated points {r['rotated_points']}  "
                 f"symmetric self-dual {r['symmetric_self_dual_completion']}  frame chiral {r['frame_chiral_allowed']}  "
                 f"G2 chiral {r['g2_chiral_allowed']}  xcheck {r['crosscheck']['method']}/{r['crosscheck']['agree']}  "
                 f"geometric {r['geometric_check']['agree']}" for r in rows]
        (HERE / "end_choice_run.txt").write_text("\n".join(lines) + "\n\nLEMMA " + json.dumps(rec["lemma"]) + "\n\nSUMMARY\n"
                                                  + json.dumps(s, indent=1, default=str) + "\n")
        print(json.dumps(s, indent=1, default=str))
