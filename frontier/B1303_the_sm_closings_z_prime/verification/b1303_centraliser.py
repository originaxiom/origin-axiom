"""B1303 Q0 -- B1140 vs fc R49, decided on main's exact E6 (the SL(3)^3 frame of B1297's step6; written before the DESIGN seal,
run only after it).

Two embeddings of so(3,1)_C (+) su(3) = sl2 (+) sl2 (+) sl3 into e6, both with colour = the third sl3 of the trinification frame:
  (T) B1140/B1138's embedding: the two sl2's are the PRINCIPAL sl2's of the first two sl3's (h = diag(2, 0, -2));
  (R) the REGULAR A1 A1 A2 embedding: the two sl2's are ROOT sl2's of the first two sl3's (h = diag(1, -1, 0)).
For each we compute, on the 64-dimensional complement of the 14: the (h1, h2)-weight table with colour content, the number of
ZERO-WEIGHT COLOUR-SINGLET vectors (what `spacetime64.py` prints beside "0 = NO hypercharge room"), and the CENTRALISER of the
14 inside the 64 = the trivial summands under sl2 (+) sl2 (+) sl3 = the trivial sl2 (+) sl2 strings in the colour-singlet sector
(what B1140 calls "invariant content" and fc R49 calls "room for a u(1)").
PRE-REGISTERED (DESIGN B1303 Q0): (T) zero-weight singlets 2, centraliser 0, the 64 = (4,0)+(0,4) singlets + 6 x (2,2) coloured,
i.e. 5 + 5 + 27 + 27; (R) zero-weight singlets 2, centraliser 2 (two commuting u(1)s). PASS iff both hold; FAIL otherwise.
Positive control: the count that distinguishes the two embeddings (0 vs 2) is printed for both, so the test can fail."""
import json, itertools
from collections import Counter
from fractions import Fraction as Fr

def eps(i):
    v = [Fr(0)] * 3; v[i] = Fr(1); return [x - Fr(1, 3) for x in v]
Z3 = [Fr(0)] * 3
def cat(*parts): return tuple(x for p in parts for x in p)
def dot(u, v): return sum(a * b for a, b in zip(u, v))
A2 = [tuple(a - b for a, b in zip(eps(i), eps(j))) for i in range(3) for j in range(3) if i != j]
roots = set()
for f in range(3):
    for r in A2:
        parts = [Z3, Z3, Z3]; parts[f] = list(r); roots.add(cat(*parts))
for i, j, k in itertools.product(range(3), repeat=3):
    w = cat(eps(i), eps(j), eps(k)); roots.add(w); roots.add(tuple(-x for x in w))
roots = sorted(roots); assert len(roots) == 72
def block(r, f): return r[3 * f:3 * f + 3]
def is_zero(v): return all(x == 0 for x in v)
def H_of(f, coeffs):
    v = [Fr(0)] * 9; v[3 * f:3 * f + 3] = [Fr(c) for c in coeffs]; return tuple(v)

def decompose_2(wts):
    """multiset of (m1, m2) weights of a finite-dimensional sl2 (+) sl2 module -> list of highest weights, by peeling"""
    c = Counter(wts); hw = []
    for w in sorted(c, key=lambda t: (-t[0], -t[1])):
        while c[w] > 0:
            a, b = w
            for i in range(int(a) + 1):
                for j in range(int(b) + 1):
                    ww = (a - 2 * i, b - 2 * j); c[ww] -= 1
                    assert c[ww] >= 0, ("not a module", ww)
            hw.append((int(a), int(b)))
    return hw

