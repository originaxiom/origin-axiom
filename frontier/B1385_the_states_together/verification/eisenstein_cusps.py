#!/usr/bin/env python3
"""B1385 S8 -- the Eisenstein cusps of the class: where, in the figure-eight's commensurability class, is a free cusp hexagonal, fixed
by an isometry that rotates it by order three, with a Higgs class that the rotation fixes and no isometry fixing the cusp negates?

On such a cusp the Eisenstein cusp lemma (S7, eisenstein_partition.py) makes the leading shell three-fold symmetric and the partition
never annular: N = -+1 for every phase of the leading coefficient but six, provided the coefficient is non-zero and the shell is not
killed by a translation part.  B1369's instrument (family_isometries.py: the canonical retriangulation's automorphisms with their exact
action on H_1(M; Q), on ann(P_c) and on the cusp torus) is reused unchanged; a thin subclass accepts a SnapPy manifold (a cover) in
place of a census name.

For every free cusp c (rank P_c < b_1): the fixers of c, their torus types, the order-3 rotations R among them (and the squares of
order-6 ones), V = ann(P_c) fixed by every R, and whether one fixer negates all of V (B1369's parity on V; if none does, a generic
class of V is parity-open).  The transfer lemma is asserted on every such cusp: a class fixed by R vanishes on the cusp's peripheral
image automatically (for x in P_c, 3 f(x) = f(x + Rx + R^2 x) = 0), so V = H^1(M; Q)^R = H^1(M/<R>; Q), the first Betti number of
the rotation's quotient orbifold.  L3, the global parity, is applied last: an isometry of M anywhere that negates the class maps
the partition at each cusp onto the negated partition at its image cusp, so the total index vanishes; a cusp is *open* only if no
isometry of M negates its invariant class.  Run on (a) the 112 members of B1186's family, (b) the covers of m004 and m003 of degree 5 to D and the double covers of the
family's three rotation-carrying members (o10_150704, o10_150725, o10_150729).
Usage: python3 eisenstein_cusps.py [D] [family,covers,rot725,rotother]   (default D = 6, all parts; the parts run independently)"""
import importlib.util
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import sympy as sp
import snappy
from snappy.snap import t3mlite

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
_spec = importlib.util.spec_from_file_location(
    "b1369_family_isometries", ROOT / "frontier" / "B1369_the_siblings_in_the_sm_frame" / "verification" / "family_isometries.py")
FI = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(FI)


class StateMember(FI.FamilyMember):
    """B1369's FamilyMember on a SnapPy manifold object (a cover has no census name)"""

    def __init__(self, M, label, canonical=True):
        self.name = label
        self.M = M
        self.T = M.canonical_retriangulation() if canonical else M
        self.mc = t3mlite.Mcomplex(self.T)
        self.cusp_idx = self.T._get_cusp_indices_and_peripheral_curve_data()[0]
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


def order(At):
    I2 = sp.eye(2)
    for k in (1, 2, 3, 4, 6):
        if At ** k == I2:
            return k
    return 0


def eisenstein_analysis(FM):
    rows = []
    for c in range(FM.num_cusps):
        cd = FM.cusp[c]
        if cd['free'] == 0:
            continue
        data = []
        for a in FM.auts:
            if FM.cusp_permutation(a)[c] != c:
                continue
            A = FM.action_on_H1(a)
            At = FM.action_on_torus(a, c)
            data.append((A, At))
        rots = []
        for A, At in data:
            if At.det() == 1 and order(At) == 3:
                rots.append(A)
            if At.det() == 1 and order(At) == 6:
                rots.append(A * A)
        annM = sp.Matrix.hstack(*cd['ann'])
        V = []
        if rots:
            stack = sp.Matrix.vstack(*[(Ar.T - sp.eye(FM.b1)) * annM for Ar in rots])
            V = [annM * v for v in stack.nullspace()]
            # the transfer lemma: every class fixed by an order-3 rotation of the cusp vanishes on P_c (1 + R + R^2 = 0 on the torus),
            # so Fix(R) on all of H^1(M; Q) -- H^1 of the quotient orbifold M/<R> -- already lies in ann(P_c)
            full = sp.Matrix.vstack(*[(Ar.T - sp.eye(FM.b1)) for Ar in rots]).nullspace()
            assert len(full) == len(V), "an order-3-invariant class that does not vanish on the cusp"
        negators = [At for A, At in data if V and all(A.T * v + v == sp.zeros(FM.b1, 1) for v in V)]
        # L3, the global parity: an isometry of M anywhere (fixing c or not) that negates the class forces the total index to 0
        global_neg = []
        if V:
            for a in FM.auts:
                A = FM.action_on_H1(a)
                if all(A.T * v + v == sp.zeros(FM.b1, 1) for v in V):
                    global_neg.append((FM.cusp_permutation(a), sorted(FM.aut_sign(a))))
        types = sorted(set(FM.torus_type(At) + ("" if At.det() == 1 else "*") for A, At in data))
        rows.append(dict(cusp=c, free=cd['free'], fixers=len(data), torus_types=types, rotation3=bool(rots), dimV=len(V),
                         V_negated_by_one_fixer=bool(negators), locally_open=bool(V) and not negators,
                         negated_globally=bool(global_neg), open=bool(V) and not negators and not global_neg))
    return rows


