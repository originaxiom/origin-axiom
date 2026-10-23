"""EXPLORATORY, labelled (post hoc rows chosen from committed results; no new data comparison): the geometry of the
left states at three rows: TWO_HIGGS's best six-row, B1735's row, P-344's nine-best row."""
import contextlib, importlib.util, io, sys, math, pathlib, json
import numpy as np
ZF = pathlib.Path(__file__).resolve().parents[2] / "chat1_2026-10-23_zero_free_frame"
sys.argv = ["x"]
spec = importlib.util.spec_from_file_location("zfc", ZF / "zero_free_census.py")
zfc = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(zfc)
rbs, B, tic = zfc.rbs, zfc.B, zfc.tic
TC = tic.TC
e1 = np.array([1, 0, 0], dtype=complex); h0 = np.array([0, 1, 1j]) / math.sqrt(2); hb = np.conj(h0)
FR = {"e1": e1, "h0": h0, "h0b": hb}

def chan_u(re_t, im_t, a, b):
    t = complex(re_t, im_t); w = a * t + b; U = {}
    for sec, (lf, rf) in TC.SECT.items():
        x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); Rr = B.residues(x, yy, t); c = B.cA(x, yy, t, Rr)
        for which in ("L_max", "L_2"):
            L = TC.L_of(t.imag, which)
            u = {kk: (math.sqrt(2 * math.pi * L + c[kk]) * Rr[kk] if c[kk] is not None and 2 * math.pi * L + c[kk] > 0 else 0) for kk in B.UNITS}
            U[(sec, which)] = u
    return U

def cross(h):
    return np.array([[0, -h[2], h[1]], [h[2], 0, -h[0]], [-h[1], h[0], 0]])

def closed(u, h):
    uv = np.array([u["i"], u["j"], u["k"]]); w = u["1"]
    return np.outer(uv, h) + np.outer(h, uv) - (uv @ h) * np.eye(3) + w * cross(h)

def comps(x):
    return " ".join(f"{k}:{abs(np.vdot(v, x)):.3f}" for k, v in FR.items())

P = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]])           # code order (j, i, k) <- unit order (i, j, k)

def study(name, re_t, im_t, a, b, hor, hdir):
    print(f"=== {name}: tau {re_t}+{im_t}i, line ({a}, {b}), {hor}")
    M = rbs.channels(re_t, im_t, a, b); U = chan_u(re_t, im_t, a, b)
    Ls = {}
    for sec in ("up", "down", "lep"):
        h = hdir[sec]
        Y = B.coupling(rbs.S_of(h), M[(sec, hor)])
        Yc = closed(U[(sec, hor)], h)
        # compare up to the block permutation and an overall factor
        Yp = P @ Yc @ P.T
        k = np.vdot(Yp.ravel(), Y.ravel()) / np.vdot(Yp.ravel(), Yp.ravel())
        dev = np.max(np.abs(Y - k * Yp)) / np.max(np.abs(Y))
        Uu, s, Vh = np.linalg.svd(Yc)
        uv = np.array([U[(sec, hor)][q] for q in "ijk"]); w = U[(sec, hor)]["1"]
        print(f" {sec}: closed-form check {dev:.1e} (factor {k:.3f});  m2/m3 {s[1]/s[0]:.3e}, m1/m3 {s[2]/s[0]:.3e}")
        print(f"   h: {comps(h)}  h.h {abs(h@h):.2e} | u: {comps(uv/np.linalg.norm(uv))} |u| {np.linalg.norm(uv):.3e} |w| {abs(w):.3e} |u.h|/|u| {abs(uv@h)/np.linalg.norm(uv):.3e} |u.u|/|u|^2 {abs(uv@uv)/np.linalg.norm(uv)**2:.3e}")
        for j, lab in ((2, "light"), (1, "middle"), (0, "heavy")):
            print(f"   left {lab:6s}: {comps(Uu[:, j])}   right {lab:6s}: {comps(np.conj(Vh[j]))}")
        Ls[sec] = Uu[:, ::-1]
    V = np.conj(Ls["up"].T) @ Ls["down"]
    print(" |V| =", np.abs(V).round(4).tolist())

def dirs(d, re_t, im_t):
    return zfc.direction(d, re_t, im_t)

r1 = (0.5625, 2.6); hu = dirs("F_6", *r1); hd = dirs("F_22", *r1)
study("TWO_HIGGS best six", *r1, 0.4, 0.1, "L_2", {"up": hu, "down": hd, "lep": hd})
r2 = (0.35, 3.05); h = dirs("dR", *r2)
study("B1735 row (dR split)", *r2, 0.4, 0.1, "L_max", {"up": np.conj(h), "down": h, "lep": h})
r3 = (0.35, 2.65); h = dirs("dR", *r3)
study("P-344 nine-best (dR S~ all)", *r3, 0.4, 0.5, "L_2", {"up": np.conj(h), "down": np.conj(h), "lep": np.conj(h)})
