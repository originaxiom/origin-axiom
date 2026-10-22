"""B1710 (P-255): the SM seat's W121 index law checked on main.  No data.  rho_T built from its definition (B1634, as in B1708):
the exponents of rho_T(T) and of its conjugate; then W121's Riemann-Roch count on a closed elliptic surface with
N = 12 chi(O_S) I_1 fibres and Deligne's canonical extension at each,
    index = 3 deg((K_C (x) L)^(1/2)) - N sum(mu) + 3 (1 - g),   deg K_C = 2g - 2, deg L = chi(O_S),
for chi = 1..6 and g = 0..3 (the genus must cancel), and on K3 (chi = 2, g = 0): the canonical extension's degree and the
index.  The reduction of the four-dimensional index to this count (by Leray) is the seat's reading and is not checked."""
import io, json, contextlib, importlib.util, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
src = (ROOT / "frontier" / "B1708_w120_w121_on_main" / "verification" / "w120_w121_on_main.py").read_text(encoding="utf-8")
part = src[src.index("# (5)"):src.index("Ta, Tb = rT")]
ns = {}
exec("import json, math, pathlib\nimport numpy as np, mpmath as mp\nmp.mp.dps = 30\n"
     "def eta(tau): q = mp.exp(2j * mp.pi * tau); return mp.exp(2j * mp.pi * tau / 24) * mp.qp(q)\n" + part, ns)
rT = ns["rT"]
def exponents(M):
    ev = np.linalg.eigvals(M)
    return sorted(Fr(float(np.angle(e) / (2 * np.pi)) % 1).limit_denominator(48) for e in ev)
mu = exponents(rT); mubar = exponents(np.conj(rT))
out = {"exponents_rho_T": [str(m) for m in mu], "sum_rho_T": str(sum(mu)), "exponents_conj": [str(m) for m in mubar], "sum_conj": str(sum(mubar))}
def index(chi, g, smu):
    N = 12 * chi; d = Fr(2 * g - 2 + chi, 2)
    return 3 * d - N * smu + 3 * (1 - g)
law = {}
for chi in range(1, 7):
    vals = {g: (index(chi, g, sum(mu)), index(chi, g, sum(mubar))) for g in range(4)}
    law[chi] = {"rho_T": str(vals[0][0]), "conj": str(vals[0][1]), "genus_cancels": len({v for v in vals.values()}) == 1}
out["law"] = law
out["law_is_-15chi_and_-18chi"] = all(Fr(law[c]["rho_T"]) == -15 * c and Fr(law[c]["conj"]) == -18 * c for c in law)
out["K3"] = {"canonical_extension_degree_rho_T": str(-24 * sum(mu)), "canonical_extension_degree_conj": str(-24 * sum(mubar)),
             "index_rho_T": str(index(2, 0, sum(mu))), "index_conj": str(index(2, 0, sum(mubar)))}
out["never_pm3"] = all(abs(Fr(law[c][h])) != 3 for c in law for h in ("rho_T", "conj"))
json.dump(out, open(HERE / "the_index_law.json", "w"), indent=1)
print(json.dumps(out, indent=1))
