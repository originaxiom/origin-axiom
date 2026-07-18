"""B699 locks — the two-object surgery test (pyenv-pure).
The mod-5 image ORDERS are recomputed from the verified holonomy trace
triples (reductions of the snappy discrete-faithful holonomy, cross-checked
two-seat). No snappy/sage needed: finite-field group closure in pure python.

Whitehead (5-split) mod (2+i): trace triple (1,4,2) in F_5 -> SL(2,5), 120.
Figure-eight (5-inert) raw mod 5: triple over F_25 -> SL(2,F_25), 15600.
"""


class F25:
    """F_25 = F_5[t]/(t^2 - 2), element a + b t."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = a % 5
        self.b = b % 5

    def __add__(s, o): return F25(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return F25(s.a - o.a, s.b - o.b)
    def __mul__(s, o):
        return F25(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))


def _order_from_triple(F, ta, tb, tab, one, zero, cap):
    """Order of <A,B> in SL(2,F) with A companion-form, B from the trace triple."""
    def mat_mul(M, N):
        return (M[0] * N[0] + M[1] * N[2], M[0] * N[1] + M[1] * N[3],
                M[2] * N[0] + M[3] * N[2], M[2] * N[1] + M[3] * N[3])
    def det(M): return M[0] * M[3] - M[1] * M[2]
    def inv(M): return (M[3], zero - M[1], zero - M[2], M[0])  # det 1
    A = (ta, zero - one, one, zero)
    B = None
    for pa in range(5):
        for pb in range(5):
            p = F(pa, pb)
            s = tb - p
            for qa in range(5):
                for qb in range(5):
                    q = F(qa, qb)
                    r = ta * p + q - tab
                    M = (p, q, r, s)
                    if det(M) == one:
                        B = M
                        break
                if B: break
            if B: break
        if B: break
    assert B is not None
    gens = [A, B, inv(A), inv(B)]
    I = (one, zero, zero, one)
    seen = {I}
    frontier = [I]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = mat_mul(x, g)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
        if len(seen) > cap:
            break
    return len(seen)


def test_whitehead_fills_SL2_5():
    """5-split Whitehead: image FILLS SL(2,5) = 2I (order 120). Falsifier fires."""
    class F5:
        __slots__ = ("a",)
        def __init__(s, a, b=0): s.a = a % 5
        def __add__(s, o): return F5(s.a + o.a)
        def __sub__(s, o): return F5(s.a - o.a)
        def __mul__(s, o): return F5(s.a * o.a)
        def __eq__(s, o): return s.a == o.a
        def __hash__(s): return hash(s.a)
    order = _order_from_triple(F5, F5(1), F5(4), F5(2), F5(1), F5(0), 200)
    assert order == 120, f"Whitehead image order {order}, expected 120 (SL(2,5))"


def test_fig8_raw_fills_SL2_25():
    """5-inert fig-8 RAW holonomy: FILLS SL(2,F_25) (order 15600), NOT 2I."""
    # trace triple over F_25: tr A = 1+3t, tr B = 1+4t, tr AB = 3
    order = _order_from_triple(F25, F25(1, 3), F25(1, 4), F25(3, 0),
                               F25(1, 0), F25(0, 0), 16000)
    assert order == 15600, f"fig-8 raw image order {order}, expected 15600"
    assert order != 120, "the raw holonomy is NOT 2I (that is the quantum hearing rep)"
