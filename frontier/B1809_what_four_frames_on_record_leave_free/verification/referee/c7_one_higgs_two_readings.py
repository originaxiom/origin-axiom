"""c7: one Higgs (DR, the record's census Higgs) at the zero line, the record's reading (up S~, down S; S~ = eps S* eps^T,
B1790 l. 3-10): is V == 1?  B1656's four-channel coupling as c1; tau generic and on Re tau = 0; L_2 of the grid point."""
import pathlib, json, math
import numpy as np, mpmath as mp
src = pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py").read_text().split("out = {")[0]
g = {"__file__": str(pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py"))}
exec(compile(src, "c1_head", "exec"), g)
B, te, secs = g["B"], g["te"], g["secs"]
def Y(sec, tau, L, ql, qr, tilde):
    t = complex(tau); x, yy = B.sector_twists(0, t, ql, qr)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in sec]
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    if tilde: Sm = B.EPS @ Sm.conj() @ B.EPS.T
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(Sm, B.weighted_M(u))
out = {}
for tau in (complex(0.25, 1.25), complex(0.15, 2.0), complex(0.0, 1.25)):
    LL = g["canon"](tau) or (0.67, 2.5)
    Yu = Y(secs["DR (k=3/2)"], tau, LL[1], 1, -4, True); Yd = Y(secs["DR (k=3/2)"], tau, LL[1], 1, 2, False)
    Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]; V = Uu.conj().T @ Ud
    J = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    out[str(tau)] = {"|V|": [[round(abs(v), 4) for v in r] for r in V], "J": J}
    print(tau, out[str(tau)], flush=True)
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
