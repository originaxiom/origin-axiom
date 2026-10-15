"""The joint law's identities on B1656's actual sector matter (P4, several L), errors measured against the natural
scale ||Y||^3 (det) and ||Y||^2 (adj), per sector; the sector data from joint_census.py's cache."""
import math, pathlib, pickle, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[3]
src = (ROOT / "frontier/B1656_the_electrons_zero/verification/the_electrons_zero.py").read_text(encoding="utf-8")
NS = {"__file__": str(ROOT / "frontier/B1656_the_electrons_zero/verification/x.py"), "__name__": "b1656_head"}
exec(compile(src.split("T0 = time.time()")[0], "b1656_head", "exec"), NS)
weighted_M, coupling, UNITS = NS["weighted_M"], NS["coupling"], NS["UNITS"]
DATA = pickle.load(open(pathlib.Path(__file__).with_name("sector_data.pkl"), "rb"))
EPS = np.array([[0, 1], [-1, 0]], dtype=complex); P = np.diag([1, -1, -1])
def A(M):
    m0, m1, m2, m3 = M.ravel(); I = 1j
    return np.array([[m0**2+m1**2+m2**2+m3**2, 2*I*(m0*m2+m1*m3), -I*(m0**2+m1**2-m2**2-m3**2)],
                     [2*I*(m0*m1+m2*m3), -4*m1*m2, 2*(m0*m1-m2*m3)],
                     [-I*(m0**2-m1**2+m2**2-m3**2), 2*(m0*m2-m1*m3), -m0**2+m1**2+m2**2-m3**2]])
def adj3(Y): return np.array([[np.linalg.det(np.delete(np.delete(Y, j, 0), i, 1))*(-1)**(i+j) for j in range(3)] for i in range(3)])
rng = np.random.default_rng(3); wd = wa = 0; dm = {}
for ln, secs in DATA.items():
    for sec, (R, c) in secs.items():
        for L in (5.0, 50.0, 500.0):
            M = weighted_M({s: (math.sqrt(2*np.pi*L + c[s])*R[s] if c[s] is not None else 0j) for s in UNITS})
            dm.setdefault(sec, []).append(abs(np.linalg.det(M))/np.linalg.norm(M)**2)
            for _ in range(3):
                S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Y = coupling(S, M); n = np.linalg.norm(Y)
                wd = max(wd, abs(np.linalg.det(Y) - 4*np.linalg.det(S)*np.linalg.det(M)*np.trace(EPS @ S @ M.T))/n**3)
                wa = max(wa, np.abs(adj3(Y) - np.linalg.det(S)*A(M) - np.linalg.det(M)*P @ A(S)).max()/n**2)
print(f"det law / ||Y||^3: {wd:.1e};  adj law / ||Y||^2: {wa:.1e}")
print("relative matter defect |det M|/||M||^2 by sector (min, max over lines and L):",
      {k: (f"{min(v):.1e}", f"{max(v):.1e}") for k, v in dm.items()})
