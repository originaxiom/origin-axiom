"""P-540 (2026-11-19): WHAT PRODUCES B940's +- PAIRING.  B933 DESIGN section 5a claimed the symmetry spec(D) = -spec(D)
from J = sigma_2 o conj; main found at S274 (tests/test_b933_j_commutes_with_d.py) that J COMMUTES with D as written, so it
doubles eigenvalues (Kramers) and does not pair lambda with -lambda.  The candidate P-540 named: m004's orientation-
reversing isometry, which reverses the 3d Dirac operator if it keeps the spin structure and the twist.  This script checks
it, exactly where the statement is algebraic and on random samples where it is an identity of smooth maps:

  E1 (exact, Q(omega)): g = [[1, x], [0, 1]] with x = 1 + omega satisfies  g conj(A) g^-1 = A  and  g conj(B) g^-1 = B A B^-1
     as matrices of SL(2, C), signs included, for the lifted generators A, B of rho_1 (B933 section 1); and g conj(g) = A.
     So Psi(h) = g conj(h) g^-1 maps the lifted group <A, B> into itself, and Psi^2 is conjugation by A, so Psi maps it ONTO
     itself.  The same holds for rho_2 = (-A, -B).  Geometrically Phi(z, t) = (conj(z) + 1 + omega, t) is an orientation-
     reversing isometry of H^3 normalising the group, whose square is the meridian's translation: an orientation-reversing
     involution of m004 that keeps each lift, i.e. each spin structure.
  E2 (exact, symbolic): U psi(p) = sigma_2 psi(Phi^-1 p) ANTICOMMUTES with D = -i[t(s1 dx + s2 dy + s3 dt) - s3] (B933
     DESIGN section 2), on a generic smooth spinor.
  E3 (exact, symbolic): sigma_2 k sigma_2^-1 = conj(k) for every k in SU(2).
  E4 (exact, symbolic): the Iwasawa section has s(conj z, t) = conj(s(z, t)) and s(z + x, t) = g s(z, t).
  E5 (random samples, 200, seeded): the cocycle k(h, p) = s(h p)^-1 h s(p) lies in SU(2) and k(conj h, R p) = conj(k(h, p)),
     R(z, t) = (conj z, t), for random h in SL(2, C) and p in H^3.
  With E1 to E5, U maps a rho_1-automorphic spinor (psi(h p) = conj(k(h, p)) psi(p), B933 DESIGN section 3) to a
  rho_1-automorphic spinor, is unitary on L^2, and U D U^-1 = -D; hence spec(D) = -spec(D) with multiplicities.  This is
  main's derivation from these identities; the script checks each identity, not the operator-theoretic closing step.
    python3 -B pairing_source.py > pairing_source_run.txt"""
import sympy as sp
import numpy as np

I = sp.I
w = sp.Rational(-1, 2) + sp.sqrt(3) * I / 2
A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-w, 1]])
conj = lambda M: M.applyfunc(sp.conjugate)
zero = lambda M: all(sp.simplify(sp.expand_complex(e)) == 0 for e in M)


def e1():
    x0 = 1 + w; g = sp.Matrix([[1, x0], [0, 1]]); gi = g.inv()
    Psi = lambda h: g * conj(h) * gi
    r = dict(x_equals_1_plus_omega=zero(sp.Matrix([sp.sqrt(3) + I]) / (sp.sqrt(3) - I) - sp.Matrix([x0])),
             A_to_A=zero(Psi(A) - A), B_to_BAB=zero(Psi(B) - B * A * B.inv()),
             minus_A_to_minus_A=zero(Psi(-A) - (-A)), minus_B_to_rho2_word=zero(Psi(-B) - (-B) * (-A) * (-B).inv()),
             g_conj_g_is_A=zero(g * conj(g) - A), traces_plus_2=(sp.simplify(Psi(A).trace()) == 2 and sp.simplify(Psi(B).trace()) == 2))
    gw = sp.Matrix([[1, 1 + sp.conjugate(w)], [0, 1]])                      # control: the conjugate translation
    r["control_x_conj_fails"] = not zero(gw * conj(B) * gw.inv() - B * A * B.inv())
    r["control_no_g_fails"] = not zero(conj(B) - B * A * B.inv())
    return r


