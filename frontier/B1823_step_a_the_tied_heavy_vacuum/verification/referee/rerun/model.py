"""STEP A v2 -- the model (data-free; no measured number is read or compared).

A gauge-consistent heavy sector coupled to the frame's Higgs multiplicity triplet, modular-invariant, with its one-loop
(Coleman-Weinberg) potential.  Two implementations of every function: numpy (double precision, for the searches) and
mpmath (``mp_`` prefix, for the checks at 30+ digits).

THE CONSTRUCTION (each item labelled in DESIGN.md)
  modular group      Mp(2, Z) (half-integral weights), acting on (tau, S) by the frame's own monomial triplet rho_R
                     (W64; B1730 section A): rho_R(T) = e^{i pi/4} L^-1, rho_R(S) = e^{i pi/4} P, L^-1 and P REAL orthogonal.
                     So on the Higgs direction S (a point of CP^2) the action is projective and real:
                         T: (tau, S) -> (tau + 1, L^-1 S),     S: (tau, S) -> (-1/tau, P S).
  Higgs              H = (H_i, H_j, H_k) x (electroweak doublet), one doublet per quaternion unit; vev v * S_hat (x) (0, 1),
                     S_hat a unit vector of C^3.  H's own rho is rho_R up to a character (any character: the bilinear
                     pairing S^T Y below is invariant because the matrices are real orthogonal).
  heavy copy i       vector-like leptons L_i, Lbar_i (doublets, Y = -1/2, +1/2) and E_i, Ebar_i (singlets, Y = -1, +1), with
                         W_i = M Y_L,i(tau) L_i Lbar_i + M Y_E,i(tau) E_i Ebar_i + lambda (H^T Y3_i(tau)) L_i Ebar_i
                     -- every term gauge-invariant (H L Ebar: -1/2 - 1/2 + 1 = 0).  Weights: k_L + k_Lbar = w_L,
                     k_E + k_Ebar = w_E, k_H + k_L + k_Ebar = w_3 (solvable per copy with one k_H); characters likewise.
  charged mass matrix rows (L_i^-, E_i), columns (Lbar_i^+, Ebar_i):  [[a_i, b_i], [0, d_i]], neutral: a_i, with
                         a_i^2 = M^2 (2 Im tau)^{w_L} |Y_L,i|^2,   d_i^2 = M^2 (2 Im tau)^{w_E} |Y_E,i|^2,
                         b_i^2 = (lambda v)^2 (2 Im tau)^{w_3} |S_hat^T Y3_i(tau)|^2           (exponent = weight).
                     Its singular values depend on |a|, |b|, |d| only (rows/columns rephased), so S's overall phase
                     drops out: S -> e^{i alpha} S is a hypercharge rotation, compensated by rephasing L, Ebar.
  potential          V = sum over every heavy mass eigenvalue m^2 of F(m^2), one shared soft mass m0 and one scale mu:
                         F(u) = (u + m0^2)^2 (log((u + m0^2)/mu^2) - 3/2) - u^2 (log(u/mu^2) - 3/2)
                     (2 complex scalars of mass^2 u + m0^2 and one Dirac fermion of mass^2 u; overall 1/(16 pi^2) dropped).
                     F'' = 2 log(1 + m0^2/u) > 0.  Per copy: F(a^2) [neutral] + F(sigma_+^2) + F(sigma_-^2) [charged].

FORMS (the record's)
  triplets   F_a = eta^(3-a) (eps th2^a, eps th4^a, i th3^a), a = 2 mod 4, eps = i^((a+2)/2)   (B1730; weight 3/2,
             rho_R (x) chi_eta^(2a)); DR = the Serre derivative of R = (-th2^2, -th4^2, i th3^2)/(th2 th3 th4)
             (B1691/B1697; weight 3/2, rho_R untwisted); a0 = D^2 R - E4 R / 48 (B1697; weight 7/2).
  singlets   eta^s E4^p E6^r, weight s/2 + 4p + 6r, character chi_eta^s (W150's eta^12 E4 is s = 12, p = 1).
Only moduli of the singlets and the moduli of the pairings S^T Y3 enter, so eta enters through |eta| = (|th2 th3 th4|/2)^(1/3).
"""
import numpy as np
import mpmath as mp

