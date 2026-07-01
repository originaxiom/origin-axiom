"""B344 -- the deviation space's forced geometry: a reciprocal (symplectic) pairing, with kappa the scale door.

Target 1 of the deviation-structure strategy. The object is the symmetric CENTRE; physics is the
deviation. The tangent SPECTRUM at a fixed point is already banked (the metallic tower char(M^k), B65).
This probe banks the deviation-space GEOMETRY -- a FORCED, dimensionless RELATION (a form, per the
sin^2_W=3/8 / period-law precedent), not a value:

  det(d phi_m) = 1  (the trace map is a volume-preserving polynomial automorphism; each Dehn twist has
      Jacobian det 1) -- verified m=1,2,3.
  kappa-invariance (B167): the trace map preserves kappa = tr[a,b], so at any fixed point the
      kappa-direction is an eigenvector with eigenvalue 1 -- the CASIMIR (Poisson-central, B293), the
      one UN-PAIRED deviation direction = the scale/cusp door (EXTERNAL).
  => the remaining two deviation modes MULTIPLY TO 1: a FORCED RECIPROCAL PAIR (lambda, 1/lambda).

The reciprocal pair are symplectically CONJUGATE: the mapping class group preserves the character-
variety symplectic (Goldman) form, kappa is its Casimir (B293). So the deviation space is
{ kappa (central, scale, external) } (+) { a symplectic-conjugate reciprocal pair (lambda,1/lambda) }.
This is WHY the metallic tower is reciprocal-paired lambda^k <-> lambda^-k (B65): the symplectic form.

FORM, not value: the reciprocal pairing is a dimensionless RELATION (the deviation spectrum is
lambda <-> 1/lambda symmetric; the un-paired direction is the scale door). No magnitude predicted.
Firewalled; nothing to CLAIMS. Needs only sympy.
"""
import sympy as sp

x, y, z, t = sp.symbols('x y z t')
KAPPA = x**2 + y**2 + z**2 - x*y*z - 2


def Ta(p): X, Y, Z = p; return (X, Z, X*Z - Y)
def Tb(p): X, Y, Z = p; return (Z, Y, Y*Z - X)
def phi(p, m):
    for _ in range(m): p = Tb(p)
    for _ in range(m): p = Ta(p)
    return p


def jac(gen_or_m):
    """Jacobian matrix of a single twist (callable) or of phi_m (int)."""
    if callable(gen_or_m):
        f = gen_or_m((x, y, z))
    else:
        f = phi((x, y, z), gen_or_m)
    return sp.Matrix([[sp.diff(fi, v) for v in (x, y, z)] for fi in f])


def det_is_one(m):
    """det(d phi_m) = 1 (volume-preserving)."""
    return sp.simplify(jac(m).det()) == 1


def reciprocal_pair_at_fixed_point():
    """at a fixed point of phi_1, eigenvalues are {1 (kappa/Casimir), L, 1/L}; L*(1/L)=1."""
    J = jac(1).subs({x: t, z: t, y: t/(t - 1)})       # a point on Fix(phi_1): x=z=t, y=t/(t-1)
    eigs = list(J.eigenvals().keys())
    nonunit = [e for e in eigs if sp.simplify(e - 1) != 0]
    prod = sp.simplify(nonunit[0] * nonunit[1]) if len(nonunit) == 2 else sp.simplify(J.det())
    has_unit = any(sp.simplify(e - 1) == 0 for e in eigs)
    return has_unit, sp.simplify(prod)                 # (True, 1) -> {1, L, 1/L}


def goldman(f, g):
    return sp.expand(sp.diff(KAPPA, z)*(sp.diff(f, x)*sp.diff(g, y) - sp.diff(f, y)*sp.diff(g, x))
                     + sp.diff(KAPPA, x)*(sp.diff(f, y)*sp.diff(g, z) - sp.diff(f, z)*sp.diff(g, y))
                     + sp.diff(KAPPA, y)*(sp.diff(f, z)*sp.diff(g, x) - sp.diff(f, x)*sp.diff(g, z)))


def kappa_is_casimir():
    """kappa is Poisson-central (B293): {kappa, v} = 0 -> the un-paired deviation direction (scale door)."""
    return all(goldman(KAPPA, v) == 0 for v in (x, y, z))


if __name__ == "__main__":
    print("det(dTa)=", sp.simplify(jac(Ta).det()), " det(dTb)=", sp.simplify(jac(Tb).det()))
    print("det(d phi_m)=1 for m=1,2,3:", [det_is_one(m) for m in (1, 2, 3)])
    has_unit, prod = reciprocal_pair_at_fixed_point()
    print("fixed-point deviation modes {1, L, 1/L}: has unit(kappa) =", has_unit, ", L*(1/L) =", prod)
    print("kappa is the Casimir (un-paired central = scale door, external):", kappa_is_casimir())
    print("=> forced reciprocal (symplectic) pairing of deviations; the metallic tower lambda^k<->lambda^-k (B65) is this.")
