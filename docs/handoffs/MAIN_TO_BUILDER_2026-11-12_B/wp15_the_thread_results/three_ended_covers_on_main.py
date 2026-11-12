#!/usr/bin/env python3
"""WP-1.5, first step; harvest row 909 on main: the three-ended covers of the family.

THE STATEMENTS (the SM seat's B1549, at its commit; read as statements, none of its code run)
  A state whose companion has a number of ends divisible by 3 has a three-ended cover: a cover of degree 3 on which the
  cusp lifts to three cusps.  To twelve ends there are thirteen such covers on ten states.  At the characters of order
  dividing 4 of these covers there are 138 members (n > 0) in 46 orbits of the deck group: 18 at sign characters, each
  reading (I(W1), I(Lambda^2 W1)) = (-1, -1), and 120 of order four reading (-1, 0), (0, -1) or (0, 0).  +LLLR's cover
  and -LLLLLR's each carry exactly three members of the first kind: the three-orbit does not single out +LLLR.
WHAT MAIN COMPUTES, with its own instrument
  The covers: every map of the state's group onto Z/3 that kills the peripheral pair, up to sign; each cover is the
  kernel, built by kernel_site.py from the base's own presentation, and must have three cusps.  The characters of order
  dividing 4, in orbits of the deck group with complex conjugation; one of each orbit read (h1, r1, n) by B1492's
  reading at 60 digits.  For one member of each orbit that holds a member: the reading (I(W1), I(Lambda^2 W1)) of each
  interior class by B1493's Room.read, the record's own code, run on the same presentation.
  Results to three_ended_covers_on_main.jsonl, one line per reading, so that a stopped run resumes.
HOW IT COULD FAIL: a cover with other than three cusps; the count of covers; a member orbit whose size is not what the
deck group and conjugation give; the read-out compares every cell with the seat's table."""
import sys, json, time, pathlib, itertools, collections
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "frontier" / "B1602_the_forced_cover_on_every_thread" / "verification"))
import snappy
import kernel_site as KS
import forced_every as FE
OUT = HERE / "three_ended_covers_on_main.jsonl"


def states(maxlen=8, max_ends=12):
    out = []
    for w in FE.words(maxlen):
        t = FE.trace(w)
        for sg, name in ((1, "b++" + w), (-1, "b+-" + w)):
            ends = abs(2 - sg * t)
            if ends % 3 == 0 and 0 < ends <= max_ends: out.append((name, ends))
    return out


def covers(name):
    M = snappy.Manifold(name); G = M.high_precision().fundamental_group(); gens = G.generators(); (mu, lam), = G.peripheral_curves()
    val = lambda w, q: sum((1 if c.islower() else -1) * q[c.lower()] for c in w) % 3
    seen, out = set(), []
    for vals in itertools.product(range(3), repeat=len(gens)):
        q = dict(zip(gens, vals))
        if not any(vals) or any(val(r, q) for r in G.relators()) or val(mu, q) or val(lam, q): continue
        key = min(vals, tuple((-v) % 3 for v in vals))
        if key in seen: continue
        seen.add(key); out.append(q)
    Ks = []
    for q in out:
        K = KS.Kernel(M, q, lambda a, b: (a + b) % 3, lambda a: (-a) % 3, 0, label=name, shorten=len(gens) > 2, longest=10, budget=200)
        assert len(K.cusps) == 3, ("not three cusps", name, len(K.cusps))
        Ks.append((q, K))
    return Ks


def orbits(K, d=4):
    deck = [K.deck_matrix(h) for h in K.Q]; ch = K.characters(d); S = set(ch); seen, out = set(), []
    for e in ch:
        if e in seen: continue
        orb = {e}; fr = [e]
        while fr:
            x = fr.pop()
            for Cm in deck:
                y = K.act(Cm, x, d); assert y in S
                for yy in (y, tuple((-v) % d for v in y)):
                    if yy not in orb: orb.add(yy); fr.append(yy)
        seen |= orb; out.append(sorted(orb))
    return ch, out


if __name__ == "__main__":
    st = states(); print("states with a three-ended cover, to 12 ends and 8 letters: %d: %s" % (len(st), st), flush=True)
    only = sys.argv[1:]
    done = {}
    if OUT.exists():
        for l in OUT.read_text().split("\n"):
            if l.strip():
                r = json.loads(l); done[(r["state"], r["cover"], tuple(r["e"]), r["what"])] = r
    total_covers = 0
    with open(OUT, "a") as fh:
        for name, ends in st:
            if only and name not in only: continue
            for ci, (q, K) in enumerate(covers(name)):
                total_covers += 1; t0 = time.time(); ch, orbs = orbits(K)
                mem = []
                for orb in orbs:
                    key = (name, ci, tuple(orb[0]), "counts")
                    if key not in done:
                        c = K.counts_mp(orb[0], 4)
                        done[key] = {"state": name, "cover": ci, "q": q, "e": list(orb[0]), "what": "counts", "orbit": len(orb), "a1": c["a1"], "r1": c["r1"], "n": c["n"], "t0": c["t0"]}
                        fh.write(json.dumps(done[key]) + "\n"); fh.flush()
                    if done[key]["n"] > 0: mem.append(orb)
                S = None
                for orb in mem:
                    key = (name, ci, tuple(orb[0]), "reading")
                    if key not in done:
                        if S is None: S = K.as_room()
                        r = S.read(K.nu_of(orb[0], 4))
                        done[key] = {"state": name, "cover": ci, "q": q, "e": list(orb[0]), "what": "reading", "orbit": len(orb), "sign character": all(x in (0, 2) for x in orb[0]),
                                     "interior": r["interior"], "m_A": r["m_A"], "b0": r["b0"],
                                     "readings": [[x["cls"], x["I_W1"], x["I_L2W1"], x["relator_ok"]] for x in r["readings"]]}
                        fh.write(json.dumps(done[key]) + "\n"); fh.flush()
                summ = collections.Counter()
                for orb in mem:
                    r = done[(name, ci, tuple(orb[0]), "reading")]
                    kind = "sign" if r["sign character"] else "order 4"
                    for x in r["readings"]:
                        if x[0].startswith("interior"): summ[(kind, x[1], x[2])] += len(orb)
                print("%-13s cover %d of ends %2d: %2d generators, %4d characters in %3d orbits; members %3d; readings of the interior classes %s  (%.0fs)" % (
                    name, ci, ends, K.n, len(ch), len(orbs), sum(len(o) for o in mem), dict(summ), time.time() - t0), flush=True)
    print("covers: %d" % total_covers, flush=True)
