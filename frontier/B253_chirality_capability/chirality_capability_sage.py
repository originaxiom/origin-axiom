"""B253 (sage-python) -- Part A of the Chat-2 chirality-reduction handoff: which exceptional groups have a COMPLEX
representation (=> chirality-capable in the 4d-GUT reading). Run: sage-python chirality_capability_sage.py.
Backs the recorded constants in chirality_capability.py."""
from sage.all import WeylCharacterRing

print("complex-rep capability of the exceptional groups (a group is chirality-capable iff it has a complex irrep):")
for typ, n in [("E6", 6), ("E7", 7), ("E8", 8)]:
    R = WeylCharacterRing(typ, style="coroots")
    degs = []
    has_complex = False
    for i in range(1, n + 1):
        w = [0] * n
        w[i - 1] = 1
        r = R(*w)
        sd = (r == r.dual())
        degs.append((r.degree(), sd))
        if not sd:
            has_complex = True
    dim, sd = min(degs)         # smallest nontrivial irrep
    print(f"  {typ}: min rep dim {dim:>3} (self-dual={sd}) | has a COMPLEX rep: {has_complex} "
          f"-> chirality-{'CAPABLE' if has_complex else 'INCAPABLE'}")

print()
print("=> E6 (Out=Z/2, complex 27): capable.  E7 (Out=1, 56 pseudoreal), E8 (Out=1, 248 real): incapable.")
print("   The figure-eight transition (B248) runs E6 (hyperbolic, capable) -> E8 (spherical, incapable).")
print("   Firewall-clean: a statement about the abstract McKay-label groups; no physics asserted.")
