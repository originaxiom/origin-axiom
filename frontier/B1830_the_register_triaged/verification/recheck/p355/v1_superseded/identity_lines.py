"""P-355, owed item 1 (data-free): the lepton-down identity's full list of lines.  For every flat line of order <= 12
(the 266 of B1825's reach) at one tau and both radii: is M_e = lam M_d^T for a phase lam (B1728's swap law: then the
3D-Higgs lepton spectrum equals the down spectrum for EVERY Higgs direction), and if not, does the spectrum still coincide
for a Higgs with no QI component (B1742's order-10 case)?  Writes identity_lines.json."""
import json, math, pathlib, sys, cmath
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/scans"))
from identities_and_order5 import M_of, S_of, B
from mirror_rule_probe import Z
lines = sorted({(F(a, N), F(b, N)) for N in range(1, 13) for a in range(N) for b in range(N) if math.gcd(math.gcd(a, b), N) == 1})
print(len(lines), "lines", flush=True)
tau = complex(0.3, 2.6); rng = np.random.default_rng(355); out = []
for line in lines:
    rec = {"line": "%s,%s" % line, "order": max(line[0].denominator, line[1].denominator)}
    for ri, L in enumerate(Z.radii(tau)):
        Md, _ = M_of(tau, line, L, "down"); Me, _ = M_of(tau, line, L, "lepton")
        lam = np.vdot(Md.T.ravel(), Me.ravel()) / max(np.vdot(Md.T.ravel(), Md.T.ravel()), 1e-300)
        res = float(np.linalg.norm(Me - lam * Md.T) / max(np.linalg.norm(Me), 1e-300))
        dev_any, dev_noQI = 0.0, 0.0
        for _ in range(6):
            h = rng.normal(size=3) + 1j * rng.normal(size=3)
            for which, hh in (("any", h), ("noQI", np.array([0, h[1], h[2]]))):
                S = S_of(0, hh)
                sd = np.sort(np.linalg.svd(B.coupling(S, Md), compute_uv=False)); se = np.sort(np.linalg.svd(B.coupling(S, Me), compute_uv=False))
                dv = float(np.abs(se / np.maximum(sd, 1e-300) - 1).max())
                if which == "any": dev_any = max(dev_any, dv)
                else: dev_noQI = max(dev_noQI, dv)
        rec["r%d" % ri] = {"MeMdT_residual": res, "lam_abs": float(abs(lam)), "spec_dev_any_higgs": dev_any, "spec_dev_noQI": dev_noQI}
    out.append(rec)
    print(rec["line"], rec["order"], " ".join("r%d res %.1e any %.1e noQI %.1e" % (i, rec["r%d" % i]["MeMdT_residual"], rec["r%d" % i]["spec_dev_any_higgs"], rec["r%d" % i]["spec_dev_noQI"]) for i in (0, 1)), flush=True)
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
