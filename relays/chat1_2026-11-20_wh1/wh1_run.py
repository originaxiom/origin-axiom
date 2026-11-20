#!/usr/bin/env python3
"""W-H1: holomorphy and the shared reading (card relays/cards/CHAT1_W-H1_holomorphy_and_the_shared_reading.md, committed
before this script). Data-free: nothing is compared and no target is opened.

    python3 -I -u wh1_run.py <a checkout of main>

It uses main's B1940 frame_mp (imported, not changed) through W-D2's script, whose per-sector steps it splits into the
channels' residues R_s(tau) and real norms n_s. The Cauchy-Riemann residual of f is
rho = max|d f/d taubar| / max|d f/d tau| over f's entries, from central differences in x and y with step 10^(-20) at 60
digits.

  H0  the frame's Higgs coefficients c_i(tau)
  H1  every channel's residue R_s(tau) that is not zero, in the up, down and lepton sectors
  H2  every channel's unnormalised coupling R_s(tau) (C_a^T eps H C_b o E_s), with H = S and with H = S~
  H3  |S~(tau) - S(-taubar)| / |S(tau)| (1-norms)
  H4  each sector's normalised coupling sum_s n_s R_s (C_a^T eps S C_b o E_s). The canonical end L is held at its value
      at the base tau, since B1927's table is read in double precision and cannot be differenced at this step. The
      card did not say this; it is disclosed here and in the relay.
"""
import json
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "chat1_2026-11-19_wd2"))
import wd2_run as W  # noqa: E402  (reads sys.argv[1] as the checkout of main)

FM, B, te, CR, H, f2m, UNITS = W.FM, W.B, W.te, W.CR, W.H, W.f2m, W.UNITS
DPS = 60
XS = (Fr(13, 100), Fr(31, 100))
YS = (Fr(3, 2), Fr(3), Fr(6))
SECS = ("up", "down", "lep")


def base(tau, L):
    I, QI, QJ, QK, EPS, U, ED, BLOCKS = FM.setup()
    eta = mp.exp(I * mp.pi * tau / 12) * mp.qp(mp.exp(2 * I * mp.pi * tau))
    c3 = [te.ev(cc, tau) for cc in te.B[1]]
    S = c3[0] * QI + c3[1] * QJ + c3[2] * QK
    St = EPS * W.conj(S) * EPS.T
    return dict(I=I, EPS=EPS, ED=ED, BLOCKS=BLOCKS, t=tau, y=mp.im(tau), L=L, t1p=2 * mp.pi * eta ** 3,
                th1=lambda z: B.th_mp(1, z, tau), c3=c3, S=S, St=St)


def channels(T, a, b, sec, norms):
    """W-D2's sector_M split: per unit s, (R_s, n_s), or None for a zero channel; n_s only if norms"""
    I, t, y, L = T["I"], T["t"], T["y"], T["L"]
    ql, qr = B.SIXY[B.SECTORS[sec][0]], B.SIXY[B.SECTORS[sec][1]]
    x = (ql * a, 2 * ql * b)
    yy = (qr * a, 2 * qr * b)
    ap, am = x[0] + yy[0], x[0] - yy[0]
    bp, bm = (x[1] + yy[1]) / 2, (x[1] - yy[1]) / 2
    e = mp.exp(-2 * I * mp.pi * f2m(x[0]))
    kap = {"1": -I * e, "i": mp.mpf(-1), "j": -e, "k": I}
    cs = {"1": (ap + H, bp + H), "i": (ap + H, bp), "j": (ap, bp + H), "k": (ap, bp)}
    ds = {"1": (am + H, bm + H), "i": (am + H, bm), "j": (am, bm + H), "k": (am, bm)}
    out = {}
    for s in UNITS:
        if FM.is_zero(cs[s]) or FM.is_zero(ds[s]):
            out[s] = None
            continue
        R = kap[s] * B.thc_mp(f2m(cs[s][0]), f2m(cs[s][1]), 0, t) * B.thc_mp(f2m(ds[s][0]), f2m(ds[s][1]), 0, t) / T["t1p"]
        n = None
        if norms:
            al, be = cs[s][0] - H, cs[s][1] - H
            z = f2m(al) * t + f2m(be)
            a0 = 2 * I * mp.pi * f2m(al) + mp.diff(T["th1"], z) / T["th1"](z)
            c = FM.F_u(cs[s][0] - H, cs[s][1] - H, t, y) + mp.pi * mp.log(y) - 2 * mp.pi * (mp.euler + mp.log(mp.pi))
            c = c - mp.pi * abs(a0) ** 2 * mp.exp(-2 * L)
            arg = 2 * mp.pi * L + c
            n = mp.sqrt(arg) if arg > 0 else mp.mpf(0)
        out[s] = (R, n)
    return out


