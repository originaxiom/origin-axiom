"""B191 -- the formal 2-cusp connector (V187). Fast locks.

A 2-cusp connector NESTS the kappa-selection: a coupling connector (mapping class phi_c) propagates leaf1's
A-poly constraint into a DISCRETE fork on leaf2 (T->9, S->16, ST->32, proliferating), while the identity
(uncoupled) connector gives a CONTINUUM (no selection). dim(leaf--connector--leaf) = (1+2+1)-2*2 = 0 (discrete
iff the connector couples its boundaries). The true geometric metallic 2-cusp connector is NEEDS-SPECIALIST.
Full version in connector.py.
"""
import sympy as sp

p, r = sp.symbols("p r")
def _f(x): return x**4 - 5*x**2 + 2
def _act(word, P, Q, R):
    for g in word:
        if g == "S": P, Q, R = Q, P, R
        elif g == "T": P, Q, R = P, R, P*R - Q
    return P, Q, R
_RQUAD = r**2 - p*_f(p)*r + p**2 + _f(p)**2 - 4


def _chain_fork(phi_c):
    P, Q, R = _act(phi_c, p, _f(p), r)
    cond = sp.expand(sp.numer(sp.together(Q - _f(P))))
    if cond == 0: return "CONTINUUM"
    res = sp.resultant(sp.Poly(cond, r), sp.Poly(_RQUAD, r), r) if cond.has(r) else cond
    return sp.Poly(sp.expand(res), p).degree()


def test_dim_count_and_identity_control():
    assert (1 + 2 + 1) - 2*2 == 0                  # leaf--connector--leaf is dim 0 (discrete) if coupled
    assert _chain_fork("") == "CONTINUUM"          # identity (uncoupled) connector -> no selection


def test_kappa_nests_discrete_and_proliferates():
    fT, fS, fST = _chain_fork("T"), _chain_fork("S"), _chain_fork("ST")
    assert fT == 9 and fS == 16 and fST == 32      # coupling connectors -> discrete forks (kappa propagates)
    assert _chain_fork("TT") > fT and fST > fS     # proliferates with connector complexity
    assert all(d > 1 for d in (fT, fS, fST))       # never collapses to forced-unique
