#!/usr/bin/env python3
"""R022: exact finite audit of the three proposed V4 presentations.

This is deliberately self-contained.  It uses only tuples, strings, and integer
arithmetic; no repository-relative imports or current-working-directory
assumptions are made.
"""

from itertools import product


V4 = ((0, 0), (1, 0), (0, 1), (1, 1))
IDENTITY = (0, 0)


def add(a, b):
    return (a[0] ^ b[0], a[1] ^ b[1])


def quadratic_discriminant(squarefree_d):
    return squarefree_d if squarefree_d % 4 == 1 else 4 * squarefree_d


def prime_support(n):
    n = abs(n); out = set(); p = 2
    while p * p <= n:
        if n % p == 0:
            out.add(p)
            while n % p == 0: n //= p
        p += 1
    if n > 1: out.add(n)
    return out


def action_table(labels, generators):
    """Return (name, image labels, fixed count, cycle lengths)."""
    pos = {x: i for i, x in enumerate(labels)}
    rows = []
    for name, g in generators:
        image = tuple(labels[pos[add(x, g)]] for x in labels)
        fixed = sum(a == b for a, b in zip(labels, image))
        seen = set()
        cycles = []
        for i in range(len(labels)):
            if i in seen:
                continue
            j, n = i, 0
            while j not in seen:
                seen.add(j)
                j = pos[add(labels[j], g)]
                n += 1
            cycles.append(n)
        rows.append((name, image, fixed, tuple(sorted(cycles))))
    return rows


def regular_character_table(generator_names):
    cols = (IDENTITY,) + tuple(generator_names) + (add(generator_names[0], generator_names[1]),)
    names = ("1", "chi_1", "chi_2", "chi_12")
    out = []
    for i, name in enumerate(names):
        values = []
        for g in cols:
            if i == 0:
                values.append(1)
            elif i == 1:
                values.append(1 if g[0] == 0 else -1)
            elif i == 2:
                values.append(1 if g[1] == 0 else -1)
            else:
                values.append(1 if (g[0] ^ g[1]) == 0 else -1)
        out.append((name, tuple(values)))
    return cols, tuple(out)


def print_regular(name, labels, generators, display=None):
    if display is None:
        display = {x: str(x) for x in labels}
    print("[%s]" % name)
    print(" labels:", tuple(display[x] for x in labels))
    all_generators = (("1", IDENTITY),) + tuple(generators)
    for n, image, fixed, cycles in action_table(labels, all_generators):
        pairs = []
        done = set()
        for i, j in enumerate(image):
            if i in done:
                continue
            k = labels.index(j)
            done.update((i, k))
            if i == k:
                pairs.append("(%s)" % display[labels[i]])
            else:
                pairs.append("(%s %s)" % (display[labels[i]], display[labels[k]]))
        print(" %s: %s fixed=%d cycles=%s" % (n, "".join(pairs), fixed, cycles))
    cols, chars = regular_character_table(tuple(g for _, g in generators))
    print(" character columns:", cols)
    for n, values in chars:
        print(" %s: %s" % (n, values))
    assert all(row[2] == (4 if row[0] == "1" else 0) for row in action_table(labels, (("1", IDENTITY),) + generators))
    return chars


def signs_to_bits(signs):
    return tuple(0 if x == 1 else 1 for x in signs)


def xor_signs(a, b):
    return tuple(x * y for x, y in zip(a, b))


def b1024_coordinate(chi, chi_plus):
    """H1 coordinate of H(sigma_chi o tau): fixed nodes 1 and 3."""
    coordinate = xor_signs(chi, chi_plus)
    bits = signs_to_bits(coordinate)
    return (bits[1], bits[3])


