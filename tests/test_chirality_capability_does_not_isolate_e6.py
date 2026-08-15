"""The complex-fundamental criterion does NOT isolate E6 among McKay images.

WHY THIS FILE EXISTS. The structure paper's largest open problem is that the
entrance classification ASSUMES exceptionality rather than deriving it. A Wave-1
inventory agent named the one available route -- B253's chirality-capability
criterion (G2 7 real, F4 26 real, E6 27 COMPLEX, E7 56 pseudoreal, E8 248 real) --
as "a cheap cell and the only thing that could convert exceptionality from input to
output", noting it had never been run over the A- and D-series.

Run here. IT COMES BACK NEGATIVE, and the negative is worth more than the open
question: the obvious route is now closed rather than untried.

THE CRITERION. A simple Lie algebra has complex (non-self-dual) representations iff
-w_0 != id, equivalently iff -1 is NOT in the Weyl group. Computed directly from the
Cartan matrix by generating W from the simple reflections.

THE RESULT. Complex reps exist for A_n (n>=2), D_n (n odd), and E6 -- so the
criterion selects an INFINITE set including every cyclic subgroup of SU(2) of order
>= 3, all of which are McKay images of type A. It isolates E6 only WITHIN the
exceptional series, which is the range B253 actually tested.
"""
import sympy as sp


def cartan(kind, n):
    C = sp.zeros(n, n)
    for i in range(n):
        C[i, i] = 2
    if kind == "A":
        for i in range(n - 1):
            C[i, i + 1] = C[i + 1, i] = -1
    if kind == "D":
        for i in range(n - 2):
            C[i, i + 1] = C[i + 1, i] = -1
        C[n - 3, n - 1] = C[n - 1, n - 3] = -1
    return C


def weyl(C):
    """Generate W acting on the weight basis; return (contains -1, |W|)."""
    n = C.shape[0]
    refl = []
    for i in range(n):
        M = sp.eye(n)
        for j in range(n):
            M[i, j] -= C[i, j]
        refl.append(M)
    seen = {sp.ImmutableMatrix(sp.eye(n))}
    frontier = [sp.eye(n)]
    while frontier:
        nxt = []
        for g in frontier:
            for s in refl:
                h = sp.ImmutableMatrix(s * g)
                if h not in seen:
                    seen.add(h)
                    nxt.append(sp.Matrix(h))
        frontier = nxt
    return sp.ImmutableMatrix(-sp.eye(n)) in seen, len(seen)


def test_weyl_orders_are_right():
    """Ground the computation: these orders are standard."""
    assert weyl(cartan("A", 1))[1] == 2        # |W(A_1)| = 2! = 2
    assert weyl(cartan("A", 2))[1] == 6        # 3!
    assert weyl(cartan("A", 3))[1] == 24       # 4!
    assert weyl(cartan("D", 4))[1] == 192      # 2^3 * 4!
    assert weyl(cartan("D", 5))[1] == 1920     # 2^4 * 5!


def test_A_type_is_chirality_capable_from_n_two():
    """Cyclic McKay images of order >= 3 have complex reps -- the whole point."""
    assert weyl(cartan("A", 1))[0] is True     # -1 in W  => NO complex reps
    for n in (2, 3):
        assert weyl(cartan("A", n))[0] is False  # -1 not in W => complex reps


def test_D_odd_is_chirality_capable():
    assert weyl(cartan("D", 4))[0] is True     # D_even: no complex reps
    assert weyl(cartan("D", 5))[0] is False    # D_odd: complex reps


def test_the_criterion_does_not_isolate_e6():
    """The load-bearing negative.

    If chirality-capability isolated E6 among McKay images, exceptionality would be
    DERIVED and the paper's largest open problem would close. It does not: type-A
    images of every order >= 3 pass the same criterion.
    """
    capable = []
    for n in (2, 3):
        if not weyl(cartan("A", n))[0]:
            capable.append(f"A_{n}")
    if not weyl(cartan("D", 5))[0]:
        capable.append("D_5")
    assert capable, "criterion selected nothing -- the test would be vacuous"
    assert len(capable) > 1, (
        "chirality-capability selects more than E6 alone; if this ever fails, "
        "re-examine, because it would mean the criterion DOES isolate and the "
        "paper's open problem has closed")
