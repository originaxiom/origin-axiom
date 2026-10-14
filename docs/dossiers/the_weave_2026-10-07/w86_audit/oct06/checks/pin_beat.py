import sympy as sp
om = sp.Symbol('om')
def red(e): return sp.expand(sp.rem(sp.expand(e), om**2 + om + 1, om))
def R(M): return M.applyfunc(red)
A = sp.Matrix([[1, 1], [0, 1]]); B = sp.Matrix([[1, 0], [-om, 1]])
SYM = {'a': A, 'A': A.adjugate(), 'b': B, 'B': B.adjugate()}
def ev(w):
    M = sp.eye(2)
    for c in w: M = R(M * SYM[c])
    return M
conj = lambda M: R(M.subs(om, -1 - om))
W = sp.Matrix([[1, -om], [0, 1]]); Wi = W.adjugate()
beat = {'a': 'a', 'b': 'BabAb'}
def beat_word(w):   # apply beat to a word letter by letter
    out = ''
    for c in w:
        img = beat[c.lower()]
        out += img if c.islower() else ''.join(ch.swapcase() for ch in reversed(img))
    return out
for g in 'ab':
    print(f"W conj(rho({g})) W^-1 == rho(beat({g})): {R(W * conj(ev(g)) * Wi) == ev(beat[g])}")
print("beat(relator) = I:", ev(beat_word('abABaBAbaB')) == sp.eye(2))
print("beat^2(b) == a b a^-1 (as matrices):", ev(beat_word(beat['b'])) == ev('abA'))
print("beat^2(a) == a:", ev(beat_word('a')) == ev('a'))