def analyse(h0, h1):
    # every basis vector of e6: 72 root vectors + 6 Cartan; colour-singlet = zero colour block (or Cartan)
    vecs = []
    for r in roots:
        vecs.append(((dot(h0, r), dot(h1, r)), is_zero(block(r, 2)), r))
    for i in range(6):
        vecs.append(((Fr(0), Fr(0)), True, ("cartan", i)))
    # the 14 to remove: the two sl2's (weights (+-2,0),(0,0) and (0,+-2),(0,0); all colour singlets) and the colour sl3 (8 at (0,0): 6 charged + 2 Cartan)
    remove_singlet = Counter([(Fr(2), Fr(0)), (Fr(0), Fr(0)), (Fr(-2), Fr(0)), (Fr(0), Fr(2)), (Fr(0), Fr(0)), (Fr(0), Fr(-2)), (Fr(0), Fr(0)), (Fr(0), Fr(0))])
    remove_charged = Counter([(Fr(0), Fr(0))] * 6)
    sing = Counter(w for w, s, r in vecs if s); chg = Counter(w for w, s, r in vecs if not s)
    for w, n in remove_singlet.items(): sing[w] -= n
    for w, n in remove_charged.items(): chg[w] -= n
    assert all(v >= 0 for v in sing.values()) and all(v >= 0 for v in chg.values())
    assert sum(sing.values()) + sum(chg.values()) == 64, (sum(sing.values()), sum(chg.values()))
    zero_weight_singlets = sing[(Fr(0), Fr(0))]
    hw_s = decompose_2(list(sing.elements())); hw_c = decompose_2(list(chg.elements()))
    centraliser = sum(1 for a, b in hw_s if (a, b) == (0, 0))
    dims_s = {k: v for k, v in Counter(hw_s).items()}; dims_c = {k: v for k, v in Counter(hw_c).items()}
    return dict(zero_weight_singlets=zero_weight_singlets, singlet_dim=sum(sing.values()), charged_dim=sum(chg.values()),
                strings_singlet=dims_s, strings_charged=dims_c, centraliser=centraliser,
                zero_weight_total=sing[(Fr(0), Fr(0))] + chg[(Fr(0), Fr(0))])

if __name__ == "__main__":
    emb = {"T (principal sl2's; B1140/B1138)": (H_of(0, (2, 0, -2)), H_of(1, (2, 0, -2))),
           "R (root sl2's, regular A1A1A2; fc R49's rank count)": (H_of(0, (1, -1, 0)), H_of(1, (1, -1, 0)))}
    res = {}
    for name, (h0, h1) in emb.items():
        a = analyse(h0, h1); res[name] = a
        print(f"{name}:")
        print(f"   64 = {a['singlet_dim']} colour-singlet + {a['charged_dim']} coloured; states at weight (0,0): {a['zero_weight_total']}, of them colour singlets: {a['zero_weight_singlets']}")
        print(f"   sl2+sl2 strings, colour-singlet sector: {a['strings_singlet']}; coloured sector: {a['strings_charged']}")
        print(f"   CENTRALISER of the 14 inside the 64 (trivial summands): {a['centraliser']}")
    T = res["T (principal sl2's; B1140/B1138)"]; R = res["R (root sl2's, regular A1A1A2; fc R49's rank count)"]
    okT = T["zero_weight_singlets"] == 2 and T["centraliser"] == 0 and T["strings_singlet"] == {(4, 0): 1, (0, 4): 1} and T["strings_charged"] == {(2, 2): 6}
    okR = R["zero_weight_singlets"] == 2 and R["centraliser"] == 2
    print(f"B1140's (b) 'invariant content = 0' holds for (T): {T['centraliser'] == 0}; the printed count 2 = the two spin-2 middle weights (members of the (4,0) and (0,4) strings), not invariants")
    print(f"fc R49's 'two u(1)s of room' holds for (R): {R['centraliser'] == 2}; the same count 2 there IS the centraliser")
    json.dump({k: {kk: (str(vv) if not isinstance(vv, int) else vv) for kk, vv in v.items()} for k, v in res.items()}, open("b1303_centraliser.json", "w"), indent=1)
    print("Q0:", "PASS" if okT and okR else "FAIL")
