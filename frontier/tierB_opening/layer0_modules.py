r"""LAYER 0 — the symbolic gate for B518 Tier B. Exact; no floats, no tolerance.

Sealed under frontier/tierB_opening/PREREGISTRATION.md
(sha256 d8725e4dcd27478649a2853ab94583ed85ab0b2b743adb1177335c0802400ef3).

WHAT THIS DECIDES
-----------------
Bellissard gap-labelling is NECESSARY: if a gap opens at IDS value v, then v lies in
the chain's frequency module G. So a label NOT in G is forbidden outright, and the
prereg's R1 fires with zero CPU.

  R1  ->  1/phi not in G_mixed, or 1/2 not in G_mixed  =>  the MIXED row is REFUTED.

THE MACHINERY SELF-TEST (prereg section 6), and it is not optional
-----------------------------------------------------------------
The naive letter-frequency tower gives G_TM = Z[1/2]. That is WRONG: the 2-block
frequencies of Thue-Morse are ab = ba = 1/3, and 1/3 is not in Z[1/2]. The correct
module is (1/3)Z[1/2]. So this file computes BLOCK frequencies, not letter
frequencies, and reproducing the 1/3 is the gate that licenses everything else.
If the 1/3 does not appear, the machinery is broken and its other outputs are void.

DECLARED DESIGN FREEDOM (prereg section 2.6): the directive must be an INFINITE rule.
The primary is the simplest periodic rule containing both substitutions,
(fib, tm) repeated, chosen on SIMPLICITY and stated before computing. Reconnaissance
(prereg K3) already suggests this tail fails; that is declared, and the prereg's
SURVIVES-WEAKENED branch and control C5 cover eventually-Fibonacci tails.

CONVENTION: the directive is applied left-to-right to the seed, w_{n+1} = sigma_{n+1}(w_n),
so one period of (fib, tm) composes as tau = tm . fib.
"""
import sympy as sp

PHI = (1 + sp.sqrt(5)) / 2

FIB = {'a': 'ab', 'b': 'a'}
TM = {'a': 'ab', 'b': 'ba'}


def compose(outer, inner):
    """The substitution w -> outer(inner(w))."""
    return {c: ''.join(outer[d] for d in inner[c]) for c in inner}


def blocks(sub, n, depth=14):
    """The n-blocks occurring in the substitution's fixed point."""
    w = 'a'
    for _ in range(depth):
        w = ''.join(sub[c] for c in w)
        if len(w) > 60000:
            break
    return sorted({w[i:i + n] for i in range(len(w) - n)})


def block_matrix(sub, n):
    """Incidence matrix of the induced n-block substitution.

    The n-block b maps to the n-blocks of sub(b) read at offsets
    0 .. |sub(b[0])| - 1 — the standard n-block (Queffelec) construction.
    """
    B = blocks(sub, n)
    idx = {b: i for i, b in enumerate(B)}
    M = sp.zeros(len(B), len(B))
    for b in B:
        img = ''.join(sub[c] for c in b)
        for off in range(len(sub[b[0]])):
            nb = img[off:off + n]
            if len(nb) == n and nb in idx:
                M[idx[nb], idx[b]] += 1
    return B, M


def frequencies(sub, n):
    """EXACT n-block frequencies = normalised Perron eigenvector."""
    B, M = block_matrix(sub, n)
    lam = max(sp.Matrix(M).eigenvals().keys(), key=lambda e: sp.re(sp.N(e)))
    ns = (M - lam * sp.eye(M.rows)).nullspace()
    if not ns:
        return B, lam, None
    v = ns[0]
    s = sum(v)
    return B, sp.nsimplify(sp.simplify(lam)), [sp.nsimplify(sp.simplify(x / s)) for x in v]


def report(name, sub, nmax=3):
    print(f'\n--- {name} ---')
    seen = []
    for n in range(1, nmax + 1):
        B, lam, f = frequencies(sub, n)
        if f is None:
            print(f'  {n}-block: no Perron eigenvector (singular) — skipped')
            continue
        print(f'  {n}-block  Perron lambda = {lam}   ({len(B)} blocks)')
        for b, x in zip(B, f):
            print(f'      freq[{b}] = {x}')
            seen.append(sp.simplify(x))
    return seen


def is_rational(x):
    return sp.simplify(sp.nsimplify(x)).is_rational


if __name__ == '__main__':
    print('LAYER 0 — exact gap-label modules. Prereg d8725e4d.')
    print('=' * 74)

    fib_f = report('FIBONACCI  a->ab, b->a', FIB)
    tm_f = report('THUE-MORSE  a->ab, b->ba', TM)

    print('\n' + '=' * 74)
    print('THE MACHINERY SELF-TEST (prereg 6): TM 2-block frequencies must')
    print('contain 1/3 — the naive letter tower gives Z[1/2] and is WRONG.')
    got_third = any(sp.simplify(x - sp.Rational(1, 3)) == 0 for x in tm_f)
    print(f'  1/3 present among TM block frequencies : {got_third}')
    if not got_third:
        print('  GATE FAILED — machinery broken, all other output void.')
        raise SystemExit(1)
    print('  GATE PASSED — block machinery licensed.')

    print('\n' + '=' * 74)
    tau = compose(TM, FIB)          # one period of (fib, tm), left-to-right
    print(f'THE MIXED CHAIN, directive (fib, tm) repeated')
    print(f'  one period composes to tau = tm . fib = {tau}')
    B1, M1 = block_matrix(tau, 1)
    print(f'  letter incidence matrix = {M1.tolist()}   det = {M1.det()}')
    mix_f = report('MIXED  tau', tau)

    print('\n' + '=' * 74)
    print('MEMBERSHIP — exact')
    half, inv_phi = sp.Rational(1, 2), sp.simplify(1 / PHI)

    fib_rational = all(is_rational(x) for x in fib_f)
    tm_rational = all(is_rational(x) for x in tm_f)
    mix_rational = all(is_rational(x) for x in mix_f)
    print(f'  Fibonacci frequencies all rational ? {fib_rational}')
    print(f'  Thue-Morse frequencies all rational? {tm_rational}')
    print(f'  MIXED      frequencies all rational? {mix_rational}')

    print()
    print('  1/2 in Z + Z*phi ?  1/2 = m + n*phi forces n = 0 (phi irrational')
    print('                      over Q), then m = 1/2 not in Z.  => NO')
    print(f'  1/phi = {sp.nsimplify(inv_phi)} is IRRATIONAL: '
          f'{not sp.nsimplify(inv_phi).is_rational}')
    print('  A module generated by RATIONAL frequencies lies in Q, so it')
    print('  cannot contain an irrational. Hence:')
    print(f'    1/phi in G_TM    ? {"NO" if tm_rational else "needs work"}')
    print(f'    1/phi in G_MIXED ? {"NO" if mix_rational else "needs work"}')

    print('\n' + '=' * 74)
    if mix_rational:
        print('  *** R1 FIRES ***')
        print('  G_mixed is generated by RATIONAL frequencies for the (fib,tm)')
        print('  directive, so the irrational 1/phi CANNOT be a gap label.')
        print('  Bellissard necessity FORBIDS the golden gap in this chain.')
        print('  The MIXED row is REFUTED for this directive — zero CPU spent')
        print('  on any spectrum, exactly as the prereg intended.')
        print('  SCOPE: this refutes the (fib,tm)-periodic directive. Control C5')
        print('  (eventually-Fibonacci tails) is a DIFFERENT chain and is not')
        print('  touched by this result. cc3 does NOT adjudicate; cc''s bench does.')
    else:
        print('  R1 does not fire on this directive. Proceed to Phase 2.')
