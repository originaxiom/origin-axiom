#!/usr/bin/env python3
"""Review 80: main's own computation of four things the readers' files say of B1895.
  (1) the SM seat's finding 23: the second convention's word, BUILT, is the seat's word conjugated by the swap, on every sequence;
  (2) its finding 24: is the allowed set closed under reversal for a mark that does not annihilate its own line?
  (3) agy-exp's first derivation: the swapped-mark recipe agrees on all 120 matrices at the two marks that annihilate their own
      line and on 88 of 120 at each of the other four;
  (4) agy-exp's second derivation: over every cyclic run sequence the least reading is the all-ones' and the second-least the
      all-twos', every other sequence reading above 17/12.
B1881's script is imported for its reading of a run sequence (heights), as B1895's own script does.  Integers and 50 digits; no
measured number."""
# NOTE OF THE MEND, 2026-11-13 (C16; owed by main's word in M22, a cold reader's finding that main checked: main's two
# check files set their root to the folder above their own, which is not the repository's root, and run in place they stop
# at their first search).  Main's script stands as main wrote it in ../checks/, held there by its hash.  This copy differs in
# the marked place: the line main wrote stands after "#| ", the line that replaces it follows, to "# END OF THE MEND".  With
# the marked block put back, and this note taken out, the file is main's, byte for byte: the arc's lock holds that.
#   0. the repository's root was counted one folder up from the script's own, which is right where main ran it and wrong here.
# END OF THE NOTE
import importlib.util, itertools, json, pathlib
import mpmath as mp
# MENDED (0).  Main wrote:
#| HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
HERE = pathlib.Path(__file__).resolve().parent; ROOT = next(p for p in HERE.parents if (p / "scripts" / "gates" / "gates.py").is_file())
# END OF THE MEND
src = next((ROOT / "frontier").glob("B1881_*/verification/whole_and_value_on_main.py"))
spec = importlib.util.spec_from_file_location("b1881_script", src); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
mp.mp.dps = 50
mul = lambda A, B: (A[0] * B[0] + A[1] * B[2], A[0] * B[1] + A[1] * B[3], A[2] * B[0] + A[3] * B[2], A[2] * B[1] + A[3] * B[3])
m5 = lambda A: tuple(x % 5 for x in A)
J, I2 = (0, 1, 1, 0), (1, 0, 0, 1)
Ls, Rs = (1, 0, 1, 1), (1, 1, 0, 1)                 # the seat's letters (rows)
L2, R2 = (1, 1, 0, 1), (1, 0, 1, 1)                 # the second convention's letters (columns)
def word(seq, a, b):
    W = I2
    for k, r in enumerate(seq):
        for _ in range(r): W = mul(W, a if k % 2 == 0 else b)
    return W
row = lambda v, g: ((v[0] * g[0] + v[1] * g[2]) % 5, (v[0] * g[1] + v[1] * g[3]) % 5)
col = lambda g, v: ((g[0] * v[0] + g[1] * v[1]) % 5, (g[2] * v[0] + g[3] * v[1]) % 5)
line = lambda w: min(((k * w[0]) % 5, (k * w[1]) % 5) for k in (1, 2, 3, 4))
VECS = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]; LINES = sorted({line(w) for w in VECS})
kept_row = lambda v, g: line(row(v, g)) == line(v); kept_col = lambda g, u: line(col(g, u)) == line(u)
own = lambda v: (v[0] * v[0] + v[1] * v[1]) % 5 == 0   # the mark annihilates its own line
seqs = [seq for n in (2, 4) for seq in itertools.product(range(1, 7), repeat=n)]
OUT = {}
# (1)
same = sum(1 for seq in seqs if word(seq, L2, R2) == mul(mul(J, word(seq, Ls, Rs)), J))
OUT["(1) sequences"] = len(seqs); OUT["(1) the second word, built over the integers, equals J W J"] = same
print("(1) %d sequences of length 2 and 4 with runs to 6; the second convention's word, built letter by letter over the integers, equals the swap-conjugate of the seat's on %d" % (len(seqs), same))
# (2)
diff = {}
for v in LINES:
    d = sum(1 for seq in seqs if kept_row(v, m5(word(seq, Ls, Rs))) != kept_row(v, m5(word(tuple(reversed(seq)), Ls, Rs))))
    diff[str(v)] = {"annihilates its own line": own(v), "sequences whose reversal is allowed differently": d}
