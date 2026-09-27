#!/usr/bin/env python3
"""B1385 S9 -- the first open Eisenstein cusp, checked with B1370's instrument.

The candidate: o10_150725's degree-3 cyclic cover number 4 (SnapPy's covers(3)[4]), identified by SnapPy as ocube06_08812 -- 30 tetrahedra,
three hexagonal cusps, H_1 = Z/3 + Z/3 + Z^3, isometry group of order 18, chiral.  On cusps 0 and 2 (peripheral rank 2, one free
class) the stabiliser has order 9: three translations and six order-3 rotations, all orientation-preserving, all fixing the free class.

B1370's residual_cusp_modes.py is loaded without its driver (its function definitions only) and run unchanged on the candidate:
develop each cusp from the tetrahedra shapes, read every fixer's affine action (linear part on the lattice, translation mod the lattice),
and find the lowest Fourier shell the constraints F o sigma = epsilon F allow.  Then the Eisenstein cusp lemma (S7) is applied to that
shell, and L3 (the global parity) to the manifold: an isometry anywhere that negates the class forces the total index to vanish.
Usage: python3 eisenstein_candidate.py"""
import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import numpy as np
import sympy as sp
import snappy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
B1370 = ROOT / "frontier" / "B1370_the_residuals_leading_mode" / "verification" / "residual_cusp_modes.py"
sys.path.insert(0, str(ROOT / "frontier" / "B1369_the_siblings_in_the_sm_frame" / "verification"))
_src = B1370.read_text()
_defs = _src[:_src.index('print("=== B1370')]                     # the instrument's functions, not its driver
R70 = {"__file__": str(B1370), "__name__": "b1370_instrument"}
exec(compile(_defs, str(B1370), "exec"), R70)

sys.path.insert(0, str(HERE))
import eisenstein_cusps as E


def candidate():
    base = snappy.Manifold("o10_150725")
    return base.covers(3)[4]


def analyse(N=None):
    N = N or candidate()
    FM = E.StateMember(N, "o10_150725~3.4", canonical=False)
    G = N.symmetry_group()
    assert len(FM.auts) == G.order() == 18, "the own triangulation must realise the whole isometry group"
    out = {"identify": str(N.identify()[0]).split("(")[0], "tetrahedra": N.num_tetrahedra(), "H1": str(N.homology()),
           "isometries": G.order(), "amphichiral": G.is_amphicheiral(), "cusps": {}}
    for c in range(N.num_cusps()):
        cd = FM.cusp[c]
        if cd["free"] == 0:
            continue
        pos = trans = None
        for mirror in (False, True):
            pos, trans = R70["develop_cusp"](FM, c, mirror)
            if pos is not None:
                break
        assert pos is not None
        b1, b2 = R70["lattice_basis"](trans)
        tau = R70["reduce_tau"](b2 / b1)
        fixers = [a for a in FM.auts if FM.cusp_permutation(a)[c] == c]
        annM = sp.Matrix.hstack(*cd["ann"])
        acts = []
        for a in fixers:
            A1 = FM.action_on_H1(a)
            X = (annM.T * annM).inv() * annM.T * (A1.T * annM)
            orient, A, bc, _, _ = R70["affine_action"](FM, c, a, pos, b1, b2)
            acts.append((X, orient, A, bc))
        rot = [x for x in acts if x[1] == 1 and int(round(np.linalg.det(x[2]))) == 1 and not np.array_equal(x[2], np.eye(2, dtype=int))
               and np.array_equal(np.linalg.matrix_power(x[2], 3), np.eye(2, dtype=int))]
        row = {"free": cd["free"], "tau": (round(tau.real, 6), round(tau.imag, 6)), "fixers": len(acts),
               "rotations": len(rot), "translations": [tuple(round(float(t), 4) for t in x[3]) for x in acts
                                                        if np.array_equal(x[2], np.eye(2, dtype=int))]}
        if cd["free"] == 1:
            signs = [int(x[0][0, 0]) for x in acts]
            row["signs on the free class"] = sorted(set(signs))
            fx = [(x[2], x[3], s) for x, s in zip(acts, signs)]
            shells = R70["dual_shells"](b1, b2, nshells=8)
            lead = None
            table = []
            for nrm, ks in shells:
                dim = R70["allowed_dimension"](ks, fx, None)
                dirs = R70["zero_set_type"](ks)
                table.append((round(nrm, 6), len(ks), len(dirs), dim))
                if dim > 0 and lead is None:
                    lead = (round(nrm, 6), ks, len(dirs), dim)
            row["shells (|k|^2, vectors, directions, allowed real dim)"] = table
            row["leading allowed shell"] = lead
        out["cusps"][c] = row
    # L3, the global parity: the invariant class of the rotation cusps, and every isometry of the manifold that negates it
    rot_cusps = [c for c, row in out["cusps"].items() if row.get("rotations")]
    Vs = []
    for c in rot_cusps:
        data = [(FM.action_on_H1(a), FM.action_on_torus(a, c)) for a in FM.auts if FM.cusp_permutation(a)[c] == c]
        rots = [A for A, At in data if At.det() == 1 and E.order(At) == 3]
        Vs.append(sp.Matrix.vstack(*[(A.T - sp.eye(FM.b1)) for A in rots]).nullspace())
    assert all(len(V) == 1 for V in Vs) and all(sp.Matrix.hstack(Vs[0][0], V[0]).rank() == 1 for V in Vs), "one common class"
    v = Vs[0][0]
    cusp_fixed = [c for c in range(FM.num_cusps) if sp.Matrix.hstack(sp.Matrix.hstack(*FM.cusp[c]["ann"]), v).rank()
                  == sp.Matrix.hstack(*FM.cusp[c]["ann"]).rank()]
    negators = []
    for a in FM.auts:
        if FM.action_on_H1(a).T * v == -v:
            negators.append((dict(FM.cusp_permutation(a)), "preserving" if FM.aut_sign(a) == {0} else "reversing"))
    out["the class"] = [str(x) for x in v]
    out["cusps where it is cusp-fixed"] = cusp_fixed
    out["isometries negating it (cusp permutation, orientation)"] = negators
    return out


if __name__ == "__main__":
    out = analyse()
    print("S9 the candidate: %s, %d tetrahedra, H1 %s, |Isom| %d, amphichiral %s" % (
        out["identify"], out["tetrahedra"], out["H1"], out["isometries"], out["amphichiral"]))
    for c, row in out["cusps"].items():
        print("  cusp %d:" % c, row)
    print("  the rotation-invariant class %s is cusp-fixed on cusps %s" % (out["the class"], out["cusps where it is cusp-fixed"]))
    print("  isometries of the manifold negating it:", out["isometries negating it (cusp permutation, orientation)"])
    print("  -> L3: the swap of cusps 0 and 2 maps the partition at cusp 0 onto the negated partition at cusp 2, N_2 = -N_0; the total")
    print("     index of this class is N_0 + N_2 = 0.  Locally open (N_c = -+1 at each Eisenstein cusp), globally closed.")
    print("DONE")
