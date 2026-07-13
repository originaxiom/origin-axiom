"""Locks for the B556 feedback ledger (chat-2 handoff, independently verified).

Covers the load-bearing arithmetic:
  - golden-norm closed form  e_1 = N_{Q(sqrt5)/Q}(g_1(phi)) = -11  (exact)
  - transfer polynomial G (deg 9), two-step law  e_{n+1} = det(G(M_{n-1}))
  - growth law: field degree 2^{n+1}, log-charge ratio -> 3
  - the quine seed-invariant: seed 'a' once, at position 0, in every sigma_4 image

See frontier/B556_escalator_tower/FINDINGS.md, section "The feedback ledger".
"""
import math
import sympy as sp

F = sp.Matrix([[1, 1], [1, 0]])
x = sp.Symbol('x')


def _T(M):
    return sp.Matrix(sp.BlockMatrix([[M, M], [M*M, M]]))


def _rung(n):
    M = F
    for _ in range(n):
        M = _T(M)
    return M


def _e(n):
    M = _rung(n)
    return int((sp.eye(M.shape[0]) - M).det(method='bareiss'))


# charge tower e_0..e_5 (exact, banked)
E = [-1, -11, -809, -18845089,
     -228654672055316545291,
     -14551745085338356602787456737044854593029948485574326872937769]


def test_charge_values_exact():
    for n in range(5):                       # e_5 (64x64) checked separately, slower
        assert _e(n) == E[n]


def test_e5_is_62_digits():
    """e5 in [2^203, 2^204): floor(log2)=203 (chat-2's 'bits'), bit_length=204.
    Both conventions are correct; chat-2's 203 is NOT an error."""
    e5 = _e(5)
    assert e5 == E[5]
    assert len(str(abs(e5))) == 62
    assert abs(e5).bit_length() == 204        # bits to store
    assert (abs(e5).bit_length() - 1) == 203  # floor(log2) magnitude = chat-2's figure


def test_golden_norm_closed_form():
    """e_1 = N_{Q(sqrt5)/Q}(g_1(phi)) with g_1 = the fixed cubic."""
    sqrt5 = sp.sqrt(5)
    phi, psi = (1 + sqrt5)/2, (1 - sqrt5)/2
    g1 = lambda t: t**3 - t**2 + 2*t - 1
    norm = sp.simplify(sp.expand(g1(phi)) * sp.expand(g1(psi)))
    assert norm == -11 == E[1]


def test_transfer_polynomial_two_step_law():
    """e_{n+1} = det(G(M_{n-1})) with G the fixed degree-9 kernel."""
    Gc = [-1, 3, -5, 2, -4, 3, -8, 6, -4, 1]      # v^9 .. v^0

    def Gmat(M):
        n = M.shape[0]
        acc = sp.zeros(n)
        for c in Gc:
            acc = acc * M + c * sp.eye(n)
        return acc

    for n in range(1, 4):                          # rungs 1..3 (M_2 is 8x8)
        rhs = int(Gmat(_rung(n - 1)).det(method='bareiss'))
        assert rhs == E[n + 1], (n, rhs, E[n + 1])


def test_growth_law_field_doubles_arithmetic_triples():
    # field degree doubles: charpoly degree 2^{n+1}, irreducible
    for n in range(4):
        cp = sp.Poly(_rung(n).charpoly(x).as_expr(), x)
        assert cp.degree() == 2 ** (n + 1)
        assert cp.is_irreducible
    # arithmetic: log-charge ratios approach 3
    ratios = [math.log(abs(E[n + 1])) / math.log(abs(E[n])) for n in range(1, 5)]
    assert ratios[-1] == sp.Float(ratios[-1])       # sanity
    assert abs(ratios[-1] - 3) < 0.05               # last ratio ~ 3.00


def test_quine_seed_invariant():
    """Every sigma_4 image contains the seed 'a' exactly once, at position 0."""
    sigma = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
    for w in sigma.values():
        assert w.count('a') == 1 and w[0] == 'a'
