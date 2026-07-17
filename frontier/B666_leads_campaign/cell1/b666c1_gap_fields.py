"""B666 cell 1 — decisive character-field identification (GAP).

For EVERY irreducible character of SL(2,Z/8): degree, kernel order,
image IdGroup, and exact field content among the three quadratic
subfields of Q(zeta_8): sqrt2 = E(8)-E(8)^3, sqrt-2 = E(8)+E(8)^3,
i = E(4). Decides: which channels of the conductor-8 shadow realize
sqrt2, and whether they are exactly the octahedral (2O = [48,28])
ones. Same for 2O's own table (control).
"""
import json
import os

from sage.all import PermutationGroup, libgap

HERE = os.path.dirname(os.path.abspath(__file__))
data = json.load(open(os.path.join(HERE, "b666c1_groups.json")))


def permgroup(key):
    gens = [[i + 1 for i in g] for g in data[key]["gens"]]
    return PermutationGroup(gens)


sqrt2 = libgap.eval("E(8)-E(8)^3")
sqrtm2 = libgap.eval("E(8)+E(8)^3")
ii = libgap.eval("E(4)")

for key in ["mod8", "2O"]:
    G = libgap(permgroup(key))
    T = G.CharacterTable()
    irr = T.Irr()
    print(f"\n[{key}] order {G.Size()} — all irreducible characters:")
    n_s2 = []
    for k, ch in enumerate(irr):
        deg = int(ch[0])
        field = libgap.Field(libgap.Rationals, list(ch))
        has_s2 = bool(sqrt2 in field)
        has_sm2 = bool(sqrtm2 in field)
        has_i = bool(ii in field)
        kerS = ch.KernelOfCharacter()
        kord = int(kerS.Size())
        if kord < int(G.Size()):
            Qt = G.FactorGroup(kerS)
            img = list(Qt.IdGroup()) if int(Qt.Size()) <= 2000 else \
                [int(Qt.Size()), "?"]
        else:
            img = [1, 1]
        tag = []
        if has_s2:
            tag.append("sqrt2")
            n_s2.append(k)
        if has_sm2:
            tag.append("sqrt-2")
        if has_i:
            tag.append("i")
        print(f"  chi_{k:>2}: deg {deg}  |ker| {kord:>3}  image "
              f"{img}  field: {'+'.join(tag) if tag else 'Q'}")
    print(f"  ==> sqrt2-realizing characters: {n_s2}")
    if key == "mod8":
        for k in n_s2:
            ch = irr[k]
            kerS = ch.KernelOfCharacter()
            Qt = G.FactorGroup(kerS)
            print(f"      chi_{k}: image IdGroup {list(Qt.IdGroup())} "
                  f"(2O = [48,28])")
print("\nDONE")
