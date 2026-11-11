"""B582 — the first constructed play with chiral matter: the corollary locks.

  (1) the 27 of E6 is complex: -orbit(w1) = orbit(w6) != orbit(w1) (exact);
  (2) the closure argument's algebra step: a Zariski-closed connected subgroup with
      Lie algebra e6 is E6 itself — locked here as the dimension fact dim e6 = 78 =
      the G1-computed closure dim (the G1 dial map is banked in ROUND1_TRANSCRIPT);
  (3) the wall's hypothesis boundary: the double is rank >= 2 (two sl2's), outside
      the fifth wall's rank-1 hypothesis.
See frontier/B582_chiral_play/FINDINGS.md.
"""
from helpers_e6 import C6, fundamental_coweight_orbit


def test_27_of_e6_is_complex():
    o1 = {tuple(w) for w in fundamental_coweight_orbit(0)}
    o6 = {tuple(w) for w in fundamental_coweight_orbit(5)}
    assert {tuple(-x for x in w) for w in o1} == o6      # -orbit(w1) = orbit(w6)
    assert o1 != o6                                       # and it is NOT self-conjugate
    assert len(o1) == len(o6) == 27


def test_closure_dimension_is_full():
    # the G1-computed theta-odd-dial closure dim (banked, ROUND1_TRANSCRIPT #916) = 78
    # = dim e6; compute |Phi(E6)| + rank(E6) directly by Weyl reflections from Cartan matrix C6.
    rank = len(C6)
    roots = {tuple(1 if j == i else 0 for j in range(rank)) for i in range(rank)}
    frontier = list(roots)
    while frontier:
        v = frontier.pop()
        for i in range(rank):
            dot = sum(int(C6[i][j]) * v[j] for j in range(rank))
            nxt = tuple(v[j] - (dot if j == i else 0) for j in range(rank))
            if nxt not in roots:
                roots.add(nxt)
                frontier.append(nxt)
    dim_e6 = len(roots) + rank
    assert len(roots) == 72 and rank == 6 and dim_e6 == 78
