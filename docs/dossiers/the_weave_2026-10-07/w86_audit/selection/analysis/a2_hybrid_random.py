import json, math, sys, subprocess
import numpy as np
S = sys.argv[1]
d = json.load(open(f"{S}/committed/chat1_2026-10-14_selection/thread_frame.json"))
per = d["readouts"]["per thread"]
banked = json.load(open(f"{S}/sm87/docs/dossiers/the_weave_2026-10-07/the_surface_yukawa.json"))
Yb = np.array([[complex(*z) for z in row] for row in banked["X4"]["Y (Y0 = 2.0)"]])
print("W72 Y (Y0=2):"); print(np.array2string(Yb, precision=4))
print("W72 Y ImY/max", np.max(np.abs(Yb.imag))/np.max(np.abs(Yb)))
def masses(K, Y):
    ev, U = np.linalg.eigh(K)
    Kmh = U @ np.diag(ev ** -0.5) @ U.conj().T
    s = np.sort(np.linalg.svd(Kmh.T @ Y @ Kmh, compute_uv=False))
    return s[1]/s[2], s[0]/s[2]
rng = np.random.default_rng(1)
print("thread  own m2/m3   hybrid(W72Y)   randomY median [10%,90%] of m2/m3/own   Y=I m2/m3/own   Ythread~Yb?")
for w, r in sorted(per.items(), key=lambda kv: kv[1]["y_max"]):
    K = np.array([[complex(*z) for z in row] for row in r["K"]]); Yt = np.array([[complex(*z) for z in row] for row in r["Y"]])
    own = masses(K, Yt); hyb = masses(K, Yb)
    rr = []
    for _ in range(2000):
        A = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3)); Yr = A + A.T
        rr.append(masses(K, Yr)[0]/own[0])
    rr = np.array(rr)
    idm = masses(K, np.eye(3))[0]/own[0]
    # compare thread Y to W72 Y: best scalar fit and residual
    a = np.vdot(Yb.flatten(), Yt.flatten())/np.vdot(Yb.flatten(), Yb.flatten())
    resid = np.linalg.norm(Yt - a*Yb)/np.linalg.norm(Yt)
    print(f"{w:6s} {own[0]:.3e}  x{hyb[0]/own[0]:.3f}   x{np.median(rr):.3g} [{np.quantile(rr,0.1):.3g}, {np.quantile(rr,0.9):.3g}]   x{idm:.3g}   resid {resid:.2f}")
# K eigen-structure for the root vs Y in K-eigenbasis
r = per["LR"]; K = np.array([[complex(*z) for z in row] for row in r["K"]]); Yt = np.array([[complex(*z) for z in row] for row in r["Y"]])
ev, U = np.linalg.eigh(K)
print("root K eig", ev)
print("root K (real part):"); print(np.array2string(K.real, precision=2))
print("root Y thread:"); print(np.array2string(Yt.real, precision=3))
print("root Y in K-eigvec basis (U^T Y U):"); print(np.array2string(np.abs(U.T @ Yt @ U), precision=3))
print("W72 Y in root K-eigvec basis:"); print(np.array2string(np.abs(U.T @ Yb @ U), precision=3))
