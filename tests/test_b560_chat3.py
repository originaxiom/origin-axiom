"""B560 — chat-3 frontier campaign (cells 1-4), headline claims re-verified in-sandbox.

Independent locks for the load-bearing, checkable results (the cells' own 26 tests
live under frontier/B560_chat3_frontier_campaign/ and also pass):
  Cell 1  : SNF(I-M4) = diag(1,1,1,11) => coker = Z/11; chi=(1,3,6,7) left-fixed mod 11.
  Cell 1B : every nonzero class of Z/11 has a finite localized carrier (defect pair
            L u R / L v R with equal 3-letter contexts and equal core length).
  Cell 4  : the degree-4 frequency module is EXACTLY Z[tau], tau=sqrt(phi), tau^4-tau^2-1=0
            -- the frequencies are the Perron eigenvector of M4 and generate Z[tau] (det 1).
See frontier/B560_chat3_frontier_campaign/FINDINGS.md.
"""
from collections import defaultdict
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

M4 = sp.Matrix([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]])
Q = {'a': 1, 'b': 3, 'A': 6, 'B': 7}
SIG = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def test_cell1_z11_charge():
    S = smith_normal_form(sp.eye(4) - M4, domain=sp.ZZ)
    assert [abs(S[i, i]) for i in range(4)] == [1, 1, 1, 11]          # coker = Z/11
    chi = sp.Matrix([[1, 3, 6, 7]])
    assert [x % 11 for x in (chi * M4)] == [1, 3, 6, 7]              # chi M = chi mod 11


def test_cell4_frequency_module_is_Z_tau():
    tau = sp.symbols('tau', positive=True)
    fa, fb, fA, fB = tau - 1, tau**3 - tau**2 - tau + 1, tau**2 - tau, -tau**3 + tau + 1
    assert sp.simplify(fa + fb + fA + fB) == 1                        # frequencies sum to 1
    beta = tau**2 + tau**3                                            # Perron = phi(1+sqrt phi)
    mp = tau**4 - tau**2 - 1                                          # tau = sqrt(phi)
    f = sp.Matrix([fa, fb, fA, fB])
    lhs = M4 * f
    assert all(sp.rem(sp.expand(lhs[i] - beta * f[i]), mp, tau) == 0 for i in range(4))
    # generate Z[tau]: coefficient matrix in basis (1,tau,tau^2,tau^3) has det +-1
    def coeffs(e):
        p = sp.Poly(sp.expand(e), tau)
        return [p.coeff_monomial(tau**k) for k in range(4)]
    C = sp.Matrix([coeffs(e) for e in (fa, fb, fA, fB)])
    assert abs(C.det()) == 1


def _word(k):
    w = 'a'
    for _ in range(k):
        w = ''.join(SIG[c] for c in w)
    return w


def test_cell1b_localized_carriers_first_core_lengths():
    """Every nonzero residue of Z/11 has a finite localized carrier (defect pair with
    equal 3-context and equal core length); the FIRST core length per class matches
    chat-3's frozen census exactly."""
    w = _word(10)
    q = lambda s: sum(Q[c] for c in s) % 11
    first = {}
    CTX = 3
    for CORE in range(1, 17):
        ctx = defaultdict(set)
        for i in range(CTX, len(w) - CORE - CTX):
            ctx[(w[i - CTX:i], w[i + CORE:i + CORE + CTX])].add(w[i:i + CORE])
        for cores in ctx.values():
            cl = list(cores)
            for u in cl:
                for v in cl:
                    if u != v:
                        c = (q(v) - q(u)) % 11
                        if c and c not in first:
                            first[c] = CORE
        if set(first) >= set(range(1, 11)):
            break
    assert first == {1: 3, 2: 9, 3: 3, 4: 16, 5: 14, 6: 14, 7: 16, 8: 3, 9: 9, 10: 3}
