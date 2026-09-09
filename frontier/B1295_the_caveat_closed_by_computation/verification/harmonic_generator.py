"""B1295 / D4(a) -- THE COEFFICIENT c_(+-2,0): the harmonic 1-form generating H^1(m004; R), computed by
Hejhal-type collocation (B792/B1007's machinery, re-purposed from the Maass eigenproblem to the
INHOMOGENEOUS equivariance problem), and its cusp Fourier coefficients read off.

Setup (Riley holonomy, cusp at infinity, as in B1007's reference solver):
    A = [[1,1],[0,1]]  (meridian, z -> z+1),   B = [[1,0],[-w,1]],  w = (-1+i sqrt3)/2.
    chi: Gamma -> Z the abelianisation, chi(A) = chi(B) = 1 (both Riley generators are meridians).
The harmonic generator omega = d phi with phi: H^3 -> R harmonic and chi-equivariant,
    phi(gamma P) = phi(P) + chi(gamma).
Write phi = phi_lin(z) + psi(z,t), phi_lin the R-linear functional with phi_lin(1) = 1 and
phi_lin(tau) = chi(T) for the second cusp translation T (z -> z + tau); psi is Lambda-periodic,
harmonic on all of H^3 and bounded as t -> inf, hence
    psi = c_0 + sum_{0 != mu in Lambda*} c_mu * t K_1(2 pi |mu| t) * e^{2 pi i <mu, z>}
(the mode ODE g'' - g'/t - (2 pi |mu|)^2 g = 0 has t K_1 decaying and t I_1 growing; the constant
mode is A + B t^2 and B = 0 because y^2-growth would make phi an Eisenstein series at its pole).
The radial component of omega is  omega(d/dt) = d_t psi = - sum c_mu 2 pi |mu| t K_0(2 pi |mu| t) e^{..}.

Collocation: sample (z_j, Y) on a horosphere below the fundamental domain, pull each back by an
explicit group element gamma_j (tracked as a WORD so chi(gamma_j) is exact) to (z*_j, t*_j), impose
    psi(z*_j, t*_j) - psi(z_j, Y) = phi_lin(z_j) - phi_lin(z*_j) + chi(gamma_j)
-- an inhomogeneous least-squares system for the real unknowns behind c_mu (c_{-mu} = conj c_mu).
Checks: residual at a second height; the generator relation phi(B P) - phi(P) = 1 at random P;
symmetry-forbidden coefficients at noise level; then the sign partition of the radial component.
"""
import sys, json, itertools
import numpy as np
from scipy.special import k0, k1
from pathlib import Path

SQ3 = np.sqrt(3.0)
OMEGA = complex(-0.5, SQ3 / 2)
A = np.array([[1, 1], [0, 1]], dtype=complex)
Ai = np.array([[1, -1], [0, 1]], dtype=complex)
B = np.array([[1, 0], [-OMEGA, 1]], dtype=complex)
Bi = np.array([[1, 0], [OMEGA, 1]], dtype=complex)
GEN = {'a': A, 'A': Ai, 'b': B, 'B': Bi}
CHI = {'a': 1, 'A': -1, 'b': 1, 'B': -1}
CANCEL = ('aA', 'Aa', 'bB', 'Bb')


def wmat(w):
    m = np.eye(2, dtype=complex)
    for ch in w:
        m = m @ GEN[ch]
    return m


def chi_word(w):
    return sum(CHI[ch] for ch in w)


def reduced_words(maxlen):
    for L in range(1, maxlen + 1):
        for tup in itertools.product('abAB', repeat=L):
            w = ''.join(tup)
            if any(x + y in CANCEL for x, y in zip(w, w[1:])):
                continue
            yield w


def apply_m(M, z, t):
    a, b = M[0]
    c, d = M[1]
    w = c * z + d
    D = abs(w) ** 2 + abs(c) ** 2 * t * t
    return ((a * z + b) * w.conjugate() + a * c.conjugate() * t * t) / D, t / D


# ---------------------------------------------------------------- cusp lattice, with chi of the second translation
def find_cusp_lattice(maxlen=8):
    trans = []
    for w in reduced_words(maxlen):
        M = wmat(w)
        if abs(M[1, 0]) > 1e-9:
            continue
        u = M[0, 0]
        if abs(u - 1) < 1e-9:
            v = M[0, 1]
        elif abs(u + 1) < 1e-9:
            v = -M[0, 1]
        else:
            continue
        if abs(v.imag) > 1e-9:
            trans.append((complex(v), w))
    v0, w0 = min(trans, key=lambda p: abs(p[0].imag))
    k = int(round(v0.real))
    tau = v0 - k                      # T = A^{-k} * (word w0): translation by tau
    chiT = chi_word(w0) - k
    if tau.imag < 0:
        tau, chiT = -tau, -chiT       # inverse element
    return tau, chiT, w0, len(trans)


