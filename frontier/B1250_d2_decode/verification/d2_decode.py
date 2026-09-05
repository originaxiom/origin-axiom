#!/usr/bin/env python3
"""B1250 -- THE D2 DECODE: the twist is the SO(10) grading of E6.

M1 on B926's surviving-shapes menu ("the strongest positive structure") has a stage (a) that
B926 marks explicitly UNAFFECTED BY THE OWNER GATE: "decode D2 -- what IS the 11-flip as a
character/Galois object?"  B916 answered NO at a necessary condition and registered a refined
question. This arc answers it POSITIVE.

WHAT B916 TESTED AND WHAT IT MISSED.  B916 searched the PLAIN character (-1)^<a,w>, a in F2^6
(64 candidates), and found none -- reproduced here, 0 solutions. The AFFINE form
(-1)^(<a,w>+1) was one bit outside that search space, and there the answer is unique:

    D2(w) = (-1)^(<w13, w> + 1),   w13 = [1, 0, -1, 0, 1, -1]

exact on all 27 weights, with w13 ITSELF one of the 27 (and itself flipped). Exactly one weight
of the 27 generates it.

NOT A FIT: 2^7 = 128 candidate affine characters against 2^27 = 134,217,728 sign patterns, so a
chance match is ~1 in 10^6. CONTROL (MB12, two-sided): 0 of 4000 random 11-subsets of the 27
admit an affine character -- the test almost always says NO.

THE DECODE, EARNED NOT DIMENSION-MATCHED.  A root vector sends w -> w + alpha, so the flip parity
changes by <w13, alpha> mod 2. The roots EVEN against w13 therefore preserve the flip class and
generate the character's stabiliser. Computed from the B883 rep (72 roots recovered cleanly; e6
has 72):

    even roots 40  ->  stabiliser dim 6 + 40 = 46 = dim(so(10) + u(1))
    odd  roots 32  ->  complement dim 32 = 16 + 16bar

and the ORBITS of the 27 under that stabiliser are [1, 10, 16] -- the SO(10) branching. The
singlet block is exactly {w13}. The flips are exactly the 1 and the 10; the 16 is untouched:

    D2 FLIPS THE 1 + 10 AND FIXES THE 16.

The identification is EARNED by the B1223 template: the subalgebra is exhibited (as the character's
stabiliser) and it ACTS (its orbits are computed and give 1+10+16), rather than matched by dimension.

B916's "11 = 8 + 3 (one octet plus three vacuum lines)" guess is CORRECTED: the split is 1 + 10.

CONSEQUENCE FOR M1. B926's stated risk was that the decode "may dissolve the twist into convention
(then the shape dies honestly)". It does not: the generator is unique and the control is 0/4000.
In E6 GUTs the 16 is one Standard Model generation and the 1+10 is the Higgs/exotic sector, so the
twist carries the matter/Higgs split. M1 SURVIVES ITS STAGE-(a) TEST.

NOT CLAIMED: no physical gauge theory, no dynamics, no measured value, no crossing. That the 16
"is a generation" is standard GUT nomenclature for the representation, NOT a derivation that this
object produces Standard Model matter. Gate 5 clean.
"""
import collections
import itertools
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[3]


def _load():
    rep = json.loads((ROOT / "frontier" / "B883_the_27" / "rep27.json").read_text())
    res = json.loads((ROOT / "frontier" / "B916_lambda_bridge" / "results.json").read_text())
    return rep["weights"], rep["rep"], res["H_prime_diag_vs_H_plus"]["D2"]


def flip_set():
    wts, _, D2 = _load()
    return wts, {i for i, s in enumerate(D2) if s == -1}


def plain_character_solutions():
    """B916's search space: (-1)^<a,w>, i.e. ODD -> flip. Must be empty."""
    wts, flip = flip_set()
    out = []
    for a in itertools.product([0, 1], repeat=6):
        pred = {i for i, w in enumerate(wts) if sum(x * y for x, y in zip(a, w)) % 2 == 1}
        if pred == flip:
            out.append(a)
    return out


def affine_character_solutions():
    """The one-bit-wider space: (-1)^(<a,w>+1), i.e. EVEN -> flip."""
    wts, flip = flip_set()
    out = []
    for a in itertools.product([0, 1], repeat=6):
        pred = {i for i, w in enumerate(wts) if sum(x * y for x, y in zip(a, w)) % 2 == 0}
        if pred == flip:
            out.append(a)
    return out


def generating_weights():
    """Which of the 27 weights, used as the character vector, reproduce D2 exactly."""
    wts, flip = flip_set()
    return [j for j, v in enumerate(wts)
            if {i for i, w in enumerate(wts)
                if (sum(x * y for x, y in zip(v, w)) + 1) % 2 == 1} == flip]


