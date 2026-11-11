"""
W-C3, item W110 (arc B1682): the word side of the record count, computed by this seat's own route.

SOURCE OF THE DEFINITIONS.  The SM seat's W110_PROOF.md as main received it (B1682's verification/received/), read
through the mask.  Neither the seat's script nor main's checking script is run or opened.  F_n is free on a1 ... an;
R_ij is a_i -> a_i a_j, L_ij is a_i -> a_j a_i, other letters fixed.  A class is a cyclic word (cyclically reduced, up
to rotation); ||v|| is the length of the cyclic reduction of v.  A move keeps the class of w when phi(w) is conjugate
to w, and keeps it up to inversion when phi(w) is conjugate to w or to w^-1.  At n = 2 the record's moves are
R: a -> ab and L: b -> ab.  The full moves add the inversions a_i -> a_i^-1 and the transpositions of the letters.

WHAT IS COMPUTED, AND WHAT WOULD COUNT AS NOT REPRODUCING (written before the run)
  C1  Whitehead's count, by direct reduction, on every class of the census below: ||R_ij(w)|| = m + n_i - 2 c_ij and
      ||R_ij^-1(w)|| = m + n_i - 2 c'_ij (n_i the number of letters a_i^{+-1}; c_ij the cyclically adjacent pairs
      a_i a_j^-1 or a_j a_i^-1; c'_ij the pairs a_i a_j or a_j^-1 a_i^-1).  One failure is NOT REPRODUCED.
  C2  n = 3 to length 8, n = 4 to length 7, n = 5 to length 6: the classes whose length is kept by every R_ij^{+-1};
      the classes kept by every transvection (R_ij^{+-1} and L_ij^{+-1}), and by the full moves, exactly and up to
      inversion.  Every count 0.  One non-trivial class in any count is NOT REPRODUCED.
  C3  n = 2 to length 12: the classes kept by R and L, by the four transvections (R_12, R_21, L_12, L_21) and by the
      full moves, exactly and up to inversion.  Kept by R and L, and by the four transvections, exactly: the classes
      of [a, b]^k, k = +-1, +-2, +-3 (six classes; three up to inversion).  The full moves keep these three up to
      inversion and keep no class exactly.  Anything else is NOT REPRODUCED.
  C4  the singular points of the level surface x^2 + y^2 + z^2 - xyz - 2 = -2: only (0, 0, 0) (sympy).
  REPORTED  the number of classes of F_2 to length 12 (the seat's exploratory note had 25 654; which classes it
      counted is not stated, so this is not a test).

CONTROLS (must come out as stated, or the code is broken)
  K1  at n = 2, [a, b] is kept by R and L, and aab is not.
  K2  the census's class counts at each length match the number of cyclically reduced cyclic words computed a second
      way (by Burnside over rotations of the cyclically reduced words).

DISCLOSED.  The seat's statements are known to this seat; this is a check, not a blind test.
"""
import itertools
import json
import sys