OUT["(2)"] = diff
print("(2) of the %d sequences, how many are allowed differently from their reversal, mark by mark:" % len(seqs))
for v, x in diff.items(): print("      mark %s  annihilates its own line: %-5s  %d" % (v, x["annihilates its own line"], x["sequences whose reversal is allowed differently"]))
# (3)
G, todo = {I2}, [I2]
while todo:
    g = todo.pop()
    for h in (m5(mul(g, (0, 4, 1, 0))), m5(mul(g, (1, 1, 0, 1)))):
        if h not in G: G.add(h); todo.append(h)
agree = {str(v): sum(1 for g in G if kept_row(v, g) == kept_col(m5(mul(mul(J, g), J)), (v[1], v[0]))) for v in LINES}
OUT["(3) matrices"] = len(G); OUT["(3) agreement of the swapped-mark recipe, mark by mark"] = {v: {"annihilates its own line": own(eval(v)), "of 120": a} for v, a in agree.items()}
print("(3) %d matrices; 'row v kept by W' against 'column J v kept by J W J', mark by mark:" % len(G), {v: a for v, a in agree.items()}, "| marks that annihilate their own line:", [str(v) for v in LINES if own(v)])
# (4)
def canon(seq): return min(tuple(seq[i:] + seq[:i]) for i in range(len(seq)))
cyc = set()
for n, top in ((1, 9), (2, 9), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 3), (9, 2), (10, 2), (12, 2)):
    for seq in itertools.product(range(1, top + 1), repeat=n): cyc.add(canon(seq))
def primitive(seq):
    n = len(seq); return not any(n % d == 0 and seq == seq[:d] * (n // d) for d in range(1, n))
prim = sorted(c for c in cyc if primitive(c))
r5, r2, b = mp.sqrt(5) / 2, mp.sqrt(2), mp.mpf(17) / 12
read = {}
for c in prim:
    seq = list(c) if len(c) % 2 == 0 else list(c) * 2          # B1881's reading takes sequences of even length
    read[c] = max(S.heights(seq))
ones, twos = read[(1,)], read[(2,)]
others = {c: h for c, h in read.items() if c not in ((1,), (2,))}
low = min(others.values()); where = [c for c, h in others.items() if h == low]
OUT["(4)"] = {"primitive cyclic sequences read": len(prim), "all ones": mp.nstr(ones, 30), "all twos": mp.nstr(twos, 30), "the least of the others": mp.nstr(low, 30), "at": [list(c) for c in where][:4],
              "all ones is sqrt5/2": bool(abs(ones - r5) < mp.mpf(10) ** -40), "all twos is sqrt2": bool(abs(twos - r2) < mp.mpf(10) ** -40),
              "every other reads above 17/12": bool(low > b), "17/12 is above sqrt2": bool(b > r2)}
print("(4) %d primitive cyclic sequences; all ones reads %s (sqrt5/2: %s); all twos %s (sqrt2: %s); the least of the others %s at %s; above 17/12 = %s: %s" % (
    len(prim), mp.nstr(ones, 12), OUT["(4)"]["all ones is sqrt5/2"], mp.nstr(twos, 12), OUT["(4)"]["all twos is sqrt2"], mp.nstr(low, 12), where[:3], mp.nstr(b, 8), low > b))
json.dump(OUT, open(HERE / "b1895_probes.json", "w"), indent=1)
