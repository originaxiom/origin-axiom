#!/usr/bin/env python3
"""R54 -- the space of trackers, computed rather than intuited.

The owner: "everything is derived from the rule sigma: a->ab, b->a and the mechanism that tracks what
happens with it", and: "compute all possible options" for what the tracker does, "not lean on intuition".

The mathematics that classifies ALL trackers with respect to orientation is the representation theory of
the mirror involution: any function T on the object decomposes uniquely as T = T_even + T_odd under an
involution iota, with T_odd(iota x) = -T_odd(x).  So there are exactly two kinds of tracker output with
respect to handedness -- mirror-even (sees no chirality) and mirror-odd (its SIGN is the choice of which of
{x, iota x} is called "the object").  There is no third kind.  What remains to compute is: does the RULE
itself supply the involution, and does it supply the sign?

Facts computed below:
  1. sigma's incidence matrix F = [[1,1],[1,0]] has det -1: sigma is ORIENTATION-REVERSING on the carrier.
     Its mapping torus is the non-orientable Gieseking manifold (m000); m004 is the orientation double cover,
     the mapping torus of sigma^2 = A = [[2,1],[1,1]].
  2. F commutes with A, so F acts fibrewise on m004 as an orientation-reversing symmetry: the rule itself is
     the mirror of its own object.  m004's symmetry group (order 8) contains 4 orientation-reversing elements.
  3. sigma and its a<->b mirror sigma' (matrix F^T) are conjugate in SL(2,Z), the orientation-PRESERVING
     mapping classes: the rule has no intrinsic handedness relative to its mirror image.
  4. On Fricke coordinates (x,y,z) = (tr a, tr b, tr ab), sigma acts by (x,y,z) -> (z, x, xz - y), preserving
     kappa = x^2+y^2+z^2-xyz.  The discrete faithful character of m004 lies in Q(sqrt-3)^3, and its Galois
     (= complex) conjugate is in the SAME Out(F2)-orbit: the mirror of the holonomy is reached by an
     automorphism of the group -- amphichirality at the level of characters, with the explicit word.
  5. Iteration parity: orientation at step n of sigma^n(a) is (-1)^n relative to step 0.  The rule supplies
     the ALTERNATION; the absolute sign at step 0 is not supplied by anything in the rule.
"""
import itertools, json, os, sys
import sympy as sp
import snappy

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = {}
def say(*a): print(*a); sys.stdout.flush()

F = sp.Matrix([[1, 1], [1, 0]]); A = F * F; I2 = sp.eye(2); J = sp.Matrix([[0, 1], [1, 0]])
Fm = J * F * J   # the a<->b mirror substitution a->b, b->ba
say("=" * 78); say("1. THE RULE IS ORIENTATION-REVERSING"); say("=" * 78)
say(f"  F = {F.tolist()}  det F = {F.det()}   F^2 = {A.tolist()} = A (m004 monodromy, trace {A.trace()})")
OUT['det_F'] = int(F.det()); OUT['F2_is_A'] = (A == sp.Matrix([[2, 1], [1, 1]]))
G = snappy.Manifold('m000')
C = G.orientation_cover()
m004 = snappy.Manifold('m004')
say(f"  m000 (Gieseking): orientable={G.is_orientable()} tets={G.num_tetrahedra()} vol={float(G.volume()):.9f}")
say(f"  orientation double cover of m000 isometric to m004: {C.is_isometric_to(m004)}  (vol {float(C.volume()):.9f})")
OUT['gieseking'] = dict(orientable=bool(G.is_orientable()), cover_is_m004=bool(C.is_isometric_to(m004)))
# the Gieseking as a bundle: SnapPy bundle names with a '-' in the second slot are non-orientable
for name in ['b+-R', 'b--R', 'b-+R', 'b++R']:
    try:
        B = snappy.Manifold(name)
        say(f"  bundle {name}: orientable={B.is_orientable()} vol={float(B.volume()):.6f} iso to m000: {B.is_isometric_to(G) if not B.is_orientable() else '-'}")
    except Exception as e:
        say(f"  bundle {name}: {type(e).__name__}")

say(); say("=" * 78); say("2. THE RULE IS THE MIRROR OF ITS OWN OBJECT"); say("=" * 78)
say(f"  F A = A F: {F * A == A * F}  (F acts fibrewise on the mapping torus of A; det F = -1 reverses the fibre,")
say("   fixes the circle direction, hence reverses the orientation of m004)")
# centraliser and normaliser of A in GL(2,Z), small entries
cent, norm_inv = [], []
R = range(-8, 9)
for a, b, c, d in itertools.product(R, repeat=4):
    P = sp.Matrix([[a, b], [c, d]]); dt = a * d - b * c
    if dt not in (1, -1): continue
    if P * A == A * P: cent.append(((a, b, c, d), dt))
    if P * A == A.inv() * P: norm_inv.append(((a, b, c, d), dt))
