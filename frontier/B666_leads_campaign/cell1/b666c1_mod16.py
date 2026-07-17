"""B666 cell 1 (L105) — the mod-16 census (the ear's corrected modulus).

The stage scan shows the silver's sqrt2 tone first rings at kappa = 16
(tr = -1 + 2*sqrt2), while kappa = 8 is rational (-1). Group fact
computed in b666c1_tone_map.py: RRLL mod 8 has order 4, and chi(g) of
an order-4 element of any 2-dim unitary channel is in {0, ±2, ±1±i} —
never ±sqrt2. So the sqrt2 tone on the WORD needs an order-8 shadow of
the word: the ear's modulus for the silver word is 16 (= f * disc =
2 * 8, the conductor of the ring class field of Z[3+2sqrt2] = Z[2sqrt2]),
not 8.

THIS SCRIPT (GAP through sage, corroborating the refined conjecture):
  - the mod-16 shadow <R,L> = SL(2,Z/16): order, RRLL's order mod 16;
  - ALL degree-2 irreducible characters of SL(2,Z/16): character field
    (sqrt2 / sqrt-2 / i / Q(zeta16)+ ...), kernel, image IdGroup,
    PROJECTIVE image (G/Z_chi) IdGroup, and the character value on the
    class of RRLL mod 16;
  - decisive question: the channels with chi(RRLL) = ±sqrt2 — are
    their images binary octahedral (2O = [48,28], projective S4 =
    [24,12] — the E7 McKay type), or something else (binary dihedral =
    D-type)?
"""
from sage.all import SL, Integers, libgap, PermutationGroup

print("B666 cell 1 — the mod-16 census")
print("=" * 68)

G = SL(2, Integers(16))
print(f"|SL(2,Z/16)| = {G.order()}")
Rm = G([[1, 1], [0, 1]])
Lm = G([[1, 0], [1, 1]])
w = Rm * Rm * Lm * Lm
print(f"RRLL mod 16 = {w.matrix().rows()}  order {w.order()}")
print(f"R mod 16 order {Rm.order()}; L mod 16 order {Lm.order()}")
print(f"<R,L> = full group: {G.subgroup([Rm, Lm]).order() == G.order()}")

g = libgap(G)
gw = libgap(w)
T = g.CharacterTable()
classes = T.ConjugacyClasses()
# locate RRLL's class
widx = None
for i, c in enumerate(classes):
    if gw in c:
        widx = i
        break
print(f"RRLL's conjugacy class index: {widx}, size "
      f"{classes[widx].Size()}, rep order "
      f"{classes[widx].Representative().Order()}")

sqrt2 = libgap.eval("E(8)-E(8)^3")
sqrtm2 = libgap.eval("E(8)+E(8)^3")
ii = libgap.eval("E(4)")

irr = T.Irr()
degs = {}
for ch in irr:
    d = int(ch[0])
    degs[d] = degs.get(d, 0) + 1
print(f"irreducible degrees histogram: {dict(sorted(degs.items()))}")

print("\nALL degree-2 irreducibles of SL(2,Z/16):")
hits = []
for k, ch in enumerate(irr):
    if int(ch[0]) != 2:
        continue
    field = libgap.Field(libgap.Rationals, list(ch))
    tags = []
    if sqrt2 in field:
        tags.append("sqrt2")
    if sqrtm2 in field:
        tags.append("sqrt-2")
    if ii in field:
        tags.append("i")
    ker = ch.KernelOfCharacter()
    img = g.FactorGroup(ker)
    imgid = list(img.IdGroup()) if int(img.Size()) <= 2000 else \
        [int(img.Size()), "?"]
    # projective image: Z_chi = { classes with |chi| = 2 }
    zch = ch.CentreOfCharacter()
    pimg = g.FactorGroup(zch)
    pid = list(pimg.IdGroup()) if int(pimg.Size()) <= 2000 else \
        [int(pimg.Size()), "?"]
    val = ch[widx]
    print(f"  chi_{k:>2}: field {'+'.join(tags) if tags else 'Q'}"
          f"  |ker| {ker.Size()}  image {imgid}  proj-image {pid}"
          f"  chi(RRLL) = {val}")
    if str(val) in ("E(8)-E(8)^3", "-E(8)+E(8)^3"):
        hits.append((k, imgid, pid))

print(f"\nchannels with chi(RRLL) = ±sqrt2: {hits}")
print("(2O = [48,28]; S4 = [24,12]; binary dihedral 2D8=Q16 = [16,9];")
print(" D4 dihedral-of-8 = [8,3]; SD16 semidihedral = [16,8])")
print("DONE")
