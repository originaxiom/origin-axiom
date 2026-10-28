import numpy as np
rng = np.random.default_rng(11)
def rsl2():
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); return A / np.sqrt(np.linalg.det(A))
def sym2raw(A):
    a, b, c, d = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
    return np.array([[a*a, a*c, c*c], [2*a*b, a*d + b*c, 2*c*d], [b*b, b*d, d*d]])
g, h = rsl2(), rsl2()
if np.allclose(sym2raw(g @ h), sym2raw(g) @ sym2raw(h)): sym2 = sym2raw
else: sym2 = lambda A: sym2raw(A.T)
assert np.allclose(sym2(g @ h), sym2(g) @ sym2(h))
gam, gg = rsl2(), rsl2(); v = rng.normal(size=3) + 0j
print("Sym2: phi invariant:", np.allclose(np.linalg.solve(sym2(gam @ gg), sym2(gam) @ v), np.linalg.solve(sym2(gg), v)),
      " PSL-well-defined:", np.allclose(sym2(-gg), sym2(gg)))
# antiholomorphic: sigma = complex conjugate rep; trivialisation conj(g)^-1 v is invariant but not holomorphic in g
cj = lambda A: A.conj(); v2 = rng.normal(size=2) + 0j
print("conj rep: phi invariant:", np.allclose(np.linalg.solve(cj(gam @ gg), cj(gam) @ v2), np.linalg.solve(cj(gg), v2)), "(smooth, antiholomorphic in g)")
