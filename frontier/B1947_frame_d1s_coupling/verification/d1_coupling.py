"""Frame D1's coupling (main, 2026-11-15; P-861; data-free). Frame C with one change: the Higgs carries its charge as a twist,
as matter does (the web seat's W-B1, frame D1), entering as the third factor of a charge-conserving overlap (the triple
overlap of magnetized tori, hep-th/0404229): B1691's triplet R = (-th2/(th3 th4), -th4/(th2 th3), i th3/(th2 th4)) built from
theta constants with characteristics shifted by twist_of(q_H w) = (q_H a, 2 q_H b), q_H = -(q_L + q_R) in 6Y (up +3, down
-3, leptons -3), and its Serre derivative D R = q dR/dq + (1/24) E2 R (weight -1/2 to 3/2), S_D1 = sum_k (D R)_k Q_k.
There is no reading S or S-tilde to choose: each sector's coupling uses its own S_D1.
Modes:
  --control   C0: with q_H = 0, S_D1's components equal frame C's q-series (te.ev of B1691's B[1]) at three moduli;
              C1: S_D1 at +q_H and -q_H coincide (theta constants are even under negating both characteristics).
  --run       the outputs, only after the card (CARD.md) is committed: at the 24 points of order 5, heights 6 and 30, the
              mixing |U_u^H U_d| (diagonal and off-diagonal extremes) and the mass ratios, written to d1_outputs.json."""
import sys, json, pathlib
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL, cusp_mixing as CM
FM = DL.FM; mp = DL.mp; B = FM.B; te = FM.te; H = FM.H; f2m = FM.f2m
QH = {"up": 3, "down": -3, "lep": -3}
V2 = "--v2" in sys.argv          # Amendment A1 (CARD.md): D1', the Higgs twisted by (q_H a, q_H b)
assert all(B.SIXY[B.SECTORS[s][0]] + B.SIXY[B.SECTORS[s][1]] + QH[s] == 0 for s in QH)       # charge conservation


def E2(t):
    q = mp.exp(2j * mp.pi * t); s = 0; n = 1
    while True:
        term = n * q ** n / (1 - q ** n); s += term; n += 1
        if abs(term) < mp.mpf(10) ** (-mp.mp.dps - 5): break
    return 1 - 24 * s


def R_tw(t, ta, tb, rep="+"):
    """rep: theta_4's representative, theta[ta, +1/2 + tb] (declared, frame C's matter convention) or theta[ta, -1/2 + tb]"""
    th = lambda a, b: B.thc_mp(f2m(a), f2m(b), 0, t)
    t2, t3, t4 = th(H + ta, tb), th(ta, tb), th(ta, (H if rep == "+" else -H) + tb)
    return [-t2 / (t3 * t4), -t4 / (t2 * t3), 1j * t3 / (t2 * t4)]


def S_comps(t, qH, a, b, rep="+"):
    """the components of S_D1 = sum_k (D R)_k Q_k at tau = t, twisted by twist_of(qH w), w = (a, b)"""
    ta, tb = (qH * a, qH * b) if V2 else (qH * a, 2 * qH * b)       # A1: D1' carries matter's residue convention (q a, q b)
    R = R_tw(t, ta, tb, rep); e2 = E2(t)
    dR = [mp.diff(lambda z, k=k: R_tw(z, ta, tb, rep)[k], t) / (2j * mp.pi) for k in range(3)]
    return [dR[k] + e2 * R[k] / 24 for k in range(3)]


def parts_d1(tx, ty, a, b, sec, rep="+", qh=None):
    """frame C's coupling at (tau, w) for one sector, with S replaced by S_D1(q_H of the sector)"""
    mp.mp.dps = int(40 + 3.5 * float(ty))
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    t = mp.mpc(mp.mpf(tx), mp.mpf(ty))
    c3 = S_comps(t, QH[sec] if qh is None else qh, a, b, rep); S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    _, Mw, _, u, cs, ds = DL.parts(tx, float(ty), a, b, sec)          # the matter side, unchanged (its precision reset below)
    mp.mp.dps = int(40 + 3.5 * float(ty))
    return mp.matrix([[sum(((Ca.T * EPS * S * Cb)[m, n] * Mw[m, n] for m in range(2) for n in range(2)), mp.mpc(0))
                       for Cb in BLOCKS] for Ca in BLOCKS])


def outputs(tx, ty, a, b, rep="+", qh=None):
    """the up and down ratios and |V| at one point"""
    Yu, Yd = parts_d1(tx, ty, a, b, "up", rep, qh), parts_d1(tx, ty, a, b, "down", rep, qh)
    sv = lambda Y: sorted((abs(v) for v in mp.svd_c(Y, compute_uv=False)), reverse=True)
    su, sd = sv(Yu), sv(Yd); Vm = CM.U_of(Yu).H * CM.U_of(Yd)
    return [float(su[1] / su[0]), float(su[2] / su[0]), float(sd[1] / sd[0]), float(sd[2] / sd[0])] + [float(abs(Vm[r, c])) for r in range(3) for c in range(3)]