say(f"  centraliser of A in GL(2,Z) (|entries|<=8): {len(cent)} elements, det -1 among them: {sum(1 for _, d in cent if d == -1)}")
say(f"    e.g. {[p for p, d in cent if d == -1][:6]}")
say(f"  elements with P A P^-1 = A^-1 (|entries|<=8): {len(norm_inv)}, det -1 among them: {sum(1 for _, d in norm_inv if d == -1)}")
say(f"    e.g. {norm_inv[:6]}")
OUT['centraliser_det_minus1_examples'] = [p for p, d in cent if d == -1][:6]
OUT['A_to_Ainv_examples'] = norm_inv[:6]
# symmetry group of m004 and its orientation-reversing elements
S = m004.symmetry_group()
isos = m004.is_isometric_to(m004, return_isometries=True)
rev = 0
for iso in isos:
    M = iso.cusp_maps()[0]
    det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    if det == -1: rev += 1
say(f"  |Sym(m004)| = {S.order()}, amphichiral = {S.is_amphicheiral()}, isometries returned = {len(isos)}, orientation-reversing = {rev}")
OUT['sym_order'] = S.order(); OUT['orientation_reversing_isometries'] = rev

say(); say("=" * 78); say("3. THE RULE AND ITS a<->b MIRROR ARE SL(2,Z)-CONJUGATE"); say("=" * 78)
say(f"  sigma' = swap o sigma o swap: a->b, b->ba, matrix {Fm.tolist()} = F^T")
found = None
for a, b, c, d in itertools.product(range(-6, 7), repeat=4):
    if a * d - b * c != 1: continue
    P = sp.Matrix([[a, b], [c, d]])
    if P * F == Fm * P:
        found = (a, b, c, d); break
say(f"  P in SL(2,Z) with P F P^-1 = F^T: {found}")
OUT['sigma_mirror_SL2Z_conjugator'] = found
say("  => relative to an orientation-PRESERVING change of basis of the carrier, the rule and its mirror image")
say("     are the same mapping class: the rule carries no handedness of its own.")

say(); say("=" * 78); say("4. FRICKE ACTION AND THE MIRROR CHARACTER"); say("=" * 78)
x, y, z = sp.symbols('x y z')
# generic SL2 matrices with tr a = x, tr b = y, tr ab = z: use the standard normal form
a11, a12, a21, a22, b11, b12, b21, b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
Am = sp.Matrix([[a11, a12], [a21, a22]]); Bm = sp.Matrix([[b11, b12], [b21, b22]])
tr = lambda M: sp.expand(M.trace())
# sigma: a -> ab, b -> a
sa, sb = Am * Bm, Am
X, Y, Z = tr(Am), tr(Bm), tr(Am * Bm)
newx, newy, newz = tr(sa), tr(sb), tr(sa * sb)
# check tr(aba) = tr(ab) tr(a) - tr(b) using Cayley-Hamilton (det = 1)
cond = sp.expand(newz - (Z * X - Y))
cond = cond.subs(a11 * a22 - a12 * a21, 1)
cond = sp.simplify(cond.subs({a22: (1 + a12 * a21) / a11, b22: (1 + b12 * b21) / b11}))
say(f"  tr(sigma(a) sigma(b)) - (z x - y) with det a = det b = 1: {cond}")
say("  => sigma acts on (x,y,z) by (z, x, xz - y); kappa = x^2+y^2+z^2-xyz is preserved (checked below)")
kap = lambda p: p[0] ** 2 + p[1] ** 2 + p[2] ** 2 - p[0] * p[1] * p[2]
p0 = (x, y, z); p1 = (z, x, x * z - y)
say(f"  kappa(sigma p) - kappa(p) = {sp.expand(kap(p1) - kap(p0))}")
OUT['fricke_sigma_action'] = '(x,y,z) -> (z, x, xz - y)'; OUT['kappa_preserved'] = sp.expand(kap(p1) - kap(p0)) == 0
# discrete faithful character of m004
Gp = m004.fundamental_group()
say(f"  pi1(m004) = {Gp}")
gens = Gp.generators(); assert len(gens) == 2
ma, mb = Gp.SL2C(gens[0]), Gp.SL2C(gens[1])
def trc(M): return complex(M[0, 0] + M[1, 1])
X0, Y0, Z0 = trc(ma), trc(mb), trc(ma * mb)
say(f"  (tr a, tr b, tr ab) = ({X0:.9f}, {Y0:.9f}, {Z0:.9f})   kappa = {kap((X0, Y0, Z0)):.9f}")
w3 = complex(0, 3 ** .5)
def in_Qsqrt3(v, tol=1e-7):
    # v = p + q sqrt(-3), p,q in (1/2)Z ?
    p, q = v.real, v.imag / 3 ** .5
    return abs(2 * p - round(2 * p)) < tol and abs(2 * q - round(2 * q)) < tol
