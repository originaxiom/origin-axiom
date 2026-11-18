"""B1957: the physical lane's package 'registered domain index join' (2026-11-16), its four field and domain notes
(PHYSICAL_FIELDS_AND_COMPLETE_DOMAIN, MARKED_PHYSICAL_FAMILY_AND_CUSP_FRAMES, PHYSICAL_INNER_ACTION_AND_SPIN_ORBIT,
SPIN_AND_CENTRAL_CORE_LIFT_EQUIVALENCE): the finite identities they use, on main.  The notes are hand derivations on
the lane's supplied parent; their analysis (domains, kernels, the Hodge passage) is not here and is not verified.
 F1  the cubic of the parent: W = (1/2) tr(q Dbar_A r - r Dbar_A q) with Dbar_A = d - i[A, .] has cubic part
     -i tr(u [a, v]) = i tr(a [u, v]) (random matrices).
 F2  the weights of the field maps under z' = f(z), d = f', s^2 = 1/d: |d| s/conj(d) = conj(s); the three kinetic
     densities (Omega^2, 1/2, Omega) with the maps lambda' = lambda, a' = a/conj(d), xi' = s xi and the area factor
     |d|^2 are unchanged; for a unitary V of determinant 1, J V = conj(V) J.  The two hand controls: z' = iz gives the
     input form the phase i and the target form -i; z' = 2z gives a' = a/2, xi' = xi/sqrt 2.
 F3  the central element on the half-root representatives: with weights (m, n) in V_(3/2) (x) V_(3/2) the gauge phase
     exp(-i pi (m + n)) is -1, +1, +1, -1 on the four representatives, the flavour centre is +1, -1, -1, +1, and their
     product is -1 on every one.
 F4  the native triplet against one common character: the three parity characters of the axis triplet are distinct
     and none is trivial, so a map to a space on which the inner group acts by one character has rank at most 1,
     and rank 0 for the trivial character.
 F5  the quaternion conjugacies U_p rho(h) U_p^-1 = p_h rho(h) with U = j, i, k for p = (-, +), (+, -), (-, -) on
     (a, b) -> (i, j); U_p^2 = -1; the sixteen labels (eta, eps) fall into four orbits under (eta, eps) -> (eta p, eps p),
     with eta eps invariant.
 F6  the cusp transition: the phase of sqrt(2 pi i w) changes sign under zeta -> zeta + 1 (w = exp(2 pi i zeta)).
 F7  E8's 248 under the half-turn Zeta: 120 coefficients periodic and 128 antiperiodic (integer and half-integer
     root coordinates)."""
import functools, itertools, cmath, math
import numpy as np
print = functools.partial(print, flush=True)
qi = np.array([[1j, 0], [0, -1j]]); qj = np.array([[0, 1], [-1, 0]], dtype=complex); qk = qi @ qj; I2 = np.eye(2, dtype=complex)

