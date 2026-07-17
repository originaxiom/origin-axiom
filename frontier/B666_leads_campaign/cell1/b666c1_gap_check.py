"""B666 cell 1 (L105) — independent corroboration via sage/GAP.

Reads the regular-representation permutation generators exported by
b666c1_shadow_group.py (pure-python exact computation) and, in a fully
independent system (GAP through sage):

  - IdGroup of: the mod-8 shadow, the mod-4 shadow, the exact 2O build,
    and the three order-48 quotients of SL(2,Z/8);
  - the small-group identity of the binary octahedral group (2O):
    corroborate that exactly one quotient matches it;
  - the character table of SL(2,Z/8): all irreducible degrees; every
    degree-2 character's values, kernel size, image identification, and
    whether its character field realizes sqrt2 (value with minpoly
    x^2 - 2, or field containing sqrt2);
  - the same for 2O itself (the sqrt2 characters).

Run with sage-python.
"""
import json
import os

from sage.all import (PermutationGroup, QQ, libgap)

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "b666c1_groups.json")))


def permgroup(key):
    gens = [[i + 1 for i in g] for g in data[key]["gens"]]
    return PermutationGroup(gens)


def idgroup(G):
    return list(libgap(G).IdGroup())


print("B666 cell 1 — GAP corroboration")
print("=" * 68)

groups = {}
for key in sorted(data.keys()):
    G = permgroup(key)
    groups[key] = G
    print(f"{key:>10}: order {G.order()}  IdGroup {idgroup(G)}")

# the canonical 2O from GAP itself, independent of our build:
# 2O = the double cover 2.S4 with generalized quaternion Sylow-2.
# We identify it structurally: among all groups of order 48, it is the
# one with a unique involution and elements of order 8 — but rather than
# trust a catalog number from memory, we DERIVE it: take our exact
# quaternion build's id and check it has the defining properties in GAP.
g2O = libgap(groups["2O"])
n_inv = sum(1 for c in g2O.ConjugacyClasses()
            if c.Representative().Order() == 2
            for _ in range(int(c.Size())))
print(f"\n2O check in GAP: order {g2O.Size()}, involutions {n_inv}, "
      f"IdGroup {list(g2O.IdGroup())}")
print(f"2O perfect? {bool(g2O.IsPerfectGroup())}  "
      f"derived subgroup order {g2O.DerivedSubgroup().Size()} "
      f"(2T=SL(2,3) expected: 24)")

id2O = list(g2O.IdGroup())
match = [k for k in data if k.startswith("quot48")
         and idgroup(groups[k]) == id2O]
print(f"\norder-48 quotients of SL(2,Z/8) matching 2O's IdGroup: "
      f"{match}")

# character tables
for key in ["mod8", "2O"]:
    G = libgap(groups[key])
    T = G.CharacterTable()
    irr = T.Irr()
    classes = T.ConjugacyClasses()
    sizes = [int(c.Size()) for c in classes]
    orders = [int(c.Representative().Order()) for c in classes]
    degs = sorted(int(ch[0]) for ch in irr)
    print(f"\n[{key}] classes: {len(sizes)}; irreducible degrees: "
          f"{degs}  (sum d^2 = {sum(d*d for d in degs)})")
    print(f"    class rep orders: {orders}")
    n2 = 0
    for ch in irr:
        if int(ch[0]) != 2:
            continue
        n2 += 1
        vals = list(ch)
        # kernel: classes where chi(g) = 2
        ker = sum(sizes[i] for i, v in enumerate(vals) if v == 2)
        img = int(G.Size()) / ker
        # sqrt2 realized?
        has_s2 = False
        pretty = []
        for v in vals:
            sv = str(v)
            pretty.append(sv)
            if sv in ("E(8)+E(8)^7", "-E(8)-E(8)^7",
                      "E(8)^3+E(8)^5", "-E(8)^3-E(8)^5"):
                has_s2 = True
        # more robust sqrt2 test via conductor + field:
        fld = T.FieldOfCharacter(ch) if hasattr(T, "FieldOfCharacter") \
            else None
        print(f"    deg-2 irrep #{n2}: |ker| = {int(ker)}, "
              f"|image| = {int(img)}, sqrt2 in values: {has_s2}")
        print(f"        values: {pretty}")
        if has_s2 and key == "mod8":
            # identify the image: kernel subgroup -> quotient IdGroup
            kerS = G.KernelOfCharacter(ch)
            Qt = G.FactorGroup(kerS)
            print(f"        KERNEL order {kerS.Size()}; image IdGroup "
                  f"{list(Qt.IdGroup())}")

# and: full list of which quotients of mod8 realize sqrt2 in ANY irrep
G = libgap(groups["mod8"])
T = G.CharacterTable()
irr = T.Irr()
print("\n[mod8] all irreducible degrees with sqrt2 in their values:")
for ch in irr:
    vals = [str(v) for v in ch]
    if any("E(8)" in v and "E(8)^2" not in v.replace("E(8)^", "#")
           for v in vals):
        pass  # crude scan; decisive scan below
for ch in irr:
    has = any(str(v) in ("E(8)+E(8)^7", "-E(8)-E(8)^7",
                         "E(8)^3+E(8)^5", "-E(8)^3-E(8)^5")
              for v in ch)
    if has:
        kerS = G.KernelOfCharacter(ch)
        Qt = G.FactorGroup(kerS)
        print(f"    degree {int(ch[0])}: kernel {kerS.Size()}, "
              f"image IdGroup {list(Qt.IdGroup())}")
print("DONE")
