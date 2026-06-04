"""B70 (trace-ring attack, Track A1) -- first result: the SL(4) two-block obstruction is RANK-1.

The B58 barrier (nilpotent gate, V36): the fixed-line Jacobian's even-k / e_2 sector needs genuine
two-block words tr(A^a B A^b B), whose fixed-line Hessian has a non-separable a*b coupling that no
single-index (r-1)^d recursion generates. This SHARPENS that barrier.

Setup: SL(4), fixed line c=n=4, A=I+eps X, B=I+eps Y (generic 4x4 X,Y). Traces vanish at first order,
so the Hessian (eps^2 coefficient) is the first nonvanishing structure. We compute the full
(a,b)-dependence of the Hessian of tr(A^a B A^b B) and isolate its non-separable part.

RESULT: the Hessian is bidegree (2,2) in (a,b), and its ONLY non-separable term is
    a * b * tr(X^2)
a SINGLE rank-1 bilinear coupling. tr(X^2) is the second power-trace invariant (the eps^2 Hessian of
tr(A^2), hence the degree-2 / even-k sector; recall tr(A^2)=tr(A)^2-2 e_2 with e_2=tr(Lambda^2 A)).
Every separable a^i / b^j piece is single-index (reachable by the nilpotent recursion).

So the two-block obstruction is MINIMAL: exactly one bilinear a*b coupling, in the power-2 (even-k)
sector -- not a high-rank wall. This is the precise structure a first-principles closure of the e_2
sector must absorb (and it bounds the problem: one two-index generator).
"""
import sympy as sp

a, b, eps = sp.symbols("a b epsilon")
X = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"x{i}{j}"))
Y = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"y{i}{j}"))
I4 = sp.eye(4)


def Apow(p, Mx):                          # (I + eps Mx)^p to O(eps^2)
    return I4 + p * eps * Mx + (p * (p - 1) / 2) * eps**2 * (Mx * Mx)


def hessian(word):                        # eps^2 coefficient of tr(product)
    P = I4
    for M in word:
        P = P * M
    return sp.expand(sp.trace(sp.expand(P)).coeff(eps, 2))


H = hessian([Apow(a, X), I4 + eps * Y, Apow(b, X), I4 + eps * Y])     # tr(A^a B A^b B)
trX2 = sp.expand(sum(X[i, j] * X[j, i] for i in range(4) for j in range(4)))   # = tr(X^2)
nonsep = sp.expand(H - H.subs(a, 0) - H.subs(b, 0) + H.subs({a: 0, b: 0}))

print("SL(4) two-block word  tr(A^a B A^b B)  fixed-line Hessian:")
print(f"  bidegree in (a,b) = ({sp.degree(H, a)}, {sp.degree(H, b)})   (<= n-1 = 3, by c=n nilpotency)")
print(f"  non-separable part == a*b*tr(X^2)  (a single RANK-1 bilinear coupling): "
      f"{sp.expand(nonsep - a * b * trX2) == 0}")
print(f"  tr(X^2) is the degree-2 even-k invariant (Hessian of the power trace tr(A^2)).")
print("\nRESULT: the SL(4) two-block obstruction is RANK-1 -- one bilinear a*b coupling in the power-2")
print("(e_2) sector. Bounds the trace-ring closure problem: a single two-index generator.")