if __name__ == "__main__":
    rng = np.random.default_rng(31); rm = lambda n=3: rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); com = lambda x, y: x @ y - y @ x
    w = 0.0
    for _ in range(50):
        a, u, v = rm(), rm(), rm(); cubic = 0.5 * (np.trace(u @ (-1j * com(a, v))) - np.trace(v @ (-1j * com(a, u)))); w = max(w, abs(cubic + 1j * np.trace(u @ com(a, v))), abs(cubic - 1j * np.trace(a @ com(u, v))))
    print("F1: the cubic part of the parent is -i tr(u [a, v]) = i tr(a [u, v]): largest difference %.1e" % w)
    w2 = 0.0; w3 = 0.0
    for _ in range(200):
        d = complex(rng.normal(), rng.normal()); s = cmath.sqrt(1 / d); Om, lam, aa, xi = abs(rng.normal()) + 0.3, rm(1)[0, 0], rm(1)[0, 0], rm(1)[0, 0]
        w2 = max(w2, abs(abs(d) * s / d.conjugate() - s.conjugate()))
        Omp = Om / abs(d); area = abs(d) ** 2; k = (Omp ** 2 * abs(lam) ** 2 * area - Om ** 2 * abs(lam) ** 2, 0.5 * abs(aa / d.conjugate()) ** 2 * area - 0.5 * abs(aa) ** 2, Omp * abs(s * xi) ** 2 * area - Om * abs(xi) ** 2); w3 = max(w3, max(abs(x) for x in k))
    th = rng.normal(size=3); V = None
    from scipy.linalg import expm
    V = expm(1j * (th[0] * np.array([[0, 1], [1, 0]]) + th[1] * np.array([[0, -1j], [1j, 0]]) + th[2] * np.array([[1, 0], [0, -1]]))); J = np.array([[0, 1], [-1, 0]])
    d = 1j; s = cmath.exp(-1j * math.pi / 4)
    print("F2: |d| s/conj(d) = conj(s): %.1e; the three kinetic densities unchanged: %.1e; J V = conj(V) J for V in SU(2): %s; at z' = iz: s^2 d = %s, the input form's phase 1/conj(d) = %s and the target's 1/d = %s; at z' = 2z: a' = a/2 and |s| = %.4f" % (
        w2, w3, np.allclose(J @ V, V.conj() @ J), np.round(s * s * d, 12), 1 / d.conjugate(), 1 / d, abs(cmath.sqrt(0.5))))
    reps = [(1.5, 1.5, 0), (-1.5, 1.5, 1), (1.5, -1.5, 1), (-1.5, -1.5, 2)]
    out = [(round(cmath.exp(-1j * math.pi * (m + n)).real), (1 if deg in (0, 2) else -1)) for m, n, deg in reps]
    print("F3: (gauge phase, flavour centre) on the four half-root representatives: %s; their product is -1 on each: %s" % (out, all(a * b == -1 for a, b in out)))
    chars = [(1, -1, -1), (-1, 1, -1)]          # the signs of O at rho(a) = i and rho(b) = j on the axes (i, j, k)
    lines = [(chars[0][ax], chars[1][ax]) for ax in range(3)]
    print("F4: the characters of the three axis lines on (a, b): %s; distinct: %s; none trivial: %s; so a common character matches at most one line (rank at most 1) and the trivial one matches none" % (lines, len(set(lines)) == 3, (1, 1) not in lines))
    conj = lambda U, x: U @ x @ np.linalg.inv(U); sgn = lambda U, x: 1 if np.allclose(conj(U, x), x) else (-1 if np.allclose(conj(U, x), -x) else None)
    print("F5: (sign on rho(a) = i, sign on rho(b) = j) under conjugation by j, i, k: %s; each squares to -1: %s" % ([(sgn(U, qi), sgn(U, qj)) for U in (qj, qi, qk)], all(np.allclose(U @ U, -I2) for U in (qj, qi, qk))))
    labels = list(itertools.product(list(itertools.product((1, -1), repeat=2)), repeat=2)); orbits = set()
    for eta, ep in labels:
        orbits.add(frozenset((tuple(e * p for e, p in zip(eta, pp)), tuple(e * p for e, p in zip(ep, pp))) for pp in itertools.product((1, -1), repeat=2)))
    inv = all(len({tuple(a * b for a, b in zip(e, f)) for e, f in o}) == 1 for o in orbits)
    print("F5: labels %d; orbits under the diagonal operation: %d, each of size %s; eta eps constant on each orbit: %s" % (len(labels), len(orbits), sorted({len(o) for o in orbits}), inv))
    z = complex(0.3, 0.8); ph = lambda zeta: (lambda x: x / abs(x))(cmath.exp(1j * math.pi * zeta) * cmath.sqrt(2j * math.pi))
    print("F6: the phase of sqrt(2 pi i w) at zeta + 1 over its value at zeta: %s" % np.round(ph(z + 1) / ph(z), 12))
    roots = set()
    for i, j in itertools.combinations(range(8), 2):
        for si in (1, -1):
            for sj in (1, -1):
                v = [0] * 8; v[i] = si; v[j] = sj; roots.add(tuple(v))
    half = [tuple(s / 2 for s in signs) for signs in itertools.product((1, -1), repeat=8) if sum(1 for x in signs if x < 0) % 2 == 0]
    print("F7: E8: %d roots with integer coordinates and 8 Cartan directions make %d; %d with half-integer coordinates; together %d" % (len(roots), len(roots) + 8, len(half), len(roots) + 8 + len(half)))
