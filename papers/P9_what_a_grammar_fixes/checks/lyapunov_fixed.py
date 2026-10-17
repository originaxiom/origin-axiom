"""Fixed-length estimate of the top Lyapunov exponent of the walk on L, R (probability (1-p)/2 each) and their inverses
(p/2 each), right multiplication: lambda = (1/n) log ||X_n||, accumulated with renormalisation. 60 walks of 40 000 steps."""
import math, random
import numpy as np
L = np.array([[1, 1], [0, 1]], float); R = np.array([[1, 0], [1, 1]], float)
Li, Ri = np.linalg.inv(L), np.linalg.inv(R)
for p in (0.0, 0.5):
    est = []
    for w in range(60):
        rng = random.Random(1000 + w); X = np.eye(2); acc = 0.0
        for n in range(40000):
            u = rng.random()
            M = L if u < (1 - p) / 2 else R if u < 1 - p else Li if u < 1 - p / 2 else Ri
            X = X @ M
            if n % 20 == 19:
                s = np.linalg.norm(X); acc += math.log(s); X /= s
        acc += math.log(np.linalg.norm(X)); est.append(acc / 40000)
    est = np.array(est); print(f"p = {p}: lambda = {est.mean():.4f} +- {est.std(ddof=1)/math.sqrt(len(est)):.4f} (60 walks x 40 000 steps)")
