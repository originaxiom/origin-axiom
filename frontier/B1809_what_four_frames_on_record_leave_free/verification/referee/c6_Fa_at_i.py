"""c6: the record's other parameter-free Higgs directions at the configuration-fixed point tau = i, zero line, B1667's
canonical radii.  At tau = i only the vector a(i) enters the coupling.  B1730's F_a = eta^(3-a) (eps th2^a, eps th4^a,
i th3^a), a = 2 mod 4, eps = i^((a+2)/2) (same component order as B1691's R = (-th2^2, -th4^2, i th3^2)/(...)); at i,
th2 = th4 and th3^2 = sqrt2 th2^2, so F_a(i) is prop. to eps(1, 1, 0) + (0, 0, i 2^(a/4)).  F_2 is prop. to R (control: must give
c1's R row).  F_a lies outside B1691/B1806's H-cov proofs (rho twisted by chi_eta^(2a); the P-406 referee's C5b) -- reported
as values only."""
import pathlib, json, math
import numpy as np
src = pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py").read_text().split("out = {")[0]
g = {"__file__": str(pathlib.Path(__file__).with_name("c1_canonical_values_at_i.py"))}
exec(compile(src, "c1_head", "exec"), g)
B = g["B"]; LI = g["LI"]
t = 1j; x, yy = B.sector_twists(0, t, 1, -4); Rr = B.residues(x, yy, t); c = B.cA(x, yy, t, Rr)
def m_of(a, L):
    Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    u = {k: (math.sqrt(2 * math.pi * L + c[k]) * Rr[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) for k in B.UNITS}
    sv = np.linalg.svd(B.coupling(Sm, B.weighted_M(u)), compute_uv=False)
    return float(sv[2] / sv[0]), float(sv[1] / sv[0])
out = {}
for a_ in (-2, 2, 6, 10, 14, 22):
    eps = 1j ** ((a_ + 2) // 2)
    v = [eps, eps, 1j * 2 ** (a_ / 4)]
    row = {Ln: dict(zip(("m1/m3", "m2/m3"), ["%.5g" % z for z in m_of(v, L)])) for Ln, L in (("L_max(i)", LI[0]), ("L_2(i)", LI[1]), ("L=2560", 2560.0))}
    out[f"F_{a_}"] = row; print(f"F_{a_}", v, row, flush=True)
json.dump(out, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