# ----------------------------------------------------------------------------------------------- the frame's action
LINV = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]], dtype=float)   # rho_R(T) ~ L^-1 (W64; B1730 part A)
LMAT = LINV.T                                                      # its inverse (orthogonal)
PMAT = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=float)    # rho_R(S) ~ P, the i-j swap
NTH = 16                                                           # theta series terms (|q| <= e^{-pi y}; y >= 0.5 ample)


def act_T(tau, S):
    return tau + 1, LINV @ S


def act_S(tau, S):
    return -1 / tau, PMAT @ S


def reduce_to_F(tau, S, maxit=200):
    """(tau, S) -> an equivalent pair with tau in the standard fundamental domain (V is invariant under the joint action)."""
    tau = complex(tau); S = np.array(S, dtype=complex)
    for _ in range(maxit):
        n = int(np.floor(tau.real + 0.5))
        if n != 0:
            tau = tau - n
            S = np.linalg.matrix_power(LMAT if n > 0 else LINV, abs(n)) @ S    # (tau, S) ~ (tau - 1, L S)
        if abs(tau) < 1 - 1e-14:
            tau, S = -1 / tau, PMAT @ S
        else:
            return tau, S
    raise RuntimeError("reduction did not terminate")


# ----------------------------------------------------------------------------------------------- numpy forms
_n = np.arange(1, NTH + 1); _m = np.arange(0, NTH + 1)


def thetas(tau):
    """th2, th3, th4 at a complex scalar tau, and their D = (1/2 pi i) d/dtau and D^2."""
    e3 = np.exp(1j * np.pi * tau * _n ** 2)
    sg = (-1.0) ** _n
    e2 = np.exp(1j * np.pi * tau * (_m + 0.5) ** 2)
    th3 = 1 + 2 * e3.sum(); th4 = 1 + 2 * (sg * e3).sum(); th2 = 2 * e2.sum()
    w3 = _n ** 2 / 2.0; w2 = (_m + 0.5) ** 2 / 2.0
    d3 = 2 * (w3 * e3).sum(); d4 = 2 * (sg * w3 * e3).sum(); d2 = 2 * (w2 * e2).sum()
    dd3 = 2 * (w3 ** 2 * e3).sum(); dd4 = 2 * (sg * w3 ** 2 * e3).sum(); dd2 = 2 * (w2 ** 2 * e2).sum()
    return (th2, th3, th4), (d2, d3, d4), (dd2, dd3, dd4)


def E4E6(th):
    t2, t3, t4 = th
    E4 = (t2 ** 8 + t3 ** 8 + t4 ** 8) / 2
    E6 = (t2 ** 4 + t3 ** 4) * (t3 ** 4 + t4 ** 4) * (t4 ** 4 - t2 ** 4) / 2
    return E4, E6


def abs_eta(th):
    return (abs(th[0] * th[1] * th[2]) / 2) ** (1.0 / 3.0)


class Singlet:
    """eta^s E4^p E6^r, weight s/2 + 4p + 6r, character chi_eta^s."""
    def __init__(self, s, p, r):
        self.s, self.p, self.r = s, p, r
        self.w = s / 2 + 4 * p + 6 * r
        self.name = "eta^%d E4^%d E6^%d" % (s, p, r)

    def absval(self, th, E4, E6, aeta):
        return aeta ** self.s * abs(E4) ** self.p * abs(E6) ** self.r


