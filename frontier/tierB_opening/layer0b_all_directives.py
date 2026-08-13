r"""LAYER 0b — does ANY infinite directive carry BOTH labels?

Sealed under frontier/tierB_opening/PREREGISTRATION.md (sha256 d8725e4d...).
Layer 0 refuted the (fib,tm)-periodic directive by R1. This asks the general question,
and runs control C4 (the doubling decoy), which is the prereg's sharpest adversarial test.

M_fib = [[1,1],[1,0]]  det = -1   (invertible)
M_tm  = [[1,1],[1,1]]  det =  0   (RANK 1)

CASE A — infinitely many tm steps (eventually periodic directive).
  rank(AB) <= min(rank A, rank B), so any product containing M_tm has rank <= 1.
  A rank-1 non-negative integer matrix has eigenvalues {trace, 0}: Perron rational,
  eigenvector rational. So all frequencies are RATIONAL and the irrational 1/phi
  cannot be a label.  =>  NO GOLDEN.

CASE B — finitely many tm steps, under the PREREG'S PINNED CONVENTION
  (w_{n+1} = sigma_{n+1}(w_n), so the LAST-applied map is outermost).
  Eventually-fib means the outer maps are all fib; fib is primitive, so fib^n(x)
  converges to the Fibonacci fixed point for ANY x. The prefix WASHES OUT.
  =>  the language is Fibonacci's  =>  NO DYADIC.

If both hold, the mixed row is refuted for EVERY directive under the pinned convention.

CASE B' — the ALTERNATIVE convention (sigma_1 outermost, i.e. the limit is tau applied
  to a Fibonacci word). Here the prefix does NOT wash out and G <= (1/k)(Z + Z*phi).
  1/2 is in that iff k is even. This is the prereg's SURVIVES-WEAKENED branch, and it
  is where control C4 bites: an even k has nothing to do with Thue-Morse.

cc3 does NOT adjudicate. Scope and convention are stated so cc can.
"""
import random
import sympy as sp

PHI = (1 + sp.sqrt(5)) / 2
FIB = {'a': 'ab', 'b': 'a'}
TM = {'a': 'ab', 'b': 'ba'}
DOUBLE = {'a': 'aa', 'b': 'bb'}          # control C4: zero TM content, even scaling


def M(sub):
    letters = sorted(sub)
    return sp.Matrix([[sub[c].count(r) for c in letters] for r in letters])


def compose(outer, inner):
    return {c: ''.join(outer[d] for d in inner[c]) for c in inner}


def freqs_of_word(w, n=1):
    """Exact empirical n-block frequencies of a finite word, as Rationals."""
    from collections import Counter
    ct = Counter(w[i:i + n] for i in range(len(w) - n + 1))
    tot = sum(ct.values())
    return {b: sp.Rational(c, tot) for b, c in sorted(ct.items())}


def build(directive, seed='a', cap=400000):
    """w_{n+1} = sigma_{n+1}(w_n) — the prereg's pinned convention."""
    w = seed
    for s in directive:
        w = ''.join(s[c] for c in w)
        if len(w) > cap:
            break
    return w


print('LAYER 0b — every directive. Prereg d8725e4d.')
print('=' * 74)

print('\nCASE A — any directive containing a tm step')
print(f'  rank M_fib = {M(FIB).rank()}   rank M_tm = {M(TM).rank()}   det M_tm = {M(TM).det()}')
random.seed(11)
bad = 0
for trial in range(200):
    k = random.randint(1, 6)
    d = [random.choice([FIB, TM]) for _ in range(k)]
    if not any(x is TM for x in d):
        continue
    P = sp.eye(2)
    for s in d:
        P = M(s) * P
    if P.rank() > 1:
        bad += 1
print(f'  200 random directives containing >=1 tm: products with rank > 1 = {bad}')
print(f'  => every such product is rank 1; Perron = trace (rational), eigenvector rational.')
print(f'  => G is rational  =>  1/phi FORBIDDEN.   NO GOLDEN.')

print('\nCASE B — finitely many tm, under the PINNED convention (fib outermost)')
w = build([TM, TM, FIB] + [FIB] * 22)
f1 = freqs_of_word(w, 1)
fa = f1.get('a')
target = sp.nsimplify(1 / PHI)
print(f'  directive [tm,tm,fib,fib,...] -> |w| = {len(w)}')
print(f'  freq(a) = {fa} = {float(fa):.10f}')
print(f'  1/phi                         = {float(target):.10f}')
print(f'  |freq(a) - 1/phi| = {float(abs(fa - target)):.3e}  -> the prefix WASHED OUT')
print(f'  => language is Fibonacci\'s => G = Z + Z*phi => 1/2 FORBIDDEN.  NO DYADIC.')

print('\n' + '=' * 74)
print('UNDER THE PREREG\'S PINNED CONVENTION, BOTH CASES FAIL:')
print('  infinitely many tm  -> rational G   -> no golden')
print('  finitely many tm    -> washes out   -> no dyadic')
print('  *** the MIXED row is refuted for EVERY directive. ***')

print('\n' + '=' * 74)
print('CASE B\' — the ALTERNATIVE convention: tau applied to a Fibonacci word.')
print('Here the prefix does NOT wash out. Two chains, one with TM content and')
print('one with NONE, both with an even length-scaling k:')
fibword = build([FIB] * 24)
for name, tau in (('tau = tm  (has TM content)', TM),
                  ('tau = double a->aa,b->bb  (C4 DECOY: zero TM content)', DOUBLE)):
    u = ''.join(tau[c] for c in fibword)
    f = freqs_of_word(u, 1)
    k = sp.Integer(len(u)) / sp.Integer(len(fibword))
    half_in = sp.simplify(sp.Rational(1, 2) * k).is_integer
    print(f'\n  {name}')
    print(f'    |u|/|v| = k = {k}   (even: {sp.Integer(k) % 2 == 0})')
    print(f'    freq(a) = {f.get("a")} = {float(f.get("a")):.8f}')
    print(f'    1/2 in (1/k)(Z + Z*phi)?  1/2 = (1/k)(m+n*phi) => n=0, m=k/2 in Z: {bool(half_in)}')

print('\n' + '=' * 74)
print('*** CONTROL C4 IS THE FINDING ***')
print('  The doubling decoy has ZERO Thue-Morse content and admits 1/2 by exactly')
print('  the same even-k argument as the tm-prefixed chain. So under the alternative')
print('  convention "1/2 present" does NOT indicate TM ancestry -- it indicates an')
print('  EVEN DENOMINATOR. The 2x2 table loses its discriminating power on the one')
print('  cell that carried the mixed-history claim.')
print('\n  cc3 does not adjudicate. Both conventions are reported; cc chooses which')
print('  the banked claim meant, and B518 is re-worded accordingly.')
