"""c5: the census's 'J = 0 on the mirror geodesics (B1750 3)' at the zero line, per-sector sections (B1656's
four-channel coupling as c1/c3).  On Re tau = 0 and Re tau = 1/2 (mirror-fixed lines of tau -> -conj(tau) mod T) with
real-coefficient sections (DR up, a0 down) vs the record's seeded sections (complex rational coefficients)."""
import pathlib, json, math
import numpy as np, mpmath as mp
src = pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py").read_text().split("out = {")[0]
g = {"__file__": str(pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py"))}
exec(compile(src, "c1_head", "exec"), g)
B, te, secs = g["B"], g["te"], g["secs"]
def Ymat(sec, tau, L, ql, qr):
    t = complex(tau); x, yy = B.sector_twists(0, t, ql, qr)
    R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
    a = [complex(te.ev(cc, mp.mpc(t.real, t.imag))) for cc in sec]
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    return B.coupling(Sm, B.weighted_M(u))
def J_of(Yu, Yd):
    Uu = np.linalg.svd(Yu)[0][:, ::-1]; Ud = np.linalg.svd(Yd)[0][:, ::-1]     # light to heavy
    V = Uu.conj().T @ Ud
    return float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1]))), [[round(abs(v), 4) for v in r] for r in V]
out = {}
for tau in (complex(0.0, 1.3), complex(0.5, 1.3), complex(0.17, 1.3)):
    for nu, nd in (("DR (k=3/2)", "a0 (k=7/2)"), ("7/2 generic seed1", "19/2 generic seed2")):
        J, V = J_of(Ymat(secs[nu], tau, 2.6, 1, -4), Ymat(secs[nd], tau, 2.6, 1, 2))
        out[f"{tau} up={nu} down={nd}"] = {"J": J, "|V|": V}
        print(tau, nu, nd, "J = %.3e" % J, V, flush=True)
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