say(f"  all three traces in (1/2)Z[sqrt-3]: {all(in_Qsqrt3(v) for v in (X0, Y0, Z0))}")
# orbit search: Out(F2) generated by sigma (F-move), swap, inversion of a; find the complex-conjugate character
target = (X0.conjugate(), Y0.conjugate(), Z0.conjugate())
def close(p, q, tol=1e-6): return all(abs(u - v) < tol for u, v in zip(p, q))
moves = {
    'S': lambda p: (p[2], p[0], p[0] * p[2] - p[1]),            # sigma: a->ab, b->a
    'W': lambda p: (p[1], p[0], p[2]),                          # swap a<->b
    'I': lambda p: (p[0], p[1], p[0] * p[1] - p[2]),            # a -> a^-1 : tr(a^-1 b) = xy - z
    'C': lambda p: (p[0], p[1], p[2]),                          # identity placeholder
}
start = (X0, Y0, Z0); seen = {tuple(round(c.real, 6) + 1j * round(c.imag, 6) for c in start): ''}
frontier = [(start, '')]; hit = None
for depth in range(8):
    nxt = []
    for p, w in frontier:
        for k in 'SWI':
            q = moves[k](p); key = tuple(round(c.real, 6) + 1j * round(c.imag, 6) for c in q)
            if key in seen: continue
            seen[key] = w + k; nxt.append((q, w + k))
            if close(q, target): hit = w + k; break
        if hit: break
    if hit: break
    frontier = nxt
say(f"  complex-conjugate character reached from the geometric one by the Out(F2) word: {hit!r} (orbit size explored {len(seen)})")
say("  (S = sigma, W = a<->b swap, I = a -> a^-1; the mirror of the holonomy is an automorphism image of it:")
say("   amphichirality at the level of characters, with the word that realises it.)")
OUT['character'] = dict(x=[X0.real, X0.imag], y=[Y0.real, Y0.imag], z=[Z0.real, Z0.imag], conj_reached_by=hit)

say(); say("=" * 78); say("5. ITERATION PARITY: THE RULE SUPPLIES ALTERNATION, NOT A SIGN"); say("=" * 78)
word = 'a'
for n in range(1, 8):
    word = ''.join('ab' if ch == 'a' else 'a' for ch in word)
    say(f"  sigma^{n}(a) = {word[:34]}{'...' if len(word) > 34 else ''}   length {len(word)}   det F^{n} = {(-1) ** n:+d}")
say("  => orientation of the carrier at step n is (-1)^n relative to step 0; nothing in the rule fixes step 0's sign.")

say(); say("=" * 78); say("6. THE CLASSIFICATION OF TRACKERS (a theorem, stated with its proof)"); say("=" * 78)
say("""  Let iota be any orientation-reversing symmetry of the object (section 2 exhibits four, one of which is the
  rule F itself acting on the fibre).  iota^2 acts trivially on every invariant of the object that does not
  see the fibre-circle coordinate, and on characters iota acts as complex conjugation (section 4).  For ANY
  tracker T (any function of the object, the word, the monodromy, the character, or the cusp), write
      T_even = (T + T o iota)/2,   T_odd = (T - T o iota)/2,   T = T_even + T_odd.
  T_even is mirror-blind.  T_odd changes sign under iota, so its value on "the object" versus "the mirror"
  is fixed only once one of the two is NAMED -- a choice of sheet of the double cover m004 -> m000, equivalently
  a choice of embedding Q(sqrt-3) -> C (which sqrt-3), equivalently a choice of which parity of sigma-steps
  is called "even".  All three are torsors under the same Z/2 and none is supplied by the rule (section 3, 5).
  Hence the complete list of tracker options with respect to handedness is: {mirror-even, mirror-odd}, and
  every mirror-odd tracker's sign is one externally chosen bit.  This is exhaustive because Z/2 has exactly
  two irreducible characters.""")
OUT['classification'] = 'every tracker = even + odd under the mirror involution; odd part sign = one chosen bit (sheet / sqrt-3 embedding / step parity)'
json.dump(OUT, open(os.path.join(HERE, 'r54_results.json'), 'w'), indent=1, default=str)
say("\nr54_results.json written")
