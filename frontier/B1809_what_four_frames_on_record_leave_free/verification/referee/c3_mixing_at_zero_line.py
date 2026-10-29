"""c3: the census's F1 row says 'V == 1 at zero line (B1620)'.  B1620 says: with couplings in tau alone every mixing
matrix is a PERMUTATION (one Higgs representation per sector).  Check in B1656's four-channel coupling at the zero line
(the record's machinery, as c1) with DIFFERENT covariant sections in the up and down sectors (DR, a0, generic 7/2 and
19/2), at a generic tau and both canonical radii: |V| = |U_u^H U_d| from the SVD's left singular vectors (sorted by
singular value)."""
import pathlib, json, math
import numpy as np, mpmath as mp
src = pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py").read_text().split("out = {")[0]
g = {"__file__": str(pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py"))}
exec(compile(src, "c1_head", "exec"), g)
B, te, secs = g["B"], g["te"], g["secs"]

def Ymat(sec, tau, L, ql=1, qr=-4):
    t = complex(tau); x, yy = B.sector_twists(0, t, ql, qr)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in sec]
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(Sm, B.weighted_M(u))

out = {}
for tau in (complex(0.25, 1.25), complex(0.15, 2.0)):
    LL = g["canon"](tau)
    for (nu, nd) in (("DR (k=3/2)", "a0 (k=7/2)"), ("7/2 generic seed1", "19/2 generic seed2"), ("DR (k=3/2)", "DR (k=3/2)")):
        for Ln, L in (("L_max", LL[0]), ("L_2", LL[1])):
            Yu = Ymat(secs[nu], tau, L, 1, -4); Yd = Ymat(secs[nd], tau, L, 1, 2)   # up: (Q,u) = (1,-4); down: (Q,d) = (1,2)
            Uu, su, _ = np.linalg.svd(Yu); Ud, sd, _ = np.linalg.svd(Yd)
            V = np.abs(Uu.conj().T @ Ud)
            key = f"{tau} {Ln} up={nu} down={nd}"
            out[key] = {"|V|": [[round(float(v), 4) for v in r] for r in V], "max offdiag": float(np.max(V - np.diag(np.diag(V)))),
                        "is_permutation": bool(np.allclose(np.sort(V, axis=1)[:, :2], 0, atol=1e-8))}
            print(key, out[key], flush=True)
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
