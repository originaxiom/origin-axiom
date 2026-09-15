#!/usr/bin/env python3
"""MEMO-97 CELL: THE BRANCH BIT TEST — does the record's own symmetry
group swap the two branches of the unstable manifold at the trivial
rep?  Campaign THE SECOND HALF: the census's candidate-8 blocker (the
arrow/seed bit), given its dynamical face by memo 94 (the two-branch
law), now tested against the object's symmetries.  This is the weld
book's instrument (i) — the arithmetic orbit-breaker test — made
concrete at the orbit level: an object symmetry that swaps the
branches would make the branch "choice" GAUGE (object-broken, no frame
bit); no such symmetry leaves the bit EXTERNAL (frame column).

SETUP (all banked): the Fricke slice (x,y,z) = (tr a, tr b, tr ab)
with kappa = x^2+y^2+z^2-xyz-2; the flow T(x,y,z) = (z, x, zx-y)
(memo 94); the trivial rep P0 = (2,2,2); the golden unstable line of
T^2 at P0 with exact eigenvector v_u = (3/2-sqrt5/2, 7/2-3sqrt5/2, 1)
and eigenvalue phi^4 (memo 94, exact).  The branch bit: v_u vs -v_u.

THE SYMMETRY CANDIDATES (the finite symmetries of the banked
structure, enumerated):
  * the character sign-twists Sigma = {diag(e1,e2,e3): e1 e2 e3 = 1}
    (the H^1(M; Z/2) twist action on characters — B782's torsor's
    natural face here);
  * s: (x,y,z) -> (y,x,z)  (the a<->b swap, realized by an isometry
    of m004);
  * e': (x,y,z) -> (x,y,xy-z)  (the fourth-trace flip
    tr(ab) <-> tr(ab^-1) — the hyperelliptic z-swap).
For each candidate g: (1) verify g preserves kappa (symbolic); (2)
does g fix P0?  (3) symbolically, is g T^2 g^-1 = T^2 (flow-
commuting) or T^-2 (time-reversing) or neither; (4) for the
flow-commuting fixers of P0: does Dg(P0) send v_u to +v_u or -v_u?

PREREGISTERED OUTCOMES (each banks):
  SWAP FOUND  => the branch bit is OBJECT-BROKEN (gauge): candidate 8
     leaves the census's blocker list as NOT-A-BIT — a major
     simplification of the frame column;
  NO SWAP, with the stabilizer computed  => the branch bit SURVIVES
     the object's symmetries: it is a genuine external residue at the
     orbit level — the census blocker types toward the frame column,
     and the weld instrument (i)'s "which Z/2" question is ANSWERED
     (the branch Z/2, not c — c acts trivially on the real slice);
  TIME-REVERSER FOUND (g T^2 g^-1 = T^-2) => recorded: the record's
     own symmetry realizes orbit-level time reversal (the dynamical
     face of B124's two-headedness), separately from the branch bit.
Gate 5 untouched (polynomial maps and exact algebra only).
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
V = (x, y, z)
kappa = x**2 + y**2 + z**2 - x*y*z - 2
phi = (1 + sp.sqrt(5))/2

def compose(f, g):
    """(f o g)(P) = f(g(P)) for maps given as coordinate 3-tuples."""
    return tuple(sp.expand(c.subs({x: g[0], y: g[1], z: g[2]}, simultaneous=True)) for c in f)

T = (z, x, z*x - y)
T2 = compose(T, T)
Tinv = (y, x*y - z, x)
assert compose(T, Tinv) == (x, y, z) and compose(Tinv, T) == (x, y, z)
T2inv = compose(Tinv, Tinv)

def preserves_kappa(g):
    return sp.simplify(kappa.subs({x: g[0], y: g[1], z: g[2]}, simultaneous=True) - kappa) == 0

# ---- candidates
cands = {}
for e1 in (1, -1):
    for e2 in (1, -1):
        e3 = e1*e2                      # the kappa-preserving sign twists
        cands[f"sigma({e1},{e2},{e3})"] = (e1*x, e2*y, e3*z)
cands["s (a<->b swap)"] = (y, x, z)
cands["e' (z -> xy-z)"] = (x, y, x*y - z)
cands["s o e'"] = compose((y, x, z), (x, y, x*y - z))

P0 = {x: 2, y: 2, z: 2}
vu = sp.Matrix([sp.Rational(3, 2) - sp.sqrt(5)/2, sp.Rational(7, 2) - 3*sp.sqrt(5)/2, 1])
# verify vu is the phi^4 eigenvector of D(T^2) at P0 (re-pin memo 94)
J2 = sp.Matrix(T2).jacobian(sp.Matrix([x, y, z])).subs(P0)
assert sp.simplify(J2*vu - phi**4*vu) == sp.zeros(3, 1)
print("re-pinned: v_u is the exact phi^4 eigenvector of D(T^2) at (2,2,2).")

print("\ncandidate | kappa | fixes P0 | vs the flow | action on v_u")
swap_found = False
reverser_found = []
survivors = []
for name, g in sorted(cands.items()):
    if g == (x, y, z):
        continue
    pk = preserves_kappa(g)
    fixes = all(sp.simplify(c.subs(P0)) == 2 for c in g)
    # flow relation: g o T2 == T2 o g  (commuting)?  g o T2 == T2inv o g (reversing)?
    gT2 = compose(g, T2)
    comm = (tuple(sp.expand(c) for c in gT2) == tuple(sp.expand(c) for c in compose(T2, g)))
    rev = (tuple(sp.expand(c) for c in gT2) == tuple(sp.expand(c) for c in compose(T2inv, g)))
    rel = "COMMUTES" if comm else ("REVERSES" if rev else "neither")
    act = "-"
    if fixes and (comm or rev):
        Dg = sp.Matrix(g).jacobian(sp.Matrix([x, y, z])).subs(P0)
        w = Dg*vu
        if sp.simplify(w - vu) == sp.zeros(3, 1):
            act = "+v_u"
        elif sp.simplify(w + vu) == sp.zeros(3, 1):
            act = "-v_u  <-- SWAP"
        else:
            act = "off the line"
        if comm and act.startswith("-v_u"):
            swap_found = True
        if comm and act == "+v_u":
            survivors.append(name)
    if rev:
        reverser_found.append((name, fixes))
    print(f"  {name:16s} | {'ok' if pk else 'NO'} | {'yes' if fixes else 'no '} | {rel:8s} | {act}")

assert all(preserves_kappa(g) for g in cands.values())

# the reverser's exact action: it must carry the unstable line to the STABLE line
R = (y, x, y*x - z)                      # s o e'
assert compose(R, R) == (x, y, z)        # an involution
assert tuple(sp.expand(c) for c in compose(R, T2)) == tuple(sp.expand(c) for c in compose(T2inv, R))
DR = sp.Matrix(R).jacobian(sp.Matrix([x, y, z])).subs(P0)
w = DR*vu
lam_check = sp.simplify((J2*w - phi**-4*w))
assert lam_check == sp.zeros(3, 1)
print("REVERSER EXACT: R = s o e' : (x,y,z) -> (y,x,yx-z) is an involution with")
print("   R T^2 R = T^-2, R(P0) = P0, and DR carries the unstable eigenvector to")
print("   an exact phi^-4 (STABLE) eigenvector — time reversal on the nose.")

print()
if swap_found:
    print("""OUTCOME: SWAP FOUND — an object symmetry commutes with the flow, fixes
