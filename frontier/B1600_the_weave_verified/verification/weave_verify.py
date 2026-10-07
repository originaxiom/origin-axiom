#!/usr/bin/env python3
"""B1600 -- main's own verification of the SM seat's weave W1-W3 (W4 by representation theory): the moves on the
three non-zero parities of the two records; the parity lemma (odd trace <=> a 3-cycle) on every signed word to length N;
the common fixed point of the moves on the Markov surface at the parabolic level (sympy); the quaternion point extended over
the base: tau in 2T and the image 2T on every odd-trace word to length M.  Writes weave_verify.json."""
import sys, json, itertools, pathlib
import numpy as np, sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
N, M_ = (int(sys.argv[1]) if len(sys.argv) > 1 else 8), (int(sys.argv[2]) if len(sys.argv) > 2 else 6)
out = {}
# W1
L = np.array([[1,1],[0,1]]); R = np.array([[1,0],[1,1]]); P = np.array([[0,1],[1,0]]); I = np.eye(2, dtype=int); par = [(1,0),(0,1),(1,1)]
act = lambda A, v: tuple(int(x) % 2 for x in A @ np.array(v)); fixed = lambda A: [v for v in par if act(A, v) == v]
perm = lambda A: tuple(par.index(act(A, v)) for v in par)
def order(p):
    k, q = 1, p
    while q != (0,1,2): q = tuple(p[i] for i in q); k += 1
    return k
out["W1"] = dict(L=fixed(L), R=fixed(R), P=fixed(P), minus_I=fixed(-I), any_two_cycle_all_three=all(max(order(perm(A@B)), order(perm(B@A))) == 3 for A, B in ((L,R),(L,P),(R,P))))
# the parity lemma
ok = True; n_all = n_odd = 0
for n in range(2, N + 1):
    for w in itertools.product("LR", repeat=n):
        if "L" not in w or "R" not in w: continue
        A = I.copy()
        for ch in w: A = A @ (L if ch == "L" else R)
        for s in (1, -1):
            n_all += 1; odd = int(np.trace(s * A)) % 2 == 1; n_odd += odd; ok &= (odd == (order(perm(s * A)) == 3))
out["parity_lemma"] = dict(words=n_all, odd=n_odd, holds=bool(ok), max_length=N)
# W2
x, y, z = sp.symbols("x y z"); kappa = x**2 + y**2 + z**2 - x*y*z - 2
Lm = {x: x, y: z, z: x*z - y}; Rm = {x: z, y: y, z: y*z - x}
fx = lambda mv: [sp.expand(v - v.subs(mv, simultaneous=True)) for v in (x, y, z)]
out["W2"] = dict(parabolic_common_fixed_points=[{str(k): str(v) for k, v in s.items()} for s in sp.solve(fx(Lm) + fx(Rm) + [kappa + 2], [x, y, z], dict=True)],
                 all_levels=[{str(k): str(v) for k, v in s.items()} for s in sp.solve(fx(Lm) + fx(Rm), [x, y, z], dict=True)])
# W3
I2 = sp.eye(2); i_ = sp.Matrix([[sp.I, 0], [0, -sp.I]]); j_ = sp.Matrix([[0, 1], [-1, 0]]); k_ = i_ * j_
q = lambda a, b, c, d: a * I2 + b * i_ + c * j_ + d * k_; h = sp.Rational(1, 2)
twoT = [q(*v) for v in [(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),(0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)]] + [q(*[s * h for s in signs]) for signs in itertools.product((1, -1), repeat=4)]
key = lambda Mx: tuple((sp.Rational(sp.re(sp.expand(e))), sp.Rational(sp.im(sp.expand(e)))) for e in Mx)
def closure(gens):
    G = {key(I2)}; fr = [I2]
    while fr:
        Mx = fr.pop()
        for g in gens:
            Nn = sp.expand(Mx * g)
            if key(Nn) not in G: G.add(key(Nn)); fr.append(Nn)
    return len(G)
def apply_word(word, A, B):
    Mx = I2
    for ch in word: Mx = Mx * ({"a": A, "b": B}[ch])
    return sp.expand(Mx)
def phi_words(w):
    imgs = ("a", "b")
    for ch in w: imgs = (imgs[0], imgs[0] + imgs[1]) if ch == "L" else (imgs[0] + imgs[1], imgs[1])
    return imgs
Ls, Rs = sp.Matrix([[1,1],[0,1]]), sp.Matrix([[1,0],[1,1]]); rows = []
for n in range(2, M_ + 1):
    for wt in itertools.product("LR", repeat=n):
        w = "".join(wt)
        if "L" not in w or "R" not in w: continue
        Mx = I2
        for ch in w: Mx = Mx * (Ls if ch == "L" else Rs)
        tr = int(Mx.trace()); pa, pb = phi_words(w); A, B = apply_word(pa, i_, j_), apply_word(pb, i_, j_)
        taus = [t for t in twoT if key(sp.expand(t * i_ * t.inv())) == key(A) and key(sp.expand(t * j_ * t.inv())) == key(B)]
        rows.append(dict(word=w, trace=tr, odd=tr % 2 == 1, taus_in_2T=len(taus), image=closure([i_, j_, taus[0]]) if taus else None))
odd = [r for r in rows if r["odd"]]; even = [r for r in rows if not r["odd"]]
out["W3"] = dict(max_length=M_, odd_words=len(odd), odd_all_2T=all(r["taus_in_2T"] == 2 and r["image"] == 24 for r in odd), even_words=len(even), even_images=sorted(set(r["image"] for r in even if r["image"])), even_without_tau_in_2T=sum(1 for r in even if not r["taus_in_2T"]), rows=rows)
out["W4"] = "A4 = 2T/{+-1} = (Z/2)^2 x| Z/3; on the three parity lines (one per non-zero parity, h^1(F; chi) = 1) the (Z/2)^2 acts by the three non-trivial characters and the 3-cycle permutes them: the standard 3-dimensional irreducible representation of A4 (its character (3, -1, 0, 0) has norm 1); for an involution it splits 1 + 2 -> 1 + 1 + 1 over C. Representation theory, no computation."
json.dump(out, open(HERE / "weave_verify.json", "w"), indent=1, default=str); print({k: (v if k not in ("W3",) else {kk: vv for kk, vv in v.items() if kk != "rows"}) for k, v in out.items()})
