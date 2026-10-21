"""P-223 (exploratory): the weave's moves act on the common point Q8 = <i, j> (a -> i, b -> j) by automorphisms; Aut(Q8) = S4
= the one-qubit Clifford group modulo phases (its action on the three Pauli axes with signs). Words: L: a -> a, b -> b a?
The record's L, R as automorphisms of F2 (B1600/B1607): R: a -> a b, b -> b; L: a -> a, b -> b a (so that sigma = L o P, sigma
a -> a b, b -> a, as B1607 states, is checked below). Each automorphism of F2 induces one of Q8 (it fixes the common point up
to conjugation, B1679); the induced map is read off as a signed 3x3 matrix on the axes (i, j, k)."""
import itertools, numpy as np
# quaternions as 4-vectors (1, i, j, k)
def qm(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2, a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)
ONE, I, J, K = (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)
def word(w, a, b):                       # evaluate a word over {a, b, A, B} (capitals = inverses) at a, b in Q8
    inv = lambda q: (q[0], -q[1], -q[2], -q[3])
    out = ONE
    for ch in w: out = qm(out, {"a": a, "b": b, "A": inv(a), "B": inv(b)}[ch])
    return out
MOVES = {"L": ("a", "ab"), "R": ("ab", "b"), "P": ("b", "a"), "sigma": ("ab", "a")}
def induced(m):
    ia, ib = word(MOVES[m][0], I, J), word(MOVES[m][1], I, J)
    k = qm(ia, ib)
    return np.array([ia[1:], ib[1:], k[1:]]).T            # columns: images of i, j, k on the axes
def compose_check():
    # sigma = L o P: apply P first, then L, as maps of F2: sigma(x) = L(P(x)) with substitution
    sub = lambda w, im: "".join({"a": im[0], "b": im[1], "A": inv_w(im[0]), "B": inv_w(im[1])}[c] for c in w)
    return sub(MOVES["P"][0], MOVES["L"]), sub(MOVES["P"][1], MOVES["L"])
def inv_w(w): return "".join({"a": "A", "b": "B", "A": "a", "B": "b"}[c] for c in reversed(w))
M = {m: induced(m) for m in MOVES}
for m, X in M.items(): print(m, "on (i, j, k):", X.astype(int).tolist(), "det", int(round(np.linalg.det(X))))
print("sigma = L o P as substitutions:", compose_check(), "(the record's sigma: a -> ab, b -> a)")
# the group generated in SO(3) (signed permutation matrices) by L and R, and with P
def gen(gs):
    els = [np.eye(3, dtype=int)]; seen = {np.eye(3, dtype=int).tobytes()}; i = 0
    while i < len(els):
        for g in gs:
            Y = (g @ els[i]).astype(int)
            if Y.tobytes() not in seen: seen.add(Y.tobytes()); els.append(Y)
        i += 1
    return els
G = gen([M["L"].astype(int), M["R"].astype(int)]); GP = gen([M["L"].astype(int), M["R"].astype(int), M["P"].astype(int)])
ords = lambda els: sorted(next(n for n in range(1, 25) if np.array_equal(np.linalg.matrix_power(X, n), np.eye(3, dtype=int))) for X in els)
from collections import Counter
print("<L, R> in Aut(Q8) on the axes: order", len(G), "element orders", dict(Counter(ords(G))), "all det +1:", all(round(np.linalg.det(X)) == 1 for X in G))
print("with the swap: order", len(GP))
# Clifford gates on the Bloch axes (X, Y, Z): S = rotation by 90 deg about Z, H = (X <-> Z, Y -> -Y)
print("L is a 90-degree rotation about the i axis:", np.array_equal(M["L"].astype(int), np.array([[1,0,0],[0,0,1],[0,-1,0]])) or np.array_equal(M["L"].astype(int), np.array([[1,0,0],[0,0,-1],[0,1,0]])))
print("R is a 90-degree rotation about the j axis:", abs(np.trace(M["R"]) - 1) < 1e-9 and np.array_equal(M["R"][:, 1].astype(int), np.array([0, 1, 0])))
print("sigma: order", next(n for n in range(1, 25) if np.array_equal(np.linalg.matrix_power(M["sigma"].astype(int), n), np.eye(3, dtype=int))), "trace", int(np.trace(M["sigma"])), "(a 120-degree rotation about a body diagonal: the T-type magic axis)")
import json, pathlib
json.dump({"moves_on_axes": {m: X.astype(int).tolist() for m, X in M.items()}, "order_LR": len(G),
           "element_orders_LR": dict(Counter(ords(G))), "order_with_swap": len(GP),
           "sigma_is_L_after_P": list(compose_check()) == ["ab", "a"]},
          open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1)
