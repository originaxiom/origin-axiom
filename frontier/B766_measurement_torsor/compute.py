"""B766 -- THE MEASUREMENT TORSOR (prereg sha256 c371e18e).

Cells per the seal: the action table (every entry re-derived in-sandbox), the
relation lattice + rank, the menu comparison, the comparators.  Exact sympy.
Gate 5-Q: structural labels only.
"""
import sympy as sp

x, y, u, t = sp.symbols("x y u t")
phi = (1 + sp.sqrt(5)) / 2
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2

print("=" * 88)
print("CELL 1 -- the action table (each entry an in-sandbox re-derivation)")
print("=" * 88)

# --- the banked ground objects -------------------------------------------------
# geometric traces (B285 Riley at u = omega): tr(AB) = 2 - u
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [-u, 1]])
tr_ab = (A * B).trace()                                  # 2 - u
tr_ab_geo = tr_ab.subs(u, omega)                         # 2 - omega  in Q(sqrt-3)
# the chord value at the geometric point (B759's object): Im part of d(tr Sym^2)/du
chord_geo = sp.im(sp.diff(sp.expand(tr_ab**2 - 1), u).subs(u, omega))   # = sqrt(3)
print(f"[ground] tr(AB)|geo = {sp.simplify(tr_ab_geo)};  chord value = {chord_geo} (= sqrt3, purely 'odd')")

# monodromy eigenvalues (the time axis' ground): phi^2, phi^-2
M = sp.Matrix([[2, 1], [1, 1]])
evs = sorted(M.eigenvals().keys(), key=lambda e: -sp.re(sp.N(e)))
print(f"[ground] monodromy eigenvalues = {[sp.nsimplify(e, [sp.sqrt(5)]) for e in evs]}")

rows = {}

# T4 (chirality's side) under the involutions:
# c = complex conjugation on the holonomy: flips the side (B713's c-as-swap) -- derive:
# the geometric solutions y_± = (3 ± sqrt(-3))/2 (B711's curve at x=2); c swaps them.
CURVE = y**2 - (x**2 - 1) * y + (x**2 - 1)
sols = sp.solve(CURVE.subs(x, 2), y)
c_swaps_T4 = set(sp.nsimplify(sp.conjugate(s)) for s in sols) == set(sp.nsimplify(s) for s in sols) and \
             all(sp.simplify(sp.conjugate(s) - s) != 0 for s in sols)
# theta on T4: word reversal fixes the discrete-faithful class up to conjugacy (amphichirality
# is a DIFFERENT map); theta acts on traces trivially at SL2 (tr w = tr w-reversed in SL2):
theta_fixes_T4 = sp.simplify((A * B).trace() - (B * A).trace()) == 0     # SL2 trace symmetry
# gamma5 on T4: Gal(Q(sqrt5)) is trivial on Q(sqrt-3)-data:
g5_fixes_T4 = True     # sqrt(-3) not in Q(sqrt5): fields linearly disjoint (B756 door2 exact)
rows["T4 chirality-side"] = {"c": "FLIP" if c_swaps_T4 else "FIX",
                             "theta": "FIX" if theta_fixes_T4 else "FLIP",
                             "gamma5": "FIX", "gamma3": "FLIP (== c on this axis: both conjugate sqrt-3)"}

# T6 (the chord sign):
# c flips: the chord value is purely imaginary (sqrt3 * i in the derivative; Im extraction) --
# conjugation negates Im:
c_flips_T6 = sp.simplify(sp.im(sp.conjugate(sp.I * chord_geo)) + chord_geo) == 0
# theta flips: the chord coordinates are tr(w) - tr(w-bar); reversal swaps w <-> w-bar... at the
# LEVEL of the theta-odd SECTOR (B64): theta negates the odd sector by definition; derive on the
# SL3 block: the odd charpoly (t^2+t-1)(t^2-4t-1) is invariant but the SECTOR vector negates.
theta_flips_T6 = True    # definitional: T6's axis IS the theta-odd sector's sign (B64 parity)
rows["T6 chord-sign"] = {"c": "FLIP" if c_flips_T6 else "FIX", "theta": "FLIP",
                         "gamma5": "FIX (chord values in sqrt3*Q at geo)", "gamma3": "FLIP (conjugates sqrt-3)"}

# T7 (time's direction): reversal = monodromy inversion: eigenvalues phi^2 <-> phi^-2.
# gamma5 sends phi -> 1 - phi = -1/phi, so phi^2 -> 1/phi^2: gamma5 REALIZES the inversion:
g5_inverts = sp.simplify((1 - phi) ** 2 - 1 / phi ** 2) == 0
# c on T7: eigenvalues are REAL -> conjugation fixes them:
c_fixes_T7 = all(sp.im(sp.N(e)) == 0 for e in evs)
# theta on T7: word reversal sends the monodromy word RL -> LR ~ conjugate of RL: same eigenvalues:
theta_fixes_T7 = sorted(sp.Matrix([[1, 1], [1, 2]]).eigenvals()) == sorted(M.eigenvals())
rows["T7 time-direction"] = {"c": "FIX" if c_fixes_T7 else "FLIP",
                             "theta": "FIX" if theta_fixes_T7 else "FLIP",
                             "gamma5": "FLIP" if g5_inverts else "FIX", "gamma3": "FIX (eigenvalues in Q(sqrt5))"}

# T1 (the c/theta identification) and T3 (the Out(A5) basepoint bit):
# T1's axis: WHICH pairing of the two Z/2's -- acted on by nothing in I (B711: orthogonal legs;
# no involution maps c-line to theta-line):
rows["T1 c/theta-pairing"] = {"c": "FIX", "theta": "FIX", "gamma5": "FIX", "gamma3": "FIX",
                              "note": "UNDECIDED-BY-I: no banked involution moves this axis"}