class Lattice:
    def __init__(self, tau, chiT):
        self.tau = tau
        self.chiT = chiT
        self.M = np.array([[1.0, tau.real], [0.0, tau.imag]])
        self.Minv = np.linalg.inv(self.M)
        U = self.Minv
        self.u1 = complex(U[0, 0], U[0, 1])
        self.u2 = complex(U[1, 0], U[1, 1])
        self.covol = abs(tau.imag)

    def coords(self, z):
        return self.Minv @ np.array([z.real, z.imag])

    def phi_lin(self, z):
        n1, n2 = self.coords(z)
        return n1 + self.chiT * n2

    def reduce(self, z):
        """z -> z - (n1 + n2 tau); the group element applied is A^{-n1} T^{-n2}, chi = -(n1 + chiT n2)."""
        n = np.round(self.coords(z))
        return z - (n[0] + n[1] * self.tau), -(int(n[0]) + self.chiT * int(n[1]))

    def modes(self, Rcut):
        N1 = int(Rcut * abs(self.u2) * self.covol) + 3
        N2 = int(Rcut * abs(self.u1) * self.covol) + 3
        out = []
        for m1 in range(-N1, N1 + 1):
            for m2 in range(-N2, N2 + 1):
                if m1 == 0 and m2 == 0:
                    continue
                mu = m1 * self.u1 + m2 * self.u2
                if abs(mu) <= Rcut:
                    out.append((m1, m2, mu))
        return out


def build_moves(maxlen=6, cmax=2.2):
    """(matrix, chi) pairs; deduped on the FULL matrix up to sign so chi is well defined."""
    mats, seen = [], set()
    for w in reduced_words(maxlen):
        M = wmat(w)
        c = M[1, 0]
        if abs(c) < 1e-12 or abs(c) > cmax:
            continue
        s = 1
        if c.real < 0 or (abs(c.real) < 1e-12 and c.imag < 0):
            M = -M
        key = tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), 8))
        if key in seen:
            continue
        seen.add(key)
        mats.append((M, chi_word(w)))
    return mats


def reduce_pt(lat, moves, z, t, itmax=400):
    """Pull (z,t) to its max-height translate; return (z*, t*, chi(gamma)) with gamma tracked exactly."""
    z, ch = lat.reduce(z)
    chi = ch
    for _ in range(itmax):
        best = None
        for M, cM in moves:
            z2, t2 = apply_m(M, z, t)
            if t2 > t * (1 + 1e-13) and (best is None or t2 > best[1]):
                best = (z2, t2, cM)
        if best is None:
            break
        z, t, cM = best
        chi += cM
        z, ch = lat.reduce(z)
        chi += ch
    return z, t, chi


# ---------------------------------------------------------------- the solve
def basis_row(lat, modes, z, t):
    """Real design row: for each mode mu, the coefficient of Re c_mu and Im c_mu in psi(z,t), pairing mu with -mu.
    We parametrise by mu in a half-lattice; psi = sum_{mu in half} 2 Re(c_mu e^{i theta}) t K_1(...)."""
    zs = np.array([z.real, z.imag])
    out = np.empty(2 * len(modes))
    for j, (m1, m2, mu) in enumerate(modes):
        th = 2 * np.pi * (mu.real * z.real + mu.imag * z.imag)
        g = t * k1(2 * np.pi * abs(mu) * t)
        out[2 * j] = 2 * np.cos(th) * g        # Re c
        out[2 * j + 1] = -2 * np.sin(th) * g   # Im c
    return out


def half_modes(modes):
    return [m for m in modes if (m[0] > 0) or (m[0] == 0 and m[1] > 0)]


def sample_grid(lat, n1, n2, rng, jitter=0.35):
    zs = []
    for i in range(n1):
        for j in range(n2):
            a = (i + 0.5 + jitter * rng.uniform(-1, 1)) / n1
            b = (j + 0.5 + jitter * rng.uniform(-1, 1)) / n2
            zs.append(a + b * lat.tau)
    return zs


