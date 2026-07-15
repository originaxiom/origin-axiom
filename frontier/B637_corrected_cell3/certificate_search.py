"""B637 part 2b-i — the van Kampen certificate: express the peripheral
commutator [lambda, mu] = LONG a LONG^-1 a^-1 as a product of conjugates
of the relator r = abABaBAbaB (the one irreducible word-problem instance
the T.H homotopy formula needs; see DERIVATION.md).

Beam search: moves = insert u r^{+-1} u^{-1} implicitly by splicing
r^{+-1} at any position, then free-reduce; track (position, sign)
history = the certificate. Verified afterwards by exact free-group
reconstruction.
"""
import heapq

REL = "abABaBAbaB"
RELI = REL[::-1].swapcase()
LONG = "abABaaBAbA"


def freduce(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase():
            out.pop()
        else:
            out.append(ch)
    return "".join(out)


def inv(w):
    return w[::-1].swapcase()


TARGET = freduce(LONG + "a" + inv(LONG) + "A")
print(f"target [lambda,mu] (reduced, len {len(TARGET)}): {TARGET}", flush=True)

# beam search: state = reduced word; move = insert REL or RELI at pos i
BEAM = 400
MAXDEPTH = 12
seen = {TARGET: (None, None, None)}          # word -> (parent, pos, sign)
beam = [(len(TARGET), TARGET)]
found = None
for depth in range(1, MAXDEPTH + 1):
    cand = {}
    for _, w in beam:
        for ins, sgn in ((REL, +1), (RELI, -1)):
            for i in range(len(w) + 1):
                nw = freduce(w[:i] + ins + w[i:])
                if nw in seen or nw in cand:
                    continue
                cand[nw] = (w, i, sgn)
    for nw, meta in cand.items():
        seen[nw] = meta
    if "" in cand:
        found = ""
        print(f"CERTIFICATE FOUND at depth {depth}", flush=True)
        break
    beam = heapq.nsmallest(BEAM, ((len(nw), nw) for nw in cand))
    if not beam:
        break
    print(f"depth {depth}: best length {beam[0][0]}, beam {len(beam)}",
          flush=True)

assert found is not None, "search failed within depth/beam limits"

# reconstruct the certificate: walking back from "" to TARGET, each step
# REMOVED r^{+-1}; forward direction: TARGET = product of conjugates.
steps = []
w = ""
while seen[w][0] is not None:
    parent, i, sgn = seen[w]
    steps.append((parent, i, sgn))
    w = parent
# steps run from "" back to TARGET: forward: TARGET -> ... -> "" by inserting
# r^{-sign}; so TARGET = prod over steps (in order) of conjugates of r^{+sign}.
print(f"certificate: {len(steps)} relator cells", flush=True)

# exact verification: replay the recorded chain from TARGET to "":
chain = []
node = ""
while seen[node][0] is not None:
    parent, i, sgn = seen[node]
    chain.append((node, parent, i, sgn))
    node = parent
chain.reverse()              # now runs TARGET -> ... -> ""
w = TARGET
ok = True
for (child, parent, i, sgn) in chain:
    assert parent == w
    ins = REL if sgn > 0 else RELI
    w = freduce(w[:i] + ins + w[i:])
    assert w == child, "replay mismatch"
print(f"replay verified: TARGET -> '' in {len(chain)} insertions", flush=True)
print("certificate steps (parent-position-sign):", flush=True)
for (child, parent, i, sgn) in chain:
    print(f"  insert r^{'+1' if sgn>0 else '-1'} at pos {i:2d} of "
          f"len-{len(parent)} word", flush=True)
import json
with open(__file__.replace("certificate_search.py", "certificate.json"),
          "w") as f:
    json.dump([[parent, i, sgn] for (child, parent, i, sgn) in chain], f)
print("certificate.json written", flush=True)