def roots():
    """Recover each root alpha from its root vector's action on the 27."""
    wts, G, _ = _load()
    out = {}
    for k in range(6, 78):
        M = G[str(k)]
        for i in range(27):
            hit = False
            for j in range(27):
                if M[i][j]:
                    out[k] = tuple(x - y for x, y in zip(wts[i], wts[j]))
                    hit = True
                    break
            if hit:
                break
    return out


def stabiliser_blocks():
    """Orbits of the 27 under the roots EVEN against w13 (the character's stabiliser)."""
    wts, G, _ = _load()
    w13 = wts[13]
    rts = roots()
    even = [k for k, a in rts.items() if sum(x * y for x, y in zip(w13, a)) % 2 == 0]
    adj = collections.defaultdict(set)
    for k in even:
        M = G[str(k)]
        for i in range(27):
            for j in range(27):
                if M[i][j]:
                    adj[i].add(j)
                    adj[j].add(i)
    seen, blocks = set(), []
    for s in range(27):
        if s in seen:
            continue
        comp, st = {s}, [s]
        while st:
            x = st.pop()
            for y in adj[x]:
                if y not in comp:
                    comp.add(y)
                    st.append(y)
        seen |= comp
        blocks.append(sorted(comp))
    return len(even), len(rts) - len(even), sorted(blocks, key=len)


def control_random_subsets(trials=4000, seed=11):
    """MB12 two-sided: how often does a random 11-subset admit an affine character?"""
    import random
    wts, _, _ = _load()
    rng = random.Random(seed)
    hits = 0
    for _ in range(trials):
        tgt = set(rng.sample(range(27), 11))
        for a in itertools.product([0, 1], repeat=6):
            for c in (0, 1):
                if {i for i, w in enumerate(wts)
                        if (sum(x * y for x, y in zip(a, w)) + c) % 2 == 1} == tgt:
                    hits += 1
                    break
            else:
                continue
            break
    return hits, trials


def selftest(verbose=True):
    fails = []
    wts, flip = flip_set()
    if len(flip) != 11:
        fails.append(f"D2 has {len(flip)} flips, expected 11")
    sums = collections.Counter(sum(wts[i]) for i in flip)
    if dict(sums) != {-1: 2, 0: 7, 1: 2}:
        fails.append(f"flip weight-sums {dict(sums)} != B916's {{-1:2,0:7,1:2}}")
    if plain_character_solutions():
        fails.append("B916's kill FAILED to reproduce: a plain character exists")
    aff = affine_character_solutions()
    if aff != [(1, 0, 1, 0, 1, 1)]:
        fails.append(f"affine solutions {aff} != [(1,0,1,0,1,1)]")
    gen = generating_weights()
    if gen != [13]:
        fails.append(f"generating weights {gen} != [13]")
    if 13 not in flip:
        fails.append("the generator w13 is not itself flipped")
    ne, no, blocks = stabiliser_blocks()
    if (ne, no) != (40, 32):
        fails.append(f"even/odd roots ({ne},{no}) != (40,32)")
    if [len(b) for b in blocks] != [1, 10, 16]:
        fails.append(f"stabiliser blocks {[len(b) for b in blocks]} != [1,10,16]")
    else:
        if blocks[0] != [13]:
            fails.append(f"the singlet block is {blocks[0]}, expected [13]")
        if set(blocks[0]) | set(blocks[1]) != flip:
            fails.append("the 1 + 10 is not exactly the flip set")
        if set(blocks[2]) & flip:
            fails.append("the 16 is not entirely unflipped")
    if verbose:
        print(f"  [flip] 11 flips, sums {dict(sums)}")
        print(f"  [B916] plain-character solutions: {len(plain_character_solutions())}  (kill reproduced)")
        print(f"  [new ] affine solutions: {aff};  generating weight of the 27: {gen}")
        print(f"  [alg ] even roots {ne}, odd {no} -> stabiliser dim {6+ne} = so(10)+u(1); complement {no} = 16+16bar")
        print(f"  [orb ] blocks {[len(b) for b in blocks]}; singlet = {blocks[0]}; flips = 1 + 10; the 16 untouched")
    return fails


if __name__ == "__main__":
    print("B1250 -- the D2 decode (selftest)")
    f = selftest()
    h, t = control_random_subsets()
    print(f"  [ctl ] random 11-subsets admitting an affine character: {h}/{t}")
    if h > 20:
        f.append(f"control too permissive: {h}/{t}")
    print()
    print("SELFTEST:", "PASS" if not f else "FAIL")
    for x in f:
        print("   !", x)
    raise SystemExit(1 if f else 0)
