#!/usr/bin/env python3
"""T1 and T2 of tick_facts.py, CORRECTED AFTER THE SEAL (post hoc; labelled).

The sealed script tested primitivity on the run SEQUENCE where it belongs on the WORD. A two-act history whose run
sequence is s.s with |s| odd is a primitive word (LR is (1,1)), and the sealed script dropped every one of them; it
also counted histories up to the mirror. Found by the seat on reading the sealed output (the class 'double of an odd
sequence' came out empty). T3 and T4 are unaffected and are not repeated here.
    python3 relays/advisor_2026-11-10_audit/principle_top_down/the_tick/tick_facts_corrected.py"""
import itertools, warnings
warnings.filterwarnings("ignore")
def necklaces(n, alphabet="LR"):
    seen = set()
    for w in itertools.product(alphabet, repeat=n):
        w = "".join(w); key = min(w[i:] + w[:i] for i in range(n))
        if key in seen: continue
        seen.add(key)
        if any(n % d == 0 and w == w[:d] * (n // d) for d in range(1, n)): continue      # a proper power as a WORD
        yield key
def runs(w):                       # cyclic run sequence, started at the beginning of an L-run
    i = next(i for i in range(len(w)) if w[i] == "L" and w[i - 1] == "R")
    w = w[i:] + w[:i]
    return tuple(len(list(g)) for _, g in itertools.groupby(w))
def odd_sequences(n):              # primitive cyclic sequences of positive integers with sum n and an odd number of parts
    seen = set()
    def comps(n):
        if n == 0: yield (); return
        for r in range(1, n + 1):
            for rest in comps(n - r): yield (r,) + rest
    for c in comps(n):
        if len(c) % 2 == 0: continue
        key = min(c[i:] + c[:i] for i in range(len(c)))
        if key in seen: continue
        seen.add(key)
        if any(len(c) % d == 0 and c == c[:d] * (len(c) // d) for d in range(1, len(c))): continue
        yield key
print("T1 (corrected)  histories with n letters: two-act histories (primitive cyclic words with both letters) / the tick's own (an odd number of runs)")
for n in range(1, 13):
    two = [w for w in necklaces(n) if "L" in w and "R" in w]
    print("    n = %2d: two-act %-4d tick-only %-4d" % (n, len(two), len(list(odd_sequences(n)))))
import snappy
def predicted(seq):
    k = len(seq)
    if any(seq[s:] + seq[:s] == seq for s in range(1, k, 2)): return "odd rotation"
    rev = seq[::-1]
    if any(rev[s:] + rev[:s] == seq and (k - 1 - s) % 2 == 1 for s in range(k)): return "parity-changing reflection"
    return None
print("T2 (corrected)  every two-act history with at most 8 letters: amphicheiral (SnapPy) against the prediction")
classes = {"double of an odd sequence": [], "its own mirror another way": [], "has a mirror partner": []}
tot = agree = 0; bad = []
for n in range(2, 9):
    for w in necklaces(n):
        if "L" not in w or "R" not in w: continue
        seq = runs(w); k = len(seq); half = k // 2
        amph = bool(snappy.Manifold("b++" + w).symmetry_group().is_amphicheiral()); pred = predicted(seq)
        dbl = half % 2 == 1 and seq[:half] == seq[half:]
        cls = "double of an odd sequence" if dbl else ("its own mirror another way" if pred else "has a mirror partner")
        classes[cls].append((w, amph)); tot += 1; agree += (amph == bool(pred))
        if amph != bool(pred): bad.append((w, seq, amph, pred))
print("    histories checked: %d; SnapPy agrees with the prediction on %d; disagreements: %s" % (tot, agree, bad[:5]))
for c, items in classes.items():
    print("    %-28s %3d histories, %3d amphicheiral   e.g. %s" % (c, len(items), sum(a for _, a in items), [w for w, _ in items[:6]]))
