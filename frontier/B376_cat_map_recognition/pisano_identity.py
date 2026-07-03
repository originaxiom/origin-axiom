"""B376 (R1 continuation) — the Pisano identity: ord(W1@N) = pi(N)/2 exactly.

The recognition candidate: the level tower is the QUANTIZED GOLDEN CAT MAP (Hannay-Berry 1980
lineage): the quantized A1 = [[2,1],[1,1]] = (Fibonacci matrix)^2 at level N has order equal to
ord(A1 mod N) = pi(N)/2 where pi is the Pisano period. Verified against the five measured
orders (20, 60, 100, 180, 300 at N = 15, 45, 75, 135, 225) — including the sector-less level.
If exact, the sector/seam arithmetic has a home literature (Kurlberg-Rudnick Hecke theory for
cat maps) and Phase 2's derive-don't-fit target is fixed. PRIOR-ART FLAG: the cat-map frame is
KNOWN mathematics; the identification claim here is only the exact order identity + the naming
of the derive-target. Nothing about the seam is claimed derived yet.
"""
import json
import os


def pisano(n):
    a, b, k = 0, 1, 0
    while True:
        a, b = b, (a + b) % n
        k += 1
        if a == 0 and b == 1:
            return k


def ord_cat(n):
    """Multiplicative order of A1 = [[2,1],[1,1]] mod n."""
    def mul(X, Y):
        return [[(X[0][0]*Y[0][0]+X[0][1]*Y[1][0]) % n, (X[0][0]*Y[0][1]+X[0][1]*Y[1][1]) % n],
                [(X[1][0]*Y[0][0]+X[1][1]*Y[1][0]) % n, (X[1][0]*Y[0][1]+X[1][1]*Y[1][1]) % n]]
    A = [[2, 1], [1, 1]]
    P, k = A, 1
    I = [[1, 0], [0, 1]]
    while P != I:
        P = mul(P, A)
        k += 1
        if k > 10 * n:
            raise RuntimeError
    return k


MEASURED = {15: 20, 45: 60, 75: 100, 135: 180, 225: 300}

if __name__ == "__main__":
    rep = {}
    for N, measured in MEASURED.items():
        pi = pisano(N)
        oc = ord_cat(N)
        rep[N] = dict(pisano=pi, half=pi // 2, ord_cat_map=oc, measured_weil_order=measured,
                      identity=(pi // 2 == measured == oc))
        print(f"N={N}: pi(N)={pi}  pi/2={pi//2}  ord(A1 mod N)={oc}  measured={measured}  "
              f"IDENTITY: {pi//2 == measured == oc}")
    # predictions for the registered next rungs
    for N in (375, 405, 675):
        pi = pisano(N)
        print(f"PREDICTION N={N}: ord(W1) = pi/2 = {pi//2}  (ord(A1 mod N) = {ord_cat(N)})")
        rep[N] = dict(pisano=pi, predicted_order=pi // 2)
    json.dump(rep, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "pisano_identity.json"), "w"), indent=1)
