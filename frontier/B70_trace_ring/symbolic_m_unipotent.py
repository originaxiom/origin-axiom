"""B70 (P5) -- the V45 unipotent expansion as a SYMBOLIC-IN-m tool, and the precise remaining gap for
a from-first-principles symbolic SL(4) fixed-line Jacobian.

V45 established that at the c=n fixed line the rep is UNIPOTENT (A=I+N, N^n=0), so A^m = sum_{j<n}
C(m,j) N^j is POLYNOMIAL in m. This sharpens to: even the perturbation derivative is symbolic in m,
   d/deps ((I+eps g) A0)^m |_0 = sum_{i=0}^{m-1} A0^i g A0^{m-i}
     = sum_{j,k<n} [ C(m+1, j+k+1) - [k==0] C(m,j) ] N^j g N^k        (Vandermonde convolution),
a closed form polynomial in m.  These two facts (`Apow_unip`, `dApow_mult`) are validated here against
numeric A^m / its derivative at integer m -- a genuine new tool enabling symbolic-m matrix work, and
matrix arithmetic auto-enforces the e_2..e_{n-1} (exterior-power) closure (no hand-built two-block
trace ring -- the B58 barrier is bypassed at the matrix level).

THE REMAINING GAP (this script's honest finding).  The fixed-line Jacobian is the linearization of the
trace map at the c=n point, which is the DEGENERATE TRIVIAL rep A=B=I (N=0) -- where trace gradients
vanish to first order (B58: the rep-Jacobian is second-order at the identity).  A single linearization
at a GENERIC unipotent rep (I+N, N!=0) is NOT at a fixed point of T_m, and its Jacobian does NOT factor
as the tower (verified: char != char(M^-1)char(M^2)char(M^3)(t-1)(t+1) for SL(3)).  The correct object
is the eps->0 PINV-LIMIT approaching the trivial rep (B59/B66/B58-PhaseA `jacobian_closure.py`, exact
over F_p at numeric m).  So a from-first-principles SYMBOLIC-m proof needs the symbolic-m eps-series
pinv-limit -- the unipotent expansion above supplies the symbolic-m matrix powers it requires, but the
eps-series normal-equation solve over Z[m] is the substantial remaining construction.

NET: V45's (3,3) bound + these symbolic-m tools turn the trace-ring proof into a concrete program
(symbolic-m eps-series pinv-limit, e_2 handled by matrix arithmetic), but the proof is not closed here.
Computer-assisted characterization; NOT a proof. Proven core P1-P16 untouched.
"""
import sympy as sp

m = sp.symbols("m")


def binom(mm, k):
    return sp.Integer(0) if k < 0 else sp.prod([mm - i for i in range(k)]) / sp.factorial(k)


def Apow_unip(N, n):
    """A0^m for A0 = I + N unipotent (N^n=0): sum_{j<n} C(m,j) N^j, symbolic in m."""
    out, Nj = sp.eye(n), sp.eye(n)
    for j in range(1, n):
        Nj = Nj * N
        out = out + binom(m, j) * Nj
    return sp.Matrix(out)


def dApow_mult(N, g, n):
    """d/deps ((I+eps g)(I+N))^m |_0 = sum_{j,k<n} [C(m+1,j+k+1) - [k==0]C(m,j)] N^j g N^k."""
    out, Nj = sp.zeros(n, n), sp.eye(n)
    for j in range(n):
        Nk = sp.eye(n)
        for k in range(n):
            S = binom(m + 1, j + k + 1) - (binom(m, j) if k == 0 else 0)
            out = out + S * Nj * g * Nk
            Nk = Nk * N
        Nj = Nj * N
    return sp.Matrix(out)


def _nilpotent(n, seed=0):
    import random
    random.seed(seed)
    M = sp.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            M[i, j] = sp.Integer(random.randint(1, 4))
    return M


def validate(n=4, mvals=(1, 2, 3, 5)):
    """Check Apow_unip and dApow_mult (symbolic in m) against direct matrix powers at integer m."""
    N = _nilpotent(n)
    A0 = sp.eye(n) + N
    g = _nilpotent(n, seed=2) - _nilpotent(n, seed=3).T   # some sl(n)-ish direction
    Am = Apow_unip(N, n)
    eps = sp.symbols("eps")
    ok = True
    for mv in mvals:
        # A^m
        direct = A0 ** mv
        if sp.expand(Am.subs(m, mv) - direct) != sp.zeros(n, n):
            ok = False
        # d/deps ((I+eps g)A0)^m at eps=0
        P = ((sp.eye(n) + eps * g) * A0) ** mv
        dP = sp.Matrix(n, n, lambda i, j: sp.diff(P[i, j], eps).subs(eps, 0))
        if sp.expand(dApow_mult(N, g, n).subs(m, mv) - dP) != sp.zeros(n, n):
            ok = False
    return ok


def main():
    print("B70 (P5) -- symbolic-m unipotent expansion: validation + the remaining gap\n")
    for n in (3, 4):
        print(f"  n={n}: Apow_unip & dApow_mult match direct matrix powers at m=1,2,3,5: {validate(n)}")
    print("\nThe symbolic-m matrix powers are correct. But the fixed-line Jacobian is the eps->0")
    print("pinv-LIMIT at the degenerate trivial rep (A=B=I); a single unipotent-rep linearization is")
    print("NOT a fixed point and does not factor as the tower. From-first-principles symbolic-m proof")
    print("=> symbolic-m eps-series pinv-limit (these tools supply its symbolic-m matrix powers).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
