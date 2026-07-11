"""
Movement XIX — the golden eigenvalue ladder explained: the trace-zero point.

Movement XVII found that at a generic fixed point of the 9d trace map sigma*, the
linearization D sigma* has a generic spectrum -- but at ONE special fixed point it
carried the golden ladder |lambda| in {1/phi, 1, phi} x3.  That point is now
identified and the ladder derived.

THE SPECIAL POINT is the TRACE-ZERO representation of F4 x|_phi Z:
  * tr(rho(g)) = 0 for all four generators a,b,A,B.  By Cayley-Hamilton (trace 0,
    det 1) this forces rho(g)^2 = -I: every generator is an ORDER-4 element
    (order 2 in PSL2).  The maximally symmetric irreducible character.
  * its twist is tau = e^{i pi/3}, a primitive 6TH ROOT OF UNITY (tau^3=-1).

At this point D sigma* has eigenvalues EXACTLY
      {phi, 1, -1/phi}  (x)  {1, omega, omega^2}     (omega = e^{2 pi i/3})
i.e. the Fibonacci eigenvalues {phi, -1/phi} together with 1, tensored with the
cube roots of unity.  The GOLDEN factor comes from the growth; the CUBE-ROOT (Z/3)
factor comes from the order-6 twist.  So the ladder is not an accident -- it is the
signature of the trace-zero representation and its 6th-root-of-unity twist.

No physics.
"""
import numpy as np
from scipy.optimize import least_squares
from scipy.linalg import expm

PHI = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
GENS = ['a', 'b', 'A', 'B']
phi = (1 + np.sqrt(5)) / 2
om = np.exp(2j * np.pi / 3)


def _mat(v):
    return np.array([[v[0], v[1]], [v[2], v[3]]], complex)


def _unpack(x):
    z = x[:len(x) // 2] + 1j * x[len(x) // 2:]
    return np.diag([z[0], 1 / z[0]]), {g: _mat(z[1 + 4 * i:5 + 4 * i]) for i, g in enumerate(GENS)}


def _wm(w, Ms, inv):
    P = np.eye(2, dtype=complex)
    for ch in w:
        P = P @ (Ms[ch] if ch in Ms else inv[ch.lower()])
    return P


def _resid(x):
    T, Ms = _unpack(x)
    Ti = np.linalg.inv(T)
    inv = {g: np.linalg.inv(Ms[g]) for g in GENS}
    r = [T @ Ms[g] @ Ti - _wm(PHI[g], Ms, inv) for g in GENS]
    d = np.array([np.linalg.det(Ms[g]) - 1 for g in GENS])
    flat = np.concatenate([m.ravel() for m in r] + [d])
    return np.concatenate([flat.real, flat.imag])


def trace_zero_point(seed=2):
    """Unconstrained fixed-point search at seed 2 lands on the trace-zero point directly."""
    np.random.seed(seed)
    for _ in range(200):
        s = least_squares(_resid, np.random.randn(34) * 0.9, method='lm', max_nfev=1500)
        if s.cost < 1e-18:
            T, Ms = _unpack(s.x)
            C = Ms['a'] @ Ms['b'] @ np.linalg.inv(Ms['a']) @ np.linalg.inv(Ms['b'])
            if abs(np.trace(C) - 2) > 0.3:                # irreducible
                return T, Ms
    return None


def dsigma_spectrum(T, Ms, eps=1e-6):
    Ti = np.linalg.inv(T)
    rho0 = dict(Ms)

    def Gf(rho):
        inv = {g: np.linalg.inv(rho[g]) for g in GENS}
        return {g: Ti @ _wm(PHI[g], rho, inv) @ T for g in GENS}
    E = [np.array([[0, 1], [0, 0]], complex), np.array([[0, 0], [1, 0]], complex),
         np.array([[1, 0], [0, -1]], complex)]

    def tc(rp):
        c = []
        for g in GENS:
            X = (rp[g] @ np.linalg.inv(rho0[g]) - np.eye(2)) / eps
            c += [X[0, 1], X[1, 0], X[0, 0]]
        return np.array(c, complex)

    def pert(idx, sgn):
        out = dict(rho0)
        out[GENS[idx // 3]] = expm(sgn * eps * E[idx % 3]) @ rho0[GENS[idx // 3]]
        return out
    DG = np.zeros((12, 12), complex)
    for j in range(12):
        DG[:, j] = (tc(Gf(pert(j, +1))) - tc(Gf(pert(j, -1)))) / 2
    conj = []
    for k in range(3):
        c = []
        for g in GENS:
            X = E[k] - rho0[g] @ E[k] @ np.linalg.inv(rho0[g])
            c += [X[0, 1], X[1, 0], X[0, 0]]
        conj.append(np.array(c, complex))
    Q, _ = np.linalg.qr(np.array(conj).T)
    U, _, _ = np.linalg.svd(np.eye(12) - Q @ Q.conj().T)
    comp = U[:, :9]
    return np.linalg.eigvals(comp.conj().T @ DG @ comp)


def ladder_matches(ev):
    """Set-based match (twist may be e^{+/- i pi/3}, flipping omega<->omega-bar)."""
    pred = [r * u for r in (phi, 1, -1 / phi) for u in (1, om, om ** 2)]
    remaining = list(pred)
    matched = 0
    for e in ev:
        for i, p in enumerate(remaining):
            if abs(e - p) < 1e-3:
                matched += 1
                remaining.pop(i)
                break
    return matched


if __name__ == "__main__":
    T, Ms = trace_zero_point()
    print("trace-zero fixed point:")
    print("  traces:", [f"{np.trace(Ms[g]):.1e}" for g in GENS])
    print("  rho(g)^2 = -I (order 4):", all(np.allclose(Ms[g] @ Ms[g], -np.eye(2), atol=1e-4) for g in GENS))
    print(f"  twist tau = {T[0,0]:.5f}  tau^6 = {T[0,0]**6:.4f}  (6th root of unity)")
    ev = dsigma_spectrum(T, Ms)
    print(f"  Dsigma* ladder {{phi,1,-1/phi}} x {{1,om,om^2}} matches: {ladder_matches(ev)}/9")
