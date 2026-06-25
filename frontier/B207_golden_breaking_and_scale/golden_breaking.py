"""B207 part 1 -- the golden shadow's symmetry-breaking lattice (firewall-clean MATH).

The golden object's congruence shadow is 2I = SL(2,F5) = E8 (B206). Symmetry breaking = G -> H
(residual subgroup). This computes, purely as finite-group structure: (a) where the metallic dynamics
RL mod 5 sits (its cyclic group, normalizer = residual symmetry), and (b) the McKay sub-chain
(2I contains 2T=E6 but NOT 2O=E7). FIREWALL: finite-group / McKay structure, NOT gauge symmetry
breaking; the Lie E8>E7>E6 chain and the finite 2I>2T containment are DIFFERENT things. Nothing to
CLAIMS.md. Cited by speculations/S038 (the firewalled reading)."""
from itertools import product
from collections import Counter

P = 5


def G():
    return [(a, b, c, d) for a, b, c, d in product(range(P), repeat=4) if (a*d-b*c) % P == 1]


def mul(x, y):
    a, b, c, d = x; e, f, g, h = y
    return ((a*e+b*g) % P, (a*f+b*h) % P, (c*e+d*g) % P, (c*f+d*h) % P)


def inv(x):
    a, b, c, d = x
    return (d % P, (-b) % P, (-c) % P, a % P)


def order(x):
    e, cur, k = (1, 0, 0, 1), x, 1
    while cur != e:
        cur = mul(cur, x); k += 1
    return k


def closure(gens):
    S, fr = {(1, 0, 0, 1)} | set(gens), set(gens)
    while fr:
        nf = set()
        for x in fr:
            for g in gens:
                for pr in (mul(x, g), mul(g, x)):
                    if pr not in S:
                        nf.add(pr); S.add(pr)
        fr = nf
    return S


def normalizer(H):
    Hs = set(H)
    return [g for g in G() if {mul(mul(g, h), inv(g)) for h in Hs} == Hs]


def contains_subgroup_of_order(n, g3_order=3, g2_order=4):
    g3 = next(x for x in G() if order(x) == g3_order)
    for h in G():
        if order(h) == g2_order and len(closure([g3, h])) == n:
            return True
    return False


def summary():
    Gl = G()
    RL = (2, 1, 1, 1)
    cyc = closure([RL])
    N = normalizer(cyc)
    return {
        "order_2I": len(Gl),
        "order_spectrum": dict(sorted(Counter(order(x) for x in Gl).items())),
        "RL_order": order(RL),
        "RL_cyclic_order": len(cyc),
        "normalizer_order": len(N),                 # residual symmetry the dynamics selects (2D5)
        "contains_2T_E6": contains_subgroup_of_order(24),    # 2I > 2T (E6)
        "contains_2O_E7": contains_subgroup_of_order(48),    # 2I > 2O (E7)?  -> False
    }


if __name__ == "__main__":
    s = summary()
    print(f"2I=SL(2,F5)=E8 order {s['order_2I']}; element-order spectrum {s['order_spectrum']}")
    print(f"metallic dynamics RL: order {s['RL_order']}, <RL> cyclic order {s['RL_cyclic_order']} (5-fold axis)")
    print(f"residual symmetry N(<RL>) order {s['normalizer_order']}  -> the dicyclic 2D5 (binary D5)")
    print(f"McKay sub-chain: 2I contains 2T=E6? {s['contains_2T_E6']}  | 2I contains 2O=E7? {s['contains_2O_E7']}")
    print("  => golden's finite shadow breaks E8 -> E6 DIRECTLY (skips E7: icosahedral has no octahedral subgroup)")
    assert s["order_2I"] == 120 and s["RL_order"] == 10 and s["normalizer_order"] == 20
    assert s["contains_2T_E6"] and not s["contains_2O_E7"]
    print("ALL CHECKS PASS")