def audit_b1024():
    print("[B1024 measurement/frame carrier]")
    # tau fixes node pairs (0,5), (2,4), and nodes 1,3.  X^tau therefore has
    # 2^4 = 16 cocycles, represented by invariant sign vectors.
    cocycles = []
    for a, b, c, d in product((1, -1), repeat=4):
        # Six Bourbaki-node signs: tau pairs 0<->5 and 2<->4, while
        # 1 and 3 are fixed.  Hence (a,b,c,d,c,a), not a seven-slot
        # palindromic surrogate.
        cocycles.append((a, b, c, d, c, a))
    assert len(cocycles) == 16 and len(set(cocycles)) == 16
    assert all(len(x) == 6 for x in cocycles)
    tau = (5, 1, 4, 3, 2, 0)
    assert all(tuple(x[tau[i]] for i in range(6)) == x for x in cocycles)
    classes = {(signs_to_bits(x)[1], signs_to_bits(x)[3]) for x in cocycles}
    assert classes == set(V4)
    counts = {k: sum((signs_to_bits(x)[1], signs_to_bits(x)[3]) == k for x in cocycles) for k in V4}
    print(" X^tau cocycles:", len(cocycles), "(a 16-point torsor under X^tau)")
    print(" H1 quotient coordinates (fixed Bourbaki nodes alpha_2,alpha_4):", sorted(classes))
    print(" class multiplicities:", counts)
    assert counts == {k: 4 for k in V4}

    # B936/B1024 source-locked annotations, retained as labels rather than
    # presented as a fresh derivation in this finite-action certificate.
    class_types = {(0, 0): (36, "C4"), (1, 0): (36, "C4"),
                   (0, 1): (36, "C4"), (1, 1): (52, "F4")}
    for k in sorted(V4):
        print(" class %s: fixed-dimension/type=%s/%s" % (k, class_types[k][0], class_types[k][1]))

    chi_plus = (1, -1, 1, -1, 1, 1)
    chi_c = (1, -1, -1, 1, -1, 1)
    all_plus = (1, 1, 1, 1, 1, 1)
    direct_c = (signs_to_bits(chi_c)[1], signs_to_bits(chi_c)[3])
    structure_c = b1024_coordinate(chi_c, chi_plus)
    reversal = b1024_coordinate(all_plus, chi_plus)
    print(" primary direct-inner convention: chi_c=%s -> c=%s" % (chi_c, direct_c))
    print(" structure-coordinate convention: chi_c*chi_plus -> c=%s" % (structure_c,))
    print(" reversal bare tau-lift chi=1 -> r=%s" % (reversal,))
    assert direct_c == (1, 0)
    assert structure_c == (0, 1)
    assert reversal == (1, 1)
    print(" coordinate-transposition fence: the two conventions swap the first two H1 axes; span is all four classes")

    # The H1 quotient is the only four-point V4 object obtainable from B1024.
    # Keep both source conventions visible: either is a regular action.
    qlabels = V4
    qdisplay = { (0, 0): "00", (1, 0): "10", (0, 1): "01", (1, 1): "11" }
    primary = (("c", (1, 0)), ("r", (1, 1)))
    corrected = (("c", (0, 1)), ("r", (1, 1)))
    print_regular("H1 quotient / primary labels", qlabels, primary, qdisplay)
    print_regular("H1 quotient / structure-coordinate labels", qlabels, corrected, qdisplay)
    return cocycles


def audit_b766():
    print("[B766 measurement distinction]")
    closings = tuple(product((0, 1), repeat=3))
    display = tuple("closing-%03d" % (4*x[0] + 2*x[1] + x[2]) for x in closings)
    print(" actual B766 closing set:", display)
    print(" structure group: (Z/2)^3, not V4; B782 verifies free transitive action on 8 points")
    assert len(closings) == 8
    fixed_counts = {}
    for g in product((0, 1), repeat=3):
        image = tuple(tuple(x[i] ^ g[i] for i in range(3)) for x in closings)
        assert set(image) == set(closings)
        fixed_counts[g] = sum(x == y for x, y in zip(closings, image))
    assert fixed_counts[(0, 0, 0)] == 8
    assert all(fixed_counts[g] == 0 for g in fixed_counts if g != (0, 0, 0))
    print(" fixed counts: identity=8; each of 7 nonidentity elements=0")


