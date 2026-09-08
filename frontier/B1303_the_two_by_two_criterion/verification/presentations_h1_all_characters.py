"""Compare h^1(Y_n; psi) over ALL characters of H_1(Y_n) for three presentations of pi_1(Y_n):
 (i)  <a,b | phi^n(x) = x>                      phi: a->a^2 b, b->a b        (B1303's)
 (ii) <a,b | phi'^n(x) = x>, phi' = c_{a^-1} phi (fixes the boundary commutator [a,b])
 (iii)<a,b | h^{2n}(x) = x>, h: a->ab, b->a     (the half-deck automorphism; h^2 = c_{ab} phi)
Exact Fox calculus over F_q (q = 1 mod m) for the character psi(a) = z^p, psi(b) = z^q0, z a primitive m-th root.
h^1 = 1 - rank(J(psi)) for a nontrivial character (deficiency-zero presentation of a closed 3-manifold group).
Characters of H_1(Y_n) = Z^2/(M^n - I): (p, q0) in (Z/m)^2 with (M^n - I)^T-compatibility: psi trivial on (M^n - I) Z^2."""
import sys, itertools
from sympy import isprime, primitive_root

def word_apply(auto, w):
    # auto: dict letter -> word (list of (letter, +-1)); apply to word w
    out = []
    for (g, e) in w:
        img = auto[g] if e == 1 else [(h, -f) for (h, f) in reversed(auto[g])]
        out += img
    return reduce_word(out)

def reduce_word(w):
    out = []
    for x in w:
        if out and out[-1][0] == x[0] and out[-1][1] == -x[1]:
            out.pop()
        else:
            out.append(x)
    return out

def power(auto, k):
    cur = {'a': [('a', 1)], 'b': [('b', 1)]}
    for _ in range(k):
        cur = {g: word_apply(auto, cur[g]) for g in 'ab'}
    return cur

def fox(w, y, val, q):
    """(d w / d y)^psi over F_q; val: letter -> psi(letter) in F_q. Left convention d(uv) = du + psi(u) dv."""
    tot = 0; pref = 1
    for (g, e) in w:
        if g == y:
            if e == 1:
                tot = (tot + pref) % q
            else:
                # d(g^-1) = -g^-1
                tot = (tot - pref * pow(val[g], q - 2, q)) % q
        pref = pref * (val[g] if e == 1 else pow(val[g], q - 2, q)) % q
    return tot

def psi_word(w, val, q):
    r = 1
    for (g, e) in w:
        r = r * (val[g] if e == 1 else pow(val[g], q - 2, q)) % q
    return r

def h1_of_presentation(rels, val, q):
    # rels: list of two words r with psi(r) = 1; J_{r,y} = fox(r, y); h1 = 1 - rank J  (2x2 over F_q)
    J = [[fox(r, y, val, q) for y in 'ab'] for r in rels]
    # rank
    if all(x == 0 for row in J for x in row):
        return 1
    det = (J[0][0] * J[1][1] - J[0][1] * J[1][0]) % q
    return 1 - (2 if det else 1)

def relators(auto_pow):
    # r_x = auto^n(x) x^-1
    return [reduce_word(auto_pow[g] + [(g, -1)]) for g in 'ab']

def conj(auto, g):
    # c_g o auto : x -> g auto(x) g^-1
    return {x: reduce_word(g + auto[x] + [(h, -e) for (h, e) in reversed(g)]) for x in 'ab'}

def main(n):
    phi = {'a': [('a', 1), ('a', 1), ('b', 1)], 'b': [('a', 1), ('b', 1)]}
    phip = conj(phi, [('a', -1)])
    h = {'a': [('a', 1), ('b', 1)], 'b': [('a', 1)]}
    # sanity: phi' fixes c = [a,b]
    c = [('a', 1), ('b', 1), ('a', -1), ('b', -1)]
    assert word_apply(phip, c) == c
    P = {'i': power(phi, n), 'ii': power(phip, n), 'iii': power(h, 2 * n)}
    R = {k: relators(v) for k, v in P.items()}
    # H_1 = Z^2/(M^n - I) with M = [[2,1],[1,1]]  (a -> (1,0), b -> (0,1)); characters: (p, q0) with psi((M^n-I)e_j) = 1
    from sympy import Matrix
    M = Matrix([[2, 1], [1, 1]]); K = M ** n - Matrix.eye(2)
    from sympy.matrices.normalforms import smith_normal_form
    from sympy import ZZ
    S = smith_normal_form(K, domain=ZZ)
    tors = [abs(int(S[i, i])) for i in range(2)]
    m = max(tors)
    # two large primes q = 1 mod m (a rank read modulo one small prime can vanish accidentally: a first run with q ~ 60
    # over-counted Y_7 by 28 and Y_9 by 36); a character is counted only if both primes agree, and disagreement is reported
    qs = []
    qq = m * (10 ** 9 // m) + 1
    while len(qs) < 2:
        if isprime(qq) and (qq - 1) % m == 0:
            qs.append(qq)
        qq += m
    zs = [pow(primitive_root(q_), (q_ - 1) // m, q_) for q_ in qs]
    # enumerate characters: psi(a) = z^p, psi(b) = z^q0 such that psi kills columns of K: K[0,j] p + K[1,j] q0 = 0 mod m for j=0,1
    counts = {k: 0 for k in R}; agree = True; nchar = 0
    disagreements = []
    for p in range(m):
        for q0 in range(m):
            if (p, q0) == (0, 0):
                continue
            if any((int(K[0, j]) * p + int(K[1, j]) * q0) % m for j in range(2)):
                continue
            nchar += 1
            res = {}
            for k, rels in R.items():
                vals = []
                for qq, z in zip(qs, zs):
                    val = {'a': pow(z, p, qq), 'b': pow(z, q0, qq)}
                    for r in rels:
                        assert psi_word(r, val, qq) == 1, (k, p, q0)
                    vals.append(h1_of_presentation(rels, val, qq))
                assert vals[0] == vals[1], ("the two primes disagree", k, p, q0, vals)
                res[k] = vals[0]
                counts[k] += res[k]
            if len(set(res.values())) > 1:
                agree = False; disagreements.append(((p, q0), res))
    print(f"n = {n}: H_1 torsion {tors}, {nchar} nontrivial characters, primes {qs}; h1 = 1 counts per presentation: {counts}; all three agree on every character: {agree}")
    for d in disagreements[:6]:
        print("   disagree:", d)

if __name__ == "__main__":
    for n in [int(x) for x in sys.argv[1:]] or [2, 3, 4, 5, 6, 7]:
        main(n)
