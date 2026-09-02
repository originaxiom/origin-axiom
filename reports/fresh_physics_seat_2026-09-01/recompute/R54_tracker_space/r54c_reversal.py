#!/usr/bin/env python3
"""R54c -- is 'time reversal' (reversing every image word) an intrinsic asymmetry of the rule?
2-letter rule: sigma a->ab, b->a; reversal sigma_bar a->ba, b->a.  4-letter (B532-I6 / B530) rule:
sigma4 a->abAAB, b->aAB, A->abAB, B->aA; B532-I6 claims 'sigma_bar not conjugate to sigma (exhaustive over 24
permutations)'.  A permutation check is not a conjugacy test in Aut(F_n); here we test INNER conjugacy
(sigma_bar = w sigma w^-1 on every letter) over words w of length <= 6, and the abelianizations."""
import itertools, sympy as sp
def inv(s): return ''.join(c.swapcase() for c in reversed(s))
def red(s):
    out = []
    for c in s:
        if out and out[-1] == c.swapcase(): out.pop()
        else: out.append(c)
    return ''.join(out)
def conj(w, s): return red(w + s + inv(w))
def words(letters, L):
    yield ''
    for n in range(1, L + 1):
        for t in itertools.product(letters, repeat=n):
            s = ''.join(t)
            if red(s) == s: yield s
def test(rule, letters, L=6):
    rev = {k: v[::-1] for k, v in rule.items()}
    for w in words(letters, L):
        if all(conj(w, rule[x]) == rev[x] for x in rule):
            return w
    return None
r2 = {'a': 'ab', 'b': 'a'}
print("2-letter rule: reversal = conjugation by w =", repr(test(r2, 'abAB')))
r4 = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
print("4-letter rule images:", r4, " reversed:", {k: v[::-1] for k, v in r4.items()})
# is r4 a genuine automorphism? check it respects inverses: r4[A] should be inv(r4[a]) if A means a^-1
print("4-letter rule respects A = a^-1, B = b^-1 as an F2-automorphism?:", r4['A'] == inv(r4['a']), r4['B'] == inv(r4['b']))
print("  (so it is a 4-letter SUBSTITUTION on the alphabet {a,b,A,B}, not the Fibonacci automorphism of F2 written with inverses)")
w = test(r4, 'abAB', 6)
print("4-letter rule: reversal = inner conjugation by a word of length <= 6?", repr(w))
# abelianizations
def mat(rule, letters):
    return sp.Matrix([[rule[y].count(x) for y in letters] for x in letters])
M4, M4r = mat(r4, 'abAB'), mat({k: v[::-1] for k, v in r4.items()}, 'abAB')
print("4-letter abelianization equal for rule and reversal:", M4 == M4r, " charpoly:", sp.factor(M4.charpoly().as_expr()), " det:", M4.det())
# the 2-letter Fibonacci automorphism written on {a,b,A,B}:
fib4 = {'a': 'ab', 'b': 'a', 'A': 'BA', 'B': 'A'}
print("Fibonacci automorphism on 4 letters: reversal inner by", repr(test(fib4, 'abAB', 6)))
