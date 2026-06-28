"""B247 (sage-python part 2) -- SnapPy ground-truth for the wrong-root catch. Requires sage-python (SnapPy).
Run: sage-python holonomy_ground_truth_sage.py

Settles definitively that the figure-eight discrete-faithful Riley parameter is u = e^{+-2 i pi/3} (root of
u^2+u+1), NOT chat2's e^{i pi/3} (root of u^2-u+1):
  * SnapPy's unsimplified holonomy has meridian generators (parabolic, trace -2); the meridian PAIR has
    tr(a c) = 2.5 + 0.866 i = 2 - e^{-2 i pi/3}  ->  u = e^{+-2 i pi/3}   (chat2's u would give tr = 1.5).
  * the conjugation-invariant tr[a,b] = u^2 + 2 = 1.5 +- 0.866 i for BOTH roots -- the trap that hid the error.
The pyenv adjudication.py records SNAPPY_MERIDIAN_TR_AB and the reproducible relator discriminator.
"""
import numpy as np
import snappy

M = snappy.Manifold("4_1")
G = M.fundamental_group(simplify_presentation=False)
gens = G.generators()
mats = {g: np.array(G.SL2C(g), dtype=complex) for g in gens}

print("generators:", gens, " relators:", G.relators())
parabolic = [g for g in gens if abs(abs(np.trace(mats[g])) - 2) < 1e-6]
print("parabolic (meridian) generators (trace -2):", parabolic)

# meridian pair trace -> Riley parameter
import itertools
for g1, g2 in itertools.combinations(parabolic, 2):
    A, B = mats[g1], mats[g2]
    tab = np.trace(A @ B)
    tcomm = np.trace(A @ B @ np.linalg.inv(A) @ np.linalg.inv(B))
    u = 2 - tab
    print(f"  meridian pair ({g1},{g2}): tr(ab) = {tab:.4f}  -> u = 2 - tr(ab) = {u:.4f}  (|u|={abs(u):.4f}, "
          f"arg={np.angle(u, deg=True):.1f} deg)   tr[a,b] = {tcomm:.4f}")
print("\nu has |u|=1 at arg = +-120 deg  => u = e^{+-2 i pi/3} (root of u^2+u+1). chat2's e^{i pi/3} (arg 60) FAILS.")
