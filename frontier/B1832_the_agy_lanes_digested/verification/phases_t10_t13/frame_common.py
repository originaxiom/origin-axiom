"""agy digest: main's own FR-FIB machinery (B1656's functions, b1656_funcs.py on main via B1691's correction folder,
the module that frontier/B1821_*/verification/cm_zero_line.py's mods()['B'] loads) with the agy lane's FR-COV scalar added
as a0 * I in the Higgs quaternion.  Nothing is imported from the agy lane; the lane's FR-COV recipe is re-typed from its
source (toe_closure.py / sm_19_gate.py at 18c607040) only to say WHAT is built:

  Higgs direction F_10 (main's cm_zero_line.direction): v = (-th2^10, -th4^10, i th3^10) on (QI, QJ, QK)
  the lane's reading S~ (h = conj v) and scalar a0 = c_s * conj(sqrt(v.v)) (principal sqrt), so
        S = a0 I + conj(v_I) QI + conj(v_J) QJ + conj(v_K) QK
  matter u_k = sqrt(2 pi L + c_k) R_k (main's rows_at), Y = coupling(S, weighted_M(u)) (main's)
  characters c_u = -sqrt(e^{i pi} - 1), c_d = -sqrt(e^{i pi/4} - 1), c_e = -1 (B1826 section 2's list)
Data-free.  Main's census evaluator is not changed."""
import cmath, math, pathlib, sys
import numpy as np
import mpmath as mp

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents if (p / "frontier").is_dir() and (p / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1691_the_exponents_at_the_two_fixed_points" / "verification" / "correction"))
import b1656_funcs as B  # noqa: E402

mp.mp.dps = 30
SECT = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6), "LL": (-3, -3)}
CHARS = {"up": complex(-cmath.sqrt(cmath.exp(1j * math.pi) - 1)), "down": complex(-cmath.sqrt(cmath.exp(1j * math.pi / 4) - 1)),
         "lepton": -1.0 + 0j}
PHI = (1 + 5 ** 0.5) / 2
TAU_G = complex(1 / 5 ** 0.5, PHI ** 2)
P = np.diag([1.0, 1.0, -1.0])


def f10(tau):
    q = mp.exp(1j * mp.pi * mp.mpc(tau.real, tau.imag))
    t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
    return np.array([complex(-t2 ** 10), complex(-t4 ** 10), complex(1j * t3 ** 10)])   # on (QI, QJ, QK)


def norms(line, tau, sector):
    ql, qr = SECT[sector]
    w = B.line_w(line[0], line[1], tau); x, y = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, y, tau); c = B.cA(x, y, tau, R)
    return R, c


def matter(R, c, L):
    return {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0j) for k in B.UNITS}


def higgs(tau, a0_coeff=None, b_override=None, reading="S~"):
    """S~ reading of F_10 with the scalar a0 = a0_coeff * conj(sqrt(v.v)) (a0_coeff None: FR-FIB, a0 = 0)."""
    v = f10(tau)
    if reading == "S~":
        h = np.conj(v); b = np.conj(np.sqrt(np.dot(v, v)))
    else:
        h = v; b = np.sqrt(np.dot(v, v))
    if b_override is not None: b = b_override
    a0 = 0j if a0_coeff is None else a0_coeff * b
    return a0 * np.eye(2) + h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK, h, b


def yukawa(S, u):
    return B.coupling(S, B.weighted_M(u))


def lane_formula(a0, h_JIK, m1, m_JIK):
    """the lane's closed form (operator_gate.quaternionic_4d_yukawa docstring), re-typed: rows/cols on [QJ, QI, QK]"""
    h = np.asarray(h_JIK, complex); m = np.asarray(m_JIK, complex)
    def sk(v): return np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]], complex)
    return np.outer(h, m) + np.outer(m, h) - np.dot(h, m) * np.eye(3) - m1 * sk(h) + a0 * (m1 * np.eye(3) - sk(m))


def phase_ratio(A, Bm):
    """the best common phase lambda with A ~ lambda Bm, and the residual max|A - lambda Bm| / max|A|"""
    lam = np.vdot(Bm.ravel(), A.ravel()) / np.vdot(Bm.ravel(), Bm.ravel())
    return lam, float(np.max(np.abs(A - lam * Bm)) / max(np.max(np.abs(A)), 1e-300))
