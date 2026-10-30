"""Confirmation checks (data-free): (1) main's correction -- at t = 0, D^2 R = R o (th2^8, th4^8, th3^8)/48 componentwise;
(2) main's stable F against 50-digit values over u in [1e-4, 1e17]; (3) the strict decoupling limit with a light copy at
n = 2: Q's lowest eigenvalue is simple (an isolated leading-order direction), so 'no isolated vacuum' needs finite lambda v."""
import sys, pathlib, json
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import mpmath as mp
import ref_model as rm
out = {}
# (1)
mp.mp.dps = 40
def serre(fvec, k, tau):
    E2 = rm.eisenstein(tau)[0]
    return [mp.diff(lambda t, j=j: fvec(t)[j], tau) / (2j * mp.pi) - mp.mpf(k) / 12 * E2 * fvec(tau)[j] for j in range(3)]
rows = []
for tau in (mp.mpc("0.17", "1.23"), mp.mpc("-0.31", "0.97")):
    D2 = serre(lambda t: rm.DRvec(t), mp.mpf(3) / 2, tau)
    t2, t3, t4 = rm.thetas(tau); R = rm.Rvec(tau)
    mono = [R[0] * t2 ** 8 / 48, R[1] * t4 ** 8 / 48, R[2] * t3 ** 8 / 48]
    rows.append(float(max(abs(a / b - 1) for a, b in zip(D2, mono))))
out["t0_D2R_equals_R_o_(th2^8,th4^8,th3^8)/48_max_rel_dev"] = rows
# (2)
mp.mp.dps = 50
m02, mu2 = 0.003, 0.3
import numpy as np
def stable(u):
    return (2 * u * m02 + m02 ** 2) * (np.log(u / mu2) - 1.5) + (u + m02) ** 2 * np.log1p(m02 / u)
worst = 0.0
for e in np.linspace(-4, 17, 85):
    u = 10.0 ** e
    if u <= m02:
        continue
    U = mp.mpf(u); M = mp.mpf(m02); MU = mp.mpf(mu2)
    ex = (U + M) ** 2 * (mp.log((U + M) / MU) - mp.mpf(3) / 2) - U ** 2 * (mp.log(U / MU) - mp.mpf(3) / 2)
    worst = max(worst, float(abs((stable(u) - ex) / ex)))
out["stable_F_max_rel_dev_vs_50_digits_u_in_(m0^2,1e17]"] = worst
# (3) Q eigenvalues at the decoupling point with a light copy (the referee's t_conventions.json)
cv = json.loads((HERE.parent / "t_conventions.json").read_text())
out["n2_light_copy_Q_eigs"] = {"%s %s/%s" % (r["menu"], r["singlets"], r["triplets"]): r["Q_eigs"] for r in cv["rows"]
                               if "singlets" in r and r["n"] == 2 and not r["all_copies_heavy"]}
(HERE / "c_checks.json").write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
