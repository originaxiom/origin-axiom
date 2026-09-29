"""B1500 -- two local models whose singular locus is a cone over a torus, checked with own code.
(a) The Harvey-Lawson T^2-cone C = {|z1|=|z2|=|z3|, z1 z2 z3 in R+} in C^3:
    - its link torus's flat metric and lattice (reduced shape tau);
    - the cone is special Lagrangian (omega|C = 0, Im(dz1^dz2^dz3)|C = 0), hence associative in R^7 = R + C^3 for phi = dt^omega + Re Omega;
    - its three smoothings L_j = {|z_j|^2 - c = |z_k|^2 = |z_l|^2, ...} each collapse one circle of the link: which lattice vectors.
(b) The nearly Kaehler S^3 x S^3 = SU(2)^3 / diag SU(2): the fixed set of diagonal conjugation by an element h of U(1) is the torus
    U(1)^3 / diag U(1); its metric from the normal metric (|X1|^2 + |X2|^2 + |X3|^2 on X1 + X2 + X3 = 0) and its lattice."""
import itertools

import numpy as np


def reduce_tau(t):
    if t.imag < 0:
        t = t.conjugate()
    for _ in range(100):
        t = complex(t.real - round(t.real), t.imag)
        if abs(t) < 1 - 1e-12:
            t = -1 / t
        else:
            return t


def lattice_shape(G):
    """Gram matrix of a lattice basis -> reduced shape tau"""
    a = np.sqrt(G[0, 0])
    b = np.sqrt(G[1, 1])
    cos = G[0, 1] / (a * b)
    tau = (b / a) * complex(cos, np.sqrt(1 - cos ** 2))
    return reduce_tau(tau)


# (a) Harvey-Lawson
def hl_point(t1, t2):
    t3 = -t1 - t2
    return np.array([np.exp(1j * t1), np.exp(1j * t2), np.exp(1j * t3)]) / np.sqrt(3)


def realify(z):
    return np.concatenate([z.real, z.imag])


rng = np.random.default_rng(0)
worst_omega, worst_im, worst_metric = 0.0, 0.0, 0.0
for _ in range(200):
    t1, t2 = rng.uniform(0, 2 * np.pi, 2)
    r = rng.uniform(0.3, 2.0)
    p = r * hl_point(t1, t2)
    e1 = r * np.array([1j * np.exp(1j * t1), 0, -1j * np.exp(1j * (-t1 - t2))]) / np.sqrt(3)     # d/dt1
    e2 = r * np.array([0, 1j * np.exp(1j * t2), -1j * np.exp(1j * (-t1 - t2))]) / np.sqrt(3)     # d/dt2
    er = p / r                                                                                  # d/dr
    vecs = [er, e1, e2]
    # Kaehler form omega(u, v) = Im(sum conj(u_i) v_i)
    om = max(abs(np.imag(np.vdot(u, v))) for u, v in itertools.combinations(vecs, 2))
    # Omega = dz1^dz2^dz3 on (er, e1, e2): the determinant of the 3x3 complex matrix
    Om = np.linalg.det(np.array(vecs).T)
    worst_omega = max(worst_omega, om)
    worst_im = max(worst_im, abs(Om.imag) / abs(Om))
    # link metric in (t1, t2) at r = 1
    g = np.array([[np.vdot(u, v).real for v in (e1 / r, e2 / r)] for u in (e1 / r, e2 / r)])
    worst_metric = max(worst_metric, np.abs(g - np.array([[2, 1], [1, 2]]) / 3).max())
print("(a) Harvey-Lawson cone: max |omega| on tangent planes %.1e; max |Im Omega|/|Omega| %.1e (special Lagrangian, phase 0)"
      % (worst_omega, worst_im))
print("    link metric in (t1, t2): (1/3)[[2,1],[1,2]] to %.1e; periods 2 pi in t1, t2 -> Gram %s -> reduced shape %s"
      % (worst_metric, (4 * np.pi ** 2 / 3 * np.array([[2, 1], [1, 2]])).round(3).tolist(),
         np.round(lattice_shape(np.array([[2, 1], [1, 2]]) / 3), 12)))
# lattice vectors and their lengths: (m, n) -> length^2 = (2 m^2 + 2 m n + 2 n^2)/3 * (2 pi)^2
short = sorted(((2 * m * m + 2 * m * n + 2 * n * n) / 3, (m, n)) for m in range(-2, 3) for n in range(-2, 3) if (m, n) != (0, 0))
print("    shortest link circles (t1, t2 periods):", [v for L, v in short if abs(L - short[0][0]) < 1e-12])
# the smoothing L_1 = {|z1|^2 - c = |z2|^2 = |z3|^2}: at z2 = z3 = 0 the T^2 orbit is {(sqrt(c) e^{i t1}, 0, 0)}: the circle of the T^2
# action (t1, t2, t3 = -t1 - t2) that fixes z1 is t1 = 0, i.e. (t1, t2) along (0, 1): (z1, z2, z3) -> (z1, e^{i s} z2, e^{-i s} z3)
collapse = {"L_1 (z2 = z3 = 0)": (0, 1), "L_2 (z1 = z3 = 0)": (1, 0), "L_3 (z1 = z2 = 0)": (1, -1)}
for name, v in collapse.items():
    L = (2 * v[0] ** 2 + 2 * v[0] * v[1] + 2 * v[1] ** 2) / 3
    print("    %s collapses the circle %s, length^2 %.4f (shortest %.4f)" % (name, v, L, short[0][0]))

# (b) nearly Kaehler S^3 x S^3: the torus U(1)^3 / diag U(1), tangent directions (a1, a2, a3) u with a1 + a2 + a3 = 0 in the normal
# metric |X1|^2 + |X2|^2 + |X3|^2; lattice: (theta1, theta2, theta3) in (2 pi Z)^3 modulo the diagonal
P = np.eye(3) - np.ones((3, 3)) / 3                                    # projection onto a1 + a2 + a3 = 0
basis = [P @ np.array([1.0, 0, 0]), P @ np.array([0, 1.0, 0])]        # images of the unit periods e1, e2 generate the quotient lattice
G = np.array([[u @ v for v in basis] for u in basis])
print("(b) S^3 x S^3 torus U(1)^3/U(1): Gram of the period lattice (units (2 pi)^2 |u|^2):", G.round(6).tolist(),
      "-> reduced shape", np.round(lattice_shape(G), 12))
