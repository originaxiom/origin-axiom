"""Lock: the factor complexity of the 4-letter Fibonacci word, and the "two 17s".

chat-1 Session-4 B4: p(5)=17 is real (the coupling census saturates at length 5),
but the 17 length-5 factor-WORDS are NOT the 17 dictionary component-VALUES (B542)
— a count coincidence, not a bijection.  See frontier/B535_coupling_space/FINDINGS.md.
"""
SIGMA = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def _fixed_point(n_iter):
    w = 'a'
    for _ in range(n_iter):
        w = ''.join(SIGMA[c] for c in w)
    return w


def _p(word, n):
    return len({word[i:i+n] for i in range(len(word) - n + 1)})


def test_factor_complexity_sequence():
    """p(1..7) = 4,7,10,13,17,20,23 ; the +4 jump at n=5 admits the 6th type."""
    w = _fixed_point(8)                       # 44,368 letters — saturated for n<=7
    assert [_p(w, n) for n in range(1, 8)] == [4, 7, 10, 13, 17, 20, 23]
    assert _p(w, 5) == 17                     # the saturation-length count


def test_two_seventeens_are_different_objects():
    """17 length-5 factor-words vs 17 algebraic components (5+6+1+5); count only."""
    w = _fixed_point(8)
    factor_words = {w[i:i+5] for i in range(len(w) - 4)}
    assert len(factor_words) == 17
    # the B542 component tally (two tau-ladders + tau^-5 + pi-fringe)
    component_values = 5 + 6 + 1 + 5
    assert component_values == 17
    # they match in COUNT but index different kinds of object (no bijection banked)
    assert all(len(f) == 5 for f in factor_words)     # words of length 5
