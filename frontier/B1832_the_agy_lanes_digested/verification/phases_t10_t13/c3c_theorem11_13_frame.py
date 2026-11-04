"""agy digest, Theorems 11 and 13 and the audit's finding 10, main's code only (frame_common).  Data-free; theta-bar is not
firewalled (Review 74); nothing is compared with a measured number.
  T11d  the mirror at matrix level, FR-COV on (2/5, 0): Y_s(-conj tau; c -> -conj c, b -> conj b) = P conj(Y_s(tau; c)) P,
        P = diag(1, 1, -1) on [QJ, QI, QK]; at tau_G and two random tau; is the principal b(-conj tau) = conj b(tau)?
  T11e  the same matrix identity for main's FR-FIB (a0 = 0) on a line with b != 0: (alpha, b) at tau vs (alpha, -b) at -conj tau
        (B1790/B1821's mirror, here as a matrix identity), readings S~ and S of F_10
  T11f  arg det(Y_u Y_d) at tau_G on (2/5, 0), F_10, S~, the lane's characters: L = 2.360032 (Theorem 11) and 2.369206
        (the audit function); arg det Y_u, arg det Y_d; main's own L_2 at Im tau = phi^2 (B1667's Re tau = 1/4 column)
  T11g  tau = 2i: |Y_u - P conj(Y_u) P| with the principal b ('the cut jump') and with the lifted scalar
  T13d  the Weinberg operator at tau_G: M_W = sym part of main's coupling on the LL pair (twist-6 norms) and the
        'minimal' variant (twist-3 norms); PMNS invariants from U_e^dag U_nu; m2/m3 of M_W; Haar invariance
  P2b   Phase 2's LL singular values (twist-3 norms, a0 = -b, L = 2.369206)
"""
import cmath, json, math, pathlib
import numpy as np
from frame_common import B, ROOT, norms, matter, higgs, yukawa, phase_ratio, CHARS, TAU_G, P, f10, PHI

OUT = {}
def rec(k, v): OUT[k] = v; print(k, ":", v, flush=True)
SEC = ("up", "down", "lepton")

def frcov(line, tau, s, L, coeff, b_override=None, reading="S~", cache=None):
    R, c = cache[(line, tau, s)] if cache is not None and (line, tau, s) in cache else norms(line, tau, s)
    if cache is not None: cache[(line, tau, s)] = (R, c)
    S, h, b = higgs(tau, coeff, b_override, reading)
    return yukawa(S, matter(R, c, L)), b

cache = {}
L11 = 2.360032127545249
rng = np.random.default_rng(2026110411)
taus = [TAU_G] + [complex(rng.uniform(0.15, 0.55), rng.uniform(1.6, 2.65)) for _ in range(2)]
for tau in taus:
    ta = -tau.conjugate(); res = {}
    for s in SEC:
        Y, b = frcov((0.4, 0.0), tau, s, L11, CHARS[s], cache=cache)
        Ya, _ = frcov((0.4, 0.0), ta, s, L11, -np.conj(CHARS[s]), b_override=np.conj(b), cache=cache)
        Yp, bp = frcov((0.4, 0.0), ta, s, L11, -np.conj(CHARS[s]), cache=cache)
        res[s] = {"|Y(-conj tau) - P conj(Y) P| (lifted b)": float(np.max(np.abs(Ya - P @ np.conj(Y) @ P))),
                  "|det Y(-conj tau) - conj det Y|": float(abs(np.linalg.det(Ya) - np.conj(np.linalg.det(Y)))),
                  "principal b(-conj tau) == conj b(tau)?": bool(abs(bp - np.conj(b)) < 1e-12 * abs(b)),
                  "|Y - P conj Y P| with principal b": float(np.max(np.abs(Yp - P @ np.conj(Y) @ P)))}
    rec("T11d tau %s" % np.round(tau, 6), res)

for reading in ("S~", "S"):
    tau = complex(0.3, 2.1); res = {}
    for s in SEC:
        Y, _ = frcov((0.4, 0.1), tau, s, L11, None, reading=reading)
        Ya, _ = frcov((0.4, -0.1), -tau.conjugate(), s, L11, None, reading=reading)
        Yb, _ = frcov((0.4, 0.1), -tau.conjugate(), s, L11, None, reading=reading)
        res[s] = {"|Y((a,-b), -conj tau) - P conj Y((a,b), tau) P|/|Y|": float(np.max(np.abs(Ya - P @ np.conj(Y) @ P)) / np.max(np.abs(Y))),
                  "control: same line (a, b) at -conj tau": float(np.max(np.abs(Yb - P @ np.conj(Y) @ P)) / np.max(np.abs(Y)))}
    rec("T11e FR-FIB, F_10 reading %s, line (2/5, 1/10), tau 0.3+2.1i" % reading, res)

