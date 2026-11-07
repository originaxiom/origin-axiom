"""L206's closure check (R76-1; data-free): does the parabolic pair (the meridian ABABB, a) generate pi_1(m003)?
With SnapPy's presentation <a, b | abAAbabbb> and its peripheral meridian ABABB, the word w = mer^-1 a^-1 mer^-1 a^-3
is claimed to equal b. The holonomy is faithful into PSL(2, C), so w b^-1 = +-I there means w = b in the group."""
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import snappy
G = snappy.Manifold("m003").fundamental_group()
assert G.generators() == ["a", "b"] and G.relators() == ["abAAbabbb"] and G.peripheral_curves()[0][0] == "ABABB"
def hol(w):
    S = G.SL2C(w); return np.array([[complex(S[i, j]) for j in range(2)] for i in range(2)])
def pm(X, Y): return min(np.abs(X - Y).max(), np.abs(X + Y).max())
w = "bbaba" + "A" + "bbaba" + "AAA"
print(f"w = {w}: |hol(w) - hol(b)| up to sign {pm(hol(w), hol('b')):.1e}; control |hol(w) - hol(a)| {pm(hol(w), hol('a')):.2f}")
print("-> b lies in <ABABB, a>, so the parabolic pair generates pi_1(m003)")
