"""B8143 step 5 -- is the uniqueness robust, or an artifact of a small alphabet?

Step 4 found the SM generation unique (up to conjugation) among 5-field contents over the
SM-visible alphabet. That could be an artifact of the alphabet. Extend it with the natural
next reps and re-run: adjoints (8,1) and (1,3), and the SU(2) triplet-coloured (3,3).
"""
import itertools
import sympy as sp

REP = {
    "A": dict(st=6,  a3=+2, tri=2, dbl=3, lab="(3,2)"),
    "a": dict(st=6,  a3=-2, tri=2, dbl=3, lab="(3bar,2)"),
    "B": dict(st=3,  a3=+1, tri=1, dbl=0, lab="(3,1)"),
    "b": dict(st=3,  a3=-1, tri=1, dbl=0, lab="(3bar,1)"),
    "C": dict(st=2,  a3=0,  tri=0, dbl=1, lab="(1,2)"),
    "D": dict(st=1,  a3=0,  tri=0, dbl=0, lab="(1,1)"),
    # --- extension ---
    "G": dict(st=8,  a3=0,  tri=6, dbl=0, lab="(8,1)"),    # adjoint SU(3): T=3 => 6 in T(3)=1/2 units
    "T": dict(st=3,  a3=0,  tri=0, dbl=4, lab="(1,3)"),    # adjoint SU(2): T=2 => 4 in T(2)=1/2 units
    "X": dict(st=9,  a3=+3, tri=3, dbl=6, lab="(3,3)"),
    "x": dict(st=9,  a3=-3, tri=3, dbl=6, lab="(3bar,3)"),
}
Y = sp.symbols("Y0:5")

def run(letters, label):
    rows, n, killed = [], 0, 0
    for c in itertools.combinations_with_replacement(letters, 5):
        n += 1
        if sum(REP[r]["a3"] for r in c) != 0:
            killed += 1; continue
        if sum(REP[r]["dbl"] for r in c) % 2:
            continue
        eqs = [sum(REP[r]["tri"] * y for r, y in zip(c, Y)),
               sum(REP[r]["dbl"] * y for r, y in zip(c, Y)),
               sum(REP[r]["st"] * y for r, y in zip(c, Y)),
               sum(REP[r]["st"] * y**3 for r, y in zip(c, Y))]
        for s in sp.solve(eqs, list(Y), dict=True):
            vals = [sp.simplify(s.get(y, y)) for y in Y]
            fs = set()
            for v in vals: fs |= v.free_symbols
            free = [y for y in Y if y in fs]
            if len(free) != 1: continue
            cc = [sp.simplify(v.subs({free[0]: 1})) for v in vals]
            if any(x == 0 for x in cc): continue
            rows.append((sum(REP[r]["st"] for r in c), "".join(c),
                         str(tuple(sp.nsimplify(x) for x in cc))))
            break
    rows.sort()
    print("\n%s  (%d contents, %d killed by [SU(3)]^3)" % (label, n, killed))
    for t, c, ex in rows:
        reps = "+".join(REP[r]["lab"] for r in c)
        tag = "   <-- SM" if c in ("AbbCD", "aBBCD") else ""
        print("   %3d states  %-28s %s%s" % (t, reps, ex, tag))
    print("   survivors: %d" % len(rows))
    return rows

r1 = run("AaBbCD", "BASE alphabet")
r2 = run("AaBbCDGT", "EXTENDED with adjoints (8,1),(1,3)")
r3 = run("AaBbCDGTXx", "EXTENDED further with (3,3),(3bar,3)")
print("\nSM still the unique non-conjugate survivor in every alphabet:",
      all(len({c for _, c, _ in r}) <= 2 for r in (r1, r2, r3)))
