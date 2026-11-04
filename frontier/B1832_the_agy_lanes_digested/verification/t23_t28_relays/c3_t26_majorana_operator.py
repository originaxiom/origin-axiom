"""c3: Theorem 26 (toe_closure.py:4988-5141 @ 18c607040): the docstring's Majorana operator against the code's.
Docstring (l. 5000-5006): P_h = h h^T / b_10^2 with b_10^2 = h.h (idempotent), M_R = b_10 (I + P_h) = b_10 I + h h^T / b_10,
  M_R^-1 = (I - P_h/2)/b_10.
Code (l. 5040-5047): P_h = h h^T / ||h||^2 (Hermitian norm), P_h^2 = alpha_h P_h with alpha_h = h.h/||h||^2,
  M_R = b_g (I + P_h), inverse (I - P_h/(1+alpha_h))/b_g.
Both inverses are Sherman-Morrison; the two operators differ unless h.h = ||h||^2 (h real)."""
import pathlib
import numpy as np
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)
rng = np.random.default_rng(26)
I3 = np.eye(3)
e1 = e2 = 0.0; diffs = []
for _ in range(20):
    h = rng.normal(size=3) + 1j * rng.normal(size=3); b = np.sqrt(h @ h)
    Pd = np.outer(h, h) / (h @ h); MRd = b * (I3 + Pd); MRd_inv = (I3 - Pd / 2) / b
    n2 = np.vdot(h, h).real; al = (h @ h) / n2; Pc = np.outer(h, h) / n2; MRc = b * (I3 + Pc); MRc_inv = (I3 - Pc / (1 + al)) / b
    e1 = max(e1, np.abs(Pd @ Pd - Pd).max(), np.abs(MRd @ MRd_inv - I3).max(), np.abs(MRd - (b * I3 + np.outer(h, h) / b)).max())
    e2 = max(e2, np.abs(Pc @ Pc - al * Pc).max(), np.abs(MRc @ MRc_inv - I3).max())
    diffs.append(np.abs(MRd - MRc).max() / np.abs(MRd).max())
say("docstring identities (P^2 = P, inverse, M_R = bI + hh^T/b): max err %.2e" % e1)
say("code identities (P^2 = alpha P, inverse): max err %.2e" % e2)
say("relative difference |M_R(doc) - M_R(code)| / |M_R(doc)| over 20 random complex h: min %.3f, median %.3f" % (min(diffs), float(np.median(diffs))))
h = np.array([1.0, 2.0, -0.5], dtype=complex); b = np.sqrt(h @ h)
say("control, h real: difference %.2e" % (np.abs(b * (I3 + np.outer(h, h) / (h @ h)) - b * (I3 + np.outer(h, h) / np.vdot(h, h).real)).max() / abs(b)))
pathlib.Path(__file__).with_name("c3_t26_majorana_operator_out.txt").write_text("\n".join(out) + "\n")
