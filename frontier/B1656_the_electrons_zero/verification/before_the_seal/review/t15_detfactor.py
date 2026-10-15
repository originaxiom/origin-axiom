import numpy as np, sys
sys.path.insert(0, ".")
from load_inst import load
ns = load()
for k in ("coupling","np","UNITS","weighted_M"): globals()[k] = ns[k]
rng = np.random.default_rng(11)
S = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
def c(): return rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2))
def ell(M): return np.linalg.det(coupling(S, M))/np.linalg.det(M)
M1, M2 = c(), c()
print("ell(M1+M2) - ell(M1) - ell(M2) =", abs(ell(M1+M2) - ell(M1) - ell(M2)), " |ell(M1)| =", abs(ell(M1)))
print("homogeneity: ell(2 M1)/ell(M1) =", ell(2*M1)/ell(M1))
