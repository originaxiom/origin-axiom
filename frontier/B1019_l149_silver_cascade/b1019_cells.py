"""B1019 -- L149's cells (sealed ce6b0329). Exact integer arithmetic throughout.

C1: the entry map for m = 2 (silver) and m = 3 (bronze): the own-conductor shadow
    <R^m, L^m> <= SL(2, Z/(m^2+4)), its order, structure fingerprint, and its McKay
    classification -- where the DECISIVE test is abstract embeddability in SU(2):
    every noncyclic finite subgroup of SU(2) has a UNIQUE involution (-1). A shadow
    with more than one involution is NO SU(2) subgroup, hence has NO McKay partner,
    hence NO Lie entry: the cascade has nowhere to start through that door.
C2: if an entry exists, the chirality gate on its minuscule carrier.
C4: the generic mod-3 door (banked B996) recorded for the refinement statement.
"""
import json
import os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def matmod(A, B, N):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % N for j in range(2))
                 for i in range(2))


def close(gens, N):
    I = ((1, 0), (0, 1))
    seen = {I}
    frontier = [I]
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                Mg = matmod(M, g, N)
                if Mg not in seen:
                    seen.add(Mg)
                    nxt.append(Mg)
        frontier = nxt
    return seen


def order_of(M, N):
    I = ((1, 0), (0, 1))
    P, k = M, 1
    while P != I:
        P = matmod(P, M, N)
        k += 1
        if k > 10000:
            raise RuntimeError("order overflow")
    return k


def analyze(m):
    N = m * m + 4
    R = ((1, m % N), (0, 1))          # R^m as a shear with parameter m (R = [[1,1],[0,1]] -> R^m)
    L = ((1, 0), (m % N, 1))
    G = close([R, L], N)
    orders = Counter(order_of(M, N) for M in G)
    involutions = orders[2]
    minus_I = ((N - 1) % N and ((N - 1, 0), (0, N - 1)) in G)
    # abelianization fingerprint: commutator subgroup size via normal closure of commutators
    # (cheap: derived subgroup by closing over all commutators of generators with everything)
    def inv2(M):
        a, b = M[0]; c, d = M[1]
        det = (a * d - b * c) % N
        # det = 1 in SL2; inverse = [[d,-b],[-c,a]]
        return ((d % N, (-b) % N), ((-c) % N, a % N))
    comms = set()
    for A in (R, L):
        for B_ in G:
            c_ = matmod(matmod(A, B_, N), matmod(inv2(A), inv2(B_), N), N)
            comms.add(c_)
    D = close(list(comms), N)
    return {
        "m": m, "conductor": N, "order": len(G),
        "element_order_histogram": dict(sorted(orders.items())),
        "involutions": involutions,
        "contains_minus_I": bool(minus_I),
        "derived_subgroup_order": len(D),
        "abelianization_order": len(G) // len(D),
        # THE DECISIVE McKAY TEST (C1). The ADE classification of finite SU(2) subgroups is
        # COMPLETE: cyclic (any order), binary dihedral Q_{4n} (unique involution), 2T (24),
        # 2O (48), 2I (120) -- so a NONCYCLIC subgroup needs (i) a UNIQUE involution AND
        # (ii) order in {4n} (with quaternion structure) or {24, 48, 120}. A first draft used
        # (i) alone -- NECESSARY READ AS SUFFICIENT (the exact slip the abelianization-proxy
        # memory names): SL(2,13) has a unique involution and order 2184, and embeds in
        # nothing. Both conditions now enforced; nonabelian order cap 120 (B997's bound).
        "cyclic": max(orders) == len(G),
        "su2_embeddable": (max(orders) == len(G)) or (
            involutions == 1 and len(G) <= 120 and (
                len(G) in (24, 48, 120) or (len(G) % 4 == 0 and max(orders) == len(G) // 2))),
    }


def main():
    out = {}
    for m in (2, 3):
        r = analyze(m)
        out[f"m{m}"] = r
        print(f"--- m = {m} (conductor {r['conductor']}) ---")
        for k, v in r.items():
            if k != "m":
                print(f"  {k}: {v}")
        if r["su2_embeddable"]:
            print("  -> SU(2)-embeddable: a McKay partner EXISTS; C2 (chirality gate) applies")
        else:
            print("  -> NOT SU(2)-embeddable (multiple involutions): NO McKay partner,")
            print("     NO Lie entry -- the cascade has nowhere to start through this door.")
    # the golden control (m = 1): conductor 5, shadow SL(2,5) = 2I, unique involution -- banked
    g = analyze(1)
    out["m1_control"] = g
    print(f"--- m = 1 control (conductor 5) ---")
    print(f"  order: {g['order']}  involutions: {g['involutions']}  su2: {g['su2_embeddable']}")
    json.dump(out, open(os.path.join(HERE, "results.json"), "w"), indent=1)
    print("results.json written")


if __name__ == "__main__":
    main()
