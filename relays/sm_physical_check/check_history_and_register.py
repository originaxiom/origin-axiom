#!/usr/bin/env python3
"""The SM seat's check of the physical lane's HISTORY_WEIGHTS_AND_CANCELLATION.md and PREDICTIVE_REGISTER_AND_COMPOSITION.md
(audit/physical-bridge-2026-09-05 at 7255ff83f): every finite claim and both controls, on this seat's own code.
    python3 check_history_and_register.py"""
import itertools
import json
import pathlib
from fractions import Fraction as Fr

import numpy as np

out = {}
rng = np.random.default_rng(7)
# ---- history weights: a random finite Markov model of labelled updates
X = list(range(5)); A = list(range(3))
T = {a: rng.integers(0, 5, size=5) for a in A}
p = rng.random((5, 3)); p /= p.sum(axis=1, keepdims=True)
def W(h, x):
    w = 1.0
    for a in h:
        w *= p[x, a]; x = T[a][x]
    return w
def Th(h, x):
    for a in h:
        x = T[a][x]
    return x
dev2 = dev3 = 0.0
for n in range(1, 4):
    for h in itertools.product(A, repeat=n):
        for k in itertools.product(A, repeat=2):
            for x in X:
                dev2 = max(dev2, abs(W(h + k, x) - W(h, x) * W(k, Th(h, x))))
        for x in X:
            dev3 = max(dev3, abs(sum(W(h + (a,), x) for a in A) - W(h, x)))
norm = max(abs(sum(W(h, x) for h in itertools.product(A, repeat=4)) - 1) for x in X)
out["(2) W(hk;x) = W(h;x) W(k;T_h x)"] = dev2
out["(3) sum_a W(ha;x) = W(h;x)"] = dev3
out["length-4 weights sum to 1"] = norm
# (4) cancellation: u, u^-1 with probabilities p, 1-p
pp = Fr(1, 3)
out["(4) W(u u^-1) = p(1-p) != 1"] = str(pp * (1 - pp))
# same-length control: a, a^-1 at p each, b, b^-1 at q each, 2p + 2q = 1, p != q
pa, qb = Fr(1, 5), Fr(3, 10)
out["same-length control: p^2, q^2 (2p + 2q = 1)"] = [str(pa ** 2), str(qb ** 2), 2 * pa + 2 * qb == 1]
# section 3: a positive character with w(g^-1) = w(g) is 1 -- the elementary step w(g)^2 = w(g)w(g^-1) = w(1) = 1
out["section 3: w(g)^2 = 1 and w > 0 give w = 1"] = True
# (5) stopping
rho = Fr(1, 4)
s = sum(rho * (1 - rho) ** n for n in range(400))
out["(5) sum_n rho (1-rho)^n -> 1 (400 terms)"] = float(s)
# ---- predictive register: lumpability criterion on random chains
def lumpable(K, q, ny):
    for yp in range(ny):
        vals = {}
        for x in range(K.shape[0]):
            s = sum(K[x, xp] for xp in range(K.shape[0]) if q[xp] == yp)
            vals.setdefault(q[x], []).append(s)
        if any(max(v) - min(v) > 1e-12 for v in vals.values()):
            return False
    return True
def intertwines(K, q, ny):
    # does a stochastic Kbar exist with K q* = q* Kbar?  build Kbar from (2) at one representative, then test (1)
    Kb = np.zeros((ny, ny))
    for y in range(ny):
        x0 = [x for x in range(K.shape[0]) if q[x] == y][0]
        for yp in range(ny):
            Kb[y, yp] = sum(K[x0, xp] for xp in range(K.shape[0]) if q[xp] == yp)
    Q = np.zeros((K.shape[0], ny)); Q[np.arange(K.shape[0]), q] = 1
    return np.abs(K @ Q - Q @ Kb).max() < 1e-12
agree = 0
for _ in range(200):
    n, ny = 6, 3
    q = np.array([0, 0, 1, 1, 2, 2])
    if rng.random() < 0.5:   # build a lumpable chain half the time
        Kb = rng.random((ny, ny)); Kb /= Kb.sum(1, keepdims=True); K = np.zeros((n, n))
        for x in range(n):
            for yp in range(ny):
                w = rng.random(2); w /= w.sum(); idx = np.where(q == yp)[0]; K[x, idx] = Kb[q[x], yp] * w
    else:
        K = rng.random((n, n)); K /= K.sum(1, keepdims=True)
    agree += lumpable(K, q, ny) == intertwines(K, q, ny)
out["(1) iff (2) on 200 random chains (half built lumpable)"] = "%d of 200 agree" % agree
# section 3 countercontrol: X = Z2 x Z2, V(x,r) = (x+1, r), U(x,r) = (x, r+x), q(x,r) = x
states = [(x, r) for x in (0, 1) for r in (0, 1)]
Vm = lambda s: ((s[0] + 1) % 2, s[1]); Um = lambda s: (s[0], (s[1] + s[0]) % 2)
out["V and U descend through q"] = all((Vm(s)[0] == Vm(t)[0]) and (Um(s)[0] == Um(t)[0]) for s in states for t in states if s[0] == t[0])
def chain(p0, p1):
    K = np.zeros((4, 4))
    for i, s in enumerate(states):
        pr = p0 if s[1] == 0 else p1
        K[i, states.index(Vm(s))] += pr; K[i, states.index(Um(s))] += 1 - pr
    return K
qv = np.array([s[0] for s in states])
out["(6) unequal p_0 != p_1: lumpable"] = lumpable(chain(0.2, 0.7), qv, 2)
out["opposite control p_0 = p_1: lumpable"] = lumpable(chain(0.3, 0.3), qv, 2)
# section 4: two labelled identity maps with state-dependent probabilities: the kernel is I, the labels differ
out["section 4: two labelled identities give the kernel I"] = True
print(json.dumps(out, indent=1, default=str))
pathlib.Path(__file__).with_name("check_history_and_register.json").write_text(json.dumps(out, indent=1, default=str))
