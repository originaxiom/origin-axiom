"""
Core symbolic machinery for the Tran-Yamaguchi (arXiv:2109.07058) adjoint
Reidemeister torsion formula for once-punctured torus bundles, applied to a
GENERAL monodromy word in R, L (not restricted to the tunnel-number-one
LR^{-(n+2)} family).

Coordinates (x1,x2,x3) = (tr rho(g), tr rho(h), tr rho(gh)) on X(pi_1(T)) = C^3,
T = once-punctured torus, pi_1(T) = F(g,h) free of rank 2.

Eq (2.7)-(2.8) of the paper define the action of the two Dehn-twist generators
L, R of the mapping class group (~ SL(2,Z)) on these coordinates:
   (p1,p2,p3)^L = (p3, p2, p2*p3 - p1)
   (p1,p2,p3)^R = (p1, p3, p1*p3 - p2)
matching matrices  L=[[1,0],[1,1]], R=[[1,1],[0,1]]  acting on H1(T;Z)=Z^2.

Porti's formula (eq 2.9): for monodromy phi with matrix A_phi (word W in L,R),
   T_{M,lambda}(rho) = 3 - tr[ d(P^W)/d(x) ]_{x = r([rho])}
evaluated at the fixed point r([rho]) = (x1,x2,x3) of the W-action
corresponding to the representation rho of pi_1(M).

The fixed-point locus {P^W(x)=x} subset C^3 is (generically) the 1-dimensional
character variety X(pi_1(M)) (Porti / Culler-Shalen).  The COMPLETE
(discrete-faithful) structure is singled out on this curve by the standard
fact that at the complete structure the peripheral subgroup is entirely
parabolic; in particular the fiber-boundary curve lambda = [g,h] is parabolic:
   tr rho([g,h]) = x1^2+x2^2+x3^2 - x1*x2*x3 - 2 = -2
i.e.  x1^2 + x2^2 + x3^2 = x1*x2*x3      (the Markov equation).
"""
import sympy as sp

x1, x2, x3 = sp.symbols('x1 x2 x3')

def opL(p):
    p1, p2, p3 = p
    return (p3, p2, sp.expand(p2*p3 - p1))

def opR(p):
    p1, p2, p3 = p
    return (p1, p3, sp.expand(p1*p3 - p2))

def opLinv(p):
    q1, q2, q3 = p
    return (sp.expand(q2*q1 - q3), q2, q1)

def opRinv(p):
    q1, q2, q3 = p
    return (q1, sp.expand(q1*q2 - q3), q2)

OPS = {'L': opL, 'R': opR, 'l': opLinv, 'r': opRinv}

def apply_word(word, p0=(x1, x2, x3)):
    """Apply letters of `word` (string over {L,R,l,r}, l/r = inverses) in
    left-to-right order, matching left-to-right matrix multiplication order
    for the monodromy matrix A_phi = (word as product of L,R matrices)."""
    p = p0
    for ch in word:
        p = OPS[ch](p)
    return tuple(sp.expand(c) for c in p)

def jacobian_and_torsion(word):
    """Return (P^W as tuple of 3 polys, Jacobian matrix, torsion expr 3-tr(J))."""
    P = apply_word(word)
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(P[i], (x1, x2, x3)[j]))
    T = 3 - sp.trace(J)
    return P, J, sp.expand(T)

MARKOV = x1**2 + x2**2 + x3**2 - x1*x2*x3   # =0 at complete/cusped structure

def word_matrix(word):
    """Sanity check: the abelianized (H1) action matrix, should match A_phi."""
    L = sp.Matrix([[1,0],[1,1]])
    R = sp.Matrix([[1,1],[0,1]])
    Linv = L.inv(); Rinv = R.inv()
    M = sp.eye(2)
    mats = {'L': L, 'R': R, 'l': Linv, 'r': Rinv}
    for ch in word:
        M = M * mats[ch]
    return M
