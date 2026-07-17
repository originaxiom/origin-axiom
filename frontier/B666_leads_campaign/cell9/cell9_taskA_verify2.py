"""B666 cell 9, TASK A, verification stage 2 (the independent-route
adjudication).

The exact multi-modular computation (cell9_taskA_exact_tau.py; 17 primes,
calibration 3/3 on the banked m=1/4/5 integers, 3 held-out primes per m)
returned RATIONAL INTEGERS for tau_7, tau_8, tau_11.  Against B627's sealed
250-dps numerics: m=7 agrees to ~27 digits, m=8 to ~18 digits (deviations
exactly at the sealed numerics' error level, real AND imaginary), while the
sealed m=11 value disagrees wholesale -- the precise hazard the B627 seat
itself pre-registered (cellF_full_result.md item 3: no independent reference
for m136 m=7/8/11; far-point check run only for m=7).

This stage adjudicates by an INDEPENDENT ROUTE: B627's own pipeline.py
(imported verbatim, unmodified), SnapPy polished m136 holonomy, at dps=500
(double the sealed precision) with extra held-out nodes.  Two-outcome:
either the numerics at higher precision converge to the exact integers
(CONFIRMED; the sealed m=11 digits are superseded as a numerical artifact),
or they reproduce the sealed values (my exact route dies and THAT banks).
"""
import sys, time, json, re
sys.path.insert(0, '/Users/dri/origin-axiom/frontier/B627_silver_heldout')
import pipeline as pl
import mpmath as mp
from fractions import Fraction

# The exact integers under test: parsed from the reconstruction transcript
# (taskA_output.txt -- each verified there on 3 held-out primes).
txt = open('/Users/dri/origin-axiom/frontier/B666_leads_campaign/cell9/'
           'taskA_output.txt').read()
EXACT = {}
for mo in re.finditer(r'm=(\d+): coords \(1,s,s\^2,s\^3, i,is,is\^2,is\^3\) =\n'
                      r'    1: (-?\d+)\n  qdeg', txt):
    EXACT[int(mo.group(1))] = Fraction(int(mo.group(2)))
assert set(EXACT) == {1, 4, 5, 7, 8, 11}, f"parse failure: {set(EXACT)}"
assert EXACT[1] == -16 and EXACT[4] == 11682800640 \
    and EXACT[5] == -1357126041600000
print("exact values under test:", {m: str(v) for m, v in sorted(EXACT.items())})


def log(msg):
    print(msg, flush=True)


gens = ['a', 'b', 'c']
relators = ['aBAbcc', 'aaCbcB']
alpha = pl.alpha_map(gens, relators)
log(f"alpha = {alpha}")
assert alpha == {'a': 0, 'b': 1, 'c': 0}

DPS = 500
# Independent-route numerics: the EXACT B649 entries (relators exactly I,
# verified in-sandbox) evaluated at 500 dps -- input precision is now
# unlimited, unlike B627's quad-double ManifoldHP holonomy (~60 digits),
# which is the diagnosed source of the sealed m=7/8/11 noise.
mp.mp.dps = DPS + 20
entries = json.load(open('/Users/dri/origin-axiom/frontier/'
                         'B649_silver_holonomy/entries_L.json'))
s_num = mp.sqrt(4 + 4 * mp.sqrt(2))          # the matching embedding
i_num = mp.mpc(0, 1)


def eval_L(pair):
    re4, im4 = pair
    v = mp.mpc(0)
    for j in range(4):
        fr = Fraction(re4[j])
        if fr:
            v += mp.mpf(fr.numerator) / mp.mpf(fr.denominator) * s_num ** j
        fi = Fraction(im4[j])
        if fi:
            v += i_num * mp.mpf(fi.numerator) / mp.mpf(fi.denominator) * s_num ** j
    return v


acts = {}
for g in gens:
    acts[g] = mp.matrix([[eval_L(entries[f"{g}00"]), eval_L(entries[f"{g}01"])],
                         [eval_L(entries[f"{g}10"]), eval_L(entries[f"{g}11"])]])
# sanity: relators ~ I at 500 dps
for rel in relators:
    Mm = mp.eye(2)
    for ch in rel:
        gm = acts[ch.lower()]
        if ch.isupper():
            gm = gm ** -1
        Mm = Mm * gm
    dev = max(abs(Mm[0, 0] - 1), abs(Mm[0, 1]), abs(Mm[1, 0]),
              abs(Mm[1, 1] - 1))
    log(f"relator {rel}: |image - I| = {mp.nstr(dev, 3)}")
    assert dev < mp.mpf(10) ** (-(DPS - 30))
log(f"exact-entry m136 holonomy at dps={DPS}: relator gates PASS")

results = {}
for m_exp in [1, 4, 5, 7, 8, 11]:
    t0 = time.time()
    tau, qn, maxrel, qdeg = pl.compute_tau_exact(
        m_exp, gens, relators, ['a', 'c'], 'b', acts, alpha,
        dps=DPS, log=log, extra=10, probe_dps=120)
    dt = time.time() - t0
    ex = EXACT[m_exp]
    exv = mp.mpf(ex.numerator) / mp.mpf(ex.denominator)
    dev = abs(tau - exv) / abs(exv)
    log(f"m={m_exp}: tau(numeric,dps500) = {mp.nstr(tau, 50)}")
    log(f"m={m_exp}: exact candidate     = {mp.nstr(exv, 50)}")
    log(f"m={m_exp}: relative deviation  = {mp.nstr(dev, 5)}   "
        f"(maxrel={mp.nstr(maxrel, 3)}, qdeg={qdeg}, {dt:.0f}s)")
    verdict = 'CONFIRMS EXACT INTEGER' if dev < mp.mpf('1e-60') else \
              ('AMBIGUOUS' if dev < mp.mpf('1e-20') else 'DISAGREES')
    log(f"m={m_exp}: VERDICT: {verdict}")
    results[m_exp] = (str(tau), str(dev), verdict)

log("ALL DONE")
for m_exp, (tau, dev, verdict) in sorted(results.items()):
    log(f"  m={m_exp}: {verdict} (rel dev {dev[:12]}...)")
