#!/usr/bin/env python3
"""R54d -- reading-direction arrow as a property of the LANGUAGE (factor set), the symbolic-dynamics sense in
which B532-I6 claimed 'sigma_bar not conjugate to sigma' for the 4-letter rule.  A substitutive system has a
time arrow iff its language is not closed under reversal.  2-letter Fibonacci is Sturmian: closed (theorem);
the 4-letter rule: check."""
def fixed_point(rule, seed, n):
    w = seed
    for _ in range(n): w = ''.join(rule[c] for c in w)
    return w
def factors(w, L): return {w[i:i + L] for i in range(len(w) - L + 1)}
for name, rule, seed, it in [("2-letter a->ab,b->a", {'a': 'ab', 'b': 'a'}, 'a', 22),
                             ("4-letter B532 rule", {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}, 'a', 9)]:
    w = fixed_point(rule, seed, it)
    print(f"{name}: word length {len(w)}")
    for L in (2, 3, 6, 10):
        F = factors(w, L); R = {f[::-1] for f in F}
        print(f"  L={L}: factors {len(F)}, reversal-closed: {F == R}, factors whose reversal is absent: {len(F - R)}")
    alph = sorted(set(w)); big = factors(w, 2)
    forb = [x + y for x in alph for y in alph if x + y not in big]
    print(f"  forbidden bigrams: {forb}")
