"""Audit: re-derive orbit_law.py's sample rule and the level-3 torsion selection, using first_background (unchanged)."""
import sys, math, itertools
sys.path.insert(0, sys.argv[1])
import first_background as F
def canon(w):
    sw = w.translate(str.maketrans('LR', 'RL'))
    return min(min(x[i:] + x[:i] for i in range(len(x))) for x in (w, sw, w[::-1], sw[::-1]))
def canon_noreverse(w):
    sw = w.translate(str.maketrans('LR', 'RL'))
    return min(min(x[i:] + x[:i] for i in range(len(x))) for x in (w, sw))
words = sorted({canon(''.join(t)) for k in range(2, 7) for t in itertools.product('LR', repeat=k) if 'L' in t and 'R' in t}, key=lambda s: (len(s), s))
words_nr = sorted({canon_noreverse(''.join(t)) for k in range(2, 7) for t in itertools.product('LR', repeat=k) if 'L' in t and 'R' in t}, key=lambda s: (len(s), s))
print('words (rotation+swap+reversal):', len(words), '; without reversal:', len(words_nr))
prod = lambda t: math.prod(t) if t else 1
for w in words:
    t2 = prod(F.torsion(F.mono(w), 2)[0]); t3p = prod(F.torsion(F.mono(w), 3)[0]); t3m = prod(F.torsion(F.mono('I' + w), 3)[0])
    print(f"  {w:8s} L2 torsion {t2:6d} {'IN ' if t2 <= 200 else 'OUT'}   L3 torsion +{t3p:7d}  -{t3m:7d}")
