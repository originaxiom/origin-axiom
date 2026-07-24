"""B779 -- cc3's convergence roadmap: lock on R1 (Galois orbits on the closing torsor)."""
import itertools
import pathlib

ARC = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B779_convergence_probe"


def test_r1_galois_orbits_labeled_by_theta():
    # V4 = <sigma_c, sigma_gamma5> (the GALOIS part) acts on F2^3 = <c, theta, gamma5>
    # by translation; orbits are the 2 cosets, labeled exactly by the theta coordinate
    F = list(itertools.product([0, 1], repeat=3))       # (c, theta, gamma5)
    V4 = [(0, 0, 0), (1, 0, 0), (0, 0, 1), (1, 0, 1)]    # theta-component always 0
    act = lambda g, x: tuple((a + b) % 2 for a, b in zip(g, x))
    orbits, seen = [], set()
    for x in F:
        if x in seen:
            continue
        o = sorted({act(g, x) for g in V4})
        orbits.append(o)
        seen |= set(o)
    assert len(orbits) == 2 and all(len(o) == 4 for o in orbits)
    # the orbit label IS the theta coordinate (the non-Galois bit)
    assert all(len({x[1] for x in o}) == 1 for o in orbits)
    # V4 acts freely (simply transitively on each coset)
    assert all(act(g, x) != x for g in V4 if g != (0, 0, 0) for x in F)


def test_b779_roadmap_folded():
    for f in ["R1_galois_orbits.md", "R2_mixing_crosscheck.md", "R3_scattering_assessment.md",
              "R5_sl3_assessment.md", "R6_maass_assessment.md", "R7_functor_assessment.md",
              "CC_GATE_NOTE.md"]:
        assert (ARC / f).exists(), f
