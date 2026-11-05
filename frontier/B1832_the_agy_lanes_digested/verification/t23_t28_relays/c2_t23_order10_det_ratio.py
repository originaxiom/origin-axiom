"""c2: Theorem 23 step 2 (toe_closure.py:4517-4527, 4540-4578 @ 18c607040) on MAIN's coupling with a scalar component
S = a0*I2 + s_I QI + s_J QJ + s_K QK (main's b1656_funcs.coupling is linear in S; c6 checks the 4D formula).

The lane: on the five order-10 lines (2/5, (2j+1)/10) the lepton channels are the down channels times one factor up to signs,
so |det Y_e / det Y_d| = 1 with a Higgs whose QI component is projected out (h_proj, l. 4537), while on the five order-5
lines (2/5, 2j/10) the identity channel flips sign and a0 != 0 breaks |det Y_e/det Y_d| = 1 (by > 0.16 at its point).
Main's S297 (P-355's first item): lepton = down spectra for every Higgs exactly on the d = e points (order 5 transposed) and,
for a QI-free Higgs, on their beta-half-lifts (orders 8, 10) -- both in the a0 = 0 frame.

Printed: per-channel ratios R_lep/R_down (sector-blind c_s, B1826, so u_lep/u_down = R_lep/R_down channel by channel) and
|det Y_lep/det Y_down| - 1 for four Higgs classes. Only determinant ratios are printed (no singular values)."""
import math, pathlib, sys
from fractions import Fraction as F
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier" / "B1821_the_frames_mirror_symmetry_in_re_tau" / "verification"))
import cm_zero_line as Z
B = Z.mods()["B"]; keys = list(B.UNITS)
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
I2 = np.eye(2, dtype=complex)
L = 2.3577376878276057   # the lane's l2_val (any L: the identities are channel-wise)
rng = np.random.default_rng(23)

def u_of(line, tau, ql, qr):
    w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)
    R = B.residues(x, yy, tau); c = B.cA(x, yy, tau, R)
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0j) for k in keys}
    return R, u

phi = (1 + math.sqrt(5)) / 2
for tau in (complex(1 / math.sqrt(5), phi * phi), complex(0.3, 2.1)):
    a = np.array(Z.direction("F_10", tau))           # main's F_10 section, coefficients of (QI, QJ, QK)
    hh = a @ a; b10 = np.sqrt(hh)
    rs = rng.normal(size=4) + 1j * rng.normal(size=4)
    higgs = {
        "a0=0, F_10 (FR-FIB)": (0j, a),
        "a0=sqrt(h.h), F_10 QI-free": (b10, np.array([0, a[1], a[2]])),
        "a0=sqrt(h.h), F_10 full": (b10, a),
        "random a0, random h, QI-free": (rs[0], np.array([0, rs[2], rs[3]])),
        "random a0, random h (QI on)": (rs[0], rs[1:]),
    }
    say("tau = %s" % tau)
    for kind, js in (("order-10 (2/5,(2j+1)/10)", [F(2 * j + 1, 10) for j in range(5)]), ("order-5  (2/5,2j/10)", [F(2 * j, 10) for j in range(5)])):
        dev = {k: 0.0 for k in higgs}; ratios = []
        for b in js:
            line = (F(2, 5), b)
            Rd, ud = u_of(line, tau, 1, 2); Re_, ue = u_of(line, tau, -3, 6)
            ratios.append({k: (complex(Re_[k] / Rd[k]) if abs(Rd[k]) > 1e-14 else None) for k in keys})
            for hk, (a0, h) in higgs.items():
                S = a0 * I2 + h[0] * B.QI + h[1] * B.QJ + h[2] * B.QK
                dd = np.linalg.det(B.coupling(S, B.weighted_M(ud))); de = np.linalg.det(B.coupling(S, B.weighted_M(ue)))
                dev[hk] = max(dev[hk], abs(abs(de / dd) - 1))
        say("  %s: R_lep/R_down per channel, line by line:" % kind)
        for b, r in zip(js, ratios):
            say("     beta=%-5s %s" % (b, {k: (None if v is None else "%+.6f%+.6fi" % (v.real, v.imag)) for k, v in r.items()}))
        for hk in higgs:
            say("     max_j | |det Y_lep/det Y_down| - 1 | with %-30s = %.2e" % (hk, dev[hk]))

pathlib.Path(__file__).with_name("c2_t23_order10_det_ratio_out.txt").write_text("\n".join(out) + "\n")
