import numpy as np
rng = np.random.default_rng(11)
Lf = np.array([[1., 1.], [0., 1.]]); Rf = np.array([[1., 0.], [1., 1.]])
Li = np.linalg.inv(Lf); Ri = np.linalg.inv(Rf)
def run(p, nsteps, nruns):
    rates = []
    for r in range(nruns):
        g = np.eye(2); logscale = 0.0
        for n in range(nsteps):
            if rng.random() < p: m = Li if rng.random() < 0.5 else Ri
            else:                m = Lf if rng.random() < 0.5 else Rf
            g = g @ m
            if n % 8 == 7:
                nrm = np.linalg.norm(g); g /= nrm; logscale += np.log(nrm)
        nrm = np.linalg.norm(g); g /= nrm; logscale += np.log(nrm)
        rates.append(logscale/nsteps)   # top Lyapunov exponent = (1/2) * hyperbolic drift
    return np.mean(rates), np.std(rates)/np.sqrt(nruns)
for p in [0.0, 0.5]:
    m, se = run(p, 40000, 60)
    print(f"p={p}: Lyapunov exponent (log-norm growth per step) = {m:.4f} +- {se:.4f}   [paper's 'escape rate': 0.3959 at p=0, 0.1007 at p=1/2]")