def solve(lat, moves, Y, Rcut, npts, seed):
    modes = half_modes(lat.modes(Rcut))
    rng = np.random.default_rng(seed)
    n2 = int(np.sqrt(npts * abs(lat.tau)))
    n1 = max(4, npts // max(n2, 1))
    zs = sample_grid(lat, n1, n2, rng)
    rows, rhs, tstars = [], [], []
    for z in zs:
        zr, _ = lat.reduce(z)                      # the base point P = (zr, Y); chi is tracked FROM zr
        zs_, ts_, chi = reduce_pt(lat, moves, zr, Y)
        if ts_ <= Y * (1 + 1e-9):
            continue                       # the point already sits at max height: no information
        rows.append(basis_row(lat, modes, zs_, ts_) - basis_row(lat, modes, zr, Y))
        rhs.append(lat.phi_lin(zr) - lat.phi_lin(zs_) + chi)
        tstars.append(ts_)
    V = np.array(rows); r = np.array(rhs)
    # column scaling for conditioning
    s = np.linalg.norm(V, axis=0); s[s == 0] = 1
    x, res, rank, sv = np.linalg.lstsq(V / s, r, rcond=None)
    x = x / s
    resid = V @ x - r
    c = {}
    for j, (m1, m2, mu) in enumerate(modes):
        c[(m1, m2)] = complex(x[2 * j], x[2 * j + 1])
    return c, modes, dict(n_eq=len(r), n_unknown=2 * len(modes), rank=int(rank), sv_min=float(sv[-1]), sv_max=float(sv[0]),
                          resid_rms=float(np.sqrt(np.mean(resid ** 2))), resid_max=float(np.abs(resid).max()),
                          tstar_min=float(min(tstars)), tstar_max=float(max(tstars)))


def psi_eval(lat, c, z, t):
    v = 0.0
    for (m1, m2), cm in c.items():
        mu = m1 * lat.u1 + m2 * lat.u2
        th = 2 * np.pi * (mu.real * z.real + mu.imag * z.imag)
        v += 2 * (cm * np.exp(1j * th)).real * t * k1(2 * np.pi * abs(mu) * t)
    return v


def phi_eval(lat, c, z, t):
    return lat.phi_lin(z) + psi_eval(lat, c, z, t)


def radial(lat, c, z, t):
    """omega(d/dt) = d_t psi."""
    v = 0.0
    for (m1, m2), cm in c.items():
        mu = m1 * lat.u1 + m2 * lat.u2
        a = 2 * np.pi * abs(mu)
        th = 2 * np.pi * (mu.real * z.real + mu.imag * z.imag)
        v += 2 * (cm * np.exp(1j * th)).real * (-a * t * k0(a * t))
    return v


if __name__ == "__main__":
    Rcut = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0
    Y = float(sys.argv[2]) if len(sys.argv) > 2 else 0.55
    npts = int(sys.argv[3]) if len(sys.argv) > 3 else 900
    tau, chiT, w0, nfound = find_cusp_lattice()
    print(f"cusp lattice: tau = {tau:.12f} (word {w0}, {nfound} parabolics), chi(T) = {chiT}")
    lat = Lattice(tau, chiT)
    moves = build_moves()
    print(f"moves: {len(moves)}; dual basis u1 = {lat.u1:.6f}, u2 = {lat.u2:.6f}")
    # relator sanity: which Riley relator holds, and chi is consistent with it
    for wname in ('aBAb', 'AbaB', 'bABa', 'BabA'):
        W = wmat(wname)
        if np.abs(W @ A - B @ W).max() < 1e-9:
            print(f"relator: w a = b w with w = {wname} (chi(w) = {chi_word(wname)}), so chi(a) = chi(b) is consistent")
    c, modes, info = solve(lat, moves, Y, Rcut, npts, seed=1)
    print("solve:", json.dumps(info))
    # independent checks
    rng = np.random.default_rng(5)
    dev_B, dev_T, nB = 0.0, 0.0, 0
    while nB < 200:
        z = complex(rng.uniform(-1, 1), rng.uniform(-2, 2)); t = rng.uniform(0.6, 1.6)
        zb, tb = apply_m(B, z, t)
        if tb < 0.6:
            continue                                   # keep both P and B.P where the truncation converges
        nB += 1
        dev_B = max(dev_B, abs(phi_eval(lat, c, zb, tb) - phi_eval(lat, c, z, t) - 1.0))
        dev_T = max(dev_T, abs(phi_eval(lat, c, z + tau, t) - phi_eval(lat, c, z, t) - chiT))
    print(f"generator check  phi(B P) - phi(P) - 1 : max |dev| = {dev_B:.2e} over 200 random P with t, t(B.P) >= 0.6")
    print(f"periodicity      phi(P + tau) - phi(P) - chi(T): {dev_T:.2e}")
    # second-height residual
    c2, _, info2 = solve(lat, moves, Y + 0.12, Rcut, npts, seed=2)
    print("second height:", json.dumps(info2))
    keys = sorted(c, key=lambda k: abs(k[0] * lat.u1 + k[1] * lat.u2))
    print("\nlow modes (m1 along the meridian dual, m2 along the second dual):  |mu|   c (height Y)   c (height Y+0.12)")
    for k in keys[:24]:
        mu = k[0] * lat.u1 + k[1] * lat.u2
        print(f"  m = ({k[0]:2d},{k[1]:2d})  |mu| = {abs(mu):.4f}   c = {c[k].real:+.6e}{c[k].imag:+.6e}i   c' = {c2[k].real:+.6e}{c2[k].imag:+.6e}i")
    json.dump({"tau": [tau.real, tau.imag], "chiT": chiT, "info": info, "info2": info2,
               "c": {f"{k[0]},{k[1]}": [c[k].real, c[k].imag] for k in keys},
               "c2": {f"{k[0]},{k[1]}": [c2[k].real, c2[k].imag] for k in keys}},
              open(Path(__file__).with_name("harmonic_generator.json"), "w"), indent=1)
