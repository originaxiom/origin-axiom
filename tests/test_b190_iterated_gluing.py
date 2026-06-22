"""B190 -- abstract iterated gluing (V183; corrected 2026-06-22 after adversarial verification). Fast locks.

Iterating the trace-ring gluing does NOT converge to a forced-unique value. OPEN gluing proliferates -- the
fork-polynomial DEGREE (a Bezout upper bound, NOT the geometric count) grows T^k -> 8+k, swaps double.
CLOSED/loop (over-determined) gluing collapses to a finite discrete set whose TOTAL count grows (1,2,3,4) but
whose GENUINE (golden-field) non-trivial points are NON-monotone (seq 0,0,2,0: appear at STST, vanish at
STSTST), never a single forced value. The lone count-1 loop ST fixes the trivial (2,2,2). Full version in
iterated_gluing.py.
"""
import sympy as sp

p, q, r = sp.symbols("p q r")
def _f(x): return x**4 - 5*x**2 + 2
def _act(word, P, Q, R):
    for g in word:
        if g == "S": P, Q, R = Q, P, R
        elif g == "T": P, Q, R = P, R, P*R - Q
    return P, Q, R

_RQUAD = r**2 - p*_f(p)*r + p**2 + _f(p)**2 - 4
def _fork_size(word):
    P, Q, R = _act(word, p, _f(p), r)
    cond = sp.expand(sp.numer(sp.together(Q - _f(P))))
    if cond == 0: return 0
    res = sp.resultant(sp.Poly(cond, r), sp.Poly(_RQUAD, r), r) if cond.has(r) else cond
    return sp.Poly(sp.expand(res), p).degree()

_REL = r**2 - p*q*r + p**2 + q**2 - 4
def _fixed(word):
    P, Q, R = _act(word, p, q, r)
    sysd = [sp.expand(e) for e in (P-p, Q-q, R-r)]; sysd = [e for e in sysd if e != 0] + [_REL]
    sols = sp.solve(sysd, [p, q, r], dict=True)
    return [s for s in sols if all(v in s for v in (p, q, r)) and not any(s[v].free_symbols for v in (p, q, r))]


def test_open_fork_polynomial_degree_proliferates():
    # the fork-polynomial DEGREE (Bezout upper bound on the geometric count) grows; never collapses to 1
    for k in (1, 2, 3):
        assert _fork_size("T"*k) == 8 + k          # degree law, linear in twists
    assert _fork_size("S") == 16 and _fork_size("ST") == 32   # doubling per swap


def test_loop_total_count_grows_genuine_nonmonotone_not_unique():
    # TOTAL fixed-point count grows monotonically; the lone count-1 (ST) is the trivial point
    assert [len(_fixed(w)) for w in ("ST", "TST", "STST", "STSTST")] == [1, 2, 3, 4]
    s = _fixed("ST")[0]; assert all(s[v] in (2, -2) for v in (p, q, r))
    # GENUINE (non-trivial) count is non-monotone: 0,0,2,0 -- golden-field points appear (STST) and vanish (STSTST)
    def genuine(w): return [t for t in _fixed(w) if not all(t[v] in (2, -2) for v in (p, q, r))]
    assert [len(genuine(w)) for w in ("ST", "TST", "STST", "STSTST")] == [0, 0, 2, 0]
    assert any(t[v].has(sp.sqrt(5)) for t in genuine("STST") for v in (p, q, r))   # golden field