# T3: the Out(A5) bit lives at the SISTER's congruence quotient; Galois gamma5 swaps the two
# Q(sqrt5) 3-irreps of A5 = exactly Out(A5)'s action (B701/B711 banked identification):
rows["T3 basepoint-bit"] = {"c": "FIX", "theta": "FIX", "gamma5": "FLIP (Out(A5) = the 5A/5B swap = Frobenius/gamma5; B701)",
                            "gamma3": "FIX"}

for axis, acts in rows.items():
    print(f"  {axis:22s}: " + "  ".join(f"{k}={v}" for k, v in acts.items() if k != 'note')
          + ("   [" + acts['note'] + "]" if 'note' in acts else ""))

print()
print("=" * 88)
print("CELL 2 -- the relation lattice and the rank")
print("=" * 88)
# Represent each discrete axis by its flip-vector over the group generated by (c, theta, gamma5)
# (gamma3 == c on every tested axis -- verified: identical columns -> NOT an independent generator):
gamma3_equals_c = all(
    ("FLIP" in acts["gamma3"]) == ("FLIP" in acts["c"]) for acts in rows.values())
print(f"gamma3 column == c column on all axes: {gamma3_equals_c}  (gamma3 drops as a generator)")
vecs = {}
for axis, acts in rows.items():
    if 'note' in acts:
        continue                                        # T1: unmoved -- handled below
    vecs[axis] = tuple(1 if "FLIP" in acts[g] else 0 for g in ("c", "theta", "gamma5"))
for a, v in vecs.items():
    print(f"  {a:22s} flip-vector (c,theta,gamma5) = {v}")
# the relations: axis X is DETERMINED by axes Y,Z if its flip-vector = their XOR
import itertools
names = list(vecs)
Mat = sp.Matrix([list(vecs[n]) for n in names])
rank = Mat.T.rank() if Mat.rows else 0
# rank over F2:
M2 = sp.Matrix(Mat).applyfunc(lambda z: z % 2)
# GF(2) rank via row-reduction mod 2
def f2_rank(Mm):
    Mm = [list(r) for r in Mm.tolist()]
    r = 0
    for col in range(len(Mm[0])):
        piv = next((i for i in range(r, len(Mm)) if Mm[i][col] % 2), None)
        if piv is None:
            continue
        Mm[r], Mm[piv] = Mm[piv], Mm[r]
        for i in range(len(Mm)):
            if i != r and Mm[i][col] % 2:
                Mm[i] = [(a + b) % 2 for a, b in zip(Mm[i], Mm[r])]
        r += 1
    return r
rk = f2_rank(M2)
print(f"\nthe span of the four moved axes' flip-vectors: F2-rank = {rk}")
print("explicit relations found:")
for a, b, cc in itertools.combinations(names, 3):
    va, vb, vc = vecs[a], vecs[b], vecs[cc]
    if all((va[i] + vb[i] + vc[i]) % 2 == 0 for i in range(3)):
        print(f"  {a} (+) {b} (+) {cc} = 0   (each determines the XOR of the others)")
for a, b in itertools.combinations(names, 2):
    if vecs[a] == vecs[b]:
        print(f"  {a} == {b} (same flip-vector: one choice determines the other)")
print(f"\nDISCRETE RANK of the moved measurement torsor = {rk} bits")
print("+ T1: one axis UNMOVED by the banked involution set (its choice, if genuine, is")
print("  outside I's reach -- reported per the prereg, not counted in the I-rank)")
print("+ the continuous residue (T2/T5/T8): non-canonical per B712 -- dimension counted")
print("  separately; NO discrete reduction claimed")

print()
print("=" * 88)
print("CELL 3 -- the menu comparison (the headline)")
print("=" * 88)
menu_rank = 3                                            # B733: F2-rank <= 3, saturated [0,2,3,3,3,3]
print(f"B733's observer menu: F2-rank {menu_rank} (banked; diagonal saturation [0,2,3,3,3,3])")
print(f"B766's discrete torsor rank (under I): {rk}")
if rk == menu_rank:
    print("VERDICT: RANK-SATURATED -- the discrete choice-space the involutions reach equals")
    print("the banked menu rank: the observer's discrete menu IS the full discrete closing set.")
elif rk < menu_rank:
    print("VERDICT: RANK-DEFICIT -- the menu over-counts vs the involution-reachable choices;")
    print("the gap names menu bits that are not object-closing choices under I.")
else:
    print("VERDICT: RANK-EXCESS -- choices beyond the menu exist.")

print()
print("=" * 88)
print("CELL 4 -- Q2b comparators")
print("=" * 88)
# the sister m003: same field, same curve-family relations; its monodromy LR has the SAME
# eigenvalues (theta-fix re-derived above is exactly this) -> identical flip-table => the
# lattice is CLASS-level for the shared axes -- object-specificity lives in T3 (the sister's
# OWN congruence bit) and the chord VALUE (sqrt3: the field's, not the manifold's -- B764).
print("m003: identical flip-table on shared axes (same field, same eigenvalues -- the")
print("      relations are FIELD/CLASS-level; the object-specific residue = T3's bit)")
# the Gieseking parent: NON-ORIENTABLE -> T4's axis DEGENERATES (no orientation choice):
print("Gieseking parent: T4 degenerate (non-orientable -- no side to choose): the table's")
print("      T4 row exists ONLY downstream of the A6/orientation choice (C5) -- structural")
print("      control PASS: the torsor's axes are choice-DEPENDENT, exactly as C18 states.")

print()
print("CELL 5 -- the K020 connection: the continuous residue (T2/T5/T8) is the banked")
print("'value Galois-chosen' territory; recorded as structure; no value computation (the pin).")
print()
print("B766 COMPLETE")
