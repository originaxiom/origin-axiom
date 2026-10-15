import math, numpy as np, runpy
ns = runpy.run_path("ref1.py", run_name="ref1")
F, in_frame = ns["F"], ns["in_frame"]
for name in ("AL", "AR", "A_RL", "A_RRL"):
    A = ns[name]; Af = in_frame(A)
    # scalar z with Af = z S, S real orthogonal det +1
    d = np.linalg.det(Af); z = d ** (1 / 3)
    best = None
    for k in range(3):
        zk = z * np.exp(2j * np.pi * k / 3)
        S = Af / zk
        if np.abs(S.imag).max() < 1e-9 and np.linalg.det(S.real) > 0: best = (zk, S.real)
    zk, S = best
    ang = math.degrees(math.acos(max(-1, min(1, (np.trace(S) - 1) / 2))))
    ev, V = np.linalg.eig(S); ax = V[:, np.argmin(np.abs(ev - 1))].real
    print(f"{name}: z = {np.round(zk,6)} (arg/2pi = {np.angle(zk)/(2*np.pi):.4f}), angle {ang:.2f} deg, axis {np.round(ax/np.max(np.abs(ax)),4)}")
    print(np.round(S, 6))
