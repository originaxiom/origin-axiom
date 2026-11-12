#!/usr/bin/env python3
"""WP-1.5, first step; harvest rows 922 and 910: the read-out of the_twelve_threads.py.

WHAT IS READ OUT
  1. For each of the twelve odd-trace threads to length six and for d = 4 and 3: the number of characters of order
     dividing d on the forced tetrahedral cover, the members (n > 0) among them with their structures (h1, r1, n), and
     the number of orbits of the deck group that the members fall into.  A character's reading is its orbit's: the
     orbits are those of the deck group with complex conjugation, one character of each was read, and every orbit that
     holds a member was then read in full.
  2. The seat's table (its W6, quoted as data below) against it.
  3. CONTROL: at the sign characters the readings, as a multiset of (h1, r1, n), must be B1602's stored rows, which were
     read on SnapPy's own triangulation of the cover: two presentations of one group, one reading.
  4. CONTROL: every orbit that holds a member, read in full, reads alike.
  5. On +LR and -LR, the parities.  V4 is the deck group's subgroup of the three translations.  A member fixed by one
     translation t_p and no other has the parity p; a member fixed by none lives on the punctures: its values on the
     four puncture loops are read, and if exactly two are non-trivial the member's parity is the translation that
     carries one of the two punctures to the other.  The count on each parity, and the members fixed by all three.
HOW IT COULD FAIL: 3 and 4 above; a thread whose readings are not complete is reported as such and not compared."""
import sys, json, math, pathlib, collections, itertools
HERE = pathlib.Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import the_twelve_threads as TT
import forced_every as FE

SEAT = {  # the SM seat's table of its W6 (docs/dossiers/the_weave_2026-10-07/NOTE.md on its branch), as data: order 4: characters, members, orbits; order 3: characters, members
    "b++LR": (1024, 54, 8, 81, 6), "b+-LR": (256, 6, 1, 81, 6), "b++LLLR": (256, 0, 0, 729, 0), "b+-LLLR": (1024, 0, 0, 81, 0),
    "b++LLLLLR": (4096, 0, 0, 81, 0), "b+-LLLLLR": (256, 0, 0, 729, 0), "b++LLLRLR": (256, 0, 0, 81, 0), "b+-LLLRLR": (1024, 0, 0, 729, 0),
    "b++LLLRRR": (1024, 0, 0, 729, 0), "b+-LLLRRR": (256, 0, 0, 81, 0), "b++LLRLRR": (4096, 0, 0, 81, 0), "b+-LLRLRR": (256, 0, 0, 81, 0)}
done = {}
for l in (HERE / "the_twelve_threads.jsonl").read_text().split("\n"):
    if l.strip():
        r = json.loads(l); done[(r["thread"], r["d"], tuple(r["e"]))] = r
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:400]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:300]) if detail else ""), flush=True)

threads = sys.argv[1:] or TT.THREADS
table, complete = {}, []
for name in threads:
    K, deck, eps, G = TT.kernel(name); row = {}
    whole = True
    for d in (4, 3):
        ch, orbs = TT.orbits(name, d); reading = {}
        for orb in orbs:
            rep = done.get((name, d, tuple(orb[0])))
            if rep is None: whole = False; continue
            for e in orb: reading[e] = (rep["a1"], rep["r1"], rep["n"])
        if len(reading) < len(ch): row[d] = {"characters": len(ch), "read": len(reading), "complete": False}; continue
        members = [e for e in ch if reading[e][2] > 0]
        # the deck group's own orbits (without conjugation) among the members
        seen, n_orb = set(), 0
        for e in members:
            if e in seen: continue
            n_orb += 1; fr = [e]; seen.add(e)
            while fr:
                x = fr.pop()
                for h in K.Q:
                    y = K.act(deck[h], x, d)
                    if y not in seen: seen.add(y); fr.append(y)
        # every orbit with a member, read in full: do they read alike?
        alike, full = True, True
        for orb in orbs:
            if reading[orb[0]][2] > 0:
                for e in orb:
                    r = done.get((name, d, tuple(e)))
                    if r is None: full = False
                    elif (r["a1"], r["r1"], r["n"]) != reading[orb[0]]: alike = False
        row[d] = {"characters": len(ch), "complete": True, "members": len(members), "orbits of the deck group among the members": n_orb,
                  "structures of the members": dict(collections.Counter(str(reading[e]) for e in members)), "member orbits read in full": full, "and they read alike": alike,
                  "reading": reading, "members list": members}
    table[name] = row
    if whole and all(row[d].get("complete") for d in (4, 3)): complete.append(name)
    print("%-11s " % name + " | ".join("order %d: %s" % (d, ("%d characters, %d members in %d orbits %s" % (row[d]["characters"], row[d]["members"], row[d]["orbits of the deck group among the members"], row[d]["structures of the members"])) if row[d].get("complete") else "NOT COMPLETE (%d of %d)" % (row[d]["read"], row[d]["characters"])) for d in (4, 3)), flush=True)

