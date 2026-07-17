"""B669 H1 — the level-ladders of chiral metallic words vs the fig-8
(prereg d5f025bf sealed first). |tr_odd(rho_kappa(W))|^2, k = 1..8."""
import importlib.util
import os

import numpy as np

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(ROOT, "frontier", "B238_su32_levelrank",
                         "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

WORDS = {"RL (fig-8)": "RL", "R2L (trace 4)": "RRL",
         "RRLL (silver m136)": "RRLL", "R3L (trace 5)": "RRRL"}
BANKED_FIG8 = [1, 1, 1, 0, 1, 1, 2, 1]

print("== the level-ladders, k = 1..8 (kappa = 4..11) ==", flush=True)
table = {}
for name, word in WORDS.items():
    row = []
    for k in range(1, 9):
        w, S, T, c = b238.su3_data(k)
        Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
        R_, L_ = T, Si @ Ti @ S
        M = np.eye(len(w), dtype=complex)
        for ch in word:
            M = M @ (R_ if ch == "R" else L_)
        prs = [(i, w.index((wt[1], wt[0]))) for i, wt in enumerate(w)
               if (wt[1], wt[0]) > wt]
        odd = np.zeros((len(w), len(prs)))
        for j, (a, b) in enumerate(prs):
            odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
        tr = np.trace(odd.T @ M @ odd)
        row.append(abs(tr) ** 2)
    table[name] = row
    print(f"  {name:20s} |Z_k|^2 = " +
          " ".join(f"{v:8.4f}" for v in row), flush=True)

fig8 = [round(v) for v in table["RL (fig-8)"]]
print(f"\nC1 fig-8 control reproduces banked {BANKED_FIG8}: "
      f"{fig8 == BANKED_FIG8}", flush=True)

print("\n== verdict per word (grows vs bounded on k = 1..8) ==", flush=True)
for name, row in table.items():
    mx = max(row)
    tail = max(row[4:])
    print(f"  {name:20s} max = {mx:.4f}; the sealed 'grows' prediction "
          f"{'CONFIRMED' if mx > 6 else 'REFUTED (bounded like the fig-8)'}",
          flush=True)

print("\n== m136 amphichirality (SnapPy) ==", flush=True)
try:
    import snappy
    sg = snappy.Manifold("m136").symmetry_group()
    print(f"  |Isom(m136)| = {sg.order()}; amphichiral: "
          f"{sg.is_amphicheiral()}", flush=True)
except Exception as e:
    print(f"  snappy unavailable: {e}", flush=True)

print("\nB669 H1 DONE", flush=True)
