"""R17 audit of the B1126 instrument -- value-free (object-side / synthetic only).

(1) Comparator power: sig_figs_agree replicated byte-for-byte from b1126_compare.py L325-349,
    tested on synthetic pairs incl. the decimal-rollover case the arc says it fixed.
(2) Planted positive for the VERDICT BRANCH: the top-level verdict flips off
    look_elsewhere_verdict.startswith('NOTABLE'); replicate p_LE = 1-(1-min(1,2*rel))^352
    and the 0.02 threshold, and show a synthetic survivor at rel=1e-6 would have flipped
    the verdict to NEEDS-INSTRUMENT (i.e. the banked negative COULD have failed).
"""
import mpmath as mp
mp.mp.dps = 60

def sig_figs_agree(period_val, target_val):
    if target_val == 0 or period_val == 0:
        return 0
    rel = abs(period_val - target_val) / abs(target_val)
    if rel == 0:
        return 30
    return max(0, int(mp.floor(-mp.log10(rel))))

print("--- (1) comparator power (synthetic, no SM values) ---")
cases = [
    (mp.mpf('1.99999995'), mp.mpf('2.00000001'), "rollover pair (arc bug case)"),
    (mp.mpf('0.5542165'), mp.mpf('0.5542165')*(1+mp.mpf('1e-4')), 'planted 1e-4 apart'),
    (mp.mpf('0.5542165'), mp.mpf('0.5542165')*(1+mp.mpf('1e-6')), 'planted 1e-6 apart'),
    (mp.mpf('3.14159265358979'), mp.mpf('2.71828'), 'far pair'),
    (mp.pi, mp.pi, 'identical'),
]
for a,b,label in cases:
    print(f"  {label:38s} -> sig_figs_agree = {sig_figs_agree(a,b)}")

print("\n--- (2) planted positive through the verdict branch ---")
n_pairs_sealed = 352
def branch(rel):
    p_single = min(1, 2*rel)
    p_LE = 1 - (1 - p_single) ** n_pairs_sealed
    notable = not (p_LE > mp.mpf('0.02'))   # code: UNREMARKABLE if p_LE > 0.02 else NOTABLE
    # top-level: survivors exist (>=3 sf) and any NOTABLE -> NEEDS-INSTRUMENT
    verdict = 'NEEDS-INSTRUMENT' if notable else 'NO-OBJECT-PERIOD-IS-AN-SM-RATIO (dismissed)'
    return p_LE, notable, verdict
for rel in [mp.mpf('2.53874e-4'), mp.mpf('2.9e-5'), mp.mpf('1e-5'), mp.mpf('1e-6')]:
    p_LE, notable, v = branch(rel)
    print(f"  rel={mp.nstr(rel,4):>10s}  p_LE={mp.nstr(p_LE,4):>10s}  NOTABLE={notable}  -> {v}")
