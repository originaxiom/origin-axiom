#!/usr/bin/env python3
"""B456 (Ethogram E4) — THE CATALOG: every observed behavior as a typed signature;
the null catalogs run through the same extraction; frozen with a hash.

Signatures use B452's typed format: (kind, ints, discs, values). No physics language.
"""
import hashlib
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "B452_ethogram_dictionary"))
from registry import signature

# ---------------- THE OBJECT'S CATALOG (from banked probes B446-B459) ----------------
OBJECT_CATALOG = [
    # reproduction & lineage (B453)
    signature("reproduction-once-no-heredity", ints=(1,), discs=(-283,)),
    signature("identical-child-two-parents", ints=(5, 1), discs=(-283,)),      # 4_1(5,1)=5_2(5,1)
    signature("cover-isolation", ints=(1,), discs=()),                          # one subgroup idx<=6
    signature("cover-torsion-lucas", ints=(11, 11, 121), discs=()),             # L_5^2 launder
    # growth & exhaustion (B454)
    signature("word-closure-lemma", ints=(), discs=(-3,)),                      # never leaves Q(sqrt-3)
    signature("deterministic-growth", ints=()),
    # the beats (B446/B447/B448)
    signature("pulse-cocycle-2cycle", ints=(2,), values=(0.010417735, 0.074495779)),
    signature("pulse-pisano-revival", ints=(60, 180, 540)),                     # ord = pi(N)/2
    signature("pulse-logperiodic-peaks", ints=(3, 3, 2, 2, 1, 1)),              # C(T) peak counts, m=1..6
    signature("orbit-tower-fields", ints=(1, 2, 4, 5, 6), discs=(-3, -7, -3)),  # periods -> fields
    signature("markov-surface", ints=(3, 3, 3)),                                # kappa=-2 = Markov
    # response (B455)
    signature("response-flat-to-3rd-order", ints=(3,)),
    signature("no-homeostasis", ints=()),                                       # retired card
    # component content (B458)
    signature("component-cs-zero", ints=(0,), discs=(-7,), values=()),          # V1/V2 cvol = 0
    signature("sym2-volume-factor", ints=(4,), values=()),                      # 4*Vol exact
    # quantum signatures (verified in-session; Zagier territory)
    signature("kashaev-small-integers", ints=(1, 5, 13, 27, 89)),
    signature("kashaev-sqrt5-at-5", ints=(46, 2), discs=(5,)),                  # 46+2sqrt5 (B384)
    # the selection-rule lattice (B459)
    signature("vanishing-subfield-lattice", ints=(120, 20, 20, 10, 70), discs=(5, -3, -15)),
    signature("no-pure-sqrt-15-values", ints=(0,), discs=(-15,)),
    # arithmetic ratios (B420/B449 confirmations)
    signature("l-ratio", values=(float(np.sqrt(5)) / 6,)),                      # sqrt5/6 in (0,1)
    signature("conductor-law", ints=(15, 8), discs=(-3, 5, -4, 8)),             # golden 15, silver 8
]

# ---------------- NULL CATALOGS (same extraction, the environment) ----------------
def word_signatures(word):
    """the word-channel extraction: closure (universal), the dynamics disc, the 2-cycle."""
    sigs = [signature("word-closure-lemma", ints=(), discs=(-3,))]   # Fricke: universal
    # dynamics disc: charpoly disc of the word's {R,L}-matrix product
    R = np.array([[1, 1], [0, 1]], dtype=object)
    L = np.array([[1, 0], [1, 1]], dtype=object)
    M = np.eye(2, dtype=object)
    for c in word:
        M = M @ (R if c == 0 else L)
    tr = int(M[0, 0] + M[1, 1])
    disc = tr * tr - 4
    # squarefree kernel
    d, k = abs(disc), 1
    i = 2
    while i * i <= d:
        while d % (i * i) == 0:
            d //= i * i
        i += 1
    sf = (1 if disc >= 0 else -1) * d
    sigs.append(signature("dynamics-disc", ints=(tr,), discs=(sf,)))
    sigs.append(signature("pulse-cocycle-2cycle", ints=(2,)))        # generic mechanism (B448)
    return sigs


def build_nulls(n_random=1000, length=21, seed=20260708):
    rng = np.random.default_rng(seed)
    nulls = []
    # Thue-Morse
    tm = [0]
    for _ in range(5):
        tm = [c for x in tm for c in ((0, 1) if x == 0 else (1, 0))]
    nulls.append(("thue-morse", word_signatures(tm[:length])))
    # random words (the p-value channel)
    for i in range(n_random):
        w = rng.integers(0, 2, length).tolist()
        nulls.append((f"rand{i}", word_signatures(w)))
    # foreign knots (knot channel: adjudication only, no p) - from banked B444/B453/B458 data
    nulls.append(("5_2", [
        signature("identical-child-two-parents", ints=(5, 1), discs=(-283,)),   # it IS the same child
        signature("cover-torsion-lucas", ints=(11, 11, 121), discs=()),
        signature("component-cs-nonzero", ints=(1,), discs=(5,),
                  values=(0.480983991, 0.657973627, 0.620799352, 0.581975038)),
        signature("sym2-volume-factor", ints=(4,)),
        signature("word-closure-lemma", ints=(), discs=(-23,)),
    ]))
    nulls.append(("6_1", [
        signature("cover-torsion-lucas", ints=(31, 31, 961), discs=()),
        signature("word-closure-lemma", ints=(), discs=()),
    ]))
    # silver/bronze (class)
    nulls.append(("silver", [
        signature("pulse-logperiodic-peaks", ints=(3, 3, 2, 2, 1, 1)),          # the SAME m-scan family data
        signature("orbit-tower-fields", ints=(1, 2), discs=(-4, -3, -15)),      # B448 silver gate/beat
        signature("conductor-law", ints=(8,), discs=(-4, 8)),
        signature("pulse-cocycle-2cycle", ints=(2,), values=(0.0227, 0.0411)),
    ]))
    return nulls


def main():
    nulls = build_nulls()
    payload = dict(object_catalog=[list(map(list, [s[1], s[2], s[3]])) + [s[0]] for s in OBJECT_CATALOG],
                   nulls={name: [list(map(list, [s[1], s[2], s[3]])) + [s[0]] for s in cat]
                          for name, cat in nulls})
    txt = json.dumps(payload, sort_keys=True)
    h = hashlib.sha256(txt.encode()).hexdigest()
    json.dump(dict(sha256=h, **payload), open("catalog_frozen.json", "w"), indent=1, sort_keys=True)
    print(f"object catalog: {len(OBJECT_CATALOG)} behaviors")
    print(f"nulls: {len(nulls)} catalogs (incl. {sum(1 for n, _ in nulls if n.startswith('rand'))} random words)")
    print(f"FROZEN sha256 = {h}")


if __name__ == "__main__":
    main()
