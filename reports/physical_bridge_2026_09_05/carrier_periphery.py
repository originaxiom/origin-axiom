"""R79 exact finite safeguards; no scientific work at import time."""
import itertools
import json

IDENTITY = ((1,), (2,))
C = (1, 2, -1, -2)
SIGMA = ((1, 2), (1,))
SIGMA_INV = ((2,), (-2, 1))
F0 = ((1, 2, 1), (2, 1))
B1303 = ((1, 1, 2), (1, 2))
GENERATORS = (
    (((2,), (1,)), ((2,), (1,))),
    (((-1,), (2,)), ((-1,), (2,))),
    (((1, 2), (2,)), ((1, -2), (2,))),
    (((1, -2), (2,)), ((1, 2), (2,))),
)


def reduce_word(word):
    out = []
    for letter in word:
        if abs(letter) not in (1, 2):
            raise ValueError("letter outside free rank-two alphabet")
        if out and out[-1] == -letter:
            out.pop()
        else:
            out.append(letter)
    return tuple(out)


def inverse(word):
    return tuple(-x for x in reversed(word))


def apply(mapping, word):
    return reduce_word(itertools.chain.from_iterable(
        mapping[x - 1] if x > 0 else inverse(mapping[-x - 1]) for x in word))


def compose(f, g):
    return tuple(apply(f, x) for x in g)


def commutator(a, b):
    return reduce_word(a + b + inverse(a) + inverse(b))


def inner(word):
    return tuple(reduce_word(word + (x,) + inverse(word)) for x in (1, 2))


def word_power(word, n):
    w = word if n >= 0 else inverse(word)
    return reduce_word(w * abs(n))


def cyclic_core(word):
    word = reduce_word(word)
    while len(word) > 1 and word[0] == -word[-1]:
        word = word[1:-1]
    return word


def conjugate(a, b):
    a, b = cyclic_core(a), cyclic_core(b)
    if len(a) != len(b):
        return False
    return not a or any(a == b[i:] + b[:i] for i in range(len(b)))


def homology(mapping):
    columns = [tuple(sum((1 if x > 0 else -1) for x in w if abs(x) == j)
                     for j in (1, 2)) for w in mapping]
    return (columns[0][0], columns[1][0], columns[0][1], columns[1][1])


def determinant(m):
    return m[0] * m[3] - m[1] * m[2]


def nielsen_sequences(depth=5):
    """Retain multiplicity; no claim of unique automorphism enumeration."""
    rows = []
    for length in range(depth + 1):
        for seq in itertools.product(range(len(GENERATORS)), repeat=length):
            f, fi = IDENTITY, IDENTITY
            for j in seq:
                g, gi = GENERATORS[j]
                f, fi = compose(g, f), compose(fi, gi)
            rows.append((seq, f, fi))
    return rows


def normalized_inverse():
    # F0 = Inner((aba)^-1) * sigma^2.
    return compose(compose(SIGMA_INV, SIGMA_INV), inner((1, 2, 1)))


def framed(k):
    return compose(inner(word_power(C, k)), F0)


def framed_inverse(k):
    return compose(normalized_inverse(), inner(word_power(C, -k)))


def shear(p, q, k):
    return (p + k * q, q)


I3 = (1, 0, 0, 1)
A3 = (0, 1, 2, 0)
B3 = (1, 1, 1, 2)


def mm(a, b, prime=3):
    return ((a[0]*b[0]+a[1]*b[2]) % prime,
            (a[0]*b[1]+a[1]*b[3]) % prime,
            (a[2]*b[0]+a[3]*b[2]) % prime,
            (a[2]*b[1]+a[3]*b[3]) % prime)


def mi(a, prime=3):
    if determinant(a) % prime != 1:
        raise ValueError("matrix must have determinant one")
    return (a[3] % prime, -a[1] % prime, -a[2] % prime, a[0] % prime)


def mp(a, n):
    if n < 0:
        return mp(mi(a), -n)
    r = I3
    for _ in range(n):
        r = mm(r, a)
    return r


def evaluate(word):
    r = I3
    for x in word:
        a = (A3, B3)[abs(x)-1]
        r = mm(r, a if x > 0 else mi(a))
    return r


def finite_transversals():
    target = tuple(evaluate(w) for w in F0)
    return [t for t in itertools.product(range(3), repeat=4)
            if determinant(t) % 3 == 1 and t != I3 and mp(t, 3) == I3
            and tuple(mm(mm(t, g), mi(t)) for g in (A3, B3)) == target]


