"""P-229 (B1652's FAILS cells): main's own census for the SM seat's W76, from its rule (e1724317, W76_RULE.md).
Every Lyndon word W in L < R of length 2 to 16; the bundle b++W; CS = Im complex_volume() reduced mod pi^2 to
(-pi^2/2, pi^2/2]; mirror-symmetric when the least rotation of swap(W) is W or the least rotation of W reversed;
the bit 0 if |CS| < 1e-8, 1/2 if ||CS| - pi^2/2| < 1e-8, else 'neither'."""
import json, math, pathlib, sys
import snappy
HERE = pathlib.Path(__file__).resolve().parent
def lyndon(n):
    """Duval's algorithm over the alphabet L < R"""
    out = []; w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        if m == n: out.append("".join("LR"[c] for c in w))
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == 1: w.pop()
    return out
def least_rot(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
words = [w for n in range(2, int(sys.argv[1]) + 1) for w in lyndon(n)]
P2 = math.pi ** 2
rows = []; counts = {}
for w in words:
    counts[len(w)] = counts.get(len(w), 0) + 1
    s = least_rot(swap(w)); r = least_rot(w[::-1])
    kind = ("rot" if s == w else "") + ("rev" if s == r else "")
    if not kind:
        continue
    M = snappy.Manifold("b++" + w)
    cs = complex(M.complex_volume()).imag
    cs = cs - P2 * math.floor(cs / P2 + 0.5)
    if cs <= -P2 / 2: cs += P2
    bit = 0 if abs(cs) < 1e-8 else (0.5 if abs(abs(cs) - P2 / 2) < 1e-8 else "neither")
    rows.append(dict(word=w, kind=kind, cs=cs, bit=bit, solution=M.solution_type()))
summ = dict(threads=len(words), by_length=counts, mirror_symmetric=len(rows),
            bits={str(b): sum(1 for r in rows if r["bit"] == b) for b in (0, 0.5, "neither")},
            kinds={k: sum(1 for r in rows if r["kind"] == k) for k in ("rot", "rev", "rotrev")},
            max_abs_cs=max(abs(r["cs"]) for r in rows),
            solutions=sorted({r["solution"] for r in rows}))
print(summ)
json.dump(dict(summary=summ, rows=rows), open(HERE / "main_w76.json", "w"), indent=0)
