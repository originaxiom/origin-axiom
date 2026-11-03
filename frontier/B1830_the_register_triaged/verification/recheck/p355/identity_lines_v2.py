"""P-355 item 1, CORRECTED (S297): v1 compared spectra by the ratio se/sd, which is noise where both sectors carry an exact
zero (B1716's zeros at orders 4 and 12) and so missed B1703's d = e on order 4. v2: spectra compared on the absolute scale
of the heaviest mass, max_i |se_i - sd_i| / max(sd_max, se_max); both identities tested, M_e = lam M_d^T (the transposed,
order 5, B1728) and M_e = lam M_d (the plain, order 4, B1728's Pati-Salam pairing). Every point (alpha, beta) of order
<= 12 (528; 266 up to sign). Data-free.  usage: identity_lines_v2.py re im seed tag"""
import json, math, pathlib, sys
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/scans"))
from identities_and_order5 import M_of, S_of, B
from mirror_rule_probe import Z
tau = complex(float(sys.argv[1]), float(sys.argv[2])); rng = np.random.default_rng(int(sys.argv[3])); tag = sys.argv[4]
pts = sorted({(F(a, N), F(b, N)) for N in range(1, 13) for a in range(N) for b in range(N) if math.gcd(math.gcd(a, b), N) == 1})
def fit(A, Bm):
    lam = np.vdot(Bm.ravel(), A.ravel()) / max(np.vdot(Bm.ravel(), Bm.ravel()).real, 1e-300)
    return float(np.linalg.norm(A - lam * Bm) / max(np.linalg.norm(A), 1e-300)), float(abs(lam))
def sdev(S, Md, Me):
    sd = np.sort(np.linalg.svd(B.coupling(S, Md), compute_uv=False)); se = np.sort(np.linalg.svd(B.coupling(S, Me), compute_uv=False))
    return float(np.abs(se - sd).max() / max(sd.max(), se.max(), 1e-300)), float(sd[0] / sd.max()), float(se[0] / se.max())
out = []
for p in pts:
    rec = {"pt": "%s,%s" % p, "order": math.lcm(p[0].denominator, p[1].denominator)}
    for ri, L in enumerate(Z.radii(tau)):
        Md, _ = M_of(tau, p, L, "down"); Me, _ = M_of(tau, p, L, "lepton")
        rT, lT = fit(Me, Md.T); rP, lP = fit(Me, Md)
        da = dq = 0.0; zmin = 1.0
        for _ in range(6):
            h = rng.normal(size=3) + 1j * rng.normal(size=3)
            a = sdev(S_of(0, h), Md, Me); q = sdev(S_of(0, np.array([0, h[1], h[2]])), Md, Me)
            da = max(da, a[0]); dq = max(dq, q[0]); zmin = min(zmin, a[1], a[2])
        rec["r%d" % ri] = dict(res_T=rT, lam_T=lT, res_P=rP, lam_P=lP, dev_any=da, dev_noQI=dq, light_min=zmin)
    out.append(rec)
    print(rec["pt"], rec["order"], " ".join("r%d T %.1e P %.1e any %.1e noQI %.1e m1 %.0e" % (i, rec["r%d" % i]["res_T"], rec["r%d" % i]["res_P"], rec["r%d" % i]["dev_any"], rec["r%d" % i]["dev_noQI"], rec["r%d" % i]["light_min"]) for i in (0, 1)), flush=True)
pathlib.Path(__file__).with_name("identity_v2_%s.json" % tag).write_text(json.dumps(dict(tau=[tau.real, tau.imag], seed=int(sys.argv[3]), points=out), indent=1))
