r"""CELL 3 — SPIN FORK (B796 Wave 1; prereg WAVE1_PREREGISTRATION.md).

The two spin structures of m004 = the two SL(2,C) lifts of the
holonomy: rho1 = (A, B) (Riley) and rho2 = (-A, -B). For each lift,
the induced spin structure on the cusp torus is read off the signs of
the lifted peripheral traces (meridian a; longitude bABaaBAb).

Convention (named): tr = -2 on a parabolic peripheral <=> spin
structure TRIVIAL (periodic) along it; LIE structure = trivial along
both; Bar: essential spectrum R iff cusp structure is Lie, else
discrete Dirac spectrum. Both orientations reported; the fork is
convention-independent if the two lifts land in different classes.

Gate 5-Q.
"""
import sympy as sp

omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-omega, 1]])

GEN = {'a': A, 'b': B, 'A': A.inv(), 'B': B.inv()}


def wmat(word, sign_a=1, sign_b=1):
    """Evaluate word with generator signs (lift choice)."""
    m = sp.eye(2)
    for ch in word:
        g = GEN[ch]
        s = sign_a if ch in 'aA' else sign_b
        m = m * (s * g)
    return sp.simplify(m)


print("=" * 72)
print("CELL 3 — SPIN FORK")
print("=" * 72)
print()

# 0. Verify both sign-assignments are genuine lifts (relator survives)
print("0. Lift verification (relator w a = b w, w = aBAb):")
for sa, sb, name in [(1, 1, 'rho1 = (A, B)'), (-1, -1, 'rho2 = (-A, -B)')]:
    W = wmat('aBAb', sa, sb)
    lhs = sp.simplify(W * (sa * A))
    rhs = sp.simplify((sb * B) * W)
    ok = sp.simplify(lhs - rhs) == sp.zeros(2, 2)
    print(f"   {name}: relator holds in SL(2,C): {ok}")
# the character: H1(m004) = Z, both a and b are meridional generators
# mapping to the generator, so the nontrivial character is a,b -> -1.
# Mixed signs (+,-)/(-,+) would need a != b in H1(Z/2) — excluded by
# H1 = Z (single generator); verify the relator anyway:
for sa, sb in [(1, -1), (-1, 1)]:
    W = wmat('aBAb', sa, sb)
    ok = sp.simplify(W * (sa * A) - (sb * B) * W) == sp.zeros(2, 2)
    print(f"   mixed signs ({sa},{sb}): relator holds: {ok} "
          f"(must be False — only 2 spin structures)")
print()

# 1. Peripheral traces for both lifts
LONG = 'bABaaBAb'
print("1. Peripheral lifted traces (exact):")
results = {}
for sa, sb, name in [(1, 1, 'rho1'), (-1, -1, 'rho2')]:
    m_tr = sp.simplify(sp.trace(sa * A))
    l_mat = wmat(LONG, sa, sb)
    l_tr = sp.simplify(sp.trace(l_mat))
    # verify longitude parabolic at infinity for this lift
    c_entry = sp.simplify(l_mat[1, 0])
    results[name] = (m_tr, l_tr)
    print(f"   {name}: tr(meridian) = {m_tr}, tr(longitude) = {l_tr} "
          f"(longitude c-entry = {c_entry})")
print()

# 2. Spin-structure classification, both conventions
print("2. Cusp spin structure per lift:")
print("   Convention C1 (named in prereg): tr = -2 <=> TRIVIAL along the")
print("   curve; LIE = trivial along both; Lie <=> essential spectrum R.")
print("   Convention C2 (opposite sign dictionary) also shown.")
print()
for name, (m_tr, l_tr) in results.items():
    for conv, trivial_tr in [('C1', -2), ('C2', 2)]:
        em = 'trivial' if m_tr == trivial_tr else 'nontrivial'
        el = 'trivial' if l_tr == trivial_tr else 'nontrivial'
        lie = (em == 'trivial' and el == 'trivial')
        print(f"   {name} under {conv}: (meridian {em}, longitude {el})"
              f" -> {'LIE: essential spectrum R' if lie else 'non-Lie: DISCRETE Dirac spectrum'}")
    print()

# 3. The fork verdict
m1, l1 = results['rho1']
m2, l2 = results['rho2']
print("=" * 72)
print("3. VERDICT (pre-registered fork)")
print("=" * 72)
pattern1 = (m1, l1)
pattern2 = (m2, l2)
print(f"   rho1 trace pattern: {pattern1};  rho2 trace pattern: {pattern2}")
if pattern1 != pattern2:
    # find which lift is Lie under each convention
    for conv, ttr in [('C1', -2), ('C2', 2)]:
        lies = [n for n, (mt, lt) in results.items()
                if mt == ttr and lt == ttr]
        print(f"   Under {conv}: Lie-type lift(s): {lies or 'NONE'}")
    print()
    print("   The two spin structures are DISTINGUISHED by the cusp data.")
else:
    print("   Both lifts induce the SAME cusp pattern.")
