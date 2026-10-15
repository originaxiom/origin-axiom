import math, numpy as np, runpy
ns = runpy.run_path("ref2.py", run_name="ref2")
F, AL, AR, A_RL, R_np, par = ns["F"], ns["AL"], ns["AR"], ns["A_RL"], ns["R_np"], ns["par"]
fr = [F[:, 0], F[:, 1], F[:, 2]]
def eigline_defect(v, A):  # 0 iff v is an eigenvector of A
    return par(A @ v, v)
pts = {"omega": complex(-0.5, math.sqrt(3) / 2), "omega+1": complex(0.5, math.sqrt(3) / 2)}
for sg in [(1, s2, s3) for s2 in (1, -1) for s3 in (1, -1)]:
    row = []
    for name, t in pts.items():
        RB = sum(sg[u] * R_np(t)[u] * fr[u] for u in range(3))
        row.append(f"{name}: {eigline_defect(RB, A_RL):.1e}")
    # sweep the fundamental strip for any tau where R_B is an RL eigenline
    best = min(((eigline_defect(sum(sg[u] * R_np(complex(x, y))[u] * fr[u] for u in range(3)), A_RL), x, y)
                for x in np.linspace(-1, 1, 81) for y in np.linspace(0.5, 2.0, 61)))
    print("signs", sg, " RL-eigenline defect at", ", ".join(row), f"; min over grid {best[0]:.1e} at tau={best[1]:+.3f}{best[2]:+.3f}i")