def run_family():
    fam = json.load(open(ROOT / "frontier" / "B1186_family_is_112" / "verification" / "family_census.json"))
    out = {}
    for name in fam['members_B']:
        M = snappy.Manifold(name)
        FM = StateMember(M, name)
        rows = eisenstein_analysis(FM)
        if rows:
            out[name] = rows
    return out


def run_covers(parents=("m004", "m003"), degrees=range(5, 8)):
    out = {}
    for P in parents:
        base = snappy.Manifold(P)
        for d in (degrees if not isinstance(degrees, dict) else degrees[P]):
            for i, C in enumerate(base.covers(d)):
                label = "%s~%d.%d" % (P, d, i)
                try:
                    FM = StateMember(C, label)
                except Exception as e:                    # a canonical retriangulation SnapPy cannot give: reported, not skipped
                    out[label] = "instrument failed: %s" % str(e)[:60]
                    continue
                rows = eisenstein_analysis(FM)
                if rows:
                    out[label] = dict(cusps=C.num_cusps(), H1=str(C.homology()), b1=FM.b1, rows=rows)
    return out


def report(cov):
    for k, v in cov.items():
        if isinstance(v, str):
            print("S8(b)", k, v, flush=True)
            continue
        for r in v['rows']:
            print("S8(b) %-16s cusps %d H1 %-22s b1 %d | cusp %d free %d fixers %d types %s rot3 %s dimV %d negated-at-cusp %s "
                  "locally-open %s negated-globally %s open %s" % (
                      k, v['cusps'], v['H1'], v['b1'], r['cusp'], r['free'], r['fixers'], r['torus_types'], r['rotation3'],
                      r['dimV'], r['V_negated_by_one_fixer'], r['locally_open'], r['negated_globally'], r['open']), flush=True)


if __name__ == "__main__":
    D = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    parts = sys.argv[2].split(",") if len(sys.argv) > 2 else ["family", "covers", "rot725", "rotother"]
    if "family" in parts:
        fam = run_family()
        nfree = sum(len(v) for v in fam.values())
        rot = [(k, r['cusp'], r['dimV'], r['V_negated_by_one_fixer'], r['negated_globally']) for k, v in fam.items() for r in v
               if r['rotation3']]
        opn = [(k, r['cusp']) for k, v in fam.items() for r in v if r['open']]
        print("S8(a) B1186's family: %d free cusps on %d members; with an order-3 rotation fixing the cusp: %d "
              "(member, cusp, dim V, negated at the cusp, negated globally) %s; open Eisenstein cusps: %s" % (
                  nfree, len(fam), len(rot), rot, opn), flush=True)
    if "covers" in parts:
        report(run_covers(degrees=range(5, D + 1)))
    if "rot725" in parts:
        report(run_covers(parents=("o10_150725",), degrees={"o10_150725": (2, 3)}))
    if "rotother" in parts:
        report(run_covers(parents=("o10_150704", "o10_150729"), degrees={"o10_150704": (2,), "o10_150729": (2,)}))
    print("DONE", parts, flush=True)
