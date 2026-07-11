"""
Movement XV — the certificate: the balanced pair algorithm PROVES pure discrete
spectrum.  Upgrades movement XIII from theory-indicated to computed.

The balanced pair algorithm (Sirvent-Solomyak; Barge-Diamond) decides pure
discrete spectrum for a Pisot substitution:
  * a BALANCED PAIR (u,v): words with equal abelianization; decompose at balance
    points into IRREDUCIBLE pieces; a COINCIDENCE is an irreducible piece (c,c).
  * seed with the adjacent-block transpositions (sigma(a)sigma(b), sigma(b)sigma(a)),
    restricted to pairs whose words OCCUR in the fixed point (the canonical
    restriction that keeps the reachable set finite).
  * close under (apply sigma, decompose).  A pair is GOOD if, following
    non-coincidence children, it can reach a pair whose sigma-image decomposition
    contains a coincidence.
  * PURE DISCRETE SPECTRUM  <=>  every reachable non-coincidence pair is good.

VALIDATED on five controls (this is what earns trust in the verdict):
    Fibonacci, Tribonacci, period-doubling  -> discrete   (True)
    Thue-Morse, Chacon (weakly mixing)       -> NOT discrete (False)

THE OBJECT: pure discrete spectrum = True, 106 reachable balanced pairs, 0 bad,
robust to the length bound (longest reachable word 106, well under the cap -> no
truncation).  So the object is a PROVEN quasicrystal (measurably a rotation on
T^3), not merely theory-indicated.

Caveat (honest): this is an in-sandbox implementation validated on 5 controls, not
a run of a peer-reviewed library; independent/library confirmation still welcome.
No physics.
"""
from collections import defaultdict, deque

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def decompose(u, v, alph):
    idx = {c: i for i, c in enumerate(alph)}
    diff = [0] * len(alph)
    pts = [0]
    for k in range(len(u)):
        diff[idx[u[k]]] += 1
        diff[idx[v[k]]] -= 1
        if not any(diff):
            pts.append(k + 1)
    return [(u[pts[i]:pts[i + 1]], v[pts[i]:pts[i + 1]]) for i in range(len(pts) - 1)]


def pure_discrete(sub, alph, wordlen=60000, maxlen=200, cap=50000):
    """Return (is_discrete, n_reachable, n_bad, max_word_len) or a diagnostic tuple."""
    S = lambda w: ''.join(sub[c] for c in w)
    u = alph[0]
    while len(u) < wordlen:
        u = ''.join(sub[c] for c in u)
    u = u[:wordlen]
    facs = set()
    for L in range(1, maxlen + 1):
        facs |= {u[i:i + L] for i in range(0, len(u) - L)}
    occ = lambda w: w in facs

    seed = set()
    for a in alph:
        for b in alph:
            if a == b:
                continue
            for p in decompose(S(a) + S(b), S(b) + S(a), alph):
                if occ(p[0]) and occ(p[1]):
                    seed.add(p)
    reach = set(seed)
    dq = deque(seed)
    child = defaultdict(set)
    immediate = {}
    ml = 0
    while dq:
        x, y = dq.popleft()
        ml = max(ml, len(x))
        if len(x) > maxlen:
            return ('BLOWUP', len(reach))
        pieces = decompose(S(x), S(y), alph)
        immediate[(x, y)] = any(pu == pv for pu, pv in pieces)
        for pu, pv in pieces:
            if pu != pv:
                if not (occ(pu) and occ(pv)):
                    continue
                child[(x, y)].add((pu, pv))
                if (pu, pv) not in reach:
                    reach.add((pu, pv))
                    dq.append((pu, pv))
                    if len(reach) > cap:
                        return ('CAP', len(reach))
    rev = defaultdict(set)
    for p, ks in child.items():
        for q in ks:
            rev[q].add(p)
    good = set(p for p in reach if p[0] != p[1] and immediate.get(p))
    dq = deque(good)
    while dq:
        q = dq.popleft()
        for p in rev[q]:
            if p not in good:
                good.add(p)
                dq.append(p)
    bad = [p for p in reach if p[0] != p[1] and p not in good]
    return (len(bad) == 0, len(reach), len(bad), ml)


CONTROLS = [
    ('Fibonacci', {'a': 'ab', 'b': 'a'}, 'ab', True),
    ('Tribonacci', {'a': 'ab', 'b': 'ac', 'c': 'a'}, 'abc', True),
    ('period-doubling', {'a': 'ab', 'b': 'aa'}, 'ab', True),
    ('Thue-Morse', {'a': 'ab', 'b': 'ba'}, 'ab', False),
    ('Chacon(weak-mix)', {'a': 'aaba', 'b': 'b'}, 'ab', False),
]

if __name__ == "__main__":
    print("controls (validation):")
    allok = True
    for name, sub, alph, want in CONTROLS:
        r = pure_discrete(sub, alph)
        ok = r[0] == want
        allok &= ok
        print(f"  {name:18s}: discrete={r[0]}  reach={r[1]}  (expected {want})  {'OK' if ok else 'MISMATCH'}")
    print("  ALL CONTROLS CORRECT:", allok)
    print("\nthe object:")
    r = pure_discrete(SUB, 'abAB')
    print(f"  pure discrete spectrum = {r[0]}   balanced pairs={r[1]}  bad={r[2]}  max word len={r[3]}")