the trivial rep, and reverses the unstable direction: the branch bit is
OBJECT-BROKEN (gauge).  Census candidate 8 leaves the blocker list as
NOT-A-BIT; the frame column simplifies.  Relay to cc.""")
else:
    print("""OUTCOME: NO SWAP — no candidate symmetry of the banked structure both
commutes with the flow, fixes the trivial rep, and reverses the
unstable direction.  THE BRANCH BIT SURVIVES the object's symmetries:
at the orbit level the branch choice is a genuine EXTERNAL residue —
the census's candidate-8 blocker types toward the FRAME column, and
the weld instrument (i)'s blocked identification is ANSWERED IN-LANE:
the arrow's Z/2 is the BRANCH Z/2 (v_u -> -v_u), which is NOT c (c
acts trivially on this real slice — consistent with memo 94's
mirror-even drift and AR6's SPLIT).""")
if reverser_found:
    print(f"""RECORDED: time-reversing symmetries found {reverser_found} — the
record's own symmetry group realizes orbit-level TIME REVERSAL
(g T^2 g^-1 = T^-2): the dynamical face of B124's two-headed time,
now exhibited as an explicit polynomial symmetry.  Note the reverser's
existence is exactly why the arrow needs a bit at all: forward and
backward dynamics are symmetry-equivalent; the branch/direction choice
breaks what the object keeps whole.""")
print("""Fences: the candidate list is the natural finite symmetry set of the
banked Fricke structure (sign twists + the isometry swap + the fourth-
trace flip); a symmetry OUTSIDE this list is not excluded by this cell
— completeness of the stabilizer is not claimed, only the tested set.
The sign twists move P0 (they permute the central characters — B782's
torsor face) and so cannot swap branches AT P0 by construction; they
are tested and recorded for exactness.  Gate 5 untouched.""")
