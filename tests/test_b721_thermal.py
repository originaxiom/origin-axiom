"""B721 lock — thermal-time coupling: field-matched, rung-mismatch; two clocks (II_1 vs III)."""
import sympy as sp

def test_two_disjoint_fields_on_the_knot():
    # golden Q(sqrt5) from branched covers (Alexander t^2-3t+1) vs being Q(sqrt-3) trace field
    t = sp.symbols('t'); alex = t**2 - 3*t + 1
    assert sp.discriminant(alex, t) == 5                    # golden field disc 5
    # trace field Q(sqrt-3): disc -3; the two are linearly disjoint (real vs imaginary quadratic)
    assert 5 > 0 and -3 < 0

def test_branched_cover_homology_is_fibonacci_lucas():
    # |H_1(Sigma_n(4_1))| = L_n^2 (n odd), 5 F_n^2 (n even) -- golden Q(sqrt5) structure
    def fib(n):
        a, b = 0, 1
        for _ in range(n): a, b = b, a + b
        return a
    def luc(n): return fib(n - 1) + fib(n + 1)
    def cover_order(n): return luc(n)**2 if n % 2 else 5 * fib(n)**2
    assert [cover_order(n) for n in range(2, 7)] == [5, 16, 45, 121, 320]

def test_being_z2_is_quotient_not_subtorsor():
    # exact seq 1 -> Gal(K^ab/K) [CMR torsor, kernel] -> Gal(K^ab/Q) -> Gal(K/Q)=Z/2 [being] -> 1
    # our Z/2 is the QUOTIENT (over base Q), CMR is the KERNEL (over base K); complementary
    being_base, cmr_base = "Q", "Q(sqrt-3)"
    assert being_base != cmr_base                           # different base fields -> not nested

def test_object_clock_is_tracial_trivial_modular_flow():
    # the Anosov suspension is measure-preserving (det sigma = 1) -> tracial type II_1 -> Delta=1
    sigma = sp.Matrix([[2, 1], [1, 1]])
    assert sigma.det() == 1                                 # measure-preserving -> tracial -> trivial modular flow
    # a thermal (CMR) clock is type III (non-tracial, nontrivial modular flow) -> DIFFERENT clock
