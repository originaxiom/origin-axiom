#!/usr/bin/env python3
"""B1386 S1 -- the search for an open Eisenstein cusp (sL-6), one level above B1385's nearest miss.

B1385 (S9, the ε analysis) located the target: on o10_150725 every isometry acts on the rotation-invariant class by
ε = (orientation) x (cusp-swap), and every cover it searched inherited an isometry with ε = -1; its nearest miss, ocube06_08812
(o10_150725's degree-3 cover no. 4), is chiral with two locally open Eisenstein cusps that an orientation-preserving swap closes.  Here
every cover of ocube06_08812 of degree 2 and 3 is searched:

(a) the rotation filter (SnapPy's symmetry groups and cusp maps): which covers have an isometry fixing a cusp and acting on its torus
    with linear part of order 3 (det 1, trace -1) or 6 (det 1, trace 1);
(b) on each, B1385's Eisenstein analysis (B1369's instrument unchanged, through B1385's thin subclass): for every free rotation cusp,
    V = H^1(M; Q)^R (the transfer lemma asserted), whether a fixer negates V (B1369's parity), whether any isometry of the manifold
    negates V (L3), and the verdict *open* = neither.  The instrument runs on the cover's own triangulation when that realises the whole
    isometry group (it does on every cover here: the lifted triangulation is geometric and its automorphisms number |Isom|), else on
    the canonical retriangulation.

Usage: python3 eisenstein_search.py filter D            (the rotation filter on the degree-D covers)
       python3 eisenstein_search.py analyse D i,j,...   (the Eisenstein analysis on the listed degree-D covers)
       python3 eisenstein_search.py classes D i,j,...   (the listed covers sorted into isometry classes)"""
import sys
import time
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import snappy
from snappy.snap import t3mlite

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "frontier" / "B1385_the_states_together" / "verification"))
import eisenstein_cusps as E


def base():
    """ocube06_08812 = o10_150725's degree-3 cover no. 4 (B1385 S9)"""
    return snappy.Manifold("o10_150725").covers(3)[4]


def _order(m, trace):
    a, b, c, d = int(m[0, 0]), int(m[0, 1]), int(m[1, 0]), int(m[1, 1])
    return a * d - b * c == 1 and a + d == trace


def rotation_cusps(M):
    G = M.symmetry_group()
    out = set()
    for iso in G.isometries():
        maps = iso.cusp_maps()
        for c, img in enumerate(iso.cusp_images()):
            if img == c and (_order(maps[c], -1) or _order(maps[c], 1)):
                out.add(c)
    return sorted(out), G.order(), G.is_amphicheiral()


def run_filter(d):
    covs = base().covers(d)
    hits = []
    for i, C in enumerate(covs):
        rc, order, amph = rotation_cusps(C)
        if rc:
            hits.append(i)
            print("  cube~%d.%d %s cusps %d |Isom| %d amphichiral %s rotation cusps %s" % (
                d, i, C.cover_info()["type"], C.num_cusps(), order, amph, rc), flush=True)
    print("S1(a) degree %d: %d covers, %d with a rotated cusp: %s" % (d, len(covs), len(hits), hits), flush=True)
    return len(covs), hits


def analyse(C, label):
    G = C.symmetry_group()
    own = len(t3mlite.Mcomplex(C).isomorphisms_to(t3mlite.Mcomplex(C)))
    canonical = not (own == G.order() and C.solution_type() == "all tetrahedra positively oriented")
    FM = E.StateMember(C, label, canonical=canonical)
    assert len(FM.auts) == G.order(), "the triangulation must realise the whole isometry group"
    rows = E.eisenstein_analysis(FM)
    rot = [r for r in rows if r["rotation3"]]
    return dict(type=C.cover_info()["type"], cusps=C.num_cusps(), H1=str(C.homology()), b1=FM.b1, isometries=G.order(),
                amphichiral=G.is_amphicheiral(), triangulation="canonical" if canonical else "own", free=len(rows),
                rot=[(r["cusp"], r["dimV"], r["V_negated_by_one_fixer"], r["negated_globally"], r["open"]) for r in rot])


def run_analyse(d, idx):
    covs = base().covers(d)
    out = {}
    for i in idx:
        t = time.time()
        r = analyse(covs[i], "cube~%d.%d" % (d, i))
        out[i] = r
        print("  cube~%d.%d %s cusps %d H1 %s |Isom| %d amphichiral %s (%s triangulation) free cusps %d | rotation cusps "
              "(cusp, dim V, negated at the cusp, negated globally, OPEN): %s (%.0fs)" % (
                  d, i, r["type"], r["cusps"], r["H1"], r["isometries"], r["amphichiral"], r["triangulation"], r["free"],
                  r["rot"], time.time() - t), flush=True)
    return out


def isometry_classes(d, idx):
    """the listed degree-d covers sorted into isometry classes (SnapPy's is_isometric_to)"""
    covs = base().covers(d)
    classes = []
    for i in idx:
        for cl in classes:
            if covs[i].is_isometric_to(covs[cl[0]]):
                cl.append(i)
                break
        else:
            classes.append([i])
    print("S1(c) isometry classes among the degree-%d covers %s: %s" % (d, idx, classes), flush=True)
    return classes


if __name__ == "__main__":
    mode, d = sys.argv[1], int(sys.argv[2])
    if mode == "filter":
        run_filter(d)
    elif mode == "classes":
        isometry_classes(d, [int(x) for x in sys.argv[3].split(",")])
    else:
        run_analyse(d, [int(x) for x in sys.argv[3].split(",")])
    print("DONE", sys.argv[1:], flush=True)
