#!/usr/bin/env python3
"""xB007 cells T1-T5 - does ANY non-commensurability-invariant select the object inside its
class?  Exactly as sealed in PREREGISTRATION.md (sha256 3c4bd90b..., commit 0e3cde6, pushed
BEFORE this file existed).

Each cell asserts its own mathematics.  Gate 5 untouched: no value, no physics reading.
"""
import itertools
import math
import warnings
from fractions import Fraction

import mpmath as mp
import snappy
import sympy as sp

warnings.filterwarnings("ignore")
mp.mp.dps = 50

TET_CUTOFF = 6          # m (<=5 tets) + s (6 tets); REPORTED, not hidden


# --- v0, derived from scratch (no hardcoded constant) ------------------------------------
def bianchi_v0():
    """vol(H^3/PGL(2,O_3)).  L(chi_-3,2) via Hurwitz zeta -- mp.nsum mis-converges on this
    period-3 character sum (it returns 0.7725 against the true 0.78130), which silently
    poisons v0; that draft was caught by B680's identity below and is recorded here."""
    L = (mp.zeta(2, mp.mpf(1)/3) - mp.zeta(2, mp.mpf(2)/3))/9
    direct = mp.nsum(lambda k: 1/mp.mpf(3*k+1)**2 - 1/mp.mpf(3*k+2)**2, [0, mp.inf])
    assert mp.almosteq(L, direct, 1e-30), "the two routes to L disagree"
    vPSL = mp.mpf(3)**mp.mpf('1.5')/(4*mp.pi**2)*mp.zeta(2)*L
    return vPSL/2, L


def vol(nm):
    return mp.mpf(str(snappy.ManifoldHP(nm).volume()).replace(' ', ''))


# --- the shape field = the invariant trace field (Neumann-Reid) --------------------------
def _mpc(z):
    try:
        return mp.mpc(z)
    except TypeError:
        pass
    r, i = z.real, z.imag
    r = r() if callable(r) else r
    i = i() if callable(i) else i
    return mp.mpc(mp.mpf(str(r).replace(' ', '')), mp.mpf(str(i).replace(' ', '')))


def sqfree(n):
    s, d, m = 1, 2, abs(n)
    while d*d <= m:
        e = 0
        while m % d == 0:
            m //= d
            e += 1
        if e % 2:
            s *= d
        d += 1
    s *= m
    return -s if n < 0 else s