def e2():
    X, Y, T = sp.symbols("x y t", real=True)
    s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
    f1, f2 = sp.Function("f1"), sp.Function("f2")
    a, b = sp.symbols("a b", real=True)                     # Phi^-1(z) = conj(z - x0): (x, y) -> (x - a, -(y - b))
    D = lambda P: -I * (T * (s1 * P.diff(X) + s2 * P.diff(Y) + s3 * P.diff(T)) - s3 * P)
    psi = sp.Matrix([f1(X, Y, T), f2(X, Y, T)])
    sub = {X: X - a, Y: -(Y - b)}
    def anti(M):
        return all(sp.simplify(e) == 0 for e in (D(M * psi.subs(sub, simultaneous=True)) + M * D(psi).subs(sub, simultaneous=True)))   # no complex expansion of derivatives
    return dict(U_D_plus_D_U_is_zero=anti(s2),
                control_identity_in_place_of_sigma2_fails=not anti(sp.eye(2)), control_sigma1_fails=not anti(s1),
                control_sigma3_fails=not anti(s3))


def e3():
    p, q, r, u = sp.symbols("p q r u", real=True)
    al, be = p + I * q, r + I * u
    k = sp.Matrix([[al, -sp.conjugate(be)], [be, sp.conjugate(al)]])
    s2 = sp.Matrix([[0, -I], [I, 0]])
    return dict(sigma2_k_sigma2inv_is_conj_k=zero(s2 * k * s2.inv() - conj(k)))


def e4():
    X, Y = sp.symbols("x y", real=True); T = sp.symbols("t", positive=True)
    z = X + I * Y; x0 = 1 + w
    s = lambda zz, tt: sp.Matrix([[sp.sqrt(tt), zz / sp.sqrt(tt)], [0, 1 / sp.sqrt(tt)]])
    return dict(s_of_reflection_is_conj_s=zero(s(sp.conjugate(z), T) - conj(s(z, T))),
                s_of_translate_is_g_s=zero(s(z + x0, T) - sp.Matrix([[1, x0], [0, 1]]) * s(z, T)))


def act(h, z, t):
    a, b, c, d = h[0, 0], h[0, 1], h[1, 0], h[1, 1]
    den = abs(c * z + d) ** 2 + abs(c) ** 2 * t * t
    return ((a * z + b) * np.conj(c * z + d) + a * np.conj(c) * t * t) / den, t / den


def sec(z, t):
    return np.array([[np.sqrt(t), z / np.sqrt(t)], [0, 1 / np.sqrt(t)]], complex)


def kk(h, z, t):
    z2, t2 = act(h, z, t)
    return np.linalg.inv(sec(z2, t2)) @ h @ sec(z, t)


def e5(n=200, seed=540):
    rng = np.random.default_rng(seed); su, cj, ctl = 0.0, 0.0, 0.0
    for _ in range(n):
        h = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); h = h / np.sqrt(np.linalg.det(h))
        z, t = complex(rng.normal(), rng.normal()), float(np.exp(rng.normal()))
        k = kk(h, z, t)
        su = max(su, np.abs(k.conj().T @ k - np.eye(2)).max(), abs(np.linalg.det(k) - 1))
        cj = max(cj, np.abs(kk(h.conj(), z.conjugate(), t) - k.conj()).max())
        ctl = max(ctl, np.abs(kk(h.conj(), z.conjugate(), t) - k).max())      # control: without the conjugation
    return dict(samples=n, k_in_SU2_max_defect=float(su), k_conj_relation_max_defect=float(cj),
                control_without_conj_max_defect=float(ctl), holds=bool(su < 1e-10 and cj < 1e-10 and ctl > 1e-3))


def main():
    for name, f in (("E1", e1), ("E2", e2), ("E3", e3), ("E4", e4), ("E5", e5)):
        r = f(); print(name, r)
    ok = all(all(v for k, v in f().items() if isinstance(v, bool)) for f in (e1, e2, e3, e4)) and e5()["holds"]
    print("ALL HOLD:", ok)


if __name__ == "__main__":
    main()
