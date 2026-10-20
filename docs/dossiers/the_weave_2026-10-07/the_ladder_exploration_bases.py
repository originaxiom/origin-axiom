"""EXPLORATORY: the commutator of every free basis of the commutator subgroup (LR, RL is one) has trace -2;
pairs that are not a basis give other traces."""
import random
import numpy as np
L = np.array([[1, 1], [0, 1]], dtype=object); R = np.array([[1, 0], [1, 1]], dtype=object)
inv = lambda M: np.array([[M[1, 1], -M[0, 1]], [-M[1, 0], M[0, 0]]], dtype=object)
comm = lambda u, v: u.dot(v).dot(inv(u)).dot(inv(v))
A, B = L.dot(R), R.dot(L)
rng = random.Random(1); traces = set()
for _ in range(2000):
    u, v = A, B
    for _ in range(rng.randint(1, 12)):
        k = rng.randrange(6)
        if k == 0: u = u.dot(v)
        elif k == 1: u = u.dot(inv(v))
        elif k == 2: v = v.dot(u)
        elif k == 3: v = v.dot(inv(u))
        elif k == 4: u, v = v, u
        else: u = inv(u)
    traces.add(comm(u, v).trace())
print("bases reached by 2000 random Nielsen products of (LR, RL): traces of their commutator:", traces)
print("not bases: tr[LR, (RL)^2] =", comm(A, B.dot(B)).trace(), "; tr[(LR)^2, RL] =", comm(A.dot(A), B).trace(),
      "; tr[L, R] =", comm(L, R).trace())
