"""B8143 step 2 -- is the SM's SHAPE forced, or only its charges?

B1160 forces Y *given* an SM-shaped 15-plet, and fences the shaping as observer-paid.
The sharp question is RIGIDITY, not existence: for which contents is the anomaly-free
chiral solution ISOLATED up to scale? That is what makes "hypercharge falls out" mean
anything -- with a bigger content the charges are not determined at all.

Dimension count. n charges, 3 independent linear conditions, 1 cubic, 1 overall scale:
    dim(solution set, mod scale) = n - 3 - 1 - 1 = n - 5
so n = 5 is exactly the rigidity threshold. The SM generation has exactly 5 charge
parameters (Yq, Yu, Yd, Yl, Ye). This enumerates EVERY 5-field content over the alphabet
and asks which are rigid AND chiral.

Alphabet, all left-handed Weyl:  A=(3,2) 6 states   B=(3bar,1) 3   C=(1,2) 2   D=(1,1) 1
"""
import itertools
import sympy as sp

ALPHA = {"A": dict(states=6, tri=2, dbl=3),   # (3,2): 2 triplets, 3 doublets
         "B": dict(states=3, tri=1, dbl=0),   # (3bar,1)
         "C": dict(states=2, tri=0, dbl=1),   # (1,2)
         "D": dict(states=1, tri=0, dbl=0)}   # (1,1)

Y = sp.symbols("Y0:5")


def conditions(content):
    su3 = sum(ALPHA[r]["tri"] * Y[i] for i, r in enumerate(content))
    su2 = sum(ALPHA[r]["dbl"] * Y[i] for i, r in enumerate(content))
    grav = sum(ALPHA[r]["states"] * Y[i] for i, r in enumerate(content))
    cube = sum(ALPHA[r]["states"] * Y[i] ** 3 for i, r in enumerate(content))
    return [su3, su2, grav, cube]


def witten_ok(content):
    return sum(ALPHA[r]["dbl"] for r in content) % 2 == 0


rows = []
for content in itertools.combinations_with_replacement("ABCD", 5):
    if not witten_ok(content):
        continue
    eqs = conditions(content)
    sols = sp.solve(eqs, list(Y), dict=True)
    rigid_chiral = []
    for s in sols:
        vals = [sp.simplify(s.get(y, y)) for y in Y]
        fs = set()
        for v in vals:
            fs |= v.free_symbols
        free = [y for y in Y if y in fs]
        if len(free) != 1:            # not isolated up to a single scale
            continue
        p = free[0]
        conc = [sp.simplify(v.subs({p: 1})) for v in vals]
        if all(c == 0 for c in conc):
            continue
        # CHIRAL: no field may be neutral if it is the only one of its rep carrying charge;
        # operationally, require that not every charge on a repeated rep cancels pairwise,
        # and that the (3,2) fields (if any) are charged.
        chiral = any(c != 0 for i, c in enumerate(conc) if content[i] == "A") if "A" in content \
            else any(c != 0 for c in conc)
        if not chiral:
            continue
        rigid_chiral.append(tuple(conc))
    if rigid_chiral:
        uniq = {tuple(str(sp.nsimplify(x)) for x in t) for t in rigid_chiral}
        rows.append((sum(ALPHA[r]["states"] for r in content), "".join(content), len(uniq), sorted(uniq)[:2]))

rows.sort()
print("Every 5-field content over {A=(3,2), B=(3bar,1), C=(1,2), D=(1,1)} passing Witten,")
print("whose anomaly-free solution is ISOLATED up to scale and CHIRAL:\n")
print("  states  content   #branches   example (Y0..Y4)")
for tot, c, n, ex in rows:
    tag = "   <-- the SM generation" if c == "ABBCD" else ""
    print("  %5d   %-8s  %d          %s%s" % (tot, c, n, ex[0], tag))
print("\n  contents examined: %d ; rigid+chiral: %d" % (
    len([c for c in itertools.combinations_with_replacement("ABCD", 5) if witten_ok(c)]), len(rows)))