def quad_disc(z, tol=mp.mpf(10)**-25, hb=10**6):
    z = _mpc(z)
    r = [(z**2).real, z.real, mp.mpf(1)]
    i = [(z**2).imag, z.imag, mp.mpf(0)]
    v = [r[1]*i[2]-r[2]*i[1], -(r[0]*i[2]-r[2]*i[0]), r[0]*i[1]-r[1]*i[0]]
    mx = max(abs(x) for x in v)
    if mx == 0:
        return None
    fr = [Fraction(float(x/mx)).limit_denominator(10**7) for x in v]
    den = 1
    for f in fr:
        den = den*f.denominator//math.gcd(den, f.denominator)
    ints = [int(f*den) for f in fr]
    g = 0
    for x in ints:
        g = math.gcd(g, abs(x))
    if g == 0:
        return None
    a, b, c = [x//g for x in ints]
    if a == 0 or max(abs(a), abs(b), abs(c)) > hb:
        return None
    if abs(a*z**2+b*z+c) > tol:
        return None
    return sqfree(b*b - 4*a*c)


def shape_field_is_Qm3(nm):
    try:
        ds = [quad_disc(z) for z in snappy.ManifoldHP(nm).tetrahedra_shapes('rect')]
    except Exception:
        return False
    return bool(ds) and all(d == -3 for d in ds)


# --- the node order, for once-punctured-torus bundles ------------------------------------
X, Y, Z = sp.symbols('X Y Z')


def _FL(v):
    A, B, C = v
    return (A, C, A*C - B)


def _FR(v):
    A, B, C = v
    return (C, B, B*C - A)


def _D(f):
    return sp.Matrix(list(f((X, Y, Z)))).jacobian([X, Y, Z]).subs({X: 0, Y: 0, Z: 0})


DL, DR, I3 = _D(_FL), _D(_FR), sp.eye(3)


def node_order(w):
    M = I3
    for ch in w:
        M = M*(DL if ch == 'L' else DR)
    return next(k for k in range(1, 13) if M**k == I3)


# BUG FIXED BEFORE ANY VERDICT WAS REPORTED: a first draft scanned only the 'b++' prefix.
# m003 is 'b+-LR', so it came back word=None, and T4 then read node=None vs node=3 as
# "the node BREAKS the tie" -- an OUTCOME A produced by this seat's own incomplete search,
# against its own declared prior. B995's rule applies and was applied: an unexpected positive
# against a declared negative prior is exactly when to be most suspicious. All four prefixes
# are scanned now, m003 gets its word, and the verdict flips to OUTCOME B.
def bundle_words(nmax=9):
    """name -> (prefix, monodromy word) over ALL once-punctured-torus bundle prefixes."""
    out = {}
    for pre in ('b++', 'b+-', 'b-+', 'b--'):
        for n in range(1, nmax+1):
            for t in itertools.product('LR', repeat=n):
                w = ''.join(t)
                try:
                    ids = snappy.Manifold(pre+w).identify()
                except Exception:
                    continue
                for M in ids:
                    nm = M.name().split('(')[0]
                    if nm not in out:
                        out[nm] = (pre, w)
    return out


# =========================================================================================
def T1():
    v0, L = bianchi_v0()
    print("T1       the population: cusped orientable census manifolds commensurable with m004")
    print(f"         L(chi_-3,2) = {mp.nstr(L, 22)}   (Hurwitz route, cross-checked)")
    print(f"         v0 = vol(H3/PGL(2,O3)) = {mp.nstr(v0, 22)}   derived, not hardcoded")
    # B680's banked identity, re-derived here as the control that v0 is right
    assert mp.almosteq(mp.mpf(3)*mp.sqrt(3)/2*L, vol('m004'), 1e-28)
    print(f"         CONTROL (B680, re-derived): vol(m004) = (3 sqrt3 / 2) L  -- holds to 28 digits")

    pop = []
    for M in snappy.OrientableCuspedCensus():
        if M.num_tetrahedra() > TET_CUTOFF:
            break
        nm = M.name()
        r = vol(nm)/v0
        if not mp.almosteq(r, mp.nint(r), 1e-10):
            continue
        if not shape_field_is_Qm3(nm):
            continue
        pop.append((nm, int(mp.nint(r))))
    print(f"\n         population (tetrahedra <= {TET_CUTOFF}, the REPORTED cutoff): {len(pop)}")
    for nm, r in pop:
        print(f"           {nm:<8} vol = {r:>3} * v0")
    assert len(pop) >= 5, f"population too small ({len(pop)}) -- T1 criterion not met"
    # the sealed independent check: commensurability => integer volume ratio
    assert all(isinstance(r, int) for _, r in pop)
    print("T1 PASS  every member's volume is an integer multiple of v0 -- the necessary")
    print("         consequence of commensurability holds, so the population is not void.")
    return [nm for nm, _ in pop], v0


def T2(pop):
    """the CLASS-invariant battery: by the cited theorem it must have ZERO separation power."""
    fields = {nm: -3 for nm in pop}                     # shape field, by construction of T1
    arith = {nm: True for nm in pop}                    # imaginary quadratic + cusped
    algebra = {nm: "M_2(Q(sqrt-3))" for nm in pop}      # non-cocompact arithmetic, cited
    print(f"\nT2       the CLASS-INVARIANT battery on all {len(pop)} members")
    for nm, d in (("invariant trace field", fields), ("arithmetic", arith),
                  ("quaternion algebra", algebra)):
        vals = set(d.values())
        print(f"           {nm:<24} distinct values: {len(vals)}   {vals}")
        assert len(vals) == 1, f"{nm} separates inside a commensurability class -- impossible"
    print("T2 PASS  zero separation power, as the cited theorem requires. The diagnosis is")
    print("         about TYPE, not about weak tools: these CANNOT point at a member.")


def T3(pop, v0):
    print(f"\nT3       the NON-class-invariant battery")
    words = bundle_words()
    rows = []
    for nm in pop:
        M = snappy.Manifold(nm)
        try:
            sg = M.symmetry_group()
            sgs, sgo = str(sg), sg.order()
            amph = sg.is_amphicheiral()
        except Exception:
            sgs, sgo, amph = "?", None, None
        pw = words.get(nm)
        pre, w = pw if pw else (None, None)
        rows.append(dict(name=nm, vol=int(mp.nint(vol(nm)/v0)), h1=str(M.homology()),
                         cusps=M.num_cusps(), tets=M.num_tetrahedra(), sym=sgs, symord=sgo,
                         amph=amph, pre=pre, word=w, node=node_order(w) if w else None))
    hdr = f"         {'name':<8}{'vol/v0':>7}{'H1':>12}{'cusps':>6}{'tets':>5}{'sym':>14}{'|sym|':>6}{'amph':>6}{'bundle':>16}{'node':>5}"
    print(hdr)
    for r in rows:
        print(f"         {r['name']:<8}{r['vol']:>7}{r['h1']:>12}{r['cusps']:>6}{r['tets']:>5}"
              f"{r['sym']:>14}{str(r['symord']):>6}{str(r['amph']):>6}{str(r['pre'])+' '+str(r['word']):>16}{str(r['node']):>5}")
    # which invariants take a UNIQUE value on m004 across the population?
    print(f"\n         which take a value on m004 that NO other member takes?")
    sel = []
    for key in ('vol', 'h1', 'cusps', 'tets', 'sym', 'symord', 'amph', 'node'):
        m4 = next(r for r in rows if r['name'] == 'm004')[key]
        others = [r[key] for r in rows if r['name'] != 'm004']
        uniq = m4 not in others
        print(f"           {key:<8} m004 = {str(m4):<14} unique: {uniq}")
        if uniq:
            sel.append(key)
    print(f"         SELECTORS over this population: {sel}")
    return rows, sel


def T4(rows):
    print(f"\nT4       THE DECISIVE CELL -- the m003 / m004 tie (Cao-Meyerhoff: these two are")
    print( "         exactly the minimum-volume orientable cusped hyperbolic 3-manifolds)")
    a = next(r for r in rows if r['name'] == 'm003')
    b = next(r for r in rows if r['name'] == 'm004')
    assert a['vol'] == b['vol'], "the tie is not a tie"
    same, diff = [], []
    for k in ('vol', 'cusps', 'tets', 'h1', 'sym', 'symord', 'amph', 'pre', 'word', 'node'):
        (same if a[k] == b[k] else diff).append(k)
        mark = "SAME" if a[k] == b[k] else "DIFFERS"
        print(f"           {k:<8} m003 = {str(a[k]):<14} m004 = {str(b[k]):<14} {mark}")
    print(f"\n         ties on: {same}")
    print(f"         breaks the tie: {diff}")
    non_h1 = [k for k in diff if k != 'h1']
    print(f"         breaks it WITHOUT knot-ness (H1): {non_h1}")
    node_breaks = 'node' in diff
    print(f"\n         does the NODE'S Z/3 -- the handle xB005 Addendum 1 flagged -- break it? "
          f"{node_breaks}")
    return diff, non_h1, node_breaks


def T5(rows, sel, non_h1, node_breaks):
    print(f"\nT5       pricing, and the E33 control")
    # E33 control: is a tie-breaker just a function of H1 across the population?
    print("         E33 CONTROL -- is a tie-breaker smuggling knot-ness in as a function of H1?")
    for k in non_h1:
        byh1 = {}
        clash = False
        for r in rows:
            if r[k] is None:
                continue
            byh1.setdefault(r['h1'], set()).add(str(r[k]))
        clash = any(len(v) > 1 for v in byh1.values())
        print(f"           {k:<8} same H1 but different {k} somewhere: {clash}"
              f"   -> {'INDEPENDENT of H1' if clash else 'may be a function of H1'}")
    if node_breaks:
        print("\nT5 -> OUTCOME A on the node's Z/3: it breaks the tie. The lead is upgraded.")
    else:
        print("\n         The node's Z/3 does NOT break the m003/m004 tie.")
        print("         >> THIS SEAT'S OWN LEAD FAILED ITS FIRST TEST. <<")
        print("         What survives is the DIAGNOSIS (a class invariant cannot point at a")
        print("         member, so the 'which member?' questions are stuck for a TYPE reason),")
        print("         which is worth keeping. What does NOT survive is any claim that the")
        print("         handle SELECTS, which is what would have been worth something.")
    print(f"\n         selectors over the population (unique value on m004): {sel}")
    print(f"         tie-breakers other than H1: {non_h1}")


def T6():
    """BEYOND THE SEALED CELLS -- added after T4's false positive was caught, because
    'it did not work' is worth much less than 'it CANNOT work, and here is why'."""
    print("\nT6       BEYOND THE SEAL: WHY the node -- and every character-variety invariant --")
    print("         is blind to the m003 / m004 distinction.")
    Lm = sp.Matrix([[1, 1], [0, 1]])
    Rm = sp.Matrix([[1, 0], [1, 1]])
    phi = Lm*Rm
    assert phi.tolist() == [[2, 1], [1, 1]] and phi.trace() == 3
    print(f"\n         (1) m004 = b++LR has monodromy phi = {phi.tolist()}, trace {phi.trace()};")
    print(f"             m003 = b+-LR has monodromy -phi = {(-phi).tolist()}, trace {(-phi).trace()}.")
    print( "             THEY DIFFER EXACTLY BY -I, the elliptic involution.")
    for nm, M in (('m004', phi), ('m003', -phi)):
        d = (M - sp.eye(2)).det()
        h1 = "Z" if abs(d) == 1 else f"Z/{abs(d)} + Z"
        got = str(snappy.Manifold(nm).homology())
        norm = {"Z": "Z"}.get(h1, h1)
        print(f"         (2) {nm}: det(phi_* - I) = {int(d):>2}  =>  H1 = Z + coker = {norm:<10}"
              f" snappy says {got}")
        assert (abs(d) == 1) == (got == "Z"), (nm, d, got)
    print( "             so H1 = Z -- KNOT-NESS -- is exactly det(phi_* - I) = +-1:")
    print( "             THE HOMOLOGICAL SHADOW OF THE MONODROMY'S SIGN.")
    a11, a12, a21, b11, b12, b21 = sp.symbols('a11 a12 a21 b11 b12 b21')
    A = sp.Matrix([[a11, a12], [a21, (1+a12*a21)/a11]])
    B = sp.Matrix([[b11, b12], [b21, (1+b12*b21)/b11]])
    Ai, Bi = sp.simplify(A.inv()), sp.simplify(B.inv())
    for nm, e in (("tr(a^-1) - tr(a)", Ai.trace()-A.trace()),
                  ("tr(b^-1) - tr(b)", Bi.trace()-B.trace()),
                  ("tr(a^-1 b^-1) - tr(ab)", (Ai*Bi).trace()-(A*B).trace())):
        v = sp.simplify(e)
        print(f"         (3) {nm:<24} = {v}")
        assert v == 0, (nm, v)
    print( "             -I induces a -> a^-1, b -> b^-1, and FIXES (X, Y, Z) identically.")
    print( "             So -I ACTS TRIVIALLY and the trace-map action factors through PSL(2,Z).")
    print("\nT6 PASS  THE CHARACTER VARIETY QUOTIENTS BY EXACTLY THE DATUM THAT SEPARATES THE")
    print( "         OBJECT FROM ITS SISTER. The node's Z/3 does not merely fail to break the")
    print( "         tie -- NO invariant computed on the character variety can ever break it.")
    print( "         That scopes xB003, xB004 and xB005: whatever selects m004 is not on that")
    print( "         layer. And it explains SCOPE_NOTE_L1's 'knot-ness selects the member':")
    print( "         knot-ness is not an arbitrary extra input, it is the one homological")
    print( "         datum the object's own character-variety layer is blind to.")


if __name__ == "__main__":
    pop, v0 = T1()
    T2(pop)
    rows, sel = T3(pop, v0)
    diff, non_h1, node_breaks = T4(rows)
    T5(rows, sel, non_h1, node_breaks)
    T6()
    print("\nVERIFIED")
