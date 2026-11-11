"""
W-C3, item W107 (arc B1676): the tick on the weave, computed by this seat's own route.

SOURCE OF THE DEFINITIONS.  The SM seat's rule W107_RULE.md as main received it (B1676's verification/received/), read
through the mask.  Neither the seat's script nor main's checking script is run or opened.  The construction below is
built from the rule's A0 alone: in the parity basis rho(L) = c(L) S(L), rho(R) = c(R) S(R), with c(L) = exp(-i pi/4),
c(R) = exp(+i pi/4), and S(L), S(R) quarter-turns about two different coordinate axes, such that
rho(L) rho(R)^-1 rho(L) = rho(R)^-1 rho(L) rho(R)^-1, generating a group of order 96.  Every choice of axes and turning
senses that satisfies the relation is run.

THE THREADS.  Every primitive cyclic word in L and R with both letters, of length 2 to 16, up to rotation (Lyndon
words; the swap L <-> R is not an identification).  A thread's matrix is the product of L = rows (1,0),(1,1) and
R = rows (1,1),(0,1) along the word; odd trace is convention-free.  A thread's tick rho(w) is the product of the lifts
along the word; its operator mean is the projector onto the eigenvalue-1 eigenspace.

WHAT IS COMPUTED, AND WHAT WOULD COUNT AS NOT REPRODUCING (written before the run)
  A0  some choice of axes and senses satisfies the relation and generates a group of order 96; otherwise the
      construction from A0 fails and nothing below is read.
  Q2  8 798 threads; 3 822 of odd trace; on every odd-trace thread S(w) has order 3, and the mean is rank one exactly
      when #L = #R (mod 8): 916 threads, and zero on the other 2 906.  A different count, or a rank-one mean off that
      rule, is NOT REPRODUCED.  (These counts depend only on c(w) and on S(w)'s conjugacy class.)
  Q3  every rank-one mean projects onto a body diagonal (+-1, +-1, +-1)/sqrt 3 of the parity basis, and all four
      diagonals occur.  The multiset of the four counts (215, 229, 235, 237) and the mean of means' largest off-diagonal
      entry (3.1 % of the diagonal) depend on which rotation represents a thread, since rotating a word conjugates its
      tick.  They are computed under four conventions (Lyndon order L < R or R < L; the product taken left to right or
      right to left) and compared under each; if no convention gives them, that is reported as DIFFERS for these
      convention-bound numbers only.  The axis as a function of the matrix modulo 4 (the seat's Q3c) is reported.
  Q4  the mean of means has diagonal 916 / (3 x 3 822) = 0.0799; its largest off-diagonal entry is at most a tenth of
      the diagonal (the seat's Q4b); the odd-trace ticks generate End(T) (dimension 9); their commutant is the
      scalars; no non-zero vector is fixed by all of them.  Any of these failing is NOT REPRODUCED.
  R1  reported, not predicted: the even-trace threads' means by the order of S(w) and by c(w); the rank-one count
      under the four sign choices of the lifts (+-c(L), +-c(R)); main records 916 against 906 between two of them.

CONTROLS (must come out as stated, or the code is broken)
  C1  the average of rho(g) over the group's 96 elements is zero.
  C2  no even-trace thread has S(w) of order 3.
  C3  the number of Lyndon words of each length equals the necklace formula (1/n) sum_{d | n} mu(d) 2^(n/d).

DISCLOSED.  The seat's numbers are known to this seat (they are in main's claim line); this is a check, not a blind
test.
"""
import itertools
import json
import sys

import numpy as np

TOL = 1e-9


def lyndon(n, alphabet):
    """Duval's algorithm: Lyndon words of length exactly n over the ordered alphabet."""
    k = len(alphabet)
    out = []
    w = [-1]
    while w:
        w[-1] += 1
        m = len(w)
        if m == n:
            out.append(''.join(alphabet[i] for i in w))
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == k - 1:
            w.pop()
    return out


def mobius(n):
    res, p, m = 1, 2, n
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res


def necklace_count(n):
    return sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n


def quarter(axis, sense):
    """Rotation by sense * 90 degrees about coordinate axis 0, 1 or 2."""
    m = np.zeros((3, 3))
    m[axis, axis] = 1
    a, b = [i for i in range(3) if i != axis]
    m[a, a] = 0
    m[b, b] = 0
    m[a, b] = -sense
    m[b, a] = sense
    return m


def close_group(gens):
    elems = [np.eye(3, dtype=complex)]
    keys = {tuple(np.round(elems[0], 9).ravel())}
    frontier = list(elems)
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = x @ g
                k = tuple(np.round(y, 9).ravel())
                if k not in keys:
                    keys.add(k)
                    elems.append(y)
                    nxt.append(y)
        frontier = nxt
        if len(elems) > 2000:
            break
    return elems


def matmod(word):
    L = np.array([[1, 0], [1, 1]], dtype=object)
    R = np.array([[1, 1], [0, 1]], dtype=object)
    M = np.array([[1, 0], [0, 1]], dtype=object)
    for ch in word:
        M = M.dot(L if ch == 'L' else R)
    return M