class Triplet:
    """kind 'F' (B1730's F_a), 'DR' (the Serre derivative of R), 'A0' (a0 = D^2 R - E4 R/48); norm: 'cusp' or 'N'."""
    def __init__(self, kind, a=None, norm="cusp"):
        self.kind, self.a, self.norm = kind, a, norm
        if kind == "F":
            self.w = 1.5; self.name = "F_%d" % a; self.eps = 1j ** (((a + 2) // 2) % 4)
            self.scale = 2.0 ** (-a / 3.0) if norm == "N" else 1.0          # 'N': N(F_a) = i eta^9 (B1730: i 2^a eta^9)
        elif kind == "DR":
            self.w = 1.5; self.name = "DR"; self.scale = 1.0
        elif kind == "A0":
            self.w = 3.5; self.name = "a0"; self.scale = 1.0
        else:
            raise ValueError(kind)

    def vec_noeta(self, th, dth, ddth, E4):
        """the triplet's value divided by its common scalar factor, and |that factor|; value = factor * vec"""
        t2, t3, t4 = th
        if self.kind == "F":
            a = self.a
            v = np.array([self.eps * t2 ** a, self.eps * t4 ** a, 1j * t3 ** a])
            return v, abs_eta(th) ** (3 - a) * self.scale
        V = np.array([-t2 ** 2, -t4 ** 2, 1j * t3 ** 2])
        d2, d3, d4 = dth; dd2, dd3, dd4 = ddth
        DV = np.array([-2 * t2 * d2, -2 * t4 * d4, 2j * t3 * d3])
        E2 = 8 * (d2 / t2 + d3 / t3 + d4 / t4)
        den = abs(t2 * t3 * t4)                                            # |2 eta^3|
        if self.kind == "DR":
            return DV - (E2 / 12) * V, 1.0 / den                           # DR = (DV - E2 V/12)/(2 eta^3)
        # a0 = D^2 R - E4 R/48 with D^2 R = D(DR) - (E2/8) DR (Serre, weight 3/2); DE2 = (E2^2 - E4)/12
        D2V = np.array([-2 * (d2 ** 2 + t2 * dd2), -2 * (d4 ** 2 + t4 * dd4), 2j * (d3 ** 2 + t3 * dd3)])
        DE2 = (E2 ** 2 - E4) / 12
        # with R = V/(2 eta^3) =: V g, Dg = -(E2/8) g; DR = (DV - E2 V/12) g
        num_DR = DV - (E2 / 12) * V
        D_num_DR = D2V - (DE2 / 12) * V - (E2 / 12) * DV
        num_DDR = D_num_DR - (E2 / 8) * num_DR                                # D(DR)/g
        num_D2R = num_DDR - (E2 / 8) * num_DR                                 # (D(DR) - E2/8 DR)/g
        return num_D2R - (E4 / 48) * V, 1.0 / den


def form_values(tau):
    th, dth, ddth = thetas(tau)
    E4, E6 = E4E6(th)
    return th, dth, ddth, E4, E6, abs_eta(th)


# ----------------------------------------------------------------------------------------------- the heavy spectrum
class Copy:
    def __init__(self, YL, YE, Y3):
        self.YL, self.YE, self.Y3 = YL, YE, Y3
        self.name = "(%s | %s | %s)" % (YL.name, YE.name, Y3.name)


def copy_masses(c, tau, S, M=1.0, lv=0.3, fv=None):
    """(a^2, d^2, b^2) of one copy at (tau, unit S)"""
    fv = form_values(tau) if fv is None else fv
    th, dth, ddth, E4, E6, ae = fv
    y2 = 2 * tau.imag
    a2 = M ** 2 * y2 ** c.YL.w * c.YL.absval(th, E4, E6, ae) ** 2
    d2 = M ** 2 * y2 ** c.YE.w * c.YE.absval(th, E4, E6, ae) ** 2
    vec, fac = c.Y3.vec_noeta(th, dth, ddth, E4)
    b2 = lv ** 2 * y2 ** c.Y3.w * fac ** 2 * abs(S @ vec) ** 2
    return a2, d2, b2


def eigs_from(a2, d2, b2):
    """the three heavy squared masses of a copy: neutral a^2, charged sigma_+^2 >= sigma_-^2 of [[a, b], [0, d]]"""
    s = a2 + b2 + d2; p2 = a2 * d2
    disc = (a2 - d2) ** 2 + b2 * (2 * a2 + 2 * d2 + b2)                  # = s^2 - 4 a^2 d^2, manifestly >= 0
    sp = 0.5 * (s + np.sqrt(disc))
    sm = p2 / sp if sp > 0 else 0.0
    return a2, sp, sm


def Ffun(u, mu2, m02):
    if u <= 0:
        return m02 ** 2 * (np.log(m02 / mu2) - 1.5)
    return (u + m02) ** 2 * (np.log((u + m02) / mu2) - 1.5) - u ** 2 * (np.log(u / mu2) - 1.5)


def unit(S):
    S = np.asarray(S, dtype=complex)
    return S / np.linalg.norm(S)


def V_total(copies, tau, S, mu2, m02, M=1.0, lv=0.3, reduce=True):
    if tau.imag <= 0:
        return np.inf
    S = unit(S)
    if reduce:
        tau, S = reduce_to_F(tau, S)
    fv = form_values(tau)
    v = 0.0
    for c in copies:
        for u in eigs_from(*copy_masses(c, tau, S, M, lv, fv)):
            v += Ffun(u, mu2, m02)
    return v


def all_eigs(copies, tau, S, M=1.0, lv=0.3):
    S = unit(S); fv = form_values(tau)
    out = []
    for c in copies:
        out.extend(eigs_from(*copy_masses(c, tau, S, M, lv, fv)))
    return np.array(out)


# ----------------------------------------------------------------------------------------------- mpmath versions
def mp_thetas(tau):
    """theta series summed in tau itself (mpmath's jtheta(2, 0, q) takes the principal q^(1/4), wrong for |Re tau| >= 1);
    D = (1/2 pi i) d/dtau of sum_n e^{i pi n^2 tau} = sum (n^2/2) e^{...}; fast convergence for Im tau >~ 0.5"""
    N = 40
    th2 = d2 = dd2 = mp.mpc(0); th3 = th4 = mp.mpc(1); d3 = d4 = dd3 = dd4 = mp.mpc(0)
    for n in range(1, N + 1):
        e = mp.exp(1j * mp.pi * tau * n * n); w = mp.mpf(n * n) / 2; sg = (-1) ** n
        th3 += 2 * e; th4 += 2 * sg * e
        d3 += 2 * w * e; d4 += 2 * sg * w * e; dd3 += 2 * w * w * e; dd4 += 2 * sg * w * w * e
    for m in range(0, N + 1):
        e = mp.exp(1j * mp.pi * tau * (m + mp.mpf(1) / 2) ** 2); w = (m + mp.mpf(1) / 2) ** 2 / 2
        th2 += 2 * e; d2 += 2 * w * e; dd2 += 2 * w * w * e
    return (th2, th3, th4), (d2, d3, d4), (dd2, dd3, dd4)


def mp_form_values(tau):
    th, dth, ddth = mp_thetas(tau)
    t2, t3, t4 = th
    E4 = (t2 ** 8 + t3 ** 8 + t4 ** 8) / 2
    E6 = (t2 ** 4 + t3 ** 4) * (t3 ** 4 + t4 ** 4) * (t4 ** 4 - t2 ** 4) / 2
    ae = mp.cbrt(abs(t2 * t3 * t4) / 2)
    return th, dth, ddth, E4, E6, ae


def mp_triplet(Y3, fv):
    th, dth, ddth, E4, E6, ae = fv
    t2, t3, t4 = th
    if Y3.kind == "F":
        a = Y3.a; eps = mp.mpc(1j) ** (((a + 2) // 2) % 4)
        sc = mp.power(2, -mp.mpf(a) / 3) if Y3.norm == "N" else mp.mpf(1)
        return [eps * t2 ** a, eps * t4 ** a, 1j * t3 ** a], mp.power(ae, 3 - a) * sc
    V = [-t2 ** 2, -t4 ** 2, 1j * t3 ** 2]
    d2, d3, d4 = dth; dd2, dd3, dd4 = ddth
    DV = [-2 * t2 * d2, -2 * t4 * d4, 2j * t3 * d3]
    E2 = 8 * (d2 / t2 + d3 / t3 + d4 / t4)
    den = abs(t2 * t3 * t4)
    num_DR = [DV[k] - E2 / 12 * V[k] for k in range(3)]
    if Y3.kind == "DR":
        return num_DR, 1 / den
    D2V = [-2 * (d2 ** 2 + t2 * dd2), -2 * (d4 ** 2 + t4 * dd4), 2j * (d3 ** 2 + t3 * dd3)]
    DE2 = (E2 ** 2 - E4) / 12
    D_num_DR = [D2V[k] - DE2 / 12 * V[k] - E2 / 12 * DV[k] for k in range(3)]
    num_DDR = [D_num_DR[k] - E2 / 8 * num_DR[k] for k in range(3)]
    num_D2R = [num_DDR[k] - E2 / 8 * num_DR[k] for k in range(3)]
    return [num_D2R[k] - E4 / 48 * V[k] for k in range(3)], 1 / den


def mp_copy_masses(c, tau, S, M=1, lv=mp.mpf("0.3"), fv=None):
    fv = mp_form_values(tau) if fv is None else fv
    th, dth, ddth, E4, E6, ae = fv
    y2 = 2 * mp.im(tau)
    def sabs(Y):
        return mp.power(ae, Y.s) * mp.power(abs(E4), Y.p) * mp.power(abs(E6), Y.r)
    a2 = M ** 2 * mp.power(y2, mp.mpf(c.YL.w)) * sabs(c.YL) ** 2
    d2 = M ** 2 * mp.power(y2, mp.mpf(c.YE.w)) * sabs(c.YE) ** 2
    vec, fac = mp_triplet(c.Y3, fv)
    b2 = lv ** 2 * mp.power(y2, mp.mpf(c.Y3.w)) * fac ** 2 * abs(sum(S[k] * vec[k] for k in range(3))) ** 2
    return a2, d2, b2


def mp_eigs_from(a2, d2, b2):
    s = a2 + b2 + d2; p2 = a2 * d2
    disc = (a2 - d2) ** 2 + b2 * (2 * a2 + 2 * d2 + b2)                  # = s^2 - 4 a^2 d^2, manifestly >= 0
    sp = (s + mp.sqrt(disc)) / 2
    return a2, sp, (p2 / sp if sp > 0 else mp.mpf(0))


def mp_F(u, mu2, m02):
    if u <= 0:
        return m02 ** 2 * (mp.log(m02 / mu2) - mp.mpf(3) / 2)
    return (u + m02) ** 2 * (mp.log((u + m02) / mu2) - mp.mpf(3) / 2) - u ** 2 * (mp.log(u / mu2) - mp.mpf(3) / 2)


def mp_unit(S):
    n = mp.sqrt(sum(abs(c) ** 2 for c in S))
    return [c / n for c in S]


def mp_V(copies, tau, S, mu2, m02, M=1, lv=mp.mpf("0.3")):
    S = mp_unit(S); fv = mp_form_values(tau); v = mp.mpf(0)
    for c in copies:
        for u in mp_eigs_from(*mp_copy_masses(c, tau, S, M, lv, fv)):
            v += mp_F(u, mu2, m02)
    return v


def mp_all_eigs(copies, tau, S, M=1, lv=mp.mpf("0.3")):
    S = mp_unit(S); fv = mp_form_values(tau); out = []
    for c in copies:
        out.extend(mp_eigs_from(*mp_copy_masses(c, tau, S, M, lv, fv)))
    return out


# ----------------------------------------------------------------------------------------------- local coordinates on H x CP^2
def frame_at(S0):
    """an orthonormal pair (e1, e2) spanning the Hermitian complement of the unit vector S0 (numpy)"""
    S0 = unit(S0)
    M = np.eye(3, dtype=complex) - np.outer(S0, S0.conj())
    U, s, Vh = np.linalg.svd(M)
    return U[:, 0], U[:, 1]


def chart(x6, tau0, S0, e1, e2):
    """6 real local coordinates -> (tau, S): tau = tau0 + x0 + i x1; S = S0 + (x2 + i x3) e1 + (x4 + i x5) e2 (normalised)"""
    tau = tau0 + x6[0] + 1j * x6[1]
    S = S0 + (x6[2] + 1j * x6[3]) * e1 + (x6[4] + 1j * x6[5]) * e2
    return tau, S