# ---- 2. the seat's table
agree = {n: (table[n][4]["characters"], table[n][4]["members"], table[n][4]["orbits of the deck group among the members"], table[n][3]["characters"], table[n][3]["members"]) == SEAT[n] for n in complete}
check("the seat's table: characters, members and orbits at order 4, characters and members at order 3, on every thread that is complete", all(agree.values()) and bool(complete), "%d of %d threads complete; agreeing: %d; differing: %s" % (len(complete), len(threads), sum(agree.values()), [n for n, a in agree.items() if not a]))
check("members appear only on +LR and -LR among the threads that are complete", all((table[n][4]["members"] + table[n][3]["members"] > 0) == (n in ("b++LR", "b+-LR")) for n in complete), [n for n in complete if table[n][4]["members"] + table[n][3]["members"] > 0])
# ---- 3. the sign characters against B1602's stored rows
ok3, n3 = True, 0
for n in complete:
    stored = json.loads(next((ROOT / "frontier").glob("B1602_*/verification/forced_%s.json" % n)).read_text())
    want = collections.Counter((r["h1"], r["r1"], r["n"]) for r in stored["covers"][0]["rows"])
    got = collections.Counter(v for e, v in table[n][4]["reading"].items() if all(x in (0, 2) for x in e))
    ok3 &= (want == got); n3 += sum(got.values())
check("CONTROL: at the sign characters the readings are B1602's stored rows, as a multiset, on every complete thread", ok3 and bool(complete), "%d sign characters on %d threads" % (n3, len(complete)))
# ---- 4. the member orbits in full
mem = [(n, d) for n in complete for d in (4, 3) if table[n][d]["members"]]
check("CONTROL: every orbit that holds a member was read in full and reads alike", all(table[n][d]["member orbits read in full"] and table[n][d]["and they read alike"] for n, d in mem), "%s" % [(n, d, table[n][d]["member orbits read in full"], table[n][d]["and they read alike"]) for n, d in mem])
# ---- 5. the parities on +LR and -LR
par = {}
for name in [n for n in ("b++LR", "b+-LR") if n in complete]:
    K, deck, eps, G = TT.kernel(name)
    order2 = [h for h in K.Q if h != FE.E and FE.mul(h, h) == FE.E]; assert len(order2) == 3, "the three translations"
    em, el = sum((1 if c.islower() else -1) * eps[c.lower()] for c in K.mu), sum((1 if c.islower() else -1) * eps[c.lower()] for c in K.lam)
    g = math.gcd(abs(em), abs(el)); i, j = el // g, -em // g                      # the fibre's puncture loop: mu^i lam^j, on which eps vanishes
    def power(w, k): return w * k if k >= 0 else TT_inv(w) * (-k)
    def TT_inv(w): return w[::-1].swapcase()
    ell = power(K.mu, i) + power(K.lam, j)
    assert K.qw(ell) == FE.E, "the puncture loop is not in the kernel"
    loops = {h: K.tau(K.rep[h] + ell + TT_inv(K.rep[h])) for h in K.cusp_reps}
    def cusp_of(h):                                                             # the cusp (a coset of the image of the peripheral group) that h lies in
        for c in K.cusp_reps:
            if any(FE.mul(c, p) == h for p in imgP): return c
        raise RuntimeError("no cusp")
    qm, ql = K.qw(K.mu), K.qw(K.lam)
    imgP = {FE.E}; fr = [FE.E]
    while fr:
        x = fr.pop()
        for y in (FE.mul(x, qm), FE.mul(x, ql)):
            if y not in imgP: imgP.add(y); fr.append(y)
    d = 4; out = collections.Counter(); per = collections.Counter(); kinds = collections.Counter()
    for e in table[name][4]["members list"]:
        stab = [t for t in order2 if K.act(deck[t], e, d) == e]
        if len(stab) == 3: kinds["fixed by all three translations"] += 1; continue
        if len(stab) == 1: kinds["fixed by one translation"] += 1; per[order2.index(stab[0])] += 1; continue
        vals = {h: K.value(e, d, loops[h]) for h in K.cusp_reps}; non = [h for h, v in vals.items() if v != 0]
        if len(non) == 2:
            t = next((t for t in order2 if cusp_of(FE.mul(t, non[0])) == non[1]), None)
            if t is not None: kinds["on an edge (two punctures)"] += 1; per[order2.index(t)] += 1; continue
        kinds["fixed by no translation, values on the punctures %s" % sorted(vals.values())] += 1
    par[name] = {"kinds": dict(kinds), "members on each parity": [per[k] for k in range(3)]}
    print("%s, order 4: %s; on each of the three parities: %s" % (name, dict(kinds), [per[k] for k in range(3)]), flush=True)
if "b++LR" in par:
    check("on +LR: 48 members have a parity, 16 on each, and 6 are fixed by all three translations (the seat's B1550 and W6)", par["b++LR"]["members on each parity"] == [16, 16, 16] and par["b++LR"]["kinds"].get("fixed by all three translations") == 6, par["b++LR"])
res = {"complete": complete, "table": {n: {str(d): {k: v for k, v in table[n][d].items() if k not in ("reading", "members list")} for d in (4, 3)} for n in table}, "parities": par, "checks": CHECKS,
       "failing": [c["check"] for c in CHECKS if not c["holds"]]}
(HERE / "the_twelve_threads_read_out.json").write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
print("\n%d checks, %d failing; %d of %d threads complete" % (len(CHECKS), len(res["failing"]), len(complete), len(threads)))
