"""Locks for B551 — the inflation-order boundary theorem (fusion death)."""

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _word(n=40000):
    w = 'a'
    while len(w) < n:
        w = ''.join(SUB[c] for c in w)
    return w[:n]


def test_case_fold_has_aaa_not_fibonacci():
    """{a,A}->a, {b,B}->b contains 'aaa' -> not the Fibonacci word."""
    w = _word()
    cf = w.translate(str.maketrans({'a': 'a', 'A': 'a', 'b': 'b', 'B': 'b'}))
    assert 'aaa' in cf


def test_old_new_is_non_sturmian():
    """{a,b}->x, {A,B}->y has complexity (2,4,7,10,14,17,20,23), not n+1."""
    w = _word()
    on = w.translate(str.maketrans({'a': 'x', 'b': 'x', 'A': 'y', 'B': 'y'}))
    comp = [len(set(on[i:i+n] for i in range(len(on)-n))) for n in range(1, 9)]
    assert comp == [2, 4, 7, 10, 14, 17, 20, 23]
    assert comp != [n+1 for n in range(1, 9)]      # non-Sturmian


def test_species_is_radius1_coloring_of_old_new():
    """species letter is determined by its old/new radius-1 window; 7 windows."""
    from collections import defaultdict
    w = _word()
    on = w.translate(str.maketrans({'a': 'x', 'b': 'x', 'A': 'y', 'B': 'y'}))
    rule = defaultdict(set)
    for i in range(1, len(w)-1):
        rule[(on[i-1], on[i], on[i+1])].add(w[i])
    assert all(len(v) == 1 for v in rule.values())
    assert len(rule) == 7
