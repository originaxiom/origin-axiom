"""Locks for B548 — un-hideability census (small cases, exact)."""
from itertools import permutations


def _langs(sub, seed, depth):
    w = seed
    for _ in range(depth):
        w = ''.join(sub[c] for c in w)
    ref_bi = frozenset(w[i:i+2] for i in range(len(w)-1))
    ref_six = frozenset(w[i:i+6] for i in range(len(w)-5))
    alpha = sorted(sub)
    perms = {g: sorted(set(permutations(sub[g]))) for g in alpha}
    langs = set()
    import itertools
    for combo in itertools.product(*[perms[g] for g in alpha]):
        s = {g: ''.join(c) for g, c in zip(alpha, combo)}
        w2 = seed
        for _ in range(depth):
            w2 = ''.join(s[c] for c in w2)
        bi = frozenset(w2[i:i+2] for i in range(len(w2)-1))
        if bi == ref_bi:
            langs.add(frozenset(w2[i:i+6] for i in range(len(w2)-5)))
    return len(langs)


def test_fibonacci_unhideable():
    assert _langs({'a': 'ab', 'b': 'a'}, 'a', 16) == 1


def test_period_doubling_unhideable_nonpisot():
    # non-Pisot yet un-hideable: refutes "un-hideable => Pisot"
    assert _langs({'a': 'ab', 'b': 'aa'}, 'a', 12) == 1


def test_reducible_unhideable():
    assert _langs({'a': 'aa', 'b': 'ab'}, 'a', 12) == 1
