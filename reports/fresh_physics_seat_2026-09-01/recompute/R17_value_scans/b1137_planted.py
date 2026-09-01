"""R17 planted-positive control for the B1137 instrument -- OBJECT SIDE ONLY.

Plant the true relation  5*V - 3*L(1,chi_-3) - 2*pi = 0  (coefficients of height <= 5,
well inside every H in the grid; involves TWO regulator/constant basis elements) and feed
V through the committed run_cell pipeline at several digit budgets:

  digits=250 : better than the search precision -- does the instrument ADMIT a real relation?
  digits=60  : the prereg precision floor.
  digits=10  : the BEST physical target's budget (m_p/m_e).

No SM value or new pairing is introduced: V is a pure regulator combination.
"""
import sys, json
sys.path.insert(0, '/home/user/origin-axiom/frontier/B1137_regulator_probe')
from mpmath import mp, mpf, nstr
import basis as basismod
import pslq_probe as probe

mp.dps = 320
b, forms, R = basismod.build_pruned_basis(dps=300)
mp.dps = 320
V_exact = (mpf(3)*mp.mpf(b['Lm3_1']) + mpf(2)*mp.mpf(b['pi'])) / mpf(5)
V_str = nstr(V_exact, 280)
print("planted V = (3*Lm3_1 + 2*pi)/5 =", nstr(V_exact, 30), "...")

out = []
for digits in [250, 60, 10]:
    for (D, H) in [(1, 100), (1, 1000000)]:
        r = probe.run_cell(V_str, digits, 1e-4, f'PLANTED_d{digits}', D, H)
        r.pop('time', None)
        out.append(r)
        keep = {k: r.get(k) for k in ['name','D','H','dps','digits','found','coeffs',
                'involves_V','involves_regulator','height_aware_ok','slack_digits',
                'exact_stable','resid_hi_digits','within_1sigma','sigma_dev','ADMITTED']}
        print(json.dumps(keep, default=str))
json.dump(out, open('b1137_planted_results.json','w'), indent=1, default=str)