def main():
    print("R022 V4 NAMED-ACTION AUDIT")
    print("exact finite certificate; all arithmetic is tuple/integer arithmetic")
    print()

    branch_labels = V4
    branch_display = {(0, 0): "B00", (1, 0): "B10", (0, 1): "B01", (1, 1): "B11"}
    print_regular("branch-selection (B1161; labels are audit coordinates only)", branch_labels,
                  (("u", (1, 0)), ("v", (0, 1))), branch_display)
    branch_quadratic_discs = tuple(quadratic_discriminant(d) for d in (-1, 3, -3))
    branch_disc = abs(branch_quadratic_discs[0] * branch_quadratic_discs[1] * branch_quadratic_discs[2])
    branch_ram = prime_support(branch_disc)
    assert branch_quadratic_discs == (-4, 12, -3) and branch_disc == 144 and branch_ram == {2, 3}
    print(" branch field: Q(zeta_12)=Q(i,sqrt(3)); quadratic subfields={Q(i),Q(sqrt(3)),Q(sqrt(-3))}")
    print(" branch discriminant=144=2^4*3^2; ramified primes={2,3}")
    print(" source-label fence: B1161 commits the free orbit but no canonical B00/B10/B01/B11 branch table")
    print()

    bh_labels = V4
    bh_display = {(0, 0): "(b+,h+)", (1, 0): "(b-,h+)",
                  (0, 1): "(b+,h-)", (1, 1): "(b-,h-)"}
    print_regular("being-by-hearing product", bh_labels,
                  (("being-c", (1, 0)), ("hearing-c", (0, 1))), bh_display)
    print(" b+= (3+sqrt(-3))/2, b-= (3-sqrt(-3))/2; field=Q(sqrt(-3))")
    print(" h+=phi, h-=-1/phi (equivalently Fibonacci/Yang-Lee); field=Q(sqrt(5))")
    bh_quadratic_discs = tuple(quadratic_discriminant(d) for d in (-3, 5, -15))
    bh_disc = abs(bh_quadratic_discs[0] * bh_quadratic_discs[1] * bh_quadratic_discs[2])
    bh_ram = prime_support(bh_disc)
    assert bh_quadratic_discs == (-3, 5, -15) and bh_disc == 225 and bh_ram == {3, 5}
    print(" compositum=Q(sqrt(-3),sqrt(5)); quadratic subfields={Q(sqrt(-3)),Q(sqrt(5)),Q(sqrt(-15))}")
    print(" compositum discriminant=225=3^2*5^2; ramified primes={3,5}")
    print()

    audit_b1024()
    print()
    audit_b766()
    print()

    # Exact field-label separator: a quadratic subfield of a cyclotomic field
    # can only ramify at primes ramifying in the ambient field.
    bh_hearing_ram = {5}
    print("[field-label separator]")
    print(" ram(Q(zeta_12))=", sorted(branch_ram), "; ram(Q(sqrt(5)))=", sorted(bh_hearing_ram))
    assert 5 not in branch_ram
    print(" sqrt(5) is not a subfield of Q(zeta_12): 5 is unramified in discriminant 144")
    print(" named branch second leg sqrt(3) != named hearing second leg sqrt(5)")
    print()

    print("[verdict]")
    print(" abstract four-point regular V4 actions: EQUIVARIANTLY ISOMORPHIC")
    print(" with field labels retained: branch-selection vs being-by-hearing are NOT label-preserving")
    print(" full three-way claim: ILL-TYPED/OPEN until branch labels and the measurement carrier are frozen")
    print(" minimal falsifier: a label-preserving map must preserve the field/Dynkin-label annotations;")
    print("                 ramification {2,3} vs hearing's {5} already separates the first two")


if __name__ == "__main__":
    main()
