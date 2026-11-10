#!/usr/bin/env python3
"""What a departure does to the symmetries of the golden ground (SnapPy; data-free).
For the golden background with k periods and for histories carrying one departure: the order of the symmetry group,
whether the manifold is amphicheiral, and whether the history with the departure on L is the mirror image of the one
with the departure on R.
    python3 relays/advisor_2026-11-10_audit/principle_top_down/symmetry_facts.py"""
import warnings; warnings.filterwarnings("ignore")
import snappy
swap = lambda w: w.translate(str.maketrans("LR", "RL"))
def info(w):
    M = snappy.Manifold("b++" + w); G = M.symmetry_group()
    return "b++%-14s volume %.6f  H1 %-18s symmetries %-3d full group %-5s amphicheiral %s" % (
        w, float(M.volume()), M.homology(), G.order(), G.is_full_group(), G.is_amphicheiral())
print("the ground")
for name, w in (("golden, 1 period", "LR"), ("golden, 2 periods", "LRLR"), ("golden, 4 periods", "LRLRLRLR")):
    print("  %-30s %s" % (name, info(w)))
print("one departure, closed by one golden period")
for name, w in (("(6)", "LLLLLLRLR"), ("(2,2,2)", "LLRRLLRLR"), ("(2,1,1,1,2)", "LLRLRLLRLR"),
                ("(2,1,2,1,2)", "LLRLLRLLRLR"), ("(2,3), not a palindrome", "LLRRRLR")):
    print("  %-30s %s" % (name, info(w)))
print("(6) closed by two golden periods")
print("  %-30s %s" % ("(6), k = 2", info("LLLLLLRLRLR")))
print("the departure on L against the departure on R")
for w in ("LLLLLLRLR", "LLRRLLRLR", "LLRRRLR"):
    A = snappy.Manifold("b++" + w); B = snappy.Manifold("b++" + swap(w))
    isos = A.is_isometric_to(B, return_isometries=True)
    dets = sorted({int(round(float(i.cusp_maps()[0].det()))) for i in isos}) if isos else []
    print("  b++%s and b++%s: isometric %s; every isometry between them has cusp-map determinant %s (-1: orientation-reversing)" % (w, swap(w), bool(isos), dets))
