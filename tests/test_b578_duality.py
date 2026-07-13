"""B578 V5 — THE GLOBAL DUALITY (L66): the C2 biconditional for reductive G(C),
with the Galois-descent (quaternionic) obstruction pinned to Hhat^0(Gal(C/R),Z(G)).

Locks (fast, deterministic, Sage-free):
 (1) obstruction group Hhat^0(Gal, mu_N) = Z/gcd(2,N); E6(mu_3) TRIVIAL, E7/SL2(mu_2) = Z/2;
 (2) descent algebra tau^2 = inn(z), z=sigma(g)g central at SL(2); both real forms realise both signs;
 (3) the fig-8 object is on the NO side of (A),(B),(C): tr(ab) non-real (C2);
 (4) sigma moves the 27-character (B573): P(z0) non-real, P(z0bar)=P(z0)*.
FS values (E6 27 COMPLEX, E6 78 REAL, E7 56 PSEUDOREAL) are Sage-verified in the arc."""
import numpy as np
import sympy as sp

s3 = sp.sqrt(3); I = sp.I


# ---------- (1) obstruction group Hhat^0(Gal(C/R), Z(G)) = Z/gcd(2,N) ----------
def tate_H0_muN(N):
    """Z=mu_N ~ Z/N, complex conjugation = inversion = negation. Tate Hhat^0 = M^G/N_G(M)."""
    conj = lambda k: (-k) % N
    fixed = {k for k in range(N) if conj(k) == k}          # M^G = mu_gcd(2,N)
    norm_img = {(k + conj(k)) % N for k in range(N)}       # N_G(M) = {0}
    assert norm_img == {0}
    return len(fixed)

def test_obstruction_group_order():
    for N in [2, 3, 4, 6, 12]:
        assert tate_H0_muN(N) == np.gcd(2, N)
    assert tate_H0_muN(3) == 1     # E6: obstruction group TRIVIAL -> descent unconditional
    assert tate_H0_muN(2) == 2     # E7 / SL2: Z/2 -> quaternionic obstruction CAN bite


# ---------- (2) descent algebra at SL(2,C): tau^2 = inn(sigma(g) g) ----------
def _tau2_is_inn_z(g):
    """tau(x)=g^-1 conj(x) g ; check tau^2(x)=z^-1 x z with z=conj(g) g on random SL(2,C)."""
    ginv = np.linalg.inv(g); z = np.conj(g) @ g
    rng = np.random.default_rng(0)
    for _ in range(30):
        x = rng.standard_normal((2, 2)) + 1j*rng.standard_normal((2, 2))
        x = x / np.sqrt(np.linalg.det(x))
        tau = ginv @ np.conj(x) @ g
        tau2 = ginv @ np.conj(tau) @ g
        assert np.linalg.norm(tau2 - np.linalg.inv(z) @ x @ z) < 1e-9
    return z

def test_descent_algebra_and_both_real_forms():
    z0 = _tau2_is_inn_z(np.eye(2, dtype=complex))            # SL(2,R): g=I, z=+I (omega=+1)
    assert np.linalg.norm(z0 - np.eye(2)) < 1e-12
    J = np.array([[0, 1], [-1, 0]], complex)                 # SU(2): conj(J)J = -I (omega=-1)
    z1 = _tau2_is_inn_z(J)
    assert np.linalg.norm(z1 + np.eye(2)) < 1e-12
    # both z scalar => tau honest involution => both classes of Hhat^0(Gal,mu_2) hit a real form.


# ---------- (3) the object: NO side of (A),(B),(C) [C2] ----------
w = sp.Rational(-1, 2) + s3*I/2
A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-w, 1]])
gen = {'a': A, 'A': A.inv(), 'b': B, 'B': B.inv()}
def _wd(s):
    R = sp.eye(2)
    for c in s: R = R*gen[c]
    return R

def test_object_no_real_form():
    assert sp.simplify(_wd('abABaBAbaB')) == sp.eye(2)                       # fig-8 relator
    t_ab = sp.simplify(sp.trace(_wd('ab')))
    assert t_ab == sp.Rational(5, 2) - s3*I/2 and sp.im(t_ab) != 0           # (A) FAILS
    assert sp.simplify(sp.trace(_wd('abAB'))) == sp.Rational(3, 2) - s3*I/2  # irreducible


# ---------- (4) sigma moves the 27-character [B573] ----------
def test_sigma_moves_27_character():
    z = sp.symbols('z')
    P = sp.expand(sp.chebyshevu(16, z/2) + sp.chebyshevu(8, z/2) + 1)
    assert all(c == int(c) for c in sp.Poly(P, z).all_coeffs())             # integer 27-char
    z0 = sp.Rational(3, 2) + s3*I/2
    Pz0 = sp.simplify(P.subs(z, z0))
    assert Pz0 == sp.Rational(6807, 2) + sp.Rational(4965, 2)*s3*I           # non-real
    assert sp.simplify(P.subs(z, sp.conjugate(z0)) - sp.conjugate(Pz0)) == 0 # Galois image


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print("ok", name)
