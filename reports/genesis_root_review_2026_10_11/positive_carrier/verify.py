"""Exact safeguards for the elementary positive-carrier proof; no dependencies."""
from itertools import product


def add(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def shift(p, e, sign=1):
    return {(i + e[0], j + e[1]): sign * c for (i, j), c in p.items()}


def pmul(p, q):
    out = {}
    for e, c in q.items():
        out = add(out, shift(p, e, c))
    return out


def mul(g, h):
    e, p, q = g
    f, r, s = h
    return ((e[0] + f[0], e[1] + f[1]),
            add(p, shift(r, e)), add(q, shift(s, e)))


def inverse(g):
    e, p, q = g
    neg = (-e[0], -e[1])
    return neg, shift(p, neg, -1), shift(q, neg, -1)


ID = ((0, 0), {}, {})
ONE = {(0, 0): 1}
GEN = {'a': ((1, 0), ONE, {}), 'b': ((0, 1), {}, ONE)}
GEN.update({'A': inverse(GEN['a']), 'B': inverse(GEN['b'])})


def evaluate(word):
    value = ID
    for letter in word:
        value = mul(value, GEN[letter])
    return value


def walk(word):
    """Independent edge accumulation, without the affine product routine."""
    x = y = 0
    p, q = {}, {}
    for c in word:
        if c in 'aA':
            if c == 'A':
                x -= 1
            p[x, y] = p.get((x, y), 0) + (1 if c == 'a' else -1)
            if c == 'a':
                x += 1
        else:
            if c == 'B':
                y -= 1
            q[x, y] = q.get((x, y), 0) + (1 if c == 'b' else -1)
            if c == 'b':
                y += 1
    return ((x, y), {e: c for e, c in p.items() if c},
            {e: c for e, c in q.items() if c})


def reduce_word(word):
    stack = []
    for c in word:
        if stack and stack[-1] == c.swapcase():
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


def invword(word):
    return word[::-1].swapcase()


def comm(u, v):
    return u + v + invword(u) + invword(v)


def words(alphabet, depth, reduced=False):
    for n in range(depth + 1):
        for letters in product(alphabet, repeat=n):
            w = ''.join(letters)
            if not reduced or reduce_word(w) == w:
                yield w


def key(g):
    return g[0], tuple(sorted(g[1].items())), tuple(sorted(g[2].items()))


def decode(g):
    endpoint, p, q = g
    events = {}
    for letter, poly in [('a', p), ('b', q)]:
        for e, coefficient in poly.items():
            t = sum(e)
            if coefficient != 1 or min(e) < 0 or t in events:
                raise ValueError('not a positive path')
            events[t] = (letter, e)
    x = y = 0
    result = []
    if set(events) != set(range(len(events))):
        raise ValueError('missing time')
    for t in range(len(events)):
        letter, e = events[t]
        if e != (x, y):
            raise ValueError('disconnected path')
        result.append(letter)
        x += letter == 'a'
        y += letter == 'b'
    if endpoint != (x, y):
        raise ValueError('wrong endpoint')
    return ''.join(result)


def substitute(word, f):
    table = {'a': f[0], 'b': f[1],
             'A': invword(f[0]), 'B': invword(f[1])}
    return reduce_word(''.join(table[c] for c in word))


def semilinear(g, f):
    ea, pa, qa = evaluate(f[0])
    eb, pb, qb = evaluate(f[1])

    def exponent(e):
        return (e[0] * ea[0] + e[1] * eb[0],
                e[0] * ea[1] + e[1] * eb[1])

    def ring(poly):
        out = {}
        for e, c in poly.items():
            new = exponent(e)
            out[new] = out.get(new, 0) + c
        return {e: c for e, c in out.items() if c}

    e, p, q = g
    sp, sq = ring(p), ring(q)
    return (exponent(e), add(pmul(pa, sp), pmul(pb, sq)),
            add(pmul(qa, sp), pmul(qb, sq)))


SUBSTITUTIONS = (
    ('sigma', ('ab', 'a')),
    ('sigma_inverse', ('b', 'Ba')),
    ('left', ('a', 'ab')),
    ('right', ('ab', 'b')),
    ('swap', ('b', 'a')),
    ('invert_a', ('A', 'b')),
    ('collapse', ('a', 'a')),
    ('commutators', ('abAB', 'abbABB')),
    ('inner_a', ('a', 'abA')),
)


def main():
    checks = 0

    def check(condition, message):
        nonlocal checks
        checks += 1
        assert condition, message

    signed = list(words('abAB', 5, reduced=True))
    for w in signed:
        check(evaluate(w) == walk(w), ('walk', w))
    for w in words('abAB', 3):
        check(evaluate(w) == evaluate(reduce_word(w)) == walk(w), ('cancel', w))
    positive = list(words('ab', 10))
    encodings = set()
    for w in positive:
        value = evaluate(w)
        check(decode(value) == w, ('decode', w))
        check(key(value) not in encodings, ('collision', w))
        encodings.add(key(value))
    check(evaluate('ab')[0] == evaluate('ba')[0], 'abelian comparator')
    check(evaluate('ab') != evaluate('ba'), 'order retained')
    c = comm('a', 'b')
    k = comm(c, comm('a', 'bb'))
    reduced_k = reduce_word(k)
    check(reduced_k == 'abABabbABaBAbbaBBA', 'explicit free kernel witness')
    check(len(reduced_k) == 18 and evaluate(k) == ID == walk(k), 'proper quotient')
    check(evaluate(c) == ((0, 0), {(0, 0): 1, (0, 1): -1},
                         {(1, 0): 1, (0, 0): -1}) != ID, 'first commutator')
    try:
        decode(evaluate(c))
    except ValueError:
        check(True, 'negative decoder control')
    else:
        check(False, 'decoder accepted signed loop')
    small = list(words('abAB', 2, reduced=True))
    for u in small:
        g = evaluate(u)
        check(mul(g, inverse(g)) == mul(inverse(g), g) == ID, ('inverse', u))
        for v in small:
            h = evaluate(v)
            check(mul(g, h) == walk(u + v), ('product', u, v))
            for t in GEN.values():
                check(mul(mul(g, h), t) == mul(g, mul(h, t)), 'associativity')
    window = list(words('abAB', 4, reduced=True))
    for name, f in SUBSTITUTIONS:
        for w in window:
            check(semilinear(evaluate(w), f) == evaluate(substitute(w, f)),
                  ('descent', name, w))
        check(evaluate(substitute(k, f)) == ID, ('kernel', name))
    sigma, tau = SUBSTITUTIONS[0][1], SUBSTITUTIONS[1][1]
    for w in window:
        for f, h in [(sigma, tau), (tau, sigma)]:
            check(substitute(substitute(w, h), f) == w, ('free inverse', w))
            check(semilinear(semilinear(evaluate(w), h), f) == evaluate(w),
                  ('quotient inverse', w))
    print('PASS:', checks, 'exact assertions')
    print('Freely reduced signed words through length five:', len(signed))
    print('Positive words through length ten including empty:', len(positive))
    print('Substitution fixtures:', len(SUBSTITUTIONS), 'on', len(window), 'signed words each')
    print('Nontrivial free kernel witness:', reduced_k)
    print('All-length claims rely on PROOF.md, not finite enumeration.')


if __name__ == '__main__':
    main()
