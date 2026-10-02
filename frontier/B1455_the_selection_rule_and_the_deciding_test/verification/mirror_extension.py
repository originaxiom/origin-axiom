#!/usr/bin/env python3
"""B1455, POST-SEAL EXTENSION (labelled as such in FINDINGS) -- the orientation-reversing symmetries.

The sealed population was the eight signed permutations of Ballas' generators; four are automorphisms and all four
preserve orientation (P1 failed).  The mirrors are found here by search: tau(m) = m^e, tau(n) = g x g^-1 with x a
generator or its inverse and g a reduced word, such that the SL(2,C) holonomy's character is complex-conjugated.
A pair of parabolics with the conjugate character is conjugate to the conjugate representation, so the relator holds
and tau is an automorphism (the image is a lattice of the same covolume inside the group's image).

    python3 mirror_extension.py      # prints, writes mirror_extension.json
"""
import itertools, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mirror_on_the_family as R1
from fractions import Fraction as F

g2, mm2, E = R1.geo()
def w2(w):
    A = [[E(1), E(0)], [E(0), E(1)]]
    for c in w: A = mm2(A, g2[c])
    return A
def t2(w):
    A = w2(w); return A[0][0] + A[1][1]
def reduce_word(w):
    out = []
    for c in w:
        if out and out[-1] == c.swapcase(): out.pop()
        else: out.append(c)
    return "".join(out)
def reduced_words(maxlen):
    yield ""
    for L in range(1, maxlen + 1):
        for w in itertools.product("mnMN", repeat=L):
            w = "".join(w)
            if all(w[i] != w[i + 1].swapcase() for i in range(L - 1)): yield w

def substitute(a, b, w):
    img = {"m": a, "n": b, "M": R1.inv_word(a), "N": R1.inv_word(b)}
    return reduce_word("".join(img[c] for c in w))

target_plain, target_conj = t2("mn"), t2("mn").conj()
assert target_plain != target_conj
zw = list(R1.zero_sum_words(5))
found = {"reversing": [], "preserving": []}
for e in ("m", "M"):
    for g in reduced_words(4):
        for x in "mnMN":
            b = reduce_word(g + x + R1.inv_word(g))
            if not b or t2(b) != E(2): continue
            tp = t2(e + b)
            kind = "reversing" if tp == target_conj else "preserving" if tp == target_plain else None
            if kind is None: continue
            # confirm on every zero-sum word, and that the relator goes to the identity
            R = w2(substitute(e, b, R1.REL)); 
            if R != [[E(1), E(0)], [E(0), E(1)]]: continue
            good = all(t2(substitute(e, b, w)) == (t2(w).conj() if kind == "reversing" else t2(w)) for w in zw)
            if good: found[kind].append((e, b))
# the shortest of each kind, and the classification of rho_q o tau
out = {"counts": {k: len(v) for k, v in found.items()}}
print("automorphisms found with tau(m) = m^+-1 and tau(n) a conjugate of a generator by a word of length <= 4:", out["counts"])
TARGET_CHARS = {str(q): {k: R1.chars(v) for k, v in R1.targets(q).items()} for q in R1.QS}      # computed once
SHORT = [w for w in R1.WORDS if len(w) <= 6]


def chars_of(pulled, maxlen):
    out = {}; level = {"": R1.ident(4)}
    for L in range(1, maxlen + 1):
        nxt = {}
        for w, A in level.items():
            for c in "mn":
                B = R1.mul(A, pulled[c]); nxt[w + c] = B; out[w + c] = R1.tr(B)
        level = nxt
    return out


def classify(a, b, maxlen=10):
    res = {}
    words = R1.WORDS if maxlen == 10 else SHORT
    for q in R1.QS:
        g = R1.ballas(q); pulled = {"m": R1.word(a, g), "n": R1.word(b, g)}
        cs = chars_of(pulled, maxlen)
        res[str(q)] = [k for k, v in TARGET_CHARS[str(q)].items() if all(cs[w] == v[w] for w in words)]
        tl, tli = R1.tr(R1.word(R1.LONG, g)), R1.tr(R1.word(R1.inv_word(R1.LONG), g))
        ts = R1.tr(R1.word(substitute(a, b, R1.LONG), g))
        res[str(q) + " longitude"] = "l" if ts == tl else "l^-1" if ts == tli else "neither"
    return res
rows = []
for kind in ("reversing", "preserving"):
    for a, b in sorted(found[kind], key=lambda p: (len(p[1]), p))[:6]:
        c = classify(a, b); rows.append(dict(kind=kind, m_to=a, n_to=b, classes=c))
        print("  %-10s m -> %-2s n -> %-12s rho_q o tau ~ %s   longitude -> %s" % (kind, a, b, sorted({tuple(v) for k, v in c.items() if "longitude" not in k}), sorted({v for k, v in c.items() if "longitude" in k})))
out["rows"] = rows
allrev = [classify(a, b, maxlen=6) for a, b in found["reversing"]]          # every one, on words to length 6
out["every_reversing_map"] = sorted({tuple(tuple(v) for k, v in sorted(c.items()) if "longitude" not in k) for c in allrev})
print("every orientation-reversing map found, by what rho_q o tau is conjugate to (per q):", out["every_reversing_map"])
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mirror_extension.json"), "w"), indent=1)
