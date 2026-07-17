"""B666 cell 1 — which irreps of SL(2,Z/16) put sqrt2 on the silver
word's class? (all degrees; the stage tone -1+2sqrt2 at kappa=16 must
be assembled from these channels)."""
from sage.all import SL, Integers, libgap

G = SL(2, Integers(16))
g = libgap(G)
Rm = G([[1, 1], [0, 1]])
Lm = G([[1, 0], [1, 1]])
w = libgap(Rm * Rm * Lm * Lm)
T = g.CharacterTable()
classes = T.ConjugacyClasses()
widx = next(i for i, c in enumerate(classes) if w in c)
sqrt2 = libgap.eval("E(8)-E(8)^3")
irr = T.Irr()
print("irreps of SL(2,Z/16) with sqrt2 IN THE VALUE chi(RRLL):")
found = []
for k, ch in enumerate(irr):
    val = ch[widx]
    fld = libgap.Field(libgap.Rationals, [val])
    if sqrt2 in fld:
        ker = ch.KernelOfCharacter()
        img = g.FactorGroup(ker)
        imgid = (list(img.IdGroup()) if int(img.Size()) <= 2000
                 else [int(img.Size()), "?"])
        zch = ch.CentreOfCharacter()
        pimg = g.FactorGroup(zch)
        pid = (list(pimg.IdGroup()) if int(pimg.Size()) <= 2000
               else [int(pimg.Size()), "?"])
        print(f"  chi_{k:>2}: deg {int(ch[0])}  chi(RRLL) = {val}  "
              f"image {imgid}  proj-image {pid}")
        found.append(k)
print(f"total: {len(found)}")
print("\n(and the full field of each such character:)")
for k in found:
    ch = irr[k]
    fld = libgap.Field(libgap.Rationals, list(ch))
    print(f"  chi_{k}: field degree {fld.DegreeOverPrimeField()}, "
          f"sqrt2 in field: {sqrt2 in fld}")
print("DONE")