def c2(qh=None):
    """C2: covariance under tau -> tau + 1, w = (a, b) -> (a, b - a) (frame C's own map, B1724), for each representative;
    returns {rep: worst relative difference} over three bulk moduli and four points"""
    worst = {}
    for rep in ("+", "-"):
        w = 0
        for tx, tx1, ty in (("0.13", "1.13", "1.7"), ("-0.31", "0.69", "2.9"), ("0.4", "1.4", "1.2")):
            for a, b in ((Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5)), (Fr(0), Fr(3, 5)), (Fr(3, 5), Fr(1, 5))):
                o0 = outputs(tx, ty, a, b, rep, qh); o1 = outputs(tx1, ty, a, (b - a) % 1, rep, qh)
                w = max(w, max(abs(x - y) / max(abs(x), 1e-30) for x, y in zip(o0[:4], o1[:4])), max(abs(x - y) for x, y in zip(o0[4:], o1[4:])))
        worst[rep] = w
    return worst


def choose(worst, tol=1e-12):
    ok = [r for r in ("+", "-") if worst[r] < tol]
    return None if not ok else ("+" if "+" in ok else ok[0])


def control():
    mp.mp.dps = 40; worst0 = 0; worst1 = 0
    for tx, ty in (("0.13", "1.7"), ("-0.31", "2.9"), ("0.4", "6.0")):
        t = mp.mpc(mp.mpf(tx), mp.mpf(ty))
        rec = [te.ev(cc, t) for cc in te.B[1]]; mine = S_comps(t, 0, Fr(0), Fr(0))
        worst0 = max(worst0, max(abs(x - y) / abs(y) for x, y in zip(mine, rec)))
        for a, b in ((Fr(1, 5), Fr(2, 5)), (Fr(2, 5), Fr(4, 5))):
            p, m = S_comps(t, 3, a, b), S_comps(t, -3, a, b)
            worst1 = max(worst1, max(abs(x - y) / abs(x) for x, y in zip(p, m)))
    print("C0: q_H = 0 against frame C's q-series, worst relative difference %.1e" % worst0)
    print("C1: q_H = +3 against -3 at two points of order 5, worst relative difference %.1e" % worst1)
    h = c2(qh=0)
    print("C2's harness with q_H = 0 (frame C's Higgs; must be covariant for both representatives): %s" % {r: "%.1e" % v for r, v in h.items()})
    return worst0, worst1, h


if __name__ == "__main__":
    if "--control" in sys.argv:
        control()
    elif "--run" in sys.argv:
        card = pathlib.Path(__file__).resolve().parents[1] / "CARD.md"
        import subprocess
        assert subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%h", "--", str(card)], capture_output=True, text=True).stdout.strip(), "the card must be committed before the run"
        w2 = c2(); rep = choose(w2)
        print("C2: covariance of frame D1 under tau -> tau + 1, worst difference by representative %s; chosen: %s" % ({r: "%.1e" % v for r, v in w2.items()}, rep), flush=True)
        out = {"C2": w2, "representative": rep}
        if rep is None:
            (pathlib.Path(__file__).resolve().parent / ("d1v2_outputs.json" if V2 else "d1_outputs.json")).write_text(json.dumps(out, indent=1))
            raise SystemExit("C2 fails for both representatives: D1 is undefined in this form (the card's rule)")
        for y in ("6.0", "30.0"):
            rows = []
            for i in range(5):
                for j in range(5):
                    if (i, j) == (0, 0): continue
                    a, b = Fr(i, 5), Fr(j, 5)
                    Yu, Yd = parts_d1("0.13", y, a, b, "up", rep), parts_d1("0.13", y, a, b, "down", rep)
                    Vm = CM.U_of(Yu).H * CM.U_of(Yd)
                    A = [[float(abs(Vm[r, c])) for c in range(3)] for r in range(3)]
                    sv = lambda Y: sorted((float(abs(v)) for v in mp.svd_c(Y, compute_uv=False)), reverse=True)
                    su, sd = sv(Yu), sv(Yd)
                    rows.append({"point": [str(a), str(b)], "V": A, "up": [su[1] / su[0], su[2] / su[0]], "down": [sd[1] / sd[0], sd[2] / sd[0]]})
            out[y] = rows
            print("height %s: smallest diagonal |V| %.3e, largest off-diagonal %.3e" % (y, min(min(r["V"][k][k] for k in range(3)) for r in rows), max(max(r["V"][p][q] for p in range(3) for q in range(3) if p != q) for r in rows)), flush=True)
        (pathlib.Path(__file__).resolve().parent / ("d1v2_outputs.json" if V2 else "d1_outputs.json")).write_text(json.dumps(out, indent=1))
