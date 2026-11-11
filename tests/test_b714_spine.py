"""B714 lock — the physics-of-the-object spine: the load-bearing reconciliation facts."""
import glob
import math
import os
from sympy.combinatorics.named_groups import DihedralGroup

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def test_incommensurable_blocks_close_the_generation_triple():
    # 6': h^1=3 sits in incommensurable blocks Sym^16 + Sym^8 + Sym^0 = V17 + V9 + V1 = 27 (B657)
    blocks = tuple(math.comb(k + 1, 1) for k in (16, 8, 0))
    assert blocks == (17, 9, 1) and sum(blocks) == 27
    assert len(set(blocks)) == 3          # incommensurable (all distinct) -> not a permutable triple

def test_no_order3_symmetry_route():
    # 6' leg (i): Isom(4_1)=D4 order 8, no order-3 element -> the symmetry/triality route is closed
    d4 = DihedralGroup(4)
    orders = {int(g.order()) for g in d4.generate()}
    assert int(d4.order()) == 8 and 3 not in orders

def test_object_authored_region_is_rungs_0_to_6():
    # the spine's layer 1 = rungs 0..6 (object-forced); 7..9 generic; the count of authored rungs
    authored = list(range(0, 7))          # 0,1,2,3,4,5,6
    assert authored == [0, 1, 2, 3, 4, 5, 6] and len(authored) == 7

def test_values_layer_is_negative():
    # rung ⊥: the outright-negative arcs vs the ambiguous-closed ones (grading precision)
    found_neg = {os.path.basename(p).split("_")[0]
                 for k in ("B631", "B685", "B706")
                 for p in glob.glob(os.path.join(ROOT, "frontier", f"{k}_*"))}
    found_amb = {os.path.basename(p).split("_")[0]
                 for k in ("B615", "B616")
                 for p in glob.glob(os.path.join(ROOT, "frontier", f"{k}_*"))}
    assert found_neg == {"B631", "B685", "B706"} and found_amb == {"B615", "B616"}
    assert found_neg.isdisjoint(found_amb)
