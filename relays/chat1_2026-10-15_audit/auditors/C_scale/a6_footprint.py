import json, math, sys
import numpy as np
d = json.load(open(sys.argv[1])); words = list(d)
Ln = {}
for w in words: Ln[len(w)] = Ln.get(len(w), 0) + 1
n = np.array([len(w) for w in words], float); vol = np.array([d[w][0] for w in words]); cs = np.array([d[w][1] for w in words])
logw = {"A": -n*math.log(2), "B": -n*math.log(3), "C": np.array([-math.log(len(w)*(len(w)-1)*Ln[len(w)]) for w in words])}
PI2 = math.pi**2
for key in "ABC":
    e = logw[key] - 6*vol/(6*math.pi); q = np.exp(e - e.max()); q /= q.sum()
    for norm, f in (("2pi k CS/pi^2", 2*math.pi/PI2), ("pi k CS/pi^2 (the other normalisation)", math.pi/PI2)):
        fp = {k: round(float(1 - (q*np.cos(f*k*cs)).sum()), 3) for k in (1, 2, 3, 4, 6)}
        print(key, norm, fp)
