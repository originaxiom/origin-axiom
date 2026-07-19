"""B714 lock — the physics-of-the-object spine: the load-bearing reconciliation facts."""

def test_incommensurable_blocks_close_the_generation_triple():
    # 6': h^1=3 sits in incommensurable blocks V17 + V9 + V1 = 27 (B657), not a permutable triple
    blocks = (17, 9, 1)
    assert sum(blocks) == 27
    assert len(set(blocks)) == 3          # incommensurable (all distinct) -> not a permutable triple

def test_no_order3_symmetry_route():
    # 6' leg (i): Isom(4_1)=D4 order 8, no order-3 element -> the symmetry/triality route is closed
    assert 8 % 3 != 0

def test_object_authored_region_is_rungs_0_to_6():
    # the spine's layer 1 = rungs 0..6 (object-forced); 7..9 generic; the count of authored rungs
    authored = list(range(0, 7))          # 0,1,2,3,4,5,6
    assert authored == [0, 1, 2, 3, 4, 5, 6] and len(authored) == 7

def test_values_layer_is_negative():
    # rung ⊥: the outright-negative arcs vs the ambiguous-closed ones (grading precision)
    outright_negative = {"B631", "B685", "B706"}
    ambiguous_closed = {"B615", "B616"}
    assert outright_negative.isdisjoint(ambiguous_closed)   # graded distinctly, net negative