col = sorted((p["tau"][1], p["L_max"], p["L_2"]) for p in json.loads((ROOT / "frontier/B1667_the_canonical_cusp/verification/the_canonical_cusp.json").read_text())["points"] if abs(p["tau"][0] - 0.25) < 1e-9)
L2_main = float(np.interp(PHI ** 2, [c[0] for c in col], [c[2] for c in col]))
rec("T11f main's L_2 at Im tau = phi^2 (B1667 column Re tau = 1/4, as cm_zero_line.radii)", L2_main)
for L in (L11, 2.369205660785321, L2_main):
    Yu, _ = frcov((0.4, 0.0), TAU_G, "up", L, CHARS["up"], cache=cache)
    Yd, _ = frcov((0.4, 0.0), TAU_G, "down", L, CHARS["down"], cache=cache)
    du, dd = np.linalg.det(Yu), np.linalg.det(Yd)
    rec("T11f L = %.6f: arg det Y_u, arg det Y_d, arg det(Y_u Y_d) (rad)" % L,
        [round(float(np.angle(du)), 6), round(float(np.angle(dd)), 6), round(float(np.angle(du * dd)), 6)])
    Yu0, _ = frcov((0.4, 0.0), TAU_G, "up", L, None, cache=cache); Yd0, _ = frcov((0.4, 0.0), TAU_G, "down", L, None, cache=cache)
    rec("T11f   control, FR-FIB (a0 = 0) same point: arg det(Y_u Y_d)", round(float(np.angle(np.linalg.det(Yu0) * np.linalg.det(Yd0))), 6))

t2i = complex(0, 2.0)
Yu, b = frcov((0.4, 0.0), t2i, "up", 2.36, CHARS["up"], cache=cache)
Yl, _ = frcov((0.4, 0.0), t2i, "up", 2.36, -np.conj(CHARS["up"]), b_override=np.conj(b), cache=cache)
rec("T11g tau = 2i: principal b, |F| = |b|^2", [complex(np.round(b, 8)), float(abs(b) ** 2)])
rec("T11g |Y_u - P conj(Y_u) P| (principal, same scalar)", float(np.max(np.abs(Yu - P @ np.conj(Yu) @ P))))
rec("T11g |Y_u(lifted, -conj c) - P conj(Y_u) P|", float(np.max(np.abs(Yl - P @ np.conj(Yu) @ P))))

# T13d
R_ll, c6 = norms((0.4, 0.0), TAU_G, "LL"); _, c3 = norms((0.4, 0.0), TAU_G, "down")
Ye, _ = frcov((0.4, 0.0), TAU_G, "lepton", L11, CHARS["lepton"], cache=cache)
S0, h, _ = higgs(TAU_G, None)
def MW(c):
    Y = yukawa(S0, matter(R_ll, c, L11)); return 0.5 * (Y + Y.T), Y
def inv(Ye, Mw):
    ue, se, _ = np.linalg.svd(Ye); ue = ue[:, np.argsort(se)]
    un, sn, _ = np.linalg.svd(Mw); un = un[:, np.argsort(sn)]
    U = ue.conj().T @ un; a = np.abs(U); s13 = a[0, 2]; c13 = math.sqrt(1 - s13 ** 2)
    J = float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))
    return np.array([(a[0, 1] / c13) ** 2, (a[1, 2] / c13) ** 2, s13 ** 2, abs(J)])
for name, c in (("twist-6 (LL norms)", c6), ("twist-3 proxy (the 'minimal')", c3)):
    Mw, Yfull = MW(c)
    sn = np.sort(np.linalg.svd(Mw, compute_uv=False))
    rec("T13d %s: |Y - Y^T| (B1799: symmetric)" % name, float(np.max(np.abs(Yfull - Yfull.T))))
    rec("T13d %s: (s12^2, s23^2, s13^2, |J|), m2/m3 of M_W" % name, [[round(float(v), 6) for v in inv(Ye, Mw)], round(float(sn[1] / sn[2]), 6)])
    worst = 0.0; base = inv(Ye, Mw)
    for _ in range(10):
        def ru():
            z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2); q, r = np.linalg.qr(z); d = np.diag(r); return q * (d / abs(d))
        UL, WR = ru(), ru()
        worst = max(worst, float(np.max(np.abs(inv(UL @ Ye @ WR.conj().T, UL @ Mw @ UL.T) - base))))
    rec("T13d %s: Haar invariance, max deviation over 10 trials" % name, worst)

# P2b
L2i = 2.369205660785321
Sll, _, _ = higgs(TAU_G, -1.0)
Yll = yukawa(Sll, matter(R_ll, c3, L2i))
rec("P2b Phase 2's LL singular values (twist-3 norms, a0 = -b, L = 2.369206)", [round(float(v), 5) for v in np.sort(np.linalg.svd(Yll, compute_uv=False))])
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(OUT, indent=1, default=str))
