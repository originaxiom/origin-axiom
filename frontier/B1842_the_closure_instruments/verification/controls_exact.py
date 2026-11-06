"""P-688 controls of the frozen-row instrument at the exact end (data-free; deviations and pass bits only, no PMNS value on
a slope-2/5 line, no cross-sector ratio):
 C-ID   ratios_of(Y) equals the web seat's ratios() at the same norms (the construction is the instrument's).
 C-M    planted: M_nu ∝ M_e where the line's order divides 6; M_nu ∝ M_u and M_e ∝ M_d where it divides 4 (B1835 § 1b),
        at the exact end, delta = 0.3 and delta = inf; order-5 lines must break them.
 C-PS   |U_PMNS| = |V_CKM^dagger| on order-4 lines (with nu read like up), at the exact end.
 C-T    the T-law (Review 76, R76-3, corrected 2026-11-06): the theta machinery run at the UNREDUCED tau + 1 with line
        (a, b - a) gives the same singular values as at (tau, (a, b)), delta = inf (t_law.py). The first version compared
        two calls that reduce to identical inputs -- a tautology -- and claimed equality 'up to phases'; that is false:
        |Y| entrywise differs by about 8 %, T acting on the generations by a non-diagonal unitary.
 C-MIR  Y((a, -b), -conj tau) = P conj(Y) P with P = diag(1, 1, -1) (T-FRAME-MIRROR) at the exact end, on lines off 2/5.
Run: python3 -B controls_exact.py"""
import sys, math, pathlib
from fractions import Fraction as F
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import exact_card_instrument as X


def order(a, b): return math.lcm(F(a).denominator, F(b).denominator)
def prop(A, B):
    c = np.vdot(B.ravel(), A.ravel()) / np.vdot(B.ravel(), B.ravel()); return float(np.max(np.abs(A - c * B)) / np.max(np.abs(A)))
def left(Ym): return np.linalg.svd(Ym)[0][:, ::-1]


def main():
    M = X.mods(); ee, B = M["ee"], M["B"]
    # C-ID
    Y, info = X.yukawas_exact(0.31, 2.9, F(1, 3), F(1, 2), 0.3, ("down",))
    tau = complex(*info["tau_reduced"]); a, b = F(info["line_reduced"][0]), F(info["line_reduced"][1])
    c, _ = X.accessory(tau); G = ee.geometry(tau, c); rd = ee.higgs(tau); w = float(a) * tau + float(b)
    x, yy = B.sector_twists(w, tau, 1, 2); R = B.residues(x, yy, tau)
    N, _ = ee.twisted_norms(tau, G["al"], G["be"], G["L_max"] + 0.3, x, yy, R, nth=X.NTH, ns=X.NS)
    ref = ee.ratios(rd, R, N); dev = max(abs(p / q - 1) for rn in ("S", "St") for p, q in zip(X.ratios_of(Y["down"][rn]), ref[rn]))
    print("C-ID: max rel dev %.1e -> %s" % (dev, "HOLDS" if dev < 1e-12 else "FAILS"), flush=True)
    # C-M, C-PS
    lines = sorted({(F(p, n), F(q, n)) for n in (2, 3, 4, 5, 6) for p in range(n) for q in range(n) if (p, q) != (0, 0)})
    lines = [l for l in lines if order(*l) in (2, 3, 4, 5, 6)]
    res = {}
    for delta in (0.3, math.inf):
        for (re_t, im_t) in ((0.31, 2.9), (0.12, 3.2)):
            for (a, b) in lines:
                n = order(a, b); Y, _ = X.yukawas_exact(re_t, im_t, a, b, delta)
                r1 = prop(Y["nu"]["St"], Y["lep"]["St"]); r2 = max(prop(Y["nu"]["St"], Y["up"]["St"]), prop(Y["lep"]["S"], Y["down"]["S"]))
                e = res.setdefault((str(delta), n), [0.0, 0.0, 0.0, 9.0, 9.0, 0])
                if 6 % n == 0: e[0] = max(e[0], r1)
                else: e[3] = min(e[3], r1)
                if 4 % n == 0:
                    e[1] = max(e[1], r2)
                    V = left(Y["up"]["St"]).conj().T @ left(Y["down"]["S"]); P = left(Y["lep"]["S"]).conj().T @ left(Y["nu"]["St"])
                    e[2] = max(e[2], float(np.max(np.abs(np.abs(P) - np.abs(V.conj().T)))))
                else: e[4] = min(e[4], r2)
                e[5] += 1
    ok = True
    for (d, n), e in sorted(res.items()):
        h1 = e[0] < 1e-10 if 6 % n == 0 else e[3] > 1e-3; h2 = e[1] < 1e-10 if 4 % n == 0 else e[4] > 1e-3; h3 = (e[2] < 1e-10) if 4 % n == 0 else True
        ok &= h1 and h2 and h3
        print("C-M/C-PS delta %s order %d (%d line-points): (1) %s (2) %s (3) %s" % (d, n, e[5],
              ("holds %.1e" % e[0]) if 6 % n == 0 else ("breaks %.2f" % e[3]), ("holds %.1e" % e[1]) if 4 % n == 0 else ("breaks %.2f" % e[4]),
              ("holds %.1e" % e[2]) if 4 % n == 0 else "n/a"), flush=True)
    print("C-M/C-PS -> %s" % ("HOLD" if ok else "FAIL"), flush=True)
    # C-T (corrected at Review 76): the genuine T-law, spectra only; the old block compared identical inputs
    import t_law as TL
    sv, ent, taut = TL.t_law()
    print("C-T: singular values %.1e -> %s (|Y| entrywise %.1e: a unitary, not phases; the old tautology %.1e)" % (
          sv, "HOLDS" if sv < 1e-10 else "FAILS", ent, taut), flush=True)
    # C-MIR, off the 2/5 class
    Pm = np.diag([1, 1, -1]); worst = 0.0
    for (re_t, im_t, a, b) in ((0.27, 2.95, F(1, 3), F(1, 7)), (0.13, 3.05, F(1, 4), F(2, 9))):
        Y1, _ = X.yukawas_exact(re_t, im_t, a, b, 0.3); Y2, _ = X.yukawas_exact(-re_t, im_t, a, (-b) % 1, 0.3)
        for sec in X.CHARGES:
            for rn in ("S", "St"):
                A = Y2[sec][rn]; Bm = Pm @ np.conj(Y1[sec][rn]) @ Pm
                worst = max(worst, float(np.max(np.abs(np.abs(A) - np.abs(Bm)))) / float(np.max(np.abs(A))))
    print("C-MIR (moduli): max rel dev %.1e -> %s" % (worst, "HOLDS" if worst < 1e-10 else "FAILS"), flush=True)
    print("controls_exact exit 0")


if __name__ == "__main__":
    main()
