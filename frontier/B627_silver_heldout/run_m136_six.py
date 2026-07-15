import sys, time
sys.path.insert(0, '.')
import pipeline as pl
import mpmath as mp


def log(msg):
    print(msg, flush=True)


gens = ['a', 'b', 'c']
relators = ['aBAbcc', 'aaCbcB']
alpha = pl.alpha_map(gens, relators)
log(f"alpha = {alpha}")

DPS = 250
acts, G = pl.get_holonomy_hp('m136', gens, dps=DPS)

import pickle
results = {}
for m_exp in [1, 4, 5, 7, 8, 11]:
    t0 = time.time()
    tau, qn, maxrel, qdeg = pl.compute_tau_exact(m_exp, gens, relators, ['a', 'c'], 'b',
                                                  acts, alpha, dps=DPS, log=log, extra=8,
                                                  probe_dps=100)
    dt = time.time() - t0
    print(f"m={m_exp}: tau={tau}  maxrel={maxrel}  qdeg={qdeg}  time={dt:.1f}s")
    print(f"  qn = {[complex(c) for c in qn]}")
    results[m_exp] = (tau, [(str(c.real), str(c.imag)) for c in qn], str(maxrel), qdeg, dt)
    pickle.dump(results, open('m136_six_results.pkl', 'wb'))

print("DONE")
