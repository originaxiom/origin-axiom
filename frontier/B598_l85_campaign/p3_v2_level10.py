"""B598 P3 — V2, LEVEL-INDEPENDENCE AT kappa = 10 (sealed prereg cell 2 of
3; runs ONLY after V1's output is committed).

Per STEP8_P3_PREREG.md: the hearing law at the NEXT golden multiple
kappa = 10 (SU(3) level k = 7, q = e^{i pi/10}; kappa = k + 3), same weld
g = RL, same construction as B593 (whose kappa = 5 numbers are reproduced
first as a machinery GATE — they are banked, so that is a gate, not a
comparison).

REQUIRED (V2 PASS): at kappa = 10,
  (a) the two theta-odd directions' hearing coefficients form a CONJUGATE
      PAIR (u6' = conj(u3') to 1e-9);
  (b) both have Im != 0 (|Im| > 1e-6);
  (c) the Im-sign of the u3-analog ((1,0)-(0,1))/sqrt2 equals the kappa=5
      sign (+, from the banked 1/(2phi) + i sin(2pi/5)/sqrt5).
Also verified en route (law gates): no O(eps) term; the eps^2 coefficient
equals the quadratic form (the hearing law itself, both levels).

Run: python3 p3_v2_level10.py   (~1 min)
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")


def hearing_coeffs(level):
    """The two theta-odd diagonal hearing coefficients u' M_odd u at the
    weld RL, via the B593 construction (state-independent; the law gates
    verified with the vacuum baseline)."""
    w, S, T, cc = b238.su3_data(level)
    n = len(w)
    conj_idx = [w.index((wt[1], wt[0])) for wt in w]
    Cm = np.zeros((n, n))
    for i, wt in enumerate(w):
        Cm[w.index((wt[1], wt[0])), i] = 1.0
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    R, L = T, Si @ Ti @ S
    WRL = R @ L
    pairs = [(w.index((1, 0)), w.index((0, 1))),
             (w.index((2, 0)), w.index((0, 2)))]
    U = np.zeros((n, 2))
    for j, (a, b) in enumerate(pairs):
        U[a, j], U[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)

    # the law gates with a C-symmetric baseline (the vacuum): no O(eps);
    # the eps^2 coefficient = the quadratic form
    psi0 = np.zeros(n, dtype=complex)
    psi0[w.index((0, 0))] = 1.0

    def amplitude(psi, twisted):
        Wm = (Cm @ WRL) if twisted else WRL
        vec = Wm @ psi
        return sum(np.conj(psi[conj_idx[i]]) * vec[i] for i in range(n))

    coeffs = []
    for j in (0, 1):
        u = U[:, j].astype(complex)
        # verify Cu = -u (theta-odd)
        assert np.allclose(Cm @ u, -u), "u not theta-odd"
        quad_t = np.conj(u) @ (Cm @ WRL) @ u
        quad_u = np.conj(u) @ WRL @ u
        coeff = (quad_t - quad_u) / 2          # u' M_odd u
        # law gates at two eps values
        for eps in (0.05, 0.2):
            psi_e = psi0 + eps * u
            At = amplitude(psi_e, True)
            Au = amplitude(psi_e, False)
            A0t = amplitude(psi0, True)
            A0u = amplitude(psi0, False)
            # no O(eps): the difference of differences is exactly quadratic
            dd = (At - Au) - (A0t - A0u)
            assert abs(dd - (-2 * eps ** 2 * coeff)) < 1e-9, \
                f"law gate failed at level {level}, eps {eps}: {dd} vs " \
                f"{-2 * eps**2 * coeff}"
        coeffs.append(coeff)
    return coeffs


# ---- machinery gate: reproduce the banked kappa = 5 numbers ----------------
c5 = hearing_coeffs(2)
phi = (1 + math.sqrt(5)) / 2
banked = 1 / (2 * phi) + 1j * math.sin(2 * math.pi / 5) / math.sqrt(5)
g5 = abs(c5[0] - banked) < 1e-9 and abs(c5[1] - banked.conjugate()) < 1e-9
print(f"kappa=5 gate: u3 = {c5[0]:+.9f} (banked {banked:+.9f}): {g5}",
      flush=True)
assert g5, "kappa=5 machinery gate failed"

# ---- THE BLIND CELL: kappa = 10 (level 7) ----------------------------------
c10 = hearing_coeffs(7)
a_pair = abs(c10[1] - c10[0].conjugate()) < 1e-9
b_im = abs(c10[0].imag) > 1e-6 and abs(c10[1].imag) > 1e-6
c_sign = (c10[0].imag > 0) == (c5[0].imag > 0)
print(f"kappa=10: u3' = {c10[0]:+.9f}", flush=True)
print(f"kappa=10: u6' = {c10[1]:+.9f}", flush=True)
print(f"(a) conjugate pair: {a_pair}", flush=True)
print(f"(b) Im != 0 both:   {b_im}", flush=True)
print(f"(c) Im-sign of the u3-analog stable (+): {c_sign}", flush=True)
verdict = a_pair and b_im and c_sign
print(f"\nV2 VERDICT (level-independence): "
      f"{'PASS' if verdict else 'FAIL'}", flush=True)
print("banked blind; V3 runs only after this output is committed.", flush=True)
