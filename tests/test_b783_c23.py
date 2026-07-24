"""C23 -- the T1-mover no-go: the realized subgroup of Out(V4)=S3 is {identity}."""
import itertools
import json
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B775_phase2_wave1"


def test_V4_abelian_so_inner_action_trivial():
    # C21's premise, re-locked: V4 abelian => conjugation acts trivially => a mover must be OUTER
    V4 = list(itertools.product([0, 1], repeat=2))
    mul = lambda a, b: tuple((x + y) % 2 for x, y in zip(a, b))
    inv = lambda a: a                      # every element is its own inverse in V4
    for g in V4:
        for v in V4:
            assert mul(mul(g, v), inv(g)) == v      # conjugation trivial


def test_three_legs_have_distinct_signatures_leaving_only_identity():
    # the two conjugation-robust invariants: (orientation holo/antiholo, pair-orbit fix/swap)
    sig = {"c": (1, 0), "j2": (0, 0), "tau": (1, 1)}   # antiholo=1, swap=0/fix=1 per the cell
    assert len(set(sig.values())) == 3                  # all three DISTINCT
    # a nontrivial S3 element must permute the legs while preserving both invariants;
    # distinct signatures => only the identity permutation can
    import itertools as it
    legs = list(sig)
    survivors = [p for p in it.permutations(legs) if all(sig[a] == sig[b] for a, b in zip(legs, p))]
    assert survivors == [tuple(legs)]                   # identity only


def test_c23_banked_from_wave1():
    d = json.loads((ARC / "wave1_results.json").read_text())
    cell = next(c for c in d["cells"] if c["id"] == "P2-T1MOVER")
    assert cell["verdict"] == "RESOLVED-B" and cell["upheld"] is True
