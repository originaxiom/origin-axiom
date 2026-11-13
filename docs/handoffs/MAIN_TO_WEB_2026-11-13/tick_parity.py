"""Main's check of 2026-11-13 (not banked; the web seat's card W-C8 part 1 is its second computation).

The agy lane's reading (relayed by the author): undoing the act reverses the bundle's orientation, so "the hand is the
arrow". Standard, and B1914's sign det X * e. This script tests the stronger claim, that the hand at the mark flips
exactly when the act is undone, on the golden thread with the record's own matrices:
  J = [[1,1],[1,0]] (the tick, LP, det -1, J^2 = LR), K = [[0,1],[-1,0]] (undoing: K LR K^-1 = (LR)^-1, det +1).
Checked: the three relations J^2 = LR, K^2 = -I, K J K^-1 = -J^-1; for every +-J^n K^e (n < 8) whether it exchanges the
mark's two pairs {+-v} and {+-2v} mod 5 (v = (1, 2), B1867), against (-1)^(n+e); and the SnapPy names: b-+R is the
Gieseking manifold m000, non-orientable, with orientation cover m004. Prints booleans and names only."""
import numpy as np

L = np.array([[1, 1], [0, 1]]); R = np.array([[1, 0], [1, 1]])
J = np.array([[1, 1], [1, 0]]); K = np.array([[0, 1], [-1, 0]]); I2 = np.eye(2, dtype=int)


def inv(A):
    d = int(round(np.linalg.det(A)))
    return d * np.array([[A[1, 1], -A[0, 1]], [-A[1, 0], A[0, 0]]])


def swaps_pairs(X, v=np.array([1, 2])):
    u = tuple((X @ v) % 5)
    keep = {tuple(v % 5), tuple((-v) % 5)}
    swap = {tuple((2 * v) % 5), tuple((-2 * v) % 5)}
    assert u in keep or u in swap, "the line is not kept"
    return u in swap


if __name__ == "__main__":
    phi = L @ R
    print("J^2 == LR:", bool((J @ J == phi).all()), "; det J =", int(round(np.linalg.det(J))))
    print("K^2 == -I:", bool((K @ K == -I2).all()), "; K LR K^-1 == (LR)^-1:", bool((K @ phi @ inv(K) == inv(phi)).all()))
    print("K J K^-1 == -J^-1:", bool((K @ J @ inv(K) == -inv(J)).all()))
    ok = True
    for s in (1, -1):
        for n in range(8):
            for e in (0, 1):
                X = s * np.linalg.matrix_power(J, n) @ np.linalg.matrix_power(K, e)
                ok &= swaps_pairs(X) == ((n + e) % 2 == 1)
    print("the hand at the mark of +-J^n K^e (n < 8) equals (-1)^(n+e):", ok)
    print("J alone (commutes with LR, det -1) exchanges the mark's pairs:", swaps_pairs(J))
    try:
        import snappy
        G = snappy.Manifold("b-+R")
        print("b-+R:", [str(x) for x in G.identify()][:1], "orientable:", G.is_orientable(),
              "; orientation cover:", [str(x) for x in G.orientation_cover().identify()][:1])
    except ImportError:
        print("snappy not available: the names are not checked")