def contraction(T, Hm, s):
    EPS, E = T["EPS"], T["ED"][s]
    return [[sum(((Ca.T * EPS * Hm * Cb)[m, n] * E[m, n] for m in range(2) for n in range(2)), mp.mpc(0))
             for Cb in T["BLOCKS"]] for Ca in T["BLOCKS"]]


def flat(v):
    if isinstance(v, mp.matrix):
        return [v[i, j] for i in range(v.rows) for j in range(v.cols)]
    if isinstance(v, list):
        out = []
        for z in v:
            out.extend(flat(z) if isinstance(z, (list, mp.matrix)) else [z])
        return out
    return [v]


def rho(fn, tau):
    h = mp.mpf(10) ** -20
    fx = [(p - m) / (2 * h) for p, m in zip(flat(fn(tau + h)), flat(fn(tau - h)))]
    fy = [(p - m) / (2 * h) for p, m in zip(flat(fn(tau + mp.mpc(0, 1) * h)), flat(fn(tau - mp.mpc(0, 1) * h)))]
    dbar = max(abs((u + mp.mpc(0, 1) * v) / 2) for u, v in zip(fx, fy))
    dtau = max(abs((u - mp.mpc(0, 1) * v) / 2) for u, v in zip(fx, fy))
    return float(dbar / dtau) if dtau > 0 else float("nan")


def f_residue(a, b, sec, s, L):
    return lambda t: channels(base(t, L), a, b, sec, False)[s][0]


def f_channel(a, b, sec, s, L, reading):
    def f(t):
        T = base(t, L)
        R = channels(T, a, b, sec, False)[s][0]
        return [[R * z for z in r] for r in contraction(T, T[reading], s)]
    return f


def f_normalised(a, b, sec, L):
    def f(t):
        T = base(t, L)
        chs = channels(T, a, b, sec, True)
        acc = [[mp.mpc(0)] * 3 for _ in range(3)]
        for s in UNITS:
            if chs[s] is None:
                continue
            K = contraction(T, T["S"], s)
            for i in range(3):
                for j in range(3):
                    acc[i][j] += chs[s][1] * chs[s][0] * K[i][j]
        return acc
    return f


def main():
    if W.MAIN is None:
        sys.exit("give a checkout of main")
    mp.mp.dps = DPS
    res = []
    for name, (a, b) in W.POINTS.items():
        for x in XS:
            for y in YS:
                tau = mp.mpc(f2m(x), f2m(y))
                xr = ((float(x) + 0.5) % 1.0) - 0.5
                L0 = mp.mpf(CR.canon(complex(xr, float(y)))["L_2"])
                row = {"point": name, "x": str(x), "y": str(y)}
                row["H0"] = rho(lambda t: base(t, L0)["c3"], tau)
                h1, h2S, h2St = [], [], []
                for sec in SECS:
                    chs = channels(base(tau, L0), a, b, sec, False)
                    for s in UNITS:
                        if chs[s] is None:
                            continue
                        h1.append(rho(f_residue(a, b, sec, s, L0), tau))
                        h2S.append(rho(f_channel(a, b, sec, s, L0, "S"), tau))
                        h2St.append(rho(f_channel(a, b, sec, s, L0, "St"), tau))
                row["channels"] = len(h1)
                row["H1"] = max(h1)
                row["H2_S"] = max(h2S)
                row["H2_St_min"] = min(h2St)
                row["H2_St_max"] = max(h2St)
                T0 = base(tau, L0)
                Tm = base(mp.mpc(-mp.re(tau), mp.im(tau)), L0)
                row["H3"] = float(mp.mnorm(T0["St"] - Tm["S"], 1) / mp.mnorm(T0["S"], 1))
                row["H4"] = {sec: rho(f_normalised(a, b, sec, L0), tau) for sec in SECS}
                res.append(row)
                print("%-4s x = %-6s y = %-3s  channels %2d  H0 %.1e  H1 %.1e  H2(S) %.1e  H2(S~) %.2e to %.2e  H3 %.1e  "
                      "H4 up %.2e down %.2e lep %.2e" % (name, x, y, row["channels"], row["H0"], row["H1"], row["H2_S"],
                                                        row["H2_St_min"], row["H2_St_max"], row["H3"], row["H4"]["up"],
                                                        row["H4"]["down"], row["H4"]["lep"]), flush=True)
    json.dump(res, open(os.path.join(HERE, "wh1_output.json"), "w"), indent=1)
    print("H0 holds:", all(r["H0"] <= 1e-15 for r in res))
    print("H1 holds:", all(r["H1"] <= 1e-15 for r in res))
    print("H2 holds:", all(r["H2_S"] <= 1e-15 and r["H2_St_max"] >= 0.1 for r in res))
    print("H3 holds:", all(r["H3"] <= 1e-20 for r in res))
    print("H4 holds:", all(min(r["H4"].values()) >= 1e-3 for r in res))


if __name__ == "__main__":
    main()