def run_checks():
    rows = nielsen_sequences()
    det_counts = {-1: 0, 1: 0}
    for _, f, fi in rows:
        assert compose(f, fi) == compose(fi, f) == IDENTITY
        d = determinant(homology(f))
        assert d in det_counts
        det_counts[d] += 1
        assert conjugate(apply(f, C), C if d == 1 else inverse(C))
    psi = ((1,), reduce_word((2,) + C))
    double_a = ((1, 1), (2,))
    assert homology(psi) == homology(IDENTITY)
    assert not any(conjugate(apply(psi, C), w) for w in (C, inverse(C)))
    assert determinant(homology(double_a)) == 2
    assert not any(conjugate(apply(double_a, C), w) for w in (C, inverse(C)))
    assert compose(SIGMA, SIGMA_INV) == compose(SIGMA_INV, SIGMA) == IDENTITY
    sigma2 = compose(SIGMA, SIGMA)
    assert apply(SIGMA, C) == reduce_word((1,) + inverse(C) + (-1,))
    assert sigma2 == ((1, 2, 1), (1, 2))
    assert apply(sigma2, C) == reduce_word((1, 2, 1) + C + (-1, -2, -1))
    assert compose(inner((-1, -2, -1)), sigma2) == F0
    assert compose(inner((-1,)), B1303) == F0
    assert compose(inner((1, 2)), B1303) == sigma2
    assert homology(F0) == (2, 1, 1, 1) and apply(F0, C) == C
    slopes = 0
    for k in range(-3, 4):
        f, fi = framed(k), framed_inverse(k)
        assert compose(f, fi) == compose(fi, f) == IDENTITY
        assert apply(f, C) == C and homology(f) == homology(F0)
        for j in (1, 2):
            assert apply(f, (j,)) == reduce_word(
                word_power(C, k) + apply(F0, (j,)) + word_power(C, -k))
        for p, q in itertools.product(range(-3, 4), repeat=2):
            assert shear(*shear(p, q, k), -k) == (p, q)
            assert reduce_word(word_power(C, p) + word_power(C, k*q)) == word_power(C, p+k*q)
            slopes += 1
    assert shear(1, 3, 1) == (4, 3) and shear(1, 3, 0) != shear(1, 3, 1)
    ts = finite_transversals()
    assert ts, "declared finite group comparator has no order-three transversal"
    t = ts[0]
    cm = evaluate(C)
    assert cm != I3 and mm(cm, t) == mm(t, cm)
    for k in range(-3, 4):
        tk = mm(mp(cm, k), t)
        assert tuple(mm(mm(tk, g), mi(tk)) for g in (A3, B3)) == tuple(evaluate(w) for w in framed(k))
        for p, q in itertools.product(range(-3, 4), repeat=2):
            assert mm(mp(cm, p), mp(tk, q)) == mm(mp(cm, p+k*q), mp(t, q))
    slope0 = mm(cm, mp(t, 3))
    t1 = mm(cm, t)
    slope1 = mm(cm, mp(t1, 3))
    transported = mm(mp(cm, 4), mp(t, 3))
    assert slope0 != I3 and slope1 == transported == I3
    # Scalar target F7^*: commutators vanish, including nontrivial base holonomy.
    scalar_checks = 0
    for a, b, base, k in itertools.product(range(1, 7), range(1, 7), range(1, 7), range(-3, 4)):
        comm = (a*b*pow(a, -1, 7)*pow(b, -1, 7)) % 7
        assert comm == 1
        assert pow(comm, k, 7)*base % 7 == base
        scalar_checks += 1
    return {"nielsen_sequences_length_0_to_5": len(rows), "determinant_counts": det_counts,
            "opposite_endomorphism_homology": homology(psi),
            "opposite_commutator_cyclic_length": len(cyclic_core(apply(psi, C))),
            "normalized_golden_images": F0, "framed_k_min_max": [-3, 3],
            "slope_integer_controls": slopes, "abelian_blind_controls": scalar_checks,
            "all_order_three_transversals_SL2F3": ts, "selected_T": t,
            "rho_commutator": cm, "rho_slope_1_3_frame0": slope0,
            "rho_slope_1_3_frame1": slope1, "rho_transported_slope_4_3_frame0": transported,
            "verdict": "PASS", "scope": "exact finite safeguards; authored universal deductions separately scoped"}


if __name__ == "__main__":
    print(json.dumps(run_checks(), sort_keys=True, indent=2))
