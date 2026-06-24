"""B206 -- the golden object's spin/congruence shadow is 2I = SL(2,F_5) = McKay-E_8 (self-contained).

INSIGHT: the four faces of the metallic object are shadows of the conjugacy class R^m L^m in SL(2,Z);
its ARITHMETIC shadow mod the field discriminant is a finite group. For the golden mean (m=1, field
Q(sqrt5), disc 5) that group is SL(2,F_5) = the binary icosahedral group 2I = the McKay partner of
affine E_8. The classical/trace level is PSL(2,F_5)=A_5 (5 irreps); the quantum/spin level is
SL(2,F_5)=2I (9 irreps); the Z/2 between them is the center {+-I} = the spin cover SU(2)->SO(3) = the
half-trace (kappa=4I+2). The 4 extra spinorial irreps {2,2,4,6} are what the quantum level sees that the
classical level cannot. GOLDEN-SPECIFIC: SL(2,F_p) is binary-polyhedral (McKay/ADE) only for p<=5, and
among metallic discriminants m^2+4 the squarefree field is 5 only for the Q(sqrt5) family (m=1,4).

Ingredients are STANDARD (2I=SL(2,F5), A5=PSL(2,F5), McKay 2I<->E_8, congruence quotients, spin cover);
the contribution is the assembly. FIREWALL: this is the McKay/representation-theoretic E_8 (the Dynkin/
character graph of 2I), NOT a claim that physics' E_8 gauge group emerges. Nothing to CLAIMS.md.
"""
from itertools import product


def sl2_Fp(p):
    return [(a, b, c, d) for a, b, c, d in product(range(p), repeat=4) if (a*d - b*c) % p == 1]


def mul(x, y, p):
    a, b, c, d = x; e, f, g, h = y
    return ((a*e + b*g) % p, (a*f + b*h) % p, (c*e + d*g) % p, (c*f + d*h) % p)


def inv(x, p):
    a, b, c, d = x  # det 1
    return (d % p, (-b) % p, (-c) % p, a % p)


def conj_classes(G, p):
    seen, classes = set(), []
    for x in G:
        if x in seen:
            continue
        cls = {mul(mul(g, x, p), inv(g, p), p) for g in G}
        seen |= cls
        classes.append(cls)
    return classes


def order_of(x, p, cap=200):
    e, cur = (1, 0, 0, 1), x
    for k in range(1, cap):
        if cur == e:
            return k
        cur = mul(cur, x, p)
    return None


def sqfree(n):
    o, f = 1, 2
    while f*f <= n:
        c = 0
        while n % f == 0:
            n //= f; c += 1
        if c % 2:
            o *= f
        f += 1
    return o*n


# known McKay data (verified by sum-of-squares against the group orders below)
DIMS_2I = [1, 2, 2, 3, 3, 4, 4, 5, 6]   # affine E_8 marks
DIMS_A5 = [1, 3, 3, 4, 5]
DIMS_SPIN = [2, 2, 4, 6]                 # the 4 spinorial irreps (2I minus A5)


def summary():
    p = 5
    G = sl2_Fp(p)
    center = [x for x in G if all(mul(x, g, p) == mul(g, x, p) for g in G)]
    cc = conj_classes(G, p)
    negI = (p-1, 0, 0, p-1)
    psl = {frozenset({x, mul(negI, x, p)}) for x in G}
    psl_cc = {frozenset(frozenset({x, mul(negI, x, p)}) for x in c) for c in cc}
    return {
        "|SL(2,F5)|": len(G), "|center|": len(center), "#cc_SL": len(cc),
        "|PSL(2,F5)|": len(psl), "#cc_PSL": len(psl_cc),
        "RL_mod5_order": order_of((2, 1, 1, 1), 5),
        "sumsq_2I": sum(d*d for d in DIMS_2I), "sumsq_A5": sum(d*d for d in DIMS_A5),
        "n_spinorial": len(DIMS_2I) - len(DIMS_A5),
        "golden_fields": [(m, m*m+4, sqfree(m*m+4)) for m in range(1, 9)],
    }


if __name__ == "__main__":
    s = summary()
    print(f"SL(2,F5): order {s['|SL(2,F5)|']} (=|2I|), center {s['|center|']} (spin Z/2),"
          f" {s['#cc_SL']} conj classes (=#irreps=affine-E8 nodes)")
    print(f"PSL(2,F5)=A5: order {s['|PSL(2,F5)|']}, {s['#cc_PSL']} conj classes (=#irreps)")
    print(f"=> quantum/spin level has {s['#cc_SL']}-{s['#cc_PSL']}={s['n_spinorial']} EXTRA spinorial irreps {DIMS_SPIN}")
    print(f"2I irrep dims {DIMS_2I}: sum sq {s['sumsq_2I']} (=120, the affine E8 marks)")
    print(f"A5 irrep dims {DIMS_A5}: sum sq {s['sumsq_A5']} (=60)")
    print(f"golden monodromy RL mod 5 order: {s['RL_mod5_order']}")
    print("golden-specificity (m, m^2+4, squarefree field): 5 => 2I=E8")
    for m, D, sf in s["golden_fields"]:
        print(f"   m={m}: m^2+4={D:>3} field sqrt{sf}" + ("  <- 2I=SL(2,F5)=McKay-E8" if sf == 5 else ""))
    assert s["|SL(2,F5)|"] == 120 and s["#cc_SL"] == 9 and s["|center|"] == 2
    assert s["|PSL(2,F5)|"] == 60 and s["#cc_PSL"] == 5
    assert s["sumsq_2I"] == 120 and s["sumsq_A5"] == 60 and s["n_spinorial"] == 4
    print("\nALL CHECKS PASS")
