"""B1118 lock -- the P-bit: the mirror (swap-factors composed with su(3)
conjugation = neg-then-blockswap) FUSES B1102's two orbits of 9 into one,
while the plain factor-swap does NOT. So the last hypercharge bit is P."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _orbits_and_maps():
    r = json.loads((ROOT / "frontier/B1102_exact_hypercharge_solve/b1102_results.json")
                   .read_text(encoding="utf-8"))
    sols = [tuple(F(x) for x in t) for t in r["all_solving_directions"]]
    S = set(sols)
    W3 = [(F(1), F(0)), (F(0), F(1)), (F(-1), F(-1))]

    def mat(p):
        a, b = W3[p[0]], W3[p[1]]
        return ((a[0], b[0]), (a[1], b[1]))
    MATS = [mat(p) for p in itertools.permutations(range(3))]

    def contr(M, v):
        d = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        inv = ((M[1][1] / d, -M[0][1] / d), (-M[1][0] / d, M[0][0] / d))
        return (inv[0][0] * v[0] + inv[1][0] * v[1], inv[0][1] * v[0] + inv[1][1] * v[1])

    def act(t, gA, gB, sw):
        tA, tB = contr(gA, (t[0], t[1])), contr(gB, (t[2], t[3]))
        o = (tA[0], tA[1], tB[0], tB[1])
        return (o[2], o[3], o[0], o[1]) if sw else o
    pres = [g for g in [(a, b, s) for a in MATS for b in MATS for s in (False, True)]
            if all(act(t, *g) in S for t in sols)]
    seen, orbits = set(), []
    for t in sols:
        if t in seen:
            continue
        orb, fr = {t}, [t]
        while fr:
            x = fr.pop()
            for g in pres:
                y = act(x, *g)
                if y in S and y not in orb:
                    orb.add(y)
                    fr.append(y)
        seen |= orb
        orbits.append(orb)
    return sols, S, orbits


def test_two_orbits_of_nine():
    _, _, orbits = _orbits_and_maps()
    assert sorted(len(o) for o in orbits) == [9, 9]


def test_plain_swap_does_not_fuse_but_mirror_does():
    sols, S, orbits = _orbits_and_maps()
    o1, o2 = orbits
    plain = lambda t: (t[2], t[3], t[0], t[1])
    mirror = lambda t: (-t[2], -t[3], -t[0], -t[1])  # neg . blockswap
    assert not any(plain(t) in o2 for t in o1), "plain swap must NOT fuse (F4b)"
    assert all(mirror(t) in o2 for t in o1) and all(mirror(t) in o1 for t in o2), \
        "the mirror (neg.blockswap) must fuse the two orbits -> the bit is P"