def order_of(S):
    X = np.eye(3)
    for k in range(1, 25):
        X = X @ S
        if np.allclose(X, np.eye(3), atol=1e-9):
            return k
    return None


def projector_one(rho):
    """Projector onto the eigenvalue-1 eigenspace of a finite-order unitary: the mean over its powers."""
    n = None
    X = np.eye(3, dtype=complex)
    acc = np.zeros((3, 3), dtype=complex)
    for k in range(1, 400):
        acc += X
        X = X @ rho
        if np.allclose(X, np.eye(3), atol=1e-9):
            n = k
            break
    return acc / n, n


DIAGS = [np.array(v) / np.sqrt(3) for v in ([1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1])]


def which_diag(P):
    for idx, v in enumerate(DIAGS):
        if np.allclose(P, np.outer(v, v), atol=1e-9):
            return idx
    return None


def main():
    out = {}
    # C3 and the threads
    words = {}
    for order_name, alph in (('L<R', 'LR'), ('R<L', 'RL')):
        ws = []
        for n in range(2, 17):
            lw = lyndon(n, alph)
            if order_name == 'L<R':
                assert len(lw) == necklace_count(n) - (2 if n == 1 else 0), n
            ws += lw
        words[order_name] = ws
    nthreads = len(words['L<R'])
    print('C3  Lyndon words of length 2-16 match the necklace formula; threads: %d (L<R), %d (R<L)'
          % (nthreads, len(words['R<L'])))
    out['threads'] = nthreads

    # A0: every admissible choice of axes and senses
    cL = np.exp(-1j * np.pi / 4)
    cR = np.exp(1j * np.pi / 4)
    choices = []
    for aL, aR in itertools.permutations(range(3), 2):
        for sL, sR in itertools.product((1, -1), repeat=2):
            SL, SR = quarter(aL, sL), quarter(aR, sR)
            rL, rR = cL * SL, cR * SR
            lhs = rL @ np.linalg.inv(rR) @ rL
            rhs = np.linalg.inv(rR) @ rL @ np.linalg.inv(rR)
            if np.allclose(lhs, rhs, atol=1e-12):
                G = close_group([rL, rR])
                choices.append((aL, sL, aR, sR, len(G)))
    print('A0  admissible choices (axis of L, sense, axis of R, sense, group order):', choices)
    out['A0_choices'] = choices
    good = [c for c in choices if c[4] == 96]
    if not good:
        print('A0  NOT REPRODUCED: no admissible choice generates a group of order 96; stopping')
        json.dump(out, open(sys.argv[1], 'w'), indent=1, default=str)
        return 1
    print('A0  REPRODUCED: %d admissible choices, each of order 96' % len(good))

    results = []
    for (aL, sL, aR, sR, _) in good:
        SL, SR = quarter(aL, sL), quarter(aR, sR)
        rL, rR = cL * SL, cR * SR
        # C1
        G = close_group([rL, rR])
        avg = sum(G) / len(G)
        c1 = np.allclose(avg, 0, atol=1e-9)
        for conv_order in ('L<R', 'R<L'):
            for direction in ('left-to-right', 'right-to-left'):
                odd = 0
                rank_one = 0
                zero = 0
                rule_ok = True
                order3_ok = True
                c2_ok = True
                diag_counts = [0, 0, 0, 0]
                off_diag_axis = 0
                mean_sum = np.zeros((3, 3), dtype=complex)
                ticks_odd = []
                axis_by_mod4 = {}
                even_report = {}
                for w in words[conv_order]:
                    seq = w if direction == 'left-to-right' else w[::-1]
                    rho = np.eye(3, dtype=complex)
                    S = np.eye(3)
                    for ch in seq:
                        rho = rho @ (rL if ch == 'L' else rR)
                        S = S @ (SL if ch == 'L' else SR)
                    M = matmod(w)
                    tr = int(M[0, 0] + M[1, 1])
                    nL, nR = w.count('L'), w.count('R')
                    cw = np.exp(1j * np.pi * (nR - nL) / 4)
                    if not np.allclose(rho, cw * S, atol=1e-9):
                        rule_ok = False
                    P, _ = projector_one(rho)
                    rk = int(round(np.real(np.trace(P))))
                    oS = order_of(S)
                    if tr % 2 == 1:
                        odd += 1
                        ticks_odd.append(rho)
                        if oS != 3:
                            order3_ok = False
                        expect_rank_one = ((nL - nR) % 8 == 0)
                        if rk == 1:
                            rank_one += 1
                            d = which_diag(P)
                            if d is None:
                                off_diag_axis += 1
                            else:
                                diag_counts[d] += 1
                                key = tuple(int(x) % 4 for x in M.ravel())
                                axis_by_mod4.setdefault(key, set()).add(d)
                        elif rk == 0:
                            zero += 1
                        if (rk == 1) != expect_rank_one:
                            rule_ok = False
                        mean_sum += P
                    else:
                        if oS == 3:
                            c2_ok = False
                        k = 'order %s, c^8-exponent %d' % (oS, (nR - nL) % 8)
                        even_report.setdefault(k, {}).setdefault(rk, 0)
                        even_report[k][rk] += 1
                Mbar = mean_sum / odd
                diag = np.real(np.diag(Mbar))
                offmax = max(abs(Mbar[i, j]) for i in range(3) for j in range(3) if i != j)
                results.append(dict(choice=(aL, sL, aR, sR), convention=conv_order, direction=direction,
                                    C1=bool(c1), C2=bool(c2_ok), threads=len(words[conv_order]), odd=odd,
                                    rank_one=rank_one, zero=zero, rule_ok=bool(rule_ok), order3_ok=bool(order3_ok),
                                    diag_counts=diag_counts, off_axis=off_diag_axis,
                                    mean_diag=[float(x) for x in diag], offdiag_rel=float(offmax / diag[0]),
                                    axis_function_of_mod4=all(len(v) == 1 for v in axis_by_mod4.values()),
                                    mod4_classes=len(axis_by_mod4), even_report=even_report))
                if conv_order == 'L<R' and direction == 'left-to-right':
                    # Q4a on this convention (the algebra does not depend on the representative)
                    basis = []
                    span = np.zeros((0, 9), dtype=complex)

                    def add(Xm):
                        nonlocal span
                        v = Xm.reshape(1, 9)
                        cand = np.vstack([span, v])
                        if np.linalg.matrix_rank(cand, tol=1e-8) > span.shape[0]:
                            span = cand
                            basis.append(Xm)
                            return True
                        return False
                    add(np.eye(3, dtype=complex))
                    for t in ticks_odd:
                        add(t)
                    changed = True
                    while changed and span.shape[0] < 9:
                        changed = False
                        for A in list(basis):
                            for B in list(basis):
                                if add(A @ B):
                                    changed = True
                    alg_dim = span.shape[0]
                    # commutant
                    rows = []
                    for t in ticks_odd[:200]:
                        rows.append(np.kron(t, np.eye(3)) - np.kron(np.eye(3), t.T))
                    Kmat = np.vstack(rows)
                    comm_dim = 9 - np.linalg.matrix_rank(Kmat, tol=1e-8)
                    fixed = np.vstack([t - np.eye(3) for t in ticks_odd])
                    fixed_dim = 3 - np.linalg.matrix_rank(fixed, tol=1e-8)
                    results[-1].update(algebra_dim=int(alg_dim), commutant_dim=int(comm_dim),
                                       common_fixed_dim=int(fixed_dim))
        # R1: the four sign choices of the lifts, on the rank-one count
        signs = {}
        for eL, eR in itertools.product((1, -1), repeat=2):
            cnt = 0
            for w in words['L<R']:
                M = matmod(w)
                if int(M[0, 0] + M[1, 1]) % 2 == 1:
                    rho = np.eye(3, dtype=complex)
                    for ch in w:
                        rho = rho @ ((eL * rL) if ch == 'L' else (eR * rR))
                    P, _ = projector_one(rho)
                    if int(round(np.real(np.trace(P)))) == 1:
                        cnt += 1
            signs['%+d c(L), %+d c(R)' % (eL, eR)] = cnt
        results[-1]['R1_sign_choices'] = signs

    out['results'] = results
    for r in results:
        print('---- choice %s, %s, %s' % (r['choice'], r['convention'], r['direction']))
        print('  C1 average over the group zero: %s; C2 no even-trace order-3 S(w): %s' % (r['C1'], r['C2']))
        print('  threads %d; odd trace %d; rank one %d; zero %d; rule #L = #R mod 8 held on every odd thread: %s; '
              'S(w) of order 3 on every odd thread: %s' % (r['threads'], r['odd'], r['rank_one'], r['zero'],
                                                            r['rule_ok'], r['order3_ok']))
        print('  body diagonals (+++, ++-, +-+, -++): %s, multiset %s; rank-one means off every diagonal: %d'
              % (r['diag_counts'], sorted(r['diag_counts']), r['off_axis']))
        print('  mean of means: diagonal %s; largest off-diagonal / diagonal = %.4f'
              % (['%.4f' % x for x in r['mean_diag']], r['offdiag_rel']))
        print('  axis a function of the matrix mod 4: %s (%d classes)' % (r['axis_function_of_mod4'],
                                                                         r['mod4_classes']))
        if 'algebra_dim' in r:
            print('  Q4a: algebra generated by the odd ticks: dim %d; commutant dim %d; common fixed vectors dim %d'
                  % (r['algebra_dim'], r['commutant_dim'], r['common_fixed_dim']))
        print('  R1 even-trace threads (order of S, exponent of c): {rank: count}:')
        for k in sorted(r['even_report']):
            print('     %s: %s' % (k, r['even_report'][k]))
        if 'R1_sign_choices' in r:
            print('  R1 rank-one counts under the four sign choices of the lifts:', r['R1_sign_choices'])
    json.dump(out, open(sys.argv[1], 'w'), indent=1, default=str)
    return 0


if __name__ == '__main__':
    sys.exit(main())
