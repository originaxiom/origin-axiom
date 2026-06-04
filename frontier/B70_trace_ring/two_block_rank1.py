"""B70 (trace-ring attack, Track A1) -- the SL(n) two-block obstruction is RANK-1.  RIGOROUS version:
the perturbations X,Y are the PROPER traceless sl(n) tangent (tracelessness imposed by substitution
AFTER the matrix products, to avoid the symbolic blowup of an up-front projection). Confirmed across
n=4,5 and two distinct two-block words, with the coupling form pinned exactly to e_2=tr(Lambda^2 A).

Barrier (B58 / nilpotent gate V36): the even-k / e_2 sector needs two-block words tr(A^a B A^b B)
whose fixed-line Hessian has a non-separable a*b coupling no single-index (r-1)^d recursion makes.

RESULT (rigorous, traceless sl(n)):
  - the Hessian of tr(A^a B A^b B) is bidegree (2,2) in (a,b);
  - its ONLY non-separable term is a SINGLE rank-1 bilinear coupling a*b*tr(X^2);
  - tr(X^2) = -2 * (Hessian of e_2 = tr(Lambda^2 A))  [the identity e_2-Hessian = -tr(X^2)/2 on sl(n)],
    so the one two-index generator is EXACTLY the e_2 coordinate.
Confirmed: SL(4) [tr(A^a B A^b B), tr(A^a B^2 A^b B)] and SL(5) [tr(A^a B A^b B)] -- all RANK-1.

So the two-block obstruction is minimal -- one e_2-tied two-index generator, not a high-rank wall.
This bounds the trace-ring closure problem (the SL(4) e_2-sector closure attempt is the continuation).
(Note: the SL(5) case takes several minutes -- exact symbolic on 5x5 matrices.)
"""
import sympy as sp

a, b, eps = sp.symbols("a b epsilon")


def setup(n):
    X = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"x{i}{j}"))
    Y = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"y{i}{j}"))
    tl = {X[n-1, n-1]: -sum(X[i, i] for i in range(n-1)),     # tracelessness as a substitution
          Y[n-1, n-1]: -sum(Y[i, i] for i in range(n-1))}
    return X, Y, tl, sp.eye(n)


def Apow(p, Mx, I):
    return I + p * eps * Mx + (p * (p - 1) / 2) * eps**2 * (Mx * Mx)


def hessian(word, I):
    P = I
    for M in word:
        P = P * M
    return sp.expand(sp.trace(sp.expand(P)).coeff(eps, 2))


def analyze(n, word_fn, label):
    X, Y, tl, I = setup(n)
    H = sp.expand(hessian(word_fn(X, Y, I), I).subs(tl, simultaneous=True))      # traceless sl(n)
    trX2 = sp.expand(sum(X[i, j] * X[j, i] for i in range(n) for j in range(n)).subs(tl, simultaneous=True))
    nonsep = sp.expand(H - H.subs(a, 0) - H.subs(b, 0) + H.subs({a: 0, b: 0}))
    Hp = sp.Poly(nonsep, a, b) if nonsep != 0 else None
    monos = [m for m, _ in (Hp.terms() if Hp else [])]
    rank1 = all(sp.expand(sp.cancel(c / trX2)).free_symbols == set() for _, c in (Hp.terms() if Hp else []))
    print(f"[{label}] SL({n}) traceless: bidegree ({sp.degree(H,a)},{sp.degree(H,b)}); "
          f"non-sep monomials {monos}; RANK-1 (all coeffs ∝ tr(X^2)): {rank1}")


if __name__ == "__main__":
    # the exact e_2 <-> tr(X^2) identity (with proper expand)
    X4, Y4, tl4, I4 = setup(4)
    A4 = I4 + eps * X4
    e2h = sp.expand(sp.expand((sp.trace(A4)**2 - sp.trace(A4*A4)) / 2).coeff(eps, 2).subs(tl4, simultaneous=True))
    trX2 = sp.expand(sum(X4[i, j]*X4[j, i] for i in range(4) for j in range(4)).subs(tl4, simultaneous=True))
    print(f"identity: e_2=tr(Lambda^2 A) Hessian == -tr(X^2)/2 on sl(4): {sp.expand(e2h + trX2/2) == 0}")
    analyze(4, lambda X, Y, I: [Apow(a, X, I), I + eps*Y, Apow(b, X, I), I + eps*Y], "tr(A^a B A^b B)")
    analyze(4, lambda X, Y, I: [Apow(a, X, I), Apow(2, Y, I), Apow(b, X, I), I + eps*Y], "tr(A^a B^2 A^b B)")
    analyze(5, lambda X, Y, I: [Apow(a, X, I), I + eps*Y, Apow(b, X, I), I + eps*Y], "tr(A^a B A^b B)")
