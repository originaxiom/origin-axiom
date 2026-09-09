"""Symmetry census BEFORE the table (PREREG §4): Isom(m004) = D4 as automorphisms of pi_1 found through the faithful
PSL rep (exact SL2 sign-twist triples; Mostow => every such endomorphism is an automorphism), orientation type,
induced action on H1(C) and on the 16 family characters, and the prediction J(psi o phi) = eps(phi) J(psi), J(psi^-1) = -J(psi)."""
import os, sys, json, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import d2lib as L
from d2lib import OMEGA

REL = L.word_from_snappy("aaabABBAb")
A = L.mat([[1 - OMEGA, 1], [-1, 0]]); B = L.mat([[0, -1], [1, OMEGA * (-2)]])
An, Bn = np.array(L.to_cx(A)), np.array(L.to_cx(B))
letters = {"a": An, "b": Bn, "A": np.linalg.inv(An), "B": np.linalg.inv(Bn)}
def ev(word):
    M = np.eye(2, dtype=complex)
    for ch in word: M = M @ letters[ch]
    return M
ta, tb, tab = np.trace(An), np.trace(Bn), np.trace(An @ Bn)
def is_pm_I(M): return np.allclose(M, np.eye(2), atol=1e-9) or np.allclose(M, -np.eye(2), atol=1e-9)
def reduced(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase(): out.pop()
        else: out.append(ch)
    return "".join(out)
def inv_str(w): return w.swapcase()[::-1]
def subst(word, ia, ib):
    out = ""
    for ch in word:
        img = ia if ch.lower() == "a" else ib
        out += img if ch.islower() else inv_str(img)
    return reduced(out)
def exps(w, g): return sum(1 if ch == g else -1 if ch == g.upper() else 0 for ch in w)
MAXLEN = 7
cands = []
for n in range(1, MAXLEN + 1):
    for tup in itertools.product("aAbB", repeat=n):
        w = "".join(tup)
        if reduced(w) == w: cands.append(w)
def okt(w, t):
    x = np.trace(ev(w))
    return any(abs(x - y) < 1e-9 for y in (t, -t, t.conjugate(), -t.conjugate()))
ca = [w for w in cands if exps(w, "b") % 3 == 0 and okt(w, ta)]
cb = [w for w in cands if exps(w, "b") in (1, -1) and okt(w, tb)]
print(f"words of length <= {MAXLEN}; candidates after trace filter: a' {len(ca)}  b' {len(cb)}")
def triple_class(Ma, Mb):
    trip = (np.trace(Ma), np.trace(Mb), np.trace(Ma @ Mb))
    for sa in (1, -1):
        for sb in (1, -1):
            if all(abs(u - v) < 1e-9 for u, v in zip(trip, (sa * ta, sb * tb, sa * sb * tab))): return +1
            if all(abs(u - v) < 1e-9 for u, v in zip(trip, (sa * ta.conjugate(), sb * tb.conjugate(), sa * sb * tab.conjugate()))): return -1
    return 0
autos = {}
for ia in ca:
    Ma = ev(ia)
    for ib in cb:
        Mb = ev(ib); eps = triple_class(Ma, Mb)
        if eps == 0: continue
        if not is_pm_I(ev(subst("aaabABBAb", ia, ib))): continue
        autos[(ia, ib)] = eps
print(f"automorphism representatives found (relator -> +-I, exact character class): {len(autos)}")

cp = json.load(open("cover_presentation.json"))
gens, rels = cp["gens"], [[tuple(x) for x in R] for R in cp["rels"]]
inv, cls, V, D, keep = L.h1_coordinates(gens, rels)
_, _, rewrite, _, _ = L.rs_cyclic(["a", "b"], [REL], {"a": 0, "b": 1}, 3)
G = [cls([(g, 1)]) for g in gens]
def phi_on_H1(ia, ib):
    rows = []
    for j in range(3):
        rows.append(cls(rewrite(L.word_from_snappy(ib * j + ia + inv_str(ib) * j))))
    rows.append(cls(rewrite(L.word_from_snappy(ib * 3))))
    return rows
def action_matrix(rows):
    sols = []
    for T in itertools.product(range(4), repeat=4):
        Tm = [[T[0], T[1]], [T[2], T[3]]]
        for c in itertools.product(range(4), repeat=2):
            for f in (1, -1):
                ok = True
                for gk, rk in zip(G, rows):
                    tor = [(Tm[i][0] * gk[0] + Tm[i][1] * gk[1] + c[i] * gk[2]) % 4 for i in range(2)]
                    if tor != [rk[0] % 4, rk[1] % 4] or f * gk[2] != rk[2]: ok = False; break
                if ok: sols.append((Tm, c, f))
    return sols
results = []; seen = {}
for (ia, ib), eps in sorted(autos.items(), key=lambda kv: (len(kv[0][0]) + len(kv[0][1]), kv[0])):
    sols = action_matrix(phi_on_H1(ia, ib))
    assert sols, ("no consistent action", ia, ib)
    Tm, c, f = sols[0]; key = (tuple(map(tuple, Tm)), tuple(c), f)
    if key not in seen:
        seen[key] = (ia, ib, eps); results.append(dict(a=ia, b=ib, eps=eps, T=Tm, c=list(c), f=f))
print("\ndistinct actions on H1(C) = Z/4 e1 + Z/4 e2 + Z e3  (T on torsion | c: free->torsion | f: free sign | eps: orientation):")
for r in results: print(f"  a->{r['a']:8s} b->{r['b']:8s} eps={r['eps']:+d}  T={r['T']} c={r['c']} f={r['f']:+d}")
n_pres = sum(1 for r in results if r["eps"] == 1); n_rev = len(results) - n_pres
print(f"count: {len(results)} = {n_pres} orientation-preserving + {n_rev} reversing   (Isom(C): 24 = 8 x 3 deck lifts; m004 amphichiral)")
assert len(results) == 24 and n_pres == 12
P = [r for r in results if r["T"] == [[3, 0], [0, 3]]]
print("elements acting as -1 on the torsion:", [(r["a"], r["b"], r["eps"], r["f"]) for r in P])

chars = [(p, q) for p in range(4) for q in range(4)]
def act(pq, Tm): return ((pq[0] * Tm[0][0] + pq[1] * Tm[1][0]) % 4, (pq[0] * Tm[0][1] + pq[1] * Tm[1][1]) % 4)
elems = {(tuple(map(tuple, r["T"])), r["eps"]) for r in results}
elems.add((((3, 0), (0, 3)), -1))                       # psi -> psi^-1 flips the sign of J (T1)
def compose(x, y):
    Tx, ex = x; Ty, ey = y
    return (tuple(tuple(sum(Tx[i][k] * Ty[k][j] for k in range(2)) % 4 for j in range(2)) for i in range(2)), ex * ey)
group = set(elems); frontier = set(elems)
while frontier:
    new = set()
    for x in group:
        for y in frontier:
            for z in (compose(x, y), compose(y, x)):
                if z not in group: new.add(z)
    group |= new; frontier = new
print("\nsigned symmetry group acting on the 16 family characters: order", len(group))
forced = {}; orbits = {}
for pq in chars:
    orb = set(); fz = None
    for T, e in group:
        img = act(pq, T); orb.add(img)
        if img == pq and e == -1 and fz is None: fz = T
    forced[pq] = fz; orbits[pq] = tuple(sorted(orb))
for o in sorted(set(orbits.values())):
    print(f"  orbit size {len(o):2d}: {o}   J forced to 0: {forced[o[0]] is not None}")
free_chars = [pq for pq in chars if forced[pq] is None]
print("\nPREDICTION (recorded before the table): characters with J forced to 0:", 16 - len(free_chars), " possibly nonzero:", free_chars)
print("mechanism: the period-2 symmetry (a->A, b->aaab; orientation-PRESERVING, +1 on the free part) acts as -1 on Tors H1(C),")
print("           i.e. psi o P = psi^-1 for every family character; with T6 (J(psi o P) = J(psi)) and T1 (J(psi^-1) = -J(psi)) => J == 0.")
json.dump(dict(autos=results, group_order=len(group), forced={f"{p}{q}": (v is not None) for (p, q), v in forced.items()},
               free_chars=free_chars), open("census.json", "w"), indent=1)
