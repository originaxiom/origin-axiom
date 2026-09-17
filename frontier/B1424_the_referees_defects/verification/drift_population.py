"""B1424: on WHICH census does the base-rate drift fall? The paper's sentence says one-cusped; the
sweep behind it ran the FULL orientable cusped census. Computed here on both, same blocks, same test.

The criterion is B1400's own: a surjection of pi_1 onto SL(2,3) = 2T, tested by brute force over
images of the generators, accepting only images that generate the whole group (order 24). Groups with
more than three generators are skipped exactly as the original does.
Run: python3 drift_population.py [block_size]
"""
import itertools, sys, json
import snappy

# SL(2,3) as explicit 2x2 matrices over F_3
def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) % 3 for j in range(2)) for i in range(2))

ID = ((1, 0), (0, 1))
E = []
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                if (a * d - b * c) % 3 == 1:
                    E.append(((a, b), (c, d)))
assert len(E) == 24, len(E)
INV = {g: next(h for h in E if mm(g, h) == ID) for g in E}


def ev(word, m):
    out = ID
    for ch in word:
        out = mm(out, m[ch.lower()] if ch.islower() else INV[m[ch.lower()]])
    return out


def gen_size(imgs):
    seen, frontier = {ID}, [ID]
    while frontier:
        nxt = []
        for x in frontier:
            for g in imgs:
                y = mm(x, g)
                if y not in seen:
                    seen.add(y); nxt.append(y)
        frontier = nxt
    return len(seen)


def has_surj(G):
    gen, rel = G.generators(), G.relators()
    if len(gen) > 3:
        return None
    for img in itertools.product(E, repeat=len(gen)):
        m = {gen[i]: img[i] for i in range(len(gen))}
        if all(ev(r, m) == ID for r in rel) and gen_size(img) == 24:
            return True
    return False


def block(census, lo, size):
    n = hit = skipped = 0
    for i in range(lo, lo + size):
        try:
            r = has_surj(census[i].fundamental_group())
        except Exception:
            skipped += 1; continue
        if r is None:
            skipped += 1; continue
        n += 1; hit += r
    return dict(lo=lo, n=n, hit=hit, skipped=skipped, rate=round(100.0 * hit / max(n, 1), 2))


if __name__ == "__main__":
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    # control: m004 must be found to surject
    assert has_surj(snappy.Manifold("m004").fundamental_group()) is True, "control failed"
    print("control: m004 surjects onto 2T -> True")
    res = {}
    for name, census in (("full orientable cusped", snappy.OrientableCuspedCensus),
                         ("one-cusped only", snappy.OrientableCuspedCensus(cusps=1))):
        rows = [block(census, lo, size) for lo in (0, 20000, 80000)]
        res[name] = rows
        print("%-22s len=%d  %s" % (name, len(census),
              "  ".join("depth %-6d %5.2f%% (n=%d, skipped %d)" % (r["lo"], r["rate"], r["n"], r["skipped"]) for r in rows)))
    json.dump(res, open("drift_population.json", "w"), indent=1)
