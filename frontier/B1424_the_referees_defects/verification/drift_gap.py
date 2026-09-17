"""B1424 (second method): the same question by GAP's GQuotients rather than brute force.

Does the base-rate decline the paper reports at census depth happen on the ONE-CUSPED census, which is
the population the surrounding sentence is about, or only on the FULL orientable cusped census, which is
what the sweep behind the sentence actually ran?
Run: sage -python drift_gap.py [block]
"""
import json, sys
import snappy
from sage.all import libgap


def surjects(M):
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    if len(gens) > 3:
        return None
    libgap.eval("F := FreeGroup(%s)" % ",".join('"%s"' % g for g in gens))
    libgap.eval("g := GeneratorsOfGroup(F)")

    def word(w):
        return "*".join("g[%d]%s" % (gens.index(c.lower()) + 1, "" if c.islower() else "^-1") for c in w)

    libgap.eval("G := F/[%s]" % ",".join(word(r) for r in rels) if rels else "G := F")
    return int(libgap.eval("Length(GQuotients(G, SL(2,3)))")) > 0


def block(census, lo, size):
    n = hit = skip = 0
    for i in range(lo, lo + size):
        try:
            r = surjects(census[i])
        except Exception:
            skip += 1; continue
        if r is None:
            skip += 1; continue
        n += 1; hit += bool(r)
    return dict(lo=lo, n=n, hit=hit, skipped=skip, rate=round(100.0 * hit / max(n, 1), 2))


if __name__ == "__main__":
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    assert surjects(snappy.Manifold("m004")) is True, "control failed: m004 must surject"
    print("control: m004 surjects -> True", flush=True)
    out = {}
    for name, C in (("one-cusped", snappy.OrientableCuspedCensus(cusps=1)),
                    ("full", snappy.OrientableCuspedCensus)):
        rows = []
        for lo in (0, 20000, 80000):
            r = block(C, lo, size); rows.append(r)
            print("%-11s depth %-6d %5.2f%%  (n=%d, skipped %d)" % (name, lo, r["rate"], r["n"], r["skipped"]), flush=True)
        out[name] = rows
    json.dump(out, open("drift_gap.json", "w"), indent=1)
