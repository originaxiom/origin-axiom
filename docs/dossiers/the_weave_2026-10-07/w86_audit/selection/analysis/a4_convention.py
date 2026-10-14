import json, sys
import numpy as np
S = sys.argv[1]
d = json.load(open(f"{S}/committed/chat1_2026-10-14_selection/post_hoc_reversal.json"))
def sv(K, Y, conv):
    ev, U = np.linalg.eigh(K)
    Kmh = U @ np.diag(ev ** -0.5) @ U.conj().T
    if conv == "script":      # (K^-1/2)^T Y K^-1/2  : kinetic read as phi^dag K phi
        Yh = Kmh.T @ Y @ Kmh
    else:                     # field Psi = sum phi^a F_a: kinetic phi^a K_ab conj(phi^b) = phi^dag K^T phi -> use K^T
        ev2, U2 = np.linalg.eigh(K.T)
        Kmh2 = U2 @ np.diag(ev2 ** -0.5) @ U2.conj().T
        Yh = Kmh2.T @ Y @ Kmh2
    s = np.sort(np.linalg.svd(Yh, compute_uv=False))
    return s[1] / s[2], s[0] / s[2]
for w, r in d["words"].items():
    K = np.array([[complex(*z) for z in row] for row in r["K"]]); Y = np.array([[complex(*z) for z in row] for row in r["Y"]])
    a = sv(K, Y, "script"); b = sv(K, Y, "KT")
    print(f"{w:9s} script m2/m3 {a[0]:.10e} m1/m3 {a[1]:.10e} | K^T convention m2/m3 {b[0]:.10e} m1/m3 {b[1]:.10e} | rel diff {abs(a[0]-b[0])/a[0]:.2e} {abs(a[1]-b[1])/a[1]:.2e}  (json {r['m2/m3']:.10e})")
# CP: Jarlskog-type invariant for a single sector is zero; check Takagi realness: phase of det
