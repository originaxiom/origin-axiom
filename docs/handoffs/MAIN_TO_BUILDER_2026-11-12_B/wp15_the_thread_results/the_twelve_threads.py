#!/usr/bin/env python3
"""WP-1.5, first step; harvest rows 922 and 910 on main: the forced tetrahedral cover of every odd-trace thread to
length six, read at every character of order dividing 4 and of order dividing 3.

THE STATEMENTS (the SM seat's W6 and its B1550, at its commits; read as statements, none of its code run)
  On the twelve odd-trace threads to word length 6, at the characters of order dividing 4 and dividing 3 of the forced
  A4 cover, a member (n > 0) appears only on +LR (54 at order 4, 6 at order 3) and on -LR (6 and 6); on +LR the members
  with a parity are 48, 16 on each parity, and 6 are fixed by all three translations.
WHAT MAIN COMPUTES, by an instrument that is not the seat's and not B1602's
  The cover's group is built from the base's presentation by Reidemeister-Schreier (kernel_site.py), so the deck group
  acts on the characters.  Characters are grouped into orbits of the deck group together with complex conjugation (the
  four is a real module, so a character and its conjugate read alike; a deck transformation carries the module to an
  isomorphic one).  ONE character of each orbit is read at 40 digits by the sealed reading; an orbit that holds a
  member is then read in full, every character, which tests the orbit rule where it matters.
  Results go to the_twelve_threads.jsonl, one line per reading, so that a stopped run resumes.
HOW IT COULD FAIL: a relator guard, the count of generators, the deck matrices carrying characters to characters (all
in kernel_site.py); a member orbit whose characters do not read alike; the sign characters disagreeing with B1602's
stored rows (checked by the read-out script)."""
import sys, json, time, pathlib, itertools, collections, multiprocessing
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / "frontier" / "B1602_the_forced_cover_on_every_thread" / "verification"))
OUT = HERE / "the_twelve_threads.jsonl"
WORDS = ["LR", "LLLR", "LLLLLR", "LLLRLR", "LLLRRR", "LLRLRR"]
THREADS = ["b+%s%s" % (s, w) for w in WORDS for s in "+-"]
_K = {}


def kernel(name):
    if name not in _K:
        import snappy, kernel_site as KS, forced_every as FE
        M = snappy.Manifold(name); G, eps, label, group, good, ks = FE.forced(M)
        assert label == "A4" and len(ks) == 1, (name, label, len(ks))
        Hg = M.high_precision().fundamental_group()
        assert Hg.generators() == G.generators() and Hg.relators() == G.relators() and Hg.peripheral_curves() == G.peripheral_curves()
        # a base group with three generators gives a cover with 25: its presentation is shortened by Tietze moves (to about
        # ten generators), which makes a reading twelve times faster and changes nothing that is read (checked in the
        # read-out against B1602's stored rows at the sign characters).  The covers with 13 generators are read as built.
        K = KS.Kernel(M, ks[0], FE.mul, FE.inv, FE.E, label=name, shorten=len(G.generators()) > 2, longest=10, budget=400)
        deck = {h: K.deck_matrix(h) for h in K.Q}
        _K[name] = (K, deck, eps, G)
    return _K[name]


def orbits(name, d):
    K, deck, eps, G = kernel(name)
    ch = K.characters(d); S = set(ch); seen, out = set(), []
    for e in ch:
        if e in seen: continue
        orb = {e}; fr = [e]
        while fr:
            x = fr.pop()
            for h in K.Q:
                y = K.act(deck[h], x, d)
                assert y in S, "a deck matrix carries a character out of the characters"
                for yy in (y, tuple((-v) % d for v in y)):
                    if yy not in orb: orb.add(yy); fr.append(yy)
        seen |= orb; out.append(sorted(orb))
    return ch, out


def read(task):
    name, d, e, why = task
    K = kernel(name)[0]; t0 = time.time(); c = K.counts_mp(tuple(e), d)
    return {"thread": name, "d": d, "e": list(e), "why": why, "a1": c["a1"], "r1": c["r1"], "n": c["n"], "t0": c["t0"], "s": round(time.time() - t0, 1)}


if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    threads = sys.argv[2:] or THREADS
    done = {}
    if OUT.exists():
        for l in OUT.read_text().split("\n"):
            if l.strip():
                r = json.loads(l); done[(r["thread"], r["d"], tuple(r["e"]))] = r
    plan = {}
    for name in threads:
        for d in (4, 3):
            ch, orb = orbits(name, d); plan[(name, d)] = orb
            print("%-12s order dividing %d: %5d characters in %4d orbits; generators of the cover's group %d" % (name, d, len(ch), len(orb), kernel(name)[0].n), flush=True)
    tasks = [(name, d, orb[0], "representative") for (name, d), orbs in plan.items() for orb in orbs if (name, d, tuple(orb[0])) not in done]
    print("%d representatives to read (%d already read)" % (len(tasks), len(done)), flush=True)
    with multiprocessing.Pool(workers) as pool, open(OUT, "a") as fh:
        for k, r in enumerate(pool.imap_unordered(read, tasks, chunksize=1), 1):
            fh.write(json.dumps(r) + "\n"); fh.flush(); done[(r["thread"], r["d"], tuple(r["e"]))] = r
            if r["n"] > 0 or k % 50 == 0: print("  %4d/%d  %-12s d=%d  (h1, r1, n) = (%d, %d, %d)  %.0fs" % (k, len(tasks), r["thread"], r["d"], r["a1"], r["r1"], r["n"], r["s"]), flush=True)
        # every orbit that holds a member, in full
        more = []
        for (name, d), orbs in plan.items():
            for orb in orbs:
                rep = done.get((name, d, tuple(orb[0])))
                if rep and rep["n"] > 0: more += [(name, d, e, "the orbit of a member") for e in orb[1:] if (name, d, tuple(e)) not in done]
        print("%d more characters to read: the orbits of the members, in full" % len(more), flush=True)
        for k, r in enumerate(pool.imap_unordered(read, more, chunksize=1), 1):
            fh.write(json.dumps(r) + "\n"); fh.flush()
    print("done", flush=True)
