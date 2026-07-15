"""B619 — the A5 bridge, verified (chat-1's mid-turn claim adjudicated).

CLAIMS TO TEST (verify-don't-trust):
  (C1) chat-1: "the theta-odd clock order at the golden stages = 60 =
       |A5|". The banked facts say the kappa=5 odd monodromy is the
       order-10 rotation e^{+-3 pi i/5} and the even block an order-20
       clock — a single matrix generates a CYCLIC group, never A5.
       Compute ord(rho(A1)), ord(rho_odd(A1)), ord(rho_even(A1)) at
       kappa = 5 exactly.
  (C2) THE REAL BRIDGE CANDIDATE (CC's sharpening): the PROJECTIVE image
       of the full golden-stage modular representation <rho(S), rho(T)>
       is PSL(2, Z/5) = A5 (order 60) — because the congruence level of
       the stage should be 5-related and PSL(2,5) is abstractly the
       icosahedral group. Compute the projective image order by BFS over
       words in S, T mod scalars, and test |G| = 60 + simplicity
       markers (element orders subset {1,2,3,5} for A5).
Both outcomes meaningful; C2 can fail (the level could be 10 or 15,
giving a bigger quotient).
"""
import importlib.util
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(HERE, "..", "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)

w, S, T, cc = b238.su3_data(2)
n = len(w)
Cm = np.zeros((n, n))
for i, wt in enumerate(w):
    Cm[w.index((wt[1], wt[0])), i] = 1.0
R = T
L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
A1 = R @ L                                     # rho(A1), the RL cat map

def order_of(M, cap=600):
    P = np.eye(n, dtype=complex)
    for k in range(1, cap + 1):
        P = P @ M
        # projective order: P proportional to I
        d = P[0, 0]
        if abs(d) > 1e-12 and np.allclose(P, d * np.eye(n), atol=1e-9):
            return k, ("scalar" if not np.allclose(P, np.eye(n), atol=1e-9)
                       else "exact")
    return None, None

prs = sorted({(min(a, b), max(a, b)) for (a, b) in w if a != b})
U = np.zeros((n, len(prs)))
for j, (a, b) in enumerate(prs):
    U[w.index((a, b)), j] = 1 / np.sqrt(2)
    U[w.index((b, a)), j] = -1 / np.sqrt(2)
evn = [i for i, wt in enumerate(w)]
A1odd = U.T @ A1 @ U

print("C1 — the clock orders at kappa = 5:", flush=True)
o_full, t_full = order_of(A1)
print(f"  ord rho(A1) (projective/exact): {o_full} ({t_full})", flush=True)
oo = None
P = np.eye(len(prs), dtype=complex)
for k in range(1, 200):
    P = P @ A1odd
    if np.allclose(P, P[0, 0] * np.eye(len(prs)), atol=1e-9) and \
            abs(P[0, 0]) > 1e-12:
        oo = k
        break
print(f"  ord rho_odd(A1): {oo}", flush=True)
print(f"  chat-1's 'clock order 60' vs the computed orders: "
      f"{'REFUTED as stated' if o_full != 60 and oo != 60 else 'matches'}",
      flush=True)

print("\nC2 — the projective image of <S, T> at kappa = 5:", flush=True)
def canon(M):
    # normalize the scalar: first nonzero entry -> 1
    idx = np.unravel_index(np.argmax(np.abs(M)), M.shape)
    Mn = M / M[idx]
    return tuple(np.round(Mn, 6).flatten())

gens = {"S": S, "T": T}
seen = {canon(np.eye(n, dtype=complex)): np.eye(n, dtype=complex)}
frontier = [np.eye(n, dtype=complex)]
while frontier and len(seen) <= 400:
    nf = []
    for M in frontier:
        for g in gens.values():
            X = M @ g
            c = canon(X)
            if c not in seen:
                seen[c] = X
                nf.append(X)
    frontier = nf
print(f"  projective image order: {len(seen)}"
      f"{' (cap hit - larger than 400)' if len(seen) > 400 else ''}",
      flush=True)
if len(seen) <= 400:
    orders = {}
    for M in seen.values():
        o, _ = order_of(M, cap=61)
        orders[o] = orders.get(o, 0) + 1
    print(f"  element projective-order census: {dict(sorted(orders.items(), key=lambda kv: (kv[0] is None, kv[0])))}",
          flush=True)
    isA5 = (len(seen) == 60 and set(k for k in orders if k) <= {1, 2, 3, 5})
    print(f"  |G| = 60 with element orders in {{1,2,3,5}} (the A5 "
          f"signature): {isA5}", flush=True)
print("B619 DONE", flush=True)