def reduce_word(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def cyc_reduce(w):
    w = reduce_word(w)
    while len(w) >= 2 and w[0] == -w[-1]:
        w = w[1:-1]
    return w


def canon(w):
    if not w:
        return ()
    m = len(w)
    return min(tuple(w[i:] + w[:i]) for i in range(m))


def inverse(w):
    return [-x for x in reversed(w)]


def classes(n, maxlen):
    letters = [i for i in range(1, n + 1)] + [-i for i in range(1, n + 1)]
    out = {}
    for m in range(1, maxlen + 1):
        res = []
        stack = [[x] for x in letters]
        while stack:
            w = stack.pop()
            if len(w) == m:
                if w[0] != -w[-1] and tuple(w) == canon(w):
                    res.append(tuple(w))
                continue
            for x in letters:
                if x != -w[-1]:
                    stack.append(w + [x])
        out[m] = res
    return out


def burnside_count(n, m):
    """Cyclic words of length m in F_n (cyclically reduced, up to rotation), counted by Burnside: the average over the
    m rotations of the number of cyclically reduced words fixed by the rotation.  A word fixed by the rotation by r is
    a power of a word of length gcd(m, r); it is cyclically reduced exactly when that word is."""
    from math import gcd

    def cr(d):
        # cyclically reduced words of length d in F_n: trace of the transfer matrix A^d, A the 2n x 2n matrix of
        # allowed successions (x followed by y unless y = x^-1)
        k = 2 * n
        import numpy as np
        A = np.ones((k, k), dtype=object)
        for i in range(n):
            A[i, i + n] = 0
            A[i + n, i] = 0
        M = np.identity(k, dtype=object)
        for _ in range(d):
            M = M.dot(A)
        return int(sum(M[i, i] for i in range(k)))
    return sum(cr(gcd(m, r)) for r in range(m)) // m


def apply(move, w):
    """move: dict letter -> image word (for positive letters); negative letters by inversion."""
    out = []
    for x in w:
        if x > 0:
            out += move.get(x, [x])
        else:
            out += inverse(move.get(-x, [-x]))
    return out


def transvections(n):
    mv = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                for e in (1, -1):
                    mv['R_%d%d^%+d' % (i, j, e)] = {i: [i, e * j]}
                    mv['L_%d%d^%+d' % (i, j, e)] = {i: [e * j, i]}
    return mv


def full_moves(n):
    mv = dict(transvections(n))
    for i in range(1, n + 1):
        mv['inv_%d' % i] = {i: [-i]}
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            mv['swap_%d%d' % (i, j)] = {i: [j], j: [i]}
    return mv


def kept(cls, moves):
    c = canon(list(cls))
    ci = canon(cyc_reduce(inverse(list(cls))))
    exact = True
    upto = True
    for mv in moves.values():
        img = canon(cyc_reduce(apply(mv, list(cls))))
        if img != c:
            exact = False
        if img != c and img != ci:
            upto = False
        if not exact and not upto:
            break
    return exact, upto


def whitehead(cls, n):
    w = list(cls)
    m = len(w)
    ok = True
    for i in range(1, n + 1):
        ni = sum(1 for x in w if abs(x) == i)
        for j in range(1, n + 1):
            if i == j:
                continue
            c = cp = 0
            for k in range(m):
                x, y = w[k], w[(k + 1) % m]
                if (x == i and y == -j) or (x == j and y == -i):
                    c += 1
                if (x == i and y == j) or (x == -j and y == -i):
                    cp += 1
            l1 = len(cyc_reduce(apply({i: [i, j]}, w)))
            l2 = len(cyc_reduce(apply({i: [i, -j]}, w)))
            if l1 != m + ni - 2 * c or l2 != m + ni - 2 * cp:
                ok = False
    return ok


def main():
    out = {}
    # K1
    R2 = {'R': {1: [1, 2]}, 'L': {2: [1, 2]}}
    comm = (1, 2, -1, -2)
    k1a = kept(canon(list(comm)), R2)[0]
    k1b = kept(canon([1, 1, 2]), R2)[0]
    print('K1  [a, b] kept by R and L: %s; aab kept: %s' % (k1a, k1b))
    out['K1'] = (k1a, k1b)

    # C2 for n = 3, 4, 5
    for n, maxlen in ((3, 8), (4, 7), (5, 6)):
        cl = classes(n, maxlen)
        k2 = all(len(cl[m]) == burnside_count(n, m) for m in cl)
        total = sum(len(v) for v in cl.values())
        Rpm = {k: v for k, v in transvections(n).items() if k.startswith('R_')}
        tv = transvections(n)
        fm = full_moves(n)
        c1_fail = 0
        len_kept = 0
        kept_tv = [0, 0]
        kept_full = [0, 0]
        for m in cl:
            for w in cl[m]:
                if not whitehead(w, n):
                    c1_fail += 1
                if all(len(cyc_reduce(apply(mv, list(w)))) == m for mv in Rpm.values()):
                    len_kept += 1
                e, u = kept(w, tv)
                kept_tv[0] += e
                kept_tv[1] += u
                e, u = kept(w, fm)
                kept_full[0] += e
                kept_full[1] += u
        r = dict(maxlen=maxlen, classes=total, K2_counts_match=k2, C1_failures=c1_fail,
                 length_kept_by_every_Rij=len_kept, kept_by_transvections_exactly=kept_tv[0],
                 kept_by_transvections_up_to_inversion=kept_tv[1], kept_by_full_exactly=kept_full[0],
                 kept_by_full_up_to_inversion=kept_full[1])
        print('C2  n = %d:' % n, r)
        out['C2_n%d' % n] = r

    # C3 for n = 2 to length 12
    cl = classes(2, 12)
    k2 = all(len(cl[m]) == burnside_count(2, m) for m in cl)
    total = sum(len(v) for v in cl.values())
    tv4 = {'R_12': {1: [1, 2]}, 'R_21': {2: [2, 1]}, 'L_12': {1: [2, 1]}, 'L_21': {2: [1, 2]}}
    fm = full_moves(2)
    res = {'R and L': [[], []], 'the four transvections': [[], []], 'the full moves': [[], []]}
    c1_fail = 0
    for m in cl:
        for w in cl[m]:
            if not whitehead(w, 2):
                c1_fail += 1
            for name, mv in (('R and L', R2), ('the four transvections', tv4), ('the full moves', fm)):
                e, u = kept(w, mv)
                if e:
                    res[name][0].append(w)
                if u:
                    res[name][1].append(w)
    powers = {canon(cyc_reduce(list(comm) * k)) for k in (1, 2, 3)} | \
             {canon(cyc_reduce(inverse(list(comm)) * k)) for k in (1, 2, 3)}

    def name_of(w):
        for k in (1, 2, 3):
            if canon(cyc_reduce(list(comm) * k)) == w:
                return '[a,b]^%d' % k
            if canon(cyc_reduce(inverse(list(comm)) * k)) == w:
                return '[a,b]^-%d' % k
        return 'other: ' + ''.join({1: 'a', 2: 'b', -1: 'A', -2: 'B'}[x] for x in w)
    summary = {}
    for name, (ex, up) in res.items():
        summary[name] = dict(exactly=sorted(name_of(w) for w in ex), up_to_inversion=sorted(name_of(w) for w in up))
    print('C3  n = 2 to length 12: %d classes (K2 counts match: %s); C1 failures %d' % (total, k2, c1_fail))
    for name, v in summary.items():
        print('     kept by %s: exactly %s; up to inversion %s' % (name, v['exactly'], v['up_to_inversion']))
    out['C3'] = dict(classes=total, K2=k2, C1_failures=c1_fail, kept=summary,
                     powers_are_exactly_those_kept_by_R_and_L=(set(res['R and L'][0]) == powers))

    # C4
    import sympy as sp
    x, y, z = sp.symbols('x y z')
    k = x ** 2 + y ** 2 + z ** 2 - x * y * z - 2
    sol = sp.solve([k + 2, sp.diff(k, x), sp.diff(k, y), sp.diff(k, z)], [x, y, z], dict=True)
    print('C4  singular points of kappa = -2:', sol)
    out['C4'] = [str(s) for s in sol]
    json.dump(out, open(sys.argv[1], 'w'), indent=1, default=str)
    return 0


if __name__ == '__main__':
    sys.exit(main())
