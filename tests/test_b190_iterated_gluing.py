"""B190 -- abstract iterated gluing (V183). Fast locks.

Iterating the trace-ring gluing does NOT converge to a forced-unique value. OPEN gluing proliferates (fork
size T^k -> 8+k, swaps double); CLOSED/loop (over-determined) gluing collapses to a finite discrete set that
also grows with the loop word (ST->1 but the trivial (2,2,2); STST->3 incl. genuine golden-field points).
Confirms B185 in the trace ring. Full version in iterated_gluing.py.
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


def test_open_fork_proliferates():
    for k in (1, 2, 3):
        assert _fork_size("T"*k) == 8 + k          # linear growth in twists
    assert _fork_size("S") == 16 and _fork_size("ST") == 32   # doubling per swap


def test_loop_overdetermination_finite_growing_not_unique():
    cST, cTST, cSTST = len(_fixed("ST")), len(_fixed("TST")), len(_fixed("STST"))
    assert (cST, cTST, cSTST) == (1, 2, 3)         # finite, growing with loop word
    # the lone unique (ST) is the trivial point; genuine golden-field points first appear at STST
    s = _fixed("ST")[0]; assert all(s[v] in (2, -2) for v in (p, q, r))
    genuine = [t for t in _fixed("STST") if not all(t[v] in (2, -2) for v in (p, q, r))]
    assert len(genuine) == 2 and any(t[v].has(sp.sqrt(5)) for t in genuine for v in (p, q, r))
